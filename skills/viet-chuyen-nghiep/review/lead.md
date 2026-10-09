# Ban Kiểm Duyệt — Trưởng Ban

**Vai trò:** Cửa cuối cho TẤT CẢ sản phẩm — kiểm soát cả nội dung lẫn hình thức xuất bản. Không có gì ra ngoài mà chưa qua ban này.

---

## Nhân sự

| Nhân viên | File | Chuyên môn | Bắt buộc? |
|-----------|------|------------|-----------|
| BTV dấu câu | punctuation.md | Dấu câu, spacing, dấu hai chấm, Oxford comma | 🔴 Bắt buộc |
| BTV viết hoa | capitalization.md | Viết hoa, tiêu đề, phân cấp heading | 🔴 Bắt buộc |
| BTV văn phong | natural.md | Văn phạm tự nhiên, format, ký hiệu nối câu | 🔴 Bắt buộc |
| BTV phát hiện AI | anti-ai.md | Dấu hiệu AI, pattern cấm, self-check | 🔴 Bắt buộc |
| Kiểm chứng viên | fact-check.md | Số liệu, trích dẫn, claims | ⚪ Tùy chọn |
| BTV nhất quán | consistency.md | Tone, thuật ngữ, xung đột quy tắc | 🔵 Mặc định |

## Giao việc

```
Khi nhận bài từ ban chủ trì:
1. SONG SONG (không phụ thuộc nhau):
   ├── punctuation.md
   ├── capitalization.md
   ├── natural.md
   ├── anti-ai.md
   └── fact-check.md (nếu có số liệu)
2. CUỐI CÙNG (cần toàn bộ bài):
   └── consistency.md

Bài dài → rà soát từng phần:
├── Chia bài theo đoạn (cách dòng trống)
├── Mỗi đoạn: chạy punctuation + capitalization + natural + anti-ai
└── Sau khi hết đoạn: chạy consistency cho toàn bài
```

## Cam kết hoàn thành

Nhiệm vụ HOÀN THÀNH khi TẤT CẢ đều đạt:
- [ ] Không vi phạm punctuation.md
- [ ] Không vi phạm capitalization.md
- [ ] Không vi phạm natural.md
- [ ] Không có dấu hiệu AI (anti-ai.md)
- [ ] Số liệu đã kiểm chứng (nếu có fact-check)
- [ ] Tone và thuật ngữ nhất quán (consistency.md)
- [ ] Format đúng kênh xuất bản (nếu đã qua platform/)

## Vòng lặp từ chối

```
Kiểm tra xong:
├── ✅ TẤT CẢ đạt → THÔNG QUA → xuất bản
└── ❌ Có lỗi → Lập PHIẾU TỪ CHỐI:
        - Lý do: [trích dẫn câu/đoạn lỗi cụ thể]
        - Loại lỗi: Nội dung / Hình thức / Số liệu
        - Mức độ: Nhẹ (sửa vài chỗ) / Nặng (viết lại đoạn)
        - Vòng: Lần [1/2]
        - Trả về ban tương ứng
        - Tối đa 2 vòng → vẫn lỗi → báo Tổng biên tập
```

## Hợp đồng ban giao

- Nhận input từ: Ban Biên tập (bài viết) hoặc Ban Xuất bản (bài đã format)
- Giao output: XUẤT BẢN (thông qua) hoặc trả lại ban gây lỗi (từ chối)

### Hành động bàn giao (GATE)

Khi duyệt xong:
- ✅ Thông qua: Ghi log "Review DUYỆT", xuất bài hoàn chỉnh vào file `[tên-bài].md`
- ❌ Từ chối: Lập phiếu từ chối (theo vòng lặp), ghi log "Review TỪ CHỐI → [ban gây lỗi]"
