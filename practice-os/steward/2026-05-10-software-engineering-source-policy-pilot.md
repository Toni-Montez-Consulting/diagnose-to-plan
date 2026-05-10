---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - Software Engineering Source Policy Pilot

Date: 2026-05-10

Status: accepted internal engineering pilot

## Trigger

After Software Architecture was promoted into the source pack, the next useful
role pilot was Software Engineering. Toni wants agents to keep moving when
implementation is approved, but not blur implementation with production,
runtime, schema, client, or cross-repo authority.

## Decision Captured

Software Engineering should be repo-grounded, implementation-forward, and
verification-led.

The role can edit code, docs, scripts, and tests when Toni has approved scope,
the owning repo is clear, local instructions have been read, and no gated
authority is being expanded. It must escalate when the work changes
architecture, runtime authority, schema/data boundaries, production operations,
cross-repo orchestration, or high-risk domains.

## Artifacts Added

- `docs/SOFTWARE_ENGINEERING_SOURCE_POLICY_PILOT_2026-05-10.md`
- `decisions/0019-software-engineering-source-pack.md`

## Artifacts Updated

- `practice-os/agents/software-engineering.md`
- `practice-os/research/source-packs/agent-source-packs.v0.json`
- `practice-os/research/source-packs/README.md`
- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`
- `practice-os/templates/activation-routing-map.md`
- `tests/test_agent_source_packs.py`

## What Worked

- The role now has a practical "when can I code?" rule.
- Architecture escalation is explicit before schema, runtime, cross-repo, or
  platform churn.
- Verification scales by blast radius instead of using one fixed test recipe.
- Official docs are used for current tool behavior, while repo evidence remains
  the source of implementation truth.

## Operating Rule Reinforced

Implementation authority is scoped, not global.

Green local tests and official docs can support implementation confidence, but
they do not authorize production writes, deploys, client communication,
runtime expansion, or public proof.

## Next Recommendation

Pilot QA / Audit next. That will turn engineering verification into a clearer
go/no-go standard and help separate automated proof, manual gates, and residual
risk before the squad expands further.

## Blocked Actions

This pilot does not approve:

- production writes or deploys;
- schema or migration changes;
- database, cloud, DNS, OAuth, billing, or secret mutation;
- payment, auth, entitlement, privacy, or legal/compliance changes;
- cross-repo orchestration;
- autonomous workflows;
- public proof or client communication.
