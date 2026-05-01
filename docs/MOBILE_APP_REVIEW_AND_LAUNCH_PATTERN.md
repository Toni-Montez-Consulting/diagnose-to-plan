---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Mobile App Review And Launch Pattern

Status: reusable Practice OS pattern seeded from the Omnexus App Store approval journey. This is not a public proof claim until the proof packet, permission, redaction, reviewer, evidence, and caveat gates pass.

Owner: `diagnose-to-plan`

Purpose: turn the Omnexus iOS approval journey into a reusable client-app build and launch pattern so future mobile projects do not rediscover the same App Store, native, billing, privacy, and evidence lessons from scratch.

## Source Pattern

The current reference implementation is `fitness-app` / Omnexus.

Observed source receipts:

- `fitness-app/docs/HOW_OMNEXUS_WORKS.md`
- `fitness-app/docs/store-metadata/app-store-approval-closeout-2026-05-01.md`
- `fitness-app/docs/audit/post-approval-zero-defect-audit-2026-05-01.md`
- `fitness-app/docs/LAUNCH-GUIDE.md`
- `fitness-app/docs/store-metadata/ios-submission-evidence-tracker.md`
- `fitness-app/docs/store-metadata/app-review-notes-package.md`
- `fitness-app/docs/store-metadata/testflight-smoke-script.md`
- `fitness-app/docs/store-metadata/submission-rules.yml`
- `fitness-app/docs/ops/submission-lint.md`
- `fitness-app/docs/engineering/release-day.md`
- `fitness-app/docs/roadmap/r1-story-e1-s5-app-store-review-repair.md`

Current milestone captured from Toni on 2026-05-01:

- Omnexus App Review was approved.
- App Store availability was expected for Saturday, 2026-05-02.
- The public listing/install proof, live-device smoke, IAP purchase/restore proof, provider dashboards, and observability review remain manual evidence gates once the public listing is available.

## Core Lesson

App Store approval is not a distribution checkbox. It is a product truth test.

Apple review forced Omnexus to prove that subscriptions, auth, privacy language, account deletion/export, native callbacks, HealthKit wording, IAP state, reviewer notes, and actual device behavior matched what the app claimed.

The reusable pattern is:

1. Define the shipped product truth.
2. Make high-risk behavior reviewer-visible and source-backed.
3. Prove native behavior on devices before submission pressure peaks.
4. Convert every review issue into a narrow repair story.
5. Preserve the evidence trail.
6. After approval, switch from submission triage to first-user trust.

## Pattern Stages

### 1. Scope Truth

Before submission, make the app's shipped truth explicit.

Required artifacts:

- V1 scope or shipped feature contract.
- User-flow map for onboarding, core usage, billing, support, account deletion, and data export.
- Native platform matrix for iOS, Android, web/PWA, and any expected differences.
- Risk inventory for auth, billing, entitlements, privacy, AI, health/fitness claims, notifications, and support.
- "Not shipping yet" list so the app does not keep expanding during review hardening.

Done gate:

- A reviewer, founder, and future agent can tell what the app actually does without reconstructing it from code.

### 2. Reviewer-Visible Trust

App review follows the app as a user, not as an engineer reading internal intent.

Required artifacts:

- App Store metadata, privacy labels, screenshots, support URL, marketing URL, and review notes.
- Demo account and review instructions stored outside git.
- Subscription and IAP explanations visible inside the app.
- Account deletion and export surfaces visible and tested.
- Auth callback paths tested for native flows.
- Medical, fitness, health, privacy, and tracking language reviewed for what the app actually does.

Done gate:

- A literal reviewer can follow the notes, find Premium/IAP surfaces, delete/export the account, and understand privacy behavior without private context.

### 3. Native Reality Early

Native behavior should not first become real during the final submission week.

Required artifacts:

- TestFlight or equivalent device smoke script.
- Signing, entitlements, provisioning, callback URL, APNs, HealthKit, camera/photo, and deep-link checks.
- Screenshots generated from current app behavior.
- Build upload evidence.
- Device-specific notes for iPhone and iPad if the app supports both.

Done gate:

- The team has current device evidence for the reviewer-critical flows, not only web or local-browser evidence.

### 4. Evidence Cockpit

A serious mobile app needs evidence beyond "it builds".

Required artifacts:

- Local gate: lint, typecheck, unit, build, route/E2E where available.
- Release gate: preview/prod verification, native build proof, security scan, dependency review, and runtime smoke.
- Data gate: database schema contracts, migration drift checks, RLS checks, or equivalent for the stack.
- Store gate: metadata, privacy labels, screenshot, IAP/product, review-note, and submission-lint checks.
- Evidence writer: markdown/JSON summaries that can be reviewed without relying on chat memory.

Done gate:

- Hard failures block release; advisory failures are surfaced, not hidden.

### 5. Rejection-To-Story Loop

When review feedback arrives, avoid broad churn.

For each rejection or reviewer concern, create:

- concise issue statement;
- affected reviewer flow;
- source artifact or screenshot reference;
- narrow repair story;
- acceptance criteria;
- verification command or manual smoke;
- review-note update if the reviewer needs new instructions;
- future lint/checklist update if the issue can be prevented.

Done gate:

- The fix changes the smallest surface that resolves the reviewer-visible mismatch and leaves a durable receipt.

### 6. Approval Closeout

Approval should close the review arc without erasing the history.

Required artifacts:

- Approval closeout note with date, source of approval report, repo state, and sensitive evidence exclusions.
- Index of primary receipts.
- Warning that old tracker rows may be historical evidence prompts, not current blockers.
- First 72-hour launch checklist.

Done gate:

- A future agent knows the difference between pre-approval blockers, historical review scars, and current post-approval gates.

### 7. First 72 Hours

After approval, the operating mode changes from "prove it to Apple" to "protect first-user trust".

Required checks:

- Public listing/install once available.
- Real-device signup/sign-in/onboarding.
- Subscription screen, purchase/restore path, and entitlement state.
- Core app loop.
- Account deletion/export and support routes.
- Crash/error monitoring.
- Provider dashboards: auth, billing, webhooks, app-store server notifications, analytics.
- Triage path for real user-impacting issues.

Done gate:

- Public install and first-user paths are verified from live surfaces, and issues go to the active backlog rather than stale submission trackers.

## Client Deliverables

For a future client mobile app, the reusable package should include:

- mobile app review journey record from `practice-os/templates/mobile-app-review-journey.md`;
- launch guide;
- store metadata and review-note packet;
- device smoke script;
- submission/evidence tracker;
- privacy and account lifecycle checklist;
- IAP/billing entitlement checklist if monetized;
- rejection response log if review feedback arrives;
- approval closeout;
- first 72-hour launch checklist;
- client handoff and support runbook;
- proof packet only after public-proof gates pass.

## Public And Private Boundaries

Never store in git:

- review credentials;
- one-time codes;
- private App Store Connect screenshots;
- private crash logs with identifiers;
- production user records;
- payment or entitlement records;
- health data;
- support inbox content;
- API keys, webhook secrets, or dashboard tokens.

Public proof may show:

- the method;
- redacted trace of the launch/review system;
- before/after process improvements;
- approved screenshots;
- aggregate verification evidence;
- caveated launch timeline;
- client-safe lessons.

Public proof must not imply:

- official Apple endorsement beyond the app being approved;
- official Microsoft involvement;
- unsupported business metrics;
- private user, reviewer, customer, or client details;
- that a reusable checklist guarantees approval.

## Next Practice Upgrades

The pattern is useful now as docs and templates. Later upgrades should be added only when a future client or Omnexus follow-up proves the need:

1. A redacted App Review response example library.
2. A generic `submission-lint` starter for mobile projects.
3. A client launch evidence ledger that maps commands, screenshots, and dashboard checks.
4. A mobile app release proof packet format for consulting.
5. An authenticated admin assistant source manifest that can read launch packets without exposing private reviewer or customer data.

## Use This When

- a client app is approaching TestFlight, App Store, Google Play, or public launch;
- a rejection arrives and needs to become a narrow repair story;
- a founder asks whether the app is launch-ready;
- proof needs to distinguish approval, public install, first-user trust, and business traction;
- a future agent needs to learn from Omnexus without mutating the Omnexus repo.

## Do Not Use This To

- publish Omnexus proof without a proof packet;
- mutate `fitness-app` while its lane is not active;
- store review credentials or private dashboard evidence;
- replace platform-specific docs for Apple or Google;
- skip live device and provider checks.
