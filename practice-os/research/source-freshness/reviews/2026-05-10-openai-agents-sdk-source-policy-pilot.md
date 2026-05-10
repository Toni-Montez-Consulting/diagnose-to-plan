---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Research Source Freshness Item - OpenAI Agents SDK Source Policy Pilot

Run id: rsf-2026-05-10-002

Source id: openai-agents-sdk-docs

Source name: OpenAI Agents SDK docs

Source tier: 1

Source URL or path: https://developers.openai.com/api/docs/guides/agents

Reviewed at: 2026-05-10

Review owner: Research Steward

Freshness state: changed_meaningful

Recommended action: create_research_decision_record

Human review state: accepted_record

## Change Summary

The first Agent Source Registry pilot reviewed current OpenAI Agents SDK source
material as an AI/platform evidence source. The reviewed source packet pointed
to official OpenAI guidance around agent orchestration, tool use, guardrails,
human review posture, tracing, and evaluation-oriented improvement loops.

## Why It Matters

This supports DTP's current stance that future agent workflows need visible
source scope, traceability, guardrails, human review, and evaluation evidence
before authority expands.

It also helps the future source-pack design: AI/platform agent sources should
not only track model capability. They should track operational controls:
guardrails, traces, approvals, evals, escalation, and auditability.

## Evidence Limit

This source does not prove DTP should adopt the OpenAI Agents SDK, build a new
runtime, or move any workflow above human-led review. It is official
AI/platform source evidence for design posture only.

The source-freshness command captured the evidence packet under ignored local
output first. The command was run in parallel with another source check and
surfaced a duplicate run-id risk, which was fixed in the same pilot pass.

## Allowed Next Artifact

- research decision record
- source-pack field candidate
- autonomy-readiness review input

## Blocked Actions

- public claims
- client communications
- tool install
- agent runtime adoption
- autonomous workflow promotion
- repo implementation outside a separately approved story

## Source Boundary

- Private/client-sensitive data involved: no
- Redaction needed: no
- Public claim allowed: no
- Client communication allowed: no
- Tool/connector action allowed: no
- Repo implementation allowed: no

## Next Review Trigger

Reopen when DTP scopes a real agent runtime, source-pack JSON, autonomy
readiness review, or client-facing explanation about agent architecture.
