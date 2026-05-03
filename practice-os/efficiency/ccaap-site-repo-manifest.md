---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: ccaap-site

## Identity

- Repo: `ccaap-site`
- GitHub repo: `Toni-Montez-Consulting/ccaap-site`
- Local path: `ccaap-site`
- Primary role: custom off-Wix public site prototype for Concerned Citizens & African American Parents
- Owner lane: first client operating kit pilot and public-site implementation
- Public/private: private repo building a public nonprofit site
- Deploy target: Cloudflare Pages

## Boundaries

- Owns: public CCAAP site pages, Astro implementation, Git-backed content, content validation, Cloudflare Pages preview readiness, and launch runbooks
- Does not own: DTP private engagement kit, raw meeting transcript, member/payment records, private form submissions, consulting proof publication, CRM, custom payment processing, or Notion source-of-truth state
- Sensitive data: private owner notes, contact form submissions, payment notifications, member/student data, unapproved photos, PayPal management access, domain/DNS access, and any private nonprofit operational details
- COI/privacy notes: public site content can use approved public facts and owner-approved assets; proof/case-study promotion requires DTP proof governance first

## Gates

- Local gate: `pnpm install --frozen-lockfile`, `pnpm lint`, `pnpm check`, `pnpm validate:content`, `pnpm build`
- CI gate: GitHub Actions CI runs lint/build on `main` and pull requests
- Release gate: Cloudflare Pages preview passes, owner review passes, PayPal links are real, contact routing is approved, DNS is ready, authentic assets are approved, and `pnpm validate:launch` passes
- Support gate: launch checklist and deployment runbook stay current
- Manual gate: public proof requires permission, redaction, reviewer, after-state evidence, and caveat

## Evidence

- Evidence path: local command output, GitHub Actions logs, Cloudflare preview URL when connected, `docs/LAUNCH_CHECKLIST.md`, and DTP steward receipts
- Latest receipt: see `practice-os/efficiency/ccaap-site-evidence-index.md`
- Proof eligibility: internal candidate only until owner permission, redaction, reviewer approval, after-state evidence, and caveat are complete
- Redaction rule: do not publish raw transcript, private emails, payment records, form submissions, student/member data, secrets, or unsupported public claims

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `pnpm lint`, `pnpm check`, `pnpm validate:content`, `pnpm validate:launch`, `pnpm build`
- Safe write commands: public site docs/content/components when the CCAAP lane is active
- Commands that need explicit approval: production DNS/domain changes, PayPal button/link changes against live accounts, contact-form routing to real inboxes, Cloudflare production deploy actions, CMS/admin setup, AI chat, and public proof publication
- Dependency maintenance: keep lightweight; use local gates and CI before merging bumps
- Toolchain pinning: Astro/TypeScript/pnpm versions are repo-local; Cloudflare Pages should use Node 24

## Next Touch

- Lane: CCAAP launch readiness
- Trigger: PayPal links, contact routing, domain/DNS access, approved assets, owner review, or Cloudflare preview setup
- Blocker: production launch waits on PayPal donation/membership links, contact routing, DNS/domain access, authentic photos/resources, Leah plus Tony review, and proof permission/internal-only decision
- Next action: gather owner inputs with `docs/OWNER_LAUNCH_INPUTS.md`, replace placeholders, connect Cloudflare preview, add authentic assets/resources, and run owner review before production
