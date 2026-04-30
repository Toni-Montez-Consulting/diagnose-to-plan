---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: FamilyTrips

## Identity

- Repo: `FamilyTrips`
- GitHub repo: `Toni-Montez-Consulting/FamilyTrips`
- Local path: `FamilyTrips`
- Primary role: private family trip and event planning hub with static trip data, copyable group-chat helpers, and optional Supabase-backed checklist sync
- Owner lane: adjacent project privacy-first maintenance
- Public/private: private/internal family app, but deployed client bundles can expose any static trip data
- Deploy target: Vercel/static host with SPA rewrites

## Boundaries

- Owns: trip/event content, trip routes, family-friendly UX, static data validation, deploy smoke checks, Supabase checklist setup docs, and local privacy warnings
- Does not own: DTP practice roadmap, consulting proof, Hub runtime records, client engagement kits, public case studies, auth platform, or AI automation
- Sensitive data: trip attendee names, phone numbers, addresses, reservation details, budgets, passwords/door codes if ever added, emergency contacts, and family-only plans
- COI/privacy notes: unlisted trips are not private; anything in `src/data/trips` ships in the client bundle

## Gates

- Local gate: `npm run validate:data`, `npm run lint`, `npm run test`, `npm run build`
- CI gate: GitHub Actions `CI` runs npm install, data validation, lint, tests, and build on `main` pushes, pull requests, and manual dispatch
- Release gate: `docs/DEPLOY_SMOKE_TEST.md` after preview/production deploys
- Support gate: `README.md`, `ARCHITECTURE.md`, `ROADMAP.md`, `docs/SUPABASE.md`, and `docs/PLAYBOOK.md`
- Manual gate: privacy review before adding sensitive family details, AI features, auth, public sharing, or stronger Supabase behavior

## Evidence

- Evidence path: local command output, GitHub Actions logs, `docs/DEPLOY_SMOKE_TEST.md`, and DTP evidence receipts
- Latest receipt: see `practice-os/efficiency/familytrips-evidence-index.md`
- Proof eligibility: not a public proof source by default; internal pattern reference only unless family permission and redaction are explicit
- Redaction rule: never publish raw trip data, addresses, phone numbers, budgets, reservation details, private family notes, or screenshots with family information

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `npm run validate:data`, `npm run lint`, `npm run test`, `npm run build`
- Safe write commands: content/docs/tests only when FamilyTrips lane is active
- Commands that need explicit approval: Supabase policy/schema changes, Vercel env changes, production deploy actions, auth migration, AI/public sharing, and any publication of family-trip screenshots or data
- Dependency maintenance: keep lightweight; add automated dependency policy only if maintenance noise grows
- Toolchain pinning: npm/Vite/React/TypeScript versions are repo-local; revisit if build or CI drift appears

## Next Touch

- Lane: privacy-first maintenance
- Trigger: new trip/event, AI/public sharing request, Supabase behavior change, deploy/release, or repeated FamilyTrips edits
- Blocker: stronger privacy requires architecture change; unlisted trip routes are only casual visibility control
- Next action: keep local gates passing and avoid putting sensitive data in static trip objects
