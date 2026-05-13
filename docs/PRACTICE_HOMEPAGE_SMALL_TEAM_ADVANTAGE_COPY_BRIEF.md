---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Practice Homepage Small Team Advantage Copy Brief

Status: internal public-copy brief

Owner: `diagnose-to-plan`, with later implementation in `consulting`

Source:
`practice-os/comms/private/small-team-advantage-positioning-memo-2026-05-10.md`

This brief has now been implemented in the consulting homepage as the compact
`#why-now` section. It remains the source note for future refinements to the
Small Team Advantage point of view.

## Recommendation

Make the idea visible soon as a supporting "why now" section.

Do not replace the homepage hero.

Current hero anchor:

> Turn the work in your head into systems your business can actually run.

Add the new section directly after the hero and before the three public doors.
That placement lets the visitor understand the market shift before choosing
whether they need to clarify, build, or improve.

## Section Job

The section should make the visitor believe:

- small teams can now do more than they could a few years ago;
- more tools do not automatically create leverage;
- the real advantage is deciding what should be built, bought, automated,
  left manual, and handed off;
- Toni's value is practical judgment plus implementation, not AI hype or
  strategy theater.

## Audience Balance

Write for both audiences at the same time:

- existing owner-led businesses with manual drag, scattered workflows, or
  practical AI/tooling questions;
- solo founders and early startup founders with an idea that needs to become a
  useful first system without expensive wrong turns.

The common buyer signal is:

> person starting or running a business with real intent, limited internal
> technical capacity, and a need for judgment plus implementation.

## Recommended Section Copy

Use this as the first implementation candidate:

```text
Small teams have more leverage than ever.

AI, cloud tools, APIs, and modern app workflows make it possible to build
systems that used to require a bigger team. But leverage does not come from
adding more tools. It comes from knowing what to build first, what to leave
alone, and how to turn the work into something the business can actually run.

That is where I help: clarify the bottleneck, sequence the work, build the
useful version, and hand it off cleanly.
```

Optional close line:

```text
Not more tools. Not a strategy deck. A working system.
```

Use the optional close line if the page needs a stronger bridge into the three
doors or the implementation promise. Skip it if it feels repetitive with the
later "No strategy deck dead-end" section.

## Alternate Copy Candidates

### More Founder-Oriented

```text
It is easier than ever to build something. It is still hard to build the right
thing.

Modern tools can help a small team move quickly, but speed only helps when the
work is aimed at the right problem. I help founders and operators decide what
should happen first, build the useful version, and avoid adding complexity the
business cannot operate.
```

### More Existing-Business-Oriented

```text
Most small businesses do not need another random tool first.

They need the work organized into a system: what comes in, who owns it, what
gets automated, what stays human, and how the business keeps moving when the
owner is not personally carrying every detail.
```

### More Point-Of-View

```text
AI did not make building easy. It made deciding more important.

Small teams can now build faster, but the risk is also higher: tool sprawl,
half-finished systems, unclear handoff, and automation attached to the wrong
workflow. The advantage belongs to teams that turn work into clear operating
systems.
```

## Heading Decision

Use this public heading first:

> Small teams have more leverage than ever.

Keep this as the internal pillar name:

> Small Team Advantage

Use with caution:

> Build the systems of a larger company without the overhead.

That line is strong, but it can imply enterprise mimicry or overbuilding if it
appears too early. It is better as a supporting line, content hook, or later
section headline after the page already establishes practical systems and
owner-operable work.

## Homepage Placement

Recommended section order:

1. Hero: thesis and broad CTA.
2. Why now: Small Team Advantage.
3. Three public doors: Clarify The Path, Build The System, Improve The System.
4. Blueprint bridge.
5. Implementation promise.
6. Proof cards.
7. Fit filter.
8. Final CTA.

## CTA Treatment

Do not add a new button unless the page feels long after implementation.

The section should naturally flow into the three doors. If a button is needed,
use the existing secondary CTA language:

> See How The Work Starts

Do not add a new AI-specific CTA.

## Public Copy Boundaries

Allowed:

- AI, cloud tools, APIs, and modern app workflows as broad context;
- practical judgment and implementation language;
- "small teams" and "owner-led businesses";
- "working system" and "business can run";
- human handoff and owner-operable systems.

Avoid:

- Microsoft endorsement or employer-adjacent credibility claims;
- enterprise AI strategy framing;
- "AI transformation";
- claims that AI makes everything easy;
- revenue, savings, or ROI claims;
- named client outcomes or metrics;
- implying every client engagement includes an AI feature.

## Authenticity Check

Before implementing in `consulting`, run the copy through this check:

- Does this still sound like Toni?
- Does it explain the practice without generic AI-agency language?
- Does it make a serious owner or founder feel seen?
- Does it preserve ambition without sounding hypey?
- Does it bridge into the three doors cleanly?
- Does it avoid unsupported claims?

## Implementation Notes For `consulting`

- Add this as a compact section, not a large manifesto.
- Keep the visual style consistent with Steel Ledger.
- Do not make it a decorative hero or a card-heavy marketing block.
- Keep text scannable on mobile.
- Do not expose internal labels like "Small Team Advantage" unless Toni
  chooses it as a visible content pillar.
- Keep exact pricing off this section.

## Implementation Receipt

Implemented in `consulting/src/pages/index.astro` on 2026-05-10.

Verification in `consulting`:

- `npm run build`
- `npm run assistant:qa`
- `npm run doctor`
- `npm run test:routes` with 32/32 passing
- `npm run security:secrets`

## Decisions

| Decision | Current recommendation | Status |
|---|---|---|
| Public heading | "Small teams have more leverage than ever." | implemented |
| Internal pillar name | "Small Team Advantage" | locked |
| Placement | after hero, before three doors | implemented |
| AI wording level | light and practical | implemented |
| Live site edit | compact `#why-now` homepage section in `consulting` | implemented 2026-05-10 |
