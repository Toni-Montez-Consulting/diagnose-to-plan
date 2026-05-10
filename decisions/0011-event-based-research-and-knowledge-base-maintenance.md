# 0011 - Event-Based Research And Knowledge Base Maintenance

Date: 2026-05-10

Status: accepted

## Context

Toni wants the Research Arm to start with a recurring source list, but the
larger need is broader than research. The practice needs help keeping knowledge
bases updated, refined, and expanded across memory management,
operationalization, project execution, agent roles, consulting strategy, and
client work.

The functions are not autonomous agents yet. Toni prefers event-based workflows
right now: when a useful signal arrives, route it, decide what it means, update
the right knowledge surface, and leave a reviewable record.

Toni also wants autonomous agents eventually and expects the squad system to
expand well beyond the first-wave role set. The near-term decision should
preserve that ambition while avoiding premature authority.

## Decision

Adopt an event-based, human-gated maintenance model for Research Arm and
knowledge-base updates.

The first V0 artifacts are:

- `docs/RESEARCH_ARM_SOURCE_LIST_V0.md`
- `docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md`
- `practice-os/templates/research-decision-record.md`
- `practice-os/templates/knowledge-base-event-record.md`

The Research Arm source list is recurring, but review is event-triggered by
default. Scheduled sweeps are optional and must be explicitly requested or tied
to a defined digest window.

Squads are used as review lenses, not autonomous authority.

This is a sequencing decision, not a permanent limitation. Event-based records
become the evidence trail for future roles, squads, scheduled reviews,
semi-autonomous functions, and eventually bounded autonomous agents.

## Consequences

- DTP remains the source of truth for research source lists, knowledge-base
  maintenance rules, templates, and steward receipts.
- Toni can forward, mention, or save a source without manually deciding every
  downstream documentation update.
- Future agents should route prompts such as "recurring source list",
  "event-based workflow", "update the knowledge base", "operationalize this",
  "memory management", and "project execution pattern" to this system.
- Public copy, client deliverables, tool installs, Notion sync, runtime
  behavior, and proof claims still require explicit gates.

## Non-Goals

- No autonomous research crawler.
- No always-on agent runtime.
- No Notion source-of-truth change.
- No automatic public copy or client communication.
- No automatic promotion of raw captures into playbook memory.
- No permanent cap on future agent roles, squads, or autonomous workflows.

## Validation

The decision is valid when:

- `dtp practice doctor` recognizes the new required docs/templates.
- Research Steward can still show active source/research items.
- The activation routing map points future prompts to these workflows.
- Documentation map surfaces the source list and event workflow clearly.
