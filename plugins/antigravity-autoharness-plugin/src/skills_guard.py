"""Dual-engine security guard for AutoHarness.
Scans proposed skill bodies, rules, and scripts against malicious patterns.
Engine 1: Regex heuristic (prompt injection, exfiltration, destructive shell).
Engine 2: Python AST analysis for helper scripts.
"""
import ast
import re

SAFETY_PATTERNS = {
    "exfiltration": [
        r"curl\s+.*\|\s*(sh|bash|powershell|cmd)",
        r"wget\s+.*\|\s*(sh|bash|powershell|cmd)",
        r"(Invoke-WebRequest|iwr|irm)\s+.*\|\s*(iex|Invoke-Expression)",
        r"(exfiltrate|leak|send|post|upload)\b.{0,30}(http|secret|token|api[_-]?key|password|credential|\benv\b)",
    ],
    "injection": [
        r"ignore\s+(all\s+|any\s+)?previous\s+instructions",
        r"disregard\s+(all\s+)?(previous|prior|above)",
        r"(override|bypass|reveal|leak)\b.{0,20}system\s+(prompt|instructions|directive)",
        r"you\s+are\s+now\s+in\s+(developer|unrestricted|god)\s+mode",
    ],
    "destructive": [
        r"\brm\s+-rf\s+(/|~|\$HOME|\*)",
        r"\bRemove-Item\s+.*-Recurse\s+.*-Force\s+([A-Za-z]:\\|~|\$env:USERPROFILE)",
        r"\b(format\s+[A-Za-z]:|mkfs\b)",
        r"\bdd\s+if=.*of=/dev/",
    ],
    "persistence": [
        r"\bcrontab\s+(-e|-r)",
        r"\b(schtasks\s+/create|New-ScheduledTask)",
        r"\b(authorized_keys|rc\.local|bashrc|profile)\b",
    ],
}

_COMPILED_SAFETY = {
    family: [re.compile(p, re.IGNORECASE) for p in patterns]
    for family, patterns in SAFETY_PATTERNS.items()
}


def scan_text(content: str) -> dict[str, list[str]]:
    """Runs Engine 1 (Regex scan) over text content.
    Returns a mapping of safety family to matched patterns. Empty means clean.
    """
    findings: dict[str, list[str]] = {}
    if not content:
        return findings

    for family, patterns in _COMPILED_SAFETY.items():
        matched = []
        for pat in patterns:
            if m := pat.search(content):
                matched.append(m.group(0))
        if matched:
            findings[family] = matched

    return findings


def scan_python_script(script_content: str) -> list[str]:
    """Runs Engine 2 (AST scan) over any accompanying Python script in skills/scripts.
    Flags dangerous dynamic execution calls.
    """
    violations = []
    try:
        tree = ast.parse(script_content)
    except SyntaxError as e:
        return [f"SyntaxError in script: {e}"]

    DANGEROUS_CALLS = {"eval", "exec", "__import__"}

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            # Check function name
            func_name = ""
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                func_name = node.func.attr

            if func_name in DANGEROUS_CALLS:
                violations.append(f"Prohibited dynamic execution call: {func_name}()")

    return violations
