---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - DevOps / Infrastructure Source Policy Pilot

Date: 2026-05-10

Status: accepted internal DevOps / Infrastructure pilot

## Trigger

After QA / Audit was promoted into the source pack, the next useful role pilot
was DevOps / Infrastructure. Toni wants agents to use credible source evidence
for runtime and deployment thinking while keeping all live mutations approval
gated.

## Decision Captured

DevOps / Infrastructure should be runtime-evidence-led and mutation-gated.

The role can evaluate deployment configs, CI/CD, environment readiness,
observability, rollback, secrets posture, provider docs, cost/maintenance risk,
and operational handoff. It must separate local readiness, CI evidence, preview
behavior, production behavior, manual dashboard gates, and live mutation
authority.

## Artifacts Added

- `docs/DEVOPS_INFRASTRUCTURE_SOURCE_POLICY_PILOT_2026-05-10.md`
- `decisions/0021-devops-infrastructure-source-pack.md`

## Artifacts Updated

- `practice-os/agents/devops-infrastructure.md`
- `practice-os/research/source-packs/agent-source-packs.v0.json`
- `practice-os/research/source-packs/README.md`
- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`
- `practice-os/templates/activation-routing-map.md`
- `tests/test_agent_source_packs.py`

## What Worked

- DevOps now has a concrete distinction between local, CI, preview, and
  production proof.
- Rollback, observability, cost, quota, maintenance, and secret inventory are
  part of readiness.
- Official platform/cloud docs are used for current behavior, while repo
  evidence remains the first source of truth.
- Live infrastructure mutation remains blocked without explicit approval.

## Operating Rule Reinforced

Deployment readiness is not deployment authority.

DevOps can say what evidence exists, what is missing, what risk remains, and
what gate comes next. It cannot deploy, mutate infrastructure, update live
config, or approve production readiness by itself.

## Next Recommendation

Pause the role-pilot chain long enough to decide whether the source packs now
need structured schema validation, a dashboard/freshness view, or another role
pilot. If continuing role pilots, Product Strategy, UX / Design, Web
Experience, General Counsel, Compliance, Data Architecture, and Controller are
strong next candidates.

## Blocked Actions

This pilot does not approve:

- production deploys;
- cloud, hosting, DNS, OAuth, billing, database, CI/CD permission, webhook,
  integration, or secret mutation;
- schema, migration, backup, restore, retention, or data-access change;
- production readiness claims;
- public proof movement;
- client-facing release communication;
- legal, finance, compliance, privacy, security, medical, or regulated
  assurance;
- autonomous workflow promotion;
- cross-repo implementation order.
