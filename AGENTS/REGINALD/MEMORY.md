# REGINALD MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

---

## Feedback
- [2026-04-02] Will values boot transparency — wants to know what REGINALD read, in what order, and whether the process is working. Don't orient silently; confirm orientation.
- [2026-04-02] Will prefers sessions to have freedom rather than being laser-focused on pre-set priorities. Provide context, not directives. Rejected ranked TOP 3 queue in favor of a single "open question."
- [2026-04-02] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-02] Will wants position data stored in REGINALD's domain (POSITIONS.md), not just FORGE. "That was just for you."
- [2026-04-02] Will prefers breaking large implementation work into discrete tasks done one at a time, with approval between each.

## Findings
- [2026-04-02] `scripts/market.py` pulls live prices via yfinance. Watchlist covers all thesis tickers + Brent (BZ=F). Must run with `.venv/bin/python3`. Added to boot step 5.
- [2026-04-02] FRED API key not configured — HY OAS, claims, and other FRED series at boot require `FRED_API_KEY` env var. Low priority but would close data gap.
- [2026-04-02] OZK price sources can conflict ($46 vs $49 in same session) — always verify at broker when discrepancy >5%.
- [2026-04-02] SAM's architecture is the best-organized agent. All key patterns now adopted: doc ownership rules, CALENDAR.md, MEMORY.md, branch point table in TIMELINE.md, session close checklist.
- [2026-04-02] PROME's SCRATCH.md is useful for system-wide context at boot — but REGINALD should not routinely read it. Only check if cross-agent context is needed.
- [2026-04-02] Inbox signals from HERMES can lag behind STATUS.md — check for staleness before processing.

## References
- [2026-04-02] FRED API key signup: https://fred.stlouisfed.org/docs/api/api_key.html
- [2026-04-02] EDGAR CIK for OZK: 0001569650 (for 8-K monitoring)

## Session Notes

⚠️ **Open question:** Three banks report in 2 weeks (ZION Apr 20, OZK+WAL Apr 21, EGBN ~Apr 22). Position decisions for all four need to be locked before ZION prints. EGBN earnings prep is grade C — needs significant research to get to A-.

### CHANGES SINCE LAST SESSION
*(leave blank — next boot populates via market.py)*

### LAST SESSION (Apr 6-7 — afternoon session)
- **Inbox processed (3 signals):** CARL FL Pincer (🔴), CARL SYF Canary (🟠), News Sweep (mixed). All moved to inbox/processed/. STATUS updated with 2 new indicators (SYF NCO, FL UI Exhaustion). CALENDAR updated with 3 new dates (SYF 8-K mid-Apr, FL UI Wave 1 Jun 24, Wave 2 Jul 26).
- **Workbook updated:** VX-REG-19.02 updated (FL UI multi-wave). VX-REG-20.01 added (SYF NCO canary). ML-REG-139 + ML-REG-140 added to KB.
- **EGBN/ subdirectory BUILT:** Full architecture matching WAL/OZK template — INDEX, STATUS, THESIS ("Crisis-in-Progress"), SCENARIOS (Bear 45%/Base 35%/Bull 20%), WEAKNESSES (7 identified), EARNINGS_PREP (grade C), workbook/KB.tsv (12 rows, 4 groups), workbook/KB_INDEX.md.
- **STATUS prices refreshed** via market.py. Brent $110.60, 10Y 4.33% (down from 4.42%), KRE $66.19, WAL $72.74 (still below $78).
- **Files created:** EGBN/INDEX.md, STATUS.md, THESIS.md, SCENARIOS.md, WEAKNESSES.md, EARNINGS_PREP.md, workbook/KB.tsv, workbook/KB_INDEX.md
- **Files updated:** STATUS.md (+EGBN section, +2 indicators, prices), CALENDAR.md (+3 dates), workbook/VX.tsv (+1 row, 1 updated), workbook/KB.tsv (+2 rows)

### LAST SESSION (Apr 5 — short session)
- First Brands auction RESOLVED. OZK date changed Apr 16→21. OZK consensus EPS filled.

### NEXT SESSION — RESEARCH GAPS
**EGBN (highest priority — grade C, needs to reach B+ before earnings):**
1. Q4 2025 10-K / earnings transcript — direct source read (no primary source read done yet)
2. Exact earnings date confirmation
3. Insider activity scan (Form 4)
4. Leadership profile (board, audit committee, CEO search status)
5. GovCon book composition — size, client profile, DOGE exposure
6. DC office vacancy Q1 data (CBRE/JLL)
7. MI3 trend direction (23.7% — stable or moving?)
8. Consensus estimates (EPS, revenue)
9. AUB relative trade analysis
10. AOCI exposure detail

**OZK (gap closure before Apr 21):**
11. SI refresh, 8-K watch, Bioterra status
12. SCENARIOS.md recalibration

**WAL (gap closure before Apr 21):**
13. Pre-print position decisions — all 4 strikes need plan
14. Updated insider filings refresh (by Apr 18)

**Pending (carried forward):**
15. Cantor PACER docket
16. Vecchione return status
17. MI3 peer comparison
