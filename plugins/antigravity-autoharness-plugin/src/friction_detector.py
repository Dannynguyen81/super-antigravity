"""Friction and correction detector for Antigravity sessions.
Triggers priority reflection when the user corrects the agent or when consecutive errors occur.
"""
import re
from typing import Any

# Vietnamese & English correction cues indicating the user is teaching or correcting behavior
CORRECTION_PATTERNS = [
    # Vietnamese signals
    r"(?i)\b(sai r[oồ]i|nh[aầ]m r[oồ]i|kh[oô]ng ph[aả]i|b[oị] l[oỗ]i|sao l[aạ]i)\b",
    r"(?i)\b(đ[uừ]ng (d[uù]ng|l[aà]m|vi[eế]t|b[oỏ]|code|ch[aạ]y)|c[aấ]m)\b",
    r"(?i)\b(thay v[aà]o đ[oó]|ph[aả]i l[aà]|h[aã]y d[uù]ng|nh[oớ] l[aà]|t[uừ] gi[oờ])\b",
    r"(?i)\b(kh[oô]ng d[uù]ng|kh[oô]ng đ[uư][oợ]c|l[aầ]n sau|t[oố]t nh[aấ]t l[aà])\b",
    r"(?i)\b(nh[oớ] r[aằ]ng|quy t[aắ]c l[aà]|chu[aẩ]n l[aà]|ch[uú] [yý])\b",
    # English signals
    r"(?i)\b(that's wrong|incorrect|don't do that|never use|stop using|avoid)\b",
    r"(?i)\b(instead of|you should|must use|always prefer|remember to|rule is)\b",
    r"(?i)\b(from now on|next time|don't forget|keep in mind)\b",
]

_COMPILED_PATTERNS = [re.compile(p) for p in CORRECTION_PATTERNS]


def detect_correction_in_text(text: str) -> bool:
    """Returns True if the text matches any correction or instruction pattern."""
    if not text:
        return False
    return any(p.search(text) for p in _COMPILED_PATTERNS)


def detect_tool_error(payload: dict[str, Any]) -> bool:
    """Checks if the PostToolUse payload indicates a critical execution error."""
    error = str(payload.get("error", "")).lower()
    if not error:
        return False
    
    error_cues = ["exit status", "traceback", "exception", "failed", "error:"]
    return any(cue in error for cue in error_cues)
