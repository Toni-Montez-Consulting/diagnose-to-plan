# Decision 0016: Agent Source Registry And Web Evidence Policy

Date: 2026-05-10

Status: Accepted

## Context

Toni clarified that all current and future agent roles should be able to search
for information when it helps the work. He also wants credible external sources
for each domain and function, but without turning the current human-led system
into autonomous agents before the gates are ready.

DTP already has:

- Agent Squads + Knowledge Base V0;
- first-wave specialized roles;
- Research Arm source lists;
- source-freshness dry-run command;
- autonomy-readiness gates;
- knowledge-base event workflows.

The missing piece was a role-level source registry and a default policy for
using broad web evidence.

## Decision

Add `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md` as the master
source registry and evidence policy for agent roles, squads, research, memory,
communications, consulting strategy, engineering, design, operations, finance,
legal, compliance, and future specialized agents.

Accepted defaults:

- include the broader future roster now, with authority still gated;
- allow broad web search for all roles when it is useful;
- treat broad web results as low-confidence until corroborated by primary,
  official, standards, or directly observed sources;
- keep official and primary sources first for factual or high-stakes work;
- use `dtp research source-freshness` when source checks should create a
  reviewable queue item;
- create a machine-readable source-pack file later, after the policy is used in
  real workflows.

## Consequences

- Future agents can search, but source quality and promotion gates are explicit.
- The squad model remains human-led and approval-gated.
- Research findings can inform internal work without automatically changing
  public copy, client communication, legal posture, pricing, architecture, or
  runtime behavior.
- The future autonomous-agent path has a source policy it can encode later.

## Non-Goals

- No autonomous crawler.
- No scheduled monitor.
- No source-pack JSON yet.
- No new agent runtime.
- No public consulting copy change.
- No client communication.
- No Notion mirror or sync.
- No legal, tax, accounting, compliance, or financial advice workflow.

## Follow-Up

After the first role workflow uses the policy, create
`practice-os/research/source-packs/agent-source-packs.v0.json` or a similarly
scoped machine-readable source-pack file.
