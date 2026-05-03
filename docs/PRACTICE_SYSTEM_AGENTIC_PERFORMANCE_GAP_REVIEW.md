# Practice System Agentic Performance Gap Review

Status: required Practice OS review layer.

Owner: `diagnose-to-plan`

Purpose: make the consulting operating system inspect how well agents, skills, prompts, templates, research, and verification performed. This fills the gap between architecture docs and real behavior: a system can look well-designed and still fail to route Toni's prompt, remember the right context, trigger the right skill, or convert a sharp idea into durable work.

## Why This Exists

The prior practice-system audit covered architecture, governance, repo boundaries, proof, durability, and implementation sequence. That was necessary but incomplete. Toni caught a deeper failure mode: if a user notices a missing behavior such as contextual activation, then there are probably other agentic performance gaps hiding in the system.

This review makes that scrutiny recurring. After major roadmap sessions, skill changes, agent misroutes, research adoption, proof decisions, or automation proposals, the system asks:

- Did the prompt activate the right process?
- Did the agent have the right current repo context?
- Did the right skill or template trigger?
- Did the idea become a story, eval, proof item, research item, decision, repo touch pass, or parked item?
- Did the correct verification and safety gates happen at the right time?
- Did any miss become a reusable lesson?

## Research Basis

These references inform the review standard:

- Anthropic context engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- OpenAI agent evals and traces: https://developers.openai.com/api/docs/guides/agent-evals
- OpenAI guardrails: https://openai.github.io/openai-agents-python/guardrails/
- OWASP Agentic Skills Top 10: https://owasp.org/www-project-agentic-skills-top-10/
- MCP specification: https://modelcontextprotocol.io/specification/2025-11-25/basic
- OpenAI Agents SDK sandboxing direction: https://openai.com/index/the-next-evolution-of-the-agents-sdk/

## Operating Principle

Treat agent behavior as a product surface. It needs routing, context, evals, guardrails, receipts, and regression checks just like application behavior needs tests and CI.

In V0, this is supervised markdown/process. It does not authorize autonomous repo edits, hosted steward queues, public proof, global installs, or self-modifying skills.

## Review Dimensions

| Dimension | Question | Failure Signal | Durable Output |
|---|---|---|---|
| Prompt intent routing | Did the activation map catch the real shape of the prompt? | Toni had to explain which lane should have activated | activation map update |
| Context quality | Did the agent load the right repo docs, current state, handoff notes, and live evidence? | agent relied on memory when local state mattered | repo manifest, evidence index, handoff, steward note |
| Skill trigger quality | Did the right `tm-skills` or DTP skill trigger? | wrong skill, duplicate skill, or no skill used | skill description update, eval fixture, misfire |
| Planning continuity | Did the idea become a durable artifact? | useful idea stayed only in chat | backlog story, template, decision, research item, proof item, parked record |
| Verification quality | Did local gates, CI, evidence, and redaction checks run at the right time? | work finished without receipts or with vague validation | evidence record, test update, CI gate |
| Research quality | Did the system use current primary/official sources before adopting a method? | roadmap adopted a trend from vibes | research radar item or rejected spike |
| Safety quality | Did install, proof, private data, hosted app, and automation gates hold? | public/private, write-enabled, or install boundary blurred | guardrail, decision record, redaction item |
| Learning loop | Did the miss become reusable? | repeated correction with no artifact | eval, checklist, skill update, lesson |

## Current Findings

### P0-APG-1: No Recurring Agentic Performance Review Gate

Evidence: the system had activation routing, stewardship, and future intelligence docs, but no required template specifically asked whether the agent setup failed to route, remember, validate, research, or learn.

Impact: Toni's memory would still be needed to notice design holes in the AI operating system.

Fix: require `practice-os/templates/agentic-performance-gap-review.md` through `dtp practice doctor`.

### P1-APG-2: Misfires Are Not Yet Consistently Converted Into Evals

Evidence: `tm-skills` has eval directories and DTP has lesson/eval lanes, but real cross-tool misfires are not yet routinely captured as fixtures.

Impact: a miss can be fixed by conversation but not prevented in future sessions.

Fix: after global skill install and smoke tests, convert any trigger miss into `tm-skills/MISFIRES.md`, a trigger eval, or a DTP activation-map update.

### P1-APG-3: Context Receipts Are Present But Not Yet Habitual

Evidence: Roadmap Steward, flight recorder, repo manifest, and evidence index templates exist, but only the first DTP pilot is active.

Impact: future agents can still spend time rediscovering repo state or over-relying on chat memory.

Fix: run the steward preflight for major roadmap moves and expand repo manifests only during active touch passes.

### P1-APG-4: Research Adoption Needs A Harder Source Standard

Evidence: the roadmap cites current AI/dev methods, but research needs a repeatable classification step before a tool becomes implementation work.

Impact: interesting agent tooling could enter the roadmap without proving value to delivery speed, proof quality, risk control, agent performance, or business leverage.

Fix: classify research as `Adopt`, `Pilot`, `Watch`, or `Reject`, and require repo-specific implementation plans for anything adopted.

### P2-APG-5: Traces And Evidence IDs Are A Future Need

Evidence: the evidence/index patterns exist, but not every agent session or proof record has a trace/eval id yet.

Impact: hosted DTP and future observability may lack stable linkage between prompt, action, evidence, decision, and proof.

Fix: add trace/eval ids later when hosted DTP or Hub has real agent workflows to persist.

## When To Run This Review

Run the template when any of these happen:

- Toni identifies a missed agent behavior or planning gap.
- A prompt spans roadmap, repo, business, proof, and implementation lanes.
- `tm-skills` trigger behavior changes.
- A major agent session changes docs, roadmap, private kits, proof, CI, or process.
- Research proposes a new method, framework, protocol, or guardrail.
- A public proof, private data, hosted app, global install, or automation gate is involved.
- A repeated mistake should become an eval, checklist, or skill update.

## V0 Done Gate

V0 is done when:

- `practice-os/templates/agentic-performance-gap-review.md` exists.
- `dtp practice doctor` requires it.
- The audit and optimization docs include the performance-gap lens.
- The activation map routes performance-gap prompts to this review.
- The first live steward receipt records why the layer was added.

## Future Automation Path

- V0: required markdown template and docs.
- V1: `dtp steward review` can flag missing performance-gap reviews after major sessions.
- V2: hosted DTP can track recurring gap review items once real records exist.
- V3: agent-assisted roadmap manager can propose skill/eval/template changes only after evals, guardrails, and human approval gates exist.
