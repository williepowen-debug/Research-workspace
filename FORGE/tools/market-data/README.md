# Market Data Tools

**Purpose:** Automated data pulls for agent threshold monitoring and position tracking.

**Location:** `FORGE/tools/market-data/`

---

## ⛔ READ THIS BEFORE YOU PULL A FUTURES PRICE (2026-09-18)

**The generic continuous tickers `CL=F` and `BZ=F` report the price of one contract month under the
label of another, and a day-change computed ACROSS a roll. Cite a NAMED contract month.**

Reproduced live at 2026-09-18 17:5x ET by PROME (raised by HAWK the same morning, independently):

| Call | Price | Day change | Tool's own label |
|---|---|---|---|
| `CL=F` | $95.47 | **−6.32%** | *"Oct 2026 (CLV26)"* — ⛔ **FALSE** |
| `CLV26` (the real October) | $99.53 | −2.34% | Oct 2026 ✅ |
| `CLX26` (November) | $95.47 | −1.81% | Nov 2026 ✅ |
| `BZ=F` | $98.77 | **−5.77%** | *"UNKNOWN"* |
| `BZZ26` (December) | $98.77 | −1.16% | Dec 2026 ✅ |

`CL=F` is **byte-identical to `CLX26`** — same price, same volume 300,567 — while labelling itself
`CLV26`. Off by one contract month. The day-change then divides the NEW month's price by the OLD
month's prior close, which manufactures a move that did not happen: $95.47/$101.91−1 = −6.32%
against November's real −1.81%. **Two defects in one call: wrong contract attribution, and a
fabricated day-move. The prices are real prices — of a different month than the label claims.**

🔑 **The tell is a day-change several points larger than the named months on the same screen.**
It is loudest on a roll day and silent on every other day, so a clean-looking pull is not evidence
the label is right.

**What to do instead:** pull the named month (`CLV26`, `CLX26`, `BZZ26`, `BZX26`) and cite it by name.
Root rule #4 requires a live price; it does not excuse an unnamed contract. This is the same class
as the kill-on-sight entries in `HEARTBEAT.md` (⛔ *"`BZ=F` is the continuous series, contract
identity UNKNOWN to the tool"*) and the `-7.5% Brent in three sessions` artifact SAM withdrew and
then mechanized (`AGENTS/SAM/scripts/oil_roll_check.py`, 2026-09-18).

⚠️ **A registered line is keyed literally on `CL=F`** — BRENT's `MKT-CL-F-ABOVE-100`, which fired
2026-09-14. October expires ~2026-09-22, after which `CL=F` becomes November and the line would
silently change contracts. BRENT owns that line and has been packeted; PROME does not re-grade it.

⚠️ Smaller, same file: the tool prints `$` against non-USD listings (`LDO.MI` is euros,
`SAAB-B.ST` is krona). Check the listing currency before quoting a level.

**Owner + fix:** PROME (FORGE is PROME-owned). The repair is registered at `PROME/DOCKET.tsv` L409
(FORGE market-data vintage + fallback repair, 2026-09-24) — WQ-229 consequential class, so it gets
acceptance conditions written BEFORE the edit and an independent reader before anyone calls it
fixed. ⛔ **This banner is a stopgap, not the repair, and it does not close L409.**

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

## Power / Grid-Stress Instrument (power_watch.py → moved to AGENTS/WATT/)

Built by DAEDALUS 2026-07-10 (Will-approved Step-1 power instrument layer). **MOVED 2026-07-10 to `AGENTS/WATT/power_watch.py`** on the WATT spinout (Step-2): the **WATT** agent now owns the grid-stress → power-price leg (was HENRY-provisional). The **EIA client routes stay here in `fetch.py`** (shared); `power_watch.py` imports them by self-location from its new home. Run it from WATT:

```bash
python3 AGENTS/WATT/power_watch.py   # self-locating, any cwd (imports FORGE fetch.py)
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
