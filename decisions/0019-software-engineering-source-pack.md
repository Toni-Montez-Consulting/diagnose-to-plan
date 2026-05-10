# Decision 0019: Software Engineering Source Pack

Date: 2026-05-10

Status: Accepted

## Context

Software Architecture is now the boundary and runtime-authority decision layer.
The next source-pack promotion needed to define how implementation agents use
that architecture boundary while still moving quickly on approved repo-local
work.

## Decision

Promote Software Engineering into
`practice-os/research/source-packs/agent-source-packs.v0.json`.

The role's source posture is:

- user request, repo state, local instructions, tests, scripts, and nearby
  implementation patterns first;
- Software Architecture handoff when implementation changes boundaries,
  schemas, runtime, autonomy, or cross-repo contracts;
- official tool, package-manager, CI, framework, and library docs for current
  behavior;
- changelogs and security advisories when dependency or vulnerability behavior
  matters;
- broad web search for source discovery only.

## Consequences

- Future implementation agents can inspect when coding is allowed and when to
  escalate.
- Engineering verification can be consumed by QA / Audit and DevOps pilots.
- Repo-local implementation remains possible without converting every task into
  architecture review.
- Production, client, runtime, data, auth, payment, legal, and cross-repo gates
  remain explicit.

## Non-Goals

- No production writes.
- No deploys.
- No schema or migration changes.
- No runtime behavior.
- No cloud, database, DNS, billing, OAuth, or secret mutation.
- No public proof or client communication.
- No autonomous workflow.

## Follow-Up

Pilot QA / Audit next so implementation evidence can become a clearer go/no-go
standard with automated proof, manual gates, and residual risk separated.
