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

⚠️ **Open question:** WAL may report as early as Apr 16 (unconfirmed). Consider selling $85P Jun before earnings — deep ITM, captures current value, avoids bounce risk on clean quarter. Structural thesis resolves over months (Call Reports May, Investor Day May 12), not one earnings print.

### CHANGES SINCE LAST SESSION
*(leave blank — next boot populates via market.py)*

### LAST SESSION (Apr 7 — full session, earnings prep)
- **Inbox processed (7 signals):** 2 CARL (already integrated, move failed last session), 5 new (WAL deep dive, CRE refi wall, PC meltdown, WAL litigation, news sweep). Key new insight: Pathward +189bps CRE reserves while industry -12bps. All moved to inbox/processed/.
- **Outbox cleared:** JEF_WAL_V2_SYNTHESIS confirmed delivered by HERMES (PROME confirmed). Moved to outbox/delivered/. Flagged HERMES should move files post-delivery.
- **CALENDAR updated:** Full Q1 earnings calendar added (MTB Apr 15, KEY+CFG Apr 16, RF Apr 17, WAL Apr 16-21 UNCONFIRMED, OZK Apr 21, EGBN ~Apr 22-25). WAL date uncertainty = must be ready by Apr 16.
- **WAL earnings discussion:** 55% prob meets/beats headline. Thesis is in the DETAIL (MI3, Cantor, OREO), not the headline EPS. Jun puts vulnerable to relief rally + IV crush. Consider selling $85P Jun before earnings, holding Sep puts for structural catalysts.
- **OZK gap closure (5 items):** EDGAR 8-K check (none), Bioterra COMPLETE no tenants, SI unchanged (13.81%), IQHQ RaDD still 3.3% lab, SCENARIOS price refresh ($46.44). Grade A-.
- **OZK Prompt #8 (Metropolitan):** 3 LLM versions integrated. KB-161→164. Met Cap failed at MI3 39.6%. MCB active at 39.6% with zero NCOs = masking. Reserve inversion -2bps confirmed.
- **OZK Prompt #9 (Affinius):** 2 LLM versions. ⚠️ MAJOR CORRECTION: Affinius has NO public bonds (private RIA). "81¢" reference was WRONG. Affinius in expansion ($3.4B Veris, $61B AUM). 8 OZK co-lending deals, zero defaults. Columbus Center $69M foreclosure = isolated office walk-away. KB-165→170.
- **OZK Prompt #10 (Sell-side):** 5B/5H/1S, avg PT $57.22. UBS Neutral $48 today. Citi SELL $40 + Mar 23 catalyst watch. Institutions ADDING (Millennium +20%, Mackenzie +17%). KB-171→175.
- **EGBN web research:** Q4 beat ($0.25 vs -$0.12 est). CEO Riel retiring. Zero insider buying. 0B/2H/0S thin coverage. GovCon "no pressure" as of Oct 2025 (pre-DOGE Q1). KB-013→018. Grade C→C+.
- **EGBN EXTERNAL_PROMPTS.md created:** 5 prompts (#1 Q4 call deep dive, #2 DC CRE conditions, #3 sell-side+M&A, #4 GovCon/DOGE, #5 MI3+AOCI).
- **OZK KB:** 159→175 rows (16 added). New group: FAILURE_COMP, AFFINIUS, SELLSIDE.
- **EGBN KB:** 12→18 rows (6 added).
- **Files updated:** STATUS.md (prices, EOD summary), CALENDAR.md (full earnings calendar), OZK/STATUS.md, OZK/EARNINGS_PREP.md, OZK/SCENARIOS.md, OZK/EXTERNAL_PROMPTS.md, EGBN/STATUS.md, EGBN/EXTERNAL_PROMPTS.md (created)

### LAST SESSION (Apr 6-7 — afternoon)
- Inbox processed (3 CARL signals). EGBN/ subdirectory BUILT. STATUS prices refreshed.

### NEXT SESSION
1. **Integrate EGBN prompts** as Will completes them (#1 most important — Q4 call transcript)
2. **WAL position decision** — sell $85P Jun before earnings? Lock by Apr 15 if WAL reports Apr 16.
3. **OZK SI refresh** (~Apr 14) — pull FINRA/Ortex
4. **OZK 8-K check** (~Apr 14) — EDGAR CIK 0001569650
5. **Read-through watchlist** — lightweight "what to watch" for MTB (Apr 15), CFG (Apr 16), RF (Apr 17)
6. **EGBN earnings date** — confirm via IR page ~Apr 14
7. **OZK remaining prompts** (#13 peer vintage, #19 metro conditions) — low priority

**Pending (carried forward):**
8. Cantor PACER docket
9. Vecchione return status
10. WAL insider refresh (by Apr 18)
