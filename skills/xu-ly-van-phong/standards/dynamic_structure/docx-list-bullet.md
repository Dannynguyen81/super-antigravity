# Danh sách & Bullet

Quy chuẩn bullet, numbered list, indent cho văn bản Office.

---

## Bullet mặc định

Bullet trong DOCX dùng **dấu gạch ngang** `-` (hyphen) — ký tự mặc định của built-in style `List Bullet` trong Word.

```
- Triển khai nhanh, mỗi tác vụ hoàn thành trong 1 đến 2 tuần.
- Đo lường được ngay, quy ra giờ công tiết kiệm theo từng tuần.
- Dễ nhân bản, cùng một công thức áp dụng cho nhiều phòng ban.
```

Sub-bullet dùng **dấu cộng** `+`:

```
- Ranh giới tiếp giáp các khu vực:
    + Phía Bắc giáp khu công nghiệp
    + Phía Nam giáp biển
```

---

## Khi nào dùng gì

| Tình huống | Ký hiệu |
|---|---|
| Liệt kê không thứ tự | Bullet `-` |
| Liệt kê có thứ tự thực hiện | Số `1.` `2.` `3.` |
| Mục con trong cấp lớn | Chữ cái `a.` `b.` `c.` |
| Mệnh đề nhỏ inline | Ngoặc số `(1)` `(2)` `(3)` |
| Bullet nhấn mạnh | `-` kèm **bold đầu dòng** |
| Sub-bullet | `+` dấu cộng |

### Mẫu bullet nhấn mạnh:

```
- **Triển khai nhanh**, mỗi tác vụ hoàn thành trong 1 đến 2 tuần.
- **Đo lường được ngay**, quy ra giờ công tiết kiệm theo từng tuần.
```

---

## Hai kiểu bullet theo loại tài liệu

**Kiểu 1 - Khối thẳng (mặc định cho văn bản dài, hành chính, báo cáo):** dấu `-` và `+` là ký tự đầu đoạn thường, KHÔNG dùng hanging list. Đoạn bullet mang first-line indent 1.25 cm giống body, left indent 0. Toàn khối văn bản thẳng đều, phân cấp bằng chuỗi ký tự `1.` → `a)` → `-` → `+` (xem `docx-page-setup.md`).

**Kiểu 2 - Hanging list (cho tài liệu ngắn kiểu tây, brochure):**

| Thông số | Giá trị | DXA |
|---|---|---|
| Bullet position (vị trí dấu gạch) | 0.25" | 360 |
| Text indent (vị trí chữ) | 0.3" | 432 |
| Follow with | Space | `suffix: LevelSuffix.SPACE` |
| Sub-bullet position / text | 0.55" / 0.6" | 792 / 864 |

Trong docx-js: `indent: { left: 432, hanging: 72 }` cho cấp 1. Bullet căn justify như body nhưng KHÔNG có first-line indent (đã có hanging indent). Khi phân vân, chọn Kiểu 1.

### Spacing:

| Yếu tố | Giá trị |
|---|---|
| Space giữa bullets | 3pt |
| Space trước bullet đầu | 6pt |
| Space sau bullet cuối | 6pt |

---

## Điều cấm

| Điều cấm | Lý do |
|---|---|
| Không dùng `•` (chấm đậm) trong DOCX | Font dependency cao, không phải ký tự mặc định Word |
| Không dùng em dash `—` làm bullet | Em dash là dấu câu, không phải ký tự danh sách |
| Không dùng `*` hay `+` làm bullet cấp 1 | Ký tự markdown, render không ổn định trong Word |
| Không trộn nhiều kiểu bullet cùng danh sách | Phá vỡ cấu trúc thị giác |
| Không dùng bullet cho dưới 3 mục | Viết thành câu: "bao gồm: x, y và z" |

---

## Lập trình: Bullet trong docx-js

Dùng `LevelFormat.BULLET` + `numbering.reference` với ký tự **gạch ngang `-`** (tuyệt đối không dùng `•`):

```javascript
const { LevelFormat, LevelSuffix, AlignmentType } = require('docx');
numbering: {
  config: [{
    reference: "dash-bullet",
    levels: [{
      level: 0,
      format: LevelFormat.BULLET,
      text: "-",
      suffix: LevelSuffix.SPACE,
      alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 432, hanging: 72 } } },
    }],
  }],
}
// Trong Paragraph: numbering: { reference: 'dash-bullet', level: 0 }, alignment: AlignmentType.JUSTIFIED
```
