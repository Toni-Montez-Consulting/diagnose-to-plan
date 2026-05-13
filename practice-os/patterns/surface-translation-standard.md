---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Surface Translation Standard

Status: reusable internal pattern.

Pattern: internal control stays visible to the operator; public and editor
surfaces get translated into the language of the person using them.

## When This Pattern Applies

Use this pattern when a site, admin dashboard, CMS/editor, client email, launch
packet, or owner handoff starts from build notes and risks exposing:

- agent instructions;
- prototype or launch-gate language;
- repo, schema, deploy, or validation mechanics;
- private proof or approval context;
- technical terms that the recipient does not need;
- stale one-off improvements that should become reusable standards.

## Core Principle

Do not make users carry the builder's context.

The system may need ledgers, gates, validations, roles, private memories, and
proof posture internally. The surface should show the next useful action in
audience language.

## Reusable Shape

1. Identify the audience and job.
2. Separate internal controls from user-facing confidence.
3. Translate implementation nouns into task verbs.
4. Remove context leakage from public/editor/client surfaces.
5. Preserve safety boundaries in the right place.
6. Verify the real surface on desktop and mobile when UI is affected.
7. Capture the correction as a reusable prompt, checklist, skill, or pattern
   when it is likely to recur.

## Examples

| Internal wording | Better surface wording |
|---|---|
| launch gate | final item to confirm |
| static rebuild | website refresh |
| CMS document | update |
| ownerApprovalStatus | photo approval |
| candidate PayPal route | PayPal link to review |
| repo-managed content | handled through the launch checklist |
| V1 scope | for launch |

## Checklist

- [ ] The public/user surface has no build notes, agent prompts, raw transcript
      language, or internal process narration.
- [ ] Admin/editor navigation uses tasks, not database terms.
- [ ] Owner/client emails explain why exact confirmations matter without
      re-asking already captured answers.
- [ ] Private data and proof gates remain visible internally but are not
      overexposed externally.
- [ ] A repeated fix is promoted into a reusable doc, prompt, skill, or pattern
      instead of staying as chat-only memory.

## Related Patterns

- `admin-surface-operating-room.md`
- `status-surface-before-scale.md`
- `practice-os/policies/authentic-voice-and-anti-slop.md`
