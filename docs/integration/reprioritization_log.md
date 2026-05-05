---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Reprioritization Log

Use this log after meaningful Practice OS changes so backlog movement is
deliberate and visible.

## 2026-05-05: No-Server Workspace Dashboard Panel

Source:

- Toni's request for a visible no-server dashboard inside VS Code or a separate
  screen because the cross-workspace roadmap state is hard to hold in chat.
- Existing-extension review: Markdown preview, HTML/Simple Browser previews,
  and Markdown Kanban tools are viable viewers or board tools but do not own
  the DTP cross-workspace refresh/source-of-truth boundary.
- `docs/WORKSPACE_DASHBOARD_READONLY.md`
- `docs/WORKSPACE_COMMAND_CENTER_V0.md`

Change:

- Kept DTP as the whole-workspace planning source of truth.
- Added a tiny local VS Code panel as a viewer/manual refresh button for the
  generated DTP dashboard.
- Preserved the no-server, no-watcher, no-cloud-call, no-sibling-command
  boundary.

Priority impact:

1. Use the VS Code panel as the operator cockpit for consulting, Architected
   Strength, Omnexus, DeMario, Hub, CCAAP, DSE, and related workspace lanes.
2. Keep generated panel cache in ignored `outputs/workspace-dashboard.html`.
3. Do not move roadmap ownership into generic Marketplace Kanban syntax.

Next review trigger:

- Toni uses the panel for a few planning sessions and identifies missing
  filters, sections, repo lanes, or visual grouping.

## 2026-05-05: DeMario Social Proof And Site-Fix Focus

Source:

- Toni's 2026-05-05 roadmap request after DeMario's pickleball site went live
  and received strong feedback.
- Toni's 2026-05-05 Omnexus update that App Store approval landed but
  subscriptions were declined/not approved.
- Live clean git refresh for `consulting`, `diagnose-to-plan`,
  `architected-strength`, and `demario-pickleball-1`.
- `docs/WORKSPACE_ROADMAP_AND_PLANNING_REPORT_2026-05-05.md`
- `docs/ROADMAP_EXECUTION_BACKLOG.md`
- `docs/PRACTICE_PROOF_QUEUE_INDEX.md`

Change:

- Promoted DeMario from generic later proof/reference material into an active
  launch-feedback social/proof packet candidate.
- Reopened Omnexus as App Store Connect/IAP support around subscription-review
  resubmission instead of treating approval as fully complete or assuming code
  changes are required.
- Reopened the consulting site as a focused fix/readiness pass, not a broad
  redesign or proof replacement.
- Reopened Architected Strength as a separate P0/P1 public-signal finish/fix
  pass before assistant-pattern work.
- Captured all three items into the Kaizen intake so they do not stay in chat.

Priority impact:

1. First: draft a DeMario LinkedIn/social proof packet with owner-approved
   wording, source/testimonial evidence, screenshot approvals, redaction,
   launch context, caveat, and final channel copy before posting.
2. Second: fill `fitness-app/docs/ops/app-store-subscription-resubmission-checklist-2026-05-05.md`
   from Omnexus App Store Connect subscription statuses and reviewer message,
   then choose manual resubmission or a code branch.
3. Third: run the consulting public-site fix/readiness pass while preserving
   Steel Ledger and Hub-first intake.
4. Fourth: run the Architected Strength P0/P1 finish/fix pass while preserving
   its personal-brand OS boundary.
5. Still blocked: public proof publishing, private screenshots, autonomous
   posting, assistant runtime, DSE proof, and broad redesign without accepted
   scope.

Next review trigger:

- Mario approves or revises the social/proof packet.
- Omnexus subscription status/reviewer message is inspected.
- The consulting site pass is scoped for implementation.
- The Architected Strength finish/fix pass is scoped for implementation.
- A new positive-feedback or proof signal arrives from any active project.

## 2026-05-04: Roadmap Alignment Drift Cleanup

Source:

- Toni's roadmap alignment implementation request.
- Live connector checks confirming Calendar/Gmail are on the founder Workspace
  account.
- Toni's manual booking, Meet link, and mailbox tests.
- `docs/BUSINESS_ADMIN_OPERATING_SYSTEM.md`
- `docs/ROADMAP_EXECUTION_BACKLOG.md`

Change:

- Reconciled stale roadmap rows that still described Google Workspace,
  Calendar/Meet, booking, and mailbox setup as blocked.
- Locked Apple Reminders in as the daily task/action system and marked Google
  Tasks out of scope unless Toni explicitly reopens the decision.
- Reduced the Workspace follow-up list to one remaining manual DNS item:
  starter DMARC after DKIM Admin verification is settled.
- Kept hosted DTP, client portals, assistants, FAOS, QuickBooks, cross-repo
  command runners, broad bots, and public proof automation behind their
  existing gates.

Priority impact:

1. Short term: commit/verify current DTP and consulting work, add/verify DMARC,
   repeat the Business Brain reset, and use DTP reply-intake/cadence templates
   on the next real client or weekly-reset loop.
2. Mid term: turn one real client/admin loop into internal proof and offer
   learning before public consulting copy changes.
3. Long term: expand hosted/private/runtime/assistant layers only after manual
   loops show repeated pain and accepted boundaries exist.

Next review trigger:

- Starter DMARC is added or intentionally deferred.
- The next Cam, Greg, CCAAP, or weekly reset loop runs through DTP templates.
- A reusable delivery pattern needs to become a private offer-catalog item.

## 2026-05-04: Google Workspace And Business Admin Operating Lane

Source:

- Toni's Google Workspace + Business Admin Operating Plan
- Toni's Apple Reminders capture request
- `founder@tonimontez.co` live workspace identity target
- `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md`
- `docs/NOTION_MIRROR_V0.md`
- `docs/OFFER_LED_PRACTICE_PACKAGING.md`

Change:

- Added `docs/BUSINESS_ADMIN_OPERATING_SYSTEM.md` as the DTP-first operating
  lane for Google Workspace, Calendar/Meet, LLC readiness, EIN/banking/tax
  prompts, contracts, insurance, brand assets, and admin cadence.
- Added `docs/INTERNAL_OFFER_REPERTOIRE_CATALOG.md` to capture reusable service
  patterns before public offer promotion.
- Added Business Admin item, Calendar Policy, and Offer Catalog item templates.
- Added an Apple Reminders capture lane and one-list pilot checklist so Toni
  can keep Reminders as the daily task layer without moving to Google Tasks.
- Updated routing docs, roadmap/backlog, connector map, and the consulting
  `/admin` launcher so public surfaces stay launcher-only and private status
  remains in DTP/Notion.

Priority impact:

1. `founder@tonimontez.co` is the active identity for external meetings.
2. Google Calendar/Meet connector, booking pages, Meet links, and mailbox flow
   are tested; only starter DMARC remains in the Workspace auth lane.
3. Apple Reminders remains the task/action layer; Google Tasks is out of scope
   and any future bridge starts as a business-only `Consulting` list pilot with
   no all-reminders access.
4. LLC/tax/legal work is a planning checklist only until professional review.
5. The offer repertoire is internal until proof, permission, redaction,
   repeatability, and positioning gates pass.
6. Notion mirrors sanitized status only; DTP remains source of truth.

Next review trigger:

- Starter DMARC is added or intentionally deferred.
- Toni decides an Apple Reminders bridge is useful enough to pilot.
- A new client delivery or internal asset should become an offer-catalog item.
- LLC filing, tax treatment, contracts, insurance, or banking moves from
  planning prompt to professional-reviewed action.

## 2026-05-03: Offer-Led Practice Machine Compression

Source:

- Mode B workspace audit in `C:\Users\tonimontez\.audit-output\`
- `docs/WORKSPACE_BUSINESS_EVIDENCE_DOSSIER_2026-05-03.md`
- `docs/PRACTICE_PRODUCTION_ROADMAP.md`
- `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md`
- Hub consulting console/runtime docs

Change:

- Added `docs/PRACTICE_MACHINE_OPERATING_MAP.md` as the offer-led compression
  map for the whole practice machine.
- Added `docs/WORKSPACE_OPERATOR_RUNBOOK.md` for repo ownership, safe command
  classes, verification paths, deploy owners, and no-touch boundaries.
- Added `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md` as the proof movement path
  that reuses existing Practice OS templates instead of duplicating them.
- Added `docs/OFFER_LED_PRACTICE_PACKAGING.md` to define the first internal
  offer set before public consulting-site copy changes.
- Added `C:\Users\tonimontez\hub\docs\HUB_RUNTIME_CURRENT_STATE.md` to
  classify Hub surfaces before more runtime expansion.

Priority impact:

1. Clarity + Proof is the current active compression sprint.
2. The next execution move is one real client loop pilot, not hosted DTP or a
   live cross-repo command runner.
3. Public proof must move through the proof promotion runbook before consulting
   copy/assets change.
4. Hub expansion is gated by the runtime current-state map.
5. Hosted DTP, client portals, autonomous agents, QuickBooks writes, public
   proof automation, DSE proof, and shared CI/bots everywhere remain gated.

Next review trigger:

- A Cameron, Greg, or CCAAP reply/cadence cycle is ready to run through the
  client loop pilot.
- The consulting public offer copy pass starts.
- Hub runtime routes or Railway/local-only assumptions change.
- A proof candidate is ready for public-claim review.

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
