---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Kaizen Existing-System Map

Date: 2026-05-04

Steward: Codex

Purpose: organize the current DTP-owned operating reality after the Kaizen
stabilization pass without creating a second roadmap.

## Source Truth

- DTP remains canonical for roadmap, steward receipts, proof governance, repo
  manifests, and private engagement routing.
- `practice-os/kaizen/intake.jsonl` is now the lightweight index for meaningful
  active/waiting/blocker items.
- Private client and COI raw text must not be committed. Committed Kaizen rows
  use redacted stubs; raw local captures go only to ignored `.dtp/kaizen/` state.
- Notion remains a sanitized mirror and inbox, not the source of truth.

## Now

| Kaizen ID | Lane | State | Next action | Boundary |
|---|---|---|---|---|
| `kzn-20260504-engagement-vault-durability-redacted` | engagement vault | now | review nested private vault state, commit coherent private-kit updates, and decide private remote before push | private-client; no public DTP details |

## Waiting On Human

| Kaizen ID | Lane | State | Next action | Boundary |
|---|---|---|---|---|
| `kzn-20260504-ccaap-owner-inputs-redacted` | CCAAP | waiting | wait for owner inputs before launch/proof movement | private-client; details stay in engagement vault |

## Waiting On Tool Or Env

| Lane | State | Next action | Boundary |
|---|---|---|---|
| Starter DMARC | waiting | add/verify after DKIM Admin verification is settled | Google Workspace admin; no repo mutation needed yet |
| Hosted DTP | waiting | use one more real operating loop with markdown fallback before normal private-record storage | no hosted client-sensitive workflow by default |

## Blocked Or Parked

| Kaizen ID | Lane | State | Next action | Boundary |
|---|---|---|---|---|
| `kzn-20260504-hub-pr68-tailwind-blocker` | Hub dependency PR #68 | blocked | keep parked until targeted Tailwind 4 migration/fix plan exists | Hub runtime support, not DTP/CRM |
| `kzn-20260504-dse-sensitive-triage-redacted` | DSE | blocked | do not touch without explicit COI-aware scope and live repo validation | COI-gated |
| none seeded | Omnexus Stripe alert | parked | reopen only when Toni selects the support lane | external dashboard/manual gate |
| none seeded | FAOS implementation | parked | separate local command/version verification pass before any repo/service creation | no orchestration substrate build |

## Public Surface Next

| Kaizen ID | Lane | State | Next action | Boundary |
|---|---|---|---|---|
| `kzn-20260504-consulting-share-readiness` | consulting | next | run manual visual QA and proof-maturity pass before redesigning public surface | public-safe only after proof gates |

## Proof Candidates

- CCAAP baseline/after-state evidence remains blocked until owner approval,
  authentic assets, and proof permission exist.
- Consulting proof should start from proof packets, not copy changes.
- Omnexus, DeMario, Architected Strength, DSE, and Hub material stays internal
  until evidence, permission, redaction, reviewer, and caveat gates pass.

## Repo-Health Lanes

- DTP: active source of truth; current work is uncommitted and should stay
  bundled deliberately with the Kaizen stabilization plus prior deep-audit docs.
- Consulting: next public proof/share-readiness lane; no redesign before proof
  and manual QA.
- Hub: runtime support; PR #68 is the current visible blocked dependency lane.
- `engagements`: private nested vault lane; commit/push only to approved private
  remote.
- DSE: COI-gated; do not inspect deeply or mutate without explicit scope.

## Operating Rule

Start broad sessions with:

```powershell
.\.venv\Scripts\python.exe -m dtp kaizen status --limit 5
.\.venv\Scripts\python.exe -m dtp workspace report
```

When a new item changes execution order, status, proof posture, repo health,
client state, or future operating behavior, capture or update it in Kaizen
before creating a larger artifact.
