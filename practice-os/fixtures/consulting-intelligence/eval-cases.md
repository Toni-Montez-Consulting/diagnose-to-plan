---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Consulting Intelligence Eval Cases

These are lightweight golden-case prompts for the Business Brain loop. They are
not automated yet; use them during weekly reset or future eval-garden work.

## Diagnosis Quality

- Input: A founder describes a marketplace/product idea with unclear build
  scope, possible investor/buyer context, and no confirmed data access.
- Good answer: separates business question from build question, asks only
  non-blocking clarifiers, proposes a small evidence-producing next step, and
  records COI/proof gates.
- Bad answer: jumps directly to app architecture, promises outcomes, or treats
  private material as proof.

## Scope Shaping

- Input: A prospective client wants an "AI system" but mostly has workflow
  bottlenecks, owner memory, and scattered documents.
- Good answer: maps current workflow, names non-AI fixes first, proposes a
  narrow implementation slice, and defines handoff/evidence gates.
- Bad answer: sells a generic chatbot or broad platform before the workflow is
  understood.

## Proof Safety

- Input: A completed project has useful screenshots, a positive owner reaction,
  and private details mixed into the source material.
- Good answer: creates proof candidate, evidence checklist, redaction item,
  permission review, caveat, and parked status until approved.
- Bad answer: writes public case-study copy from private notes.

## Follow-Up Quality

- Input: A client replied positively but still owes source files or meeting
  availability.
- Good answer: drafts a short owner-friendly reply, records waiting state, and
  avoids creating repo/build work before the requested packet arrives.
- Bad answer: starts implementation or sends a long technical message.

## Handoff Quality

- Input: A local business site or app is nearly launch-ready but the owner must
  operate it after delivery.
- Good answer: produces a simple runbook, account ownership notes, verification
  receipt, and manual gates; recommends a command room only if recurring pain is
  proven.
- Bad answer: adds a portal because it is interesting.

## Operator Voice

- Input: Public-facing copy needs to describe Toni's work.
- Good answer: direct, specific, implementation-first, evidence-backed,
  non-generic, and honest about manual gates.
- Bad answer: uses vague AI-agency language, hype, or inflated claims.

## Memory Spine App Round Trip

- Input: Hosted DTP imports a sanitized DTP operating artifact and exports a
  markdown fallback with hosted record pointers.
- Good answer: preserves DTP as source of truth, verifies Auth/RLS and
  second-operator isolation, keeps data class/permission/redaction/proof/source
  fields intact, and records correction hooks before widening automation.
- Bad answer: stores client facts only in Supabase, drops gates during export,
  treats smoke proof as public proof, or uses the round trip to unlock FAOS or
  autonomous agents early.
