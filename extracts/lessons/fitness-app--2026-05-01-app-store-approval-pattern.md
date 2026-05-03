---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Lesson: Omnexus App Store Approval Pattern

## Source

- Repo: `fitness-app` / Omnexus
- Engagement/project: Omnexus iOS App Store launch
- Session or evidence link: Omnexus repo docs: `docs/HOW_OMNEXUS_WORKS.md`, `docs/store-metadata/app-store-approval-closeout-2026-05-01.md`, `docs/audit/post-approval-zero-defect-audit-2026-05-01.md`
- Date: 2026-05-01
- Reviewer: Codex

## What Happened

Toni reported that Omnexus was approved by iOS App Review on 2026-05-01 and expected to be available in the App Store on Saturday, 2026-05-02. The Omnexus repo already contains a documented launch and review journey, including the master narrative, approval closeout, submission evidence tracker, App Review notes, TestFlight smoke script, submission linter, release guide, and post-approval audit.

## What Worked

- The launch trail was preserved in the repo instead of only in chat.
- Review concerns were converted into narrow repair stories and evidence artifacts.
- Reviewer-visible trust was treated as a product requirement: IAP, auth callbacks, account deletion/export, privacy language, HealthKit wording, and review notes had to match app behavior.
- The verification cockpit gave Omnexus a stronger proof layer than a single build command.
- The approval closeout explicitly separated historical tracker rows from current post-approval gates.

## What Failed Or Slowed Us Down

- The review journey still depends on sensitive evidence that cannot live in git: reviewer credentials, App Store Connect screenshots, private crash logs, provider dashboards, and device proof.
- Old pre-approval tracker rows can look like current blockers unless a closeout note explains the transition.
- Public proof could overclaim if approval, public install, first-user trust, and business traction are not separated.
- Future client apps would repeat this work unless DTP captures the pattern as a reusable launch packet.

## Reusable Lesson

App Store approval is a product truth test. For future mobile client builds, the practice should plan review readiness as a system: shipped scope, reviewer-visible trust, native device proof, store metadata, billing/IAP state, account lifecycle, privacy language, rejection-to-story repair, evidence artifacts, approval closeout, and first 72-hour support.

## Proposed Change

- Skill update: no immediate `tm-skills` change; consider adding mobile launch review triggers to `delivery-baseline` after one more client-app use.
- Checklist update: add a reusable mobile app review journey template and pattern.
- Eval fixture: not yet; seed an eval only after an agent mishandles mobile launch/review advice.
- Roadmap/doc update: add the Omnexus approval pattern to DTP roadmap, documentation map, evidence index, and Future Intelligence lane.
- CI/gate update: no new DTP CI gate; future mobile repos can adopt submission lint and evidence cockpit patterns when their stack justifies it.
- No change: do not mutate Omnexus while its lane is not explicitly active.

## Approval

- Owner: Toni
- Status: proposed
- Follow-up: use this pattern for future client mobile app launch planning and keep Omnexus public proof behind proof/redaction gates.

## Redaction Notes

Do not include reviewer credentials, App Store Connect private screenshots, one-time codes, private crash logs, production user data, billing records, health data, support inbox content, secrets, or unsupported public claims.
