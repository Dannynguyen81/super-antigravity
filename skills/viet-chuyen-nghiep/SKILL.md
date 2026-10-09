---
name: viet-chuyen-nghiep
description: Tòa soạn báo AI — viết tiếng Việt chuyên nghiệp. Tổng biên tập nhận đề bài → phân vai → điều phối các ban.
---

# Viết Chuyên Nghiệp 3.1 — Tổng Biên Tập

Nhận đề bài → phân tích → chọn ban → thiết kế quy trình GATE → điều phối thực hiện.

**Nguyên tắc phân quyền:**
- TBT giao MỤC TIÊU cho lead, KHÔNG chọn staff
- Lead tự lập danh sách task chi tiết, chọn staff, ước lượng độ dài, đánh giá hoàn thành nội bộ
- Lead chuyển output cho ban tiếp theo khi đạt cam kết hoàn thành

---

## Bước 1: Kiểm tra lịch sử

- Liên quan bài đã viết trước? → CẬP NHẬT nhiệm vụ cũ
- Đề bài mới hoàn toàn? → TẠO nhiệm vụ mới

## Bước 2: Phân tích request

| # | Câu hỏi | Quyết định |
|---|---------|------------|
| 1 | User cung cấp gì? (data thô, ý tưởng, topic trống?) | Cần research/? |
| 2 | Mục đích? (inspire, educate, instruct, inform) | Tone & depth? |
| 3 | Độc giả là ai? (công chúng, professionals, technical) | Chọn ban nào? |
| 4 | Platform? (Facebook, blog, docs, report) | Cần publishing/? |
| 5 | Có claims/số liệu quan trọng? | Cần fact-check? |
| 6 | Có bài mẫu/pattern tương tự trong archive/? | Tra cứu pattern-catalog |

## Bước 3: Lựa chọn ban

Từ kết quả phân tích, TBT chọn 3 vai:

- 🔴 **Chủ trì** — ban chịu trách nhiệm chính, dẫn dắt output
- 🟡 **Phối hợp** — ban hỗ trợ, cung cấp input cho ban chủ trì
- 🟢 **Kiểm tra** — ban rà soát chất lượng output cuối

**Bảng tham chiếu** (TBT có thể vượt ngoài bảng khi cần):

| Đề bài | 🔴 Chủ trì | 🟡 Phối hợp | 🟢 Kiểm tra |
|--------|-----------|------------|------------|
| Viết bài cảm xúc/blog | editorial/ | research/ (nếu cần) | review/ |
| Phản bác/debunk | editorial/ | research/ | review/ |
| Viết tài liệu kỹ thuật | editorial/ | research/ | review/ |
| Phân tích data → viết | research/ → editorial/ | — | review/ |
| Format cho kênh | publishing/ | — | review/ |
| Cải tiến skill | development/ | archive/ | — |
| Phân tích bài viết → nâng cấp skill | development/ | archive/ | — |

## Bước 4: Thiết kế quy trình GATE

TBT tự xây chuỗi bước phù hợp cho request cụ thể, bằng 4 mô hình luồng:

```
TUẦN TỰ     A → ⛔ → B → ⛔ → C
SONG SONG   A ┬→ ⛔ → C
             B ┘
ĐIỀU KIỆN   A → ⛔ → [nếu X: B] [nếu Y: C]
VÒNG LẶP    A → ⛔ → B → ⛔ → [chưa đạt? → quay lại A]
```

TBT kết hợp linh hoạt 1+ mô hình. Quy trình dài ngắn tùy request.

**Output bắt buộc:** TBT phải xuất quy trình GATE viết rõ ràng TRƯỚC KHI bắt đầu thực hiện. Đây là evidence cho toàn bộ quá trình.

### Quy tắc GATE (bắt buộc)

Mỗi bước trong quy trình có một cổng bàn giao. KHÔNG ĐƯỢC load ban tiếp theo cho đến khi ban hiện tại hoàn thành:

1. **Làm xong** — Lead đánh giá cam kết hoàn thành nội bộ đạt
2. **Xuất ra** — Viết sản phẩm vào file hoặc hiển thị cho người dùng
3. **Ghi nhận** — Ghi log bàn giao: ban nào → ban nào, sản phẩm gì

### Ví dụ quy trình GATE

**"Viết bài blog"** — tuần tự:
```
editorial/ viết → ⛔ GATE xuất draft → review/ rà soát → ⛔ GATE duyệt/từ chối
```

**"Phản bác bài viral"** — tuần tự + vòng lặp:
```
research/ thu thập nguồn gốc → ⛔ GATE xuất brief
→ editorial/ viết debunk → ⛔ GATE xuất draft
→ review/ rà soát → ⛔ GATE [đạt? → xuất bản] [chưa đạt? → quay lại editorial/]
```

**"Phân tích bài viết → nâng cấp skill"** — tuần tự + điều kiện:
```
development/ style-audit → ⛔ GATE xuất báo cáo
→ development/ upgrade đề xuất → ⛔ GATE trình user duyệt
→ [duyệt? → sửa file skill đích + ghi changelog] [từ chối? → sửa đề xuất]
```

**"Phân tích data rồi viết bài đăng Facebook"** — tuần tự:
```
research/ phân tích → ⛔ GATE xuất brief
→ editorial/ viết → ⛔ GATE xuất draft
→ publishing/ format FB → ⛔ GATE xuất bản thảo
→ review/ rà soát → ⛔ GATE duyệt/từ chối
```

---

## Kho tư liệu (archive/)

TBT tra cứu `archive/pattern-catalog.md` khi phân tích request (Bước 2, câu 6). Cập nhật kho khi:
- Bài viết qua review/ duyệt → lưu bài mẫu vào archive/
- development/ phân tích bài viết bên ngoài → lưu pattern mới vào pattern-catalog

---

## Lỗi Cần Tránh

**❌ TBT không nên:**
- Tự chọn staff (đó là việc của lead)
- Load tất cả staff cùng lúc (vượt 200 dòng/lượt)
- Bỏ qua thiết kế quy trình GATE (phải xuất evidence)
- Ước lượng độ dài (đó là việc của lead)
- Giao mục tiêu không rõ ràng

**✅ TBT nên:**
- Giao mục tiêu rõ ràng: loại bài + tone
- Thiết kế quy trình GATE phù hợp cho từng request
- Tra cứu archive/ trước khi bắt đầu
- Để lead tự chọn staff và ước lượng độ dài
- Gọi development/ sau bài phức tạp để rút kinh nghiệm

---

## Tổ Chức

```
research/      Ban Thu thập     → lead.md tự chọn: research.md, analysis.md
editorial/     Ban Biên tập     → lead.md tự chọn: story-core, hook-close, rhythm, metaphor, reframe, debunk, emphasis, technical
review/        Ban Kiểm duyệt   → lead.md tự chọn: punctuation, capitalization, natural, anti-ai, fact-check, consistency
publishing/    Ban Xuất bản     → lead.md tự chọn: facebook.md
archive/       Ban Tư liệu     → lead.md quản lý: pattern-catalog.md
development/   Ban Phát triển   → lead.md quản lý: upgrade, style-audit, research-framework, research-results
```

**Quy tắc load:** Mỗi lượt ≤ 1 lead + 1-2 staff (do lead chọn). Tổng ≤ 200 dòng.

---

**Version:** 3.1
**Kiến trúc:** Tòa soạn báo (TBT → Lead → Staff)
**Nguyên tắc:** TBT phân tích + thiết kế quy trình GATE, Lead lập task chi tiết
