---
id: KH-2026-10-harness-patterns
title: Kế hoạch triển khai - áp dụng mẫu harness vào SUPER-ANTIGRAVITY (nhóm A + B)
version: 1.0
status: draft
author: Claude Code (phiên cloud)
approver: Chủ repo (Dannynguyen81)
tags: [harness, hook, an-toan, antigravity, ke-hoach]
---

# Kế hoạch triển khai: áp dụng mẫu harness (nhóm A + B)

> **Dành cho Antigravity.** Tệp này tự đủ để Antigravity xác minh các giả định trên môi trường thật, triển khai và kiểm thử. Theo quy tắc mục 5 trong `AGENTS.md`: **chỉ triển khai sau khi chủ repo phê duyệt rõ ràng.** Mục "Cần quyết" ở cuối chưa có câu trả lời, nên dùng mặc định được ghi kèm.

- **Nguồn ý tưởng**: bài "12 Agentic Harness Patterns From Claude Code" của Bilgin Ibryam (đăng lại từ *The Generative Programmer*, 10/10/2026). Đây là bản tổng hợp của tác giả; nội bộ Claude Code chưa được kiểm chứng.
- **Nhánh làm việc**: `claude/dreamy-newton-rxfm6g` (đã đồng bộ `main`).
- **Lệnh kiểm thử toàn bộ**: `python3 -m unittest discover -s tests` (phải xanh trước và sau mỗi giai đoạn; hiện 59 test).
- **Ràng buộc**: chỉ dùng thư viện chuẩn Python; không chạy lệnh phá hoại thật khi thử (chỉ dùng chuỗi lệnh giả); không sửa `plugins/ppt-master-plugin/` (cổng toàn vẹn của upstream sẽ hỏng).

## 0. Việc phải làm trước: xác minh giả định trên Antigravity thật

Mã hiện có (`plugins/antigravity-autoharness-plugin/hooks.json`, `src/safety_gate.py`) dựa trên các giả định chưa kiểm chứng. Antigravity ghi kết quả từng mục vào `30-working/ket-qua-xac-minh-harness.md` (Đạt / Không đạt / Không rõ + bằng chứng: lệnh đã chạy, kết quả thực tế).

| Mã | Giả định | Cách thử (không gây hại) | Nếu sai |
| :-- | :--- | :--- | :--- |
| V1 | Hook `PreToolUse` nhận payload JSON qua stdin; lệnh nằm ở `toolCall.args.CommandLine` | Ghi tạm một hook in nguyên payload ra tệp, cho agent chạy `echo xin-chao`, đọc tệp | Sửa `extract_command` theo payload thật |
| V2 | Mã thoát `1` làm Antigravity từ chối lệnh | Cho agent chạy `echo format C: la-chuoi-thu` (phải qua) rồi dùng payload giả qua `python src/safety_gate.py` (phải thoát 1). Với lệnh thật: dùng một luật thử nghiệm chặn từ khóa vô hại `CHAN_THU_123` | Tìm quy ước chặn đúng (mã khác, hoặc JSON trên stdout) |
| V3 | Cú pháp đăng ký lồng `matcher` + `hooks` hoạt động cho `PreToolUse` | Xem hook V1 có được gọi không | Đổi sang dạng phẳng như `PreInvocation` |
| V4 | `matcher: "*"` áp dụng được cho `PreToolUse` | Đăng ký hook ghi nhật ký với `*`, cho agent đọc và ghi một tệp thử | Dùng danh sách matcher cụ thể |
| V5 | Tên công cụ ghi tệp (đoán: `write_to_file`, `replace_file_content`, `multi_replace_file_content`) | Từ payload V1/V4, ghi lại tên công cụ thật khi agent sửa tệp | Cập nhật `plan_gate.json` mặc định |
| V6 | Hook có thể báo "hỏi người dùng" thay vì chặn hẳn | Đọc tài liệu Antigravity về hook, thử phản hồi JSON | Giữ thiết kế "chặn + phê duyệt qua script" |

**Quy tắc quyết định**: nếu V1–V3 không đạt, **dừng**, báo chủ repo, không triển khai A1–A3. B4–B6′ không phụ thuộc hook nên vẫn làm được.

## Giai đoạn A – Hook an toàn và quan sát được

Tất cả trong `plugins/antigravity-autoharness-plugin/` trừ khi ghi khác.

### A1. Quan sát hook (mẫu 12)
- **Mới** `src/gate_audit.py`: hàm `log_decision(workspace_root, hook, decision, rule_id, command)`; mỗi lần ghi một dòng JSON vào `.agents/autoharness/gate-audit.jsonl` với các trường `ts` (ISO 8601), `hook`, `decision` (`allow`/`deny`/`ask`), `rule_id`, `command` (cắt 200 ký tự, đã lọc bí mật bằng `src/redact.py`). Mọi lỗi ghi log phải bị nuốt (không đổi quyết định của cổng).
- **Mới** `scripts/harness_doctor.py`: kiểm tra (1) `hooks.json` là JSON hợp lệ, (2) có `PreToolUse` trỏ tới `src/safety_gate.py` và tệp tồn tại, (3) chạy thử một payload chặn (mong đợi mã thoát 1) và một payload qua (mong đợi 0), (4) in trạng thái `plan_gate`. Thoát 0 nếu đạt hết, 1 nếu có lỗi; in từng bước dạng `[OK]`/`[LỖI]`.
- **Sửa** `.gitignore`: thêm `.agents/autoharness/gate-audit.jsonl`, `.agents/autoharness/approvals.json`, `.agents/autoharness/plan-approved.json`.

### A2. Phân loại rủi ro 3 mức (mẫu 10)
- **Mới** `safety_rules.json`: danh sách `{"id","level","pattern","message"}`, `level` là `deny` hoặc `ask`. Chuyển nguyên 5 luật `deny` hiện có trong `src/safety_gate.py` (`unix-root-delete`, `filesystem-format`, `raw-disk-overwrite`, `windows-drive-format`, `windows-root-delete`). Thêm luật `ask`:
  - `git-force-push`: `git push` kèm `--force` hoặc `-f` (không tính `--force-with-lease`)
  - `git-hard-reset`: `git reset --hard`
  - `pipe-to-shell`: `curl` hoặc `wget` có `|` tới `sh`/`bash`
  - `chmod-777-recursive`: `chmod -R 777`
  - `sql-drop`: `DROP TABLE` hoặc `DROP DATABASE`
- **Sửa** `src/safety_gate.py`: nạp luật từ JSON (hỏng hoặc thiếu thì dùng bản luật cứng trong mã). `deny` chặn (thoát 1, thông báo `BỊ CHẶN`). `ask` chặn với thông báo `CẦN XÁC NHẬN` kèm mã luật, **trừ khi** `.agents/autoharness/approvals.json` có phê duyệt `allow` còn hạn cho mã luật đó. Mọi quyết định gọi `gate_audit.log_decision`. Giữ nguyên cách xử lý lỗi (JSON hỏng, payload quá 1 MiB: cho qua).
- **Mới** `scripts/harness_approve.py` (chỉ thư viện chuẩn):
  - `allow <mã_luật> --minutes N` (mặc định 10, tối đa 60): ghi `approvals.json` dạng `{"allow": {"<mã_luật>": {"expires_at": "<ISO>"}}}`.
  - `plan "<tên kế hoạch>" --hours N` (mặc định 4, tối đa 24): ghi `plan-approved.json` dạng `{"plan": "...", "approved_at": "...", "expires_at": "..."}`.
  - `status`: in các phê duyệt còn hạn. `revoke`: xóa hết.
  - Ghi tệp nguyên tử (ghi tệp tạm rồi đổi tên).

### A3. Ép Explore-Plan-Act (mẫu 6) - tùy chọn, mặc định tắt
- **Mới** `src/plan_gate.py`: hook `PreToolUse`. Đọc `.agents/autoharness/plan_gate.json` `{"enabled": false, "write_tools": [...]}`. Tắt hoặc thiếu tệp: thoát 0 ngay. Bật: nếu tên công cụ trong `toolCall.name` thuộc `write_tools` mà không có `plan-approved.json` còn hạn thì thoát 1 với thông báo `CHƯA CÓ KẾ HOẠCH ĐƯỢC PHÊ DUYỆT` và hướng dẫn chạy `python scripts/harness_approve.py plan "<tên>"`. Công cụ đọc luôn qua. Ghi `gate_audit`.
- **Mới** `.agents/autoharness/plan_gate.json` với `enabled: false` và `write_tools` lấy từ kết quả V5 (mặc định đoán: `write_to_file`, `replace_file_content`, `multi_replace_file_content`).
- **Sửa** `hooks.json`: thêm mục `PreToolUse` thứ hai `matcher: "*"` chạy `python src/plan_gate.py` (theo kết quả V3/V4).
- **Lưu ý thiết kế**: phê duyệt do **người dùng** chạy script; agent không nên tự tạo `plan-approved.json` (quy tắc này ghi trong `README` của plugin).

## Giai đoạn B – Quy tắc và ngữ cảnh

### B4. Chỉ dẫn theo thư mục (mẫu 2)
- **Mới** `AGENTS.md` và `AGENTS.en.md` (mỗi file ≤ 25 dòng, link qua lại) trong `40-knowledge/`, `30-working/`, `50-outputs/`:
  - `40-knowledge/`: không ghi trực tiếp; bản thảo qua `10-inbox/` hoặc `30-working/`; chỉ thăng cấp khi `status: approved` và có người duyệt.
  - `30-working/`: dùng mẫu trong `_templates/`; frontmatter bắt buộc; ghi `status: draft`.
  - `50-outputs/`: chỉ chứa sản phẩm đã hoàn chỉnh; ghi rõ nguồn trong `40-knowledge/`.
- **Sửa** `AGENTS.md` và `AGENTS.en.md` gốc: thêm mục ngắn "Phạm vi chỉ dẫn" (chỉ dẫn trong thư mục con bổ sung và ưu tiên hơn chỉ dẫn gốc cho tệp trong thư mục đó). Giữ số mục `##` của hai bản bằng nhau (test đồng bộ).

### B5. Bảng nén lũy tiến (mẫu 5)
- **Sửa** `.agents/rules/strategic-compaction.md`: thêm bảng 3 mức - **Gần** (vài lượt gần nhất: giữ nguyên chi tiết), **Cũ** (tóm tắt nhẹ: quyết định và kết quả), **Rất cũ** (gộp mạnh: một dòng mỗi giai đoạn) - và mục "Luôn giữ": quyết định đã chốt, trạng thái hiện tại, kế hoạch đã được duyệt.

### B6′. Chỉ mục quy tắc sạch (mẫu 3)
- **Sửa** `src/admission_promoter.py`, hàm `get_skills_summary_index`: gộp khoảng trắng và xuống dòng của mô tả thành một dòng, bỏ thẻ `<USER_REQUEST>`, cắt tại ranh giới từ theo `INDEX_DESC_MAX_CHARS`. **Không** đổi nội dung các tệp `learned-rule-*`. Không thêm `MEMORY.md` (chỉ mục đã có sẵn).

### Chung
- `NOTICE.md`: ghi công bài của Bilgin Ibryam.
- `plugins/antigravity-autoharness-plugin/README.md`: mô tả A1–A3, hai script, và cách bật/tắt `plan_gate`.

## Kiểm thử bắt buộc

Tất cả trong `tests/` (thư viện chuẩn `unittest`, chỉ dùng payload và lệnh giả). Mục tiêu: **toàn bộ test cũ vẫn xanh**, cộng các test mới sau.

| Nhóm | Ca kiểm thử |
| :--- | :--- |
| A1 | Log có đủ trường; bí mật (chuỗi dạng `sk-...`, `token=`) bị che; log không ghi được (thư mục chỉ đọc) thì cổng vẫn trả đúng quyết định; `harness_doctor.py` thoát 0 khi cấu hình đúng, thoát 1 khi `hooks.json` hỏng |
| A2 | 5 luật `deny` giữ nguyên kết quả (test cũ trong `tests/test_safety_gate.py`); mỗi luật `ask` chặn lệnh mẫu; ca cho qua: `git push --force-with-lease`, `git reset --soft`, `curl -o f.txt URL`, `chmod 755 f.sh`, `SELECT ... DROP` trong chuỗi chú thích; `ask` có phê duyệt còn hạn thì qua; hết hạn hoặc sai mã luật thì chặn lại; `safety_rules.json` hỏng hoặc thiếu thì dùng luật cứng |
| A3 | Tắt: mọi lệnh qua; bật + không phê duyệt: công cụ ghi bị chặn, công cụ đọc qua; có phê duyệt còn hạn: qua; hết hạn: chặn; `plan_gate.json` hỏng thì coi như tắt |
| Script | `harness_approve.py`: `allow` và `plan` ghi đúng định dạng; vượt giới hạn phút/giờ bị từ chối; `status`/`revoke` hoạt động |
| B4 | 3 thư mục × 2 ngôn ngữ tồn tại, ≤ 25 dòng, link hai chiều; AGENTS gốc có mục "Phạm vi chỉ dẫn"; số mục `##` bản Việt bằng bản Anh |
| B5 | `strategic-compaction.md` có đủ ba mức và mục "Luôn giữ" |
| B6′ | Dòng chỉ mục là một dòng, không chứa `<USER_REQUEST>` hoặc ký tự xuống dòng; mô tả dài bị cắt đúng ranh giới từ |

## Tiêu chí hoàn thành
1. `python3 -m unittest discover -s tests` xanh, không đánh dấu bỏ qua hay `expectedFailure` để lách.
2. `python3 scripts/harness_doctor.py` thoát 0.
3. `30-working/ket-qua-xac-minh-harness.md` có đủ V1–V6 với bằng chứng thật.
4. Không sửa `plugins/ppt-master-plugin/`; `attribution_guard.py` vẫn thoát 0.
5. Ba commit riêng (A, B, tài liệu), một PR; không tự merge.

## Rủi ro và cách giảm
| Rủi ro | Giảm |
| :--- | :--- |
| Luật `ask` chặn nhầm lệnh hợp lệ | Có đường phê duyệt ngắn hạn; thêm ca cho qua trong test; ghi nhật ký để tinh chỉnh |
| A3 làm kẹt phiên nếu tên công cụ sai | Mặc định tắt; `harness_doctor.py` hiển thị trạng thái; ghi rõ cách tắt (`enabled: false`) |
| Lớp thực thi thứ hai khó gỡ lỗi (cảnh báo của bài gốc) | A1: nhật ký và `doctor` |
| Thêm tệp chỉ dẫn tốn ngữ cảnh | Mỗi tệp ≤ 25 dòng; tuân `.agents/rules/context-budget.md` |
| Phê duyệt bị agent giả mạo | Phê duyệt chỉ do người dùng chạy script; agent không tự tạo; ghi trong README plugin |

## Cần quyết (mặc định nếu chưa trả lời)
1. Có làm **A3** không? *Mặc định: làm nhưng tắt sẵn; chỉ bật sau khi V1-V5 đạt.*
2. Thay B6 (`MEMORY.md`) bằng **B6′** (làm sạch chỉ mục)? *Mặc định: có.*
3. Có tạo PR sau khi xong? *Mặc định: có, không tự merge.*
