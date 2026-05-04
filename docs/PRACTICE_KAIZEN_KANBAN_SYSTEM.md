---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Practice Kaizen Kanban System

Status: active DTP-first operating loop.

Owner: `diagnose-to-plan`

Purpose: make every meaningful new idea, ask, feature, engagement signal,
blocker, proof candidate, correction, repo issue, or process improvement land in
one small index before it becomes roadmap work, client work, public proof, or
automation.

This is not another narrative-doc layer. It is the intake/index layer above the
existing roadmap, steward receipts, proof packets, engagement kits, repo
manifests, and Notion mirror.

## Operating Contract

The loop is:

1. Capture: record the item with `dtp kaizen capture`.
2. Classify: assign type, sensitivity, owning repo, status, and Notion target.
3. Route: connect it to the right DTP source path and next action.
4. Stage: leave it in inbox, move it to `now`, `waiting`, `blocked`, or
   `parked`, or promote it to a real artifact.
5. Execute: work only from the accepted queue and repo boundary.
6. Verify: run the owning repo's local, CI, manual, proof, or privacy gates.
7. Record: update the Kaizen record, backlog, steward receipt, proof packet,
   engagement kit, or decision record.
8. Improve: convert repeated misses into templates, checks, docs, or backlog
   stories.

## Source-Of-Truth Rule

DTP owns the truth:

- `practice-os/kaizen/intake.jsonl` owns lightweight capture.
- `docs/ROADMAP_EXECUTION_BACKLOG.md` owns active Kanban story state.
- `practice-os/steward/` owns session receipts and focus decisions.
- `engagements/` owns private client truth.
- `practice-os/templates/*proof*` and `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md`
  own proof movement.

Notion mirrors safe summaries. If Notion and DTP disagree, DTP wins until a
steward review intentionally updates DTP.

## CLI Surface

```powershell
.\.venv\Scripts\python.exe -m dtp kaizen capture "New idea or request"
.\.venv\Scripts\python.exe -m dtp kaizen capture "Client reply landed" --type client_reply --sensitivity private-client --status waiting
.\.venv\Scripts\python.exe -m dtp kaizen update kzn-YYYYMMDD-slug-hash --status waiting --next-action "wait on owner"
.\.venv\Scripts\python.exe -m dtp kaizen status --status now --limit 5
.\.venv\Scripts\python.exe -m dtp kaizen mirror --dry-run --limit 100
```

`capture` creates one committed JSONL record by default. If sensitivity is
`private-client` or `coi-gated`, or the text contains private/secret markers,
the committed record stores only a redacted stub and writes raw text to ignored
local state at `.dtp/kaizen/private-intake.jsonl`.

`update` moves an existing record through the lifecycle without hand-editing
JSONL. Use it for status, owner repo, next action, sensitivity, DTP source path,
Notion target, and tags.

`status` shows counts for inbox, now, next, waiting, blocked, parked, done, and
the latest records in active queues. Use `--status` and `--limit` for bounded
review.

`mirror --dry-run` emits sanitized Notion rows and explicit blocked rows. It
skips `done` rows by default; use `--include-done` only for deliberate archive
or closeout review.

`mirror --apply` is gated. Live Notion writes require reviewed dry-run output,
available Notion auth, and a steward receipt recording the write boundary.

## Record Shape

Each JSONL row has:

- `id`: stable `kzn-YYYYMMDD-slug-hash` record ID.
- `captured_at`: ISO timestamp.
- `title`: short human title.
- `text`: source capture text. Keep it concise.
- `item_type`: `ask`, `idea`, `feature`, `engagement`, `client_reply`,
  `proof`, `repo_issue`, `blocker`, `correction`, `decision`, `research`,
  `tooling`, or `process`.
- `status`: `inbox`, `now`, `next`, `waiting`, `blocked`, `parked`, or `done`.
- `sensitivity`: `public-safe`, `internal-only`, `private-client`, or
  `coi-gated`.
- `repo`: owning repo or lane.
- `source`: `codex`, `notion`, `meeting`, `repo`, `gmail`, or another capture
  source.
- `dtp_source_path`: DTP path that backs or will back the item.
- `notion_target`: `Ideas`, `Roadmap Stories`, `Repo Health`, `Proof Queue`,
  `Waiting On`, or `Today`.
- `next_action`: smallest useful next move.
- `tags`: optional lightweight tags.
- `raw_ref`: optional pointer to ignored local raw-private state. This must never
  be a public URL or committed raw text.

## Classification Defaults

Use `--type auto` and `--sensitivity auto` unless the source is obvious.

Automatic classification is deliberately conservative:

- client names, engagement terms, raw replies, payment, secrets, or private-kit
  language become private-client or blocked from Notion;
- DSE, Microsoft confidential, or COI terms become COI-gated;
- proof and public-claim language routes to proof governance;
- repo/PR/failing/dirty state routes to repo health;
- feature/build/add/implement language routes to roadmap stories;
- process/kaizen/kanban/sprint language routes to process.

Steward review can override the type, owner, and status later.

## Promotion Rules

Promote a Kaizen record only when the next artifact is real:

| If the item is... | Promote to... |
|---|---|
| active roadmap work | `docs/ROADMAP_EXECUTION_BACKLOG.md` story |
| major planning/session state | `practice-os/steward/*.md` receipt |
| private client work | `engagements/` kit or vault note |
| proof candidate | proof packet plus redaction/permission gates |
| architecture or workflow choice | `decisions/` record |
| research/tool signal | research radar or bounded research spike |
| recurring process miss | template, doctor check, or backlog story |
| useful but inactive | parked queue with next review trigger |

Do not promote everything. Capture everything meaningful, then promote only what
changes execution order, status, evidence, proof, repo health, client state, or
future operating behavior.

## Notion Mirror Rules

Allowed in Notion dry-run rows:

- sanitized title and summary;
- status, type, repo, next action, and DTP source path;
- public-safe or internal-only sensitivity.

Blocked from Notion rows:

- `private-client` and `coi-gated` records;
- secrets, tokens, passwords, raw transcripts, payment or banking details;
- unreviewed proof claims;
- private client notes, raw DSE material, or unsupported public claims.

Notion-to-DTP starts as inbox capture only. It does not directly mutate DTP
roadmap status until a steward review promotes the item.

## Private Capture Rule

Private capture is allowed only because the committed index is sanitized.

Committed:

- stable ID;
- redacted title/text;
- type, status, sensitivity, owning repo, DTP source path, Notion target, next
  action, tags;
- optional `raw_ref` pointing to ignored local state.

Ignored local state:

- `.dtp/kaizen/private-intake.jsonl`;
- raw private-client or COI capture text;
- never committed, mirrored, or used as proof.

## Daily Use

Start broad work with:

```powershell
.\.venv\Scripts\python.exe -m dtp kaizen status
.\.venv\Scripts\python.exe -m dtp workspace report
```

When Toni adds something meaningful mid-session, capture it immediately:

```powershell
.\.venv\Scripts\python.exe -m dtp kaizen capture "..."
```

At the end of a major work block, either leave records in the right status or
promote them into backlog, steward, proof, engagement, research, or decision
artifacts. Then run the relevant verification gates.
