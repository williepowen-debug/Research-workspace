> **COMPLETE 2026-07-09** (not FROZEN — plan was fully executed) — all 8 scripts + `boot.py` orchestrator described below exist and are now wired into CLAUDE.md boot sequence (step 7b, 2026-07-09). Kept for historical build-rationale reference, not a live TODO.

# REGINALD Automation Plan
**Created:** 2026-04-09 | **Status:** APPROVED — execute in next session

---

## Overview

Build a complete automated monitoring toolkit for REGINALD. Eight scripts, executed in priority order. Each script is standalone, testable, and appends to workbook TSVs where applicable. The final deliverable is `boot.py` which orchestrates everything into a single morning brief.

All scripts live in `AGENTS/REGINALD/scripts/`. All use the workspace `.venv/bin/python3`. No external API keys required (except FRED, noted as optional).

---

## Build Order (priority sequence)

### Phase 1 — Core monitoring (build first)

**1. thresholds.py** *(~10 min)*
- Pulls live prices via yfinance for all thesis tickers
- Compares against hardcoded thresholds from STATUS.md:
  - KRE <$60 (acute stress), WAL <$78 (hidden CRE accelerating), HY OAS >320 (credit confirmed)
  - OZK <$40 (crisis), EGBN <$22 (capital raise territory)
  - Brent >$120 (stagflation), Claims >300K (employment break)
- Prints only breaches and "within 5%" warnings
- No TSV — just console output at boot

**2. insider.py** *(~15 min)*
- Queries SEC EDGAR full-text search API (efts.sec.gov) for Form 4 filings
- Tickers: WAL (CIK 1564196), OZK (CIK 1569650), EGBN (CIK 827809)
- Filters for filings in last 14 days
- Parses for transaction type — flags OPEN MARKET PURCHASES (code P)
- Ignores RSU settlements (code F), tax withholdings (code M), awards (code A)
- Prints summary: "WAL: 3 filings, all RSU settlements. No open market buys."
- CRITICAL before earnings — any insider buying is a thesis challenge signal

**3. kre_float.py** *(~10 min)*
- Scrapes SSGA KRE fund page for current shares outstanding and AUM
- Compares to last known value (stored in a small state file or DARKPOOL.tsv)
- Prints: "KRE shares: 56.9M (unchanged from Apr 8)" or "KRE shares: 54.2M (DOWN 4.7% from 56.9M)"
- The -12.4% shrinkage was a key Task 4 finding — this automates ongoing detection

### Phase 2 — Enrichment (build second)

**4. options_oi.py** *(~20 min)*
- Pulls options chains via yfinance for WAL, OZK, EGBN, KRE
- Focuses on near-term + Jun expiries
- Computes: total put OI, total call OI, P/C ratio, top 5 put strikes by OI
- Appends snapshot to `workbook/OPTIONS_OI.tsv` (new file)
- Schema: Date | Ticker | Expiry | Total_Put_OI | Total_Call_OI | PC_Ratio | Top_Strike | Top_OI
- Run weekly (not daily — OI changes slowly)
- Detects: new large put positions building (like Peak6's $15M bet)

**5. si_refresh.py** *(~15 min)*
- Scrapes Benzinga or finviz for current short interest data
- Tickers: WAL, OZK, EGBN, KRE, ZION, CFG
- Appends to `workbook/SHORT_INTEREST.tsv` if data is newer than last entry
- Prints: "OZK SI: 15.28% (unchanged)" or "OZK SI: 16.1% (UP from 15.28%)"
- Run at boot — will only append when new bi-monthly data drops

**6. 8k_monitor.py** *(~15 min)*
- Queries SEC EDGAR for new 8-K filings from WAL and OZK
- CIKs: WAL 1564196, OZK 1569650
- Checks for filings in last 7 days
- Prints filing date, type, and description
- Would catch: surprise credit events, management changes, capital raises, dividend changes

### Phase 3 — Orchestration (build last)

**7. earnings_countdown.py** *(~10 min)*
- Reads CALENDAR.md (or hardcoded dates)
- Prints days until each thesis-name earnings date
- Flags anything within 5 trading days with ⚠️
- Simple but prevents calendar drift

**8. boot.py** *(~15 min)*
- Master orchestrator — runs all of the above in sequence:
  1. market.py (prices)
  2. darkpool.py (off-exchange % + short volume)
  3. thresholds.py (breach alerts)
  4. insider.py (Form 4 check)
  5. kre_float.py (ETF shrinkage)
  6. si_refresh.py (short interest)
  7. earnings_countdown.py (calendar)
- Prints consolidated output with section headers
- Suppresses verbose output — summary only
- Single command: `.venv/bin/python3 AGENTS/REGINALD/scripts/boot.py`
- Replaces the 6-step manual boot sequence in CLAUDE.md

---

## Existing (already built)

| Script | Status | Purpose |
|--------|--------|---------|
| `scripts/darkpool.py` | ✅ DONE | Off-exchange % + short volume, appends to TSVs |
| `../../scripts/market.py` | ✅ EXISTS | Price watchlist (shared, workspace root) |

---

## Estimated Total Build Time

| Phase | Scripts | Est. Time |
|-------|---------|-----------|
| Phase 1 | thresholds, insider, kre_float | ~35 min |
| Phase 2 | options_oi, si_refresh, 8k_monitor | ~50 min |
| Phase 3 | earnings_countdown, boot.py | ~25 min |
| **Total** | **8 scripts** | **~110 min** |

---

## Execution Notes

- Build and TEST each script individually before moving to the next
- After each script works, commit it
- boot.py is last because it depends on all others existing
- After boot.py works, update CLAUDE.md boot sequence to reference it
- All scripts should fail gracefully (network errors, missing data) — print warning and continue, never crash the boot sequence
