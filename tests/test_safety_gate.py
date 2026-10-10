"""Cổng an toàn PreToolUse: chỉ dùng chuỗi lệnh giả, KHÔNG chạy lệnh thật."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins/antigravity-autoharness-plugin"
SCRIPT = PLUGIN / "src/safety_gate.py"

spec = importlib.util.spec_from_file_location("safety_gate", SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def run_gate(stdin: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-I", str(SCRIPT)], input=stdin, capture_output=True, text=True)


class EvaluateTest(unittest.TestCase):
    BLOCKED = (
        ("rm -rf /", "unix-root-delete"),
        ("rm -fr /", "unix-root-delete"),
        ("sudo rm -rf /*", "unix-root-delete"),
        ("echo ok && rm -rf / ", "unix-root-delete"),
        ("rm -rf -- /", "unix-root-delete"),
        ("mkfs.ext4 /dev/sda1", "filesystem-format"),
        ("sudo mkfs /dev/sdb", "filesystem-format"),
        ("dd if=/dev/zero of=/dev/sda bs=1M", "raw-disk-overwrite"),
        ("dd if=x of=/dev/nvme0n1", "raw-disk-overwrite"),
        ("format C:", "windows-drive-format"),
        ("FORMAT D: /q", "windows-drive-format"),
        ("Remove-Item -Recurse -Force C:\\", "windows-root-delete"),
        ("remove-item -r -fo C:\\*", "windows-root-delete"),
    )
    ALLOWED = (
        "rm -rf node_modules",
        "rm -rf ./dist",
        "rm -rf /tmp/build-cache",
        "rm -rf /home/user/project/build",
        "rm file.txt",
        "ls -la /",
        "cat /etc/hostname",
        "dd if=/dev/zero of=./test.img bs=1M count=1",
        "echo format C: is dangerous",
        "git clean -fd",
        "Remove-Item -Recurse -Force .\\dist",
        "Remove-Item -Recurse -Force C:\\Users\\me\\project\\build",
        "python -m unittest discover -s tests",
    )

    def test_blocked_commands_report_expected_rule(self) -> None:
        for command, rule in self.BLOCKED:
            allowed, rule_id, _ = gate.evaluate_command(command)
            self.assertFalse(allowed, command)
            self.assertEqual(rule_id, rule, command)

    def test_ordinary_commands_pass(self) -> None:
        for command in self.ALLOWED:
            allowed, rule_id, _ = gate.evaluate_command(command)
            self.assertTrue(allowed, f"{command!r} bị chặn nhầm bởi {rule_id}")


class ExtractCommandTest(unittest.TestCase):
    def test_supported_payload_shapes(self) -> None:
        shapes = (
            {"toolCall": {"name": "run_command", "args": {"CommandLine": "ls"}}},
            {"tool_args": {"command": "ls"}},
            {"toolArgs": {"cmd": "ls"}},
            {"arguments": {"commandLine": "ls"}},
            {"command": "ls"},
            {"cmd": "ls"},
        )
        for payload in shapes:
            self.assertEqual(gate.extract_command(payload), "ls", payload)

    def test_missing_or_malformed_payloads(self) -> None:
        for payload in ({}, [], "x", None, {"toolCall": "oops"}, {"toolCall": {"args": {"CommandLine": "  "}}}):
            self.assertEqual(gate.extract_command(payload), "", payload)


class ProcessTest(unittest.TestCase):
    def test_blocks_with_exit_code_1(self) -> None:
        out = run_gate(json.dumps({"toolCall": {"name": "run_command", "args": {"CommandLine": "rm -rf /"}}}))
        self.assertEqual(out.returncode, 1)
        self.assertIn("BỊ CHẶN", out.stderr)
        self.assertIn("unix-root-delete", out.stderr)

    def test_allows_with_exit_code_0(self) -> None:
        out = run_gate(json.dumps({"toolCall": {"name": "run_command", "args": {"CommandLine": "rm -rf node_modules"}}}))
        self.assertEqual(out.returncode, 0)

    def test_fails_open_on_bad_input(self) -> None:
        for stdin in ("", "{}", "not json", "[1,2,3]", json.dumps({"toolCall": {"args": {}}})):
            self.assertEqual(run_gate(stdin).returncode, 0, stdin)

    def test_fails_open_on_oversized_payload(self) -> None:
        big = json.dumps({"command": "x" * (1024 * 1024 + 10)})
        self.assertEqual(run_gate(big).returncode, 0)


class HooksConfigTest(unittest.TestCase):
    def test_pretooluse_registered_for_run_command(self) -> None:
        cfg = json.loads((PLUGIN / "hooks.json").read_text(encoding="utf-8"))["agy-autoharness"]
        entries = cfg["PreToolUse"]
        self.assertEqual(entries[0]["matcher"], "run_command")
        hook = entries[0]["hooks"][0]
        self.assertEqual(hook["type"], "command")
        self.assertIn("src/safety_gate.py", hook["command"])
        self.assertTrue((PLUGIN / hook["command"].split()[-1]).is_file())
        self.assertLessEqual(hook["timeout"], 300)

    def test_existing_hooks_untouched(self) -> None:
        cfg = json.loads((PLUGIN / "hooks.json").read_text(encoding="utf-8"))["agy-autoharness"]
        for event in ("PreInvocation", "PostToolUse", "Stop"):
            self.assertIn(event, cfg)


if __name__ == "__main__":
    unittest.main()
