---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: consulting

## Repo

- Name: `consulting`
- Branch: `main`
- Last updated: 2026-05-06
- Reviewer: Consulting live intake smoke pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| brand system | 2026-05-04 | pass | current branch | Official 2026-05-04 logo kit promoted into header, footer, favicon, Open Graph image, homepage slogan, `/start` copy, public assistant source docs, and repo-local brand decision record; see `practice-os/steward/2026-05-04-consulting-brand-system-promotion.md` |
| local | 2026-05-04 | pass | current branch | `npm run build`, `CONSULTING_PLAYWRIGHT_PORT=4322 npm run test:routes` (26/26), `npm run doctor`, `npm run security:secrets`, `npm run matrix`, and `git diff --check` passed; desktop/mobile screenshots recorded in `.audit-output` |
| support | 2026-05-06 | passed_with_notes | production | Live synthetic intake POST to `https://onhand.dev/api/intake` returned `ok: true`; private Hub dashboard verified the matching `supabase.intake_submissions` row by summarized fields; see `practice-os/steward/2026-05-06-consulting-live-intake-receipt.md` |
| CI | 2026-04-29 | pass | `4b9d0bc` | Consulting CI run `25132059660`: build and secret scan |
| release | 2026-04-30 | manual_pending | `4b9d0bc` | Vercel/live route proof not rerun in this batch |
| proof | 2026-04-30 | blocked | current branch | public proof needs DTP proof packet, permission, redaction, reviewer, and caveat |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| The consulting site has a Hub-first intake path and public/private command-room boundary | `README.md`, `docs/LAUNCH_CHECKLIST.md`, `/admin` implementation, `practice-os/steward/2026-05-06-consulting-live-intake-receipt.md` | internal_only | public-safe summary only; no private Hub rows or screenshots | Toni |
| Mom nonprofit clarity/maintainability improvement | private Mom kit proof candidate | missing owner permission | pending | pending |

## Open Gaps

- Public proof maturity is still the main business gap: proof packets must mature before consulting proof pages, screenshots, claims, or case-study assets change.
- Live intake support evidence has a production smoke receipt; cleanup is still
  not automated because Hub does not currently expose an intake delete/archive
  endpoint.
- Route tests are confirmed on the current machine as of 2026-05-04; browser CI expansion remains advisory.
- Live deployment was not triggered by the brand pass.

## Notes

This index records the planning surface only. It does not replace the consulting repo's local scripts, Vercel deployment evidence, or DTP proof packets.
