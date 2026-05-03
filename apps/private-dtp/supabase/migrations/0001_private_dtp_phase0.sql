-- Private DTP Phase 0
-- Single-operator hosted schema for DTP engagement, evidence, redaction,
-- proof, decision, steward, and research records.

create extension if not exists pgcrypto;

create or replace function private_dtp_set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create table if not exists private_dtp_engagements (
  id uuid primary key default gen_random_uuid(),
  operator_id uuid not null default auth.uid(),
  title text not null,
  client_or_project_alias text not null,
  kind text not null check (
    kind in ('client', 'internal', 'product', 'proof_track', 'family_private')
  ),
  stage text not null default 'intake' check (
    stage in (
      'intake',
      'diagnose',
      'plan',
      'build',
      'handoff',
      'support',
      'proof_review',
      'archived'
    )
  ),
  sensitivity text not null default 'internal_only' check (
    sensitivity in ('public', 'internal_only', 'private', 'client_confidential', 'coi_review')
  ),
  owner text,
  source_repo text,
  local_pointer text,
  unique (id, operator_id),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists private_dtp_artifacts (
  id uuid primary key default gen_random_uuid(),
  operator_id uuid not null default auth.uid(),
  engagement_id uuid not null,
  artifact_type text not null check (
    artifact_type in (
      'note',
      'kit_doc',
      'screenshot',
      'report',
      'evidence',
      'runbook',
      'decision',
      'asset',
      'other'
    )
  ),
  title text not null,
  source_kind text not null check (
    source_kind in ('local_markdown', 'repo_file', 'ci_artifact', 'upload', 'external_link', 'hub_reference')
  ),
  source_pointer text not null,
  storage_pointer text,
  summary text,
  data_class text not null default 'P1',
  permission_level text not null default 'internal_only',
  redaction_status text not null default 'not_reviewed' check (
    redaction_status in ('not_reviewed', 'needs_redaction', 'redacted', 'public_safe', 'restricted')
  ),
  proof_eligibility text not null default 'not_candidate' check (
    proof_eligibility in ('not_candidate', 'candidate', 'approved', 'rejected')
  ),
  unique (id, operator_id),
  foreign key (engagement_id, operator_id)
    references private_dtp_engagements(id, operator_id)
    on delete cascade,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists private_dtp_artifact_versions (
  id uuid primary key default gen_random_uuid(),
  operator_id uuid not null default auth.uid(),
  artifact_id uuid not null,
  version_label text not null,
  source_pointer text not null,
  storage_pointer text,
  summary text,
  foreign key (artifact_id, operator_id)
    references private_dtp_artifacts(id, operator_id)
    on delete cascade,
  created_at timestamptz not null default now()
);

create table if not exists private_dtp_evidence_runs (
  id uuid primary key default gen_random_uuid(),
  operator_id uuid not null default auth.uid(),
  engagement_id uuid,
  repo text not null,
  branch text,
  commit_sha text,
  lane text not null check (lane in ('local', 'ci', 'release', 'support', 'proof', 'manual')),
  result text not null check (
    result in ('pass', 'fail', 'advisory_pass', 'manual_pending', 'not_checked')
  ),
  commands text[] not null default '{}',
  hard_gate_status text not null default 'not_checked',
  advisory_gate_status text not null default 'not_checked',
  manual_gate_status text not null default 'not_checked',
  artifact_path text,
  redaction_status text not null default 'not_reviewed',
  reviewer text,
  notes text,
  unique (id, operator_id),
  foreign key (engagement_id, operator_id)
    references private_dtp_engagements(id, operator_id)
    on delete cascade,
  created_at timestamptz not null default now()
);

create table if not exists private_dtp_redaction_reviews (
  id uuid primary key default gen_random_uuid(),
  operator_id uuid not null default auth.uid(),
  engagement_id uuid,
  target_type text not null check (
    target_type in ('artifact', 'evidence_run', 'proof_candidate')
  ),
  target_id uuid not null,
  reviewer text,
  status text not null default 'not_started' check (
    status in ('not_started', 'needs_changes', 'approved_internal', 'approved_public', 'rejected')
  ),
  permission_level text not null default 'internal_only' check (
    permission_level in (
      'internal_only',
      'owner_approved',
      'client_approved',
      'public_safe',
      'restricted'
    )
  ),
  notes text,
  foreign key (engagement_id, operator_id)
    references private_dtp_engagements(id, operator_id)
    on delete cascade,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists private_dtp_proof_candidates (
  id uuid primary key default gen_random_uuid(),
  operator_id uuid not null default auth.uid(),
  engagement_id uuid not null,
  artifact_id uuid,
  public_claim text,
  baseline text,
  after_state text,
  metric text,
  caveat text,
  evidence_source text,
  permission_status text not null default 'not_requested' check (
    permission_status in (
      'not_requested',
      'owner_approved',
      'client_approved',
      'public_safe',
      'rejected',
      'restricted'
    )
  ),
  redaction_status text not null default 'not_reviewed' check (
    redaction_status in (
      'not_reviewed',
      'needs_redaction',
      'approved_internal',
      'approved_public',
      'public_safe',
      'rejected'
    )
  ),
  reviewer text,
  status text not null default 'proposed' check (
    status in (
      'proposed',
      'needs_evidence',
      'needs_permission',
      'approved',
      'rejected',
      'parked'
    )
  ),
  check (
    status <> 'approved'
    or (
      nullif(trim(public_claim), '') is not null
      and nullif(trim(evidence_source), '') is not null
      and nullif(trim(caveat), '') is not null
      and permission_status in ('owner_approved', 'client_approved', 'public_safe')
      and redaction_status in ('approved_public', 'public_safe')
      and nullif(trim(reviewer), '') is not null
    )
  ),
  unique (id, operator_id),
  foreign key (engagement_id, operator_id)
    references private_dtp_engagements(id, operator_id)
    on delete cascade,
  foreign key (artifact_id, operator_id)
    references private_dtp_artifacts(id, operator_id),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists private_dtp_decisions (
  id uuid primary key default gen_random_uuid(),
  operator_id uuid not null default auth.uid(),
  engagement_id uuid,
  title text not null,
  status text not null default 'proposed' check (
    status in ('proposed', 'accepted', 'superseded', 'rejected')
  ),
  context text,
  options_considered text,
  chosen_path text,
  consequences text,
  related_artifact_id uuid,
  related_evidence_run_id uuid,
  foreign key (engagement_id, operator_id)
    references private_dtp_engagements(id, operator_id)
    on delete cascade,
  foreign key (related_artifact_id, operator_id)
    references private_dtp_artifacts(id, operator_id),
  foreign key (related_evidence_run_id, operator_id)
    references private_dtp_evidence_runs(id, operator_id),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists private_dtp_steward_items (
  id uuid primary key default gen_random_uuid(),
  operator_id uuid not null default auth.uid(),
  title text not null,
  item_type text not null check (
    item_type in ('correction', 'memory_candidate', 'roadmap_item', 'blocked_gate', 'follow_up')
  ),
  source_pointer text,
  destination_pointer text,
  status text not null default 'open' check (
    status in ('open', 'approved', 'promoted', 'parked', 'rejected', 'done')
  ),
  sensitivity text not null default 'internal_only',
  human_approval text,
  notes text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists private_dtp_research_items (
  id uuid primary key default gen_random_uuid(),
  operator_id uuid not null default auth.uid(),
  title text not null,
  source_url text,
  source_pointer text,
  classification text not null default 'watch' check (
    classification in ('adopt', 'pilot', 'watch', 'reject')
  ),
  decision_reason text,
  linked_roadmap_item text,
  status text not null default 'open' check (
    status in ('open', 'accepted', 'parked', 'rejected', 'done')
  ),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists private_dtp_import_export_receipts (
  id uuid primary key default gen_random_uuid(),
  operator_id uuid not null default auth.uid(),
  direction text not null check (direction in ('import', 'export')),
  source_pointer text not null,
  destination_pointer text,
  result text not null check (result in ('pass', 'fail', 'partial', 'manual_pending')),
  record_counts jsonb not null default '{}'::jsonb,
  notes text,
  created_at timestamptz not null default now()
);

create index if not exists private_dtp_engagements_operator_stage_idx
on private_dtp_engagements(operator_id, stage, updated_at desc);

create index if not exists private_dtp_artifacts_engagement_idx
on private_dtp_artifacts(operator_id, engagement_id, updated_at desc);

create index if not exists private_dtp_artifacts_review_idx
on private_dtp_artifacts(operator_id, redaction_status, proof_eligibility);

create index if not exists private_dtp_artifact_versions_artifact_idx
on private_dtp_artifact_versions(operator_id, artifact_id, created_at desc);

create index if not exists private_dtp_evidence_runs_engagement_idx
on private_dtp_evidence_runs(operator_id, engagement_id, created_at desc);

create index if not exists private_dtp_evidence_runs_repo_lane_idx
on private_dtp_evidence_runs(operator_id, repo, lane, created_at desc);

create index if not exists private_dtp_redaction_reviews_queue_idx
on private_dtp_redaction_reviews(operator_id, status, updated_at desc);

create index if not exists private_dtp_proof_candidates_queue_idx
on private_dtp_proof_candidates(operator_id, status, updated_at desc);

create index if not exists private_dtp_decisions_engagement_idx
on private_dtp_decisions(operator_id, engagement_id, updated_at desc);

create index if not exists private_dtp_steward_items_status_idx
on private_dtp_steward_items(operator_id, status, updated_at desc);

create index if not exists private_dtp_research_items_status_idx
on private_dtp_research_items(operator_id, classification, status, updated_at desc);

create trigger private_dtp_engagements_updated_at
before update on private_dtp_engagements
for each row execute function private_dtp_set_updated_at();

create trigger private_dtp_artifacts_updated_at
before update on private_dtp_artifacts
for each row execute function private_dtp_set_updated_at();

create trigger private_dtp_redaction_reviews_updated_at
before update on private_dtp_redaction_reviews
for each row execute function private_dtp_set_updated_at();

create trigger private_dtp_proof_candidates_updated_at
before update on private_dtp_proof_candidates
for each row execute function private_dtp_set_updated_at();

create trigger private_dtp_decisions_updated_at
before update on private_dtp_decisions
for each row execute function private_dtp_set_updated_at();

create trigger private_dtp_steward_items_updated_at
before update on private_dtp_steward_items
for each row execute function private_dtp_set_updated_at();

create trigger private_dtp_research_items_updated_at
before update on private_dtp_research_items
for each row execute function private_dtp_set_updated_at();

alter table private_dtp_engagements enable row level security;
alter table private_dtp_artifacts enable row level security;
alter table private_dtp_artifact_versions enable row level security;
alter table private_dtp_evidence_runs enable row level security;
alter table private_dtp_redaction_reviews enable row level security;
alter table private_dtp_proof_candidates enable row level security;
alter table private_dtp_decisions enable row level security;
alter table private_dtp_steward_items enable row level security;
alter table private_dtp_research_items enable row level security;
alter table private_dtp_import_export_receipts enable row level security;

grant usage on schema public to authenticated;

revoke all
on
  private_dtp_engagements,
  private_dtp_artifacts,
  private_dtp_artifact_versions,
  private_dtp_evidence_runs,
  private_dtp_redaction_reviews,
  private_dtp_proof_candidates,
  private_dtp_decisions,
  private_dtp_steward_items,
  private_dtp_research_items,
  private_dtp_import_export_receipts
from anon;

grant select, insert, update, delete
on
  private_dtp_engagements,
  private_dtp_artifacts,
  private_dtp_artifact_versions,
  private_dtp_evidence_runs,
  private_dtp_redaction_reviews,
  private_dtp_proof_candidates,
  private_dtp_decisions,
  private_dtp_steward_items,
  private_dtp_research_items,
  private_dtp_import_export_receipts
to authenticated;

create policy "operator manages own engagements"
on private_dtp_engagements for all
using (auth.uid() is not null and operator_id = auth.uid())
with check (auth.uid() is not null and operator_id = auth.uid());

create policy "operator manages own artifacts"
on private_dtp_artifacts for all
using (auth.uid() is not null and operator_id = auth.uid())
with check (auth.uid() is not null and operator_id = auth.uid());

create policy "operator manages own artifact versions"
on private_dtp_artifact_versions for all
using (auth.uid() is not null and operator_id = auth.uid())
with check (auth.uid() is not null and operator_id = auth.uid());

create policy "operator manages own evidence runs"
on private_dtp_evidence_runs for all
using (auth.uid() is not null and operator_id = auth.uid())
with check (auth.uid() is not null and operator_id = auth.uid());

create policy "operator manages own redaction reviews"
on private_dtp_redaction_reviews for all
using (auth.uid() is not null and operator_id = auth.uid())
with check (auth.uid() is not null and operator_id = auth.uid());

create policy "operator manages own proof candidates"
on private_dtp_proof_candidates for all
using (auth.uid() is not null and operator_id = auth.uid())
with check (auth.uid() is not null and operator_id = auth.uid());

create policy "operator manages own decisions"
on private_dtp_decisions for all
using (auth.uid() is not null and operator_id = auth.uid())
with check (auth.uid() is not null and operator_id = auth.uid());

create policy "operator manages own steward items"
on private_dtp_steward_items for all
using (auth.uid() is not null and operator_id = auth.uid())
with check (auth.uid() is not null and operator_id = auth.uid());

create policy "operator manages own research items"
on private_dtp_research_items for all
using (auth.uid() is not null and operator_id = auth.uid())
with check (auth.uid() is not null and operator_id = auth.uid());

create policy "operator manages own import export receipts"
on private_dtp_import_export_receipts for all
using (auth.uid() is not null and operator_id = auth.uid())
with check (auth.uid() is not null and operator_id = auth.uid());
