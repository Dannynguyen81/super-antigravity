**🌐** [🇻🇳 Tiếng Việt](CONTRIBUTING.md) · 🇬🇧 English

# 🤝 Knowledge Contribution Guide — SecondBrain (CONTRIBUTING)

Welcome to everyone helping to build and extend the SecondBrain digital knowledge base! The system follows the **Knowledge Lifecycle Model**, ensuring safety, consistency and transparency.

---

## 🔄 1. Promotion Lifecycle

Every document in the repository moves through 4 value tiers:

```text
[10-inbox] ─────► [30-working] ─────► [40-knowledge] ─────► [50-outputs]
 (Raw intake)      (Draft)             (Approved)            (Deliverable)
```

1. **Intake (`10-inbox/`)**: drop raw documents and quick notes here.
2. **Drafting (`30-working/`)**: create drafts, forms and minutes with `status: draft`.
3. **Approval (`40-knowledge/`)**: after peer review and sign-off by a leader/expert, a document is promoted to `40-knowledge/` with `status: approved`.
4. **Packaging (`50-outputs/`)**: final summary reports, official letters or submission files are stored in `50-outputs/`.

---

## 🌿 2. Contribution Workflow via Git & GitHub

### Step 1: Create a new branch
- New procedure/document: `feature/them-[document-name]`
- Fix an existing procedure: `hotfix/sua-[code]`
- Update a form/checklist: `docs/cap-nhat-[form-name]`

### Step 2: Write from the standard templates
- Always copy from the matching `_templates/` folder (e.g. `40-knowledge/_templates/mau-quy-trinh-sop.md` or `30-working/_templates/mau-checklist-ca.md`).
- The YAML frontmatter must be fully filled in:
  ```yaml
  ---
  id: DOCUMENT-CODE
  title: Document title
  version: 1.0
  status: draft # Always draft when newly created
  author: Author name
  approver: Approver
  tags: [topic, category]
  ---
  ```

### Step 3: Check integrity before submitting
Run the check script to make sure there are no broken links or missing metadata:
```powershell
python scripts/kiem-tra-suc-khoe-brain.py
```

### Step 4: Open a Pull Request (PR)
- Push the branch to GitHub and open a Pull Request.
- Describe clearly: what changed, why, and name the PR reviewer.

---

## 🔒 3. Absolute Security Rules (Zero-Leak)

1. **Never commit sensitive information**:
   - Never store passwords, API keys or personal access tokens in Markdown files.
   - Environment variables and personal config belong in a `.env` file (blocked by `.gitignore`).
2. **Protect personal and partner data**:
   - When adding documents or minutes to the repository, hide/encrypt any sensitive details that are not needed.
