---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: fitness-app / Omnexus

## Identity

- Repo: `fitness-app` / Omnexus
- Local path: `fitness-app`
- Primary role: founder/product/operator app with mobile release, billing, entitlements, Supabase contracts, verification cockpit, and public-proof potential
- Owner lane: adjacent project verification cockpit reference and app-release evidence
- Public/private: app source repo with private production data, credentials, billing records, app-store state, and user data kept outside git
- Deploy target: Vercel web app plus Capacitor/iOS/Android release surfaces

## Boundaries

- Owns: Omnexus product code, app release workflow, billing/entitlements, Supabase migrations/contracts, app-store support artifacts, CI/security gates, and verification cockpit implementation
- Does not own: DTP practice roadmap, consulting public proof pages, Hub runtime intake, private DTP engagement kits, `tm-skills`, or workspace-wide command runners
- Sensitive data: Supabase production data, auth users, subscriptions, Stripe/IAP records, HealthKit-related user data, App Store reviewer details, Sentry/PostHog data, env vars, and private proof screenshots
- COI/privacy notes: Omnexus can be a strong proof/reference source, but public claims need proof packet, permission, redaction, reviewer, and caveat gates before consulting publication

## Gates

- Local gate: `npm run lint`, `npm run typecheck`, `npm run build`, `npm run db:schema:contract:local`, `npx supabase db lint --local`, and `npm run tools:verify:local` when the local Docker/Supabase setup is available
- CI gate: GitHub Actions `CI`, `Security Ops`, `Semgrep`, `PR Hygiene`, `Dependency Review`, and workflow-dispatched `Verification Toolkit` when release evidence is needed
- Release gate: `Preview/Production Verification Gate`, Vercel status, `npm run tools:verify:release`, App Store/TestFlight manual evidence, and production verification runbooks
- Support gate: health/synthetic-monitor workflows, release evidence, Sentry/PostHog review, Supabase production-safe SQL checks, and app-store evidence trackers
- Manual gate: production data checks, App Review state, IAP product state, reviewer credentials, mobile-device QA, public proof permission, and screenshot/redaction approval

## Evidence

- Evidence path: GitHub Actions logs, `artifacts/verification/`, `docs/engineering/ci-runbook.md`, `docs/engineering/production-verification-cli-stack.md`, and DTP evidence receipts
- Latest receipt: see `practice-os/efficiency/fitness-app-evidence-index.md`
- Proof eligibility: internal reference and future public proof candidate only after proof/redaction gates pass
- Redaction rule: never publish raw scanner logs with sensitive paths, production data, user records, billing records, private app-store details, unapproved screenshots, credentials, or env values

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `gh pr view`, `gh run list`, `npm run tools:doctor`, `npm run tools:matrix`
- Safe write commands: docs/tests/source changes only when the Omnexus lane is explicitly active
- Commands that need explicit approval: production Supabase mutations, Stripe/App Store changes, Vercel env changes, release publication, proof publication, and any action involving real user/billing data
- Dependency maintenance: use the verification cockpit and release gates before dependency/security changes merge
- Toolchain pinning: Node, npm packages, Supabase CLI expectations, Docker images, and scanner images should stay explicit through repo-local lock/config files

## Next Touch

- Lane: verification cockpit reference, app-release evidence, and proof candidate extraction
- Trigger: verification cockpit pattern changes, release readiness work, app-store proof, public proof request, or a recurring Omnexus support/release failure
- Blocker: public proof remains blocked until evidence, permission, redaction, reviewer, and caveat are real
- Next action: keep DTP pattern extraction current without mutating Omnexus code unless the Omnexus lane is explicitly reopened
