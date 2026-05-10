# 0012 - Autonomy Readiness Ladder

Date: 2026-05-10

Status: accepted

## Context

Toni clarified that V0 human-gated workflows are not the final ambition. The
practice should eventually include more squads, more specialized agents, and
autonomous agents where autonomy is valuable and safe.

The current system has the right foundations: DTP source-of-truth docs, agent
squad role specs, event-based knowledge-base workflows, research/memory
stewards, practice dashboards, and FAOS as a future orchestration substrate.
What was missing was a clear readiness ladder that explains how a workflow
moves from manual to read-only to draft-only to supervised execution to bounded
autonomy.

## Decision

Adopt `docs/AUTONOMY_READINESS_LADDER_V0.md` as the DTP source of truth for
autonomy sequencing.

Require `practice-os/templates/autonomy-readiness-review.md` before moving any
workflow into a higher autonomy level, especially scheduled, write-enabled, or
live-action behavior.

The first likely autonomy candidates are:

- Research source freshness;
- Memory review queue;
- Practice/status dashboards;
- Knowledge-base drift review;
- External communications drafts;
- Repo-local validation sweeps;
- Notion mirror draft updates.

## Consequences

- "No autonomous agents yet" now means "not before readiness," not "never."
- Future squads and roles can be added when repeated workflow evidence proves
  the need.
- FAOS has a clearer bridge from roadmap idea to implementation gate.
- Risky actions stay human-approved until source scope, permissions, evals,
  audit logs, rollback, override, and privacy boundaries are accepted.

## Non-Goals

- No autonomous runtime implementation in this decision.
- No new hosted DTP, FAOS repo, MCP server, connector, or scheduled job.
- No Notion live sync.
- No public/client action.
- No write-enabled automation.

## Validation

This decision is valid when:

- Practice doctor recognizes the autonomy readiness doc and template.
- Activation routing sends autonomy prompts to the ladder.
- Agent Squads and FAOS docs point to the ladder.
- The DTP test suite still passes.

