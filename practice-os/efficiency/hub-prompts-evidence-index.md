---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: hub-prompts

## Repo

- Name: `hub-prompts`
- Branch: `main`
- Last updated: 2026-04-30
- Reviewer: accepted by steward review on 2026-04-30

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| local | 2026-04-30 | pass | `49c3d63` | `npm test`: `npm run validate` and `npm run validate:phase0`; 6 prompts checked; Phase 0 prompts valid |
| CI | 2026-04-29 | pass | `49c3d63` | GitHub Actions `Validate Prompts` run 25132070092 |
| release | 2026-04-30 | not_applicable | `49c3d63` | no prompt content or prompt schema changed in this DTP coverage pass |
| support | 2026-04-30 | hub_owned | `49c3d63` | Hub prompt sync/runtime verification stays in Hub, not `hub-prompts` |
| proof | 2026-04-30 | internal_only | `49c3d63` | prompt validation evidence is not public proof by default |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| Hub prompt catalogue has a local validation gate | `npm test` output and GitHub Actions run 25132070092 | internal_only | no public proof | steward reviewed |

## Open Gaps

- No prompt eval garden has been added yet.
- Golden fixtures should be added only after real prompt misfires or high-value workflows justify them.
- Hub runtime prompt sync remains Hub-owned.

## Notes

This index is a DTP-owned planning receipt. It does not replace the repo's own validation workflow or authorize prompt content changes.
