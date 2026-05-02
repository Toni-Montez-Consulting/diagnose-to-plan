---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice OS Source Index

This index records the additive source material integrated on 2026-05-02.

These files preserve strategic thinking. Do not rewrite, dilute, or flatten
them into generic SaaS or generic AI-consulting language. Convert them into
integration maps, ADRs, backlog items, templates, or implementation specs
instead.

## Source Files

| Source | Original location | Repo location | Purpose | Authority |
|---|---|---|---|---|
| Practice OS Build Spec v0.1 | `C:\Users\tonimontez\Downloads\practice_os_build_spec_v0_1.md` | `docs/source/practice_os_build_spec_v0_1.md` | Internal Practice OS product/source spec for the capture -> learn loop and MVP modules. | Additive source material; not an implementation override by itself. |
| AI Implementation Layer Thesis And Build Spec v0.1 | `C:\Users\tonimontez\Downloads\ai_implementation_layer_thesis_and_build_spec_v0_1.md` | `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md` | Company thesis, market framing, operating beliefs, offer architecture, and repeated Practice OS build spec. | Additive source material; preserve strategic nuance. |
| Practice OS Schema v0.1 | `C:\Users\tonimontez\Downloads\practice_os_schema_v0_1.sql` | `database/schema/practice_os_schema_v0_1.sql` | Starter schema for clients, engagements, raw inputs, intent briefs, questions, assumptions, workflows, opportunities, specs, tasks, exceptions, value metrics, memory, decisions, and runbooks. | Schema starter only; not a runnable migration until reconciled with Hosted DTP Phase 0. |
| AI Implementation Layer Thesis DOCX | `C:\Users\tonimontez\Downloads\AI_Implementation_Layer_Thesis_and_Build_Spec_v0.1.docx` | Not committed by default. | Archival duplicate of the Markdown thesis/spec. | External archival source unless Toni explicitly asks to version the binary. |

## Source-Of-Truth Order

When these sources conflict with existing implementation or decisions, use the
order already recorded in `AGENTS.md`:

1. Current `AGENTS.md`.
2. Existing working repo architecture.
3. ADRs / decision records.
4. `docs/source/practice_os_build_spec_v0_1.md`.
5. `database/schema/practice_os_schema_v0_1.sql`.
6. `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md`.

## Integration Rule

- Preserve the source files.
- Map concepts into integration docs before implementation.
- Record ADRs in `decisions/`; `docs/adr/README.md` exists only as a pointer
  because DTP's established convention is ADR-lite decision records.
- Prefer additive templates/docs before code.
- Keep DTP local-first until hosted implementation is explicitly opened.
- Keep durable memory human-approved.
- Keep client-facing portal, autonomous agents, and unmanaged self-learning
  blocked until separate gates are accepted.
