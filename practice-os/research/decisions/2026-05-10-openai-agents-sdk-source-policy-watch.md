---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Research Decision Record - OpenAI Agents SDK As Agent Source-Policy Input

Date: 2026-05-10

Reviewer: Toni / Research Steward

Decision: Watch

Confidence: medium

## Source Signal

- Source: OpenAI Agents SDK docs
- Source type: official AI/platform documentation
- Link or local path:
  - https://platform.openai.com/docs/guides/agents-sdk
  - https://openai.github.io/openai-agents-python/tracing/
  - https://openai.github.io/openai-agents-python/guardrails/
- Date reviewed: 2026-05-10

## What Changed

The first source-policy pilot used the OpenAI Agents SDK docs to test whether a
role-specific source registry can turn external technical sources into useful
internal operating guidance.

The docs are useful as source material for agent architecture posture because
they expose the concepts DTP should keep visible before agent authority grows:
tools, orchestration, guardrails, human review, tracing, and eval loops.

## Why It Matters

DTP's current agent system is intentionally human-led. This source strengthens
that direction rather than replacing it. The useful lesson is not "install this
SDK now." The useful lesson is that credible AI/platform sources should be
used to check whether DTP's own agent model has the right operating controls.

## Decision Rationale

Watch the SDK as an official source for agent architecture, guardrail, tracing,
and eval posture.

Do not adopt the SDK yet. DTP does not currently need a new agent runtime, and
the next useful step is still source-pack design and reviewed pilots.

## Evidence Limit

This source does not prove:

- that DTP should use the SDK;
- that autonomous agents are ready;
- that source packs should become runtime configuration immediately;
- that any client-facing claim is safe.

## Public Claim Status

- Public-safe now: no
- Requires source-specific review: yes
- Requires client/proof permission: not applicable
- Requires legal/privacy/security review: yes, if used in public trust or
  compliance language

## Destination

- Owning repo or lane: `diagnose-to-plan`
- Artifact to update: future source-pack file and autonomy-readiness reviews
- Squad lenses applied: Research Steward, Software Architecture, QA / Audit,
  Compliance / AI Governance

## Next Action

Use this as one input when creating the first machine-readable agent
source-pack file. Include fields for guardrails, traces, evals, review gates,
and blocked actions.

## Review Trigger

Revisit when DTP scopes an agent runtime, source-pack JSON, scheduled
stewards, or a client-safe explanation of agent architecture.

## Approval Gate

Toni must approve before this changes tooling, runtime behavior, public copy,
client deliverables, or autonomy level.
