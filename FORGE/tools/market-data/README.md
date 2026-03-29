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

## Build Status

- [ ] Layer 1: fetch.py (FRED + yfinance)
- [ ] Layer 2: config.py (agent mapping + thresholds)
- [ ] Layer 3: dashboard.py
- [ ] Tier 3 series added
- [ ] Cron automation
- [ ] STATUS file auto-update
