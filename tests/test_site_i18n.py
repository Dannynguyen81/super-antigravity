"""Trang web site/ và các bản README song ngữ phải đồng bộ với nhau."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
LANGS = ("vi", "en")
ENTRY = re.compile(
    r'^\s*"([^"]+)":\s*\{\s*vi:\s*"((?:[^"\\]|\\.)*)",\s*en:\s*"((?:[^"\\]|\\.)*)"\s*\},?\s*$',
    re.MULTILINE,
)
PAIRS = (
    ("README.md", "README.en.md"),
    ("AGENTS.md", "AGENTS.en.md"),
    ("CONTRIBUTING.md", "CONTRIBUTING.en.md"),
    ("SOUL.md", "SOUL.en.md"),
)


def load_strings() -> dict[str, dict[str, str]]:
    text = (SITE / "i18n.js").read_text(encoding="utf-8")
    return {k: {"vi": vi, "en": en} for k, vi, en in ENTRY.findall(text)}


def html_keys(html: str) -> set[str]:
    keys = set(re.findall(r'data-i18n="([^"]+)"', html))
    for attr in re.findall(r'data-i18n-attr="([^"]+)"', html):
        keys.update(pair.split(":", 1)[1] for pair in attr.split(","))
    return keys


def linked(text: str, target: str) -> bool:
    return f"({target})" in text or f'href="{target}"' in text


class SiteI18nTest(unittest.TestCase):
    def test_every_entry_parses(self) -> None:
        text = (SITE / "i18n.js").read_text(encoding="utf-8")
        declared = len(re.findall(r'^\s*"[^"]+":\s*\{', text, re.MULTILINE))
        self.assertEqual(declared, len(load_strings()))

    def test_both_languages_are_filled(self) -> None:
        for key, values in load_strings().items():
            for lang in LANGS:
                self.assertTrue(values[lang].strip(), f"{key} thiếu bản {lang}")

    def test_html_keys_all_defined(self) -> None:
        html = (SITE / "index.html").read_text(encoding="utf-8")
        missing = html_keys(html) - set(load_strings())
        self.assertFalse(missing, f"khóa dùng trong HTML nhưng chưa có bản dịch: {sorted(missing)}")

    def test_no_unused_strings(self) -> None:
        html = (SITE / "index.html").read_text(encoding="utf-8")
        unused = set(load_strings()) - html_keys(html) - {"meta.title"}
        self.assertFalse(unused, f"bản dịch không được dùng: {sorted(unused)}")

    def test_html_fallback_matches_default_language(self) -> None:
        html = (SITE / "index.html").read_text(encoding="utf-8")
        strings = load_strings()
        for key, text in re.findall(r'data-i18n="([^"]+)"[^>]*>([^<]+)<', html):
            self.assertEqual(text.strip(), strings[key]["vi"], f"nội dung HTML của {key} lệch với i18n.js")

    def test_language_switch_present(self) -> None:
        html = (SITE / "index.html").read_text(encoding="utf-8")
        self.assertIn('<html lang="vi">', html)
        for lang in LANGS:
            self.assertIn(f'data-lang="{lang}"', html)

    def test_title_matches_default_language(self) -> None:
        html = (SITE / "index.html").read_text(encoding="utf-8")
        title = re.search(r"<title>(.*?)</title>", html).group(1)
        self.assertEqual(title, load_strings()["meta.title"]["vi"])


class ReadmePairsTest(unittest.TestCase):
    def test_pairs_exist_and_link_each_other(self) -> None:
        for vi, en in PAIRS:
            vi_text = (ROOT / vi).read_text(encoding="utf-8")
            en_text = (ROOT / en).read_text(encoding="utf-8")
            self.assertTrue(linked(vi_text, en), f"{vi} thiếu link sang {en}")
            self.assertTrue(linked(en_text, vi), f"{en} thiếu link về {vi}")

    def test_pairs_have_same_section_count(self) -> None:
        for vi, en in PAIRS:
            counts = [
                len(re.findall(r"^## ", (ROOT / name).read_text(encoding="utf-8"), re.MULTILINE))
                for name in (vi, en)
            ]
            self.assertEqual(counts[0], counts[1], f"{vi} và {en} lệch số mục ##")


if __name__ == "__main__":
    unittest.main()
