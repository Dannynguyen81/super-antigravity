# 🔨 30 - Không Gian Làm Việc Đang Xử Lý (Working)

Không gian làm việc năng động (Active Workspace) dành cho các tài liệu đang trong quá trình soạn thảo, các dự án đang triển khai, bản thảo, biên bản cuộc họp và checklist theo dõi hằng ngày.

## 📌 Cấu Trúc Thư Mục Con
- `checklists/`: Danh mục kiểm tra công việc, bàn giao ca, rà soát hệ thống.
- `bien-ban-nhat-ky/`: Biên bản các cuộc họp, nhật ký hoạt động định kỳ.
- `du-an/`: Các tài liệu dự án đang thực hiện có thời hạn và mục tiêu cụ thể.
- `_templates/`: Các biểu mẫu chuẩn để tạo nhanh ghi chú làm việc mới.

## 📌 Nguyên Tắc Hoạt Động
- Mọi tài liệu ở đây thường có nhãn `status: draft` hoặc `status: in-progress`.
- Khi một quy trình hoặc tài liệu trong `30-working/` hoàn thiện và được phê duyệt chính thức:
  * Nếu là quy chuẩn/hướng dẫn vĩnh viễn ➔ Thăng cấp (Promote) vào `40-knowledge/`.
  * Nếu là báo cáo/kết quả bàn giao ➔ Đóng gói đưa vào `50-outputs/`.
