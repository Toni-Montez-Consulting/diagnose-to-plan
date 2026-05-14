---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Platform Operating Patterns V0 Receipt

## Trigger

Toni liked the operating feel of Vercel and Supabase and asked whether those
platform behaviors could be extracted into the consulting practice and active
repos. He also asked to hold the Greg soft-launch proof until after tomorrow's
meeting.

## Scope

Docs/protocol only in DTP.

Included:

- platform-inspired operating plan;
- reusable manual templates;
- draft internal pattern candidates;
- Workspace OS and roadmap pointers.

Excluded:

- Greg soft-launch proof receipt or public proof movement;
- consulting public copy;
- Hub runtime changes;
- Vercel/Supabase dashboard changes;
- production writes;
- app code;
- hosted DTP behavior;
- `tm-skills` mutation.

## Artifacts Added

- `docs/PLATFORM_OPERATING_PATTERNS_V0.md`
- `practice-os/templates/platform-preview-receipt.md`
- `practice-os/templates/environment-ledger.md`
- `practice-os/templates/data-boundary-ledger.md`
- `practice-os/templates/client-handoff-console-spec.md`
- `practice-os/templates/launch-momentum-receipt.md`
- `practice-os/research/pattern-candidates/2026-05-14-preview-to-production-ladder.md`
- `practice-os/research/pattern-candidates/2026-05-14-environment-ledger-as-delivery-control.md`
- `practice-os/research/pattern-candidates/2026-05-14-data-boundary-ledger.md`
- `practice-os/research/pattern-candidates/2026-05-14-client-handoff-console.md`
- `practice-os/research/pattern-candidates/2026-05-14-launch-momentum-receipt.md`

## What Was Extracted

| Platform behavior | Workspace OS translation |
|---|---|
| Vercel preview and production deployment levels | Preview-to-production claim ladder |
| Vercel environment scopes and deployment state | Environment ledger with secret-free config names and proof paths |
| Vercel storage marketplace and managed integrations | Tool choice belongs in the Tooling Steward and active repo lane, not default stack doctrine |
| Supabase local development and migrations | Data changes should have reset/test/migration proof before handoff |
| Supabase RLS and auth boundaries | Data boundary ledgers should name exposure, policies, service-role paths, and public-safe surfaces |
| Platform dashboards | Client handoff consoles should show owner decisions, not raw implementation guts |
| Starter templates | DTP templates should reduce blank-page friction without making projects generic |

## Soft-Launch Boundary

The Launch Momentum Receipt template is ready, but Greg's current soft-launch
screenshots are not converted into a DTP artifact yet.

Reason:

- Toni is meeting with Greg tomorrow.
- Decisions should wait for that conversation.
- The screenshots contain private/user-identifying material and need redaction
  and permission review before any public proof movement.

Safe next move after the meeting:

1. Summarize what Greg confirms.
2. Create a private Launch Momentum Receipt if Toni wants it.
3. Decide whether the signal changes product, support, advertising, proof, or
   handoff next actions.
4. Only then consider proof packet inputs.

## Evidence Sources

Official/reference sources used for pattern extraction:

- Vercel Deploying to Vercel:
  `https://vercel.com/docs/deployments/deployment-methods`
- Vercel Environment Variables:
  `https://vercel.com/docs/projects/environment-variables`
- Vercel Storage:
  `https://vercel.com/docs/storage`
- Supabase local development with migrations:
  `https://supabase.com/docs/guides/cli/local-development`
- Supabase Row Level Security:
  `https://supabase.com/docs/guides/database/postgres/row-level-security`

Internal DTP sources used:

- `docs/CONSULTING_WORKSPACE_OS_V0.md`
- `docs/UAT_KIT_V0.md`
- `practice-os/templates/uat-receipt.md`
- `practice-os/templates/pre-ship-integrity-gate.md`
- `practice-os/policies/integrity-layer-craft-standard.md`

## Acceptance

- The platform inspiration is captured as DTP-owned operating behavior, not
  as a tool mandate.
- The artifacts stay manual/docs-first.
- Runtime, public copy, client communication, and proof promotion remain
  separate gates.
- A future agent can choose the right template based on claim level, environment
  state, data boundary, handoff surface, or launch signal.

## Next Actions

1. Use the Launch Momentum Receipt only after the Greg meeting if Toni decides
   to capture the soft-launch signal.
2. Use the Environment Ledger and Platform Preview Receipt on the next Hub
   runtime/dependency cleanup lane.
3. Use the Data Boundary Ledger on the next Omnexus release-proof or Hub data
   cleanup lane.
4. Use the Client Handoff Console Spec when CCAAP, DeMario, or another client
   lane needs operator-facing handoff.
5. Review these draft candidates after one or two real uses before promoting
   anything into `practice-os/patterns/` or `tm-skills`.

