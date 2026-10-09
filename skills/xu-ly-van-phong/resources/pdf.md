# Kỹ năng PDF — Xử lý cục bộ

Mọi xử lý PDF chạy local, **không upload lên cloud** (bảo mật dữ liệu).

---

## Hai loại PDF

| Loại | Nhận dạng | Cách xử lý |
|---|---|---|
| **PDF digital** (text-based) | Select được text | Script: pypdf, pdfplumber |
| **PDF scan** (image-based) | Không select được text | OCR hoặc AI Vision |

---

## Thao tác PDF digital

| Thao tác | Công cụ |
|---|---|
| Ghép / tách / xoay trang / mật khẩu | `pypdf` |
| Trích text | `pypdf` hoặc `pdfplumber` |
| Trích bảng | `pdfplumber` (tốt hơn pypdf cho bảng) |

---

## Chuyển đổi PDF → DOCX

| Loại PDF | Phương pháp |
|---|---|
| PDF digital | `python scripts/extractor/convert/convert_pdf_to_docx.py input.pdf output.docx` (dùng `pdf2docx`, giữ layout gốc) |
| PDF scan | AI Vision phân tích cấu trúc + màu sắc → tái tạo bằng Generator (Track 2) |

Khi tái tạo từ PDF scan, phân tích đầy đủ:

- **Cấu trúc**: heading hierarchy, table layout, bullet indentation — map vào `standards/dynamic_structure/`
- **Màu sắc**: header, fill, text — ghi thành `brand_kit.json` theo schema chuẩn rồi đưa vào Generator

---

## Dependencies

```
pip install pypdf pdfplumber pdf2docx
```
