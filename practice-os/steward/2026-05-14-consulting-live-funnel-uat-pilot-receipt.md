---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Consulting Live Funnel UAT Pilot Receipt

## Metadata

- Work item: Consulting live-funnel and proof-readiness UAT pilot
- Repo / lane: `consulting` public route, Hub intake runtime, DTP proof-readiness
- Date: 2026-05-14
- Operator: Codex for Toni
- Reviewer: Toni
- UAT type: public_route | proof_surface | pattern_candidate
- Kaizen closure: `kzn-20260514-run-first-uat-kit-v0-pilot-on-the-ecec80e0`
- Related requirements brief: `docs/CONSULTING_WORKSPACE_OS_V0.md`
- Related decision ledger: none; this receipt records a UAT decision only
- Related Integrity Gate: `practice-os/templates/pre-ship-integrity-gate.md`
- Related proof / redaction / permission gate:
  `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md`,
  `practice-os/policies/redaction-policy.md`

## Claim Under Review

- Claim: The consulting live funnel has enough current evidence to be treated
  as internally operational for the Hub-first intake path, post-submit
  Diagnostic Call gate, noindex admin boundary, and proof-readiness receipt
  pattern.
- Claim level: production | internal_pattern
- What this UAT can prove:
  - The current consulting checkout still builds and passes local route,
    assistant, doctor, matrix, and secret-scan gates.
  - Existing live-funnel receipts show the production `/start` path could submit
    a synthetic intake to Hub, show the post-submit Diagnostic Call CTA, and
    verify the private Hub row by summarized fields.
  - The evidence is usable as internal operational confidence and as input to
    the four draft Workspace OS pattern candidates.
- What this UAT cannot prove:
  - It does not prove real prospect conversion, buyer quality, or follow-up
    quality.
  - It does not authorize public screenshots, private Hub excerpts, public case
    study claims, or public proof copy.
  - It does not prove synthetic-intake cleanup automation, because Hub still has
    no intake archive/delete route recorded in this lane.
  - It does not prove the next real prospect intake will be triaged correctly;
    that still needs the prospect-intake triage template.

## Journey

- User / operator: Prospect reaches the consulting `/start` path; Toni or a
  future operator reviews the resulting intake through the DTP workflow.
- Starting point: Public consulting site and DTP Workspace OS evidence.
- Main path:
  1. Prospect reaches `/start`.
  2. Public form remains Hub-first when configured and safe fallback when not.
  3. Normal pre-submit state does not expose the Diagnostic Call link.
  4. Post-submit state shows the approved Diagnostic Call path.
  5. Hub stores the intake record.
  6. DTP owns interpretation, route decision, proof boundary, and next artifact.
- Expected outcome: The funnel can be treated as internally ready with caveats,
  while public proof and cleanup remain gated.
- Expected next action: Use `practice-os/templates/prospect-intake-triage.md`
  on the next real prospect intake; do not rerun production synthetic intake
  until cleanup or rollback value justifies it.

## Repo Gates

| Command or check | Required? | Result | Evidence or note |
|---|---|---|---|
| `npm run build` in `consulting` | yes | pass | Astro check reported 0 errors, 0 warnings, 0 hints; 8 static pages built on 2026-05-14 |
| `CONSULTING_PLAYWRIGHT_PORT=4322 npm run test:routes` in `consulting` | yes | pass | 34/34 Playwright route, layout, admin, sitemap, contact, post-submit, and advisory axe checks passed |
| `npm run assistant:qa` in `consulting` | yes | pass | public source corpus, blocked private sources, refusal fixtures, and no-widget boundary passed |
| `npm run doctor` in `consulting` | yes | pass | Node, npm, scripts, Playwright config, gitleaks, env example, and admin private-key guard passed |
| `npm run matrix` in `consulting` | yes | pass | verification matrix printed current gate policy |
| `npm run security:secrets` in `consulting` | yes | pass | gitleaks scanned about 5.89 MB; no leaks found |
| Existing production live-funnel smoke | yes | pass_with_caveats | May 11 receipt proves synthetic production submit and summarized Hub verification; no new production submit was run in this UAT |
| DTP proof promotion | yes | hold | no public proof promotion was requested or approved |

## Manual UAT

| Area | Result | Evidence or note |
|---|---|---|
| Core journey | pass_with_caveats | Existing May 11 live receipt plus current route tests support the public intake path and post-submit state |
| Mobile / small screen | pass | route tests covered mobile route smoke and horizontal overflow checks |
| Desktop / wide screen | pass | route tests covered desktop route smoke and horizontal overflow checks |
| Error states | skipped | no new error-state manual browser run was requested; route checks cover fallback contact behavior |
| Empty states | skipped | not central to this funnel receipt |
| Auth / permissions | pass_with_caveats | `/admin` noindex and no-private-row checks passed; protected Hub verification remains private and summarized only |
| Data / privacy | pass_with_caveats | no new private data submitted; source receipts avoid raw Hub rows; synthetic cleanup debt remains |
| AI output review | pass | DTP docs and pattern candidates were reviewed as internal artifacts; no AI output was promoted to public copy |
| Handoff clarity | pass_with_caveats | DTP owns triage/proof next steps; next real intake still needs a prospect-intake triage receipt |

## Quality And Integrity

- Truth: The claim is limited to internal operational readiness with caveats.
  The receipt does not call synthetic smoke proof a public result, client proof,
  or conversion evidence.
- Usefulness: The UAT helps Toni and future agents decide whether the
  consulting funnel is safe to use as a real intake lane and pattern input.
- Restraint: No public copy, Hub runtime, production record, calendar, hosted
  DTP, or `tm-skills` behavior was changed.
- Durability: Evidence includes current local gates, existing production smoke
  receipt, source-index entry, and pattern-candidate traceability instead of
  one unrecorded demo.
- Handoff: Future operators can follow DTP source paths instead of reopening raw
  Hub data or chat history.
- AI usage, if relevant: AI assisted the receipt and synthesis; final claims are
  bounded by repo commands and existing evidence artifacts.

## Pattern Candidate Check

| Pattern candidate | UAT read |
|---|---|
| Hub-first intake with DTP source of truth | Supported as an internal pattern candidate; next proof needs a real prospect triage artifact |
| Post-submit Diagnostic Call gating | Supported by current route tests and May 11 production smoke; real buyer behavior remains unproven |
| Noindex admin command-room boundary | Supported by route tests for noindex, sitemap exclusion, and no private rows |
| Proof/readiness receipt with cleanup debt | Supported; this UAT reinforces `pass_with_caveats` as the honest decision shape |

## Evidence And Caveats

- Evidence pointers:
  - `practice-os/efficiency/consulting-evidence-index.md`
  - `practice-os/steward/2026-05-11-live-funnel-closeout-receipt.md`
  - `practice-os/steward/2026-05-11-live-intake-operator-workflow-receipt.md`
  - `practice-os/research/pattern-candidates/2026-05-14-hub-first-intake-dtp-source-of-truth.md`
  - `practice-os/research/pattern-candidates/2026-05-14-post-submit-diagnostic-call-gating.md`
  - `practice-os/research/pattern-candidates/2026-05-14-noindex-admin-command-room-boundary.md`
  - `practice-os/research/pattern-candidates/2026-05-14-proof-readiness-receipt-with-cleanup-debt.md`
  - `docs/UAT_KIT_V0.md`
- Screenshots or logs, if redacted: none added to this DTP receipt.
- Known limitations:
  - no new live production submission was run;
  - no raw Hub row, screenshot, private console capture, or private record was
    copied into DTP;
  - real prospect quality and conversion are unproven;
  - cleanup automation remains absent for intake submissions.
- Manual gates still open:
  - first real prospect intake triage;
  - public proof promotion review;
  - optional Hub intake archive/delete cleanup design if repeated smoke or ops
    friction justifies runtime work.
- Cleanup debt: one prior synthetic live-intake record remains labeled as test
  data according to the May 11 live-funnel receipt.
- Privacy / proof boundary: internal-only. This receipt is not public proof.

## Decision

- Decision: pass_with_caveats
- Required before ship or handoff:
  - none for internal operational use of the live funnel;
  - use prospect triage before acting on a real submission;
  - run proof promotion before any public proof claim.
- Parked follow-up:
  - Hub intake archive/delete cleanup remains a later Hub runtime task.
  - Visual QA, design integrity, mobile app UAT, and client handoff UAT variants
    remain deferred until repeated receipts prove the need.
- Owner: Toni
- Next review trigger:
  - first real prospect intake;
  - any public proof/public copy request using this evidence;
  - another synthetic intake smoke where cleanup or rollback matters;
  - repeated UAT receipts showing this template is too heavy or too light.

## Public Proof Notes

This receipt is not public proof by itself. It supports private operational
confidence and DTP pattern learning only. Public proof still requires source
evidence, permission, redaction, reviewer approval, and caveat.
