# 💎 40 - Kho Tri Thức Cốt Lõi (Canonical Knowledge)

Nơi lưu trữ **chân lý cốt lõi (Single Source of Truth)** của hệ thống: các quy chế, quy trình chuẩn (SOP), cẩm nang xử lý sự cố (Runbooks), nguyên lý kiến trúc và hướng dẫn nghiệp vụ đã được kiểm duyệt và phê duyệt chính thức.

## 📌 Cấu Trúc Thư Mục Con
- `quy-dinh/`: Quy chế tổ chức, chức năng, quyền hạn, quyết định pháp lý.
- `quy-trinh-sop/`: Quy trình vận hành chuẩn (SOP) với các bước thực hiện chi tiết và SLA cam kết.
- `runbooks/`: Cẩm nang chẩn đoán và khắc phục sự cố kỹ thuật (P1-P4).
- `_templates/`: Biểu mẫu chuẩn để viết SOP và Runbook mới.

## 📌 Nguyên Tắc Hoạt Động (Strict Canonical Gate)
1. **Chất lượng kiểm duyệt cao**: Tài liệu tại đây phải đạt trạng thái `status: approved` hoặc `status: reviewed`.
2. **Không ghi đè tùy tiện**: AI Agent tuyệt đối không tự ý sửa đổi hoặc xóa tài liệu trong thư mục này nếu không có chỉ đạo rõ ràng từ người dùng/cấp quản lý.
3. **Mã hiệu định danh**: Mọi tài liệu chuẩn phải có ID ổn định (`QC-XX`, `SOP-XX`, `RB-XX`).
