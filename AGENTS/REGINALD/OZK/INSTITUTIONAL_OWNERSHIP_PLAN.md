# OZK Institutional Ownership Verification Plan
**Created:** 2026-04-12 | **Status:** DRAFT | **Trigger:** 13F data review showing Wellington -43%, smart money divergence

---

## What We Know (13F, as of Dec 31 2025)

| Institution | Type | Shares (MM) | Change | Read |
|---|---|---|---|---|
| Vanguard | Index/passive | 11.08 | -1.35% | Slight trim, mechanical |
| BlackRock | Index/passive | 10.11 | +1.13% | Mechanical |
| Wasatch Advisors | Active small/mid-cap | 6.95 | -6.62% | Bank specialist reducing |
| Dimensional | Systematic/factor | 6.59 | +1.93% | Factor rebalance |
| State Street | Index/passive | 6.56 | +9.10% | Mechanical |
| Schwab IM | Index/passive | 4.55 | +1.65% | Mechanical |
| American Century | Mixed | 3.05 | +11.21% | Adding |
| First Trust | ETF | 2.90 | +3.33% | Mechanical |
| AQR Capital | Quant | 1.58 | -19.97% | Quant selling |
| Morgan Stanley | Bank/wealth | 1.47 | -14.61% | Sell-side pulling back |
| D.E. Shaw | Quant | 1.38 | -26.06% | Major quant reduction |
| Citadel | Market maker/multi-strat | 1.27 | +259.52% | Likely hedging/arb, not conviction |
| Wellington Mgmt | Fundamental/credit | 1.25 | -42.89% | HEADLINE — deep credit shop nearly halved |
| Millennium | Multi-strategy | 1.08 | +20.06% | Pod-level, short horizon |
| Renaissance Tech | Pure quant | 0.87 | +35.71% | Statistical/mean-reversion |
| 1832 Asset Mgmt | Canadian AM | 1.63 | +21,166% | New position |

**Pattern:** Fundamental credit analysts (Wellington, Wasatch) selling hard. Quant/trading (Citadel, Renaissance, Millennium) adding. Index (Vanguard, BlackRock, State Street) roughly flat.

---

## Three Unknowns

### 1. WHY did Wellington, Wasatch, D.E. Shaw, AQR sell?

| Source | What It Tells Us | Where to Find | Feasibility |
|---|---|---|---|
| **Wellington fund shareholder reports (N-CSR)** | Fund commentary sometimes names holdings and explains sells | EDGAR: search "Wellington" filer, form type N-CSR, full-text search "Bank OZK" or "OZK" | MEDIUM — they manage dozens of funds, would need to find which fund(s) held OZK |
| **Wasatch quarterly fund letters** | Wasatch is unusually transparent about small-cap thesis changes | Wasatch website (public), or EDGAR N-CSR | HIGH — Wasatch often names specific holdings |
| **Sell-side research timed to the exit** | If a downgrade or negative initiation coincided with the selling period | Check for Oct-Dec 2025 analyst actions on OZK. We already have Citi SELL $40 and UBS Neutral $48. Were these issued in Q4? | MEDIUM — we'd need to confirm timing |
| **Conference call Q&A** | Did Wellington or Wasatch analysts ask questions on Q4 earnings call (Jan)? Asking tough questions + selling = conviction | OZK Q4 2025 earnings call transcript | HIGH — transcripts are available |

**Priority action:** Search EDGAR for Wasatch N-CSR mentioning OZK. Wasatch is the most likely to explain in writing.

### 2. WHAT have they done since Dec 31?

| Source | What It Tells Us | Where to Find | Feasibility |
|---|---|---|---|
| **13D/13G filings** | Any holder crossing 5% threshold must file within 10 days. Would catch if Vanguard, BlackRock, Wasatch, Dimensional, or State Street (all near/above 5%) crossed in either direction | EDGAR: search OZK (CIK 0001569650), form types SC 13D, SC 13G, SC 13G/A | HIGH — quick EDGAR search |
| **Form 4 (insider transactions)** | Not institutional, but insiders buying/selling tells us what management sees pre-earnings | EDGAR: CIK 0001569650, form type 4 | HIGH — already tracked in KB-142-146, need Q1 2026 update |
| **N-PORT filings (monthly fund holdings)** | Mutual funds file monthly holdings with 60-day lag. Jan 2026 filed by Mar 31. Feb 2026 filed by Apr 30. | EDGAR: search filer (e.g., Wellington, Wasatch), form type N-PORT, then search holdings for OZK | MEDIUM — N-PORT files are large XML, need to find OZK within them |
| **WhaleWisdom / Fintel** | Aggregated institutional data, sometimes has intra-quarter estimates | Web search | LOW — paywalled, may not have more recent data |

**Priority action:** EDGAR search for OZK 13D/13G filings in 2026. Fast, free, definitive for 5% threshold crossings.

### 3. WHAT'S coming next (forward-looking)?

| Source | What It Tells Us | Where to Find | Feasibility |
|---|---|---|---|
| **Q1 2026 13F filings (due ~May 15)** | Full institutional position update as of Mar 31, 2026 | EDGAR, but won't be available until mid-May | NOT YET — 1 month away |
| **Options market positioning** | Unusual institutional put/call activity signals positioning ahead of earnings | Options flow data, unusual activity scanners | MEDIUM — we'd need a data source |
| **Short interest (mid-Apr FINRA)** | Already tracking (13.81% / 11.2 DTC as of Mar 25). Next release imminent | FINRA short interest data | HIGH — already on research agenda |
| **Proxy filing / annual meeting** | Shareholder proposals, activist involvement | EDGAR DEF 14A for OZK | LOW priority — no activist angle currently |

**Priority action:** Pull updated short interest when mid-Apr FINRA data drops (~Apr 14-15). Already on research agenda.

---

## Execution Plan (Priority Order)

| # | Action | Source | Time | Answers |
|---|---|---|---|---|
| 1 | Search EDGAR for OZK 13D/13G filings in 2026 | EDGAR full-text search | 10 min | Did any major holder cross 5% since Dec 31? |
| 2 | Search EDGAR for Wasatch N-CSR mentioning OZK | EDGAR filer search | 15 min | Why did Wasatch reduce? Did they explain? |
| 3 | Pull OZK Form 4 filings for Q1 2026 | EDGAR CIK search | 10 min | Any insider buys pre-earnings? (updates KB-142-146) |
| 4 | Check OZK Q4 2025 earnings call for Wellington/Wasatch analyst questions | Transcript | 15 min | Did sellers ask tough questions on the call? |
| 5 | Search for Wellington N-PORT (Jan 2026) mentioning OZK | EDGAR | 20 min | Did Wellington continue selling in Jan? |
| 6 | Pull short interest update when available (~Apr 14) | FINRA | 5 min | Has short interest increased alongside institutional selling? |

**Total estimated effort:** ~75 min of research across 2-3 sessions

---

## What Would Change Our View?

| Finding | Impact |
|---|---|
| Wellington N-PORT shows they REVERSED and bought back in Jan/Feb | Weakens thesis — their sell was tactical, not credit-driven |
| Wasatch letter explicitly cites CRE/credit concerns for selling OZK | Strengthens thesis — independent validation of our channel analysis |
| 13D/13G shows a new 5%+ holder emerged in Q1 2026 | Depends on who — activist = catalyst, index = neutral |
| Wellington analyst asked pointed CRE questions on Q4 call | Strengthens thesis — selling + probing = conviction |
| Short interest rising alongside institutional selling | Convergence signal — multiple independent actors bearish |
