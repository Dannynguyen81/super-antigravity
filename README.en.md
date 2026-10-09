<p align="center">
  <a href="README.md">Tiếng Việt</a> |
  <strong>English</strong> |
  <a href="site/index.html?lang=en">Website</a>
</p>

# 🚀 SUPER-ANTIGRAVITY

> **The ultimate battle-tested operating harness and skill ecosystem for Google Antigravity.**
> Turn Google Antigravity from an ordinary AI assistant into a self-learning engineering operating system that resists code-quality decay and integrates knowledge-lifecycle management with premium engineering standards.

[![Antigravity](https://img.shields.io/badge/Antigravity-2.0%2B-blue?style=for-the-badge&logo=google)](https://antigravity.google.com)
[![Obsidian Ready](https://img.shields.io/badge/Obsidian-Compatible-purple?style=for-the-badge&logo=obsidian)](https://obsidian.md)
[![Zero AI Slop](https://img.shields.io/badge/Policy-Zero--Placeholder-success?style=for-the-badge)](AGENTS.en.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.en.md)

---

## ⚡ 1. Why SUPER-ANTIGRAVITY?

Although **Google Antigravity** has outstanding reasoning and system-level capabilities, developers regularly hit 6 recurring obstacles in real projects. **SUPER-ANTIGRAVITY** is designed to remove each bottleneck:

| Inherent Antigravity bottleneck | Solution built into SUPER-ANTIGRAVITY |
| :--- | :--- |
| ❌ **Forgets lessons from past sessions**: the next session repeats the previous mistakes, wasting time re-tuning prompts. | 🧠 **Self-Learning Harness Engine**: automatically catches errors (Dynamic Friction Trigger), distills lessons via the `/learn` command and stores them in `.agents/rules/` for permanent reuse. |
| ❌ **Lazy / truncated code (AI Slop)**: often emits `// TODO: continue coding`, `/* keep as is */`. | 🛡️ **Zero-Placeholder Policy**: enforces complete code (`anti-slop-and-full-output`) and breaks safely (Safe Token Breakpoint) when hitting the token limit. |
| ❌ **Context overflow and token waste**: bulky code reads, rambling analysis, losing the original goal. | ⚡ **Strategic Compactor & Smart Explore**: proactively compacts session memory and parses AST (tree-sitter) so only the code that needs changing is read. |
| ❌ **No quality-gate discipline**: declares "done" in a hurry without running tests. | 🚦 **5-Gate Elite Workflows (gstack)**: forces the Agent through a strict cycle: `spec` ➔ `plan-review` ➔ `implementation` ➔ `qa` ➔ `ship & handoff`. |
| ❌ **Crude, unattractive generated UI**: monotone layouts, dull template-like AI colors. | 🎨 **Anti-Slop Design Trio**: `impeccable` + `design-taste-frontend` + `ui-ux-pro-max` keep output at premium commercial quality. |
| ❌ **No local knowledge store**: nowhere to keep SOPs, runbooks, meeting minutes. | 💎 **SecondBrain Knowledge Lifecycle**: 6 knowledge-management tiers, 100% compatible with the Obsidian Graph View. |
| ❌ **Guesses vague requests and rushes into code**: acts on ambiguous commands and goes off-track. | 🎯 **Scope-Locking & Grill-Me Protocol**: automatically runs a 2–3 question multiple-choice interview to lock the scope before coding. |

---

## 📂 2. Architecture Map

```text
SUPER-ANTIGRAVITY/
├── 🤖 .agents/                     # Self-learning & orchestration layer (AutoHarness Engine)
│   ├── rules/                     # 4 core rules: Anti-slop, Quality Gate, Compaction, Scope-Locking
│   └── skills/                    # Skills generated from real-world experience
│
├── 💎 plugins/                     # 9 standard modular plugin packages
│   ├── antigravity-autoharness/   # Native hooks (PreInvocation, PostToolUse) & Friction Trigger
│   ├── baoyu-creative-suite/      # [New] 13 Baoyu tools: SVG diagram, infographic, slides, translation
│   ├── elite-workflows-and-taste/ # gstack workflows: spec, plan-review, qa, ship, handoff
│   ├── antigravity-kit-plugin/    # Clean code, API patterns, TDD, DB design, UI-UX Pro Max
│   ├── cloudflare-suite/          # Full serverless: Workers, Wrangler, Agents SDK, Durable Objects
│   ├── developer-power-skills/    # Advanced office (docx/xlsx/pptx/pdf), MCP builder, sandbox
│   ├── modern-web-guidance-plugin/# Modern web best practices & Chrome Extensions
│   ├── openspec-plugin/           # OpenSpec specification and software change management
│   ├── chrome-devtools-plugin/    # Interactive testing via Chrome DevTools MCP
│
├── 🎯 skills/                      # 7 standalone skills for operations & SecondBrain
│   ├── tra-cuu-sop/               # Look up operating procedures & incident runbooks
│   ├── soan-bien-ban-hop/         # Turn raw notes into professional meeting minutes
│   ├── lap-checklist-ca/          # Generate shift-handover checklists with checkboxes
│   ├── xu-ly-van-phong/          # Draft reports and official documents in Vietnamese administrative format
│   ├── tu-van-phap-luat/          # Cite Vietnamese legal normative documents
│   ├── viet-chuyen-nghiep/        # AI newsroom: sharp, professional Vietnamese editing
│   └── cham-soc-may-tinh/         # Optimize, clean and maintain Windows PCs
│
├── 🧠 Knowledge lifecycle (Obsidian):
│   ├── 10-inbox/                  # Funnel for raw documents and quick notes
│   ├── 20-sources/                # Original references, material extracted from the inbox
│   ├── 30-working/                # Workspace: running projects, shift checklists
│   ├── 40-knowledge/              # Core truth: SOPs, P1–P4 runbooks
│   ├── 50-outputs/                # Published deliverables: reports, handover documents
│   └── 90-archive/                # Historical archive of earlier periods
│
├── ⚡ scripts/                      # One-click automation tools
├── 📋 AGENTS.md                     # Natural-language intent router (intent classifier)
├── 🧭 SOUL.md                       # Operating philosophy & AI ethics
└── 📖 README.md                     # User guide
```

> The knowledge folders and skill names stay in Vietnamese (e.g. `tra-cuu-sop`) because they are identifiers used by the agent; only the documentation is translated.

---

## 🚀 3. Quickstart (1-Click Install)

### Option 1: Use Directly as a Workspace (Recommended)
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/super-antigravity.git
   cd super-antigravity
   ```
2. Open the folder with **Google Antigravity IDE** or **Cursor / VS Code**.
3. Open it with **Obsidian** (`Open folder as vault`) to use the visual knowledge-linking features.
4. Run the environment setup script on Windows:
   ```powershell
   .\scripts\setup-windows.ps1
   ```

### Option 2: Install Plugins Globally into Antigravity
To use all 9 SUPER-ANTIGRAVITY plugins for every project on your machine:
```powershell
# Run the one-click install script
.\scripts\install-plugins-global.ps1
```

---

## 💬 4. Natural-Language Control (Vietnamese or English)

Just talk naturally; the ecosystem activates the right module automatically:

* *"Write a spec for the new feature"* ➔ activates `spec` (Elite Workflows).
* *"Review this idea from a CEO's perspective"* ➔ activates `plan-ceo-review`.
* *"Review the technical architecture and system load"* ➔ activates `plan-eng-review`.
* *"Find bugs and test the UI"* ➔ activates `qa`.
* *"Ship this feature to git"* ➔ activates `ship`.
* *"Create a handoff document"* ➔ activates `handoff`.
* *"Look up the request-intake procedure and SLA"* ➔ activates `tra-cuu-sop`.
* *"Draft minutes for this morning's briefing"* ➔ activates `soan-bien-ban-hop`.
* *"Clean up the code and refactor it"* ➔ activates `clean-code`.
* *"Draw the system architecture as dark-mode SVG"* ➔ activates `baoyu-diagram` (`baoyu-creative-suite`).
* *"Design an infographic summarizing this article"* ➔ activates `baoyu-infographic` (`baoyu-creative-suite`).
* *"Create a professional article cover image"* ➔ activates `baoyu-cover-image` (`baoyu-creative-suite`).
* *"Deploy the worker to Cloudflare"* ➔ activates `cloudflare-suite`.

---

## 🤝 5. Contributing

All contributions that improve the SUPER-ANTIGRAVITY framework are welcome! Please read [CONTRIBUTING.en.md](CONTRIBUTING.en.md) for:
- Pull Request standards.
- Knowledge-lifecycle preservation rules (Zero-Pollution).
- Full-Output standards for code contributions.

---

## 📄 6. License

Released under the **MIT License**. Free to use, modify and share for personal and commercial purposes.
