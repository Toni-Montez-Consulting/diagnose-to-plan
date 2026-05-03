import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { execFileSync } from "node:child_process";
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
const repoRoot = resolve(process.cwd(), "..", "..");
const sourcePointer = "practice-os/steward/2026-05-03-business-brain-weekly-reset.md";
const sourcePath = resolve(repoRoot, sourcePointer);
const exportPointer = "practice-os/steward/2026-05-03-hosted-dtp-live-roundtrip-export.md";
const exportPath = resolve(repoRoot, exportPointer);
const sourceMarkdown = readFileSync(sourcePath, "utf8");
const sourceFrontmatter = parseFrontmatter(sourceMarkdown);
const branch = git(["rev-parse", "--abbrev-ref", "HEAD"]);
const commitSha = git(["rev-parse", "--short", "HEAD"]);

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
    title: "Hosted DTP Business Brain Round Trip",
    client_or_project_alias: "hosted-dtp-business-brain-roundtrip",
    kind: "internal",
    stage: "proof_review",
    sensitivity: "internal_only",
    owner: "Toni",
    source_repo: "diagnose-to-plan",
    local_pointer: sourcePointer,
  });

  const artifact = await insert("private_dtp_artifacts", {
    engagement_id: engagement.id,
    artifact_type: "kit_doc",
    title: "Business Brain Weekly Operating Packet",
    source_kind: "repo_file",
    source_pointer: sourcePointer,
    summary:
      "Sanitized live import of the Business Brain weekly packet metadata, lane map, gates, and next actions.",
    data_class: sourceFrontmatter.data_class || "P0",
    permission_level: sourceFrontmatter.permission_level || "internal_only",
    redaction_status: "restricted",
    proof_eligibility: "not_candidate",
  });

  await insert("private_dtp_artifact_versions", {
    artifact_id: artifact.id,
    version_label: "phase-0.2-roundtrip",
    source_pointer: sourcePointer,
    summary: "Live Hosted DTP import/export round-trip source pointer.",
  });

  const evidenceRun = await insert("private_dtp_evidence_runs", {
    engagement_id: engagement.id,
    repo: "diagnose-to-plan",
    branch,
    commit_sha: commitSha,
    lane: "local",
    result: "pass",
    commands: ["npm run roundtrip:live"],
    hard_gate_status: "pass",
    advisory_gate_status: "not_checked",
    manual_gate_status: "manual_pending",
    artifact_path: exportPointer,
    redaction_status: "restricted",
    reviewer: "Toni",
    notes: "Hosted DTP live import/export round trip from a sanitized DTP artifact.",
  });

  await insert("private_dtp_redaction_reviews", {
    engagement_id: engagement.id,
    target_type: "artifact",
    target_id: artifact.id,
    reviewer: "Toni",
    status: "not_started",
    permission_level: "internal_only",
    notes: "Round-trip artifact remains internal and restricted; not public proof.",
  });

  const proofCandidate = await insert("private_dtp_proof_candidates", {
    engagement_id: engagement.id,
    artifact_id: artifact.id,
    public_claim: "Hosted DTP can import and export a Business Brain operating artifact.",
    caveat: "Internal infrastructure proof only; not public proof.",
    evidence_source: exportPointer,
    permission_status: "not_requested",
    redaction_status: "not_reviewed",
    reviewer: "Toni",
    status: "parked",
  });

  const decision = await insert("private_dtp_decisions", {
    engagement_id: engagement.id,
    title: "Keep Hosted DTP record-first after live round trip",
    status: "accepted",
    context:
      "A sanitized Business Brain operating packet was imported into Hosted DTP and exported back to markdown.",
    options_considered:
      "Skip round trip; store only in Supabase; preserve markdown fallback while testing live records.",
    chosen_path:
      "Preserve markdown fallback and use Hosted DTP as a private record surface, not the only copy.",
    consequences:
      "Hosted DTP can join operating loops while DTP steward artifacts remain auditable.",
    related_artifact_id: artifact.id,
    related_evidence_run_id: evidenceRun.id,
  });

  await insert("private_dtp_steward_items", {
    title: "Promote Hosted DTP round trip into the Memory Spine",
    item_type: "memory_candidate",
    source_pointer: sourcePointer,
    destination_pointer: exportPointer,
    status: "open",
    sensitivity: "internal_only",
    human_approval: "pending Toni correction",
    notes:
      "Use this round trip as the first private app participation in the DTP Memory Spine.",
  });

  await insert("private_dtp_research_items", {
    title: "FAOS stays readiness-only after Hosted DTP round trip",
    source_pointer: "practice-os/steward/2026-05-03-faos-phase-0a-readiness-review.md",
    classification: "watch",
    decision_reason:
      "Hosted DTP has a live data plane, but orchestration still needs more real operating cycles.",
    linked_roadmap_item: "FAOS Phase 0A readiness",
    status: "parked",
  });

  await insert("private_dtp_import_export_receipts", {
    direction: "import",
    source_pointer: sourcePointer,
    destination_pointer: `private_dtp_engagements:${engagement.id}`,
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
    notes: "Imported a sanitized DTP Business Brain artifact into live Hosted DTP records.",
  });

  const exportMarkdown = buildRoundTripExportMarkdown({
    engagement,
    artifact,
    evidenceRun,
    proofCandidate,
    decision,
    sourceFrontmatter,
  });

  assertExportSafe(exportMarkdown);
  mkdirSync(dirname(exportPath), { recursive: true });
  writeFileSync(exportPath, exportMarkdown, "utf8");

  await insert("private_dtp_import_export_receipts", {
    direction: "export",
    source_pointer: `private_dtp_engagements:${engagement.id}`,
    destination_pointer: exportPointer,
    result: "pass",
    record_counts: {
      engagements: 1,
      artifacts: 1,
      evidence_runs: 1,
      proof_candidates: 1,
      decisions: 1,
    },
    notes: "Exported live Hosted DTP round-trip summary back to tracked DTP markdown.",
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
    source_pointer: sourcePointer,
    export_pointer: exportPointer,
    created_tables: [...new Set(created.map((item) => item.table))],
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
      title: "Forbidden cross-operator round-trip artifact",
      source_kind: "repo_file",
      source_pointer: sourcePointer,
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

function buildRoundTripExportMarkdown(input) {
  const { engagement, artifact, evidenceRun, proofCandidate, decision, sourceFrontmatter } = input;
  return [
    "---",
    `data_class: ${sourceFrontmatter.data_class || "P0"}`,
    "confidential: false",
    `permission_level: ${sourceFrontmatter.permission_level || "internal_only"}`,
    "review_status: exported",
    "redaction_status: restricted",
    "proof_eligibility: not_candidate",
    "---",
    "",
    "# Hosted DTP Live Round Trip Export",
    "",
    "## Source",
    "",
    `- Source pointer: ${sourcePointer}`,
    `- Source data class: ${sourceFrontmatter.data_class || "P0"}`,
    `- Source permission: ${sourceFrontmatter.permission_level || "internal_only"}`,
    "- Source body copied: no",
    "",
    "## Hosted Records",
    "",
    `- Engagement: ${engagement.id}`,
    `- Artifact: ${artifact.id}`,
    `- Evidence run: ${evidenceRun.id}`,
    `- Decision: ${decision.id}`,
    `- Proof candidate: ${proofCandidate.id}`,
    "",
    "## Preserved Gates",
    "",
    `- Artifact data class: ${artifact.data_class}`,
    `- Artifact permission: ${artifact.permission_level}`,
    `- Artifact redaction: ${artifact.redaction_status}`,
    `- Artifact proof eligibility: ${artifact.proof_eligibility}`,
    `- Proof status: ${proofCandidate.status}`,
    `- Proof permission: ${proofCandidate.permission_status}`,
    `- Proof redaction: ${proofCandidate.redaction_status}`,
    "",
    "## Decision",
    "",
    `- ${decision.title}`,
    `- Chosen path: ${decision.chosen_path}`,
    "",
    "## Correction Checklist",
    "",
    "- Confirm this should count as the first Hosted DTP Memory Spine round trip.",
    "- Confirm smoke fixtures can remain in the dedicated DTP Supabase project.",
    "- Confirm non-smoke client records should still wait for lane-specific export fallback.",
    "",
    "## Export Boundary",
    "",
    "- This export contains record pointers and sanitized summaries only.",
    "- Raw private notes, emails, credentials, payment/member records, screenshots, and public proof copy are excluded.",
  ].join("\n");
}

function assertExportSafe(markdown) {
  const forbidden = [
    process.env.PRIVATE_DTP_OPERATOR_PASSWORD,
    process.env.PRIVATE_DTP_SECOND_OPERATOR_PASSWORD,
    "gmail_message_id",
    "PRIVATE_DTP_OPERATOR_PASSWORD",
    "PRIVATE_DTP_SECOND_OPERATOR_PASSWORD",
  ].filter(Boolean);
  for (const value of forbidden) {
    if (markdown.includes(value)) {
      throw new Error("Generated export leaked a forbidden value");
    }
  }
  if (!markdown.includes("Source body copied: no")) {
    throw new Error("Generated export did not record the source-body exclusion");
  }
}

function parseFrontmatter(markdown) {
  const normalized = markdown.replace(/\r\n/g, "\n").trim();
  const match = normalized.match(/^---\n([\s\S]*?)\n---/);
  const frontmatter = {};
  if (!match) return frontmatter;
  for (const line of match[1].split("\n")) {
    const separator = line.indexOf(":");
    if (separator === -1) continue;
    const key = line.slice(0, separator).trim();
    const value = line.slice(separator + 1).trim().replace(/^['"]|['"]$/g, "");
    if (key) frontmatter[key] = value;
  }
  return frontmatter;
}

function git(args) {
  return execFileSync("git", args, { cwd: repoRoot, encoding: "utf8" }).trim();
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
  console.error(`Hosted DTP live round trip failed: ${message}`);
  process.exit(1);
}
