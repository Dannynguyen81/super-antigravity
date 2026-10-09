# Kỹ năng PPTX — PowerPoint

Hướng dẫn đọc, tạo và kiểm tra slide.

---

## Đọc nội dung

```bash
python -m markitdown presentation.pptx                              # Text extraction
python scripts/extractor/office/unpack.py presentation.pptx unpacked/  # Raw XML
python scripts/extractor/extract_brand.py presentation.pptx --out bk/  # Bóc Brand Kit
```

---

## Tạo slide

| Tình huống | Dùng |
|---|---|
| Có template/file mẫu, chỉ thay nội dung | Unpack → sửa XML → Pack (Extractor toolkit) |
| Tạo mới theo Brand Kit (Track 2) | `pptxgenjs` — khung mẫu: `scripts/generator/template_pptx.js` |

---

## Nguyên tắc thiết kế

- **Mỗi slide cần ít nhất 1 yếu tố thị giác** (image, chart, icon, shape). Slide chỉ text là không chấp nhận.
- **Font lấy từ Brand Kit** (`fonts.heading` / `fonts.body`). Chỉ khi brand kit không có font mới chọn font pairing có cá tính (Georgia/Calibri, Cambria/Calibri...), không default Arial.
- **Cỡ chữ:** Title 36-44pt, section 20-24pt, body 14-16pt, caption 10-12pt.
- **Độ dài tiêu đề slide:** với khổ 13.33" và cỡ 28-30pt, tiêu đề chỉ được ~50-55 ký tự trên 1 dòng. Dài hơn sẽ tràn xuống dòng 2 và đè lên vạch trang trí/subtitle — rút gọn tiêu đề, đẩy phần thừa xuống subtitle.
- **Margin tối thiểu 0.5"**, gap giữa content blocks 0.3-0.5".
- **Không lặp layout** — vary columns, cards, callouts qua các slide.
- **KHÔNG dùng accent line dưới title** — dấu hiệu slide AI tạo.

---

## Layout options

Two-column (text + illustration), icon + text rows, 2x2 / 2x3 grid, half-bleed image + overlay, large stat callouts (số lớn 60-72pt + label nhỏ), timeline / process flow. Chi tiết: `standards/dynamic_structure/pptx-structure.md`.

---

## QA bắt buộc

```bash
python -m markitdown output.pptx                                            # Content check
python scripts/extractor/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide                                      # Visual check
```

Kiểm tra: overlap, text overflow, contrast thấp, spacing không đều, placeholder còn sót.

**Verification loop:** Generate → Convert → Inspect → Fix → Re-verify. Không báo xong trước khi hoàn thành ít nhất 1 chu kỳ fix-and-verify.

---

## Dependencies

```
pip install "markitdown[pptx]" Pillow
npm install pptxgenjs
```
