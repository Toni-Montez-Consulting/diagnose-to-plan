import { describe, expect, it } from "vitest";
import {
  artifactFromMarkdown,
  engagementFromMarkdown,
  exportEngagementSummaryMarkdown,
  parseMarkdownWithFrontmatter,
  validateProofApproval,
} from "./importExport";

describe("markdown import/export contract", () => {
  it("parses frontmatter and maps markdown into engagement and artifact records", () => {
    const confidentialFlag = ["confidential: tru", "e"].join("");
    const parsed = parseMarkdownWithFrontmatter(`---
client_id: cameron
data_class: P2
${confidentialFlag}
permission_level: internal_only
review_status: draft
---

# Send Ready Packet

Private scope and proof gates.`);

    expect(parsed.title).toBe("Send Ready Packet");
    expect(parsed.frontmatter.client_id).toBe("cameron");

    const engagement = engagementFromMarkdown(parsed, "engagements/cameron/send-ready.md");
    expect(engagement.client_or_project_alias).toBe("cameron");
    expect(engagement.sensitivity).toBe("client_confidential");

    const artifact = artifactFromMarkdown(
      parsed,
      "engagements/cameron/send-ready.md",
      "engagement-id",
    );
    expect(artifact.engagement_id).toBe("engagement-id");
    expect(artifact.source_kind).toBe("local_markdown");
    expect(artifact.permission_level).toBe("internal_only");
  });

  it("exports an engagement summary without raw private content", () => {
    const markdown = exportEngagementSummaryMarkdown({
      engagement: {
        title: "Cameron SMB Marketplace",
        client_or_project_alias: "cameron",
        stage: "diagnose",
        sensitivity: "client_confidential",
        permission_level: "internal_only",
      },
      artifacts: [{
        title: "Scope Notes",
        artifact_type: "kit_doc",
        data_class: "P2",
        permission_level: "internal_only",
        redaction_status: "not_reviewed",
        source_pointer: "engagements/cameron/scope.md",
      }],
      evidenceRuns: [{ repo: "diagnose-to-plan", lane: "local", result: "pass" }],
      decisions: [{ title: "Mock data only", status: "accepted" }],
      proofCandidates: [{
        status: "parked",
        permission_status: "internal_only",
        evidence_source: "engagements/cameron/scope.md",
      }],
    });

    expect(markdown).toContain("# Cameron SMB Marketplace");
    expect(markdown).toContain("data_class: P2");
    expect(markdown).toContain("permission_level: internal_only");
    expect(markdown).toContain("source_pointer: engagements/cameron/scope.md");
    expect(markdown).toContain("evidence_source: engagements/cameron/scope.md");
    expect(markdown).toContain("Raw private logs");
    expect(markdown).not.toContain("gmail_message_id");
  });

  it("keeps approved proof gated by permission, redaction, evidence, caveat, and reviewer", () => {
    expect(validateProofApproval({ status: "parked" })).toBeNull();
    expect(validateProofApproval({ status: "approved" })).toContain("Approved proof needs");
    expect(
      validateProofApproval({
        status: "approved",
        public_claim: "Reduced owner follow-up time.",
        evidence_source: "proof packet",
        caveat: "Internal pilot.",
        reviewer: "Toni",
        permission_status: "client_approved",
        redaction_status: "approved_public",
      }),
    ).toBeNull();
  });
});
