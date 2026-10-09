# 🧠 Antigravity AutoHarness Plugin

Tầng kỹ năng tự học (**Self-Learning Skill & Rule Layer**) tối ưu riêng cho **Google Antigravity**.

Tự động học hỏi từ các phiên làm việc thực tế, phân loại tri thức 3 tầng (Rules / Skills / Knowledge), tự cập nhật, hợp nhất các kỹ năng trùng lặp, và đào thải các kỹ năng không còn được sử dụng dựa trên tỷ lệ triệu hồi thực nghiệm (**empirical call-rate**).

---

## 🌟 Tính Năng Nổi Bật Cho Antigravity

1. **Native Antigravity Lifecycle Hooks**:
   - Sử dụng chuẩn `hooks.json` của Antigravity (`PreInvocation`, `PostToolUse`, `Stop`).
   - Tận dụng `transcriptPath` được Antigravity tự động chuyển giao trong payload `stdin`.
   - Bơm tủ kỹ năng gọn gàng qua `ephemeralMessage` tại `PreInvocation` mà không làm ô nhiễm lịch sử trò chuyện.
2. **Tri-Tier Distillation (Phân Luồng Tri Thức 3 Tầng)**:
   - **Tier 1 - Rules (`.agents/rules/*.md`)**: Cho các ràng buộc hành vi, phong cách, câu lệnh ngắn (<12 dòng).
   - **Tier 2 - Skills (`.agents/skills/*/SKILL.md`)**: Cho các quy trình nghiệp vụ nhiều bước, runbooks, scripts.
   - **Tier 3 - Knowledge (`.agents/knowledge/decisions.md`)**: Cho các quyết định kiến trúc, thông số môi trường cố định.
3. **Dynamic Friction Trigger**:
   - Tự động kích hoạt đúc kết ngay lập tức khi phát hiện tín hiệu người dùng chỉnh sửa (*"sai rồi", "đừng dùng", "hãy thay bằng"*) hoặc chuỗi lỗi tool liên tiếp, không cần đợi đếm chay 50 tool calls.
4. **Bảo Mật 2 Lớp (Dual-Engine Safety Gate)**:
   - Lớp 1: Regex heuristic lọc lệnh độc hại (`curl | bash`, `ignore previous instructions`).
   - Lớp 2: AST Analysis phân tích tĩnh các script Python đi kèm để cấm gọi hàm động nguy hiểm.
5. **Windows Native & Concurrency Lock**:
   - Chạy thuần chuẩn Python 3.11+ Standard Library (không cần cài thêm bất kỳ thư viện bên ngoài nào).
   - Cơ chế khóa file tương thích Windows (`msvcrt`) và Unix (`fcntl`) chống race condition khi mở nhiều cửa sổ terminal.
6. **Bảo Toàn Kỹ Năng Do Người Dùng Viết**:
   - Tuyệt đối chỉ quản lý và đào thải các kỹ năng do AI tự tạo (`created_by: agent`). Không bao giờ xâm phạm các kỹ năng do lập trình viên tự viết.

---

## 🚀 Kích Hoạt & Cài Đặt

Chạy script cài đặt toàn cục sang Antigravity:
```powershell
.\scripts\install-to-antigravity.ps1
```

Hoặc kích hoạt lệnh tức thì trong phiên Antigravity:
- Gõ `/learn` hoặc nói: *"Ghi nhớ bài học phiên này"* để đúc kết kinh nghiệm ngay lập tức.
