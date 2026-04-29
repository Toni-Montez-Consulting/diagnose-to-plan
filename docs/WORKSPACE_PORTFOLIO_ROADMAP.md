# Workspace Portfolio Roadmap

Last updated: 2026-04-29

This plan consolidates the current consulting workspace, prior direction, live repo evidence, and current agentic-AI/development research into one prioritized execution map.

The practical thesis is:

1. Make every future agent session better.
2. Make every repo's delivery state observable.
3. Turn real delivery evidence into proof.
4. Build hosted/private surfaces only when they connect to real artifacts.
5. Add deeper agent automation only after permissions, evals, evidence, and human-review gates exist.

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

The first two items are now implemented to the intended boundary: `tm-skills` is activated through remote/push/dry-run checks, and the Client Command Room templates exist in Practice OS. The next active item is thin CI.

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

An item should be delayed or cut if it mostly creates:

- A prettier dashboard with no connected evidence.
- A portal where a checklist would work.
- Agent autonomy before consent, logging, and rollback.
- Duplicate state between DTP, Hub, and project repos.
- New framework complexity before a workflow has proven pain.

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

Status: implemented for the core-plus-map scope. DTP, consulting, and `tm-skills` now have thin CI workflows; `hub-prompts` and `hub-registry` workflows run their full local `npm test` gates; Hub's existing CI/security workflows already cover the stable lane and were left in place.

Value: makes the existing local gates repeatable before hosted dashboards or support automation display them.

Updated input from Omnexus: PR `https://github.com/toniomon96/Omnexus/pull/553` proves the fuller version of this pattern with a shared toolkit registry, lock file, Docker-backed specialty tools, ignored `artifacts/verification/`, GitHub evidence upload, and Supabase migration drift/fresh-replay repair guard. For Sprint 2, use that as the reference implementation, but keep DTP/consulting/Hub CI thin until their local gates are stable.

First CI targets:

- DTP: `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor`.
- Consulting: `npm run build`, `npm run security:secrets`; route tests remain advisory until browser CI setup is intentionally expanded.
- Hub: existing CI/security workflows cover format, lint, build, typecheck, tests, CLI smoke, audit, and secret scanning.
- `tm-skills`: `.\scripts\doctor.ps1`, `.\scripts\freshness-check.ps1`.
- `hub-prompts`: `npm test`.
- `hub-registry`: `npm test`.

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
| `diagnose-to-plan` | Practice OS, evidence contracts, redaction, hosted-DTP planning | Thin Python/Practice OS CI plus roadmap alignment | Hosted DTP Phase 0 schema/app boundary |
| `consulting` | Public storefront, proof surface, Hub intake path | Thin build and secret-scan CI | Proof/redaction queue and optional route CI expansion |
| `hub` | Runtime intake, console records, health, prompts/runs | Existing CI/security reviewed; no churn | Prompt/registry cross-validation and v0.4 hardening |
| `tm-skills` | Global agent SDLC behavior across all repos | Thin Windows CI for doctor/freshness/install preview | Explicit install approval, tool reloads, discovery smoke tests |
| `engineering-playbook` | Doctrine, portfolio schemas, secret-management references | Alignment only; no duplicated roadmap ownership | Update only when general doctrine changes |
| `hub-prompts` | Prompt catalogue consumed by Hub | Workflow now runs full `npm test` | Add/evolve eval fixtures for high-value prompts |
| `hub-registry` | Hub automation target routing | Workflow now runs full `npm test` | Cross-validate referenced prompt ids against `hub-prompts` |
| `fitness-app` / Omnexus | Reference verification cockpit and product proof track | No mutation because active branch has uncommitted work | Finish/review PR #553 and promote patterns only after permission/redaction |
| `demario-pickleball-1` | Client Command Room reference and local-business proof track | Alignment only; existing CI remains owner | Manual launch gates, venue rules, Node 24 maintenance |
| `FamilyTrips` | Private family planning app | Alignment only | Privacy-first `validate:data`, build, and tests before feature work |
| `dse-content` | Microsoft/internal readiness and workflow proof track | Alignment only | COI-aware internal proof and live-branch verification before any public reuse |

### Story 4: Hosted DTP Phase 0 Schema And App Boundary

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

### Story 5: Public Proof And Redaction Queue

Value: proof maturity is the business bottleneck. The site already has a good shell; the next lift is receipts.

Build first:

- Proof packet template.
- Asset/redaction queue template.
- Permission/reviewer checklist.
- Evidence-source checklist.
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
- The Client Command Room templates now exist, but they still need a first pilot against Mom nonprofit, Greg, Cam, or another operator workflow.
- Hosted DTP Phase 0 needs a written schema/app boundary before code.
- Public proof has a strong shell but needs asset/redaction/permission queue discipline.
- Agent-security research is now represented here; promote specific gates into implementation docs before any deeper autonomous workflows.

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

## Recommended Next Execution Order From Here

1. Draft hosted DTP Phase 0 schema/app-boundary doc.
2. Add proof packet and redaction queue templates.
3. Run Mom nonprofit as the first Client Operating Kit pilot and use the Command Room fit assessment before deciding on a portal.
4. Add prompt id cross-validation between `hub-prompts` and `hub-registry`.
5. Use DeMario command room and Omnexus verification toolkit as proof/reference material only after permission/redaction review.
6. Start hosted DTP implementation only after the schema, evidence contract, and redaction/proof queue are accepted.
