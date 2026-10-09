---
name: tra-cuu-sop
description: Tra cứu quy trình vận hành chuẩn (SOP) và cẩm nang sự cố (Runbooks) trong kho tri thức cốt lõi (40-knowledge). Triggers on: 'tra cứu sop', 'xem quy trình', 'các bước xử lý', 'hướng dẫn thao tác', 'runbook sự cố'.
---

# Kỹ Năng: Tra Cứu Quy Trình & Cẩm Nang Sự Cố

Kỹ năng này giúp AI nhanh chóng tìm kiếm, tổng hợp và trích dẫn chính xác các quy trình vận hành (SOP) và cẩm nang xử lý sự cố (Runbooks) có trong kho tri thức cốt lõi (`40-knowledge/`).

## Khi Nào Kích Hoạt?
- Người dùng hỏi về cách xử lý một sự cố cụ thể hoặc quy trình thao tác chuẩn.
- Người dùng hỏi về quy trình tiếp nhận, bàn giao hoặc phê duyệt.
- Người dùng cần biết chỉ số SLA cam kết cho từng loại dịch vụ/công việc.

## Quy Trình Xử Lý Của Agent
1. **Quét tài liệu liên quan**:
   - Tìm kiếm file trong thư mục `40-knowledge/quy-trinh-sop/` và `40-knowledge/runbooks/`.
2. **Trích xuất thông tin trọng tâm**:
   - Nếu là sự cố (Runbook):
     * Cung cấp ngay **Bước 1: Hành động ngăn chặn khẩn cấp**.
     * Cung cấp **Quy trình chẩn đoán tuần tự**.
     * Cung cấp **Ma trận leo thang (Escalation path)** theo mốc thời gian.
   - Nếu là quy trình (SOP):
     * Nêu rõ đối tượng thực hiện và các bước tuần tự 1, 2, 3.
     * Nêu rõ chỉ số SLA và biểu mẫu liên quan.
3. **Định dạng câu trả lời**:
   - Luôn đặt link wiki nội bộ: `[[40-knowledge/quy-trinh-sop/sop-xx|SOP-XX]]` hoặc `[[40-knowledge/runbooks/rb-xx|RB-XX]]`.
   - Kết thúc câu trả lời bằng lời nhắc an toàn vận hành.
