import type { SupabaseClient } from "@supabase/supabase-js";
import type { DtpRecord, TableName } from "./types";

export class PrivateDtpRepository {
  constructor(private readonly client: SupabaseClient) {}

  async list(table: TableName, sortBy = "created_at"): Promise<DtpRecord[]> {
    const { data, error } = await this.client
      .from(table)
      .select("*")
      .order(sortBy, { ascending: false });

    if (error) throw error;
    return (data ?? []) as DtpRecord[];
  }

  async listBy(
    table: TableName,
    column: string,
    value: string,
    sortBy = "created_at",
  ): Promise<DtpRecord[]> {
    const { data, error } = await this.client
      .from(table)
      .select("*")
      .eq(column, value)
      .order(sortBy, { ascending: false });

    if (error) throw error;
    return (data ?? []) as DtpRecord[];
  }

  async create(table: TableName, values: DtpRecord): Promise<DtpRecord> {
    const { data, error } = await this.client
      .from(table)
      .insert(normalizeValues(values))
      .select("*")
      .single();

    if (error) throw error;
    return data as DtpRecord;
  }
}

export function normalizeValues(values: DtpRecord): DtpRecord {
  return Object.fromEntries(
    Object.entries(values)
      .map(([key, value]) => {
        if (typeof value === "string") {
          const trimmed = value.trim();
          return [key, trimmed === "" ? null : trimmed];
        }
        if (Array.isArray(value)) {
          return [key, value.filter((item) => String(item).trim() !== "")];
        }
        return [key, value ?? null];
      })
      .filter(([, value]) => value !== null),
  );
}
