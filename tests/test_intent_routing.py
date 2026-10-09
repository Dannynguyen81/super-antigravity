"""Kiểm tra cấu trúc bảng ý định và định tuyến mẫu trong AGENTS.md / AGENTS.en.md."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROUTERS = ("AGENTS.md", "AGENTS.en.md")
ROW = re.compile(r"^\|\s*\*(.+?)\*\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")


def rows(router: str) -> list[tuple[list[str], str, str]]:
    out = []
    for line in (ROOT / router).read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if m:
            phrases = re.findall(r'"([^"]+)"', m.group(1))
            out.append((phrases, m.group(2), m.group(3)))
    return out


def skill_dirs() -> dict[str, Path]:
    dirs = list((ROOT / "skills").iterdir()) + list((ROOT / "plugins").glob("*/skills/*"))
    return {d.name: d for d in dirs if (d / "SKILL.md").is_file()}


def route(router: str, utterance: str) -> list[str]:
    """Trả về các mục tiêu (cột 2) có cụm từ khóa nằm trong câu người dùng."""
    text = utterance.lower()
    return [target for phrases, target, _ in rows(router) if any(p.lower() in text for p in phrases)]


class RouterStructureTest(unittest.TestCase):
    def test_rows_parse_with_phrases(self) -> None:
        for router in ROUTERS:
            parsed = rows(router)
            self.assertGreaterEqual(len(parsed), 30, router)
            for phrases, target, action in parsed:
                self.assertTrue(phrases, f"{router}: hàng thiếu cụm từ khóa ({target})")
                self.assertTrue(target.strip() and action.strip(), f"{router}: ô trống ({phrases})")

    def test_vi_and_en_have_same_row_count(self) -> None:
        self.assertEqual(len(rows("AGENTS.md")), len(rows("AGENTS.en.md")))

    def test_vi_and_en_route_to_same_targets_in_order(self) -> None:
        self.assertEqual([t for _, t, _ in rows("AGENTS.md")], [t for _, t, _ in rows("AGENTS.en.md")])

    def test_no_duplicate_phrase_inside_router(self) -> None:
        for router in ROUTERS:
            seen: dict[str, str] = {}
            for phrases, target, _ in rows(router):
                for p in phrases:
                    key = p.lower()
                    self.assertNotIn(key, seen, f"{router}: cụm '{p}' trùng ở {seen.get(key)} và {target}")
                    seen[key] = target

    def test_referenced_skills_exist(self) -> None:
        known = set(skill_dirs()) | {d.name for d in (ROOT / "plugins").iterdir()}
        # problem-solving-pro là skill của developer-power-skills; kiểm tra qua known.
        for router in ROUTERS:
            for _, target, _ in rows(router):
                for name in re.findall(r"`([^`]+)`", target):
                    leaf = name.split("/")[-1]
                    self.assertIn(leaf, known, f"{router}: '{name}' không tồn tại trong repo")

    def test_referenced_folders_exist(self) -> None:
        for router in ROUTERS:
            text = (ROOT / router).read_text(encoding="utf-8")
            for path in set(re.findall(r"`((?:\d\d-[a-z]+)/[a-z0-9-/]*)`", text)):
                self.assertTrue((ROOT / path).exists(), f"{router}: thư mục '{path}' không tồn tại")


class SampleRoutingTest(unittest.TestCase):
    CASES = (
        ("tra cứu quy trình tiếp nhận yêu cầu", "tra-cuu-sop"),
        ("máy chủ bị sự cố mất kết nối", "tra-cuu-sop"),
        ("soạn biên bản họp giao ban sáng nay", "soan-bien-ban-hop"),
        ("tạo checklist bàn giao ca trực", "lap-checklist-ca"),
        ("soạn báo cáo tuần", "xu-ly-van-phong"),
        ("tư vấn luật về điều khoản hợp đồng", "tu-van-phap-luat"),
        ("máy tính chậm quá", "cham-soc-may-tinh"),
        ("lập spec cho tính năng đăng nhập", "spec"),
        ("tìm bug giúp tôi", "qa"),
        ("vẽ diagram luồng đăng ký", "baoyu-diagram"),
        ("viết code sạch hơn", "clean-code"),
        ("thiết kế api cho đơn hàng", "api-patterns"),
        ("quét lỗ hổng bảo mật", "vulnerability-scanner"),
        ("deploy cloudflare worker", "cloudflare-suite"),
        ("làm file excel báo cáo doanh thu", "xlsx"),
        ("tạo pptx cho buổi họp", "pptx"),
        ("gộp pdf hai tệp này", "pdf"),
        ("soạn file word hợp đồng", "docx"),
        ("điều tra lỗi thanh toán", "investigate"),
        ("tôi muốn rút bài học từ phiên này", "learn"),
        ("review pr số 12", "code-review-skill"),
        ("dọn test thừa trong dự án", "test-audit"),
        ("openspec tạo thay đổi mới cho module báo cáo", "openspec-new-change"),
        ("openspec lưu trữ thay đổi đã xong", "openspec-archive-change"),
        ("openspec xác minh thay đổi trước khi ship", "openspec-verify-change"),
        ("làm giao diện tối giản", "minimalist-ui"),
        ("nén ảnh banner này", "baoyu-compress-image"),
        ("markdown sang html cho wechat", "baoyu-markdown-to-html"),
        ("kiểm tra hiệu năng web và core web vitals", "web-perf"),
        ("tối ưu seo cho trang chủ", "seo-fundamentals"),
        ("viết ứng dụng react native", "vercel-react-native-skills"),
        ("tạo chrome extension chặn quảng cáo", "chrome-extensions"),
        ("xây mcp server trên cloudflare", "building-mcp-server-on-cloudflare"),
        ("cần đối tượng bền vững giữ phòng chat", "durable-objects"),
        ("viết script powershell dọn thư mục", "powershell-windows"),
    )
    CASES_EN = (
        ("look up procedure for onboarding", "tra-cuu-sop"),
        ("draft minutes of the meeting", "soan-bien-ban-hop"),
        ("write spec for login", "spec"),
        ("find bugs in the checkout", "qa"),
        ("draw diagram of the flow", "baoyu-diagram"),
        ("design API for orders", "api-patterns"),
        ("deploy cloudflare today", "cloudflare-suite"),
        ("make excel file from this data", "xlsx"),
        ("merge pdf files", "pdf"),
        ("investigate error in payments", "investigate"),
        ("review pr 12", "code-review-skill"),
        ("openspec create new change for reports", "openspec-new-change"),
        ("compress image before upload", "baoyu-compress-image"),
        ("improve web performance, check lcp score", "web-perf"),
        ("build mcp server on cloudflare", "building-mcp-server-on-cloudflare"),
        ("write a powershell script", "powershell-windows"),
    )

    def assert_routes(self, router: str, cases) -> None:
        for utterance, expected in cases:
            targets = route(router, utterance)
            self.assertTrue(
                any(expected in t for t in targets),
                f"{router}: '{utterance}' phải tới '{expected}', thực tế: {targets}",
            )

    def test_vietnamese_utterances(self) -> None:
        self.assert_routes("AGENTS.md", self.CASES)

    def test_english_utterances(self) -> None:
        self.assert_routes("AGENTS.en.md", self.CASES_EN)

    def test_unrelated_utterance_matches_nothing(self) -> None:
        self.assertEqual(route("AGENTS.md", "hôm nay trời đẹp quá"), [])
        self.assertEqual(route("AGENTS.en.md", "what a lovely day"), [])

    def test_generic_phrases_do_not_hit_openspec(self) -> None:
        for router, text in (("AGENTS.md", "cập nhật thay đổi trong báo cáo"), ("AGENTS.en.md", "update change in the report")):
            self.assertFalse(any("openspec" in t for t in route(router, text)), router)

    def test_case_insensitive(self) -> None:
        self.assertTrue(route("AGENTS.md", "TRA CỨU QUY TRÌNH"))


if __name__ == "__main__":
    unittest.main()
