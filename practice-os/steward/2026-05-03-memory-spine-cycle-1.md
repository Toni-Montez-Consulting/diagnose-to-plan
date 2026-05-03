---
data_class: P0
confidential: false
permission_level: internal_only
review_status: checked
---

# Memory Spine Cycle 1

Date: 2026-05-03

Purpose: run the new Memory Spine as a real broad-session rehydration flow, not
only a doctor check.

## Source Sweep

| Source | Current read | Confidence |
|---|---|---:|
| DTP git state | `v2/harness` is ahead of origin and contains the Iteration 1 brain slice plus this cycle | high |
| Hub git state | `main` has the Supabase temp Prettier-ignore cleanup | high |
| `tm-skills` git state | `main` is ahead and has the misfire-to-DTP promotion note | high |
| DTP memory command | `dtp memory status` passes and finds recent memory/intelligence steward receipts | high |
| DTP workspace report | coverage exists for consulting, DTP, Hub, `tm-skills`, CCAAP, DeMario, Omnexus, DSE, FamilyTrips, and adjacent references | high |
| Saved Codex memory | useful for continuity, but not authoritative when live repo state is cheap to check | high |

## Active Lanes

| Lane | Current state | Next natural action | Gate |
|---|---|---|---|
| DTP brain infrastructure | Memory Spine V1, Hosted DTP Phase 0 scaffold, DSE coverage, kit scanner, and validation gates are implemented locally | package the slice, then move Hosted DTP to Phase 0.1 UI | validation and commit hygiene |
| Business Brain / Consulting OS | weekly packet and correction checklist templates exist | run the first weekly reset from current lane state | keep private kits as source for client facts |
| Cameron / SMB marketplace | follow-up packet sent; waiting on Cameron's requested item packet | wait for packet, then run reply intake | COI, data, repo access, compensation, and proof gates |
| Greg / TheGrantApp | follow-up packet sent; waiting on Greg reply | wait for discovery availability and proof boundaries | no public proof without written permission |
| CCAAP | parked until owner-approved values arrive | collect PayPal/contact/meeting/DNS/assets/review/proof inputs | no production or proof movement while waiting |
| Omnexus | internal app-review and launch-learning pattern exists | use as internal pattern only | no public proof without permission/redaction/reviewer/caveat |
| DeMario | launch/handoff reference lane exists | keep as command-room reference, not public proof yet | owner permission and redaction |
| DSE | workspace coverage recorded, not verified live in this cycle | touch only if explicitly selected with COI scope | COI, permission, repo-local verification |
| Hub | runtime/intake support layer remains separate from DTP | keep Hub verification green; no DTP migration into Hub | repo boundary |
| `tm-skills` | SDLC behavior layer has doctor/freshness/install checks | convert real misses into skill/eval/checklist updates | external Claude/Copilot smoke remains manual |
| FAOS | roadmap and readiness template exist | run readiness review before any repo/service implementation | do not create FAOS repo yet |

## Source Of Truth Order

1. Current repo files and validation output.
2. DTP steward receipts, roadmaps, evidence indexes, and private engagement kits.
3. Saved memory and rollout summaries, labeled as continuity context.
4. Chat synthesis, only after promotion into DTP.

## Memory Caveats

- Memory may describe a previous dirty or verified state; current git status wins
  when the repo is available.
- Client facts from `engagements/` stay private and should be summarized only at
  lane-status level in tracked steward artifacts.
- Notion remains mirror/inbox only and should not become the source for proof,
  client facts, secrets, or final decisions.
- Public proof remains blocked until evidence, permission, redaction, reviewer,
  and caveat are recorded.

## Open Decisions

| Decision | Default for now | Revisit trigger |
|---|---|---|
| Hosted DTP Phase 0.1 stack | Vite React + TypeScript in `apps/private-dtp` | Supabase deployment or auth model changes require a decision record |
| Hosted DTP live environment | not selected in this cycle | Toni chooses Supabase project and operator account |
| FAOS repo boundary | separate future repo at `C:\Users\tonimontez\code\faos` | readiness review is accepted |
| Business Brain eval automation | fixture-first, manual evaluation for now | enough real replies/misfires exist to justify runner work |
| External skill smoke | manual back-burner | Toni opens Claude Code/Copilot discovery verification |

## Correction Checklist For Toni

| Claim or section | Source used | What to correct if wrong | Destination |
|---|---|---|---|
| DTP owns the private operating brain | roadmap, steward receipts, memory status | Tell me if Hub should own any private methodology surface | roadmap / decision |
| Hosted DTP should be private single-operator first | Hosted DTP Phase 0 doc | Tell me if this should become multi-user earlier | Hosted DTP doc |
| Current client lanes should wait on replies/owner inputs | private kits summarized at lane level | Tell me if a client lane is active now despite the recorded waiting state | engagement kit / weekly packet |
| FAOS should stay behind readiness review | FAOS roadmap and backlog | Tell me if FAOS should be pulled forward before Hosted DTP proves useful | FAOS readiness review |
| Public proof is still gated | proof templates and client lane docs | Tell me if any lane has explicit permission that is not captured yet | proof packet / redaction queue |

## Durable Promotions From This Cycle

- Memory Spine was used as a live session rehydration packet.
- Current lane state was converted into a Business Brain weekly reset artifact.
- Hosted DTP Phase 0.1 moved from scaffold-only to private app implementation.
- FAOS readiness remained gated instead of becoming implementation by inertia.

## Verification Receipt

Baseline before this cycle:

- `pytest`: 55 passed, 3 skipped.
- `ruff check .`: passed.
- `dtp memory status`: passed.
- `dtp practice doctor`: passed.
- `dtp skills --validate`: passed.
- `dtp workspace report`: passed with no missing coverage.
- `dtp redact check practice-os --profile practice`: passed.
- `dtp kit status`: no missing kit files; redaction/handoff still needed.
- `gitleaks detect --source . --config .gitleaks.toml --no-git --redact`: no leaks.
- Hub `pnpm verify`: passed.
- `tm-skills` doctor/freshness/install preview: passed.
