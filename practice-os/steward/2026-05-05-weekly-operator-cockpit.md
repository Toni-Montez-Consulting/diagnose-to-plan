# Weekly Operator Cockpit - 2026-05-05

Purpose: choose what gets touched this week, what stays status-only, and what must not be touched.

## Operator Reprioritization Addendum

New signal from Toni on 2026-05-05: DeMario's pickleball site is live, the feedback is strong, and Toni wants a LinkedIn/social post path. Omnexus is approved on the App Store, but the first subscription products were declined/not approved. Toni also wants to fix the consulting site and finish/fix Architected Strength without losing the plot.

Live git refresh at intake:

- `consulting`: clean on `main...origin/main`.
- `diagnose-to-plan`: clean on `main...origin/main` before this addendum.
- `architected-strength`: clean on `main...origin/main`.
- `demario-pickleball-1`: clean on `master...origin/master`.

Straight-and-narrow queue:

1. DeMario launch-feedback social/proof packet: draft, evidence, permission, redaction, caveat, and final channel copy before posting.
2. Omnexus subscription-review resubmission: fill `fitness-app/docs/ops/app-store-subscription-resubmission-checklist-2026-05-05.md` from exact App Store Connect status/reviewer detail, then decide manual resubmission versus code branch.
3. Consulting public-site fix/readiness pass: Hub-first intake, route/build checks, visual QA, proof posture, and Steel Ledger preservation before redesign.
4. Architected Strength P0/P1 finish/fix pass: public signal, claim hygiene, positioning, craft, and repo-local gates before assistant-pattern work.

## Week

- Week of: 2026-05-05
- Operator: Toni with Codex
- Source report: `docs/WORKSPACE_ROADMAP_AND_PLANNING_REPORT_2026-05-05.md`

## Allowed Lanes

| Lane | Allowed work | Done condition |
|---|---|---|
| `diagnose-to-plan` | Checkpoint current roadmap/report/proof/control-plane docs, templates, ADR, dashboard, steward artifacts, and DTP-only gates. | DTP readiness receipt records branch, commit, dirty scope, commands, results, known exceptions, and a clear decision. |
| `consulting` | Run a focused public-site fix/readiness pass: Hub-first intake, visual QA, route/build checks, proof posture, and Steel Ledger preservation. | Consulting readiness receipt records branch, commit, commands, results, exceptions, and share-ready/parked/not-ready decision. |
| `demario-pickleball-1` plus DTP proof lane | Prep social/proof package only; do not publish, scrape private admin data, or move screenshots without owner approval. | LinkedIn/social packet has owner-approved wording, source/testimonial evidence, redacted screenshots, launch context, caveat, and final human-posted copy. |
| `fitness-app` / Omnexus | App Store Connect subscription-review support: inspect status/reviewer message, subscription metadata, screenshots, availability, and whether first subscriptions need a new app version. | A resubmission checklist names whether this is manual App Store Connect work, a new build/version submission, or a real code patch. |
| `architected-strength` | Run or prepare a P0/P1 public-signal finish/fix pass, keeping it separate from consulting and employer/private material. | Repo-local gates pass and DTP records whether it remains a north-star candidate or is ready for reference promotion review. |
| `tm-skills` | Inventory Azure/Foundry incubator dirty state, classify the change set, and run skill repo gates. | tm-skills readiness receipt records promoted/incubator/delete/parked decision, checks, and whether global skill behavior can be trusted. |

## Status-Only Lanes

| Lane | Current state | Next check |
|---|---|---|
| `diagnose-to-plan/engagements` | Clean on `main...origin/main`; private waiting-state lane only. | Recheck on next real client/owner reply before build, scheduling, or proof movement. |
| `hub` | `main...origin/main` with untracked `docs/PR68_TAILWIND4_MIGRATION_PLAN.md`; PR #68 remains parked. | Recheck only when Hub PR #68/Tailwind work is explicitly reopened. |
| `ccaap-site` | Clean on `main...origin/main`; production waits on owner inputs and Cloudflare path. | Recheck after Leah/Tony owner inputs or deploy-path decision. |
| `FamilyTrips` | Clean on `main...origin/main`; static/casual privacy lane remains intentional. | Recheck on concrete trip/event/privacy request. |
| `hub-prompts` | Clean on `main...origin/main`; prompt catalog stable. | Recheck on prompt behavior change or misfire-to-fixture pass. |
| `hub-registry` | Clean on `main...origin/main`; registry stable. | Recheck on trigger/target/dispatch change. |
| `engineering-playbook` | Clean on `main...origin/main`; doctrine/reference only. | Recheck on general doctrine or portfolio-policy change. |

## Blocked Or Do-Not-Touch Lanes

| Lane | Reason | Unlock condition |
|---|---|---|
| Public proof publishing | Proof candidates still need evidence, permission, redaction, reviewer, and caveat. | DTP proof queue item passes all promotion gates. |
| Hub-as-CRM / Hub-as-DTP | ADR 0009 keeps Hub as runtime support only. | Separate accepted boundary decision and explicit implementation approval. |
| Autonomous client communications | Relationship, consent, rollback, and audit model are not accepted. | Explicit client-consent and review workflow decision. |
| QuickBooks writes or live imports | Finance/records risk is too high. | Read-only connector readiness, credential model, and owner approval. |
| Write-enabled cross-repo runner | Workspace command center remains read-only. | Separate accepted decision authorizes live git/CI reads or command execution. |
| Broad consulting redesign or proof replacement | Focused readiness/fix work is allowed, but stronger public proof and redesign still need evidence, permission, redaction, reviewer, caveat, and accepted scope. | Consulting readiness pass is clean and a DTP proof item is approved for exact public copy/assets. |

## Dirty Worktrees

| Repo | Branch | Dirty scope | Decision |
|---|---|---|---|
| `diagnose-to-plan` | `main...origin/main` | Control-plane report/templates/ADR, proof queue, offer matrix, dashboard, gate ledger, roadmap/horizon/runbook updates, steward artifacts, fixture/pattern additions. | fix now |
| `consulting` | `main...origin/main` | Share-readiness docs, assistant QA docs/script, package scripts, doctor/matrix checks, `/start` updates. | fix now |
| `tm-skills` | `main...origin/main` | Azure/Foundry skill modifications, deleted eval artifacts, and untracked Azure skill folders. | park or accept only after gate results |
| `hub` | `main...origin/main` | Untracked PR #68 Tailwind migration plan. | park |

## Client Waiting States

| Client or lane | Waiting on | Next action | Earliest follow-up |
|---|---|---|---|
| Cameron / SMB marketplace | Requested packet or direct owner/client input. | Run DTP reply intake before repo access, scheduling, build, or proof movement. | On next reply. |
| Greg / TheGrantApp | Reply or approved discovery cadence. | Update private kit first, then decide whether discovery/case-study lane activates. | On next reply or explicit cadence decision. |
| CCAAP / Mom nonprofit | PayPal/contact/DNS/assets/review/proof decisions from Leah/Tony. | Keep `ccaap-site` status-only until owner inputs land. | On owner response. |

## Proof Gates

| Candidate | Current gate | Missing before public use |
|---|---|---|
| CCAAP site refresh | Internal-only proof candidate. | Owner permission, reviewer, after-state evidence, redaction, caveat. |
| Omnexus App Store journey | Reference pattern only. | Proof permission, source review, redaction, reviewer, public-safe caveat. |
| DeMario launch-feedback social packet | Active social/proof prep candidate. | Mario-approved wording, review/testimonial source evidence, screenshot permission, private admin redaction, reviewer, launch context, caveat, and final channel copy. |
| DeMario Command Room | Reference implementation only. | Review/testimonial evidence, screenshot permission, redaction, reviewer, launch context. |
| Omnexus subscription-review state | App is approved, subscriptions declined/not approved. | Exact App Store Connect product status, reviewer message, metadata/screenshot/availability check, and new app version attachment if first subscriptions. |
| Hub/intake | Runtime evidence only. | Live proof, cleanup record, permissioned public framing, no private rows. |
| Architected Strength assistant pattern | Later candidate. | Accepted manifest, source corpus, refusal tests, logging, handoff, route smoke. |

## This Week's Focus

- One thing to finish: create a viewable dashboard from DTP's read-only report and Kaizen queue so Toni can see the active lanes without holding them in memory.
- One thing not to touch: public proof publishing, private admin screenshots, or broad site redesign before the gates are real.

## Validation Notes

- Required checks: DTP gates first, then consulting gates, then tm-skills gates.
- Manual checks: client one-pager stays generic and client-safe; status-only lanes remain unmodified.
- Evidence receipts: `2026-05-05-dtp-control-plane-readiness-receipt.md`, `2026-05-05-consulting-share-readiness-receipt.md`, `2026-05-05-tm-skills-azure-incubator-readiness-receipt.md`.

## Cycle Results

| Lane | Result | Decision |
|---|---|---|
| `diagnose-to-plan` | DTP gates passed; worktree dirty state is documented. | accepted with documented dirty state |
| `consulting` | Build, assistant QA, route tests, doctor, matrix, secret scan, and diff check passed; live Hub intake smoke not run. | parked with named manual gates |
| `tm-skills` | Freshness and install preview passed; doctor failed on missing evals, unexpected frontmatter, and unexpected untracked skill directories. | not ready |
| Status-only lanes | Live status captured without repo-local edits. | unchanged |
| Client-safe translation | Generic one-page roadmap candidate created without live client details. | candidate only |
