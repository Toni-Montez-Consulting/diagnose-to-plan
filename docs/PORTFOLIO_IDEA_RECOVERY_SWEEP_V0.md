---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Portfolio Idea Recovery Sweep V0

## Purpose

This is a DTP-owned recovery exercise for ideas, concepts, patterns, preferences, product lanes, and operating rules that may have been missed or under-captured across Toni's portfolio.

This is not a claim that old chats can be reconstructed perfectly. Old chats, memory summaries, rollout summaries, repo docs, dashboards, roadmap notes, and recovery candidates are treated as leads. A lead becomes durable only after review, dedupe, sensitivity labeling, and placement into the right DTP or repo-owned destination.

## Boundaries

This pass is docs/protocol only.

- No Omnexus runtime/code changes.
- No consulting public copy changes.
- No Hub runtime changes.
- No `tm-skills` mutation.
- No Notion mutation.
- No raw transcript text in tracked docs.
- No client/private vault promotion unless a later reviewed pass finds genuinely private engagement material.

## Source Evidence

Current DTP recovery dry run:

- Command: `dtp workspace recover --dry-run`
- Result: 331 candidates
- Ignored generated files:
  - `outputs/workspace-recovery-candidates.json`
  - `outputs/workspace-recovery-candidates.md`
  - `outputs/notion-workspace-cockpit.json`

Observed candidate status mix:

| Status | Count |
| --- | ---: |
| done | 144 |
| parked | 88 |
| inbox | 55 |
| next | 13 |
| blocked | 10 |
| now | 6 |
| superseded | 5 |
| decision_needed | 4 |
| waiting | 3 |
| cancelled | 2 |
| discarded | 1 |

Observed top source coverage:

| Repo/source | Count |
| --- | ---: |
| diagnose-to-plan | 101 |
| codex | 55 |
| memory | 44 |
| consulting | 11 |
| tm-skills | 8 |
| hub | 7 |
| fitness-app / Omnexus | 5 |
| demario | 5 |
| dse | 5 |

The recovery dry run is a read-only lead generator. It is not live PR, CI, production, deployment, email, or client-state truth.

## Privacy Model

### Tracked DTP Artifacts

Tracked DTP artifacts may include:

- reviewed summaries;
- source pointers;
- repo/project labels;
- category;
- confidence;
- sensitivity;
- duplicate or superseded status;
- recommended destination;
- Toni review decision;
- next action.

Tracked DTP artifacts must not include raw transcript dumps or sensitive client/private material.

### Ignored Open-Internal Packets

Ignored files under `outputs/` may include fuller context notes for local review when context is useful. They are not a source of truth and must not be promoted directly into tracked docs without summarization, sensitivity review, and dedupe.

Current open-internal packet:

- `outputs/portfolio-idea-recovery-open-internal-2026-05-14.md`

## Ledger Schema

Each reviewed candidate should use this schema:

| Field | Meaning |
| --- | --- |
| Candidate ID | Stable ID inside this sweep. |
| Title | Short human-readable lead name. |
| Source type | Recovery candidate, repo doc, memory note, rollout summary, roadmap, receipt, PR note, or manual Toni input. |
| Source pointer | Path, command output pointer, receipt, candidate file, PR, or memory pointer. |
| Repo/project | DTP, consulting, Omnexus, Hub, `tm-skills`, FamilyTrips, CCAAP, DeMario, DSE, or portfolio-wide. |
| Category | Agent rule, product idea, process pattern, roadmap lane, client loop, QA/UAT, design, data, business, or cleanup. |
| Confidence | High, medium, or low. |
| Sensitivity | Public-safe, internal, client-sensitive, COI-sensitive, private, or unknown. |
| Duplicate status | New, duplicate, superseded, already captured, or needs merge. |
| Recommended destination | Kaizen intake, roadmap/backlog, pattern candidate, `tm-skills`, repo `AGENTS.md`, private vault, ignored packet, or kill. |
| Toni decision | Pending, keep, kill, later, rewrite, merge, or promoted. |
| Next action | Specific action and owner. |

## First Batch Review

This first batch covers 25 leads:

- 12 agent-rule and reusable behavior candidates.
- 13 product and roadmap candidates.

Toni review decisions are recorded for this batch.

Remaining unreviewed after this batch: 306 detected candidates.

## Agent Rule Candidates

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | Truthful reporting / no-overhype standard | `tm-skills` truthful-reporting work; memory ad-hoc note; Toni explicit request | Portfolio-wide | High | Internal | Already captured, needs smoke proof | `tm-skills`, global agent instructions, DTP integrity standards | Promoted | Keep as promoted behavior; verify external reload behavior in a later smoke pass. |
| A2 | Requirements Gatherer V1 | `docs/CONSULTING_WORKSPACE_OS_V0.md`; `practice-os/templates/requirements-gathering-brief.md`; `practice-os/templates/requirements-decision-ledger.md` | DTP / consulting pilot | High | Internal | Already captured | DTP protocol, later `tm-skills` after evidence | Promoted | Treat as DTP-promoted now; use next meaningful asks as evidence for a future dedicated `tm-skills` behavior. |
| A3 | Remaining Locks Ledger | `practice-os/templates/remaining-locks-ledger.md`; consulting repo instructions | DTP / consulting | High | Internal | Already captured | DTP template and repo `AGENTS.md` references | Keep | Keep active for offer, homepage, proof, and strategy threads. |
| A4 | Surface Translation Standard | `practice-os/patterns/surface-translation-standard.md`; consulting context-leak fixes | Portfolio-wide | High | Internal | Already captured | DTP pattern, repo `AGENTS.md` where public/client surfaces exist | Promoted | Treat as a promoted DTP pattern now; apply during public, admin, owner, and client-facing cleanup work. |
| A5 | Integrity Layer and Pre-Ship Gate | `practice-os/policies/integrity-layer-craft-standard.md`; `practice-os/templates/pre-ship-integrity-gate.md` | DTP / consulting pilot | High | Internal | Already captured | DTP policy and templates | Promoted | Treat as a promoted DTP quality standard now; use as a gate for UAT, pattern cards, proof, AI usage, public claims, and handoff docs. |
| A6 | UAT Kit V0 and receipt modes | `docs/UAT_KIT_V0.md`; `practice-os/templates/uat-receipt.md`; UAT receipt pilots | DTP | High | Internal | Already captured | DTP UAT standard, later narrower variants | Promoted | Treat as a promoted DTP operating standard now; run more receipts before splitting into narrower templates. |
| A7 | Client/prospect context pass before drafting | DTP client-reply loop docs; consulting repo instructions; memory preference | Consulting / DTP | High | Client-sensitive when applied | Already captured | DTP external communications pattern | Promoted | Before drafting, check available context, summarize what changed, then draft; never send or act without explicit approval. |
| A8 | Public proof promotion gates | `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md`; `docs/PRACTICE_PROOF_QUEUE_INDEX.md` | Consulting / DTP | High | Internal | Already captured | DTP proof queue and promotion runbook | Promoted | Keep private proof, sensitive evidence, metrics, and readiness claims out of public copy until promotion gates pass. |
| A9 | Raw transcript dump into tracked docs | `docs/WORKSPACE_DASHBOARD_READONLY.md`; Kaizen cancelled raw transcript note | DTP | High | Unknown to private | Superseded / rejected | Kill for tracked docs; keep source pointers only | Kill | Do not commit raw transcripts; summarize leads and source pointers only. |
| A10 | Durable preference capture and external reload limits | Global truthful-reporting note; `tm-skills` misfire capture | Portfolio-wide | High | Internal | Already captured | Global memory note, `tm-skills`, DTP patterns when useful | Merge into A1 | Preserve as the enforcement/limitation side of A1: save durable preferences, but do not claim universal permanence beyond actual loaded files/tools. |
| A11 | Source-pack and evidence policy for public assistants | `docs/decisions/0016-*.md` through assistant/source-pack docs | Consulting / DTP | Medium | Internal | Needs merge | DTP source-pack docs and assistant manifest surfaces | Keep | Keep tied to assistant/source-pack work now; promote later once the public assistant source-pack lane has enough evidence. |
| A12 | Read-only Recovery Inbox workflow | `docs/WORKSPACE_DASHBOARD_READONLY.md`; workspace recovery outputs | DTP | High | Internal | Already captured | Workspace dashboard and this recovery ledger | Promoted | Recovery outputs are leads, not truth; apply only reviewed rows. |

## Product And Roadmap Candidates

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | Omnexus Natural-Language Nutrition Input V0 | Omnexus audit docs; data-source ledger; Toni friend feedback | Omnexus | High | Internal / user-data sensitive when implemented | Active next lane | Omnexus roadmap and data-consistency backlog | Keep | Start after nutrition cloud contract/logging stack is merged and main is clean. |
| P2 | Omnexus health source and freshness model | Omnexus whole-app data/UX audit; data-source ledger | Omnexus | High | User-data sensitive | New / adjacent | Omnexus data boundary backlog | Keep | Sequence after nutrition input so source-of-truth behavior is explicit. |
| P3 | Omnexus HealthKit Workout Import proof | Omnexus audit; Apple Watch friend feedback | Omnexus | Medium | User-data sensitive | New / sequenced | Omnexus roadmap | Keep | Do right after the health source/freshness model so Apple Watch data does not become another silo. |
| P4 | Omnexus Data and Sync Trust Center | Omnexus audit; data-source ledger | Omnexus | Medium | User-data sensitive | New / later | Omnexus roadmap | Keep | Sequence after P1-P3 and after the underlying data contracts are real enough to expose sync/trust state honestly. |
| P5 | Consulting public assistant manifest | `docs/assistant-manifests/consulting-public-v0.md`; `consulting/docs/ASSISTANT_PUBLIC_V0_SOURCE_CORPUS.md` | Consulting / DTP | Medium | Public-safe after review | Captured, not runtime | DTP assistant manifest and consulting docs | Keep | Keep as manifest/source-corpus work; do not create widget/runtime yet. |
| P6 | Cross-site assistant architecture | `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md` | Portfolio-wide | Medium | Internal | Captured / later | DTP architecture backlog | Later | Revisit after one assistant surface, likely consulting, proves useful. |
| P7 | Hub Environment Ledger / Platform Preview Receipt | `docs/PLATFORM_OPERATING_PATTERNS_V0.md`; platform receipt templates | Hub / DTP | Medium | Internal | Captured / waiting | DTP pattern candidate and Hub backlog | Keep | Use after Hub dependency and lockfile lanes are clean. |
| P8 | Greg Launch Momentum Receipt | `practice-os/templates/launch-momentum-receipt.md`; platform patterns steward notes | Consulting / client ops | Medium | Client-sensitive | Captured / waiting | Private/client operating artifact after meeting | Keep | Wait for real Greg meeting facts before creating a private receipt. |
| P9 | Business Brain real-reply loop | `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md`; real-reply seed queue | Consulting / DTP | Medium | Client-sensitive when applied | Captured / waiting | DTP client-reply operating loop | Promoted | Use on the next real client/prospect reply: capture what they said, what they want, what changed, recommended response, and next artifact before drafting or acting. |
| P10 | Client Command Room pattern | `docs/CLIENT_COMMAND_ROOM_PATTERN.md`; related templates | Consulting / Hub | Medium | Client-sensitive when populated | Captured / later | DTP roadmap/backlog | Keep | Preserve for implementation; sequence later when recurring client workflow pain justifies the heavier command-room surface. |
| P11 | Portfolio context-leak cleanup pattern | Surface Translation Standard; FamilyTrips context-leak history | Portfolio-wide / FamilyTrips next example | Medium | Internal / family-sensitive when applied | Merge into A4 | Surface Translation Standard plus repo-local backlogs when reopened | Merge into A4 | Apply across all projects through the promoted Surface Translation Standard; keep FamilyTrips as a later repo-local proof lane when reopened. |
| P12 | Hosted DTP / private vault with markdown fallback | `README.md`; hosted DTP and vault docs | DTP | Medium | Private when populated | Captured / later | DTP roadmap | Later | Implement eventually, gated behind a stable manual workflow and explicit privacy/access model. |
| P13 | Business Admin OS public-offer timing | `docs/BUSINESS_ADMIN_OPERATING_SYSTEM.md`; `docs/ROADMAP_EXECUTION_BACKLOG.md` | Consulting / DTP | Medium | Internal | Captured / decision needed | Consulting offer roadmap | Later | Reassess only after core consulting proof and intake loop stabilize. |

## Second Batch Review

This second batch covers 5 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 301 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R26 | Consulting UX/design-system audit | `docs/ROADMAP_EXECUTION_BACKLOG.md#consulting-ux-design-system-audit`; dashboard recovery row `wst-consulting-consulting-ux-design-system-audit-b8939fb2` | Consulting / DTP | High | Internal | Active lane | Consulting roadmap and DTP proof gates | Promoted | Treat as an active consulting quality lane. Audit CTA clarity, visual polish, proof presentation, component/design-system health, and route/data-flow architecture while keeping public proof changes blocked until DTP proof gates pass. |
| R27 | DeMario launch-feedback social packet | `docs/PRACTICE_PROOF_QUEUE_INDEX.md`; `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md`; `practice-os/proof-packets/demario-consulting-proof-prep-2026-05-10.md`; `practice-os/proof-packets/consulting-demario-proof-card-rollout-receipt-2026-05-13.md` | DeMario / consulting proof | High | Internal / public-safe only at approved card scope | Already deployed narrow card | DTP proof queue, optional case-study asset pass | Keep | Current proof packet is rich enough for the narrow live homepage proof card and social proof record. It is not yet rich enough for a full case study, screenshots, testimonials, metrics, admin views, booking rows, payment proof, or stronger business-impact claims. |
| R28 | Practice OS strategic backlog | `docs/ROADMAP_EXECUTION_BACKLOG.md#practice-os-strategic-backlog`; dashboard recovery row `wst-diagnose-to-plan-practice-os-strategic-backlog-a512bd43` | DTP | High | Internal | Active control surface | DTP roadmap/backlog | Promoted | Keep as the current DTP sequencing surface for this wave. |
| R29 | Second-cycle client reply/template pilot | `docs/ROADMAP_EXECUTION_BACKLOG.md#second-cycle-client-reply-template-pilot`; dashboard recovery row `wst-diagnose-to-plan-private-kits-or-steward-receipts-second-cycle-client--b009a975` | DTP / private kits or steward receipts | High | Internal / client-sensitive when applied | Merge into P9 | Business Brain real-reply loop | Merge into P9 | Treat as the next execution of the promoted Business Brain real-reply loop, not a separate lane. |
| R30 | Private engagement-vault durability pass | `docs/ROADMAP_EXECUTION_BACKLOG.md#private-engagement-vault-durability-pass`; dashboard recovery row `wst-private-engagements-repo-private-engagement-vault-durability-pass-15e5df1e` | Private engagements repo | High | Private-client | Active later/private lane | Private engagement vault backlog | Keep | Preserve as a future private-infrastructure lane. Do not public-commit client kit material; configure or push only to an approved private remote after explicit access/privacy approval. |

## Third Batch Review

This third batch covers 5 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 296 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R31 | May 2026 Client OS pilot wave | `docs/ROADMAP_EXECUTION_BACKLOG.md#may-2026-client-os-pilot-wave`; dashboard recovery row `wst-private-engagements-sanitized-dtp-may-2026-client-os-pilot-wave-679a78c2` | Private engagements / sanitized DTP | High | Private-client | Active wave | Workflow Spine and client operating artifacts | Keep | Run through Workflow Spine one client lane at a time: Greg and Cam first, with CCAAP staying in its existing packet lane until reopened. |
| R32 | Consulting public assistant manifest | `docs/PRACTICE_PROOF_QUEUE_INDEX.md`; `docs/assistant-manifests/consulting-public-v0.md`; `consulting/docs/ASSISTANT_PUBLIC_V0_SOURCE_CORPUS.md`; dashboard row `wst-consulting-consulting-public-assistant-manifest-b34f0a50` | Consulting / DTP | High | Internal | Merge into P5 | Consulting public assistant manifest | Merge into P5 | Keep as no-widget source-corpus, refusal, QA, logging, and handoff-boundary work before any runtime/widget. |
| R33 | Cross-site assistant architecture brief | `docs/ROADMAP_EXECUTION_BACKLOG.md#cross-site-assistant-architecture-brief`; dashboard row `wst-diagnose-to-plan-cross-site-assistant-architecture-brief-5392a681` | DTP / portfolio-wide | High | Internal | Merge into P6 | Cross-site assistant architecture | Merge into P6 | Keep later; prove one assistant surface before building cross-site architecture. |
| R34 | Business Admin OS public-offer timing | `docs/ROADMAP_EXECUTION_BACKLOG.md#business-admin-os-public-offer-timing`; dashboard row `wst-diagnose-to-plan-later-consulting-business-admin-os-public-offer-timin-c52c7332` | DTP / consulting | High | Internal | Merge into P13 | Consulting offer roadmap | Merge into P13 | Keep later until consulting proof, intake, and offer posture are stronger. |
| R35 | Consulting public assistant pilot manifest | `docs/ROADMAP_EXECUTION_BACKLOG.md#consulting-public-assistant-pilot-manifest`; dashboard row `wst-diagnose-to-plan-later-consulting-and-hub-future-runtime-consulting-pu-4e031f74` | DTP / consulting / future Hub runtime | High | Internal | Merge into P5 | Consulting public assistant manifest | Merge into P5 | Keep tied to source corpus, tests, manifest, refusal, logging, and handoff gates. No widget/runtime yet. |

## Fourth Batch Review

This fourth batch covers 5 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 291 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R36 | CCAAP baseline and after-state owner flow | Dashboard recovery row `wst-ccaap-site-private-dtp-kit-ccaap-baseline-and-after-state-owner-flow-503a90cc` | CCAAP / DTP proof lane | High | Client-sensitive | Active blocked lane | CCAAP proof queue and owner-flow packet | Keep / finish | Toni wants this finished. Keep active, but do not mark unblocked until Leah/Tony inputs, owner permission, authentic assets, launch review, redaction, reviewer, and caveat are captured. |
| R37 | Consulting Hub-first intake route | Dashboard recovery row `wst-consulting-hub-consulting-hub-first-intake-route-6bdddf9e` | Consulting / Hub | High | Internal / private runtime-support | Active blocked lane | Hub cleanup backlog and consulting evidence | Keep | Keep as private runtime-support evidence. Do not make public proof claims from private Hub rows. Add Hub intake archive/delete cleanup before calling the workflow clean. |
| R38 | Public proof promotion | Dashboard recovery row `wst-consulting-public-proof-promotion-e3e02193`; `docs/PRACTICE_PROOF_QUEUE_INDEX.md` | Consulting / DTP | High | Internal | Merge into A8 | Public proof promotion gates | Merge into A8 | No auto-publish. Permission, redaction, reviewer, evidence, and caveat must be approved before any public proof movement. |
| R39 | DeMario launch/admin command room | Dashboard recovery row `wst-demario-pickleball-1-demario-launch-admin-command-room-14d7ab9a` | DeMario / DTP proof lane | High | Client-sensitive / private admin-sensitive | Active blocked lane | DeMario proof backlog and optional case-study asset pass | Keep / permission to start | Toni granted permission to pursue this. Still requires owner/asset-specific review, private admin redaction, booking/payment data exclusion, caveat, and reviewer before any public use. |
| R40 | QuickBooks read-only connector readiness | Dashboard recovery row `wst-diagnose-to-plan-future-hosted-dtp-hub-quickbooks-read-only-connector--dd62ddc3` | DTP / future hosted DTP / Hub | High | Financial / private | Later approved lane | Business Admin OS / hosted DTP connector backlog | Later / permission to evaluate | Toni granted permission to evaluate when it makes sense. Do not connect or configure until a future scoped pass defines Intuit/OAuth setup, credential storage, allowed reports/entities, source-of-truth rules, and no-write boundary. |

## Fifth Batch Review

This fifth batch covers 5 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 286 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R41 | DSE redacted COI-gated repo issue | Dashboard recovery row `wst-dse-content-redacted-coi-gated-repo-issue-7cc5afe8` | DSE content | High | COI-sensitive | Blocked / fenced | DSE COI-aware backlog only | Keep blocked / do not touch | Keep fenced. Reopen only with explicit COI-aware scope and live repo validation. |
| R42 | Business Brain real reply loop eval cases | Dashboard recovery row `wst-dtp-business-brain-business-brain-real-reply-loop-ade74923` | DTP Business Brain | High | Client-sensitive when applied | Merge into P9 | Business Brain real-reply loop | Merge into P9 | Add redacted eval cases only after a real substantive Cam/Greg/CCAAP reply. No raw private text. |
| R43 | Omnexus launch and review journey | Dashboard recovery row `wst-fitness-app-omnexus-omnexus-launch-and-review-journey-3988d3b1` | Omnexus / fitness-app | High | App/account/user-data sensitive | Active proof/release lane | Omnexus proof/release backlog | Keep | Keep public-safe app-review proof separate from private app, billing, account, support, dashboard records, and user data. Refresh live state before acting. |
| R44 | Hub blocked dependency fix pass | Dashboard recovery row `wst-hub-hub-blocked-dependency-fix-pass-311a5327` | Hub | High | Internal | Active blocked lane | Hub dependency backlog | Keep | Keep as a separate Hub-local fix pass. Reproduce and resolve PR #77/#78 build/typecheck failures before merge. |
| R45 | Hub dependency lane refreshed on 2026-05-11 | Dashboard recovery row `wst-hub-hub-dependency-lane-refreshed-on-2026-05-11-green-prs-74-75-and-76-8528c373` | Hub | High | Internal | Merge into R44 | Hub dependency backlog | Merge into R44 | Treat as status context for R44: #74/#75/#76 merged; #77/#78 remain the active blocked dependency work. |

## Sixth Batch Review

This sixth batch covers 5 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 281 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R46 | CCAAP private-client engagement capture | Dashboard recovery row `wst-ccaap-site-redacted-private-client-engagement-capture-9c96ef8e` | CCAAP | High | Private-client | Merge with R36 | CCAAP proof queue and owner-flow packet | Keep waiting / merge with R36 | Wait for detailed Leah/Tony review, DNS/domain path, Sanity invite acceptance, and proof posture. Keep connected to R36 rather than creating a separate CCAAP lane. |
| R47 | Omnexus subscriptions now work in-app | Dashboard recovery row `wst-fitness-app-omnexus-subscriptions-now-work-in-app-by-toni-s-2026-05-07-95405d43` | Omnexus / fitness-app | High | Internal / App Store account-sensitive | Merge into R48 | Omnexus release/live-proof closeout | Merge into R48 | Treat as status context for R48: subscription blocker was operator-confirmed closed. |
| R48 | Omnexus release/live-proof closeout | Dashboard recovery row `wst-fitness-app-app-store-connect-omnexus-release-live-proof-closeout-bd72ce57` | Omnexus / fitness-app / App Store Connect | High | App/account/user-data sensitive | Active proof/release lane | Omnexus proof/release backlog | Keep / operator-confirmed current App Store status good | Toni confirmed the current App Store status is good and there is no need to worry about this now. No App Store action in this recovery pass; refresh live state only before a future release/proof action. |
| R49 | Documentation propagation lane | Dashboard recovery row `wst-all-workspace-repos-documentation-propagation-lane-3156a341` | Portfolio-wide | High | Internal | Active later lane | Repo-local instructions/backlogs when opened | Keep / no bulk edits | Keep as a reminder that standards may need repo-local propagation, but do not bulk-edit repos. Apply when a repo is active or a specific repo needs it. |
| R50 | Consulting proof backlog | Dashboard recovery row `wst-consulting-consulting-proof-backlog-3add6113` | Consulting | High | Internal | Active proof lane | Consulting proof queue | Keep | Keep as a proof queue after DeMario, CCAAP, Greg, and related proof lanes. Do not treat it as permission to publish everything. |

## Seventh Batch Review

This seventh batch covers 5 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 276 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R51 | Business Brain eval garden | Dashboard recovery row `wst-diagnose-to-plan-business-brain-eval-garden-b41de928` | DTP | High | Client-sensitive when populated | Active next lane | Business Brain evaluation backlog | Keep | Add redacted real-reply examples after the next Cam/Greg/CCAAP reply. No raw private text. |
| R52 | Knowledge Base V1 markdown corpus | Dashboard recovery row `wst-diagnose-to-plan-knowledge-base-v1-markdown-corpus-a2240d4f` | DTP | High | Internal / client-sensitive when populated | Later lane | DTP knowledge-base backlog | Later | Keep markdown-first and wait for Greg/CCAAP loops to show friction before adding doctor gates or heavier corpus tooling. |
| R53 | Merged hosted-DTP schema design | Dashboard recovery row `wst-diagnose-to-plan-merged-hosted-dtp-schema-design-53833a0c` | DTP | High | Internal / private when implemented | Later lane | Hosted DTP schema backlog | Later | Start only when hosted schema work is explicitly reopened. No schema or migration work in this recovery pass. |
| R54 | Research Radar first item | Dashboard recovery row `wst-diagnose-to-plan-research-radar-first-item-6617bc6f` | DTP / portfolio-wide | High | Internal | Promoted operating pattern candidate | Research Radar / future skill or agent design | Promoted | Make this proactive: maintain awareness of business, technology, and relevant subdomain changes that could affect strategy, product choices, tooling, compliance, and standards. Decide later whether this becomes a DTP protocol, skill, scheduled agent, or research loop. |
| R55 | Vector Brain path | Dashboard recovery row `wst-diagnose-to-plan-vector-brain-path-3d887756` | DTP | High | Private when populated | Later lane | Retrieval / knowledge infrastructure backlog | Later | Do not implement retrieval until corpus boundaries and privacy evals exist. |

## Eighth Batch Review

This eighth batch covers 5 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 271 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R56 | Handoff/runbook | Dashboard recovery row `wst-diagnose-to-plan-plus-project-repo-handoff-runbook-6e866c7f` | DTP plus project repo | High | Internal / client-sensitive when populated | Promoted operating standard | Handoff/runbook templates and Integrity Layer | Promoted | Treat meaningful builds as requiring useful handoff/runbook material after build scope is known. |
| R57 | Reference promotion gate | Dashboard recovery row `wst-diagnose-to-plan-candidate-repos-reference-promotion-gate-d4128147` | DTP / candidate repos | High | Internal | Promoted gate | Reference promotion / quality gates | Promoted | Do not call a repo a reference or gold standard until it has passed production-level checks. Architected Strength and consulting remain candidates until explicitly promoted. |
| R58 | Consulting proof/offer pilot | Dashboard recovery row `wst-diagnose-to-plan-consulting-consulting-proof-offer-pilot-dc7c5853` | DTP / consulting | High | Internal | Active next lane | Consulting proof and offer backlog | Keep | Use on the next real proof/offer move. Keep tied to evidence and offer movement, not abstract planning. |
| R59 | Architecture review packet | Dashboard recovery row `wst-diagnose-to-plan-touched-repos-architecture-review-packet-65bbe7ae` | DTP / touched repos | High | Internal | Active next lane | Architecture review backlog | Keep | Use before consulting, Hub, `tm-skills`, or cross-repo cleanup implementation. Not required for every small edit. |
| R60 | Hub runtime readiness note | Dashboard recovery row `wst-hub-hub-runtime-readiness-note-85e3add4` | Hub | High | Internal | Active next lane | Hub runtime backlog | Keep | Keep v0.4 hardening first and keep this separate from DTP docs and the Hub dependency PR cleanup lane. |

## Ninth Batch Review

This ninth batch covers 5 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 266 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R61 | tm-skills readiness note | Dashboard recovery row `wst-tm-skills-tm-skills-readiness-note-03283ff3` | `tm-skills` | High | Internal | Promoted gate | `tm-skills` readiness gate | Promoted as gate | Do not promote candidate skills or run global installs without a separate readiness gate. |
| R62 | Review Codex session: Add admin dashboard | Dashboard recovery row `wst-codex-add-admin-dashboard-5761fee3` | Codex recovery inbox | Medium | Unknown until source review | Inbox lead | Recovery inbox | Review later | Do not promote from title alone. Review source pointers before deciding whether this contains a reusable admin-dashboard pattern. |
| R63 | Review Codex session: Add Leah as admin | Dashboard recovery row `wst-codex-add-leah-as-admin-9e736ebb` | Codex recovery inbox / CCAAP candidate | Medium | Potentially client-sensitive | No longer relevant | Kill | Kill | Toni marked this no longer relevant. Do not promote. |
| R64 | Review Codex session: Add photo and tournament research | Dashboard recovery row `wst-codex-add-photo-and-tournament-research-6a5e6ad0` | Codex recovery inbox | Medium | Unknown until source review | No longer relevant | Kill | Kill | Toni marked this no longer relevant. Do not promote. |
| R65 | Review Codex session: Add systems-health-review skill | Dashboard recovery row `wst-codex-add-systems-health-review-skill-a46f5af0` | Codex recovery inbox / `tm-skills` candidate | Medium | Internal | Possible skill candidate | `tm-skills` candidate backlog via R61 gate | Keep / possible skill candidate | Promising reusable skill lead. Review source pointers, then route through the promoted `tm-skills` readiness gate before any skill promotion or global install. |

## Tenth Batch Review

This tenth batch covers 5 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 261 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R66 | Review Codex session: Add trip to site | Dashboard recovery row `wst-codex-add-trip-to-site-3a02c555` | Codex recovery inbox | Medium | Unknown | Disregarded | Kill | Kill | Toni said to disregard. Do not promote. |
| R67 | Review Codex session: App Store review approved | Dashboard recovery row `wst-codex-app-store-review-approved-6f1b0cea` | Codex recovery inbox | Medium | App/account-sensitive | Disregarded | Kill | Kill | Toni said to disregard. Current App Store status was separately operator-confirmed good under R48. |
| R68 | Review Codex session: Audit Azure Readiness Kit | Dashboard recovery row `wst-codex-audit-azure-readiness-kit-b54d8200` | Codex recovery inbox | Medium | Potentially COI-sensitive | Disregarded | Kill | Kill | Toni said to disregard. Do not promote. |
| R69 | Review Codex session: Audit chat history recovery | Dashboard recovery row `wst-codex-audit-chat-history-recovery-2aaac1ba` | Codex recovery inbox / DTP recovery | Medium | Internal | Merge into this sweep | Portfolio Idea Recovery Sweep V0 | Merge into recovery sweep | Treat as evidence/context for this recovery sweep, not a separate lane. |
| R70 | Review Codex session: Audit Family Trips app | Dashboard recovery row `wst-codex-audit-family-trips-app-e7313b01` | Codex recovery inbox | Medium | Unknown / family-sensitive if reopened | Disregarded | Kill | Kill | Toni said to disregard. Do not promote. |

## Eleventh Batch Review

This eleventh batch covers 10 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 251 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R71 | Review Codex session: Audit frontend UX and accessibility | Dashboard recovery row `wst-codex-audit-frontend-ux-and-accessibility-e4c9f6b5` | Codex recovery inbox | Medium | Internal | Merge into R26 / A4 / A5 | Consulting UX/design audit, Surface Translation, Integrity Layer | Merge | Fold into the active consulting UX/design audit and promoted surface/quality standards unless source review reveals a distinct reusable audit template. |
| R72 | Review Codex session: Audit iOS App Store reliability | Dashboard recovery row `wst-codex-audit-ios-app-store-reliability-de4a5555` | Codex recovery inbox / Omnexus | Medium | App/account-sensitive | Merge into R43 / R48 | Omnexus release/review lane | Merge | Keep as release reliability context under Omnexus release/live-proof lanes. |
| R73 | Review Codex session: Audit Omnexus app | Dashboard recovery row `wst-codex-audit-omnexus-app-390ce0de` | Codex recovery inbox / Omnexus | Medium | App/user-data sensitive if reopened | Merge into Omnexus roadmap | Omnexus roadmap and audit backlog | Merge | Fold into the Omnexus whole-app audit and data/product roadmap unless source review reveals missed items. |
| R74 | Review Codex session: Audit test and release gates | Dashboard recovery row `wst-codex-audit-test-and-release-gates-0db416b7` | Codex recovery inbox / portfolio-wide | Medium | Internal | Promoted gate candidate | Integrity Layer / UAT / release-proof gates | Promoted as gate candidate | Preserve as a reusable test/release gate candidate routed through Integrity Layer, UAT, and release-proof standards. |
| R75 | Review Codex session: Build review prompt | Dashboard recovery row `wst-codex-build-review-prompt-2b1aa176` | Codex recovery inbox | Medium | Internal | Inbox lead | Recovery inbox | Review later | Potential reusable prompt, but title is too vague. Review source pointers before promotion. |
| R76 | Review Codex session: Fix App Store rejection | Dashboard recovery row `wst-codex-fix-app-store-rejection-620bd75c` | Codex recovery inbox / Omnexus | Medium | App/account-sensitive | Merge into R48 | Omnexus release/review history | Merge | Keep only as App Store review history under R48. Current App Store status was separately operator-confirmed good. |
| R77 | Review Codex session: Implement Phase 0 prompts | Dashboard recovery row `wst-codex-implement-phase-0-prompts-2e9bf8c1` | Codex recovery inbox | Medium | Unknown | Inbox lead | Recovery inbox | Review later | Too vague to promote from title. Review source pointers before deciding. |
| R78 | Review Codex session: Implement plan site | Dashboard recovery row `wst-codex-implement-plan-site-bda32b69` | Codex recovery inbox | Medium | Unknown | Inbox lead | Recovery inbox | Review later | Too vague to promote from title. Review source pointers before deciding. |
| R79 | Review Codex session: Inspect consulting roadmap | Dashboard recovery row `wst-codex-inspect-consulting-roadmap-1380652b` | Codex recovery inbox / consulting | Medium | Internal | Merge into DTP/consulting roadmap | DTP roadmap control plane | Merge | Fold into the DTP/consulting roadmap control plane unless source review reveals a missed item. |
| R80 | Review Codex session: Organize roadmap, logs, email | Dashboard recovery row `wst-codex-organize-roadmap-logs-email-3d245b6c` | Codex recovery inbox / DTP | Medium | Internal / client-sensitive when applied | Merge into Business Brain / recovery sweep | Business Brain and recovery sweep | Merge | Keep as context for Business Brain, memory/control-plane, and recovery sweep work rather than a separate lane. |

## Twelfth Batch Review

This twelfth batch covers 10 recovery candidates from the current recovery pool.

Remaining unreviewed after this batch: 241 detected candidates.

| ID | Candidate | Source pointer | Repo/project | Confidence | Sensitivity | Duplicate status | Recommended destination | Toni decision | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R81 | Review Codex session: Plan agent squads and knowledge base | Dashboard recovery row `wst-codex-plan-agent-squads-and-knowledge-base-28bde0a2` | Codex recovery inbox / DTP | Medium | Internal | Merge into DTP squad/KB lanes | Client OS, Workflow Spine, Knowledge Base V1, `tm-skills` gates | Merge | Fold into existing DTP squad and knowledge-base lanes unless source review reveals a missed decision. |
| R82 | Review Codex session: Plan AI Gateway cost control | Dashboard recovery row `wst-codex-plan-ai-gateway-cost-control-20854892` | Codex recovery inbox / DSE or hosted DTP candidate | Medium | Internal / potentially COI-sensitive | Inbox lead | Recovery inbox | Keep / review later | Potentially useful for AI Gateway or hosted DTP, but source review and repo-boundary check are required first. |
| R83 | Review Codex session: Plan Azure readiness fixes | Dashboard recovery row `wst-codex-plan-azure-readiness-fixes-490120ea` | Codex recovery inbox / DSE candidate | Medium | Potentially COI-sensitive | Disregarded unless reopened | Kill | Kill unless COI-aware reopened | Do not promote unless Toni explicitly reopens with COI-aware scope. |
| R84 | Review Codex session: Plan CCAAP next steps | Dashboard recovery row `wst-codex-plan-ccaap-next-steps-ca96d866` | Codex recovery inbox / CCAAP | Medium | Client-sensitive | Merge into R36/R46 | CCAAP proof and owner-flow lanes | Merge | Fold into R36/R46: owner-flow, baseline/after-state, Leah/Tony inputs, DNS/domain path, Sanity, and proof posture. |
| R85 | Review Codex session: Plan codebase audit | Dashboard recovery row `wst-codex-plan-codebase-audit-00da44ca` | Codex recovery inbox / portfolio-wide | Medium | Internal | Merge into R59/R74 | Architecture review and test/release gate candidates | Merge | Treat as part of the architecture review packet and test/release gate candidate work. |
| R86 | Review Codex session: Plan cross-site AI assistants | Dashboard recovery row `wst-codex-plan-cross-site-ai-assistants-b3582995` | Codex recovery inbox / portfolio-wide | Medium | Internal | Merge into P6/R33/R35 | Cross-site assistant architecture | Merge | Keep later after one assistant surface proves useful. |
| R87 | Review Codex session: Plan Google integrations | Dashboard recovery row `wst-codex-plan-google-integrations-e24d10d5` | Codex recovery inbox | Medium | Private/account-sensitive if implemented | Inbox lead | Recovery inbox | Review later | Could matter for Calendar, Gmail, Drive, or Sheets, but needs source review and privacy boundary first. |
| R88 | Review Codex session: Plan honeymoon itinerary | Dashboard recovery row `wst-codex-plan-honeymoon-itinerary-c667b6a6` | Codex recovery inbox | Low | Personal | Disregarded | Kill | Kill | Not a portfolio, product, or agent-pattern lane. |
| R89 | Review Codex session: Plan multi-agent phased rollout | Dashboard recovery row `wst-codex-plan-multi-agent-phased-rollout-3531ff73` | Codex recovery inbox / DTP | Medium | Internal | Merge into DTP agent squad / `tm-skills` gates | Agent squad and skill-readiness lanes | Merge | Fold into DTP squad, Requirements Gatherer, and `tm-skills` readiness gates. |
| R90 | Review Codex session: Plan next steps | Dashboard recovery row `wst-codex-plan-next-steps-1995363f` | Codex recovery inbox | Low | Unknown | Disregarded | Kill | Kill | Too generic to preserve without source evidence. |

## Bulk Final Review

This bulk review closes the remaining recovery candidates from the current 331-candidate dry run.

Coverage:

- Candidate range: residual dry-run pool after the individually reviewed rows.
- Count: 266 dry-run rows.
- Status mix in the remaining pool after R90:
  - `done`: 144
  - `parked`: 88
  - `inbox`: 26
  - `superseded`: 5
  - `cancelled`: 2
  - `discarded`: 1

Decision: the rest of the pool is lower signal than the first 50-70 reviewed leads. Nothing in the remaining pool should outrank the already-promoted standards, active Omnexus data-consistency lanes, client/proof loops, CCAAP owner-flow work, Hub dependency/runtime lanes, or Research Radar.

Remaining unreviewed after this bulk review: 0 from the current 331-candidate dry run. Some items remain intentionally parked or review-later, but they are no longer unreviewed.

### R91-R116 Title-Only Inbox Decisions

| ID | Candidate | Toni decision | Destination / note |
| --- | --- | --- | --- |
| R91 | Plan OS import validation gates | Promoted as gate candidate | Recovery Inbox, dashboard validation, import/export, and source-of-truth safety. |
| R92 | Plan Strength OS integration | Review later | Reopen only with Architected Strength, Omnexus, or Strength OS source context. |
| R93 | Plan today's next best steps | Kill | Generic session-planning noise. |
| R94 | Read audit specs | Merge | Fold into architecture review and test/release gate candidates. |
| R95 | Refine MVP rollout plan | Review later | Too vague without source review. |
| R96 | Review and run prompts | Review later / possible prompt QA pattern | Preserve only if source review reveals a reusable prompt QA/eval pattern. |
| R97 | Review App Mod Signal Mapper | Kill unless DSE/App Mod reopened | Do not promote without explicit DSE/App Mod scope. |
| R98 | Review audit specs | Merge | Duplicate of R94; fold into architecture/test/release gates. |
| R99 | Review Azure readiness feedback | Kill unless COI-aware reopened | Do not promote without explicit COI-aware scope. |
| R100 | Review branch changes | Kill | Generic repo-state/session hygiene. |
| R101 | Review build spec | Merge | Fold into Requirements Gatherer, build-ready brief, architecture review, and release gates. |
| R102 | Review open items | Kill | Too generic without source evidence. |
| R103 | Review Phase 0 roadmap | Merge | Fold into DTP roadmap/backlog and hosted-DTP parked lanes. |
| R104 | Review roadmap implementation plan | Merge | Fold into DTP roadmap/backlog. |
| R105 | Review site audit | Merge | Fold into consulting UX/design audit, Surface Translation, and Integrity Layer. |
| R106 | Start master roadmap | Merge | Fold into DTP roadmap/backlog and Documentation Map. |
| R107 | Start with dashboard | Merge | Fold into Workspace Dashboard / read-only command center. |
| R108 | Synthesize roadmap candidates | Merge | Fold into this recovery sweep and DTP roadmap control plane. |
| R109 | Update collaboration instructions | Merge | Fold into promoted agent rules: truthful reporting, Requirements Gatherer, Surface Translation, and question gates. |
| R110 | Update consulting intake docs | Merge | Fold into Hub-first intake route and consulting intake/source corpus lanes. |
| R111 | Update consulting OS prompt | Merge | Fold into Consulting Workspace OS and Requirements Gatherer. |
| R112 | Update Copilot Concierge rules | Review later only if reopened | Do not promote without source review or an active Copilot Concierge lane. |
| R113 | Update Google refresh token | Kill / credential hygiene only | Do not preserve token work as an idea. Never store secrets in tracked docs. |
| R114 | Update portfolio ops wrapper | Merge | Fold into Workspace Dashboard / command-center / DTP ops wrapper ideas. |
| R115 | Update roadmap priorities | Merge | Fold into DTP roadmap/backlog. |
| R116 | Update Tampa trip budget | Kill | Personal/travel budget item, not a portfolio recovery lane. |

### Statused Non-Inbox Group Decisions

| Group | Decision | Rationale / destination |
| --- | --- | --- |
| Already-done DTP/portfolio rows | Archive as captured | 144 `done` rows remain useful as evidence and source pointers, but do not need new backlog lanes. Reopen only through the canonical doc named by the row. |
| Superseded/cancelled/discarded rows | Keep terminal | Keep terminal archive status. Do not revive without a new explicit decision and current-state verification. |
| Memory pointers | Merge as evidence pointers only | Use memory rows as leads. Verify against live DTP/repo source before promoting. Do not treat memory pointers as current truth. |
| DSE / Azure / App Mod / COI-sensitive rows | Keep blocked or kill unless explicitly reopened | No DSE/COI-adjacent item moves without explicit COI-aware scope and live repo validation. |
| Public proof and proof-packet rows | Merge into promoted proof gates | DeMario, CCAAP, Omnexus, command-room, and consulting proof rows route through A8, R27, R36/R46, R39, R43/R48, and R50. |
| Assistant/runtime rows | Keep parked | Architected Strength assistant, cross-site assistant, CCAAP assistant, DeMario admin assistant, and future runtime rows stay parked until the consulting assistant source/refusal/QA lane proves useful. |
| FAOS / advanced agent infrastructure rows | Keep parked behind gates | FAOS, durable execution, business agent stack, code agent stack, DSPy/GEPA, Inspect AI, red-team lab, hosted squad records, central squad board, and hosted steward queue are future infrastructure. Do not implement until evals, privacy boundaries, and readiness gates exist. |
| Research/tooling leads | Merge into Research Radar or Tooling Steward | 2026 State of AI Agents Report, Harvey MCP, AI Gateway cost control, Spec-Kit, MCP recall, and similar leads route through promoted Research Radar or tooling steward review. |
| Verification/process leads | Promote or merge into gates | Affected-only verification, dependency maintenance policy, tool reload smoke, stack overlays, project-pinned canary, and import validation gates route through UAT, Integrity Layer, release gates, and `tm-skills` readiness. |
| Hosted DTP / private vault / knowledge rows | Keep later | Hosted squad records, hosted steward queue, schema/app-shell, Vector Brain, knowledge corpus, and private-vault rows stay later until manual workflows and privacy models are stable. |
| Repo-local propagation rows | Keep no-bulk-edit rule | CMS/editor fit, repo-local custom craft pointers, documentation propagation, and cross-project skill propagation should be applied only when a repo is active or explicitly reopened. |
| Generic session rows | Kill or archive as noise | Generic "next steps", "open items", branch hygiene, personal travel, and title-only session rows are not durable ideas. |

## Promotion Rules

Use these destinations after Toni review:

- **DTP Kaizen intake:** small ideas, issues, misfires, and improvement prompts.
- **DTP roadmap/backlog:** active or later lanes that need sequencing.
- **DTP pattern candidates:** reusable build, QA, workflow, client, or process patterns.
- **`tm-skills`:** cross-agent behavior after DTP protocol proves useful.
- **Repo `AGENTS.md`:** repo-specific behavior only.
- **Private/client vault:** only for client-sensitive material after an explicit private pass.
- **Ignored packet only:** useful context that should not become durable.
- **Kill:** duplicates, stale ideas, rejected directions, or raw transcript artifacts.

## Review Workflow

1. Run `dtp workspace recover --dry-run`.
2. Refresh ignored candidate outputs.
3. Prepare a tracked batch ledger with summaries only.
4. Prepare an ignored open-internal packet when fuller context helps review.
5. Review about 25 candidates at a time.
6. Mark each row as keep, kill, later, rewrite, merge, or promoted.
7. Promote only reviewed rows to the right destination.
8. Update this ledger with what remains unreviewed.

## Recurring Closeout Questions

Add these questions to future major lanes before closing the work:

1. What did we decide?
2. What did we defer?
3. What pattern should be reused?
4. What should become an instruction, skill, or checklist?
5. What is risky to forget?

## Acceptance Criteria

- The first reviewed batch separates keep, kill, later, rewrite, merge, and promoted decisions.
- No raw transcript text is committed.
- Each promoted item has a destination and source pointer.
- Duplicates are marked instead of creating parallel backlog noise.
- The system can answer what remains unreviewed.
- DTP remains the source of truth for this recovery pass.
