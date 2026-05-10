---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Evolution System V0

Status: internal operating spine

Owner repo: `diagnose-to-plan`

## Thesis

The practice needs a durable way to keep valuable ideas, collaboration
patterns, research signals, messaging language, and client lessons from being
captured once and forgotten.

The system should be ambitious about learning, but conservative about authority.

Core rule:

> Capture broadly. Promote deliberately.

V0 is not autonomous self-learning. It is a human-gated evolution loop that
turns useful raw material into better decisions, templates, patterns,
messaging, and future implementation proposals.

## Why This Exists

Toni and the agent often discover valuable working patterns mid-conversation:

- a better way to ask clarifying questions;
- a better way to keep a ledger;
- a sharper practice message;
- a reusable client-delivery move;
- a research signal that should change future diagnostics;
- a mistake that should become a guardrail;
- a workflow that worked once and should be tried again.

Without an evolution system, those ideas either stay in chat or become
lightweight Kaizen rows with no path to deeper development. This system creates
that path.

## Source Of Truth

DTP owns the evolution rules and promoted memory.

| Surface | Owns | Does Not Own |
|---|---|---|
| DTP | evolution rules, templates, promoted patterns, messaging knowledge base, steward receipts | live client-private truth, public copy authority, autonomous runtime |
| `consulting` | public storefront after DTP-approved copy/proof decisions | practice memory, raw ideas, private signals, evolution authority |
| private engagement vault | private client context and live engagement truth | reusable public claims without review |
| Notion | sanitized mirror/cockpit after review | source of truth, private raw memory, autonomous status changes |
| Hub | runtime support when explicitly scoped | practice strategy, memory promotion, raw relationship records |

## V0 Loop

```text
raw signal -> Kaizen capture -> idea evolution record -> review lenses
-> promotion decision -> artifact/update proposal -> steward receipt
```

The loop should increase resolution without turning every idea into immediate
work.

## CLI Workflow

Use the CLI when a captured idea is ready to become a reviewable working
artifact:

```powershell
.\.venv\Scripts\dtp.exe evolution new "Keep a visible ledger in strategy threads"
.\.venv\Scripts\dtp.exe evolution new --from-kaizen kzn-YYYYMMDD-slug-hash
.\.venv\Scripts\dtp.exe evolution new "Owners buy clarity before automation" --kind research-pattern
.\.venv\Scripts\dtp.exe evolution status
```

The command creates:

- idea and meta-pattern records in `practice-os/evolution/records/`;
- research and field-observation candidates in
  `practice-os/research/pattern-candidates/`.

This is an operator workflow, not an autonomous promotion engine. The draft
still needs review before it becomes decision memory, pattern memory, playbook
memory, public copy, or implementation work.

## Memory Levels

Use the existing Practice OS memory ladder:

| Level | Meaning | Authority |
|---|---|---|
| raw_capture | unreviewed input, idea, email, meeting note, or observation | captured only |
| working_memory | useful for the current thread or active work block | temporary guidance |
| decision_memory | accepted decision, status, or boundary | can guide future work |
| pattern_memory | reusable pattern with evidence and limits | can be applied with judgment |
| playbook_memory | durable operating rule, template, or standard | should be followed until changed |

Reusable memory starts only after review. Raw capture is not playbook memory.

## Operating Rules

- Keep a visible working ledger during strategy, offer, proof, positioning,
  product-shaping, or long planning threads.
- Ask clarifying questions when they materially improve the output or help Toni
  understand where the work is going. Keep most questions non-blocking and
  momentum-preserving.
- Use question checkpoints for substantial strategy/build work:
  1. Start with a compact ledger.
  2. State what the agent thinks it is building, why it matters, and the likely
     path.
  3. Ask one to three questions that help Toni steer, learn, or increase
     resolution before the next meaningful layer.
  4. Offer the practical path and the ambitious path when a meaningful fork
     exists.
  5. Build the next useful slice with labeled assumptions if the answers are
     not required to proceed.
  6. Ask checkpoint questions again before moving into a new meaningful layer
     on longer builds.
- Preserve the ambition of the idea before reducing it to risks.
- Separate prototype thinking from production authority.
- Treat squads and agent roles as review lenses unless Toni explicitly asks for
  delegated agent work.
- Let research propose updates, not authorize them.
- Let messaging drafts inform future copy, not silently change public surfaces.
- Use client work as evidence only after permission, redaction, and proof gates.
- Close, supersede, or park ideas explicitly so they do not linger forever.

## Review Lenses

Apply only the lenses that materially improve the record:

| Lens | Question |
|---|---|
| Consulting Strategy | Does this sharpen the buyer, offer, proof, pricing, or scope story? |
| External Communications | Does this improve how Toni explains or sends something? |
| Product Strategy | Does this clarify what should be built, piloted, watched, or ignored? |
| UX / Design | Does this change how a user, client, or operator experiences the work? |
| Software Architecture | Does this change system boundaries, authority, data flow, or integration shape? |
| Software Engineering | Does this become scoped implementation work? |
| QA / Audit | What evidence or regression test would prove this works? |
| General Counsel | Does this touch legal, proof, permission, COI, privacy, or contracting risk? |
| COO | Does this improve operating cadence, handoff, or accountability? |

V0 does not create new autonomous Practice Steward or Memory Steward agents.
Those are functions performed through this loop, Kaizen, templates, and steward
receipts.

## Pilot Lanes

### 1. Messaging Knowledge Base

Use `practice-os/comms/private/messaging-knowledge-base-2026-05-10.md` as the
first internal consolidation of:

- owner bottleneck language;
- 10-second, 30-second, 60-second, and 2-minute explanations;
- claims and metaphor candidates;
- visual asset seeds;
- internal-only vs future public-copy candidate language.

Do not move this language to the consulting site until the public-copy gate is
opened.

### 2. Research Pattern Extraction

Use `practice-os/templates/research-pattern-candidate.md` when a research
signal, business story, store observation, client conversation, or market note
should become a reusable pattern candidate rather than a loose summary.

Research pattern candidates should state:

- the observation;
- the underlying principle;
- the consulting translation;
- possible artifacts;
- evidence limits;
- next experiment.

### 3. Meta-Pattern Evolution

Use `practice-os/templates/idea-evolution-record.md` when a collaboration move,
agent behavior, process tweak, repeated mistake, or new system idea should be
developed beyond Kaizen capture.

Accepted playbook memory:

- `practice-os/evolution/records/2026-05-10-question-checkpoint-rule-for-substantial-strategy-build-work.md`
  records the question-checkpoint rule as a standing collaboration protocol for
  substantial strategy/build work.

### 4. Visible Cockpit Later

The current accepted sequence is iterative:

1. Keep the former path now: CLI/operator-first capture and review records.
2. Plan the latter path later: a visible cockpit/dashboard once two or three
   real evolution records prove the right fields, views, and review rhythm.

Do not build the cockpit before the record workflow has real usage evidence.

## Promotion Decision

Each evolved idea should end in one of these states:

- `parked`: saved, but not worth building now;
- `working_memory`: useful for the current lane, not general yet;
- `decision_memory`: accepted boundary or operating decision;
- `pattern_candidate`: worth testing again;
- `pattern_memory`: reusable after evidence review;
- `playbook_memory`: durable rule/template after approval;
- `superseded`: replaced by a better artifact;
- `discarded`: intentionally rejected.

## Acceptance Criteria

V0 works if:

- important ideas do not rely on chat memory;
- future agents can see what is raw, reviewed, promoted, or parked;
- useful collaboration methods become repeatable when they prove themselves;
- research becomes patterns and proposals, not random summaries;
- messaging gets sharper without prematurely changing public copy;
- public/client/legal/security actions stay approval-gated;
- the system keeps ambition alive without creating uncontrolled backlog churn.

## Non-Goals

- No autonomous self-learning.
- No always-on hosted agent runtime.
- No live Notion writes.
- No consulting site copy changes.
- No client communication.
- No public proof movement.
- No automatic agent spawning.
- No new CRM or private relationship store.
- No vector database or retrieval implementation.
