# Ghi Nhận Nguồn

Một số nội dung trong repo này được chắt lọc và điều chỉnh từ dự án mã nguồn mở **Antigravity Kit**:

- **Kho nguồn**: https://github.com/vudovn/antigravity-kit
- **Phiên bản tham chiếu**: `2026.8.31`
- **Giấy phép**: MIT, Copyright (c) 2026 VUDOVN

## Nội Dung Bắt Nguồn

| Thành phần trong repo này | Nguồn gốc |
| :--- | :--- |
| `.agents/rules/context-budget.md` (ý tưởng ngân sách ngữ cảnh và nạp 3 tầng) | Sách "Antigravity Kit - Hướng dẫn toàn diện" và kho nguồn |
| Thang kiểm tra P0-P4 trong `.agents/rules/quality-gate-workflows.md` | Lớp kiểm chứng (Validation Layer) của Antigravity Kit |
| `plugins/antigravity-kit-plugin/skills/design-spec/` | Kỹ năng `design-spec` |
| `plugins/antigravity-kit-plugin/skills/verify-changes/` | Kỹ năng `verify-changes` |
| `plugins/antigravity-kit-plugin/skills/brainstorming/` | Kỹ năng `brainstorming` |
| `plugins/antigravity-kit-plugin/skills/i18n-localization/` | Kỹ năng `i18n-localization` |
| `plugins/antigravity-kit-plugin/skills/coordinator-mode/` | Kỹ năng `coordinator-mode` và `parallel-agents` |
| `plugins/antigravity-autoharness-plugin/src/safety_gate.py` | Viết lại bằng Python từ `validate-tool-call.mjs` |

## Thành Phần Nhập Nguyên Bản: PPT Master

- **Kho nguồn**: https://github.com/hugohe3/ppt-master (tag `v6.7.0`, commit `b4efe3d`)
- **Giấy phép**: MIT, Copyright (c) 2025-2026 Hugo He
- **Vị trí**: `plugins/ppt-master-plugin/skills/ppt-master/` được chép **nguyên bản, không chỉnh sửa**.
- **Ràng buộc**: skill có cổng toàn vẹn (`scripts/attribution_guard.py`) và dừng hẳn nếu `LICENSE`, `SPONSORS.md`, `SPONSORS_CN.md` hoặc metadata nguồn bị sửa hoặc xóa. Không được chỉnh các tệp này.
- **Công cụ gỡ watermark Gemini** (`scripts/gemini_watermark_remover.py`): giữ và dùng theo quyết định của chủ repo. Script xử lý cục bộ bằng Pillow và NumPy, không gọi mạng. Chỉ dùng cho ảnh bạn có quyền xử lý, tuân thủ điều khoản dịch vụ của Gemini và nên ghi chú nội dung do AI tạo khi công bố.
- **Cài thư viện**: chạy `pip install -r plugins/ppt-master-plugin/skills/ppt-master/requirements.txt` khi cần dùng.

## Lưu Ý Về Hook An Toàn

`safety_gate.py` chỉ chặn một số mẫu lệnh phá hoại có độ tin cậy cao. Đây **không phải sandbox**. Cơ chế quyền và tin cậy không gian làm việc của Antigravity vẫn là hàng rào chính.

## Văn Bản Giấy Phép Gốc (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
