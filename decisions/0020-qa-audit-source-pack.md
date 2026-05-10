# Decision 0020: QA / Audit Source Pack

Date: 2026-05-10

Status: Accepted

## Context

Software Engineering now defines repo-grounded implementation authority and
verification evidence. The next source-pack promotion needed to define how QA /
Audit evaluates that evidence without overstating what it proves.

## Decision

Promote QA / Audit into
`practice-os/research/source-packs/agent-source-packs.v0.json`.

The role's source posture is:

- acceptance criteria, active request, repo state, diff, tests, CI, logs,
  screenshots, route checks, and handoff receipts first;
- Software Engineering evidence to understand what was implemented and what
  was verified;
- official testing, browser, CI, security, accessibility, and platform docs
  when a claim depends on current tool or standard behavior;
- broad web search for source discovery and risk-category research only;
- human-gated promotion before QA findings become production, public, client,
  legal, finance, compliance, privacy, security, or runtime approval.

## Consequences

- Future agents can separate verified passes, confirmed failures, missing
  evidence, manual gates, residual risk, and queued follow-up.
- Engineering evidence can become clearer go/no-go language.
- QA can be direct without pretending it has authority to approve public proof,
  client communication, production releases, or regulated assurance.
- DevOps / Infrastructure can later consume QA evidence for deploy, runtime,
  rollback, and observability gates.

## Non-Goals

- No production release approval.
- No public proof movement.
- No client-facing claims or communication.
- No legal, finance, compliance, privacy, security, medical, or regulated
  assurance.
- No deployment, database, cloud, DNS, OAuth, billing, or secret mutation.
- No autonomous workflow promotion.
- No cross-repo implementation order.

## Follow-Up

Pilot DevOps / Infrastructure next so QA evidence can be connected to runtime
readiness, deploy gates, rollback proof, observability, environment inventory,
and cost/risk posture.
