---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: hub

## Identity

- Repo: `hub`
- Local path: `hub`
- Primary role: private runtime support for intake, console records, Supabase-backed operations, webhooks, captures, runs, prompts, and registry dispatch
- Owner lane: runtime/intake infrastructure
- Public/private: private operational runtime with public API edges
- Deploy target: Vercel plus Supabase-backed runtime tables

## Boundaries

- Owns: Hub CLI, web app, server/API, Vercel Functions, Supabase runtime tables, intake API, console APIs, webhook ingress, capture/run/prompt runtime records
- Does not own: public consulting proof pages, DTP engagement kits, DTP roadmap ownership, client CRM/billing, proof permission decisions, global skill installation
- Sensitive data: Supabase service credentials, webhook secrets, intake rows, captures, run records, prompt outputs, operational todos/outreach
- COI/privacy notes: DSE/Microsoft-adjacent runtime data requires COI-aware handling before professional/public reuse

## Gates

- Local gate: `pnpm verify`; for targeted work use `pnpm format:check`, `pnpm lint`, `pnpm build`, `pnpm typecheck`, `pnpm test`, `pnpm hub doctor`
- CI gate: `ci` workflow plus `security` workflow on `main`
- Release gate: Vercel deployment, Supabase migration review, environment checks, `/health`, `/api/intake`, `/console`, and webhook smoke checks
- Support gate: live Hub health, protected console routes, intake origin behavior, webhook auth behavior, Supabase storage configured
- Manual gate: production Supabase writes, service-role use, live intake cleanup, webhook delivery tests, public proof promotion

## Evidence

- Evidence path: GitHub Actions logs, `docs/CONSULTING_CONSOLE_FULL_STACK.md`, future DTP evidence records for live runtime checks
- Latest receipt: see `practice-os/efficiency/hub-evidence-index.md`
- Proof eligibility: internal runtime evidence only until redacted and permissioned
- Redaction rule: never place service keys, raw intake, webhook payloads, private run outputs, or private Hub rows in public docs

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `pnpm --filter ... test` on targeted packages
- Safe write commands: code/docs/tests/migrations after repo-specific task approval
- Commands that need explicit approval: production migrations, service-role operations, live webhook tests, sending external actions, deleting/archiving production rows
- Dependency maintenance: CI already covers Node 22/24 build/test surface; keep Dependabot changes evidence-backed
- Toolchain pinning: Node `>=22.5.0`, `pnpm@10.33.0`

## Next Touch

- Lane: Hub prompt/registry cross-validation
- Trigger: after Mom/proof smoke path or when Hub prompt/registry work resumes
- Blocker: sibling repo access in CI is not yet safely configured for full portfolio manifest validation
- Next action: add prompt id cross-validation between `hub-prompts` and `hub-registry` without turning Hub into DTP
