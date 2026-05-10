---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Source Freshness Dry-Run V0

Status: dry-run specification plus local dry-run command

Owner repo: `diagnose-to-plan`

## Purpose

The Research Arm has a source list, steward role, decision templates, and an
autonomy-readiness approval to move Research source freshness forward as the
first internal autonomy candidate.

This document defines the dry-run surface before any scheduled workflow,
crawler, Notion sync, digest automation, or autonomous source-monitoring
runtime exists. The local command can write review queues under ignored
`outputs/`, but those queues are evidence only.

Core rule:

> The first source-freshness workflow produces reviewable evidence, not action.

## What This Is

Research Source Freshness Dry-Run V0 is a manual or operator-triggered review
that checks a small subset of approved sources and produces a queue of source
freshness findings.

It answers:

1. Did this source change in a meaningful way?
2. Does the change matter to Toni's practice?
3. Is the evidence strong enough to create a decision record, pattern
   candidate, digest, or implementation review?
4. What is explicitly not allowed from this source?

## What This Is Not

This is not:

- an autonomous research agent;
- a live crawler;
- a scheduled job;
- a public-claim feed;
- a Notion sync;
- a client communication workflow;
- an offer/pricing updater;
- a tool-install trigger;
- a repo-changing workflow.

## Local Command

Use the local command when Toni asks to check source freshness, capture operator
notes, inspect a pasted URL, or search for source evidence:

```powershell
.\.venv\Scripts\dtp.exe research source-freshness `
  --source-id openai-api-codex-changelog `
  --note "Check whether agent tooling guidance changed." `
  --url "https://developers.openai.com/api/docs/changelog" `
  --query "OpenAI Codex changelog agents evals"
```

The command supports:

- operator notes with `--note`;
- pasted source URL metadata with `--url`;
- optional public URL excerpt fetching with `--fetch-url`;
- search packets with `--query`;
- optional public search result fetching with `--search-web`;
- official-source-first search URL generation by default.

Default behavior is conservative:

- URL content is not fetched unless `--fetch-url` is passed.
- Search result pages are not fetched unless `--search-web` is passed.
- Local/private hosts are blocked.
- Search results are low-confidence until reviewed against primary sources.
- Agent-role source checks should follow
  `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md` before promotion.
- Output stays under ignored `outputs/research-source-freshness/`.
- Human review is required before creating a decision record, digest, pattern
  candidate, implementation review, public claim, client message, or repo task.

## Source Subset For First Dry Run

Start with a narrow set so noise is visible early.

| Source ID | Source | Tier | Why Included | First-Run Question |
|---|---|---:|---|---|
| `dtp-repo-evidence` | DTP docs, receipts, Kaizen, evolution, research artifacts | 0 | strongest source for what has actually been approved or parked | Did any internal decision supersede the source list or research posture? |
| `openai-api-codex-changelog` | OpenAI API and Codex changelog | 1 | directly affects Codex/API/agent implementation work | Did a platform change affect agent workflows, evals, tools, or implementation guidance? |
| `openai-agents-sdk-docs` | OpenAI Agents SDK docs | 1 | key source for future agent architecture and guardrails | Did agent architecture, tool use, guardrail, or tracing guidance materially change? |
| `anthropic-claude-release-notes` | Anthropic Claude release notes | 1 | relevant to coding-agent and client explanation posture | Did a Claude/tooling change affect coding workflow or agent capabilities? |
| `github-copilot-changelog` | GitHub Copilot changelog | 1 | relevant to workspace coding-agent behavior and client implementation comparisons | Did Copilot add/change behavior worth tracking for coding workflow or skill routing? |
| `vercel-changelog` | Vercel changelog | 1 | relevant to consulting site, Hub-adjacent deployments, and web AI surfaces | Did hosting/web/AI SDK/security behavior change in a way that affects current repos? |
| `supabase-changelog` | Supabase changelog | 1 | relevant to Hub intake/runtime and Omnexus/database patterns | Did auth/database/runtime changes create a repo task or risk note? |
| `owasp-genai` | OWASP GenAI Security Project | 2 | relevant to AI guardrails, prompt-injection, and excessive-agency boundaries | Did safety guidance change enough to update an AI red-team or guardrail note? |

Do not include Gmail, private client transcripts, Notion, paid tools,
relationship records, Microsoft confidential sources, or local downloads in the
first dry run unless Toni explicitly opens that source for review.

## Dry-Run Queue Path

Raw dry-run output should go to ignored local output first:

```text
outputs/research-source-freshness/source-freshness-YYYY-MM-DD.jsonl
outputs/research-source-freshness/source-freshness-YYYY-MM-DD.md
```

Reviewed source-freshness items that should survive in git can be promoted to:

```text
practice-os/research/source-freshness/reviews/
```

Use `practice-os/templates/research-source-freshness-item.md` for promoted
review items.

## Output Schema

Each dry-run item should carry:

| Field | Required | Notes |
|---|---|---|
| `run_id` | yes | date-based id, for example `rsf-2026-05-10-001` |
| `source_id` | yes | stable id from the source subset |
| `source_name` | yes | human-readable source |
| `source_tier` | yes | source-list tier |
| `source_url_or_path` | yes | public URL or DTP path |
| `reviewed_at` | yes | ISO date/time |
| `freshness_state` | yes | see allowed states below |
| `change_summary` | yes | short summary; "none observed" is allowed |
| `why_it_matters` | yes | practice/client/workflow relevance |
| `evidence_limit` | yes | what this source does not prove |
| `recommended_action` | yes | see allowed actions below |
| `allowed_next_artifact` | yes | digest, decision record, pattern candidate, etc. |
| `blocked_actions` | yes | public claims, client comms, tool installs, etc. |
| `review_owner` | yes | Toni, Research Steward, or named lane |
| `next_review_trigger` | yes | what reopens this item |

Allowed `freshness_state` values:

- `unchanged`
- `changed_minor`
- `changed_meaningful`
- `stale_local_record`
- `source_unreachable`
- `blocked_source`
- `needs_manual_review`

Allowed `recommended_action` values:

- `ignore`
- `watch`
- `create_research_decision_record`
- `create_research_pattern_candidate`
- `create_digest`
- `open_implementation_review`
- `update_source_list`
- `route_to_guardrail_review`
- `blocked`

## Human Review States

After a dry-run queue item is reviewed, assign one:

| State | Meaning |
|---|---|
| `accepted_watch` | keep visible but do not act |
| `accepted_record` | create the recommended DTP record |
| `accepted_build_review` | open a scoped implementation/review artifact |
| `parked` | preserve but no current work |
| `rejected_noise` | not useful enough to track |
| `blocked_sensitive` | source or implication hits privacy/COI/legal/security boundary |
| `superseded` | newer source or DTP decision replaces it |

## Blocked-Source Behavior

If a source is blocked:

1. Do not summarize raw content.
2. Record only the source category and why it is blocked.
3. Route to the owning gate if the source may matter later.
4. Do not create public claims, client deliverables, Notion mirrors, or repo
   tasks from the blocked source.

Blocked sources include:

- secrets or credentials;
- raw private client material;
- Microsoft confidential or day-job context;
- private relationship records;
- raw Gmail unless Toni explicitly asks to use the message;
- paid/private databases;
- unsourced social claims as action evidence.

## Validation Command

For the spec-only phase:

```powershell
.\.venv\Scripts\dtp.exe practice doctor
git diff --check
.\.venv\Scripts\python.exe -m pytest tests\test_practice.py
```

For a future CLI dry-run implementation, add tests that verify:

- the first-run source subset is loaded;
- blocked sources do not emit raw content;
- queue items validate against the output schema;
- unknown freshness/recommendation states fail validation;
- dry-run writes only to ignored `outputs/` unless explicitly promoted;
- no Notion, Gmail, client, public, or repo mutation side effects occur.

## Implemented Local Dry-Run Command

The first local command is:

```powershell
.\.venv\Scripts\dtp.exe research source-freshness
```

It:

1. uses the source subset above for known `--source-id` values;
2. accepts manually supplied source snapshots, operator notes, URLs, and search
   queries;
3. emits JSONL and Markdown dry-run queue files under
   `outputs/research-source-freshness/`;
4. validates queue item fields and states;
5. prints a short human review summary;
6. can optionally fetch public URL excerpts or public search-result pages;
7. blocks local/private URL fetches;
8. does not schedule, sync, send, install, promote, or mutate tracked repo
   artifacts from findings.

More advanced browsing, deduplication, source diffing, and scheduling can come
later, after the command produces useful low-noise queues.

## Promotion Gate

The spec-to-command gate is satisfied for a local dry-run only:

- Toni accepts the source subset;
- the output schema is stable enough for a first command;
- tests cover notes, URL metadata, public URL fetch excerpts, blocked local
  URLs, and CLI output;
- the implementation is local-only and dry-run by default.

Move from dry-run command to scheduled workflow only after:

- multiple dry-runs produce useful, low-noise queues;
- human review states are being used;
- an autonomy-readiness review is updated;
- a kill switch, audit log, duplicate handling, and failure behavior are
  accepted.

## Acceptance Criteria

This spec is accepted if future agents can tell:

- which sources belong in the first dry run;
- where raw and reviewed queue items go;
- what fields each item must include;
- how source changes are classified;
- what actions are explicitly blocked;
- what validation is required before implementation;
- why scheduled autonomy is still not approved.
