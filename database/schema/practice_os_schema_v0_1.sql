create table clients (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  business_type text,
  revenue_model text,
  notes text,
  risk_level text,
  status text,
  created_at timestamptz default now()
);

create table engagements (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  offer_type text,
  stage text,
  start_date date,
  end_date date,
  budget numeric,
  status text,
  created_at timestamptz default now()
);

create table raw_inputs (
  id uuid primary key default gen_random_uuid(),
  source_type text,
  raw_text text not null,
  related_client_id uuid references clients(id),
  related_project_id uuid,
  tags text[],
  created_at timestamptz default now()
);

create table intent_briefs (
  id uuid primary key default gen_random_uuid(),
  raw_input_id uuid references raw_inputs(id),
  artifact_type text,
  core_intent text,
  audience text,
  business_goal text,
  emotional_tone text,
  must_include jsonb,
  must_avoid jsonb,
  phrases_to_preserve jsonb,
  assumptions jsonb,
  open_questions jsonb,
  created_at timestamptz default now()
);

create table clarifying_questions (
  id uuid primary key default gen_random_uuid(),
  related_input_id uuid references raw_inputs(id),
  related_client_id uuid references clients(id),
  related_project_id uuid,
  question_text text not null,
  question_type text,
  importance text,
  blocking boolean default false,
  default_assumption text,
  why_it_matters text,
  answer text,
  status text default 'open',
  created_at timestamptz default now(),
  answered_at timestamptz
);

create table assumptions (
  id uuid primary key default gen_random_uuid(),
  related_input_id uuid references raw_inputs(id),
  related_project_id uuid,
  assumption_text text,
  source text,
  confidence text,
  needs_review boolean default true,
  confirmed boolean default false,
  created_at timestamptz default now()
);

create table workflows (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  name text not null,
  trigger text,
  current_state text,
  desired_state text,
  frequency numeric,
  time_cost numeric,
  business_impact text,
  owner_bottleneck_score int,
  status text,
  created_at timestamptz default now()
);

create table opportunities (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  workflow_id uuid references workflows(id),
  title text,
  description text,
  frequency_score int,
  owner_bottleneck_score int,
  revenue_proximity_score int,
  pain_score int,
  data_readiness_score int,
  adoption_score int,
  reusability_score int,
  complexity_score int,
  risk_score int,
  priority_score int,
  recommended_phase text,
  created_at timestamptz default now()
);

create table implementation_specs (
  id uuid primary key default gen_random_uuid(),
  opportunity_id uuid references opportunities(id),
  project_name text,
  business_goal text,
  problem_statement text,
  non_goals jsonb,
  users jsonb,
  inputs jsonb,
  outputs jsonb,
  systems_of_record jsonb,
  acceptance_criteria jsonb,
  risks jsonb,
  value_metrics jsonb,
  handoff_requirements jsonb,
  status text,
  created_at timestamptz default now()
);

create table build_tasks (
  id uuid primary key default gen_random_uuid(),
  spec_id uuid references implementation_specs(id),
  title text,
  description text,
  status text,
  priority text,
  acceptance_criteria jsonb,
  linked_exception_id uuid,
  created_at timestamptz default now()
);

create table exceptions (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  workflow_id uuid references workflows(id),
  severity text,
  expected_behavior text,
  observed_behavior text,
  detected_by text,
  root_cause text,
  fix text,
  status text,
  lesson_learned text,
  promote_to_memory boolean default false,
  created_at timestamptz default now()
);

create table value_metrics (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  engagement_id uuid references engagements(id),
  metric_name text,
  baseline_value numeric,
  current_value numeric,
  unit text,
  confidence text,
  notes text,
  created_at timestamptz default now()
);

create table memory_items (
  id uuid primary key default gen_random_uuid(),
  title text,
  content text,
  memory_level text,
  source text,
  approved boolean default false,
  tags text[],
  related_client_id uuid references clients(id),
  created_at timestamptz default now()
);

create table decision_logs (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  engagement_id uuid references engagements(id),
  decision text,
  options_considered jsonb,
  rationale text,
  tradeoffs text,
  decided_at timestamptz default now()
);

create table runbooks (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),
  engagement_id uuid references engagements(id),
  title text,
  content text,
  version text,
  last_updated_at timestamptz default now()
);
