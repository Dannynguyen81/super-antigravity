---
name: context-budget
description: "Ngân sách ngữ cảnh: mỗi tác vụ chỉ nạp tối đa 2-3 kỹ năng và nạp theo 3 tầng để tránh tràn token."
trigger: always_on
---

# Quy Tắc Cốt Lõi: Ngân Sách Ngữ Cảnh Kỹ Năng

> Repo có hơn 100 kỹ năng. Nạp tất cả cùng lúc làm loãng ngữ cảnh và giảm chất lượng. Quy tắc này giới hạn số kỹ năng nạp và cách nạp.

## 1. Giới Hạn Số Kỹ Năng
- Mỗi tác vụ chỉ nạp **tối đa 2-3 kỹ năng**, chọn theo bảng ý định trong `AGENTS.md`.
- Cần nhiều hơn 3 kỹ năng thì tách thành các tác vụ con và nạp riêng cho từng tác vụ.
- Hàng ý định gộp nhiều kỹ năng (ví dụ `openspec-new-change` / `openspec-continue-change`) chỉ nạp kỹ năng khớp với việc đang làm.

## 2. Nạp Theo 3 Tầng (Progressive Disclosure)
| Tầng | Nội dung | Khi nào nạp |
| :--- | :--- | :--- |
| 1 | Frontmatter YAML (`name`, `description`) | Luôn có sẵn |
| 2 | Thân `SKILL.md` | Khi kỹ năng liên quan tới tác vụ |
| 3 | Thư mục `references/`, `scripts/` | Chỉ khi cần kiến thức sâu hoặc chạy tự động |

## 3. Kỷ Luật
- Không đọc tầng 3 "cho chắc". Chỉ đọc đúng tệp cần dùng.
- Khi ngữ cảnh đầy, áp dụng `strategic-compaction` trước khi nạp thêm kỹ năng.

> Nguồn ý tưởng: Antigravity Kit (MIT). Xem `NOTICE.md`.
