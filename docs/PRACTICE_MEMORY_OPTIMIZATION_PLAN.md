---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Memory Optimization Plan

Status: active operating plan.

Owner repo: `diagnose-to-plan`

## Short Answer

Yes, persistent storage would help Codex operate better for Toni's practice,
but only if it stores source-aware records, pointers, summaries, decisions,
and gates. A generic memory bucket would make things feel better for a week and
then become another unreliable source.

The right order is:

1. Make session rehydration reliable from DTP, git, Gmail, Calendar, Notion, and
   active repo state.
2. Improve local DTP recall/index use before adding hosted infrastructure.
3. Add private persistent storage only for records that have ownership,
   classification, redaction, and source pointers.
4. Add vector retrieval or MCP recall only after the approved corpus and
   refusal/eval rules are clear.

## Why This Exists

Toni is now running several live or near-live streams at once:

- Cam / SMB marketplace prototype.
- Greg / TheGrantApp.io discovery and case-study path.
- CCAAP owner-input and redesign path.
- Consulting site and future public assistant.
- Business Brain / Notion cockpit.
- QuickBooks and other connector candidates.
- Adjacent repo work across Omnexus, DeMario, Hub, `tm-skills`, and others.

That load can be handled, but not by chat memory alone. The practice needs an
explicit retrieval discipline so every session can answer:

- What is authoritative?
- What is stale?
- What is private?
- What changed since the last session?
- What can be acted on now?
- What is blocked by a human, proof gate, COI gate, repo gate, or privacy gate?

## Current Memory Layers

| Layer | Role | Authority |
|---|---|---|
| Chat context | fast working memory for the current session | volatile, never authoritative |
| Codex saved memory | prior-run hints and preferences | useful for rehydration, verify against live sources when drift matters |
| DTP tracked docs | durable practice operating system | authoritative for public/internal practice rules |
| DTP ignored engagement kits | private client source of truth | authoritative for client-specific facts and gates |
| Git history | durable implementation and receipt trail | authoritative for committed repo changes |
| Steward receipts | session closeout and rationale memory | authoritative for what a sprint claimed to do |
| `dtp index` / `dtp recall` / `dtp synthesize` | local retrieval and synthesis layer | helper layer, source output must still be checked |
| Notion | daily cockpit and phone inbox | mirror only, not source of truth |
| Gmail / Calendar | external input and scheduling surfaces | input surfaces, not memory by themselves |
| QuickBooks | future financial input | not connected; manual/export-first until approved |

## Immediate Optimization

Use this before adding any hosted memory service.

### Start Of Broad Session

Run or inspect:

- `git status --short --branch` in the repo that may be edited.
- `dtp workspace report` when the request spans more than one workstream.
- `dtp kit status cameron-mckesson` when Cam is in scope.
- `dtp kit status greg-thegrantapp` when Greg is in scope.
- `dtp kit status mom-nonprofit` when CCAAP is in scope.
- `rg` over DTP docs/templates/steward receipts for the relevant topic.
- Gmail search only for the specific thread or client reply in scope.
- Notion Command Center only for sanitized cockpit state.

Then fill or mentally execute
`practice-os/templates/session-rehydration-checklist.md`.

### During Work

- Promote important ideas into a DTP doc, roadmap row, template, decision
  record, or steward receipt.
- Store source paths, commit IDs, timestamps, email thread IDs, and command
  names instead of vague recollection.
- Treat private details as private kit material, not public docs.
- Treat Notion entries as inbox items until DTP triage accepts them.
- Keep raw transcripts out of public docs and Notion by default.

### End Of Work

- Leave a steward receipt for meaningful infrastructure, client, repo, or proof
  movement.
- Update the roadmap/backlog if priority or status changed.
- Update Notion only with sanitized status fields.
- Commit tracked DTP infrastructure docs when they are meant to become durable.
- Leave ignored/private engagement files out of git unless a private durability
  path exists.

## Persistent Storage Ladder

### V0: Markdown, Git, Ignored Kits, Notion Cockpit

Use now.

- DTP tracked docs hold operating rules.
- Ignored `engagements/` kits hold private client state.
- Steward receipts capture meaningful session outcomes.
- Notion mirrors only daily visible status.

This is still the best default because it is inspectable, cheap, and easy for
agents to rehydrate.

### V0.5: Local Recall Discipline

Use now and improve before hosted memory.

- Run `dtp index` when repo-wide recall needs a fresh index.
- Use `dtp recall` for source-grounded lookup.
- Use `dtp synthesize` to create reviewed summaries from known sources.
- Add `practice-os/templates/memory-source-index.md` when a topic keeps being
  rediscovered.

This stage reduces repeated searching without changing the storage model.

### V1: Private Vault Snapshots

Use when ignored engagement kits need a durable backup or review receipt.

- Use `dtp vault` only for approved private snapshots.
- Store pointers and summaries, not unreviewed raw data dumps.
- Keep credentials, secrets, raw financial records, and unnecessary personal
  data out of vault artifacts.

### V2: Hosted DTP Private Records

Use only after the Phase 0 hosted DTP gate is accepted for implementation.

- Store private engagement records, artifacts, evidence, decisions, redaction
  reviews, and proof candidates in a private Postgres/Supabase-backed model.
- Use RLS and private auth from the start.
- Keep local markdown import/export as fallback.
- Store pointers and reviewed summaries before copying raw materials.

The starting point remains `docs/HOSTED_DTP_PHASE_0.md`.

### V3: Source-Aware Retrieval

Use after a private corpus and redaction rules exist.

- Retrieval may include embeddings, search indexes, or a private assistant.
- Corpora must be explicitly approved.
- Retrieval results must cite source pointers.
- Private client kits, Notion private pages, Hub rows, financial records, raw
  traces, and proof candidates need separate access rules.
- Refusal tests are required before assistant/runtime use.

### V4: MCP Recall / Private Business Brain Assistant

Use only after repeated sessions prove manual recall is still the bottleneck.

- The assistant may retrieve private practice records only through approved
  tools and permissions.
- Every answer must separate verified source facts from inference.
- It must never become an auto-send, auto-launch, payment, public-proof, or
  repo-write actor without a separate gate.

## When Persistent Storage Is Worth It

Persistent storage becomes justified when at least two of these are true:

- More than three active engagements require weekly tracking.
- Rehydration regularly takes more than ten minutes.
- Important context is missed despite DTP docs and steward receipts.
- Private ignored kits need searchable durability beyond local markdown.
- Proof, decisions, artifacts, evidence, and client replies need cross-linking.
- Toni needs reliable weekly close summaries across clients, repos, and finance.
- Notion cockpit entries are accumulating faster than DTP triage can process.

## What Not To Do

- Do not store secrets, credentials, API tokens, OAuth refresh tokens, or private
  financial details in tracked docs.
- Do not make Notion the source of truth.
- Do not create a vector database before data classification, redaction, source
  ownership, and refusal tests exist.
- Do not store raw transcripts by default.
- Do not mirror private client terms, proof claims, payment/member details, or
  confidential notes into Notion.
- Do not solve poor intake discipline with more automation.

## Next Implementation Slice

1. Use `practice-os/templates/session-rehydration-checklist.md` at the start of
   the next broad client or infrastructure session.
2. Use `practice-os/templates/memory-source-index.md` when a topic is important
   enough to need durable rehydration pointers.
3. Keep QuickBooks manual/export-first until the connector boundary is accepted.
4. Keep Notion Premium as a cockpit enhancement, not an authority change.
5. Revisit hosted DTP/private storage after two weekly Business Brain resets and
   at least one real reply cycle from Cam, Greg, or CCAAP.
