---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Iteration 1 Brain Completion Implementation

## Trigger

Toni asked to implement the Iteration 1 Brain Completion Roadmap and shift the
practice from planning into stronger operating-brain infrastructure.

## Scope

- Make memory a first-class DTP health surface.
- Start Hosted DTP Phase 0 as schema/app-shell infrastructure, not dashboard
  theater.
- Seed Business Brain weekly operating and consulting-intelligence eval
  fixtures.
- Close obvious workspace-report and verification blockers.
- Keep Hub, `tm-skills`, consulting, DTP, and future FAOS boundaries distinct.

## Implemented

- Added `dtp memory status` for Memory Spine V1 health checks.
- Made memory/correction and Business Brain weekly templates doctor-required.
- Added a correction checklist so broad reports produce source-promotable fixes.
- Added a Business Brain weekly operating packet.
- Added public-safe consulting intelligence fixtures and eval cases.
- Added Hosted DTP Phase 0 scaffold under `apps/private-dtp/`:
  - Supabase schema and RLS migration.
  - Private app-shell screen contract.
  - Markdown/private-kit import/export contract.
- Added DSE workspace manifest/evidence coverage while preserving COI gates.
- Tightened DTP kit status so hidden/system dirs and local sample kits do not
  pollute default status.
- Updated roadmap/evidence surfaces for the Iteration 1 brain lane.

## Boundaries Preserved

- DTP remains the source of truth.
- Notion remains mirror/inbox only.
- Hub remains runtime/intake/prompt support, not DTP methodology storage.
- `tm-skills` remains coding-agent behavior infrastructure.
- FAOS remains gated behind Phase 0A readiness review.
- Hosted DTP is schema/app-shell only in this slice; no public dashboard,
  client portal, QuickBooks write path, deep Hub sync, MCP recall, or autonomy.

## Follow-Up Gates

- Validate DTP tests, Ruff, doctor, skills validation, memory status, workspace
  report, redaction checks, and gitleaks.
- Validate Hub `pnpm verify` after `.prettierignore` cleanup.
- Run `tm-skills` doctor/freshness/install preview before claiming skill-layer
  completion for this iteration.
- Build the deployable private DTP UI only after the schema/app-shell scaffold
  is accepted and a Supabase environment is selected.
- Run FAOS Phase 0A readiness review before creating a `faos` repo, `op`
  wrapper, tracing store, or memory substrate.

## Correction Prompt

Toni should correct:

- Any lane that should be active now but is still marked gated.
- Any infrastructure component that should live in Hub rather than DTP.
- Any Business Brain fixture family that misses a key sales/delivery behavior.
- Any Hosted DTP screen that should be removed from Phase 0.
- Any proof lane whose privacy or permission posture is misclassified.
