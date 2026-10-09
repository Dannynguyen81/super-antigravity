"""Data sanitization and sensitive credential redaction.
Redacts API keys, tokens, passwords, and private user paths before reflection.
"""
import re

PATTERNS = [
    # API keys and bearer tokens
    (re.compile(r"(?i)\b(api[_-]?key|secret|token|password|auth|bearer)\s*[:=]\s*['\"]?([A-Za-z0-9_\-\.]{8,})['\"]?"), r"\1: [REDACTED]"),
    (re.compile(r"\b(AIza[0-9A-Za-z-_]{35})\b"), "[REDACTED_GEMINI_KEY]"),
    (re.compile(r"\b(sk-[A-Za-z0-9]{20,})\b"), "[REDACTED_API_KEY]"),
    (re.compile(r"\b(ghp_[A-Za-z0-9]{36})\b"), "[REDACTED_GITHUB_TOKEN]"),
    # Windows and Unix user home paths
    (re.compile(r"([A-Za-z]:\\[Uu]sers\\[^\\]+)"), "[USER_HOME]"),
    (re.compile(r"(/home/[^/\s]+|/Users/[^/\s]+)"), "[USER_HOME]"),
]


def redact_text(text: str) -> str:
    """Sanitizes text by replacing sensitive substrings with redaction placeholders."""
    if not text:
        return ""
    result = text
    for pattern, replacement in PATTERNS:
        result = pattern.sub(replacement, result)
    return result
