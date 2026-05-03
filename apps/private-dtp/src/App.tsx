import {
  Archive,
  CheckCircle2,
  ClipboardCheck,
  FileInput,
  FileText,
  FolderKanban,
  GitBranch,
  KeyRound,
  LogOut,
  Plus,
  RefreshCcw,
  ShieldCheck,
  Sparkles,
} from "lucide-react";
import { FormEvent, useEffect, useMemo, useState } from "react";
import type { Session } from "@supabase/supabase-js";
import {
  artifactFromMarkdown,
  engagementFromMarkdown,
  exportEngagementSummaryMarkdown,
  parseMarkdownWithFrontmatter,
  validateProofApproval,
} from "./importExport";
import { PrivateDtpRepository } from "./repository";
import { entityConfigs } from "./schema";
import "./styles.css";
import { supabase, supabaseConfigured } from "./supabaseClient";
import type { DtpRecord, EntityConfig, FieldConfig, TableName } from "./types";

const iconMap = {
  engagements: FolderKanban,
  artifacts: Archive,
  evidence: ClipboardCheck,
  redaction: ShieldCheck,
  proof: CheckCircle2,
  decisions: GitBranch,
  steward: Sparkles,
  research: FileText,
};

export default function App() {
  const [session, setSession] = useState<Session | null>(null);
  const [activeId, setActiveId] = useState(entityConfigs[0].id);
  const repository = useMemo(() => (supabase ? new PrivateDtpRepository(supabase) : null), []);

  useEffect(() => {
    if (!supabase) return;
    supabase.auth.getSession().then(({ data }) => setSession(data.session ?? null));
    const subscription = supabase.auth.onAuthStateChange((_event, nextSession) => {
      setSession(nextSession);
    });
    return () => subscription.data.subscription.unsubscribe();
  }, []);

  if (!supabaseConfigured || !supabase) return <SetupState />;
  if (!session) return <LoginState />;

  const activeConfig = entityConfigs.find((config) => config.id === activeId) ?? entityConfigs[0];

  return (
    <main className="appShell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brandMark">DTP</div>
          <div>
            <strong>Private DTP</strong>
            <span>Phase 0.1</span>
          </div>
        </div>

        <nav className="navList" aria-label="Private DTP records">
          {entityConfigs.map((config) => {
            const Icon = iconMap[config.id as keyof typeof iconMap] ?? FileText;
            return (
              <button
                key={config.id}
                className={activeId === config.id ? "navButton active" : "navButton"}
                onClick={() => setActiveId(config.id)}
                title={config.title}
              >
                <Icon size={18} aria-hidden="true" />
                <span>{config.shortTitle}</span>
              </button>
            );
          })}
        </nav>

        <button className="ghostButton" onClick={() => supabase?.auth.signOut()} title="Sign out">
          <LogOut size={18} aria-hidden="true" />
          <span>Sign Out</span>
        </button>
      </aside>

      <section className="workspace">
        <Screen config={activeConfig} repository={repository} />
      </section>
    </main>
  );
}

function SetupState() {
  return (
    <main className="centered">
      <section className="authPanel">
        <KeyRound size={28} aria-hidden="true" />
        <h1>Private DTP Setup</h1>
        <p>Set `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY` in `apps/private-dtp/.env`.</p>
      </section>
    </main>
  );
}

function LoginState() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  async function submit(event: FormEvent) {
    event.preventDefault();
    setMessage("");
    const { error } = await supabase!.auth.signInWithPassword({ email, password });
    if (error) setMessage(error.message);
  }

  return (
    <main className="centered">
      <form className="authPanel" onSubmit={submit}>
        <KeyRound size={28} aria-hidden="true" />
        <h1>Private DTP</h1>
        <label>
          Email
          <input value={email} onChange={(event) => setEmail(event.target.value)} type="email" />
        </label>
        <label>
          Password
          <input
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            type="password"
          />
        </label>
        <button className="primaryButton" type="submit">
          <KeyRound size={18} aria-hidden="true" />
          <span>Sign In</span>
        </button>
        {message ? <p className="errorText">{message}</p> : null}
      </form>
    </main>
  );
}

function Screen({
  config,
  repository,
}: {
  config: EntityConfig;
  repository: PrivateDtpRepository | null;
}) {
  const [records, setRecords] = useState<DtpRecord[]>([]);
  const [engagements, setEngagements] = useState<DtpRecord[]>([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  async function load() {
    if (!repository) return;
    setLoading(true);
    setMessage("");
    try {
      const [nextRecords, nextEngagements] = await Promise.all([
        repository.list(config.table, config.sortBy),
        repository.list("private_dtp_engagements", "updated_at"),
      ]);
      setRecords(nextRecords);
      setEngagements(nextEngagements);
    } catch (error) {
      setMessage(error instanceof Error ? error.message : "Unable to load records.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [config.id]);

  const queueCount = queueSize(config, records);

  return (
    <div className="screen">
      <header className="screenHeader">
        <div>
          <p className="eyebrow">Private operating records</p>
          <h1>{config.title}</h1>
          <p>{config.description}</p>
        </div>
        <button className="iconButton" onClick={load} title="Refresh records">
          <RefreshCcw size={18} aria-hidden="true" />
        </button>
      </header>

      <section className="metricsRow" aria-label="Record counts">
        <Metric label="Records" value={records.length} />
        <Metric label="Queue" value={queueCount} />
        <Metric label="Engagements" value={engagements.length} />
      </section>

      <section className="workGrid">
        <RecordForm
          config={config}
          repository={repository}
          engagements={engagements}
          onSaved={load}
          onMessage={setMessage}
        />
        <ImportExportPanel repository={repository} engagements={engagements} onSaved={load} />
      </section>

      {message ? <p className="errorText">{message}</p> : null}
      {loading ? <p className="muted">Loading records...</p> : <RecordTable config={config} records={records} />}
    </div>
  );
}

function Metric({ label, value }: { label: string; value: number }) {
  return (
    <div className="metric">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function RecordForm({
  config,
  repository,
  engagements,
  onSaved,
  onMessage,
}: {
  config: EntityConfig;
  repository: PrivateDtpRepository | null;
  engagements: DtpRecord[];
  onSaved: () => void;
  onMessage: (message: string) => void;
}) {
  const [values, setValues] = useState<DtpRecord>(() => initialValues(config));

  useEffect(() => {
    setValues(initialValues(config));
  }, [config.id]);

  async function submit(event: FormEvent) {
    event.preventDefault();
    if (!repository) return;
    onMessage("");

    const nextValues = inflateArrayFields(config.fields, values);
    const validationMessage =
      config.table === "private_dtp_proof_candidates" ? validateProofApproval(nextValues) : null;
    if (validationMessage) {
      onMessage(validationMessage);
      return;
    }

    try {
      await repository.create(config.table, nextValues);
      setValues(initialValues(config));
      await onSaved();
    } catch (error) {
      onMessage(error instanceof Error ? error.message : "Unable to save record.");
    }
  }

  return (
    <form className="panel" onSubmit={submit}>
      <div className="panelTitle">
        <Plus size={18} aria-hidden="true" />
        <h2>New {config.shortTitle.slice(0, -1) || config.shortTitle}</h2>
      </div>

      <div className="formGrid">
        {config.fields.map((field) => (
          <Field
            key={field.key}
            field={field}
            value={String(values[field.key] ?? "")}
            engagements={engagements}
            onChange={(value) => setValues((current) => ({ ...current, [field.key]: value }))}
          />
        ))}
      </div>

      <button className="primaryButton" type="submit">
        <Plus size={18} aria-hidden="true" />
        <span>Add Record</span>
      </button>
    </form>
  );
}

function Field({
  field,
  value,
  engagements,
  onChange,
}: {
  field: FieldConfig;
  value: string;
  engagements: DtpRecord[];
  onChange: (value: string) => void;
}) {
  const className = field.kind === "textarea" || field.kind === "array" ? "wideField" : undefined;
  const engagementOptions = field.key === "engagement_id" ? engagements : [];

  return (
    <label className={className}>
      {field.label}
      {field.kind === "textarea" || field.kind === "array" ? (
        <textarea
          value={value}
          onChange={(event) => onChange(event.target.value)}
          required={field.required}
          placeholder={field.placeholder}
          rows={field.kind === "array" ? 3 : 4}
        />
      ) : field.kind === "select" ? (
        <select value={value} onChange={(event) => onChange(event.target.value)} required={field.required}>
          <option value="">Select</option>
          {field.options?.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      ) : engagementOptions.length > 0 ? (
        <input
          value={value}
          onChange={(event) => onChange(event.target.value)}
          required={field.required}
          list="engagements"
        />
      ) : (
        <input
          value={value}
          onChange={(event) => onChange(event.target.value)}
          required={field.required}
          placeholder={field.placeholder}
        />
      )}
      {engagementOptions.length > 0 ? (
        <datalist id="engagements">
          {engagementOptions.map((engagement) => (
            <option key={String(engagement.id)} value={String(engagement.id)}>
              {String(engagement.title ?? engagement.client_or_project_alias ?? engagement.id)}
            </option>
          ))}
        </datalist>
      ) : null}
    </label>
  );
}

function ImportExportPanel({
  repository,
  engagements,
  onSaved,
}: {
  repository: PrivateDtpRepository | null;
  engagements: DtpRecord[];
  onSaved: () => void;
}) {
  const [sourcePointer, setSourcePointer] = useState("");
  const [selectedEngagementId, setSelectedEngagementId] = useState("");
  const [markdown, setMarkdown] = useState("");
  const [exported, setExported] = useState("");
  const [message, setMessage] = useState("");

  async function importMarkdown() {
    if (!repository) return;
    setMessage("");
    try {
      const parsed = parseMarkdownWithFrontmatter(markdown);
      let engagementId = selectedEngagementId;

      if (!engagementId) {
        const engagement = await repository.create(
          "private_dtp_engagements",
          engagementFromMarkdown(parsed, sourcePointer || "manual-import.md"),
        );
        engagementId = String(engagement.id);
      }

      await repository.create(
        "private_dtp_artifacts",
        artifactFromMarkdown(parsed, sourcePointer || "manual-import.md", engagementId),
      );
      await repository.create("private_dtp_import_export_receipts", {
        direction: "import",
        source_pointer: sourcePointer || "manual-import.md",
        destination_pointer: engagementId,
        result: "pass",
        record_counts: { artifacts: 1, engagements: selectedEngagementId ? 0 : 1 },
        notes: "Imported from markdown fallback.",
      });
      setMarkdown("");
      setMessage("Imported markdown.");
      await onSaved();
    } catch (error) {
      setMessage(error instanceof Error ? error.message : "Import failed.");
    }
  }

  async function exportSummary() {
    if (!repository || !selectedEngagementId) return;
    setMessage("");
    try {
      const engagement = engagements.find((item) => item.id === selectedEngagementId);
      if (!engagement) throw new Error("Select a known engagement.");
      const [artifacts, evidenceRuns, decisions, proofCandidates] = await Promise.all([
        repository.listBy("private_dtp_artifacts", "engagement_id", selectedEngagementId, "updated_at"),
        repository.listBy("private_dtp_evidence_runs", "engagement_id", selectedEngagementId, "created_at"),
        repository.listBy("private_dtp_decisions", "engagement_id", selectedEngagementId, "updated_at"),
        repository.listBy("private_dtp_proof_candidates", "engagement_id", selectedEngagementId, "updated_at"),
      ]);
      const output = exportEngagementSummaryMarkdown({
        engagement,
        artifacts,
        evidenceRuns,
        decisions,
        proofCandidates,
      });
      setExported(output);
      await repository.create("private_dtp_import_export_receipts", {
        direction: "export",
        source_pointer: selectedEngagementId,
        destination_pointer: "hosted-export-summary.md",
        result: "pass",
        record_counts: {
          artifacts: artifacts.length,
          evidence_runs: evidenceRuns.length,
          decisions: decisions.length,
          proof_candidates: proofCandidates.length,
        },
        notes: "Exported engagement summary markdown.",
      });
      setMessage("Exported summary.");
    } catch (error) {
      setMessage(error instanceof Error ? error.message : "Export failed.");
    }
  }

  function readFile(file: File | undefined) {
    if (!file) return;
    setSourcePointer(file.name);
    file.text().then(setMarkdown).catch(() => setMessage("Could not read file."));
  }

  return (
    <section className="panel">
      <div className="panelTitle">
        <FileInput size={18} aria-hidden="true" />
        <h2>Import / Export</h2>
      </div>

      <label>
        Engagement
        <select
          value={selectedEngagementId}
          onChange={(event) => setSelectedEngagementId(event.target.value)}
        >
          <option value="">Create from markdown</option>
          {engagements.map((engagement) => (
            <option key={String(engagement.id)} value={String(engagement.id)}>
              {String(engagement.title ?? engagement.client_or_project_alias ?? engagement.id)}
            </option>
          ))}
        </select>
      </label>
      <label>
        Source pointer
        <input value={sourcePointer} onChange={(event) => setSourcePointer(event.target.value)} />
      </label>
      <label>
        Markdown
        <input type="file" accept=".md,.markdown,text/markdown,text/plain" onChange={(event) => readFile(event.target.files?.[0])} />
        <textarea value={markdown} onChange={(event) => setMarkdown(event.target.value)} rows={7} />
      </label>

      <div className="buttonRow">
        <button className="secondaryButton" type="button" onClick={importMarkdown}>
          Import
        </button>
        <button className="secondaryButton" type="button" onClick={exportSummary}>
          Export
        </button>
      </div>

      {exported ? <textarea className="exportBox" value={exported} readOnly rows={7} /> : null}
      {message ? <p className="muted">{message}</p> : null}
    </section>
  );
}

function RecordTable({ config, records }: { config: EntityConfig; records: DtpRecord[] }) {
  if (records.length === 0) {
    return <p className="emptyState">No records yet.</p>;
  }

  return (
    <section className="records" aria-label={`${config.title} records`}>
      {records.map((record) => (
        <article key={String(record.id)} className="recordCard">
          <div>
            <h3>{String(record.title ?? record.public_claim ?? record.repo ?? record.id)}</h3>
            <p>{String(record.id ?? "")}</p>
          </div>
          <dl>
            {config.display.map((key) => (
              <div key={key}>
                <dt>{key.replaceAll("_", " ")}</dt>
                <dd>{formatValue(record[key])}</dd>
              </div>
            ))}
          </dl>
        </article>
      ))}
    </section>
  );
}

function queueSize(config: EntityConfig, records: DtpRecord[]): number {
  if (!config.queueStatusField || !config.queueStatuses) return 0;
  return records.filter((record) =>
    config.queueStatuses!.includes(String(record[config.queueStatusField!] ?? "")),
  ).length;
}

function initialValues(config: EntityConfig): DtpRecord {
  return Object.fromEntries(
    config.fields.map((field) => [field.key, defaultValue(field, config.table)]),
  );
}

function defaultValue(field: FieldConfig, table: TableName): string {
  if (field.key === "data_class") return "P1";
  if (field.key === "permission_level") return "internal_only";
  if (field.key === "permission_status") return "not_requested";
  if (field.key === "redaction_status") return "not_reviewed";
  if (field.key === "proof_eligibility") return "not_candidate";
  if (field.key === "sensitivity") return "internal_only";
  if (field.key === "stage") return "intake";
  if (field.key === "kind") return "client";
  if (field.key === "lane") return "local";
  if (field.key === "result") return "pass";
  if (field.key === "classification") return "watch";
  if (field.key === "item_type") return "follow_up";
  if (field.key === "status") {
    if (table === "private_dtp_proof_candidates") return "proposed";
    if (table === "private_dtp_decisions") return "proposed";
    if (table === "private_dtp_redaction_reviews") return "not_started";
    return "open";
  }
  if (field.key.endsWith("_status")) return "not_reviewed";
  return "";
}

function inflateArrayFields(fields: readonly FieldConfig[], values: DtpRecord): DtpRecord {
  const result = { ...values };
  for (const field of fields) {
    if (field.kind === "array") {
      result[field.key] = String(values[field.key] ?? "")
        .split("\n")
        .map((item) => item.trim())
        .filter(Boolean);
    }
  }
  return result;
}

function formatValue(value: unknown): string {
  if (Array.isArray(value)) return value.join(", ");
  if (value === null || value === undefined || value === "") return "not recorded";
  return String(value);
}
