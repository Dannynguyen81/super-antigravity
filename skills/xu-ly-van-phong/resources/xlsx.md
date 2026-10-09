# Kỹ năng XLSX — Excel

Nguyên tắc chung cho bảng tính, áp dụng cho cả 2 chiều (đọc bằng openpyxl, ghi bằng exceljs).

---

## Nguyên tắc tối thượng: Live Formula

Tuyệt đối cấm hardcode kết quả tính toán vào cell. Excel phải "sống" — tính lại khi đổi đầu vào.

```javascript
// exceljs (Generator - Track 2)
sheet.getCell('B10').value = { formula: 'SUM(B2:B9)' };   // ✅
sheet.getCell('C5').value = { formula: '(C4-C2)/C2' };    // ✅
```

```python
# openpyxl (Extractor hoặc file đơn giản)
sheet['B10'] = '=SUM(B2:B9)'   # ✅
sheet['B10'] = total            # ❌ hardcode
```

---

## Công cụ theo chiều

| Chiều | Công cụ | Dùng cho |
|---|---|---|
| Đọc & bóc tách | `openpyxl` (`data_only=False`), `pandas` | Cào số liệu, giữ công thức gốc, data cleaning |
| Ghi & tái tạo (Track 2) | `exceljs` (Node.js) | Sinh file mới mang Brand Kit |

---

## Column width chuẩn

| Loại cột | Width | Align |
|---|---|---|
| STT | 4-7 | Center |
| Tên / nội dung | 28-48 | Left, wrap |
| Trạng thái | 14-17 | Center |
| Ngày | 12-14 | Center |
| Phần trăm | 10-12 | Center |
| Ghi chú | 25-32 | Left, wrap |

Chi tiết bố cục multi-sheet, phân cấp row, dòng tổng: xem `standards/dynamic_structure/xlsx-structure.md`.

---

## Zero Error Policy

Cấm tuyệt đối khi mở file:

- `#REF!` — cell trỏ vùng không tồn tại
- `#DIV/0!` — chia cho 0 chưa bọc `IF`
- `#VALUE!` — lộn data type

---

## Dependencies

```
pip install openpyxl pandas
npm install exceljs
```
