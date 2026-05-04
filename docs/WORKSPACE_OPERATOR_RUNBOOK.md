# Workspace Operator Runbook

Status: active safe-work runbook for Toni's multi-repo consulting workspace.

Owner: `diagnose-to-plan`

Purpose: let Toni, Codex, Claude, future agents, and collaborators identify the right repo, safe command class, verification path, and no-touch boundary before doing cross-repo work.

This runbook does not authorize a live cross-repo command runner. `dtp workspace report` remains read-only.

## Command Classes

| Class | Meaning | Examples | Default posture |
|---|---|---|---|
| `safe-read` | Reads files or repo state without changing tracked files or live systems | `rg`, `git status --short`, `Get-ChildItem`, opening docs | Allowed for planning and audit |
| `safe-local-check` | Local validation that may create caches/build artifacts but does not deploy or mutate source intentionally | tests, builds, doctor checks, static validators | Allowed when relevant and scoped |
| `mutating` | Edits tracked files, writes generated tracked outputs, applies migrations, reformats, or updates lockfiles | `apply_patch`, formatters with write mode, migrations, codegen | Requires explicit implementation request |
| `deploy` | Changes live hosting, cloud settings, DNS, production database, or app-store state | Vercel deploy/env writes, Supabase SQL, Azure deploy, App Store upload | Forbidden without explicit deploy request |
| `forbidden-without-explicit-request` | High-risk or easy-to-confuse operations | deleting data, printing secrets, live client comms, public proof publish, cross-repo automation, global installs | Do not run from inference |

## Global Operating Rules

- Start from repo ownership, not from file proximity.
- Prefer DTP for practice roadmap, proof, redaction, Business Brain, and client operating methodology.
- Prefer consulting for public-site copy, public proof layout, `/start`, `/admin`, and visual trust.
- Prefer Hub for runtime intake, console, webhooks, cron, prompts, registry execution, and private operational rows.
- Prefer project repos for their own product/client code and launch surfaces.
- Do not print secrets. Report env variable presence, names, and posture only.
- Do not deploy, migrate, mutate production, send client communications, or publish proof without an explicit request.
- Keep `dse-content` boundary-level by default.
- Keep Notion as mirror/capture only.
- Keep Hub as runtime support, not CRM, billing, DTP cockpit, or client portal.

## Repo Matrix

| Repo | Role | Tooling | Normal verification | Safe reads | Deploy/live owner | No-touch boundary |
|---|---|---|---|---|---|---|
| `diagnose-to-plan` | Practice OS, Business Brain, roadmap, kits, proof/redaction, COI, memory, hosted DTP planning | Python, `dtp` CLI, markdown | `.\.venv\Scripts\python.exe -m dtp practice doctor`; broader gates may include `pytest`, `ruff check .`, `dtp skills --validate`, redaction checks | `git status --short --branch`, `rg`, `dtp workspace report`, docs/templates | No deploy by default; hosted DTP gated separately | Do not commit private engagement material; do not build hosted DTP without separate approval |
| `consulting` | Public storefront, proof surface, `/start`, noindex `/admin`, Hub-first intake | npm, Astro, Vercel | `npm run build`, `npm run test:routes`, `npm run security:secrets` when changing site/proof/intake | routes, README, launch checklist, public assets, env examples | Vercel project, but deploy/env writes need explicit request | No private DTP kits, Hub rows, raw proof, secrets, or unreviewed claims |
| `hub` | Runtime intake, private console, Supabase/Vercel support, webhooks, cron, prompts/runs/captures | pnpm, TypeScript monorepo, Vercel, Supabase | `pnpm verify`, `pnpm test`, `pnpm hub doctor` when relevant and env supports it | README, architecture, runtime docs, Vercel config, API route shape | Vercel/Supabase/Railway-transition state; live checks require explicit runtime scope | Do not turn Hub into CRM, billing, DTP, public proof, or client portal |
| `tm-skills` | Reusable SDLC skill layer for coding agents | PowerShell scripts, markdown skills | `.\scripts\doctor.ps1`, `.\scripts\freshness-check.ps1`, `.\scripts\install.ps1 -WhatIf` | manifest, skill docs, install docs | Global install only after explicit approval | Do not move DTP operator/business skills here |
| `engineering-playbook` | Portfolio doctrine, templates, secret-management references | Markdown, PowerShell utilities | Repo-local script checks when touched | docs, schemas, secret inventory docs | None by default | Does not own current practice sequencing |
| `hub-prompts` | Prompt catalog consumed by Hub | npm, markdown prompts, Zod validation | `npm test` or repo validation script | prompt frontmatter, README, validation config | Prompt publishing/sync should be a separate Hub decision | Does not own prompt targets or practice roadmap |
| `hub-registry` | Hub automation target registry | npm, YAML validation | `npm test`, `npm run validate` if present | `targets.yml`, README, validation config | Registry mutation affects automation routing; treat as mutating | Does not own prompt content or DTP planning |
| `fitness-app` | Omnexus product app, mobile/native/app-store/release proof source | npm, React/Vite/Capacitor, Vercel, Supabase, Stripe, app stores | Repo-owned gates such as build/lint/typecheck/schema contract/release checks depending on lane | README, launch docs, architecture docs, ops proof docs | Live Vercel/Supabase/Stripe/App Store changes require explicit request | High-risk billing/auth/health/AI/user-data surface; do not touch casually |
| `demario-pickleball-1` | DeMario booking/admin site and command-room reference | npm, Next.js, Supabase, Vercel | `npm run ci`, `npm run test:e2e` when launch/admin work changes | setup, release checklist, developer plan, admin/booking docs | Vercel/Supabase/env/admin changes require explicit request | Do not alter booking/payments/admin access without owner-safe plan |
| `ccaap-site` | CCAAP off-Wix public-site implementation | pnpm, Astro, content validators | `pnpm validate:content`; `pnpm validate:launch` only after launch inputs are ready | README, launch checklist, content settings | Cloudflare/Vercel/DNS changes need explicit request | No member/payment/contact/private data; owner inputs gate launch |
| `FamilyTrips` | Casual family trip hub | npm, Vite/React, optional Supabase | `npm run build`, `npm test`, `npm run validate:data` when touched | README, trip data, Supabase docs | Deploy/env writes need explicit request | Casual privacy is not auth; no sensitive trip details in public/static/open data |
| `architected-strength` | Personal brand OS, proof lab, content/networking surface | pnpm, web app, Azure Bicep, evals | `pnpm run doctor`, `pnpm run ci` when scoped | README, content/agent/infra docs | Azure deploy needs explicit request | Not official Microsoft/client project; no confidential material |
| `dse-content` | Internal Azure Apps/AI and DSE execution OS | npm, Next.js, Azure SWA/App Service, MSX/Dataverse/MCP | Boundary-level only unless explicitly authorized | README, architecture, public/private route docs, high-level deploy docs | Azure/MSX/Dataverse/live/internal work requires explicit request | COI, Microsoft, internal data, dirty worktree, public-proof hold |

## Operating Procedure

1. Identify the user goal and classify it as public offer, private practice, Hub runtime, reusable skill/prompt, project repo, proof, or parked idea.
2. Use `docs/PRACTICE_MACHINE_OPERATING_MAP.md` to choose `Now`, `Next`, `Later`, or `Hold`.
3. Use this runbook to choose repo and command class.
4. Use `safe-read` commands first.
5. If implementation is requested, edit only the owning repo(s) and preserve unrelated dirty work.
6. If proof is involved, route through `docs/PUBLIC_PROOF_PROMOTION_RUNBOOK.md`.
7. If Hub is involved, check `C:\Users\tonimontez\hub\docs\HUB_RUNTIME_CURRENT_STATE.md` before expanding or treating runtime evidence as current.
8. If verification is needed, run the repo-local check that matches the changed surface.
9. Record durable outcomes in the owning doc, steward receipt, evidence index, or backlog story.

## Explicit No-Go List

Do not infer permission to:

- deploy any repo;
- run Supabase SQL or migrations against production;
- change Vercel, Azure, Stripe, App Store, Google, Supabase, or DNS settings;
- publish consulting proof;
- read, print, or store secret values;
- send client communications;
- mutate `dse-content` or inspect internal data deeply;
- create a client portal;
- make Notion the source of truth;
- install global skills or tooling with force;
- create a live cross-repo command runner.

## When In Doubt

Use the narrowest safe path:

1. Read docs and live repo state.
2. Write a DTP plan or runbook.
3. Keep the idea staged rather than activated.
4. Ask Toni only when the remaining choice is about business intent, proof permission, money, privacy, legal/COI risk, or irreversible operations.
