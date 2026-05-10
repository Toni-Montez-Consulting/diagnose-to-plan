---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Knowledge Base Event Workflows V0

Status: event-based maintenance rule

Owner repo: `diagnose-to-plan`

## Thesis

The practice should not rely on Toni manually remembering to refine every
knowledge base, agent role, prompt, template, operating rule, source list, or
execution pattern.

The right V0 is not autonomous agents. The right V0 is event-based,
human-gated maintenance.

This is a foundation for future autonomy, not a rejection of autonomy. The
practice should eventually support more squads, more specialized roles, and
bounded autonomous workflows. V0 records the events, decisions, sources,
destinations, and gates that future autonomous agents will need before they can
act safely.

Core rule:

> When a meaningful event happens, update the right knowledge surface or leave
> a decision record explaining why not.

## What Counts As An Event

| Event Type | Examples | Default Destination |
|---|---|---|
| Research signal | new AI report, platform release, governance guidance, saved article | Research Arm digest, source list, research decision record |
| Memory or meta-pattern | "this worked well", "always do this", repeated collaboration miss, new question protocol | Practice Evolution record, Memory Steward review, playbook memory candidate |
| Operating workflow | new cadence, client prep pattern, email sweep habit, ledger rule, status dashboard need | operating doc, template, steward receipt |
| Project execution | repeated repo task, validation pattern, delivery evidence need, timeout recovery | repo doc, DTP pattern, runbook, verification template |
| Client or prospect reply | email, call transcript, owner clarification, safe client fact | client reply intake, engagement receipt, proof/offer gate |
| Agent/system miss | skipped questions, stale context, lost connection, wrong routing, lightweight capture drift | agentic performance gap review, routing update, template change |
| Public/proof claim | case study claim, homepage line, outcome metric, proof card | proof promotion runbook, public claim review |
| Knowledge-base drift | stale doc, conflicting rule, missing route, repeated re-discovery | source map update, docs map update, steward receipt |

## Standard Workflow

Use this loop when a signal may need durable maintenance:

```text
event -> classify -> decide -> update -> receipt -> validate -> queue next review
```

1. Capture the event in the smallest useful artifact.
2. Classify the affected lane: research, memory, messaging, operations,
   project execution, client work, proof, repo docs, or agent roles.
3. Use a simple decision record when the event changes a rule, destination, or
   default behavior.
4. Update the owning knowledge base only when the destination is clear.
5. Leave a steward receipt for future agents.
6. Run the relevant validation check.
7. Park or schedule anything that should not be built now.

## Human-Gated Authority

Codex can assist by:

- noticing events;
- asking clarifying questions;
- proposing the destination;
- drafting or updating DTP docs/templates;
- creating decision records;
- summarizing source material;
- recommending promotion, parking, rejection, or a bounded experiment.

Codex cannot silently:

- promote raw capture into playbook memory;
- change public site copy;
- send client communications;
- install tools or connectors;
- create autonomous runtime behavior;
- update Notion as source of truth;
- mutate client/private data;
- change pricing, offers, proof claims, or legal/compliance language without
  approval.

## Squad Review Lenses

The squad concept is used as a review lens in V0.

| Lens | Use It When |
|---|---|
| Memory Steward | deciding what should be remembered, parked, promoted, or superseded |
| Research Steward | deciding whether a source becomes a digest, pattern candidate, radar item, spike, or parked signal |
| Consulting Strategy | changing offer, buyer, scope, pricing posture, proof language, or business model |
| External Communications | drafting or improving emails, client updates, sendable summaries, or executive notes |
| Product Strategy | deciding whether an idea becomes an experiment, feature, roadmap item, or no-go |
| Software Architecture | changing system boundaries, data flow, integration authority, or runtime posture |
| Software Engineering | turning a decision into scoped code, tests, docs, or repo changes |
| UX / Design | changing user flows, page spines, interface standards, or client-facing experience |
| QA / Audit | proving the change, identifying regression risk, or defining go/no-go criteria |
| General Counsel | touching legal, privacy, proof permission, COI, contracts, or sensitive client claims |
| COO | improving accountability, cadence, handoff, capacity, or operating rhythm |

Do not create new autonomous agent roles just because a lens exists. Promote a
role only after repeated use proves the current role set cannot cover the gap.

When repeated events show that a lens needs to become a role, squad, scheduled
workflow, or semi-autonomous function, capture that through a knowledge-base
event record and route it to Agent Squads, Practice Evolution, or FAOS
readiness. If the request would move any workflow beyond human-led review, also
route it through `docs/AUTONOMY_READINESS_LADDER_V0.md` and
`practice-os/templates/autonomy-readiness-review.md` before changing authority.

## Knowledge Base Destinations

| Destination | Owns |
|---|---|
| `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md` | idea, meta-pattern, messaging, and collaboration evolution rules |
| `docs/RESEARCH_ARM_V0.md` | research intake, digest, steward, and authority loop |
| `docs/RESEARCH_ARM_SOURCE_LIST_V0.md` | recurring source list and source-review triggers |
| `docs/PRACTICE_KNOWLEDGE_BASE_V1.md` | markdown-first knowledge corpus and future retrieval design |
| `docs/PRACTICE_MEMORY_CONTROL_PLANE.md` | chat-to-source memory durability and control-plane boundaries |
| `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md` | broad rehydration and input routing across clients, repos, tools, and knowledge |
| `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md` | human-led squad contracts, source-indexed handoffs, approval gates |
| `docs/AUTONOMY_READINESS_LADDER_V0.md` | staged readiness gate for read-only, draft-only, supervised, scheduled, live, or autonomous workflows |
| `practice-os/agents/` | role specs and read-only steward guidance |
| `practice-os/templates/` | repeatable forms, receipts, reviews, and records |
| `practice-os/comms/private/` | internal messaging and external-communications knowledge |
| owning repo docs | repo-specific implementation, validation, or runtime instructions |

## Default Artifacts

Use:

- `practice-os/templates/research-decision-record.md` for source-backed
  adopt/pilot/watch/reject/park decisions.
- `practice-os/templates/knowledge-base-event-record.md` for broad maintenance
  events that update or intentionally do not update a knowledge base.
- `practice-os/templates/autonomy-readiness-review.md` when a maintenance event
  suggests a workflow should move up the autonomy ladder.
- `practice-os/templates/idea-evolution-record.md` for meta-patterns,
  collaboration practices, and ideas that should mature.
- `practice-os/templates/agentic-performance-gap-review.md` for system misses.
- `practice-os/templates/roadmap-steward-review.md` when priority, status,
  ownership, or next work changes.

## Validation

Minimum validation for DTP-owned maintenance:

```powershell
.\.venv\Scripts\dtp.exe practice doctor
.\.venv\Scripts\dtp.exe research steward --limit 8
git diff --check
```

Add targeted tests when a CLI, required template, generated dashboard, routing
map, or repo-local behavior changes.

## Acceptance Criteria

This workflow is working if:

- Toni can forward or mention a signal and see where it went.
- Knowledge bases improve without Toni doing all maintenance by hand.
- Useful ideas are not lost between chats.
- Raw captures do not become public claims or autonomous behavior by accident.
- Future agents can identify the source, decision, destination, validation, and
  next review trigger.
- The system keeps moving without pretending every useful idea needs to be
  built immediately.
- Autonomy candidates become visible, staged, and testable instead of being
  forgotten or overbuilt.
