# Practice System Audit And Gap Review

Status: hard scrutiny of the current consulting operating system.

Owner: `diagnose-to-plan`

Method: static inspection of the current workspace contracts, roadmap docs, visible repo status, and known verification lanes. This is not a full all-repo runtime audit. It is a system-design audit to identify the highest-value gaps before more platform surface is built.

## Executive Finding

The system is pointed in the right direction. DTP has become the source of truth for roadmap execution, prompt routing, steward review, hosted-DTP design, proof/redaction governance, and cross-workspace coverage. The biggest remaining risk is not lack of ideas. It is operational drift: too many valuable lanes can exist as docs unless the steward loop, evidence receipts, and proof gates are used in real work.

The next optimization should therefore make execution easier to continue without memory and should inspect the agent system itself, not only the roadmap artifacts:

1. Finish the Mom nonprofit private kit with real facts.
2. Use the proof/redaction templates on one real claim.
3. Expand repo manifests only when the next repo lane is touched.
4. Cross-validate Hub prompts and registry before deeper Hub work.
5. Keep hosted DTP implementation gated until there are real records to persist.
6. Run agentic performance gap reviews when a session exposes a missed routing, context, skill-trigger, verification, research, safety, or learning-loop behavior.

## What Is Strong

| Strength | Why It Matters |
|---|---|
| DTP source of truth is clear | Prevents consulting, Hub, and project repos from duplicating roadmap ownership |
| Kanban backlog exists | Turns the roadmap into epics, stories, statuses, Done gates, and next actions |
| Activation map exists | Future agents can route prompts to skills, templates, gates, and repo lanes |
| Agentic performance gap review now exists | Future audits check whether the agent system routed, remembered, validated, researched, and learned correctly |
| Story activation index exists | Roadmap stories can suggest the right skill, template, agent role, and gate |
| Roadmap Steward loop exists | Reduces dependence on Toni's memory for next story, blockers, and repo coverage |
| Hosted DTP Phase 0 boundary exists | Prevents a dashboard-first app with no real artifacts |
| Proof/redaction templates exist | Public proof can become evidence-backed instead of vibe-based |
| `tm-skills` exists as a separate repo | Reusable SDLC behavior can help every repo without folding into DTP |
| Omnexus verification cockpit is a reference | Gives a concrete pattern for doctor/matrix/evidence/toolkit design |
| Consulting/Hub/DTP boundaries are documented | Keeps public site, runtime intake, and private methodology separate |

## Severity Model

- `P0`: blocks safe execution or can cause public/private boundary failure.
- `P1`: high-value reliability, proof, or execution gap.
- `P2`: useful improvement after current pilot path is stable.
- `P3`: later optimization or optional automation.

## Findings

### P0-1: Public Proof Is Still The Main Business Bottleneck

Evidence: the roadmap, consulting docs, and proof templates all identify proof maturity as the remaining public-facing gap.

Impact: the public site can explain the offer, but the strongest trust signal still depends on real receipts: before/after, metrics, screenshots, decisions, caveats, and permission.

Fix: run the proof packet and redaction queue on one real claim before expanding public proof pages.

Owner: `diagnose-to-plan` first, then `consulting` once approved.

Follow-up story: First proof/redaction pilot.

### P0-2: Private Engagement Durability Is Not Fully Proven

Evidence: `engagements/` is intentionally ignored, and the Mom nonprofit kit lives locally. `dtp vault` exists, but private remote durability is still a separate decision.

Impact: private client work is correctly kept out of the public repo, but durable backup and recovery need an explicit private path before relying on it for real delivery history.

Fix: decide when to initialize a private vault and private remote for real engagement material.

Owner: `diagnose-to-plan`.

Follow-up story: Private Kit Durability.

### P0-3: Hosted DTP Must Not Become Dashboard Theater

Evidence: hosted DTP Phase 0 is documented, but implementation is intentionally gated.

Impact: a hosted app built before real records exist could duplicate docs, create stale state, and distract from proof and delivery.

Fix: keep app implementation blocked until the Mom pilot or another real workflow produces engagement, artifact, evidence, redaction, proof, and decision records worth persisting.

Owner: `diagnose-to-plan`.

Follow-up story: Hosted DTP implementation readiness review.

### P1-1: Hub Prompt/Registry Cross-Validation Is A Small But Important Drift Risk

Evidence: `hub-prompts` owns prompt content, `hub-registry` owns automation targets, and Hub owns runtime usage. These are intentionally separate, but separation creates drift risk.

Impact: Hub could route to stale prompt ids or assume prompt behavior that changed in the catalog.

Fix: add a cross-validation story that checks registry references against prompt ids without forcing private sibling access into repo-scoped CI.

Owner: `hub-prompts`, `hub-registry`, and `hub`.

Follow-up story: Prompt id cross-validation.

### P1-1A: Agentic Performance Gaps Need A Standing Review

Evidence: Toni identified a specific design gap: contextual awareness and skill/agent activation should happen progressively from prompt intent, roadmap stories, and new ideas. If that gap had to be caught by Toni, the system needs a repeatable review that asks what else failed to route, remember, validate, research, protect, or learn.

Impact: without this layer, the architecture can look complete while future agent sessions still depend on Toni's memory to catch misroutes and missing process.

Fix: require `practice-os/templates/agentic-performance-gap-review.md`, document the lens in `docs/PRACTICE_SYSTEM_AGENTIC_PERFORMANCE_GAP_REVIEW.md`, and convert confirmed misses into activation-map updates, evals, `tm-skills` trigger fixes, research radar items, decision records, or backlog stories.

Owner: `diagnose-to-plan`, with `tm-skills` owning reusable SDLC trigger/eval fixes.

Follow-up story: Agentic Performance Gap Review V0.

### P1-2: `tm-skills` Activation Needs Cross-Tool Smoke Verification

Evidence: the skills repo exists, safe checks pass, and global install was explicitly approved and applied on 2026-04-30 without `-Force`. The current session cannot fully verify external Claude Code and GitHub Copilot reload/discovery behavior.

Impact: prompt-routing docs can point to skills and the global discovery paths now exist, but cross-tool behavior still depends on reload and smoke prompts.

Fix: reload Codex, Claude Code, and GitHub Copilot, run the smoke prompts, and record any misses in `tm-skills/MISFIRES.md`, trigger evals, or the DTP activation map.

Owner: `tm-skills`.

Follow-up story: Tool reload smoke test.

### P1-3: Repo Manifests And Evidence Indexes Exist Only As A DTP Pilot

Evidence: DTP has the first manifest/evidence-index pilot, while consulting, Hub, and `tm-skills` are ready but not yet expanded.

Impact: future agents still need to rediscover repo purpose and gates outside DTP unless their repo lanes have local manifests.

Fix: expand manifests to consulting, Hub, and `tm-skills` when those lanes are touched.

Owner: each repo, coordinated by DTP.

Follow-up story: Repo manifest expansion.

### P1-4: Roadmap Steward Is Manual

Evidence: steward template and roadmap lane exist; `dtp steward review` is intentionally later.

Impact: the process solves memory burden only if future sessions actually run the template and update receipts.

Fix: use steward review around major roadmap sessions; build CLI drift reporting only after repeated manual use proves the checks.

Owner: `diagnose-to-plan`.

Follow-up story: `dtp steward review` command.

### P1-5: Documentation Propagation Is Not Yet Local To Every Repo

Evidence: DTP owns the master docs, but secondary repos do not all have local pointers to the system architecture.

Impact: a future agent starting in a project repo may miss DTP's current rules unless it checks workspace docs or memory.

Fix: add lightweight local pointers during each repo touch pass, not as a bulk edit.

Owner: DTP plus each repo during its lane.

Follow-up story: Documentation propagation lane.

### P1-6: FamilyTrips Needs A Privacy-First Maintenance Pass

Evidence: FamilyTrips is on the roadmap, but the quick workspace review found less local roadmap surface than core repos.

Impact: private family data and travel coordination need explicit validation/build/privacy rules before new feature or AI work.

Fix: create a privacy-first repo touch pass before adding AI or public sharing.

Owner: `FamilyTrips`.

Follow-up story: FamilyTrips privacy maintenance pass.

### P1-7: DSE Needs COI-Aware Proof Handling

Evidence: `dse-content` is Microsoft-adjacent and has internal/professional proof potential, but public use requires COI, permission, and redaction.

Impact: useful professional evidence could create conflict or confidentiality risk if promoted too casually.

Fix: keep DSE as internal/professional proof only until a COI screen, permission review, and redaction pass are complete.

Owner: `dse-content` plus DTP COI/proof process.

Follow-up story: DSE COI-aware proof pass.

### P2-1: Omnexus Verification Cockpit Is A Reference, Not A Shared Platform

Evidence: Omnexus has a fuller toolkit registry/evidence pattern than the rest of the workspace.

Impact: copying it wholesale into every repo would create unnecessary overhead, but ignoring it would waste a proven pattern.

Fix: extract only the pattern into DTP docs and use thin repo-local gates until a repo needs a cockpit.

Owner: `fitness-app` as reference; DTP as pattern owner.

Follow-up story: Omnexus verification cockpit review.

### P2-2: DeMario Command Room Needs Permissioned Proof Before Public Use

Evidence: DeMario is the command-room reference, but client/public proof still requires permission and launch context.

Impact: screenshots or workflows could be useful proof but should not be published without owner-safe review.

Fix: use it as an internal pattern now; public proof only after launch/permission/redaction.

Owner: `demario-pickleball-1`, DTP proof process, consulting public site.

Follow-up story: DeMario proof packet.

### P2-3: Future Intelligence Templates Need First Real Use

Evidence: templates exist for lessons, research radar, portfolio scorecards, flight records, red-team plans, feature flags, and supply-chain baselines.

Impact: templates will not compound unless actual sessions produce receipts and eval candidates.

Fix: capture the first agent flight record and first research radar item during the next complex session that produces reusable learning.

Owner: `diagnose-to-plan`.

Follow-up story: First agent flight record.

### P2-4: Supply Chain And Red-Team Tooling Should Stay Risk-Based

Evidence: release trust, SBOMs, OpenSSF, CodeQL/Semgrep, and Promptfoo-style red teaming are on the roadmap.

Impact: broad rollout too early creates ceremony and alert fatigue; delaying too long creates risk for AI, billing, intake, and production automation.

Fix: apply first to higher-risk repos and workflows: Omnexus, Hub, hosted DTP, consulting intake/proof, and client-facing launch surfaces.

Owner: repo-specific.

Follow-up story: AI red-team and release trust pilot.

### P3-1: Agent Protocols Are Watch Items

Evidence: AG-UI, A2A, MCP recall, OpenAI Agents SDK, Google ADK, Temporal, and LangGraph are intentionally later.

Impact: adopting a framework before workflow pain exists would add complexity.

Fix: keep watch/spike status until DTP or Hub has real long-running, stateful, approval-heavy workflows.

Owner: DTP Future Intelligence lane.

Follow-up story: protocol/tool spike later.

## Cross-Repo Coverage Check

| Repo | Covered In Roadmap | Needs Later Local Touch |
|---|---:|---|
| `consulting` | yes | proof and local pointer |
| `diagnose-to-plan` | yes | ongoing source of truth |
| `hub` | yes | prompt/registry validation and local pointer |
| `engineering-playbook` | yes | pointer audit |
| `hub-prompts` | yes | prompt eval/cross-validation |
| `hub-registry` | yes | registry cross-validation |
| `fitness-app` | yes | reference extraction/proof after branch review |
| `FamilyTrips` | yes | privacy maintenance pass |
| `demario-pickleball-1` | yes | manifest/evidence index done; command-room proof pass still later |
| `dse-content` | yes | COI-aware proof pass |
| `tm-skills` | yes | cross-tool reload smoke tests |

## Audit Conclusion

No major roadmap concept needs to be removed. The system is expansive, but it is not chaotic because the current docs now separate:

- source of truth from local repo docs
- roadmap from backlog
- routing from autonomy
- proof governance from public publishing
- hosted design from hosted implementation
- pattern extraction from bulk repo mutation

The biggest improvement is to make the next real work leave receipts. The system will become trustworthy when every meaningful delivery produces evidence, a decision, a steward note, a proof/redaction update, or an eval candidate.
