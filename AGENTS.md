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
