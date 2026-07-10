# Market Data Tools

**Purpose:** Automated data pulls for agent threshold monitoring and position tracking.

**Location:** `FORGE/tools/market-data/`

---

## Architecture

```
Layer 1: Data Pulls     → fetch.py (FRED + yfinance, raw data retrieval)
Layer 2: Agent Mapping   → config.py (series → agent, thresholds, colors)
Layer 3: Automation      → dashboard.py (combined view, alerts, STATUS updates)
```

## Data Sources (all free)

| Source | What | API Key? |
|--------|------|----------|
| FRED | Economic series (claims, delinquencies, SOFR, yields) | Yes (free) — already have one |
| yfinance | Equity/ETF/commodity/FX prices | No |
| EDGAR | SEC filings | No |
| EIA v2 | Petroleum stocks (`eia_fetch`), EIA-930 hourly demand + retail power prices (`eia_fetch_facets`) | Yes (free) — in `.env` |
| PJM emergency postings | Grid emergency-procedure postings (scraped, `power_watch.py`) | No |

## Coverage

### Tier 1 — Decision Drivers (daily)
- HY OAS, Brent, Gas (AAA), USD/JPY, Initial Claims, Continuing Claims

### Tier 2 — Position Monitoring (daily)
- KRE, APO, ARES, OZK, WAL, FXY, TLT, VIX

### Tier 3 — Structural Signals (weekly) — Phase 2
- SOFR, Reverse Repo, Auto DQ, CC DQ, U-6, 10Y, 2Y, Mortgage 30Y

## Usage (target)

```bash
python3 dashboard.py                 # Full dashboard, all tiers
python3 dashboard.py --agent LABOR   # Single agent view
python3 dashboard.py --tier 1        # Decision drivers only
python3 fetch.py price KRE           # Single ticker price
python3 fetch.py fred ICSA           # Single FRED series
```

## Power / Grid-Stress Instrument (power_watch.py)

Built by DAEDALUS 2026-07-10 (Will-approved Step-1 power instrument layer — power-agent staged path; see `AGENTS/DAEDALUS/outbox/2026-07-10_to-PROME_tier3-gaps-and-power-agent-memo.md` §5). **Consumer: HENRY (provisional)** — boot-time read of the grid-stress → power-price leg.

```bash
python3 FORGE/tools/market-data/power_watch.py   # self-locating, any cwd
# rc 0 = quiet · 1 = emergency-class PJM posting(s) — REVIEW · 2 = fetch failure
```

Three reads, one verdict line:
1. **PJM emergency postings** — scrapes `https://emergencyprocedures.pjm.com/` (public, server-rendered; browser UA). Flag-not-fire: emergency-class types (EEA/Capacity Emergency/Load Shed/…) print REVIEW + rc=1; routine local transmission warnings are counted but don't trip. Never auto-declares a C3 event (AEOLUS/HENRY judgment).
2. **PJM hourly demand** — EIA-930 via new `fetch.eia_pjm_demand()` (route `electricity/rto/region-data`, respondent=PJM, type=D). UTC hour stamps; publishes ~2-6h behind real time.
3. **Retail price backdrop** — monthly US industrial+residential c/kWh via new `fetch.eia_retail_power_price()` (route `electricity/retail-sales`). **~2-month lag** — cite the month label, never call it current.

Client surface added to `fetch.py` (non-breaking; petroleum `eia_fetch()` untouched): generic `eia_fetch_facets(route, facets, …)` + the two wrappers above. All routes verified live 2026-07-10.

**The PJM-key wall:** actual LMPs (RT/DA prices) need PJM Data Miner 2 — free pjm.com account + subscription key, one-time human registration (6 calls/min non-member). Next increment once a key lands in `.env` as `PJM_API_KEY`. Alternative: gridstatus.io free tier (also signup-gated). Structural capacity-cost leg (BRA auctions: 26/27 cleared at the $329.17 cap, 27/28 at $333.44, 6,623 MW short) is annual-cadence via BRA PDFs, not this script.

## Citation Convention (CRITICAL — read before citing data)

**FRED data has a publication lag.** OAS series (HY, CCC, BBB), yields (DGS2, DGS10), spreads (T10Y2Y, T10YIE), and claims (ICSA, CCSA) are **end-of-day computed** and **publish T+1** — meaning at any point during a trading day, the latest data available from FRED is **yesterday's close at the earliest** (and on a weekend, Friday's). Yfinance prices (KRE, APO, etc.) are intraday-live; only FRED data has the lag.

**Standard cite format for FRED data:**

```
HY OAS 280bps [FRED 5/20 close]    ← preferred (explicit)
HY OAS 280bps [5/20]               ← shorthand acceptable in compact contexts
```

**Standard cite format for yfinance data:**

```
KRE $69.10 [yfinance live 13:45]   ← intraday timestamp
KRE $69.10                          ← timestamp implied current if no tag
```

**Rule:** Do NOT call a FRED-sourced number "live" or "today" without verifying the observation date matches today. The dashboard (`dashboard.py`) appends the observation date to every FRED row — propagate that date into your STATUS, HEARTBEAT, and analysis cites.

**Why this matters:** When numbers are within bps of a trigger or threshold (e.g., HY OAS approaching 260 kill or 290 R11 trigger), a 1-2 day lag changes whether the trigger is "almost firing" or "comfortably distant." Mis-stamped data has caused 4-agent convergence misalignment (5/21 incident — VIOLET KB-VIO-060).

**Per-series publication cadence (for interpretation):**
- **Daily T+1:** HY OAS, CCC OAS, BBB OAS, DGS2, DGS10, T10Y2Y, T10YIE, DCOILBRENTEU
- **Weekly:** ICSA + CCSA (Thursday AM, prior week), GASREGW (Monday AM, prior week)
- **Monthly:** PCE, CPI, PPI series

---

## Build Status

- [x] Layer 1: fetch.py (FRED + yfinance) — fixed price_fetch bug Mar 29
- [x] Layer 2: config.py (agent mapping + thresholds) — approved Mar 28
- [x] Layer 3: dashboard.py — ALL segments complete Mar 29
- [x] Layer 3 Segment 4: cron + Telegram auto-alerts — installed `*/5 * * * *`
- [ ] Tier 3 series added
- [ ] STATUS file auto-update
- [ ] server.py → config.py unification
