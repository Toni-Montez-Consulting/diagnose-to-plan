---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Workspace OS And UAT Rollout Agent Flight Record

## Session

- Goal: Capture the Consulting Workspace OS, Requirements Gatherer, Integrity
  Layer, UAT Kit, and first UAT pilot rollout as a reusable agent-session record.
- Date: 2026-05-14
- Agent/tool: Codex for Toni
- Repos touched:
  - `diagnose-to-plan` for canonical docs, templates, pattern candidates, and
    steward receipts.
  - `consulting` as evidence source and verification target only.
- Branches and PRs:
  - PR #67: `docs/consulting-workspace-os-protocols`
  - PR #68: UAT Kit V0
  - PR #69: first consulting live-funnel UAT pilot
  - PR #70: second-wave consulting public-assistant and admin-command-room UAT
    pilots
- Reviewer: Toni

## Work Performed

- Added Consulting Workspace OS V0 as the DTP-owned source of truth for
  Requirements Gatherer, Integrity Layer, pattern loop, and UAT Kit sequencing.
- Added Requirements Gatherer V1 protocol and templates for build-ready briefs
  and decision ledgers.
- Added Integrity Layer craft standard and Pre-Ship Integrity Gate.
- Created four internal consulting pattern candidates from live-funnel,
  Diagnostic Call, admin boundary, and proof-readiness evidence.
- Added UAT Kit V0 plus reusable UAT receipt template.
- Ran three UAT receipts:
  - consulting live-funnel / proof-readiness;
  - consulting public assistant no-widget / no-runtime boundary;
  - consulting `/admin` noindex command-room boundary.
- Reviewed UAT receipt friction before creating variants or global skill
  behavior.

## Evidence Produced

- `docs/CONSULTING_WORKSPACE_OS_V0.md`
- `docs/UAT_KIT_V0.md`
- `practice-os/templates/requirements-gathering-brief.md`
- `practice-os/templates/requirements-decision-ledger.md`
- `practice-os/policies/integrity-layer-craft-standard.md`
- `practice-os/templates/pre-ship-integrity-gate.md`
- `practice-os/templates/uat-receipt.md`
- `practice-os/steward/2026-05-14-consulting-live-funnel-uat-pilot-receipt.md`
- `practice-os/steward/2026-05-14-consulting-public-assistant-uat-receipt.md`
- `practice-os/steward/2026-05-14-consulting-admin-command-room-uat-receipt.md`
- `practice-os/steward/2026-05-14-uat-receipt-friction-review.md`

## Verification

Passed during the rollout:

- DTP practice doctor.
- DTP skills validation.
- `ruff check .`
- `git diff --check`
- targeted DTP redaction checks for changed markdown/JSONL files.
- gitleaks through the commit hook where commits were made.
- consulting `npm run build`.
- consulting route tests.
- consulting assistant QA.
- consulting doctor.
- consulting verification matrix.
- consulting secret scan.

Skipped or intentionally out of scope:

- public consulting copy changes;
- Hub runtime changes;
- hosted DTP changes;
- production writes;
- private engagement vault changes;
- `tm-skills` mutation;
- public proof promotion;
- client communication or calendar action.

## Failures Or Misfires

- Local PowerShell did not have `dtp` on PATH in this later session. Use
  `.venv\Scripts\dtp.exe` from the DTP repo when PATH is not hydrated.
- Consulting build and route checks should not run in parallel when route tests
  depend on generated `dist` output. A concurrent build can clean the output
  while tests are reading it. Run build first, then route/browser checks.
- DTP redaction check is simplest when run on one changed file at a time.

## Lessons

- `pass_with_caveats` is the right default decision shape for internal
  operational confidence that still has proof, runtime, client, or cleanup
  gates open.
- Requirements Gatherer, Integrity Layer, and UAT Kit work best as a chain:
  understand the work, check the standard, then record acceptance evidence.
- DTP should own the protocol until repeated use proves stable triggers and
  expected outputs. `tm-skills` should receive behavior only after there are
  eval candidates and misfire history.
- Boundary-only UAT is real UAT. It should prove what is intentionally not
  allowed, not pretend a runtime or proof claim exists.

## Eval Candidates

- Prompt asks for a meaningful public/client/operator change with unclear
  acceptance: agent should invoke Requirements Gatherer before implementation.
- Prompt asks whether something is ready: agent should choose UAT Kit and name
  claim level before checking evidence.
- Prompt tries to convert internal evidence into public proof: agent should
  route to proof/redaction gates and refuse unsupported claims.
- Prompt asks to create a skill after one pilot: agent should require repeated
  DTP-reviewed examples before `tm-skills` promotion.
- Prompt runs build and browser checks together: agent should prefer sequential
  build then route/browser checks unless repo docs allow parallel execution.

## Follow-ups

1. Use one more meaningful UAT receipt outside the current consulting boundary
   set before creating a narrower UAT template.
2. Run client reply intake on the next real Cam, Greg, or CCAAP reply before
   Notion, calendar, build, or proof movement.
3. Reopen Omnexus release proof only with live App Store/current-state
   verification.
4. Reopen Hub cleanup only as a Hub-local runtime/dependency task, not as part
   of DTP docs work.
5. Consider `tm-skills` promotion only after repeated DTP-reviewed examples,
   expected outputs, and trigger/misfire evidence exist.

## Safety Notes

This record contains no secrets, raw private records, Hub rows, client data,
private screenshots, access tokens, or public proof claims.

