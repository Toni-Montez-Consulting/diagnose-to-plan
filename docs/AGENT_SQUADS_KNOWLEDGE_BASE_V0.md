---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Agent Squads + Knowledge Base V0

Status: DTP-owned operating model for human-led agent squads, source-indexed
knowledge, business justification, approval gates, and handoff receipts.

Owner: `diagnose-to-plan`

Consulting role: public storefront and proof surface only. Consulting may point
to this operating model, but it does not own squad state, private knowledge, or
practice-wide sequencing.

## Thesis

Agent squads are a way to organize work, not a license to create autonomous
workers. V0 gives future agents a clear operating structure:

- which squad owns the work;
- what knowledge sources are allowed;
- what business/operator problem is being solved;
- what approval is required before continuing;
- what evidence and handoff receipt must survive the session.

The goal is to make the practice easier to run and easier to trust without
installing a new framework, moving source of truth out of DTP, or letting model
roleplay outrun human judgment.

## V0 Boundary

V0 is manual and human-led.

| Area | V0 Decision |
|---|---|
| Source of truth | DTP markdown docs and templates |
| Persistence target | hosted DTP records later, after real receipts prove the shapes |
| Interaction surface | story activation plus squad handoff receipts |
| Central squad board | future story, not V0 |
| External frameworks | inspiration only; no install, dependency, or copied operating state |
| Agent spawning | only when Toni explicitly asks for agents, delegation, or parallel agent work |
| Public proof | blocked until evidence, permission, redaction, reviewer, caveat, and approval pass |
| Client communication | draft/review only unless a human approves sending |
| Production writes | blocked until repo-local and approval gates pass |
| Repo mutation | blocked unless the owning repo lane is active and the work is explicitly scoped |

## Inspiration Sources

The linked frameworks are useful patterns, not operating dependencies:

- `https://github.com/bradygaster/squad`: persistent, human-directed agent teams,
  repo-local role files, decision sharing, and oversight close to the code.
- `https://github.com/SuperClaude-Org/SuperClaude_Framework`: structured
  commands, specialized agents/personas, modes, MCP routing, and knowledge docs.

DTP should borrow the durable ideas: persistent roles, explicit knowledge scope,
commands/modes, approval gates, and routing. DTP should not install either
framework, copy their repo structure, or imply their agents can act without the
existing human gates.

## V0 Squads

| Squad | Owns | Does Not Own | Primary Templates |
|---|---|---|---|
| Delivery Squad | repo/codebase management, architecture review, implementation scope, tests, verification, release/handoff notes | business value claim by itself, public proof, client comms, production writes without gates | `agent-squad-charter.md`, `knowledge-scope-source-index.md`, `approval-gate.md`, `squad-handoff-receipt.md` |
| Business Justification Squad | buyer/operator problem, workflow fit, business value, proof posture, usefulness, approval posture | code implementation by itself, unsupported ROI claims, pricing/public offer changes without review | `business-justification-scorecard.md`, `knowledge-scope-source-index.md`, `approval-gate.md`, `squad-handoff-receipt.md` |

Both squads can be active on one story. Delivery decides how the work should be
built and verified. Business Justification decides why the work deserves time,
what simpler alternative was considered, and whether it creates useful value.

## Specialized Agent Roles

Squads are the operating container. Specialized agent roles are the discipline
lenses inside that container.

The long-term vision is a coordinated system of specialized operational
intelligences that can contribute expert reasoning, critique, drafting,
validation, and execution support while staying human-led and approval-gated.
This should feel like an elite multidisciplinary team, not one generic assistant
pretending to do everything.

Current DTP-owned role specs live in `practice-os/agents/`:

| Role | Primary Use | Status |
|---|---|---|
| Consulting Strategy | practice positioning, offer logic, buyer fit, scope shape, pricing posture, value case, proof posture, and proposal framing | draft |
| Controller | financial summaries, weekly/monthly close inputs, pipeline arithmetic, and operating metrics | draft |
| COO | operating rhythm, meeting prep, engagement runbooks, handoffs, and install plans | draft |
| DevOps / Infrastructure | deployment readiness, CI/CD, environments, runtime boundaries, observability, secrets posture, rollback planning, cost awareness, and operational handoff | draft |
| External Communications | customer-facing and professional messages, client/prospect email summaries, sendable drafts, and Gmail draft receipts | draft |
| General Counsel | COI, contracting gates, proof permission, and legal-risk routing | draft |
| Memory Steward | memory visibility, promotion/parking recommendations, source-of-truth checks, drift risk, and human-gated memory levels | draft |
| Product Strategy | product direction, user/persona clarity, feature prioritization, launch sequencing, adoption loops, value proposition, roadmap shape, and product-market learning | draft |
| QA / Audit | verification strategy, regression risk, release readiness, acceptance checks, quality gates, and honest go/no-go language | draft |
| Software Architecture | system boundaries, module shape, integration design, technical tradeoffs, data flow, runtime authority, and architectural validation | draft |
| Software Engineering | scoped implementation, repo-grounded code changes, test selection, maintainability, integration safety, and technical handoff | draft |
| UX / Design | user experience, information architecture, visual hierarchy, interaction quality, responsive behavior, accessibility posture, and design-system fit | draft |

Future candidate roles include PR / Brand Narrative, Internal Review, Data
Architecture, Web Experience, Compliance, and Research.

Each specialized role must define:

- the domain it owns;
- the domain it does not own;
- allowed reads and writes;
- communication style or output format;
- collaboration points with other roles;
- refusal and escalation rules;
- regression fixtures that prove the behavior stays useful.

Use `practice-os/templates/specialized-agent-role-spec.md` when adding a new
role so the architecture stays consistent.

Roles do not authorize autonomous action. They improve reasoning, structure,
review quality, and handoff durability.

## First-Wave Role Boundary

The first wave is now intentionally broad enough to pilot:

- Consulting Strategy
- External Communications
- Product Strategy
- UX / Design
- Software Architecture
- Software Engineering
- DevOps / Infrastructure
- QA / Audit
- COO
- Controller
- General Counsel
- Memory Steward

Do not add more roles by default. Memory Steward was added because Toni
explicitly chose it as the first more active assistant behavior after the
Practice Evolution dashboard. Run these roles against real work first: client
emails, Greg/Cam deliverables, consulting site changes, Hub intake, Omnexus
proof/release gates, and practice operating decisions. Add another new role only
when a real repeated workflow does not fit the current set.

First public-safe role pilot:

- `practice-os/steward/2026-05-09-first-wave-agent-role-pilot-consulting-site.md`

Use this receipt as the baseline for future role pilots. A good role pilot
should name the artifact, the sources, the roles used, the decisions locked, the
questions still open, and the approval-gated actions.

## Knowledge Base V0

The V0 knowledge base is a source-indexed markdown discipline, not a vector
database.

Every squad-run story should name:

- authoritative source docs;
- repo-local files used;
- private sources that were intentionally excluded;
- evidence freshness and drift risk;
- what source would have to change before the conclusion should be revisited.

Source order:

1. Live repo state and accepted DTP docs.
2. Toni's latest direct instruction.
3. Repo-local AGENTS.md / `.repo.yml` / roadmap docs.
4. DTP policies, proof gates, and source-of-truth docs.
5. Private engagement records only when the current work is allowed to use them.
6. External frameworks or public research only as cited inspiration.

Blocked sources:

- secrets, credentials, raw private intake, private client financial details,
  Microsoft confidential material, unredacted logs, unsupported public claims,
  and chat-only memory that has not been promoted to a durable artifact.

## Business Justification Standard

Every squad-run work item must answer:

1. What business/operator problem is this solving?
2. Why is this worth doing now?
3. What existing evidence supports it?
4. What simpler alternative was considered?
5. What workflow, revenue, trust, delivery, or maintenance value does it create?
6. What approval is needed before continuing?

Longer-term ROI belongs at end-of-engagement or post-delivery closeout, after
real evidence exists. V0 should avoid invented ROI math.

## Approval Gates

Every squad-run item can carry an approval gate with these fields:

- `required_approver`
- `approval_state`
- `approval_scope`
- `stop_conditions`
- `approved_at`
- `approved_by`
- `evidence`

Allowed `approval_state` values:

- `not_required`
- `pending`
- `approved`
- `rejected`
- `blocked`

Stop conditions:

- public proof, screenshots, case-study language, metrics, or testimonials
  without proof/redaction gates;
- client or prospect communication that has not been reviewed;
- production writes, deploys, billing changes, database changes, live cloud
  mutations, or credentialed integrations without explicit approval;
- repo mutation outside the active owning lane;
- work that changes pricing, public offers, legal/compliance posture, tax or
  accounting interpretation, or client data handling without human review.

## V0 Workflow

1. Route the prompt through `practice-os/templates/activation-routing-map.md`.
2. Attach the story to `docs/ROADMAP_STORY_ACTIVATION_INDEX.md` or create a
   one-off story activation contract.
3. Select the owning squad or squads.
4. Fill a knowledge-scope/source index.
5. Fill the business justification scorecard when value, fit, proof, or client
   usefulness is involved.
6. Fill an approval gate if the work touches public proof, client comms,
   production writes, repo mutation, pricing, private data, or gated automation.
7. Execute the scoped work.
8. Leave a squad handoff receipt with sources, decisions, verification, gates,
   next action, and parked follow-up.

## First Pilots

The first implementation wave uses two related pilots:

1. the Client OS pilot wave in `docs/CLIENT_OS_PILOT_WAVE_2026-05.md`;
2. the consulting proof/offer lane, now including
   `practice-os/steward/2026-05-09-first-wave-agent-role-pilot-consulting-site.md`.

The Client OS wave proves whether source-indexed packets, draft-only automation,
approval gates, and handoff receipts work in real operating loops. The
consulting proof/offer lane proves whether those records can safely guide public
copy and proof presentation without moving private client material into the
storefront repo.

Allowed:

- source-indexed preparation for Greg, CCAAP, and Cam in the private engagement
  vault;
- source-indexed review of DTP offer/proof docs;
- business justification scorecard for a consulting offer/proof move;
- Delivery Squad review of consulting docs or public-site implementation scope;
- Business Justification Squad review of buyer problem, workflow fit, proof
  strength, and client/operator usefulness.

Blocked:

- exposing private client data;
- publishing proof before proof gates pass;
- changing public consulting copy from private/unreviewed material;
- turning consulting into the squad source of truth.

## Future Hosted DTP Records

When V0 receipts prove useful, hosted DTP can persist:

- squad charter;
- squad assignment;
- knowledge scope;
- source index;
- business justification scorecard;
- approval gate;
- squad handoff receipt;
- central squad board item.

Markdown remains the fallback import/export and recovery surface. Hosted records
should improve durability and retrieval, not replace the source-index habit.

## Acceptance Checks

A future agent should be able to answer:

- Which squad owns this work item?
- Which sources are authoritative and which are blocked?
- What is the business/operator justification?
- What approval is required before continuing?
- What stop condition would block public proof, client communication,
  production writes, or repo mutation?
- Where is the handoff receipt?
- Is this a V0 manual workflow, a hosted DTP future record, or a parked central
  board idea?
