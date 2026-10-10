/*!
 * SUPER-ANTIGRAVITY - nội dung trang web song ngữ vi / en.
 * Khóa ánh xạ 1:1 với [data-i18n] / [data-i18n-attr] trong index.html.
 * Mỗi mục nằm trên một dòng để tests/test_site_i18n.py đọc được.
 */
window.SAG_I18N = {
  defaultLang: "vi",
  meta: {
    vi: { label: "Tiếng Việt", short: "VI", htmlLang: "vi" },
    en: { label: "English", short: "EN", htmlLang: "en" }
  },
  strings: {
    "meta.title": { vi: "SUPER-ANTIGRAVITY — Khung vận hành cho Google Antigravity", en: "SUPER-ANTIGRAVITY — Operating harness for Google Antigravity" },

    "nav.skip": { vi: "Bỏ qua, tới nội dung", en: "Skip to content" },
    "nav.problems": { vi: "Vì sao cần", en: "Why" },
    "nav.structure": { vi: "Kiến trúc", en: "Architecture" },
    "nav.quickstart": { vi: "Cài đặt", en: "Quickstart" },
    "nav.intents": { vi: "Ra lệnh tự nhiên", en: "Natural commands" },
    "nav.contribute": { vi: "Đóng góp", en: "Contribute" },
    "nav.lang": { vi: "Đổi ngôn ngữ", en: "Change language" },

    "hero.eyebrow": { vi: "Khung vận hành đã được thực chiến", en: "Battle-tested operating harness" },
    "hero.title": { vi: "Biến Google Antigravity thành hệ điều hành kỹ thuật tự học", en: "Turn Google Antigravity into a self-learning engineering OS" },
    "hero.lead": { vi: "Chống suy thoái chất lượng mã, quản trị tri thức theo vòng đời và quy chuẩn công nghệ cao cấp, điều khiển bằng tiếng Việt tự nhiên.", en: "Resists code-quality decay, manages knowledge through its lifecycle and enforces premium engineering standards, controlled in natural language." },
    "hero.cta1": { vi: "Bắt đầu cài đặt", en: "Get started" },
    "hero.cta2": { vi: "Xem trên GitHub", en: "View on GitHub" },

    "problems.title": { vi: "Vì sao cần SUPER-ANTIGRAVITY?", en: "Why SUPER-ANTIGRAVITY?" },
    "problems.lead": { vi: "Bảy điểm nghẽn thường gặp, mỗi điểm một giải pháp tích hợp sẵn.", en: "Seven recurring bottlenecks, each with a built-in solution." },
    "problems.p1.t": { vi: "Bộ máy tự học", en: "Self-learning engine" },
    "problems.p1.d": { vi: "Tự bắt lỗi, đúc kết bài học qua lệnh /learn và lưu vào .agents/rules/ để dùng lại vĩnh viễn.", en: "Catches errors automatically, distills lessons with /learn and stores them in .agents/rules/ for permanent reuse." },
    "problems.p2.t": { vi: "Không để trống mã", en: "Zero placeholders" },
    "problems.p2.d": { vi: "Bắt buộc viết mã đầy đủ, ngắt an toàn khi chạm ngưỡng token thay vì cắt xén.", en: "Enforces complete code and breaks safely at the token limit instead of truncating." },
    "problems.p3.t": { vi: "Nén ngữ cảnh chiến lược", en: "Strategic compaction" },
    "problems.p3.d": { vi: "Chủ động nén bộ nhớ phiên và đọc cây cú pháp AST để chỉ đọc đúng mã cần sửa.", en: "Proactively compacts session memory and reads the AST so only the code to change is read." },
    "problems.p4.t": { vi: "Quy trình 5 cổng chất lượng", en: "Five quality gates" },
    "problems.p4.d": { vi: "spec, plan-review, implementation, qa, ship và handoff, không báo xong khi chưa kiểm thử.", en: "spec, plan-review, implementation, qa, ship and handoff, never done before it is tested." },
    "problems.p5.t": { vi: "Bộ ba thẩm mỹ chống slop", en: "Anti-slop design trio" },
    "problems.p5.d": { vi: "impeccable, design-taste-frontend và ui-ux-pro-max giữ giao diện ở chuẩn thương mại cao cấp.", en: "impeccable, design-taste-frontend and ui-ux-pro-max keep the UI at premium commercial quality." },
    "problems.p6.t": { vi: "Vòng đời tri thức SecondBrain", en: "SecondBrain knowledge lifecycle" },
    "problems.p6.d": { vi: "Sáu tầng quản trị tri thức, tương thích hoàn toàn với Obsidian Graph View.", en: "Six knowledge tiers, fully compatible with the Obsidian Graph View." },
    "problems.p7.t": { vi: "Khóa phạm vi trước khi code", en: "Scope-locking before code" },
    "problems.p7.d": { vi: "Phỏng vấn trắc nghiệm 2-3 câu then chốt để chốt yêu cầu rồi mới bắt tay làm.", en: "A 2-3 question multiple-choice interview locks the requirements before any work starts." },

    "structure.title": { vi: "Kiến trúc hệ thống", en: "Architecture" },
    "structure.lead": { vi: "Tài liệu đi qua các tầng từ thô tới thành phẩm.", en: "Documents move through tiers from raw to finished." },
    "structure.s10": { vi: "Phễu tiếp nhận tài liệu thô, ghi chú nhanh", en: "Funnel for raw documents and quick notes" },
    "structure.s20": { vi: "Nguồn tham khảo gốc, tài liệu bóc tách từ inbox", en: "Original references and material extracted from the inbox" },
    "structure.s30": { vi: "Không gian làm việc, checklist ca, biên bản", en: "Workspace, shift checklists, meeting minutes" },
    "structure.s40": { vi: "Chân lý cốt lõi: SOP, Runbook", en: "Core truth: SOPs and runbooks" },
    "structure.s50": { vi: "Thành phẩm phát hành: báo cáo, công văn", en: "Published deliverables: reports and official letters" },
    "structure.s90": { vi: "Lưu trữ lịch sử các giai đoạn trước", en: "Historical archive of earlier periods" },

    "quick.title": { vi: "Cài đặt một chạm", en: "One-click install" },
    "quick.opt1.title": { vi: "Cách 1: dùng trực tiếp làm workspace (khuyến nghị)", en: "Option 1: use directly as a workspace (recommended)" },
    "quick.opt1.s1": { vi: "Clone repo về máy.", en: "Clone the repo." },
    "quick.opt1.s2": { vi: "Mở thư mục bằng Google Antigravity IDE, Cursor hoặc VS Code.", en: "Open the folder in Google Antigravity IDE, Cursor or VS Code." },
    "quick.opt1.s3": { vi: "Mở bằng Obsidian (Open folder as vault) để xem đồ thị tri thức.", en: "Open it in Obsidian (Open folder as vault) to browse the knowledge graph." },
    "quick.opt1.s4": { vi: "Chạy script thiết lập trên Windows.", en: "Run the setup script on Windows." },
    "quick.opt2.title": { vi: "Cách 2: cài plugin toàn cục vào Antigravity", en: "Option 2: install plugins globally into Antigravity" },
    "quick.opt2.desc": { vi: "Dùng đủ 10 plugin cho mọi dự án trên máy.", en: "Use all 10 plugins for every project on your machine." },

    "intents.title": { vi: "Ra lệnh bằng ngôn ngữ tự nhiên", en: "Control it in natural language" },
    "intents.lead": { vi: "Cứ nói tự nhiên, hệ thống tự kích hoạt đúng mô-đun.", en: "Just talk naturally; the right module activates automatically." },
    "intents.i1": { vi: "Lập đặc tả tính năng mới", en: "Write a spec for the new feature" },
    "intents.i2": { vi: "Tra cứu quy trình tiếp nhận yêu cầu và SLA", en: "Look up the request-intake procedure and SLA" },
    "intents.i3": { vi: "Soạn biên bản cuộc họp giao ban sáng nay", en: "Draft minutes for this morning's briefing" },
    "intents.i4": { vi: "Tìm bug và kiểm thử giao diện", en: "Find bugs and test the UI" },
    "intents.i5": { vi: "Vẽ sơ đồ kiến trúc hệ thống chuẩn SVG", en: "Draw the system architecture as SVG" },
    "intents.i6": { vi: "Deploy worker lên Cloudflare", en: "Deploy the worker to Cloudflare" },

    "contrib.title": { vi: "Đóng góp", en: "Contribute" },
    "contrib.desc": { vi: "Mọi đóng góp hoàn thiện khung vận hành đều được chào đón. Đọc hướng dẫn về quy chuẩn Pull Request, bảo toàn vòng đời tri thức và đầu ra đầy đủ.", en: "All contributions that improve the framework are welcome. Read the guide on Pull Request standards, knowledge-lifecycle preservation and full output." },
    "contrib.link": { vi: "Đọc hướng dẫn đóng góp", en: "Read the contribution guide" },

    "foot.license": { vi: "Phát hành theo giấy phép MIT. Tự do sử dụng, tùy biến và chia sẻ.", en: "Released under the MIT License. Free to use, modify and share." }
  }
};
