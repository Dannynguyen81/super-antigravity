"""Số liệu và liên kết trong tài liệu phải khớp với nội dung thật của repo."""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ("README.md", "README.en.md", "AGENTS.md", "AGENTS.en.md", "CONTRIBUTING.md",
        "CONTRIBUTING.en.md", "SOUL.md", "SOUL.en.md")


def plugin_count() -> int:
    return sum(1 for d in (ROOT / "plugins").iterdir() if d.is_dir())


class CountsTest(unittest.TestCase):
    def test_plugin_count_in_readmes(self) -> None:
        n = plugin_count()
        for name in ("README.md", "README.en.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            numbers = {int(x) for x in re.findall(r"\b(\d+)\s+(?:plugins?|Gói|standard|gói)", text, re.IGNORECASE)}
            self.assertEqual(numbers, {n}, f"{name}: số plugin nêu {numbers}, thực tế {n}")

    def test_plugin_count_on_site(self) -> None:
        n = plugin_count()
        for name in ("index.html", "i18n.js"):
            text = (ROOT / "site" / name).read_text(encoding="utf-8")
            numbers = {int(x) for x in re.findall(r"\b(\d+)\s+plugins?", text)}
            self.assertEqual(numbers, {n}, f"site/{name}: nêu {numbers}, thực tế {n}")

    def test_every_plugin_is_listed_in_readme(self) -> None:
        for name in ("README.md", "README.en.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            for d in (ROOT / "plugins").iterdir():
                if d.is_dir():
                    short = d.name.removesuffix("-plugin")
                    self.assertIn(short, text, f"{name}: thiếu plugin '{d.name}'")

    def test_standalone_skills_count(self) -> None:
        n = sum(1 for d in (ROOT / "skills").iterdir() if (d / "SKILL.md").is_file())
        for name in ("README.md", "README.en.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn(f"{n} ", text, name)


class LinksTest(unittest.TestCase):
    def test_relative_markdown_links_resolve(self) -> None:
        for name in DOCS:
            text = (ROOT / name).read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)#\s]+)\)", text):
                if re.match(r"^[a-z]+:", target):
                    continue
                self.assertTrue((ROOT / target).exists(), f"{name}: link '{target}' không tồn tại")

    def test_html_hrefs_resolve(self) -> None:
        for name in ("README.md", "README.en.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            for target in re.findall(r'href="([^"#?]+)', text):
                if re.match(r"^[a-z]+:", target):
                    continue
                self.assertTrue((ROOT / target).exists(), f"{name}: href '{target}' không tồn tại")

    def test_clone_url_has_no_placeholder(self) -> None:
        for name in ("README.md", "README.en.md", "site/index.html"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertNotIn("<your-username>", text, name)
            self.assertIn("github.com/Dannynguyen81/super-antigravity", text, name)


class SkillFilesTest(unittest.TestCase):
    def test_every_skill_has_frontmatter_name_and_description(self) -> None:
        dirs = list((ROOT / "skills").iterdir()) + list((ROOT / "plugins").glob("*/skills/*"))
        for d in dirs:
            f = d / "SKILL.md"
            if not f.is_file():
                continue
            head = f.read_text(encoding="utf-8").split("---")
            self.assertGreaterEqual(len(head), 3, f"{f.relative_to(ROOT)}: thiếu frontmatter")
            self.assertRegex(head[1], r"(?m)^name:\s*\S+", f"{f.relative_to(ROOT)}: thiếu name")
            self.assertRegex(head[1], r"(?m)^description:", f"{f.relative_to(ROOT)}: thiếu description")

    def test_every_plugin_has_manifest(self) -> None:
        for d in (ROOT / "plugins").iterdir():
            if d.is_dir():
                self.assertTrue((d / "plugin.json").is_file(), f"{d.name}: thiếu plugin.json")


class LanguageHygieneTest(unittest.TestCase):
    def test_vietnamese_docs_have_no_english_parenthetical_headings(self) -> None:
        for name in ("README.md", "AGENTS.md", "CONTRIBUTING.md", "SOUL.md"):
            for line in (ROOT / name).read_text(encoding="utf-8").splitlines():
                if line.startswith("#"):
                    self.assertNotRegex(line, r"\([A-Z][A-Za-z &-]{5,}\)", f"{name}: '{line}'")


if __name__ == "__main__":
    unittest.main()


class PlanApprovalRuleTest(unittest.TestCase):
    def test_rule_present_in_both_languages(self) -> None:
        for name, needles in (
            ("AGENTS.md", ("Kế hoạch triển khai", "phê duyệt")),
            ("AGENTS.en.md", ("Implementation Plan", "approval")),
            (".agents/rules/quality-gate-workflows.md", ("Implementation Plan", "phê duyệt")),
        ):
            text = (ROOT / name).read_text(encoding="utf-8")
            for needle in needles:
                self.assertIn(needle, text, f"{name}: thiếu quy tắc phê duyệt kế hoạch ('{needle}')")


class ContextBudgetRuleTest(unittest.TestCase):
    def test_rule_file_and_references(self) -> None:
        rule = (ROOT / ".agents/rules/context-budget.md").read_text(encoding="utf-8")
        self.assertIn("tối đa 2-3 kỹ năng", rule)
        self.assertTrue(rule.startswith("---\nname: context-budget"))
        for name, needle in (("AGENTS.md", "Ngân sách ngữ cảnh"), ("AGENTS.en.md", "Context budget")):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn(needle, text, name)
            self.assertIn(".agents/rules/context-budget.md", text, name)

    def test_validation_ladder_in_quality_gate(self) -> None:
        text = (ROOT / ".agents/rules/quality-gate-workflows.md").read_text(encoding="utf-8")
        for level in ("P0", "P1", "P1.5", "P2", "P3", "P4"):
            self.assertIn(f"| {level} |", text)

    def test_notice_credits_upstream(self) -> None:
        text = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
        for needle in ("vudovn/antigravity-kit", "MIT", "VUDOVN"):
            self.assertIn(needle, text)


class AntigravityKitSkillsTest(unittest.TestCase):
    BASE = ROOT / "plugins/antigravity-kit-plugin/skills"

    def test_imported_skills_present(self) -> None:
        for name in ("design-spec", "verify-changes", "brainstorming", "i18n-localization", "coordinator-mode"):
            self.assertTrue((self.BASE / name / "SKILL.md").is_file(), name)

    def test_no_dangling_workflow_or_memory_references(self) -> None:
        for name in ("design-spec", "verify-changes", "brainstorming", "i18n-localization", "coordinator-mode"):
            for f in (self.BASE / name).rglob("*.md"):
                text = f.read_text(encoding="utf-8")
                for bad in ("/remember", ".agents/memory", "design-rules.md", "/orchestrate", "/coordinate", "/brainstorm", "/verify"):
                    self.assertNotIn(bad, text, f"{f.relative_to(ROOT)}: còn tham chiếu '{bad}'")

    def test_coordinator_keeps_approval_gate_and_reference(self) -> None:
        text = (self.BASE / "coordinator-mode/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Approval gate", text)
        self.assertTrue((self.BASE / "coordinator-mode/references/parallel-agents.md").is_file())

    def test_i18n_checker_runs(self) -> None:
        import subprocess, sys
        script = self.BASE / "i18n-localization/scripts/i18n_checker.py"
        out = subprocess.run([sys.executable, "-I", str(script), str(ROOT / "site")], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stdout + out.stderr)


class PptMasterTest(unittest.TestCase):
    BASE = ROOT / "plugins/ppt-master-plugin"
    SKILL = BASE / "skills/ppt-master"

    def test_imported_verbatim_with_attribution_files(self) -> None:
        for name in ("SKILL.md", "LICENSE", "SPONSORS.md", "SPONSORS_CN.md", "scripts/attribution_guard.py"):
            self.assertTrue((self.SKILL / name).is_file(), name)

    def test_upstream_integrity_guard_passes(self) -> None:
        import subprocess, sys
        out = subprocess.run([sys.executable, "-I", str(self.SKILL / "scripts/attribution_guard.py")],
                             capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stdout + out.stderr)

    def test_manifest_and_notice(self) -> None:
        manifest = json.loads((self.BASE / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "ppt-master-plugin")
        self.assertEqual(manifest["license"], "MIT")
        notice = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
        for needle in ("hugohe3/ppt-master", "v6.7.0", "nguyên bản"):
            self.assertIn(needle, notice)

    def test_env_example_not_ignored(self) -> None:
        self.assertIn("!.env.example", (ROOT / ".gitignore").read_text(encoding="utf-8"))


class GeminiWatermarkToolTest(unittest.TestCase):
    SCRIPT = ROOT / "plugins/ppt-master-plugin/skills/ppt-master/scripts/gemini_watermark_remover.py"

    def test_script_kept_and_routed(self) -> None:
        self.assertTrue(self.SCRIPT.is_file())
        for name in ("AGENTS.md", "AGENTS.en.md"):
            self.assertIn("gemini_watermark_remover.py", (ROOT / name).read_text(encoding="utf-8"), name)

    def test_script_is_local_only(self) -> None:
        text = self.SCRIPT.read_text(encoding="utf-8")
        for banned in ("requests", "urllib", "socket", "subprocess", "http://", "https://"):
            self.assertNotIn(banned, text, f"script gỡ watermark không được dùng '{banned}'")

    def test_responsible_use_notice(self) -> None:
        notice = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
        self.assertIn("gemini_watermark_remover.py", notice)
        self.assertIn("ghi chú nội dung do AI tạo", notice)


class PptMasterSecurityNoticeTest(unittest.TestCase):
    def test_security_notes_present(self) -> None:
        notice = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
        self.assertIn("Lưu Ý Bảo Mật Khi Dùng PPT Master", notice)
        for needle in ("môi trường ảo", "update_repo.py", "*_BASE_URL", "127.0.0.1", "Không commit `.env`"):
            self.assertIn(needle, notice)

    def test_update_repo_is_inert_in_this_layout(self) -> None:
        # update_repo.py chỉ chạy được trong kho Git riêng; thư mục plugin không được có .git.
        self.assertFalse((ROOT / "plugins/ppt-master-plugin/.git").exists())
