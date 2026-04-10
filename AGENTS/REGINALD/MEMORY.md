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

⚠️ **Open question:** EGBN continuity awards (Mar 16) signal either FDIC-resolution prep, distressed restructuring, or pure leadership-vacuum retention. Microstructure (10.34x P/C, Jun $5P at 1,301 OI, dark pool +8.8pp) leans toward failure-pricing. Need to confirm Riel family relationship and pull Q4 10-K for DOGE commentary before Apr 22-25 earnings to size correctly.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py + darkpool.py)*

### LAST SESSION (Apr 10 — automation toolkit + EGBN deep-dive)
- **AUTOMATION TOOLKIT BUILT (8 scripts, 30s boot):** thresholds.py, insider.py, kre_float.py, options_oi.py, si_refresh.py, 8k_monitor.py, earnings_countdown.py, boot.py. All standalone-testable. Plan in scripts/AUTOMATION_PLAN.md fully executed. boot.py replaces manual boot sequence.
- **Key finding from boot.py output:** WAL breached $78 threshold ($76.75 close). KRE float 54.05M (-5% from 56.9M Mar peak — AP redemption persistent). VIX -24% on the rally day. EGBN dark pool 41.7% (+8.8pp) — biggest delta of any thesis name. EGBN P/C 10.34x — extreme.
- **EGBN DEEP-DIVE TRIGGERED:** Mar 18 8-K (event Mar 16) disclosed Continuity Awards: CFO Newell $425K cash + $100K RSU, Evelyn Lee $325K + $100K, Ryan Riel $425K + $100K. Total ~$1.475M cash + $300K equity. 15-month retention through Jun 30 2027. Filing language: "given Ms. Riel's previously announced intention to retire and the ongoing search for her successor." Logged as ML-REG-139.
- **Riel/Riel name overlap noted** — CEO Susan Riel and named exec Ryan A. Riel. Family connection at distressed bank = governance flag. Not yet confirmed from 8-K alone — need proxy/10-K.
- **EGBN STATUS.md updated** — new "What's Changed" entries for Apr 9 microstructure + Apr 10 continuity award detail. Position note: Jun $5P with 1,301 OI = failure-priced (FDIC scenario, not M&A floor).
- **Insider scan re-confirmed (90d):** WAL 40 filings all routine, OZK zero filings, EGBN 25 all routine. NO open market purchases anywhere. Pattern unchanged from earlier work.
- **8-K monitor refinement noted:** Item 5.02 over-flagged because subitem (e) compensatory arrangements is treated same as departures. Both EGBN Feb 25 and Mar 18 were 5.02(e), not departures. Worth a future refinement to parse subitems if signal/noise becomes a problem.
- **Git:** Did NOT pull (CARL/SAM/BRENT/WALTER had uncommitted work). Stashed working tree, pulled remote, popped stash, pushed clean. Toolkit committed as 26c0f71f.

### LAST SESSION (Apr 9 PM — microstructure completion + 13F discovery)
- **RP-REG-5.1 ALL 7 TASKS COMPLETE.** Tasks 5 (dark pool), 6 (options), 7 (short interest) written up.
- **Task 5:** WAL 54% off-exchange on +6.3% day (vs 37% avg). OZK 42% (vs 34%). EGBN 46% (vs 33%). Weakest names spike dark pool on up days. Identified two-channel distribution: ETF structural (AP redemption) + single-name tactical (dark pool selling on rallies). WAL's dark pool activity = longs exiting (short vol only ~40%), not shorts entering.
- **Task 6:** KRE 300K put contracts Apr 17 (53% of float). $68 strike = 57K OI gravity well. OZK May $40P = 1,647 OI. WAL Jun $60P = 1,744 OI. Distribution through shares, conviction through options.
- **Task 7:** OZK 15.28% SI, rising 5 months. WAL 3.46% SI, declining (shorts covered 1.07M shares). KRE SI 69.4M > 56.9M shares outstanding. Shorts concentrating into OZK+KRE, covering WAL.
- **13F INSTITUTIONAL ANALYSIS (from Fintel via Will):** OZK has 50+ full institutional exits. Wellington -43%, AQR -20%, Two Sigma -34%, Point72 -35%, Morgan Stanley -15%, Canada Pension GONE, Ontario Teachers GONE. Quant replacements: Citadel +260%, Millennium +20%, Renaissance +36%. Peak6 opened $15.2M PUT. April filings (Q1 data) show exits CONTINUING — 3 more full exits in first week. **Ownership quality degrading while institutional % appears stable/rising.**
- **OZK Mar 18 (80% short vol day):** Triggered by hot PPI + Fed hold. Macro catalyst, not OZK-specific. Shorts view OZK as rates/CRE duration bet.
- **Insider check:** WAL zero open market buys in 2026. OZK 0.00% insider ownership.
- **Built `scripts/darkpool.py`** — scrapes chartexchange (off-exchange %) + FINRA RegSHO (short vol), auto-appends to TSVs. Run at boot alongside market.py.
- **Created 3 workbook files:** DARKPOOL.tsv (daily off-exchange %), SHORT_VOL.tsv (396 rows YTD from FINRA), SHORT_INTEREST.tsv (6-month bi-monthly history).
- **Full YTD short volume analysis (66 trading days):** OZK shorts press regardless of direction. WAL short activity collapsed 20pp. KRE shorts MORE active on UP days (AP mechanics). EGBN short pressure intensifying on down days.
- **Will engaged deeply** — asked for plain-English explanations, challenged conclusions, drove the 13F investigation. Will's instinct that institutional % rising while quality degrades was confirmed by the data.
- **Git:** Did NOT pull (other agents had uncommitted changes). Committed REGINALD files only.

### LAST SESSION (Apr 9 AM — Tasks 1-4)
- RP-REG-5.1 created. Volume analysis across KRE and thesis names. AP redemption confirmed. OZK cleanest distribution. WAL ambiguous. Will pushed back on overstating "all institutions left."

### LAST SESSION (Apr 7 — full session, earnings prep)
- Inbox processed (7 signals). CALENDAR updated. OZK/EGBN research.

### NEXT SESSION (TODAY'S PLAN — EGBN follow-throughs)
**EGBN-specific (highest priority — 12-15 days to earnings):**
1. **Pull EGBN proxy / latest 10-K** — confirm Riel family relationship (Susan ↔ Ryan A. Riel). Get Ryan's title, tenure, role. Family-linked exec at distressed bank materially changes the governance read.
2. **Pull EGBN Q4 2025 10-K / earnings transcript** — DOGE commentary, GovCon book detail, MI3 trend, AOCI exposure. Currently flagged in EGBN/STATUS.md research agenda but never executed.
3. **Web search EGBN CEO succession** — any leaked candidate names, search firm hired, board comments
4. **EGBN earnings date confirmation** — check IR page after Apr 14 (per CALENDAR.md)
5. **Re-rank EGBN in convergence matrix** — score 12 currently #4 due to "value trap / M&A floor" classification. The continuity award is mildly contrary to clean strategic acquirer scenario. Decide whether to upgrade to #1 alongside WAL.

**Boot routine (use new toolkit):**
6. **Run boot.py at session start** — replaces 6-step manual sequence. Only insider/8K parts are slow; use --skip-slow if rushed.
7. **CPI reaction (Apr 10 data, today)** — hot CPI = stagflation persists. Watch options_oi.py for KRE $68 wall pressure. Re-run darkpool.py for Apr 10 comparison.
8. **KRE $68 put wall monitoring** — 57K OI expires Apr 17 (~7 trading days). Daily proximity check via thresholds.py + market.py.

**Other carryover:**
9. **WAL position decision** — hold Jun $85P through earnings? Short covering fuel spent. Dark pool distribution ongoing.
10. **OZK 8-K check** (~Apr 14) — boot.py 8k_monitor will catch automatically
11. **Read-through watchlist** — MTB (Apr 15), CFG (Apr 16), RF (Apr 17)

**Pending (carried forward, no time pressure):**
12. Cantor PACER docket (Will needs PACER access)
13. Vecchione return status (8-K or LinkedIn check)
14. OZK remaining prompts (#13 peer vintage, #19 metro conditions)
15. Off-exchange % YTD backfill — needs chartexchange premium or FINRA OTC API registration. Tracking forward via darkpool.py instead.
12. Off-exchange % YTD backfill — needs chartexchange premium or FINRA OTC API registration. Deferred; tracking forward via darkpool.py instead.
