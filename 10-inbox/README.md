# 📥 10 - Hộp Thư Tiếp Nhận (Inbox)

Phễu tiếp nhận ban đầu của toàn bộ hệ thống tri thức. Mọi thông tin thô, tài liệu mới, bài viết, ý tưởng hay tài liệu tải về chưa phân loại đều được đưa vào đây.

## 📌 Nguyên Tắc Hoạt Động
1. **Không phân vân khi lưu trữ**: Khi nhận được tài liệu mới hoặc có ý tưởng bất chợt, hãy thả ngay vào `10-inbox/` để không làm gián đoạn luồng làm việc.
2. **Xử lý tự động (Auto-Ingest)**:
   - Các file văn phòng (`.docx`, `.xlsx`, `.pptx`, `.pdf`, `.txt`) sẽ được script `python scripts/nhap-tai-lieu.py` tự động chuyển đổi thành Markdown sạch.
3. **Không tích tụ lâu dài (Zero Inbox Rule)**:
   - Thư mục này mang tính chất tạm thời. Định kỳ, tài liệu sau khi được xử lý sẽ được phân loại:
     - Nguồn tham khảo ➔ Chuyển vào `20-sources/`
     - Đang soạn thảo/làm dở ➔ Chuyển vào `30-working/`
     - Đã chuẩn hóa thành quy chuẩn/SOP ➔ Chuyển vào `40-knowledge/`
     - Không còn giá trị ➔ Chuyển vào `_Delete/` hoặc `90-archive/`
