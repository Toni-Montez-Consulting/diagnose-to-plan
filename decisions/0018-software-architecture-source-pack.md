# Decision 0018: Software Architecture Source Pack

Date: 2026-05-10

Status: Accepted

## Context

Decision 0017 created the first machine-readable source pack with the three
role pilots that had already proven their source behavior.

The next role pilot reviewed Software Architecture because it is the technical
decision layer that should guide larger implementation, runtime, schema,
automation, and cross-repo work without authorizing those changes by itself.

## Decision

Promote Software Architecture into
`practice-os/research/source-packs/agent-source-packs.v0.json`.

The role's source posture is:

- DTP and repo evidence first;
- official platform docs when current technical behavior matters;
- architecture frameworks as review lenses, not mandates;
- broad web search for source discovery only;
- explicit approval required for schema, runtime, cross-repo, cloud, or
  autonomous behavior.

## Consequences

- Future agents and dashboards can inspect Software Architecture source posture
  without parsing prose docs.
- Software Engineering, DevOps, Data Architecture, and QA pilots can treat this
  as the boundary and handoff source.
- Architecture recommendations remain review-first and do not grant mutation
  authority.

## Non-Goals

- No schema changes.
- No hosted DTP implementation.
- No runtime behavior.
- No cloud or database mutation.
- No autonomous workflow.
- No public/client architecture claims.

## Follow-Up

Use the next Software Engineering or DevOps pilot to test whether the
architecture source pack needs additional fields for implementation handoff,
verification evidence, or runtime authority classification.
