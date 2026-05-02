---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Integration Conflict Register

Use this register when new source material, thesis docs, schema drafts, or
implementation prompts conflict with existing DTP architecture, decisions, or
repo conventions.

## Open Items

| Date | Source | Conflict / ambiguity | Current handling | Resolution needed |
|---|---|---|---|---|
| 2026-05-02 | `AGENTS.md` Practice OS Build Appendage | The appendage names `docs/source/practice_os_build_spec_v0_1.md`, `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md`, and `database/schema/practice_os_schema_v0_1.sql`, but those files are not present in the repo yet. | Preserve the appendage as additive guidance; use existing DTP docs, ADRs, and working architecture until the source files are added or mapped. | Add the source files, map them to existing docs, or record a decision that supersedes/renames the referenced paths. |
