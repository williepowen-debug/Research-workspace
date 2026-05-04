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
- [2026-03-31] MHLW wage data runs ~2 month lag. Release pattern: ~8th-9th of month.
- [2026-05-03] **Sub-agent fresh-context usability tests surface gaps invisible to the builder.** Built USDJPY at-a-glance May 3; first sub-agent test (general-purpose, restricted to ONLY the new 2-line boot block) immediately flagged the load-bearing gap — "160 (3d)" was silent on whether MOF intervened, the actual risk question. Builder's context (familiar with thesis, intervention episodes) blinded me to it. Pattern: when shipping agent-facing tooling, spawn fresh-context agent with realistic decision question + scoped context restriction, ask for honest gaps. ~30s/test, high-yield. Used 2× this session: round 1 caught substantive gap, round 2 (post-fix) caught smaller cosmetic ones. Re-applicable to any future SAM build/refactor.
- [2026-05-03] **Phase 3 — partial ship (May 3).** USDJPY at-a-glance build (Phase 1) shipped May 3. Sub-agent usability test surfaced the load-bearing gap: "160 (3d)" was silent on whether MOF intervened — a recent touch with NO intervention is much hotter than one that triggered MOF. Lite Phase 3 added: MOF episode catalog as `MOF_INTERVENTIONS` dict in `scripts/usdjpy.py` (Sep22, Oct22, Apr24, May24, Jul24 — public record dates + sizes), cross-referenced against touch dates with ±3 day window. Format now: `160 (3d, no MOF)` or `160 (3d, MOF Apr24)`. **Still deferred — full narrative doc** (`reference/USDJPY_REGIMES.md` covering Aug 2024 unwind mechanics, intervention effectiveness analysis, technical levels with provenance). Build trigger: when the in-script catalog proves insufficient. Phase 2 (replicate TSV+summary for JGB10Y/Brent/FXY) still future work.
## References
- [2026-04-11] **Primary data sources now wrapped by `AGENTS/SAM/scripts/` toolkit.** Run `boot.py` for one-command morning refresh. For one-off queries: `jgb_yields.py`, `jgb_auctions.py --date YYYY-MM-DD`, `cftc_jpy.py`, `mof_flows.py`, `fxy_options.py`, `thresholds.py`, `catalyst_countdown.py`, `usdjpy.py`. Source URLs documented in scripts and CLAUDE.md boot step 7.
- [2026-04-07] FORGE toolkit + yfinance commands moved to CLAUDE.md boot step 7 (permanent). Don't duplicate here.
- [2026-03-31] MOF ITS release schedule: mof.go.jp/english/policy/international_policy/reference/itn_transactions_in_securities/schedule.htm
- [2026-03-31] JGB auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/index.htm
- [2026-04-01] April 2026 auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/2604e.htm
- [2026-04-02] Vol/options monitoring sources: CME CVOL (JPVL) for JPY implied vol, Barchart for FXY options OI, Investing.com for USD/JPY risk reversals. All render dynamically — can't auto-scrape, need manual check or Perplexity. Full framework: research/outputs/VOL_OPTIONS_FRAMEWORK.md. (FXY options OI now auto-captured by `fxy_options.py`.)

## Session Notes

### CHANGES SINCE LAST SESSION
- [populate at next boot during market refresh — ~hours-to-days offline since May 3 evening commit chain]
- Project Freedom (Mon May 4) is the dominant overnight event — check Brent direction first.

### LAST SESSION (May 3 evening — THESIS audit + USDJPY at-a-glance build)

Two-track: housekeeping (THESIS audit) → architecture build (USDJPY at-a-glance), the second triggered by audit pass exposing line 37 "at current ~160" staleness.

**THESIS audit pass 1 — 9 fixes shipped (437d7e6f).** Deleted contradicted "Dovish BOJ pivot (hold+dovish Apr 28)" risk row. Added missing predictions: SAM-04, SAM-06 → CONFIRMED; SAM-08 (90%-conf miss), SAM-19, SAM-20 → FALSIFIED. Date fix Thu May 8→Thu May 7. Brent $107.85→$107.98 across 4 spots. ESR "Mid-May"→"Fri May 15". Apr 28 dissent split promoted to top of Channel 3 BOJ evidence.

**THESIS audit pass 2 — 7 items NOT fixed (Will redirected to architecture work).** Listed in NEXT SESSION pickup. Substantive: line 37, line 100, line 160. Minor: NEW— tags, undated ¥13.2T, threshold format, line 78 ESR.

**USDJPY at-a-glance build (38e42854, 63b08f9b, 5faba6fd, b1e84825).** New `scripts/usdjpy.py` + `workbook/USDJPY.tsv` (5Y daily OHLC, 1299 rows). Wired into boot.py. Iterative ship with sub-agent usability tests:
- Phase 1: TSV + summary + boot wiring
- Bug fix: skip today's intraday partial
- Phase 3 lite: MOF_INTERVENTIONS catalog (5 episodes, ±3d window) — closes load-bearing "did MOF intervene" gap caught by sub-agent test
- Polish: 5d trend tag + arrow separator on touch line

Final block:
```
🟠 USDJPY 157.03 (5d: -2.7) | 30d: 155.5-160.7 | 90d: 152.3-160.7 | 52wk: 142.1-160.7
🟠 Days since touch: 160 → 3d, no MOF | 155 → 68d, no MOF | ...
```
Boot time +1.0s. Sub-agent test pattern logged as Finding (re-applicable to future builds).

**No position action.** FXY $58.44 inside Tranche 2 upper band, STRATEGY no-chase holds. **No thesis bump** (housekeeping + infrastructure, not thesis work).

### NEXT SESSION

**Imminent (hours-to-days):**
1. **🔴 Mon May 4: "Project Freedom" Hormuz escort start.** Iran response = oil swing direction. Resistance → snap back to $115+ (Phase 1 reasserts, USDJPY upside pressure). Passive Iran → Brent slides toward $100 (Phase 2 path accelerates, intervention pressure off).
2. **🟠 Thu May 7: MOF ITS weekly (Apr 26-May 2)** — first full-week flow read post-Apr 28 BOJ. (Note: Thu, NOT Fri — May 8 is Friday.)
3. **🟠 Fri May 8: CFTC JPY release.** -110K would put us at ~61% of Jul24 peak — unwind asymmetry continues to grow. Cover signal would be the surprise.

**Mid-month thesis tests:**
4. **🟠 Thu May 14: Japan Q1 GDP prelim.** First post-war quarter; BOJ already cut FY26 to 0.5%. Contraction = EWJ trigger.
5. **🔴 Fri May 15: FY2025 ESR disclosures begin.** PRIMARY Channel 1 test. Big 4 ESR <200% = HARD TRIGGER for Tranche 2 add per STRATEGY.
6. **🟠 Wed May 20: April trade balance** — first full post-blockade month; Phase 1 oil mechanism re-test.
7. **🟠 Fri May 22: April CPI** — oil passthrough; locks/loosens June hike.

**Hard trigger window:**
8. **🔴🔴 Tue Jun 16: BOJ MPM — BASE CASE HIKE.** SAM-21 (70% / market 74%). Tranche 2 hard trigger. Prep scenario tree ~end-May.

**Background watches (no action by themselves):**
- **Brent direction:** $107.98 at session end. Through $100 = Phase 2 acceleration; through $115 = Phase 1 reasserts. Watch boot output for first move.
- **FXY $58.44:** Inside Tranche 2 upper band. No-chase rule holds. Pullback to $58.00-58.25 within 14d of June BOJ (late-May+) = live add.
- **JGB long end:** 30Y 3.721, 40Y 3.743 — 26-28bp from 4.0%. Auto-pulled by boot.py.

**Pickup work (if no urgent priorities):**
- **THESIS audit pass 2 cleanup** — 7 items deferred this session. 3 substantive: line 37 "at current ~160" stale (USDJPY is 157), line 100 "April-July collision window" past-tense (now June-July), line 160 "oil-yen paradox" reads as if yen still weakening (pre-Apr-28 framing). 4 minor: "NEW —" tags on month-old additions, undated ¥13.2T Big 4 figure, threshold table format inconsistency, line 78 ESR "mid-May" → "Fri May 15".
- **Use the new USDJPY at-a-glance** in real session decisions; if useful, candidate Phase 2 (replicate TSV + summary pattern for JGB10Y, Brent, FXY).

### PENDING (carry-over)
- v1.4 thesis decision gate after ESR disclosures mid-May (hedged/unhedged nuance refinement; SAM-19 lesson).
- STRATEGY no-chase rule: do NOT add Tranche 2 above $58.25 unless hard trigger fires.
- USDJPY_REGIMES.md narrative doc still deferred — build trigger now is "when in-script MOF catalog proves insufficient."

### INFRASTRUCTURE STATUS (persistent)
- Boot scripts: 7/8 green (JGB Auctions weekend-FAIL is normal Sun/Mon; USDJPY added May 3, +1.0s boot).
- Workbook auto-pulls current through: JGB_YIELDS Apr 30, MOF_FLOWS Apr 19-25, JGB_AUCTIONS Apr 30 (2Y), CFTC_JPY Apr 28, FXY_OPTIONS May 3, **USDJPY May 1 close (5Y daily OHLC, 1299 rows; today's intraday deliberately skipped)**.
- **NEW: USDJPY at-a-glance** — 2-line boot block with current + 5d trend + 30/90/365 ranges + days-since-touch annotated with MOF intervention markers.
- **NEW: MOF intervention catalog** hardcoded in `scripts/usdjpy.py` (`MOF_INTERVENTIONS` dict — Sep22, Oct22, Apr24, May24, Jul24). Extend if new episode occurs.
- CATALYSTS.tsv synced to v1.3 thesis.
- STRATEGY.md canonical decision doc; STATUS scenario matrices subordinate.
- Golden Week: Japan markets closed May 3-6 (Constitution Day, Greenery Day, Children's Day) — expect no new MOF/JGB data until ~May 7.
