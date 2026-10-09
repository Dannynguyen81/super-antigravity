"""Main entry point for all Antigravity hook events.
Parses camelCase payload from stdin, routes to appropriate handlers, and responds via stdout.
"""
import argparse
import json
import os
import sys
from pathlib import Path

# Add plugin root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import INDEX_SUSPENDED
from src import admission_promoter, friction_detector


def get_workspace_root(payload: dict) -> Path:
    """Extracts workspace root from payload or falls back to current working directory."""
    paths = payload.get("workspacePaths") or []
    if paths and isinstance(paths, list):
        return Path(paths[0])
    return Path.cwd()


def handle_pre_invocation(payload: dict):
    """Injects index of learned skills and rules into the turn context."""
    if INDEX_SUSPENDED:
        sys.stdout.write(json.dumps({}))
        return

    workspace_root = get_workspace_root(payload)
    index_text = admission_promoter.get_skills_summary_index(workspace_root)

    # If there are active learned skills, inject as an ephemeral notification
    if index_text and index_text != "(chưa có skill tự học nào)":
        output = {
            "injectSteps": [
                {
                    "ephemeralMessage": f"[AutoHarness] Tủ kỹ năng tự học khả dụng:\n{index_text}"
                }
            ]
        }
    else:
        output = {}

    sys.stdout.write(json.dumps(output))


def handle_post_tool_use(payload: dict):
    """Tracks tool calls and registers friction errors."""
    workspace_root = get_workspace_root(payload)
    has_err = friction_detector.detect_tool_error(payload)

    # Check if a specific skill was read/used
    tool_call = payload.get("toolCall") or {}
    tool_name = tool_call.get("name", "")
    args = tool_call.get("args") or {}

    if tool_name == "view_file":
        abs_path = args.get("AbsolutePath", "")
        if ".agents/skills/" in abs_path or "skills/" in abs_path:
            parts = Path(abs_path).parts
            if "skills" in parts:
                idx = parts.index("skills")
                if idx + 1 < len(parts):
                    skill_name = parts[idx + 1]
                    admission_promoter.record_skill_usage(workspace_root, skill_name)

    admission_promoter.increment_tool_counter(workspace_root, priority=has_err)
    sys.stdout.write(json.dumps({}))


def handle_stop(payload: dict):
    """Called when an agent execution turn terminates. Evaluates whether to reflect."""
    workspace_root = get_workspace_root(payload)
    admission_promoter.increment_turn_counter(workspace_root)

    if admission_promoter.should_trigger_reflection(workspace_root):
        transcript_path = payload.get("transcriptPath")
        admission_promoter.spawn_background_reflector(transcript_path, workspace_root)

    sys.stdout.write(json.dumps({}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", required=True, choices=["PreInvocation", "PostToolUse", "Stop"])
    args = parser.parse_args()

    try:
        raw_input = sys.stdin.read()
        payload = json.loads(raw_input) if raw_input.strip() else {}
    except Exception:
        payload = {}

    if args.event == "PreInvocation":
        handle_pre_invocation(payload)
    elif args.event == "PostToolUse":
        handle_post_tool_use(payload)
    elif args.event == "Stop":
        handle_stop(payload)
    else:
        sys.stdout.write(json.dumps({}))


if __name__ == "__main__":
    main()
