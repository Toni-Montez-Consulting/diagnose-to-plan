export type TableName =
  | "private_dtp_engagements"
  | "private_dtp_artifacts"
  | "private_dtp_artifact_versions"
  | "private_dtp_evidence_runs"
  | "private_dtp_redaction_reviews"
  | "private_dtp_proof_candidates"
  | "private_dtp_decisions"
  | "private_dtp_steward_items"
  | "private_dtp_research_items"
  | "private_dtp_import_export_receipts";

export type FieldKind = "text" | "textarea" | "select" | "array";

export type DtpRecord = {
  id?: string;
  title?: string;
  created_at?: string;
  updated_at?: string;
  [key: string]: unknown;
};

export type FieldConfig = {
  key: string;
  label: string;
  kind: FieldKind;
  required?: boolean;
  options?: readonly string[];
  placeholder?: string;
};

export type EntityConfig = {
  id: string;
  title: string;
  shortTitle: string;
  table: TableName;
  description: string;
  fields: readonly FieldConfig[];
  display: readonly string[];
  sortBy?: string;
  queueStatusField?: string;
  queueStatuses?: readonly string[];
};

export type ImportMarkdownResult = {
  frontmatter: Record<string, string>;
  body: string;
  title: string;
};
