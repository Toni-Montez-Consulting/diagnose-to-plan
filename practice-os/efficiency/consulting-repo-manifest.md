---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: consulting

## Identity

- Repo: `consulting`
- GitHub repo: `Toni-Montez-Consulting/consulting`
- Local path: `consulting`
- Primary role: public consulting storefront, official Toni Montez brand surface, public-safe proof surface, Hub-first intake path, and noindex admin command room
- Owner lane: public proof and storefront
- Public/private: public site repo with private operational boundaries
- Deploy target: Vercel, canonical domain `tonimontez.co`

## Boundaries

- Owns: public routes, official consulting brand application, site copy, Steel Ledger visual baseline, proof presentation, `/start` intake UX, `/admin` command-room launcher, Hub/Formspree/email fallback routing
- Does not own: private DTP engagement kits, Hub runtime rows, Supabase service-role access, global skills, client CRM/billing, private proof review
- Sensitive data: proof assets, intake endpoint configuration, owner/client evidence before redaction, admin links
- COI/privacy notes: public proof needs DTP proof/redaction review before publication; Microsoft/DSE-adjacent proof needs COI-aware screening before reuse

## Gates

- Local gate: `npm run build`, `npm run security:secrets`; `npm run test:routes` when browser setup is available
- CI gate: Consulting CI runs build and secret scan on `main`
- Release gate: Vercel deployment, route smoke, `/admin` noindex, sitemap exclusion, form destination check, Hub CORS/intake behavior when available
- Support gate: Hub intake is primary, Formspree fallback is secondary, email is last fallback
- Manual gate: public proof requires evidence, permission, redaction, reviewer, and caveat

## Evidence

- Evidence path: GitHub Actions logs, Playwright route artifacts when route tests run, DTP proof packets for public claims
- Latest receipt: see `practice-os/efficiency/consulting-evidence-index.md`
- Proof eligibility: public proof only after DTP proof/redaction gates pass
- Redaction rule: never publish raw client material, private screenshots, intake records, service-role data, or unapproved claims

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `npm run doctor`, `npm run matrix`
- Safe write commands: public site docs/content/components after task approval
- Commands that need explicit approval: Vercel environment changes, public proof publication, production intake tests, proof asset replacement
- Dependency maintenance: use CI/build evidence before merging dependency bumps
- Toolchain pinning: Node/Astro/Tailwind versions remain repo-local; revisit during dependency-maintenance lane

## Next Touch

- Lane: public brand/proof upgrade and route/visual verification
- Trigger: a reviewed DTP proof packet is ready, Toni approves a newer brand source, or the consulting site intake/proof lane resumes
- Blocker: no proof should publish until permission, redaction, reviewer, evidence, and caveat are real
- Next action: keep current site stable; promote Mom/Omnexus/DeMario proof only through the DTP proof packet flow
