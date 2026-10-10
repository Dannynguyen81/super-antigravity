<p align="center">
  <strong>Tiếng Việt</strong> |
  <a href="README.en.md">English</a> |
  <a href="site/index.html">Trang web</a>
</p>

# 🚀 SUPER-ANTIGRAVITY

> **Khung vận hành tinh hoa đã được thực chiến và hệ sinh thái kỹ năng dành cho Google Antigravity.**
> Biến Google Antigravity từ một trợ lý AI thông thường thành một hệ điều hành kỹ thuật tự học, chống suy thoái chất lượng mã, tích hợp quản trị tri thức vòng đời và quy chuẩn công nghệ cao cấp.

[![Antigravity](https://img.shields.io/badge/Antigravity-2.0%2B-blue?style=for-the-badge&logo=google)](https://antigravity.google.com)
[![Obsidian Ready](https://img.shields.io/badge/Obsidian-Compatible-purple?style=for-the-badge&logo=obsidian)](https://obsidian.md)
[![Zero AI Slop](https://img.shields.io/badge/Policy-Zero--Placeholder-success?style=for-the-badge)](AGENTS.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

---

## ⚡ 1. Vì Sao Cần SUPER-ANTIGRAVITY?

Mặc dù **Google Antigravity** sở hữu năng lực suy luận và can thiệp hệ thống vượt trội, các lập trình viên thường xuyên gặp phải 6 rào cản cố hữu trong các dự án thực tế. **SUPER-ANTIGRAVITY** được thiết kế để khắc phục triệt để từng điểm nghẽn:

| Điểm Nghẽn Cố Hữu của Antigravity | Giải Pháp Tích Hợp Trong SUPER-ANTIGRAVITY |
| :--- | :--- |
| ❌ **Quên bài học phiên cũ**: Phiên sau lặp lại lỗi phiên trước, mất thời gian chỉnh lại prompt. | 🧠 **Bộ máy tự học**: Tự động bắt lỗi (kích hoạt theo ma sát động), đúc kết bài học qua lệnh `/learn` và lưu vào `.agents/rules/` để tái sử dụng vĩnh viễn. |
| ❌ **Bệnh code lười / Cắt xén (AI Slop)**: Thường sinh `// TODO: tự code tiếp`, `/* giữ nguyên */`. | 🛡️ **Chính sách không để trống mã**: Cơ chế bắt buộc viết mã đầy đủ (`anti-slop-and-full-output`), tự động ngắt quãng an toàn (điểm ngắt token an toàn) khi chạm ngưỡng token. |
| ❌ **Tràn Context & Tiêu hao Token**: Đọc mã cồng kềnh, phân tích lan man, mau quên mục tiêu ban đầu. | ⚡ **Nén ngữ cảnh chiến lược & Khám phá thông minh**: Cơ chế chủ động nén bộ nhớ phiên làm việc kết hợp bóc tách cây cú pháp AST (tree-sitter) để chỉ đọc đúng mã cần sửa. |
| ❌ **Thiếu kỷ luật kiểm soát chất lượng (Quality Gate)**: Code xong vội vã báo xong mà chưa chạy test. | 🚦 **Quy trình tinh hoa 5 cổng (gstack)**: Buộc Agent tuân thủ chu trình nghiêm ngặt: `spec` ➔ `plan-review` ➔ `implementation` ➔ `qa` ➔ `ship & handoff`. |
| ❌ **Giao diện sinh ra thô sơ, thiếu thẩm mỹ**: UI đơn điệu, màu sắc xỉn màu kiểu AI sinh mẫu. | 🎨 **Bộ ba thẩm mỹ chống slop**: Bộ tam thẩm mỹ `impeccable` + `design-taste-frontend` + `ui-ux-pro-max` đảm bảo sản phẩm đạt chuẩn thương mại cao cấp. |
| ❌ **Thiếu kết nối tri thức cục bộ (Local Knowledge)**: Không có nơi lưu trữ SOP, runbooks, biên bản. | 💎 **Vòng đời tri thức SecondBrain**: 6 phân tầng quản trị tri thức chuẩn mực tương thích 100% với Obsidian Graph View. |
| ❌ **Đoán mò yêu cầu & Vội vàng gõ code lung tung**: Nhận lệnh mơ hồ là code ngay, sinh lỗi trật hướng. | 🎯 **Giao thức khóa phạm vi & phỏng vấn làm rõ**: Tự động kích hoạt phỏng vấn trắc nghiệm 2-3 câu hỏi then chốt để khóa cứng phạm vi trước khi code. |

---

## 📂 2. Kiến Trúc Hệ Thống

```text
SUPER-ANTIGRAVITY/
├── 🤖 .agents/                     # Tầng Tự Học & Điều Phối
│   ├── rules/                     # 4 Core Rules: Anti-slop, Quality Gate, Compaction, Scope-Locking
│   └── skills/                    # Kỹ năng tự sinh qua quá trình trải nghiệm thực tế
│
├── 💎 plugins/                     # 10 Gói Tiện Ích Đóng Gói Chuẩn (mô-đun)
│   ├── antigravity-autoharness/   # Native Hooks (PreInvocation, PostToolUse) & Friction Trigger
│   ├── baoyu-creative-suite/      # [Plugin Mới] Bộ 13 công cụ Baoyu: SVG diagram, Infographic, Slide, Dịch thuật
│   ├── elite-workflows-and-taste/ # Bộ quy trình gstack: spec, plan-review, qa, ship, handoff
│   ├── antigravity-kit-plugin/    # Clean code, API patterns, TDD, DB design, UI-UX Pro Max
│   ├── cloudflare-suite/          # Trọn gói Serverless: Workers, Wrangler, Agents SDK, Durable Objects
│   ├── developer-power-skills/    # Văn phòng cao cấp (docx/xlsx/pptx/pdf), MCP builder, Sandbox
│   ├── modern-web-guidance-plugin/# Best practices web hiện đại & Chrome Extensions
│   ├── openspec-plugin/           # Quy chuẩn đặc tả và quản lý thay đổi phần mềm OpenSpec
│   ├── chrome-devtools-plugin/    # Tương tác kiểm thử qua Chrome DevTools MCP
│   └── ppt-master-plugin/         # [Plugin Mới] Tạo, làm đẹp, điền mẫu PPTX chỉnh sửa được (nguồn: ppt-master)
│
├── 🎯 skills/                      # 7 Kỹ Năng Độc Lập Cho Vận Hành & SecondBrain (độc lập)
│   ├── tra-cuu-sop/               # Tra cứu quy trình vận hành & cẩm nang sự cố (Runbooks)
│   ├── soan-bien-ban-hop/         # Chuyển ghi chú thô thành biên bản họp chuyên nghiệp
│   ├── lap-checklist-ca/          # Sinh bảng kiểm tra bàn giao ca trực có checkbox
│   ├── xu-ly-van-phong/          # Soạn thảo báo cáo, công văn chuẩn thể thức hành chính VN
│   ├── tu-van-phap-luat/          # Dẫn chiếu văn bản quy phạm pháp luật Việt Nam
│   ├── viet-chuyen-nghiep/        # Tòa soạn AI - biên tập ngôn ngữ chuyên môn, sắc bén
│   └── cham-soc-may-tinh/         # Tối ưu hóa, dọn dẹp và bảo dưỡng máy tính Windows
│
├── 🧠 Vòng Đời Tri Thức (Obsidian):
│   ├── 10-inbox/                  # Phễu tiếp nhận tài liệu thô, ghi chú nhanh
│   ├── 20-sources/                # Nguồn tham khảo gốc, tài liệu bóc tách từ inbox
│   ├── 30-working/                # Không gian làm việc, dự án đang chạy, checklist ca
│   ├── 40-knowledge/              # Chân lý cốt lõi: SOPs, Runbooks P1-P4
│   ├── 50-outputs/                # Thành phẩm phát hành: Báo cáo, công văn bàn giao
│   └── 90-archive/                # Lưu trữ lịch sử các giai đoạn trước
│
├── ⚡ scripts/                      # Bộ công cụ tự động hóa 1-Click
├── 📋 AGENTS.md                     # Bộ định tuyến ý định tự nhiên (phân loại ý định)
├── 🧭 SOUL.md                       # Triết lý tác nghiệp & Đạo đức AI
└── 📖 README.md                     # Tài liệu hướng dẫn sử dụng
```

---

## 🚀 3. Hướng Dẫn Cài Đặt 1-Click

### Cách 1: Sử Dụng Trực Tiếp Làm Workspace (Khuyến Nghị)
1. Clone repo về máy:
   ```bash
   git clone https://github.com/Dannynguyen81/super-antigravity.git
   cd super-antigravity
   ```
2. Mở thư mục này bằng **Google Antigravity IDE** hoặc **Cursor / VS Code**.
3. Mở bằng **Obsidian** (chọn `Open folder as vault`) để khai thác tính năng kết nối tri thức trực quan.
4. Chạy script thiết lập môi trường trên Windows:
   ```powershell
   .\scripts\setup-windows.ps1
   ```

### Cách 2: Cài Đặt Plugins Toàn Cục Vào Antigravity
Nếu bạn muốn sử dụng trọn bộ 10 plugins của SUPER-ANTIGRAVITY cho mọi dự án trên máy:
```powershell
# Chạy script tự động cài đặt 1-click
.\scripts\install-plugins-global.ps1
```

---

## 💬 4. Điều Khiển Bằng Tiếng Việt Tự Nhiên (có thể gõ tiếng Anh)

Bạn chỉ cần trò chuyện tự nhiên, hệ sinh thái sẽ tự động kích hoạt module phù hợp:

* *"Lập đặc tả tính năng mới"* ➔ Kích hoạt `spec` (quy trình tinh hoa).
* *"Review ý tưởng này dưới góc nhìn CEO"* ➔ Kích hoạt `plan-ceo-review`.
* *"Review kiến trúc kỹ thuật và tải hệ thống"* ➔ Kích hoạt `plan-eng-review`.
* *"Tìm bug và kiểm thử giao diện"* ➔ Kích hoạt `qa`.
* *"Ship tính năng này lên git"* ➔ Kích hoạt `ship`.
* *"Tạo tài liệu bàn giao handoff"* ➔ Kích hoạt `handoff`.
* *"Tra cứu quy trình tiếp nhận yêu cầu và SLA"* ➔ Kích hoạt `tra-cuu-sop`.
* *"Soạn biên bản cuộc họp giao ban sáng nay"* ➔ Kích hoạt `soan-bien-ban-hop`.
* *"Làm sạch mã nguồn và refactor gọn lại"* ➔ Kích hoạt `clean-code`.
* *"Vẽ sơ đồ kiến trúc hệ thống chuẩn SVG dark mode"* ➔ Kích hoạt `baoyu-diagram` (`baoyu-creative-suite`).
* *"Thiết kế infographic tóm tắt bài viết này"* ➔ Kích hoạt `baoyu-infographic` (`baoyu-creative-suite`).
* *"Tạo ảnh bìa bài viết chuyên nghiệp"* ➔ Kích hoạt `baoyu-cover-image` (`baoyu-creative-suite`).
* *"Deploy worker lên Cloudflare"* ➔ Kích hoạt `cloudflare-suite`.

---

## 🤝 5. Đóng Góp Phát Triển

Mọi đóng góp nhằm hoàn thiện khung vận hành SUPER-ANTIGRAVITY đều được chào đón! Vui lòng đọc [CONTRIBUTING.md](CONTRIBUTING.md) để nắm rõ:
- Quy chuẩn tạo Pull Request.
- Quy định bảo toàn vòng đời tri thức (không gây ô nhiễm).
- Tiêu chuẩn đầu ra đầy đủ cho các đóng góp mã nguồn.

---

## 📄 6. Giấy Phép

Dự án được phân phối dưới giấy phép **MIT License**. Tự do sử dụng, tùy biến và chia sẻ cho mục đích cá nhân lẫn thương mại.
