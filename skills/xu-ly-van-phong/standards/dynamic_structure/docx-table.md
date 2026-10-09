# Bảng (Table Patterns)

Các mẫu bảng chuẩn hóa cho DOCX và XLSX.

---

## Bề rộng bảng và cột (mặc định của skill)

Hai quy tắc bắt buộc:

1. **Tổng bề rộng bảng = bề rộng khổ nội dung** (Content Width = Page Width − lề trái − lề phải). Trong docx-js: `width: { size: 100, type: WidthType.PERCENTAGE }`.
2. **Bề rộng từng cột phải fit theo nội dung** (cơ chế tương tự AutoFit Contents của Word) rồi chia tỷ lệ lấp đủ 100%. Không chia đều các cột khi nội dung chênh lệch.

Thuật toán content-fit dùng trong Generator:

```javascript
// rows: mảng các dòng, mỗi dòng là mảng string theo cột (dòng 0 là header)
function fitColumns(rows, opts = {}) {
  const minPct = opts.minPct || 8;   // cột hẹp nhất không dưới 8%
  const cap = opts.cap || 60;        // cap ký tự để cột văn dài không nuốt hết bảng
  const nCols = rows[0].length;
  const weights = Array(nCols).fill(0);
  rows.forEach((r, ri) => r.forEach((cell, ci) => {
    const len = String(cell || '').length * (ri === 0 ? 1.2 : 1);
    weights[ci] = Math.max(weights[ci], Math.min(len, cap));
  }));
  let pct = weights.map(w => Math.max(minPct, (w / weights.reduce((a, b) => a + b, 0)) * 100));
  const sum = pct.reduce((a, b) => a + b, 0);
  return pct.map(p => Math.round((p / sum) * 100));
}
// Áp vào từng TableCell: width: { size: pct[i], type: WidthType.PERCENTAGE }
```

Sau khi tính máy, Agent soi lại bằng mắt ở bước QA: cột STT/mã không quá rộng, cột mô tả dài không bị bóp gãy chữ.

---

## Typography trong bảng (mặc định chung, rút từ văn bản thực tế)

| Quy tắc | Giá trị |
|---|---|
| Cỡ chữ trong bảng | Giảm 1-2pt so với body (body 14pt → bảng 12-13pt; body 11pt → bảng 9.5-10pt) |
| Header | Bold + center, có shading nhạt (đen trắng: xám nhạt; Track 2: accent1 chữ lt1) |
| Cột STT | Rộng ~0.9-1.0 cm, căn giữa |
| Cột số liệu | Căn PHẢI, không căn giữa |
| Đơn vị đo | Đặt trong header dạng "(ha)", "(%)", "(VNĐ)", không lặp lại ở từng ô |
| Trong ô | Không first-line indent, không justify (trái hoặc theo loại cột) |

---

## Mẫu T1 — Bảng lộ trình / giai đoạn

Dùng cho roadmap, milestone, chương trình đào tạo.

| Yếu tố | Quy chuẩn |
|---|---|
| Header | Fill đậm + text trắng bold, center, vAlign center |
| Cột 1 (nhãn) | Bold, center, zebra fill |
| Cột nội dung | Regular, align left |
| Border | `thin` toàn bộ |
| Row height | Header ≥ 30pt, body ≥ 24pt |
| Cell padding | 0.1 cm top/bottom, 0.15 cm left/right |

---

## Mẫu T2 — Bảng phân loại 3 cấp (Traffic Light)

Dùng cho phân loại rủi ro, xếp hạng ưu tiên, đánh giá bảo mật.

| Row | Fill | Ý nghĩa |
|---|---|---|
| Header | Đậm + text trắng | Tiêu đề |
| Cấp 1 / Safe | Xanh lá nhạt | An toàn, được phép |
| Cấp 2 / Warn | Vàng nhạt | Cần thận trọng |
| Cấp 3 / Danger | Đỏ nhạt | Cấm hoặc nhạy cảm |

Text trong cell giữ màu đen, chỉ fill cell thay đổi để đảm bảo contrast.

---

## Mẫu T3 — Bảng zebra (xen kẽ màu)

Dùng cho bảng số liệu, so sánh, thống kê.

| Yếu tố | Quy chuẩn |
|---|---|
| Header | Fill đậm + text trắng bold center |
| Row lẻ | Fill xám nhạt |
| Row chẵn | Trắng |
| Cột text | Align left |
| Cột số | Align right hoặc center |
| Dòng tổng cuối | Bold |

---

## Mẫu T4 — Bảng ma trận so sánh (2 trục)

Dùng cho so sánh cũ/mới, module × thuộc tính.

| Yếu tố | Quy chuẩn |
|---|---|
| Header hàng đầu | Đậm, text trắng |
| Cột 1 (tiêu chí) | Bold, fill nhẹ |
| Các cột so sánh | Regular |

---

## Mẫu T5 — Bảng số liệu kỹ thuật (VB dài)

Dùng cho bảng dữ liệu quan trắc, thống kê theo tháng.

| Yếu tố | Quy chuẩn |
|---|---|
| Style | Normal Table mặc định |
| Border | Thin 0.5pt đen |
| Header | Bold 11pt center |
| Data | Regular 11pt |
| Fill | **Không fill** (bảng số liệu không dùng màu) |

---

## Quy tắc chung mọi bảng

- Không bao giờ dùng bảng 1 cột — đó là list, viết lại thành bullet.
- Header luôn bold + center + contrast cao.
- Cột số luôn align phải, cột text align trái, cột nhãn ngắn center.
- Bảng từ 5 dòng trở lên bắt buộc zebra row.
- Bảng dài trên 20 dòng phải có dòng tổng cuối.
- Không merge cell theo chiều dọc trong body — phá vỡ sort/filter.
- Mỗi bảng có caption ngắn phía trên (bold) mô tả ý đồ.
- **Màu cụ thể** cho header/zebra: lấy từ `brand_kit.json` (header fill `accent1` chữ `lt1`, zebra fill `lt2`). Mặc định đen trắng: header fill xám đậm, zebra fill xám nhạt.
