---
name: lap-checklist-ca
description: Tạo biểu mẫu checklist kiểm tra hệ thống và bàn giao ca trực vận hành, lưu vào 30-working/checklists. Triggers on: 'tạo checklist', 'kiểm tra đầu ca', 'bàn giao ca trực', 'danh mục kiểm tra ca'.
---

# Kỹ Năng: Lập Checklist Công Việc & Ca Trực

Kỹ năng này tự động sinh danh mục kiểm tra (Checklist) cho nhân sự thực thi, phù hợp với từng ca làm việc hoặc theo đặc thù thời điểm (kiểm tra định kỳ, rà soát trước phát hành).

## Khi Nào Kích Hoạt?
- Nhân sự chuẩn bị vào ca trực hoặc thực hiện quy trình phức tạp cần danh mục kiểm tra.
- Bàn giao công việc giữa các bộ phận hoặc giữa hai ca làm việc.
- Chuẩn bị thực hiện công tác bảo dưỡng, rà soát hệ thống.

## Tiêu Chuẩn Checklist
Mỗi checklist sinh ra phải bao gồm tối thiểu:
1. **Thông tin chung**: Thời điểm, người thực hiện, phạm vi kiểm tra.
2. **Các hạng mục kiểm tra cụ thể**: Phân nhóm logic theo từng khu vực hoặc từng module.
3. **Mục ghi chú bất thường**: Nơi ghi lại lỗi hoặc ticket phát sinh.
4. **Xác nhận bàn giao**: Chữ ký hoặc xác nhận hoàn tất.

## Hành Động Của Agent
- Sinh checklist dạng checkbox markdown (`- [ ]`).
- Đính kèm phần thông tin xác nhận cuối ca/kỳ kiểm tra.
- Gợi ý lưu vào `30-working/checklists/cl-YYYY-MM-DD-[ten-checklist].md`.
