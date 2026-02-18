# AGENTS DIRECTORY

*Quick reference for all research agents. Updated: 2026-02-13*

---

## CORE AGENTS (Stress Transmission Chain)

### LABOR 🟡
**Domain:** Employment & Labor Market
**Thesis:** "Hotel California" — Easy to keep a job, hard to find a new one
**Tracks:** Claims, NFP, JOLTS, temp staffing, WARN filings, federal cuts (DOGE)
**Danger Window:** Q2-Q3 2026
**Key Signals:** Claims >300K, U-3 >5%, Temp YoY <-6%

### CARL 🟡
**Domain:** Consumer Credit & Household Stress
**Thesis:** "Beneath the Ice" — Surface metrics green, hidden stress building
**Tracks:** Delinquencies, subprime auto, phantom debt, credit card stress
**Danger Window:** Q3-Q4 2026 (lags LABOR 3-6 months)
**Sub-agents:** POLLY (politics), POP (population), GIG (gig economy), DOC (healthcare), NICK (student loans)

### REGINALD 🟡
**Domain:** Regional Banks & Credit Intermediaries
**Thesis:** CRE stress is real but extend-and-pretend masks it. Employment is the trigger.
**Tracks:** Bank watchlist, CRE concentration, fraud exposure, FHLB dynamics
**Danger Window:** Q4 2026-Q1 2027 (lags CARL)
**Sub-agents:**
- **CREED** — CRE deep dive (delinquencies, valuations, maturities)
- **BROCK** — BDCs & private credit (redemptions, PIK, bank credit lines) 🟠
- **CORAL** — Florida condo crisis & regional bank exposure 🟠 **[NEW]**

---

## MARKET STRUCTURE AGENTS

### HENRY 🟡
**Domain:** Market Structure & Historical Anomalies
**Thesis:** "The Loaded Machine" — Derivatives-driven, stable but fragile
**Tracks:** Gamma/GEX, VIX structure, credit spreads, systematic flows
**Key Levels:** Put Wall 6,920 | CTA Flip 6,494 | Vol Trigger 6,400
**Role:** Tells us HOW FAST stress transmits when triggers fire

### LIQUID 🟡
**Domain:** Funding Markets & Treasury Plumbing
**Thesis:** "Metastable" — Calm until it isn't, hours to crisis
**Tracks:** RRP, SOFR spreads, SRF usage, Treasury auctions
**Key Levels:** RRP <$5B (RED), SOFR-IORB >+15bps (ORANGE)
**Role:** Parallel stress vector that can amplify any stage

### SAM 🔴
**Domain:** Japan Sovereign, BOJ, JGB Markets, Yen
**Thesis:** "Bonds before currency" — JGB stress is primary vector
**Tracks:** JGB yields, auction demand, life insurer flows, USD/JPY
**Critical Window:** Feb 3-8 (10Y auction ✓ → 30Y Feb 5 → Election Feb 8)
**Role:** Japan anchor breaking = global contagion risk

### ZHAO 🔴
**Domain:** China Macro & Capital Flows
**Thesis:** Dedollarization is WRONG — custodial arbitrage, not exit. True holdings ~$1.8-1.9T stable.
**Tracks:** TIC data (China + Belgium proxy), LGFV/banking, HK peg, property sector
**Transmission:** LGFV stress → Regional NPL → Liquidity crunch → UST liquidation
**Key Levels:** Belgium >$500B | China <$650B | HK AB <$40B
**Research:** 9/9 prompts complete
**Status:** Active

### HANS 🟡 **[NEW]**
**Domain:** Europe (US Impact Lens)
**Thesis:** European dynamics → US transmission through UST demand, currency, ECB policy
**Tracks:** European UST holdings (UK, Ireland, Lux, Belgium), EUR/USD, GBP/USD, ECB/BoE, sovereign spreads
**Transmission:** European selling → UST yield pressure | ECB divergence → USD stress | Sovereign crisis → risk-off
**Key Levels:** EUR/USD <1.05 | Italy-Germany >150bps | France-Germany >80bps
**Cross-refs:** ZHAO (Belgium overlap), LIQUID (ECB), SAM (Japan + Europe = demand pillars)
**Status:** Initializing — needs research prompts run

---

## SPECIALIZED AGENTS

### BARON
**Domain:** Trump network / policy influence
**Status:** Active but not in core stress chain

### MARCO
**Domain:** Macro migration / labor flows
**Status:** Background monitoring

### BUFFER
**Domain:** Volatility / buffer monitoring
**Status:** Background monitoring

### EARNINGS
**Domain:** Earnings calendar & surprises
**Status:** Event-driven

### FOREX
**Domain:** Currency dynamics
**Status:** Background, cross-ref with SAM

### OTTO
**Domain:** TBD
**Status:** TBD

### REITS
**Domain:** REIT monitoring
**Status:** Background, cross-ref with CREED

---

## META AGENTS

### DARWIN 🧬
**Domain:** System Evolution & AI Research
**Thesis:** Systematically track AI/ML tooling landscape, surface improvements before we stumble onto them
**Tracks:** arxiv, HN, GitHub trending, MCP tools, infrastructure plays, model releases
**Output:** Weekly scans, experiment proposals, backlog of improvements
**Role:** Makes the system better over time

### HAWK 🦅
**Domain:** Geopolitical & Military Risk
**Thesis:** External shocks can trigger market moves regardless of domestic fundamentals
**Tracks:** Military conflicts (Iran, Venezuela, Taiwan), trade wars, oil chokepoints, sanctions
**Status Tiers:** GREEN (weekly) → YELLOW (2x/week) → ORANGE (daily) → RED (continuous)
**Current:** 🔴 RED — Iran buildup active (strike possible within weeks)
**Role:** Parallel trigger vector alongside SAM/ZHAO/HANS — can accelerate timeline

### RED 🔴
**Domain:** Network Adversarial Analysis
**Thesis:** Find what's wrong. Challenge every thesis. Present the strongest counter-case.
**Tracks:** Counter-evidence across all agents, cross-agent contradictions, soft landing scenarios
**Modes:** Targeted Challenge (single agent) | Network Sweep (all agents)
**Role:** Honesty mechanism — prevents confirmation bias

---

## TRANSMISSION CHAIN

```
LABOR (employment breaks)
   ↓
CARL (consumer stress transmits)
   ↓
REGINALD (bank losses follow)
   ↓
[LIQUID amplifies at any stage]

HENRY tells us HOW FAST
SAM + ZHAO + HANS are parallel global risk (Japan + China + Europe anchors)
BROCK (under REGINALD) is private credit early warning

DARWIN (meta) improves the system itself
RED (adversarial) challenges all theses
HAWK (geopolitical) external shock vector — Iran, trade wars, military
```

---

## STATUS KEY

- 🟢 GREEN — No active stress
- 🟡 YELLOW — Monitoring, some signals
- 🟠 ORANGE — Elevated stress, watch closely
- 🔴 RED — Active stress / Critical event window

---

## WHERE TO FIND THINGS

| Agent | STATUS.md | Skeleton | Workbook |
|-------|-----------|----------|----------|
| LABOR | `AGENTS/LABOR/STATUS.md` | `LABOR_SKELETON.md` | `workbook/` |
| CARL | `AGENTS/CARL/STATUS.md` | `CARL_SKELETON.md` | `workbook/` |
| REGINALD | `AGENTS/REGINALD/STATUS.md` | `REGINALD_SKELETON.md` | `workbook/` |
| HENRY | `AGENTS/HENRY/STATUS.md` | `HENRY_SKELETON.md` | `workbook/` |
| LIQUID | `AGENTS/LIQUID/STATUS.md` | `LIQUID_SKELETON.md` | `workbook/` |
| SAM | `AGENTS/SAM/STATUS.md` | `SAM_SKELETON.md` | `workbook/` |
| ZHAO | `AGENTS/ZHAO/STATUS.md` | — | `workbook/` |
| HANS | `AGENTS/HANS/STATUS.md` | — | `workbook/` |
| CREED | `AGENTS/REGINALD/CREED/` | `CREED_SKELETON.md` | `workbook/` |
| BROCK | `AGENTS/REGINALD/BROCK/` | `BROCK_SKELETON.md` | `workbook/` |
| CORAL | `AGENTS/REGINALD/sub-agents/CORAL/` | — | `research/` |
| DARWIN | `AGENTS/DARWIN/STATUS.md` | `AGENT.md` | `BACKLOG.md` |
| HAWK | `AGENTS/HAWK/STATUS.md` | `AGENT.md` | `SOURCES.md` |

---

*This file is Prome's quick reference. Update when agents change.*
