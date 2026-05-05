# Weekly Operator Cockpit - 2026-05-05

Purpose: choose what gets touched this week, what stays status-only, and what must not be touched.

## Week

- Week of: 2026-05-05
- Operator: Toni with Codex
- Source report: `docs/WORKSPACE_ROADMAP_AND_PLANNING_REPORT_2026-05-05.md`

## Allowed Lanes

| Lane | Allowed work | Done condition |
|---|---|---|
| `diagnose-to-plan` | Checkpoint current roadmap/report/proof/control-plane docs, templates, ADR, dashboard, steward artifacts, and DTP-only gates. | DTP readiness receipt records branch, commit, dirty scope, commands, results, known exceptions, and a clear decision. |
| `consulting` | Resolve or validate existing share-readiness and assistant QA dirty state only. No new site scope. | Consulting readiness receipt records branch, commit, commands, results, exceptions, and share-ready/parked/not-ready decision. |
| `tm-skills` | Inventory Azure/Foundry incubator dirty state, classify the change set, and run skill repo gates. | tm-skills readiness receipt records promoted/incubator/delete/parked decision, checks, and whether global skill behavior can be trusted. |

## Status-Only Lanes

| Lane | Current state | Next check |
|---|---|---|
| `diagnose-to-plan/engagements` | Clean on `main...origin/main`; private waiting-state lane only. | Recheck on next real client/owner reply before build, scheduling, or proof movement. |
| `hub` | `main...origin/main` with untracked `docs/PR68_TAILWIND4_MIGRATION_PLAN.md`; PR #68 remains parked. | Recheck only when Hub PR #68/Tailwind work is explicitly reopened. |
| `ccaap-site` | Clean on `main...origin/main`; production waits on owner inputs and Cloudflare path. | Recheck after Leah/Tony owner inputs or deploy-path decision. |
| `fitness-app` / Omnexus | Clean on `main...origin/main`; Stripe support lane remains parked. | Recheck only if Omnexus support or proof lane is explicitly reopened. |
| `demario-pickleball-1` | Clean on `master...origin/master`; proof remains permission-gated. | Recheck after owner/admin launch proof or proof request. |
| `FamilyTrips` | Clean on `main...origin/main`; static/casual privacy lane remains intentional. | Recheck on concrete trip/event/privacy request. |
| `architected-strength` | Clean on `main...origin/main`; public signal lane only. | Recheck on personal-brand proof/craft or assistant-pattern request. |
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
| New consulting site scope | Current dirty work must be closed first. | Consulting readiness receipt marks existing share-readiness/assistant QA lane stable or parked. |

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
| DeMario Command Room | Reference implementation only. | Review/testimonial evidence, screenshot permission, redaction, reviewer, launch context. |
| Hub/intake | Runtime evidence only. | Live proof, cleanup record, permissioned public framing, no private rows. |
| Architected Strength assistant pattern | Later candidate. | Accepted manifest, source corpus, refusal tests, logging, handoff, route smoke. |

## This Week's Focus

- One thing to finish: turn the current DTP control-plane state into a checkpoint with receipts and gate results.
- One thing not to touch: public proof publishing or new consulting-site scope.

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
