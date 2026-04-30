---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: ccaap-site

## Repo

- Name: `ccaap-site`
- Branch: `main`
- Last updated: 2026-04-30
- Reviewer: CCAAP memory-capture and launch-readiness pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| install | 2026-04-30 | pass_with_advisory | current branch | `pnpm install --frozen-lockfile`; pnpm reports ignored build scripts for esbuild/sharp until explicitly approved |
| lint | 2026-04-30 | pass | current branch | `pnpm lint`; Astro check and content validation passed |
| typecheck | 2026-04-30 | pass | current branch | `pnpm check`; 14 Astro files checked with 0 errors/warnings/hints |
| content | 2026-04-30 | pass_with_expected_warnings | current branch | `pnpm validate:content`; PayPal/contact placeholders remain expected production blockers |
| build | 2026-04-30 | pass_with_expected_warnings | current branch | `pnpm build`; 8 static pages generated, PayPal/contact placeholders remain expected production blockers |
| launch gate | 2026-04-30 | pass_with_expected_failure | `e7522c2` | `pnpm validate:launch` now fails production launch while meeting links, board approval, PayPal URLs, and contact routing remain placeholders |
| docs | 2026-04-30 | pass | `e7522c2` | README, owner input packet, prototype plan, launch checklist, and deployment runbook document remaining launch/proof gates |
| proof | 2026-04-30 | blocked | current branch | public proof remains blocked until permission, redaction, reviewer, evidence, and caveat are complete |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| CCAAP is moving from Wix to a lower-cost custom site with clearer launch gates | private owner conversation summary, `ccaap-site` prototype, DTP steward receipts | owner permission missing for public proof | pending | pending |

## Open Gaps

- Exact PayPal donation link/button ID is still missing.
- Exact PayPal `$25` membership link/button ID is still missing.
- Contact routing inbox and spam protection are still missing.
- Exact public meeting link label/destination is still missing.
- Board/profile copy and media approval is still missing.
- Domain/DNS access is still missing.
- Authentic photos and scholarship/resource files are still missing.
- Leah plus Dad owner review is still pending.
- Cloudflare Pages preview is not connected yet.
- Public consulting proof remains blocked until permission, redaction, reviewer, evidence, and caveat pass.

## Notes

This DTP-owned index records launch-readiness evidence. It does not replace the CCAAP repo's local gates, Cloudflare preview evidence, private DTP engagement kit, or proof packet.
