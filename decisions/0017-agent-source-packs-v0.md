# Decision 0017: Agent Source Packs V0

Date: 2026-05-10

Status: Accepted

## Context

The Agent Source Registry and Web Evidence Policy said a machine-readable
source-pack file should be created after real role workflows proved the fields.

Three role pilots now exist:

- Research Steward / Research Arm;
- External Communications;
- Consulting Strategy.

Those pilots proved the system needs a small encoded source pack before any
dashboard, steward, or future automation tries to infer source behavior from
prose.

## Decision

Add `practice-os/research/source-packs/agent-source-packs.v0.json` as the first
machine-readable source-pack file.

V0 includes only the three proven roles. It encodes:

- role id and name;
- source-pack version;
- pilot artifacts;
- primary sources;
- allowed web sources;
- search posture;
- blocked sources;
- default outputs;
- promotion requirements;
- next review trigger.

Add `practice-os/research/source-packs/README.md` and make the source-pack file
required by `dtp practice doctor`.

## Consequences

- Future agents and tools have a structured source-policy artifact.
- Source packs stay internal and do not add authority.
- The next source-pack iterations can add roles only after pilots prove their
  source behavior.
- The source-pack shape can feed a future dashboard without creating scheduled
  monitoring or autonomous action.

## Non-Goals

- No source-pack runtime.
- No autonomous agent behavior.
- No scheduled source monitor.
- No public copy.
- No client communication.
- No Notion sync.
- No new source-fetching behavior.

## Follow-Up

Use the next real role pilot to decide whether V0 needs a JSON schema, CLI
validator, dashboard status view, or source-pack freshness command.
