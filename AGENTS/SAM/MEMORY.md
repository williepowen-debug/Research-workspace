# SAM MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate.*

---

## Feedback
- [2026-03-31] Will values boot transparency — wants to know what SAM read, in what order, and whether the process is working well. Don't just orient silently; confirm orientation.
- [2026-03-31] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-01] Key dates were getting buried in STATUS.md. Will approved CALENDAR.md as standalone living doc — pure table format, forward-looking only, pruned weekly. Added to boot sequence as step 5.
- [2026-04-02] When explaining complex financial mechanics, Will needs the simplified version first. Start with the plain-English punchline, then layer in detail only if asked. He asked for a re-explain on hedge ratios/repatriation spiral — the second attempt (simpler) landed, the first (detailed) didn't.
- [2026-04-02] Will uses Perplexity for deep research and shares outputs. Treat Perplexity data as high-quality but verify framework logic independently. Will explicitly asked SAM to validate the vol/options framework rather than accepting it uncritically.
- [2026-04-11] **Script-defined alert thresholds MUST match THESIS scenario bucket definitions** — not invented independently. Built `mof_flows.py` with arbitrary "CRISIS ¥4T/4wk" threshold and reported MOF flows at "crisis pace" to Will. When Will asked "how dramatic would Option C be?" I re-checked and found: 4-week rolling was in THESIS stress-case range ($25-40B/mo), not crisis case ($100B+/mo). My "crisis" label was 3.5× too lenient relative to THESIS. Fixed script to calibrate at ¥1.4T elevated / ¥3.5T stress / ¥14T crisis based on THESIS midpoints. **Lesson:** when a script introduces a severity label (CRISIS/STRESS/etc.), that label must cross-reference THESIS.md or use distinct vocabulary. Don't allow label collision with canonical scenario names.
- [2026-04-11] Will prefers intellectually honest corrections over doubling down. When I over-reported "CRISIS PACE" and then had to correct to "STRESS CASE", he didn't push back on the retraction — he took the corrected read and approved the more conservative Option B. Lean toward restraint on thesis-level updates; the data may support it but one data point rarely justifies 15-25pp probability shifts.

## Findings
- [2026-03-31] PROME's SCRATCH.md is the single most useful file at boot for system-wide context. The "QUICKSTART" line and handoff notes give instant orientation.
- [2026-03-31] Inbox items from HERMES often lag behind STATUS.md — check for staleness before processing.
- [2026-03-31] EUR/JPY went unmonitored for 8 weeks and blew through RED (175) to 183. Cross-pair yen weakness can be a blind spot when USD/JPY dominates attention. Check EUR/JPY alongside USD/JPY.
- [2026-03-31] SocGen ¥7.5T "buying" figure from web searches was from 2025, not 2026 — always verify article dates on flow data.
- [2026-04-01] MOF cutting super-long issuance to ¥17T (17-year low) — they know demand is fragile. Context for interpreting auction BTC ratios.
- [2026-04-01] Mar 5 30Y auction: BTC 3.65x at 3.406% yield. Jan: 3.14x. Feb: firmer. Trend data for comparison when Apr 7 results come in.
- [2026-03-31] MHLW wage data runs ~2 month lag. Release pattern: ~8th-9th of month.
## References
- [2026-04-11] **Primary data sources now wrapped by `AGENTS/SAM/scripts/` toolkit.** Run `boot.py` for one-command morning refresh. For one-off queries: `jgb_yields.py`, `jgb_auctions.py --date YYYY-MM-DD`, `cftc_jpy.py`, `mof_flows.py`, `fxy_options.py`, `thresholds.py`, `catalyst_countdown.py`. Source URLs documented in scripts and CLAUDE.md boot step 7.
- [2026-04-07] FORGE toolkit + yfinance commands moved to CLAUDE.md boot step 7 (permanent). Don't duplicate here.
- [2026-03-31] MOF ITS release schedule: mof.go.jp/english/policy/international_policy/reference/itn_transactions_in_securities/schedule.htm
- [2026-03-31] JGB auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/index.htm
- [2026-04-01] April 2026 auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/2604e.htm
- [2026-04-02] Vol/options monitoring sources: CME CVOL (JPVL) for JPY implied vol, Barchart for FXY options OI, Investing.com for USD/JPY risk reversals. All render dynamically — can't auto-scrape, need manual check or Perplexity. Full framework: research/outputs/VOL_OPTIONS_FRAMEWORK.md. (FXY options OI now auto-captured by `fxy_options.py`.)

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 12 → Apr 13)
- Blockade reaction continuing: Brent $101.67 (+6.8%), USD/JPY 159.73 (0.2% from 160).
- FXY $57.48 (flat at entry, -0.28%).
- No new MOF data (Apr 10 was last publish). JGB 10Y breach at 2.439% still the reference level.

### LAST SESSION (Apr 13 — gap analysis, insurer intel, monitoring buildout)
- **Committed + pushed** prior session's 12-file housekeeping update (was uncommitted due to API errors).
- **File maintenance (items 1-5):** Fixed stale TRADE.md (BOJ date 23-24→28, carry 60d 95→97%, dating), STRATEGY.md (v1.0→v1.2), TIMELINE.md (CFTC 67.8K→93.7K, May 1 rate fix 0.75→1.00%, Apr 28 view updated). CALENDAR Apr 13 item marked resolved. Flagged stuck HERMES delivery to Prome (outbox signal).
- **Insurer FY2026 intel sweep:** Ran monitoring queries from TRACKER checklist. FY2026 plans NOT YET DROPPED — window opens tomorrow. Pre-plan intel gathered: Nippon Life ESR 222% (-2pp, unrealized gains ¥12T→¥7.4T, domestic bond losses -¥3.6T, reducing super-long on book-value basis), Dai-ichi doubling overseas strategic investment to ¥600B (M&G ¥160B, Challenger ¥100B, Capula), Mar 2026 survey confirms all Big 3 maintaining private credit plans. Updated TRACKER + nippon-life.md + dai-ichi.md.
- **Key insight:** Nippon Life ESR at 222% despite massive losses = repatriation is ECONOMIC (hedged returns negative), not regulatory panic. Voluntary flows are steady/persistent, not spiky/reversible. Watch for ESR below 200% at May-Jun disclosures — that's when character changes.
- **Gap analysis completed.** Identified 7 gaps. Closed 5 today:
  1. Vol convergence: FXY OI refreshed (stable). CVOL + risk reversals STALE — need terminal/Perplexity mid-week.
  2. Predictions: 5 new falsifiable calls laid down (SAM-16 through SAM-20).
  3. BOJ QT: Now tracked — ¥2.5T/mo purchases (down from ¥6T peak), ¥200B/quarter taper. Vector VX-SAM-12.04 added.
  4. Trade balance: Now tracked — Feb surplus ¥57B (razor-thin, pre-oil-shock). March data mid-April. Vector VX-SAM-11.02 added.
  5. GDP: Q4 2025 +0.3% QoQ (+1.3% ann), avoided recession. Consumption fragile. EWJ trigger not yet fired. Next: Q1 prelim May 14.
- **Remaining gaps (not addressed):** Megabank foreign bond behavior (wait for Apr 15 TIC), Japan energy policy response (low priority).

### NEXT SESSION
1. **🔴 Tue Apr 14: 20Y JGB auction.** Run `jgb_auctions.py --date 2026-04-14`. BTC <2.0x = 🔴 signal to LIQUID, HENRY. Prediction SAM-16: BTC ≥2.5x (70%).
2. **🔴 Tue Apr 14: Insurer FY2026 plans — first movers.** WebSearch TRACKER monitoring queries for Fukoku, T&D/Taiyo. Update TRACKER.md. Prediction SAM-19: ≥2 of 5 announce foreign bond cuts (75%).
3. **🟠 Wed Apr 15: Feb TIC data.** Japan UST selling. Prediction SAM-17: >$10B (65%). Also check megabank vs insurer breakdown (gap #5).
4. **⚠️ Mid-week: CVOL + risk reversal refresh.** Will should check via Perplexity or terminal — these are the critical vol check window signals (STRATEGY.md Apr 14-18).
5. **🔴🔴 DECISIVE — Thu Apr 16: MOF ITS weekly release.** `mof_flows.py`. Prediction SAM-18: >¥1.5T (55%). IF >¥2T → Option C rebalance, THESIS v1.3, 🔴 signal to LIQUID + PROME.
6. **🟠 ~Apr 16-21: March trade balance (MOF customs).** First war-impacted month. Expect large deficit.
7. **🔴 Apr 21-25: Big 4 insurer plans.** Nippon (~Apr 24), Dai-ichi, Meiji Yasuda.
8. **🔴🔴 Apr 28: BOJ MPM.** Prediction SAM-20: hike to 1.00% (60%).

### INFRASTRUCTURE CHANGES (persistent)
- Boot step 7 in `AGENTS/SAM/CLAUDE.md` now says "preferred: run `boot.py`". Old manual instructions preserved as fallback.
- `AGENTS/SAM/tools/usdjpy_monitor.sh` retired — moved to `archive/tools/`. Had a stale "moltbot" VPS path from an old migration. Functionally replaced by `scripts/thresholds.py`.
- All 6 new TSV workbook files seeded with live data:
  - `CATALYSTS.tsv` — 13 events forward-looking
  - `FXY_OPTIONS.tsv` — 4 expiries as of Apr 11
  - `JGB_YIELDS.tsv` — 7 days from MOF CSV
  - `JGB_AUCTIONS.tsv` — Apr 2/7/9 parsed from MOF pages
  - `CFTC_JPY.tsv` — Apr 7 snapshot
  - `MOF_FLOWS.tsv` — 1,109 rows of historical weekly data
