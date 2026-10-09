# Trang bìa (Cover Page)

Các mẫu trang bìa theo loại văn bản.

---

## Bìa hiện đại với Brand Kit (khuyến nghị cho Track 2)

Bìa căn giữa thuần chữ trông "máy móc". Bìa hiện đại dùng khối màu và căn trái để tạo cảm giác được thiết kế:

| Vị trí | Thành phần | Cách làm trong docx-js |
|---|---|---|
| Đỉnh trang | Băng màu accent1 mỏng full-width | Table 1 hàng 1 ô, fill accent1, không border, cao ~0.15-0.2 cm |
| 1/3 trang | Kicker line: "LOẠI TÀI LIỆU · ĐỊA ĐIỂM · NĂM" | 10-11pt bold, màu accent2, căn trái |
| Giữa | TIÊU ĐỀ LỚN | 36-44pt bold, màu accent1, căn trái, được phép xuống 2 dòng |
| Dưới tiêu đề | Vạch nhấn ngắn màu accent phụ | Table cell fill, rộng ~1/6 trang, cao ~0.1 cm |
| | Subtitle + tagline | 14-16pt màu dk2, tagline italic |
| 2/3 trang | Khối thông tin chính | Table 2 cột không border, fill lt2: nhãn bold accent2 + giá trị |
| Đáy trang | Băng accent1 chứa liên hệ | Table 1 ô fill accent1, chữ lt1 |

Nguyên tắc: bìa KHÔNG dùng first-line indent, không justify; tối đa 3 màu; khoảng trắng chiếm ít nhất 40% trang.

---

## Bìa VB ngắn / trung bình (đề xuất, báo cáo)

Thứ tự từ trên xuống:

| Vị trí | Nội dung | Style |
|---|---|---|
| Spacer | Đẩy tiêu đề xuống giữa trang | ~1800 DXA |
| Dòng 1 | TIÊU ĐỀ CHÍNH | Bold 24pt, center |
| Dòng 2 | (trống) | |
| Dòng 3 | Phụ đề hoặc mô tả ngắn | Italic 14pt, center |
| Dòng 4 | Đường viền trên + dưới (tạo khung) | Border cùng màu heading |
| Spacer | | ~900 DXA |
| Dòng 5 | PHẠM VI ÁP DỤNG | Bold 12pt caps, center |
| Dòng 6 | Tên đơn vị tiếp nhận | Bold 16pt, center |
| Spacer | | ~480 DXA |
| Dòng 7 | LĨNH VỰC TRỌNG TÂM | Bold 12pt caps, center |
| Dòng 8 | Mô tả phạm vi | Bold 13pt, center |
| Dòng 9 | Mô tả phụ | Italic 11pt, center |
| | **Page Break** | |

---

## Bìa VB dài / kỹ thuật (thuyết minh, nghiên cứu)

| Vị trí | Nội dung | Style |
|---|---|---|
| Dòng 1 | Header 2 cột (xem `header-footer.md`) | Bảng vô hình |
| Khoảng trống | 3-5 dòng | |
| Trung tâm 1 | Loại tài liệu (VD: "THUYẾT MINH") | Bold 20pt, center |
| Trung tâm 2 | Tên dự án / đồ án | Bold 16pt, center |
| Trung tâm 3 | Tên phụ | Bold 14pt, center |
| Khoảng trống | 2-3 dòng | |
| Địa điểm | ĐỊA ĐIỂM: ... | Regular 10pt, center |
| Cuối trang | Năm lập | Regular 12pt, center |

---

## Nguyên tắc chung

- Trang bìa là ấn tượng đầu tiên — luôn đầu tư thiết kế.
- Luôn có Page Break sau bìa.
- Tiêu đề lớn (24pt+) căn giữa.
- Phụ đề italic, cỡ nhỏ hơn.
- **Màu sắc**: xem `standards/color/`. Mặc định đen trắng vẫn đủ chuyên nghiệp nếu có đường viền và spacing tốt.
