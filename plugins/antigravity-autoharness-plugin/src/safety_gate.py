"""Cổng an toàn PreToolUse: chặn các lệnh phá hoại có độ tin cậy cao.

Chỉ chặn các mẫu rõ ràng (xóa gốc hệ thống, định dạng ổ đĩa, ghi đè đĩa thô).
Đây KHÔNG phải sandbox: cơ chế quyền và tin cậy không gian làm việc của
Antigravity vẫn là hàng rào chính.

Nguồn ý tưởng: Antigravity Kit (MIT, (c) 2026 VUDOVN), viết lại bằng Python.
Xem NOTICE.md ở thư mục gốc repo.

Giao thức: đọc payload JSON từ stdin; thoát với mã 1 để chặn, mã 0 để cho qua.
"""
import json
import re
import sys

MAX_PAYLOAD_BYTES = 1024 * 1024

BLOCK_RULES = (
    (
        "unix-root-delete",
        re.compile(
            r"(?:^|[;&|]\s*)(?:sudo\s+)?rm\s+"
            r"(?:-[A-Za-z]*r[A-Za-z]*f[A-Za-z]*|-[A-Za-z]*f[A-Za-z]*r[A-Za-z]*)\s+"
            r"(?:--\s+)?/(?:\*|\s|$)",
            re.IGNORECASE,
        ),
        "xóa đệ quy thư mục gốc của hệ thống tệp",
    ),
    (
        "filesystem-format",
        re.compile(r"(?:^|[;&|]\s*)(?:sudo\s+)?mkfs(?:\.[A-Za-z0-9_-]+)?\b", re.IGNORECASE),
        "lệnh định dạng hệ thống tệp",
    ),
    (
        "raw-disk-overwrite",
        re.compile(r"\bdd\b[^\n]*\bof=/dev/(?:sd|nvme|vd|xvd)[A-Za-z0-9_-]*", re.IGNORECASE),
        "ghi đè đĩa thô",
    ),
    (
        "windows-drive-format",
        re.compile(r"(?:^|[;&|]\s*)format(?:\.com)?\s+[A-Za-z]:", re.IGNORECASE),
        "định dạng ổ đĩa Windows",
    ),
    (
        "windows-root-delete",
        re.compile(
            r"remove-item\b[^\n]*-(?:recurse|r)\b[^\n]*-(?:force|fo)\b"
            r"[^\n]*(?:[A-Za-z]:\\(?:\s|$)|[A-Za-z]:\\\*)",
            re.IGNORECASE,
        ),
        "xóa đệ quy gốc ổ đĩa Windows",
    ),
)

COMMAND_KEYS = ("CommandLine", "commandLine", "command", "cmd")


def _first_string(*values):
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def extract_command(payload):
    """Lấy chuỗi lệnh từ các dạng payload mà Antigravity có thể gửi."""
    if not isinstance(payload, dict):
        return ""
    tool_call = payload.get("toolCall")
    candidates = (
        tool_call.get("args") if isinstance(tool_call, dict) else None,
        payload.get("tool_args"),
        payload.get("toolArgs"),
        payload.get("arguments"),
    )
    for args in candidates:
        if isinstance(args, dict):
            found = _first_string(*(args.get(key) for key in COMMAND_KEYS))
            if found:
                return found
    return _first_string(payload.get("command"), payload.get("cmd"))


def evaluate_command(command):
    """Trả về (allowed, rule_id, reason)."""
    for rule_id, pattern, message in BLOCK_RULES:
        if pattern.search(command):
            return False, rule_id, message
    return True, None, "không khớp mẫu lệnh phá hoại nào"


def main():
    raw = sys.stdin.read(MAX_PAYLOAD_BYTES + 1)
    if len(raw) > MAX_PAYLOAD_BYTES:
        sys.stderr.write("Cảnh báo safety_gate: payload vượt 1 MiB, cho qua.\n")
        return 0
    try:
        payload = json.loads(raw or "{}")
    except json.JSONDecodeError:
        sys.stderr.write("Cảnh báo safety_gate: JSON không hợp lệ, cho qua để tránh khóa phiên.\n")
        return 0

    command = extract_command(payload)
    if not command:
        sys.stdout.write("safety_gate: không có lệnh trong payload, cho qua.\n")
        return 0

    allowed, rule_id, reason = evaluate_command(command)
    if not allowed:
        sys.stderr.write(f"BỊ CHẶN bởi safety_gate ({rule_id}): {reason}.\n")
        return 1
    sys.stdout.write("safety_gate: lệnh qua cổng kiểm tra phá hoại.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
