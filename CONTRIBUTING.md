# 🤝 Hướng Dẫn Đóng Góp Tri Thức — SecondBrain (CONTRIBUTING.md)

Chào mừng các thành viên cùng tham gia hoàn thiện và mở rộng kho tri thức số SecondBrain! Hệ thống vận hành theo **Mô hình Vòng Đời Tri Thức (Knowledge Lifecycle)**, bảo đảm tính an toàn, nhất quán và minh bạch.

---

## 🔄 1. Vòng Đời Thăng Cấp Tri Thức (Promotion Lifecycle)

Mọi tài liệu trong kho đều dịch chuyển theo 4 nấc thang giá trị:

```text
[10-inbox] ─────► [30-working] ─────► [40-knowledge] ─────► [50-outputs]
 (Thu nạp thô)    (Bản thảo draft)     (Đã phê chuẩn)      (Sản phẩm ra)
```

1. **Thu nạp (`10-inbox/`)**: Ném tài liệu thô, ghi chú nhanh vào đây.
2. **Soạn thảo (`30-working/`)**: Tạo bản thảo, biểu mẫu, biên bản với `status: draft`.
3. **Phê chuẩn (`40-knowledge/`)**: Sau khi được phản biện và lãnh đạo/chuyên gia duyệt, tài liệu được thăng cấp vào `40-knowledge/` với `status: approved`.
4. **Đóng gói (`50-outputs/`)**: Báo cáo tổng kết, công văn hoặc hồ sơ giao nộp cuối cùng được lưu trữ tại `50-outputs/`.

---

## 🌿 2. Quy Trình Đóng Góp Qua Git & GitHub

### Bước 1: Tạo nhánh mới (Branch)
- Soạn quy trình/tài liệu mới: `feature/them-[ten-tai-lieu]`
- Sửa đổi quy trình hiện có: `hotfix/sua-[ma-hieu]`
- Cập nhật biểu mẫu/checklist: `docs/cap-nhat-[ten-form]`

### Bước 2: Soạn thảo theo Templates chuẩn
- Luôn sao chép nội dung từ thư mục `_templates/` tương ứng (Ví dụ: `40-knowledge/_templates/mau-quy-trinh-sop.md` hoặc `30-working/_templates/mau-checklist-ca.md`).
- Bắt buộc điền đầy đủ Frontmatter YAML:
  ```yaml
  ---
  id: MA-SO-TAI-LIEU
  title: Tên tài liệu
  version: 1.0
  status: draft # Luôn để draft khi mới tạo
  author: Tên tác giả
  approver: Người phê duyệt
  tags: [chu-de, phan-loai]
  ---
  ```

### Bước 3: Kiểm tra tính toàn vẹn trước khi gửi
Chạy script kiểm tra để đảm bảo không bị gãy liên kết hay thiếu metadata:
```powershell
python scripts/kiem-tra-suc-khoe-brain.py
```

### Bước 4: Tạo Pull Request (PR)
- Đẩy nhánh lên GitHub và tạo Pull Request.
- Mô tả rõ: Nội dung thay đổi, lý do cập nhật và chỉ định người phụ trách duyệt PR.

---

## 🔒 3. Quy Tắc Bảo Mật Tuyệt Đối (Zero-Leak)

1. **Không commit thông tin nhạy cảm**:
   - Tuyệt đối không lưu mật khẩu, API keys, token truy cập cá nhân vào file Markdown.
   - Các biến môi trường hoặc cấu hình cá nhân phải lưu trong file `.env` (đã được chặn bởi `.gitignore`).
2. **Bảo mật dữ liệu cá nhân & đối tác**:
   - Khi đưa tài liệu hoặc biên bản vào kho, ẩn/mã hóa các thông tin nhạy cảm không cần thiết.
