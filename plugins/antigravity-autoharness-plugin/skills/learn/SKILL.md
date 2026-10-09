---
name: learn
description: "Use when users request /learn, 'ghi nhớ bài học phiên này', 'tự học kinh nghiệm', or ask to distill the current conversation into durable skills or rules."
category: meta
---

# Learn: Chắt Lọc Bài Học Phiên Này Vào Tủ Kỹ Năng

Khi người dùng yêu cầu `/learn`, hãy phân tích toàn bộ phiên trò chuyện vừa diễn ra để chắt lọc những bài học có giá trị dài hạn.

## Quy Trình 3 Bước:

### 1. Phân loại Tri Thức (Tri-Tier Routing)
- **Ràng buộc hành vi / Phong cách (<12 dòng)**: Đề xuất tạo Rule (`.agents/rules/<name>.md`).
  *Ví dụ: "Luôn dùng tiếng Việt khi viết commit", "Không dùng thư viện X".*
- **Quy trình nhiều bước / Kỹ thuật giải quyết lỗi**: Đề xuất tạo Skill (`.agents/skills/<name>/SKILL.md`).
  *Ví dụ: "Quy trình thiết lập Docker cho dự án", "Cách bypass lỗi build Vite".*
- **Quyết định kiến trúc / Tham số môi trường**: Đề xuất ghi vào `.agents/knowledge/decisions.md`.

### 2. Nguyên Tắc So Sánh Trước (Compare-First)
- Kiểm tra danh mục skill và rule hiện có trong `.agents/skills/` và `.agents/rules/`.
- Nếu chủ đề đã tồn tại: Cập nhật hoặc bổ sung subsection vào skill cũ, tuyệt đối không tạo bản sao gần trùng lặp.

### 3. Đảm Bảo Chuẩn Mực
- Không sao chép nguyên văn nhật ký trò chuyện.
- Thân skill ngắn gọn, súc tích (dưới 25 dòng). Các code mẫu chi tiết chuyển vào `references/` hoặc `scripts/`.
- Sử dụng công cụ `write_to_file` để lưu lại sau khi người dùng xác nhận.
