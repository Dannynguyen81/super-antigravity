# Tài liệu Hướng dẫn: Chiều Đọc & Bóc tách (The Extractor)

Hướng dẫn bóc tách Dữ liệu (Content) và Giao diện (Brand Kit) từ một file Office mẫu.

---

## 1. Nguyên lý Bóc tách XML (Unpack XML)

Mọi file `.docx`, `.xlsx`, `.pptx` bản chất là một file nén zip. Thay vì chỉ dùng `python-docx` (chỉ đọc được chữ), Agent giải nén file để vào tầng đáy OOXML lấy cấu trúc chuẩn xác nhất.

```bash
# Unpack file để xem XML thô
python scripts/extractor/office/unpack.py input.docx unpacked/

# Pack lại sau khi sửa (giữ nguyên format gốc, chỉ thay nội dung)
python scripts/extractor/office/pack.py unpacked/ output.docx

# Validate file sau khi pack
python scripts/extractor/office/validate.py output.docx
```

---

## 2. Bóc tách Brand Kit (UI/Theme)

Dùng script có sẵn — KHÔNG tự viết lại:

```bash
python scripts/extractor/extract_brand.py file_mau.docx --out standards/brand_kits/ten_doanh_nghiep
```

Script tự động: đọc `theme1.xml` (Word/PPT/Excel đều hỗ trợ), bóc 10 màu theme + 2 font, trích toàn bộ ảnh từ `media/` vào `assets/`, lưu `brand_kit.json`.

### Schema chuẩn của `brand_kit.json` (DUY NHẤT — mọi script phải theo)

```json
{
  "company_name": "TenDoanhNghiep",
  "colors": {
    "dk1": "000000",
    "lt1": "FFFFFF",
    "dk2": "333333",
    "lt2": "F8F9FA",
    "accent1": "C22620",
    "accent2": "D4AF37",
    "accent3": "2E75B6",
    "accent4": "548235",
    "accent5": "BF8F00",
    "accent6": "2F5597"
  },
  "fonts": { "heading": "Inter", "body": "Inter" },
  "assets": { "logo": "assets/logo.png" }
}
```

### Ý nghĩa từng khóa màu (theo chuẩn OOXML)

| Khóa | Vai trò | Dùng cho |
|---|---|---|
| `dk1` | Text chính | Chữ body trên nền sáng |
| `lt1` | Nền chính | Background trang/slide |
| `dk2` | Text phụ | Chữ phụ, caption, subtitle |
| `lt2` | Nền phụ nhạt | Callout box, zebra row, header nhạt |
| `accent1` | Màu chủ đạo brand | Heading 1, header bảng, nút chính |
| `accent2` | Màu nhấn phụ | Heading 2, đường viền, điểm nhấn |
| `accent3`–`accent6` | Màu bổ trợ | Series biểu đồ, traffic light |

**Lưu ý:** `assets.logo` có thể vắng mặt (file mẫu không có ảnh). Generator phải kiểm tra tồn tại trước khi nhúng.

**Giới hạn của theme1.xml:** Nhiều file mẫu tô màu bằng formatting trực tiếp, KHÔNG khai trong theme — khi đó `extract_brand.py` chỉ bóc được theme Office mặc định (nhận biết: accent1=4F81BD, dk2=1F497D). Gặp trường hợp này, bóc màu thật bằng cách đếm tần suất trong `document.xml`:

```bash
unzip -p file_mau.docx word/document.xml | grep -oP '(w:color w:val|w:fill)="[0-9A-Fa-f]{6}"' | sort | uniq -c | sort -rn | head -10
```

Rồi tự map vào schema: màu fill/heading xuất hiện nhiều nhất → `accent1`, nền nhạt lặp lại → `lt2`, xám chữ phụ → `dk2`.

---

## 3. Bóc tách Tài nguyên Vật lý (Assets)

- **Hình ảnh:** `extract_brand.py` tự trích toàn bộ ảnh từ `word/media/` hoặc `ppt/media/` vào `assets/`. Sau khi chạy, Agent xem thư mục `assets/` và tự nhận diện file nào là logo, cập nhật lại `assets.logo` trong JSON nếu script chọn sai.
- **Sơ đồ/Biểu đồ:** Không copy XML chết. Cào Data thô (con số, chữ) trong sơ đồ và ghi nhận loại biểu đồ (Bar, Pie, Phân cấp). Đưa Data này sang Chiều Ghi để dùng Node.js vẽ lại.

---

## 4. Bóc tách Content (Text, Bảng, Số liệu)

| Cần lấy | Công cụ |
|---|---|
| Text thô toàn文 | `python -m markitdown input.docx` (hoặc .pptx/.xlsx) |
| Cấu trúc chính xác (style, run) | Unpack XML rồi đọc `document.xml` |
| Số liệu + công thức Excel | `openpyxl` với `data_only=False` để giữ công thức |
| Bảng trong PDF digital | `pdfplumber` |
