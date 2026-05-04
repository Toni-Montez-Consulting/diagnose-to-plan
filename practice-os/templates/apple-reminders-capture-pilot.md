---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Apple Reminders Capture Pilot

Use this before connecting Apple Reminders to any Notion, DTP, Hub, Google, or
third-party automation flow.

## Pilot Posture

- Apple Reminders remains Toni's daily action system.
- Google Tasks is not the replacement target.
- The pilot may mirror one dedicated business list only.
- DTP remains the source of truth for planning and promoted actions.
- Notion may mirror sanitized status after review.

## Source List

| Field | Value |
|---|---|
| Apple Reminders list name | `Consulting` for the first pilot; `Omnexus` and `Architected Strength` stay separate |
| Owner | Toni |
| List purpose | business capture / admin inbox / client follow-up / other |
| Included reminder types |  |
| Excluded reminder types | personal / family / health / legal-private / tax-private / client-private / unrelated Omnexus work / unrelated Architected Strength work |
| Review cadence | daily / weekly |

## Bridge Candidate

| Option | Decision | Notes |
|---|---|---|
| Manual review only | use / reject / later | simplest fallback |
| IFTTT iOS Reminders | pilot / reject / later | fastest one-list test; depends on iOS app permissions and background syncing |
| iOS Shortcuts webhook | pilot / reject / later | most controlled bridge; requires phone-side setup |
| macOS local script/EventKit | pilot / reject / later | private and controllable if a Mac is always on |
| Task-manager import | reject / later | avoid if it pulls Toni away from Reminders |

## Allowed Payload

Mirror only:

- reminder title;
- due date/time if present;
- source list name;
- source marker: `apple-reminders`;
- optional reviewed category assigned by Toni.

Do not mirror:

- notes/body text unless Toni explicitly approves the list and field;
- URLs or attachments by default;
- personal/family/health reminders;
- legal, tax, banking, or insurance detail;
- raw client-private tasks;
- completion state until duplicate/completion behavior is tested.

## Test Plan

| Test | Expected result | Evidence |
|---|---|---|
| Add non-private reminder to pilot list | appears in chosen bridge destination |  |
| Add reminder outside pilot list | does not appear in destination |  |
| Add reminder with due date | due date mirrors correctly or is omitted by design |  |
| Complete reminder in Apple Reminders | no external auto-completion unless approved |  |
| Disable bridge | new reminders stop moving |  |
| Revoke permission | tool no longer has Reminders access |  |

## Promotion Gate

- One-list pilot ran for at least one normal workday:
- No private reminders leaked:
- Background/scheduled behavior was reliable enough:
- Review workflow felt easier, not heavier:
- DTP source artifact updated first:
- Notion mirror row updated with sanitized status only:
- Public-site changes needed:

## Outcome

- Decision: keep manual / continue pilot / expand carefully / park / reject
- Next action:
- Blocker:
- Follow-up date:
