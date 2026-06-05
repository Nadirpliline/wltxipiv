// Lightweight typed API client for the Mandate backend.
// In the browser we hit the same origin and rely on Next.js rewrites to proxy
// /api/* to the FastAPI service (see next.config.mjs).

export const ORG_ID = 1;

async function http<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`/api/v1${path}`, {
    ...init,
    headers: { "Content-Type": "application/json", ...(init?.headers || {}) },
    cache: "no-store",
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`${res.status}: ${text}`);
  }
  return res.json() as Promise<T>;
}

// --- Types ---------------------------------------------------------------

export interface Overview {
  organization: { id: number; name: string; slug: string };
  nav_usd: number;
  liquid_usd: number;
  yield_usd: number;
  stablecoin_usd: number;
  volatile_usd: number;
  stablecoin_pct: number;
  by_chain: Record<string, number>;
  by_asset: Record<string, number>;
  projected_annual_yield_usd: number;
  policy: Record<string, number | string>;
  wallet_count: number;
}

export interface WalletAsset {
  asset: string;
  amount: number;
  usd_price: number;
  usd_value: number;
}
export interface Wallet {
  wallet_id: number;
  label: string;
  chain: string;
  address: string;
  kind: string;
  threshold: number;
  owners: number;
  assets: WalletAsset[];
  usd_value: number;
}

export interface Recommendation {
  kind: string;
  severity: string;
  title: string;
  detail: string;
  amount_usd: number;
  venue?: string;
  apy?: number;
}

export interface AgentStep {
  idx: number;
  kind: string;
  tool: string;
  message: string;
  arguments: Record<string, unknown>;
  observation: Record<string, unknown>;
}
export interface AgentRun {
  id: number;
  goal: string;
  status: string;
  provider: string;
  summary: string;
  steps: AgentStep[];
}

export interface Payment {
  id: number;
  payee_name: string;
  country: string;
  amount_usd: number;
  chain: string;
  asset: string;
  to_address: string;
  fee_usd: number;
  route: string;
  status: string;
  memo: string;
}
export interface Batch {
  id: number;
  name: string;
  status: string;
  total_usd: number;
  total_fees_usd: number;
  payment_count: number;
  created_at: string;
  payments: Payment[];
}

export interface TrialBalanceRow {
  code: string;
  name: string;
  type: string;
  debit: number;
  credit: number;
  balance: number;
}
export interface TrialBalance {
  rows: TrialBalanceRow[];
  total_debit: number;
  total_credit: number;
  balanced: boolean;
}

export interface JournalLine {
  account_code: string;
  account_name: string;
  debit: number;
  credit: number;
  memo: string;
}
export interface JournalEntry {
  id: number;
  date: string;
  memo: string;
  reference: string;
  source: string;
  balanced: boolean;
  total_debit: number;
  total_credit: number;
  lines: JournalLine[];
}

export interface YieldVenue {
  venue: string;
  asset: string;
  chain: string;
  apy: number;
  risk_tier: string;
}

export interface Transaction {
  id: number;
  tx_type: string;
  status: string;
  chain: string;
  asset: string;
  amount: number;
  usd_value: number;
  fee_usd: number;
  counterparty: string;
  category: string;
  memo: string;
  created_at: string;
}

// --- Endpoints -----------------------------------------------------------

export const api = {
  overview: () => http<Overview>(`/orgs/${ORG_ID}/overview`),
  wallets: () => http<Wallet[]>(`/orgs/${ORG_ID}/wallets`),
  recommendations: () => http<Recommendation[]>(`/orgs/${ORG_ID}/recommendations`),
  transactions: () => http<Transaction[]>(`/orgs/${ORG_ID}/transactions?limit=100`),

  runAgent: (goal: string) =>
    http<AgentRun>(`/orgs/${ORG_ID}/agent/run`, {
      method: "POST",
      body: JSON.stringify({ goal }),
    }),
  agentRuns: () => http<AgentRun[]>(`/orgs/${ORG_ID}/agent/runs`),

  batches: () => http<Batch[]>(`/orgs/${ORG_ID}/payroll/batches`),
  sampleBatch: (name = "Sample payroll (12 contractors)") =>
    http<Batch>(`/orgs/${ORG_ID}/payroll/sample?name=${encodeURIComponent(name)}`, {
      method: "POST",
    }),
  batch: (id: number) => http<Batch>(`/orgs/${ORG_ID}/payroll/batches/${id}`),
  uploadPayroll: async (name: string, file: File) => {
    const form = new FormData();
    form.append("file", file);
    const res = await fetch(
      `/api/v1/orgs/${ORG_ID}/payroll/upload?name=${encodeURIComponent(name)}`,
      { method: "POST", body: form }
    );
    if (!res.ok) throw new Error(`${res.status}: ${await res.text()}`);
    return (await res.json()) as Batch;
  },
  proposeBatch: (id: number) =>
    http<{ proposals: { chain: string; payment_count: number; total_usd: number; safe_tx_hash: string }[] }>(
      `/orgs/${ORG_ID}/payroll/batches/${id}/propose`,
      { method: "POST" }
    ),
  executeBatch: (id: number) =>
    http<{ executed_payments: number; total_usd: number; total_fees_usd: number }>(
      `/orgs/${ORG_ID}/payroll/batches/${id}/execute`,
      { method: "POST" }
    ),

  trialBalance: () => http<TrialBalance>(`/orgs/${ORG_ID}/ledger/trial-balance`),
  journal: () => http<JournalEntry[]>(`/orgs/${ORG_ID}/ledger/journal`),
  yieldVenues: () => http<YieldVenue[]>(`/orgs/${ORG_ID}/yield/venues`),

  reportUrls: {
    auditorPdf: `/api/v1/orgs/${ORG_ID}/reports/auditor.pdf`,
    quickbooksCsv: `/api/v1/orgs/${ORG_ID}/reports/quickbooks.csv`,
    transactionsCsv: `/api/v1/orgs/${ORG_ID}/reports/transactions.csv`,
  },
};

export function fmtUsd(n: number, max = 0): string {
  return n.toLocaleString("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: max,
  });
}
export function fmtPct(n: number): string {
  return `${(n * 100).toFixed(1)}%`;
}
