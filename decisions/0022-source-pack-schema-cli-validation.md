# Decision 0022: Source Pack Schema CLI Validation

Date: 2026-05-10

Status: Accepted

## Context

The source-pack file now covers seven pilot-proven roles. That makes it useful
enough to be a durable operating contract, but also large enough that silent
shape drift would be easy: missing evidence limits, duplicate role ids,
authority-boundary changes, or incomplete role packs could undermine future
stewards.

## Decision

Add dependency-free local validation for
`practice-os/research/source-packs/agent-source-packs.v0.json`.

The validation is exposed through:

```powershell
.\.venv\Scripts\dtp.exe practice source-packs validate
```

`dtp practice doctor` also runs the same validation so source-pack contract
drift becomes visible during normal Practice OS checks.

The schema contract is documented in `docs/AGENT_SOURCE_PACK_SCHEMA_V0.md`.

## Consequences

- Future source-pack edits have a concrete contract before more roles are
  added.
- Future dashboards and stewards can consume the validator result instead of
  inventing a parallel schema.
- The source pack remains an internal evidence and routing surface, not a
  source of authority.
- Web search can stay broadly available to roles while promotion gates remain
  explicit.

## Non-Goals

- No public copy changes.
- No client communication.
- No Notion sync.
- No scheduled research/source workflow.
- No autonomous agent behavior.
- No live web freshness scoring.
- No production, repo, cloud, billing, legal, finance, or compliance action.

## Follow-Up

Next choose one:

- build a lightweight source-pack freshness/status dashboard; or
- continue role pilots for Product Strategy, UX / Design, Web Experience,
  General Counsel, Compliance, Data Architecture, or Controller.
