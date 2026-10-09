# Ban Phát Triển — Trưởng Ban

**Vai trò:** Nâng cấp toàn diện hệ thống — cập nhật tài liệu, nâng cấp quy trình, quản trị nhân sự, tối ưu ngữ cảnh.

---

## Nhân sự

| Nhân viên | File | Chuyên môn | Bắt buộc? |
|-----------|------|------------|-----------|
| Chuyên viên nâng cấp | upgrade.md | Phân tích output → rút pattern → bổ sung skill | ⚪ Tùy chọn |
| Kiểm toán viên | style-audit.md | Phân tích bài mẫu → rút style DNA | ⚪ Tùy chọn |
| Framework nghiên cứu | research-framework.md | Quy trình thu thập + phân tích bài báo | ⚪ Tùy chọn |
| Kết quả nghiên cứu | research-results.md | Kho dữ liệu pattern đã phát hiện | ⚪ Tùy chọn |

## Giao việc

```
1. Sau bài viết phức tạp:
   └── style-audit.md phân tích → upgrade.md bổ sung (TUẦN TỰ)

2. User cung cấp bài viết mẫu để nâng cấp skill:
   └── Xem quy trình chi tiết bên dưới (§ Phân tích bài viết mẫu)

3. Khi cần quản trị nhân sự:
   └── upgrade.md thực hiện (xem quy trình Quản trị nhân sự)

4. Tối ưu ngữ cảnh định kỳ:
   └── upgrade.md rà soát kích thước module
```

### Phân tích bài viết mẫu → nâng cấp skill

```
Bước 1: style-audit.md phân tích từng bài (4 bước)
        → Bao gồm: đếm số câu/đoạn, xác định đoạn siêu dài và LÝ DO
        ⛔ GATE: Xuất báo cáo style-audit → ghi log

Bước 2: upgrade.md nhận output → so sánh registry các file skill
        → Đề xuất bổ sung, format 5 thành phần (Tên + Mô tả + Công thức + Ví dụ + Cấm)
        → Chỉ rõ FILE SKILL ĐÍCH (editorial/rhythm.md, review/natural.md, v.v.)
        ⛔ GATE: Xuất đề xuất → trình user duyệt

Bước 3: Sau khi user duyệt → sửa các file skill đích
        → Ghi changelog vào upgrade.md
        → Kiểm tra module ≤ 300 dòng, tổng load ≤ 200 dòng/lượt
```

**Nguyên tắc:** Ban Phát triển PHÂN TÍCH + ĐỀ XUẤT. Cập nhật thực tế nằm ở file skill đích (editorial/, review/, v.v.), KHÔNG lưu nội dung skill trong development/.

## Cam kết hoàn thành

- [ ] Pattern mới đã được document đúng format (5 thành phần)
- [ ] Lead file của ban liên quan đã cập nhật bảng nhân sự
- [ ] Changelog đã ghi nhận
- [ ] Tổng instructions mỗi lượt load vẫn ≤ 200 dòng

## Quản trị nhân sự

```
THÊM nhân viên mới:
├── Xác định thuộc ban nào
├── Tạo file mới theo format nhân viên (header + quy tắc + checklist)
├── Cập nhật lead-*.md → thêm vào bảng nhân sự
├── Cập nhật SKILL.md nếu ảnh hưởng dispatch
└── Ghi changelog vào upgrade.md

LOẠI BỎ nhân viên:
├── Đánh giá: được gọi trong 3 bài gần nhất?
├── KHÔNG → gộp vào file khác hoặc xóa
├── Cập nhật lead-*.md + SKILL.md
└── Ghi changelog

CẬP NHẬT nhân viên:
├── Thêm/sửa/bỏ quy tắc trong file nhân viên
├── Cập nhật cam kết hoàn thành trong lead nếu ảnh hưởng
└── Ghi changelog
```

## Tối ưu ngữ cảnh

```
Rà soát sau mỗi bài phức tạp:
├── File nào > 150 dòng? → Cân nhắc tách
├── File nào < 30 dòng? → Cân nhắc gộp
├── Nội dung trùng giữa 2 file? → Hợp nhất
├── Lead file outdated? → Cập nhật bảng nhân sự
├── Bài mẫu mới? → Lưu vào examples/
└── Tổng instructions mỗi lượt load vẫn ≤ 200 dòng?
```

## Hợp đồng ban giao

- Nhận input từ: Tổng biên tập (yêu cầu cải tiến) hoặc tự khởi xướng sau bài phức tạp
- Giao output: Cập nhật trực tiếp vào các file module + lead + SKILL.md
