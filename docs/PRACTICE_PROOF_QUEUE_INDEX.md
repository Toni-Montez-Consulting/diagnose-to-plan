---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Proof Queue Index

Status: active proof-candidate queue.

Owner: `diagnose-to-plan`

Purpose: keep proof candidates in one DTP-owned place before they become public
consulting copy, public case studies, offer proof, screenshots, or reusable
patterns. This index does not approve public use. It points each candidate at
the next proof gate in `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md`.

## Queue Rules

- Public movement requires evidence, permission, redaction, reviewer, caveat,
  and exact approved wording.
- Project repos own their product state. DTP owns proof routing and the public
  promotion decision.
- Consulting may receive only approved public-safe claims or assets.
- Hub evidence is runtime-support evidence only; do not publish private rows,
  prompts, webhook records, console screenshots, secrets, or run traces.
- DSE remains COI-gated and cannot become public proof without explicit
  boundary review.

## Current Proof Candidates

| Candidate | Lane | Source pointer | Offer supported | Status | Next proof action | Hard gates |
|---|---|---|---|---|---|---|
| CCAAP baseline and after-state owner flow | `ccaap-site`, private DTP kit | `practice-os/efficiency/ccaap-site-evidence-index.md`; `practice-os/steward/2026-05-04-kaizen-existing-system-map.md` | Launch / Proof Hardening Sprint; Client Command Room / Workflow System Sprint | `needs_permission` | wait for Leah/Tony inputs, then inventory baseline, after-state, screenshots, and owner-approved wording | owner permission, authentic assets, launch review, redaction, reviewer, caveat |
| Omnexus launch and review journey | `fitness-app` / Omnexus | `practice-os/efficiency/fitness-app-evidence-index.md`; `docs/MOBILE_APP_REVIEW_AND_LAUNCH_PATTERN.md` | Launch / Proof Hardening Sprint | `needs_redaction` | separate public-safe app-review proof from private app, billing, account, support, and dashboard records | app/privacy caveats, no private user data, source review, reviewer, approved wording |
| DeMario launch-feedback social packet | `demario-pickleball-1`, DTP proof lane, human-owned social channels | `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md`; `practice-os/efficiency/demario-pickleball-1-evidence-index.md`; `practice-os/kaizen/intake.jsonl#kzn-20260505-demario-pickleball-site-is-live-an-29574ac8` | Launch / Proof Hardening Sprint; Client Command Room / Workflow System Sprint; practice proof signal | `posted_url_pending` | capture the exact LinkedIn/Instagram post URL(s) if Toni wants durable public-link proof; keep private screenshots, testimonials, metrics, admin rows, payment proof, and booking data gated | plain/non-gimmicky Mario voice, no unsupported metrics, no autonomous-tool overclaim, no private admin/booking/payment data, private screenshots/testimonials require separate source review |
| DeMario launch/admin command room | `demario-pickleball-1` | `practice-os/efficiency/demario-pickleball-1-evidence-index.md`; `docs/CLIENT_COMMAND_ROOM_PATTERN.md` | Client Command Room / Workflow System Sprint; Launch / Proof Hardening Sprint | `needs_permission` | collect owner-approved walkthrough candidates and redact booking/admin/payment details | owner permission, private admin redaction, caveat, reviewer |
| Consulting Hub-first intake route | `consulting`, `hub` | `practice-os/efficiency/consulting-evidence-index.md`; `practice-os/efficiency/hub-evidence-index.md`; `practice-os/steward/2026-05-06-consulting-live-intake-receipt.md`; `hub/docs/CONSULTING_CONSOLE_FULL_STACK.md` | Business / AI Operating System Sprint; proof of operating discipline | `restricted_internal` | keep as private runtime-support evidence; add a Hub intake archive/delete path before calling cleanup automated | no private row screenshots, no secrets, no public proof claim from private Hub rows, DTP receipt |
| Architected Strength assistant/reference lane | `architected-strength` | `practice-os/efficiency/architected-strength-evidence-index.md`; `docs/assistant-manifests/architected-strength-public-v0.md` | later public assistant pattern candidate | `parked` | wait for consulting assistant source/refusal QA to prove the pattern first | consulting pilot acceptance, repo-local corpus, refusal tests, logging boundary |
| Consulting public assistant manifest | `consulting` | `docs/assistant-manifests/consulting-public-v0.md`; `consulting/docs/ASSISTANT_PUBLIC_V0_SOURCE_CORPUS.md`; `consulting/docs/ASSISTANT_PUBLIC_V0_REFUSAL_FIXTURES.md` | Business / AI Operating System Sprint | `review_ready` for QA only | keep as no-widget QA harness until source and refusal gates pass | approved public corpus, refusal checklist/test, logging policy, human handoff, route/widget smoke before runtime |
| Business Brain real reply loop | DTP Business Brain | `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md`; `practice-os/fixtures/consulting-intelligence/` | Business / AI Operating System Sprint | `needs_evidence` | seed redacted eval cases from the next substantive Cam/Greg/CCAAP reply | no raw private text, client-safe abstraction, expected behavior, reviewer |
| DSE Azure readiness kit | `dse-content` | `practice-os/efficiency/dse-content-evidence-index.md` | possible future readiness product lane | `parked` | hold until COI-aware scope is explicitly selected | COI, live repo validation, permission, redaction, reviewer, caveat |

## Next Review Queue

1. DeMario launch feedback was posted from Toni-owned LinkedIn and Instagram
   channels on 2026-05-06 per Toni's report. Exact post URL(s) remain pending
   only if durable public-link proof is useful; private admin screenshots,
   testimonials, student data, metrics, and payment proof remain separately
   gated.
2. CCAAP remains the first likely client proof packet, but only after owner
   inputs and permission.
3. Consulting plus Hub intake now has a private passed_with_notes smoke receipt,
   but public copy still must not claim "proven intake" from private Hub rows.
4. Omnexus and DeMario command-room material are strong internal proof sources,
   but public proof must stay caveated and permissioned.
5. The public assistant lane may advance to QA harness and manual review, not a
   widget or endpoint.
6. DSE remains a sensitive boundary item, not a public proof backlog item.

## Relationship To Offers

Use `docs/OFFER_TO_PROOF_MATRIX.md` to decide which candidate strengthens each
offer. Use this file to decide where the candidate currently sits in the proof
promotion queue.

