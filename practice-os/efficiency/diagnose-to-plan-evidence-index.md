---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: diagnose-to-plan

## Repo

- Name: `diagnose-to-plan`
- Branch: `v2/harness`
- Last updated: 2026-05-03
- Reviewer: Iteration 1 brain completion and Phase 0.2 implementation pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| Hosted DTP Phase 0.2 round trip | 2026-05-03 | pass | current branch | `npm run roundtrip:live` imported the Business Brain weekly packet into the dedicated live Hosted DTP project, created engagement/artifact/version/evidence/redaction/proof/decision/steward/research/import-export records, exported `practice-os/steward/2026-05-03-hosted-dtp-live-roundtrip-export.md`, preserved P0/internal/restricted/not-candidate gates, and confirmed second-operator RLS plus cross-operator attachment blocking. |
| Hosted DTP live smoke | 2026-05-03 | pass | current branch | Dedicated Supabase project `DTP Private` was created in the existing org, the Phase 0 migration was applied, local ignored `.env` was configured, two smoke operator accounts were created/confirmed, `npm run smoke:live` passed, RLS blocked the second operator from all primary-operator rows, cross-operator artifact attachment failed, and metadata verification showed RLS enabled, authenticated access granted, and anon table access revoked across all `private_dtp_*` tables. |
| Iteration 1 Brain Completion / Phase 0.1 | 2026-05-03 | pass | current branch | Memory Spine V1 CLI/doctor gate, correction checklist, first Business Brain weekly reset, consulting intelligence eval JSON, Hosted DTP Phase 0 schema/app-shell scaffold, Phase 0.1 Vite React private UI, markdown import/export tests, DSE coverage artifacts, kit scanner cleanup, Hub verification ignore fix, and FAOS Phase 0A readiness review were implemented; Hosted DTP has operator-aware composite FKs, queue indexes, approved-proof constraints, Supabase Auth/RLS client access, and npm test/build/audit passing; full DTP/Hub/tm-skills validation was green before the Phase 0.1 edits and should be rerun before commit |
| intelligence control plane sprint | 2026-05-02 | pass_with_manual_gates | current branch | Practice Intelligence Control Plane doc, memory-source index, tooling steward snapshot, connector map expansion, live Gmail/Calendar/Notion read-only checks, and steward receipt were added; hosted DTP, QuickBooks OAuth, assistant runtime, vector memory, client portal, and autonomous agents remain gated |
| source-material/control-plane sprint | 2026-05-02 | pass_with_manual_gates | current branch | Practice OS source docs remain preserved, integration docs and ADR convention are documented, manual Thought Inbox/Input Studio/Context Pack/Opportunity Score/Exception Register/Value Ledger/Memory Review Queue templates were added, schema reconciliation was documented without migrations, and the Business Brain reset was piloted with sanitized reply-state evidence plus a sanitized Notion cockpit mirror |
| infrastructure sprint | 2026-05-02 | pass_with_manual_gates | current branch | Client reply intake pattern/template, roadmap/doc alignment, first Cam reply capture, consulting assistant pre-code source/refusal artifacts, Notion cockpit views, and Business Brain calendar reset were prepared; validation recorded in the sprint steward receipt |
| client cadence + light infrastructure | 2026-05-01 | pass_with_manual_gates | current branch | Recurring client cadence pattern/template, Cam/Greg/CCAAP private cadence records, consulting public assistant manifest/source corpus, roadmap alignment, and sanitized Notion cockpit page were prepared; `git diff --check`, `dtp workspace report`, kit status checks, `dtp practice doctor`, `dtp skills --validate`, `pytest`, `ruff check .`, and Notion fetch passed |
| client follow-up sprint | 2026-05-01 | pass_with_manual_gates | current branch | Cam and Greg send-ready packets plus CCAAP waiting state were prepared in private engagement kits; Notion mirror is sanitized; `dtp workspace report`, kit status checks, `dtp practice doctor`, `dtp skills --validate`, `pytest`, and `ruff check .` passed; next manual gate is Toni review/send and client replies before repo access, live data, public proof, or production launch |
| steward receipt | 2026-05-01 | pass_with_manual_gates | current branch | Custom Interface Craft and CCAAP closeout recorded in `practice-os/steward/2026-05-01-custom-interface-craft-and-ccaap-closeout.md`; DTP, `tm-skills`, and `ccaap-site` dirty work is verified but still uncommitted; CCAAP launch blockers remain owner-approved PayPal/contact/meeting/asset/proof inputs |
| CCAAP owner review | 2026-05-01 | sent_with_temp_preview | current branch | Owner review packet and temporary prototype link were sent to Leah plus Tony; DTP records local gates, temporary route smoke, and the durable Cloudflare Pages CLI blocker without treating the tunnel as production readiness |
| assistant manifest | 2026-05-01 | draft | current branch | Architected Strength public assistant V0 manifest added at `docs/assistant-manifests/architected-strength-public-v0.md`; implementation remains blocked until source corpus, refusal/handoff tests, analytics/logging review, and human approval are accepted |
| steward receipt | 2026-05-01 | pass | current branch | Omnexus closeout postflight recorded with commit `65d9ea44`, live-proof checklist commit `deceade8`, local gates, CI run `25198605657`, Build iOS runs `25198605656`/`25198820004`, Security Ops runs `25198605663`/`25198820007`, Semgrep runs `25198605662`/`25198820015`, and the current CCAAP owner-input launch blockers |
| planning | 2026-05-01 | pass | current branch | Cross-site assistant architecture brief added; DTP backlog and portfolio roadmap now track Architected Strength, CCAAP, and the governed public/admin assistant lane without starting assistant implementation |
| workspace coverage | 2026-05-01 | pass | current branch | Architected Strength repo manifest and evidence index added; `dtp workspace report` canonical repo list now includes Architected Strength and CCAAP |
| private kit | 2026-04-30 | pass_with_manual_gates | current branch | CCAAP owner action packet, call-to-action extraction ledger, reusable owner-call extraction template, and raw pattern candidate added; PayPal/contact/meeting/assets/DNS/proof remain owner-input gates |
| local | 2026-04-30 | pass | current branch | Notion/CCAAP memory-capture pass: targeted redaction checks, `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor`, `dtp workspace report`, and `dtp workspace report --json`; `ccaap-site` now appears as manifest=ok/evidence=ok |
| setup | 2026-04-30 | pass | local Codex user config plus Notion workspace | Notion MCP endpoint is configured; OAuth completed; refreshed Codex session exposed Notion tools; smoke page, V0 databases, safe seed rows, and phone-friendly views were created; DTP remains source of truth |
| planning | 2026-04-30 | pass | current branch | Notion Mirror V0 docs/templates/steward receipt added; Notion remains a mirror/inbox and DTP remains source of truth; manual Notion setup was completed later after OAuth/tool reload |
| local | 2026-04-30 | pass | current branch | `hub-prompts npm test`; `hub-registry npm run validate`, `npm run validate:manifests`, `npm run validate:prompt-ids`, `npm test`; DTP `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor`, `dtp workspace report`, `dtp workspace report --json`; Workspace Command Center blocker carry-forward test/report, including Omnexus org-migration closeout, parked Hub dependency PRs, Mom owner facts, DSE no-touch, and FAOS parked |
| private kit | 2026-04-30 | pass_with_manual_gates | vault `2b9e6ca` | Mom nonprofit owner-facts intake, handoff checklist, proof packet, redaction item, decision log, plan, and eval notes updated for owner conversation readiness; private vault snapshot committed locally; no public proof or hosted implementation approved |
| local | 2026-04-30 | pass | current branch | GitHub organization ownership alignment: local remotes, manifests, roadmap surfaces, and `hub-registry` targets updated for `Toni-Montez-Consulting`; `dse-content` intentionally excluded; targeted redaction and DTP validation passed |
| CI | 2026-04-29 | pass | `dd359db` | GitHub Actions DTP CI before this workspace-report batch |
| release | 2026-04-30 | pass_with_note | current branch | targeted redaction checks passed for changed docs/templates; broad `docs/` scan still has a pre-existing `docs/build-spec-v2.md` email finding |
| support | 2026-04-30 | not_applicable | current branch | hosted DTP not implemented; Workspace Command Center V0 is recorded-artifact-only |
| proof | 2026-04-30 | manual_pending | current branch | proof/redaction templates define required review fields; public proof remains blocked |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| DTP now has a private hosted-DTP Phase 0/0.2 boundary, live Auth/RLS smoke, and live import/export round trip | `docs/HOSTED_DTP_PHASE_0.md`, `apps/private-dtp/`, `practice-os/steward/2026-05-03-hosted-dtp-live-roundtrip-export.md` | internal_only | steward review accepted | reviewed |
| DTP now has proof/redaction queue templates | `practice-os/templates/` | internal_only | steward review accepted | reviewed |

## Open Gaps

- Hosted DTP now has a Phase 0 schema/app-shell scaffold, Phase 0.2 local private UI, accepted real-operator/smoke-fixture/deployment/backup-export governance, a passed live smoke, and a passed live import/export round trip against the dedicated `DTP Private` Supabase project. The next hosted gate is one more real operating loop with lane-specific markdown fallback before storing client-sensitive non-smoke records as normal workflow.
- CCAAP owner direction and off-Wix rebuild preference are captured; remaining gates are exact PayPal links, contact routing, domain/DNS, authentic photos/resources, owner review, and proof permissions.
- Cam and Greg follow-ups are sent. Cameron sent an initial positive reply, copied his preferred personal route, and is still expected to provide the requested item packet. Greg has no visible reply in the latest matching Gmail check. Client replies should update private engagement kits before Notion mirrors, calendar invites, repo access, build work, or public proof surfaces.
- The first Memory Spine and Business Brain weekly reset cycle is recorded. Repeat on the next substantive client reply before making the module chain stricter.
- Schema reconciliation is documented in `docs/integration/schema_reconciliation_v0.md`; no client portal, autonomous agent, QuickBooks write path, deep Hub sync, or unmanaged memory behavior is approved.
- Notion Mirror V0 manual setup is complete for phone-first capture/review; future MCP/API sync still needs a DTP-owned dry-run export, redaction review, and steward approval.
- Public proof still needs permission, redaction, reviewer, evidence, and caveat gates.
- GitHub Enterprise org-migration closeout is complete for Omnexus PR #559; Hub PRs #59 and #55 are merged; non-DSE org alignment is no longer the active blocker.
- Workspace Command Center V0 reports recorded artifacts only; live git/CI reads and command execution remain later. Missing repo rows may carry explicit Active Next Queue blockers without inferring gates.
- Repo manifest/evidence index shape now covers DTP, consulting, Architected Strength, Hub, `hub-prompts`, `hub-registry`, `tm-skills`, DeMario, `ccaap-site`, FamilyTrips, engineering-playbook, `dse-content`, and `fitness-app` / Omnexus. `dse-content` remains COI-gated and not proof-ready until explicitly selected with permission, redaction, reviewer, evidence, and caveat gates.
- Cross-site assistant implementation is intentionally not started; the consulting public assistant is the first pilot candidate and remains gated on turning the accepted manifest, repo-local source corpus, refusal/handoff fixtures, logging/analytics policy, and launch gate into tests or a reviewed QA checklist.
- Practice Intelligence Control Plane V0 is documentation/control-plane only. It improves rehydration, routing, and tool/client status discipline, but it does not authorize hosted DTP, private retrieval, QuickBooks OAuth, assistant runtime, client portal, auto-send, auto-schedule, or autonomous work.

## Notes

This index is a pilot artifact. It does not replace GitHub Actions, local validation output, or future hosted DTP evidence records.
