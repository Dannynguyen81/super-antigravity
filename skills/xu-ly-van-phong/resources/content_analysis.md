# Phân tích Nội dung & Lập Kế hoạch Thiết kế (Content Analyzer)

Dùng khi user chỉ đưa **content thô** (file MD, text, hoặc nội dung chat) và yêu cầu chuyển sang DOCX/XLSX/PPTX — KHÔNG có file mẫu để bóc Brand Kit.

Đây là mảnh ghép thứ 3 của kiến trúc: **Extractor** (bóc từ file mẫu) — **Content Analyzer** (phân tích content thô) — **Generator** (vẽ file).

---

## 1. Quy trình bắt buộc 3 bước

```
Bước 1: PHÂN TÍCH content (mục 2) → lập Kế hoạch Thiết kế
Bước 2: CHỐT Brand Kit (mục 3) → hỏi user, không tự đoán
Bước 3: BIÊN TẬP nội dung theo định dạng đích (mục 3b)
Bước 4: GENERATE theo kế hoạch + brand kit đã chốt → QA loop
```

**Cấm** nhảy thẳng từ nhận file MD sang generate. Kế hoạch Thiết kế (bước 1) phải được trình bày ngắn gọn cho user trước khi vẽ.

### 3b. Biên tập nội dung — không copy nguyên văn MD

File MD nguồn thường viết cho màn hình (giọng liệt kê, câu rời, emoji, markdown syntax). Đổ nguyên văn vào DOCX sẽ ra tài liệu "máy móc". Trước khi generate phải biên tập:

- **Câu dẫn mở section:** mỗi phần lớn có 1-2 câu dẫn dắt tự nhiên trước khi vào bullet/bảng, không để heading rồi nhảy thẳng vào danh sách.
- **Nối mạch giữa các đoạn:** thêm từ nối, tránh chuỗi đoạn cộc bắt đầu giống nhau.
- **Bullet chỉ dành cho liệt kê thật:** ý nào là lập luận liền mạch thì viết thành đoạn văn justify, không bẻ thành bullet.
- **Xóa dấu vết màn hình:** emoji, "→", markdown thô, IN HOA giữa câu (trừ tên riêng/cảnh báo chủ đích).
- **Giữ nguyên fact:** số liệu, giá, ngày tháng, tên riêng không được đổi khi biên tập.

**Khử dấu vết AI trong dấu câu (bắt buộc, áp dụng cho mọi text đổ vào DOCX/PPTX/XLSX):**

| Dấu vết AI | Quy định | Cách thay |
|---|---|---|
| Em dash `—` | CẤM tuyệt đối | Gạch ngang cách hai bên ` - `; hoặc từ nối theo chức năng: giải thích → "tức là/nghĩa là", tương phản → "nhưng/thế mà", chêm xen → ngoặc đơn `( )`; không chắc thì tách thành câu riêng |
| Dấu hai chấm trong tiêu đề | CẤM | Thay bằng ` - ` hoặc viết lại tiêu đề ("Nỗi đau: nghịch lý AI" → "Nghịch lý AI - cá nhân bay cao, tổ chức đứng im") |
| Dấu hai chấm giữa câu | Hạn chế | Chỉ giữ khi có từ dẫn nhập liệt kê (gồm, như sau, bao gồm) hoặc trích dẫn; còn lại thay bằng "là", "rằng", "trong đó", hoặc dấu phẩy |
| Oxford comma `, và` | CẤM | Bỏ dấu phẩy trước "và"; nếu gây nhập nhằng (chuỗi đã có "và" bên trong) thì thay bằng "cùng" hoặc viết lại |

Sau khi generate, chạy vòng kiểm tra tự động trên text bóc từ file xuất ra: đếm `—`, `, và ` và `:` trong heading phải bằng 0. Kiểm tra sâu hơn dùng skill `kiem-tra-bai-viet` (quy trình SCAN 8 tầng).

---

## 2. Phân tích tín hiệu trong content

Quét content và kiểm kê các tín hiệu sau:

| Tín hiệu trong MD | Ý nghĩa thiết kế |
|---|---|
| Số heading H1/H2/H3, độ sâu | Quy mô tài liệu, cách chia chương/slide |
| Bảng markdown | Ứng viên cho Excel sheet, DOCX table, hoặc chart |
| Cột chứa toàn số / % / tiền | Cần numFmt, dòng tổng Live Formula, hoặc vẽ chart |
| Danh sách bullet/số | DOCX list, PPTX icon rows, timeline |
| Con số nổi bật trong văn xuôi (%, x lần, tiền) | Stat callout trên slide, highlight box trong DOCX |
| Blockquote, câu cảnh báo/lưu ý | Callout box (viền accent1, nền lt2) |
| Code block | Khối code font Courier, nền lt2 |
| Cặp "Trước/Sau", "Vấn đề/Giải pháp" | Layout 2 cột |
| Chuỗi bước 1→2→3 | Process flow / timeline |

Kết quả kiểm kê quyết định **định dạng đích phù hợp** (khi user chưa chỉ định):

- Nhiều bảng số liệu, cần tính toán/lọc → **XLSX**
- Văn bản dài, cần đọc tuần tự, in ấn → **DOCX**
- Trình bày trước đám đông, nhiều thông điệp ngắn → **PPTX**
- User yêu cầu cả 3 → mỗi định dạng lấy phần content phù hợp với nó, KHÔNG nhồi 100% content vào cả 3 (xem mục 4).

---

## 3. Chốt Brand Kit khi không có file mẫu

**CẤM dùng `brand_kits/example/`** — đó là brand kit giả định, chỉ dành cho test script.

Có **thư viện 10 preset** phân loại theo trục sáng/tối, nóng/lạnh/trung tính, cổ điển/hiện đại — xem bảng chọn và cách đề xuất 2 bước trong `standards/brand_kits/README.md`.

Các hướng chốt (đưa bảng lựa chọn, không hỏi mở):

| Lựa chọn | Khi nào phù hợp |
|---|---|
| Chọn 1 trong 10 preset | User không có brand riêng → lọc theo bối cảnh, đưa 2-3 ứng viên |
| User cung cấp màu/logo | User có brand riêng → tạo `brand_kits/<ten>/brand_kit.json` mới theo schema chuẩn |
| Bóc từ file mẫu khác | User có file cũ của công ty → chạy Track 3 (extract_brand.py) |
| Đen trắng | Tài liệu hành chính hoặc user muốn tối giản → Track 1 hoặc Pandoc |

Nếu user đã có folder brand trong `standards/brand_kits/` từ phiên trước → dùng lại, chỉ cần xác nhận.

---

## 4. Quy tắc map MD → từng định dạng

### MD → DOCX

| Thành phần MD | Thành phần DOCX |
|---|---|
| H1 | Tiêu đề tài liệu / Heading 1 (accent1, font heading) |
| H2, H3 | Heading 2, 3 — hệ phân cấp theo `dynamic_structure/docx-heading-numbering.md` |
| Bảng | Table theo `dynamic_structure/docx-table.md` (header accent1 chữ lt1, zebra lt2) |
| Blockquote | Callout box viền trái accent1, nền lt2 |
| Tài liệu >10 trang | Thêm cover page + TOC + header/footer theo `dynamic_structure/` |

### MD → XLSX

- **Mỗi bảng MD lớn** → 1 sheet riêng, đặt tên theo heading gần nhất.
- **Nhiều bảng nhỏ cùng chủ đề** → chung 1 sheet, cách nhau 2 dòng, mỗi bảng có title row.
- **Cột số** → numFmt phù hợp (`#,##0`, `0.0%`), thêm dòng TỔNG bằng Live Formula nếu cột có tính cộng dồn.
- **Cột % hoặc trạng thái** → conditional formatting / traffic light (accent3-4-2).
- **Văn xuôi ngoài bảng** → KHÔNG nhét vào Excel. Chỉ giữ lại làm sheet "Ghi chú" nếu user yêu cầu, mặc định bỏ qua và báo user biết.
- Nếu content **không có bảng nào** → báo user content này không phù hợp Excel, đề xuất DOCX/PPTX thay thế. Không cố ép.

### MD → PPTX

- **H1** → slide tiêu đề. **Mỗi H2** → 1 slide mới (H3 là block trong slide).
- **Giới hạn ~50-80 từ/slide** — vượt quá thì tách slide hoặc rút gọn thành bullet, KHÔNG copy nguyên đoạn văn dài lên slide.
- **Bảng ≤5 dòng** → giữ dạng bảng. **Bảng >5 dòng hoặc toàn số liệu so sánh** → vẽ chart sống (`addChart`, màu accent1-6).
- **Con số đắt giá** (%, tăng trưởng, tiền) → stat callout 60-72pt.
- **Chuỗi bước** → timeline/process flow. **Cặp đối lập** → layout 2 cột.
- Mỗi slide ≥1 yếu tố thị giác — theo `resources/pptx.md`.
- Kết thúc: slide tóm tắt/CTA nếu content có phần kết luận.

---

## 5. Mẫu Kế hoạch Thiết kế trình user (trước khi vẽ)

Ngắn gọn 5-7 dòng, ví dụ:

> Content có 4 phần (H2), 2 bảng số liệu, 6 con số nổi bật.
> - DOCX: 12 trang, cover + TOC, 2 bảng zebra, 3 callout
> - XLSX: 2 sheet (Ngân sách, Tiến độ), dòng tổng live formula
> - PPTX: 7 slide (1 title, 4 nội dung, 1 chart từ bảng ngân sách, 1 kết)
> - Brand: preset-modern-blue (hoặc anh cho tôi mã màu/logo công ty)
> OK thì tôi chạy.
