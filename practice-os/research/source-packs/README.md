---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Agent Source Packs

This folder stores machine-readable source packs for DTP agent roles.

The source packs encode `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
for tools, dashboards, stewards, and future automation. They do not add new
authority.

## Current Pack

```text
practice-os/research/source-packs/agent-source-packs.v0.json
```

V0 includes only the three roles proven by source-policy pilots:

- Research Steward / Research Arm;
- External Communications;
- Consulting Strategy.

## Rules

- DTP remains the source of truth.
- Source packs are internal-only until a separate public-copy gate approves
  derived language.
- Web search may inform a role, but it does not authorize action.
- Broad web evidence stays low-confidence until corroborated.
- Public copy, client communication, pricing, legal/finance/compliance claims,
  proof movement, repo changes, runtime behavior, and autonomous authority all
  require the matching promotion and approval gate.

## Update Path

Update this folder when:

- a role pilot proves a new source posture;
- a role's primary sources change;
- a new source tier or blocked action becomes necessary;
- the source pack schema changes;
- a future dashboard or steward needs additional machine-readable fields.

When updating, also check:

- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`;
- `docs/DOCUMENTATION_MAP.md`;
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`;
- `practice-os/templates/activation-routing-map.md` if prompt routing changes;
- the related steward receipt.
