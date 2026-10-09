---
name: anti-slop-and-full-output
description: "Bắt buộc sinh mã đầy đủ, cấm cắt xén, cấm placeholder (TODO, ..., giữ nguyên) trong mọi hoàn cảnh."
trigger: always_on
---

# Quy Tắc Cốt Lõi: Zero-Placeholder & Full-Output Enforcement

> Áp dụng bắt buộc cho mọi phản hồi kỹ thuật, viết mã nguồn, sửa file và tài liệu.

## 1. Cấm Tuyệt Đối Mọi Mẫu Code Bỏ Dở (Zero Placeholder)
Tuyệt đối KHÔNG sử dụng các hình thức viết tắt làm đứt gãy luồng thực thi:
- ❌ CẤM: `// TODO: tự code tiếp`, `// Implement here`, `// Logic tương tự...`
- ❌ CẤM: `/* các hàm khác giữ nguyên */`, `// Keep other methods unchanged`
- ❌ CẤM: Dấu ba chấm trần `...` thay thế cho logic bị bỏ sót.
- ❌ CẤM: Viết dở dang giữa một khối lệnh rồi kết thúc câu trả lời.

## 2. Quy Trình Ngắt Quãng An Toàn (Safe Token Breakpoint)
Khi nội dung phản hồi quá dài và tiếp cận giới hạn token:
1. Hoàn thành trọn vẹn đến ranh giới hàm, lớp hoặc file gần nhất.
2. Tuyệt đối không tự ý nén hay lược bỏ mã nguồn ở phần còn lại.
3. Kết thúc phản hồi bằng chỉ dẫn tiếp nối:
   ```text
   [PAUSED — X of Y complete. Gửi "continue" để viết tiếp từ: <tên_hàm_hoặc_file_tiếp_theo>]
   ```
4. Khi người dùng gửi "continue", tiếp tục viết trọn vẹn phần còn lại mà không lặp lại nội dung đã xuất xưởng.
