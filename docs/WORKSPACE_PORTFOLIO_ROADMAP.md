# Workspace Portfolio Roadmap

Last updated: 2026-04-29

This plan consolidates the current consulting workspace, prior direction, live repo evidence, and current agentic-AI/development research into one prioritized execution map.

The practical thesis is:

1. Make every future agent session better.
2. Make every repo's delivery state observable.
3. Turn real delivery evidence into proof.
4. Build hosted/private surfaces only when they connect to real artifacts.
5. Add deeper agent automation only after permissions, evals, evidence, and human-review gates exist.
6. Turn delivery, research, failures, and agent-session receipts into compounding practice knowledge.
7. Reduce repeated discovery, setup drift, CI waste, and handoff friction across the whole workspace.

## Scope

Workspace folders currently listed in `C:\Users\tonimontez\toni-consulting-ops.code-workspace`:

- `consulting`
- `Projects/diagnose-to-plan`
- `hub`
- `engineering-playbook`
- `hub-prompts`
- `hub-registry`
- `fitness-app`
- `FamilyTrips`
- `demario-pickleball-1`
- `dse-content`
- `tm-skills`

## Priority Decision

The recommended order from the previous discussion is still valid and now more strongly supported:

1. `tm-skills`
2. Client Command Room template/pattern
3. Light GitHub Actions / CI
4. Hosted private DTP Phase 0
5. Public proof upgrades

The first four items are now implemented to the intended boundary: `tm-skills` is activated through remote/push/dry-run checks, the Client Command Room templates exist in Practice OS, the core-plus-map CI pass is in place, and hosted private DTP Phase 0 has a schema/app-boundary design. The next active item is first proof/redaction use through a real pilot.

Roadmap invariant: every repo in the workspace stays on this roadmap. Some repos are core infrastructure and get touched immediately; other repos are project/product tracks and get touched when the relevant verification, proof, launch, privacy, or COI lane is ready. Nothing falls off the map just because it is not part of the current sprint.

Still later:

- MCP recall.
- Support automation beyond simple health/intake checks.
- Vertical bundles.
- Deep Hub/DTP integration.
- Heavy observability/load tooling.

## Value Standard

An item stays on the roadmap only if it creates at least one of these forms of value:

- Better future agent execution.
- Lower launch or support risk.
- Stronger public proof with real evidence.
- Faster delivery for Toni or a client.
- Clearer owner/client handoff.
- Better security, redaction, COI, or permission control.
- More repeatable revenue motion.
- Stronger research-to-implementation signal, agent performance, or release trust.
- Less repeated setup, rediscovery, verification runtime, or dependency-maintenance noise.

An item should be delayed or cut if it mostly creates:

- A prettier dashboard with no connected evidence.
- A portal where a checklist would work.
- Agent autonomy before consent, logging, and rollback.
- Duplicate state between DTP, Hub, and project repos.
- New framework complexity before a workflow has proven pain.
- Research novelty that does not improve delivery speed, proof quality, risk control, agent performance, or business leverage.
- Efficiency tooling that hides repo boundaries or makes agents skip required local evidence.

## Future Intelligence Layer

Status: roadmap expansion, not a priority reset. The current next order stays intact: hosted DTP Phase 0, proof/redaction queues, first Client Operating Kit pilot, prompt/registry validation, then repo-specific touch passes.

Purpose: make the practice compound. Every delivery, failure, proof packet, research finding, and agent session should be able to become reusable knowledge, an eval, a checklist, a skill update, a gate, or operating doctrine.

Operating rules:

- Keep the learning loop supervised. No self-rewriting skills, autonomous repo edits, auto-published proof, or client-facing automation without explicit approval.
- Start as curated markdown, templates, eval fixtures, and review queues; build hosted automation only after repeated usage proves the workflow.
- Prefer primary sources, official docs, and real repo evidence over AI trend summaries.
- Every new intelligence asset must point back to a repo, engagement, proof packet, eval, or decision it improves.

Components:

- Supervised Self-Learning Loop: work produces evidence, evidence produces lessons, lessons produce evals/checklists/skills, and future work improves.
- Research Arm / Research Radar: track AI/dev trends as `Adopt`, `Pilot`, `Watch`, or `Reject`, with source, relevance, risk, and next review date.
- Agent Flight Recorder: leave a compact receipt for major agent sessions: goal, repos touched, commands, files changed, failures, lessons, follow-ups, and eval candidates.
- Portfolio Scorecard: one health card per repo covering CI, last verified date, proof readiness, privacy/COI risk, next touch lane, and blocker.
- Context Engineering Lane: formalize repo context packs, compact handoffs, structured notes, and just-in-time retrieval patterns for long sessions.
- AI Red-Team / Guardrail Lab: run prompt/agent evals, Promptfoo-style red teams, NIST/OWASP checks, and OpenAI guardrail thinking before write-enabled automation or public AI workflows.
- Release Trust / Supply Chain Spine: layer in SLSA/OpenSSF Scorecard, CycloneDX SBOMs, dependency review, CodeQL/Semgrep, and signed/evidence-backed release artifacts when a repo's risk justifies it.
- Feature Flag / Kill Switch Standard: use explicit flags and rollback paths for AI, billing, intake, client-facing, and automation features; watch OpenFeature as a future standard.
- Agent Protocol Watchlist: keep MCP later as planned; add AG-UI for future agent frontends and A2A as watch-only until multi-agent interoperability is a real need.

Suggested priority:

1. Roadmap-only capture now.
2. Low-cost Practice OS templates next: lesson capture, research radar item, research spike, portfolio scorecard, agent session record, AI red-team plan, feature flag/kill switch plan, and supply-chain baseline.
3. Eval garden after that: convert real misfires from Hub, DTP, and `tm-skills` into small fixtures.
4. Red-team lab before autonomy: add guardrail/red-team tests before any write-enabled agent workflow.
5. Protocol/tool spikes later: AG-UI, A2A, OpenAI Agents SDK, Google ADK, Temporal, and deeper MCP only after DTP/Hub have real workflows that justify them.

Initial sources:

- OpenAI Agents SDK, evals, tracing, and guardrails: https://developers.openai.com/api/docs/guides/agents
- OpenAI agent evals: https://developers.openai.com/api/docs/guides/agent-evals
- Anthropic context engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Google ADK evaluation: https://adk.dev/evaluate/
- AG-UI protocol: https://docs.ag-ui.com/introduction
- A2A specification: https://google-a2a.github.io/A2A/specification/
- Promptfoo red teaming: https://www.promptfoo.dev/docs/red-team/
- DORA metrics: https://dora.dev/guides/dora-metrics/
- OpenFeature: https://openfeature.dev/docs/reference/intro/
- CycloneDX SBOMs: https://cyclonedx.org/specification/overview/
- OpenAlex API: https://developers.openalex.org/api-reference/introduction
- Hugging Face Papers: https://huggingface.co/papers

## Workspace Efficiency Layer

Status: roadmap expansion, not a priority reset. This layer reduces operational drag across the workspace, but it must not turn the workspace into a forced monorepo or hide repo-specific safety gates.

Purpose: make future work faster by giving humans and agents a consistent way to discover repo purpose, run the right checks, avoid unnecessary CI work, capture decisions, and start new projects with the correct baseline.

Operating rules:

- Keep repo boundaries explicit: each repo still owns its own app, gates, deploy target, data rules, and proof lane.
- Prefer manifests, wrappers, and docs before a hosted dashboard.
- Use affected-only checks for speed, but keep full hard gates before release, proof promotion, or risky production changes.
- Do not centralize secrets, private client data, or production write credentials in workspace-level tooling.
- Optimize for fewer repeated decisions, not more ceremony.

Components:

- Workspace Command Center: a root-level command or script that answers what changed, which repos need checks, what to run next, and where the latest evidence lives.
- Repo Manifest Standard: a tiny `.repo.yml` or `repo.toml` per repo with purpose, owner lane, local gates, CI gates, evidence paths, deploy target, data sensitivity, and proof rules.
- Affected-Only Verification: run fast checks only for changed repos/files during normal development, while preserving full gates before release.
- Shared GitHub Actions, Later: extract repeated setup/cache/secret-scan/build patterns into reusable workflows only after thin CI stabilizes.
- Dependency Maintenance Lane: add Renovate or Dependabot with grouped updates, dashboard issue, and repo-specific approval rules.
- Dev Environment Pinning: standardize tool versions with `.tool-versions`, devcontainer/devbox notes, or equivalent repo-local setup docs.
- Evidence Index: keep a lightweight per-repo index of latest verification receipts, proof packets, redaction state, CI runs, and deploys.
- Decision Log Automation: make important tradeoffs easy to record so future agents do not relitigate the same choices.
- Project Starter Factory: create a Practice OS baseline for new client/project repos with README, CI, launch checklist, proof packet, privacy/COI notes, and command-room decision template.
- CI Cache Hygiene: tune GitHub Actions cache/setup-node/setup-python/pnpm/pip patterns per repo, and consider Turborepo/Nx-style remote or affected caching only when the repo shape justifies it.

Suggested priority:

1. Add repo manifest and evidence-index templates.
2. Draft the Workspace Command Center spec.
3. Add a decision-record template and use it on the next real architecture choice.
4. Add dependency-maintenance policy to the roadmap for each repo before enabling bots everywhere.
5. Pilot affected-only verification in DTP or Hub after the repo manifest shape is stable.
6. Extract shared CI only after at least three repos repeat the same reliable workflow pattern.
7. Add starter-factory templates after the Mom nonprofit or next client pilot clarifies the baseline.

Initial sources:

- GitHub reusable workflows: https://docs.github.com/actions/concepts/workflows-and-actions/reusing-workflow-configurations
- GitHub dependency caching: https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching
- Renovate Dependency Dashboard: https://docs.renovatebot.com/key-concepts/dashboard/
- Dependabot version updates: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates
- Turborepo remote caching: https://turborepo.com/repo/docs/core-concepts/remote-caching
- Nx affected/CI waste reduction: https://nx.dev/docs/concepts/ci-concepts/reduce-waste
- asdf tool version manager: https://asdf-vm.com/guide/introduction.html
- Dev Containers: https://containers.dev/

## Sprint 2: Practice Platform Foundations

### Story 1: Finish `tm-skills` Activation

Status: activated to the approved dry-run boundary. The repo is in the VS Code workspace, private GitHub remote `toniomon96/tm-skills` exists, `main` is pushed and tracking `origin/main`, and the safe checks pass. Global install remains gated.

Value: immediately improves every future repo session by making review, frontend craft, backend boundaries, testing judgment, and delivery hygiene reusable across tools.

Remaining work:

- If safe, run `.\scripts\install.ps1 -Apply` only after explicitly approving global links/files.
- Reload Codex, Claude Code, and GitHub Copilot.
- Smoke-test discovery with the prompts in `tm-skills/README.md`.
- Do not create `compliance-coi`; keep COI in DTP plus global instruction floor.
- After global discovery works, pick one low-risk project-pinned canary.

Validation:

```powershell
cd C:\Users\tonimontez\tm-skills
.\scripts\doctor.ps1
.\scripts\freshness-check.ps1
.\scripts\install.ps1 -WhatIf
git status --short --branch
```

### Story 2: Add Client Command Room Template To DTP

Status: implemented in Practice OS as `practice-os/templates/client-command-room-fit-assessment.md` and `practice-os/templates/client-command-room-spec.md`, and enforced by `dtp practice doctor`.

Value: converts the DeMario admin portal learning into a reusable pattern without prematurely building a client portal product.

Scope:

- Add a Practice OS template for command-room fit assessment.
- Add a template for owner dashboard, owner tasks, business roadmap, developer roadmap, and handoff/rules.
- Add a "checklist instead of portal" decision path.
- Keep support/verification panels placeholder-only until CLI evidence artifacts exist.

Source:

- `docs/CLIENT_COMMAND_ROOM_PATTERN.md`

Acceptance:

- A future agent can start a Mom nonprofit, Greg, Cam, or local-business command-room decision from the template.
- The template explicitly says when not to build a command room.
- Owner-facing and developer-facing surfaces stay separate.

### Story 3: Add Thin CI For Stable Local Gates

Status: implemented for the core-plus-map scope. DTP, consulting, and `tm-skills` now have thin CI workflows; `hub-prompts` runs its full local `npm test` gate; `hub-registry` runs CI-safe registry validation while full portfolio manifest validation remains a local gate until CI has explicit private sibling-repo access; Hub's existing CI/security workflows already cover the stable lane and were left in place.

Value: makes the existing local gates repeatable before hosted dashboards or support automation display them.

Updated input from Omnexus: PR `https://github.com/toniomon96/Omnexus/pull/553` proves the fuller version of this pattern with a shared toolkit registry, lock file, Docker-backed specialty tools, ignored `artifacts/verification/`, GitHub evidence upload, and Supabase migration drift/fresh-replay repair guard. For Sprint 2, use that as the reference implementation, but keep DTP/consulting/Hub CI thin until their local gates are stable.

First CI targets:

- DTP: `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor`.
- Consulting: `npm run build`, `npm run security:secrets`; route tests remain advisory until browser CI setup is intentionally expanded.
- Hub: existing CI/security workflows cover format, lint, build, typecheck, tests, CLI smoke, audit, and secret scanning.
- `tm-skills`: `.\scripts\doctor.ps1`, `.\scripts\freshness-check.ps1`.
- `hub-prompts`: `npm test`.
- `hub-registry`: CI runs `npm run validate`; local portfolio validation remains `npm test`.

Keep it thin:

- One workflow per repo is enough.
- Use exact local commands first.
- Save shared/reusable workflows for later.
- Mark browser, external-service, or dashboard checks as manual/advisory unless credentials are guaranteed.
- Add a registry/lock/artifact convention only when a repo has enough tools to justify it.
- Promote specialty Docker scanners from advisory to hard only after the baseline is stable and false positives are understood.

### Workspace Benefit Matrix

Every workspace repo benefits, but not every repo needs a CI change in this story.

| Repo | Improvement lane | Story 3 touch | Next gate |
|---|---|---|---|
| `diagnose-to-plan` | Practice OS, evidence contracts, redaction, hosted-DTP planning | Thin Python/Practice OS CI plus roadmap alignment | Review Phase 0 boundary and use proof/redaction templates on first pilot |
| `consulting` | Public storefront, proof surface, Hub intake path | Thin build and secret-scan CI | First redacted proof packet and optional route CI expansion |
| `hub` | Runtime intake, console records, health, prompts/runs | Existing CI/security reviewed; no churn | Prompt/registry cross-validation and v0.4 hardening |
| `tm-skills` | Global agent SDLC behavior across all repos | Thin Windows CI for doctor/freshness/install preview | Explicit install approval, tool reloads, discovery smoke tests |
| `engineering-playbook` | Doctrine, portfolio schemas, secret-management references | Alignment only; no duplicated roadmap ownership | Update only when general doctrine changes |
| `hub-prompts` | Prompt catalogue consumed by Hub | Workflow now runs full `npm test` | Add/evolve eval fixtures for high-value prompts |
| `hub-registry` | Hub automation target routing | Workflow keeps CI-safe registry validation; local `npm test` still validates sibling manifests | Cross-validate referenced prompt ids against `hub-prompts` and design private sibling-repo access for CI manifest checks |
| `fitness-app` / Omnexus | Reference verification cockpit and product proof track | No mutation because active branch has uncommitted work | Finish/review PR #553 and promote patterns only after permission/redaction |
| `demario-pickleball-1` | Client Command Room reference and local-business proof track | Alignment only; existing CI remains owner | Manual launch gates, venue rules, Node 24 maintenance |
| `FamilyTrips` | Private family planning app | Alignment only | Privacy-first `validate:data`, build, and tests before feature work |
| `dse-content` | Microsoft/internal readiness and workflow proof track | Alignment only | COI-aware internal proof and live-branch verification before any public reuse |

### Eventual Touch Roadmap By Repo

This is the master coverage queue. Each repo gets at least one explicit future pass, but the pass should match the repo's role.

| Repo | Eventual touch pass | Trigger | Output |
|---|---|---|---|
| `diagnose-to-plan` | Hosted DTP Phase 0 and proof/redaction governance | Current Sprint 2 sequence | Phase 0 design exists; first proof/redaction pilot next, later private app shell |
| `consulting` | Public proof upgrade and route/visual verification expansion | Proof packet and redaction queue exist | Receipt-style proof pages, noindex/admin checks, optional route CI |
| `hub` | Runtime hardening and prompt/registry consistency | After core CI is stable | v0.4 hardening notes, prompt id cross-validation, support checks |
| `tm-skills` | Global install and discovery smoke test | Explicit approval to run install | Installed/reloaded skills, discovery evidence, one canary decision |
| `engineering-playbook` | Doctrine refresh and pointer audit | After DTP Phase 0/proof contracts settle | Updated general doctrine only where DTP decisions should become reusable principles |
| `hub-prompts` | Prompt eval/golden fixture pass | After Hub cross-validation design | High-value prompt fixtures and versioning rules |
| `hub-registry` | Cross-repo prompt id and manifest validation pass | After private sibling-repo CI access is decided | Prompt id validation and safe manifest validation lane |
| `fitness-app` / Omnexus | Verification cockpit review and launch-stability pass | After active PR/branch work is human-reviewed | Merge/readiness decision, reusable verification lessons, redacted proof candidates |
| `demario-pickleball-1` | Launch/Command Room proof pass | After manual launch gates and permission are handled | Owner-safe proof packet, venue-routing maintenance, Node 24 CI maintenance |
| `FamilyTrips` | Privacy-first maintenance pass | Before adding features or AI/public sharing | Data validation/build/test status, privacy/data ownership notes, lightweight CI decision |
| `dse-content` | COI-aware internal proof and workflow maintenance pass | Before any DSE material is reused publicly or professionally | COI screen, redaction/permission notes, live-branch verification |

No repo should receive a platform-style build just to satisfy this table. A "touch" can be a verification pass, roadmap/doc alignment, CI maintenance, privacy review, proof packet, launch gate, or scoped feature plan.

### Story 4: Hosted DTP Phase 0 Schema And App Boundary

Status: implemented to the design-boundary only. `docs/HOSTED_DTP_PHASE_0.md` defines the private/single-operator app boundary, conceptual data contracts, import/export rules, and implementation gate. No hosted app, migrations, dashboard, MCP recall, or Supabase schema has been built yet.

Value: creates the private foundation for engagements, artifacts, redaction, and proof without pretending dashboards are ready.

Phase 0 scope:

- Auth: single-user/private auth boundary.
- Engagements: id, title, client/project alias, stage, sensitivity, created/updated.
- Artifacts: type, title, source, storage pointer, redaction status, proof eligibility.
- Evidence: repo, branch, commit, lane, result, commands, hard/advisory/manual gates.
- Redaction queue: artifact id, reviewer, status, notes, permission level.
- Proof queue: candidate artifact, public claim, caveat, permission, reviewer.

Out of scope:

- Client-facing portal.
- Multi-user SaaS.
- Deep Hub/DTP sync.
- Dashboards that do not read real artifacts.
- MCP recall.

Architecture rule:

- Keep CLI/local markdown import-export as a fallback.
- Use Hub for runtime intake/support records, not DTP engagement kits.
- Use DTP for practice methodology, artifact state, redaction, and proof governance.
- Use `decisions/0004-hosted-dtp-private-practice-os-boundary.md` as the accepted boundary decision.
- Use `practice-os/efficiency/diagnose-to-plan-repo-manifest.md` and `practice-os/efficiency/diagnose-to-plan-evidence-index.md` as the first Workspace Efficiency pilot artifacts.

### Story 5: Public Proof And Redaction Queue

Status: implemented to the template boundary. Practice OS now includes proof packet, redaction queue item, permission/reviewer checklist, evidence-source checklist, public claim review, and asset inventory templates. First real use is still pending.

Value: proof maturity is the business bottleneck. The site already has a good shell; the next lift is receipts.

Build first:

- Proof packet template. Done: `practice-os/templates/proof-packet.md`.
- Asset/redaction queue templates. Done: `practice-os/templates/asset-inventory.md` and `practice-os/templates/redaction-queue-item.md`.
- Permission/reviewer checklist. Done: `practice-os/templates/permission-reviewer-checklist.md`.
- Evidence-source checklist. Done: `practice-os/templates/evidence-source-checklist.md`.
- Public claim review. Done: `practice-os/templates/public-claim-review.md`.
- Consulting site proof backlog mapped to real source material.

Receipt-style proof packet fields:

- Baseline.
- After-state.
- Evidence source.
- Metric and caveat.
- Screenshots or walkthrough source.
- Redaction status.
- Permission level.
- Reviewer.
- Public claim.
- What stayed manual on purpose.

Do not publish:

- Private client records.
- Unreviewed Hub rows.
- DTP kit content.
- App Store/revenue/customer claims without source and caveat.
- Microsoft/client-adjacent proof without COI review.

## Repo Priorities

### DTP

Owns: practice OS, Client Operating Kits, COI, redaction, proof governance, verification spine, hosted DTP roadmap.

Next:

- Pilot the Client Command Room fit template on Mom nonprofit, Greg, Cam, or a local-business engagement before building a new portal surface.
- Add hosted DTP Phase 0 schema/design.
- Add proof/redaction queue templates.
- Add evidence import/export design.
- Keep `PRACTICE_PRODUCTION_ROADMAP.md` canonical.

Do not:

- Turn Hub into DTP.
- Deploy the local Workbench as hosted DTP.
- Add MCP recall before 2-3 real engagements make manual recall painful.

### `tm-skills`

Owns: cross-repo SDLC behavior for agents.

Next:

- Install/smoke only after explicit approval.
- Add one project-pinned canary after global discovery works.
- Add stack overlays only after base skills prove useful.

Do not:

- Add client records.
- Add a Phase 1 COI skill.
- Add tool execution scripts that bypass review.

### Consulting

Owns: public storefront, `/start`, public proof, noindex `/admin` command room.

Next:

- Keep Hub intake primary, Formspree fallback, email last.
- Add real proof packets only after redaction/permission.
- Keep Steel Ledger baseline.
- Verify `/admin` noindex and sitemap exclusion.
- Replace local DTP links with hosted DTP links only after hosted DTP exists.

Validation:

```powershell
npm run build
npm run test:routes
npm run security:secrets
```

### Hub

Owns: private runtime intake, console records, captures, runs, prompts, webhooks, health.

Next:

- Prioritize v0.4 hardening and CI.
- Keep runtime records separate from DTP engagement kits.
- Add prompt/registry cross-validation before deeper automation.
- Keep `/health`, protected-console, intake CORS, and Supabase migration status as support checks.

Do not:

- Become the DTP cockpit.
- Become a CRM/billing/client portal.
- Run higher-risk automations without consent/audit trail.

### `hub-prompts`

Owns: prompt catalogue consumed by Hub.

Next:

- Keep prompt frontmatter validated.
- Add or preserve golden/eval fixtures for high-value prompts.
- Version breaking prompt changes.
- Coordinate ids with `hub-registry`.

### `hub-registry`

Owns: prompt target routing.

Next:

- Add cross-repo validation that every referenced prompt id exists in `hub-prompts`.
- Keep sensitivity inheritance explicit.
- Avoid new scheduled automations until Hub runtime gates are trustworthy.

### `engineering-playbook`

Owns: general doctrine, templates, historical decisions, secret-management references.

Next:

- Keep pointing practice-production sequencing back to DTP.
- Update only when the general doctrine changes.

Do not:

- Revive it as the canonical roadmap.

### Omnexus / `fitness-app`

Owns: live AI fitness app, iOS/App Store readiness, subscription/entitlement loop, reference verification toolkit shape.

Priority:

- Post-launch stabilization and iOS/App Store proof.
- Subscription/IAP/Stripe safety.
- PR #553 verification cockpit is the concrete reference for the practice-wide CLI verification pattern: `tools:doctor`, `tools:matrix`, `tools:verify:local`, registry, lock file, Docker-backed scanners, evidence artifacts, and GitHub checks.
- Supabase local migration ordering repair is fixed on the PR branch with a narrow hash-pinned migration drift exception; keep that pattern as a one-time repair rule, not a normal migration-edit policy.
- Expired/demo account setup from actual query output, not assumptions.
- AI route cost/eval/entitlement controls.
- Merge PR #553 only after human review decides the draft is ready.

Do not:

- Let Omnexus become practice-platform work.
- Treat Sentry as a launch blocker if it has already been accepted as long-term ops.

### `demario-pickleball-1`

Owns: local business launch track and current Client Command Room reference.

Priority:

- Finish manual launch gates.
- Keep venue routing matrix current.
- Keep Sentry as post-launch unless Mario/Tonio make it mandatory.
- Move GitHub Actions to Node 24 before GitHub's 2026 runner transition dates.
- Use command-room screenshots/walkthroughs as proof only after permission.

### `FamilyTrips`

Owns: private family trip planning app.

Priority:

- Keep privacy model simple.
- Run data validation/build before adding features.
- Do not add AI or public sharing until data ownership/privacy rules are explicit.

Validation:

```powershell
npm run validate:data
npm run build
npm run test
```

### `dse-content`

Owns: internal Azure Apps/AI content, readiness/workflow surfaces, MSX/DSE automation.

Priority:

- Keep Microsoft/customer-adjacent work behind COI awareness.
- Continue only from live branch state.
- Treat DSE content as internal/professional proof only after permission and redaction.
- Do not fold this into public consulting offers without a DTP COI screen.

## What Still Needs Attention

- `tm-skills` global install and cross-tool smoke tests are still pending explicit approval.
- Prompt id cross-validation between `hub-prompts` and `hub-registry` is a small but valuable gap.
- `hub-registry` portfolio manifest validation still depends on sibling repo manifests that are available locally but not safely available to repo-scoped CI without explicit private-repo access.
- The Client Command Room templates now exist, but they still need a first pilot against Mom nonprofit, Greg, Cam, or another operator workflow.
- Hosted DTP Phase 0 now has a written schema/app boundary; it still needs review before implementation.
- Public proof now has asset/redaction/permission templates; it still needs first real use and reviewed source material.
- Agent-security research is now represented here; promote specific gates into implementation docs before any deeper autonomous workflows.
- Future Intelligence templates now exist as optional Practice OS assets, but they still need first real use before becoming required gates.
- Workspace Efficiency templates now exist as optional Practice OS assets, and DTP has the first repo-manifest/evidence-index pilot; the shape still needs review before expanding to other repos.

## Research Additions To Roadmap

### 1. Skills As A Cross-Tool Layer

Codex and Copilot both support skill folders with `SKILL.md`, and both use descriptions to decide when skills apply. Codex supports `$HOME/.agents/skills`, repo-scoped `.agents/skills`, and symlinked skill folders. Copilot supports project skills in `.github/skills`, `.claude/skills`, or `.agents/skills`, and personal skills in `~/.copilot/skills` or `~/.agents/skills`.

Roadmap impact:

- Keep `tm-skills` as a separate repo.
- Use `$HOME/.agents/skills` as the shared personal path.
- Keep descriptions precise.
- Avoid duplicate project-pinned skill names until global discovery is proven.
- Do not pre-approve shell execution for skills unless the script is reviewed and necessary.

Sources:

- https://developers.openai.com/codex/skills
- https://developers.openai.com/codex/guides/agents-md
- https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills

### 2. Eval-Driven Agent And Prompt Development

OpenAI's eval guidance reinforces that AI testing needs task-specific datasets, continuous evaluation, human calibration, and tool-selection/tool-argument checks for agents.

Roadmap impact:

- Add small JSONL/eval fixtures to Hub prompts, DTP operator Skills, and `tm-skills`.
- Prefer pass/fail, classification, tool-selection, and pairwise evals over open-ended vibe checks.
- Mine real misfires into eval cases.
- Add evals before multi-agent or autonomous workflows.

Source:

- https://developers.openai.com/api/docs/guides/evaluation-best-practices

### 3. MCP As A Later Integration Layer

MCP is now a broad standard for connecting AI applications to external data, tools, and workflows. The latest spec emphasizes resources, prompts, tools, consent, privacy, and tool safety.

Roadmap impact:

- Keep MCP recall later, not Sprint 2.
- Start with read-only DTP/Hub MCP surfaces only after artifacts/evidence/permissions exist.
- Treat MCP server descriptions and tool behavior as untrusted unless controlled.
- Require explicit consent before tool execution.

Sources:

- https://modelcontextprotocol.io/docs/getting-started/intro
- https://modelcontextprotocol.io/specification/2025-11-25

### 4. Agent Security Before Agent Autonomy

OWASP now has LLM, Agentic AI, and Agentic Skills security guidance. The Agentic Skills Top 10 specifically calls out skills as a vulnerable behavior layer between models and tools.

Roadmap impact:

- Add an "agent security review" gate before any workflow can write data, trigger external actions, or call high-impact tools.
- Use least agency: small tool scopes, explicit approval, reversible actions, and clear audit logs.
- Add memory poisoning, tool misuse, excessive agency, sensitive disclosure, and prompt injection checks to future Hub/DTP agent work.
- Keep global skills instruction-only until a script has a clear safety story.

Sources:

- https://owasp.org/www-project-top-10-for-large-language-model-applications/
- https://genai.owasp.org/initiatives/agentic-security-initiative/
- https://owasp.org/www-project-agentic-skills-top-10/

### 5. Simple Workflows Before Frameworks

Anthropic's agent guidance and 12-factor agents both point toward simple, composable workflows, clear tool interfaces, owned prompts/context, small focused agents, pause/resume, and human review.

Roadmap impact:

- Use deterministic workflows and DB state machines first.
- Add an agent framework only when the workflow has long-running state, branching, human review, or tool orchestration pain.
- Keep tools documented like product interfaces.
- Prefer workflow/routing/evaluator loops over open-ended agents for practice operations.

Sources:

- https://www.anthropic.com/engineering/building-effective-agents
- https://github.com/humanlayer/12-factor-agents

### 6. Typed Agent Frameworks As Optional Later Tools

Pydantic AI is a good candidate for Python-side typed agents/evals if DTP eventually needs code-owned orchestration, typed dependencies, structured output, MCP, human approval, and durable execution.

Roadmap impact:

- Add a research spike later, not now.
- Candidate fit: hosted DTP proof/redaction assistant, evidence classifier, or import/export validator.
- Start with the existing DTP CLI and Pydantic models before adopting a new framework.

Source:

- https://pydantic.dev/docs/ai/overview/

### 7. Durable Execution Only When Needed

LangGraph's durable execution is useful for long-running, interruptible, human-in-the-loop workflows with resumable state, but it requires determinism, idempotency, and side-effect discipline.

Roadmap impact:

- Use normal Postgres state for Hosted DTP Phase 0.
- Consider LangGraph only if proof/redaction/import workflows become long-running and hard to resume with simple state tables.

Source:

- https://docs.langchain.com/oss/python/langgraph/durable-execution

### 8. Observability: Design For It, Defer Heavy Tooling

OpenTelemetry has GenAI semantic conventions for events, exceptions, metrics, model spans, and agent spans. Langfuse/Phoenix-style tools add tracing/evals/prompt management, but they are valuable only once there are real agent/LLM workflows to inspect.

Roadmap impact:

- Add trace/eval ids to evidence schemas now.
- Defer Langfuse/Phoenix until hosted DTP or Hub has at least two meaningful LLM workflows with production-like usage.
- Prefer evidence artifacts and eval fixtures before hosted observability dashboards.

Sources:

- https://opentelemetry.io/docs/specs/semconv/gen-ai/
- https://langfuse.com/docs/observability/overview
- https://arize.com/docs/phoenix/

### 9. Microsoft Agent Governance Toolkit: Watch, Do Not Adopt Yet

Microsoft released an open-source Agent Governance Toolkit in April 2026 that maps to OWASP Agentic AI risks and includes policy enforcement, identity, runtime rings, SRE patterns, compliance, marketplace signing, and integrations.

Roadmap impact:

- Track this for Microsoft-adjacent governance thinking.
- Do not add it to Sprint 2.
- Consider a private spike only after DTP/Hub has a real autonomous agent with tool execution risk and COI clearance.

Source:

- https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/

### 10. OpenAI Agents SDK And Google ADK: Watch/Pilot Later

OpenAI Agents SDK has first-class concepts for agents, tools, handoffs, tracing, guardrails, and agent workflow evaluation. Google ADK similarly emphasizes building, evaluating, and deploying agents with multi-agent and graph-based workflows.

Roadmap impact:

- Keep current DTP/Hub flows as explicit workflows and state machines first.
- Add a small research spike only after hosted DTP has a real proof/redaction assistant or Hub has a real support/intake agent workflow.
- Require trace ids, eval cases, guardrail expectations, and rollback before any write-enabled agent runs.

Sources:

- https://developers.openai.com/api/docs/guides/agents
- https://developers.openai.com/api/docs/guides/agent-evals
- https://adk.dev/evaluate/

### 11. Context Engineering As Operating Discipline

Context engineering is the practice of curating the right information, tools, examples, state, and history for an agent at each step. It matters more as sessions become long-running and cross-repo.

Roadmap impact:

- Add repo context packs, compact handoffs, and agent session records before building recall automation.
- Treat context as a finite resource: prefer high-signal file paths, commands, receipts, and decisions over dumping everything into prompts.
- Use structured notes and just-in-time retrieval before persistent MCP recall.

Sources:

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://docs.langchain.com/oss/python/langchain/context-engineering

### 12. AG-UI And A2A Protocol Watchlist

AG-UI standardizes event-based interaction between agent backends and user-facing applications. A2A standardizes agent-to-agent communication. Both are useful to watch, but neither should drive Sprint 2 implementation.

Roadmap impact:

- Keep hosted DTP Phase 0 as a private app/data foundation, not an agent frontend experiment.
- Consider AG-UI only if DTP or Hub needs a real-time agent UI with state, tool progress, approvals, and resumable interactions.
- Keep A2A watch-only until there are multiple independent agents or vendors that genuinely need interoperability.

Sources:

- https://docs.ag-ui.com/introduction
- https://google-a2a.github.io/A2A/specification/

### 13. Red-Team And Guardrail Lab

Promptfoo, OpenAI guardrails/evals, OWASP, and NIST AI RMF point to the same practical rule: adversarial testing should exist before agentic systems touch sensitive data, external tools, or public user flows.

Roadmap impact:

- Add AI red-team plans before public AI workflows, write-enabled agents, support automation, or agentic client communication.
- Convert actual failures into eval fixtures and policy checks.
- Keep red-team reports internal unless sanitized and intentionally promoted into proof.

Sources:

- https://www.promptfoo.dev/docs/red-team/
- https://openai.github.io/openai-agents-python/guardrails/
- https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

### 14. Delivery Metrics, Release Trust, And Feature Flags

DORA metrics help assess delivery performance. OpenFeature provides a vendor-neutral feature-flag API. CycloneDX supports machine-readable supply-chain evidence. SLSA/OpenSSF-style release trust belongs on the roadmap, but only where repo risk justifies the overhead.

Roadmap impact:

- Add portfolio scorecards before dashboards.
- Use feature flags and kill switches for AI, billing, intake, client-facing, and automation features.
- Add SBOM/release-trust evidence first to higher-risk repos such as Omnexus, Hub, hosted DTP, and client-facing launch surfaces.

Sources:

- https://dora.dev/guides/dora-metrics/
- https://openfeature.dev/docs/reference/intro/
- https://cyclonedx.org/specification/overview/
- https://openssf.org/projects/slsa/

### 15. Research Radar Sources

A small research arm can stay lightweight by using curated, high-signal sources rather than building another platform.

Roadmap impact:

- Start with markdown research radar items and a weekly/monthly review rhythm.
- Use Hugging Face Papers for AI research discovery, OpenAlex for broader scholarly metadata, and official vendor/spec docs for implementation decisions.
- Classify each item as `Adopt`, `Pilot`, `Watch`, or `Reject`; anything marked `Adopt` still needs a repo-specific implementation plan.

Sources:

- https://huggingface.co/papers
- https://developers.openalex.org/api-reference/introduction

### 16. Workspace Command Center And Repo Manifests

Cross-repo work gets slower when every session has to rediscover repo purpose, local gates, CI shape, deploy target, and proof rules. A workspace command center plus repo manifests can make future sessions start from known truth.

Roadmap impact:

- Add a small manifest per repo before building workspace automation.
- Use the manifest to drive "what changed, what should run, what evidence exists" summaries.
- Keep implementation repo-local first; the command center should orchestrate, not own, each repo's rules.

Sources:

- https://docs.github.com/actions/concepts/workflows-and-actions/reusing-workflow-configurations
- https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching

### 17. Affected-Only Checks And Cache Hygiene

Nx and Turborepo both show the core efficiency pattern: use change detection and caching to avoid rerunning work that cannot be affected by the current change.

Roadmap impact:

- Start with explicit repo manifests and simple changed-file detection before adopting a framework.
- Keep full hard gates before release, proof promotion, or production-sensitive changes.
- Consider remote caching only for repos with repeated slow deterministic tasks.

Sources:

- https://nx.dev/docs/concepts/ci-concepts/reduce-waste
- https://turborepo.com/repo/docs/core-concepts/remote-caching

### 18. Dependency Maintenance And Toolchain Pinning

Dependency and toolchain drift can become silent drag. Renovate/Dependabot can group updates and create dashboards; `.tool-versions`, devcontainer/devbox notes, or equivalent setup docs can make new machines and CI less surprising.

Roadmap impact:

- Add dependency update policy before enabling broad automation.
- Use grouped updates and approval rules so maintenance does not flood the workspace.
- Pin tool versions where mismatches cause real failures: Node, Python, pnpm/npm, Supabase CLI, Vercel, and mobile/native tools.

Sources:

- https://docs.renovatebot.com/key-concepts/dashboard/
- https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates
- https://asdf-vm.com/guide/introduction.html

### 19. Project Starter Factory And Decision Logs

New projects should begin with the right operating baseline instead of rediscovering README, CI, launch checklist, proof, privacy, COI, and handoff structure each time.

Roadmap impact:

- Create starter templates after the Mom nonprofit/client pilot clarifies the baseline.
- Use lightweight decision records for architecture, security, public proof, dependency automation, and workflow choices.
- Keep starters modular so a private family app, public consulting surface, local-business client site, and AI product do not inherit the same unnecessary machinery.

Source:

- https://containers.dev/

## Parked Or Explicitly Later

- Multi-user SaaS.
- Public skill marketplace.
- Self-rewriting skills.
- Autonomous client communications.
- Auto-published proof.
- CRM replacement.
- Billing/e-signature integration.
- Deep Hub/DTP sync.
- MCP recall before real engagement volume.
- Client-side autonomous routines.
- Heavy load testing before load exists.
- Visual-regression SaaS before visual-regression pain exists.
- Self-learning without human review.
- Research automation that creates implementation work without acceptance.
- A2A/AG-UI/MCP protocol adoption before a real workflow needs it.
- Supply-chain ceremony in low-risk repos before the value is clear.
- Workspace command center that mutates repos before repo manifests and gates are trustworthy.
- Shared CI abstractions before at least three repos repeat the same stable pattern.
- Dependency bots without grouping, schedule, and human approval rules.
- Forced monorepo migration for repos that are intentionally separate.

## Recommended Next Execution Order From Here

1. Review and accept `docs/HOSTED_DTP_PHASE_0.md`, the proof/redaction templates, and the DTP repo-manifest/evidence-index pilot.
2. Run Mom nonprofit as the first Client Operating Kit pilot and use the Command Room fit assessment before deciding on a portal.
3. Use the proof/redaction templates on that pilot before anything moves to consulting proof.
4. Add prompt id cross-validation between `hub-prompts` and `hub-registry`.
5. Run the first adjacent-project touch pass: pick the repo whose trigger is ready first (`fitness-app`, `demario-pickleball-1`, `FamilyTrips`, or `dse-content`) and execute only its matching lane.
6. Use DeMario command room and Omnexus verification toolkit as proof/reference material only after permission/redaction review.
7. Start hosted DTP implementation only after the schema, evidence contract, redaction/proof queue, and DTP efficiency pilot are accepted.

Non-blocking intelligence track: use the optional Future Intelligence templates during the next real delivery/research sessions, but do not insert them ahead of hosted DTP Phase 0 or proof/redaction work.

Non-blocking efficiency track: pilot repo manifests and evidence indexes alongside the next DTP/Hub/consulting work, then draft the Workspace Command Center only after the manifest shape proves useful.
