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

⚠️ **Open question:** Volume research (Tasks 1-4 complete) confirms thin-market rally — institutional distribution through AP redemption, not open-market selling. OZK has the cleanest put confirmation. WAL more ambiguous. KRE ETF structurally shrinking. Tasks 5-7 (dark pool, options vol, SI overlay) remain. Does the volume lens change Jun put management?

### CHANGES SINCE LAST SESSION
- **Prices (Apr 9 intraday):** KRE $69.71 (+4.4%), WAL $76.49 (+6.3%), OZK $47.97 (+2.9%), Brent $95.49 (-13.6% from $110.55). HY OAS 294bps (down from 305). Major oil de-escalation driving risk-on.
- **KRE shares outstanding:** 56.9M (confirmed SSGA Apr 8), down from ~65.0M on Mar 24 (-12.4%). Price up 6.8% in same window.

### LAST SESSION (Apr 9 — volume deep-dive with Will)
- **RP-REG-5.1 created:** `trade/market-microstructure/RP-REG-5.1_KRE_Volume_Analysis.md` — comprehensive volume analysis, Tasks 1-4.
- **Task 1 (name vs ETF):** KRE is least active name (0.85x 20d avg). All individual names above 1.0x. Volume migrating from ETF to single names. 90th percentile divergence, organic (not OpEx).
- **Task 2 (up/down volume):** All names have more volume on down days. OZK worst at 0.53x (selling days carry 2x volume). WAL recovered to 0.96x. Magnitude-weighted shows recent pops are thin-book short covering, not accumulation.
- **Task 3 (catalyst volume):** Selling is anticipatory (elevated D-2 before stress events). Buying is reactive (dead before relief, only picks up D+1/D+2 after). WAL-specific catalysts (downgrades, First Brands) got NO volume reaction. OZK dividend hike: stock fell on low volume.
- **Task 4 (ETF flows):** $670.8M single-week outflow Mar 3 (biggest in 4 years). KRE shares -12.4% in 2 weeks while price +6.8%. AP redemption confirmed. XLF getting +$1.22B/month inflows vs KRE -$8M — surgical regional de-risking.
- **Key insight for positions:** Single-name puts (WAL, OZK) are cleaner expressions than KRE puts in current regime. OZK has strongest distribution signal. Thin market amplifies moves in both directions — timing risk on Jun puts elevated.
- **Will pushed back on "all institutions left"** — correct, 12.4% reduction is significant but $3.9B still in fund. Many institutions remain. Overstated the conclusion.
- **Git:** Did NOT pull (BRENT, CARL, SAM had uncommitted changes). My files clean. Inbox empty.

### LAST SESSION (Apr 7 — full session, earnings prep)
- Inbox processed (7 signals). CALENDAR updated with full earnings wave. WAL/OZK earnings discussion. OZK prompts #8-10 integrated. EGBN research + EXTERNAL_PROMPTS created. OZK KB 159→175, EGBN KB 12→18.

### NEXT SESSION
1. **Complete volume research Tasks 5-7:** Dark pool %, options vol vs equity vol, short interest overlay. Full details in RP-REG-5.1.
2. **WAL position decision** — sell $85P Jun before earnings? Volume data adds urgency — thin market + ambiguous WAL profile. Lock by Apr 15.
3. **Integrate EGBN prompts** as Will completes them
4. **OZK SI refresh** (~Apr 14) — pair with Task 7 overlay
5. **OZK 8-K check** (~Apr 14) — EDGAR CIK 0001569650
6. **Read-through watchlist** for MTB (Apr 15), CFG (Apr 16), RF (Apr 17)
7. **EGBN earnings date** — confirm via IR page ~Apr 14

**Pending (carried forward):**
8. Cantor PACER docket
9. Vecchione return status
10. WAL insider refresh (by Apr 18)
11. OZK remaining prompts (#13 peer vintage, #19 metro conditions)
