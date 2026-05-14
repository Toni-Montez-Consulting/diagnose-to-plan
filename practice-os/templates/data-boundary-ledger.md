---
data_class: P0
confidential: false
permission_level: internal_only
review_status: template
---

# Data Boundary Ledger

Use this when a lane touches Supabase, Postgres, storage, auth, private records,
client data, proof assets, admin dashboards, or service-role operations.

## Ledger Metadata

- Repo/lane:
- Created:
- Owner:
- Reviewer:
- Data class: P0 | P1 | P2 | P3
- Status: draft | current | stale | archived

## Data Inventory

| Data object | Source of truth | Contains private data | Exposed surface | Owner |
|---|---|---|---|---|
|  |  | yes/no |  |  |

## Access Boundary

- Auth model:
- RLS or policy model:
- Route/API protection:
- Admin/service-role operations:
- Browser-safe credentials:
- Credentials or secrets printed in docs: no

## Public Surface Boundary

- Safe to show:
- Must redact:
- Never public:
- Needs permission:
- Needs reviewer:

## Migration And Change Control

- Migration path:
- Local reset/test path:
- Production change path:
- Rollback/repair path:
- Drift check:

## Verification

- RLS/auth checks:
- API checks:
- Data-write checks:
- Delete/archive checks:
- Skipped checks and reason:

## Handoff

- Client or operator owner:
- Account/billing owner:
- Common failure modes:
- Recovery notes:
- Future maintainer notes:

