---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Evolution Records

This folder holds reviewable evolution records created from ideas,
collaboration patterns, agent behaviors, messaging lines, research signals, or
client lessons that should mature beyond basic Kaizen capture.

Use:

```powershell
.\.venv\Scripts\dtp.exe evolution new "Keep a working ledger in strategy threads"
.\.venv\Scripts\dtp.exe evolution new --from-kaizen kzn-YYYYMMDD-slug-hash
.\.venv\Scripts\dtp.exe evolution status
.\.venv\Scripts\dtp.exe evolution dashboard
```

Rules:

- Raw capture is not playbook memory.
- Use `records/` for idea and meta-pattern evolution drafts.
- Use `practice-os/research/pattern-candidates/` for research or field-note
  pattern candidates.
- Use `dtp evolution dashboard` for a local static status dashboard generated
  from the reviewed markdown record set. It is a visibility surface, not a
  promotion engine or hosted runtime.
- Promote only after review, evidence limits, and boundary checks.
- Do not use this folder for raw private client facts, secret material,
  unsupported public claims, or autonomous agent authority.
