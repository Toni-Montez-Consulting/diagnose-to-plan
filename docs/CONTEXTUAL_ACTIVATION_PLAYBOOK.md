# Contextual Activation Playbook

Status: operating contract for turning Toni's ideas, designs, and work prompts
into the right next action without relying on memory.

This playbook sits between the raw prompt and the roadmap. It is the "what should
activate now?" layer for development enhancements, development work, project/client
work, business ideas, proof candidates, research, process improvements, and
agent/skill automation ideas.

## Activation Ladder

Use the lightest rung that captures the idea and protects the right gate.

1. Capture the raw idea.
2. Classify the idea type.
3. Attach it to the owning repo or mark it workspace-wide.
4. Attach it to an existing roadmap epic/story or create a candidate story.
5. Activate the right skill, template, gate, or repo lane.
6. Choose the next artifact: answer, story, spec, decision record, proof item,
   research item, eval/lesson, repo manifest update, implementation plan, direct
   implementation, or parked item.
7. Run the gates for the chosen artifact.
8. Update the steward/backlog only when status actually changes.

## Idea Types

| Idea type | Use when Toni says | Primary activation | Typical artifact | Gate |
|---|---|---|---|---|
| Development enhancement | "make this cleaner", "improve this infra", "add better checks" | `tm-skills/testing-ladder` or `delivery-baseline`; repo manifest | work item spec or implementation | local gates before CI |
| Development implementation | "build this", "fix this", "add this feature" | repo-specific skill/context plus story activation index | implementation plan or direct code change | repo tests/build/CI |
| Product/design | "new UI", "design idea", "make this experience better" | `tm-skills/frontend-craft`, Command Room fit if owner-facing | design spec or frontend implementation | visual/mobile QA and product boundary |
| Project/client work | "Mom nonprofit", "client kit", "handoff" | Client Operating Kit and steward review | private kit, runbook, proof packet | consent, COI, redaction |
| Business/offer/pricing | "new offer", "package this", "how do I sell this" | Practice Production Roadmap and offer docs | decision record or roadmap story | public claims need proof |
| Proof/case study | "can this become proof", "case study", "show this publicly" | proof/redaction templates | proof packet, asset inventory, claim review | evidence, caveat, permission, reviewer |
| Research/tooling | "research this", "should we adopt X" | research radar or research spike | Adopt/Pilot/Watch/Reject item | primary/official sources |
| Process/infrastructure | "make this repeatable", "avoid memory", "agent manager" | Roadmap Steward, story activation, workspace efficiency | template, backlog story, decision record | no autonomy before evals/guardrails |
| Agent/skill/automation | "trigger agents", "self-learning", "skills" | Activation Map, Story Activation Index, Future Intelligence | skill update, eval, guardrail plan | no global install/autonomy without approval |
| COI/privacy/security | "DSE", "Microsoft", "private data", "safe to publish" | COI screen, redaction policy, AI red-team if applicable | review item or parked story | pause before implementation |

## Steward Intake Rule

When a prompt introduces a new idea or design, the Roadmap Steward should answer
these questions before implementation:

- Is this a current active story, a new candidate story, a proof item, a research
  item, a decision record, an eval/lesson, a repo touch pass, or parked?
- Which repo owns it?
- Which skill/template should activate?
- What is the smallest useful next artifact?
- What must not be touched yet?
- Which gate makes the next step done?

Use `practice-os/templates/contextual-idea-intake.md` when the prompt is more than
a quick answer or when the idea could affect multiple repos, business strategy,
public proof, client work, agent behavior, or automation.

## Tie-In Files

- Prompt routing: `practice-os/templates/activation-routing-map.md`
- Story routing: `docs/ROADMAP_STORY_ACTIVATION_INDEX.md`
- Steward review: `practice-os/templates/roadmap-steward-review.md`
- One-off story activation: `practice-os/templates/story-activation-contract.md`
- Idea intake template: `practice-os/templates/contextual-idea-intake.md`
- Owner call extraction: `practice-os/templates/owner-call-to-action-extraction.md`
- Kanban backlog: `docs/ROADMAP_EXECUTION_BACKLOG.md`

## No-Touch Defaults

- Do not spawn subagents unless Toni explicitly asks for agents/delegation/parallel work.
- Do not globally install skills unless explicitly approved.
- Do not publish proof without evidence, caveat, permission, redaction, and reviewer.
- Do not start hosted DTP implementation from an idea intake alone.
- Do not mutate sibling repos unless the owning lane is active and gates are known.
- Do not let a new idea overwrite the current active queue unless Toni explicitly changes priority.
