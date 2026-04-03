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

⚠️ **Open question:** First Brands auction result (Mar 31) still unknown — affects BROCK/OTTO T-15 chain and WAL V2 vector

### CHANGES SINCE LAST SESSION
- [Populated at boot from market.py + inbox scan — what moved while REGINALD was offline]

### LAST SESSION (Apr 2 — full afternoon session, ~3 hours)
- **Architecture overhaul** — 11 total improvements to REGINALD infrastructure:
  1. OZK/WAL research sections moved out of STATUS.md → bank-specific STATUS files
  2. Open question format added (now in MEMORY.md)
  3. Price refresh step added to boot (market.py, yfinance installed)
  4. Inbox scan step added to boot
  5. CHANGELOG rule enforced for thesis/timeline edits
  6. Doc ownership table added to CLAUDE.md (10 docs mapped)
  7. CALENDAR.md created (earnings wave, Call Reports, AOCI, predictions, options expiry)
  8. MEMORY.md created (this file — replaces LAST_COMPLETION.md)
  9. Boot sequence reordered with Boot/Execute/Write-back sections
  10. Branch point table added to thesis/TIMELINE.md (13 events)
  11. Session close checklist added to CLAUDE.md
- **STATUS.md trimmed** 178 → 147 lines, now a pure dashboard
- **POSITIONS.md created** from broker screenshot — thesis positions only
- **2 inbox signals processed** (CARL SYF subprime canary, CRE fraud/insurance trifecta)
- **PROME/SCRATCH.md updated** to Apr 2
- **Live prices:** WAL $72.09 (+6% from $68), KRE $65.83, OZK $46.25, WTI $111.40 (+11.3%)
- **OWL $9.5P:** Decision was hold-to-expiry (Mar 29). Will confirmed still in portfolio — check auto-exercise.
- **Treasury meeting (Apr 1):** No outcomes documented. Gap.

### NEXT SESSION
1. First Brands auction result — still unknown, affects BROCK/OTTO T-15 and WAL V2
2. OZK earnings prep — 14 days, consensus EPS gap still open
3. WAL earnings prep — 19 days, EARNINGS_PREP at A-
4. Cantor PACER docket — still pending
5. Vecchione return status — still pending
6. MI3 peer comparison — still pending
