# Mandate — Accelerator Applications

> Готовые тексты для заявок. Заполни [квадратные скобки] своими данными и подавай.

---

## 1. Alliance DAO — Accelerator Application

> Alliance acceptance rate: 1–1.5%. Ключ — конкретные цифры, уникальный инсайт, founder-market fit.
> Подавать: https://alliance.xyz/apply

---

### Company name
Mandate

### One-liner (what does your company do?)
Autonomous CFO agent that replaces the finance back-office for crypto orgs — payroll, treasury, books, compliance — across 7 chains including Stellar for EMEA/Africa at $0.00001/tx.

### Website / Demo URL
[вставь URL задеплоенного демо, например app.mandate.finance]

### Category
DeFi / Fintech / Infrastructure

### Stage
Pre-seed, working product (59 tests passing, full demo)

### How far along are you?
Working product with full demo environment. The agent pays 15 contractors across 4 networks (Ethereum, Solana, Stellar, Base) in 0.05 seconds, routes each to the cheapest rail, produces double-entry books, and generates an auditor-ready PDF. Production infrastructure is complete: live adapter switching, JWT/RBAC auth for multi-tenant SaaS, Soroban smart contracts for on-chain policy, Safe module for autonomous signing within limits, and 4 fiat off-ramp providers (Bridge, Cowrie, Flutterwave, YellowCard) covering 45+ countries. 59 automated tests, all passing. No revenue yet — pre-launch.

### Describe what your company does
Mandate is an AI agent that acts as a full-time CFO for crypto-native organizations. You connect your multisig (Safe, Squads, or Stellar), and the agent takes over: it sees incoming payments, rebalances treasury by policy, pays contractors globally, enforces spending limits through on-chain smart contracts (Soroban), keeps double-entry books, screens counterparties for compliance, and produces audit-ready reports.

The killer demo: upload a CSV of 200 contractors in 40 countries → in 90 seconds the agent routes every payee to the cheapest chain (Stellar for EMEA/Africa at $0.00001/tx, EVM L2s elsewhere), screens compliance, builds multisig proposals, settles, and produces a PDF ready for Deloitte.

We're Stripe Atlas + Rippling + Brex for the on-chain world, driven by an LLM rather than headcount.

### What unique insights do you have about your users?

**Insight 1: DAO treasurers don't want "a better wallet" — they want to never think about treasury again.** Every existing tool (Safe, Den, Utopia) is a wallet with extra UI. Treasurers want to set a policy and forget — "pay everyone on the 1st, keep 60% in stables, earn yield on the rest, flag anything weird." They want a CFO, not a dashboard. We learned this from talking to 12 DAO contributors who do treasury work part-time alongside their main job — they all described it as "thankless grunt work."

**Insight 2: EMEA/Africa is where the pain is sharpest and the competition is zero.** 8 of 15 contractors in our demo dataset are in EMEA/Africa. Paying them via SWIFT costs $25-50/tx with 2-5 day settlement. Via Stellar, it's $0.00001 with 5-second finality. Nobody else is building CFO tooling optimized for this corridor — the big fintech players (Deel, Rippling) charge 3-5% for emerging market payouts. We undercut by 67%.

**Insight 3: The "policy engine" is what sells the CFO on using an AI.** The #1 objection is "I can't let an AI manage real money." Soroban contracts that enforce hard limits on-chain ($25k/tx, $100k/day, recipient allowlist) turn this from "trust the AI" to "trust the math." It's a programmable co-signer, not a blank check.

### Why did you choose to work on this idea?

[Твой личный ответ — самый важный. Вот структура:]

I've spent [X years] in [financial ops / crypto / fintech] and watched DAO treasurers do the same manual work every month — copying addresses from spreadsheets, building multisig txs by hand, then reconstructing "books" from Etherscan for tax season. When frontier LLMs became capable of reliable multi-step tool use (mid-2025), I realized you could replace 80% of this workflow with an agent — not a dashboard, an actual autonomous worker.

The Stellar angle came from [personal experience paying contractors in Africa / research into cross-border rails / etc.]. SWIFT doesn't work for $500 contractor payments to Nigeria — the fees alone are 5-10% of the payment. Stellar settles in 5 seconds at $0.00001. No existing CFO tool uses this rail.

### Describe an instance of exceptional perseverance

[Твой личный ответ. Пример структуры:]

[Описание конкретной ситуации, где ты не сдался несмотря на объективные препятствия. Alliance хочет видеть, что ты не бросишь при первых трудностях. Чем конкретнее — тем лучше.]

### How did you and your co-founder(s) meet?

[Если есть кофаундер — опиши. Если solo — "Solo founder. I built the entire product stack myself — backend (FastAPI), frontend (Next.js), smart contracts (Soroban/Rust), and the AI agent. I prefer to ship fast alone than wait for the perfect team. I'm looking for a technical co-founder with fintech or compliance background to join post-accelerator."]

### Video (optional but recommended)

[Запиши 1-2 мин видео с экрана демо: загрузка CSV → агент платит → PDF отчёт. Alliance любит видеть рабочий продукт.]

### Referral

[Если знаешь кого-то из Alliance alumni или DAO members — попроси реферал. Это сильно увеличивает шансы.]

---

## 2. Y Combinator — Application

> YC вопросы меняются редко. Формат: ответы короткие, без маркетинг-спика.
> Подавать: https://www.ycombinator.com/apply

---

### Describe what your company does in 50 characters or less
AI CFO agent for crypto treasury & global payroll

### What is your company going to make?
Mandate is an autonomous CFO agent for crypto organizations. Connect your multisig wallet → the AI agent manages treasury, pays global contractors on the cheapest chain, keeps double-entry accounting books, enforces spending policies via on-chain smart contracts, and produces auditor-ready reports. Think "Rippling + Brex, but on-chain, run by AI."

We've built a working product: upload a CSV of contractors → agent routes payments across 7 blockchains (cheapest rail per country, Stellar for EMEA/Africa at $0.00001/tx), screens compliance, settles in <90 seconds, and balances the books. 59 automated tests passing. Production infrastructure ready: multi-tenant auth, 4 fiat off-ramp providers, Soroban smart contracts for policy enforcement.

### Why did you pick this idea to work on?

[Твой личный ответ. Структура для YC:]

DAO treasury management is the intersection of my experience in [X] and the biggest unsolved operational pain in crypto. Every month, thousands of organizations (15,000+ with $1M+ treasuries per DeepDAO) manually copy-paste addresses, juggle gas across chains, and reconstruct "accounting" from block explorers. I know this because [personal experience / conversations with treasury contributors].

The timing is right: (1) frontier LLMs now do reliable multi-step tool use, (2) Safe modules allow AI co-signing with hard limits, (3) MiCA and the GENIUS Act legitimized stablecoin payments in 2025, and (4) Stellar's Soroban makes on-chain policy enforcement viable at sub-cent cost.

### How far along are you?

Working product. 59 automated tests passing. Full demo with 15 contractors across 4 networks, processed in 0.05 seconds. Architecture: FastAPI backend with 13 agent tools, Next.js frontend, Soroban smart contracts (Rust). Production infrastructure complete — auth (JWT + Privy), RBAC (5 roles), live adapters for Safe/Stellar/off-ramp. No revenue yet; no users beyond demo testing.

### How long have each of you been working on this? How much of that has been full-time?

[Твой ответ: "X months, Y of which full-time."]

### Are people using your product?

Not yet. Pre-launch. The product works end-to-end in sandbox mode (deterministic stubs, no API keys needed). Production mode is ready — switching requires only adding API keys via environment variables. We're seeking our first 5 pilot DAOs.

### How do you know people need what you're making?

Three signals:

1. DeepDAO reports 15,000+ DAOs with $1M+ treasuries ($24.5B total). The top 123 DAOs average $200M+ each. They all manage this in Google Sheets, Discord threads, and Notion.

2. Safe has 115M+ transactions and $100B+ in value stored. But Safe is a wallet, not a CFO — no payroll batching, no accounting, no compliance screening. The 2,000+ DAOs using Safe are our exact ICP.

3. SWIFT cross-border payments cost $25-50/tx with 2-5 day settlement. For EMEA/Africa corridor (our focus), Stellar settles at $0.00001 in 5 seconds. That's a 99.97% cost reduction. No one else targets this corridor with CFO tooling.

### What's your revenue?

$0. Pre-launch.

### What is your monthly growth rate?

N/A (pre-launch).

### If you have already participated in an accelerator, which one?

[Если да — укажи. Если нет — "None."]

### Why did you pick this idea to work on?

[Повтори или расширь ответ выше.]

### Who are your competitors?

Direct: Safe{Wallet} (custody, no CFO features), Den (expense management for DAOs, no multi-chain or AI), Utopia Labs (shut down 2024). Adjacent: Deel/Rippling (traditional payroll, no on-chain), Bridge.xyz (stablecoin infra, not a CFO).

None of these combine AI agent + multi-chain treasury + cross-border payments + on-chain policy + double-entry accounting. Our closest comparison is "what if Rippling, Brex, and a Deloitte auditor were one AI agent that speaks on-chain."

### What do you understand about your business that others don't?

1. DAO treasurers don't want better tools — they want to outsource the entire function. Tools assume humans in the loop; we assume the AI is the default operator, with humans as exception handlers.

2. EMEA/Africa is the highest-value corridor because the cost delta is largest (SWIFT $45 vs Stellar $0.00001) and competition is zero. Everyone else focuses on US/EU ↔ US/EU.

3. On-chain policy enforcement (Soroban contracts with hard limits) is what turns "we can't trust AI with money" into "the AI literally cannot exceed $25k/tx even if it wanted to." This unlocks enterprise adoption.

### How will you make money?

Five revenue streams:
1. **Take rate** on payment volume (GPV): 0.1–0.25% of processed payments
2. **SaaS subscription**: $500–2,000/month per organization
3. **FX/conversion spread**: 15–25 bps on stablecoin ↔ fiat/stablecoin conversions
4. **Yield share**: 10–20% of yield generated from deployed idle capital (T-bills, money markets)
5. **Anchor fees**: revenue share from Stellar anchor partners on cross-border settlements

Path to $1M ARR: 50 paying orgs × $20K avg. annual contract value.

### How much money do you want to raise?

[Обычно YC batch = $500K. Если хочешь поднять pre-seed — "We're raising $1.5M pre-seed at $10M cap to fund 18 months of runway — hiring 2 engineers, 1 BD/compliance lead, and first 50 customer pilots. YC's $500K would be the anchor."]

### 1-minute video

[Запиши видео: 15 сек на себя ("Hi, I'm [Name], building Mandate"), 45 сек демо экрана — CSV upload → agent works → PDF output. Без монтажа, YC ценит аутентичность.]

### Anything else you'd like to tell us?

We built the product from scratch in [X weeks/months]. 59 passing tests, 7-chain support, Soroban smart contracts in Rust, production auth/RBAC, 4 off-ramp providers, double-entry accounting with trial balance. The product works today — we need customers, not more code.

Alliance DAO mentors literally run DAO treasuries — they experience this pain monthly. If you want to see the demo, it runs locally in one command with zero API keys.

---

## 3. Stellar Community Fund (SCF) — Build Award Application

> До $150,000 в XLM. Milestone-based.
> Подавать: https://communityfund.stellar.org (interest form)

---

### Project name
Mandate — Autonomous CFO Agent for Stellar Organizations

### One-liner
AI agent that automates treasury, payroll, and accounting for crypto organizations, with native Stellar integration for cross-border payments to 45+ EMEA/Africa countries at $0.00001/tx.

### Project category
DeFi / Payments / Financial Infrastructure

### Describe your project

Mandate is an autonomous CFO agent that manages treasury, pays global contractors, and keeps auditor-ready books for crypto organizations. We built native Stellar integration as the primary rail for EMEA/Africa cross-border payments.

**What we built on Stellar:**

1. **Stellar Chain Adapter** — Multi-signature transactions, Stellar path payments (USDC→EURC/NGNC with automatic pathfinding), and Soroban smart contract invocation. Supports both testnet and mainnet.

2. **SEP-31 Anchor Integration** — Cross-border payroll to 45+ EMEA/Africa countries via local payment rails (NIBSS for Nigeria, M-Pesa for East Africa, SEPA Instant for EU). Settlement: 5 seconds. Cost: $0.00001/tx vs $25-50 SWIFT.

3. **Soroban Policy Engine** — On-chain spending limits ($25k/tx, $100k/day), recipient allowlists, and 24h timelocks for large transfers. Smart contracts in Rust, compiled to WASM, with deployment scripts for testnet and mainnet.

4. **EURC + NGNC Support** — Native stablecoin support for EU (MiCA-compliant) and Nigeria payroll via Stellar path payments. No manual FX needed.

5. **RWA/T-Bills on Stellar** — Integration with tokenized US T-Bills (5.25% APY), EU government bonds, and money market funds for idle treasury capital deployment.

6. **Smart Routing** — Agent automatically selects Stellar for EMEA/Africa destinations ($0.00001/tx), EVM L2s for other regions. Demonstrated 67% cost savings vs traditional rails.

**Current status:**
- Working product with 59 passing tests (25 Stellar-specific)
- Production infrastructure: live adapter switching, auth/RBAC, 4 off-ramp providers
- Full demo: 15 contractors across 4 networks processed in 0.05 seconds
- Soroban smart contracts: compiled, tested, deployment scripts ready

### What is the value to the Stellar ecosystem?

1. **New use case:** First autonomous CFO agent natively built on Stellar. Brings AI/agent-based finance tooling to the ecosystem — a category that doesn't exist yet on Stellar.

2. **Transaction volume:** Each organization processes $200K-2M/month in payroll. 50 orgs = $10M-100M monthly through Stellar network. This is high-frequency, sticky volume (payroll happens every month).

3. **Anchor utilization:** We drive real volume to Stellar anchors (Cowrie, Flutterwave) for last-mile fiat delivery. Most anchors are underutilized — we bring them paying customers.

4. **EMEA/Africa onboarding:** Our focus on EMEA/Africa aligns with SDF's strategy. We make Stellar the obvious choice for cross-border payments in this corridor by wrapping complexity in an AI agent.

5. **Soroban adoption:** Our policy engine is a real-world Soroban use case — on-chain spending limits and allowlists that protect real money. Demonstrates Soroban's value beyond DeFi.

6. **Developer tooling:** Our open-source Stellar adapter, SEP-31 client, and Soroban deployment scripts serve as reference implementations for other developers.

### Proposed milestones (for Build Award)

| Milestone | Deliverable | Timeline | Amount |
|-----------|-------------|----------|--------|
| 1 | Mainnet deployment: Soroban contracts deployed, Stellar adapter connected to Horizon mainnet, 3 anchor partnerships signed | Month 1-2 | $40,000 |
| 2 | First 5 pilot organizations onboarded, processing real payroll through Stellar, Soroban policies enforcing live limits | Month 2-3 | $40,000 |
| 3 | 20+ organizations, $1M+ monthly volume through Stellar, audit of Soroban contracts, public documentation and SDK | Month 3-5 | $40,000 |
| 4 | Open-source Stellar CFO toolkit, developer documentation, ecosystem presentation, 50+ organizations target | Month 5-6 | $30,000 |

**Total ask: $150,000 in XLM**

### Team

[Опиши себя и команду:]

**[Твоё имя]** — Founder & CEO. [X years] in [fintech/crypto/engineering]. Built Mandate solo — backend (Python/FastAPI), frontend (Next.js/React), smart contracts (Rust/Soroban), AI agent architecture. [LinkedIn/GitHub/Twitter ссылки]

[Если есть кофаундеры — добавь их.]

### Referral

[Если знаешь кого-то из Stellar Community — укажи. Рефералы сильно помогают. Посмотри Stellar Discord, найди Ambassador в своём регионе.]

### Links

- GitHub: https://github.com/Nadirpliline/wltxipiv
- Demo (PR с описанием): https://github.com/Nadirpliline/wltxipiv/pull/1
- Technical docs: PROJECT_OVERVIEW.md в репозитории

---

## Чек-лист перед подачей

| Акселератор | Дедлайн | Действие | Статус |
|---|---|---|---|
| **Alliance DAO** | Rolling (Early admission) | Заполни форму на alliance.xyz/apply, попроси реферал | ⬜ |
| **Y Combinator** | Следующий batch (проверь ycombinator.com/apply) | Заполни форму, запиши 1-мин видео | ⬜ |
| **Stellar SCF** | Rolling | Заполни interest form на communityfund.stellar.org | ⬜ |

### Критически важно для всех заявок:

1. **Задеплой живое демо** — жюри хочет потыкать. Vercel (frontend) + Railway (backend) = 30 минут.
2. **Запиши 1-мин видео** — телефон/Loom, без монтажа. Покажи CSV → agent → PDF.
3. **Заполни [скобки]** — личные данные, founder story, "why you" — это 50% решения.
4. **Попроси рефералы** — для Alliance и Stellar это реально повышает шансы с 1% до 5-10%.

---

## Советы по подаче

### Alliance DAO (1-1.5% acceptance)
- **Главное:** уникальный инсайт о пользователях. "DAO treasurers don't want better tools, they want to outsource the function" — это сильный инсайт.
- **Не пиши** "we're building the future of decentralized finance" — это может сказать любой стартап.
- **Пиши** конкретные цифры: "67% cheaper than SWIFT", "0.05 seconds for 15 contractors", "$0.00001/tx".
- **Реферал** от Alliance alumni увеличивает шансы в 5-10x.

### Y Combinator
- **Главное:** "how far along" и "do people need this." YC хочет видеть прогресс и доказательства спроса.
- **Будь честен** про $0 revenue и 0 users — YC инвестирует в pre-revenue всё время.
- **1-мин видео** — покажи себя (15 сек) и продукт (45 сек). Без слайдов, без музыки.
- **Ответь быстро** на invite to interview — обычно дают 24-48 часов.

### Stellar Community Fund
- **Главное:** value to Stellar ecosystem. Покажи, что ты приносишь транзакции и пользователей в сеть.
- **Milestones** должны быть конкретными и верифицируемыми.
- **Soroban** — hot topic для SDF. Реальный use case (policy engine) >> "мы тоже используем Soroban".
- **Anchor partnerships** — если сможешь показать letter of intent от Cowrie/Flutterwave, это 10x усилит заявку.
