---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Workspace Dashboard Read-Only

Status: static dashboard spec from the existing read-only workspace report.

Owner: `diagnose-to-plan`

Purpose: define the dashboard view that can be generated from
`dtp workspace report --json` without creating a live cross-repo command runner.

## Boundary

Allowed:

- read DTP-owned repo manifests and evidence indexes;
- read DTP roadmap/backlog docs;
- render a static HTML, Markdown, JSON, or Notion-safe summary;
- show recorded evidence, blockers, gates, proof posture, and next actions.

Not allowed:

- run repo-local commands;
- call GitHub, Vercel, Supabase, Notion, or live CI APIs;
- mutate files;
- publish proof;
- read secrets, private rows, raw logs, or private client material;
- infer live git status beyond what the current report records.

## Refresh Command

```powershell
.\.venv\Scripts\python.exe -m dtp workspace report --json
```

The dashboard may be regenerated from this JSON. If live repo, PR, CI, or cloud
state is needed, create a separate boundary decision first.

## Current Static View

| Repo | Lane | Dashboard status | Next action | Blocker or gate |
|---|---|---|---|---|
| `diagnose-to-plan` | Practice OS source of truth | source docs, templates, Kaizen, workspace report, proof queue active | keep roadmap/proof queue current | no private raw engagement material in public repo |
| `consulting` | public storefront and proof surface | share-ready path plus assistant QA and qualification pass | build, route smoke, doctor, matrix, manual visual QA | Hub endpoint proof and proof-gated assets |
| `hub` | runtime/intake support | manifests and evidence exist; PR #68 visible blocker | use docs-only Tailwind 4 plan before code | runtime validation and PR-local checks |
| `ccaap-site` | client launch/proof candidate | waiting owner inputs | collect PayPal/contact/DNS/assets/review/proof decision | permission, redaction, owner approval |
| `fitness-app` / Omnexus | mobile launch proof candidate | strong internal evidence | review proof candidates privately | privacy, billing, app/user-data caveats |
| `demario-pickleball-1` | command-room proof candidate | owner-safe launch/admin reference | proof only after owner permission and redaction | private admin/booking/payment data |
| `architected-strength` | separate personal-brand OS | later assistant-pattern candidate | wait for consulting assistant pilot | source/refusal/logging gates |
| `dse-content` | sensitive readiness incubator | COI-gated | do not touch without explicit scope | COI, permission, redaction, live validation |
| `tm-skills` | reusable SDLC skills | global install and Codex discovery proven | keep external smoke manual | Claude/Copilot reload remains non-blocking |

## First Dashboard Acceptance

- The dashboard makes the current lane, next action, and gate visible without
  running live commands.
- It does not replace repo-local verification.
- It points proof candidates back to `docs/PRACTICE_PROOF_QUEUE_INDEX.md`.
- It points offer copy decisions back to `docs/OFFER_TO_PROOF_MATRIX.md`.

