---
name: soan-bien-ban-hop
description: Chuyển đổi ghi chú thô hoặc tóm tắt cuộc họp thành biên bản họp chính thức chuẩn thể thức, lưu vào 30-working/bien-ban-nhat-ky. Triggers on: 'soạn biên bản', 'họp giao ban', 'biên bản cuộc họp', 'tổng hợp họp'.
---

# Kỹ Năng: Soạn Thảo Biên Bản Cuộc Họp

Kỹ năng này giúp AI tiếp nhận các ghi chú thô, gạch đầu dòng từ cuộc họp và tự động cấu trúc thành biên bản họp chuyên nghiệp, sẵn sàng lưu trữ vào `30-working/bien-ban-nhat-ky/`.

## Khi Nào Kích Hoạt?
- Người dùng dán nội dung trao đổi trong cuộc họp và yêu cầu lập biên bản.
- Kết thúc một phiên thảo luận, cần tổng hợp thành nghị quyết/kết luận chỉ đạo và phân công nhiệm vụ.

## Tiêu Chuẩn Biên Bản Chuẩn
1. **Phần đầu**:
   - Thời gian, địa điểm, thành phần tham dự, người chủ trì và thư ký.
2. **Nội dung thảo luận**:
   - Tách bạch rõ các ý kiến báo cáo, khó khăn tồn tại và ý kiến phản hồi.
3. **Kết luận của Chủ trì**:
   - Đánh số thứ tự từng chỉ đạo rõ ràng.
4. **Bảng phân công nhiệm vụ (Bắt buộc phải có Action Items)**:
   - Cột: STT | Nhiệm vụ | Người chịu trách nhiệm | Hạn hoàn thành (Deadline) | Sản phẩm đầu ra.

## Hành Động Của Agent
- Tự động gợi ý tên file theo chuẩn: `30-working/bien-ban-nhat-ky/bb-YYYY-MM-DD-[ten-cuoc-hop].md`.
- Tạo file với đầy đủ Frontmatter YAML chuẩn của SecondBrain.
