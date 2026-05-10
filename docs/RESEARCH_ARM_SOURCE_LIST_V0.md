---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Arm Source List V0

Status: recurring source list, event-triggered review

Owner repo: `diagnose-to-plan`

## Purpose

This source list gives the Research Arm a stable set of places to check when
Toni asks what changed in AI, agent tooling, consulting operations, platform
infrastructure, governance, or client-ready workflow implementation.

It is not an autonomous crawler, content calendar, public-claim feed, or
write-enabled agent. It is a recurring source list that supports
event-triggered research decisions.

Core rule:

> Sources feed review. Review feeds decisions. Decisions feed artifacts.

## Default Workflow

Use the list when one of these events happens:

- Toni forwards or saves a research signal.
- A client or prospect asks about AI, automation, tooling, governance, cost, or
  implementation readiness.
- A platform used by the practice ships a meaningful change.
- A claim, offer line, proof statement, or client explanation needs evidence.
- A recurring pattern appears in client work, email, meetings, or repo
  execution.
- A knowledge base feels stale and needs a source-backed refresh.
- Toni asks to keep current without manually maintaining every source.

Default cadence is event-based. A scheduled sweep is optional and must be
explicitly requested or tied to a defined digest window.

## Source Tiers

| Tier | Source Type | Default Use | Claim Confidence |
|---|---|---|---|
| 0 | Toni-provided source material, client/operator field notes, repo evidence, meeting transcripts, founder emails | highest-priority practice signal and proof of real operating needs | high for internal intent; public claims still gated |
| 1 | Official product docs, release notes, changelogs, primary vendor announcements | current technical facts, platform changes, implementation implications | medium to high after source-specific review |
| 2 | Standards, governance, security, and risk bodies | safety, compliance posture, AI governance, client trust language | medium to high after applicability review |
| 3 | reputable reports, analyst writing, business essays, newsletters, podcasts, social posts with sources | trend sensing, framing, language, possible hypotheses | low to medium until corroborated |
| 4 | loose takes, screenshots, social threads, unsourced claims | inspiration only | low; do not use for claims |

## Recurring Sources

| Source | Type | Link or Path | Use | Default Trigger | Output |
|---|---|---|---|---|---|
| Toni founder email captures | internal source | Gmail or exported digest | raw ideas, positioning, market observations, research saves | Toni forwards or references an email | digest, idea evolution record, message KB update |
| Client and prospect meetings | internal source | `engagements/`, approved transcripts, meeting receipts | field evidence, objections, delivery patterns, product/service needs | client call, reply, transcript, or post-meeting receipt | client receipt, pattern candidate, offer refinement |
| DTP repo evidence | internal source | DTP docs, steward receipts, kaizen/evolution records | what has actually been built, approved, parked, or superseded | implementation, status review, repo audit | knowledge-base update, steward receipt |
| OpenAI API and Codex changelog | official docs | https://developers.openai.com/api/docs/changelog | model/platform changes, agent tooling, implementation opportunities | OpenAI-related source event or monthly scan | research decision record, implementation note |
| OpenAI Agents SDK docs | official docs | https://developers.openai.com/api/docs/guides/agents | agent architecture, guardrails, orchestration, eval posture | agent/workflow design event | architecture note, research pattern |
| Anthropic Claude release notes | official docs | https://platform.claude.com/docs/en/release-notes/overview | model/tooling changes and client explanation language | Claude/coding-agent/tooling event | research decision record |
| Microsoft Work Trend Index | primary research | https://www.microsoft.com/en-us/worklab/work-trend-index | work, agents, adoption, leadership, human agency framing | AI workforce/client explanation event | digest or messaging candidate |
| GitHub Copilot changelog | official changelog | https://github.blog/changelog/label/copilot/ | coding-agent workflow changes and developer-productivity signals | GitHub/Copilot/workspace workflow event | implementation or research note |
| AWS What's New | official changelog | https://aws.amazon.com/new/ | Bedrock, cloud, agent, and infrastructure changes | AWS/Bedrock/client-platform event | research decision record |
| Google Cloud Vertex AI release notes | official docs | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/release-notes | enterprise AI/platform changes and client architecture signals | Google/Vertex/agentic platform event | research note |
| Vercel changelog | official changelog | https://vercel.com/changelog | web platform, AI SDK, hosting, workflows, security releases | consulting/Hub/site platform event | repo task or research note |
| Supabase changelog | official changelog | https://supabase.com/changelog | database/auth/storage/runtime changes | Supabase/Hub/intake event | repo task or decision record |
| Stripe changelog | official changelog | https://docs.stripe.com/changelog | payment, billing, subscription, checkout, compliance changes | paid offer/product/payment event | repo task or risk note |
| NIST AI Risk Management Framework | standards body | https://airc.nist.gov/airmf-resources/airmf/ | AI risk, trustworthiness, governance language | AI governance or client trust event | policy/pattern candidate |
| OWASP GenAI Security Project | security body | https://owasp.org/www-project-top-10-for-large-language-model-applications/ | prompt injection, excessive agency, overreliance, disclosure risk | AI app/security/client-data event | AI red-team or guardrail note |
| Local saved reports | local source | `inputs/`, downloads, or DTP research notes | deeper source packets that Toni flags as useful | Toni saves report or asks to digest | parked research item, digest, pattern candidate |

## Source Review Requirements

Every source-backed change should answer:

- What changed?
- Why does it matter to Toni's practice?
- Is it real enough to act on, or just a watch item?
- What is the evidence limit?
- Does it affect a client explanation, internal operating rule, repo task,
  template, agent role, offer, or public claim?
- What approval gate is required before use?

Use `practice-os/templates/research-decision-record.md` when a source changes a
decision or should be adopted, piloted, watched, rejected, or parked.

Use `practice-os/templates/research-pattern-candidate.md` when the source
suggests a reusable consulting principle or client artifact.

## Knowledge Base Maintenance Rule

The Research Arm can recommend updates to knowledge bases. It does not silently
rewrite them.

When a source implies a durable update, route it through
`docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md`.

Valid destinations include:

- `docs/PRACTICE_EVOLUTION_SYSTEM_V0.md`
- `docs/PRACTICE_KNOWLEDGE_BASE_V1.md`
- `docs/PRACTICE_MEMORY_CONTROL_PLANE.md`
- `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md`
- `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md`
- `practice-os/agents/`
- `practice-os/templates/`
- `practice-os/comms/private/`
- repo-local docs when the owning repo is clear

## Public Claim Boundary

No source in this list makes a public claim automatically safe.

Public claims still require:

- source-specific review;
- accurate date/context;
- caveats when needed;
- proof or permission when tied to client work;
- redaction and privacy review;
- Toni approval before public site, client deliverable, sales copy, or external
  communication use.

## Notion Boundary

Notion can mirror:

- source name;
- classification;
- why it matters;
- review date;
- DTP path.

Notion does not own the source list, raw notes, approval authority, private
client facts, or public-claim state.
