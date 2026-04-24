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

### LAST SESSION (Apr 24 — v1.3 thesis refresh + Tranche 2 lock + SAM-19 close)

**Part 1: 11-day gap closure + THESIS v1.3**
- Boot green. 11 parallel web searches across 4 domains (BOJ, TIC, insurers, trade/CPI).
- THESIS v1.2 → v1.3: minor bump. TIMING stretch (BOJ April → June base case), flow pace Stress → Base. Structure, channels, conviction HIGH unchanged. Full rationale in CHANGELOG 2026-04-24 entry.
- Updated: CHANGELOG, THESIS, TIMELINE, PREDICTIONS (SAM-16 TRUE, SAM-17/18 FALSE, +SAM-21/22), STATUS, CALENDAR.
- Committed as `92fd12c4` and pushed.

**Part 2: Tranche 2 matrix locked (P0)**
- Replaced old "BOJ hold dip" card with 4-scenario matrix in TRADE.md + STATUS.md.
- Decision: **no chase on surprise hike**. Modal outcome (hold+hawkish ~45%) → add +2 at $58.00-58.25, +2 more at $58.50+ or pre-June CPI. Dry powder reserved for June hike (true base case, SAM-21 @ 70%).
- Will's call: reframe clarified that chase design was for a 10% branch; the actual decision simplified to calm hawkish-hold adds.

**Part 3: SAM-19 resolved FAILED FALSE (P1)**
- Zero of 5 insurer plans announced clean foreign bond cuts.
- **Key thesis-level finding:** insurers rotating WITHIN foreign bonds (unhedged DOWN, hedged UP for ALM matching). Reconciles Feb TIC mystery. Channel 1 signal narrower than framed — mid-May ESR disclosures are the real test.
- Finding logged as candidate v1.4 refinement. NOT bumped to v1.4 today per Apr 11 restraint lesson.
- TRACKER.md updated with KEY INSIGHT section + Nippon/Meiji Yasuda rows corrected.
- Committed as `35eeff13` and pushed.

**Calibration note:** 3 of 4 resolvable predictions FALSE (SAM-17, 18, 19). SAM-19 miss was most informative — exposed a thesis MODEL gap (binary cut/not-cut missed mix-shift reality), not just data interpretation. Scenario weights held at 70/25/5 per restraint lesson; correct call to not over-rebalance.

### NEXT SESSION

1. **🔴 Mon Apr 27 pre-meeting boot.** Run `boot.py`. Watch USD/JPY drift toward 160; MOF intervention risk. Check Reuters/Nikkei for overnight BOJ trial balloons.
2. **🔴🔴 Tue Apr 28: BOJ MPM + Outlook Report + Ueda presser.** Base case HOLD+hawkish (~45%). Tranche 2 matrix in STATUS.md/TRADE.md — no chase on hike. Post-meeting: update STATUS, resolve SAM-20, execute Tranche 2 if scenario triggers.
3. **🟠 Apr 30 (Thu): 2Y JGB auction** — routine.
4. **🔴 Mid-May: ESR disclosures (FY2025) begin.** ELEVATED per v1.3 + hedged/unhedged nuance. Big 4 ESR levels are now Channel 1's primary test. If Meiji Yasuda discloses and ESR <200% → potential v1.4 trigger.
5. **🟠 ~May 20: April trade balance.** First post-blockade month — Phase 1 re-test.
6. **🟠 Late May: April CPI.** Oil passthrough fully visible; June hike lock check.
7. **🔴🔴 Mid-June: BOJ MPM — NEW BASE CASE HIKE (SAM-21 @ 70%).** Prep scenario tree closer to date.
8. **v1.4 decision gate:** after ESR disclosures, evaluate whether hedged/unhedged nuance warrants thesis refinement.

### INFRASTRUCTURE STATUS (persistent)
- Boot scripts working cleanly (10-second total). MOF ITS auto-updated through Apr 12-18 week. CFTC auto-refresh working.
- SAM-21 + SAM-22 added to PREDICTIONS.tsv as forward calls.
- Workbook files: MOF_FLOWS.tsv has the Apr 5-11 reversal data that falsified SAM-18. JGB_AUCTIONS.tsv has the 20Y result.
