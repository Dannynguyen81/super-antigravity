---
id: RB-01
title: Xử lý sự cố mất kết nối mạng truyền dẫn diện rộng
severity: P1
status: approved
updated_date: 2026-02-20
author: To-Ky-Thuat-Mang
service_affected: "Hệ thống Mạng & Dịch vụ Truyền dẫn DVVH"
tags:
  - runbook
  - su-co
  - mat-ket-noi
  - network
  - p1
---

# Runbook: Xử Lý Sự Cố Mất Kết Nối Mạng Truyền Dẫn

> **Mức độ khẩn**: `P1 - Khẩn cấp` | **Dịch vụ**: `Hệ thống Mạng & Dịch vụ Truyền dẫn`

---

## 1. Dấu Hiệu Nhận Biết (Triệu Chứng)
- Hệ thống NMS báo động đỏ: Hàng loạt node mất tín hiệu (Down / Unreachable).
- Mất kết nối tới trung tâm dữ liệu hoặc các trạm trạm vệ tinh.
- Hotline trực ca nhận liên tiếp trên 3 cuộc gọi báo gián đoạn dịch vụ trong 5 phút.

## 2. Bước 1: Hành Động Ngăn Chặn Khẩn Cấp (Trong 5 phút đầu)
1. **Kiểm tra trạng thái đường truyền thứ cấp (Backup Link)**:
   - Xác nhận đường truyền dự phòng có tự động chuyển đổi (auto-failover) hay không.
   - Nếu không tự chuyển: Thực hiện chuyển đổi thủ công sang kênh dự phòng 4G/Kênh thuê riêng thứ cấp.
2. **Thông báo khẩn**: Gửi cảnh báo P1 vào kênh trực ban điều hành.

## 3. Bước 2: Chẩn Đoán Tuần Tự
- [ ] **Kiểm tra nguồn điện & thiết bị vật lý**: Xác nhận phòng máy/tủ thiết bị có mất điện lưới hoặc nhảy aptomat không.
- [ ] **Kiểm tra cổng quang (Optical Interface)**: Đo mức suy hao công suất quang Rx. Nếu Rx < -27 dBm ➔ đứt cáp hoặc suy hao cao.
- [ ] **Kiểm tra nhà cung cấp dịch vụ (ISP / Telco)**: Liên hệ đầu mối NOC của đối tác viễn thông để xác nhận sự cố tuyến cáp quang trục.

## 4. Bước 3: Phối Hợp Khắc Phục
- Nếu đứt cáp quang ngoại vi: Yêu cầu đội ứng cứu cáp xuất phát ngay, thời gian hàn nối tối đa 2 giờ.
- Nếu lỗi thiết bị định tuyến: Thay thế bằng card/thiết bị dự phòng nóng (Hot-spare).

## 5. Quy Trình Leo Thang (Escalation)
- **10 phút**: Báo cáo Trưởng ca điều phối.
- **20 phút**: Báo cáo Phó Trưởng ban phụ trách kỹ thuật.
- **30 phút**: Báo cáo Trưởng ban DVVH và kích hoạt đội ứng cứu khẩn cấp ngoài hiện trường.
