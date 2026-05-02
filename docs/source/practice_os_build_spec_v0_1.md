# Practice OS Build Spec v0.1

**Purpose:** Internal build spec for an AI/software implementation consulting operating system.

**Core loop:** Capture -> clarify -> structure -> score -> specify -> build -> debug -> hand off -> measure -> learn.

---

# Part V: Practice OS build spec

## Product purpose

Practice OS is the internal operating system for the consulting practice.

It helps turn messy human input and client context into working systems.

It should support this loop:

> Capture -> clarify -> structure -> score -> specify -> build -> debug -> hand off -> measure -> learn.

## Product non-goals

The MVP should not:

- become a full client portal
- automate final business decisions
- silently update permanent memory
- build autonomous agents that act without review
- manage client credentials
- replace legal, medical, financial, or compliance review
- become a generic project management clone
- support every possible consulting workflow

## Primary users

### User 1: Toni / consultant

Needs:

- capture thoughts quickly
- structure client discovery
- generate audit outputs
- create implementation specs
- turn specs into code tasks
- track exceptions
- track value
- preserve reusable patterns

### User 2: future client viewer

Needs:

- see what was built
- see how it works
- see known issues
- see value metrics
- access runbook
- submit requests

The MVP should focus on User 1 only.

## System architecture overview

### V0: Manual operating system

Use before coding everything:

- Notion / Google Docs for notes
- spreadsheet for opportunity scores
- GitHub repo for templates/code
- markdown runbooks
- manual value ledger

### V1: Internal web app

Suggested stack:

- Next.js / React frontend
- Supabase Postgres database
- Supabase Auth
- server-side LLM calls
- file/transcript upload
- vector search later, not first
- GitHub integration later
- LangSmith/OpenAI tracing later

### V2: AI-assisted Practice OS

Add model-assisted drafting:

- intent extraction
- clarifying question generation
- context pack building
- opportunity scoring suggestions
- implementation spec drafts
- anti-slop review
- exception analysis
- value summary drafts
- memory promotion suggestions

### V3: Client-facing portal

Only after repeated client patterns appear:

- runbook access
- value ledger
- issue/request tracker
- monthly review notes
- system inventory
- next-phase backlog

---

# Part VI: Core modules

## Module 1: Thought Inbox

### Purpose

Capture raw thoughts before they disappear.

### Inputs

- voice note transcript
- typed note
- meeting note
- client idea
- offer idea
- code idea
- market observation
- lesson learned

### Fields

```text
id
title
raw_text
source_type
category
related_client_id
related_project_id
tags
confidence
next_action
promoted_to
created_at
```

### Behavior

The system can suggest categories, tags, and next actions, but should not promote anything into durable memory without approval.

## Module 2: Input Studio

### Purpose

Convert raw human input into structured context and artifacts without losing voice or intent.

### Pipeline

```text
Raw Input
-> Intent Brief
-> Clarifying Questions
-> Assumption Set
-> Context Pack
-> Output Blueprint
-> Draft Artifact
-> Anti-Slop Review
-> Human Feedback
-> Final Artifact
-> Memory Promotion
```

### Key entities

```text
RawInput
IntentBrief
ClarifyingQuestion
Assumption
ContextPack
OutputBlueprint
Artifact
ArtifactReview
FeedbackNote
MemoryPromotion
```

## Module 3: Clarifying Question Layer

### Purpose

Increase input resolution without creating friction.

### Core rule

> Ask the fewest questions necessary to materially improve the output.

### Authority rule

The user's stated intent is primary. The system may clarify, improve, or name tradeoffs, but it should not override the user's direction unless there is safety, legal, privacy, security, compliance, money-movement, irreversible-action, or W-2 conflict risk.

### Modes

| Mode | Use case | Question budget |
|---|---|---|
| Fast | early idea, low stakes | 0-1 |
| Refine | serious artifact | 2-4 |
| Build | specs / workflows / code | 4-8, grouped |
| Guardrail | risk area | blocking questions required |

### Question types

- intent
- audience
- voice
- constraint
- success metric
- risk
- implementation
- adoption
- value tracking

### Question object

```json
{
  "question_id": "Q-001",
  "question_text": "Who is the first audience for this artifact?",
  "question_type": "audience",
  "importance": "high",
  "blocking": false,
  "default_assumption": "Owner-led small business buyer",
  "why_it_matters": "Audience changes tone, examples, and call to action.",
  "answer": null,
  "status": "open"
}
```

## Module 4: Client Intelligence

### Purpose

Turn every client conversation into structured business context.

### Fields

```text
client_id
business_type
revenue_model
customer_types
owner_bottlenecks
current_tools
data_sources
repeated_workflows
pain_points
budget
maintenance_constraints
team_adoption_risk
privacy_security_risk
first_recommended_project
engagement_stage
value_metrics
```

## Module 5: Workflow Map

### Purpose

Represent business process in a way that can become a build spec.

### Workflow object

```json
{
  "workflow_name": "New lead intake",
  "trigger": "Prospect submits form, calls, texts, or gets referred",
  "actors": ["owner", "sales rep"],
  "systems": ["website", "phone", "CRM", "email"],
  "current_steps": [
    "Lead contacts business",
    "Owner manually replies",
    "Owner asks qualification questions",
    "Owner remembers to follow up",
    "Lead may or may not be entered into CRM"
  ],
  "failure_points": [
    "Lead not captured",
    "Follow-up delayed",
    "No status tracking",
    "Owner is the bottleneck"
  ],
  "frequency_per_week": 25,
  "estimated_time_per_event_minutes": 12,
  "business_impact": "Missed or delayed lead follow-up",
  "recommended_first_build": "Lead intake + follow-up workflow",
  "human_review_required": true
}
```

## Module 6: Opportunity Scorer

### Purpose

Prevent chasing impressive but low-value builds.

### Score factors

Score 1-5:

- frequency
- owner bottleneck
- revenue proximity
- pain level
- data readiness
- adoption likelihood
- reusability
- build complexity
- risk

### Priority formula

```text
Priority Score =
(frequency + owner_bottleneck + revenue_proximity + pain + data_readiness + adoption_likelihood + reusability)
- (build_complexity + risk)
```

### Client-facing explanation

> "This is not the flashiest project, but it scores highest because it happens often, touches revenue, reduces owner load, and is easy for your team to adopt."

## Module 7: Implementation Spec Generator

### Purpose

Turn business context into code-ready specs.

### Spec object

```json
{
  "project_name": "Lead intake and follow-up workflow",
  "client": "Example Mobile Home Business",
  "business_goal": "Reduce missed leads and speed up follow-up",
  "problem_statement": "Leads arrive through multiple channels and depend on the owner remembering to respond and track status.",
  "non_goals": [
    "Do not replace human sales conversations",
    "Do not automate financing advice",
    "Do not build a full custom CRM in Phase 1"
  ],
  "users": [
    {"role": "Owner", "needs": "Visibility into active leads and next actions"},
    {"role": "Sales rep", "needs": "Clear follow-up tasks and approved response templates"}
  ],
  "inputs": ["Website form", "Manual lead entry", "Text/call note", "Lead source"],
  "outputs": ["CRM record", "Follow-up task", "Notification", "Status update", "Weekly lead report"],
  "systems_of_record": ["CRM", "Google Workspace", "Website"],
  "acceptance_criteria": [
    "Every web lead creates a CRM record",
    "Every new lead gets a next-step task",
    "Owner receives daily digest of untouched leads",
    "Lead status can be updated by non-technical user",
    "Runbook explains how to edit templates"
  ],
  "value_metrics": [
    "Average lead response time",
    "Number of unassigned leads",
    "Number of overdue follow-ups",
    "Estimated admin time saved"
  ],
  "risks": ["Bad source data", "Team ignores CRM", "Notification fatigue"],
  "handoff_requirements": ["Recorded walkthrough", "Runbook", "Admin credentials owned by client", "Common failure guide"]
}
```

## Module 8: Build Tracker

### Purpose

Keep work tied to scope and acceptance criteria.

### Fields

```text
build_task_id
spec_id
title
description
status
priority
acceptance_criteria
linked_exception_id
client_input_needed
out_of_scope_flag
created_at
updated_at
```

## Module 9: Exception Register

### Purpose

Make debugging explicit and turn failures into reusable lessons.

### Severity levels

| Severity | Meaning | Example |
|---|---|---|
| S0 | Observation | Client asked for Phase 2 feature |
| S1 | Minor issue | Automation ran late but completed |
| S2 | Workflow issue | Lead created but no follow-up task generated |
| S3 | Client-facing failure | Customer received wrong message |
| S4 | Security/compliance issue | Sensitive data exposed to wrong tool |
| S5 | Business-critical incident | Payment/invoice/customer workflow materially affected |

### Exception object

```json
{
  "exception_id": "EX-001",
  "client": "Example Client",
  "workflow": "Lead intake",
  "severity": "S2",
  "expected_behavior": "Every new lead creates a CRM task",
  "observed_behavior": "CRM record was created but task was missing",
  "detected_by": "Daily workflow check",
  "root_cause": "Missing required field in form submission",
  "status": "Resolved",
  "fix": "Added fallback default owner and validation check",
  "lesson_learned": "All intake automations need required-field validation before CRM write",
  "promote_to_pattern_memory": true
}
```

## Module 10: Value Ledger

### Purpose

Track what changed.

### Value object

```json
{
  "project": "Lead intake and follow-up workflow",
  "baseline": {
    "average_response_time_hours": 18,
    "weekly_leads": 25,
    "manual_admin_hours_per_week": 5,
    "missed_followups_per_week": 7
  },
  "after_launch": {
    "average_response_time_hours": 3,
    "weekly_leads": 27,
    "manual_admin_hours_per_week": 2,
    "missed_followups_per_week": 1
  },
  "value_summary": [
    "Response time improved by 15 hours",
    "Admin work reduced by approximately 3 hours/week",
    "Missed follow-ups reduced from 7/week to 1/week"
  ],
  "confidence": "medium",
  "notes": "Savings are estimated based on owner-reported time and workflow logs."
}
```

## Module 11: Anti-Slop Reviewer

### Purpose

Keep AI output specific, useful, authentic, and tied to context.

### Review dimensions

| Dimension | Question | Bad output looks like |
|---|---|---|
| Specificity | Is it tied to real context? | Generic claims, vague benefits |
| Voice | Does it sound like the person/business? | Polished but fake |
| Usefulness | Does it help someone decide, act, or understand? | Pretty words with no operational value |
| Truth | Is it supported by known facts? | Confident unsupported claims |
| Restraint | Does it avoid overclaiming? | Hype, exaggeration, fake certainty |
| Buildability | Can it be implemented? | Vague requirements |
| Testability | Are acceptance criteria clear? | No way to know if done |

### Review object

```json
{
  "artifact_id": "A-001",
  "specificity_score": 4,
  "voice_score": 3,
  "usefulness_score": 5,
  "truth_score": 5,
  "restraint_score": 4,
  "slop_flags": ["generic phrase: unlock the power of AI"],
  "recommended_edits": [
    "Remove generic phrase",
    "Add concrete example",
    "Make closing less polished and more grounded"
  ]
}
```

## Module 12: Memory Review Queue

### Purpose

Let the system learn without silently poisoning itself.

### Promotion flow

```text
Raw note -> extracted insight -> proposed memory -> human approval -> memory item -> reusable context
```

### Memory item fields

```text
id
title
content
memory_level
source
approved
tags
related_client_id
created_at
```

---

# Part VII: Database schema starter

```sql
create table clients (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  business_type text,
  revenue_model text,
  notes text,
  risk_level text,
  status text,
  created_at timestamptz default now()
);

create table engagements (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  offer_type text,
  stage text,
  start_date date,
  end_date date,
  budget numeric,
  status text,
  created_at timestamptz default now()
);

create table raw_inputs (
  id uuid primary key default gen_random_uuid(),
  source_type text,
  raw_text text not null,
  related_client_id uuid references clients(id),
  related_project_id uuid,
  tags text[],
  created_at timestamptz default now()
);

create table intent_briefs (
  id uuid primary key default gen_random_uuid(),
  raw_input_id uuid references raw_inputs(id),
  artifact_type text,
  core_intent text,
  audience text,
  business_goal text,
  emotional_tone text,
  must_include jsonb,
  must_avoid jsonb,
  phrases_to_preserve jsonb,
  assumptions jsonb,
  open_questions jsonb,
  created_at timestamptz default now()
);

create table clarifying_questions (
  id uuid primary key default gen_random_uuid(),
  related_input_id uuid references raw_inputs(id),
  related_client_id uuid references clients(id),
  related_project_id uuid,
  question_text text not null,
  question_type text,
  importance text,
  blocking boolean default false,
  default_assumption text,
  why_it_matters text,
  answer text,
  status text default 'open',
  created_at timestamptz default now(),
  answered_at timestamptz
);

create table assumptions (
  id uuid primary key default gen_random_uuid(),
  related_input_id uuid references raw_inputs(id),
  related_project_id uuid,
  assumption_text text,
  source text,
  confidence text,
  needs_review boolean default true,
  confirmed boolean default false,
  created_at timestamptz default now()
);

create table workflows (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  name text not null,
  trigger text,
  current_state text,
  desired_state text,
  frequency numeric,
  time_cost numeric,
  business_impact text,
  owner_bottleneck_score int,
  status text,
  created_at timestamptz default now()
);

create table opportunities (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  workflow_id uuid references workflows(id),
  title text,
  description text,
  frequency_score int,
  owner_bottleneck_score int,
  revenue_proximity_score int,
  pain_score int,
  data_readiness_score int,
  adoption_score int,
  reusability_score int,
  complexity_score int,
  risk_score int,
  priority_score int,
  recommended_phase text,
  created_at timestamptz default now()
);

create table implementation_specs (
  id uuid primary key default gen_random_uuid(),
  opportunity_id uuid references opportunities(id),
  project_name text,
  business_goal text,
  problem_statement text,
  non_goals jsonb,
  users jsonb,
  inputs jsonb,
  outputs jsonb,
  systems_of_record jsonb,
  acceptance_criteria jsonb,
  risks jsonb,
  value_metrics jsonb,
  handoff_requirements jsonb,
  status text,
  created_at timestamptz default now()
);

create table build_tasks (
  id uuid primary key default gen_random_uuid(),
  spec_id uuid references implementation_specs(id),
  title text,
  description text,
  status text,
  priority text,
  acceptance_criteria jsonb,
  linked_exception_id uuid,
  created_at timestamptz default now()
);

create table exceptions (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  workflow_id uuid references workflows(id),
  severity text,
  expected_behavior text,
  observed_behavior text,
  detected_by text,
  root_cause text,
  fix text,
  status text,
  lesson_learned text,
  promote_to_memory boolean default false,
  created_at timestamptz default now()
);

create table value_metrics (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  engagement_id uuid references engagements(id),
  metric_name text,
  baseline_value numeric,
  current_value numeric,
  unit text,
  confidence text,
  notes text,
  created_at timestamptz default now()
);

create table memory_items (
  id uuid primary key default gen_random_uuid(),
  title text,
  content text,
  memory_level text,
  source text,
  approved boolean default false,
  tags text[],
  related_client_id uuid references clients(id),
  created_at timestamptz default now()
);

create table decision_logs (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  engagement_id uuid references engagements(id),
  decision text,
  options_considered jsonb,
  rationale text,
  tradeoffs text,
  decided_at timestamptz default now()
);

create table runbooks (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  engagement_id uuid references engagements(id),
  title text,
  content text,
  version text,
  last_updated_at timestamptz default now()
);
```

---

# Part VIII: MVP roadmap

## Phase 0: Manual proof loop

Duration: 1-2 weeks

Deliverables:

- AI Upgrade Audit template
- workflow map template
- opportunity scorer spreadsheet
- implementation spec markdown template
- runbook template
- value ledger template
- exception register template

Goal:

> Use the system manually on 2-3 real or mock clients before coding the app.

## Phase 1: Internal app skeleton

Duration: 1-2 weeks

Screens:

1. Thought Inbox
2. Client Record
3. Workflow Map
4. Opportunity Scorer
5. Implementation Spec
6. Value Ledger
7. Exception Register
8. Memory Queue

Goal:

> Make the core operating loop usable without AI automation.

## Phase 2: Input Studio

Duration: 1-2 weeks

Features:

- paste transcript / raw note
- create intent brief
- generate clarifying questions
- create assumptions
- build context pack
- draft artifact
- anti-slop review
- save feedback
- suggest memory promotions

Goal:

> Turn raw human thought into structured output without losing voice or intent.

## Phase 3: Spec-to-code support

Duration: 1-2 weeks

Features:

- generate implementation spec from opportunity
- export as Markdown
- export as JSON
- generate build tasks
- generate test cases
- generate code-tool prompt
- connect to GitHub manually or through export

Goal:

> Give coding agents high-resolution input.

## Phase 4: Observability and exception loop

Duration: 1-2 weeks

Features:

- trace fields
- model/prompt version tracking
- tool call notes
- exception severity
- root cause
- fix notes
- lesson promotion

Goal:

> Make AI/client workflow failures debuggable and reusable.

## Phase 5: Client-facing slice

Do not build until real clients repeatedly ask for visibility.

Possible first client-facing screens:

- System Handoff Pack
- Runbook
- Value Ledger
- Known Issues
- Request Queue
- Next-Phase Backlog

---

# Part IX: First artifact templates

## AI Upgrade Audit output

```text
Client:
Business type:
Date:

1. Current state
- How work moves today
- Tools used
- Who owns the workflow
- Where things break

2. Top bottlenecks
- Bottleneck 1
- Bottleneck 2
- Bottleneck 3

3. Opportunity score
- Opportunity
- Why it matters
- Score
- Risk
- Recommendation

4. First recommended build
- Goal
- Scope
- Non-goals
- Timeline
- Estimated cost
- Required client input

5. Value tracking plan
- Baseline metrics
- After-launch metrics
- Confidence level

6. What not to build yet
- Item
- Reason

7. Next step
- Build option
- Handoff expectations
- Support option
```

## System Handoff Pack

```text
1. What was built
2. Why it was built
3. What tools are involved
4. Who owns each account
5. Monthly costs
6. How the workflow runs
7. How to make common changes
8. What can break
9. How to fix common issues
10. What to do if it breaks and cannot be fixed internally
11. Value ledger
12. Decision log
13. Phase 2 backlog
```

## Clarifying question defaults

For marketing:

- Who is this for?
- What should it make them think/do?
- Should it sound raw, polished, memo-like, or conversational?
- What phrase or idea must be preserved?
- What should it avoid sounding like?

For client diagnosis:

- Where does this workflow start?
- Who touches it?
- What happens when it breaks?
- What does only the owner know how to do?
- What would make fixing it worth the money?

For code/build:

- What is the system of record?
- What triggers the workflow?
- Who uses it?
- What is out of scope?
- What does done mean?
- What should happen when it fails?

---

# Part X: Refined public language

## One-sentence pitch

> I help owner-led businesses figure out what is actually worth doing with AI and software, then build the useful version and leave them with a system they can run.

## Stronger founder pitch

> A lot of businesses are experimenting with AI, but most of it is random. Someone is using ChatGPT, someone bought a tool, someone wants a chatbot, but none of it is connected to how the business actually runs. I help them step back, find the bottleneck, choose the highest-leverage workflow, and build the first useful system around it.

## Website hero

**An engineer for businesses without a software team.**

I help owner-led businesses use AI and software to remove bottlenecks, clean up workflows, and build systems their team can actually run.

## The problem section

AI is easy to try. It is hard to implement.

Most businesses now have access to powerful tools, but access does not create a working system. The hard part is knowing what to build, where it fits, how it changes the workflow, and how the team will keep using it after the first week.

## The method section

Most engagements follow the same order:

> Understand the real problem. Write the plan. Explain the tradeoffs. Build the useful thing. Document it. Hand it off. Support it if that makes sense.

## The close

The goal is not more software.

The goal is a business that runs cleaner than it did before.

---

# Part XI: What to build next

Build the manual templates first, then the internal app.

The first coded MVP should have four screens:

1. **Input Studio**  
   Capture raw notes, generate intent briefs, ask clarifying questions, and create context packs.

2. **Client + Workflow Map**  
   Store client context, workflows, bottlenecks, tools, and adoption constraints.

3. **Opportunity Scorer + Implementation Spec**  
   Score opportunities, choose the first build, generate specs, and export code-tool briefs.

4. **Value Ledger + Exception Register**  
   Track baseline/current metrics, failures, fixes, and lessons learned.

Do not build the client portal yet.

Do not overbuild memory yet.

Do not create autonomous agents that can act without review.

Get the loop working manually, then automate the parts that are repetitive.

---

# Part XII: Open questions for you

These questions should not block progress, but they would sharpen the next version.

1. **First buyer:** Which warm lead is most likely to let you run a real AI Upgrade Audit first?
2. **Stack:** Do you want Practice OS to be Next.js + Supabase by default, or would you rather begin with Notion/Airtable plus scripts?
3. **Voice capture:** Do you want transcription in the first coded MVP, or is paste-transcript enough for v0?
4. **Memory boundary:** What should be allowed into reusable memory, and what should stay client-specific?
5. **Public identity:** What name do you want to test: "engineer for businesses without a software team," "operator's engineer," or something else?
6. **First productized module:** Which module should become the first repeatable build: lead follow-up, internal knowledge assistant, content verification, or Business Brain Capture?
7. **Compliance:** What has been disclosed/approved for outside work, and what public language remains off-limits?
8. **Value metrics:** For the first client, what metric would make the project clearly worth the money?

---

---

# References

[R1] McKinsey, "The State of AI: Global Survey 2025," Nov. 5, 2025. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

[R2] McKinsey, "The State of AI: How organizations are rewiring to capture value," Mar. 12, 2025. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value

[R3] Deloitte, "The State of AI in the Enterprise - 2026 AI report." https://www.deloitte.com/ce/en/issues/generative-ai/state-of-ai-in-enterprise.html

[R4] Stanford HAI, "The 2025 AI Index Report." https://hai.stanford.edu/ai-index/2025-ai-index-report

[R5] Federal Reserve, "Monitoring AI Adoption in the U.S. Economy," Apr. 3, 2026. https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html

[R6] U.S. Chamber of Commerce, "The Majority of Small Businesses Embrace Artificial Intelligence," Aug. 18, 2025. https://www.uschamber.com/technology/empowering-small-business-the-impact-of-technology-on-u-s-small-business

[R7] JPMorgan Chase Institute, "Understanding the use of AI among small businesses," Apr. 14, 2026. https://www.jpmorganchase.com/institute/all-topics/business-growth-and-entrepreneurship/understanding-ai-use-by-small-businesses

[R8] IBM, "The 5 biggest AI adoption challenges for 2025." https://www.ibm.com/think/insights/ai-adoption-challenges

[R9] OpenAI, "Prompt engineering." https://developers.openai.com/api/docs/guides/prompt-engineering

[R10] Anthropic, "Prompt engineering overview" and "Prompting best practices." https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

[R11] Verizon Business, "Small Business Survey 2025." https://www.verizon.com/about/news/small-business-survey

[R12] Google Cloud, "Prompt Engineering for AI Guide." https://cloud.google.com/discover/what-is-prompt-engineering

[R13] GitHub Docs, "About GitHub Copilot cloud agent." https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent

[R14] GitHub Docs, "Research, plan, and iterate on code changes with Copilot cloud agent." https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/research-plan-iterate

[R15] OpenAI, "Structured model outputs." https://developers.openai.com/api/docs/guides/structured-outputs

[R16] OpenAI, "Evaluate agent workflows." https://developers.openai.com/api/docs/guides/agent-evals

[R17] OpenAI Agents SDK, "Tracing." https://openai.github.io/openai-agents-python/tracing/

[R18] LangChain Docs, "LangSmith Observability." https://docs.langchain.com/langsmith/observability

[R19] Toni Montez, "The Operating Doc: Methodology, Competitive Landscape, and Positioning for a Solo AI Consulting Practice," uploaded internal document, April 2026.

[R20] OWASP, "Top 10 for Large Language Model Applications." https://owasp.org/www-project-top-10-for-large-language-model-applications/

[R21] Anthropic, "Mitigating the risk of prompt injections in browser use," Nov. 24, 2025. https://www.anthropic.com/news/prompt-injection-defenses

[R22] NIST, "AI Risk Management Framework." https://www.nist.gov/itl/ai-risk-management-framework

[R23] Microsoft Investor Relations, "FY26 Q3 Earnings Conference Call," Apr. 29, 2026. https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3
