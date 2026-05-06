---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: demario-pickleball-1

## Identity

- Repo: `demario-pickleball-1`
- GitHub repo: `Toni-Montez-Consulting/demario-pickleball`
- Local path: `demario-pickleball-1`
- Primary role: DeMario Pickleball public site, booking flow, admin command room, owner tasks, owner roadmap, and local-business launch track
- Owner lane: adjacent project launch, proof, and Client Command Room reference
- Public/private: public marketing and booking site with private admin, booking, inquiry, payment, and Supabase boundaries
- Deploy target: Vercel, canonical domain `demariomontezpb.com`

## Boundaries

- Owns: public lesson site, booking workflow, `/pay`, `/admin`, owner tasks, owner roadmap, developer roadmap, venue-routing rules, admin handoff, booking/inquiry APIs, Supabase launch SQL docs, and local-business launch gates
- Does not own: DTP's practice roadmap, consulting public proof pages, Hub runtime rows, global skill installation, private DTP engagement kits, or final public proof approval
- Sensitive data: booking records, inquiry records, student names/emails/phones, admin emails, Supabase keys, Google OAuth tokens, payment memos, venue agreements, insurance/waiver proof, private testimonials, and unapproved screenshots
- COI/privacy notes: this repo is not Microsoft-adjacent by default. Toni-owned
  text posting about the public launch was posted on 2026-05-06 per Toni's
  report through the DTP proof packet boundary; consulting-site proof reuse,
  testimonials, metrics, and private screenshots still require source evidence,
  redaction, reviewer approval, and caveats.

## Gates

- Local gate: `npm run ci` for `typecheck`, `lint`, Vitest, and `next build`
- E2E gate: `npm run test:e2e` when browser dependencies and test data are intentionally available
- CI gate: GitHub Actions `CI` on `master` runs `npm ci`, `typecheck`, `lint`, tests, build, Playwright browser install, and E2E
- Release gate: `docs/RELEASE_CHECKLIST.md`, including Supabase SQL, admin/MFA, Google Calendar OAuth, live booking QA, monitoring, and business gates
- Support gate: `docs/ADMIN_HANDOFF.md`, `docs/MARIO_ACTION_PLAN.md`, `/admin/tasks`, `/admin/roadmap`, and `docs/VENUE_RULES.md`
- Manual gate: public text copy was cleared and posted from Toni-owned channels; review/testimonial claims, metrics, command-room screenshots, and owner walkthroughs need explicit permission before public proof reuse

## Evidence

- Evidence path: GitHub Actions logs, local `npm run ci`, `docs/RELEASE_CHECKLIST.md`, `docs/LAUNCH_OUTSTANDING.md`, `docs/ADMIN_HANDOFF.md`, `docs/MARIO_ACTION_PLAN.md`, and future DTP proof packets
- Latest receipt: see `practice-os/efficiency/demario-pickleball-1-evidence-index.md`
- Proof eligibility: Toni-owned text copy was posted on LinkedIn/Instagram per
  Toni's 2026-05-06 report; exact post URL capture remains pending if durable
  public-link proof is useful. Command-room proof, testimonials, metrics, and
  consulting-site reuse still need permission, redaction, reviewer, evidence,
  and caveat gates.
- Redaction rule: never publish raw booking rows, inquiry rows, phone numbers, emails, payment records, admin screenshots with private data, Supabase/OAuth values, venue agreements, insurance certificates, or student/private testimonial material

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `npm run ci`, `gh run list`
- Safe write commands: repo docs, site copy, tests, and app code only when the DeMario lane is active and the change matches owner/developer roadmap scope
- Commands that need explicit approval: production Supabase SQL, Vercel environment changes, Google OAuth refresh-token generation, live booking/payment tests, production admin actions, public screenshot capture, and public proof publication
- Dependency maintenance: Node 24 migration is already tracked as a developer-roadmap item; dependency advisory upgrades should use a tested branch, not `npm audit fix --force`
- Toolchain pinning: Next 16, React 19, Node 20 CI today; revisit runner/toolchain expectations before GitHub's Node 24 default transition

## Next Touch

- Lane: launch gate cleanup, command-room proof packet, and Node/toolchain maintenance
- Trigger: final public post URLs are available, a venue-routing rule changes, Node 24 migration becomes current, or the consulting proof lane needs owner-approved DeMario evidence
- Blocker: testimonials, metrics, command-room screenshot proof, booking/payment proof, and consulting-site reuse are blocked until source evidence, permission, redaction, reviewer approval, and launch context are real
- Next action: capture exact LinkedIn/Instagram post URL(s) if durable public-link proof is useful; do not promote screenshots, metrics, testimonials, or private claims into consulting until a separate proof packet clears them
