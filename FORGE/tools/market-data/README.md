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
