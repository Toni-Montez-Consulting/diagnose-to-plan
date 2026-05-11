---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Prospect Follow-Up Drafting Kit Receipt

Date: 2026-05-11

Owner repo: `diagnose-to-plan`

Status: implemented as draft-only Practice OS documentation and templates.

## Trigger

The live intake workflow now turns a `tonimontez.co/start` submission into a
triage and route decision. The next operator gap was the follow-up step: how to
produce a useful prospect-facing draft without auto-sending, leaking internal
reasoning, or collapsing every route into "book a call."

## Sources Used

- `docs/LIVE_INTAKE_TO_PRACTICE_OS_WORKFLOW_V0.md`
- `practice-os/templates/prospect-intake-triage.md`
- `practice-os/agents/external-communications.md`
- `docs/CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md`
- `practice-os/templates/approval-gate.md`

## Decision

Add a draft-only prospect follow-up kit:

- one playbook for choosing the follow-up path;
- one fit-call follow-up template;
- one paid Blueprint follow-up template;
- one park-or-decline follow-up template;
- roadmap and documentation-map pointers.

Do not add Gmail automation, calendar automation, Hub triage fields, pricing
defaults, public proof movement, or hosted-DTP record behavior in this slice.

## Business Value

This closes the next loop after intake:

1. Hub records the inquiry.
2. DTP triages what it means.
3. Toni gets a practical draft for the next human-reviewed step.

The value is not automatic sales. The value is better first-response judgment:
clearer routing, less rewriting, fewer accidental promises, and more consistent
builder-led communication.

## Work Performed

- Added `docs/PROSPECT_FOLLOW_UP_DRAFTING_PLAYBOOK_V0.md`.
- Added `practice-os/templates/prospect-fit-call-follow-up.md`.
- Added `practice-os/templates/prospect-paid-blueprint-follow-up.md`.
- Added `practice-os/templates/prospect-park-or-decline-follow-up.md`.
- Updated live-intake, roadmap, documentation-map, control-plane, backlog, and
  reprioritization pointers.

## Approval Gates Preserved

| Gate | State |
|---|---|
| Client/prospect communication send | pending Toni review |
| Gmail draft creation | pending Toni request and connector support |
| Calendar invite | blocked until time and attendees are confirmed |
| Pricing | pending Toni approval |
| Public proof | blocked until proof promotion gates pass |
| Legal/contract/data language | escalate before send |
| Production implementation | blocked until scoped and approved |

## Non-Goals

- No exact pricing.
- No proposal/SOW generator.
- No auto-send.
- No CRM workflow.
- No Hub schema change.
- No Notion or Gmail sync.
- No public proof promotion.
- No hosted DTP expansion.

## Verification

- `git diff --check`: passed with line-ending warnings only.
- `.\.venv\Scripts\python.exe -m ruff check .`: passed.
- `.\.venv\Scripts\python.exe -m dtp skills --validate`: passed.
- `.\.venv\Scripts\python.exe -m dtp practice doctor`: passed.
- `.\.venv\Scripts\python.exe -m pytest`: passed, 145 passed and 3 skipped.
- `gitleaks detect --no-git --source . --config .gitleaks.toml --redact --verbose`:
  passed with no leaks found.

## Next Action

Use the prospect intake triage template and then one follow-up draft template on
the next real prospect intake. After two or three real uses, decide whether the
kit needs more routes, examples, or Hub/Notion status support.

## Open Questions

These are non-blocking:

1. Should the first real intake default to a fit call before a paid Blueprint
   pitch, or should strong high-intent cases go straight to Blueprint language?
2. Should Toni maintain one approved booking link for all fit calls, or keep
   scheduling manual until volume proves the need?
3. Should we later add a Fast Track follow-up template, or wait until a real
   intake proves a small implementation scope?
