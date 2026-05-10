---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Agent Source Pack Schema V0

Purpose: keep the machine-readable agent source-pack file useful for future
sessions, dashboards, and stewards without letting it become hidden authority.

Canonical file:

```text
practice-os/research/source-packs/agent-source-packs.v0.json
```

Validation command:

```powershell
.\.venv\Scripts\dtp.exe practice source-packs validate
```

`dtp practice doctor` also runs this validation. The validator is deliberately
local, dependency-free, and contract-focused.

## Top-Level Contract

Required top-level fields:

- `schema_version`: must be `agent-source-packs.v0`.
- `review_status`: review state for the pack.
- `owner_repo`: repo that owns the pack.
- `created_at` and `updated_at`: date strings for operator review.
- `policy_doc`: local policy doc path.
- `governing_rule`: plain-language rule for source use.
- `authority_boundary`: explicit flags that prevent silent authority drift.
- `evidence_tiers`: evidence confidence model.
- `packs`: role-level source packs.

## Authority Boundary

Required flags:

- `adds_authority`: `false`
- `allows_web_search`: `true`
- `allows_autonomous_actions`: `false`
- `requires_human_promotion`: `true`

The source pack can inform a role. It cannot approve public claims, client
communication, legal/finance/compliance advice, repo mutation, production
deployment, secret movement, billing changes, or autonomous runtime behavior.

## Evidence Tiers

The V0 pack must include tiers `0` through `4`:

- `0`: owner-verified local truth.
- `1`: repo-local committed source.
- `2`: official or primary external source.
- `3`: reputable secondary source.
- `4`: broad web discovery or weak signal.

Broad web evidence can start discovery, but it needs corroboration and human
review before promotion.

## Role Pack Contract

Each item in `packs` requires:

- `role_id`: unique machine-readable role id.
- `role_name`: human-readable role name.
- `source_pack_version`: version/date for that role pack.
- `status`: current review status.
- `last_reviewed_at`: review date.
- `pilot_artifacts`: local evidence files proving the role shape.
- `primary_sources`: role-specific source list.
- `allowed_web_sources`: source categories the role can search.
- `search_posture`: how search should be trusted and queried.
- `blocked_sources`: sources or source behaviors to avoid.
- `default_outputs`: artifacts the role may produce.
- `promotion_required_for`: actions requiring review/approval.
- `next_review_trigger`: what should reopen the pack.

## Primary Source Contract

Each `primary_sources` entry requires:

- `id`: unique source id inside the role pack.
- `tier`: evidence tier.
- `type`: source type.
- `path_or_url`: local path, URL, or descriptive source pointer.
- `use`: how the source should be used.
- `evidence_limit`: what the source does not prove.

## Validator Scope

The validator checks:

- JSON readability.
- required top-level fields.
- authority-boundary flags.
- evidence tiers `0-4`.
- unique role ids.
- required role-pack fields.
- required primary-source fields.
- local pilot-artifact existence.

The validator does not check live web freshness, source quality, public-copy
eligibility, or whether a role should be promoted. Those remain human-gated
stewardship decisions.

## Status Dashboard

The first scalable layer now consumes the validator result:

```powershell
.\.venv\Scripts\dtp.exe practice source-packs status
.\.venv\Scripts\dtp.exe practice source-packs dashboard
```

The status command summarizes role freshness, source counts, promotion gates,
and validation problems. The dashboard command writes:

```text
docs/source-pack-status-dashboard.html
```

This remains a local read-only view. It does not check live web freshness,
promote sources, approve role behavior, sync Notion, or authorize external
actions.

## Future Growth

Future layers should keep consuming the same validator/status model rather than
inventing a second contract:

- source decay / stale source prompts;
- live source-freshness evidence after review;
- broader squad roster coverage;
- autonomy-readiness evidence gates.
