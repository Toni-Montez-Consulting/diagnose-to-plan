---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - Agent Source Registry And Web Evidence Policy

Date: 2026-05-10

Status: accepted internal policy

## Trigger

Toni clarified that all agent roles and future squads should be able to search
for information, because each domain has credible external sources. He also
confirmed:

- include the broader agent roster now;
- create a master policy now and machine-readable source packs later;
- allow broad web search, but treat it as lower-confidence unless corroborated
  by primary or stronger evidence.

## Decision Captured

Add a DTP-owned Agent Source Registry and Web Evidence Policy.

The policy keeps the ambition:

- every role may use web search when useful;
- credible external sources should strengthen each domain;
- future autonomous agents should have source packs.

The policy keeps the gates:

- broad search does not authorize action;
- official and primary sources come first for factual work;
- high-risk legal, finance, compliance, security, privacy, public proof, client
  communication, repo, and runtime changes still require human review.

## Artifacts Added

- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
- `decisions/0016-agent-source-registry-web-evidence-policy.md`

## Artifacts Updated

- `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md`
- `docs/RESEARCH_ARM_SOURCE_LIST_V0.md`
- `docs/RESEARCH_SOURCE_FRESHNESS_DRY_RUN_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `practice-os/templates/activation-routing-map.md`
- `src/dtp/commands/practice.py`
- `tests/test_practice.py`

## Operating Boundary

This work does not create:

- autonomous agents;
- scheduled web monitors;
- a source-pack runtime;
- public consulting copy;
- client communication;
- Notion sync;
- legal, tax, accounting, compliance, or financial advice.

## Next Use

Run the next real Research Steward or agent-role workflow through the policy.
If the registry helps, create the first machine-readable source-pack file and
add role-specific examples to the role specs.
