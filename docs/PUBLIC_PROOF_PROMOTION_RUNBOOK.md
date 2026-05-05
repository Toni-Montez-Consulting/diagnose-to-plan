# Public Proof Promotion Runbook

Status: active proof-governance runbook.

Owner: `diagnose-to-plan`

Purpose: define the required path for any private evidence, project artifact, screenshot, metric, claim, case study, public page, or offer proof before it appears in the public consulting repo or other public surface.

This runbook reuses existing Practice OS templates. It does not create a parallel proof system.

## Source Templates

Use these existing templates in this order:

1. `practice-os/templates/asset-inventory.md`
2. `practice-os/templates/evidence-source-checklist.md`
3. `practice-os/templates/permission-reviewer-checklist.md`
4. `practice-os/templates/redaction-queue-item.md`
5. `practice-os/templates/proof-packet.md`
6. `practice-os/templates/public-claim-review.md`
7. `practice-os/templates/copy-authenticity-audit.md`

Optional supporting templates:

- `practice-os/templates/verification-evidence.md`
- `practice-os/templates/value-ledger.md`
- `practice-os/templates/client-reply-intake.md`
- `practice-os/templates/recurring-engagement-cadence.md`
- `practice-os/templates/mobile-app-review-journey.md`
- `practice-os/templates/client-command-room-fit-assessment.md`

## Promotion Path

Public proof must move through this path:

```text
proof candidate queue
-> private evidence
-> asset inventory
-> evidence source review
-> permission review
-> redaction queue
-> proof packet
-> public claim review
-> copy authenticity audit
-> consulting copy/assets
```

If any step fails, the proof remains private, internal-only, or parked.

Use `docs/PRACTICE_PROOF_QUEUE_INDEX.md` to decide which candidate is active
before starting the path.

## Minimum Required Fields

No public proof moves forward without:

- source owner;
- source path or evidence pointer;
- baseline or before-state;
- after-state;
- measurement caveat;
- permission level;
- redaction status;
- reviewer;
- approved public wording;
- rejected wording or blocked claims;
- public surface target;
- next review date or stale-after date.

## Statuses

Use these statuses consistently:

| Status | Meaning | Public movement allowed? |
|---|---|---|
| `captured` | source exists, not reviewed | No |
| `needs_evidence` | claim lacks source/baseline/after-state | No |
| `needs_permission` | source owner/client/platform permission missing | No |
| `needs_redaction` | source may be useful but is not public-safe | No |
| `review_ready` | source, caveat, permission, and redaction are prepared | No, reviewer still required |
| `approved_public_safe` | reviewer approved exact use and wording | Yes, only for the approved scope |
| `restricted_internal` | useful internally but not public | No |
| `parked` | valuable idea but wrong time or insufficient proof | No |
| `rejected` | should not be used | No |

## Hard Stops

Stop immediately and route to DTP review when proof involves:

- `dse-content`, Microsoft-adjacent work, MSX, Dataverse, WorkIQ, internal systems, employer context, or COI risk;
- client material without written permission;
- family/private projects without explicit purpose and permission;
- screenshots containing private data, names, emails, account IDs, calendar details, payment details, health data, admin rows, or raw logs;
- metrics without baseline, after-state, date range, and caveat;
- app-store, billing, auth, subscription, account deletion, health, or user-data claims;
- Hub runtime rows, prompts, webhook records, or console screenshots;
- AI/automation claims that imply autonomy, private retrieval, client communication, or production writes beyond what is actually implemented;
- public copy that sounds generic, inflated, or unsupported by source material.

## Lane-Specific Rules

| Lane | Public proof posture | Required before public use |
|---|---|---|
| Consulting site | Can publish only reviewed proof and public-safe offer language | proof packet, claim review, copy audit |
| CCAAP | Public site implementation may become proof later | owner approval, no private records, screenshot/content permission |
| Greg | High-leverage proof candidate if permission arrives | written permission, claim boundaries, source review |
| Cameron | Private engagement by default | permission, redaction, client-safe claims, no sensitive transaction details |
| Omnexus | Strong product proof candidate | source review, app/privacy/billing caveats, no private dashboard data |
| DeMario | Command-room and launch reference candidate | owner permission, booking/admin data redaction, plain-language caveats |
| Architected Strength | Personal brand proof lab | no employer/client confidential material, source-backed claims |
| FamilyTrips | Not public proof by default | explicit purpose, no sensitive trip details, privacy caveat |
| DSE | Hold | COI, permission, redaction, reviewer, and public/professional boundary decision |
| Hub | Runtime-support evidence only | no private rows/secrets; use DTP evidence fields |

## Approved Output Types

Public proof may become:

- a short receipt-style case study;
- a redacted screenshot or asset;
- a metric card with caveat;
- a public-safe system map;
- a before/after note;
- a launch or review journey summary;
- an offer proof bullet;
- a public-safe runbook excerpt.

Public proof should not become:

- raw client files;
- private dashboards;
- unredacted screenshots;
- internal workflow dumps;
- unsupported impact claims;
- generic "AI transformation" copy;
- proof that implies client approval when only internal work exists.

## Review Checklist

Before anything moves into `consulting`:

- [ ] Asset inventory exists.
- [ ] Evidence-source checklist exists.
- [ ] Permission/reviewer checklist exists.
- [ ] Redaction queue item exists if needed.
- [ ] Proof packet exists.
- [ ] Public claim review approves exact language.
- [ ] Copy authenticity audit passes.
- [ ] DSE/COI/client/family/internal hard stops were checked.
- [ ] The public target is named.
- [ ] The proof can be removed or revised if permission changes.

## Failure Modes

| Failure | Response |
|---|---|
| Strong story but no permission | keep as internal learning and ask for permission separately |
| Great screenshot but private details | redact or use a recreated public-safe diagram |
| Metric sounds impressive but has no baseline | do not publish metric; use qualitative caveated language only if sourced |
| Client likes work but has not approved proof | do not imply endorsement |
| DSE work looks compelling | hold at boundary-level until COI and permission are explicit |
| Hub proof requires private rows | use architecture/runtime summary, not row screenshots |

## Relationship To Offers

Offer copy can mention capabilities before proof is fully public, but it must not claim outcomes, approvals, client wins, or product maturity beyond the reviewed proof.

Use `docs/OFFER_LED_PRACTICE_PACKAGING.md` to decide which proof would strengthen an offer. Use this runbook to decide whether that proof can be public.
