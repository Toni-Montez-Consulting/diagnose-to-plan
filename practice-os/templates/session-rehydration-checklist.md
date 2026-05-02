---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Session Rehydration Checklist

Use this before a broad session where memory drift could cause missed context,
wrong repo edits, premature client actions, or duplicate infrastructure.

## Session

- Date:
- Prompt / reason:
- Primary repo:
- Other repos in scope:
- Clients / workstreams in scope:
- Explicit no-touch areas:

## Source Sweep

| Source | Check | Result / pointer |
|---|---|---|
| DTP roadmap/backlog | `docs/ROADMAP_EXECUTION_BACKLOG.md` and owning docs |  |
| DTP docs map | `docs/DOCUMENTATION_MAP.md` |  |
| Steward receipts | `practice-os/steward/` recent relevant receipts |  |
| Active engagement kit | `engagements/<client>/<engagement>/` |  |
| Git state | `git status --short --branch` |  |
| Recent commits | `git log --oneline -n 8` |  |
| Workspace report | `dtp workspace report` when cross-repo |  |
| Client kit status | `dtp kit status <client>` when client-specific |  |
| Gmail | relevant thread only |  |
| Calendar | relevant meeting/cadence only |  |
| Notion | sanitized cockpit status only |  |

## Active State

| Workstream | Current status | Waiting on | Next action | Blocked by |
|---|---|---|---|---|
| Cam |  |  |  |  |
| Greg |  |  |  |  |
| CCAAP |  |  |  |  |
| Consulting site |  |  |  |  |
| Business Brain / DTP |  |  |  |  |

## Memory Confidence

| Claim / assumption | Source used | Last verified | Drift risk | Refresh needed? |
|---|---|---|---|---|
|  |  |  | low / medium / high | yes / no |

## Decisions Before Action

- Can this be implemented now?
- Does DTP need updating before Notion?
- Does a human need to reply before work proceeds?
- Is any repo access, live data, public proof, payment, legal, COI, or privacy
  gate involved?
- Does this need a steward receipt?

## Closeout

- DTP files updated:
- Notion mirror updated:
- Gmail/Calendar action:
- Verification run:
- Commit:
- Remaining unknowns:
