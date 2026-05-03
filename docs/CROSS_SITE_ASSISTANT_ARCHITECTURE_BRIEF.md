---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Cross-Site Assistant Architecture Brief

Status: architecture brief only. Do not build chat widgets, admin assistants, private retrieval, or write-enabled workflows from this document without a separate implementation story.

Owner: `diagnose-to-plan`

Purpose: define the reusable assistant pattern for Toni's project websites so each site can eventually have a public visitor assistant and, where justified, a private/admin operator assistant without mixing public content, private records, client data, or unsupported claims.

## Priority Decision

The assistant lane is real, but it does not outrank the CCAAP launch gates.

Current order:

1. Keep CCAAP launch gates waiting on owner inputs; do not advance CCAAP assistant work.
2. Use consulting as the first public assistant pilot because it directly reduces intake/navigation friction for the practice.
3. Keep Architected Strength merged as the personal-brand OS baseline and later assistant-pattern candidate.
4. Build only the first narrow assistant after source corpus, auth boundary, refusal rules, analytics, and human handoff are accepted.

## Shared Pattern

Use one governed assistant pattern with site-specific manifests, not one generic chatbot pasted across every project.

Preferred V0 shape:

- A shared assistant gateway, likely owned by Hub or a small Hub-adjacent runtime, receives `siteId`, route context, surface mode, and the user message.
- Each site owns a small manifest that defines approved sources, tone, handoff route, refusal rules, analytics policy, and launch gates.
- The public website widget is read-only, page-grounded, and link-oriented.
- The admin widget is authenticated, read-only first, and action-disabled until a later story adds explicit confirmation, auditing, and rollback rules.
- DTP owns the planning, redaction, proof, and governance record; project repos own their local UI and launch gates.

## Assistant Manifest Contract

Every assistant surface needs a manifest before implementation:

| Field | Purpose |
|---|---|
| `siteId` | Stable site key such as `architected-strength`, `consulting`, `demario-pickleball`, or `ccaap-site`. |
| `surface` | `public` or `admin`. |
| `ownerRepo` | Repo that owns the visible route/widget. |
| `runtimeOwner` | Hub, project repo, or future approved assistant gateway. |
| `approvedSources` | Public pages, content collections, docs, or admin records allowed for this assistant. |
| `blockedSources` | Private notes, secrets, raw intake, payment/member records, DTP private kits, or employer/client confidential material. |
| `allowedActions` | Safe read-only behaviors and human handoff paths. |
| `disallowedActions` | Writes, sends, cancellations, payment changes, public proof claims, or private data retrieval unless explicitly approved. |
| `authBoundary` | Public anonymous, public rate-limited, protected admin, or Hub-authenticated. |
| `handoffRoute` | Contact, booking, `/start`, Hub console, owner inbox, or admin task path. |
| `refusalPolicy` | What the assistant must decline, redirect, or caveat. |
| `loggingPolicy` | What is logged, redacted, retained, and excluded. |
| `analyticsPolicy` | Minimal events for usefulness and safety; no private content logging by default. |
| `launchGate` | Required repo-local checks, privacy review, owner approval, and manual smoke steps. |

## Public Assistant Rules

Public assistants may:

- answer from approved public site content;
- explain services, methods, field notes, resources, booking paths, meetings, or contact options;
- link users to the right route;
- prepare a visitor for a human-owned intake, booking, donation, membership, or contact path;
- say when a question needs a human, official source, or owner-approved answer.

Public assistants must not:

- use private Hub rows, DTP engagement kits, Notion private notes, payment/member records, form submissions, raw traces, or private client data;
- present employer, Microsoft, client, medical, legal, financial, or payment claims beyond approved source text;
- invent proof, testimonials, metrics, launch status, or owner approval;
- collect sensitive information unless the site already has an approved intake path and privacy boundary;
- replace human outreach, publishing, owner approval, or support judgment.

## Admin Assistant Rules

Admin assistants require an authenticated/private surface before they can read anything non-public.

Admin V0 should be read-only and may:

- summarize pending admin tasks;
- explain the current launch checklist or owner handoff;
- draft messages for human review;
- surface stale tasks, unpaid follow-ups, booking/inquiry queues, or proof blockers from approved admin records;
- link the operator to the correct admin route.

Admin V0 must not:

- mutate Hub, Supabase, bookings, payments, DNS, Notion, DTP, or project repo files;
- send email, text, outreach, contact-form messages, cancellations, refunds, or public posts;
- expose service-role keys, private notes, raw traces, payment records, member/student data, or cross-site private data;
- cross-contaminate one site's admin context with another site's private corpus.

## Rollout Order

| Order | Site | First useful assistant | Gate |
|---|---|---|---|
| 1 | Consulting | Public service/intake guide for `/`, `/start`, proof, method, and collaboration paths | Manifest and approved source corpus are accepted; Hub-first intake remains the human-owned route; no private Hub rows in public assistant. |
| 2 | Architected Strength | Public personal-brand guide over OS pages, builds, field notes, training systems, and collaborate route | Source private stays protected; public copy has no official Microsoft endorsement or confidential employer/client material. |
| 3 | Consulting or Hub admin | Read-only operator helper for intake status, route checks, and proof blockers | Auth boundary and private-record access must be accepted first. |
| 4 | DeMario | Admin helper for bookings, inquiries, unpaid lessons, venue routing, and weekly owner tasks | Protected admin exists; writes, texts, cancellations, and payment state remain human-confirmed. |
| 5 | CCAAP | Public resource/meeting/donation guide, then optional admin helper | Only after CCAAP launch inputs, owner review, DNS, contact routing, assets, and proof/privacy decisions are stable. |
| 6 | Future sites | Apply the manifest pattern only when a real visitor or operator workflow exists | Do not add assistants as decoration. |

## CCAAP-Specific Hold

CCAAP assistant work stays parked until:

- PayPal donation and membership links are owner-approved;
- contact routing and spam protection are approved;
- public meeting labels/destinations are verified;
- authentic photos/resources are approved;
- Cloudflare preview and owner review are complete;
- production launch gate passes or the owner explicitly approves a pre-launch assistant preview;
- proof remains `internal_only` unless permission, redaction, reviewer, evidence, and caveat gates are complete.

No CCAAP assistant may touch member records, payment records, student/family data, form submissions, private nonprofit notes, or raw DTP engagement material.

## Implementation Gate For The First Assistant

Before any code:

1. Choose the first site and surface.
2. Create the site manifest.
3. Define the approved source corpus and blocked corpus.
4. Choose runtime owner and environment variables.
5. Add refusal and handoff tests.
6. Add route/widget smoke tests.
7. Add redaction/logging review.
8. Record acceptance in DTP and the owning repo.

## Parked

- Vector database or private retrieval.
- Cross-site memory.
- Autonomous outreach.
- AI-written public updates.
- Payment/member/student data access.
- Notion two-way sync.
- Admin writes or record mutation.
- Site-wide rollout before one assistant proves useful.
