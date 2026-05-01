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

### CHANGES SINCE LAST SESSION (Apr 28 → May 1 — 3 day gap, post-BOJ Tokyo digest)

**Markets:**
- USD/JPY 159.60 → **157.19** (-2.41 yen, broad yen strength)
- FXY $57.49 → **$58.63 (+1.98%)** — Tranche 2 zone $58.00-58.25 BREACHED upward
- JGB 10Y 2.477% → **2.520%** (+4bp; 28-yr high zone)
- EUR/JPY 186.92 → 184.34; GBP/JPY 215.77 → 213.78 — broad strength (not USD-specific)
- Brent $111.26 → $111.75 — Phase 1 oil pressure persists
- MOF 4W rolling: ¥-2.74T → ¥-2.68T (Apr 19-25 latest, ELEVATED)
- Boot.py Brent reconciled — $111.75 today vs $104.35 Apr 28 intraday

**Major events resolved:**
- **Apr 29-30 Tokyo session: BULL FORK** — JPY broadly strengthened, FXY +1.98%
- **Apr 30 2Y JGB auction:** BTC 5.24x, tail 0.005y, yield 1.407% — orderly
- **Apr 29-30 Katayama/Aida political response:** QUIET — no Diet pushback, no BOJ Law threats. D2 channel quiet.

### LAST SESSION (May 1 — post-Tokyo-reprice boot + STRATEGY sync)

**Boot:** boot.py clean (7.8s, all 7 scripts green). FXY in Tranche 2 zone, JGB 10Y +4bp, MOF 4W elevated, FXY P/C 0.10x call-heavy.

**Caught and fixed: CATALYSTS.tsv data staleness.** TSV had stale labels from pre-v1.3 thesis (May 1 mislabeled "BASE CASE HIKE", Jun 16 mislabeled "backstop", resolved Apr rows still present). Rewrote TSV to match v1.3 thesis. Catalyst countdown now reads correctly.

**Apr 30 verification (parallel):** WebFetch on MOF auction page (2Y BTC 5.24x). WebSearch on Katayama/Aida — no escalation found.

**File updates (sequenced as 3 chunks + STRATEGY):**
1. STATUS.md — full sync: header, market table, carry unwind probabilities, BOJ 48hr-watch flipped to RESOLVED, intervention status downgraded ELEVATED→MODERATE, Tranche 2 matrix marked FIRED, thresholds, watch list, reference data
2. CALENDAR.md — Apr 27-30 row collapsed to RESOLVED outcomes; added May 1 CFTC release as 🟠
3. TIMELINE.md — new top entry "Apr 29-30 Tokyo Session Reprice" as BULL FORK; branch points table appended
4. CATALYSTS.tsv — full rewrite to match v1.3 thesis
5. STRATEGY.md — **major v1.3 sync.** Stage table refreshed (Stage 2 = pre-trigger setup). Hard triggers expanded: June BOJ primary + 4 alternates. **NEW soft-signal convergence rule:** matrix-defined +2 entries fire ONLY if a hard trigger is within 14 days. **NEW no-chase rule:** if matrix zone breached upward, add forfeited at that level. CHANGELOG entry added.

**Position decision (held off):** Tranche 2 trigger condition per Apr 28 STATUS matrix met (Tokyo did re-rate). But STRATEGY.md hard triggers NOT met (June BOJ ~6wk out, USDJPY 157.19 not <155). Recommended HOLD — preserve dry powder for hard trigger or pullback to $58.00-58.25 limit.

**Doc conflict caught and resolved:** STATUS matrix said "Tranche 2 fires"; STRATEGY said "no add — hard triggers not met." Updated STRATEGY to be canonical decision doc; matrices subordinate via soft-signal convergence rule. Process improvement that reduces conviction-bias adds under pressure.

**No thesis bump** — Apr 29-30 Tokyo reprice CONFIRMED v1.3, didn't refine it. ESR mid-May remains the next genuine thesis-test.

### NEXT SESSION

1. **🟠 May 1 BOJ MPM secondary** — low info; check Ueda one-pager language for any softening from Apr 28.
2. **🟠 May 1 CFTC JPY release** — first post-Apr-28 positioning read. Cover signal vs continued build is the real test of carry-unwind 7d.
3. **🟡 Watch FXY pullback to $58.00-58.25** — if pullback happens within 14 days of June BOJ (i.e., late May), Tranche 2 +2 is live per new STRATEGY rules.
4. **🟠 May 14: Q1 GDP prelim** — first post-war quarter; BOJ already cut FY26 to 0.5%, contraction = EWJ trigger.
5. **🔴 Mid-May: ESR disclosures (FY2025) begin.** Primary Channel 1 test. Big 4 ESR <200% = HARD TRIGGER for Tranche 2 add per updated STRATEGY.
6. **🟠 ~May 20: April trade balance.** Brent $111 makes this hot — Phase 1 mechanism re-test.
7. **🟠 Late May: April CPI.** Oil passthrough; June hike lock.
8. **🔴🔴 Mid-June: BOJ MPM — BASE CASE HIKE (SAM-21 70%; market 74%).** Hard trigger; prep scenario tree closer to date.

### PENDING (carry-over)
- v1.4 decision gate after ESR disclosures (hedged/unhedged nuance refinement).
- Per new STRATEGY no-chase rule: do NOT add Tranche 2 above $58.25 unless hard trigger fires.

### INFRASTRUCTURE STATUS (persistent)
- Boot scripts working cleanly (7.8s). JGB yields auto-pulled through Apr 30. MOF ITS through Apr 19-25.
- CATALYSTS.tsv now synced to v1.3 thesis (was stale).
- STRATEGY.md now canonical decision doc; STATUS scenario matrices subordinate.
- Workbook TSVs auto-updated by boot scripts (FXY_OPTIONS, JGB_AUCTIONS, JGB_YIELDS, MOF_FLOWS).
