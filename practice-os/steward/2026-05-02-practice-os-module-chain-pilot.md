---
data_class: P0
confidential: false
permission_level: internal_only
review_status: checked
---

# Steward Receipt: Practice OS Module-Chain Pilot

Date: 2026-05-02

## Purpose

Run one real Practice OS input through the current manual template/control-plane
chain before implementing app features, hosted DTP, schema migrations, client
portals, autonomous agents, or unmanaged memory.

This is a documentation-only pilot. It preserves the source thesis and tests
whether the current artifacts can carry the full Practice OS loop.

## 1. Raw Input / Thought Inbox

### Capture

- Captured date: 2026-05-02
- Captured by: Codex with Toni approval
- Source type: chat
- Source pointer: current DTP infrastructure sprint thread
- Owning repo or engagement: `diagnose-to-plan`
- Raw input summary: Toni wants Practice OS to turn raw business thought into a
  repeatable implementation and learning chain that compounds over time.
- Phrases or framing to preserve:
  - "capture raw business thoughts"
  - "clarify them without blocking momentum"
  - "builds on itself without forgetting"

### Exact Input

> I want Practice OS to help me capture raw business thoughts, clarify them
> without blocking momentum, convert them into context packs, workflow maps,
> opportunity scores, implementation specs, build tasks, exception/value
> tracking, and human-approved memory so the consulting practice builds on
> itself without forgetting.

### Classification

| Question | Answer |
|---|---|
| Primary lane | infrastructure / product / memory |
| Sensitivity | internal-only |
| Urgency | this week |
| Needs DTP source-of-truth update | yes |
| Needs Notion mirror | optional sanitized status only |
| Needs human approval before reuse | yes |
| Blocking risk present | none for this pilot; future hosted memory/schema/app work remains gated |

## 2. Input Studio Extraction

### Intent Brief

- Core intent: make Practice OS a reliable business-to-system translation loop,
  not just a folder of prompts or a chat memory crutch.
- Business goal: reduce mental load while making consulting work compound
  through better capture, clarification, planning, implementation, exception
  learning, value tracking, and approved memory.
- User / owner need: Toni needs to trust that ideas, client context, decisions,
  and follow-up work will land in the right artifact and be findable later.
- Emotional tone: ambitious, practical, slightly urgent; preserve the sense that
  this is an operating system, not generic AI productivity software.
- Must include: raw capture, non-blocking questions, assumptions, context pack,
  workflow map, opportunity score, implementation spec, build tasks, exception
  register, value ledger, memory review, and reprioritization only when warranted.
- Must avoid: hosted app work, source-doc rewriting, generic SaaS framing,
  autonomous agents, unmanaged learning, premature schema migration, client
  portal behavior, and public proof claims.
- Success shape: one complete manual chain proves the current templates can move
  a real idea from raw thought to a scoped next implementation slice.

### Output Contract

- Output type: steward receipt / module-chain pilot
- Non-goals: no app code, no database migration, no hosted DTP, no portal, no
  autonomous agents, no unmanaged memory.
- Data boundaries: internal-only Practice OS infrastructure; no private client
  facts, raw transcripts, payment records, or confidential employer/client data.
- Proof boundaries: no public proof; no ROI claims.
- Source-of-truth update: this receipt in `practice-os/steward/`.
- Notion mirror allowed: "Practice OS module-chain pilot recorded; next slice is
  a structured manual chain runner or chain template." No raw thread content.

## 3. Clarifying Questions

These questions are non-blocking. The pilot proceeds with labeled assumptions.

| Question | Type | Blocking? | Why it matters | Default assumption if unanswered |
|---|---|---|---|---|
| Should the first productized chain remain file/template-first or become CLI-assisted immediately? | resolution | no | This affects the next slice size. | Start file/template-first, then add CLI only after one more pilot. |
| Should workflow maps get their own template before any app/schema work? | resolution | no | The pilot exposed this as the clearest missing module artifact. | Create a small workflow-map template before app work. |
| Should memory promotion become doctor-required now? | memory / governance | no | Too much enforcement too early can slow learning. | Keep memory review optional until two real cycles prove the shape. |

## 4. Assumptions

| Assumption | Confidence | Needs review? | Revisit trigger |
|---|---|---|---|
| DTP remains the source of truth for this chain. | high | no | Accepted roadmap or ADR changes. |
| This input is safe for tracked internal docs. | high | no | Private client facts or confidential data enter the chain. |
| The current manual templates are sufficient for a pilot. | medium | yes | The pilot feels too fragmented or duplicative. |
| Reprioritization is not needed unless the pilot changes the active next story. | high | no | Pilot reveals a more urgent missing infrastructure piece. |
| Durable playbook memory should wait for human approval and repeated usage. | high | no | Toni explicitly approves promotion. |

## 5. Context Pack

### Identity

- Context pack: Practice OS module-chain pilot
- Date: 2026-05-02
- Owner: Toni
- Repo or engagement: `diagnose-to-plan`
- Related source artifacts:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `docs/source/practice_os_build_spec_v0_1.md`
  - `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md`
  - `database/schema/practice_os_schema_v0_1.sql`
  - `docs/integration/integration_map.md`
  - `docs/integration/schema_reconciliation_v0.md`
  - `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md`
  - `docs/PRACTICE_MEMORY_CONTROL_PLANE.md`
  - `docs/ROADMAP_EXECUTION_BACKLOG.md`
- Current status: manual chain pilot in progress; no product behavior added.

### Situation

- What is happening: Practice OS has the thesis, source docs, schema starter,
  control-plane docs, and module templates, but needs proof that the chain can
  run end to end on a real idea.
- Why now: Toni has multiple live workstreams and wants an intelligence layer
  that reduces memory load before more client delivery.
- What changed recently: source material and templates were integrated; the
  verification audit accepted the next move as a real module-chain pilot.
- What should not change: source docs, hosted DTP gates, human-approved memory,
  DTP source-of-truth status, and privacy/proof/COI boundaries.
- Known constraints: no app code, SQL migration, hosted DTP, client portal,
  autonomous agents, unmanaged memory, raw transcript storage, or public proof.

### Current Facts

| Fact | Source | Confidence | Sensitivity |
|---|---|---|---|
| Practice OS is intended to turn messy business context into working systems. | `AGENTS.md`, source docs | high | public-safe / internal |
| Manual templates exist for Thought Inbox, Input Studio, Context Pack, Opportunity Score, Exception Register, Value Ledger, and Memory Review Queue. | `practice-os/templates/` | high | public-safe / internal |
| No dedicated workflow-map template exists yet. | current template inventory | high | public-safe / internal |
| Starter SQL is not an approved migration. | `docs/integration/schema_reconciliation_v0.md` | high | public-safe / internal |
| Hosted DTP and portal work remain gated. | ADRs, roadmap, Hosted DTP Phase 0 | high | public-safe / internal |

## 6. Workflow Map

No dedicated `workflow-map.md` template exists yet. This section records the
manual map for the pilot and marks that missing template as friction.

| Step | Input | Output | Owner | Gate |
|---|---|---|---|---|
| Raw capture | Rough business thought | Thought Inbox entry | Toni / Codex | preserve wording; classify sensitivity |
| Clarify | Raw capture | Questions plus default assumptions | Toni / Codex | ask at most three non-blocking questions |
| Shape | Clarified intent | Input Studio extraction | Codex | do not flatten thesis or voice |
| Pack context | Intent plus sources | Context Pack | Codex | separate verified facts from assumptions |
| Map workflow | Context pack | Workflow map | Codex | missing template; keep simple |
| Prioritize | Workflow / idea | Opportunity Score | Codex | advisory only; user intent remains primary |
| Specify | Selected slice | Work Item Spec | Codex | no app/schema work unless explicitly opened |
| Track build | Spec | Build tasks | Codex / future implementer | small, reviewable tasks |
| Learn from misses | Friction / exception | Exception Register | Codex | no blame; capture repair and lesson |
| Record value | Completed pilot | Value Ledger | Codex | internal value only; no fake ROI |
| Promote memory | Candidate lesson | Memory Review Queue | Toni | human approval required |
| Reprioritize | Meaningful event | Reprioritization note | Toni / Codex | only if priority changes |

## 7. Opportunity Score

| Dimension | Score | Notes |
|---|---:|---|
| Frequency | 5 | Every client, idea, meeting, and infrastructure stream needs this path. |
| Owner bottleneck relief | 5 | Directly reduces Toni's mental load. |
| Revenue or value proximity | 4 | Better intake and specs improve delivery quality before sales/proof. |
| Pain / urgency | 5 | Current work already spans Cam, Greg, CCAAP, Notion, tools, and infrastructure. |
| Data readiness | 4 | Templates and docs exist; product workflow is not automated yet. |
| Adoption likelihood | 5 | Matches Toni's existing working style. |
| Reusability | 5 | Can become the standard Practice OS operating loop. |
| Strategic fit | 5 | This is the core product thesis. |
| Learning value | 5 | Exposes which modules should become structured product behavior. |
| Complexity, lower is better | 2 | Documentation pilot is simple; productization later is larger. |
| Risk, lower is better | 1 | Internal-only and no app/data migration. |

- Priority score: high
- Recommended phase: now
- Best small slice: create one chain artifact and record friction.
- Why this is worth doing: it tests whether Practice OS can operate from its
  own source ideas before building more infrastructure.
- Why this may not be worth expanding immediately: one pilot is not enough to
  justify hosted app, schema, or enforcement gates.

## 8. Implementation Spec

### Outcome

Create a structured manual Practice OS chain pattern that turns one raw input
into a complete artifact trail and identifies the next scoped implementation
slice.

### User Or Operator Value

Toni can see the whole Practice OS loop in one place, verify that the thesis is
preserved, and decide what deserves productization without trusting chat memory.

### Scope

- Use existing templates/control-plane docs as the source shapes.
- Create one steward receipt containing the chain.
- Identify missing module/template friction.
- Avoid all app/runtime/schema behavior.

### Constraints

- No hosted DTP.
- No database migration.
- No client portal.
- No autonomous agents.
- No unmanaged memory.
- No source-doc edits.
- No public proof claims.

### Data Class

P0 internal-only infrastructure note. No private client data is included.

### Files Likely Touched

- This steward receipt.
- Reprioritization log only if priority changes.

### Acceptance Criteria

- Raw input is preserved exactly.
- Every requested module appears in the chain.
- Missing workflow-map friction is recorded.
- Next scoped slice is concrete.
- Memory promotion remains human-approved.

### Test Command

- `git diff --check`
- `.\.venv\Scripts\python.exe -m dtp practice doctor`
- `.\.venv\Scripts\python.exe -m dtp workspace report`

### Review Gate

Toni accepts whether this chain is useful enough to become a reusable template,
CLI-assisted workflow, or Workbench surface.

### Rollback

Remove this steward receipt before commit if Toni rejects the chain shape.

## 9. Build Tasks

These are proposed tasks only. They are not implemented in this slice.

| Task | Owner | Status | Gate |
|---|---|---|---|
| Create a dedicated workflow-map template. | Codex | proposed | Toni accepts this pilot finding. |
| Create a reusable module-chain-run template. | Codex | proposed | One more real input confirms the chain shape. |
| Add optional doctor visibility for module-chain assets. | Codex | parked | Do not make required until repeated use proves value. |
| Design a CLI-assisted chain runner. | Codex | parked | Manual template proves too slow or scattered. |
| Design merged hosted schema support. | Codex | later | Hosted DTP explicitly reopened and schema design accepted. |

## 10. Exception Register Entry

### Exception

- Date: 2026-05-02
- Source: manual Practice OS module-chain pilot
- Repo or engagement: `diagnose-to-plan`
- Detected by: verification audit plus pilot execution
- Severity: medium
- Status: open / observed

### Behavior

- Expected behavior: a raw idea should move through the full Practice OS chain
  without losing source language, decisions, gates, or memory promotion rules.
- Observed behavior: most modules have templates, but the chain is not yet a
  single product workflow. Workflow Map and Build Tasks are less formal than the
  other modules.
- Impact: future agents may scatter chain state across multiple documents unless
  the chain pattern is made reusable.
- Was private, client, financial, proof, or COI material involved: no.

### Diagnosis

- Root cause: the module vocabulary is preserved, but chain orchestration is
  still manual.
- Contributing factors: templates were added before repeated pilots; this is
  appropriate, but it creates some navigation overhead.
- What check would have caught this: this exact end-to-end pilot.
- Was this a one-off or repeat pattern: likely repeatable until a chain template
  or CLI-assisted runner exists.

### Repair

| Action | Owner | Status | Gate |
|---|---|---|---|
| Record this pilot artifact. | Codex | done | steward receipt created |
| Add workflow-map template later. | Codex | proposed | Toni accepts next slice |
| Pilot on one client reply before enforcing gates. | Codex | proposed | Cam, Greg, or CCAAP reply arrives |

### Learning

- Lesson: Practice OS needs a chain artifact or chain runner, not only separate
  module templates.
- Should this update a template: yes, later.
- Should this update a roadmap story: no priority change yet; backlog already
  names the second-cycle template pilot.
- Should this become an eval fixture: later, after one client-reply example.
- Should this become playbook memory: not yet.
- Human approval needed before reuse: yes.

## 11. Value Ledger Entry

### Value Record

- Date: 2026-05-02
- Repo or engagement: `diagnose-to-plan`
- Work item: Practice OS module-chain pilot
- Owner: Toni
- Audience: internal Practice OS operator
- Status: recorded

### Baseline

- Before state: Practice OS had source docs, templates, and control-plane docs,
  but the full chain was not visible in one concrete artifact.
- Pain or risk: future work could rely on chat memory or scattered templates.
- Baseline metric: one accepted audit finding that the product workflow is still
  mostly manual.
- Confidence: high
- Source: verification audit and current template inventory.

### After State

- What changed: one full manual chain now exists as a durable steward receipt.
- Current metric: all requested modules represented in one artifact.
- Confidence: high
- Evidence source: this file.
- Caveats: this is not product behavior and should not be marketed as public
  proof or ROI.

### Value Types

| Type | Present? | Notes |
|---|---|---|
| Time saved | yes | Future agents can see the intended chain shape quickly. |
| Revenue enabled | no | Too indirect for a claim. |
| Risk reduced | yes | Reduces chat-only memory and source-dilution risk. |
| Launch readiness improved | no | No public launch surface affected. |
| Owner clarity improved | yes | Names missing module friction and next slice. |
| Reusable pattern created | candidate | Needs one more use before pattern promotion. |
| Client trust improved | indirect | Better internal operation can improve client follow-through. |
| Learning produced | yes | Workflow-map and chain-runner gaps are visible. |

### Proof Boundary

- Internal only: yes
- Named public allowed: no
- Anonymized public allowed: no
- Evidence reviewed: internal only
- Redaction reviewed: not applicable
- Permission reviewed: internal-only
- Public claim draft: none

## 12. Memory Review Queue Entry

### Candidate

- Candidate date: 2026-05-02
- Source: this pilot receipt
- Repo or engagement: `diagnose-to-plan`
- Proposed memory title: Practice OS module-chain should be a first-class
  operating pattern
- Proposed memory level: decision memory now; pattern memory after repeated use
- Sensitivity: internal-only

### Source Summary

- What happened: the core Practice OS input was routed through the full manual
  module chain.
- Why it matters: it confirms the system needs chain orchestration, not only
  individual templates.
- Exact source paths:
  - `practice-os/steward/2026-05-02-practice-os-module-chain-pilot.md`
  - `practice-os/templates/thought-inbox.md`
  - `practice-os/templates/input-studio.md`
  - `practice-os/templates/context-pack.md`
  - `practice-os/templates/opportunity-score.md`
  - `practice-os/templates/work-item-spec.md`
  - `practice-os/templates/exception-register.md`
  - `practice-os/templates/value-ledger.md`
  - `practice-os/templates/memory-review-queue.md`
- Evidence: this complete chain artifact.
- Drift risk: medium; future template changes could supersede this shape.
- Refresh method: compare against current templates and roadmap before reuse.

### Promotion Review

| Question | Answer |
|---|---|
| Is this accurate enough to reuse? | Accurate as a V0 pilot, not yet a final playbook. |
| Is it broadly useful or project-specific? | Broadly useful for Practice OS. |
| Does it contain private or client details? | No. |
| Does it require redaction? | No. |
| Does it require permission? | Toni approval before promotion. |
| Is human approval recorded? | Not for pattern/playbook promotion yet. |
| Should this update a template, doc, roadmap, skill, eval, or memory index? | Template/doc later; no roadmap priority change yet. |

### Decision

- Decision: park for pattern promotion
- Approved memory level: decision memory candidate
- Approved by: pending Toni review
- Date: 2026-05-02
- Reason: one pilot is useful evidence, but not enough to promote to playbook
  memory or strict gates.

### Destination

| Destination | Update needed? | Notes |
|---|---|---|
| DTP doc | yes | This steward receipt. |
| Practice OS template | later | Create workflow-map or chain-run template after acceptance. |
| Roadmap / backlog | no | Current backlog already points to second-cycle template pilot. |
| Skill / eval fixture | later | Seed after a real client reply example. |
| Memory source index | later | Add if this keeps being rediscovered. |
| External memory | no | DTP remains authoritative. |

## 13. Reprioritization Note

No update to `docs/integration/reprioritization_log.md` is needed from this
pilot.

Reason: the current roadmap and reprioritization log already identify the
manual module templates as done and the next real template/client-reply pilot as
the active next step. This pilot confirms that direction rather than changing
priority.

## 14. Pilot Findings

### What Worked

- The raw input could be preserved without flattening the thesis.
- Thought Inbox, Input Studio, Context Pack, Opportunity Score, Work Item Spec,
  Exception Register, Value Ledger, and Memory Review Queue templates map well
  to the intended Practice OS loop.
- The control-plane boundaries were clear enough to prevent accidental app,
  schema, portal, or autonomous-agent work.
- Human-approved memory stayed explicit.

### What Felt Awkward Or Duplicative

- Input Studio, Context Pack, and Memory Review all repeat source/sensitivity
  metadata. That is acceptable manually, but a future product workflow should
  carry shared metadata forward.
- Opportunity Score and Work Item Spec overlap on "why now" and "scope"; a
  future chain runner should transform the score into the spec instead of
  making the operator retype context.
- Reprioritization is easy to overuse; this pilot did not justify a log update.

### What Template Or Module Was Missing

- Dedicated Workflow Map template.
- Dedicated Build Tasks template or build-task section standard.
- Dedicated module-chain-run template that ties the separate module templates
  together.

### What Should Become Structured Product Workflow Later

- Carry-forward metadata: source, sensitivity, owner, repo/engagement, and
  status should flow from raw input into all later artifacts.
- Question state: unanswered, answered, assumed, blocking, and revisited should
  be visible.
- Artifact links: context pack, workflow map, score, spec, tasks, exceptions,
  value records, and memory decisions should cross-link.
- Memory promotion: no pattern/playbook memory without explicit approval.
- Reprioritization: only meaningful events should trigger priority movement.

### What Should Remain Manual For Now

- Human approval for durable memory.
- COI, legal, privacy, security, compliance, money movement, irreversible
  actions, public proof, and client communication gates.
- Public proof permission, redaction, evidence, reviewer, and caveat checks.
- Hosted schema design and migrations.
- Notion mirroring.

### Next Scoped Implementation Slice

Create two small manual assets:

1. `practice-os/templates/workflow-map.md`
2. `practice-os/templates/practice-os-module-chain.md`

Keep them optional at first. Then run one live client reply through the chain
before making either template doctor-required or designing CLI/workbench
support.

### Reprioritization Log Decision

No reprioritization update is needed. The pilot validates the current active
direction rather than changing the work order.
