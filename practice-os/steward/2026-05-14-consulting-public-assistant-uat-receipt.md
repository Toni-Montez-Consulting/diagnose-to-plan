---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Consulting Public Assistant UAT Receipt

## Metadata

- Work item: Consulting Public Assistant V0 no-runtime UAT
- Repo / lane: `consulting` public assistant boundary, DTP assistant manifest
- Date: 2026-05-14
- Operator: Codex for Toni
- Reviewer: Toni
- UAT type: ai_workflow | public_route
- Kaizen closure: `kzn-20260514-run-second-wave-uat-kit-v0-pilots-defd92f1`
- Related requirements brief: `docs/assistant-manifests/consulting-public-v0.md`
- Related decision ledger: `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md`
- Related Integrity Gate: `practice-os/templates/pre-ship-integrity-gate.md`
- Related proof / redaction / permission gate:
  `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md`,
  `practice-os/policies/redaction-policy.md`

## Claim Under Review

- Claim: The consulting public assistant lane is ready as an accepted
  no-widget, no-runtime QA boundary and source-corpus gate.
- Claim level: internal_pattern
- What this UAT can prove:
  - The DTP assistant manifest defines approved public sources, blocked private
    sources, refusal behavior, logging limits, handoff route, and launch gates.
  - The consulting repo has source-corpus and refusal-fixture QA that passes.
  - The current consulting public routes build and route-test successfully.
- What this UAT cannot prove:
  - It does not prove a widget, endpoint, retrieval index, hosted assistant, or
    production runtime is ready.
  - It does not approve private retrieval, raw message logging, public proof
    claims, scheduling, intake submission, or any write action.
  - It does not prove visitor usefulness until a runtime prototype exists and
    is tested separately.

## Journey

- User / operator: Future visitor asks a public question about Toni's services,
  proof boundaries, work examples, or next step.
- Starting point: DTP assistant manifest and consulting repo no-widget QA docs.
- Main path:
  1. Assistant scope is checked against the accepted manifest.
  2. Answer sources are limited to approved public consulting routes.
  3. Private, unsupported, action-taking, or advice requests are refused or
     redirected.
  4. Handoff remains `/start`.
  5. Runtime work stays blocked until a separate launch gate accepts provider,
     rate limit, logging, smoke tests, and UI.
- Expected outcome: The assistant lane is safe to keep as a pre-code boundary
  and future implementation input.
- Expected next action: Do not build runtime yet. If reopened, create a
  runtime-owner and logging decision before implementation.

## Repo Gates

| Command or check | Required? | Result | Evidence or note |
|---|---|---|---|
| `npm run assistant:qa` in `consulting` | yes | pass | source corpus routes, blocked private sources, refusal fixture coverage, and no-widget launch boundary passed |
| `CONSULTING_PLAYWRIGHT_PORT=4322 npm run test:routes` in `consulting` | yes | pass | 34/34 route, layout, admin, sitemap, contact, post-submit, and advisory axe checks passed |
| `npm run build` in `consulting` | yes | pass | sequential rerun passed after an earlier parallel build/test race; Astro check reported 0 errors, 0 warnings, 0 hints |
| `npm run doctor` in `consulting` | yes | pass | assistant QA docs, Playwright config, gitleaks, env example, and admin private-key guard passed |
| `npm run security:secrets` in `consulting` | yes | pass | gitleaks scanned about 5.89 MB; no leaks found |

## Manual UAT

| Area | Result | Evidence or note |
|---|---|---|
| Core journey | pass_with_caveats | the pre-code assistant journey is defined; no runtime exists yet |
| Mobile / small screen | pass | route tests covered public routes on mobile |
| Desktop / wide screen | pass | route tests covered public routes on desktop |
| Error states | skipped | no runtime error states exist yet |
| Empty states | skipped | no assistant UI state exists yet |
| Auth / permissions | pass | public assistant is constrained to public anonymous/rate-limited future scope; private sources are blocked |
| Data / privacy | pass_with_caveats | no raw message logging or sensitive data collection is approved |
| AI output review | pass_with_caveats | refusal fixtures and public corpus exist; real assistant outputs need future runtime QA |
| Handoff clarity | pass | `/start` remains the human-owned handoff route |

## Quality And Integrity

- Truth: The lane is described as accepted pre-code/no-widget only. No runtime
  capability is implied.
- Usefulness: The manifest and QA docs make future assistant work safer by
  bounding sources, refusals, handoff, and launch gates.
- Restraint: No widget, endpoint, vector index, hosted runtime, provider,
  logging system, or automation was added.
- Durability: The boundary is testable through `npm run assistant:qa` and
  consulting route checks.
- Handoff: A future builder can see what is allowed, blocked, and required
  before runtime implementation.
- AI usage, if relevant: AI behavior remains planned and bounded; no live AI
  feature is treated as shipped.

## Evidence And Caveats

- Evidence pointers:
  - `docs/assistant-manifests/consulting-public-v0.md`
  - `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md`
  - `consulting/docs/ASSISTANT_PUBLIC_V0_QA_CHECKLIST.md`
  - `consulting/docs/ASSISTANT_PUBLIC_V0_SOURCE_CORPUS.md`
  - `consulting/docs/ASSISTANT_PUBLIC_V0_REFUSAL_FIXTURES.md`
  - `consulting/scripts/verify/assistant-public-v0.mjs`
- Screenshots or logs, if redacted: none added.
- Known limitations:
  - no runtime owner, model/provider, rate limit, logging policy, UI, widget
    smoke test, or production assistant exists;
  - no visitor usefulness evidence exists;
  - no public proof claim is authorized.
- Manual gates still open:
  - runtime-owner decision;
  - no-raw-message logging policy;
  - provider/model/rate-limit decision;
  - route/widget smoke tests;
  - manual output QA after a prototype exists.
- Cleanup debt: none in this slice.
- Privacy / proof boundary: internal-only until runtime and public proof gates
  are separately accepted.

## Decision

- Decision: pass_with_caveats
- Required before ship or handoff: separate runtime implementation gate.
- Parked follow-up: public assistant runtime and any cross-site assistant
  rollout remain parked.
- Owner: Toni
- Next review trigger:
  - Toni explicitly reopens assistant runtime work;
  - the source corpus changes materially;
  - another site asks for assistant behavior before consulting proves it.

## Public Proof Notes

This receipt is not public proof and does not authorize a public assistant
launch. It confirms only that the no-runtime boundary is usable as a future
implementation input.
