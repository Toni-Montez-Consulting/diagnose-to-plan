---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Reprioritization Log

Use this log after meaningful Practice OS changes so backlog movement is
deliberate and visible.

## 2026-05-13: Consulting Workspace OS And Requirements Gatherer V1 Added

Source:

- Toni's self-email idea for a Consulting Workspace OS.
- Toni's requirement that the plan add a systematic Requirements Gatherer
  without removing the Workspace OS idea.
- `docs/CONSULTING_WORKSPACE_OS_V0.md`
- `practice-os/templates/requirements-gathering-brief.md`
- `practice-os/templates/requirements-decision-ledger.md`
- `practice-os/steward/2026-05-13-consulting-workspace-os-requirements-gatherer-v1.md`
- `practice-os/kaizen/intake.jsonl`

Change:

- Added a DTP-owned Consulting Workspace OS V0 plan that keeps the system
  internal, additive, and source-of-truth aligned.
- Added Requirements Gatherer V1 as the first new module: risk-based
  activation, Micro/Standard/Deep/Workshop tiers, 5-6 question batches,
  escalation with permission, build-ready brief output, and memory promotion
  boundaries.
- Added durable templates for requirements briefs and decision ledgers.
- Kept `tm-skills` as a future skill candidate only after the DTP protocol has
  been reviewed once.
- Preserved the boundary that consulting is the first pilot, while public copy,
  app code, Hub runtime, hosted DTP, global installs, and proof publication
  remain untouched.

Priority impact:

1. Future substantial requests should use Requirements Gatherer instead of ad
   hoc clarifying questions when discovery would materially improve the build.
2. Consulting is the first pattern-scan pilot for the Workspace OS, but DTP
   remains the source of truth.
3. The next implementation move is to pilot Requirements Gatherer on real
   requests and run the consulting pattern scan, not to build dashboards,
   hosted workflow, or a `tm-skills` skill immediately.

Next review trigger:

- Three meaningful requests use Requirements Gatherer.
- Toni says the gatherer is too heavy, too light, or still not asking enough.
- The consulting pattern scan produces reusable pattern candidates.

## 2026-05-12: CMS And Editor Tooling Moved To Backburner Planning Lane

Source:

- Toni asked whether Sanity could fit elsewhere in the workspace and whether
  similar tools could help build better products.
- Toni then clarified that the idea should be added to the broader roadmap,
  skills, agent work, and planning only, with implementation on the backburner.
- `docs/CMS_EDITOR_TOOLING_DECISION_LADDER.md`

Change:

- Added a DTP-owned CMS/editor decision ladder for choosing between Git/static
  content, Sanity, Supabase app data, Payload, Directus, Strapi, Tina, Decap,
  Builder.io, Contentful, Hygraph, Webflow, Framer, Notion mirror, or custom
  admin surfaces.
- Routed CMS/editor/page-builder prompts through Tooling Steward, Software
  Architecture, Product Strategy, UX / Design, QA / Audit, DevOps /
  Infrastructure, External Communications, and `tm-skills/backend-design` as
  needed.
- Added `cms-editor-fit` as a parked future `tm-skills` concept only, not a
  skill folder or implementation request.
- Preserved CCAAP as the first proof of need while blocking broad CMS adoption
  until another project shows the same repeated owner-editing pattern.

Priority impact:

1. Future Sanity/CMS/editor questions should now start with fit assessment and
   source-of-truth boundaries, not implementation.
2. CCAAP can keep its V1 `/admin` lane without turning every repo into a CMS
   migration candidate.
3. The next real CMS/editor work item must name owner persona, content types,
   public/private boundary, cost/roles, review/publish gate, and verification
   before build work starts.

Next review trigger:

- Another project besides CCAAP asks for non-technical owner editing.
- Toni asks to compare Sanity/Payload/Directus/Strapi/Tina/Decap/Builder.io/
  Contentful/Hygraph/Webflow/Framer/Notion with current docs for a specific
  repo.
- CCAAP Leah/Tony use `/admin` enough to produce an owner-editor handoff
  pattern.

## 2026-05-12: CCAAP V1 Owner Editor Promoted To Launch Blocker

Source:

- Toni clarified that the meeting transcript's admin/content-management item is
  not optional for later; it needs to be addressed as part of V1.
- `ccaap-site/docs/V1_ADMIN_WORKFLOW.md`
- `ccaap-site/src/sanity/schemaTypes/`
- `practice-os/efficiency/ccaap-site-evidence-index.md`

Change:

- Superseded the earlier post-launch CMS/editor posture for CCAAP.
- Added Sanity Studio at `/admin` as the V1 owner-editing path for updates and
  photos only.
- Kept board, meetings, PayPal, contact routing, resources, payment records,
  member records, private notes, form submissions, and credentials outside the
  editor scope.
- Preserved review-before-publish: public pages query only approved and
  published Sanity content.
- Kept Leah/Tony editor invitations approval-gated until Toni or the owners
  approve adding them to the editor.

Priority impact:

1. CCAAP V1 launch readiness now includes a working `/admin` editor workflow,
   not only Git-backed Toni updates.
2. Sanity project setup, Vercel environment variables, editor access, and
   approved-content publish smoke are launch gates.
3. Production DNS remains blocked until payment/contact/meeting/media/DNS,
   admin workflow, and owner approval gates are closed.

Next review trigger:

- Sanity project creation/env setup succeeds or fails and needs operator
  intervention.
- Leah/Tony approve editor invitations.
- Vercel Git auto-deploy is repaired and previews rebuild from Git.

## 2026-05-11: Practice Brand Round 3E-3I Source Mining Added

Source:

- Toni confirmed the naming priority stack as compounding human capability,
  disciplined ambition, and builder-led delivery.
- Privacy-safe review of selected founder-mailbox self-forwarded notes
  and existing DTP source thesis docs.
- `docs/PRACTICE_BRAND_NAMING_BRIEF_V2.md`

Change:

- Added a Round 3E founder-language source board to the practice naming brief.
- Converted private founder notes into public-safe naming patterns without
  quoting client-specific or private email content.
- Added a reaction-test candidate set led by `Capien`, `Synesis`, `Noetia`, and
  `Aptum`.
- Demoted `Telic` from the lead pressure-test position after Toni's reaction
  that it felt too short and did not create enough founder pull.
- Narrowed the next branch after Toni reacted positively to `Synesis` and
  `Noetia`, because they feel rooted, intellectual, human, and less like
  visible word-combination names.
- Added Round 3F as a rooted intellectual / human consequence pass, with
  `Synesis`, `Noesis`, `Noetia`, `Sensus`, and `Capax` as the best reaction
  set before any clearance work.
- Added Round 3G as an Anthropic-style Greek / Greek-derived source-root branch,
  including `Synesis` / `Noesis`, `Dynamis`, `Ergon` / `Poiesis`, and
  `Heuristic`.
- Captured Toni's off-the-dome `Synetic` / `Synestic` branch: `Synetic`
  validates the sound/meaning instinct but appears collision-heavy in adjacent
  AI/consulting spaces; `Synestic` remains a reaction seed, not a finalist.
- Added Round 3H as a back-to-the-drawing-board reset after the `Synetic`
  collision disappointment. The reset keeps the qualities of `Synetic`
  (intelligent, active, serious, human-adjacent understanding in motion) while
  stopping the search from chasing weaker `Syn-` variants.
- Separated Greek-rooted source concepts from direct candidate names:
  maieutic idea-birth, potential-to-actual, work made real, practical
  discovery, and disciplined capability.
- Added Round 3I as a Latin/Roman source branch led by the thesis sentence
  "capability becoming real through disciplined understanding and building."
- Recorded that `Conatus` / `Conari`, `Molior`, `Capax`, `Auctor` / `Artifex` /
  `Opifex`, and `Efficere` / `Actus` are the strongest source concepts from
  this branch.
- Recorded the light scan result that raw Latin/Roman roots are conceptually
  useful but too crowded across adjacent AI, software, consulting, workflow,
  and implementation categories to advance as direct finalists without deeper
  clearance.
- Added Round 3J as the first synthesis pass around Toni's deeper founder code:
  relentless, loving, AVO as private origin, IWPWE / persisting without
  exception, battle, and love.
- Demoted `Valent` from the active lead set after Toni confirmed it does not
  hit harder than `Conatus`.
- Promoted `Conara`, `Tenara`, `Coratus`, `Inceptis`, and `Ingenta` as the
  current Round 3J reaction set for "relentless care turned into working
  systems."
- Captured Toni's later reaction that Round 3J was a dead end. Do not keep
  refining `Conara`, `Tenara`, `Coratus`, `Inceptis`, `Ingenta`, `Yuktis`,
  `Nishara`, or `Renara` unless Toni explicitly reopens one.
- Added Round 3K as a sound-first reset. The next pass should allow both simple
  real English words and invented words, then backfill meaning only after a
  name creates founder pull.

Priority impact:

1. Keep the public site and logo unchanged until Toni reacts to Round 3E and a
   name creates real founder pull.
2. Continue naming from human capability plus intelligence before doing legal,
   domain, social, or visual identity work.
3. Avoid visible compound names in the next pass; prefer rooted intellectual
   words or coined names whose construction is invisible.
4. Use founder pull before clearance: only scan domains, social, and trademark
   surfaces after one or two names survive reaction testing.
5. Treat Greek roots as source material, not automatic final names.
6. Do not settle for weaker cousin names after a liked name proves
   collision-heavy; preserve the felt qualities and restart from adjacent roots.
7. Keep DTP as the durable naming source and consulting as the eventual public
   consumer.
8. Treat raw Latin/Roman roots as source material rather than direct brand
   candidates unless one later earns founder pull and passes real clearance.
9. Make Round 3J an English-feeling or lightly coined synthesis from
   **striving + making real + capability**, not another list of direct Latin
   words.
10. Keep AVO, IWPWE, battle, and love as founder-origin material unless Toni
    later chooses to expose part of that story publicly.
11. Test the next name set against **relentless care**, not just abstract
    intelligence or classical-root cleverness.
12. Stop source-root mining for now. The naming process should prioritize
    sound, memorability, credibility, and Toni's willingness to say the name out
    loud.
13. Allow simple real English words in Round 3K; do not force every name to be
    coined or etymologically defensible.

Next review trigger:

- Toni reacts to the Round 3E candidate set.
- A candidate creates enough energy to justify clearance research.
- Toni asks to branch into a new source-root lane.
- Toni reacts to the Round 3I root concepts and the Round 3J synthesis prompt.
- Toni asks to generate Round 3K sound-first names.
- Toni reacts to Round 3K and identifies any name that creates founder pull
  before explanation.

## 2026-05-10: Question Checkpoint Rule Promoted

Source:

- Toni clarified that questions are part of how he learns what Codex is doing,
  where the work is going, and how to steer substantial work.
- `AGENTS.md`
- `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md`
- `practice-os/evolution/records/2026-05-10-question-checkpoint-rule-for-substantial-strategy-build-work.md`
- `practice-os/kaizen/intake.jsonl`

Change:

- Promoted the Question Checkpoint Rule to playbook memory for substantial
  strategy/build work.
- Locked the default protocol: compact ledger, state what Codex thinks is being
  built and why, ask one to three non-blocking questions, show practical and
  ambitious paths, build with labeled assumptions, and ask again before a new
  meaningful layer.
- Kept the current Practice Evolution System CLI/operator-first, with a visible
  cockpit/dashboard planned only after real record usage.

Priority impact:

1. Future DTP/practice/consulting strategy and build threads should include
   question checkpoints by default.
2. Small mechanical tasks and urgent safe fixes do not need the full protocol.
3. The visible cockpit remains a later iteration, not the next immediate build.

Next review trigger:

- Three substantial threads have used the protocol.
- Toni says questions are too heavy, too light, too late, or not helping him
  steer.
- The Practice Evolution cockpit/dashboard is reopened for implementation.

## 2026-05-10: Practice Evolution System V0 Added

Source:

- Toni asked for meta-patterns, idea evolution, messaging language, research
  signals, and useful collaboration practices to stop getting captured once and
  forgotten.
- `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md`
- `practice-os/templates/idea-evolution-record.md`
- `practice-os/templates/research-pattern-candidate.md`
- `practice-os/comms/private/messaging-knowledge-base-2026-05-10.md`
- `practice-os/kaizen/intake.jsonl`

Change:

- Added an internal Practice Evolution System that captures broadly and
  promotes deliberately.
- Added templates for idea evolution records and research/field-observation
  pattern candidates.
- Added an internal-only messaging knowledge base for owner-bottleneck language,
  explanation lengths, claims, metaphors, visual seeds, and future public-copy
  candidates.
- Routed "don't forget this", meta-pattern, messaging system, pitch system,
  and research-pattern prompts into DTP artifacts instead of leaving them in
  chat.
- Preserved the boundary that Notion is a cockpit/mirror, consulting is the
  public storefront, and public/client/runtime changes require separate gates.

Priority impact:

1. The first slice is done as internal OS infrastructure, not site copy,
   Notion automation, client communication, or runtime behavior.
2. Meta-pattern, messaging, and research-pattern ideas can now be captured as
   raw or working memory without becoming immediate builds.
3. Playbook memory still requires human-gated promotion and evidence.
4. Future consulting-site copy can consume the messaging knowledge base only
   after a public-copy/proof/positioning review.

Next review trigger:

- Toni says a collaboration pattern "worked well" or should become how Codex
  works across projects.
- Toni sends new messaging language, pitch language, metaphors, or visual
  asset ideas.
- A research article, report, or field observation should become a reusable
  consulting pattern candidate.
- The Notion mirror/cockpit is ready to reflect sanitized statuses from DTP.

## 2026-05-08: AI Agents Report And Legal MCP Saved As Parked Research

Source:

- Toni asked to save Harvey MCP for possible legal work down the road.
- Toni provided local report pointer:
  `C:\Users\tonimontez\Downloads\2026 State of AI Agents Report.pdf`.
- `practice-os/steward/2026-05-08-ai-agents-report-and-legal-mcp-research-radar.md`
- `practice-os/kaizen/intake.jsonl`

Change:

- Captured Harvey MCP as a parked legal/compliance/tooling research signal, not
  an implementation or adoption decision.
- Captured the 2026 State of AI Agents Report as a parked Future Intelligence
  reference for AI-agent adoption, ROI, implementation barriers,
  human-in-the-loop operating models, and consulting/practice thesis evidence.
- Preserved the rule that future public claims need citation review before the
  report can be used in public consulting copy.

Priority impact:

1. No active queue or client lane changes.
2. Harvey MCP should only be revisited when a legal/compliance workflow,
   contract-review lane, policy-review lane, or general-counsel drafting mode is
   being scoped.
3. The AI agents report can inform future Practice OS, consulting offer,
   client education, and agent-workflow work after a citation-safe review.
4. Do not connect legal tooling, copy private/legal records, publish report
   claims, or create a production integration from this capture alone.

Next review trigger:

- Toni asks to scope legal/compliance or contract-review workflows.
- Toni wants AI-agent adoption evidence for consulting copy, a client-facing
  brief, or Practice OS agent workflow design.
- Harvey MCP becomes available in the local tool/plugin ecosystem and Toni asks
  to evaluate it from primary sources.

## 2026-05-07: Omnexus Subscriptions Working, Release Proof Remains

Source:

- Toni reported that the products/subscription issue is fixed and the app now
  works with subscriptions.
- The `fitness-app` docs branch records the in-app subscription path as
  operator-confirmed working while keeping private App Store, receipt,
  transaction, entitlement, account, and dashboard proof outside git.
- `practice-os/efficiency/fitness-app-evidence-index.md`

Change:

- Superseded the older "subscription review is no longer active" waiting item
  with a clearer release/live-proof waiting item.
- Treated product approval, product loading, purchase, and in-app subscription
  state as fixed by operator confirmation.
- Kept the remaining Omnexus question focused on the `1.0.1` candidate
  build/version, final smoke, provider/data checks, observability, and
  first-availability proof.

Priority impact:

1. Greg Client OS prep still stays first because the May 8 meeting is
   time-bound.
2. Omnexus is no longer a subscription-products task; it is a release-proof
   task.
3. Do not change IAP code, product IDs, App Store settings, public proof, or
   release state unless Toni approves the manual action or fresh Apple evidence
   requires it.

Next review trigger:

- Toni is ready to make the App Store release/submission decision.
- App Store Connect contradicts the current subscription-working state.
- A live-proof gate fails during final smoke or first-availability checks.

## 2026-05-07: Omnexus Approved Subscriptions Narrow Submit Gate

Source:

- Toni/operator-reported App Store Connect state says Monthly, Annual, and the
  subscription group localization are `Approved`.
- The `fitness-app` docs branch records that approved subscriptions do not need
  app-version attachment just to continue the release workflow.
- `practice-os/steward/2026-05-06-operator-review-state-update.md`

Change:

- Superseded the older "hold while subscriptions wait for review" queue item.
- Kept Omnexus as a manual App Store Connect/live-proof gate, not a code task.
- Narrowed the active release question to: is the selected App Store Connect
  candidate build/version really `1.0.1`, and are metadata, screenshots,
  privacy labels, review notes, reviewer credentials, and final smoke ready?

Priority impact:

1. Do Greg Client OS prep first because the May 8 meeting is time-bound.
2. For Omnexus, re-confirm App Store Connect product approval and candidate
   build/version before submit/release.
3. Do not change IAP code, product IDs, or public proof unless fresh App Store
   Connect/reviewer evidence requires it.

Next review trigger:

- Toni opens App Store Connect and confirms or contradicts the current
  operator-reported approval/build state.
- A new App Review message, rejection, or live-proof failure appears.

## 2026-05-06: Omnexus App Approved, Hold Release For Subscription Review

Source:

- Toni reported that Omnexus app version `1.0.1` is approved and `Pending
  Developer Release`.
- Toni reported that monthly and annual subscription products remain `Waiting
  for Review`.
- Apple App Store Connect help states first In-App Purchases/subscriptions must
  be submitted with a new app version, `Waiting for Review` means the IAP was
  submitted to Apple, and `Approved` means the IAP can go live with its
  associated app.
- `practice-os/steward/2026-05-06-operator-review-state-update.md`

Change:

- Moved Omnexus from "wait for app and subscription review" to "app approved,
  hold developer release while subscriptions wait for review."
- Preserved the no-code-change boundary until Apple returns exact
  reviewer/status evidence requiring code.
- Preserved the private-evidence boundary: do not copy App Store screenshots,
  reviewer messages, credentials, or private billing/user records into public
  DTP.

Priority impact:

1. Do not click `Release This Version` while monthly/annual subscriptions remain
   `Waiting for Review`, unless Apple confirms this is the safe first-IAP path.
2. If subscriptions approve, release version `1.0.1` and run the post-approval
   live IAP proof checklist.
3. If subscriptions reject or move to developer action, capture exact status and
   reviewer message privately before deciding whether the fix is metadata,
   availability, App Store Connect attachment, or code.
4. Architected Strength P0/P1 can proceed as the next build lane only with an
   Apple-review interrupt rule.

Next review trigger:

- Subscription statuses change from `Waiting for Review`.
- Apple/App Review sends a reviewer note or Resolution Center message.
- Toni decides to ask Apple support whether the pending app can safely release
  before the subscriptions approve.

## 2026-05-06: Operator Review State Moved To Apple Review Watch

Source:

- Toni reported that Omnexus PR #562 was merged.
- Toni reported that monthly and annual subscription statuses were
  `Waiting for Review` when submitted.
- Toni reported that app version `1.0.1` was submitted for review.
- Toni provided exact DeMario LinkedIn and Instagram post URLs.
- `practice-os/steward/2026-05-06-operator-review-state-update.md`

Change:

- Moved Omnexus from "submit/attach after PR review" to "wait for Apple review
  result."
- Recorded DeMario exact public post URLs and closed the durable-link proof
  follow-up.
- Preserved the privacy boundary: no App Store screenshots, reviewer messages,
  credentials, private app data, post metrics, testimonials, or private
  screenshots were copied into public DTP.

Priority impact:

1. Omnexus is no longer a repo/code task unless Apple returns exact rejection
   evidence requiring code.
2. DeMario social proof is now durable-link recorded and remains public-safe
   text/post proof only.
3. The next live manual watch item is Apple's review result.
4. Consulting taste review, Greg prep, Cam packet wait, CCAAP owner-input wait,
   and Architected Strength P0/P1 sequencing remain.

Next review trigger:

- Apple approves or rejects app version `1.0.1` and/or the monthly/annual
  subscriptions.
- Toni wants to start the Architected Strength P0/P1 finish branch.

## 2026-05-06: DeMario Social Posting Completed

Source:

- Toni reported on 2026-05-06 that he posted his brother's site on LinkedIn
  and Instagram.
- LinkedIn account: `https://www.linkedin.com/in/toni-montez`
- Instagram account(s): personal handle `toni.montez`; Architected Strength
  handle text `architected strength`
- `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md`
- `docs/PRACTICE_PROOF_QUEUE_INDEX.md`
- `practice-os/kaizen/intake.jsonl`

Change:

- Moved DeMario launch-feedback social proof from public-copy-ready to
  posted_urls_recorded.
- Recorded that posting happened from Toni-owned channels without adding
  unsupported metrics, testimonials, private screenshots, admin records,
  payment proof, or business-impact claims.
- Recorded exact LinkedIn/Instagram post URL capture as complete.

Priority impact:

1. DeMario human posting and durable URL capture are no longer active manual
   gates.
2. DeMario consulting-site reuse, screenshots, testimonials, metrics, and
   command-room proof remain separately gated.

Next review trigger:

- Toni wants to reuse the DeMario work on the consulting site as a case study.
- Toni wants to publish screenshots, testimonials, metrics, or private admin
  proof beyond the current public-page/text scope.

## 2026-05-06: Active Queue Closeout Pass

Source:

- Toni asked to implement the active queue closeout plan across DeMario,
  Omnexus, consulting, and Architected Strength.
- `docs/ROADMAP_EXECUTION_BACKLOG.md`
- `practice-os/kaizen/intake.jsonl`

Change:

- Recorded DeMario as posted from Toni-owned LinkedIn/Instagram channels, with
  exact public URLs now captured for durable link proof.
- Verified Omnexus PR #562 later merged and the App Store Connect posture moved
  to app version `1.0.1` plus monthly/annual subscriptions waiting for review.
- Landed consulting PR #3 with the 2026-05-06 public-site readiness receipt,
  live route smoke, Hub-first intake proof, and remaining manual gates.
- Merged Architected Strength PR #2 as the repo-local boundary/roadmap note
  without expanding into assistant-pattern or broader site work.

Priority impact:

1. Remaining human/manual gate is Apple review outcome; DeMario exact post URL
   capture is complete.
2. Consulting public-site readiness is no longer an active DTP queue item.
3. Architected Strength implementation remains next/later on a fresh branch.

Next review trigger:

- Apple approves or rejects app version `1.0.1` and/or the monthly/annual
  subscriptions.

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
3. Posting completed later on 2026-05-06; exact public post URLs were recorded
   after Toni provided them.

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
3. Post URL capture remains the only follow-up for durable proof tracking.

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

1. DeMario social copy is no longer the active blocker; posting completed later
   on 2026-05-06 and exact URL capture is the remaining durability follow-up.
2. Keep DeMario public proof limited to the approved text/public-page scope.
3. Move the next execution queue back to Omnexus subscription review,
   consulting readiness/proof maturity, and Architected Strength P0/P1.

Next review trigger:

- Toni has exact LinkedIn or Instagram final URL(s) to record.
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
- Founder mailbox live workspace identity target
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

1. The founder mailbox is the active identity for external meetings.
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

## 2026-05-06: 48-Hour Operator Checkpoint Updated

Source:

- `practice-os/steward/2026-05-06-active-queue-closeout-receipt.md`
- `practice-os/steward/2026-05-06-consulting-live-intake-receipt.md`
- `practice-os/steward/2026-05-06-starter-dmarc-receipt.md`
- private `engagements/` client-kit checkpoint

Change:

- Moved confidential active-lane inbox/calendar reconciliation out of public DTP
  and into the private engagement vault.
- Recorded the consulting live-intake smoke as passed with notes: the synthetic
  intake reached Hub, but cleanup remains structural until Hub has an
  archive/delete path.
- Added and verified starter DMARC for `tonimontez.co` in monitoring mode.
- Kept Omnexus as manual-review-state first: PR checks are green, but required
  review and App Store Connect status capture remain human gates.

Priority impact:

1. DTP public checkpoint and the private engagement vault are the protected
   source-of-truth split.
2. Omnexus PR review plus App Store Connect monthly/annual subscription status
   capture stays ahead of new build work.
3. DeMario exact social URL capture and consulting visual taste review are
   useful but not blockers.
4. Architected Strength P0/P1 starts only as a separate branch after manual
   gates are stable.

Next review trigger:

- Apple approves or rejects app version `1.0.1` and/or the monthly/annual
  subscriptions.
- Hub gains an intake archive/delete path or Toni decides the labeled smoke row
  is acceptable as the cleanup boundary.

## 2026-05-11: Live Intake Operator Workflow Added

Source:

- `docs/LIVE_INTAKE_TO_PRACTICE_OS_WORKFLOW_V0.md`
- `practice-os/templates/prospect-intake-triage.md`
- `practice-os/steward/2026-05-11-live-intake-operator-workflow-receipt.md`

Change:

- Added the DTP-owned workflow for turning a live `tonimontez.co/start`
  submission stored in Hub into a fit decision, offer route, Practice OS
  artifact, approval gate, and handoff receipt.
- Added the reusable Prospect Intake Triage template.
- Updated roadmap, docs map, and system architecture pointers so the workflow
  is discoverable before future Hub, Notion, Gmail, or hosted-DTP expansion.

Priority impact:

1. Use the manual triage workflow on the next real prospect intake before
   adding more runtime behavior.
2. Keep Hub as runtime support and DTP as source of truth until repeated manual
   friction proves a hosted or console enhancement is worth building.
3. Treat client follow-up, public proof, production writes, and integration
   expansion as separate approval-gated actions.

Next review trigger:

- A real prospect intake arrives.
- Three intakes use the triage template.
- Toni asks to connect Gmail, Calendar, Notion, Hub console triage status, or
  hosted DTP records to the workflow.

## 2026-05-11: Prospect Follow-Up Drafting Kit Added

Source:

- `docs/PROSPECT_FOLLOW_UP_DRAFTING_PLAYBOOK_V0.md`
- `practice-os/templates/prospect-fit-call-follow-up.md`
- `practice-os/templates/prospect-paid-blueprint-follow-up.md`
- `practice-os/templates/prospect-park-or-decline-follow-up.md`
- `practice-os/steward/2026-05-11-prospect-follow-up-drafting-kit-receipt.md`

Change:

- Added a draft-only follow-up playbook for converting prospect intake triage
  into reviewable external messages.
- Added first-class templates for fit-call, paid Blueprint, and
  no-build-yet/parked/bad-fit follow-up routes.
- Updated roadmap, documentation map, live-intake workflow, and control-plane
  routing so follow-up drafting stays connected to DTP triage and approval
  gates.

Priority impact:

1. The next real prospect intake can now move from Hub record to DTP triage to
   a reviewable draft without relying on chat memory.
2. The practice has a clearer first-response loop without adding CRM behavior,
   auto-send, exact pricing, calendar actions, public proof, or hosted-DTP
   expansion.
3. Fast Track follow-up language should wait for a real small-scope intake
   before becoming a template.

Next review trigger:

- A real prospect intake uses the follow-up kit.
- Toni approves or rejects the default Blueprint language.
- Two or three real drafts reveal repeated missing routes, examples, or
  status fields.

## 2026-05-11: Diagnostic Call Booking Link Policy Locked

Source:

- `docs/PROSPECT_FOLLOW_UP_DRAFTING_PLAYBOOK_V0.md`
- `practice-os/templates/prospect-fit-call-follow-up.md`
- `docs/LIVE_INTAKE_TO_PRACTICE_OS_WORKFLOW_V0.md`
- `docs/BUSINESS_ADMIN_OPERATING_SYSTEM.md`

Change:

- Locked `Diagnostic Call` as the public scheduling label.
- Preserved `fit-call` as the internal route value until a later schema/template
  rename is worth doing.
- Chose intake-first booking: the public `/start` page may show the approved
  Diagnostic Call booking link only after intake submission.
- Kept manual scheduling as a fallback, not the default.

Priority impact:

1. Consulting can add a post-submit booking CTA without changing Hub authority
   or creating a fake booking link.
2. The booking link should be environment-configured and absent when no real
   URL is available.
3. The next selectivity change should wait until real volume or bad-fit calls
   prove the need.

Next review trigger:

- The first live prospect books through the post-submit Diagnostic Call path.
- Toni wants the booking link hidden behind manual review.
- The internal route vocabulary becomes confusing enough to justify renaming
  `fit-call` files and route values.

## 2026-05-11: Live Funnel Closeout And Hub Dependency Triage

Source:

- `practice-os/steward/2026-05-11-live-funnel-closeout-receipt.md`
- `practice-os/efficiency/consulting-evidence-index.md`
- `practice-os/efficiency/hub-evidence-index.md`
- `docs/ROADMAP_EXECUTION_BACKLOG.md`

Change:

- Confirmed the approved Diagnostic Call booking link is live only after
  `/start` intake submission.
- Submitted one browser-based synthetic production intake through
  `https://tonimontez.co/start`.
- Verified the matching Hub row through the protected dashboard by summarized
  fields only.
- Recorded that Hub still lacks intake archive/delete support.
- Merged green Hub dependency PRs #74, #75, and #76; kept PRs #77 and #78
  blocked because build/typecheck gates fail.

Priority impact:

1. Future agents should not reopen booking-link configuration as pending work.
2. The live buyer path is proved enough to move the remaining consulting gate
   to visual/taste QA and real prospect learning.
3. Hub dependency maintenance stays separate from consulting/DTP proof and
   public-site strategy.

Next review trigger:

- A real prospect submits intake or books through the Diagnostic Call link.
- Toni decides intake cleanup automation is worth a Hub runtime change.
- Hub PR #77 or #78 is explicitly reopened for a targeted fix pass.

## 2026-05-12: CCAAP Prototype Review Moves To Vercel Launch Packet

Source:

- `engagements/mom-nonprofit/site-rebuild/post-meeting-receipt-2026-05-12.md`
- `engagements/mom-nonprofit/site-rebuild/decision-log.md`
- `practice-os/efficiency/ccaap-site-evidence-index.md`
- `ccaap-site/docs/OWNER_LAUNCH_PACKET_2026-05-12.md`

Change:

- Captured the May 12 prototype review as launch-packet direction, not final
  production approval.
- Switched the CCAAP hosting path from Cloudflare Pages to Vercel because Toni
  manages current web operations there and the static Astro site does not need
  Cloudflare-specific behavior.
- Preserved the remaining gates: PayPal donation/membership URLs, contact
  routing/spam choice, meeting label/destination, DNS/current-site access,
  approved logo/photos/resources/board media, Leah/Tony preview approval, and
  proof posture.

Priority impact:

1. CCAAP moves from generic owner-input wait to a concrete Vercel launch packet
   and implementation queue.
2. Public site updates can proceed only for owner-safe docs/config and design
   follow-up; production values still wait on approved inputs.
3. Public proof remains blocked by permission, redaction, reviewer, evidence,
   and caveat despite positive verbal review feedback.

Next review trigger:

- Exact owner-approved PayPal/contact/meeting/DNS/assets values arrive.
- Vercel preview is connected and ready for Leah/Tony review.
- Toni explicitly opens the next CCAAP visual/design implementation pass.

## 2026-05-12: CCAAP PayPal Candidates Staged, Launch Gate Preserved

Source:

- `engagements/mom-nonprofit/site-rebuild/email-scan-extraction-2026-05-12.md`
- `engagements/mom-nonprofit/site-rebuild/owner-follow-up-draft-2026-05-12.md`
- `practice-os/efficiency/ccaap-site-evidence-index.md`
- `ccaap-site/src/content/settings/site.json`

Change:

- Converted the fresh Gmail scan into a private extraction receipt and
  sendable follow-up draft.
- Staged the owner-provided PayPal donation and membership candidates in the
  CCAAP site repo with `paymentStatus: candidate`.
- Preserved launch blocking by keeping payment candidate status out of
  production verification and leaving contact, meeting, board/media, asset,
  DNS, preview approval, and proof gates open.

Priority impact:

1. The next CCAAP implementation pass can test the Join/Donate page flow
   without inventing payment values.
2. The owner follow-up is now narrower: meeting URL, contact/spam preference,
   logo/source files, homepage image, board photos, graphics folder, Wix invite,
   DNS registrar, and proof posture.
3. CCAAP remains a launch candidate, not a production-ready site.

Next review trigger:

- Leah/Tony confirm the staged PayPal routes are stable for production.
- The meeting URL conflict is resolved.
- Required assets or no-photo launch decision arrive.

## 2026-05-12: CCAAP Board Photos And Bios Staged, Identity Gate Preserved

Source:

- Resent Gmail `Pictures` messages surfaced as inline image payloads.
- `engagements/mom-nonprofit/site-rebuild/assets/board-photos-2026-05-12/source-manifest.md`
- `practice-os/efficiency/ccaap-site-evidence-index.md`
- `ccaap-site/src/content/board/`

Change:

- Staged eight resent board-photo candidates in private DTP asset intake.
- Copied clear named photo candidates into the public prototype asset folder.
- Rendered Tony-provided board bios as draft owner-review content.
- Assigned only the exact Vernell Gregg filename match in the board page and
  left generic or mismatched images unassigned.
- Staged the CCAAP public contact mailbox as a candidate public contact route
  while keeping spam/routing approval as a launch blocker.

Priority impact:

1. The next preview can show real board content without pretending media is
   production-approved.
2. The owner follow-up should not ask for PayPal values or board bios again.
3. The remaining board ask is narrower: confirm final copy, photo identity
   assignments, and photo approval.

Next review trigger:

- Leah/Tony review the staged board page.
- Generic or mismatched photo identities are confirmed.
- Contact spam/routing preference is approved.

## 2026-05-12: CCAAP Layout Review, Footer Polish, And Parent Draft Created

Source:

- `ccaap-site/docs/SITE_REVIEW_2026-05-12.md`
- `practice-os/efficiency/ccaap-site-evidence-index.md`
- Gmail draft `r-8887800189854309482`

Change:

- Reworked the prototype layout system so desktop and laptop margins are wider
  and subpage headings no longer feel pinched.
- Redesigned the footer as a lighter civic information band with clearer
  navigation and quieter prototype status.
- Staged Dad's Google Meet evidence as the meeting candidate instead of
  re-asking for the link, while keeping production launch blocked by final
  review.
- Created a new Gmail draft to Tony and Leah with the completed work and the
  remaining owner asks.

Priority impact:

1. The next parent-facing review can focus on approvals and assets, not
   re-explaining the prototype.
2. The meeting ask is narrowed to final review of the staged destination.
3. Site polish is now a review artifact with local validation evidence.

Next review trigger:

- Toni reviews/approves or edits Gmail draft `r-8887800189854309482`.
- Leah/Tony provide logo, homepage image, board photo approvals, PayPal/contact
  confirmation, spam preference, DNS/Wix path, or resource files.

## 2026-05-12: CCAAP Vercel Prototype Published And Parent Draft Clarified

Source:

- `ccaap-site/docs/SITE_REVIEW_2026-05-12.md`
- `ccaap-site/docs/LAUNCH_CHECKLIST.md`
- `practice-os/efficiency/ccaap-site-evidence-index.md`
- Gmail draft `r-8887800189854309482`

Change:

- Published the CCAAP launch-candidate prototype to Vercel at
  `https://ccaap-site.vercel.app`.
- Route-smoked all public pages on the live Vercel URL.
- Updated the parent draft so the remaining asks explain why exact
  confirmations are still needed for testing, security, privacy, payment
  safety, contact routing, meeting access, and long-term maintenance.
- Reaffirmed that the meeting transcript/admin-content item was captured:
  first launch remains Toni-managed and Git-backed, while owner-editable
  updates/posts/photos workflow is a post-launch CMS/editor decision unless
  Leah needs direct editing sooner.
- Recorded the deployment caveat that the Vercel project is live, but GitHub
  auto-deploy connection failed during CLI setup and still needs repair.

Priority impact:

1. Leah/Tony can review the real prototype URL without waiting for DNS changes.
2. Parent follow-up now separates already-captured direction from exact
   launch confirmations.
3. The admin/content-management registration question is preserved as a
   deliberate post-launch workflow decision, not an omitted requirement.

Next review trigger:

- Toni approves, edits, or sends Gmail draft `r-8887800189854309482`.
- GitHub auto-deploy is connected in Vercel.
- Leah/Tony decide whether direct owner editing is needed before launch or can
  wait until after launch.

## 2026-05-14: Integrity Layer Added To Consulting Workspace OS

Source:

- Toni's Integrity Layer / Craft Standard concept.
- `docs/CONSULTING_WORKSPACE_OS_V0.md`
- `practice-os/policies/integrity-layer-craft-standard.md`
- `practice-os/templates/pre-ship-integrity-gate.md`

Change:

- Promoted the quality thesis into DTP as an internal Integrity Layer, not a
  public marketing claim or parallel `_system` tree.
- Added a practical Craft Standard for truth, usefulness, restraint, handoff,
  durability, clarity, and AI-output judgment under pressure.
- Added the first Pre-Ship Integrity Gate template for meaningful public,
  client-facing, operator-facing, AI-assisted, data-sensitive, or reusable work.
- Wired the layer into the Consulting Workspace OS, documentation map,
  production roadmap, backlog, and steward receipt.

Priority impact:

1. Requirements Gatherer now handles discovery while Integrity Layer handles
   quality and handoff posture before ship.
2. The next consulting pattern scan should include integrity questions before
   any pattern candidate is promoted.
3. UAT Kit V0 should include quality/integrity UAT instead of only technical
   pass/fail checks.

Next review trigger:

- A public, client-facing, operator-facing, AI-assisted, or reusable artifact is
  ready to ship.
- The consulting pilot pattern scan produces promotion candidates.
- Toni says the standard feels too heavy, too abstract, too soft, or not
  strong enough.

## 2026-05-14: First Consulting Workspace OS Pattern Scan Completed

Source:

- `practice-os/efficiency/consulting-evidence-index.md`
- `practice-os/steward/2026-05-11-live-funnel-closeout-receipt.md`
- `practice-os/steward/2026-05-11-live-intake-operator-workflow-receipt.md`
- `docs/CONSULTING_WORKSPACE_OS_V0.md`

Change:

- Created four internal draft pattern candidates from the consulting/Hub live
  funnel evidence:
  - Hub-first intake with DTP source of truth.
  - Post-submit Diagnostic Call gating.
  - Noindex admin command-room boundary.
  - Proof/readiness receipt with synthetic-intake cleanup debt.
- Applied the Integrity Layer to each draft through misuse risk, dependency
  risk, clarity/complexity, proof required, simpler version, safer version, and
  documentation-before-ship checks.
- Kept all four candidates in draft state under
  `practice-os/research/pattern-candidates/`; none were promoted to
  `practice-os/patterns/`.

Priority impact:

1. The Consulting Workspace OS has now completed its first lean pilot scan.
2. The next Workspace OS proof point is real-use review, not more pattern
   inventory.
3. Requirements Gatherer should be applied on the next two meaningful requests
   before `tm-skills` skill creation is reconsidered.

Next review trigger:

- A real prospect intake uses the Hub-first intake and Diagnostic Call route.
- A client/admin surface needs a command-room boundary decision.
- UAT Kit V0 starts and can reuse the proof/readiness receipt candidate.
