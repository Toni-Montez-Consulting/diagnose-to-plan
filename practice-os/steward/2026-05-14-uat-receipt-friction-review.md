---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# UAT Receipt Friction Review

## Session

- Date: 2026-05-14
- Reviewer: Codex for Toni
- Trigger: Three Consulting Workspace OS UAT receipts now exist and need a
  small evidence-based review before narrower templates or `tm-skills` behavior
  are created.
- Scope: DTP docs-only review of UAT Kit V0 receipt friction.
- Inputs:
  - `docs/UAT_KIT_V0.md`
  - `practice-os/templates/uat-receipt.md`
  - `practice-os/steward/2026-05-14-consulting-live-funnel-uat-pilot-receipt.md`
  - `practice-os/steward/2026-05-14-consulting-public-assistant-uat-receipt.md`
  - `practice-os/steward/2026-05-14-consulting-admin-command-room-uat-receipt.md`

## Summary Read

The base UAT receipt is working. It forced the right claims, caveats, privacy
boundaries, Integrity Layer checks, and final `pass_with_caveats` decisions.

The friction is not that the template is wrong. The friction is that it is a
full receipt being used across three different shapes:

- proof-readiness and live-funnel evidence;
- no-runtime assistant boundary review;
- public-safe operator/admin boundary review.

Those shapes need different emphasis, but they do not yet justify separate
canonical templates. The better V0.1 move is to keep the base receipt canonical
and add lightweight operating modes or overlays inside the UAT Kit guidance.

Do not create `tm-skills` behavior yet.

## Receipt Comparison

| Receipt | What worked | Friction | Read |
|---|---|---|---|
| Consulting live funnel / proof-readiness | Strong fit for claim limits, proof gates, Hub/DTP boundary, caveats, and next trigger | Some overlap between proof boundary fields and evidence/caveat fields | Keep base receipt; proof-readiness may later deserve a small overlay |
| Consulting public assistant no-runtime boundary | Strong fit for stopping runtime creep and naming what cannot be proven | Manual UAT rows for error, empty, mobile, desktop, and AI output were partly proxy checks because no runtime exists | Keep base receipt; add a boundary-only mode before creating an assistant-runtime variant |
| Consulting admin command-room boundary | Strong fit for noindex, sitemap, no-private-data, and operator-surface boundary | Error/empty/AI rows were mostly skipped; real operator usefulness remains observational | Keep base receipt; operator-surface overlay is justified only after another real admin/operator lane |

## Direct Answers

### Is The Base Template Working?

Yes. The base template reliably produced:

- a bounded claim;
- a clear "what this can and cannot prove" section;
- repo-local gate evidence;
- manual acceptance checks;
- Integrity Layer review;
- named caveats and cleanup debt;
- a final decision that did not overclaim.

The most valuable behavior is the claim boundary. It prevented internal
operational evidence from turning into public proof, runtime authority, or
skill behavior too early.

### Which Fields Felt Repeated, Too Heavy, Or Unclear?

Repeated:

- proof/redaction boundaries appear in metadata, evidence/caveats, and public
  proof notes;
- repo gates repeated across receipts when the same consulting commands covered
  multiple lanes;
- `pass_with_caveats` language repeated because every current pilot was an
  internal boundary, not a final launch.

Too heavy:

- full manual UAT rows are heavy for no-runtime, no-widget, or no-private-data
  boundary reviews;
- error and empty-state rows are often irrelevant when no user-facing runtime
  exists;
- AI output review is awkward when the assistant exists only as a manifest and
  refusal fixture.

Unclear:

- "Related decision ledger" is often missing or not the right artifact for a
  receipt-only review;
- "claim level" can mix production, internal pattern, and proof-readiness in a
  way future agents may need to explain more plainly;
- mobile/desktop checks should say whether they test the actual experience or a
  proxy route boundary.

### Do We Need Narrower Variants Yet?

Not as canonical templates.

We have enough evidence to name candidate modes, but not enough repeated use to
split the template. Splitting now would create template sprawl before DTP knows
which fields future receipts actually use.

Recommended V0.1 posture:

- keep `practice-os/templates/uat-receipt.md` as the base receipt;
- add lightweight mode guidance in `docs/UAT_KIT_V0.md`;
- wait for at least one non-consulting or client-facing receipt before creating
  a new template;
- keep `tm-skills` promotion blocked until the triggers and expected output are
  proven across more than consulting.

### Which Variants Are Justified By Evidence?

Evidence justifies these as candidate modes, not separate templates yet:

- Proof-readiness mode: best for funnel, launch, case-study, or public-claim
  evidence where the decision is about what can be said.
- Boundary-only mode: best for manifests, architecture boundaries, no-runtime
  gates, noindex routes, blocked private sources, and "do not build yet" lanes.
- Operator-surface mode: best for admin launchers, command rooms, dashboards,
  and internal task surfaces where usefulness and privacy matter more than
  public polish.

Evidence is not yet strong enough for:

- visual QA template;
- design integrity template;
- mobile app UAT template;
- client handoff template;
- assistant-runtime template;
- `tm-skills` UAT behavior.

Those should wait for one or two receipts outside the current consulting
boundary set.

### What Should Remain DTP-Only Before Any `tm-skills` Promotion?

Keep these in DTP:

- when to choose Micro, Standard, Deep, or Workshop discovery before UAT;
- when a UAT receipt is needed at all;
- when `pass_with_caveats` is the honest decision;
- how proof, privacy, and public-claim gates are stated;
- how to choose between proof-readiness, boundary-only, and operator-surface
  modes;
- how redaction checks and evidence pointers are recorded;
- how repeated friction becomes a template, eval, or skill update.

Only promote to `tm-skills` after DTP has at least:

- one more meaningful receipt outside the consulting no-runtime/admin boundary
  cluster;
- one clear example where a narrower mode reduced friction;
- one trigger/eval fixture showing when an agent should pick that mode;
- one reviewed expected-output example.

## Process Lesson

Do not run consulting `npm run build` in parallel with route tests that depend
on the built output. The build can clean `dist` while another process is still
reading from it. For future UAT receipts, run build and route/browser checks
sequentially unless the owning repo explicitly supports concurrent execution.

Also note that local PowerShell sessions may not have `dtp` on PATH. In this
repo, use `.venv\Scripts\dtp.exe` when needed.

## Decision

- Decision: keep the base UAT receipt canonical.
- New canonical template: no.
- New `tm-skills` behavior: no.
- UAT Kit guidance update: yes, add V0.1 mode guidance and this review pointer.
- Next receipt target: one meaningful non-consulting, client-handoff,
  app-release, visual/design, or runtime-assistant lane before template split.
- Owner: Toni
- Next review trigger:
  - another UAT receipt repeats the same skipped fields;
  - Toni asks for a visual QA, mobile app, client handoff, assistant-runtime,
    or operator-surface UAT template;
  - `tm-skills` promotion is reopened.

