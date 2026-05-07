---
created: '2026-05-06T14:20:00Z'
data_class: P0
confidential: false
permission_level: internal_only
review_status: recorded
---

# Operator Review State Update - 2026-05-06

Status: recorded.

2026-05-07 supersession note: Toni's later App Store Connect check narrowed the
Omnexus gate. Monthly and annual subscriptions plus the subscription group
localization are now operator-reported as `Approved`; approved subscriptions do
not need app-version attachment. The current gate is App Store Connect
candidate build/version proof for `1.0.1` plus normal metadata, screenshot,
privacy-label, review-note, reviewer-credential, and final smoke evidence.

2026-05-07 subscription-working note: Toni later confirmed the
products/subscription issue is fixed and the app now works with subscriptions.
Treat product approval, product loading, purchase, and in-app subscription state
as fixed by operator confirmation unless fresh Apple or device evidence
contradicts it. The current gate is release/live proof, not subscription repair.

## Source

Toni reported the final manual updates after the 48-hour operator checkpoint:

- Omnexus PR #562 was merged.
- Monthly and annual Omnexus subscription products were `Waiting for Review`
  when submitted.
- App version `1.0.1` was submitted for App Review with those subscriptions.
- App version `1.0.1` was approved and is now `Pending Developer Release` per
  Toni's later 2026-05-06 update.
- Monthly and annual Omnexus subscription products were later operator-reported
  as `Approved` in App Store Connect, along with the subscription group
  localization. No App Store Connect screenshots or private transaction proof
  are stored in this repo.
- DeMario exact public social post URLs were provided for LinkedIn and
  Instagram.

## Omnexus

| Item | Current state |
|---|---|
| PR #562 | merged on 2026-05-06 |
| Merge commit | `0b971aa515bca3f611f7a1c54096479284e2899e` |
| App version | `1.0.1` approved; `Pending Developer Release` per Toni |
| Monthly subscription | `Approved` per operator-reported App Store Connect check |
| Annual subscription | `Approved` per operator-reported App Store Connect check |
| In-app subscription path | working per Toni's 2026-05-07 operator confirmation |
| Current posture | verify selected App Store Connect candidate build/version is `1.0.1`, then complete release/live-proof gates |

Boundary:

- Re-open App Store Connect before any submission or developer release and
  confirm the selected candidate build/version is `1.0.1`.
- Do not make IAP code changes or replacement subscription products unless
  Apple returns exact reviewer/status evidence requiring a runtime or product-ID
  fix.
- Do not treat app-version attachment, product approval, product loading,
  purchase, or in-app subscription state as the current blocker while the
  subscription path is operator-confirmed working.
- Run final smoke, provider/data, observability, first-availability, and
  status-only release proof before calling the release clean.
- If Apple rejects, capture the exact product status and reviewer message
  privately before deciding whether the fix is metadata, App Store Connect
  attachment, or code.
- Keep App Store Connect screenshots, transaction IDs, receipts, private account
  data, and dashboard proof outside git.

Apple-doc basis checked on 2026-05-06:

- First In-App Purchases/subscriptions must be submitted with a new app version.
- `Waiting for Review` means the In-App Purchase was submitted to Apple and is
  not yet approved.
- `Approved` means Apple has approved the In-App Purchase to go live with its
  associated app.
- `Pending Developer Release` means the approved app version can be manually
  released, but this DTP posture holds release until the subscription products
  also approve or Apple confirms otherwise.

## DeMario Public Post URLs

Canonical public URLs recorded without tracking query parameters:

- LinkedIn:
  `https://www.linkedin.com/posts/toni-montez_vibecoding-ai-share-7457778664995434496-_YWO`
- Instagram:
  `https://www.instagram.com/reel/DX_7B34AKFK/`

Boundary:

- These URLs confirm public posting only.
- They do not add metrics, testimonials, private screenshots, student/admin
  data, booking/payment records, or business-impact claims.

## Where This Leaves The Queue

- Omnexus has moved from "approved subscriptions, verify the `1.0.1` candidate
  build/version" to "subscriptions work in-app; finish release/live-proof
  gates."
- DeMario URL capture is complete for durable public-link proof.
- Consulting live intake remains passed with notes; human visual/taste review
  and optional Hub intake archive/delete path remain.
- Client lanes remain prep/waiting: Greg discovery, Cam item-packet gate, and
  CCAAP owner-input gate.
- Architected Strength P0/P1 can be the next build lane once Toni is ready to
  start a clean focused branch.
