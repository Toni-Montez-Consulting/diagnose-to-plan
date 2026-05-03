---
data_class: P0
confidential: false
permission_level: internal_only
review_status: checked
---

# Hosted DTP Phase 0.2 Governance

## Trigger

After the live smoke passed against the dedicated `DTP Private` Supabase
project, Toni asked to keep building the operational/application/systems
infrastructure without widening into FAOS, autonomous agents, public proof,
Stripe, or client portals.

## Accepted Governance

- Real operator account: non-smoke private records should be owned by Toni's
  real operator account.
- Smoke accounts: keep the two smoke operator accounts as tagged regression
  fixtures.
- Smoke records: retain them for RLS regression unless they become noisy.
- Deployment posture: local private app plus live Supabase for now; no public
  deploy.
- Backup/export: do not make Hosted DTP the only copy of a non-smoke private
  engagement until markdown fallback/export is verified for that lane.

## Operating Meaning

Hosted DTP is now allowed to participate in private operating loops as a
record surface. It is not allowed to replace DTP markdown, private kits, steward
receipts, or decision records as the audit trail.

The next implementation slice should prove a live import/export round trip
from a sanitized DTP artifact before storing client-sensitive, non-smoke
records.

## No-Touch Boundaries

- No FAOS repo, services, wrapper, orchestration runtime, or agent substrate.
- No autonomous record mutation, email sending, public proof publishing, or
  client-facing portal.
- No QuickBooks, Stripe, deep Hub sync, or Notion source-of-truth behavior.
- No reuse of Omnexus, Consulting, FamilyTrips, or Mario Supabase projects for
  the DTP brain.
