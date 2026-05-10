---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - Software Architecture Source Policy Pilot

Date: 2026-05-10

Status: accepted internal architecture pilot

## Trigger

After the first agent source-pack file was merged, the next useful role pilot
was Software Architecture. Toni wants the broader squad to use credible sources
and eventually support more autonomous work, but the technical decision layer
needs clear gates before code, runtime, or schema changes expand.

## Decision Captured

Software Architecture should be boundary-first and implementation-ready.

The role may use official platform docs and architecture frameworks, but it
must start with DTP, repo state, local contracts, and Toni's latest direction.
External sources can inform architecture. They cannot authorize runtime,
schema, cross-repo, cloud, or autonomous behavior.

## Artifacts Added

- `docs/SOFTWARE_ARCHITECTURE_SOURCE_POLICY_PILOT_2026-05-10.md`
- `decisions/0018-software-architecture-source-pack.md`

## Artifacts Updated

- `practice-os/agents/software-architecture.md`
- `practice-os/research/source-packs/agent-source-packs.v0.json`
- `practice-os/research/source-packs/README.md`
- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`
- `practice-os/templates/activation-routing-map.md`
- `tests/test_agent_source_packs.py`

## What Worked

- The role became concrete enough for a source-pack entry without adding
  runtime authority.
- Official cloud/platform sources were positioned as review lenses and
  current-fact sources, not mandates.
- The source-of-truth, runtime-authority, and approval boundaries stayed clear.
- The output standard now produces architecture that can hand off to
  engineering, DevOps, data, QA, product, or consulting strategy without
  pretending those roles are the same job.

## Operating Rule Reinforced

Architecture can recommend the shape of a system, but implementation authority
still belongs to the explicit repo/workflow approval path.

## Next Recommendation

Pilot Software Engineering next, using this architecture source posture as the
handoff boundary. That should clarify how implementation agents consume an
architecture packet, when they can code directly, and when they must escalate
back to architecture, DevOps, data, or QA.

## Blocked Actions

This pilot does not approve:

- schema or migration changes;
- runtime behavior;
- hosted DTP implementation;
- Hub runtime expansion;
- cross-repo orchestration;
- autonomous agents;
- cloud, DNS, deploy, billing, or database mutation;
- public or client-facing architecture claims.
