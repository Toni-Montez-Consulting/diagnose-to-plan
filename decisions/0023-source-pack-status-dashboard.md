# Decision 0023: Source Pack Status Dashboard

Date: 2026-05-10

Status: Accepted

## Context

The source-pack validator made contract drift visible, but Toni also needs a
fast operating view: which roles exist, how recently they were reviewed, how
many sources they depend on, and which promotion gates stay active.

The first dashboard should be practical and expandable. It should not become a
new source of authority or a hidden automation layer.

## Decision

Add read-only source-pack status and dashboard commands:

```powershell
.\.venv\Scripts\dtp.exe practice source-packs status
.\.venv\Scripts\dtp.exe practice source-packs dashboard
```

`status` prints role freshness, source counts, source posture, and promotion
gate counts. `dashboard` writes:

```text
docs/source-pack-status-dashboard.html
```

The dashboard consumes the same validator/status model as the CLI so future
freshness work can grow without creating a second contract.

## Consequences

- Future agents can inspect the source-pack system before adding roles.
- Toni gets a quick internal dashboard for the squad/source layer.
- Stale role reviews can become visible without needing autonomous monitoring.
- The same status model can later absorb reviewed source-freshness evidence.

## Non-Goals

- No live web freshness scoring.
- No scheduled source monitor.
- No Notion sync.
- No source promotion.
- No public copy changes.
- No client communication.
- No autonomous role behavior.
- No repo, production, cloud, billing, legal, finance, or compliance action.

## Follow-Up

Next choose one:

- connect reviewed source-freshness records to source-pack dashboard warnings;
  or
- continue role pilots for Product Strategy, UX / Design, Web Experience,
  General Counsel, Compliance, Data Architecture, or Controller.
