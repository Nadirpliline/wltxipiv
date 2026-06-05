# Mandate — Autonomous CFO Agent for Crypto-Native Organizations & DAOs

> **Stripe Atlas + Rippling + Brex for the on-chain world — run by an LLM, not by people.**

---

## 1. Elevator pitch

**To your mom:** *"It's a smart robot accountant that pays your contractors all over
the world in dollar-stablecoins, handles the bookkeeping and taxes, and emails you a
clean report."*

**To a VC:** *"Mandate is an autonomous treasury agent for crypto-native orgs. You
connect your Safe / Squads multisig; the agent sees incoming payments, converts to
your chosen stablecoin, rebalances the treasury by policy, pays payroll and vendors
in 90+ countries, keeps double-entry on-chain books, and prepares auditor-ready
reports. It's Stripe Atlas + Rippling + Brex for on-chain, driven by an LLM rather
than headcount."*

**The killer demo:** upload a CSV of 200 contractors in 40 countries → in ~90 seconds
the agent routes every payee to the cheapest chain (or a local fiat rail), screens
each for compliance, builds the multisig proposals, settles them, and produces a PDF
report ready for a Deloitte auditor. Alliance DAO's mentors run Alliance DAO's own
treasury — this is *their* pain. They can sign a check before the Zoom call ends.

---

## 2. The problem

Thousands of DAOs and crypto startups run treasuries worth $1M–$1B **in Google
Sheets**. The day-to-day reality:

- **Payroll is manual and global.** Paying 50–200 contributors across dozens of
  countries means juggling chains, stablecoins, gas, FX, and local off-ramps by hand.
- **No real books.** There is no double-entry ledger, so audits, taxes, and investor
  reporting are a quarterly fire drill reconstructed from block explorers.
- **Multisig friction.** Safe/Squads are great for custody but terrible as a finance
  workflow: no policy engine, no payee directory, no categorization, no reporting.
- **Compliance is bolted on.** KYC/AML screening of counterparties is ad hoc, if it
  happens at all.
- **Idle capital.** Millions sit idle in stablecoins instead of earning T-bill / DeFi
  yield, because nobody owns the rebalancing decision.

Existing fintech (Brex, Mercury, Rippling, Deel) doesn't speak on-chain. Existing
crypto tools (Safe, Squads, Den, Utopia) are wallets, not finance teams.

---

## 3. Why now

1. **Regulatory unlock.** The **GENIUS Act** (US) and **MiCA** (EU) legitimized
   stablecoin payments; stablecoin payroll roughly doubled in 2025.
2. **Models can finally do this.** Frontier models (Claude Opus/Sonnet 4, GPT-5) do
   reliable multi-step **tool-use** in financial workflows — not true a year ago.
3. **Programmable multisig.** Safe modules and Squads let an agent be a **co-signer
   with risk limits** — autonomy without surrendering keys.
4. **Compliance & identity APIs.** Bridge, Brale, Privy, Dynamic close KYC/AML and
   on/off-ramp faster than a bank ever could.
5. **The pain is acute and universal.** Every DAO treasurer feels it monthly.

---

## 4. What Mandate does (product)

| Capability | What it means | Status in this build |
|---|---|---|
| **Multi-chain treasury** | Aggregate balances across Ethereum, Base, Arbitrum, Optimism, Polygon, Solana; NAV, allocation by chain/asset, stablecoin %. | ✅ End-to-end |
| **Autonomous CFO agent** | Plain-English goals → planned, policy-bounded tool calls → audited execution trace. | ✅ End-to-end |
| **Policy engine** | Min operating reserve, target stablecoin %, idle-yield threshold, max autonomous transfer, required signatures. | ✅ End-to-end |
| **Global payroll** | CSV import → cheapest-chain routing or fiat off-ramp → compliance screen → multisig proposals → execute. | ✅ End-to-end |
| **Double-entry ledger** | Every action posts balanced journal entries; trial balance & income statement always reconcile. | ✅ End-to-end |
| **Yield deployment** | Survey venues (Aave/Morpho/Ondo T-bills), deploy idle stablecoins, track accrual. | ✅ End-to-end |
| **FX / swap routing** | Li.Fi-style quotes with realistic spreads for stablecoin/asset rebalancing. | ✅ End-to-end |
| **Compliance screening** | Sanctioned-country + address checks gate every payee before funds move. | ✅ End-to-end |
| **Auditor reporting** | One-click **PDF** (treasury position, trial balance, P&L, register) + **QuickBooks CSV**. | ✅ End-to-end |
| **Dashboard** | Next.js + Tailwind UI over the whole system. | ✅ End-to-end |

Everything runs in **sandbox mode** with no private keys and no external API keys, so
the product is fully demonstrable offline and in CI. Flipping to **live mode** points
the same adapters at real services.

---

## 5. Architecture

```
                          ┌───────────────────────────────────────────────┐
                          │                  Frontend                      │
                          │           Next.js 14 + Tailwind                │
                          │  Dashboard · Agent · Payroll · Ledger/Reports  │
                          └───────────────────────┬───────────────────────┘
                                                  │  /api/* (proxied)
                          ┌───────────────────────▼───────────────────────┐
                          │                 FastAPI backend                │
                          │                                                │
                          │  ┌──────────────┐   ┌────────────────────────┐ │
                          │  │  Agent core  │──▶│  Tool registry (9)     │ │
                          │  │ orchestrator │   │  overview, balance,    │ │
                          │  │ (det. / LLM) │   │  recommend, yield,     │ │
                          │  └──────────────┘   │  swap, transfer,       │ │
                          │         │           │  batch_payout, deploy, │ │
                          │         │           │  categorize            │ │
                          │         ▼           └───────────┬────────────┘ │
                          │  ┌──────────────────────────────▼───────────┐  │
                          │  │                 Services                  │  │
                          │  │ ledger · treasury · routing · payroll ·   │  │
                          │  │ categorization · seed                     │  │
                          │  └───────┬───────────────────────┬──────────┘  │
                          │          │                       │             │
                          │  ┌───────▼────────┐     ┌────────▼──────────┐  │
                          │  │   Adapters     │     │   Reports         │  │
                          │  │ Safe · Squads  │     │  Auditor PDF      │  │
                          │  │ Li.Fi · Bridge │     │  QuickBooks CSV   │  │
                          │  │ yield · KYC ·  │     └───────────────────┘  │
                          │  │ pricing        │                            │
                          │  └───────┬────────┘                            │
                          │          │ sandbox (deterministic) │ live      │
                          └──────────┼────────────────────────────────────┘
                                     ▼
        Safe Tx Service · Squads · Li.Fi · Bridge.xyz · Aave/Morpho/Ondo · screening
                                     │
                          ┌──────────▼───────────┐
                          │   SQLAlchemy ORM      │
                          │ SQLite (dev) /        │
                          │ Postgres (prod)       │
                          └───────────────────────┘
```

### Layering principle

- **Adapters** wrap the outside world (chains, swaps, off-ramps, yield, compliance,
  pricing). Each has a `sandbox` and a `live` path behind one interface, so the rest
  of the system never knows or cares whether it's hitting a real API.
- **Services** hold business logic: the double-entry ledger, treasury/NAV math,
  cheapest-chain routing, the payroll pipeline, categorization, and seeding.
- **Agent** exposes services as typed **tools** and an **orchestrator** that turns a
  goal into an ordered, audited sequence of tool calls.
- **API** is a thin FastAPI layer over services and the agent.
- **Frontend** is a stateless dashboard that talks only to the API.

### The agent core

The agent is intentionally **provider-agnostic**:

- **Deterministic planner (default).** An intent parser maps goals to typed tool
  calls. This makes the entire product work with **zero credentials**, keeps demos and
  tests reproducible, and provides a safe fallback.
- **LLM planner (optional).** Set `MANDATE_LLM_PROVIDER=anthropic|openai` and a key;
  the same tools and specs are handed to the model for genuine multi-step tool-use.
  Any failure degrades gracefully back to the deterministic planner.

Every run is persisted as an `AgentRun` with ordered `AgentRunStep`s (thought → tool →
observation), so **every decision the agent makes is auditable** — essential for a
product that moves money.

### Safety model

- Mandate **never holds private keys.** It *builds* Safe/Squads proposals; humans (or
  a policy-bounded co-signer module) sign.
- **Policy limits** are enforced in code: transfers above
  `max_autonomous_transfer_usd` are marked `awaiting_signatures` rather than executed.
- **Compliance gates** run before any payee is included in a payable batch.
- **Books can't silently break:** `post_entry` rejects unbalanced journal entries, and
  the payroll executor re-verifies the trial balance after posting.

---

## 6. Data model (double-entry at the core)

| Domain | Models |
|---|---|
| Org & policy | `Organization`, `TreasuryPolicy` |
| Treasury | `Wallet`, `WalletBalance`, `Transaction`, `YieldPosition` |
| Accounting | `Account`, `JournalEntry`, `JournalLine` |
| Payments | `Contractor`, `PayrollBatch`, `Payment` |
| Agent | `AgentRun`, `AgentRunStep` |

A default **chart of accounts** (10 accounts spanning asset/liability/equity/
revenue/expense) is seeded per org. Example postings:

- *Deploy idle USDC to Morpho:* debit `1100 Yield Positions`, credit `1000 Treasury`.
- *Execute payroll:* debit `5000 Payroll Expense` + `5200 Network Fees`, credit
  `1000 Treasury`.

The trial balance reconciles after every operation — verified in tests.

---

## 7. Tech stack

- **Backend:** Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic v2, ReportLab (PDF).
- **DB:** SQLite for dev/CI, Postgres for production (one env var to switch).
- **Frontend:** Next.js 14 (App Router), React 18, TypeScript, Tailwind CSS.
- **Agent:** in-house orchestrator; optional Anthropic/OpenAI tool-use.
- **Infra:** Docker + docker-compose (backend, frontend, Postgres).
- **Tests:** pytest (ledger invariant, payroll pipeline, routing, compliance, agent,
  PDF).

---

## 8. Business model — the path to $10M+ ARR

1. **Take rate on payments:** **0.1–0.25%** of GPV routed through the agent (Stripe,
   but in stablecoins). At $5B GPV → **$5–12M ARR**.
2. **SaaS seats:** **$500–2,000/mo** per finance seat + per-agent fee.
3. **FX / conversion spread:** **15–25 bps** on stablecoin↔stablecoin and on/off-ramp.
4. **Yield share:** park idle treasury in Aave/Morpho/T-bill tokens, take **10–20%**
   of the yield generated.

**TAM:** ~15,000 crypto-native orgs hold $1M+ treasuries today; the adjacent
Brex/Mercury fintech market is **$50B+**. At 3% penetration and $100M ARR, comparable
multiples (Ramp/Brex) imply a **$2–3B** valuation.

---

## 9. Go-to-market (built for Alliance DAO)

- **Wedge:** payroll + bookkeeping for DAOs and crypto startups already on Safe/Squads.
- **Distribution:** Alliance DAO and accelerator networks first (mentors are users),
  then Safe/Squads app ecosystems, then the broader fintech market.
- **Proof:** the "I just paid 47 contractors in 90 seconds" Loom + auditor-grade PDF
  is a self-evident demo. Sign 5 DAOs to pilot LOIs as traction.
- **Moat over time:** the **ledger + payee graph + policy history** become switching
  costs; the agent's audit trail becomes the system of record finance teams trust.

---

## 10. Demo script (what the recording shows)

1. **Dashboard** — $4.25M NAV across 4 multisig wallets on 4 chains; agent flags idle
   cash to deploy and a rebalance toward target stablecoin %.
2. **CFO Agent** — *"Deploy $250,000 idle USDC into the highest-yield venue."* The
   agent calls `list_yield_venues` → `deploy_yield` (Morpho, 6.48% APY) with a visible
   audit trace.
3. **Payroll** — **Run sample batch** (12 contractors, 10 countries): auto-routes to
   Polygon/Solana or SEPA/SPEI fiat rails, screens compliance, builds 3 multisig
   proposals, executes all 12 — *"Paid 12 contractors in 0.02s."*
4. **Ledger & Reports** — books still balance ($3,576,257 = $3,576,257); download the
   **Auditor PDF** and **QuickBooks CSV**.

---

## 11. How to run

```bash
# One command (Docker):
docker compose up --build
#   Dashboard → http://localhost:3000   API docs → http://localhost:8000/docs

# Or local dev:
cd backend && python3 -m venv .venv && . .venv/bin/activate \
  && pip install -r requirements.txt && uvicorn app.main:app --reload --port 8000
cd frontend && npm install && npm run dev

# Tests:
cd backend && . .venv/bin/activate && PYTHONPATH=. pytest -q   # 13 passing
```

---

## 12. Roadmap from MMP → production

- **Live adapters:** Safe Transaction Service + Squads program calls; Li.Fi and
  Bridge.xyz live APIs; on-chain balance indexing (e.g. via RPC/Subgraph).
- **Co-signer module:** deploy a Safe module so the agent can auto-sign within policy
  limits, with slashing/timelocks for safety.
- **Richer accounting:** cost-basis lot tracking, multi-currency, accrual schedules,
  tax-lot reporting, and direct QuickBooks/Xero sync.
- **LLM long-tail:** model-driven categorization and anomaly detection on top of the
  deterministic rules.
- **Auth & multi-tenant:** Privy/Dynamic login, org RBAC, SOC 2 controls.

---

## 13. Why Mandate wins

- It is the **safest path to revenue** among on-chain AI ideas: recurring SaaS + take
  rate + yield share, selling into an acute, universal pain.
- It is **defensible**: the ledger, payee graph, and audit trail compound into
  switching costs and become the financial system of record.
- It is **demonstrably real today**: this repository runs the entire flow end-to-end,
  offline, with balanced books and an auditor-ready report — not slides.
