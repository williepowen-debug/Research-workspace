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

### CHANGES SINCE LAST SESSION (May 1 → May 3 — 2 day gap, weekend)

**Markets (vs May 1 close):**
- USD/JPY 157.19 → **157.03** (flat)
- FXY $58.63 → **$58.44** (-0.32%, still inside Tranche 2 upper band)
- EUR/JPY 184.34 → 184.06; GBP/JPY 213.78 → 213.21 — broad yen strength holding
- **Brent $111.75 → $107.48 (-3.8%)** — Phase 1 oil pressure easing over weekend
- JGB 10Y 2.520% (no new MOF data — last published Apr 30)
- MOF 4W rolling: ¥-2.68T (no new release — last covers Apr 19-25)

**Major events resolved (May 1):**
- **CFTC JPY release: -94,460 → -102,059** (+7,599 build). Shorts pressed THROUGH BOJ event = no covering on hawkish hold. Now **56.7% of Jul 2024 peak** (highest of cycle). Tilts 30d carry-unwind prob 70 → 72.
- **"BOJ MPM secondary" was a calendar artifact** — Apr 28 was THE meeting. No actual May 1 policy event; nothing to fold in.

### LAST SESSION (May 3 — light boot + May 1 catch-up)

**Boot:** boot.py 7.7s, 6/7 green (JGB Auctions failed — Sun/Mon = no scheduled auction, non-issue).

**Verification (parallel):** Workbook CFTC_JPY.tsv had auto-pulled May 1 data (-102,059); STATUS was stale. WebSearch confirmed (FX.co cited -102.1K). WebSearch on May 1 BOJ — no policy event found, confirming "MPM secondary" was a calendar mislabel.

**File updates:**
1. STATUS.md — header refreshed (date, levels, oil), market table refreshed (May 3 levels, CFTC -102K, status notes), carry unwind probs (30d 70 → 72 on stronger fuel load), watch list (May 1 rows resolved), reference data CFTC paragraph rewritten.
2. CALENDAR.md — Week of May 1 collapsed to RESOLVED outcomes; date-stamp updated.
3. MEMORY.md — this section.

**No position action.** FXY $58.44 inside Tranche 2 zone but per STRATEGY no-chase rule + hard-trigger convergence rule, June BOJ still 44 cal days out (>14d window). Hold. CFTC fuel build is bullish-thesis but doesn't trigger an add by itself.

**No thesis bump** — May 1 CFTC reads as v1.3 confirmation (CFTC build through delay = larger eventual unwind). Per Apr 11 restraint lesson, +2pp on 30d prob is the appropriate scale.

### NEXT SESSION

1. **🟠 May 14 (Thu): Q1 GDP prelim** — 11 calendar days. First post-war quarter; BOJ already cut FY26 to 0.5%. Contraction = EWJ trigger.
2. **🔴 May 15 (Fri): FY2025 ESR disclosures begin.** 12 calendar days. **Primary Channel 1 test** — Big 4 ESR <200% = HARD TRIGGER for Tranche 2 add per STRATEGY.
3. **🟠 May 20 (Wed): April trade balance** — first full post-blockade month; Phase 1 oil mechanism re-test (Brent now $107, easing slightly but still elevated).
4. **🟠 May 22 (Fri): April CPI** — oil passthrough; locks/loosens June hike.
5. **🟡 Brent track:** Down to $107 over weekend (-3.8%). Watch for further easing — if Brent breaks $100, intervention pressure off and Phase 2 path accelerates. If reverses to $115+, Phase 1 dominates.
6. **🟡 FXY watch:** Inside Tranche 2 upper band ($58.44 vs $58.00-58.25). No-chase rule holds; pullback within 14d of June BOJ = live add.
7. **🟠 Next CFTC release Fri May 8** — does the build continue? -110K would put us at Jul24 peak proximity = unwind asymmetry continues to grow.
8. **🔴🔴 Mid-June: BOJ MPM (Jun 16 per countdown)** — BASE CASE HIKE; SAM-21 (70% / market 74%). Hard trigger. Prep scenario tree as date approaches.

### PENDING (carry-over)
- v1.4 decision gate after ESR disclosures (hedged/unhedged nuance refinement).
- Per new STRATEGY no-chase rule: do NOT add Tranche 2 above $58.25 unless hard trigger fires.

### INFRASTRUCTURE STATUS (persistent)
- Boot scripts working cleanly (7.8s). JGB yields auto-pulled through Apr 30. MOF ITS through Apr 19-25.
- CATALYSTS.tsv now synced to v1.3 thesis (was stale).
- STRATEGY.md now canonical decision doc; STATUS scenario matrices subordinate.
- Workbook TSVs auto-updated by boot scripts (FXY_OPTIONS, JGB_AUCTIONS, JGB_YIELDS, MOF_FLOWS).
