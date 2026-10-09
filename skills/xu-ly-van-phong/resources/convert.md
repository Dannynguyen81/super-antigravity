# Chuyển đổi Tài liệu (Convert)

Pipeline chuyển đổi giữa các định dạng.

---

## MD → DOCX (Pandoc + Format)

```powershell
# Bước 1: Pandoc convert
pandoc input.md -o output.docx --markdown-headings=atx -f markdown+raw_attribute --wrap=none

# Bước 2: Post-process (font, margin, heading colors, bullet, code block)
python scripts/extractor/format/format_docx.py output.docx
```

### Nhiều file MD (xuất bản sách)

```powershell
$files = Get-ChildItem "chapters\*.md" | Sort-Object Name
$merged = ($files | ForEach-Object { Get-Content $_ -Raw -Encoding UTF8 }) -join "`n`n"
$merged | Out-File "_merged.md" -Encoding UTF8
pandoc _merged.md -o output.docx
python scripts/extractor/format/format_docx.py output.docx
```

**Lưu ý Track 2:** nếu tài liệu cần mang Brand Kit, ưu tiên đưa content vào Generator Node.js (`template_docx.js`) thay vì Pandoc — Pandoc chỉ phù hợp tài liệu đen trắng hoặc format đơn giản.

---

## PDF → DOCX

| Loại | Cách làm |
|---|---|
| PDF digital | `python scripts/extractor/convert/convert_pdf_to_docx.py input.pdf output.docx` |
| PDF scan | AI Vision phân tích → tái tạo bằng Generator. Xem `pdf.md` |

---

## DOCX → PDF

```powershell
python scripts/extractor/office/soffice.py --headless --convert-to pdf input.docx
```

---

## Dependencies

```
pip install python-docx pdf2docx
winget install pandoc
```
