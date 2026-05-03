# CLI Verification And Automation Pattern

This pattern captures the useful operating shape from the Omnexus / `fitness-app` toolkit and turns it into a practice-wide infrastructure pattern.

The goal is not to copy Omnexus scripts into every repo. The goal is to make each repo explain, through the CLI, what tools it has, what checks matter, what evidence was produced, and what the next debug command is when something fails.

## Source Pattern

The current reference implementation is `fitness-app` / Omnexus.

As of 2026-04-30, the concrete reference is merged and available as practice evidence:

- PR: `https://github.com/Toni-Montez-Consulting/Omnexus/pull/553`
- Branch: `feat/verification-toolkit-supabase-cockpit`
- Status verified from GitHub CLI: merged on 2026-04-29 with green checks
- Merge commit: `1347368a01480110e3816e2f4b067102891bde23`
- Post-merge evidence: Verification Toolkit workflow run `25137681778` passed on `main`
- Commits: `52f56097 chore: add verification toolkit cockpit`, `2ffd3088 fix: align verification gates with baseline repair`

The Omnexus implementation is useful because it proves the cockpit pattern against a real production app, not just a doc sketch:

- `npm run tools:doctor`: reports installed tools, version drift, missing hard-gate tools, and next commands.
- `npm run tools:matrix`: prints phase, tool, failure policy, output path, and command.
- `npm run tools:verify:local`: runs deterministic local verification.
- `npm run tools:verify:release`: runs evidence-first release verification with security, performance, native, billing, and release evidence steps.
- `npm run ops:release:evidence`: writes release evidence artifacts.
- `artifacts/verification/`: stores scanner reports, logs, and release evidence.
- `docs/engineering/production-verification-cli-stack.md`: explains the verification stack.
- `scripts/ops/toolkit-registry.js`: shared source of truth for tool ids, install source, version expectation, command, env names, report path, docs link, and failure policy.
- `scripts/ops/toolkit-lock.json`: pinned Docker image and CLI expectations.
- `.github/workflows/verification-toolkit.yml`: CI evidence upload for `artifacts/verification/`.
- `scripts/ci/check-migration-drift.js`: Supabase migration drift gate with a one-time, hash-pinned repair exception for the repaired first migration.

Useful design details:

- The registry is explicit. Tools know their phase, policy, command, output, docs, and install/source mode.
- The doctor is friendly. It tells the operator what is missing and what to run next.
- The matrix is inspectable. A future agent can understand the gate without reading every script.
- Each step prints the exact command and next debug command.
- Secret values are never printed.
- Hard-gate tools are separated from advisory tools.
- Evidence artifacts are written to disk so release/proof decisions do not depend on chat memory.
- Docker carries the specialty scanners and load/security tools so local machines do not become magical.
- Fresh local Supabase replay is treated as truth for schema viability.
- Legacy migration edits remain blocked unless a narrow, documented hash-pinned repair exception is required for fresh replay.

The GitHub checks that made this reference credible included Supabase migration drift, preview/production verification, lint, typecheck, unit tests, quality gate, secret scanning, Semgrep, accessibility, production audit, dependency review, and Vercel preview status. DTP now tracks the reference through `practice-os/efficiency/fitness-app-repo-manifest.md`, `practice-os/efficiency/fitness-app-evidence-index.md`, and the Omnexus steward receipt.

## Required Guardrail

Do not let an advisory mode hide a hard failure.

The reusable rule is:

- hard steps fail the aggregate gate;
- advisory steps can fail without blocking the aggregate gate;
- release verification can finish with advisory failures only if every hard step passed;
- the final summary must list advisory failures instead of quietly calling the run clean.

This matters because a release runner that returns success whenever advisory failures are allowed can accidentally make a secret-scan failure look like a passing release. That is the exact class of mistake this pattern should prevent.

## Supabase Replay Repair Rule

Migrations should remain append-only by default. If a fresh local replay fails because an old migration was internally inconsistent, adding a later migration may not be enough: the database still has to apply the broken old migration first.

If that happens:

- prove the failure with Docker-backed local Supabase from a clean database;
- make the smallest repair to the old migration needed for fresh replay;
- add a hash-pinned exception to the drift checker for that exact repaired blob;
- document the reason in the checker or adjacent docs;
- keep every other old migration edit blocked;
- add a new migration for any production-forward schema change.

This is a repair path, not a general permission to edit history.

## Practice-Wide Shape

Every important repo should eventually have a small verification spine:

1. **Doctor**
   - Shows local tool availability, version drift, missing env names, and next commands.
   - Never prints secret values.
   - Exits non-zero only when hard requirements are missing.

2. **Matrix**
   - Lists checks by phase: local, security, data, deploy, runtime, support, proof.
   - Shows whether each check is hard, advisory, or manual.
   - Shows the output artifact path.

3. **Local Gate**
   - Runs the smallest deterministic check stack for ordinary development.
   - Usually lint, typecheck, tests, build, and repo-specific contract checks.

4. **Release Gate**
   - Runs local gate plus security, deployment, performance, env, runtime, and evidence checks.
   - Allows advisory scanner failures only when they are surfaced for review.

5. **Support Gate**
   - Runs health checks, uptime checks, webhook checks, intake checks, and connected-system diagnostics.
   - Should be cheap enough to run before a client support call.

6. **Evidence Writer**
   - Writes JSON and markdown summaries.
   - Stores raw scanner/report outputs where safe.
   - Redacts or omits sensitive values.
   - Produces proof material that can later be referenced by DTP, a command room, or a case-study packet.

## CLI Tools To Prefer

Prefer existing CLI tools and hosted APIs before inventing app surfaces:

- `git`: repo state, branch, commits, changed files.
- `gh`: PRs, issues, workflow runs, release notes, CI status.
- `vercel`: deployments, env scopes, project links, build status.
- `npx supabase`: migration list, local status, db lint, generated types, project checks.
- `npm` / `pnpm`: package scripts, workspace tests, lint, typecheck, build.
- `python`, `pytest`, `ruff`: DTP checks.
- `playwright`: visual and flow QA where a browser matters.
- `@axe-core/playwright`: advisory accessibility evidence alongside browser smoke tests.
- `gitleaks`: hard secret-scanning gate; missing local binary should be reported clearly by doctor/matrix until CI or Docker fallback is added.
- `knip`: advisory unused dependency/export/file detection; use findings as hypotheses, not deletion orders.
- `lighthouse` / Lighthouse CI: advisory public-site performance/accessibility evidence after the route smoke baseline is stable.
- `semgrep`: advisory static analysis until the rules are tuned for the repo.
- Renovate or Dependabot: dependency hygiene after the local verification lanes are reliable.
- `docker`: optional scanner/runtime fallback when local global tools are missing.
- `az`: Azure checks when a Microsoft/Azure engagement actually needs them.
- `stripe`, `sentry-cli`, Apple/native tooling: only in repos that own billing, observability, or mobile release responsibilities.

The first version should use the CLIs already present in the repo or available through `npx`. Missing optional tools should be reported by the doctor, not turned into a new installation project.

## Tooling Roadmap

### Add Now

- Evidence writer/templates so every meaningful run leaves a receipt.
- Gitleaks as a hard gate across DTP, consulting, Hub, and future client-kit repos.
- Playwright plus axe for consulting route smoke, visual QA evidence, form action checks, `/admin` noindex, and sitemap exclusion.
- Knip as advisory cleanup evidence for consulting and Hub.
- Doctor/matrix scripts or docs so each repo can explain its gates.
- Tool registry and lock-file pattern for repos with more than a few verification tools.

### Add Soon

- Lighthouse CI as advisory public-site evidence.
- Semgrep as advisory static analysis.
- Renovate or grouped Dependabot after local gates are stable.
- Shared GitHub Actions workflows after repo-local commands stop shifting.
- Prompt/registry cross-validation for Hub once the local command shape is stable.

### Table

- Dashboards that do not display real evidence.
- Storybook/Chromatic until components become a maintained design system.
- Percy/Applitools until visual regression pain is real.
- OpenTelemetry until hosted DTP/runtime complexity warrants it.
- k6/load testing until Hub or a client runtime has meaningful load.
- PostHog for consulting until Plausible plus intake evidence is insufficient.

## Repo Fit

### DTP

DTP should own the cross-practice verification model.

Near-term DTP work:

- keep `dtp practice doctor` as the current health check;
- add a documented verification matrix before adding more hosted product surface;
- later add `dtp verify local`, `dtp verify release`, and `dtp verify support` only when the command surface has stabilized;
- write evidence to markdown/JSON artifacts that can round-trip into hosted DTP later;
- keep redaction and COI checks hard gates when evidence is promoted.

### Consulting

Consulting should stay public-safe and proof-focused.

Useful CLI checks:

- `npm run build`;
- confirm `/admin` emits `noindex,nofollow`;
- confirm sitemap excludes `/admin`;
- inspect Vercel deployment status;
- verify Hub intake endpoint and CORS behavior when possible;
- run visual QA before public proof changes ship.

### Hub

Hub should keep runtime support checks close to its own code.

Useful CLI checks:

- `pnpm typecheck`;
- `pnpm test`;
- health route check;
- protected console check;
- intake submission smoke when practical;
- Supabase migration/status checks;
- Vercel deployment checks.

Hub should not become the Practice OS, but its console can expose runtime evidence that DTP links to.

### tm-skills

`tm-skills` should teach future agents to choose and run the right verification lane.

The `testing-ladder` and `delivery-baseline` skills should reference this pattern so agents ask:

- what is the local gate;
- what is the release gate;
- what is manual;
- what evidence artifact was produced;
- what was advisory versus blocking.

### Client Command Rooms

Command rooms can expose a support and verification panel once there is a real operating workflow.

Possible widgets:

- last successful local/release verification;
- last deployment;
- last health check;
- open support tasks;
- connected-system status;
- missing evidence;
- manual gates still owned by the client.

Do this only after the command room has real operational value. Do not add dashboard furniture just because the infrastructure exists.

### Project Repos

Each project repo owns its own app-specific checks:

- Brother / DeMario: booking, payment, admin auth, owner tasks, roadmap checks, venue rules, email, deployment.
- Omnexus: app release, billing, entitlements, native submission, Supabase contracts, security, monitoring.
- Mom nonprofit: content ownership, forms/intake, donation/contact flows if present, handoff, uptime, admin access.
- Cam and Greg: launch checklist, scope control, build/deploy checks, support handoff once their stacks are known.

## Infrastructure-First Build Order

1. **Document the pattern.**
   - Keep this doc and the master roadmap in DTP.
   - Do not change project repos until the repo-specific implementation work begins.

2. **Inventory tools per repo.**
   - Record installed/available CLIs.
   - Identify hard, advisory, and manual gates.
   - Decide output artifact paths.

3. **Standardize naming.**
   - Prefer `doctor`, `matrix`, `verify:local`, `verify:release`, `verify:support`, and `release:evidence`.
   - Match each repo's package manager and language instead of forcing one framework.

4. **Implement the smallest local gate first.**
   - Do not start with scanners, dashboards, or hosted evidence.
   - Make the common daily command reliable.

5. **Add release evidence.**
   - Store machine-readable JSON and human-readable markdown.
   - Include commit, branch, commands, pass/fail state, manual gates, and artifact paths.

6. **Add support automation.**
   - Add health/runtime checks that reduce support friction.
   - Keep production mutations out of generic runners.

7. **Expose evidence in hosted DTP.**
   - Hosted DTP should ingest or link to evidence artifacts.
   - DTP should make evidence searchable by engagement, repo, proof packet, and support event.

8. **Expose client-safe views in command rooms.**
   - Show the client only what helps them operate.
   - Keep developer/system gates separate from owner tasks.

## Evidence Contract

Every durable verification artifact should include:

```yaml
repo:
commit:
branch:
run_at:
lane: local | release | support | proof
result: pass | fail | advisory_pass | manual_pending
hard_failures:
advisory_failures:
manual_gates:
commands:
artifacts:
redaction_status:
reviewer:
next_action:
```

Client-facing proof packets should not include raw scanner logs, secrets, private URLs, environment values, customer data, or internal notes. Public proof should receive a redacted summary with evidence source, baseline, after-state, caveat, permission level, and reviewer.

Use `practice-os/templates/verification-evidence.md` and `practice-os/templates/verification-evidence.json` as the first reusable artifact shape. If a repo writes raw scanner output, keep it internal/private unless it has been intentionally redacted.

## Value

This gives the practice leverage without forcing every project into the same app:

- Future agents can discover the right command instead of guessing.
- Releases produce receipts.
- Support calls start with evidence instead of vibes.
- Case studies can cite real artifacts.
- Hosted DTP has useful data to persist.
- Command rooms can show clients operational truth.
- Toni can keep infrastructure first while still moving toward a polished private UI.
