---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
created: '2026-05-16T00:00:00Z'
---

# DTP Client Delivery Engine Audit - Steward Receipt

## Trigger

Toni corrected a delivery failure in the Greg and Cam follow-up loop. DTP had
useful meeting notes, private packets, action records, and Gmail draft ability,
but the process did not force one clear delivery surface. That let a cover
email drift away from the packet it was supposed to send.

## Findings

| Priority | Finding | Why It Matters | Correction |
|---|---|---|---|
| P0 | No hard note-to-deliverable-to-Gmail gate | Meeting notes could become internal artifacts without a clean recipient-facing packet attached to the email. | Meeting, receipt, reply-intake, workflow-spine, and bridge-queue templates now require relationship posture, packet path, Gmail draft id, attachment/source path, and send/hold status. |
| P0 | Relationship tone was not forced from meeting notes | Friend / early-collaborator follow-ups could sound like formal client recaps or premature paid scope. | Templates now capture relationship stage, tone to use/avoid, payment/scope posture, and what the email must not imply. |
| P0 | Source pack contradicted the intended Gmail draft default | External Communications still said Gmail draft receipts were only created on request. | Source pack now says Gmail drafts with attachments are the default for client/prospect/professional email drafting when recipient and source are safe. |
| P1 | Post-meeting receipts did not prove delivery state | A meeting could be marked operationally handled while the active spine, packet, Gmail receipt, or old draft status stayed stale. | Receipt and workflow-spine templates now include a Client Delivery Gate and Client Delivery Surface. |
| P1 | Private Greg/Cam operating records could drift after draft creation | Action extraction/source indexes could still imply no Gmail draft existed after one had been created. | Private records should be updated in the engagement vault alongside Gmail draft creation. |
| P2 | Packet format is still Markdown-first | This is fine for proof, but not always the most polished client attachment. | Keep Markdown for now; consider PDF/DOCX only after repeated real use shows it improves review. |

## What Already Worked

- Private engagement vaults kept client-specific detail out of tracked DTP.
- Meeting notes, source indexes, action extraction, active workflow spines, and
  steward receipts already existed.
- The External Communications Agent already held readability, summary,
  no-send, proof, and surface-translation standards.
- Gmail drafts can be created for Toni review while send approval stays human.
- Public proof, live systems, connectors, budgets, ad accounts, App Store
  actions, Hub, Notion, QuickBooks, and automation remained blocked.

## Corrections Implemented

- Added a durable memory correction for client emails, deliverables, tone, and
  meeting-note usage.
- Updated the consulting repo's durable agent instructions with the same rule.
- Updated DTP External Communications in the prior correction lane.
- Hardened DTP templates:
  - `practice-os/templates/client-os-meeting-notes.md`
  - `practice-os/templates/client-os-post-meeting-receipt.md`
  - `practice-os/templates/client-reply-intake.md`
  - `practice-os/templates/workflow-spine.md`
  - `practice-os/templates/client-os-bridge-queue.md`
- Updated `docs/CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md`.
- Updated `practice-os/research/source-packs/agent-source-packs.v0.json` so
  Gmail draft creation is not treated as exceptional when drafting external
  client/prospect/professional email.

## Client Delivery Gate

Before any future client/prospect/friend-collaborator follow-up is considered
ready for Toni review, confirm:

1. Relevant meeting notes/transcripts and reply records were read.
2. Relationship stage, tone, and payment/scope posture are explicit.
3. There is one recipient-friendly packet or a recorded reason none is needed.
4. The Gmail draft exists when email drafting is requested and connector support
   is available.
5. The Gmail draft includes the packet when the email references it.
6. The private kit records Gmail draft id, attachment/source path, old draft
   supersession, and send/hold status.
7. The signature is complete.
8. No public proof, live system, client-send, payment/scope, legal/IP, or
   automation movement is implied without Toni's explicit approval.

## Next Action

Use this gate on the next Greg, Cam, CCAAP, or owner-follow-up loop before
calling the draft ready. If the Markdown packet format feels clunky after two
more real sends, add a small PDF/DOCX attachment-format lane; do not build more
software for this problem yet.
