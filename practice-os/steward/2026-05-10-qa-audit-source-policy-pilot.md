---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - QA / Audit Source Policy Pilot

Date: 2026-05-10

Status: accepted internal QA / Audit pilot

## Trigger

After Software Engineering was promoted into the source pack, the next useful
role pilot was QA / Audit. Toni wants agents to keep moving, but not call work
done just because a narrow check passed or a plan feels complete.

## Decision Captured

QA / Audit should be evidence-led and claim-scoped.

The role can evaluate implementation evidence, acceptance criteria, automated
checks, CI, screenshots, route checks, logs, and handoff receipts. It must say
what passed, what failed, what remains unproven, what is a manual gate, what is
acceptable residual risk, and what still needs Toni approval.

## Artifacts Added

- `docs/QA_AUDIT_SOURCE_POLICY_PILOT_2026-05-10.md`
- `decisions/0020-qa-audit-source-pack.md`

## Artifacts Updated

- `practice-os/agents/qa-audit.md`
- `practice-os/research/source-packs/agent-source-packs.v0.json`
- `practice-os/research/source-packs/README.md`
- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`
- `practice-os/templates/activation-routing-map.md`
- `tests/test_agent_source_packs.py`

## What Worked

- QA now has a concrete standard for matching evidence to claims.
- Manual gates remain visible instead of getting buried under green checks.
- The role can produce a useful go/no-go read without approving production,
  public, client, legal, compliance, privacy, security, or runtime actions.
- Process misses can route into Agentic Performance Gap Review instead of
  disappearing into chat.

## Operating Rule Reinforced

Evidence must match the claim.

A build, test, CI run, screenshot, route check, or secret scan supports only the
surface it actually exercised. QA can state the evidence and risk plainly, but
it cannot convert incomplete evidence into approval.

## Next Recommendation

Pilot DevOps / Infrastructure next. That will connect QA evidence to deploy
readiness, runtime proof, rollback posture, environment inventory,
observability, and cost/risk review.

## Blocked Actions

This pilot does not approve:

- production release approval;
- public proof movement;
- client-facing claims or communication;
- legal, finance, compliance, privacy, security, medical, or regulated
  assurance;
- deployment, database, cloud, DNS, OAuth, billing, or secret mutation;
- autonomous workflow promotion;
- cross-repo implementation order.
