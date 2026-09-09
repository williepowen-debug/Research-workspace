# BRENT Scripts Build Plan

> **HISTORICAL April 16 plan — reviewed September 8, 2026. Not a current implementation or threshold specification.** FRED returns “series does not exist” for the advertised `BAMLH0A0E2Y`; broad HY is not upstream E&P OAS. The planned continuous-futures crack construction does not establish matched delivery months. Runtime truth is `boot.py` and `workbook/REGISTRY.tsv`, not the checkmarks, old thresholds, credential advice or calendar examples below. Original plan retained as history; [verification and recovered diagnostic](../research/2026-09-08_batch2/REPORT.md).

**Created:** 2026-04-16
**Modeled on:** SAM/scripts/, CARL/scripts/, REGINALD/scripts/
**Status:** PHASE 1 IN PROGRESS

---

## ARCHITECTURE

Same pattern as SAM / CARL / REGINALD:
- Each script is standalone, pulls one data domain, prints to stdout (+ optional TSV append)
- `boot.py` orchestrator runs them in sequence, collapses output to alerts only
- Market data via `yfinance`; economic data via FRED API (urllib, no `fredapi` dep)
- Scrapes only where no API exists (AAA retail gas, Baker Hughes rigs, Baltic Exchange)
- Output data to `AGENTS/BRENT/scripts/data/` TSVs

---

## BRENT's MANUAL PAIN POINTS (what to automate)

| # | Task | Current | Automate? | Frequency |
|---|------|---------|-----------|-----------|
| 1 | Brent/WTI spot + futures | FORGE fetch.py | ✅ via yfinance BZ=F CL=F | Session |
| 2 | Dated Brent (physical) | Manual search | ✅ FRED DCOILBRENTEU | Session |
| 3 | USO / STNG / CVX / XOM marks | Manual | ✅ yfinance | Session |
| 4 | Crack spreads (3-2-1) | Manual calc | ✅ BZ=F, RB=F, HO=F | Session |
| 5 | EIA weekly (stocks, util, Cushing, SPR) | Manual scrape | ✅ EIA API | Weekly Wed |
| 6 | Baker Hughes rig count | Manual | ✅ scrape | Weekly Fri |
| 7 | CFTC NYMEX positioning | Manual | ✅ CFTC CSV | Weekly Fri |
| 8 | VLCC / LR2 / MR rates | Manual | 🟡 no free API — use STNG/FRO/EURN as proxy | Weekly |
| 9 | JKM / TTF LNG spot | Manual | 🟡 scrape (fragile) | Weekly |
| 10 | Retail gas (AAA) | Cross-ref CARL | ⏩ CARL owns this | Daily |
| 11 | HY energy OAS | Manual | ✅ FRED BAMLH0A0E2Y | Weekly |
| 12 | OPEC+ / EIA / earnings countdown | Eyeball TIMELINE | ✅ parse CATALYSTS.tsv | Session |
| 13 | Threshold diff vs STATUS | Mental | ✅ thresholds.py | Session |

**Items 1–7, 11–13: deterministic → automate.**
**Items 8–9: fragile scrapes, acceptable to defer or partial.**
**Item 10: CARL owns it; BRENT consumes via cross-ref.**

---

## SCRIPT PRIORITY

### Phase 1 — CORE (build this session)
| # | Script | Purpose | Effort |
|---|--------|---------|--------|
| 1 | `thresholds.py` | yfinance + FRED diff vs BRENT thresholds | HIGH value, ~30 min |
| 2 | `eia_weekly.py` | EIA API: crude/gas/distillate stocks, Cushing, SPR, util | HIGH value, ~30 min |
| 3 | `catalyst_countdown.py` | Trading days to EIA/BH/OPEC/earnings | MED, ~15 min |
| 4 | `boot.py` | Orchestrator — direct port of SAM's | LAST, ~20 min |

### Phase 2 — EXTEND (next session)
| # | Script | Purpose |
|---|--------|---------|
| 5 | `crack_spreads.py` | Calc 3-2-1 from BZ=F / RB=F / HO=F |
| 6 | `cftc_nymex.py` | CFTC COT report, NYMEX crude net longs |
| 7 | `rig_count.py` | Baker Hughes Friday scrape |
| 8 | `tanker_rates.py` | STNG/FRO/EURN proxies + Baltic scrape |
| 9 | `lng_prices.py` | JKM / TTF scrape (fragile) |

---

## BRENT THRESHOLDS (Phase 1 thresholds.py)

### Market (yfinance)
```
BZ=F (Brent futures):
  >$120 = risk (demand destruction territory)
  >$100 = stress (HAWK Scenario C confirmation)
  <$75  = thesis-break (squeeze failed)
CL=F (WTI futures):
  >$100 = stress
USO:
  <$80  = monitor (position drawdown)
  <$75  = stop territory
STNG:
  <$71.50 = stop loss
  >$100   = target zone
LNG (Cheniere):
  >$255  = in position
  >$285  = analyst PT range
```

### FRED
```
DCOILBRENTEU (Dated Brent):
  >$140 = extreme (we hit ATH $144 intraweek)
  >$120 = stress
BAMLH0A0E2Y (HY Energy OAS):
  >400bps = energy credit stress emerging
  >300bps = elevated (currently ~300)
DHHNGSP (Henry Hub natgas):
  context only
DCOILWTICO (WTI spot):
  context
GASREGW (retail gas, CARL primary):
  reference only — CARL owns
```

### Storage / operational (EIA)
Tracked in `eia_weekly.py` not thresholds.py (different cadence).
```
Cushing < 20M bbl = operational minimum, WTI dislocation risk
SPR < 400M = near SPR floor
Gasoline stocks YoY -5% = demand destruction confirm
Refinery util > 95% = crack spread squeeze
```

---

## EIA API (Phase 1 eia_weekly.py)

**Source:** https://api.eia.gov/v2/petroleum/
**API key:** Register free at eia.gov/opendata. Store in env var `EIA_API_KEY`.

### Series to pull
```
WCESTUS1  — Weekly US crude stocks (excl SPR)
WCESTP31  — Cushing stocks
WTTSTUS1  — Total crude stocks (incl SPR)
WCRSTUS1  — SPR stocks
WGTSTUS1  — Total gasoline stocks
WDISTUS1  — Distillate stocks
WPULEUS3  — Refinery utilization %
WGFUPUS2  — Finished gasoline product supplied (implied demand)
WDIUPUS2  — Distillate product supplied
WTTIMUS2  — Total crude imports
WTTEXUS2  — Total crude exports
```

Each row: Date | Series | Value | Prior | WoW_Chg | YoY_Chg | Status

---

## CATALYSTS.tsv (Phase 1 catalyst_countdown.py)

Create `AGENTS/BRENT/workbook/CATALYSTS.tsv` with columns matching SAM:
```
date	event	what_to_check	threshold_signal	priority	who_cares	notes
2026-04-22	EIA Weekly	Gasoline stocks + util + Cushing	Gas YoY <-5% = Path B	🔴	BRENT,CARL	First EIA under blockade regime
2026-04-25	Baker Hughes	Total rigs	>595 = shale response	🟠	BRENT	SIG-009 lag watch
2026-04-25	CFTC COT	NYMEX NC net longs	Decline 2nd wk = Path B signal	🟠	BRENT	
2026-04-28	Cheniere Q1	EPS vs $3.15 cons	Beat $5+ = LNG thesis	🟠	BRENT,SAM	BRT-10 validation
2026-05-01	BOJ Meeting	Rate decision	Hike → carry unwind → brief oil selloff	🟠	SAM,BRENT	Cross-agent
2026-06-07	OPEC+ Meeting	3.24 mbpd unwind trigger	If Hormuz open = flood	🔴	BRENT,ALL	BRT-11 trigger
```

---

## DEPENDENCIES

Already available in `.venv/`:
- `yfinance` 1.2.0
- `urllib.request`, `json` (stdlib)
- `pandas`, `beautifulsoup4`, `requests`

Need to install:
- NONE — reuse urllib for FRED/EIA, skip fredapi dep

Env vars needed:
- `FRED_API_KEY` — already hard-coded in CARL scripts (same key reused)
- `EIA_API_KEY` — register free; store in shell profile or hardcode

---

## BOOT SEQUENCE (Phase 1)

```
1. thresholds.py         — live prices + FRED diff vs BRENT levels
2. eia_weekly.py         — latest EIA petroleum status
3. catalyst_countdown.py — next events in trading days
```

Usage:
```
.venv/bin/python3 AGENTS/BRENT/scripts/boot.py
.venv/bin/python3 AGENTS/BRENT/scripts/boot.py --quick     # skip slow fetches
.venv/bin/python3 AGENTS/BRENT/scripts/boot.py --verbose   # full output
```

---

## INTEGRATION WITH BRENT BOOT SEQUENCE

Once built, BRENT's CLAUDE.md spawn protocol step 4 changes from:
```
4. Use web_search for latest developments — oil moves fast
```
to:
```
4. Run: .venv/bin/python3 AGENTS/BRENT/scripts/boot.py
   Read output for threshold breaches, EIA changes, catalyst proximity.
   Web search only for headline/narrative catalysts not in structured data.
```

---

## NOTES

- SAM's `thresholds.py` is the cleanest reference structure — port directly
- CARL's `thresholds.py` has the FRED integration pattern — copy that
- All scripts idempotent (safe to re-run)
- Failures in any one script don't halt `boot.py` sequence
- TSV append pattern from SAM: check if today's row exists first
