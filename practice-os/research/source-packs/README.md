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

V0 includes the roles proven by source-policy pilots:

- Research Steward / Research Arm;
- External Communications;
- Consulting Strategy;
- Software Architecture;
- Software Engineering;
- QA / Audit;
- DevOps / Infrastructure.

## Validation

Source packs are validated by the local DTP CLI:

```powershell
.\.venv\Scripts\dtp.exe practice source-packs validate
```

`dtp practice doctor` also runs the source-pack validator. The validation
contract is documented in `docs/AGENT_SOURCE_PACK_SCHEMA_V0.md`.

## Status Dashboard

Source-pack freshness and role coverage can be reviewed locally:

```powershell
.\.venv\Scripts\dtp.exe practice source-packs status
.\.venv\Scripts\dtp.exe practice source-packs dashboard
```

The dashboard command writes `docs/source-pack-status-dashboard.html`. It is a
read-only status surface for role freshness, source counts, promotion gates, and
validation problems. It does not promote sources or authorize actions.

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
- `docs/AGENT_SOURCE_PACK_SCHEMA_V0.md`;
- `dtp practice source-packs validate`;
- `dtp practice source-packs status`;
- `dtp practice source-packs dashboard`;
- `docs/DOCUMENTATION_MAP.md`;
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`;
- `practice-os/templates/activation-routing-map.md` if prompt routing changes;
- the related steward receipt.
