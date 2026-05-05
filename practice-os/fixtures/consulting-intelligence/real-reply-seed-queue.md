---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Real Reply Seed Queue

Status: waiting for the next substantive client or owner reply.

Purpose: capture how real Cam, Greg, CCAAP, or weekly Business Brain replies
should become redacted eval cases without copying private raw material into the
fixture set.

## Trigger

Create a seed when a real reply exposes one of these behaviors:

- diagnosis changed after new owner context;
- proof permission, refusal, or redaction decision was needed;
- scope needed to stay narrower than the user's first ask;
- an owner action became a build blocker;
- a reply required private-kit-first updates before Notion, calendar, or repo
  changes;
- an agent answer was too generic, too shallow, or too confident.

## Seed Shape

| Field | Content |
|---|---|
| Lane | Cam, Greg, CCAAP, Toni weekly reset, or other approved lane |
| Sanitized input | one-paragraph abstraction, no raw private text |
| Expected routing | DTP artifact, private kit, Notion mirror, calendar, repo work, or hold |
| Expected behavior | what the assistant should do |
| Refusal or caution | what the assistant must not do |
| Proof posture | internal only, needs permission, needs redaction, or public-safe |
| Evaluation focus | diagnosis, scope, proof safety, follow-up, handoff, operator voice, or memory correction |

## Current Queue

| Lane | Waiting for | Seed target |
|---|---|---|
| CCAAP | Leah/Tony owner inputs and review response | owner-action extraction and proof-permission routing |
| Greg | next discovery/case-study reply | case-study permission, public-claim boundaries, and follow-up quality |
| Cameron | next marketplace/workflow reply | COI-aware sales support, scope shaping, and private-kit-first updates |
| Toni weekly reset | next broad Business Brain cycle | memory promotion, proof queue triage, and value-ledger quality |

## Promotion Rule

After a real reply arrives, create a small sanitized case in
`eval-cases.md` and `eval-cases.json` only if it would improve future behavior.
Use `practice-os/templates/client-reply-intake.md`,
`practice-os/templates/correction-checklist-for-toni.md`, and proof/redaction
templates before any public movement.

