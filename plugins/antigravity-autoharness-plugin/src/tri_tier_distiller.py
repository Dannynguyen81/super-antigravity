"""Tri-tier distillation router.
Directs distilled lessons into Rules, Skills, or Knowledge based on intent nature.
"""
from pathlib import Path
from typing import Any


def determine_tier(intent: dict[str, Any]) -> str:
    """Infers the appropriate tier if not explicitly specified.
    - 'rule': Concise behavioral guidelines, constraints, style mandates (<15 lines).
    - 'skill': Multi-step operational procedures, runbooks, scripts, workflows.
    - 'memory': Project-specific facts, architectural decisions, environment parameters.
    """
    if tier := intent.get("tier"):
        return tier.lower()

    content = intent.get("content", "")
    lines = [ln for ln in content.splitlines() if ln.strip()]

    # If it's very short, guideline-focused, prefer rule
    if len(lines) <= 12 and not intent.get("files"):
        return "rule"

    # Default to skill
    return "skill"


def get_target_path(tier: str, name: str, workspace_root: Path) -> Path:
    """Returns the primary target file path for the given tier and name."""
    if tier == "rule":
        return workspace_root / ".agents" / "rules" / f"{name}.md"
    elif tier == "memory":
        return workspace_root / ".agents" / "knowledge" / "decisions.md"
    else:  # skill
        return workspace_root / ".agents" / "skills" / name / "SKILL.md"
