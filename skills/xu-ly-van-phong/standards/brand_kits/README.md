# Thư viện Brand Kit Preset

10 bộ phối màu sẵn dùng khi user KHÔNG có file mẫu/brand riêng. Mỗi folder chứa `brand_kit.json` theo schema chuẩn (xem `resources/extractor_docs.md`).

**Quy ước quan trọng:** `dk1` luôn là MÀU CHỮ CHÍNH, `lt1` luôn là MÀU NỀN CHÍNH — vai trò cố định. Ở preset tối, dk1 là màu sáng và lt1 là màu tối.

---

## Bảng chọn theo tông màu

| Preset | Sáng/Tối | Nhiệt độ | Phong cách | Hợp với |
|---|---|---|---|---|
| `preset-formal-navy` | Sáng | Lạnh | Cổ điển trang trọng | Đề xuất chiến lược, tập đoàn, gửi lãnh đạo |
| `preset-modern-blue` | Sáng | Lạnh | Hiện đại | Startup, SME, quy trình nội bộ |
| `preset-editorial-burgundy` | Sáng | Nóng | Editorial | Review, phản biện, phân tích chuyên sâu |
| `preset-classic-ivory` | Sáng | Ấm trung tính | Cổ điển | Sách, chứng chỉ, thư ngỏ, di sản |
| `preset-warm-earth` | Sáng | Nóng | Mộc mạc ấm | F&B, thủ công, giáo dục, cộng đồng |
| `preset-vibrant-coral` | Sáng | Nóng | Năng động | Marketing, sự kiện, sản phẩm trẻ |
| `preset-fresh-nature` | Sáng | Mát | Tươi mới | Nông nghiệp, sức khỏe, môi trường |
| `preset-neutral-minimal` | Sáng | Trung tính | Tối giản | Kiến trúc, luật, tư vấn, kỹ thuật |
| `preset-dark-tech` | **Tối** | Lạnh | Hiện đại công nghệ | Slide AI, sản phẩm số, demo tech |
| `preset-luxury-dark-gold` | **Tối** | Ấm | Sang trọng | Bìa sách, pitch deck cao cấp, premium |

---

## Cách đề xuất với user

Không hỏi mở "anh thích màu gì". Hỏi bằng 2 bước lọc:

1. **Bối cảnh tài liệu?** (trang trọng / doanh nghiệp hiện đại / sáng tạo / kỹ thuật) → lọc còn 2-3 preset
2. **Đưa 2-3 preset ứng viên** kèm 1 dòng mô tả mỗi bộ → user chọn

Với slide thuyết trình có thể gợi ý thêm cặp Sáng/Tối (phòng họp sáng → nền sáng; trình chiếu sân khấu → nền tối).

## Quy tắc

- `example/` là brand kit GIẢ ĐỊNH (CongTyABC) — CHỈ dùng test script, CẤM dùng cho tài liệu user thật.
- User có brand riêng → tạo folder mới theo tên doanh nghiệp (bóc bằng `extract_brand.py` hoặc nhập tay màu/logo user cung cấp), không sửa preset.
- Preset dùng font hệ thống Windows phổ biến (Times New Roman, Georgia, Arial, Calibri, Segoe UI, Verdana) — không cần cài thêm.
