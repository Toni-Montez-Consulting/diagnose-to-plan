import type { DtpRecord, ImportMarkdownResult } from "./types";

export function parseMarkdownWithFrontmatter(markdown: string): ImportMarkdownResult {
  const normalized = markdown.replace(/\r\n/g, "\n").trim();
  const match = normalized.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  const frontmatter: Record<string, string> = {};
  let body = normalized;

  if (match) {
    for (const line of match[1].split("\n")) {
      const separator = line.indexOf(":");
      if (separator === -1) continue;
      const key = line.slice(0, separator).trim();
      const value = line.slice(separator + 1).trim().replace(/^['"]|['"]$/g, "");
      if (key) frontmatter[key] = value;
    }
    body = match[2].trim();
  }

  const heading = body.match(/^#\s+(.+)$/m)?.[1]?.trim();
  const title = heading || frontmatter.title || frontmatter.engagement_id || "Imported Markdown";

  return { frontmatter, body, title };
}

export function engagementFromMarkdown(
  parsed: ImportMarkdownResult,
  sourcePointer: string,
): DtpRecord {
  const alias =
    parsed.frontmatter.client_id ||
    parsed.frontmatter.client ||
    parsed.frontmatter.project ||
    "imported";

  return {
    title: parsed.title,
    client_or_project_alias: alias,
    kind: normalizeOption(parsed.frontmatter.kind, "client"),
    stage: normalizeOption(parsed.frontmatter.stage, "intake"),
    sensitivity: sensitivityFromFrontmatter(parsed.frontmatter),
    owner: parsed.frontmatter.owner,
    source_repo: parsed.frontmatter.source_repo || "diagnose-to-plan",
    local_pointer: sourcePointer,
  };
}

export function artifactFromMarkdown(
  parsed: ImportMarkdownResult,
  sourcePointer: string,
  engagementId: string,
): DtpRecord {
  return {
    engagement_id: engagementId,
    artifact_type: normalizeOption(parsed.frontmatter.artifact_type, "kit_doc"),
    title: parsed.title,
    source_kind: "local_markdown",
    source_pointer: sourcePointer,
    summary: summarizeMarkdown(parsed.body),
    data_class: parsed.frontmatter.data_class || "P1",
    permission_level: parsed.frontmatter.permission_level || "internal_only",
    redaction_status: redactionFromFrontmatter(parsed.frontmatter),
    proof_eligibility: parsed.frontmatter.proof_eligibility || "not_candidate",
  };
}

export function exportEngagementSummaryMarkdown(input: {
  engagement: DtpRecord;
  artifacts: DtpRecord[];
  evidenceRuns: DtpRecord[];
  decisions: DtpRecord[];
  proofCandidates: DtpRecord[];
}): string {
  const { engagement, artifacts, evidenceRuns, decisions, proofCandidates } = input;
  const title = String(engagement.title ?? "Hosted DTP Export");
  const alias = String(engagement.client_or_project_alias ?? "unknown");
  const sensitivity = String(engagement.sensitivity ?? "internal_only");

  return [
    "---",
    "data_class: P0",
    "confidential: false",
    `permission_level: ${String(engagement.permission_level ?? "internal_only")}`,
    "review_status: exported",
    "---",
    "",
    `# ${title}`,
    "",
    "## Engagement",
    "",
    `- Alias: ${alias}`,
    `- Stage: ${String(engagement.stage ?? "unknown")}`,
    `- Sensitivity: ${sensitivity}`,
    `- Source repo: ${String(engagement.source_repo ?? "not_recorded")}`,
    "",
    renderList("Artifacts", artifacts, ["title", "artifact_type", "redaction_status", "proof_eligibility"]),
    renderList("Evidence Runs", evidenceRuns, ["repo", "lane", "result", "artifact_path"]),
    renderList("Decisions", decisions, ["title", "status", "chosen_path"]),
    renderList("Proof Candidates", proofCandidates, ["status", "permission_status", "redaction_status", "public_claim"]),
    "",
    "## Export Boundary",
    "",
    "- Raw private logs, secrets, payment/member records, unreviewed screenshots, and unapproved public claims are excluded.",
  ].join("\n");
}

export function validateProofApproval(values: DtpRecord): string | null {
  if (values.status !== "approved") return null;

  const missing = [
    "public_claim",
    "evidence_source",
    "caveat",
    "reviewer",
  ].filter((key) => !String(values[key] ?? "").trim());

  const permission = String(values.permission_status ?? "");
  const redaction = String(values.redaction_status ?? "");
  if (!["owner_approved", "client_approved", "public_safe"].includes(permission)) {
    missing.push("publishable permission");
  }
  if (!["approved_public", "public_safe"].includes(redaction)) {
    missing.push("public redaction");
  }

  return missing.length > 0
    ? `Approved proof needs: ${missing.join(", ")}.`
    : null;
}

function summarizeMarkdown(body: string): string {
  return body
    .replace(/^#+\s+/gm, "")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 280);
}

function sensitivityFromFrontmatter(frontmatter: Record<string, string>): string {
  if (frontmatter.sensitivity) return frontmatter.sensitivity;
  if (frontmatter.confidential === "true") return "client_confidential";
  return "internal_only";
}

function redactionFromFrontmatter(frontmatter: Record<string, string>): string {
  if (frontmatter.redaction_status) return frontmatter.redaction_status;
  if (frontmatter.review_status === "reviewed") return "redacted";
  return "not_reviewed";
}

function normalizeOption(value: string | undefined, fallback: string): string {
  return value && value.trim() ? value.trim() : fallback;
}

function renderList(title: string, records: DtpRecord[], keys: string[]): string {
  if (records.length === 0) {
    return [`## ${title}`, "", "- None recorded."].join("\n");
  }

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
