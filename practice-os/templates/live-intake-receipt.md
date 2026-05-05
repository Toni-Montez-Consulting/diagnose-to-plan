---
template: live-intake-receipt
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Live Intake Receipt

Use this template after a human-approved live intake smoke. It records evidence
that a public form submission reached the private Hub intake path and was
cleaned up without exposing secrets or private row data.

## Receipt Metadata

- Date:
- Operator:
- Public surface:
- Runtime owner:
- Consulting commit:
- Hub commit:
- Environment:
- Test record label:

## Preflight

- [ ] `consulting` build or latest deployment is known.
- [ ] Public form renders the expected endpoint path.
- [ ] Hub `/health` is reachable.
- [ ] CORS allows the public origin.
- [ ] Test record uses synthetic, clearly disposable content.
- [ ] No real client/private data will be submitted.

## Submission

- Submitted at:
- Browser or command used:
- Public route:
- Endpoint path:
- Response status:
- User-visible result:

## Hub Verification

Do not paste the full private row.

- Verified at:
- Verified by:
- Row/table pointer:
- Expected field summary:
- Storage result:
- Any unexpected field:
- Screenshot or log path, if redacted:

## Cleanup

- [ ] Test row archived, deleted, or clearly labeled as test data.
- Cleanup action:
- Cleanup verified at:
- Residual record, if any:

## Result

- Status: `passed`, `passed_with_notes`, `failed`, or `blocked`
- What this proves:
- What this does not prove:
- Follow-up:

## Proof Boundary

- This receipt may support private operational confidence.
- This receipt does not authorize public screenshots, private row excerpts, Hub
  console captures, or proof claims without the proof promotion runbook.

