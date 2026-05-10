---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - Research Source List And KB Event Workflow

Date: 2026-05-10

Status: accepted internal operating update

## Trigger

Toni approved defining a recurring source list and confirmed that event-based
workflows are the right default because the functions are not autonomous agents
yet.

He also clarified that knowledge bases need assistance across more than
research: memory management, operationalization, project execution, and other
facets of the practice/business.

## Decision Captured

- Use a recurring source list for Research Arm.
- Use simple research decision records when a source changes a practice
  decision.
- Use event-based knowledge-base maintenance as the broader pattern.
- Treat squads as review lenses, not autonomous authority.
- Preserve the future direction toward more squads, more specialized roles, and
  eventually autonomous agents after the required source, review, eval,
  permission, rollback, and privacy gates are proven.
- Keep DTP as source of truth.
- Keep Notion as mirror/cockpit only.
- Do not change public copy, client deliverables, runtime behavior, or tool
  access in this slice.

## Artifacts Added

- `decisions/0011-event-based-research-and-knowledge-base-maintenance.md`
- `docs/RESEARCH_ARM_SOURCE_LIST_V0.md`
- `docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md`
- `practice-os/templates/research-decision-record.md`
- `practice-os/templates/knowledge-base-event-record.md`

## Artifacts Updated

- `docs/RESEARCH_ARM_V0.md`
- `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `practice-os/templates/activation-routing-map.md`
- `src/dtp/commands/practice.py`
- `tests/test_practice.py`

## Boundaries

- No autonomous source monitoring.
- No scheduled sweep unless explicitly requested.
- No public-claim authority.
- No Notion live sync.
- No client communication.
- No repo implementation outside DTP.
- No permanent constraint against future autonomy.

## Next Use

When Toni forwards a source, mentions a research article, identifies a
collaboration pattern, asks to operationalize a workflow, or says a knowledge
base needs to be updated, future agents should:

1. classify the event;
2. choose the owning knowledge surface;
3. create a decision or event record when needed;
4. update the source-of-truth artifact;
5. leave a receipt and validation evidence.
