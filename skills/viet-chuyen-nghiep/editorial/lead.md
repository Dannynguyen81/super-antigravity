# Ban Biên Tập — Trưởng Ban

**Vai trò:** Quản lý viết bài, chọn phong cách, xây dựng câu chuyện. Ban chủ trì chính cho đa số đề bài.

---

## Nhân sự

| Nhân viên | File | Chức năng | Load khi |
|-----------|------|-----------|----------|
| BTV Cốt truyện | story-core.md | Insight + logic + show-tell + vernacular | 🔵 Mặc định |
| BTV Đóng khung | hook-close.md | 4 hook mở + 3 kỹ thuật kết | 🔵 Mặc định |
| BTV Nhịp văn | rhythm.md | 70-20-10, pacing, biến thiên | 🔵 Mặc định |
| BTV Ẩn dụ | metaphor.md | Extended metaphor, compounding, loop | ⚪ Tùy chọn |
| BTV Lật góc | reframe.md | Concept naming, paradox flip, parallel analogy | ⚪ Tùy chọn |
| BTV Phản bác | debunk.md | Structured debunk, gentle debunk, commentary | ⚪ Tùy chọn |
| BTV Nhấn mạnh | emphasis.md | Reframing, tách dòng, strategic caps | ⚪ Tùy chọn |
| BTV Học thuật | technical.md | Viết kỹ thuật/academic | ⚪ Thay thế |

## Giao việc

```
Khi nhận nhiệm vụ:
1. Loại bài nào?
   ├── Blog / storytelling
   │    → story-core + hook-close + rhythm (MẶC ĐỊNH, song song)
   │    ├── + Cần ẩn dụ sâu?        → + metaphor
   │    ├── + Cần đặt tên/lật góc?  → + reframe
   │    ├── + Cần phản bác?         → + debunk
   │    └── + Cần nhấn mạnh?        → + emphasis
   │
   └── Tài liệu kỹ thuật
        → technical (THAY THẾ story-core + rhythm)
        ⚠️ technical KHÔNG dùng chung với story-core

2. Ước lượng độ dài?
   ├── Ngắn (< 1.500 ký tự)    → Viết liền 1 lượt
   ├── Trung bình (1.500-5.000) → Viết liền, kiểm tra từng phần
   └── Dài (> 5.000)           → BẮT BUỘC Outline-First
       → Viết từng phần, mỗi lượt chỉ load 1-2 nhân viên
```

## Cam kết hoàn thành

Nhiệm vụ HOÀN THÀNH khi:
- [ ] Bài viết có core insight rõ ràng
- [ ] Logic chain flow tự nhiên A → B → C
- [ ] Phân bố đoạn văn theo 70-20-10 (nếu storytelling)
- [ ] Kỹ thuật nâng cao được áp dụng đúng (nếu có)

## Hợp đồng ban giao

- Nhận input từ: Ban Thu thập (Content Brief) hoặc Tổng biên tập (đề bài trực tiếp)
- Giao output cho: Ban Xuất bản (nếu cần format) hoặc Ban Kiểm duyệt (quality/)
- Khi bị quality/ từ chối vì lỗi nội dung: sửa theo phiếu từ chối, giao lại

### Hành động bàn giao (GATE)

Khi cam kết hoàn thành đạt:
1. Viết bài vào file `[tên-bài]-draft.md`
2. DỪNG — không load ban tiếp theo
3. Ghi log: "Editorial → [ban tiếp theo], sản phẩm: [tên file]"
4. SAU ĐÓ mới load lead.md của ban tiếp theo
