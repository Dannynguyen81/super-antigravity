---
id: SOP-01
title: Quy trình tiếp nhận và xử lý yêu cầu dịch vụ vận hành
version: 1.0
status: approved
created_date: 2026-01-10
updated_date: 2026-03-15
author: To-Dieu-Phoi
approver: Truong-Ban-DVVH
sla_target: "Phản hồi trong 15 phút, xử lý theo mức độ ưu tiên P1-P4"
tags:
  - sop
  - tiep-nhan
  - yeu-cau
  - sla
---

# Quy Trình: Tiếp Nhận & Xử Lý Yêu Cầu Dịch Vụ Vận Hành

> **Mã hiệu**: `SOP-01` | **Phiên bản**: `1.0` | **Trạng thái**: `approved`

---

## 1. Mục Đích & Phạm Vi Áp Dụng
- **Mục đích**: Chuẩn hóa quy trình từ lúc phát sinh yêu cầu hỗ trợ vận hành từ đối tác/khách hàng/nội bộ đến khi xử lý dứt điểm và đóng ticket.
- **Phạm vi**: Áp dụng cho toàn bộ kỹ sư trực ca và tổ điều phối.

## 2. Ma Trận Phân Loại Mức Độ Ưu Tiên (SLA)
| Mức độ | Định nghĩa | Thời gian phản hồi | Thời gian xử lý cam kết |
| :--- | :--- | :--- | :--- |
| **P1 - Khẩn cấp** | Toàn bộ dịch vụ gián đoạn, ảnh hưởng diện rộng | <= 5 phút | <= 1 giờ |
| **P2 - Cao** | Dịch vụ suy giảm chất lượng nghiêm trọng, không có đường dự phòng | <= 15 phút | <= 4 giờ |
| **P3 - Trung bình** | Sự cố cục bộ, đã có phương án thay thế tạm thời | <= 30 phút | <= 8 giờ |
| **P4 - Thấp** | Yêu cầu hỗ trợ thông tin, thay đổi cấu hình nhỏ | <= 60 phút | <= 24 giờ |

## 3. Các Bước Thực Hiện Chi Tiết

### Bước 1: Tiếp nhận thông tin
- Kênh tiếp nhận: Hotline, Email điều hành hoặc Hệ thống Giám sát tự động.
- Ghi nhận đầy đủ: Đơn vị yêu cầu, người liên hệ, thời điểm phát sinh, triệu chứng cụ thể, log/ảnh chụp nếu có.

### Bước 2: Phân loại & Điều phối
- Kỹ sư trực ca đối chiếu bảng SLA phía trên để gán mức P1 - P4.
- Nếu là P1/P2: Kích hoạt ngay lập tức [[40-knowledge/runbooks/rb-01-su-co-mat-ket-noi|Runbook sự cố khẩn cấp]] và báo cáo Trưởng ca.

### Bước 3: Xử lý kỹ thuật & Cập nhật tiến độ
- Kỹ sư được phân công thực hiện xử lý theo SOP kỹ thuật chuyên môn.
- Cập nhật định kỳ trạng thái xử lý mỗi 30 phút đối với P1/P2.

### Bước 4: Nghiệm thu & Đóng yêu cầu
- Xác nhận lại với đơn vị yêu cầu rằng dịch vụ đã ổn định hoàn toàn.
- Ghi log vào [[30-working/bien-ban-nhat-ky/bb-2026-10-giao-ban-tuan|Nhật ký ca trực]].
