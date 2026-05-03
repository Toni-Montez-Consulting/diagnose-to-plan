# Workspace And Business Evidence Dossier

Date prepared: 2026-05-03

Status: internal DTP synthesis. This is not public proof, site copy, a sales
page, or an assistant source corpus. It is a correction-ready reconstruction of
the workspace, business, implementation state, roadmap, and idea inventory.

Evidence standard:

- Verified repo fact: found in current checked-out files.
- Verified git fact: found in current `git status`, `git log`, or command output.
- Memory-derived context: found in Codex memory or rollout summaries; useful
  for continuity, but weaker than current repo state.
- Inference: reasoned synthesis from multiple verified sources.
- Open question: not provable from available sources.

Post-closeout update on 2026-05-03:

- DTP PR #1 `Promote DTP V2 harness foundation` merged into `main` at
  `f5d1f20` after GitHub Actions passed.
- CCAAP PR #1 `Refine CCAAP civic prototype` merged into `main` at
  `fd18b92` after GitHub Actions passed.
- Consulting `main`, DTP `main`, and CCAAP `main` are clean and synced with
  origin after the PR closeout.
- The git-state snapshot later in this dossier is preserved as the verified
  state at the time the dossier was prepared, not the current post-merge state.

## 1. Executive Reconstruction

Toni is building a consulting practice and operating system for owner-led
businesses that need real implementation, not just tool suggestions. The core
business promise is to translate messy owner/operator context into working
systems: intake paths, workflow redesign, software, automations, assistants,
runbooks, proof packets, and operating handoffs.

The strongest current framing is:

- "An engineer for businesses without a software team."
- "The operator's engineer."
- "The business-to-system translation layer."
- "Operating systems for owner-led businesses."

The product is not one app. It is a practice stack:

1. DTP is the private Practice OS and source of truth.
2. Business Brain / Consulting OS is the operating layer for Toni's own
   practice.
3. The consulting site is the public storefront and proof surface.
4. Hub is the runtime/intake/private console layer.
5. `tm-skills` is the reusable coding-agent SDLC behavior layer.
6. Sibling repos such as Omnexus, DeMario, CCAAP, DSE, Architected Strength,
   FamilyTrips, Hub prompts, and Hub registry are proof, reference, runtime, or
   client lanes, not a single merged platform.

The thesis is already documented in DTP: businesses have access to AI, but
access does not create value by itself. Value comes from capturing real
business context, finding the bottleneck, choosing the right first build,
translating the work into software and process, documenting the system,
measuring whether it helped, and improving it over time.

The practical loop is:

raw input -> intent brief -> clarifying questions -> assumptions -> context pack
-> opportunity score -> implementation spec -> build tasks -> exception
tracking -> runbook -> value ledger -> lesson memory.

Evidence:

- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:13-25`
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:37-58`
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:232-267`
- `docs/PRACTICE_PRODUCTION_ROADMAP.md:3-7`
- `README.md:7-9`
- `README.md:50-52`

## 2. North Star / Ethos

The ethos is practical, operator-centered, privacy-aware, and proof-driven.
This is not generic AI adoption. DTP's source thesis says the work is workflow
redesign with AI/software as the execution layer. The goal is not more
software. The goal is that the operator and the business run cleaner.

The desired feel:

- calm judgment over hype;
- plain-language technical translation;
- smallest useful system first;
- source material before claims;
- handoff and adoption before polish;
- evidence before public proof;
- human approval before memory promotion or agent autonomy;
- client ownership of the installed system.

Negative identity is equally important:

- not an AI agency selling vague transformation;
- not a chatbot shop;
- not a cheap dev shop;
- not a dashboard-first SaaS project;
- not a public proof machine that skips permission;
- not autonomous agents writing to business systems;
- not Notion as the private source of truth;
- not Hub as DTP, CRM, billing, or client portal.

Evidence:

- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:99`
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:251-267`
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:374-376`
- `AGENTS.md:86-90`
- `AGENTS.md:117-190`
- `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md:79-91`
- `docs/PRACTICE_SYSTEM_ARCHITECTURE.md:245-256`

## 3. Business Model

### Target customer

The early target is owner-led businesses and small teams with repeated manual
workflows, direct access to the decision-maker, weak internal systems, and
enough revenue to justify a paid audit or small build. The current strategy is
to narrow by problem pattern, not by industry.

Evidence:

- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:41`
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:421`

### Offer architecture

DTP's source thesis currently names six offer shapes:

1. AI Upgrade Audit.
2. Business Brain Capture.
3. AI Assistant for a Business Function.
4. Operating System Install.
5. AI Second Opinion.
6. Launch Sprint.

The strongest business lane appears to be the Operating System Install: a
bounded engagement that can include intake, CRM cleanup, lead follow-up,
documents, knowledge, automations, an assistant where appropriate, reporting,
runbook, handoff, and review. The smaller offers serve as wedges, diagnostics,
or trust-building entry points.

Evidence:

- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:510-641`
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:1603-1629`

### Public proof gap

The current site shell is stronger than the current public proof assets. DTP and
consulting both say public proof must be evidence-backed, redacted, permissioned,
reviewed, and caveated. The current public site direction is good, but the
remaining bottleneck is real source material and cleared proof, not more generic
copy.

Evidence:

- `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md:47-57`
- `docs/PRACTICE_VERIFICATION_SPINE.md:107-115`
- `C:\Users\tonimontez\consulting\docs\SITE_NEXT_PASS_ROADMAP.md:136-153`
- `C:\Users\tonimontez\consulting\docs\PROTOTYPE_DESIGN_ROADMAP.md:102-103`

## 4. Workspace Architecture

### DTP

DTP owns practice methodology, source-of-truth roadmap, private client kits,
redaction, COI, proof governance, Practice OS templates, Business Brain, hosted
DTP planning, workspace command center records, and operating methodology.

DTP does not own the public consulting site, Hub runtime rows, project repo code,
or client-facing portals by default.

Evidence:

- `README.md:3-24`
- `README.md:50-52`
- `docs/PRACTICE_PRODUCTION_ROADMAP.md:3-7`
- `docs/PRACTICE_SYSTEM_ARCHITECTURE.md:249-256`

### Consulting

The consulting repo owns the public storefront, proof surface, `/start`, and
noindex `/admin` command room. It is designed as a portrait-led operating record
with proof records, evidence drawers, redaction boundaries, and a structured
contact path. It keeps Hub intake as primary, Formspree as fallback, and email
as last fallback.

Evidence:

- `C:\Users\tonimontez\consulting\README.md:3-7`
- `C:\Users\tonimontez\consulting\README.md:34-44`
- `C:\Users\tonimontez\consulting\README.md:62-64`
- `C:\Users\tonimontez\consulting\AGENTS.md:16-18`
- `C:\Users\tonimontez\consulting\src\pages\index.astro:114-147`
- `C:\Users\tonimontez\consulting\src\pages\start.astro:11-31`
- `C:\Users\tonimontez\consulting\src\pages\admin.astro:145-162`

### Hub

Hub owns runtime/intake/private console support. It receives consulting intake,
stores operational runtime records, and supports private review. It does not own
DTP methodology, DTP engagement kits, billing, CRM replacement, or client portal
behavior by default.

Evidence:

- `docs/PRACTICE_PRODUCTION_ROADMAP.md:110-115`
- `docs/PRACTICE_SYSTEM_ARCHITECTURE.md:111-134`
- `practice-os/efficiency/hub-repo-manifest.md:16-20`
- `practice-os/efficiency/hub-repo-manifest.md:50-55`

### `tm-skills`

`tm-skills` is a separate version-controlled personal skills repo for reusable
software-development behavior across coding agents. It is not DTP, not a client
vault, not a CRM, and not a public product.

Evidence:

- `docs/PRACTICE_PRODUCTION_ROADMAP.md:25`
- `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md:3-19`
- `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md:21-29`
- `practice-os/efficiency/tm-skills-repo-manifest.md:16-20`

### Sibling repo roles

The sibling repo landscape is broad but deliberately classified:

- `fitness-app` / Omnexus: verification cockpit reference, app-review learning
  pattern, and app-release evidence.
- `demario-pickleball-1`: adjacent project launch, proof, and Client Command
  Room reference.
- `ccaap-site`: first client operating-kit public-site implementation, blocked
  on owner inputs.
- `architected-strength`: personal brand OS and later assistant-pattern
  candidate.
- `hub-prompts`: prompt catalog consumed by Hub.
- `hub-registry`: prompt routing and automation-target governance.
- `engineering-playbook`: adjacent reference/doctrine maintenance.
- `FamilyTrips`: privacy-first adjacent project maintenance.
- `dse-content`: COI-aware internal/professional proof lane; current DTP
  manifest/evidence coverage is missing in the Workspace Command Center output.

Evidence:

- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:315-349`
- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:601-609`
- `docs/PRACTICE_SYSTEM_ARCHITECTURE.md:260-270`
- `.venv\Scripts\python.exe -m dtp workspace report` output on 2026-05-03

## 5. Implemented Work Ledger

### Current live git state before this dossier was added

DTP:

- Branch: `v2/harness...origin/v2/harness [ahead 12]`.
- Untracked before this dossier: `practice-os/steward/2026-05-02-practice-os-module-chain-pilot.md`.
- Recent commits:
  - `5a164d4 Add practice intelligence control plane`
  - `fe01c00 Add Practice OS module templates and evidence closeout`
  - `b076617 Document DTP ADR convention`
  - `11024f0 Integrate Practice OS source material`
  - `89cc6d2 Add Practice OS agent appendage`
  - `1001060 Add agent memory optimization plan`
  - `a39e3ec Record business brain memory tooling closeout`
  - `7809b9c Add practice tooling steward pattern`
  - `24a3706 Add practice memory control plane`
  - `e80700c Add client reply intake and cockpit loop`
  - `96a6493 Add client cadence and consulting assistant manifest`
  - `e16ac35 Stabilize business brain operating sprint`

Consulting:

- Branch: `main...origin/main [ahead 1]`.
- Recent ahead commit: `d334ebe Add consulting public assistant source fixtures`.

Sibling repo live status sampled on 2026-05-03:

- `hub`: clean on `main...origin/main`.
- `tm-skills`: `main...origin/main [ahead 1]`.
- `fitness-app`: clean on `main...origin/main`.
- `demario-pickleball-1`: clean on `master...origin/master`.
- `dse-content`: clean on `dev...origin/dev`.
- `ccaap-site`: `main...origin/main [ahead 2]`.
- `architected-strength`: clean on `main...origin/main`.
- `hub-prompts`: clean on `main...origin/main`.
- `hub-registry`: clean on `main...origin/main`.
- `engineering-playbook`: clean on `main...origin/main`.
- `FamilyTrips`: clean on `main...origin/main`.

Evidence type: verified git fact from live `git status --short --branch` and
`git log --oneline --decorate` commands run on 2026-05-03.

### What was actually built in DTP

Recent DTP work programmatically delivered:

- Practice Intelligence Control Plane.
- Practice Memory Control Plane.
- Practice Tooling Steward.
- Business Brain / Consulting OS lane.
- Business Brain command contracts and first fixtures.
- Controller, General Counsel, and COO role specs.
- Private-first comms drafts.
- Recurring client cadence pattern.
- Client reply intake pattern.
- Practice OS source material integration.
- Manual module templates: Thought Inbox, Input Studio, Context Pack,
  Opportunity Score, Exception Register, Value Ledger, Memory Review Queue.
- Workspace Command Center V0 read-only report.
- Hosted DTP Phase 0 design boundary.
- Proof/redaction templates and evidence-source checklists.
- Repo manifests and evidence indexes for most workspace lanes.

Evidence:

- `docs/ROADMAP_EXECUTION_BACKLOG.md:260-278`
- `docs/ROADMAP_EXECUTION_BACKLOG.md:280-306`
- `docs/PRACTICE_PRODUCTION_ROADMAP.md:57-98`
- `practice-os/templates/`
- `practice-os/commands/`
- `practice-os/agents/`
- `practice-os/fixtures/business-brain/`

### Tooling nuance

The bare `dtp workspace report` command was not on PATH in this shell. The repo
documented invocation worked:

`.\.venv\Scripts\python.exe -m dtp workspace report`

That command produced the Workspace Command Center V0 report and confirmed its
own V0 boundary: it reads recorded DTP artifacts only and does not execute
checks, call GitHub, mutate repos, install skills, publish proof, touch
production systems, touch DSE, or build FAOS.

Evidence:

- `README.md:23`
- `README.md:98`
- `docs/WORKSPACE_COMMAND_CENTER_V0.md:10-18`
- live command output on 2026-05-03

## 6. Active Client / Proof Lanes

### Cameron / SMB M&A platform

Current state:

- Follow-up packet sent from Toni's Gmail on 2026-05-02.
- Cameron replied on 2026-05-02 and said he will send requested items.
- Current state is waiting on the requested item packet.
- Future communications should use the personal email recorded in the private
  kit unless Cameron asks otherwise.

Business/product shape:

- Cameron is exploring an SMB buy/sell platform with valuation features.
- First useful build slice: valuation worksheet, buyer/seller qualification
  forms, and a simple dashboard/output flow using mock data.
- Full marketplace, transaction workflow, legal templates, data room, and live
  sensitive data are explicitly not first.

Risks/gates:

- No live buyer/seller/tax/EIN/financial/deal materials.
- No public proof without written permission and redaction.
- No repo access until GitHub username, safe-artifact confirmation, and
  guardrail acceptance.
- No valuation claims before data source, method, caveats, audience, and output
  are clear.

Evidence:

- `engagements/cameron-mckesson/client-context.md:16-29`
- `engagements/cameron-mckesson/client-context.md:40-41`
- `engagements/cameron-mckesson/client-context.md:67-93`
- `engagements/cameron-mckesson/smb-ma-platform/send-now.md:29-43`
- `engagements/cameron-mckesson/smb-ma-platform/send-now.md:82-97`
- `engagements/cameron-mckesson/smb-ma-platform/plan.md:25-49`
- `engagements/cameron-mckesson/smb-ma-platform/plan.md:59-107`

### Greg / TheGrantApp.io

Current state:

- Follow-up packet sent on 2026-05-02.
- Current state is waiting on Greg's reply.

Business/product shape:

- The next step is not a giant rebuild.
- The high-leverage lane is launch readiness: onboarding, trust in grant
  matches, what a user should do next, and learning from a first soft-launch
  group without harming first impression.

Risks/gates:

- Do not publish or draft public case-study language until Greg confirms
  permission boundaries in writing.
- Do not claim pricing, approval, conversion, or launch status until Greg
  confirms.
- Soft launch can harm adoption if onboarding or bugs create confusion.

Evidence:

- `engagements/greg-thegrantapp/case-study-sprint/send-now.md:27-33`
- `engagements/greg-thegrantapp/case-study-sprint/send-now.md:67-92`
- `engagements/greg-thegrantapp/case-study-sprint/plan.md:17-20`
- `engagements/greg-thegrantapp/case-study-sprint/plan.md:50-82`

### CCAAP / Mom nonprofit site rebuild

Current state:

- CCAAP is intentionally waiting.
- Clarification reply sent to Dad and Leah on 2026-05-02.
- Latest recorded state: no owner clarification reply yet.

Blocked by:

- PayPal donation link verification.
- PayPal membership hosted-button verification.
- Contact form destination and spam-protection preference.
- Meeting link label and destination conflict.
- Domain/DNS or Cloudflare access path.
- Authentic board/member photos and resources.
- Owner review.
- Proof decision.

Hard gates:

- No production DNS move.
- No fake PayPal/contact/meeting replacements.
- No public proof claim.
- No member/payment/contact/private data in repo or Notion.
- No assistant/chatbot lane.

Evidence:

- `engagements/mom-nonprofit/site-rebuild/waiting-state.md:14-24`
- `engagements/mom-nonprofit/site-rebuild/waiting-state.md:36-45`
- `engagements/client-follow-up-send-queue-2026-05-02.md:75-89`
- `practice-os/efficiency/ccaap-site-repo-manifest.md:16-20`
- `practice-os/efficiency/ccaap-site-repo-manifest.md:37-55`

### Omnexus / fitness-app

Current state:

- Omnexus is a reference implementation for verification cockpit, App Store
  review-to-launch learning, app-release evidence, and future client mobile app
  patterns.
- Current sampled repo state is clean on `main...origin/main`.
- DTP Workspace Command Center reports live proof checklist, local, and CI
  evidence as pass or pass-with-manual-gates.

Use:

- Use DTP's mobile app review pattern for future client app builds.
- Keep Omnexus source changes repo-owned and explicitly scoped.
- Do not publish Omnexus proof until proof gates pass.

Evidence:

- `practice-os/efficiency/fitness-app-repo-manifest.md:16-20`
- `practice-os/efficiency/fitness-app-repo-manifest.md:31-39`
- `practice-os/efficiency/fitness-app-repo-manifest.md:50-55`
- `practice-os/efficiency/fitness-app-evidence-index.md:25-29`
- `docs/PRACTICE_VERIFICATION_SPINE.md:26-54`
- live git status on 2026-05-03

### DeMario / demario-pickleball-1

Current state:

- DeMario is the command-room reference and adjacent local-business launch lane.
- Current sampled repo state is clean on `master...origin/master`.

Use:

- Keep as an internal reference implementation.
- Do not promote screenshots or claims into consulting until DTP proof packet
  flow clears them.
- Node/toolchain maintenance remains developer-facing.

Evidence:

- `practice-os/efficiency/demario-pickleball-1-repo-manifest.md:16-20`
- `practice-os/efficiency/demario-pickleball-1-repo-manifest.md:36-56`
- `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md:191-201`
- live git status on 2026-05-03

### DSE / dse-content

Current state:

- Current sampled repo state is clean on `dev...origin/dev`.
- Workspace Command Center reports DSE manifest/evidence coverage as missing.
- DSE remains a COI-aware internal/professional proof lane.

Use:

- Do not move, publish, or reuse DSE material publicly without COI, permission,
  and redaction review.
- Add DTP-owned manifest/evidence coverage only when explicitly selected or when
  the lane is clean and intentionally reopened.

Evidence:

- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:49`
- `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md:167-177`
- `.venv\Scripts\python.exe -m dtp workspace report` output on 2026-05-03
- live git status on 2026-05-03

## 7. Roadmap

### Done / implemented to current boundary

- DTP source-of-truth roadmap.
- Business Brain / Consulting OS lane.
- Practice Intelligence Control Plane.
- Practice Memory Control Plane.
- Practice Tooling Steward.
- Client reply intake and recurring cadence patterns.
- Business Brain command contracts.
- First Greg, Cameron, and Mom/Mario fixtures.
- Private-first comms kit.
- Practice OS source material integration.
- Manual module templates.
- Hosted DTP Phase 0 design boundary.
- Workspace Command Center V0 report.
- Proof/redaction templates.
- Consulting public assistant source/refusal fixtures.
- Repo manifests/evidence indexes for most active lanes.
- Omnexus mobile app review-to-launch learning extraction.

Evidence:

- `docs/ROADMAP_EXECUTION_BACKLOG.md:253-278`
- `docs/ROADMAP_EXECUTION_BACKLOG.md:280-306`
- `docs/PRACTICE_PRODUCTION_ROADMAP.md:57-98`
- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:51-67`

### Active now

- Use Practice Intelligence Control Plane as broad-session preflight.
- Run the recurring client cadence and reply intake loop.
- Wait for Cameron's item packet.
- Wait for Greg's reply.
- Keep CCAAP parked until owner inputs arrive.
- Pilot Thought Inbox, Input Studio, Context Pack, Opportunity Score, Exception
  Register, Value Ledger, and Memory Review Queue on the next real reply/reset.
- Keep public proof moving only through DTP proof packet and redaction review.

Evidence:

- `docs/ROADMAP_EXECUTION_BACKLOG.md:280-306`
- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:1005-1032`
- `engagements/client-follow-up-send-queue-2026-05-02.md:15-17`
- `engagements/client-follow-up-send-queue-2026-05-02.md:36-89`

### Next

- Second-cycle client reply/template pilot.
- Seed Business Brain eval garden from real Cam/Greg/CCAAP reply examples.
- Accept/revise consulting public assistant manifest and route source corpus.
- Replace consulting proof placeholders with cleared source material.
- Capture CCAAP baseline/after-state evidence after owner review.
- Keep Hub prompt/registry validation local-first.
- Run `tm-skills` smoke prompts in external tools when practical.
- Add DSE manifest/evidence coverage only when selected with COI-aware scope.

Evidence:

- `docs/ROADMAP_EXECUTION_BACKLOG.md:276-304`
- `C:\Users\tonimontez\consulting\docs\ASSISTANT_PUBLIC_V0_SOURCE_CORPUS.md:3-7`
- `C:\Users\tonimontez\consulting\docs\ASSISTANT_PUBLIC_V0_REFUSAL_FIXTURES.md:7-11`
- `C:\Users\tonimontez\consulting\docs\LAUNCH_CHECKLIST.md:18`

### Mid-term

- Hosted private DTP schema/app shell after merged schema design and real pilot
  records.
- Client Operating Kit pilots and Client Command Room patterns.
- Public proof upgrade with real, redacted source material.
- Read-only evidence surfaces and support receipts.
- Cross-site assistant pattern after one narrow consulting assistant proves
  useful.
- Business ops/finance inputs as manual or read-only only.

Evidence:

- `docs/HOSTED_DTP_PHASE_0.md:7-30`
- `docs/HOSTED_DTP_PHASE_0.md:245-271`
- `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md:10-37`
- `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md:97-133`
- `docs/PRACTICE_MEMORY_CONTROL_PLANE.md:137-184`

### Long-term

- Client-facing portal only after real clients repeatedly need visibility.
- MCP/agent memory and richer automation only after artifacts, permissions,
  evals, and human review exist.
- FAOS orchestration readiness review after the current pilot/proof/smoke/Hub
  validation path.
- More durable execution tooling only when a workflow truly needs it.
- Red-team, eval, and observability expansion as risk justifies it.

Evidence:

- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:337-341`
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:1489`
- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:647-823`
- `docs/ROADMAP_EXECUTION_BACKLOG.md:214-227`
- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:1032`

### Parked / forbidden until unlocked

- Multi-tenant SaaS.
- Public proof auto-publishing.
- Autonomous client communications.
- QuickBooks write behavior or live imports.
- Notion as source of truth.
- Client portal before repeated client demand.
- Deep Hub/DTP sync before real need.
- Site-wide assistant rollout before one assistant proves useful.
- CCAAP assistant work before launch inputs and owner review.
- DSE public proof before COI, permission, and redaction.

Evidence:

- `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md:123-134`
- `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md:108-144`
- `docs/PRACTICE_MEMORY_CONTROL_PLANE.md:184-192`
- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:980-999`

## 8. Idea Inventory

### Captured and implemented as durable artifacts

- Practice OS as DTP's internal operating system.
- Business Brain / Consulting OS.
- Command contracts for diagnose, COI, proposal, and comms.
- Business role specs: Controller, General Counsel, COO.
- Client reply intake.
- Recurring client cadence.
- Proof packet and redaction queue.
- Practice Intelligence Control Plane.
- Practice Memory Control Plane.
- Tooling Steward.
- Workspace Command Center V0.
- Hosted DTP Phase 0.
- Custom interface craft standard.
- Mobile app review-to-launch pattern.
- Cross-site assistant architecture brief.
- Public consulting assistant source and refusal fixtures.
- Repo manifests/evidence indexes.

Evidence:

- `docs/ROADMAP_EXECUTION_BACKLOG.md:253-278`
- `docs/ROADMAP_EXECUTION_BACKLOG.md:203-209`
- `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md:10-37`
- `C:\Users\tonimontez\consulting\docs\ASSISTANT_PUBLIC_V0_SOURCE_CORPUS.md:3-7`
- `C:\Users\tonimontez\consulting\docs\ASSISTANT_PUBLIC_V0_REFUSAL_FIXTURES.md:7-11`

### Partially implemented ideas

- Hosted private DTP: design boundary exists; app/schema implementation is gated.
- Consulting public assistant: source corpus and refusal fixtures exist; runtime is
  blocked until tests/gates are accepted.
- Public proof system: templates exist; first real proof still needs source,
  permission, redaction, reviewer, caveat, and after-state evidence.
- `tm-skills`: installed/active to Codex boundary; external Claude Code and
  GitHub Copilot smoke tests remain manual.
- Workspace Command Center: V0 read-only report exists; live git/CI runner is
  intentionally not implemented.
- Business Brain eval garden: ready, but not seeded with enough real reply
  examples yet.

Evidence:

- `docs/HOSTED_DTP_PHASE_0.md:269-271`
- `docs/ROADMAP_EXECUTION_BACKLOG.md:237-239`
- `docs/ROADMAP_EXECUTION_BACKLOG.md:276-278`
- `.venv\Scripts\python.exe -m dtp workspace report` output on 2026-05-03

### Ideas captured but intentionally later

- Client-facing portal.
- FAOS orchestration substrate.
- Agent protocol watchlist.
- Rich MCP recall / vector memory.
- Read-only QuickBooks connector.
- Admin assistants.
- Cross-site assistant rollout.
- Supply-chain/red-team/observability expansion.
- Shared GitHub Actions and advanced caching.

Evidence:

- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:647-823`
- `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:928-956`
- `docs/ROADMAP_EXECUTION_BACKLOG.md:214-227`
- `docs/PRACTICE_TOOLING_STEWARD.md:90-119`

### Ideas only safe if corrected by future evidence

- Precise pricing, outside rough offer bands.
- Public claims about client outcomes.
- Case-study language for Greg, Cameron, CCAAP, Omnexus, DeMario, or DSE.
- Any claim that a client has approved proof.
- Any claim that a tool/assistant can access private records.
- Any claim that QuickBooks, Notion sync, or hosted DTP is live.

Evidence:

- `docs/PRACTICE_VERIFICATION_SPINE.md:107-115`
- `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md:123-134`
- `engagements/cameron-mckesson/smb-ma-platform/plan.md:59-62`
- `engagements/greg-thegrantapp/case-study-sprint/send-now.md:89-92`
- `engagements/mom-nonprofit/site-rebuild/waiting-state.md:36-45`

## 9. Claim Ledger

| Claim | Evidence type | Confidence | Source | Correction needed |
| --- | --- | --- | --- | --- |
| The core business is an implementation layer for owner-led businesses without a software team. | Verified repo fact | High | `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:13-25` | No |
| The practical method is raw input to value ledger to lesson memory. | Verified repo fact | High | `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:58` | No |
| The ethos is operator's engineer / business-to-system translation, not generic AI agency work. | Verified repo fact + inference | High | `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md:259-267`; `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md:79-91` | No |
| DTP is the private Practice OS and source of truth. | Verified repo fact | High | `docs/PRACTICE_PRODUCTION_ROADMAP.md:3-7`; `README.md:7-9` | No |
| Consulting is public storefront and proof surface. | Verified repo fact | High | `C:\Users\tonimontez\consulting\README.md:3-7` | No |
| Hub is intake/runtime support, not DTP or CRM. | Verified repo fact | High | `docs/PRACTICE_PRODUCTION_ROADMAP.md:110-115` | No |
| `tm-skills` is a cross-repo SDLC behavior layer, not a client vault. | Verified repo fact | High | `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md:3-19` | No |
| Public proof is the main business bottleneck. | Verified repo fact + inference | High | `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md:47-57`; consulting proof docs | No |
| Cameron lane is active but waiting on an item packet. | Verified repo fact | High | `engagements/cameron-mckesson/smb-ma-platform/plan.md:25-29`; `send-now.md:92-97` | No |
| Cameron first build slice is valuation plus buyer/seller qualification and dashboard/output flow using mock data. | Verified repo fact | High | `engagements/cameron-mckesson/smb-ma-platform/send-now.md:29-43` | No |
| Greg lane is active but waiting on reply. | Verified repo fact | High | `engagements/greg-thegrantapp/case-study-sprint/plan.md:17-20`; `send-now.md:89-92` | No |
| Greg's high-leverage lane is launch readiness, not a rebuild. | Verified repo fact | High | `engagements/greg-thegrantapp/case-study-sprint/send-now.md:27-33` | No |
| CCAAP is parked until owner inputs arrive. | Verified repo fact | High | `engagements/mom-nonprofit/site-rebuild/waiting-state.md:14-24` | No |
| CCAAP assistant work is blocked. | Verified repo fact | High | `engagements/mom-nonprofit/site-rebuild/waiting-state.md:41-45`; `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md:108-120` | No |
| Omnexus is a reference pattern, not current public proof. | Verified repo fact | High | `practice-os/efficiency/fitness-app-repo-manifest.md:16-20`; `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md:179-189` | No |
| DeMario is a command-room reference but public proof is blocked. | Verified repo fact | High | `practice-os/efficiency/demario-pickleball-1-repo-manifest.md:16-20`; `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md:191-201` | No |
| DSE is COI-aware and not ready for public proof. | Verified repo fact + live status | High | `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md:167-177`; live git status | No |
| Hosted DTP should not start as a dashboard. | Verified repo fact | High | `docs/HOSTED_DTP_PHASE_0.md:7-30` | No |
| First hosted DTP implementation should be schema/app shell only, not SaaS/client portal/deep Hub sync. | Verified repo fact | High | `docs/HOSTED_DTP_PHASE_0.md:269-271` | No |
| Consulting public assistant is real but pre-code. | Verified repo fact | High | `C:\Users\tonimontez\consulting\docs\ASSISTANT_PUBLIC_V0_SOURCE_CORPUS.md:3-7`; `docs/ROADMAP_EXECUTION_BACKLOG.md:237-239` | No |
| Cross-site assistant pattern should be manifest-governed, not generic chat widgets everywhere. | Verified repo fact | High | `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md:10-37` | No |
| Business Brain scope includes operations/admin/finance/reporting/pricing/valuation/compliance/handoff/support. | Memory-derived context + verified repo fact | High | `rollout_summaries/2026-05-01T14-00-42-mEyJ-business_brain_consulting_os_dtp_roadmap_implementation.md:8-24`; `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md:14-18` | No |
| DTP branch was ahead 12 before this dossier. | Verified git fact | High | live `git status` on 2026-05-03 | No |
| Consulting branch was ahead 1 before this dossier. | Verified git fact | High | live `git status` on 2026-05-03 | No |
| `dtp workspace report` is documented but bare `dtp` was not on PATH in this shell. | Verified command fact | High | failed bare command, successful `.venv` module command | No |
| The report should be a durable DTP artifact, not chat-only. | Memory-derived context + user request | High | `memory_summary.md:9`; user request | No |
| The business becomes stronger when every meaningful delivery leaves evidence, decisions, proof/redaction updates, or eval candidates. | Verified repo fact + inference | High | `docs/PRACTICE_SYSTEM_AUDIT_AND_GAP_REVIEW.md:255-266` | No |
| The public positioning and private operating stack are coherent but proof maturity is the limiting sales asset. | Inference from repo facts | Medium-high | consulting proof docs plus DTP audit/roadmap | Review by Toni |
| The current best next operational move is client cadence and template pilots, not a new platform build. | Inference from roadmap | Medium-high | `docs/ROADMAP_EXECUTION_BACKLOG.md:280-306`; `docs/WORKSPACE_PORTFOLIO_ROADMAP.md:1005-1032` | Review by Toni |

## 10. Correction Checklist For Toni

Use this section to mark what I got wrong or underweighted.

### Missing business direction

- Is the primary customer still owner-led businesses without software teams?
- Should the first buyer be narrower than owner-led businesses, for example
  local service businesses, nonprofits, founder-led SaaS, expert consultants, or
  SMB operators?
- Is "operator's engineer" the right front-door identity, or should another
  phrase lead?

### Missing offer / product lane

- Are AI Upgrade Audit and Operating System Install the right first public
  offers?
- Should Business Brain Capture become a public offer sooner?
- Should Launch Sprint be a standalone offer or only part of operating-system
  installs?
- Is the client-facing portal truly later, or do you want to pull a narrow
  client-view into near-term hosted DTP?

### Missing client/project

- Did I miss an active client or proof lane outside Cameron, Greg, CCAAP,
  Omnexus, DeMario, DSE, Architected Strength, Hub, `tm-skills`, FamilyTrips,
  Hub prompts, Hub registry, and engineering-playbook?
- Should CCAAP be treated as a client proof lane, family/private lane, or both?
- Should Architected Strength be treated as part of the consulting business or
  as separate personal-brand infrastructure?

### Misread priority

- Is public proof really the current business bottleneck?
- Is the next move client cadence/template pilots, or should hosted DTP move
  sooner?
- Should assistant work remain behind proof and CCAAP owner gates?
- Should `tm-skills` external smoke tests be treated as active, or are they
  acceptable manual follow-up?

### Misread tone / ethos

- Is "calm operator's engineer" too restrained?
- Should the public brand be more ambitious, more premium, more technical, more
  local-business oriented, or more founder/operator oriented?
- Should the site sound more first-person, more productized, or more advisory?

### Misclassified parked vs active work

- Hosted DTP app shell.
- Client portal.
- Cross-site assistant runtime.
- QuickBooks read-only connector.
- Notion mirror/sync.
- FAOS orchestration.
- DSE proof pass.
- Omnexus public proof.
- DeMario public proof.

## 11. What I Would Do Next

Recommended next action:

1. Toni reviews this dossier and marks corrections directly in this file or in
   a follow-up message.
2. Convert corrections into a DTP steward receipt or roadmap update.
3. Run the next real client reply through the new module chain:
   Thought Inbox -> Input Studio -> Context Pack -> Opportunity Score ->
   Exception Register -> Value Ledger -> Memory Review Queue.
4. Use the first corrected proof candidate to fill a proof packet and redaction
   queue item.
5. Only after those records exist, decide whether hosted DTP app implementation
   should start.

My current interpretation:

The business is most likely to work if it sells calm, high-trust
implementation to owner-led businesses, proves itself through real source
material and permissioned case evidence, and uses DTP internally so the practice
gets sharper after every client, every blocked proof claim, every support
handoff, and every agent-system miss.
