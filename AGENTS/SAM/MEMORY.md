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

### CHANGES SINCE LAST SESSION (Apr 24 → Apr 28 — 4 day gap, BOJ binary)

**Markets:**
- USD/JPY 159.60 (flat from 159.61) — odd given hawkish hold
- FXY $57.49 (flat from $57.50) — Tranche 2 trigger zone $58.00-58.25 NOT yet hit
- JGB 10Y 2.477% (was 2.429% Apr 23, +5bp) — grinding higher
- **Brent $111.26 settle (CNBC) — +12% from $99.21 Apr 24** on Trump rejecting Iran Hormuz proposal
  - boot.py BZ=F showed $104.35 (likely intraday US session vs settle)
- CFTC JPY net -93,742, still SHORT BUILDING

**Major catalyst resolved:**
- **Apr 28 BOJ MPM: HOLD + 3 dissents (Takata, Tamura, Nakagawa) for 1.00%** — biggest split since 2016, first under Ueda
- FY2026 GDP cut 1.0% → 0.5%; inflation forecasts upgraded; Ueda hawkish presser
- **Swap markets repriced June hike to 74%** (vs SAM-21 70%)

### LAST SESSION (Apr 28 — BOJ post-meeting boot)

**Boot + market refresh:**
- Standard boot.py ran clean (13.1s). All 7 scripts green.
- Two parallel WebSearches: BOJ Apr 28 outcome + Brent/Hormuz context.

**File updates (sequenced):**
1. STATUS.md — header, market table, BOJ assessment, Tranche 2 status, thresholds, watch list, short-form thesis
2. PREDICTIONS.tsv — SAM-20 resolved FAILED FALSE with calibration note
3. TIMELINE.md — Apr 28 + Brent $111 events added at top; Week 4 Apr 27 collapsed to "resolved" pointer; branch points table updated
4. CALENDAR.md — Apr 28 marked ✅; pruned insurer table (SAM-19 closed); added Apr 29 Tokyo session as 🔴 watch
5. CHANGELOG.md — 2026-04-28 entry added (no thesis version bump per Apr 11 restraint lesson)
6. MEMORY.md (this) — session notes refreshed

**Key calibration finding:** SAM-20 60% FALSE was a significant miss. Lesson logged in PREDICTIONS notes: when political ceiling is explicit (Takaichi 0.75% line) AND external uncertainty is high (oil/war), BOJ defers to consensus optics even when data supports action. Hawkish dissents are how the board telegraphs intent without breaking that consensus. This is a NEW lesson worth promoting if it repeats.

**No thesis bump** — per Apr 11 restraint lesson. Apr 28 confirmed v1.3 modal scenario; 3-dissent + GDP cut is hawkish-augmenting but doesn't change structure. ESR disclosures (mid-May) remain the next genuine thesis-test.

### NEXT SESSION

1. **🔴 Apr 29 morning: check overnight Tokyo session.** Did FXY rally to $58.00-58.25 trigger zone on the dissent split? If yes → execute Tranche 2 +2. If FXY didn't budge → market is signaling hawkish-hold isn't enough fuel; no chase.
2. **🟠 Apr 29-30: Katayama / Aida political reaction** to 3-dissent split. Takaichi tone matters (BOJ Law revision threats = D2 escalation signal).
3. **🟡 Apr 30 (Thu): 2Y JGB auction** — routine.
4. **🟡 May 1 (Fri): BOJ MPM secondary** — low info if Apr 28 holds.
5. **🟠 May 14: Q1 GDP prelim** — first post-war quarter; BOJ already cut FY26 to 0.5%, contraction = EWJ trigger.
6. **🔴 Mid-May: ESR disclosures (FY2025) begin.** Primary Channel 1 test per v1.4 candidate. Meiji Yasuda ESR <200% = potential v1.4 trigger.
7. **🟠 ~May 20: April trade balance.** Brent $111 makes this hot — Phase 1 mechanism re-test.
8. **🟠 Late May: April CPI.** Oil passthrough; June hike lock.
9. **🔴🔴 Mid-June: BOJ MPM — BASE CASE HIKE (SAM-21 70%; market 74%).** Prep scenario tree closer to date.

### PENDING (carry-over)
- v1.4 decision gate after ESR disclosures (hedged/unhedged nuance refinement).
- Verify Brent $104 (BZ=F intraday) vs $111.26 (CNBC settle) discrepancy at next boot.

### INFRASTRUCTURE STATUS (persistent)
- Boot scripts working cleanly (13.1s). JGB yields auto-pulled through Apr 27. MOF ITS through Apr 12-18 week.
- Catalyst countdown caught BOJ Apr 28 correctly. SAM-21/22 still OPEN forward calls.
- Workbook files NOT updated this session (no new MOF/JGB data since Apr 24); update when Apr 19-25 MOF ITS lands (Apr 30).
