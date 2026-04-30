# FAOS Orchestration Roadmap

Status: planning integration and technical review, not implementation.

Owner: `diagnose-to-plan`

Source spec: `C:\Users\tonimontez\Downloads\FAOS_BUILD_SPEC_v1.md`

Purpose: merge the Frontier Agentic Operating System idea into the DTP master roadmap, Kanban backlog, and agent-management planning without replacing the current Practice OS. FAOS is a future orchestration substrate candidate. DTP remains the practice source of truth.

## Boundary

FAOS should not start by creating another platform that competes with DTP, Hub, consulting, or `tm-skills`.

Current ownership stays intact:

| Layer | Current Owner | FAOS Relationship |
|---|---|---|
| Practice roadmap, client kits, proof, COI, redaction, stewarding | `diagnose-to-plan` | FAOS reads and automates around these contracts later |
| Global reusable SDLC behavior | `tm-skills` | FAOS may route to skills and eval them later; it should not duplicate the skill repo |
| Public site and proof | `consulting` | FAOS may supply evidence and traces later; consulting publishes only reviewed proof |
| Intake/runtime records | `hub` | FAOS may observe or call Hub later; Hub does not become FAOS memory |
| Product/client repos | project repos | FAOS touches each repo only through accepted story gates |

No FAOS implementation is approved by this document. Do not create `C:\Users\tonimontez\code\faos`, install services, modify DTP tracing, add MCP servers, or change Claude/Codex settings until the readiness review gate is accepted.

## Fit With Existing Practice System

The build spec is directionally strong because it formalizes the exact pressure Toni identified: agents should remember the roadmap, route prompts to the right skills, produce evidence, learn from misses, and escalate only through gates.

It also overlaps with work that already exists in DTP:

- Activation Routing Map: prompt-to-process routing.
- Roadmap Steward Loop: current story, repo lane, gate, blocker, and follow-up continuity.
- Agentic Performance Gap Review: recurring audit of routing, context, skill trigger, verification, research, safety, and learning misses.
- Future Intelligence Layer: lessons, research radar, eval candidates, flight records, and supervised learning.
- Workspace Efficiency Layer: repo manifests, evidence indexes, command-center planning, dependency maintenance, and starter baselines.
- `tm-skills`: installed cross-repo SDLC skills and trigger evals.

FAOS should become the future technical substrate under those contracts, not a second operating model.

## Eleven-Layer Mapping

| FAOS Layer | Keep / Improve / Defer | DTP-Aligned Interpretation |
|---|---|---|
| L1 Specification and Intent: Spec-Kit + constitution | Improve, then pilot | Use only after a readiness review. Map Spec-Kit to DTP Work Item Specs, Contextual Idea Intake, and story activation. Do not let a FAOS constitution override DTP safety, privacy, COI, or roadmap gates. |
| L2 Capability Units: skills + eval fixtures | Keep and improve | `tm-skills` already owns global SDLC skills. Add eval thresholds, misfire capture, and promotion rules before adding more skills. DTP practice skills stay in DTP. |
| L3 Execution Contexts: subagents, hooks, commands | Defer to gated pilot | Useful later for code-review/test/eval/trace roles. Hooks are powerful but must be path-scoped, reversible, and redaction-aware before they can enforce edits or outbound actions. |
| L4 Tool Integration: internal MCP servers | Defer | MCP remains later. Start with read-only, repo-local, least-privilege tools and only after artifact/evidence boundaries are accepted. |
| L5 Memory: Mem0 + Letta + Postgres | Defer with design corrections | DTP already has steward receipts, flight records, repo manifests, and private kits. Add persistent memory only after redaction, classification, trace schema, and retention rules exist. |
| L6 Trace and Observability: Langfuse | Defer with design corrections | The trace thesis is right. Implement after defining what may be traced, redacted, sampled, retained, and linked to evidence. |
| L7 Eval Harness: Inspect AI | Pilot later | Strong candidate for skill/agent evals after there are enough real misfires and fixtures. Keep current lightweight evals first. |
| L8 Self-Improvement: DSPy/GEPA | Later, supervised only | Use only after traces and evals exist. Reflection may propose skill changes; humans approve them. No self-modifying skills. |
| L9 Durable Execution: Inngest/DBOS | Later | Useful when workflows span hours/days or machine restarts. Keep simple Postgres state first for hosted DTP Phase 0. |
| L10 Sandboxes: E2B/Daytona/Browserbase | Later | Add only when untrusted execution or browser automation needs isolation beyond current Playwright/browser workflows. |
| L11 Operator Orchestrator: DTP + `op` | Improve carefully | DTP remains the operating brain. An `op` wrapper is allowed only if it reduces real repeated friction and reads DTP contracts rather than replacing them. |

## Technical Soundness Review

Verdict: adopt the FAOS architecture as a long-term orchestration thesis, but do not run the Phase 0 prompt as written. It needs a preflight correction pass first.

### Strong And Aligned

- Layered architecture is a good way to prevent a single "agent manager" blob.
- "One operator, many tools" aligns with the current DTP steward model.
- Local-first and cloud-later matches the hosted DTP and private-kit boundary.
- Hooks versus skills is a useful distinction: enforcement belongs in hooks/gates, persuasion belongs in skills.
- Explicit promotion and ADRs match the current `tm-skills` and DTP decision-record pattern.
- Trace/eval/lesson loops align with Future Intelligence and Agentic Performance Gap Review.
- Business-agent prediction scoring is valuable later because business work lacks simple pass/fail signals.

### Must Correct Before Implementation

1. Langfuse v3 is not a two-container Postgres-only compose stack. The official self-hosted architecture uses Langfuse web, Langfuse worker, Postgres, ClickHouse, Redis/Valkey, and S3/blob storage components. A Phase 0 compose file must be built from the current official compose, not the simplified spec snippet.

2. The spec's `pip install mem0ai letta` conflicts with the stated `uv`-only package rule. Implementation must use `uv add`, `uv run`, `uvx`, or service containers.

3. "Mem0 + Letta on the same Postgres instance" should mean the same Postgres server with separate databases or schemas, explicit extensions, and isolated migrations. Do not point both tools at one unpartitioned database and hope migrations do not collide.

4. Mem0 self-hosting may require more than Postgres, depending on the chosen mode. Current docs and deployment examples include pgvector and may include Neo4j or other provider-specific services. Verify the minimum local stack before writing compose.

5. Letta Postgres configuration and server command must be verified against current docs. Do not hard-code the spec command until the current supported env vars and CLI are confirmed.

6. "Every Claude Code session produces a trace" is not guaranteed by FAOS alone. It likely requires Claude Code hooks, SDK wrappers, or external session instrumentation. Treat this as a manual acceptance gate until the exact integration is proven.

7. The Phase 0 prompt says not to modify DTP but also requires `dtp draft` to emit Langfuse traces. That is a boundary conflict. Either Phase 0 only instruments `op`, or a separate DTP adapter story must be accepted.

8. Raw traces can leak prompts, tool args, file paths, private client facts, secrets, and Microsoft-adjacent context. Trace capture needs a redaction and sensitivity policy before "everything writes to traces."

9. Spec-Kit flags and integration names are current enough to be promising, but implementation must run `specify integration list` and `specify init --help` before hard-coding commands.

10. The spec's `compliance-coi` global skill conflicts with the current DTP decision to keep COI in DTP, not `tm-skills` Phase 1. FAOS may call a DTP COI hook later; it should not create a broad global COI skill yet.

11. "Latest" dependency pins are not acceptable for an operating substrate. Use lockfiles, explicit tags, checked compose versions, and ADRs for deviations.

12. "CONSTITUTION.md is the only document that can override per-task instructions" is too broad. A FAOS constitution can govern the FAOS repo, but it cannot override DTP privacy, COI, proof, hosted implementation, repo-boundary, or user approval gates.

13. The `~/code/faos` path should be normalized for this Windows workspace as `C:\Users\tonimontez\code\faos` if implementation is approved.

14. The 89 percent multi-agent convergence claim is useful as a design intuition, but it is not cited in the provided spec. Treat it as an internal thesis until sourced or removed from acceptance logic.

## Phase Plan

### Phase -1: Roadmap Capture

Status: implemented by this planning pass.

Done gate:

- DTP has this roadmap.
- The Kanban backlog has a FAOS epic and gated stories.
- The activation map routes FAOS prompts to readiness review instead of direct implementation.
- The master roadmap keeps all prior priorities intact.

### Phase 0A: FAOS Readiness Review

Status: Ready, not active.

Purpose: convert the build spec into an executable, corrected implementation plan.

Required outputs:

- Completed `practice-os/templates/faos-phase-readiness-review.md`.
- Decision on separate `faos` repo versus DTP extension. Default: separate `C:\Users\tonimontez\code\faos` repo if approved.
- Corrected compose architecture for Langfuse v3 and memory services.
- Trace schema and redaction policy.
- DTP trace integration boundary decision.
- COI hook boundary decision.
- Spec-Kit CLI command verification.
- Dependency version pinning plan.
- Acceptance checklist rewritten to remove impossible or conflicting gates.

Do not proceed to FAOS Phase 0 implementation until this review is accepted.

### Phase 0B: Foundation Implementation

Status: Later, gated.

Candidate scope if approved later:

- Initialize `faos` repo on a branch.
- Add Spec-Kit or equivalent spec-driven flow after CLI verification.
- Stand up corrected local services.
- Add minimal `op` CLI.
- Add memory MCP only after the storage model and redaction policy are accepted.
- Add tracing only for approved `op` and wrapper flows first.
- Keep DTP modifications in a separate story.

### Phase 1+: Later Build Sequence

Keep the FAOS phase names as future stories, but gate each phase behind real need:

| Phase | DTP Roadmap Status | Gate |
|---|---|---|
| 1. Spec-driven flow | Later | At least one project story proves Work Item Spec is too light |
| 2. Code agent stack | Later | Skill triggers and review/test workflows have eval fixtures |
| 3. Eval harness | Later | Enough real skill/agent misfires exist to seed Inspect AI |
| 4. Self-improvement | Later | Traces and evals exist; human review queue is trusted |
| 5. Durable execution | Later | A workflow must survive sleep/crash or run for days |
| 6. Cross-project propagation | Later | Multiple project-local skills have promotion candidates |
| 7. Business agent stack | Later | Discovery/proposal workflows are repeatable and privacy-gated |
| 8. Predictive/calibration | Later | Business agents emit repeatable judgments worth scoring |
| 9. Cloud migration | Later | Local stack hits explicit pain or collaboration threshold |

## Implementation Acceptance Rewrite

Before any FAOS Phase 0 build prompt is accepted, these gates must be true:

- [ ] Phase 0A readiness review is complete and accepted.
- [ ] Langfuse compose architecture is corrected against current official docs.
- [ ] Mem0 and Letta storage model is isolated and migration-safe.
- [ ] `uv`-only package flow is documented.
- [ ] DTP tracing conflict is resolved as either "op only" or "separate DTP adapter story."
- [ ] Trace redaction/sensitivity policy is accepted.
- [ ] Spec-Kit commands are verified from current CLI help.
- [ ] COI stays DTP-owned unless a new decision explicitly changes that.
- [ ] No Microsoft/customer/day-job or sensitivity-tier-3 paths are read or traced.
- [ ] No global install, public proof, hosted DTP implementation, or autonomous repo mutation is implied by FAOS work.

## Value Standard

FAOS components should be adopted only when they improve at least one of:

- agent routing accuracy
- context durability
- verification quality
- research-to-roadmap quality
- proof safety and evidence quality
- cross-repo delivery speed
- business workflow reliability
- reduction in Toni's memory burden

Delay or reject a component if it mostly adds ceremony, duplicates DTP, hides repo boundaries, captures sensitive data without redaction, or creates an operator dashboard with no real workflow behind it.

## Sources Reviewed

- FAOS build spec: `C:\Users\tonimontez\Downloads\FAOS_BUILD_SPEC_v1.md`
- Langfuse self-hosting: https://langfuse.com/self-hosting
- Langfuse Docker Compose deployment: https://langfuse.com/self-hosting/deployment/docker-compose
- Mem0 self-hosting: https://docs.mem0.ai/open-source/setup
- Mem0 pgvector docs: https://docs.mem0.ai/components/vectordbs/dbs/pgvector
- Letta self-hosting: https://docs.letta.com/guides/server/docker
- GitHub Spec-Kit integrations: https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md
- Claude Agent SDK Python reference: https://docs.claude.com/en/docs/agent-sdk/python
- OpenTelemetry GenAI semantic conventions: https://opentelemetry.io/docs/specs/semconv/gen-ai/
- MCP specification: https://modelcontextprotocol.io/specification/2025-11-25/basic
- Inspect AI: https://inspect.aisi.org.uk/
- DBOS docs: https://docs.dbos.dev/
- Inngest durable execution docs: https://www.inngest.com/docs/learn/how-functions-are-executed
