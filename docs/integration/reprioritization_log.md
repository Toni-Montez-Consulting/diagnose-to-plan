---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Reprioritization Log

Use this log after meaningful Practice OS changes so backlog movement is
deliberate and visible.

## 2026-05-02: Source Material Closeout And Template Pass

Source:

- `docs/source/practice_os_build_spec_v0_1.md`
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md`
- `database/schema/practice_os_schema_v0_1.sql`
- `docs/HOSTED_DTP_PHASE_0.md`
- Current Cam, Greg, and CCAAP reply-state checks

Change:

- Added manual templates for Thought Inbox, Input Studio, Context Pack,
  Opportunity Score, Exception Register, Value Ledger, and Memory Review Queue.
- Added schema reconciliation planning against Hosted DTP Phase 0 without
  running SQL or implementing hosted DTP.
- Added steward/evidence closeout for the source-material/control-plane sprint.
- Piloted the template set on a sanitized weekly Business Brain reset.

Priority impact:

1. Module templates are now Done as manual assets, not doctor-required gates.
2. First real Practice OS template pilot is Active next.
3. Schema reconciliation doc is Done, but merged schema design remains Ready.
4. QuickBooks remains Blocked until connector boundary, credentials, and
   source-of-truth rules are accepted.
5. Hosted DTP app/schema implementation remains Later/Gated.

Next review trigger:

- Cam sends the requested item packet.
- Greg replies with discovery availability.
- Leah/Tony clarify CCAAP owner inputs.
- Toni explicitly reopens hosted schema/app work.
- Two Business Brain reset cycles reveal which templates deserve stricter
  enforcement.

## 2026-05-02: Source Thesis/Spec/Schema Integrated

Source:

- `docs/source/practice_os_build_spec_v0_1.md`
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md`
- `database/schema/practice_os_schema_v0_1.sql`

Change:

- Preserved the new source material in canonical DTP paths.
- Added a source index, integration map, concept registry, and source-material
  ADR.
- Closed the missing-source-file conflict and opened narrower schema/app/portal
  integration conflicts for future resolution.

Priority impact:

1. Source preservation is complete for this slice.
2. Integration mapping is the current control layer.
3. Schema reconciliation against Hosted DTP Phase 0 is now Ready, not active.
4. Thought Inbox / Input Studio module templates are the next additive product
   slice.
5. Hosted app implementation remains gated and separate.

Next review trigger:

- Toni approves the next module-template slice.
- Hosted DTP schema/app implementation is explicitly reopened.
- A client cycle produces real inputs for Thought Inbox, Input Studio,
  Opportunity Scoring, Exception Register, Value Ledger, or Memory Review.

## 2026-05-02: Practice OS Build Appendage Added

Source: `AGENTS.md`

Change:

- Added additive Practice OS product guidance to the DTP root agent
  instructions.
- Preserved the existing repo boundary that `CLAUDE.md` remains required
  reading for DTP work.
- Recorded the current gap that the newly referenced source/spec/schema files
  are not present yet.

Priority impact:

- Keep DTP as the internal Practice OS source of truth.
- Treat the named source docs and schema as pending inputs until they are added
  or mapped.
- Continue implementing scoped additive slices from the current DTP
  architecture instead of restructuring around absent source files.

Next review trigger:

- A new source thesis/spec/schema file is added.
- Hosted DTP/schema work resumes.
- A future implementation prompt relies on the newly referenced source paths.
