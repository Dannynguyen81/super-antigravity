---
id: RB-XX
title: Tên Sự Cố & Triệu Chứng
severity: P1 # P1-Critical | P2-High | P3-Medium | P4-Low
status: approved
updated_date: YYYY-MM-DD
author: Ten-Kỹ-Sư
service_affected: "Tên hệ thống / dịch vụ bị ảnh hưởng"
tags:
  - runbook
  - su-co
  - troubleshooting
---

# Runbook: [TÊN SỰ CỐ / MÃ LỖI]

> **Mức độ khẩn**: `severity: [P1/P2/P3]` | **Dịch vụ**: `[Tên dịch vụ]`

---

## 1. Dấu Hiệu Nhận Biết (Triệu Chứng)
- Cảnh báo giám sát (Alert message / Monitoring dashboard):
- Triệu chứng phía người dùng / khách hàng phản ánh:
- Mã lỗi thường gặp (Error codes / HTTP status / Syslog):

## 2. Bước 1: Hành Động Ngăn Chặn Khẩn Cấp (Immediate Mitigation)
*Mục tiêu: Giảm thiểu thiệt hại ngay trong 5-15 phút đầu tiên mà chưa cần biết nguyên nhân sâu xa.*
1. Thao tác kích hoạt hệ thống dự phòng (Failover / Switch):
   ```text
   [Ghi rõ lệnh hoặc nút bật/tắt dự phòng]
   ```
2. Thao tác cô lập luồng lỗi (Isolate):
   ```text
   [Ghi rõ lệnh cô lập]
   ```

## 3. Bước 2: Chẩn Đoán & Xác Định Nguyên Nhân (Diagnostic Flow)
Thực hiện tuần tự các bước kiểm tra sau:
- [ ] Kiểm tra 1: ... (Kết quả mong muốn: ...)
- [ ] Kiểm tra 2: ... (Nếu bất thường: xem bước X)
- [ ] Kiểm tra 3: ...

## 4. Bước 3: Khắc Phục Triệt Để & Khôi Phục Dịch Vụ
- Hướng dẫn các bước sửa lỗi chi tiết:
  1. ...
  2. ...
- Xác nhận hoàn tất khôi phục:
  - Chỉ số kiểm tra xác nhận hệ thống đã bình thường trở lại.

## 5. Quy Trình Báo Cáo & Leo Thang (Escalation Path)
| Thời gian quá hạn | Người nhận báo cáo | Kênh liên lạc |
| :--- | :--- | :--- |
| Sau 15 phút chưa rõ nguyên nhân | Trưởng ca trực | Điện thoại trực tiếp |
| Sau 30 phút chưa khắc phục được | Phó Trưởng ban kỹ thuật | Họp khẩn online / Hotline |
| Sau 60 phút (P1) | Trưởng ban DVVH | Báo cáo nhanh SMS/Hotline |
