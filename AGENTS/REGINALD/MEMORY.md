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

⚠️ **Open question:** OZK + WAL reporting same day (Apr 21) — need to finalize all position decisions BEFORE print. ZION (Apr 20) is only leading indicator now.

### CHANGES SINCE LAST SESSION
- **Prices (Apr 4):** WAL $72.07 (-0.43%), OZK $46.31 (+0.30%), KRE $66.00, Brent $111.60, VIX 23.87, APO $107.04 (-2.91%)
- **3 inbox signals** unprocessed (CARL FL pincer, CARL SYF canary, sweep Apr 3)

### LAST SESSION (Apr 5 — short session)
- **First Brands auction RESOLVED:** Piecemeal liquidation confirmed. $75M total recovery vs $9.3B debt (<1%). Debt 30-47¢. $2.3B fabricated receivables. WAL $126.4M likely unrecoverable — Q1 earnings catalyst. Updated FIRST_BRANDS.md with full auction results, recovery math, WAL V2 impact.
- **OZK earnings date CHANGED:** Apr 16 → Apr 21 (GlobeNewswire Mar 31). OZK and WAL now report SAME DAY. Rewrote EARNINGS_PREP.md WAL read-through section — no more 5-day tactical window. ZION (Apr 20) is the only pre-print sector read.
- **OZK consensus EPS filled:** $1.52 (Zacks Feb 2026 revision, down from $1.58). FY2026 $6.02. Beat/miss: >$1.55 = beat, <$1.48 = miss.
- **Files updated:** CALENDAR.md, STATUS.md, OZK/STATUS.md, OZK/EARNINGS_PREP.md, WAL/FRAUD/FIRST_BRANDS.md, MEMORY.md

### LAST SESSION (Apr 2 — full afternoon session, ~3 hours)
- Architecture overhaul (11 improvements), STATUS.md trimmed, POSITIONS.md created, 2 inbox signals processed, live prices refreshed

### NEXT SESSION
1. OZK earnings prep remaining gaps — SI refresh, 8-K watch, Bioterra status, SCENARIOS.md recalibration
2. WAL earnings prep — 16 days, same-day as OZK now. Pre-print position decisions critical.
3. Process 3 inbox signals (CARL FL pincer, CARL SYF canary, sweep Apr 3)
4. Cantor PACER docket — still pending
5. Vecchione return status — still pending
6. MI3 peer comparison — still pending
