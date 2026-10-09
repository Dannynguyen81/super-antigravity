---
name: scope-locking-and-grill-me
description: "Chống đoán mò yêu cầu mơ hồ: Tự động kích hoạt Grill-Me Mode đặt tối đa 2-3 câu hỏi trắc nghiệm làm rõ trước khi thực thi tính năng mới."
trigger: always_on
---

# Quy Tắc Cốt Lõi: Khóa Phạm Vi & Phỏng Vấn Làm Rõ (Scope Locking & Grill-Me Protocol)

> **Mục tiêu**: Khắc phục triệt để điểm yếu "đoán mò ý định" và "vội vàng gõ code lung tung" của AI khi nhận các chỉ thị ngắn gọn, mơ hồ hoặc tiềm ẩn nhiều phương án kiến trúc.

---

## 1. Cơ Chế Grill-Me (Relentless Clarification)

Khi người dùng đưa ra một yêu cầu mới mang tính kiến trúc, thay đổi luồng nghiệp vụ lớn, hoặc khi chỉ thị còn mơ hồ:

1. **Tuyệt đối KHÔNG**:
   - ❌ Không tự tiện suy diễn yêu cầu rồi cặm cụi code ngay.
   - ❌ Không đặt những câu hỏi mở chung chung làm mất thời gian của người dùng.
   - ❌ Không đưa ra danh sách dài hơn 3 câu hỏi.

2. **Bắt buộc THỰC HIỆN**:
   - Sử dụng công cụ tương tác chuyên biệt `ask_question` (hoặc định dạng trắc nghiệm sắc nét nếu gọi text).
   - Đưa ra **tối đa 2 đến 3 câu hỏi trắc nghiệm then chốt**, mỗi câu có từ 2-4 phương án cụ thể kèm khuyến nghị `(Recommended)`.
   - Các câu hỏi phải xoay quanh:
     * **Ranh giới phạm vi (Scope Boundary)**: Tính năng này chỉ áp dụng cục bộ hay ảnh hưởng toàn hệ thống?
     * **Phương án kỹ thuật (Architectural Trade-off)**: Chọn hiệu năng tối đa hay triển khai đơn giản, ít phụ thuộc thư viện ngoài?
     * **Mức độ tương thích ngược (Backward Compatibility)**: Giữ nguyên cấu trúc cũ hay refactor toàn diện?

---

## 2. Tiêu Chuẩn Câu Hỏi Chuẩn "Grill-Me"

- Mỗi câu hỏi phải định hình rõ ràng tác động của quyết định:
  ```text
  Ví dụ:
  Câu hỏi 1: "Phương thức lưu trữ trạng thái phiên làm việc nên dùng giải pháp nào?"
  - (Recommended) Phương án A: Lưu trữ cục bộ qua file JSON/Markdown trong `.agents/` (nhẹ, zero-dependency).
  - Phương án B: Sử dụng SQLite database để hỗ trợ truy vấn phức tạp và đánh chỉ mục.
  ```

---

## 3. Khóa Phạm Vi (Scope Locking) Sau Khi Làm Rõ

Sau khi người dùng đã lựa chọn các phương án:
1. Agent lập tức **khóa chặt phạm vi (Lock Scope)** vào tài liệu kế hoạch hoặc artifact.
2. Tuyệt đối **không mở rộng phạm vi (No Scope Creep)** ngoài những gì người dùng đã chốt.
3. Nếu phát hiện rủi ro phát sinh trong lúc code, dừng lại và cảnh báo thay vì âm thầm làm thêm việc ngoài thỏa thuận ban đầu.
