---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - Agent Source Policy First Pilot

Date: 2026-05-10

Status: accepted first pilot

## Trigger

After merging the Agent Source Registry and Web Evidence Policy, Toni approved
rolling into the next useful step. The chosen pilot used:

- one AI/platform source;
- one consulting/business source.

## Sources Piloted

| Source | Type | Purpose | Outcome |
|---|---|---|---|
| OpenAI Agents SDK docs | Tier 1 official AI/platform docs | test whether a technical agent source can inform DTP's agent authority, guardrail, tracing, and eval posture | accepted watch decision record |
| Microsoft 2026 Work Trend Index | Tier 3 primary business research / report | test whether business research can become a reusable consulting pattern without becoming public proof | draft research pattern candidate |

## What Worked

- The source registry gave each source a clear role: one technical/control
  source and one business/change-management source.
- The source-freshness command produced reviewable ignored evidence before any
  tracked artifact was created.
- The promotion path worked: source freshness item -> decision record or
  pattern candidate.
- The evidence limits stayed explicit.

## What The Pilot Caught

Running two source-freshness checks in parallel surfaced a duplicate run-id
risk in the local dry-run command. The command now reserves run ids with marker
files under ignored output state before writing queue items.

## Artifacts Added

- `practice-os/research/source-freshness/reviews/2026-05-10-openai-agents-sdk-source-policy-pilot.md`
- `practice-os/research/source-freshness/reviews/2026-05-10-microsoft-work-trend-index-source-policy-pilot.md`
- `practice-os/research/decisions/2026-05-10-openai-agents-sdk-source-policy-watch.md`
- `practice-os/research/pattern-candidates/2026-05-10-ai-implementation-is-operating-model-redesign.md`

## Artifacts Updated

- `src/dtp/commands/research_source_freshness.py`
- `tests/test_research.py`
- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
- `docs/RESEARCH_SOURCE_FRESHNESS_DRY_RUN_V0.md`
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`
- `docs/DOCUMENTATION_MAP.md`

## Next Recommendation

Do one more role-pilot before building the machine-readable source-pack file.
Best next choices:

- External Communications Agent, because it will test how source evidence
  becomes professional, client-safe language.
- Consulting Strategy Agent, because it will test how research becomes offer
  and buyer-fit reasoning without overclaiming.

## Blocked Actions

This pilot does not approve:

- public consulting copy changes;
- client communication;
- OpenAI Agents SDK adoption;
- Microsoft-sourced public claims;
- scheduled source monitoring;
- source-pack runtime behavior;
- autonomous agents.
