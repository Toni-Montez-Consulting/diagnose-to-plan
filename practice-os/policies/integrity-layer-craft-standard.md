---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Integrity Layer Craft Standard

Status: V0 internal standard for the Consulting Workspace OS.

Quality is downstream of process. Process is downstream of standards.
Standards are downstream of values. Values only hold under pressure when they
are built into the system.

## Purpose

The Integrity Layer is the quality standard underneath the Consulting Workspace
OS. It exists so the practice does not depend on everyone being clear, rested,
confident, disciplined, and perfectly honest in every moment.

It is not public marketing copy. It is not a moral scoreboard. It is not an app
that judges people. It is an internal operating layer that helps Toni and future
agents make the stronger choice when the work is rushed, ambiguous, exciting,
tedious, client-facing, or tempting to overbuild.

The mature frame is:

Systems should be designed with human weakness in mind, so weak moments do not
become bad outcomes.

## Standard

Build useful things. Tell the truth. Respect the user. Respect the client.
Respect the future maintainer. Test what matters. Document what matters. Hand
it off cleanly. Do not use complexity to hide weak thinking.

Strength does not mean force, ego, domination, or trying to look impressive.
Strength means the ability to stay honest, useful, restrained, clear, and kind
under pressure.

## What The System Guards Against

Bad outcomes usually do not come out of nowhere. A messy app, brittle workflow,
confusing dashboard, or weak handoff usually starts with a process miss.

Watch for:

- rushing;
- hiding uncertainty;
- wanting to look smart;
- skipping boring work;
- chasing novelty;
- overbuilding;
- avoiding conflict;
- making the tool the point;
- making the client dependent;
- calling something done because the builder is tired of looking at it;
- choosing impressive over useful;
- letting AI-generated output pass because it looks polished.

## Core Principles

### 1. Truth Over Performance

Do not make the work look better than it is.

In practice:

- no fake AI claims;
- no inflated ROI claims;
- no pretending a prototype is a finished system;
- no hiding uncertainty;
- no unsupported "saves 20 hours a week" claims;
- no calling something automated when it still needs manual babysitting.

Question to ask: Am I saying what is true, or what sounds good?

### 2. Usefulness Over Impressiveness

A feature is not good because it is clever. It is good if it helps someone
decide, act, understand, or operate.

In practice:

- dashboards must answer real questions;
- AI assistants must reduce real friction;
- automations must remove real load;
- content must help the user move;
- design must clarify the task;
- every feature needs a reason to exist.

Question to ask: What does this help the user do?

### 3. Restraint Over Excess

Strong builders do not build everything they can build.

In practice:

- do not add features just because the tool can;
- do not automate unclear processes;
- do not add stack complexity without a reason;
- do not build a custom system when buying is better;
- do not chase the newest tool without a real use case;
- do not force Phase 2 ideas into Phase 1.

Question to ask: Is this necessary now, or is this ego, fear, or novelty?

### 4. Handoff Over Dependency

The client should not be trapped.

In practice:

- client owns accounts and billing when practical;
- a runbook is required for meaningful client/operator work;
- decisions are documented;
- common breakpoints are explained;
- future maintainers can understand the system;
- retainer support is optional value, not hostage-taking.

Question to ask: Could the client or a future maintainer understand this
without me?

### 5. Durability Over Speed Theater

Moving fast is good only if the thing still works.

In practice:

- core flows get UAT;
- error states are handled;
- telemetry exists where decisions depend on it;
- auth and data rules are checked;
- mobile experience is tested;
- launch readiness is real;
- the demo working once is not proof the system works.

Question to ask: What proves this works besides my confidence?

### 6. Kindness Through Clarity

Kindness is not avoiding the truth. Kindness is making the truth usable.

In practice:

- explain tradeoffs plainly;
- do not bury clients in jargon;
- do not shame people for messy systems;
- do not make people feel dumb for not knowing technical terms;
- tell them when the requested solution is not the right move;
- translate the work so they can own it.

Question to ask: Did I make this easier to understand, or did I make myself
look smart?

### 7. Strength Under Pressure

The standard matters most when the builder is tired, rushed, excited, trying to
impress someone, or trying to avoid a hard conversation.

In practice:

- do not skip the checklist because the demo looks good;
- do not ship without the runbook;
- do not accept vague scope creep;
- do not ignore compliance because the opportunity is attractive;
- do not say yes when the right answer is "not this way";
- do not lower the quality bar just because the client may not notice.

Question to ask: What would the stronger version of me do here?

## Method Checkpoints

Use these checks across the consulting method.

### Diagnose

- Am I hearing the real problem, or accepting the first version?
- Am I mapping the actual constraint?
- Am I telling the truth about what is worth doing?

### Plan

- Am I sequencing the work honestly?
- Am I shrinking scope instead of discounting quality?
- Am I choosing tools because they fit, not because I like them?

### Translate

- Am I making the client more capable?
- Am I using jargon to clarify or to impress?
- Can the client explain the plan in their own words?

### Build

- Am I shipping vertical slices?
- Am I documenting as I go?
- Am I testing what matters?
- Am I avoiding gold-plating?

### Hand Off

- Is the client independent enough to operate the result?
- Does the runbook exist?
- Are accounts, billing, ownership, and support paths clear?
- Could a future maintainer understand why decisions were made?

### Stay Close

- Am I providing real value?
- Am I watching for drift?
- Am I helping the client grow beyond me if that becomes the right move?

## AI Usage Standard

AI should speed up the work, but it should not lower the standard.

Rules:

- AI can draft, but Toni owns the final judgment.
- AI can generate code, but tests prove whether it works.
- AI can create UI, but design direction decides whether it is good.
- AI can suggest tools, but the tooling standard decides whether they fit.
- AI can write docs, but the client must be able to understand them.
- AI can automate, but unclear processes should be clarified before they are
  automated.
- AI can make things look polished, but polish cannot hide weak thinking.

## Workspace Integration

The Integrity Layer should show up in practical artifacts, not only as a memo.

Use it in:

- Requirements Gatherer briefs and decision ledgers;
- pattern cards;
- UAT standards;
- design reviews;
- build checklists;
- client handoff docs;
- tool selection;
- scope decisions;
- AI usage rules;
- business model decisions;
- compliance and proof checkpoints.

Start with `practice-os/templates/pre-ship-integrity-gate.md`. Later
iterations may add narrower design, UAT, AI, client-duty, and pattern-card
templates if repeated work proves those deserve their own artifacts.

## Pattern Card Integrity Questions

When a pattern may become reusable, ask:

- What could go wrong if this pattern is misused?
- Does this create dependency on Toni?
- Does this increase clarity or complexity?
- Does this respect the user's time and data?
- What would prove this works?
- What is the simpler version?
- What is the safer version?
- What should be documented before this ships?

## Promotion Rule

Do not turn this standard into public copy, client promises, skill behavior, or
repo-wide hard gates until it has been applied in real work and reviewed.

The first proof of value is better decisions, cleaner handoffs, fewer generic
AI outputs, and quality that Toni can defend.
