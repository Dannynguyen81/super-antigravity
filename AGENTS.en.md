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
