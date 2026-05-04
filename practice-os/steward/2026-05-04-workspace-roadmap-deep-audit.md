---
data_class: P0
confidential: false
permission_level: internal_only
review_status: checked
---

# Workspace Roadmap Deep Audit - 2026-05-04

## Trigger

Toni asked for a private-inclusive, full-map audit of the workspace roadmap so
open sprints, epics, planning threads, PRs, private engagements, and sensitive
DSE work can be aligned into one DTP-owned operating queue.

## Audit Boundary

This was a control-plane alignment pass. It inspected repo state, roadmap
surfaces, PR queues, DTP reports, the nested private `engagements` repository,
and DSE branch/PR posture. It did not deploy, write env vars, run live database
or Azure changes, send client communications, publish public proof, or copy
private client/DSE notes into public-safe artifacts.

Sensitive lanes were summarized by state, blocker, and next action only.

## Answer

Yes, the workspace is in an epic/Kanban operating model, not a single fixed
sprint. Most lanes are either clean and waiting, clean and parked, or blocked
on proof/human/runtime gates. The only live state that needs special handling
right now is:

1. the private `engagements` vault, which is dirty and has no remote;
2. CCAAP/Cameron/Greg client-loop waiting state, which should not be advanced
   until real owner/client input arrives;
3. the consulting public site share-readiness/proof-maturity lane, which is
   close but still has manual visual QA and real intake/proof gates;
4. DSE, which is a separate sensitive internal lane with dirty/ahead local work
   and a large open PR queue.

## Now Queue

Keep the active focus to these three items:

| Rank | Lane | Owner | Why now | Next action |
|---|---|---|---|---|
| 1 | Private engagement-vault durability | `diagnose-to-plan/engagements` private repo | DTP root is clean, but the ignored private vault is dirty and has no remote. That can hide real client-state drift. | Review private diff, decide commit scope, create a private vault commit, and configure/push to a private remote only after Toni approves the vault home. |
| 2 | Human-gated client/proof loop | DTP private kits plus CCAAP/Cameron/Greg lanes | CCAAP, Cameron, and Greg are waiting on owner/client input. Moving build/proof/scheduling without that input would create noise. | On the next real reply, run reply intake first, then update private kits and only mirror sanitized status. |
| 3 | Consulting share-readiness and proof maturity | `consulting` plus DTP proof gate | The public site is aligned to the new brand and Hub path, but trust still depends on manual QA and cleared proof. | Run manual browser/taste QA and real test intake when approved; replace public-safe proof only with DTP-reviewed evidence. |

DSE is not in the main `Now` queue because it is sensitive, dirty, ahead, and
has many open PRs. It needs a separate DSE triage pass, not blended consulting
roadmap work.

## Full Workspace Map

| Lane / repo | Live state | Open PR posture | Current status | Blocker | Next action | Gate |
|---|---|---|---|---|---|---|
| `diagnose-to-plan` | `main...origin/main`, clean before this audit artifact | 0 open PRs | Canonical roadmap, Practice OS, proof, memory, Business Brain | Public proof and hosted persistence remain gated | Keep DTP as source of truth; update backlog/steward only when lanes move | `git diff --check`, `dtp workspace report`, `dtp practice doctor` |
| `engagements` private vault | nested repo on `main`, dirty, no remote configured | no remote to query | Private client kits and send queue | No private durability push path; public DTP ignores it by design | Review and commit private vault state separately | `git -C engagements status --short --branch` |
| `consulting` | `main...origin/main`, clean | 0 open PRs | Public offer/proof surface aligned to 2026-05-04 brand | Manual visual QA and real test intake remain | Keep stable; promote proof only after DTP review | `npm run verify`, `npm run doctor`, `npm run matrix` when site claims change |
| `hub` | `main...origin/main`, clean | PR `#68` Tailwind 4 is mergeable by GitHub but failing typecheck/build-test checks | Runtime support/intake layer | Tailwind 4 dependency PR is blocked by CI failures | Leave #68 parked until a targeted migration/fix plan exists | `pnpm verify`, PR checks |
| `tm-skills` | `main...origin/main`, clean | 0 open PRs | Global SDLC skill layer | External Claude/Copilot discovery smoke remains manual | Leave parked unless tool behavior misfires | `.\scripts\doctor.ps1`, freshness, install WhatIf |
| `fitness-app` / Omnexus | `main...origin/main`, clean | 0 open PRs | App Store/Stripe/proof reference lane | Stripe webhook alert parked per Toni; public proof gated | Reopen only for support/proof packet work | repo-specific app/release gates |
| `architected-strength` | `main...origin/main`, clean | 0 open PRs | Personal brand OS and later assistant-pattern candidate | Not the consulting offer surface | Revisit only when its lane is explicitly reopened | `pnpm run ci` |
| `ccaap-site` | `main...origin/main`, clean | 0 open PRs | Client public-site implementation waiting on owner inputs | PayPal/contact/DNS/assets/review/proof decisions | Continue only after owner-approved values arrive | `pnpm validate:launch` after inputs |
| `demario-pickleball-1` | `master...origin/master`, clean | PR `#3` is draft, mergeable, Vercel checks green | Local-business launch/command-room reference | Draft docs PR is not active launch work | Leave draft parked unless repo guidance is reopened | `npm run ci` for meaningful app changes |
| `FamilyTrips` | `main...origin/main`, clean | 0 open PRs | Privacy-first family app lane | Stronger privacy needs architecture change | Leave parked until feature/privacy work reopens | repo data/build/test gates |
| `engineering-playbook` | `main...origin/main`, clean | 0 open PRs | Cross-project doctrine/reference | Must not become roadmap owner | Touch only for general doctrine or policy drift | repo parse/status checks |
| `hub-prompts` | `main...origin/main`, clean | 0 open PRs | Prompt catalog | Runtime proof depends on Hub evidence | Add evals only after real prompt misfires | `npm test` |
| `hub-registry` | `main...origin/main`, clean | 0 open PRs | Prompt target registry | Sibling CI access intentionally deferred | Keep local-first validation | `npm test` / registry validation |
| `dse-content` | `dev...origin/dev [ahead 4]`, dirty Azure readiness work | 64 open PRs: 57 artifact-notification PRs and 7 dependency PRs | Sensitive internal DSE execution OS lane | COI/proof boundary, local dirty state, many PRs; #337 dependency PR has Azure Forge build/deploy failure | Run a separate DSE PR/dirty-branch triage; do not fold into consulting proof | DSE repo-local validation before touching |

## PR Classification

| Repo | PRs | Classification |
|---|---|---|
| `consulting`, DTP, `tm-skills`, Omnexus, Architected Strength, CCAAP, FamilyTrips, engineering-playbook, `hub-prompts`, `hub-registry` | none | no PR action |
| `hub` | `#68` Tailwind 4 | blocked/parked: typecheck and build-test are failing even though GitHub marks it mergeable |
| `demario-pickleball-1` | `#3` docs PR | parked/draft: mergeable and preview checks green, but intentionally draft |
| `dse-content` | 64 total | sensitive separate triage: 57 WorkIQ/artifact notification PRs and 7 dependency PRs should be handled in DSE context only |

## Contradictions And Drift Found

- DTP root cleanliness can hide private engagement work because
  `engagements/` is ignored by the public DTP repo and is its own nested git
  repo.
- The private engagement vault has no remote configured, so "commit and push"
  cannot safely include client-kit durability until a private remote/vault home
  is chosen.
- The older Hub blocker text mentioned older dependency PRs, but live PR state
  shows only `#68` remaining in the visible Hub queue; it is blocked by failed
  CI checks.
- DSE is materially active even though it should stay boundary-level for the
  consulting roadmap: local `dev` is ahead 4, dirty, and has 64 open PRs.
- Consulting is share-ready in source posture but not fully polished-public:
  manual browser/taste QA and a real test intake remain manual gates.

## Waiting On Human

- Cameron: wait for the requested packet or direct confirmation before build,
  access, cadence, or proof movement.
- Greg: wait for reply or approved discovery cadence before scheduling,
  proof, or case-study movement.
- CCAAP: wait for Leah plus Tony owner inputs before DNS, production launch,
  contact/payment routing, public proof, or copy movement.
- Consulting proof: wait for permissioned evidence packets before replacing
  public-safe proof shells.

## Waiting On Tool Or Environment

- `engagements`: private remote/vault home is missing.
- Hub `#68`: Tailwind 4 migration needs targeted fix work before merge.
- `tm-skills`: external Claude Code and GitHub Copilot smoke checks are manual.
- Google Workspace: starter DMARC waits until DKIM Admin verification is
  settled.
- DSE: separate repo-local validation and PR triage are needed before any
  merge/cleanup.

## Parked

- Hosted DTP normal workflow for client-sensitive records.
- Omnexus Stripe webhook recovery, per Toni, until support lane is reopened.
- QuickBooks read-only connector.
- Public assistant widget/runtime.
- FAOS implementation.
- DSE public/professional proof reuse.
- Autonomous client communications.
- Public proof auto-publishing.
- Cross-repo live command runner.

## Do Not Touch Without Explicit Approval

- Deploys, DNS, Vercel/Azure/Supabase/Stripe/App Store settings, production DB
  writes, env writes, secret reads/printing, client communications, public proof
  publishing, DSE deep mutation, hosted DTP implementation, QuickBooks OAuth,
  client portals, and autonomous write-enabled agent work.

## Implementation Decision

The next useful sprint is not "build more platform." It is:

1. make the private engagement vault durable;
2. run the next client/owner reply through DTP reply intake when it arrives;
3. finish consulting share-readiness manually and improve proof only from
   reviewed packets;
4. schedule DSE as a separate sensitive cleanup lane.

That gives Toni a focused operating queue without losing the larger roadmap.
