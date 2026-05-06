---
created: '2026-05-06T13:49:49Z'
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Consulting Live Intake Receipt

## Receipt Metadata

- Date: 2026-05-06
- Operator: Codex for Toni
- Public surface: `https://tonimontez.co/start`
- Runtime owner: Hub on `https://onhand.dev`
- Consulting commit: current production deployment, source behavior unchanged in
  this smoke
- Hub commit: current production deployment, source behavior unchanged in this
  smoke
- Environment: production public intake to production Hub runtime
- Test record label: `DTP live intake smoke 20260506T134949Z`

## Preflight

- [x] Public form renders the expected Hub endpoint path.
- [x] Hub `/health` was already verified reachable in the active queue receipt.
- [x] CORS accepts the public origin `https://tonimontez.co`.
- [x] Test record uses synthetic, clearly disposable content.
- [x] No real client/private data was submitted.

## Submission

- Submitted at: 2026-05-06T13:49:49Z
- Browser or command used: CLI POST with synthetic JSON payload
- Public route: `https://tonimontez.co/start`
- Endpoint path: `https://onhand.dev/api/intake`
- Response status: HTTP 201 JSON response with `ok: true`
- User-visible result: not browser-verified in this smoke; endpoint response
  confirms successful intake creation

## Hub Verification

Do not paste the full private row.

- Verified at: 2026-05-06T13:49:49Z
- Verified by: Hub private dashboard API with operator token
- Row/table pointer: `supabase.intake_submissions`, row id suffix `934db178`
- Expected field summary: synthetic smoke-test name, redacted synthetic test
  email marker, source `tonimontez.co-smoke`, and project label
  `DTP live intake smoke 20260506T134949Z`
- Storage result: row found with status `new`
- Any unexpected field: none observed from the summarized row fields
- Screenshot or log path, if redacted: none captured

## Cleanup

- [x] Test row is clearly labeled as disposable test data.
- Cleanup action: no delete/archive endpoint exists for intake submissions in
  the current Hub console API; residual row remains clearly test-labeled.
- Cleanup verified at: 2026-05-06T13:49:49Z
- Residual record, if any: one synthetic test row remains in
  `supabase.intake_submissions` with the smoke-test label.

## Result

- Status: `passed_with_notes`
- What this proves: the live consulting intake endpoint accepts an allowed
  `tonimontez.co` submission and stores it in the private Hub intake table.
- What this does not prove: public proof, conversion quality, real lead fit,
  private row screenshots, full browser form UX, or cleanup automation.
- Follow-up: add or use an intake archive/delete path before treating cleanup
  as fully automated; run a human desktop/mobile taste pass before broader site
  sharing.

## Proof Boundary

- This receipt supports private operational confidence.
- This receipt does not authorize public screenshots, private row excerpts, Hub
  console captures, or proof claims without the proof promotion runbook.
