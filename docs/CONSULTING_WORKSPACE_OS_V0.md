---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Consulting Workspace OS V0

Status: additive DTP plan artifact.

Use this document when Toni asks about the Consulting Workspace OS, asks to make
agents ask better questions before building, asks how the practice should learn
from work across repos, or wants a future agent to continue the Workspace OS
plan without rereading the originating email thread.

## Purpose

The Consulting Workspace OS is the internal operating layer that makes every
client build, app build, site pass, hotfix, launch, proof pass, and handoff make
the next one sharper.

It is not a new public product, dashboard, CRM, or autonomous agent manager. It
is a DTP-owned operating system for turning repeated work into better
requirements, better patterns, better verification, better handoffs, and better
builder judgment across Toni's workspace.

V0 preserves the email idea and adds two foundational modules:

- the Requirements Gatherer, a systematic requirements-discovery protocol that
  replaces ad hoc "clarifying questions" with risk-sized discovery;
- the Integrity Layer, a craft and quality standard that makes stronger
  choices easier under pressure.

## V0 Boundary

This slice is intentionally additive.

- DTP owns the canonical plan and operating protocol.
- Consulting is the first pilot surface, not the source of truth.
- Hub remains runtime support for intake and private console records.
- `tm-skills` is the future cross-project skill layer after the DTP protocol
  has been reviewed through real use.
- Project repos are pattern sources and implementation targets only when their
  own lanes are active.
- No parallel `_system/` tree is created.
- No public consulting copy, app code, hosted DTP behavior, Hub route, calendar,
  client communication, proof publication, or global skill install is changed by
  this plan.
- Integrity Layer artifacts live under `practice-os/`, not a parallel
  `_system/` tree.

## Locked Decisions

| Decision | V0 lock |
|---|---|
| Source of truth | DTP-owned |
| Product shape | Internal OS for Toni plus agents |
| First pilot | Consulting |
| First workflow | Pattern loop |
| First agent-behavior module | Requirements Gatherer |
| First quality module | Integrity Layer |
| First quality gate | Pre-Ship Integrity Gate |
| Daily surface | DTP docs and CLI first |
| Promotion gate | Human-reviewed |
| Pattern priority | Delivery and handoff |
| Approved output | Reusable playbook only after proof |
| 30-day success | Less rediscovery |
| V1 feel | Operator manual, not SaaS dashboard |
| First scan scope | Consulting only |
| Business role | Invisible leverage behind the practice |
| First follow-on module | UAT Kit |
| Skill posture | DTP protocol first, `tm-skills` skill later |

## Existing Surface Map

| Surface | Current role | Workspace OS implication |
|---|---|---|
| DTP `docs/` | Canonical roadmap, source maps, operating plans, review loops | Owns the plan, sequencing, and additive integration |
| DTP `practice-os/` | Policies, templates, agents, skills, steward receipts, reviewed patterns | Owns reusable operating artifacts and human-gated promotion |
| Kaizen and Practice Evolution | Capture and promote meaningful ideas deliberately | Receives raw/improving signals before they become playbook memory |
| `consulting` | Public storefront, proof surface, `/start`, noindex admin room | First pattern-scan pilot, but not the private OS |
| Hub | Runtime intake and private console support | Source of runtime evidence only; not a CRM replacement or DTP cockpit |
| `tm-skills` | Cross-repo SDLC behavior for coding agents | Future home for a Requirements Gatherer skill after DTP protocol review; Integrity Layer skill behavior waits for real use |
| Project repos | Delivery and proof evidence | Provide pattern candidates only when their lane is touched |
| Notion | Mobile mirror and capture surface | Optional cockpit later, never source of truth by default |

## Gap Ledger

| Gap | Current state | V0 action |
|---|---|---|
| Pattern loop | Reviewed bottleneck patterns exist, but consulting-specific delivery patterns are not yet scanned as a batch | Use consulting as the first scoped pattern scan |
| Requirements gathering | Question checkpoint rule exists, but not a full tiered requirements protocol | Add Requirements Gatherer V1 in this plan |
| Integrity / craft standard | Custom UI, proof, handoff, and anti-slop rules exist, but the deeper quality standard is scattered | Add Integrity Layer V0 and a Pre-Ship Integrity Gate |
| UAT and visual QA kit | UAT Kit V0 now exists as a manual DTP standard and receipt template | Pilot it on the next meaningful consulting, app-release, client-handoff, or proof-readiness check |
| Tool registry | Tooling Steward exists, but tool-choice facts are not yet a reusable registry | Keep as later module after pattern loop |
| Platform operating patterns | Vercel/Supabase-style behaviors are useful, but not yet translated into tool-neutral practice patterns | Add Platform Operating Patterns V0 as manual templates and draft pattern candidates |
| Design reference vault | Custom craft standard exists, but reusable reference/component rules are early | Keep as later module after UAT Kit |
| Skill packaging | `tm-skills` exists, but Requirements Gatherer is not yet a skill | Defer skill until protocol survives one review |
| Dashboard or hosted workflow | Many docs exist, but no need for more UI before the manual loop is useful | Keep dashboard/hosted surfaces later |

## Requirements Gatherer V1

The Requirements Gatherer turns "ask clarifying questions" into a repeatable
pre-build protocol. Its job is to help Toni think more clearly, give agents
more context, and produce build-ready work without making small tasks feel
heavy.

### Activation

The gatherer activates by risk and ambiguity.

| Tier | Use when | Expected question volume | Default artifact |
|---|---|---:|---|
| Micro | Mechanical edits, obvious cleanup, tiny hotfixes, low-risk docs | 0-3 | Chat checkpoint or labeled assumption |
| Standard | Normal feature/change with some product or implementation choices | 5-15 | Requirements brief |
| Deep | Cross-surface feature, public/client-facing work, major UX/backend/ops work, unclear success criteria | 20-50 | Build-ready brief plus decision ledger |
| Workshop | New product, major system, business model, large cross-repo program, high ambiguity | 50-100 | Iterative brief, ledger, phased plan |

Use elastic ranges. Stop early when the work is decision-complete.

### Escalation Rule

If discovery shows the work is larger, riskier, more public, more client-facing,
or more ambiguous than first estimated, the agent must:

1. State the original tier and the proposed new tier.
2. Explain the evidence for escalation.
3. Ask permission before continuing into deeper discovery.
4. Preserve the current locks so Toni does not have to repeat himself.

Do not silently turn a small request into a workshop.

### Question Batching

For Standard, Deep, and Workshop discovery, ask 5-6 questions at a time. Each
batch should materially change scope, success criteria, interface design, data
model, verification, rollout, tone, ownership, risk, or handoff.

Avoid filler questions. If the repo or environment can answer something, inspect
first instead of asking Toni.

### Default Coverage

When relevant, the gatherer should cover:

- user or audience;
- problem and trigger;
- desired outcome;
- in scope and out of scope;
- examples and anti-examples;
- UX and interaction expectations;
- data, privacy, security, and source-of-truth boundaries;
- backend/API/state/persistence needs;
- operational workflow and ownership;
- testing, QA, and acceptance criteria;
- rollout, rollback, and monitoring;
- proof, public-copy, client, COI, or permission gates;
- implementation constraints and repo boundaries;
- what Toni does not want the work to imply.

### Work-Type Question Packs

Use different packs by work type instead of one generic interview.

| Pack | Required focus |
|---|---|
| Feature | user, workflow, success criteria, state, edge cases, acceptance |
| Hotfix | urgency, impact, rollback, verification, affected users |
| Cleanup | ownership, deletion risk, traversal noise, validation, no-touch areas |
| UI/design | audience, desired feel, examples, anti-examples, assets, responsive behavior |
| Backend/data | source of truth, schema, API, auth, failure modes, migration, observability |
| Public copy/positioning | audience, promise, proof boundary, claims, voice, next action |
| Business strategy | buyer, offer, value case, constraints, risks, decision needed |
| Client work | client ask, permissions, private/public boundary, comms, handoff |
| Operations | owner, cadence, artifacts, status surface, exception path, review loop |

### Output

The default output is a Build-Ready Brief plus a Decision Ledger.

Use:

- `practice-os/templates/requirements-gathering-brief.md`
- `practice-os/templates/requirements-decision-ledger.md`

Micro work may stay in chat. Standard work should produce a concise brief.
Deep and Workshop work should create or update a durable DTP artifact before
implementation.

### Challenge Style

The gatherer should think with Toni. It should build the strongest useful
version of the idea, ask sharper questions, name weak spots, and propose better
paths without flattening momentum.

Use red-team posture only when Toni asks for critique, teardown, brutal honesty,
or risk review.

### Memory And Promotion

Do not save every question and answer by default.

Promote only:

- locked decisions;
- reusable patterns;
- build-ready briefs;
- accepted requirements;
- repeated misses or correction patterns;
- evidence-backed playbook candidates.

Raw or working records should stay in Kaizen, Practice Evolution, a local brief,
or a private engagement artifact until they are reviewed.

### Fast Override

Toni may bypass deeper discovery with explicit speed language such as:

- "emergency"
- "just do it"
- "skip requirements"
- "hotfix only"

Even then, the agent should keep a tiny safety gate for impact, rollback, and
verification unless the task is purely mechanical.

## Integrity Layer V0

The Integrity Layer is the quality standard underneath the Workspace OS.
Requirements Gatherer asks whether the work is understood well enough to build.
The Integrity Layer asks whether the work is honest, useful, restrained,
durable, clear, and cleanly handed off.

Canonical source:

- `practice-os/policies/integrity-layer-craft-standard.md`
- `practice-os/templates/pre-ship-integrity-gate.md`

Core line:

> Quality is downstream of process. Process is downstream of standards.
> Standards are downstream of values. Values only hold under pressure when they
> are built into the system.

The Integrity Layer should not become preachy public copy or an abstract values
essay. It should become a practical operating layer for:

- truthfulness in claims and proof;
- usefulness over impressiveness;
- restraint over excess;
- handoff over dependency;
- durability over speed theater;
- kindness through clarity;
- strength under pressure.

### Activation

Use the Integrity Layer when work is:

- public-facing;
- client-facing;
- operator-facing;
- AI-assisted in a way that affects claims, decisions, code, or UX;
- likely to become a reusable pattern;
- high enough risk that "it looks good" is not proof it is good.

Small mechanical work may skip the full gate with a labeled hotfix exception:
impact, rollback, and verification.

### Pre-Ship Gate

Use `practice-os/templates/pre-ship-integrity-gate.md` before shipping or
handing off meaningful public, client-facing, operator-facing, AI-assisted,
data-sensitive, or reusable work.

The gate does not replace tests, UAT, redaction, proof review, or client
approval. It asks whether the result is something Toni can defend.

## Pattern Loop V1

The first Workspace OS workflow is the pattern loop:

1. Identify a real completed or active work slice.
2. Extract pattern candidates from delivery, design, operations, QA, proof,
   handoff, or client communication.
3. Record practical cards, not essays.
4. Review before promotion.
5. Promote only after evidence shows the pattern is reusable.

### Pattern Card Interface

A practical Workspace OS pattern card should capture:

- name;
- category;
- source repo or client lane;
- problem;
- context;
- solution;
- implementation notes;
- tools and dependencies;
- tests or verification;
- handoff notes;
- integrity check;
- use when;
- do not use when;
- last validated;
- related patterns;
- promotion state.

Use `practice-os/templates/business-pattern-candidate.md`,
`practice-os/templates/research-pattern-candidate.md`, or a narrower future
pattern-card template depending on the source.

### Consulting Pilot Scan

The first scan should stay scoped to the consulting lane and produce practical
cards from already-proven work:

- live `/start` funnel to Hub intake;
- post-submit Diagnostic Call path;
- noindex `/admin` command-room boundary;
- public proof posture and redaction gates;
- Steel Ledger visual/copy discipline;
- visual QA and live readiness receipts;
- Hub runtime evidence while DTP remains source of truth;
- labeled synthetic intake cleanup debt.

The output should be a small set of internal pattern candidates, not public copy
or new consulting-site changes.

First lean scan completed on 2026-05-14 as internal draft candidates:

- `practice-os/research/pattern-candidates/2026-05-14-hub-first-intake-dtp-source-of-truth.md`
- `practice-os/research/pattern-candidates/2026-05-14-post-submit-diagnostic-call-gating.md`
- `practice-os/research/pattern-candidates/2026-05-14-noindex-admin-command-room-boundary.md`
- `practice-os/research/pattern-candidates/2026-05-14-proof-readiness-receipt-with-cleanup-debt.md`

These are not promoted playbook patterns. Review them after real use before
moving anything into `practice-os/patterns/`, public copy, client advice, offer
language, pricing, or a `tm-skills` behavior change.

## Long-Term Roadmap

### Phase 0: Map And Lock V0

- Keep this document as the canonical Workspace OS map.
- Add templates for requirements briefs and decision ledgers.
- Add the Integrity Layer craft standard and Pre-Ship Integrity Gate.
- Record a steward receipt and backlog pointer.
- Do not build runtime behavior.

### Phase 1: Pattern Registry V1

- Run the consulting pilot scan.
- Create practical pattern cards from real consulting closeout evidence.
- Include integrity questions before any pattern is promoted.
- Promote only human-reviewed cards.
- Preserve DTP as the source of truth.

### Phase 2: Requirements Gatherer Pilot

- Use the tier rubric on the next three meaningful requests.
- Track whether Micro, Standard, Deep, and Workshop sizing feels right.
- Record any misses in Practice Evolution or Agentic Performance Gap Review.
- Only then decide whether to create a `tm-skills` skill.

### Phase 3: UAT Kit V0

- Consolidate visual QA, journey QA, acceptance checks, browser/device checks,
  manual gates, and evidence receipts into one reusable package.
- Include Quality and Integrity UAT checks from the Integrity Layer.
- Start with consulting and one app or client project.

Status: V0 added on 2026-05-14.

Canonical sources:

- `docs/UAT_KIT_V0.md`
- `practice-os/templates/uat-receipt.md`
- `practice-os/steward/2026-05-14-uat-kit-v0-receipt.md`
- `practice-os/steward/2026-05-14-consulting-live-funnel-uat-pilot-receipt.md`
- `practice-os/steward/2026-05-14-consulting-public-assistant-uat-receipt.md`
- `practice-os/steward/2026-05-14-consulting-admin-command-room-uat-receipt.md`

Keep the kit manual and docs-first until repeated receipts prove what should
become a narrower visual QA, design integrity, mobile app, client handoff, or
agent-skill artifact.

Pilot result: three consulting UAT receipts landed as `pass_with_caveats`,
covering live-funnel proof-readiness, public assistant/no-runtime boundaries,
and noindex admin command-room boundaries without turning internal evidence into
public proof or runtime authority.

Friction review:

- `practice-os/steward/2026-05-14-uat-receipt-friction-review.md`
- `practice-os/steward/2026-05-14-workspace-os-uat-rollout-agent-flight-record.md`

Decision: keep the base UAT receipt canonical and use lightweight V0.1 modes
for proof-readiness, boundary-only, and operator-surface receipts. Do not create
separate UAT variants or `tm-skills` behavior until one more meaningful receipt
outside the current consulting boundary cluster proves repeated friction.

### Phase 3A: Platform Operating Patterns V0

- Extract the useful operating behavior from Vercel and Supabase without making
  them mandatory tools.
- Add manual templates for preview receipts, environment ledgers, data boundary
  ledgers, client handoff consoles, and launch momentum receipts.
- Add draft pattern candidates for preview-to-production, environment control,
  data boundaries, client handoff consoles, and launch momentum capture.
- Keep Greg's current soft-launch evidence deferred until after the next
  meeting and permission/redaction review.

Status: V0 added on 2026-05-14.

Canonical sources:

- `docs/PLATFORM_OPERATING_PATTERNS_V0.md`
- `practice-os/templates/platform-preview-receipt.md`
- `practice-os/templates/environment-ledger.md`
- `practice-os/templates/data-boundary-ledger.md`
- `practice-os/templates/client-handoff-console-spec.md`
- `practice-os/templates/launch-momentum-receipt.md`
- `practice-os/steward/2026-05-14-platform-operating-patterns-v0.md`

Keep the patterns manual and tool-neutral until at least one real Hub,
Omnexus, CCAAP, or Greg follow-up lane proves which pieces should become
reviewed patterns or skill behavior.

### Phase 4: Playbook Modules

- Tool registry and tool-choice rubric.
- Platform operating patterns promoted from V0 only after real receipts.
- Design reference vault and anti-generic UI rules.
- Design integrity review, client-duty rules, and AI usage standard if repeated
  work proves separate artifacts are useful.
- CRM/client operating layer choices.
- Telemetry and events taxonomy.
- Handoff and support playbooks.

### Phase 5: Skill And Agent Packaging

- Add a Requirements Gatherer skill to `tm-skills` only after one DTP review.
- Add trigger evals and expected outputs.
- Keep DTP as the canonical protocol and `tm-skills` as delivery behavior.
- Consider a standalone Requirements Gatherer agent only after the skill has
  real usage and misfire history.

### Phase 6: Hosted Or Dashboard Surface

- Add a dashboard, hosted DTP surface, Notion mirror, or CLI command only after
  the manual loop proves what fields and workflows are actually useful.

## V1 Acceptance Criteria

A future agent should be able to answer these from this document and linked
templates:

- where the Workspace OS lives;
- which repo owns the plan;
- what consulting is piloting first;
- how patterns are captured and promoted;
- when Requirements Gatherer activates;
- how much discovery to do;
- when to escalate;
- how to batch questions;
- what artifact to produce;
- how requirements feed memory without uncontrolled self-learning;
- which standard governs quality, truthfulness, restraint, and handoff;
- when to create a `tm-skills` skill;
- what remains out of scope.

## Future Implementation Prompt

Use this prompt only after reviewing this document and current repo state:

```text
Implement the next Workspace OS slice from
docs/CONSULTING_WORKSPACE_OS_V0.md. Start with the consulting pilot pattern
scan, Requirements Gatherer pilot, and Integrity Layer gate. Keep DTP as source of truth, do not edit
public consulting copy, do not create a parallel _system tree, and do not create
a tm-skills skill until the DTP protocol has been reviewed once. Produce a
small set of practical pattern candidates, use the requirements brief and
decision-ledger templates when discovery is needed, apply the pre-ship
integrity gate when work is public, client-facing, operator-facing,
AI-assisted, or reusable, update the steward receipt and reprioritization log,
then run the DTP validation gates.
```
