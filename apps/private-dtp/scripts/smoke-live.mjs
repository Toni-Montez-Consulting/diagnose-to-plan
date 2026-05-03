import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { createClient } from "@supabase/supabase-js";

const loadedEnvKeys = new Set();

loadEnvFile(".env");
loadEnvFile(".env.local", { overrideFileValues: true });

const required = [
  "VITE_SUPABASE_URL",
  "VITE_SUPABASE_ANON_KEY",
  "PRIVATE_DTP_OPERATOR_EMAIL",
  "PRIVATE_DTP_OPERATOR_PASSWORD",
  "PRIVATE_DTP_SECOND_OPERATOR_EMAIL",
  "PRIVATE_DTP_SECOND_OPERATOR_PASSWORD",
];

const missing = required.filter((key) => !process.env[key]);
if (missing.length > 0) {
  fail(`Missing required env vars: ${missing.join(", ")}`);
}

const url = process.env.VITE_SUPABASE_URL;
const anonKey = process.env.VITE_SUPABASE_ANON_KEY;
const stamp = new Date().toISOString().replace(/[:.]/g, "-");

const operator = createBrowserLikeClient();
const secondOperator = createBrowserLikeClient();

const created = [];

try {
  const operatorUser = await signIn(
    operator,
    process.env.PRIVATE_DTP_OPERATOR_EMAIL,
    process.env.PRIVATE_DTP_OPERATOR_PASSWORD,
    "operator",
  );
  await signIn(
    secondOperator,
    process.env.PRIVATE_DTP_SECOND_OPERATOR_EMAIL,
    process.env.PRIVATE_DTP_SECOND_OPERATOR_PASSWORD,
    "second operator",
  );

  const engagement = await insert("private_dtp_engagements", {
    title: `Hosted DTP smoke ${stamp}`,
    client_or_project_alias: `hosted-dtp-smoke-${stamp}`,
    kind: "internal",
    stage: "intake",
    sensitivity: "internal_only",
    owner: "Toni",
    source_repo: "diagnose-to-plan",
    local_pointer: "apps/private-dtp/scripts/smoke-live.mjs",
  });

  const artifact = await insert("private_dtp_artifacts", {
    engagement_id: engagement.id,
    artifact_type: "kit_doc",
    title: `Smoke artifact ${stamp}`,
    source_kind: "repo_file",
    source_pointer: "practice-os/steward/2026-05-03-business-brain-weekly-reset.md",
    summary: "Hosted DTP live smoke artifact pointer.",
    data_class: "P0",
    permission_level: "internal_only",
    redaction_status: "not_reviewed",
    proof_eligibility: "not_candidate",
  });

  await insert("private_dtp_artifact_versions", {
    artifact_id: artifact.id,
    version_label: "smoke-v1",
    source_pointer: artifact.source_pointer,
    summary: "Smoke version record.",
  });

  const evidenceRun = await insert("private_dtp_evidence_runs", {
    engagement_id: engagement.id,
    repo: "diagnose-to-plan",
    branch: "v2/harness",
    lane: "local",
    result: "pass",
    commands: ["npm run smoke:live"],
    hard_gate_status: "pass",
    advisory_gate_status: "not_checked",
    manual_gate_status: "manual_pending",
    artifact_path: "apps/private-dtp/scripts/smoke-live.mjs",
    redaction_status: "not_reviewed",
    reviewer: "Toni",
    notes: "Hosted DTP live smoke record.",
  });

  await insert("private_dtp_redaction_reviews", {
    engagement_id: engagement.id,
    target_type: "artifact",
    target_id: artifact.id,
    reviewer: "Toni",
    status: "not_started",
    permission_level: "internal_only",
    notes: "Smoke redaction queue item.",
  });

  const proofCandidate = await insert("private_dtp_proof_candidates", {
    engagement_id: engagement.id,
    artifact_id: artifact.id,
    public_claim: "Hosted DTP can record a proof candidate without approving it.",
    caveat: "Smoke record only; not public proof.",
    evidence_source: artifact.source_pointer,
    permission_status: "not_requested",
    redaction_status: "not_reviewed",
    reviewer: "Toni",
    status: "parked",
  });

  const decision = await insert("private_dtp_decisions", {
    engagement_id: engagement.id,
    title: `Smoke decision ${stamp}`,
    status: "accepted",
    context: "Hosted DTP live smoke.",
    options_considered: "Do nothing; verify core record writes.",
    chosen_path: "Verify core record writes with RLS.",
    consequences: "If this passes, the app can use the private tables through Auth/RLS.",
    related_artifact_id: artifact.id,
    related_evidence_run_id: evidenceRun.id,
  });

  await insert("private_dtp_steward_items", {
    title: `Smoke steward item ${stamp}`,
    item_type: "follow_up",
    source_pointer: "apps/private-dtp/scripts/smoke-live.mjs",
    destination_pointer: "practice-os/steward/",
    status: "open",
    sensitivity: "internal_only",
    human_approval: "operator smoke",
    notes: "Smoke steward queue item.",
  });

  await insert("private_dtp_research_items", {
    title: `Smoke research item ${stamp}`,
    source_pointer: "apps/private-dtp/README.md",
    classification: "watch",
    decision_reason: "Smoke research queue item.",
    linked_roadmap_item: "Hosted DTP Phase 0.1",
    status: "open",
  });

  const exportMarkdown = buildExportMarkdown({
    engagement,
    artifacts: [artifact],
    evidenceRuns: [evidenceRun],
    decisions: [decision],
    proofCandidates: [proofCandidate],
  });
  if (!exportMarkdown.includes(`# ${engagement.title}`)) {
    throw new Error("Generated export markdown did not include the smoke engagement title");
  }
  if (exportMarkdown.includes(process.env.PRIVATE_DTP_OPERATOR_PASSWORD)) {
    throw new Error("Generated export markdown leaked the operator password");
  }

  await insert("private_dtp_import_export_receipts", {
    direction: "export",
    source_pointer: `private_dtp_engagements:${engagement.id}`,
    destination_pointer: `hosted-dtp-smoke-${stamp}.md`,
    result: "pass",
    record_counts: {
      engagements: 1,
      artifacts: 1,
      artifact_versions: 1,
      evidence_runs: 1,
      redaction_reviews: 1,
      proof_candidates: 1,
      decisions: 1,
      steward_items: 1,
      research_items: 1,
    },
    notes: "Smoke export receipt.",
  });

  for (const item of created) {
    await assertVisible(operator, item.table, item.id, true);
    await assertVisible(secondOperator, item.table, item.id, false);
  }
  await assertForeignRowBlocked(secondOperator, engagement.id);

  console.log(JSON.stringify({
    ok: true,
    operator_id: operatorUser.id,
    engagement_id: engagement.id,
    created_tables: [...new Set(created.map((item) => item.table))],
    export_markdown_characters: exportMarkdown.length,
    rls_second_operator_blocked: true,
    second_operator_foreign_insert_blocked: true,
  }, null, 2));
} catch (error) {
  fail(error.message || String(error));
}

function createBrowserLikeClient() {
  return createClient(url, anonKey, {
    auth: {
      autoRefreshToken: false,
      persistSession: false,
      detectSessionInUrl: false,
    },
  });
}

async function signIn(client, email, password, label) {
  const { data, error } = await client.auth.signInWithPassword({ email, password });
  if (error) throw new Error(`Failed to sign in ${label}: ${error.message}`);
  if (!data.user) throw new Error(`Failed to sign in ${label}: no user returned`);
  return data.user;
}

async function insert(table, values) {
  const { data, error } = await operator.from(table).insert(values).select("*").single();
  if (error) throw new Error(`Insert failed for ${table}: ${error.message}`);
  created.push({ table, id: data.id });
  return data;
}

async function assertVisible(client, table, id, expectedVisible) {
  const { data, error } = await client.from(table).select("id").eq("id", id);
  if (error) throw new Error(`RLS visibility check failed for ${table}: ${error.message}`);
  const visible = (data ?? []).length > 0;
  if (visible !== expectedVisible) {
    throw new Error(
      `Unexpected RLS visibility for ${table}:${id}; expected ${expectedVisible}, got ${visible}`,
    );
  }
}

async function assertForeignRowBlocked(client, engagementId) {
  const { data, error } = await client
    .from("private_dtp_artifacts")
    .insert({
      engagement_id: engagementId,
      artifact_type: "kit_doc",
      title: "Forbidden cross-operator artifact",
      source_kind: "repo_file",
      source_pointer: "apps/private-dtp/scripts/smoke-live.mjs",
      summary: "This insert should be blocked by composite ownership constraints.",
      data_class: "P0",
      permission_level: "internal_only",
      redaction_status: "not_reviewed",
      proof_eligibility: "not_candidate",
    })
    .select("id");

  if (!error && (data ?? []).length > 0) {
    throw new Error("Second operator could create an artifact linked to another operator engagement");
  }
}

function buildExportMarkdown(input) {
  const { engagement, artifacts, evidenceRuns, decisions, proofCandidates } = input;
  return [
    "---",
    "data_class: P0",
    "confidential: false",
    "permission_level: internal_only",
    "review_status: exported",
    "---",
    "",
    `# ${engagement.title}`,
    "",
    "## Engagement",
    "",
    `- Alias: ${engagement.client_or_project_alias}`,
    `- Stage: ${engagement.stage}`,
    `- Sensitivity: ${engagement.sensitivity}`,
    `- Source repo: ${engagement.source_repo}`,
    "",
    renderList("Artifacts", artifacts, ["title", "artifact_type", "redaction_status", "proof_eligibility"]),
    renderList("Evidence Runs", evidenceRuns, ["repo", "lane", "result", "artifact_path"]),
    renderList("Decisions", decisions, ["title", "status", "chosen_path"]),
    renderList(
      "Proof Candidates",
      proofCandidates,
      ["status", "permission_status", "redaction_status", "public_claim"],
    ),
    "",
    "## Export Boundary",
    "",
    "- Raw private logs, tokens, payment/member records, unreviewed screenshots, and unapproved public claims are excluded.",
  ].join("\n");
}

function renderList(title, records, keys) {
  const lines = [`## ${title}`, ""];
  for (const record of records) {
    const label = String(record.title ?? record.public_claim ?? record.repo ?? record.id ?? "Record");
    lines.push(`- ${label}`);
    for (const key of keys) {
      if (key === "title") continue;
      const value = record[key];
      if (value) lines.push(`  - ${key}: ${String(value).replace(/\n/g, " ")}`);
    }
  }
  return lines.join("\n");
}

function loadEnvFile(filename, options = {}) {
  const path = resolve(process.cwd(), filename);
  try {
    const content = readFileSync(path, "utf8");
    for (const line of content.split(/\r?\n/)) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith("#")) continue;
      const separator = trimmed.indexOf("=");
      if (separator === -1) continue;
      const key = trimmed.slice(0, separator).trim();
      const value = trimmed.slice(separator + 1).trim().replace(/^['"]|['"]$/g, "");
      if (
        key &&
        (process.env[key] === undefined ||
          (options.overrideFileValues && loadedEnvKeys.has(key)))
      ) {
        process.env[key] = value;
        loadedEnvKeys.add(key);
      }
    }
  } catch (error) {
    if (error.code !== "ENOENT") throw error;
  }
}

function fail(message) {
  console.error(`Hosted DTP live smoke failed: ${message}`);
  process.exit(1);
}
