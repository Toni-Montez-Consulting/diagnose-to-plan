---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Workspace Dashboard Read-Only

Status: static dashboard plus local VS Code panel from the existing read-only
workspace report.

Owner: `diagnose-to-plan`

Purpose: define the dashboard view that can be generated from
`dtp workspace report --json` without creating a live cross-repo command runner.

This is a whole-workspace planning and roadmap cockpit. DTP owns the rendered
state because it already indexes consulting, Architected Strength, Omnexus,
DeMario, Hub, CCAAP, DSE, `tm-skills`, and other workspace lanes through
manifests, evidence indexes, Kaizen, proof queues, roadmap reports, and steward
receipts. The dashboard is not limited to DTP repo work.

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

## Viewable Dashboard Command

```powershell
.\.venv\Scripts\python.exe -m dtp workspace dashboard
```

Default output:

```text
docs/workspace-dashboard.html
```

This generates a static browser-viewable dashboard from:

- `dtp workspace report`
- `practice-os/kaizen/intake.jsonl`
- `docs/PRACTICE_PROOF_QUEUE_INDEX.md`

It is intentionally static and read-only. It makes the active queue, repo
coverage, proof candidates, and blockers visible without running sibling repo
commands, reading dashboards, calling APIs, or creating another source of truth.

For the VS Code panel surface:

```powershell
.\.venv\Scripts\python.exe -m dtp workspace dashboard --surface vscode --out outputs/workspace-dashboard.html
```

`outputs/workspace-dashboard.html` is ignored local cache. It is the preferred
panel cache because it lets the extension refresh the view without committing
generated dashboard churn.

## VS Code Panel

The local extension lives at `tools/vscode-dtp-dashboard`.

Commands:

- `DTP: Open Workspace Dashboard`
- `DTP: Refresh Workspace Dashboard`
- `DTP: Open Dashboard Source Docs`

Install locally:

```powershell
cd C:\Users\tonimontez\Projects\diagnose-to-plan\tools\vscode-dtp-dashboard
npm install
npm run package:vsix
code --install-extension dist/dtp-workspace-dashboard.vsix --force
```

On Toni's Windows machine, if the `code` shim does not accept
`--install-extension`, use the VS Code command shim directly:

```powershell
& "$env:LOCALAPPDATA\Programs\Microsoft VS Code\bin\code.cmd" --install-extension dist\dtp-workspace-dashboard.vsix --force
```

The extension does not own roadmap state. It only finds the `diagnose-to-plan`
workspace folder, opens a VS Code webview panel, and manually runs the
read-only DTP dashboard command when Toni invokes refresh.

## Existing Extension Decision

Existing VS Code options are useful but not sufficient as the primary cockpit:

- Built-in Markdown preview is the lowest-friction fallback, but it would
  require a less capable generated Markdown view and separate task/keybinding
  glue for refresh.
- HTML/Simple Browser preview extensions can show a static file, but they do
  not know DTP root resolution, DTP refresh commands, or the workspace boundary.
- Markdown Kanban extensions are good for Markdown-owned boards, but this
  workspace already has DTP-owned cross-repo roadmap state. Moving the source
  of truth into a generic Kanban syntax would create drift.

Decision: use a tiny local extension only as a VS Code viewer and manual refresh
button. Keep DTP as the source of truth.

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
- It can be opened directly from `docs/workspace-dashboard.html`.
- It can be opened inside VS Code through the local panel without a server,
  background watcher, deployment, or third-party dashboard source of truth.

