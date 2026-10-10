**🌐** [🇻🇳 Tiếng Việt](AGENTS.md) · 🇬🇧 English

# 🤖 Operating Rules & Intent Map — SUPER-ANTIGRAVITY

> **SUPER-ANTIGRAVITY**: operating framework and elite skill ecosystem optimized for **Google Antigravity**.
> Natural intent recognition in Vietnamese and English, tightly combining Knowledge Lifecycle management with Software Engineering.

---

## 1. Core Identity & Operating Principles

1. **Evidence-First**:
   - When giving technical advice or looking up procedures, the AI must cite the actual code, file:line or source path.
   - Never speculate or invent technical figures, SLAs or API parameters.

2. **Anti-AI-Slop & Full-Output Policy (Zero Placeholder)**:
   - Abbreviated code is strictly forbidden: `// TODO: continue coding`, `/* keep as is */`, `...`.
   - All generated code must run immediately, complete and intact.

3. **Quality Gate Discipline**:
   - Follow the 5-step process: `spec` ➔ `plan-review` ➔ `implementation` ➔ `qa` ➔ `ship & handoff`.

4. **Preserve the Knowledge Lifecycle structure**:
   - `40-knowledge/`: authoritative knowledge (SOPs, Runbooks).
   - `10-inbox/` and `30-working/`: where drafts are received and processed.
   - `50-outputs/`: finished deliverables.

5. **An approved implementation plan is mandatory**:
   - Before editing code or creating/deleting files, the AI must write an **Implementation Plan** stating: goal, scope, affected files, steps, risks and how it will be tested.
   - Present the plan to the user and **wait for explicit user approval** before implementing. Silence or the original request does not count as approval.
   - If the plan changes (added scope, new direction), present it again and obtain fresh approval.
   - Only pure lookup questions that change no files may skip this.

6. **Context budget**:
   - Load at most 2-3 skills per task, in 3 tiers (description always available, `SKILL.md` body when relevant, `references/` only when deep knowledge is needed).
   - Details in `.agents/rules/context-budget.md`.

---

## 2. Hierarchy of Truth

When receiving a question or business request, the AI searches in this priority order:
1. **`40-knowledge/`**: standards, operating procedures (SOPs), incident runbooks.
2. **`20-sources/`**: original references, partner/expert documents.
3. **`30-working/`**: active workspace (shift checklists, meeting minutes, sprint plans).
4. **`50-outputs/`**: published reports and deliverables.
5. **`10-inbox/`**: newly ingested raw data not yet processed.
6. **`90-archive/`**: historical records of earlier periods.

---

## 3. Natural Intent Classifier

The agent automatically recognizes the user's natural phrasing (Vietnamese or English) to activate the matching skill or plugin. Skill and plugin names are fixed identifiers and are not translated.

### 🏛️ Group 1: Knowledge Management & Operations
| User phrasing / need | Plugin / skill activated | Agent action |
| :--- | :--- | :--- |
| *"look up procedure", "view SOP", "handling steps", "how-to guide"* | `skills/tra-cuu-sop` | Search `40-knowledge/quy-trinh-sop/`, extract steps and SLA |
| *"incident", "lost connection", "system error", "check runbook", "red alert"* | `skills/tra-cuu-sop` + `problem-solving-pro` | Open `40-knowledge/runbooks/`, give emergency steps and escalation matrix immediately |
| *"draft minutes", "briefing meeting", "meeting notes", "summarize meeting opinions"* | `skills/soan-bien-ban-hop` | Create a new minutes file using the `BB-YYYY-MM-DD` template in `30-working/bien-ban-nhat-ky/` |
| *"create checklist", "start-of-shift check", "shift handover", "checklist"* | `skills/lap-checklist-ca` | Create a shift-handover checklist from the standard template in `30-working/checklists/` |
| *"write report", "weekly/monthly report", "summarize results"* | `skills/xu-ly-van-phong` | Produce a complete summary report saved to `50-outputs/bao-cao/` |
| *"standardize official letter", "document format", "decree 30", "fix document"* | `skills/xu-ly-van-phong` | Proofread, align margins, number headings per administrative format |
| *"write announcement", "email to boss", "letter to partner", "write professionally"* | `skills/viet-chuyen-nghiep` | Draft formal text with proper diplomatic and managerial tone |
| *"legal advice", "look up decree", "legal regulations", "clause"* | `skills/tu-van-phap-luat` | Look up and cite valid Vietnamese legal normative documents |
| *"slow computer", "clean junk", "optimize windows", "free up RAM"* | `skills/cham-soc-may-tinh` | Inspect the system and run the Windows maintenance routine |
| *"make excel file", "spreadsheet", "process xlsx"* | `developer-power-skills` (`xlsx`) | Create, read and edit .xlsx/.csv spreadsheets: formulas, formatting, charts |
| *"write word file", "create docx", "edit word document"* | `developer-power-skills` (`docx`) | Create, read and edit Word .docx files, preserving formatting and tracked changes |
| *"make powerpoint file", "create pptx", "edit slide file"* | `developer-power-skills` (`pptx`) | Create and edit .pptx presentations |
| *"read pdf file", "merge pdf", "split pdf", "fill pdf form"* | `developer-power-skills` (`pdf`) | Extract, merge, split, fill forms and OCR PDF files |

### ⚡ Group 2: Elite Development Workflows (gstack)
| User phrasing / need | Plugin / skill activated | Agent action |
| :--- | :--- | :--- |
| *"write spec", "write specification", "create requirements doc"* | `elite-workflows-and-taste` (`spec`) | Produce a 5-phase specification from the initial intent |
| *"founder review", "CEO view", "evaluate big idea"* | `elite-workflows-and-taste` (`plan-ceo-review`) | Challenge the plan from positioning and core-value angles |
| *"eng manager review", "architecture review", "technical review"* | `elite-workflows-and-taste` (`plan-eng-review`) | Assess technical feasibility, architecture risk and system load |
| *"find bugs", "test the UI", "system QA", "testing"* | `elite-workflows-and-taste` (`qa`) | Run automated tests, catch API, CLI and webhook errors |
| *"ship code", "launch feature", "package release", "create PR"* | `elite-workflows-and-taste` (`ship`) | Check branch, run test suite, review diff and ship code |
| *"hand over version", "work handoff", "handover document"* | `elite-workflows-and-taste` (`handoff`) | Create `HANDOFF.md` summarizing state and takeover steps |
| *"compact context", "clean up conversation", "manage context"* | `elite-workflows-and-taste` (`strategic-compact`) | Compact session memory to avoid token overflow |
| *"search source code", "find code structure", "find function"* | `elite-workflows-and-taste` (`smart-explore`) | Scan the tree-sitter AST structure to find symbols precisely |
| *"extract lessons", "remember this session's lessons", "learn from experience", "/learn"* | `antigravity-autoharness-plugin` (`learn`) | Distill this session's lessons into rules stored in `.agents/rules/` |
| *"continuous learning", "extract reusable patterns"* | `elite-workflows-and-taste` (`continuous-learning`) | Automatically extract reusable patterns from sessions and save them as skills |
| *"investigate error", "find root cause", "systematic debugging"* | `elite-workflows-and-taste` (`investigate`) | Debug systematically and investigate the root cause |
| *"get to know a new project", "read the whole codebase"* | `elite-workflows-and-taste` (`learn-codebase`) | Read every source file to prime an unfamiliar codebase before working |
| *"map feature flows", "find duplicated logic", "codebase map"* | `elite-workflows-and-taste` (`pathfinder`) | Map feature flowcharts, find duplicated concerns and propose unification |
| *"design plan review", "designer's view"* | `elite-workflows-and-taste` (`plan-design-review`) | Interactive plan review from a designer's perspective |
| *"developer experience review", "devex review"* | `elite-workflows-and-taste` (`plan-devex-review`) | Interactive plan review of the developer experience |
| *"review pr", "evaluate pull request", "review source code"* | `elite-workflows-and-taste` (`code-review-skill`) + `developer-power-skills` (`bmad-os-review-pr`) | Review pull requests and source code against a review checklist |
| *"remove redundant tests", "duplicate tests", "audit tests"* | `elite-workflows-and-taste` (`test-audit`) | Find low-value or duplicate tests and the test-only code they keep alive |
| *"coding standards", "typescript conventions"* | `elite-workflows-and-taste` (`coding-standards`) | Apply coding standards for TypeScript, JavaScript, React and Node.js |
| *"agent cost report", "token cost", "weekly agent cost"* | `elite-workflows-and-taste` (`agent-cost-report`) | Produce a periodic agent cost report from transcripts and list prices |
| *"enforce full code", "ban truncated code"* | `elite-workflows-and-taste` (`full-output-enforcement`) | Enforce complete code generation and ban placeholder patterns |
| *"security check for new login", "handle user input", "manage secrets"* | `elite-workflows-and-taste` (`security-review`) | Security review for authentication, user input, secrets and API endpoints |
| *"decision matrix", "analyze options"* | `developer-power-skills` (`make-decision`) | Analyze and decide between options |
| *"test web app", "playwright", "browser e2e test"* | `developer-power-skills` (`webapp-testing`) | Test web applications automatically in a browser |
| *"test patterns", "testing strategy"* | `antigravity-kit-plugin` (`testing-patterns`) | Apply testing patterns and strategy |
| *"create a new skill", "write a skill"* | `developer-power-skills` (`skill-creator`) | Guide for creating or updating a skill |
| *"mcp builder", "write local mcp"* | `developer-power-skills` (`mcp-builder`) | Build an MCP server |
| *"openspec create new change", "openspec continue change"* | `openspec-plugin` (`openspec-new-change` / `openspec-continue-change`) | Start a new OpenSpec change or continue one in progress |
| *"openspec fast-forward change", "openspec update change"* | `openspec-plugin` (`openspec-ff-change` / `openspec-update-change`) | Fast-forward a change's artifacts or update an existing change |
| *"openspec verify change", "sync specs"* | `openspec-plugin` (`openspec-verify-change` / `openspec-sync-specs`) | Verify a change was implemented correctly and sync delta specs into main specs |
| *"openspec archive change", "openspec bulk archive"* | `openspec-plugin` (`openspec-archive-change` / `openspec-bulk-archive-change`) | Archive one or many completed OpenSpec changes |
| *"openspec explore change", "get started with openspec"* | `openspec-plugin` (`openspec-explore` / `openspec-onboard`) | Explore ideas before changing or onboard to OpenSpec |
| *"run it to prove it works", "confirm the code runs", "verify by execution"* | `antigravity-kit-plugin` (`verify-changes`) | Prove a change works by actually running it, not by inspecting it |
| *"brainstorm ideas", "explore options", "clarify requirements"* | `antigravity-kit-plugin` (`brainstorming`) | Ask Socratic questions in 4 phases before implementation; does not replace scope-locking |
| *"coordinate multiple agents", "run agents in parallel", "orchestrate specialists"* | `antigravity-kit-plugin` (`coordinator-mode`) | Decompose the task, present the plan for approval, dispatch workers in parallel and synthesize |

### 🎨 Group 3: UI, Graphics & Content Creation (Baoyu & UI Pro)
| User phrasing / need | Plugin / skill activated | Agent action |
| :--- | :--- | :--- |
| *"beautiful UI", "design UI", "color palette", "UI style"* | `antigravity-kit-plugin` (`ui-ux-pro-max`) | Suggest styles, typography and palettes from 50+ modern styles |
| *"polish UI", "make the UI stunning", "audit UI"* | `elite-workflows-and-taste` (`impeccable`) | Review and elevate the UI, fine-tune padding/margin/contrast |
| *"anti-slop", "UI aesthetics", "nice landing page"* | `elite-workflows-and-taste` (`design-taste-frontend`) | Apply high-end aesthetic thinking, remove cheap AI-looking UI |
| *"draw SVG chart", "draw diagram", "flowchart"* | `baoyu-creative-suite` (`baoyu-diagram`) | Generate pure SVG for flowcharts and multi-layer architecture |
| *"make infographic", "create info image", "design infographic"* | `baoyu-creative-suite` (`baoyu-infographic`) | Create infographics from 21 layouts and 22 styles |
| *"make cover", "create cover image", "article thumbnail"* | `baoyu-creative-suite` (`baoyu-cover-image`) | Design article covers across dimensions (Type, Palette, Mood) |
| *"create slide deck", "make presentation slides", "slide outline"* | `baoyu-creative-suite` (`baoyu-slide-deck`) | Outline and generate professional presentation slide images |
| *"scrape web to markdown", "save article as md", "extract link"* | `baoyu-creative-suite` (`baoyu-url-to-markdown`) | Extract a web article into clean Markdown |
| *"get youtube subtitles", "summarize youtube video"* | `baoyu-creative-suite` (`baoyu-youtube-transcript`) | Download subtitles and extract YouTube video transcript content |
| *"translate article", "translate document", "translate keep markdown"* | `baoyu-creative-suite` (`baoyu-translate`) | In-depth translation preserving Markdown formatting |
| *"knowledge comic", "draw comic", "illustrate story"* | `baoyu-creative-suite` (`baoyu-comic`) | Write educational comic scripts and illustrated panels |
| *"xiaohongshu cards", "xhs card", "create image card series"* | `baoyu-creative-suite` (`baoyu-xhs-images`) | Design a series of XHS-style infographic cards |
| *"minimalist interface", "editorial style"* | `elite-workflows-and-taste` (`minimalist-ui`) | Design clean editorial-style interfaces with a warm monochrome palette |
| *"brutalist interface", "raw mechanical ui"* | `elite-workflows-and-taste` (`industrial-brutalist-ui`) | Design raw mechanical interfaces with rigid grids and military-terminal aesthetics |
| *"design like a premium agency", "agency-grade interface"* | `elite-workflows-and-taste` (`high-end-visual-design`) | Design like a high-end agency: fonts, spacing, shadows, cards |
| *"gsap motion effects", "gsap"* | `elite-workflows-and-taste` (`gpt-taste`) | Apply advanced UX/UI and GSAP motion design |
| *"upgrade old website", "redesign existing project"* | `elite-workflows-and-taste` (`redesign-existing-projects`) | Audit current design and upgrade websites and apps to premium quality |
| *"brand identity", "brand kit", "design logo"* | `elite-workflows-and-taste` (`brandkit`) | Generate premium brand-guidelines boards and logo systems |
| *"draw p5js art", "algorithmic art"* | `developer-power-skills` (`algorithmic-art`) | Create algorithmic art with p5.js and seeded randomness |
| *"canvas design", "make poster png pdf"* | `developer-power-skills` (`canvas-design`) | Create visual art as .png and .pdf documents from a design philosophy |
| *"draw data chart", "metrics dashboard", "visual report", "data visualization"* | `developer-power-skills` (`lieflat-charts`) | Create charts, data visualizations and dashboards |
| *"illustrate article", "insert illustrations"* | `baoyu-creative-suite` (`baoyu-article-illustrator`) | Analyze an article, find where visuals belong and generate illustrations |
| *"compress image", "reduce image size"* | `baoyu-creative-suite` (`baoyu-compress-image`) | Compress images to WebP or PNG with automatic tool selection |
| *"format markdown", "normalize markdown"* | `baoyu-creative-suite` (`baoyu-format-markdown`) | Format text with frontmatter, titles, summaries, headings, lists and code blocks |
| *"markdown to html", "export wechat article"* | `baoyu-creative-suite` (`baoyu-markdown-to-html`) | Convert Markdown to styled HTML with code highlighting, math and Mermaid |
| *"create html artifact", "web artifact"* | `developer-power-skills` (`web-artifacts-builder`) | Build multi-component HTML artifacts with modern frontend technology |
| *"write design spec", "create design.md", "define design tokens"* | `antigravity-kit-plugin` (`design-spec`) | Author a `DESIGN.md` (color and type tokens, rationale) before building any UI |

### 💻 Group 4: Software Engineering & Cloudflare
| User phrasing / need | Plugin / skill activated | Agent action |
| :--- | :--- | :--- |
| *"write clean code", "refactor", "standardize source code"* | `antigravity-kit-plugin` (`clean-code`) | Optimize code per SOLID, keep it tidy, remove over-engineering |
| *"design tables", "database", "schema", "create DB tables"* | `antigravity-kit-plugin` (`database-design`) | Design DB schema, indexing strategy and table relations |
| *"design API", "REST API", "endpoint standard"* | `antigravity-kit-plugin` (`api-patterns`) | Design RESTful/GraphQL standards, error codes and pagination |
| *"write tests", "TDD", "unit testing"* | `antigravity-kit-plugin` (`tdd-workflow`) | Execute the Red-Green-Refactor cycle |
| *"security review", "scan vulnerabilities", "security audit"* | `antigravity-kit-plugin` (`vulnerability-scanner`) | Scan for vulnerabilities per OWASP Top 10 |
| *"deploy cloudflare", "write worker", "durable objects"* | `cloudflare-suite` (`wrangler` / `workers-best-practices`) | Develop and deploy serverless systems on Cloudflare |
| *"change management", "propose spec change"* | `openspec-plugin` (`openspec-propose` / `openspec-apply-change`) | Apply OpenSpec software-change standards |
| *"create chrome extension", "chrome add-on"* | `modern-web-guidance-plugin` (`chrome-extensions`) | Develop Chrome extensions following best practices |
| *"modern web standards", "web best practices"* | `modern-web-guidance-plugin` (`modern-web-guidance`) | Apply modern web guidance |
| *"web performance", "core web vitals", "lcp score"* | `developer-power-skills` (`web-perf`) | Measure web performance with Chrome DevTools MCP: FCP, LCP, TBT, CLS |
| *"optimize seo", "google ranking"* | `antigravity-kit-plugin` (`seo-fundamentals`) | Apply SEO fundamentals to a website |
| *"next.js", "react expert"* | `antigravity-kit-plugin` (`nextjs-react-expert`) | Advise on and write expert Next.js/React code |
| *"node.js best practices", "node backend"* | `antigravity-kit-plugin` (`nodejs-best-practices`) | Apply Node.js best practices |
| *"react best practices", "react composition"* | `developer-power-skills` (`vercel-react-best-practices` / `vercel-composition-patterns`) | Apply React best practices and composition patterns |
| *"react native", "expo", "mobile app"* | `developer-power-skills` (`vercel-react-native-skills`) | Build performant React Native and Expo mobile apps |
| *"check web design", "web design guidelines"* | `developer-power-skills` (`web-design-guidelines`) | Check web UI against design guidelines |
| *"powershell", "windows script"* | `antigravity-kit-plugin` (`powershell-windows`) | Write PowerShell scripts for Windows following best practices |
| *"agent on cloudflare", "agents sdk"* | `cloudflare-suite` (`agents-sdk` / `building-ai-agent-on-cloudflare`) | Build stateful AI agents on Cloudflare Workers |
| *"mcp server on cloudflare"* | `cloudflare-suite` (`building-mcp-server-on-cloudflare`) | Build an MCP server on Cloudflare |
| *"persistent objects", "stateful websocket"* | `cloudflare-suite` (`durable-objects`) | Design Durable Objects: state, WebSockets, coordination |
| *"cloudflare overview", "kv d1 r2", "workers ai"* | `cloudflare-suite` (`cloudflare`) | Reference the Cloudflare platform: Workers, Pages, KV, D1, R2, Workers AI |
| *"sandbox to run code safely", "code interpreter"* | `developer-power-skills` (`sandbox-sdk`) | Build sandboxed applications for secure code execution |
| *"multi-language", "hard-coded strings", "i18n", "localization"* | `antigravity-kit-plugin` (`i18n-localization`) | Detect hard-coded strings, check locale files for missing keys and support RTL |
