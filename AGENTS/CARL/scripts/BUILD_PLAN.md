# CARL Scripts Build Plan
**Created:** 2026-04-13
**Modeled on:** SAM/scripts/ and REGINALD/scripts/ architecture
**Status:** PLAN — not yet built

---

## ARCHITECTURE

Same pattern as SAM/REGINALD:
- Each script is standalone, pulls one data domain, writes to a TSV
- `boot.py` orchestrator runs them all in sequence
- Scripts use yfinance for market data, FRED API for economic series, web scraping for specific sources
- All output goes to `AGENTS/CARL/workbook/` TSVs or a new `AGENTS/CARL/scripts/data/` directory
- Exit codes captured by boot.py — failures don't stop the sequence

---

## SCRIPTS TO BUILD (ordered by value)

### 1. thresholds.py — Consumer Stress Threshold Monitor
**What:** Pull live prices/data for CARL's key indicators and compare against VX thresholds.
**Source:** yfinance + FRED API (via fredapi package)
**Writes to:** stdout (boot summary) + optional THRESHOLDS_LOG.tsv

```
MARKET TICKERS (yfinance):
- Gas proxy: UGA (US Gasoline Fund) or pull AAA via web scrape
- HY spreads: HYG price as proxy (inverse = stress)
- Consumer discretionary: XLY, XRT (retail ETF)
- SYF (Synchrony — CC canary)
- ALLY (auto lending canary)
- DFS (Discover — CC issuer)
- COF (Capital One)
- Homebuilders: LEN, DHI, TOL, PHM
- KRE (regional banks — cross-reference REGINALD)
- SPY, VIX (macro context)

FRED SERIES (fredapi):
- MORTGAGE30US — 30yr mortgage rate (weekly, Freddie PMMS)
- DCOILBRENTEU — Brent crude
- GASREGW — Regular gas price (weekly EIA)
- BAMLH0A0HYM2 — HY OAS spread (daily ICE BofA)
- PSAVERT — Personal savings rate (monthly)
- PCE — Core PCE (monthly)
- UNRATE — Unemployment rate (monthly)
- ICSA — Initial claims (weekly)
- CCSA — Continuing claims (weekly)
- JTSJOL — JOLTS openings (monthly)
- TOTALSL — Total student loan balance (quarterly)
- CCLACBW027SBOG — CC balances (weekly)
- DRCCLACBS — CC delinquency rate (quarterly)

THRESHOLDS (from CARL VX.tsv / CLAUDE.md):
- Gas national avg: $4.50 = next breakpoint (🔴)
- HY OAS: >350bps = stress (🔴), >300 = elevated (🟠)
- Mortgage 30yr: >6.5% = orange/red boundary, >7.0% = red
- Savings rate: <3% = red
- Initial claims: >250K = yellow
- Continuing claims: >1,900K = yellow, >2,000K = red
- SYF price: thesis canary (track direction)
```

**Priority:** HIGH — this is the single most valuable script

---

### 2. consumer_pulse.py — FRED Economic Series Monitor
**What:** Pull key consumer health series from FRED, compare to prior period, flag direction changes.
**Source:** FRED API
**Writes to:** workbook/CONSUMER_PULSE.tsv (append daily/weekly row with latest values)

```
SERIES TO TRACK:
- CC delinquency rate (DRCCLACBS) — quarterly
- Auto loan delinquency (DRCLACBS) — quarterly  
- Personal savings rate (PSAVERT) — monthly
- Real disposable personal income (DSPIC96) — monthly
- Retail sales (RSXFS) — monthly
- Consumer sentiment UMich (UMCSENT) — monthly
- Core PCE (PCEPILFE) — monthly
- CPI Food (CPIUFDNS) — monthly
- CPI Energy (CPIENGNS) — monthly
- Total consumer credit (TOTALNS) — monthly

Each row: Date | Series | Value | Prior | Change | MoM% | YoY% | Status
Status = GREEN/YELLOW/ORANGE/RED based on VX thresholds
```

**Priority:** HIGH — replaces manual web search for macro data

---

### 3. gas_tracker.py — AAA Gas Price Monitor
**What:** Scrape AAA gas prices (national + state level for FL, TX, CA).
**Source:** AAA gasprices website (gasprices.aaa.com) or GasBuddy API
**Writes to:** workbook/GAS_TRACKER.tsv

```
Fields: Date | National_Avg | FL | TX | CA | Diesel | Week_Chg | Month_Chg | Status
Status: GREEN (<$3.50) | YELLOW ($3.50-$4.00) | ORANGE ($4.00-$4.50) | RED (>$4.50)

Also track: days above $4 (behavioral breakpoint counter)
```

**Priority:** HIGH — gas is a live convergence vector, currently manual

---

### 4. catalyst_countdown.py — Trading Day Countdown
**What:** Read STATUS.md DANGER WINDOW table + TEAM.md catalysts, compute trading days to each.
**Source:** Parse local files, use pandas trading calendar
**Writes to:** stdout (boot summary)

```
Output format:
  🔴  1 TD  Apr 15  Sweet v. McMahon non-Exhibit C deadline
  🔴  1 TD  Apr 15  NAHB HMI April + MBA Apps
  🟠  5 TD  Apr 21  SYF Q1 earnings — CRL-12 test
  🟠  5 TD  Apr 21  DHI Q2 FY2026 earnings
  ...
```

**Priority:** MEDIUM — useful but not data-pulling

---

### 5. abs_monitor.py — ABS Trust EDGAR Monitor
**What:** Query EDGAR for new 10-D filings from tracked ABS trusts (SDART, HAROT, DFS, COF).
**Source:** SEC EDGAR company filings API
**Writes to:** workbook/ABS_FILINGS.tsv + alerts on threshold breaches

```
TRUSTS TO MONITOR:
- SDART 2023-2, 2024-1, 2024-3, 2024-5, 2025-1 (Santander subprime auto)
- HAROT 2024-1, 2024-3 (Honda prime auto — control)
- DCENT / DCMT (Discover CC trusts)
- Capital One CC trusts

Each 10-D has EX-99.1 (servicer certificate) with:
- Monthly net loss rate
- Cumulative net loss
- 30/60/90+ DQ rates
- Payment rate
- Pool factor

Script checks for new filings, downloads EX-99.1, extracts key metrics,
compares to ABS_BASELINE.tsv thresholds, flags breaches.
```

**Priority:** MEDIUM-HIGH — fills a persistent gap, but EDGAR parsing is complex

---

### 6. housing_pulse.py — Housing Data Monitor
**What:** Pull housing-related FRED series and check Fannie/Freddie websites for MF DQ updates.
**Source:** FRED API + web scrape fanniemae.com monthly summary
**Writes to:** workbook/HOUSING_PULSE.tsv

```
FRED SERIES:
- MORTGAGE30US — 30yr rate
- HOUST — Housing starts
- PERMIT — Building permits
- EXHOSLUSM495S — Existing home sales
- HSN1F — New home sales
- MSPUS — Median home price
- CSUSHPINSA — Case-Shiller national

WEB SCRAPE:
- Fannie Mae monthly summary page → MF serious DQ rate
- MBA weekly apps (press release scrape)

Each row: Date | Series | Value | Prior | Change | Status
```

**Priority:** MEDIUM — many series are monthly/quarterly so less urgent than daily feeds

---

### 7. boot.py — Master Orchestrator
**What:** Run all CARL scripts in sequence, capture results, print consolidated boot brief.
**Pattern:** Identical to SAM/REGINALD boot.py

```
BOOT SEQUENCE:
1. thresholds.py      — live market + FRED thresholds
2. gas_tracker.py     — AAA gas prices
3. consumer_pulse.py  — FRED consumer series
4. housing_pulse.py   — FRED housing + Fannie MF check
5. catalyst_countdown.py — upcoming catalysts
6. abs_monitor.py     — EDGAR ABS filings (--skip-slow to skip)

FLAGS:
  --quick    skip EDGAR + housing web scrape
  --verbose  show full script output
```

**Priority:** Build LAST (after individual scripts work)

---

## DEPENDENCIES

```
# Already in .venv:
yfinance    — market data (SAM/REGINALD already use)

# Need to install:
fredapi     — FRED economic data (pip install fredapi)
              Requires free API key from fred.stlouisfed.org

# Already available:
requests    — web scraping
beautifulsoup4 — HTML parsing (for AAA, Fannie scrapes)
```

**FRED API Key:** Free from https://fred.stlouisfed.org/docs/api/api_key.html
Store in `.env` file or `AGENTS/CARL/scripts/.fred_api_key`

---

## BUILD ORDER

| Phase | Script | Est. Effort | Dependencies |
|-------|--------|-------------|--------------|
| 1 | thresholds.py | ~30 min | yfinance (installed), fredapi (install + key) |
| 2 | gas_tracker.py | ~20 min | requests, bs4 |
| 3 | consumer_pulse.py | ~30 min | fredapi |
| 4 | catalyst_countdown.py | ~15 min | none (reads local files) |
| 5 | housing_pulse.py | ~30 min | fredapi + web scrape |
| 6 | abs_monitor.py | ~45 min | EDGAR API (complex parsing) |
| 7 | boot.py | ~20 min | all above working |

**Total estimate:** ~3 hours across 1-2 sessions.

---

## INTEGRATION WITH CARL BOOT SEQUENCE

Once built, CARL's CLAUDE.md boot step changes from:
```
7. (manual web search for stale dashboard values)
```
to:
```
7. Run: .venv/bin/python3 AGENTS/CARL/scripts/boot.py
   Read output for threshold breaches and stale data alerts.
```

Sub-agent spawns become TARGETED — only spawn STUE/HOMER when boot.py flags something stale or breached, not for routine data pulls.

---

## NOTES

- SAM's scripts are the cleanest reference — start by copying thresholds.py structure
- REGINALD's boot.py has the --skip-slow pattern which CARL should adopt for EDGAR
- All scripts should be idempotent (safe to run multiple times)
- TSV append pattern: check if today's row exists before writing (SAM's _has_today_row)
- Error handling: print error, return non-zero exit code, don't crash boot sequence
