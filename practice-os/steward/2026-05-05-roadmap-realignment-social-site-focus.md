# Roadmap Realignment: Social Proof And Site-Fix Focus

Date: 2026-05-05  
Owner: Toni with Codex  
Status: roadmap/steward receipt, not public proof

## Trigger

Toni reported that DeMario's pickleball site is live and receiving strong
feedback. Omnexus is approved on the App Store, but the subscription products
were declined/not approved. Toni also wants to fix the consulting site and
finish/fix Architected Strength while keeping the broader roadmap straight.

## Live Intake Snapshot

Checked before editing this receipt:

- `consulting`: clean on `main...origin/main`.
- `diagnose-to-plan`: clean on `main...origin/main`.
- `architected-strength`: clean on `main...origin/main`.
- `fitness-app`: clean on `main...origin/main`.
- `demario-pickleball-1`: clean on `master...origin/master`.

## Decision

The next practical queue is:

1. DeMario launch-feedback social/proof packet.
2. Omnexus subscription-review resubmission.
3. Consulting public-site fix/readiness pass.
4. Architected Strength P0/P1 finish/fix pass.

This is a priority realignment, not approval to publish proof, post on social,
ship broad redesign, launch assistants, or rewrite Omnexus billing code before
the App Store Connect status/reviewer message is inspected.

## DeMario Social/Proof Packet

Goal: turn the strong live feedback into a clean LinkedIn/social package.

Required before posting:

- Mario-approved wording.
- Source/testimonial evidence for the feedback.
- Screenshot approval and redaction.
- Launch context and caveat.
- Reviewer check.
- Final channel-specific drafts for LinkedIn and any other social channel.
- Human posting by Toni or Mario, not automated posting.

Do not include private admin data, booking details, payment details, raw client
messages, or unsupported outcome claims.

## Omnexus Subscription Review

Goal: move the approved app into a subscription-approved state without
overcorrecting the codebase.

Current Apple-docs read:

- First In-App Purchases/subscriptions must be submitted with a new app
  version.
- If multiple products relate to that version, submit them together.
- Rejected IAP/subscription products may require either a new product or
  Developer Action Needed changes depending on the exact status.

Required next step:

- Inspect the exact App Store Connect subscription statuses and reviewer
  message.
- Verify metadata, localization, screenshot, pricing, availability, tax
  category, product IDs, subscription group, and review notes.
- If these are the first subscriptions, prepare a new app version/build and
  attach all subscription products to that version's In-App Purchases and
  Subscriptions section before submitting.
- Change code only if the reviewer message or device proof shows product load,
  purchase, restore, entitlement, or copy behavior is wrong.

## Consulting Site Fix Pass

Goal: make the current public consulting site feel ready and trustworthy.

Scope:

- Preserve Steel Ledger.
- Verify Hub-first intake and fallback posture.
- Run route/build checks and manual desktop/mobile visual QA.
- Tighten proof posture without adding uncleared public claims.
- Keep `/admin` as launcher/status only.

Non-goals:

- Broad redesign.
- Public proof replacement without DTP gates.
- Public assistant runtime or widget.
- Hub-as-CRM or DTP replacement.

## Architected Strength Finish/Fix Pass

Goal: finish the personal-brand/public-signal site lane on its own terms.

Scope:

- P0/P1 public-signal polish.
- Claim hygiene and source posture.
- Positioning clarity.
- Content/craft pass.
- Repo-local validation.

Non-goals:

- Migrating it into consulting.
- Employer, client, or private workspace proof.
- Live assistant widget.
- Notion automation or public posting automation.

## Backlog And Queue Updates

Updated:

- `practice-os/kaizen/intake.jsonl`
- `docs/ROADMAP_EXECUTION_BACKLOG.md`
- `docs/PRACTICE_PROOF_QUEUE_INDEX.md`
- `docs/PRACTICE_ROADMAP_HORIZONS_2026.md`
- `docs/WORKSPACE_ROADMAP_AND_PLANNING_REPORT_2026-05-05.md`
- `practice-os/steward/2026-05-05-weekly-operator-cockpit.md`
- `docs/integration/reprioritization_log.md`

## Next Action

Start with the viewable dashboard and Omnexus subscription-review checklist,
then use the dashboard to keep DeMario, consulting, and Architected Strength in
the right order. DeMario remains the cleanest social/proof win, but it must
stay permissioned and caveated before public posting.
