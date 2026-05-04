# Offer-Led Practice Packaging

Status: internal offer-packaging source for the consulting practice.

Owner: `diagnose-to-plan`, with later public-copy implementation in `consulting`.

Purpose: define the first sellable offers without flattening the broader Practice OS, Business Brain, Hub, proof, skills, and platform vision.

This is not public site copy yet. It is the source for a later consulting-site copy pass after proof and positioning review.

## Private Repertoire Layer

The public offer set stays intentionally simple, but the internal catalog is now
allowed to be broader. Use
`docs/INTERNAL_OFFER_REPERTOIRE_CATALOG.md` as the private source for reusable
capabilities that emerge from Toni's own operating system and client delivery.

Current private components include Google Workspace setup, business admin
cockpit setup, Apple Reminders capture bridges, logo/brand kit production,
mission/vision/message sprints, intake systems, admin rooms, client command
rooms, launch hardening, and follow-up queues. These are not automatically
public offers. They become public only after proof, privacy, permission,
repeatability, and positioning gates are clear.

## Positioning Thesis

Toni builds practical AI and software operating systems for people and businesses that need better execution, not another strategy deck.

The practice combines:

- custom software implementation;
- AI-assisted operating systems;
- launch and proof hardening;
- workflow diagnosis;
- owner/admin command rooms;
- private evidence and redaction discipline;
- reusable verification and handoff patterns.

The public offer should feel concrete, evidence-backed, and operator-led. The internal machine can be deep; the external package should be simple enough for a good prospect to understand quickly.

## Offer Set V0

Keep the first public offer set to three offers.

### 1. Business / AI Operating System Sprint

Audience:

- founders, operators, solo owners, small teams, and high-agency professionals whose business knowledge lives in scattered notes, meetings, messages, spreadsheets, tools, and mental load.

Painful problem:

- the business has real momentum, but decisions, follow-up, context, proof, and execution are fragmented.

Promise:

- turn messy business context into a working operating rhythm, practical AI-assisted workflows, and durable artifacts the owner can actually use.

Deliverables:

- current-state diagnosis;
- workflow map;
- priority operating loops;
- AI/tooling opportunity score;
- starter command or assistant workflow where useful;
- runbook and handoff packet;
- proof/redaction and data-boundary notes;
- next 30-day execution backlog.

Repo/tool support:

- DTP Business Brain;
- Practice OS templates;
- client reply/cadence patterns;
- Hub intake/runtime if needed;
- `tm-skills` only when software delivery work is part of the sprint.

Proof needed:

- redacted Business Brain or client cadence example;
- before/after workflow map;
- owner-safe runbook sample;
- proof packet showing how context became decisions/actions.

Intentionally not included:

- full SaaS platform build;
- unmanaged autonomous agents;
- QuickBooks writes;
- Notion as source of truth;
- client portal unless the command-room fit assessment says it is needed.

Best first public phrasing:

> I help operators turn scattered business context into working AI/software operating systems: workflows, decisions, runbooks, proof, and tools that make the business easier to run.

### 2. Launch / Proof Hardening Sprint

Audience:

- founders, client teams, and builders with an app, site, internal tool, or launch surface that is close but not yet trustworthy enough to share broadly.

Painful problem:

- the product exists, but launch confidence, proof, QA, privacy, support, handoff, and operational readiness are not tight enough.

Promise:

- turn a near-launch system into a credible launch, review, proof, or handoff package.

Deliverables:

- launch-readiness audit;
- hard/advisory/manual gate matrix;
- local/CI verification path;
- privacy/security/data-boundary review;
- launch checklist;
- owner/operator runbook;
- proof candidate inventory;
- first proof packet or redaction queue item.

Repo/tool support:

- Omnexus launch/review patterns;
- CLI verification automation pattern;
- mobile app review pattern when applicable;
- consulting proof standards;
- DTP proof templates.

Proof needed:

- Omnexus App Store journey, if cleared;
- Demario launch/admin readiness pattern, if owner-approved;
- CCAAP launch gates, once owner inputs and permission are complete;
- redacted verification evidence sample.

Intentionally not included:

- rewriting the product by default;
- live deploy without explicit approval;
- public proof without permission;
- broad platform automation before launch gates are understood.

Best first public phrasing:

> I help teams cross the last mile from "it works" to "we can trust it": launch gates, verification, proof, privacy boundaries, runbooks, and owner-ready handoff.

### 3. Client Command Room / Workflow System Sprint

Audience:

- owners or teams with recurring operational work after launch: bookings, tasks, follow-up, admin routines, content updates, approvals, support, or multi-person handoff.

Painful problem:

- work keeps falling into texts, memory, spreadsheets, and manual reminders after the site/app/tool ships.

Promise:

- create a focused owner-facing command room or workflow system only where recurring operations justify it.

Deliverables:

- command-room fit assessment;
- workflow and role map;
- owner/admin task model;
- public/private boundary plan;
- initial dashboard or checklist concept;
- handoff rules;
- verification and support gates;
- future enhancement backlog.

Repo/tool support:

- Client Command Room pattern;
- DeMario admin portal reference;
- DTP private kits;
- Hub runtime support only if intake/admin records need a private console;
- project repo implementation when the fit assessment justifies code.

Proof needed:

- DeMario command-room screenshots/walkthrough only after owner permission and redaction;
- CCAAP owner-launch process after permission;
- internal command-room fit/spec examples.

Intentionally not included:

- portal for every client;
- CRM/billing/time tracking by default;
- private client data in public repos;
- Hub replacing DTP or the client repo.

Best first public phrasing:

> When a site or app needs an operating layer, I design the owner/admin workflow behind it: tasks, dashboards, handoffs, proof, and support rhythms that keep the thing useful after launch.

## Not Yet Standalone Offers

These ideas have value, but should not be public offers yet:

| Idea | Stage | Why not yet | Activation condition |
|---|---|---|---|
| Business Brain Capture | Later | useful internal method, but too abstract as a standalone buyer-facing offer | two real client cycles produce clear before/after artifacts |
| Hosted DTP / private Practice OS | Later | internal source-of-truth and persistence layer, not a public product yet | real artifacts repeatedly need hosted persistence |
| Public AI assistant | Hold | trust/source/refusal/logging gates not accepted | source corpus and refusal fixtures pass |
| DSE/Azure readiness proof | Hold | COI and professional boundary risk | explicit COI, permission, and redaction review |
| Autonomous operating agents | Hold | relationship, permission, and production-write risk | reviewed narrow workflow with rollback and human approval |
| QuickBooks/finance connector | Hold | money/records/source-of-truth risk | read-only model and finance controls accepted |

## Public Site Translation Rules

When this becomes `consulting` copy:

- lead with the buyer problem, not the internal system names;
- use "operating system" carefully as a practical business/workflow concept, not vague hype;
- keep DTP, Hub, and repo names mostly behind the scenes;
- show proof only after `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md` gates pass;
- keep operator voice: direct, specific, evidence-backed, not generic AI consultancy language;
- preserve the Steel Ledger/custom-authored interface standard;
- avoid implying live hosted DTP, Notion sync, QuickBooks integration, or autonomous agents.

## First Public Packaging Pass

The next consulting-site pass should:

1. simplify the primary offer language around the three offers above;
2. update `/start` so intake routes prospects into one of these offers;
3. keep proof frames honest until proof packets are approved;
4. keep Hub intake primary and Formspree fallback;
5. leave DTP private and source-of-truth owned.

## Proof Wishlist

| Offer | Strongest proof candidate | Current status |
|---|---|---|
| Business / AI Operating System Sprint | real client cadence/reply loop producing decisions, actions, and handoff | needs next client loop pilot |
| Launch / Proof Hardening Sprint | Omnexus launch/review journey; Demario launch/admin hardening | strong internal evidence, public permission/review still needed |
| Client Command Room / Workflow System Sprint | DeMario command room and CCAAP owner workflow | permission and redaction gates still needed |

## Decision Default

When a new idea could become either an offer, a feature, a proof packet, or platform work:

1. stage it in `docs/PRACTICE_MACHINE_OPERATING_MAP.md`;
2. ask what buyer problem it clarifies;
3. route proof through `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md`;
4. keep platform implementation later unless manual delivery proves the bottleneck.
