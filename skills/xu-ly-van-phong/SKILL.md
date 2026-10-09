---
name: xu-ly-van-phong
description: TẠO, SỬA, CHUYỂN ĐỔI FILE VĂN PHÒNG (WORD, EXCEL, POWERPOINT, PDF) THEO KIẾN TRÚC 2 CHIỀU. Chiều Đọc bóc tách Brand Kit (màu sắc, font, logo) và Data từ file mẫu; Chiều Ghi tái tạo file mới bằng Node.js mang Brand DNA. Hỗ trợ 2 luồng xuất bản - Chuẩn Hành chính NĐ 30 (đen trắng, nghiêm ngặt) và Chuẩn Thẩm mỹ Hiện đại (Brand Kit linh hoạt). Kích hoạt khi user đề cập 'soạn công văn', 'tạo file word', 'làm slide', 'tạo bảng tính', 'cắt file pdf'; yêu cầu 'tạo báo cáo', 'làm đề xuất', 'bóc tách format file này', 'bắt chước format file này', 'xuất bản sách', 'chuyển sang word'; nói 'gộp file', 'tách trang', 'đổi sang pdf', 'format cho đẹp', 'chuyển file md này thành word/excel/slide'; trong tình huống user gửi file Word/Excel/PDF/Slide kèm yêu cầu chỉnh sửa, gửi file MD/text thô cần chuyển thành tài liệu chuyên nghiệp, hoặc cần tạo tài liệu từ đầu. KHÔNG dùng cho viết nội dung bài viết (skill này chỉ chuyên thiết kế và cấu trúc file), lập trình phần mềm, đăng bài mạng xã hội. Dùng cho MỌI nghiệp vụ tạo và xử lý file văn phòng — kể cả khi user chỉ gửi 1 file và nói 'xử lý giúp tôi'.
---

# Xử lý Văn phòng 2.0 (Bi-directional Pipeline)

Skill xử lý toàn diện file văn phòng (DOCX, XLSX, PPTX, PDF). Hệ thống hoạt động theo **Kiến trúc Song song 2 Chiều (Extractor & Generator)**: bóc tách Dữ liệu/Giao diện từ file cũ và vẽ lại hoàn toàn bằng Code.

---

## 1. Nguyên lý Hoạt động Cốt lõi (2 Chiều)

Mọi tài liệu đi qua hệ thống đều phân tách rõ Tầng Dữ liệu (Content) và Tầng Hiển thị (UI/Theme). Không sửa trực tiếp trên file xấu — bóc tách Data rồi sinh file mới.

### Chiều Đọc & Bóc tách (The Extractor) — Python

1. **Content:** Cào text thô, con số, công thức (markitdown, openpyxl, pdfplumber).
2. **Brand Kit (UI):** Chạy `scripts/extractor/extract_brand.py` — đọc `theme1.xml`, xuất `brand_kit.json` theo **schema chuẩn duy nhất** (khóa màu `dk1, lt1, dk2, lt2, accent1..accent6` — xem `resources/extractor_docs.md`).
3. **Assets:** Trích ảnh/logo từ `media/` ra `assets/`. Bóc Data từ biểu đồ/sơ đồ (không copy hình chết).

### Chiều Ghi & Tái tạo (The Generator) — Node.js

1. **Global Styles:** Nạp `brand_kit.json` vào Document Styles / Header Styles / Slide Master.
2. **Tái tạo Assets:** Nhúng ảnh từ `assets/` (kiểm tra tồn tại trước). Vẽ lại sơ đồ/biểu đồ dạng "sống".
3. **Đổ Content:** Đưa dữ liệu thô vào khung đã cấu hình Brand DNA và xuất bản.

---

## 2. Đường ray Đôi (Dual-Track) & Agent Workflow

**TỐI QUAN TRỌNG:** Agent KHÔNG ĐƯỢC tự ý đoán luồng định dạng. Trước khi tạo file, bắt buộc hỏi người dùng chọn 1 trong 3 tùy chọn:

| Lựa chọn | Luồng Thực thi | Ứng dụng | Kỹ thuật & Rào cản |
|:---:|---|---|---|
| **[1]** | **Chuẩn Hành chính Quốc gia (NĐ 30)** | Công văn, Tờ trình, Quyết định nhà nước | **Đen/Trắng tuyệt đối.** Cấm Brand Kit. Times New Roman, lề chuẩn (Trái 3, Phải 1.5, Trên/Dưới 2), header Quốc hiệu 2 cột. Theo `standards/nd30.md` + `templates/docx-hanh-chinh-*.md` |
| **[2]** | **Chuẩn Thẩm mỹ Hiện đại (Doanh nghiệp)** | Đề xuất, Pitch Deck, Báo cáo nội bộ, Tài liệu quy trình | **Kích hoạt Brand Kit.** Dùng Node.js Generator (`docx`, `exceljs`, `pptxgenjs`). Bảng zebra, callout box, nhúng logo và màu công ty |
| **[3]** | **Trích xuất Brand & Assets (chỉ bóc tách)** | Cào file mẫu lấy format làm chuẩn về sau | Chỉ chạy Extractor: `extract_brand.py` → `brand_kit.json` + `assets/`. Báo cáo thông số bóc được |

### Nhánh đặc biệt: User chỉ đưa CONTENT (file MD, text) — không có file mẫu

Đây là tình huống thường gặp nhất. KHÔNG được nhảy thẳng vào generate. Làm theo quy trình 3 bước trong `resources/content_analysis.md`:

1. **Phân tích content** → lập Kế hoạch Thiết kế (chia slide/sheet/heading, bảng nào thành chart, số nào thành callout) và trình user duyệt.
2. **Chốt Brand Kit** → đề xuất 2-3 preset từ thư viện 10 bộ (`standards/brand_kits/README.md` — phân loại sáng/tối, nóng/lạnh/trung tính, cổ điển/hiện đại), hoặc nhận màu/logo user cung cấp. **CẤM dùng `brand_kits/example/` cho tài liệu user thật.**
3. **Generate + QA loop.**

Ngoài các track trên, nghiệp vụ PDF (cắt/ghép/trích/convert) làm theo `resources/pdf.md` và `resources/convert.md` — xử lý cục bộ, không upload cloud.

---

## 3. Kiến trúc Vật lý của Skill

### Tầng 1: Tài liệu Hướng dẫn (`resources/`)

| File | Nội dung |
|---|---|
| `extractor_docs.md` | Bóc Brand Kit & Data bằng Python/XML Unpack. **Chứa schema chuẩn brand_kit.json** |
| `generator_docs.md` | Sinh file bằng Node.js từ Brand Kit. QA loop bắt buộc |
| `content_analysis.md` | **Content Analyzer** — quy tắc phân tích MD/text thô và map sang DOCX/XLSX/PPTX khi không có file mẫu |
| `xlsx.md` | Nguyên tắc Excel: Live Formula, Zero Error, column width chuẩn |
| `pptx.md` | Nguyên tắc slide: yếu tố thị giác, cỡ chữ, layout, QA visual |
| `pdf.md` | PDF digital vs scan, cắt/ghép/trích, PDF→DOCX |
| `convert.md` | Pipeline MD→DOCX (Pandoc), PDF→DOCX, DOCX→PDF |

### Tầng 2: Tiêu chuẩn (`standards/`)

- `nd30.md`: (Track 1) Bộ luật cứng cho văn bản nhà nước.
- `brand_kits/`: (Track 2) Thư mục "sống" — mỗi doanh nghiệp 1 folder con gồm `brand_kit.json` + `assets/`. Có sẵn **10 preset** phân loại theo tông màu (xem `brand_kits/README.md`) và `example/` (chỉ dùng test script).
- `dynamic_structure/`: 11 file quy chuẩn bố cục (page-setup, typography, heading, table, cover, header-footer, caption, list, special-blocks, xlsx-structure, pptx-structure) — nhận tham số màu/font từ Brand Kit.

### Tầng 3: Kịch bản Thực thi (`scripts/`)

- `extractor/extract_brand.py`: Bóc Brand Kit từ file Office bất kỳ.
- `extractor/office/`: Toolkit XML — unpack, pack, clone_text, validate, soffice.
- `extractor/convert/` + `extractor/format/`: Convert MD/PDF→DOCX, post-process Pandoc.
- `generator/template_docx.js`, `generator/template_xlsx.js`, `generator/template_pptx.js`: 3 khung Node.js sinh file từ `brand_kit.json` — dùng làm điểm khởi đầu, mở rộng theo yêu cầu.

### Tầng 4: Templates & Examples

- `templates/docx-hanh-chinh-*.md`: 9 mẫu khung nội dung văn bản NĐ 30 (công văn, quyết định, tờ trình...) + 1 mẫu đề xuất.
- `examples/`: 6 file tham chiếu, mở xem để "nhìn thấy" đích đến trước khi tạo file mới. Gồm 4 file sinh bằng chính skill này theo khung mặc định (`docx-mau-khung-chuan` đen trắng, `docx-mau-de-xuat-brand` Track 2 đủ bìa/callout/bảng màu, `pptx-mau-brand` 5 layout slide, `xlsx-mau-tracking` live formula) và 2 file Track 1 NĐ 30 (`docx-cong-van-mau`, `docx-quyet-dinh-mau`).

---

## Nguyên tắc Tuân thủ Tuyệt đối

1. **HỎI TRƯỚC KHI VẼ:** Luôn dùng Bảng 3 Lựa chọn hỏi User trước khi tạo file.
2. **TRACK 1 CẤM MÀU SẮC:** User chọn [1] → nghiêm cấm hàm vẽ màu, callout, font nghệ thuật. Tuân thủ tuyệt đối `nd30.md`. Không trộn format NĐ 30 với format doanh nghiệp.
3. **TRACK 2 PHẢI DÙNG NODE.JS:** User chọn [2] → dùng `docx`/`exceljs`/`pptxgenjs`. Không dùng `python-docx` để sinh file mới. Riêng trường hợp "giữ nguyên format file mẫu, chỉ thay nội dung" → dùng Unpack/Pack XML.
4. **MỘT SCHEMA DUY NHẤT:** Mọi script đọc/ghi `brand_kit.json` phải theo schema trong `extractor_docs.md`. Cấm hardcode mã màu.
5. **SƠ ĐỒ PHẢI SỐNG:** Cấm copy SmartArt/Chart cũ bằng ảnh (trừ logo). Bóc Data và vẽ lại bằng code.
6. **EXCEL PHẢI SỐNG:** Mọi ô tính toán dùng Live Formula, không hardcode kết quả.
7. **QA TRƯỚC KHI GIAO:** Convert sang PDF/ảnh soi bằng mắt ít nhất 1 vòng Generate → Inspect → Fix. Mọi tổ hợp text/nền đạt contrast WCAG.
8. **CONTENT-ONLY PHẢI QUA PHÂN TÍCH:** User chỉ đưa MD/text → bắt buộc chạy quy trình 4 bước của `content_analysis.md` (phân tích → chốt brand → biên tập → generate). Cấm dùng `brand_kits/example/` cho tài liệu thật, cấm nhồi 100% văn xuôi vào Excel/Slide.
9. **DOCX PHẢI THEO KHUNG MẶC ĐỊNH CHUNG:** Body justify + first-line indent 1.25cm + spacing 3pt/3pt + line atLeast 1.3 lần cỡ chữ; phân cấp bằng ký tự đầu dòng với left indent 0, đề mục cấp cao nhô trái 1.0cm (chi tiết trong `dynamic_structure/docx-page-setup.md`). Bullet dấu gạch `-`, không dùng `•`. Bảng full khổ nội dung, cột fit theo content, chữ trong bảng nhỏ hơn body 1-2pt. Nội dung phải qua biên tập, không copy nguyên văn MD. **Khung này áp dụng cho MỌI track; Brand Kit (Track 2) chỉ đắp lớp màu lên khung** gồm màu bảng biểu, màu chữ heading, highlight, callout box và thiết kế bìa, không được thay đổi thông số khung.
10. **KHỬ DẤU VẾT AI TRONG DẤU CÂU:** Cấm em dash `—` (thay ` - ` hoặc từ nối), cấm dấu hai chấm trong tiêu đề, cấm Oxford comma `, và`. Áp dụng cho mọi text trong DOCX/PPTX/XLSX, bảng quy tắc chi tiết trong `content_analysis.md` mục 3b. Sau generate phải đếm kiểm tra: `—`, `, và` và `:` trong heading đều phải bằng 0.

---

## Tác giả

**Nguyễn Duy Tùng**
Tư vấn xây dựng Song sinh số Doanh nghiệp (EDT) & Lực lượng Lao động AI (AI Workforce)
Liên hệ: 0904.004.920
