"""Deterministic validation classes for Antigravity AutoHarness proposals.
Validates shaped text in memory before any write occurs.
"""
import re
from typing import Any

from config import (
    INDEX_DESC_MAX_CHARS,
    RULE_BODY_MAX_LINES,
    SKILL_BODY_MAX_LINES,
    SKILL_DESC_MAX_CHARS,
)
from src import skills_guard

_FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
_PLACEHOLDER_RE = re.compile(
    r"\b(TODO|FIXME|XXX):|<(?:TODO|FIXME|XXX|TBD|PLACEHOLDER|REPLACE[_ ]?ME|INSERT[_ ]?HERE|FILL[_ ]?IN)>",
    re.IGNORECASE,
)
_TRIGGER_CUE_RE = re.compile(r"(?i)\b(when|use when|khi|dùng khi|trigger|nếu)\b|['\"`][^'\"`]+['\"`]")


def extract_frontmatter(content: str) -> tuple[dict[str, str], str]:
    """Extracts YAML frontmatter dictionary and the remaining body."""
    match = _FRONTMATTER_RE.match(content)
    if not match:
        return {}, content

    fm_raw = match.group(1)
    body = content[match.end():]
    fm_dict = {}

    for line in fm_raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, val = line.split(":", 1)
        val = val.strip().strip("'\"")
        fm_dict[key.strip()] = val

    return fm_dict, body


def validate_intent(intent: dict[str, Any], live_sidecar: dict[str, Any] | None = None) -> list[str]:
    """Validates an intent before admission. Returns a list of findings (errors).
    An empty list indicates validation pass.
    """
    findings: list[str] = []
    action = intent.get("action", "create")
    tier = intent.get("tier", "skill")
    content = intent.get("content", "")

    # 1. Action & Ownership Boundary check
    if action in ("update", "patch", "delete"):
        if live_sidecar and live_sidecar.get("created_by") != "agent":
            findings.append("Ownership violation: Cannot modify user-authored skill or rule.")

    if action == "delete":
        return findings

    if not content.strip():
        findings.append("Empty content: Body cannot be blank.")
        return findings

    # 2. Safety Scan (Regex & Injection)
    safety_hits = skills_guard.scan_text(content)
    for family, hits in safety_hits.items():
        findings.append(f"Security violation ({family}): {', '.join(hits)}")

    # 3. Structure & Frontmatter Validation
    fm, body = extract_frontmatter(content)
    if tier in ("skill", "rule"):
        if not fm.get("name"):
            findings.append("Missing frontmatter field: 'name' is required.")
        if not fm.get("description"):
            findings.append("Missing frontmatter field: 'description' is required.")
        else:
            desc = fm["description"]
            if len(desc) > SKILL_DESC_MAX_CHARS:
                findings.append(f"Description length ({len(desc)}) exceeds maximum {SKILL_DESC_MAX_CHARS}.")
            if not _TRIGGER_CUE_RE.search(desc):
                findings.append("Description lacks trigger cue: Must contain 'when'/'khi' or quoted phrase.")

    # 4. Altitude Gate (Chống transcript bloat)
    non_blank_lines = [line for line in body.splitlines() if line.strip()]
    max_lines = RULE_BODY_MAX_LINES if tier == "rule" else SKILL_BODY_MAX_LINES
    if len(non_blank_lines) > max_lines:
        findings.append(
            f"Altitude violation: Content has {len(non_blank_lines)} non-blank lines "
            f"(maximum allowed is {max_lines}). Condense to core rules and push details to references/."
        )

    # 5. Anti-Placeholder Check
    if _PLACEHOLDER_RE.search(content):
        findings.append("Placeholder violation: Found TODO, FIXME, or unfinished code markers.")

    # 6. Embedded Scripts AST Scan (if any subfiles attached)
    files = intent.get("files", {})
    for filepath, file_content in files.items():
        if filepath.endswith(".py"):
            ast_errors = skills_guard.scan_python_script(file_content)
            findings.extend(ast_errors)

    return findings
