---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Steward Receipt: Notion Command Center V1

Date: 2026-05-03

Owner repo: `diagnose-to-plan`

Live Notion surface: `DTP Practice OS Command Center`

Notion page: `https://www.notion.so/35272f18e4cc81838fa8fc90e397057a`

## Decision

Improve the existing Notion command center in place. DTP remains the source of
truth; Notion remains the phone-friendly cockpit, mirror, and inbox.

## DTP Changes

- Added `practice-os/templates/notion-cockpit-audit.md`.
- Updated `docs/NOTION_MIRROR_V0.md` with the V1 Command Center upgrade rule.
- Updated roadmap and documentation pointers so future Notion rebuilds route
  through DTP first.
- Added `notion-cockpit-audit.md` to `dtp practice doctor`.

## Live Notion Changes

- Kept the existing `DTP Practice OS Command Center`; no parallel cockpit was
  created.
- Added missing Client Pilot Snapshot fields:
  - `Lane`
  - `DTP Source`
  - `proof_status`
- Added Roadmap Stories field:
  - `Phase`
- Rebuilt the Command Center page around these sections:
  - `Today`
  - `This Week`
  - `Waiting On`
  - `Decision Needed`
  - `Client Lanes`
  - `Proof Queue`
  - `Roadmap`
  - `Idea Inbox`
  - `Repo Health`
  - `Meetings`
  - `Archive`
- Added linked cockpit views for:
  - Today
  - This Week
  - Waiting On
  - Decision Needed
  - Client Lanes
  - Proof Blocked
  - Roadmap Active Next
  - Idea Inbox
  - Repo Health
  - Recent Meetings

## Audit Result

| Check | Result |
|---|---|
| Existing command center found | yes |
| Expected V0 databases present | yes |
| Parallel command center created | no |
| Private engagement data mirrored | no |
| Secrets/raw emails/transcripts/payment records mirrored | no |
| Unsupported public proof claims mirrored | no |
| DTP source-of-truth boundary preserved | yes |
| One DTP-backed sanitized mirror item added | yes; Notion row `https://www.notion.so/35572f18e4cc81e0850bf1c2a39987e7` |

## Verification

- Fetched the rebuilt Command Center after update and confirmed the visible
  section order is:
  `Today`, `This Week`, `Waiting On`, `Decision Needed`, `Client Lanes`,
  `Proof Queue`, `Roadmap`, `Idea Inbox`, `Repo Health`, `Meetings`,
  `Operating Rule`, `Safety Boundary`, `Archive`.
- Searched Notion for the sanitized decision row and confirmed the row points to
  `practice-os/steward/2026-05-03-notion-command-center-v1.md`.
- Notion SQL data-source query was advertised by tool discovery but unavailable
  at runtime, so live verification used fetch/search instead.
- DTP validation passed:
  - `git diff --check` with line-ending warnings only
  - `pytest`
  - `ruff check .`
  - `dtp practice doctor`
  - `dtp skills --validate`
  - `dtp redact check practice-os --profile practice`

## Open / Parked

- Notion is still not a two-way sync surface.
- Notion database templates/buttons were not deeply built in this slice; the
  cockpit now has the structure for those templates, but reusable Notion-native
  templates should be added only after Toni uses the V1 cockpit for a real reset.
- Automated DTP-to-Notion export remains parked behind a dry-run export and
  redaction review.

## Toni Correction Checklist

- Is the first-screen order right: `Today`, `This Week`, `Waiting On`,
  `Decision Needed`, then lanes/proof/roadmap?
- Should `Proof Queue` be above client lanes, or is its current position right?
- Are `Lane` and `proof_status` the right names, or should Notion use friendlier
  labels while DTP keeps stricter field names?
- Is the Archive section helpful, or should source databases be moved lower or
  hidden after a week of use?
- Does any wording on the page feel too generic, too polished, or unclear?

## Next Action

Use the next Business Brain reset or real Cam/Greg/CCAAP reply to update DTP
first, then mirror only the safe cockpit fields into Notion.
