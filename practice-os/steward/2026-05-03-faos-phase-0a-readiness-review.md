---
data_class: P0
confidential: false
permission_level: internal_only
review_status: checked
---

# FAOS Phase 0A Readiness Review

## Phase

- Phase: FAOS Phase 0A readiness review
- Source spec section: FAOS Phase 0 / orchestration substrate
- Proposed branch: none yet
- Proposed repo: future `C:\Users\tonimontez\code\faos` if accepted later
- Requested by: Toni
- Review date: 2026-05-03

## Intended Capability

- What the operator should be able to do after this phase: decide whether a
  future FAOS repo, `op` wrapper, trace store, memory substrate, Spec-Kit flow,
  and eval harness are worth implementing.
- Which current pain this solves: agents need better context durability,
  routing, verification evidence, misfire learning, and guarded orchestration.
- Which DTP roadmap item or backlog story owns it: Epic 12, FAOS Agentic
  Orchestration Substrate.

## Existing Equivalent

| Proposed FAOS component | Existing DTP / tm-skills / Hub / repo equivalent | Reuse, improve, replace, or defer |
|---|---|---|
| Spec-driven flow | DTP Work Item Spec, Context Pack, Story Activation Contract | improve later |
| Skills | `tm-skills` plus DTP Practice OS skills | reuse |
| Memory | DTP steward receipts, memory status, source indexes, private kits | improve, do not replace |
| Tracing | evidence indexes, verification receipts, Hub runtime logs | defer until redaction policy exists |
| Eval harness | consulting-intelligence fixtures, `tm-skills` misfires | improve after more real cases |
| Durable execution | hosted DTP records, future queue possibilities | defer |
| Operator wrapper | DTP CLI and Hub CLI/runtime surfaces | pilot only if repeated friction appears |

## Technical Accuracy Check

| Item | Current-source verification | Result | Correction needed |
|---|---|---|---|
| Langfuse service topology | 2026-05-03 docs say self-hosting uses Langfuse Web, Langfuse Worker, Postgres, ClickHouse, Redis/Valkey, S3/blob storage, and optional LLM gateway | pass | do not use simplified Postgres-only compose |
| Langfuse Docker Compose fit | Docker Compose is documented for local/VM and low-scale testing, without HA/scaling/backup guarantees | pass | treat as local pilot only |
| Mem0 local stack | docs describe bundled Postgres/pgvector overrides and `make up` / `make bootstrap` stack | pass | isolate from DTP and Letta databases |
| Letta Postgres | docs say `LETTA_PG_URI` can connect to external Postgres and requires pgvector | pass | use separate DB/schema and migration ownership |
| Spec-Kit install/integration | GitHub docs recommend `uv tool install` or `uvx` from the official repo and list Codex integration support | pass | pin a release tag before implementation |
| CLI flags and install commands | current docs are promising, but no local CLI was installed or run in this review | unknown | verify `specify version`, `specify init --help`, and `specify integration list` before build |
| Tracing/telemetry path | no verified Claude/Codex automatic trace path exists in DTP yet | unknown | start with `op` wrapper traces only, if accepted |
| MCP/tool surface | no MCP server needed for Phase 0A | pass | keep read-only and repo-local first |

## Boundary Check

- Repos allowed to change now: `diagnose-to-plan` only, for this readiness
  artifact and roadmap status.
- Repos explicitly not allowed to change now: future `faos`, Hub runtime, DTP
  CLI tracing, `tm-skills`, consulting, and client/project repos.
- Private/client data boundary: no raw engagement content in traces or memory
  stores.
- Microsoft/COI boundary: no DSE, employer, customer, or Microsoft-adjacent
  material enters FAOS without explicit COI review.
- Hosted DTP boundary: FAOS may read DTP contracts later; it may not become DTP
  source of truth.
- Public proof boundary: FAOS traces are not proof until the normal proof packet
  gates pass.
- Global skill install boundary: no global skill/hook install in Phase 0A.
- Autonomous/write-enabled automation boundary: no autonomous repo mutation.

## Trace And Memory Safety

- What data will be traced: none in Phase 0A.
- What data must be redacted before trace: prompts, tool args, file paths,
  private client facts, proof candidates, secret-like values, and COI-sensitive
  context.
- What data must never be traced: secrets, credentials, payment/member records,
  raw client communications, raw transcripts, employer/customer-adjacent details,
  and day-job-sensitive material.
- Retention expectation: not accepted yet.
- Memory scopes: separate FAOS store if built later; DTP remains authoritative.
- Memory write approval: human-approved promotion only.
- Memory delete/export path: required before persistent memory implementation.

## Acceptance Criteria Rewrite

Original acceptance criteria:

- [ ] Build FAOS Phase 0 from the raw prompt.
- [ ] Start tracing every agent session.
- [ ] Stand up memory and trace services together.
- [ ] Let FAOS orchestrate DTP behavior.

Corrected acceptance criteria:

- [x] Readiness review is recorded in DTP.
- [x] Current Langfuse, Mem0, Letta, and Spec-Kit docs are checked at a high level.
- [x] Repo boundary remains separate future `faos`, not DTP or Hub.
- [x] Trace redaction and memory isolation are named as blockers.
- [x] DTP source-of-truth and proof/COI gates remain intact.
- [ ] Live CLI/service commands are verified in an explicit future FAOS prep pass.
- [ ] No FAOS repo/services are created before Toni accepts the readiness review.

Manual verification:

- [x] DTP roadmap already has FAOS Epic 12 and active queue gate.
- [x] This artifact keeps implementation parked.
- [ ] Future pass verifies command help and versions locally.

## Decisions Required Before Build

| Decision | Owner | Required before implementation? | Notes |
|---|---|---|---|
| Create separate `faos` repo | Toni | yes | default path remains `C:\Users\tonimontez\code\faos` |
| Trace policy | Toni / DTP | yes | must define redact, never-trace, retention, and review |
| Memory storage isolation | Toni / DTP | yes | separate DB/schema/store per tool |
| DTP adapter scope | Toni | yes | either `op` only or separate DTP adapter story |
| Spec-Kit adoption | Toni | yes | pin release and verify commands first |
| Langfuse deployment shape | Toni | yes | local Docker Compose only until scale/backup needs exist |

## Value Gate

Checked value candidates:

- [x] Agent routing accuracy
- [x] Context durability
- [x] Verification quality
- [x] Research-to-roadmap quality
- [x] Proof safety or evidence quality
- [x] Cross-repo delivery speed
- [x] Business workflow reliability
- [x] Lower memory burden for Toni

Reject or defer if the phase mostly adds ceremony, duplicate state, sensitive
trace risk, or a dashboard without a workflow.

## Recommendation

- Decision: Park implementation; accept readiness review as the correct gate.
- Confidence: high for boundary, medium for exact future service commands.
- Next action: finish packaging the current DTP/Hosted DTP/Business Brain slice,
  then run a future FAOS prep pass that verifies commands locally without
  creating services.
- Backlog update needed: mark readiness review complete / implementation still
  gated.
- Related decision record: none required yet; create one only when FAOS repo or
  `op` wrapper implementation is accepted.

## Sources Checked On 2026-05-03

- Langfuse self-hosting: https://langfuse.com/self-hosting
- Langfuse Docker Compose: https://langfuse.com/self-hosting/deployment/docker-compose
- Mem0 self-hosted setup: https://docs.mem0.ai/open-source/setup
- Letta Docker server: https://docs.letta.com/guides/docker
- GitHub Spec-Kit integrations: https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md
- GitHub Spec-Kit README: https://github.com/github/spec-kit
