**🌐** 🇻🇳 Tiếng Việt · [🇬🇧 English](AGENTS.en.md)

# 🤖 Quy Tắc Tác Nghiệp & Bản Đồ Ý Định — SUPER-ANTIGRAVITY

> **SUPER-ANTIGRAVITY**: Khung vận hành & Hệ sinh thái kỹ năng tinh hoa tối ưu hóa cho **Google Antigravity**.
> Nhận diện ý định tự nhiên bằng tiếng Việt, kết hợp chặt chẽ giữa Quản trị Tri thức và Kỹ thuật Phần mềm.

---

## 1. Bản Sắc & Nguyên Tắc Tác Nghiệp Cốt Lõi

1. **Nói có sách, mách có chứng**:
   - Khi tư vấn kỹ thuật hoặc tra cứu quy trình, AI bắt buộc phải trích dẫn mã hiệu, file:line hoặc đường dẫn nguồn thực tế.
   - Không suy diễn hoặc bịa đặt số liệu kỹ thuật, SLA hay tham số API.

2. **Chống mã rác do AI & Chính sách đầu ra đầy đủ (không để trống)**:
   - Cấm hoàn toàn các đoạn mã viết tắt: `// TODO: code tiếp`, `/* giữ nguyên */`, `...`.
   - Mọi mã nguồn sinh ra phải chạy được ngay, đầy đủ và nguyên vẹn.

3. **Kỷ luật Cổng Kiểm Soát Chất Lượng**:
   - Tuân thủ quy trình 5 bước: `spec` ➔ `plan-review` ➔ `implementation` ➔ `qa` ➔ `ship & handoff`.

4. **Bảo toàn Cấu trúc Vòng Đời Tri Thức**:
   - `40-knowledge/`: Tri thức chuẩn mực (SOPs, Runbooks).
   - `10-inbox/` và `30-working/`: Nơi tiếp nhận và xử lý bản thảo đang thực hiện.
   - `50-outputs/`: Sản phẩm bàn giao hoàn chỉnh.

5. **Kế hoạch triển khai phải được phê duyệt (bắt buộc)**:
   - Trước khi sửa mã, tạo hoặc xóa file, AI phải lập **Kế hoạch triển khai (Implementation Plan)** nêu rõ: mục tiêu, phạm vi, danh sách file bị tác động, các bước, rủi ro và cách kiểm thử.
   - Trình kế hoạch cho người dùng và **chờ người dùng phê duyệt rõ ràng** mới được triển khai. Không tự coi im lặng hoặc yêu cầu ban đầu là đã phê duyệt.
   - Kế hoạch thay đổi (thêm phạm vi, đổi hướng) phải trình lại và được phê duyệt lại.
   - Chỉ được bỏ qua với câu hỏi thuần tra cứu, không thay đổi tệp nào.

6. **Ngân sách ngữ cảnh**:
   - Mỗi tác vụ chỉ nạp tối đa 2-3 kỹ năng, nạp theo 3 tầng (mô tả luôn có, thân `SKILL.md` khi liên quan, `references/` khi cần sâu).
   - Chi tiết tại `.agents/rules/context-budget.md`.

---

## 2. Thứ Tự Tra Cứu Tri Thức

Khi nhận câu hỏi hoặc yêu cầu nghiệp vụ, AI tra cứu theo thứ tự ưu tiên:
1. **`40-knowledge/`**: Quy chuẩn, quy trình vận hành (SOP), cẩm nang sự cố (Runbooks).
2. **`20-sources/`**: Nguồn tham khảo gốc, tài liệu từ đối tác/chuyên gia.
3. **`30-working/`**: Không gian đang tác nghiệp (Checklist ca trực, biên bản cuộc họp, kế hoạch sprint).
4. **`50-outputs/`**: Báo cáo và sản phẩm đã phát hành.
5. **`10-inbox/`**: Dữ liệu thô mới nạp chưa xử lý.
6. **`90-archive/`**: Hồ sơ lịch sử các giai đoạn trước.

---

## 3. Bộ Phân Loại Ý Định Tự Nhiên

Agent tự động nhận diện khẩu ngữ tiếng Việt của người dùng để kích hoạt kỹ năng hoặc plugin tương ứng:

### 🏛️ Phân hệ 1: Quản Trị Tri Thức & Nghiệp Vụ Vận Hành
| Khẩu ngữ / Nhu cầu người dùng | Plugin / Kỹ năng kích hoạt | Hành động của Agent |
| :--- | :--- | :--- |
| *"tra cứu quy trình", "xem sop", "các bước xử lý", "hướng dẫn thao tác"* | `skills/tra-cuu-sop` | Tìm kiếm trong `40-knowledge/quy-trinh-sop/`, trích xuất các bước và SLA |
| *"bị sự cố", "mất kết nối", "lỗi hệ thống", "tra runbook", "báo động đỏ"* | `skills/tra-cuu-sop` + `problem-solving-pro` | Mở `40-knowledge/runbooks/`, đưa ngay bước xử lý khẩn cấp và ma trận leo thang |
| *"soạn biên bản", "họp giao ban", "ghi chú cuộc họp", "tổng hợp ý kiến họp"* | `skills/soan-bien-ban-hop` | Tạo file biên bản họp mới theo mẫu `BB-YYYY-MM-DD` trong `30-working/bien-ban-nhat-ky/` |
| *"tạo checklist", "kiểm tra đầu ca", "bàn giao ca trực", "danh mục kiểm tra"* | `skills/lap-checklist-ca` | Tạo bảng checklist bàn giao ca theo mẫu chuẩn trong `30-working/checklists/` |
| *"soạn báo cáo", "lập báo cáo tuần/tháng", "tổng hợp kết quả"* | `skills/xu-ly-van-phong` | Tạo báo cáo tổng kết hoàn chỉnh lưu vào `50-outputs/bao-cao/` |
| *"chuẩn hóa công văn", "thể thức văn bản", "nghị định 30", "chỉnh văn bản"* | `skills/xu-ly-van-phong` | Soát lỗi chính tả, căn chỉnh lề, đánh số đề mục chuẩn thể thức hành chính |
| *"viết thông báo", "soạn email sếp", "thư đối tác", "viết chuyên nghiệp"* | `skills/viet-chuyen-nghiep` | Soạn thảo văn bản trang trọng, chuẩn mực ngoại giao và điều hành |
| *"tư vấn luật", "tra cứu nghị định", "quy định pháp luật", "điều khoản"* | `skills/tu-van-phap-luat` | Tra cứu và dẫn chiếu văn bản quy phạm pháp luật Việt Nam có hiệu lực |
| *"máy tính chậm", "dọn rác máy", "tối ưu windows", "giải phóng ram"* | `skills/cham-soc-may-tinh` | Kiểm tra hệ thống và chạy quy trình bảo dưỡng máy tính Windows |
| *"làm file excel", "bảng tính", "xử lý xlsx"* | `developer-power-skills` (`xlsx`) | Tạo, đọc, sửa bảng tính .xlsx/.csv: công thức, định dạng, biểu đồ |
| *"soạn file word", "tạo docx", "chỉnh tài liệu word"* | `developer-power-skills` (`docx`) | Tạo, đọc, sửa tài liệu Word .docx, giữ định dạng và theo dõi thay đổi |
| *"làm file powerpoint", "tạo pptx", "sửa file slide"* | `developer-power-skills` (`pptx`) | Tạo và chỉnh bài trình chiếu .pptx |
| *"đọc file pdf", "gộp pdf", "tách pdf", "điền form pdf"* | `developer-power-skills` (`pdf`) | Trích xuất, gộp, tách, điền biểu mẫu và OCR tệp PDF |

### ⚡ Phân hệ 2: Quy Trình Phát Triển Cao Cấp (gstack)
| Khẩu ngữ / Nhu cầu người dùng | Plugin / Kỹ năng kích hoạt | Hành động của Agent |
| :--- | :--- | :--- |
| *"lập spec", "viết đặc tả", "tạo bản mô tả yêu cầu"* | `elite-workflows-and-taste` (`spec`) | Tạo tài liệu đặc tả 5 giai đoạn từ ý định sơ khởi |
| *"founder review", "góc nhìn CEO", "đánh giá ý tưởng lớn"* | `elite-workflows-and-taste` (`plan-ceo-review`) | Phản biện kế hoạch dưới góc nhìn định vị và giá trị cốt lõi |
| *"eng manager review", "đánh giá kiến trúc", "review kỹ thuật"* | `elite-workflows-and-taste` (`plan-eng-review`) | Đánh giá tính khả thi kỹ thuật, rủi ro kiến trúc và tải hệ thống |
| *"tìm bug", "test giao diện", "qa hệ thống", "kiểm thử"* | `elite-workflows-and-taste` (`qa`) | Chạy kiểm thử tự động, bắt lỗi API, CLI, webhooks |
| *"ship code", "ra mắt tính năng", "đóng gói release", "tạo pr"* | `elite-workflows-and-taste` (`ship`) | Kiểm tra branch, chạy test suite, review diff và ship code |
| *"bàn giao phiên bản", "handoff công việc", "tài liệu bàn giao"* | `elite-workflows-and-taste` (`handoff`) | Tạo `HANDOFF.md` tóm tắt trạng thái và các bước tiếp quản |
| *"nén context", "dọn dẹp hội thoại", "quản lý ngữ cảnh"* | `elite-workflows-and-taste` (`strategic-compact`) | Nén bộ nhớ phiên làm việc để tránh tràn token |
| *"tra cứu mã nguồn", "tìm kiếm cấu trúc code", "tìm hàm"* | `elite-workflows-and-taste` (`smart-explore`) | Quét cấu trúc AST tree-sitter để tìm kiếm biểu tượng chính xác |
| *"rút bài học", "ghi nhớ bài học phiên này", "tự học kinh nghiệm", "/learn"* | `antigravity-autoharness-plugin` (`learn`) | Đúc kết bài học phiên hiện tại thành quy tắc lưu trong `.agents/rules/` |
| *"học liên tục", "trích xuất mẫu tái dùng"* | `elite-workflows-and-taste` (`continuous-learning`) | Tự trích xuất mẫu tái sử dụng từ phiên làm việc và lưu thành kỹ năng |
| *"điều tra lỗi", "tìm nguyên nhân gốc", "debug có hệ thống"* | `elite-workflows-and-taste` (`investigate`) | Gỡ lỗi có hệ thống, điều tra nguyên nhân gốc rễ |
| *"làm quen dự án mới", "đọc hiểu toàn bộ codebase"* | `elite-workflows-and-taste` (`learn-codebase`) | Đọc toàn bộ mã nguồn để nắm dự án lạ trước khi làm việc |
| *"vẽ bản đồ luồng tính năng", "tìm logic trùng lặp", "bản đồ codebase"* | `elite-workflows-and-taste` (`pathfinder`) | Vẽ sơ đồ luồng theo tính năng, phát hiện logic trùng và đề xuất hợp nhất |
| *"review thiết kế kế hoạch", "góc nhìn designer"* | `elite-workflows-and-taste` (`plan-design-review`) | Phản biện kế hoạch dưới góc nhìn nhà thiết kế, tương tác từng bước |
| *"review trải nghiệm lập trình viên", "đánh giá devex"* | `elite-workflows-and-taste` (`plan-devex-review`) | Phản biện kế hoạch về trải nghiệm lập trình viên, tương tác từng bước |
| *"review pr", "đánh giá pull request", "soát mã nguồn"* | `elite-workflows-and-taste` (`code-review-skill`) + `developer-power-skills` (`bmad-os-review-pr`) | Rà soát pull request và mã nguồn theo checklist review |
| *"dọn test thừa", "test trùng lặp", "kiểm toán test"* | `elite-workflows-and-taste` (`test-audit`) | Tìm test giá trị thấp, test trùng và mã chỉ tồn tại vì test |
| *"coding standards", "quy ước code typescript"* | `elite-workflows-and-taste` (`coding-standards`) | Áp dụng chuẩn viết mã TypeScript, JavaScript, React, Node.js |
| *"báo cáo chi phí agent", "chi phí token", "chi phí agent theo tuần"* | `elite-workflows-and-taste` (`agent-cost-report`) | Lập báo cáo chi phí agent theo kỳ từ transcript và giá niêm yết |
| *"ép viết đủ mã", "cấm cắt xén mã"* | `elite-workflows-and-taste` (`full-output-enforcement`) | Bắt buộc sinh mã đầy đủ, cấm mọi dạng giữ chỗ |
| *"rà soát bảo mật khi thêm đăng nhập", "xử lý dữ liệu nhập", "quản lý secret"* | `elite-workflows-and-taste` (`security-review`) | Rà soát bảo mật khi làm xác thực, dữ liệu nhập, bí mật và endpoint API |
| *"ma trận quyết định", "phân tích lựa chọn"* | `developer-power-skills` (`make-decision`) | Phân tích và chốt quyết định giữa các phương án |
| *"test web app", "playwright", "e2e trình duyệt"* | `developer-power-skills` (`webapp-testing`) | Kiểm thử ứng dụng web tự động trên trình duyệt |
| *"mẫu viết test", "chiến lược kiểm thử"* | `antigravity-kit-plugin` (`testing-patterns`) | Áp dụng mẫu viết test và chiến lược kiểm thử |
| *"tạo kỹ năng mới", "viết skill"* | `developer-power-skills` (`skill-creator`) | Hướng dẫn tạo hoặc cập nhật một skill |
| *"mcp builder", "viết mcp cục bộ"* | `developer-power-skills` (`mcp-builder`) | Xây dựng máy chủ MCP |
| *"openspec tạo thay đổi mới", "openspec làm tiếp thay đổi"* | `openspec-plugin` (`openspec-new-change` / `openspec-continue-change`) | Mở thay đổi OpenSpec mới hoặc tiếp tục thay đổi đang dở |
| *"openspec chạy nhanh thay đổi", "openspec cập nhật thay đổi"* | `openspec-plugin` (`openspec-ff-change` / `openspec-update-change`) | Chạy nhanh các artifact của thay đổi hoặc cập nhật thay đổi hiện có |
| *"openspec xác minh thay đổi", "đồng bộ spec"* | `openspec-plugin` (`openspec-verify-change` / `openspec-sync-specs`) | Xác minh thay đổi đã triển khai đúng, đồng bộ spec delta vào spec chính |
| *"openspec lưu trữ thay đổi", "openspec lưu trữ hàng loạt"* | `openspec-plugin` (`openspec-archive-change` / `openspec-bulk-archive-change`) | Lưu trữ một hoặc nhiều thay đổi OpenSpec đã hoàn tất |
| *"openspec khám phá thay đổi", "làm quen openspec"* | `openspec-plugin` (`openspec-explore` / `openspec-onboard`) | Khảo sát ý tưởng trước khi đổi hoặc hướng dẫn làm quen OpenSpec |

### 🎨 Phân hệ 3: Giao Diện, Đồ Họa & Sáng Tạo Nội Dung
| Khẩu ngữ / Nhu cầu người dùng | Plugin / Kỹ năng kích hoạt | Hành động của Agent |
| :--- | :--- | :--- |
| *"giao diện đẹp", "thiết kế ui", "bảng màu", "style giao diện"* | `antigravity-kit-plugin` (`ui-ux-pro-max`) | Gợi ý phong cách, typography, bảng màu từ 50+ phong cách hiện đại |
| *"trau chuốt ui", "làm đẹp giao diện đỉnh cao", "audit ui"* | `elite-workflows-and-taste` (`impeccable`) | Rà soát và nâng tầm giao diện, tinh chỉnh padding/margin/contrast |
| *"chống slop", "thẩm mỹ giao diện", "landing page đẹp"* | `elite-workflows-and-taste` (`design-taste-frontend`) | Áp dụng tư duy thẩm mỹ cao cấp, loại bỏ giao diện AI rẻ tiền |
| *"vẽ biểu đồ svg", "vẽ diagram", "sơ đồ luồng"* | `baoyu-creative-suite` (`baoyu-diagram`) | Tự sinh mã SVG thuần cho biểu đồ luồng, kiến trúc đa tầng |
| *"làm infographic", "tạo ảnh thông tin", "thiết kế infographic"* | `baoyu-creative-suite` (`baoyu-infographic`) | Tạo hình ảnh infographic theo 21 layout và 22 phong cách |
| *"làm ảnh bìa", "tạo cover image", "ảnh đại diện bài viết"* | `baoyu-creative-suite` (`baoyu-cover-image`) | Thiết kế ảnh bìa bài viết đa chiều (Type, Palette, Mood) |
| *"tạo slide deck", "làm slide thuyết trình", "dàn ý slide"* | `baoyu-creative-suite` (`baoyu-slide-deck`) | Lên dàn ý và sinh hình ảnh slide thuyết trình chuyên nghiệp |
| *"cào web ra markdown", "tải bài viết về md", "trích xuất link"* | `baoyu-creative-suite` (`baoyu-url-to-markdown`) | Bóc tách bài viết trên trang web thành Markdown sạch |
| *"lấy phụ đề youtube", "tóm tắt video youtube"* | `baoyu-creative-suite` (`baoyu-youtube-transcript`) | Tải phụ đề và trích xuất nội dung transcript video YouTube |
| *"dịch bài viết", "dịch tài liệu", "translate giữ markdown"* | `baoyu-creative-suite` (`baoyu-translate`) | Dịch thuật chuyên sâu giữ nguyên định dạng Markdown |
| *"truyện tranh kiến thức", "vẽ comic", "minh họa truyện"* | `baoyu-creative-suite` (`baoyu-comic`) | Sáng tác kịch bản truyện tranh giáo dục và phân cảnh minh họa |
| *"thẻ ảnh tiểu hồng thư", "xhs card", "tạo chuỗi thẻ ảnh"* | `baoyu-creative-suite` (`baoyu-xhs-images`) | Thiết kế chuỗi card infographic phong cách XHS |
| *"giao diện tối giản", "phong cách editorial"* | `elite-workflows-and-taste` (`minimalist-ui`) | Thiết kế giao diện tối giản kiểu tạp chí, tông đơn sắc ấm |
| *"giao diện brutalist", "ui cơ khí thô"* | `elite-workflows-and-taste` (`industrial-brutalist-ui`) | Thiết kế giao diện thô cơ khí, lưới cứng, thẩm mỹ terminal quân sự |
| *"thiết kế như agency cao cấp", "giao diện agency cao cấp"* | `elite-workflows-and-taste` (`high-end-visual-design`) | Thiết kế như agency cao cấp: phông, khoảng cách, bóng đổ, thẻ |
| *"hiệu ứng chuyển động gsap", "gsap"* | `elite-workflows-and-taste` (`gpt-taste`) | Áp dụng UX/UI và chuyển động GSAP nâng cao |
| *"nâng cấp website cũ", "redesign dự án cũ"* | `elite-workflows-and-taste` (`redesign-existing-projects`) | Kiểm tra thiết kế hiện tại và nâng website/app lên chuẩn cao cấp |
| *"bộ nhận diện thương hiệu", "brand kit", "thiết kế logo"* | `elite-workflows-and-taste` (`brandkit`) | Tạo bảng hướng dẫn thương hiệu và hệ logo cao cấp |
| *"vẽ tranh p5js", "nghệ thuật thuật toán"* | `developer-power-skills` (`algorithmic-art`) | Tạo nghệ thuật thuật toán bằng p5.js với ngẫu nhiên có hạt giống |
| *"thiết kế canvas", "làm poster png pdf"* | `developer-power-skills` (`canvas-design`) | Tạo tác phẩm thị giác dạng .png và .pdf theo triết lý thiết kế |
| *"vẽ biểu đồ số liệu", "dashboard số liệu", "báo cáo trực quan", "trực quan hóa dữ liệu"* | `developer-power-skills` (`lieflat-charts`) | Tạo biểu đồ, trực quan hóa dữ liệu và bảng điều khiển |
| *"minh họa bài viết", "chèn ảnh minh họa"* | `baoyu-creative-suite` (`baoyu-article-illustrator`) | Phân tích bài viết, xác định vị trí cần hình và sinh ảnh minh họa |
| *"nén ảnh", "giảm dung lượng ảnh"* | `baoyu-creative-suite` (`baoyu-compress-image`) | Nén ảnh sang WebP hoặc PNG với công cụ tự chọn |
| *"định dạng markdown", "chuẩn hóa markdown"* | `baoyu-creative-suite` (`baoyu-format-markdown`) | Định dạng văn bản: frontmatter, tiêu đề, tóm tắt, danh sách, khối mã |
| *"markdown sang html", "xuất bài wechat"* | `baoyu-creative-suite` (`baoyu-markdown-to-html`) | Chuyển Markdown thành HTML có giao diện, hỗ trợ code, toán, Mermaid |
| *"tạo artifact html", "web artifact"* | `developer-power-skills` (`web-artifacts-builder`) | Dựng artifact HTML nhiều thành phần bằng công nghệ frontend hiện đại |

### 💻 Phân hệ 4: Kỹ Thuật Lập Trình & Cloudflare
| Khẩu ngữ / Nhu cầu người dùng | Plugin / Kỹ năng kích hoạt | Hành động của Agent |
| :--- | :--- | :--- |
| *"viết code sạch", "refactor gọn", "chuẩn hóa mã nguồn"* | `antigravity-kit-plugin` (`clean-code`) | Tối ưu mã theo SOLID, gọn gàng, loại bỏ over-engineering |
| *"thiết kế bảng", "database", "schema", "tạo bảng csdl"* | `antigravity-kit-plugin` (`database-design`) | Thiết kế schema CSDL, chiến lược indexing và quan hệ bảng |
| *"thiết kế api", "rest api", "chuẩn endpoint"* | `antigravity-kit-plugin` (`api-patterns`) | Thiết kế chuẩn RESTful, GraphQL, mã lỗi và phân trang |
| *"viết test", "tdd", "kiểm thử đơn vị"* | `antigravity-kit-plugin` (`tdd-workflow`) | Thực thi chu trình Red-Green-Refactor |
| *"soát lỗi bảo mật", "quét lỗ hổng", "security audit"* | `antigravity-kit-plugin` (`vulnerability-scanner`) | Quét lỗ hổng theo chuẩn OWASP Top 10 |
| *"deploy cloudflare", "viết worker", "durable objects"* | `cloudflare-suite` (`wrangler` / `workers-best-practices`) | Phát triển và triển khai hệ thống serverless trên Cloudflare |
| *"quản lý thay đổi", "đề xuất thay đổi spec"* | `openspec-plugin` (`openspec-propose` / `openspec-apply-change`) | Áp dụng quy chuẩn thay đổi phần mềm OpenSpec |
| *"tạo chrome extension", "tiện ích chrome"* | `modern-web-guidance-plugin` (`chrome-extensions`) | Phát triển tiện ích mở rộng Chrome theo thực hành tốt |
| *"chuẩn web hiện đại", "thực hành tốt web"* | `modern-web-guidance-plugin` (`modern-web-guidance`) | Áp dụng hướng dẫn web hiện đại |
| *"hiệu năng web", "core web vitals", "chỉ số lcp"* | `developer-power-skills` (`web-perf`) | Đo hiệu năng web bằng Chrome DevTools MCP: FCP, LCP, TBT, CLS |
| *"tối ưu seo", "xếp hạng google"* | `antigravity-kit-plugin` (`seo-fundamentals`) | Áp dụng nền tảng SEO cho website |
| *"next.js", "chuyên gia react"* | `antigravity-kit-plugin` (`nextjs-react-expert`) | Tư vấn và viết mã Next.js/React chuyên sâu |
| *"node.js chuẩn", "backend node"* | `antigravity-kit-plugin` (`nodejs-best-practices`) | Áp dụng thực hành tốt cho Node.js |
| *"react chuẩn hiệu năng", "composition react"* | `developer-power-skills` (`vercel-react-best-practices` / `vercel-composition-patterns`) | Áp dụng thực hành tốt và mẫu composition cho React |
| *"react native", "expo", "ứng dụng di động"* | `developer-power-skills` (`vercel-react-native-skills`) | Xây ứng dụng di động React Native/Expo hiệu năng cao |
| *"kiểm tra thiết kế web", "chuẩn thiết kế web"* | `developer-power-skills` (`web-design-guidelines`) | Đối chiếu giao diện web với hướng dẫn thiết kế |
| *"powershell", "script windows"* | `antigravity-kit-plugin` (`powershell-windows`) | Viết script PowerShell cho Windows theo thực hành tốt |
| *"agent trên cloudflare", "agents sdk"* | `cloudflare-suite` (`agents-sdk` / `building-ai-agent-on-cloudflare`) | Xây agent AI có trạng thái trên Cloudflare Workers |
| *"mcp server trên cloudflare"* | `cloudflare-suite` (`building-mcp-server-on-cloudflare`) | Xây máy chủ MCP trên Cloudflare |
| *"đối tượng bền vững", "websocket có trạng thái"* | `cloudflare-suite` (`durable-objects`) | Thiết kế Durable Objects: trạng thái, WebSocket, đồng bộ |
| *"tổng quan cloudflare", "kv d1 r2", "workers ai"* | `cloudflare-suite` (`cloudflare`) | Tra cứu nền tảng Cloudflare: Workers, Pages, KV, D1, R2, Workers AI |
| *"sandbox chạy mã an toàn", "code interpreter"* | `developer-power-skills` (`sandbox-sdk`) | Xây ứng dụng sandbox thực thi mã an toàn |
