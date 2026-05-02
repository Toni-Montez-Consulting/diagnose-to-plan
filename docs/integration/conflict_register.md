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

## Closed Items

| Date | Source | Conflict / ambiguity | Resolution |
|---|---|---|---|
| 2026-05-02 | `AGENTS.md` Practice OS Build Appendage | The appendage named `docs/source/practice_os_build_spec_v0_1.md`, `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md`, and `database/schema/practice_os_schema_v0_1.sql`, but those files were not present in the repo yet. | Closed by copying the Markdown source files and SQL starter schema into those canonical repo paths. |

## Open Items

| Date | Source | Conflict / ambiguity | Current handling | Resolution needed |
|---|---|---|---|---|
| 2026-05-02 | `database/schema/practice_os_schema_v0_1.sql` | Starter schema is broader than current Hosted DTP Phase 0 in some places and lighter in others. It lacks the accepted RLS/storage/import-export/redaction/proof-review detail from current DTP docs. | Treat as schema source material only, not a migration. | Reconcile against `docs/HOSTED_DTP_PHASE_0.md` before any database implementation. |
| 2026-05-02 | Source docs V1 app direction | Source docs mention a Next.js/Supabase internal app, while current DTP remains Python CLI/local Workbench until hosted implementation is explicitly opened. | Preserve current DTP architecture. | Create a separate hosted-DTP implementation plan before app work. |
| 2026-05-02 | Future client viewer / portal | Source docs include future client viewer needs, while current roadmap blocks client-facing portal work until repeated client patterns prove need. | Keep client portal out of current scope. | Revisit only after repeated client-facing handoff/value-ledger needs appear. |
| 2026-05-02 | AI-assisted drafting/tracing | Source docs name AI-assisted drafting, tracing, and memory suggestions, while current DTP blocks autonomous agents and unmanaged self-learning. | Keep AI assistance draft-only and human-approved. | Add eval/refusal/memory-review gates before any assistant or tracing runtime. |
