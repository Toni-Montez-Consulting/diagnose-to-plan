---
data_class: P0
confidential: false
permission_level: internal_only
review_status: template
---

# Platform Preview Receipt

Use this when a meaningful change needs reviewable proof before production,
handoff, release, or public proof movement.

## Receipt Metadata

- Receipt id:
- Created:
- Repo/lane:
- Owner:
- Reviewer:
- Claim level: local | preview | production | operator-ready | public-proof-ready
- Status: draft | pass | pass_with_caveats | hold | block

## Change

- What changed:
- Why it changed:
- User/operator journey:
- Non-goals:
- No-touch areas:

## Environment

- Local URL or command:
- Preview URL:
- Production URL:
- Deployment id or commit:
- Environment variables checked by name only:
- Secret values printed: no

## Evidence

- Build/test/lint commands:
- Route/API checks:
- Browser/device checks:
- Screenshots or recordings:
- Logs inspected:
- Data writes or migrations:
- Skipped checks and reason:

## Integrity Check

- Truth: what can we honestly claim?
- Usefulness: what decision or action does this help?
- Restraint: what did we avoid overbuilding?
- Durability: what proves this beyond one demo?
- Handoff: what would a future maintainer need?

## Decision

- Decision:
- Caveats:
- Rollback path:
- Next action:
- Follow-up owner:

## Notes

Do not paste secrets, private rows, raw client screenshots, or unsupported proof
claims into this receipt.

