---
data_class: P0
confidential: false
permission_level: internal_only
review_status: checked
---

# Consulting Brand System Promotion - 2026-05-04

## Trigger

Toni called out that the public marketing updates, including slogan and logo,
had not been carried into the relevant public surfaces. The fix needed to
implement the current brand where safe and record the broader rollout boundary
so future agents do not rely on stale chat memory.

## Source Of Truth

Official brand kit:

`C:\Users\tonimontez\Pictures\Toni-Montez-Official-Logo-Kit\2026-05-04`

Approved brand language:

- Primary slogan: `Get the Work Out of Your Head.`
- Supporting descriptor: `Custom Apps / Workflow Systems / Practical AI Tools`
- Full explanation: `I help owner-led businesses turn scattered processes,
  manual work, and owner-only knowledge into custom apps, workflow systems, and
  practical AI tools that make the business easier to run.`

## Implemented In `consulting`

| Surface | Change |
|---|---|
| Header | replaced the generated text wordmark with the official horizontal reverse logo |
| Footer | replaced the generated `tm` mark with the official TM monogram |
| Favicon | replaced root and brand favicon SVG; added official `.ico` |
| Social card | installed the official `13-open-graph-1200x630.png` as the default Open Graph image |
| Homepage | promoted the official slogan, descriptor, and full explanation into the hero |
| `/start` | aligned the diagnostic entry copy with the new brand promise |
| Docs | updated public assistant source docs, launch checklist, site roadmap, product contract, Figma handoff, and repo roadmap |
| Decision log | added a repo-local decision record for the brand integration |

## Boundary

- This was a consulting public-site update, not a proof promotion.
- No new client proof, employer proof, Microsoft proof, or endorsement language
  was added.
- Architected Strength and other sibling sites were not bulk-edited. They need a
  separately reopened scope because their brand role is not identical to the
  consulting offer surface.
- The official logo blue remains an identity-asset exception for now; the Steel
  Ledger site accent remains `--signal` unless a full visual design pass is
  opened.

## Verification

Consulting checks after the update:

| Check | Result |
|---|---|
| `npm run build` | pass |
| `CONSULTING_PLAYWRIGHT_PORT=4322 npm run test:routes` | pass, 26/26 |
| `npm run doctor` | pass |
| `npm run security:secrets` | pass, no leaks found |
| `npm run matrix` | pass, matrix printed |
| `git diff --check` | pass; only line-ending warnings from the Windows checkout |

Manual screenshot review:

- Desktop screenshot: `C:\Users\tonimontez\.audit-output\consulting-brand-home-desktop-2026-05-04.png`
- Mobile screenshot: `C:\Users\tonimontez\.audit-output\consulting-brand-home-mobile-2026-05-04.png`
- Result: official logo renders, homepage slogan leads, descriptor wraps on
  mobile, and the route suite found no horizontal overflow.

## Next

Keep the brand kit path in the Business Admin OS as the source. If Toni wants
the updated identity moved into Architected Strength, Omnexus, DeMario, CCAAP,
or another public surface, open that lane explicitly and apply the local public
boundary before changing assets or copy.
