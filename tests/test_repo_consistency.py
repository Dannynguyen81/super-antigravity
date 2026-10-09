"""Số liệu và liên kết trong tài liệu phải khớp với nội dung thật của repo."""
from __future__ import annotations

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
