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
- [2026-04-24] **Channel 1 hedged-vs-unhedged nuance — candidate v1.4 refinement.** FY2026 insurer plans (Apr 14-25 window) revealed Japanese insurers are rotating WITHIN foreign bonds (reducing unhedged, increasing hedged credit for ALM duration matching) rather than net-cutting foreign bonds. This reconciles Feb TIC (Japan UST holdings +$53.8B Dec→Feb) with MOF ITS showing residents selling foreign bonds. Aggregate TIC will likely NEVER cleanly confirm thesis — signal is in hedged/unhedged sector breakdowns (harder to see). ESR disclosures mid-May become MORE important. Meiji Yasuda explicitly "adding domestic bonds and foreign credit with currency hedge." DO NOT immediately bump to v1.4 — per Apr 11 restraint lesson, let ESR disclosures confirm before refining thesis. Source: Aviva Bond Voyage Feb 2026, Meiji Yasuda briefings, SAM-19 resolution Apr 24.
- [2026-04-24] **SAM-19 miss had two distinct errors worth noting.** (1) Setup mismatch — conflated "super-long JGB avoidance" signals with "foreign bond cut" signals; those are domestic vs foreign. (2) Model oversimplification — binary cut/not-cut framing missed the actual mix-shift behavior (unhedged → hedged). More informative than SAM-17 (TIC miss) because it exposes a THESIS MODEL gap, not just data interpretation.
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

### CHANGES SINCE LAST SESSION (Apr 13 → Apr 24 — 11 day gap)

**Predictions resolved:**
- SAM-16 (20Y BTC ≥2.5x @ 70%): ✅ TRUE — BTC 4.82x, tail 0.2bp exceptional demand
- SAM-17 (Feb TIC Japan UST net selling >$10B @ 65%): ❌ FALSE — Japan holdings rose +$53.8B Dec→Feb
- SAM-18 (MOF Apr 5-11 selling >¥1.5T @ 55%): ❌ FALSE — actual +¥698B net BUYING; Mar 29-Apr 4 was seasonal

**Market:** USD/JPY ~flat at 159.61 (was 159.59 Apr 13); FXY $57.50 (was $57.52); Brent $99.21 (was $100.52); JGB 10Y 2.429% (MOF Apr 23).

**Major catalysts resolved:**
- Apr 13 Ueda speech (dovish) — hike odds 70% → 3-10%
- Apr 14 20Y auction BTC 4.82x — exceptional
- Apr 15 Feb TIC — Japan holdings rose
- Apr 16 MOF ITS — base pace not stress, decisive AGAINST Option C
- Apr 22 ceasefire EXTENDED (not indefinite); Iran seized 2 ships; blockade continues
- Apr 22 March trade SURPLUS ¥667B (Phase 1 didn't fire)
- Apr 22 Nippon Life briefing — paring yen bonds, foreign direction ambiguous
- Apr 23 March CPI core 1.8% (accelerated, still sub-target)

### LAST SESSION (Apr 24 — v1.3 thesis refresh)

- **Boot:** All 7 boot scripts green. Market flat over 11 days despite major catalysts.
- **Research:** 11 parallel web searches across 4 domains (BOJ, TIC, insurers, trade/CPI). Closed all 7 research gaps.
- **THESIS refresh v1.2 → v1.3:** Minor version bump. Structure intact, channels intact, conviction HIGH. What changed: TIMING (BOJ April → June base case) and FLOW PACE framing (Stress → Base). Full rationale in CHANGELOG 2026-04-24 entry.
- **Key file updates:**
  - `CHANGELOG.md` — v1.3 entry with old→new view + intellectual restraint section
  - `THESIS.md` — header, one-liner, Channel 1-2-3 updates, catalyst sequence rebuilt, Oil-in-Yen Phase 1 downgrade, thresholds updated, predictions section added FALSIFIED sub-table
  - `TIMELINE.md` — 8 events marked RESOLVED (Apr 13-23), forward section rebuilt for June base case, branch point table expanded
  - `PREDICTIONS.tsv` — SAM-16 CONFIRMED, SAM-17/18 FAILED, SAM-19/20 status refreshed, added SAM-21 (June hike 70%) + SAM-22 (CFTC persistence 65%)
  - `STATUS.md` — full rewrite reflecting v1.3
  - `CALENDAR.md` — rebuilt around Apr 28 binary + May ESR + June hike

**Calibration note:** 2 of 3 resolvable predictions FALSE. Pattern: over-weighted acceleration signals vs reversion. SAM-17 miss driven by stock-vs-flow confusion. SAM-18 was 50/50 going in. Reading Apr 11 lesson ("one data point rarely justifies 15-25pp shifts") correctly avoided the opposite mistake — kept scenario weights at 70/25/5.

### NEXT SESSION

1. **🔴🔴 Apr 28 (Tue): BOJ MPM + Outlook Report + Ueda presser.** Base case HOLD + hawkish (v1.3 ~45%). 4-outcome scenario tree in STATUS.md. Post-meeting: update STATUS, resolve SAM-20, consider FXY Tranche 2 action.
2. **🔴 Mon Apr 27 pre-meeting:** Run `boot.py`. Watch USD/JPY drift toward 160; MOF intervention risk rising. Check for any Reuters/Nikkei trial balloons in Asia overnight.
3. **🟠 Apr 21-25 remaining insurer plans:** Meiji Yasuda, Dai-ichi, Sumitomo. Update TRACKER.md. Resolve SAM-19 (trending FALSE).
4. **🟠 Apr 30 (Thu): 2Y JGB auction** — routine, lower priority.
5. **🔴 Mid-May: ESR disclosures (FY2025) begin.** Now ELEVATED importance per v1.3. Big 4 ESR levels are Channel 1's next real test.
6. **🔴🔴 Mid-June: BOJ MPM — NEW BASE CASE HIKE.** SAM-21 (70%). Prep scenario tree closer to date.
7. **Tranche 2 logic revision:** Pre-BOJ discussion with Will — original card said "BOJ hold dip" was trigger, but that's now base case. Either wait for Apr 28 outcome and re-rank triggers, or pre-stage levels for each of 4 scenarios.

### INFRASTRUCTURE STATUS (persistent)
- Boot scripts working cleanly (10-second total). MOF ITS auto-updated through Apr 12-18 week. CFTC auto-refresh working.
- SAM-21 + SAM-22 added to PREDICTIONS.tsv as forward calls.
- Workbook files: MOF_FLOWS.tsv has the Apr 5-11 reversal data that falsified SAM-18. JGB_AUCTIONS.tsv has the 20Y result.
