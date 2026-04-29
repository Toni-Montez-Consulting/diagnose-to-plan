# Practice Production Roadmap

This is the canonical roadmap for bringing Toni Montez's consulting practice from working infrastructure to a live, repeatable practice.

DTP owns this roadmap because DTP is the private Practice OS: the place where client kits, redaction, COI, patterns, proof capture, and operating methodology are organized. The consulting site is the public storefront and proof surface. Hub is the intake/runtime support layer.

`tm-skills` is a separate sibling layer for Toni's reusable software-development skills. It does not replace DTP. DTP owns consulting practice memory and client operating methodology. `tm-skills` owns cross-repo SDLC behavior for coding agents: review discipline, frontend craft, backend boundaries, testing judgment, and delivery hygiene. See `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md`.

The reusable admin/customer portal concept is captured as the Client Command Room pattern. It is inspired by the `demario-pickleball-1` admin portal and should guide future owner-facing operating rooms for Toni, clients, and selected engagements. Start with `practice-os/templates/client-command-room-fit-assessment.md`, then use `practice-os/templates/client-command-room-spec.md` only when the fit assessment says to build. See `docs/CLIENT_COMMAND_ROOM_PATTERN.md`.

The reusable verification/support automation concept is captured as the CLI Verification And Automation pattern. It is inspired by the Omnexus / `fitness-app` toolkit and should guide infrastructure-first doctor, matrix, local gate, release gate, support gate, and evidence artifacts before heavier hosted product work. See `docs/CLI_VERIFICATION_AUTOMATION_PATTERN.md`.

## Current Implemented State

### DTP

- `dtp draft`, `skills`, `note`, `story`, and `mentor` support the original diagnose-to-plan harness.
- `dtp index`, `detect`, `lesson`, `recall`, and `synthesize` support Extract Through Synthesis.
- `practice-os/` contains reusable policies, templates, operator Skills, and reviewed Bottleneck Patterns.
- Practice OS includes Client Command Room fit/spec templates so future engagements can decide between a command room, a handoff checklist, no private surface, or a deferred revisit before building portal UI.
- `engagements/` is the gitignored private work area for Client Operating Kits.
- `dtp kit new`, `dtp kit status`, `dtp redact check`, and `dtp practice doctor` support local Client Operating Kit workflows.
- `dtp web` provides a local browser Workbench over the same markdown contracts.
- `dtp vault` can initialize a separate private git repo inside `engagements/` for private engagement durability.

### Consulting

- `tonimontez.co` is the public storefront/proof surface.
- `/start` is the high-intent diagnostic path.
- `/admin` is a noindex public-safe command room and launcher for Hub/DTP links; it does not render private records.
- Public proof is currently framed around Omnexus, SuperKart, AI/ML work, and redacted/private-boundary artifacts.
- The main remaining gap is proof maturity: real/redacted source material and receipt-style case-study packets.

### Hub

- Hub is the private Vercel/Supabase runtime for intake, admin console records, captures, runs, briefings, projects, prompts, and webhook receipts.
- Consulting intake routes into Hub through `PUBLIC_CONSULTING_INTAKE_ENDPOINT`.
- Hub owns runtime records and operator review, not DTP engagement kits.
- Hub should not become the DTP cockpit, CRM, billing surface, client portal, or generalized project management app unless the manual process proves a real bottleneck.

### tm-skills

- Separate version-controlled skills repo exists at `C:\Users\tonimontez\tm-skills` with private GitHub remote `toniomon96/tm-skills`.
- Phase 1 scope is five SDLC skills: `review-checklist`, `frontend-craft`, `backend-design`, `testing-ladder`, and `delivery-baseline`.
- Safe activation checks pass: doctor, freshness, and install dry-run.
- Global install remains gated until explicitly approved; do not run `install.ps1 -Apply` by default.
- COI/Microsoft boundaries stay always-on and point back to DTP's COI screen. Do not create a Phase 1 `compliance-coi` skill.
- Implementation details, install paths, local-state notes, and smoke tests live in `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md`.

### Adjacent Portfolio Repos

- `engineering-playbook` remains useful for portfolio schemas, templates, historical decisions, secret management, and general operating doctrine.
- `hub-prompts` remains the prompt catalogue consumed by Hub.
- `hub-registry` remains the Hub automation target registry.
- These repos should not duplicate this roadmap. They should point here when the question is practice production sequencing, hosted DTP, Client Operating Kits, proof promotion, or `tm-skills` build order.

### Client Command Room Pattern

- Build concept reviewed from `demario-pickleball-1`.
- Reference shape: protected owner dashboard, tasks, business roadmap, developer roadmap, handoff/rules docs, and domain-specific operating records.
- Practice OS templates now cover fit assessment and first-room spec.
- Intended use: Toni's private hosted DTP cockpit and selected client engagements that need ongoing operations after launch.
- Do not turn every site into a portal. Use the pattern only when there is a real recurring workflow.
- Implementation details live in `docs/CLIENT_COMMAND_ROOM_PATTERN.md`.

### CLI Verification And Automation Pattern

- Build concept reviewed from Omnexus / `fitness-app`, now backed by PR `https://github.com/toniomon96/Omnexus/pull/553` on branch `feat/verification-toolkit-supabase-cockpit`.
- Reference shape: CLI doctor, tool matrix, local verification, release verification, support/runtime checks, and evidence artifacts.
- Concrete shape: shared tool registry, lock file, Docker-backed specialty tools, ignored `artifacts/verification/`, CI evidence upload, and Supabase migration drift/fresh-replay repair guard.
- Intended use: make infrastructure observable and repeatable before building more UI.
- The pattern is infrastructure first: each repo should explain its own gates before hosted DTP tries to persist or display them.
- Sprint 1 verification contract lives in `docs/PRACTICE_VERIFICATION_SPINE.md`.
- Implementation details live in `docs/CLI_VERIFICATION_AUTOMATION_PATTERN.md`.

## Outstanding Work

### Infrastructure-First Verification And Automation

- Inventory CLI tools and verification lanes per repo before building more hosted product surface.
- Define hard, advisory, and manual gates for DTP, consulting, Hub, `tm-skills`, and each project repo.
- Add or document repo-local doctor/matrix commands where they do not exist yet.
- Preserve current reliable commands while planning future wrapper commands.
- Write verification evidence to durable markdown/JSON artifacts.
- Keep hard gates hard: redaction, COI, secret scans, auth boundaries, and production-data safety must not be hidden by advisory modes.
- Feed evidence into hosted DTP and Client Command Rooms only after the CLI spine is reliable.
- Thin CI is now installed or reviewed for the core lane: DTP, consulting, Hub, `tm-skills`, `hub-prompts`, and `hub-registry`.
- Add Sprint 1 tools in phases: evidence templates, Gitleaks, consulting Playwright/axe, advisory Knip, and repo doctor/matrix coverage now; Lighthouse CI, Semgrep, dependency automation, and shared GitHub Actions soon; dashboards, Storybook/Chromatic, Percy/Applitools, OpenTelemetry, k6, and PostHog-for-consulting later only when proven useful.

### Practice OS

- Keep policies current: data classification, COI, redaction, kill switch, no-secrets-in-git, and client consent.
- Add or strengthen templates for proposal/SOW, case-study proof packet, Work Item Spec, and hosted-DTP import/export.
- Add tiny fixtures/evals for high-value Skills: COI, redact, diagnose, proposal, handoff, and case-study capture.
- Promote only reviewed redacted patterns from `extracts/` into `practice-os/patterns/`.

### Hosted DTP

- Build a private single-user DTP app with Supabase Auth, Postgres, Storage, and RLS.
- Keep the Python CLI, local Workbench, markdown artifacts, and vault as fallback/import-export surfaces.
- Do not deploy the current local Workbench as-is. It has no hosted auth model and assumes local trust.
- Replace consulting's local `PUBLIC_DTP_WORKBENCH_URL` default with a hosted DTP URL once the private app exists.

### Client Operating Kits

- Create the Mom nonprofit kit first.
- Use Brother site, Omnexus, Cam, and Greg as structured proof tracks.
- Capture one primary metric and one secondary metric for full kits.
- Run redaction before any proof moves into consulting or reusable Practice OS assets.

### Public Proof

- Replace generic/public-safe frames with real or redacted source material.
- Use receipt-style case studies: before/after screenshots, metric card, walkthrough, system map, decision log, runbook sample, caveats, and permission level.
- Do not publish case-study claims without evidence source, baseline, after-state, measurement caveat, permission level, redaction status, and reviewer.

### SDLC Skills Library

- Keep the separate `tm-skills` repo tool-neutral and Windows-friendly.
- Install globally only after explicit approval and after reviewing the dry-run output.
- Reload Codex, Claude Code, and GitHub Copilot after install approval.
- Smoke-test discovery using the prompts in `tm-skills/README.md`.
- Use one project-pinned canary only after global discovery works.

### Client Command Rooms

- Use the DeMario admin portal as the reviewed reusable pattern source.
- Start each candidate with `practice-os/templates/client-command-room-fit-assessment.md`.
- Use `practice-os/templates/client-command-room-spec.md` only when the assessment says to build.
- Decide per engagement whether the client needs a command room, a simple handoff checklist, or no private surface at all.
- Keep owner-facing tasks and developer/system roadmaps separate.
- Add support/verification panels only when they connect to real CLI evidence.
- Treat command room screenshots and walkthroughs as future proof-packet evidence after redaction/permission review.

## Near Term

Complete these before treating the practice as ready for soft launch.

1. Build the infrastructure-first verification spine.
   - Use `docs/PRACTICE_VERIFICATION_SPINE.md` as the Sprint 1 contract.
   - Use `docs/CLI_VERIFICATION_AUTOMATION_PATTERN.md` as the implementation handoff.
   - Inventory the CLI tools available for DTP, consulting, Hub, `tm-skills`, Brother/DeMario, Omnexus, Mom nonprofit, Cam, and Greg.
   - For each repo, name the local gate, release gate, support gate, manual gates, and evidence artifact path.
   - Classify each gate as hard, advisory, or manual.
   - Add the no-slop quality gate for public/proof-facing work: real evidence, operator voice, Steel Ledger preservation, no fake dashboards or booking links, and no unreviewed proof or AI feature without source material and eval path.
   - Keep this as docs/contract work first. Do not build hosted dashboards before the CLI gates are clear.

2. Stabilize current verification.
   - DTP: `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor`, `dtp index --all`, `dtp synthesize --no-confirm`.
   - Consulting: `npm run build`, visual QA, `/admin` noindex check, sitemap exclusion check.
   - Hub: health check, protected console check, and one real consulting intake submission when practical.
   - Omnexus reference: study PR `https://github.com/toniomon96/Omnexus/pull/553`, `tools:doctor`, `tools:matrix`, `tools:verify:local`, `tools:verify:release`, `ops:release:evidence`, `scripts/ops/toolkit-registry.js`, `scripts/ops/toolkit-lock.json`, and `scripts/ci/check-migration-drift.js` for reusable shape, not direct copying.

3. Clean up private durability.
   - Decide whether to keep or remove any local fake engagement kits.
   - Initialize `dtp vault` only when there is private engagement material worth preserving.
   - Add a private remote before relying on the vault for durable off-laptop storage.

4. Start Mom nonprofit pilot.
   - Run COI and consent first.
   - Create `mom-nonprofit/site-rebuild` kit.
   - Fill `client-context.md`, `data-inventory.md`, `consent.md`, `diagnose.md`, and `plan.md`.
   - Define primary and secondary metrics before building.
   - Decide early whether Mom needs a lightweight handoff checklist or a real command room.
   - Define support/verification evidence before launch: build status, form/intake status, owner access, handoff checklist, and uptime/manual checks.

5. Define the proof packet format.
   - Use a receipt-style case-study template, not a long enterprise essay.
   - Add baseline, after-state, evidence, caveats, permission, redaction, reviewer, and public/private asset rules.
   - Use this format for Mom nonprofit first, then backfill Brother/Omnexus/Cam/Greg.
   - Include verification artifacts as proof sources where useful, but publish only redacted summaries.

6. Keep consulting aligned.
   - Keep `/admin` as command room/launcher only.
   - Keep Hub intake primary and Formspree fallback.
   - Add source-material assets only after redaction review.
   - Add hosted DTP and verification links later only when they are private-safe.

7. Prepare `tm-skills` Phase 1.
   - Use `docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md` as the implementation handoff.
   - Keep `tm-skills` as the separate pushed repo and do not fold it into DTP.
   - Run global install only after explicit approval.
   - After install approval, smoke-test discovery in Codex first, then Claude Code and GitHub Copilot.
   - Do not overwrite existing global instructions or legacy skill folders.
   - Make `testing-ladder` and `delivery-baseline` aware of doctor/matrix/local/release/support/evidence gates.

8. Capture the Client Command Room pattern.
   - Use `docs/CLIENT_COMMAND_ROOM_PATTERN.md` as the implementation handoff.
   - Treat Brother/DeMario as the reference implementation.
   - Use the Practice OS fit/spec templates for owner dashboard, tasks, business roadmap, developer roadmap, and handoff/rules.
   - Use Mom nonprofit to decide whether the pattern should be a full portal or a lighter handoff checklist.
   - Keep the optional support/verification surface tied to real CLI evidence.

## Mid Term

Build these after the near-term documentation and pilot path are stable.

1. Hosted private DTP.
   - Add a private web app in `diagnose-to-plan`.
   - Use Supabase Auth, RLS, and Storage.
   - Persist engagements, artifacts, artifact versions, metrics, redaction reviews, pattern candidates, and decisions.
   - Add import/export so local markdown kits and hosted records can round-trip.
   - Persist verification evidence only after the CLI evidence contract is stable.

2. Hosted verification and support evidence.
   - Add a durable evidence model for local, release, support, and proof runs.
   - Store command summaries, artifact paths, commit/branch, hard failures, advisory failures, manual gates, and redaction status.
   - Link evidence to engagements, proof packets, support events, and command-room surfaces.
   - Keep raw sensitive logs out of hosted DTP unless there is a clear private-storage reason.

3. Client Operating Kit pilot.
   - Run the Mom nonprofit engagement through diagnose, plan, build, handoff, eval, and redacted proof.
   - Produce a real runbook and walkthrough.
   - Promote one reviewed Bottleneck Pattern.

4. Project proof tracks.
   - Brother site: local business launch proof and handoff pattern.
   - Omnexus: founder/product/operator proof and App Store/product hardening evidence.
   - Cam app: Builder Launch Sprint proof with decision clarity and scope control.
   - Greg app/site: second builder/operator pilot once scope is clearer.
   - Consulting site: public proof layer that receives only reviewed redacted packets.
   - Hub: intake/runtime support, not Client Operating Kit storage.
   - Each project should identify its own CLI verification/support lane before its proof packet is finalized.

5. Business ops.
   - Finalize offer architecture: AI Upgrade Audit, Launch Sprint, Assistant/Workflow Kit, Operating System install.
   - Finalize proposal/SOW template and pricing discipline.
   - Add "what I will not build" filters to reduce bad-fit leads.
   - Add scheduling only when the real booking path exists.

6. `tm-skills` canary and overlays.
   - Pin `tm-skills` into one low-risk repo after global discovery works.
   - Use consulting or `demario-pickleball-1` as the first canary only if duplicate-skill behavior is clear.
   - Add stack overlays after Phase 1 proves useful: `stack-astro`, `stack-nextjs`, `stack-swift-ios`, `architecture-doc`, and `codebase-audit`.
   - Keep stack overlays thin. They should compose with the five base skills, not duplicate them.
   - Add a `verification-toolkit` or `release-evidence` overlay only after the DTP CLI pattern has been used in at least two repos.

7. Client Command Room pilot.
   - Use the DeMario admin portal pattern plus the Practice OS fit/spec templates.
   - Use the Mom nonprofit pilot to test whether the command-room model helps a non-technical operator.
   - Add command-room proof to consulting only after screenshots/walkthroughs are redacted and permissioned.
   - Keep client portals optional until repeated handoff/support pain proves the need.
   - Add support/verification widgets only after evidence artifacts exist.

## Long Term

Build these only after repeated usage proves the need.

- MCP recall across engagements after 2-3 real engagements make manual recall painful.
- Operator routines after the workflow is stable and draft-only checks are enough.
- Client-side routines only when the workflow is proven, low-risk, and easy to disable.
- Release train and support automation after repo-local gates produce trustworthy evidence.
- Vertical bundles only after repeated Bottleneck Patterns exist across multiple engagements.
- Client portal only after handoff/support pain is real.
- Deeper Hub/DTP integration only after manual tracking becomes the bottleneck.
- `tm-skills` keeper automation after skills have real misfire history and repeated update needs.
- Optional plugin packaging only if the skills need to be distributed beyond Toni's local environment.
- Heavier customer portals after the lightweight Client Command Room pattern proves value across multiple engagements.

## Parked

Do not build these into the near-term practice.

- Multi-user SaaS.
- Public Skill marketplace.
- `tm-skills` public distribution or marketplace.
- Self-rewriting skills.
- Skill telemetry beyond local evals and `MISFIRES.md`.
- CRM replacement.
- Billing or e-signature integration.
- Auto-publishing case studies.
- Auto-send client/customer communications.
- Auto-remediation that changes production, databases, billing, or client data without explicit review.
- Client-side autonomous routines.
- Regulated-data verticals.
- Microsoft-conflict-prone offers.
- Public claims that depend on private client material without written permission.

## Repo Ownership Map

| Repo | Owns | Does Not Own |
|---|---|---|
| `diagnose-to-plan` | Practice OS, Client Operating Kits, redaction, COI, patterns, hosted DTP roadmap, private engagement methodology, CLI verification/evidence pattern | Public marketing site, Hub runtime records |
| `consulting` | Public storefront, `/start`, public proof, `/admin` command room, launch/design docs | Private client kits, source-of-truth practice roadmap, runtime intake store |
| `hub` | Runtime intake, private console, Supabase operational tables, webhook/capture/runs support | DTP engagement kits, public proof pages, CRM replacement |
| `tm-skills` | Cross-repo SDLC skills, global coding-agent instructions, trigger evals, skill install/doctor scripts, agent behavior for verification gates | Client engagement records, consulting-practice memory, public proof |
| `engineering-playbook` | Portfolio schemas, templates, historical decisions, general operating doctrine, secret-management references | Source-of-truth practice production roadmap |
| `hub-prompts` | Hub prompt catalogue, prompt schemas, prompt validation fixtures | Practice roadmap, SDLC skills repo, Hub automation target routing |
| `hub-registry` | Hub automation targets and routing config | Consulting knowledge registry, DTP engagement kits, case-study planning |
| `demario-pickleball-1` | Brother/local business launch proof track, client project delivery, Client Command Room reference implementation | Practice-wide roadmap |
| `fitness-app` / Omnexus | Founder/product/operator proof, app launch evidence, reference CLI verification toolkit shape | Practice OS source of truth |
| `FamilyTrips` | Private family trip planning app, data validation, privacy-bound trip coordination | Practice-wide roadmap, public proof, consulting runtime |
| `dse-content` | Internal Azure Apps/AI content, readiness/workflow surfaces, MSX/DSE automation, Microsoft-adjacent proof candidates | Public consulting proof without COI, permission, and redaction review |
| Cam/Greg repos | Project-specific launch/operator proof tracks once created or clarified | Practice-wide roadmap |

For workspace-wide prioritization, missing-item sweeps, and current agentic-AI research additions, see `docs/WORKSPACE_PORTFOLIO_ROADMAP.md`.

## Validation Commands

Run these when roadmap or docs change.

### DTP

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m dtp skills --validate
.\.venv\Scripts\python.exe -m dtp practice doctor
.\.venv\Scripts\python.exe -m dtp index --all
.\.venv\Scripts\python.exe -m dtp synthesize --no-confirm
.\.venv\Scripts\python.exe -m dtp redact check practice-os --profile practice
gitleaks detect --no-git --source . --config .gitleaks.toml --redact --verbose
```

If `gitleaks` is not installed locally, record that as a missing hard-gate tool in the evidence artifact instead of treating the secret scan as passed.

### tm-skills

After the repo exists, run the repo's own doctor and smoke tests. The implementation roadmap defines the exact commands, but the expected checks are:

```powershell
.\scripts\doctor.ps1
.\scripts\freshness-check.ps1
```

Then ask Codex, Claude Code, and GitHub Copilot what skills they can see and run the trigger prompts in `skills/*/evals/trigger.json`.

### Consulting

```powershell
npm run build
```

Confirm `/admin` stays noindex and excluded from the sitemap.

### Hub

```powershell
pnpm test
```

For docs-only Hub changes, this can be skipped if no runtime files changed, but `docs/CONSULTING_CONSOLE_FULL_STACK.md` should still describe Hub as intake/runtime support rather than the DTP cockpit.
