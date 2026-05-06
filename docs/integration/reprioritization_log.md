---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Reprioritization Log

Use this log after meaningful Practice OS changes so backlog movement is
deliberate and visible.

## 2026-05-06: Active Queue Closeout Pass

Source:

- Toni asked to implement the active queue closeout plan across DeMario,
  Omnexus, consulting, and Architected Strength.
- `docs/ROADMAP_EXECUTION_BACKLOG.md`
- `practice-os/kaizen/intake.jsonl`

Change:

- Recorded DeMario as waiting on human-owned public URL capture after the
  approved builder-journey post goes live.
- Verified Omnexus PR #562 has green latest checks but remains blocked by
  required review and exact App Store Connect product-status evidence.
- Landed consulting PR #3 with the 2026-05-06 public-site readiness receipt,
  live route smoke, Hub-first intake proof, and remaining manual gates.
- Merged Architected Strength PR #2 as the repo-local boundary/roadmap note
  without expanding into assistant-pattern or broader site work.

Priority impact:

1. Remaining human/manual gates are DeMario post URL capture and Omnexus PR
   review plus App Store Connect status fill.
2. Consulting public-site readiness is no longer an active DTP queue item.
3. Architected Strength implementation remains next/later on a fresh branch.

Next review trigger:

- Toni posts DeMario URLs, Omnexus PR #562 receives required review, or
  App Store Connect status proves an IAP code change is needed.

## 2026-05-06: DeMario Human Builder-Journey Copy

Source:

- Toni asked to make the Mario post more human by opening with his current
  developer/creator process using GitHub Copilot, Codex, and Claude.
- `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md`

Change:

- Reframed the DeMario post around Toni's current builder journey, then moved
  into Mario's DFW pickleball coaching business and the site features.
- Added public-safe copy that names GitHub Copilot, Codex, and Claude without
  implying the tools built the site autonomously.
- Kept the plain/non-gimmicky Mario voice guardrail and public-proof boundaries.

Priority impact:

1. Use the builder-journey LinkedIn draft as the preferred public post.
2. Keep the CTA simple: DFW pickleball players should hit up Mario.
3. Record final post URL(s) after Toni posts.

Next review trigger:

- Toni wants to turn the builder journey into a recurring creator/dev series.

## 2026-05-06: DeMario Plain Social Voice Correction

Source:

- Toni explicitly said never to use inspirational or gimmicky phrasing for his
  brother's posts.
- `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md`

Change:

- Added a Mario-specific voice guardrail: plain, specific, practical, and free
  of inspirational, gimmicky, motivational, or slogan-like phrasing.
- Replaced the LinkedIn, Instagram, and carousel drafts with direct copy about
  the site, booking flow, venue routing, payment guidance, and admin workflow.
- Kept the existing proof/privacy boundary unchanged.

Priority impact:

1. Future DeMario/Mario social copy must start from concrete facts, not
   sentiment-led framing.
2. The approved public-safe status still applies to the revised plain-language
   copy.
3. Post URL capture remains the only follow-up after Toni posts.

Next review trigger:

- Toni wants another Mario post, carousel, case-study blurb, or consulting-site
  proof reuse.

## 2026-05-06: DeMario Public Social Copy Cleared

Source:

- Toni confirmed on 2026-05-06 that he is good to post about Mario's site and
  that the remaining Mario site work is finished.
- `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md`
- `docs/PRACTICE_PROOF_QUEUE_INDEX.md`
- `docs/ROADMAP_EXECUTION_BACKLOG.md`

Change:

- Moved the DeMario launch-feedback packet from permission-gated draft to
  public-safe text copy for Toni-owned LinkedIn and Instagram posting.
- Replaced the bland draft with more personal LinkedIn, Instagram, and carousel
  options grounded in the public site, booking flow, venue routing, payment
  guidance, and owner/admin workflow.
- Preserved the privacy boundary: private admin screenshots, student data,
  payment proof, testimonials, metrics, and consulting-site reuse still need
  separate source review and redaction.

Priority impact:

1. DeMario social copy is no longer the active blocker; the only remaining
   action is human posting plus recording final public URL(s).
2. Keep DeMario public proof limited to the approved text/public-page scope.
3. Move the next execution queue back to Omnexus subscription review,
   consulting readiness/proof maturity, and Architected Strength P0/P1.

Next review trigger:

- Toni posts on LinkedIn or Instagram and has final URL(s) to record.
- Toni wants to reuse the DeMario work on the consulting site as a case study.
- Toni wants to publish screenshots, testimonials, metrics, or private admin
  proof beyond the current public-page/text scope.

## 2026-05-06: DeMario CI Repair And Proof Evidence Refresh

Source:

- DeMario `master` GitHub CI was red after the application-overview docs commit.
- `demario-pickleball-1` commit `e92b1c0`.
- GitHub Actions CI run `25413691658` and CodeQL run `25413691307`.
- `practice-os/efficiency/demario-pickleball-1-evidence-index.md`
- `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md`

Change:

- Repaired stale DeMario tests that drifted against the booking-window date and
  current admin Availability UI/API shape.
- Refreshed repo-local DeMario docs so the application overview, launch
  checklist, setup guide, and outstanding gates match current API routes and
  Supabase priority migration requirements.
- Updated DTP proof evidence without changing the public-proof decision: the
  DeMario lane is technically healthier, but public use still requires Mario's
  permission, source evidence, screenshot approval, redaction, reviewer, and
  caveat.

Priority impact:

1. Keep DeMario social/proof prep active, but do not post or promote screenshots
   until owner permission clears.
2. Treat DeMario code gates as green at `e92b1c0`; remaining launch work is
   manual owner/admin proof, Google Calendar, Supabase production checks, and
   live booking QA.
3. Keep Node 24 runner/toolchain migration on the developer-maintenance roadmap
   because GitHub still reports the Node 20 actions deprecation warning.

Next review trigger:

- Mario approves/revises the proof wording or screenshot use.
- DeMario live booking QA or Google Calendar/Supabase launch gates are completed.
- GitHub's Node 24 runner transition becomes urgent for this repo.

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

## 2026-05-05: Systems Health Review Skill Routed

Source:

- `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md`
- `practice-os/templates/activation-routing-map.md`

Change:

- Registered `systems-health-review` as a Phase 1 `tm-skills` diagnostic lane
  in DTP roadmap surfaces.
- Routed systems-health prompts to `tm-skills/systems-health-review`.
- Documented Toni's Windows VS Code extension install fallback for the local
  workspace dashboard.

Priority impact:

- Keep systems-health review as a review-first diagnostic skill, not a rewrite
  mandate.
- Keep DTP as the router/source map while the actual skill implementation lives
  in `tm-skills`.
- Keep the dashboard extension local, manual-refresh, and no-server.

Next review trigger:

- The `tm-skills` systems-health-review work is committed and validated.
- A repo or client operating system asks for a weakest-system review.
- The dashboard extension needs reinstall or machine-specific setup notes.
