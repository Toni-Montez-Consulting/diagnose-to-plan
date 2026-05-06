---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Practice Roadmap Horizons 2026

Status: active horizon overlay for the practice roadmap.

Owner: `diagnose-to-plan`

Purpose: organize urgent, short-term, mid-term, and long-term work without
creating a second roadmap. This document reads from the DTP roadmap/backlog,
Kaizen queue, workspace report, proof governance, private engagement posture, and
future-state docs. It tells Toni and future agents what to do now, what to
improve next, and what remains gated until repeated manual pain proves the need.

## Operating Thesis

Run the practice as a Kaizen/Kanban operating system:

- DTP is the source of truth.
- `engagements/` is private client truth.
- `consulting` is the public proof/storefront.
- Hub is runtime support.
- Notion is a sanitized cockpit and inbox.
- Project repos remain source owners for their own products.

The strategic arc is: stabilize the control plane, preserve private client
state, turn real delivery into proof, then build larger platform, assistant, and
automation surfaces only when repeated manual pain proves the need.

## Current Now Queue

| Lane | Current state | Next action | Boundary |
|---|---|---|---|
| DTP control plane | Kaizen, deep audit, existing-system map, proof queue, offer/proof matrix, gate ledger, docs, CLI, tests, public-safe proof queue updates, and live-intake/DMARC receipts are ready for PR review | keep public DTP commits sanitized and use proof queue before public copy | public repo; no private raw text |
| Engagement vault | private nested repo is committed and pushed to the approved private vault remote | keep client-kit updates private-first and push only coherent engagement batches | private-client |
| CCAAP | waiting on owner inputs | wait; update private kit first if replies arrive | private-client; proof gated |
| DeMario social/proof prep | posted from Toni-owned LinkedIn and Instagram channels with exact public URLs recorded | keep private screenshots, metrics, testimonials, booking/admin rows, payment proof, and student data gated | human-owned public communication; private screenshots/metrics remain gated |
| Omnexus subscriptions | app version `1.0.1` is approved and `Pending Developer Release`; monthly/annual subscriptions remain `Waiting for Review` per Toni | hold developer release until subscriptions approve or Apple confirms safe release; then release and run live IAP proof, or capture exact reviewer/status evidence before changing code if rejected | App Store Connect/manual review-state first; code only if evidence shows runtime issue |
| Consulting | share-ready/proof-maturity lane has `/start` qualification, no-widget assistant QA, merged readiness work, and a passed-with-notes live intake smoke | finish human desktop/mobile taste review; add Hub intake archive/delete only if cleanup automation is needed | public-safe only |
| Architected Strength | P0/P1 public-signal finish pass merged in PR #3 with repo-local gates and visual QA | keep it as a personal-brand OS/reference candidate; reopen only for publishing, assistant-pattern, deploy, or proof work when those gates are explicit | personal-brand OS; no employer/private material |
| Hub | PR #68 is the active visible dependency blocker and now has a targeted docs-only plan | execute Hub-local Tailwind 4 fix/migration plan only when activated | runtime support |
| DSE | sensitive lane | do not touch without explicit COI-aware scope and live validation | COI-gated |

## Urgent: 1-7 Days

- Preserve the DTP control-plane checkpoint in the public PR: Kaizen CLI,
  redacted capture, existing-system map, deep audit, docs, tests, proof queue,
  live-intake receipt, and starter DMARC receipt.
- Keep private engagement-vault durability on the approved private remote; do
  not public-commit client kit material.
- Start every broad work block with `dtp kaizen status --limit 5` and
  `dtp workspace report`.
- Do not build around waiting states. CCAAP waits on owner inputs; Cam and Greg
  have accepted discovery/cadence signals but repo/proof movement stays gated;
  DSE stays COI-gated; Hub PR #68 stays parked.
- Keep DeMario public proof to the posted, public-safe packet and recorded
  public URLs unless new permissioned proof arrives.
- Keep Omnexus IAP support in release-hold mode: app version `1.0.1` is
  approved and `Pending Developer Release`, but the monthly/annual
  subscriptions are still `Waiting for Review`. Do not manually release until
  subscriptions approve or Apple confirms the safe first-IAP release path.
- Make consulting share-ready before redesign: preserve route coverage,
  assistant QA, build/doctor/matrix checks, live intake receipt, manual visual
  QA, and proof readiness.
- Preserve the completed Architected Strength P0/P1 finish pass and keep
  publishing, assistant-pattern work, Azure deploy, Notion writes, consulting
  copy, and public proof expansion behind explicit reopen gates.

## Short Term: 2-4 Weeks

- Make the client loop repeatable: reply intake, owner-call extraction, weekly
  Business Brain packets, Kaizen updates, and private-kit-first status changes.
- Turn proof into a pipeline: proof queue, evidence, permission, redaction,
  reviewer, caveat, and proof packet before any consulting copy change.
- Use the DeMario launch-feedback signal to test that pipeline with a real
  human-owned social package before broader case-study promotion.
- Promote offer clarity from real delivery: use offer-led packaging and the
  offer-to-proof matrix plus internal offer repertoire before public language
  changes.
- Harden Kaizen V1 with lightweight saved views for Today, Waiting, Proof Queue,
  and Repo Health; keep Notion as dry-run mirror until one reviewed safe apply is
  explicitly approved.
- Preserve business-admin basics: starter DMARC monitoring, Calendar/Meet
  hygiene, and Apple Reminders-first task flow.

## Mid Term: 1-3 Months

- Graduate Hosted DTP only after usage pressure: run one more real private
  operating loop with markdown fallback before making hosted records normal.
- Build the proof/reference engine: promote CCAAP, Omnexus, DeMario, Architected
  Strength, Hub, or DSE only through proof gates.
- Pilot one command room only if the fit assessment proves repeated owner/client
  workflow pain.
- Accept or revise assistant manifests before implementation: source corpus,
  refusals, logging, analytics, handoff, and proof posture must be real.
- Improve agent quality loops with real reply examples, eval garden additions,
  misfire receipts, and prompt/skill changes only after evidence.

## Long Term: 3-12 Months

- Hosted Practice OS: private engagement/artifact/evidence/proof/decision
  cockpit with import/export, RLS, backup, redaction, and markdown fallback.
- Public trust ecosystem: consulting becomes proof-backed storefront;
  Architected Strength stays a separate personal-brand/reference lane; project
  repos remain source owners.
- Selective automation: QuickBooks read-only, Notion sync, Hub expansion,
  public assistants, and FAOS-style orchestration stay gated until manual
  workflow pain and ROI are clear.
- Supervised learning, not autonomy: future intelligence suggests changes into
  review queues; no autonomous client comms, public proof publishing, finance
  writes, or self-modifying skills.
- Reference library: convert real delivery into reusable offers, templates,
  proof packets, command-room specs, launch packets, eval fixtures, and client
  handoff patterns.

## Feature Enhancements To Revisit

| Surface | Enhancements | Gate |
|---|---|---|
| Kaizen | saved views, stale-item detection, promotion helpers, steward receipts from status output, Notion dry-run diffs, safe one-row apply | current CLI proves useful across real weekly use |
| Workspace report | optional live repo/PR adapters behind explicit read-only gates | V0 report is used often enough that live refresh saves time |
| Engagement kits | better reply intake, owner-input trackers, proof readiness, private vault snapshots | private vault durability is settled |
| Consulting | proof-backed offer pages, manual visual QA checklist, share-ready route matrix, noindex admin refinements | proof and offer language are source-backed |
| Hub | runtime current-state clarity, intake health checks, prompt/registry validation, PR #68 plan | selected runtime bottleneck exists |
| Hosted DTP | private records, export, evidence, redaction, review queues | markdown fallback becomes painful |

## Cadence

- Daily: check Kaizen plus current blocker/waiting state.
- Weekly: Business Brain reset, proof queue review, client waiting-state review,
  and repo-health skim.
- Monthly: roadmap steward review, tooling review, proof/reference promotion
  review, and parked-lane pruning.
- Quarterly: decide whether Hosted DTP, assistant pilots, QuickBooks read-only,
  or deeper Hub automation has earned implementation.

## Do Not Build Yet

- No live Notion writes without reviewed dry run and steward receipt.
- No DSE mutation or proof movement without explicit COI-aware scope.
- No public proof without evidence, permission, redaction, reviewer, and caveat.
- No autonomous client communications.
- No QuickBooks writes or live imports.
- No Hub-as-CRM or DTP replacement.
- No broad public-site redesign before share-readiness and proof maturity.
