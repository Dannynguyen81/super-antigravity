---
name: strategic-compaction
description: "Chủ động kiểm soát ngữ cảnh, hướng dẫn nén context thông minh để tránh token burn và suy giảm trí nhớ trong phiên dài."
trigger: model_decision
---

# Quy Tắc Cốt Lõi: Quản Lý Ngữ Cảnh Chủ Động (Strategic Context Compactor)

> Ngăn chặn hiện tượng tràn bộ nhớ (Context Window Overflow), giảm token burn và duy trì độ sắc bén của Agent trong các phiên làm việc kéo dài.

## 1. Dấu Hiệu Cần Nén Ngữ Cảnh (Compaction Triggers)
Agent cần chủ động đề xuất hoặc thực hiện nén ngữ cảnh khi:
1. Phiên làm việc đã thực hiện trên **25 tool calls** hoặc hội thoại vượt qua **3 giai đoạn công việc lớn**.
2. Mô hình bắt đầu quên các chỉ thị đầu phiên hoặc lặp lại câu hỏi đã được giải quyết.
3. Chuẩn bị chuyển giao từ giai đoạn lập kế hoạch (Planning) sang giai đoạn triển khai (Implementation) hoặc nghiệm thu (Verification).

## 2. Tiêu Chuẩn Nén Ngữ Cảnh
Khi nén hoặc tổng hợp tiến trình:
- **Giữ lại**: Quyết định kiến trúc đã chốt, danh sách file đã thay đổi, trạng thái các task còn tồn đọng, các lỗi nghiêm trọng đã khắc phục.
- **Lược bỏ**: Toàn bộ log lỗi terminal trung gian, mã nháp tạm thời, các bước thăm dò file thất bại.
- **Đóng gói**: Sử dụng cú pháp Task Digest hoặc tạo file checkpoint `30-working/tasks/CHECKPOINT-YYYYMMDD.md` để lưu vết lâu dài.
