---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - Autonomy Readiness Ladder

Date: 2026-05-10

Status: accepted internal operating update

## Trigger

After event-based Research Arm and knowledge-base workflows were merged, Toni
clarified that he still wants autonomous agents eventually and wants more
specialized agents across multiple squads over time.

## Decision Captured

- Human-gated V0 is the foundation, not the ceiling.
- More squads and more specialized roles remain part of the long-term vision.
- Autonomy should be staged through explicit readiness levels.
- Research, memory, status, and knowledge-base freshness are the safest first
  autonomy candidates.
- Write-enabled or live-action autonomy must wait for source scope,
  permissions, evals, audit logs, rollback, approval gates, and privacy
  boundaries.

## Artifacts Added

- `docs/AUTONOMY_READINESS_LADDER_V0.md`
- `practice-os/templates/autonomy-readiness-review.md`
- `decisions/0012-autonomy-readiness-ladder.md`

## Artifacts Updated

- `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md`
- `docs/FAOS_ORCHESTRATION_ROADMAP.md`
- `docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md`
- `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md`
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`
- `docs/DOCUMENTATION_MAP.md`
- `practice-os/templates/activation-routing-map.md`
- `src/dtp/commands/practice.py`
- `tests/test_practice.py`

## Boundaries

- No autonomous runtime was added.
- No hosted DTP/FAOS implementation was started.
- No Notion sync, client communication, public proof, tool install, deploy, or
  live write behavior changed.

## Next Use

When Toni asks for autonomous agents, scheduled stewards, an agent manager,
more squads, a new specialized agent role, automated research, automated memory
maintenance, or write-enabled workflows, future agents should classify the
workflow against the autonomy ladder before implementing.
