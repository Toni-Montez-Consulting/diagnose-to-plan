---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Workspace Dashboard Read-Only

Status: static daily cockpit plus local VS Code panel from DTP-owned read-only
sources and the reviewed workspace task ledger.

Owner: `diagnose-to-plan`

Purpose: define the dashboard view that can be generated from DTP-owned source
artifacts without creating a live cross-repo command runner.

This is a whole-workspace planning and roadmap cockpit. DTP owns the rendered
state because it already indexes consulting, Architected Strength, Omnexus,
DeMario, Hub, CCAAP, DSE, `tm-skills`, and other workspace lanes through the
workspace task ledger, manifests, evidence indexes, Kaizen, proof queues,
roadmap reports, steward receipts, and reviewed recovery candidates. The
dashboard is not limited to DTP repo work. It shows today's attention queue,
closed work, proof candidates, repo coverage, sweep coverage, and open gates
without blending terminal archive rows into active execution lanes.

## Boundary

Allowed:

- read DTP-owned repo manifests and evidence indexes;
- read DTP roadmap/backlog docs;
- render a static HTML, Markdown, JSON, or Notion-safe summary;
- show recorded evidence, blockers, gates, proof posture, next actions, closed
  archive counts, and sweep coverage.
- run deterministic dry-run recovery into ignored `outputs/` review artifacts;
- export sanitized Notion cockpit rows as a mirror, not authority.

Not allowed:

- run repo-local commands;
- call GitHub, Vercel, Supabase, Notion, or live CI APIs;
- mutate tracked files during dashboard refresh or recovery dry-run;
- publish proof;
- read secrets, private rows, raw logs, or private client material;
- infer live git status beyond what the current report records.

## Refresh Command

```powershell
.\.venv\Scripts\python.exe -m dtp workspace report --json
```

The dashboard may be regenerated from this JSON plus the task ledger and
structured DTP docs. If live repo, PR, CI, or cloud state is needed, create a
separate boundary decision first.

## Viewable Dashboard Command

```powershell
.\.venv\Scripts\python.exe -m dtp workspace dashboard
```

Default output:

```text
docs/workspace-dashboard.html
```

This generates a static browser-viewable dashboard from:

- `practice-os/workspace/task-ledger.jsonl`
- `dtp workspace report`
- `practice-os/kaizen/intake.jsonl`
- `docs/ROADMAP_EXECUTION_BACKLOG.md`
- `docs/PRACTICE_PROOF_QUEUE_INDEX.md`
- `docs/WORKSPACE_DOCS_AND_CHAT_SWEEP_LEDGER_2026-05-05.md`
- repo-local boards listed in `.dtp/workspace.yaml`, when present

It is intentionally static and read-only. It makes the active queue, Item
Register, Recovery Inbox, repo coverage, closed archive, proof candidates,
sweep coverage, data-health warnings, and blockers visible without running
sibling repo commands, reading dashboards, calling APIs, or creating another
source of truth.

The first screen is the daily cockpit:

- `Needs Attention`
- `Waiting On Toni/Owner`
- `Blocked`
- `Decision Needed`
- `Proof Blocked`
- `Recently Closed`

The top Accounting Summary separates the counts that are easy to confuse:
reviewed dashboard rows, unreviewed Recovery Inbox rows, total detected rows,
and reviewed closed rows. `Total detected` is reviewed rows plus Recovery Inbox
candidates; it is not a count of completed work.

Longer material lives behind static tabs: `Today`, `Workstreams`, `Proof`,
`Register`, `Recovery Inbox`, `Repos`, `Archive`, and `Coverage`. Local
JavaScript only handles tab switching, count-focused filtering, copy affordances,
and search/filtering inside the generated file. If JavaScript is blocked, all
panels remain visible so the anchor links still land on useful content.

The Item Register is the count-proof surface. Metric cards route to Register
filters so `Needs Attention`, `Proof Blocked`, and `Recently Closed` show
numbered rows and a visible `Showing X of Y` status. The Archive still keeps
terminal lanes, but the Register is the fastest way to verify all rows. Register
rows keep source, evidence, blocker, and closure metadata inside expandable row
details so the table stays traversable.

The Recovery Inbox accounts for dry-run candidates that are not yet reviewed
operating rows. For example, a dry run may detect 259 candidates while the
reviewed dashboard has 183 rows and the closed archive has 110 rows. The
difference belongs in Recovery Inbox until a human reviews and imports the
candidate into `practice-os/workspace/task-ledger.jsonl`. Recovery candidates
are grouped into review buckets: high-confidence import, merge/duplicate review,
Codex-session lead, memory pointer, private/COI gated, and likely discard.

For the VS Code panel surface:

```powershell
.\.venv\Scripts\python.exe -m dtp workspace dashboard --surface vscode --out outputs/workspace-dashboard.html
```

`outputs/workspace-dashboard.html` is ignored local cache. It is the preferred
panel cache because it lets the extension refresh the view without committing
generated dashboard churn.

## Recovery Command

Use recovery when the question is "what did we do or discuss that is missing
from the tracker?"

```powershell
.\.venv\Scripts\python.exe -m dtp workspace recover --dry-run
```

Dry run writes review artifacts only:

- `outputs/workspace-recovery-candidates.json`
- `outputs/workspace-recovery-candidates.md`
- `outputs/notion-workspace-cockpit.json`

The recovery pass scans structured DTP docs, roadmap backlog rows, Kaizen,
proof queue rows, workspace report sources, repo-local Kanban boards, Codex
session-index metadata, and saved memory registry pointers. It does not copy
raw transcripts into tracked docs.

After review, import only approved rows:

```powershell
.\.venv\Scripts\python.exe -m dtp workspace recover --apply --approved outputs/workspace-recovery-candidates.json
```

`--apply` writes the reviewed rows into
`practice-os/workspace/task-ledger.jsonl`. That ledger becomes the first source
the dashboard reads before enriching from Kaizen, proof, repo coverage, and
backlog docs.

## Dashboard Validation

```powershell
.\.venv\Scripts\python.exe -m dtp workspace validate-dashboard
```

Validation writes ignored review artifacts:

- `outputs/workspace-dashboard-validation.json`
- `outputs/workspace-dashboard-validation.md`

The report compares reviewed dashboard rows, Recovery Inbox candidates, rendered
HTML row counts, metric counts, local source refs, terminal archive rows,
Register filter counts, Recovery Inbox bucket counts, local source refs,
terminal archive rows, private/COI redaction posture, duplicate task IDs, and
duplicate merges. Its summary categories are `in_dashboard`, `recovery_inbox`,
`excluded_or_redacted`, `duplicate_merged`, `source_missing`, `count_mismatch`,
and `duplicate_task_ids`.

## One-Screen Operating Workflow

```powershell
.\.venv\Scripts\python.exe -m dtp kaizen capture "New idea or issue"
.\.venv\Scripts\python.exe -m dtp workspace recover --dry-run
.\.venv\Scripts\python.exe -m dtp workspace recover --apply --approved outputs/workspace-recovery-approved.json
.\.venv\Scripts\python.exe -m dtp workspace dashboard
.\.venv\Scripts\python.exe -m dtp workspace validate-dashboard
```

Use `dtp workspace task add` only when the row is already reviewed and has a
clear source ref:

```powershell
.\.venv\Scripts\python.exe -m dtp workspace task add --title "Reviewed item" --repo diagnose-to-plan --status now --priority P1 --next-action "do the next reviewed action" --source-ref docs/ROADMAP_EXECUTION_BACKLOG.md --sensitivity internal-only --confidence high
```

## Notion Mirror Export

Dashboard and recovery refreshes write:

```text
outputs/notion-workspace-cockpit.json
```

This export is safe for manual Notion import or connector-based mirroring. It
contains only sanitized fields: title, repo, status, next action, DTP source
pointer, blocker class, priority, and last verified. DTP remains the source of
truth; Notion is the phone-friendly review/capture layer.

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
- The dashboard starts with the daily cockpit, not a long status dump.
- The dashboard reads the normalized workspace task ledger first, then enriches
  from Kaizen, proof queue, roadmap docs, repo manifests, evidence indexes, and
  repo-local boards.
- It makes `done`, `cancelled`, `superseded`, and `discarded` work visible as a
  closed archive without putting those rows back into active execution.
- It can recover older backlog, repo-local Kanban, proof, Codex session-index,
  and memory-pointer candidates through `dtp workspace recover --dry-run`.
- It shows sweep coverage from
  `docs/WORKSPACE_DOCS_AND_CHAT_SWEEP_LEDGER_2026-05-05.md`, including repos,
  Codex sources, and private/COI-gated exclusions.
- It does not replace repo-local verification.
- It points proof candidates back to `docs/PRACTICE_PROOF_QUEUE_INDEX.md`.
- It points offer copy decisions back to `docs/OFFER_TO_PROOF_MATRIX.md`.
- It can be opened directly from `docs/workspace-dashboard.html`.
- It can be opened inside VS Code through the local panel without a server,
  background watcher, deployment, or third-party dashboard source of truth.
- It writes a sanitized Notion mirror export under ignored `outputs/` without
  making Notion authoritative.

