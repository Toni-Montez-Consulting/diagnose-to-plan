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
- Last updated: 2026-05-12
- Reviewer: CCAAP memory-capture and launch-readiness pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| V1 admin workflow | 2026-05-12 | pass_with_manual_gates | current branch | Sanity project `lbdkj3q0`, dataset `production`, CORS for `https://ccaap-site.vercel.app`, external Studio registration `fvaz4fy9de8i2gxh0a4k0inv`, and schema `_.schemas.ccaap` are configured; `/admin/` reaches the Sanity login provider screen; Leah and Tony have pending `Editor` invitations and still need to accept before end-to-end owner workflow testing |
| Vercel live prototype | 2026-05-12 | pass_with_manual_gates | `876e9bb` | Latest prototype is live at `https://ccaap-site.vercel.app`; manual Vercel deployment `dpl_3tUUjEAMSkXQDrgPusBe6MfTCw2V` route smoke returned `200` for `/`, `/board/`, `/meetings/`, `/join-donate/`, `/contact/`, and `/admin/`; GitHub CLI account `toniomon96` can read the private repo and branch `codex/ccaap-v1-admin-workflow` is pushed, but `vercel git connect` still fails until Vercel's GitHub app is granted access to `Toni-Montez-Consulting/ccaap-site` |
| Vercel Git preview | 2026-05-12 | pass_with_access_gate | `53c1865` | Vercel project link now points to GitHub org `Toni-Montez-Consulting`, repo `ccaap-site`, production branch `main`; push `53c1865` created automatic Preview deployment `dpl_NTn9duRpYLNS7U2ijnxQ3wN8UET7`, but unauthenticated preview route smoke returns `401` because Vercel preview protection is enabled |
| parent draft clarification | 2026-05-12 | draft_updated | current branch | Gmail draft `r-8887800189854309482` / message `19e1e21145573a24` now explains why apparently answered items still need exact launch confirmations for testing, security, privacy, payment safety, contact routing, meeting access, and site maintenance; it no longer re-asks for board approvals and asks Leah/Tony to accept pending Sanity editor invites |
| board approval correction | 2026-05-12 | corrected | current branch | Toni clarified that board photo/name approvals were already captured in the transcript; `ccaap-site` board profiles now set `ownerApproved: true`, board approval removed from active launch blockers, and public consulting proof remains blocked |
| layout/footer review and parent draft | 2026-05-12 | pass_with_manual_gates | current branch | CCAAP site review polished desktop/laptop/mobile spacing, widened subpage hero headings, redesigned footer treatment, staged Dad's Google Meet candidate while keeping launch blocked, and created Gmail draft `r-8887800189854309482` to Tony plus Leah |
| board-photo and bio staging | 2026-05-12 | pass_with_manual_gates | current branch | Resent Gmail `Pictures` messages exposed eight inline images; all were staged privately, only the exact Vernell Gregg filename match is assigned in the public prototype, and board launch remains blocked by final copy/photo approval |
| launch-candidate payment staging | 2026-05-12 | pass_with_manual_gates | current branch | Fresh Gmail scan found owner-provided PayPal candidates; `ccaap-site` staged them as `paymentStatus: candidate` so Join/Donate can be tested while production launch stays blocked by final payment review plus contact, meeting, board/media, asset, DNS, and proof gates |
| owner launch packet | 2026-05-12 | pass_with_manual_gates | current branch | May 12 prototype review captured a Vercel hosting decision, design direction, asset asks, update-workflow boundary, and remaining owner gates in `ccaap-site/docs/OWNER_LAUNCH_PACKET_2026-05-12.md` and `engagements/mom-nonprofit/site-rebuild/post-meeting-receipt-2026-05-12.md`; exact owner-approved launch inputs remain pending |
| owner review packet | 2026-05-01 | sent_with_temp_preview | current branch | Toni sent the owner review message and temporary prototype link to Leah plus Tony; exact owner-approved launch inputs remain pending |
| temporary preview smoke | 2026-05-01 | pass_with_advisory | current branch | Local `pnpm lint`, `pnpm check`, `pnpm validate:content`, and `pnpm build` passed; temporary Cloudflare quick-tunnel route smoke returned 200 for `/`, `/about/`, `/meetings/`, `/join-donate/`, `/resources/`, `/updates/`, `/board/`, and `/contact/`; link is ephemeral and only valid while Toni's machine/tunnel stay running |
| Cloudflare Pages CLI | 2026-05-01 | blocked_by_local_tooling | current branch | Direct Cloudflare Pages deploy via latest Wrangler was blocked on native Windows ARM64 because `workerd` reported unsupported platform; no Cloudflare API token was present in the shell; durable Pages setup still needs dashboard, API token, CI secret, or an x64/Linux deploy path |
| content | 2026-05-01 | pass_with_expected_warnings | current branch | `pnpm validate:content`; PayPal/contact placeholders remain expected production blockers |
| launch gate | 2026-05-01 | pass_with_expected_failure | current branch | `pnpm validate:launch` fails as intended on meeting link placeholders, board approval, PayPal URLs, and contact routing |
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

- PayPal donation link is staged as a candidate; final review is still needed before production.
- PayPal `$25` membership hosted button is staged as a candidate; final review is still needed before production.
- `info@citizensandparents.org` is staged as the likely public contact route; spam/routing approval is still missing.
- Dad's Google Meet evidence is staged as a candidate; final preview review is still needed before production.
- Board/profile names, copy, and received board-photo approval are captured for
  site use; any later gallery/archive placement is not a production-launch
  blocker.
- Domain/DNS access is still missing.
- Authentic photos and scholarship/resource files are still missing.
- Leah plus Tony owner feedback is now requested and still pending.
- Vercel live prototype exists at `https://ccaap-site.vercel.app`; GitHub
  review branch is pushed and GitHub CLI can read the repo, but Vercel GitHub
  app access to the private repo is still missing, so automatic push-to-preview
  is not complete.
- Owner-editable updates/photos workflow is now a V1 launch blocker: Sanity
  `/admin` project/env/schema/Studio registration is configured, and Leah/Tony
  editor invitations are pending acceptance.
- Public consulting proof remains blocked until permission, redaction, reviewer, evidence, and caveat pass.

## Notes

This DTP-owned index records launch-readiness evidence. It does not replace the CCAAP repo's local gates, Vercel preview evidence, private DTP engagement kit, or proof packet.
