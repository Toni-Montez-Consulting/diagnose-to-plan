---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# UAT Kit V0

Status: DTP-owned manual UAT standard for the Consulting Workspace OS.

Use this kit when a site, app, workflow, client handoff, public proof surface,
operator dashboard, AI-assisted feature, or reusable pattern needs acceptance
evidence beyond "the tests passed" or "the demo worked once."

## Purpose

UAT Kit V0 turns user acceptance testing into a repeatable operating artifact.
It connects:

- requirements and acceptance criteria from the Requirements Gatherer;
- repo-local tests and checks from each implementation repo;
- Integrity Layer checks for truth, usefulness, restraint, durability, and
  handoff;
- proof, privacy, and public-claim gates from DTP.

It is manual and docs-first. It does not add browser automation, a hosted
dashboard, cross-repo runners, public copy, production writes, or runtime
behavior.

## Boundary

| Layer | Role |
|---|---|
| Requirements Gatherer | defines what the work should do and what acceptance means |
| Repo-local gates | prove build, lint, tests, route checks, or platform checks passed |
| UAT Kit | checks the human journey, device states, failures, evidence, and caveats |
| Integrity Layer | asks whether the result is honest, useful, restrained, durable, and handoff-ready |
| Pre-Ship Integrity Gate | final ship/handoff check for meaningful work |
| Proof promotion | separate gate before public claims, screenshots, case studies, or metrics move |

## When To Use

Use UAT Kit V0 for:

- public-facing route or copy changes;
- client-facing or owner-facing handoff work;
- operator/admin surfaces;
- app releases or launch-candidate flows;
- AI-assisted workflows where output quality affects decisions;
- data-sensitive or permission-sensitive workflows;
- reusable pattern candidates before promotion;
- any work where a user journey matters more than a unit test.

Tiny hotfixes may use a lighter gate: impact, rollback, verification, and known
risk. Do not use UAT Kit V0 to slow down purely mechanical docs edits.

## UAT Flow

1. Name the claim.
   - What are we trying to say is ready?
   - Is the claim local, live, client-facing, public-proof, or release-ready?

2. Name the journey.
   - Who is the user or operator?
   - What should they do from start to finish?
   - What is the expected next action?

3. Run the repo-local gates.
   - Use the owning repo's build, test, lint, security, route, or platform
     checks.
   - Mark skipped gates with a reason.

4. Run manual acceptance checks.
   - Core journey.
   - Mobile or small-screen state where relevant.
   - Desktop or wide state where relevant.
   - Error and empty states.
   - Auth, permission, data, and privacy boundaries where relevant.
   - AI output review where relevant.
   - Handoff and future-maintainer clarity where relevant.

5. Apply quality and integrity checks.
   - Are claims accurate?
   - Does the flow help the user decide, act, understand, or operate?
   - Is anything overbuilt, misleading, or harder than needed?
   - Is the evidence stronger than "it worked once"?
   - Can the client, operator, or future maintainer understand what to do next?

6. Record evidence and caveats.
   - Use `practice-os/templates/uat-receipt.md`.
   - Do not paste private rows, secrets, private screenshots, client data, or
     raw proof into public/tracked artifacts.
   - Use summarized fields and redacted evidence pointers.

7. Decide.
   - `pass`: ready for the stated claim.
   - `pass_with_caveats`: ready with named limits or manual follow-up.
   - `hold`: useful but not ready for the stated claim.
   - `block`: do not ship or hand off until a named issue is fixed.

## Default Check Matrix

| Check area | What to verify |
|---|---|
| Core journey | user can complete the main path and understands the outcome |
| Mobile / small screen | layout, text fit, navigation, form states, and primary action work |
| Desktop / wide screen | layout, hierarchy, scanability, and proof/CTA placement work |
| Error states | failures explain what happened and what to do next |
| Empty states | no-data states are useful and honest |
| Data and permissions | only necessary data is requested; private data stays protected |
| Claims and proof | no unsupported ROI, automation, AI, launch, or client-result claims |
| AI behavior | generated output is reviewed, constrained, and not treated as authority |
| Handoff | owner/client/future maintainer can operate the result or know where to look |
| Evidence | commands, screenshots, logs, receipts, or notes match the claim being made |
| Caveats | limits, manual gates, and cleanup debt are named instead of hidden |

## First Pilot Inputs

UAT Kit V0 should learn from the first Consulting Workspace OS pattern scan:

- Hub-first intake with DTP source of truth;
- post-submit Diagnostic Call gating;
- noindex admin command-room boundary;
- proof/readiness receipt with synthetic-intake cleanup debt.

The first practical use should be consulting or another already-active lane.
Do not bulk-apply this kit across inactive repos.

## Done Criteria

A UAT pass is complete when:

- the claim is clear;
- the user journey is named;
- repo-local gates are recorded;
- manual checks are recorded;
- evidence and caveats are captured;
- privacy/proof boundaries are respected;
- Integrity Layer questions are answered;
- the final decision is `pass`, `pass_with_caveats`, `hold`, or `block`;
- the next action is named.

## Future Promotion

After repeated use, consider:

- a narrower visual QA checklist;
- a design integrity review template;
- a mobile app UAT receipt variant;
- a client handoff UAT variant;
- `tm-skills` behavior only after real usage proves stable triggers and
  expected outputs.
