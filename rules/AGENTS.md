# Global Workspace Rules & Intent Classifier

> Áp dụng toàn cục cho mọi dự án, hỗ trợ tự nhiên tiếng Việt và tiếng Anh.

## 1. Nguyên tắc nhận diện ngôn ngữ tiếng Việt tự nhiên
- Luôn thấu hiểu mọi yêu cầu bằng tiếng Việt (bao gồm khẩu ngữ, từ lóng kỹ thuật, cách diễn đạt đời thường).
- Không yêu cầu người dùng phải gõ đúng tên skill hay cú pháp tiếng Anh.
- Tự động map ý định người dùng tới các bộ skills tương ứng:
  * "viết code sạch / gọn lại / dễ đọc" -> clean-code
  * "thiết kế bảng / database / csdl" -> database-design
  * "giao diện đẹp / làm lại ui / bảng màu" -> ui-ux-pro-max
  * "vẽ biểu đồ / làm chart / dashboard" -> lieflat-charts
  * "làm cho nó người hơn / khử giọng ai / nhân tính hơn" -> humanizer
  * "tạo file word / xuất word" -> docx
  * "làm slide / thuyết trình" -> pptx
  * "tính toán / xuất excel" -> xlsx
  * "soi lỗi pr / review pr" -> bmad-os-review-pr
  * "bị lỗi / tìm nguyên nhân / tại sao bị vậy" -> problem-solving-pro
  * "phân vân / nên chọn cái nào / so sánh" -> make-decision
  * "lập spec / viết đặc tả / tạo đề xuất thay đổi" -> openspec-propose
  * "thảo luận ý tưởng / khảo sát giải pháp" -> openspec-explore
  * "triển khai spec / code theo spec" -> openspec-apply-change
  * "nghiệm thu spec / kiểm tra khớp spec" -> openspec-verify-change
  * "lưu trữ spec / đóng spec" -> openspec-archive-change
  * "trau chuốt ui / làm đẹp giao diện đỉnh cao / thiết kế đẳng cấp / audit ui" -> impeccable
  * "chống slop / thẩm mỹ giao diện / gu thiết kế / landing page đẹp" -> design-taste-frontend
  * "giao diện tối giản / phong cách báo chí / minimalist" -> minimalist-ui
  * "giao diện brutalist / thô mộc / phong cách kỹ thuật" -> industrial-brutalist-ui
  * "viết code đầy đủ / không viết tắt / không bỏ sót code" -> full-output-enforcement
  * "review code đa ngôn ngữ / kiểm tra pr chi tiết" -> code-review-skill
  * "founder review / góc nhìn ceo / đánh giá ý tưởng lớn" -> plan-ceo-review
  * "eng manager review / đánh giá kiến trúc kỹ thuật" -> plan-eng-review
  * "tìm bug / test giao diện / qa hệ thống" -> qa
  * "ship code / ra mắt tính năng / đóng gói release" -> ship
  * "bàn giao phiên bản / handoff công việc" -> handoff
  * "nén context / quản lý ngữ cảnh chủ động" -> strategic-compact
  * "chăm sóc máy tính / dọn rác máy / tối ưu windows / giải phóng ram / bảo dưỡng pc" -> cham-soc-may-tinh
  * "tư vấn pháp luật / luật quy định / tranh chấp / bị kiện / xử lý pháp lý" -> tu-van-phap-luat
  * "viết chuyên nghiệp / tòa soạn báo / tổng biên tập / bài viết chuyên sâu" -> viet-chuyen-nghiep
  * "xử lý văn phòng / tạo tài liệu văn phòng / chuẩn nd 30 / bóc tách brand kit" -> xu-ly-van-phong
  * "tự học kinh nghiệm / ghi nhớ bài học phiên này / đúc kết phiên / tự tối ưu kỹ năng" -> learn
  * "dọn tủ kỹ năng / hợp nhất các skill trùng / audit skill / thanh lọc kỹ năng" -> curator
  * "dựng 3d / phối cảnh 3d / mô hình 3d / threejs / webgl / blender" -> 3dviz-pro-max
  * "prompt ảnh / phong cách ảnh / style gpt image / mẫu prompt ảnh" -> gpt-image-2-style-library
  * "vẽ sơ đồ kiến trúc / diagram design / sơ đồ hệ thống / wardley map" -> diagram-design
  * "vẽ biểu đồ svg / vẽ diagram / biểu đồ dark mode / sơ đồ luồng" -> baoyu-diagram
  * "làm infographic / tạo ảnh thông tin / thiết kế infographic / sơ đồ trực quan hóa" -> baoyu-infographic
  * "làm ảnh bìa / tạo cover image / ảnh đại diện bài viết / thiết kế bìa" -> baoyu-cover-image
  * "tạo slide deck / làm slide thuyết trình / dàn ý slide / bài trình chiếu" -> baoyu-slide-deck
  * "làm ảnh xhs / ảnh tiểu hồng thư / thẻ ảnh tri thức / card tóm tắt" -> baoyu-xhs-images
  * "minh họa bài viết / tìm ảnh minh họa / vẽ hình cho bài / gợi ý hình ảnh" -> baoyu-article-illustrator
  * "vẽ truyện tranh / tạo comic / kiến thức dạng truyện / comic strip" -> baoyu-comic
  * "định dạng markdown / format bài viết / chuẩn hóa văn bản md / dọn trình bày" -> baoyu-format-markdown
  * "chuyển md sang html / xuất html từ markdown / định dạng bài đăng" -> baoyu-markdown-to-html
  * "cào web ra markdown / tải bài viết về md / bóc tách link web" -> baoyu-url-to-markdown
  * "dịch bài viết / dịch tài liệu kỹ thuật / translate giữ markdown" -> baoyu-translate
  * "lấy phụ đề youtube / tóm tắt video youtube / get youtube transcript" -> baoyu-youtube-transcript
  * "nén ảnh / giảm dung lượng ảnh / tối ưu ảnh webp" -> baoyu-compress-image

## 2. Tiêu chuẩn phản hồi
- Giữ phong cách ngắn gọn, súc tích, giải quyết thẳng vào vấn đề.
- Ưu tiên hiển thị giải pháp hoặc code mẫu trực tiếp, không vòng vo giải thích thừa.
