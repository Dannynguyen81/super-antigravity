"""Central configuration for Antigravity AutoHarness Plugin.
Environment variables can override all defaults via AUTOHARNESS_*.
"""
import os
import sys
import warnings
from pathlib import Path


def _int_env(name: str, default: int) -> int:
    try:
        return int(os.environ[name])
    except KeyError:
        return default
    except ValueError:
        warnings.warn(
            f"{name}={os.environ[name]!r} is not a valid integer; using default {default}",
            stacklevel=2,
        )
        return default


def _bool_env(name: str, default: bool) -> bool:
    val = os.environ.get(name)
    if val is None:
        return default
    return val.strip().lower() in ("1", "true", "yes", "on")


# Cadence triggers
REFLECT_EVERY_N = _int_env("AUTOHARNESS_REFLECT_EVERY_N", 50)
CONSOLIDATE_EVERY_N = _int_env("AUTOHARNESS_CONSOLIDATE_EVERY_N", 250)
FRICTION_TRIGGER_ENABLED = _bool_env("AUTOHARNESS_FRICTION_TRIGGER", True)

# Altitude and content gates
SKILL_BODY_MAX_LINES = _int_env("AUTOHARNESS_SKILL_BODY_MAX_LINES", 25)
RULE_BODY_MAX_LINES = _int_env("AUTOHARNESS_RULE_BODY_MAX_LINES", 15)
SKILL_DESC_MAX_CHARS = _int_env("AUTOHARNESS_SKILL_DESC_MAX_CHARS", 1024)
INDEX_DESC_MAX_CHARS = _int_env("AUTOHARNESS_INDEX_DESC_MAX_CHARS", 80)
INDEX_SUSPENDED = _bool_env("AUTOHARNESS_INDEX_SUSPENDED", False)

# Window & payload caps
CAPTURE_MAX_RECORD_BYTES = 4_000
CAPTURE_MAX_WINDOW_BYTES = 200_000
DIGEST_EXCHANGES = _int_env("AUTOHARNESS_DIGEST_EXCHANGES", 20)

# Lifecycle gates
MATURITY_PROJECT = _int_env("AUTOHARNESS_MATURITY_PROJECT", 100)
MATURITY_GLOBAL = _int_env("AUTOHARNESS_MATURITY_GLOBAL", 300)
CAPACITY_PROJECT = _int_env("AUTOHARNESS_CAPACITY_PROJECT", 50)
CAPACITY_GLOBAL = _int_env("AUTOHARNESS_CAPACITY_GLOBAL", 20)


def get_global_state_dir() -> Path:
    """Return user-level global state directory."""
    user_home = Path.home()
    state_dir = user_home / ".gemini" / "antigravity" / "autoharness"
    state_dir.mkdir(parents=True, exist_ok=True)
    return state_dir


def get_workspace_state_dir(workspace_root: str | Path | None = None) -> Path:
    """Return workspace-level state directory."""
    if workspace_root:
        root = Path(workspace_root)
    else:
        root = Path.cwd()
    state_dir = root / ".agents" / "autoharness"
    state_dir.mkdir(parents=True, exist_ok=True)
    return state_dir
