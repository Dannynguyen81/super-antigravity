---
id: CL-XX
title: Tên Biểu Mẫu Checklist
frequency: "Hằng ngày / Mỗi ca trực / Hằng tuần"
role: "Kỹ sư trực ca"
status: approved
tags:
  - checklist
  - ca-truc
  - bieu-mau
---

# Checklist: [TÊN CHECKLIST / BIỂU MẪU]

> **Kỳ thực hiện**: `frequency` | **Người thực hiện**: `role`

---

## 1. Thông Tin Ca Trực
- **Ngày thực hiện**: YYYY-MM-DD
- **Ca trực**: [Ca 1: 06h00 - 14h00 / Ca 2: 14h00 - 22h00 / Ca 3: 22h00 - 06h00]
- **Nhân sự trực**: [Tên nhân sự 1, Tên nhân sự 2]
- **Trưởng ca phụ trách**: [Tên trưởng ca]

## 2. Danh Mục Kiểm Tra Trọng Yếu

### A. Kiểm tra Hạ tầng & Môi trường Phòng máy
- [ ] Nhiệt độ phòng máy ổn định (18°C - 22°C, độ ẩm 45% - 55%)
- [ ] Hệ thống nguồn điện chính và UPS báo trạng thái bình thường (Normal)
- [ ] Hệ thống PCCC khí sạch không có cảnh báo lỗi

### B. Kiểm tra Tình trạng Hệ thống & Dịch vụ
- [ ] Bảng điều khiển giám sát (Dashboard NMS/Monitoring): Tất cả dịch vụ xanh (Green)
- [ ] Tải CPU và RAM của các máy chủ trọng yếu < 70%
- [ ] Dung lượng ổ đĩa lưu trữ còn trống > 25%
- [ ] Trạng thái sao lưu (Backup) ngày hôm trước thành công 100%

### C. Kiểm tra An toàn & Kết nối
- [ ] Kết nối mạng truyền dẫn chính và phụ hoạt động tốt
- [ ] Không có cảnh báo bất thường về an ninh mạng hoặc truy cập trái phép

## 3. Ghi Chú Sự Cố Hoặc Bất Thường Trong Ca
*(Nếu có sự cố, ghi rõ mã ticket hoặc liên kết đến Runbook)*
- Sự cố 1: ... (Đã xử lý / Đang bàn giao)

## 4. Xác Nhận Bàn Giao
- **Người bàn giao**: (Ký / Ghi rõ họ tên)
- **Người nhận bàn giao**: (Ký / Ghi rõ họ tên)
