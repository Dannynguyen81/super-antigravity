"""Admission promoter: the single deterministic writer and state manager for AutoHarness.
Implements in-flight validation, atomic write, sidecar stamping, and safe archiving.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from config import (
    CAPACITY_PROJECT,
    CONSOLIDATE_EVERY_N,
    INDEX_DESC_MAX_CHARS,
    MATURITY_PROJECT,
    REFLECT_EVERY_N,
    get_workspace_state_dir,
)
from src import lifecycle, platform_lock, tri_tier_distiller, validate

COUNTERS_FILE = "counters.json"
LEDGER_FILE = "ledger.jsonl"
INTENTS_FILE = "intents_queue.jsonl"


def _get_counters_path(workspace_root: Path) -> Path:
    return get_workspace_state_dir(workspace_root) / COUNTERS_FILE


def load_counters(workspace_root: Path) -> dict[str, Any]:
    path = _get_counters_path(workspace_root)
    if not path.exists():
        return {
            "tool_calls": 0,
            "requests": 0,
            "priority_flag": False,
            "skills": {},
        }
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {
            "tool_calls": 0,
            "requests": 0,
            "priority_flag": False,
            "skills": {},
        }


def save_counters(workspace_root: Path, counters: dict[str, Any]):
    path = _get_counters_path(workspace_root)
    lock_file = path.with_suffix(".lock")
    with platform_lock.file_lock(lock_file):
        tmp_fd, tmp_path = tempfile.mkstemp(dir=path.parent, prefix="cnt_")
        try:
            with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
                json.dump(counters, f, indent=2, ensure_ascii=False)
            os.replace(tmp_path, path)
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)


def increment_tool_counter(workspace_root: Path, priority: bool = False):
    """Increments tool call count and records priority friction flag."""
    counters = load_counters(workspace_root)
    counters["tool_calls"] = counters.get("tool_calls", 0) + 1
    if priority:
        counters["priority_flag"] = True
    save_counters(workspace_root, counters)


def increment_turn_counter(workspace_root: Path):
    """Increments request turn counter upon turn completion."""
    counters = load_counters(workspace_root)
    counters["requests"] = counters.get("requests", 0) + 1
    save_counters(workspace_root, counters)


def record_skill_usage(workspace_root: Path, skill_name: str):
    """Increments call count for an activated skill."""
    counters = load_counters(workspace_root)
    skills = counters.setdefault("skills", {})
    skills[skill_name] = skills.get(skill_name, 0) + 1
    save_counters(workspace_root, counters)


def should_trigger_reflection(workspace_root: Path) -> bool:
    """Evaluates whether cadence threshold or priority friction was reached."""
    counters = load_counters(workspace_root)
    tool_calls = counters.get("tool_calls", 0)
    priority = counters.get("priority_flag", False)

    if priority:
        return True
    return tool_calls >= REFLECT_EVERY_N


def reset_reflection_counters(workspace_root: Path):
    """Resets tool counter and priority flag after reflection spawns."""
    counters = load_counters(workspace_root)
    counters["tool_calls"] = 0
    counters["priority_flag"] = False
    save_counters(workspace_root, counters)


def get_skills_summary_index(workspace_root: Path) -> str:
    """Builds a condensed index of managed skills and rules for context injection."""
    lines = []

    # 1. Rules
    rules_dir = workspace_root / ".agents" / "rules"
    if rules_dir.exists():
        for f in sorted(rules_dir.glob("*.md")):
            fm, _ = validate.extract_frontmatter(f.read_text(encoding="utf-8"))
            desc = fm.get("description", f.stem)[:INDEX_DESC_MAX_CHARS]
            lines.append(f"- [rule] {f.stem}: {desc}")

    # 2. Skills
    skills_dir = workspace_root / ".agents" / "skills"
    if skills_dir.exists():
        for f in sorted(skills_dir.glob("*/SKILL.md")):
            fm, _ = validate.extract_frontmatter(f.read_text(encoding="utf-8"))
            name = fm.get("name", f.parent.name)
            desc = fm.get("description", "(no description)")[:INDEX_DESC_MAX_CHARS]
            lines.append(f"- [skill] {name}: {desc}")

    return "\n".join(lines) if lines else "(chưa có skill tự học nào)"


def land_intent(intent: dict[str, Any], workspace_root: Path) -> dict[str, Any]:
    """Admission controller: Validates and writes intent atomically.
    Returns status dict {ok: bool, message: str, findings: list}.
    """
    tier = tri_tier_distiller.determine_tier(intent)
    name = intent.get("name", "").strip().lower()
    action = intent.get("action", "create")
    content = intent.get("content", "")

    if not name:
        return {"ok": False, "message": "Intent name is required", "findings": ["Missing name"]}

    target_path = tri_tier_distiller.get_target_path(tier, name, workspace_root)
    sidecar_path = target_path.parent / ".sidecar.json"
    
    # Read existing sidecar if any
    existing_sidecar = None
    if sidecar_path.exists():
        try:
            existing_sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    # 1. In-flight validation
    findings = validate.validate_intent(intent, existing_sidecar)
    if findings:
        return {"ok": False, "message": "Validation failed", "findings": findings}

    # 2. Path Traversal & Escape Check
    try:
        resolved_target = target_path.resolve()
        resolved_root = workspace_root.resolve()
        if not resolved_target.is_relative_to(resolved_root):
            return {"ok": False, "message": "Security error: Path escape detected", "findings": ["Path traversal"]}
    except Exception as e:
        return {"ok": False, "message": f"Path error: {e}", "findings": [str(e)]}

    counters = load_counters(workspace_root)
    current_request = counters.get("requests", 0)

    # 3. Perform Action
    if action == "delete":
        if target_path.exists():
            archive_dir = get_workspace_state_dir(workspace_root) / "archive"
            archive_dir.mkdir(parents=True, exist_ok=True)
            if tier == "skill":
                shutil.move(str(target_path.parent), str(archive_dir / f"{name}_{current_request}"))
            else:
                shutil.move(str(target_path), str(archive_dir / f"{name}_{current_request}.md"))
        return {"ok": True, "message": f"Archived {name} safely", "findings": []}

    target_path.parent.mkdir(parents=True, exist_ok=True)

    # Atomic write target file
    tmp_fd, tmp_file = tempfile.mkstemp(dir=target_path.parent, prefix="land_")
    try:
        with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
            f.write(content)
        os.replace(tmp_file, target_path)
    finally:
        if os.path.exists(tmp_file):
            os.unlink(tmp_file)

    # Write subfiles if any (scripts, references)
    for rel_path, sub_content in intent.get("files", {}).items():
        sub_target = target_path.parent / rel_path
        sub_target.parent.mkdir(parents=True, exist_ok=True)
        sub_tmp_fd, sub_tmp = tempfile.mkstemp(dir=sub_target.parent, prefix="sub_")
        try:
            with os.fdopen(sub_tmp_fd, "w", encoding="utf-8") as f:
                f.write(sub_content)
            os.replace(sub_tmp, sub_target)
        finally:
            if os.path.exists(sub_tmp):
                os.unlink(sub_tmp)

    # Write Sidecar Metadata
    sidecar_data = {
        "name": name,
        "tier": tier,
        "created_by": "agent",
        "created_at_request": current_request,
        "evidence_reason": intent.get("reason", ""),
        "evidence_hash": hashlib.sha256(content.encode("utf-8")).hexdigest()[:12],
    }
    sidecar_path.write_text(json.dumps(sidecar_data, indent=2, ensure_ascii=False), encoding="utf-8")

    # Append to Ledger
    ledger_path = get_workspace_state_dir(workspace_root) / LEDGER_FILE
    with open(ledger_path, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "action": action,
            "name": name,
            "tier": tier,
            "reason": intent.get("reason", ""),
            "request_num": current_request,
        }, ensure_ascii=False) + "\n")

    return {"ok": True, "message": f"Successfully landed {name} into {tier}", "findings": []}


def perform_lifecycle_pass(workspace_root: Path):
    """Executes periodic graduation review and capacity archiving on active skills."""
    skills_dir = workspace_root / ".agents" / "skills"
    if not skills_dir.exists():
        return

    counters = load_counters(workspace_root)
    current_request = counters.get("requests", 0)
    usage_map = counters.get("skills", {})

    managed_skills = []
    for sidecar_file in skills_dir.glob("*/.sidecar.json"):
        try:
            data = json.loads(sidecar_file.read_text(encoding="utf-8"))
            if data.get("created_by") == "agent":
                name = data["name"]
                managed_skills.append({
                    "name": name,
                    "created_at_request": data.get("created_at_request", 0),
                    "call_count": usage_map.get(name, 0),
                })
        except Exception:
            continue

    to_archive = lifecycle.evaluate_lifecycle(
        managed_skills=managed_skills,
        current_request_count=current_request,
        maturity_threshold=MATURITY_PROJECT,
        capacity_limit=CAPACITY_PROJECT,
    )

    for skill_name in to_archive:
        land_intent({"action": "delete", "name": skill_name, "tier": "skill"}, workspace_root)


def spawn_background_reflector(transcript_path: str | None, workspace_root: Path):
    """Spawns non-blocking worker script in background to process transcript reflection."""
    reset_reflection_counters(workspace_root)

    script_path = Path(__file__).parent / "worker_reflect.py"
    cmd = [
        sys.executable,
        str(script_path),
        "--workspace",
        str(workspace_root),
    ]
    if transcript_path:
        cmd.extend(["--transcript", str(transcript_path)])

    # Detached background process on Windows and Unix
    kwargs: dict[str, Any] = {
        "stdin": subprocess.DEVNULL,
        "stdout": subprocess.DEVNULL,
        "stderr": subprocess.DEVNULL,
    }
    if sys.platform == "win32":
        # CREATE_NO_WINDOW | DETACHED_PROCESS
        kwargs["creationflags"] = 0x08000000 | 0x00000008
    else:
        kwargs["start_new_session"] = True

    try:
        subprocess.Popen(cmd, **kwargs)
    except Exception as e:
        # Fail-safe: A background reflection error must never break the main session
        sys.stderr.write(f"autoharness: error spawning background reflector: {e}\n")
