# Tài liệu Hướng dẫn: Chiều Ghi & Tái tạo (The Generator)

Hướng dẫn dùng thư viện Node.js để "Vẽ UI" và sinh file Office, nạp thông số từ Brand Kit.

---

## 1. Nguyên tắc cốt lõi

- Mọi file Đề xuất, Báo cáo, Slide (KHÔNG phải văn bản NĐ 30) **BẮT BUỘC** dùng luồng Node.js Generator.
- **Cấm hardcode mã màu** vào script. Mọi thông số thiết kế phải nạp từ `brand_kit.json` theo schema chuẩn (xem `extractor_docs.md` — khóa màu là `dk1, lt1, dk2, lt2, accent1..accent6`).
- Ba script mẫu có sẵn trong `scripts/generator/` — dùng làm khung khởi đầu, mở rộng theo nhu cầu:

| Script | Thư viện | Chạy |
|---|---|---|
| `template_docx.js` | `docx` | `node template_docx.js path/to/brand_kit.json` |
| `template_xlsx.js` | `exceljs` | `node template_xlsx.js path/to/brand_kit.json` |
| `template_pptx.js` | `pptxgenjs` | `node template_pptx.js path/to/brand_kit.json` |

Cài đặt: `npm install docx exceljs pptxgenjs`

---

## 2. Kỹ thuật nạp Brand Kit

### DOCX (`docx` module)

**Khung mặc định chung cho body text** (chi tiết trong `dynamic_structure/docx-page-setup.md`): justify + first-line indent 1.25cm + spacing 3pt/3pt + line atLeast 1.3 lần cỡ chữ. Phân cấp bằng ký tự đầu dòng, left indent 0, đề mục cấp cao nhô trái 1.0cm. Ngoại lệ: trong bảng, heading, đoạn căn giữa. Bullet dùng dấu gạch `-` (xem `dynamic_structure/docx-list-bullet.md`), bảng full khổ nội dung + cột fit theo content + chữ nhỏ hơn body 1-2pt (xem `dynamic_structure/docx-table.md`, hàm `fitColumns`).

```javascript
const { LineRuleType } = require('docx');
// Body 11pt: line atLeast 14pt (280). Body 14pt (hành chính): line atLeast 18pt (360).
const BODY = { alignment: AlignmentType.JUSTIFIED, indent: { firstLine: 709 }, spacing: { before: 60, after: 60, line: 280, lineRule: LineRuleType.AT_LEAST } };
const HEAD_TOP = { indent: { firstLine: 567 } }; // đề mục cấp cao nhô trái 1.0cm
```

**Vai trò của Brand Kit trên khung này:** chỉ thêm lớp màu, gồm fill header bảng và zebra, màu chữ heading, highlight từ khóa, callout box và thiết kế bìa. Không đổi thông số khung (indent, spacing, alignment).

Không gán màu vào từng Paragraph. Khai báo `styles` toàn Document:

```javascript
const brand = JSON.parse(fs.readFileSync(brandKitPath, 'utf8'));
const doc = new Document({
  styles: {
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1",
        run: { color: brand.colors.accent1, font: brand.fonts.heading, bold: true }
      },
      {
        id: "Normal", name: "Normal",
        run: { color: brand.colors.dk1, font: brand.fonts.body }
      }
    ]
  }
});
```

### XLSX (`exceljs` module)

Tạo đối tượng Style và áp dụng hàng loạt:

```javascript
const headerStyle = {
  font: { name: brand.fonts.heading, bold: true, color: { argb: 'FF' + brand.colors.lt1 } },
  fill: { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FF' + brand.colors.accent1 } },
  alignment: { horizontal: 'center', vertical: 'middle', wrapText: true }
};
worksheet.getRow(1).eachCell((cell) => { Object.assign(cell, headerStyle); });
```

**Live Formula bắt buộc:** ô tính toán phải là công thức sống, không hardcode kết quả:

```javascript
// ❌ SAI
sheet.getCell('B10').value = 4500;
// ✅ ĐÚNG
sheet.getCell('B10').value = { formula: 'SUM(B2:B9)' };
```

### PPTX (`pptxgenjs` module)

Thiết lập Master Slide một lần duy nhất:

```javascript
const masterObjects = [
  { rect: { x: 0, y: 7.0, w: '100%', h: 0.52, fill: { color: brand.colors.accent1 } } }
];
if (brand.assets && brand.assets.logo && fs.existsSync(brand.assets.logo)) {
  masterObjects.push({ image: { x: 0.5, y: 0.35, w: 1.4, h: 0.7, path: brand.assets.logo } });
}
pptx.defineSlideMaster({
  title: 'MASTER_SLIDE',
  background: { color: brand.colors.lt1 },
  objects: masterObjects
});
```

---

## 3. Quản lý Asset & Tái tạo Biểu đồ

- **Logo/ảnh:** luôn kiểm tra `fs.existsSync()` trước khi nhúng — `assets.logo` có thể vắng mặt.
- **Biểu đồ:** dùng `pptx.addChart()` (hoặc chart của exceljs), nạp mảng Data thô đã bóc từ Extractor, tô màu bằng mảng `[brand.colors.accent1, brand.colors.accent2, brand.colors.accent3, ...]`. Không copy ảnh chụp biểu đồ cũ.

---

## 4. Bài học thực chiến khi viết script build

- **Syntax-check trước khi chạy:** luôn chạy `node --check script.js` trước khi thực thi. Nếu script được ghi qua ổ đĩa đồng bộ (mount Windows), kiểm tra thêm đuôi file — có thể bị byte null hoặc cụt ký tự cuối, khắc phục bằng `tr -d '\000'` và soi `tail -1`.
- **Script build riêng cho từng deliverable:** đặt tên file output theo nội dung + loại (ví dụ "Ten du an - Gioi thieu.docx", "Ten du an - Slide gioi thieu.pptx", "Ten du an - Du lieu.xlsx") thay vì Output_X chung chung.
- **Brand kit truyền qua argv:** script nhận đường dẫn brand_kit.json làm tham số, luôn dùng đường dẫn tuyệt đối khi chạy từ thư mục khác.

## 5. QA bắt buộc trước khi giao file

```bash
# Convert sang PDF để soi bằng mắt
python scripts/extractor/office/soffice.py --headless --convert-to pdf output.docx
pdftoppm -jpeg -r 150 output.pdf page

# Đọc lại nội dung
python -m markitdown output.docx
```

Kiểm tra: chữ tràn khung, contrast thấp (mọi tổ hợp text/nền phải đạt WCAG), placeholder còn sót, màu có đúng brand kit không. Vòng lặp: Generate → Convert → Inspect → Fix → Re-verify, ít nhất 1 chu kỳ trước khi báo xong.

**Mẹo soi nhanh nhiều trang:** ghép các ảnh trang/slide thành 1-2 ảnh lưới (PIL: paste vào grid 2×3) rồi xem 1 lần, thay vì mở từng ảnh. Lỗi hay gặp nhất: tiêu đề slide dài tràn 2 dòng đè lên vạch trang trí — xem quy tắc độ dài trong `pptx.md`.
