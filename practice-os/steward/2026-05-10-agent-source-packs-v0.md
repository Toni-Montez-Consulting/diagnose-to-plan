---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - Agent Source Packs V0

Date: 2026-05-10

Status: accepted machine-readable source pack

## Trigger

After three source-policy pilots, Toni approved continuing forward. The next
natural step was a small machine-readable source-pack file based on real role
behavior rather than guessed future automation.

## Decision Captured

Create the first source-pack file:

```text
practice-os/research/source-packs/agent-source-packs.v0.json
```

Include only the three proven roles:

- Research Steward / Research Arm;
- External Communications;
- Consulting Strategy.

## Artifacts Added

- `practice-os/research/source-packs/README.md`
- `practice-os/research/source-packs/agent-source-packs.v0.json`
- `decisions/0017-agent-source-packs-v0.md`
- `tests/test_agent_source_packs.py`

## Artifacts Updated

- `src/dtp/commands/practice.py`
- `tests/test_practice.py`
- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`

## What This Enables

- Future agents can inspect source posture without parsing long prose docs.
- A later dashboard can show which roles have source packs and which roles are
  still prose-only.
- Future automation can use the pack as configuration only after autonomy
  gates are accepted.

## Boundary

The source pack does not approve:

- web crawling;
- scheduled source monitoring;
- autonomous role behavior;
- public copy;
- client communication;
- source-pack runtime;
- Notion sync;
- legal, finance, compliance, or proof claims.

## Next Recommendation

Use the next real role pilot to decide whether V0 needs:

- JSON schema;
- CLI validation command;
- source-pack dashboard;
- source-pack freshness check;
- additional role packs.
