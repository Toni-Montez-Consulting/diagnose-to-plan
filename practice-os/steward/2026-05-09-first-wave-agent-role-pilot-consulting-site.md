---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# First-Wave Agent Role Pilot: Consulting Site / Business Plan

Date: 2026-05-09

## Purpose

Use the first-wave specialized agent roles against a real, public-safe workstream:
the consulting homepage, `/start` intake flow, `/blueprint` sample, and the
builder-led offer posture behind them.

This is not an autonomous runtime, hosted orchestrator, or permission to create
more agent roles. The goal is to prove that the current role set helps turn a
messy business/build conversation into sharper decisions, safer artifacts, and
clearer next actions.

## Source Frame

Primary sources:

- `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md`
- `practice-os/agents/README.md`
- `practice-os/agents/*.md`
- `practice-os/templates/activation-routing-map.md`
- `docs/PRACTICE_PUBLIC_OFFER_SEQUENCE.md`
- `docs/PRACTICE_BUILDER_LED_OFFER_MODEL.md`
- `docs/PRACTICE_HOMEPAGE_START_AND_BLUEPRINT_COPY_LOCK.md`

Consulting implementation surfaces:

- `consulting/src/pages/index.astro`
- `consulting/src/pages/start.astro`
- `consulting/src/pages/blueprint.astro`
- `consulting/src/components/ContactIntake.astro`
- `consulting/AGENTS.md`
- `consulting/docs/repo-os/agent-squads-knowledge-base.md`

Validation evidence from the site pass:

- `npm run build`
- `npm run assistant:qa`
- `npm run test:routes`
- `npm run doctor`
- `npm run security:secrets`
- local preview and screenshot pass for `/`, `/start`, and `/blueprint`

## Pilot Target

The pilot target is the live consulting front door:

- thesis: turn unclear ideas, broken workflows, and tech bottlenecks into
  practical systems that work;
- public doors: clarify the path, build the system, improve the system;
- entry path: broad public site, then fit call, then Blueprint, Fast Track, or
  Custom SOW;
- proof posture: Omnexus, DeMario, and the consulting system can be shown at
  proof-type level; Greg, Cam, and CCAAP remain emerging until complete and
  approved;
- business posture: Toni is a builder/advisor hybrid, not a generic AI
  consultant and not a cheap website or random automation shop.

## Role Pass

### Consulting Strategy

Finding: The current site thesis is directionally right. It avoids generic AI
consultancy language and frames the work around serious owners, founders, and
operators who need useful systems, clarity, implementation, and operating assets.

Decision: Keep the public offer broad first, then route into the Blueprint or a
more direct implementation path. Do not lead with detailed pricing on the
homepage. Keep the Blueprint as the paid diagnostic/entry artifact and credit it
toward implementation when appropriate.

Open question for Toni: What is the first public price anchor that feels honest
without attracting cheap-site buyers?

### Product Strategy

Finding: The public flow now behaves like a useful product funnel rather than a
static portfolio page:

1. visitor recognizes the problem;
2. visitor chooses the closest door;
3. visitor sees proof types;
4. visitor starts with a fit call;
5. intake answers route the next step.

Decision: Keep `/start` short and owner-friendly. It should triage for fit,
friction, timeline, readiness, and privacy context, not become a full consulting
questionnaire.

Open question for Toni: After the first few real submissions, what signal should
decide whether someone gets Fit Call, Blueprint, Fast Track, or Custom SOW?

### UX / Design

Finding: The Steel Ledger system still fits. The site should feel polished,
serious, and operator-built, without drifting into either cold consulting-firm
brochure language or overdesigned AI startup noise.

Decision: Keep the first viewport direct and practical. Use the Blueprint as a
supporting artifact, not the whole homepage. Keep proof cards concise and
readable. Continue checking desktop and mobile screenshots before calling visual
work done.

Open question for Toni: Does the homepage feel enough like "trusted builder" at
first glance, or does it still need more personal presence?

### Software Architecture

Finding: The current repo boundary is correct:

- DTP owns thesis, proof gates, role specs, templates, and operating receipts;
- consulting owns the public storefront and public-safe copy;
- Hub owns runtime intake storage and console behavior;
- Gmail/calendar/client comms remain approval-gated.

Decision: Do not move DTP source-of-truth material into the consulting repo.
Consulting should point back to DTP's role specs and operating model. Hub intake
migration can wait until the site contract is stable.

Open question for Toni: When Hub migration resumes, should the intake schema stay
minimal for now or capture richer scoring fields for future routing?

### Software Engineering

Finding: The site implementation is functionally complete for this pass. The new
route, updated intake fields, docs, tests, and route checks align with the
approved plan.

Decision: No more site feature work should happen until the current public flow
gets a human taste pass and the repo changes are packaged. Future engineering
work should be either bug fixes, Hub migration, or analytics/intake proof.

Open question for Toni: Should the current consulting changes be committed as
one coordinated business-plan/site pass, or split into public-site and operating
docs commits?

### Software Architecture + DevOps / Infrastructure

Finding: The build and local preview path worked, but the preview restart hit a
Windows command-wrapper issue. The recovery rule is now explicit: after stream
disconnects or command wrapper failures, verify process state, restart with the
right shell command, and recapture evidence instead of trusting prior status.

Decision: Use `npm.cmd` style invocation when needed on Windows preview/build
wrappers. Do not treat a local preview as live deployment. Do not run Hub
migrations or production writes without explicit approval.

Open question for Toni: Before live deploy, do you want a manual screenshot
receipt attached in DTP, or is test output plus local review enough?

### QA / Audit

Finding: The route and assistant QA checks passed during the site pass. The
remaining risk is not compile correctness; it is business precision, public
proof wording, and whether real prospects understand what to do next.

Decision: Keep proof language at proof-type level until redaction and permission
gates are complete. Keep `/admin` noindex and sitemap-excluded. Keep privacy
warnings visible on `/start`.

Open question for Toni: Which proof card should be strongest on the page today:
Omnexus, DeMario, or the consulting operating system?

### External Communications

Finding: The strongest immediate use of the External Communications Agent is
client/prospect replies, not marketing copy. Every client email should start
with a summary of what the sender said, what they want, what changed, and the
recommended response.

Decision: Draft external emails with clear structure, spacing, and action items.
Create Gmail drafts when requested and available. Do not send without explicit
approval.

Open question for Toni: Should public inbound leads receive a short human reply
first, or should they get a structured "here is what I heard / here is the next
step" response immediately?

### COO

Finding: The operating model is strongest when each conversation produces a
ledger, an artifact, and a next action. The user should not have to remember the
remaining locks from chat.

Decision: Use dated receipts for meaningful pivots, especially after disconnects,
client calls, site-positioning work, and agent-system changes.

Open question for Toni: Which recurring weekly review should own this system:
practice thesis, client queue, public site, or operating infrastructure?

### General Counsel

Finding: The current public posture is safer than metric-heavy case studies. It
uses proof categories and implementation patterns without implying specific
outcomes that have not been approved for public use.

Decision: No client names, outcomes, screenshots, testimonials, or private
details move public without proof/redaction gates.

Open question for Toni: Are Omnexus and DeMario approved only as named proof
cards, or can they also support short story excerpts once the copy is reviewed?

### Controller

Finding: The pricing and income-replacement model is still internal strategy,
not public copy. The business plan can use price anchors to guide fit and
capacity planning, but the homepage should not become a menu of cheap services.

Decision: Keep public pricing light. Use the Blueprint as the clearest public
buy-in mechanism. Use internal pricing bands and capacity math to guide offer
discipline.

Open question for Toni: Should internal pricing rules be locked next as a
capacity plan, an offer menu, or a statement-of-work template?

## Decisions Locked By This Pilot

- Keep the first-wave role set; stop adding roles by default.
- DTP remains the system-of-record for agent roles, proof gates, and operating
  receipts.
- Consulting remains the public storefront and does not become the agent-system
  source of truth.
- External communication workflows now start with an email/request summary
  before drafting.
- Reconnects, timeouts, and stream disconnects require live verification before
  claiming status.
- Human approval remains required before client communication, live deployment,
  public proof, repo access, production writes, Gmail sends, or calendar changes.

## Next Best Actions

1. Run this same role set against the Greg post-call packet and follow-up loop.
2. Run it against the Cam mock valuation worksheet/product-spec memo.
3. Decide whether the current consulting site and DTP operating changes should
   be committed together or split.
4. Do a human taste pass on the consulting preview before live deploy.
5. Resume Hub intake migration later, after the public flow and triage language
   are stable.

## Ledger

Locked:

- First-wave specialized role set.
- DTP as source of truth for roles and operating receipts.
- Consulting as public storefront.
- External Communications Agent behavior for client/prospect emails.
- Reconnect recovery rule.
- No autonomous runtime yet.

Partial:

- Consulting site/business-plan implementation is built and validated locally,
  but not yet committed or deployed in this receipt.
- Hub intake migration is planned but intentionally deferred.
- Role system has one real public-safe pilot; it still needs Greg/Cam loops to
  prove repeatability.

Open:

- Commit/package strategy.
- Final human taste pass.
- Public price anchor and internal capacity model.
- First real inbound lead handling pattern.

Blocked / Approval-Gated:

- Gmail sends.
- Calendar changes.
- Live deploy.
- Hub migration.
- Public proof expansion.
- Client screenshots, metrics, testimonials, or story excerpts.

## Honest Assessment

This direction has real value. The role system is becoming a practical operating
layer, not a toy agent roster. The biggest risk is role sprawl before behavior
is proven. The best next move is to use the current roles on Greg and Cam, watch
where the outputs get sharper, and only then decide whether more roles,
automation, or hosted orchestration are justified.
