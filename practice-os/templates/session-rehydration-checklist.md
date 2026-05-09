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
- Rehydration trigger: new session | resume | reconnect | timeout | compacted context | handoff | other
- Last visible ledger item:
- Interrupted command/tool/process:
- Last known artifact/log/screenshot/draft:

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
| Tool/process state | background servers, preview ports, long-running commands, interrupted tool calls |  |
| Latest validation evidence | command logs, screenshots, test output, build output |  |

## Reconnect / Timeout Recovery

Use this section when the chat stream disconnects, a command times out, Codex
reconnects, context compacts, or a long-running tool call is interrupted.

- Did any command finish after the last visible assistant message?
- Did any background process remain running?
- Did any validation output become stale because a later command rebuilt,
  cleaned, redeployed, or regenerated files?
- Were screenshots, previews, test logs, drafts, or deployment state captured
  while another command was mutating the same output?
- What live evidence was checked after reconnect?
- What should Toni know about the trust level of the recovered state?
- What ledger item should carry forward?

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
