# Thiết lập Trang (Page Setup)

Quy chuẩn khổ giấy, lề và line spacing cho các loại văn bản.

---

## Khổ giấy

Mọi văn bản dùng **A4** (210 × 297 mm / 595 × 842 pt / 11906 × 16838 DXA).

---

## Margin theo loại văn bản

| Loại | Top | Bottom | Left | Right | Ghi chú |
|---|---|---|---|---|---|
| VB ngắn/trung bình (đề xuất, báo cáo) | 2 cm | 2 cm | **3 cm** | 2 cm | Left 3 cm để đóng gáy |
| VB dài (thuyết minh, nghiên cứu) | 2 cm | 2 cm | **3 cm** | **1.5 cm** | Right hẹp vì in 1 mặt |
| VB hành chính NĐ 30 | 2 cm | 2 cm | **3 cm** | 2 cm | Theo NĐ 30/2020 |
| Slide PPTX | — | — | — | — | Không áp dụng page margin |

**Quy đổi DXA:** 1 cm = 567 DXA. Ví dụ: 3 cm = 1701 DXA, 2 cm = 1134 DXA.

**Chiều rộng nội dung (Content Width):** Lấy Page Width trừ Left trừ Right.
- VB ngắn: `11906 − 1701 − 1134 = 9071 DXA`
- VB dài: `11906 − 1701 − 851 = 9354 DXA`

---

## MẶC ĐỊNH BODY PARAGRAPH (bắt buộc, chung cho mọi DOCX)

Bộ thiết lập này rút từ nghiên cứu văn bản hành chính thực tế (quyết định phê duyệt quy hoạch) kết hợp yêu cầu người dùng. Đây là KHUNG chung, không phụ thuộc Track: Track 2 chỉ đắp thêm lớp màu, không thay đổi khung này. Ngoại lệ duy nhất: nội dung trong bảng, heading và đoạn cần căn giữa (bìa, motto, caption).

| Thuộc tính | Giá trị | Trong docx-js |
|---|---|---|
| Alignment | **Justified** | `alignment: AlignmentType.JUSTIFIED` |
| First line indent | **1.25 cm** (709 DXA), thống nhất cho MỌI cấp nội dung | `indent: { firstLine: 709 }` |
| Space before / after | **3pt / 3pt** (đối xứng) | `spacing: { before: 60, after: 60 }` |
| Line spacing | **At least 1.3 × cỡ chữ** (font 14pt → atLeast 18pt = 360; font 11pt → atLeast 14pt = 280) | `spacing: { line: 360, lineRule: LineRuleType.AT_LEAST }` |

### Phân cấp đề mục (quy tắc khối thẳng)

- KHÔNG tăng left indent theo cấp. Mọi cấp đều `left indent = 0`, phân cấp thể hiện thuần bằng ký tự đầu dòng theo chuỗi `Điều X.` / `I.` → `1.` → `a)` → `-` → `+` (hoặc H1 → H2 → bullet với tài liệu doanh nghiệp). Khối văn bản thẳng đều, tiết kiệm chiều ngang.
- Đề mục cấp cao nhất dùng first-line indent **1.0 cm** (nhỏ hơn body 1.25 cm) để "nhô trái", tạo điểm neo thị giác mà không cần đổi cỡ chữ.
- Đề mục bold, nội dung regular. Không dùng italic hay underline để phân cấp.

### Lề nén cho văn bản dài

Văn bản dài nhiều trang được phép nén lề trên/dưới xuống **1.75 cm** để tiết kiệm giấy (giữ nguyên lề trái 3 cm). VB hành chính NĐ 30 nộp chính thức giữ 2.0-2.5 cm theo `standards/nd30.md`.

---

## Line spacing các loại đoạn khác

| Loại đoạn | Giá trị |
|---|---|
| Heading | 1.15-1.33, không thụt đầu dòng |
| Title doc | 1.0 |
| Bảng caption | 1.15 |
| Code block / ASCII art | 1.0, bắt buộc không giãn |

---

## Paragraph spacing các loại đoạn khác

| Loại đoạn | Space before | Space after |
|---|---|---|
| List item | 2pt | 3pt |
| Heading cấp 1 | 18pt | 8pt |
| Heading cấp 2 | 12pt | 6pt |
| Title doc | 0 | 6pt |
| Caption dưới bảng | 0 | 12pt |

---

## Header và Footer distance

| Thông số | Giá trị |
|---|---|
| Header distance from top | 0.8 cm (22.7pt) |
| Footer distance from bottom | 1.3 cm (36pt) |

<!-- NDT-0904004920 -->
