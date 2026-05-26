# SAM MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate.*

---

## Feedback
- [2026-03-31] Will values boot transparency — wants to know what SAM read, in what order, and whether the process is working well. Don't just orient silently; confirm orientation.
- [2026-03-31] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-01] Key dates were getting buried in STATUS.md. Will approved CALENDAR.md as standalone living doc — pure table format, forward-looking only, pruned weekly. Added to boot sequence as step 5.
- [2026-04-02] When explaining complex financial mechanics, Will needs the simplified version first. Start with the plain-English punchline, then layer in detail only if asked.
- [2026-04-02] Will uses Perplexity for deep research and shares outputs. Treat Perplexity data as high-quality but verify framework logic independently.
- [2026-04-11] **Script-defined alert thresholds MUST match THESIS scenario bucket definitions** — not invented independently.
- [2026-04-11] Will prefers intellectually honest corrections over doubling down. Lean toward restraint on thesis-level updates; one data point rarely justifies 15-25pp probability shifts.
- [2026-05-25] **Will wants gap-check before writebacks.** When SAM proposes writebacks, Will asks "any other searches?" — surfaces gaps the synthesis missed. Build in a "what's still missing?" beat before executing multi-file passes.

## Findings
- [2026-05-12] **Read intraday extremes, not just closes — Apr 30 intervention misread.** May 3 STATUS logged Apr 30 yen move as "Tokyo session reprice" when it was MOF intervention (intraday range 5.15y). Add intraday-range alert when single-day range >2.5y. `usdjpy.py` touch tolerance band needed (May 6 low 155.05 failed strict ≤155).
- [2026-05-25] **Threshold-durability ≠ mechanism-durability — SAM-26 lesson.** Predicting a number-level holds is fragile when the underlying mechanism is right but cross-currents drive temporary retracement. JGB 30Y broke 4.0% (May 15) on J-ICS lifer abandonment; retraced to 3.931% within 1 week on oil collapse + dovish CPI even though insurers did NOT return as buyers (bid came from non-insurer flow). **Lesson:** when writing falsifiable predictions, separate "mechanism intact" propositions from "threshold sticks" propositions. Threshold predictions need explicit cross-current language ("holds X through event Y absent oil/Fed/intervention shock"). Transferable to any threshold-based prediction (yield levels, FX levels, CFTC contract counts).
- [2026-05-26] **Threshold-vs-mechanism trap fired in real-time on SAM-25 hours after logging.** SAM-25 (any Big 3 <200% ESR @40%) printed TRUE literally on Nippon 195% — but mechanism is M&A capital deployment (Resolution Life $10.6B subsidiarization, -28pt), NOT market stress. Foreign book in unrealized GAIN +¥3.99T. Market priced as capital action (USDJPY 158.95 → 159.24, yen WEAKER). **Same lesson as SAM-26 but on a level-breach instead of a level-hold.** Lesson extension: ESR / capital-ratio predictions must explicitly distinguish "<200% via market stress (forced rebalance signal)" from "<200% via capital action (M&A, sub-debt, dividend)." The intent of these predictions is to flag forced-selling triggers, not generic capital-ratio movement. Future versions: prefix with "due to market losses / forced rebalance" qualifier or split into two sub-predictions.
- [2026-05-26] **Audit cleanup: rank by behavioral impact before line-count impact.** Ran 6-candidate boot-doc maintenance pass (TIMELINE split, PREDICTIONS restructure, THESIS de-dupe + 3 residuals, STATUS compress). Boot context 1,230 → 815 lines (-34%). Honest retro: only ~30% had genuine behavioral impact (PREDICTIONS calibration scoreboard changes future prediction-writing; co-located archive convention transfers to other agents). Other ~70% was cosmetic — line count savings don't matter when Claude has huge context windows. ~3hrs spent could have been 30min focused on PREDICTIONS scoreboard + archive convention. **Lesson:** when audit findings come up, rank by behavioral impact first (does this change what SAM DOES?) before line-count impact. Execute top 1-2 cuts, defer the rest. Will's pushback on PREDICTIONS plan (preserve calibration record, don't archive) was the single best decision of the session — was about to archive the calibration gold. Transferable to any doc-hygiene audit on any agent.
- [2026-05-03] **Sub-agent fresh-context usability tests surface gaps invisible to the builder.** ~30s/test, high-yield. Re-applicable to any future SAM build/refactor.
- [2026-03-31] PROME's SCRATCH.md is the single most useful file at boot for system-wide context.
- [2026-03-31] EUR/JPY went unmonitored for 8 weeks and blew through 175 to 183. Cross-pair yen weakness can be a blind spot when USD/JPY dominates attention.

## References
- [2026-04-11] **Primary data sources wrapped by `AGENTS/SAM/scripts/`.** `boot.py` for morning refresh. One-off: `jgb_yields.py`, `jgb_auctions.py`, `cftc_jpy.py`, `mof_flows.py`, `fxy_options.py`, `thresholds.py`, `catalyst_countdown.py`, `usdjpy.py`. Source URLs in scripts and CLAUDE.md boot step 7.
- [2026-04-07] FORGE toolkit + yfinance commands in CLAUDE.md boot step 7.
- [2026-03-31] MOF ITS release schedule: mof.go.jp/english/policy/international_policy/reference/itn_transactions_in_securities/schedule.htm
- [2026-03-31] JGB auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/index.htm
- [2026-04-02] Vol/options sources: CME CVOL (JPVL), Barchart FXY OI, Investing.com risk reversals. FXY OI auto-captured by `fxy_options.py`.

## Session Notes

### CHANGES SINCE LAST SESSION
*(populated at next boot — step 7 market refresh)*

### LAST SESSION (2026-05-26 — Big 3 ESR Day 1 + boot-doc maintenance pass)

**Phase A (AM — Big 3 ESR Day 1):** Boot 9:36 AM ET; boot.py 12.7s, 7/8 green. Nippon Life FY2025 ESR 195% (vs 222%, -27pt) — breached 200% threshold BUT decomposition is M&A capital action (Resolution Life $10.6B subsidiarization, -28pt; economic environment only -4pt). Foreign book unrealized GAIN +¥3.99T (+¥909B YoY). Meiji Yasuda 208% (manageable; +¥709B GAIN). Market priced as capital action (USDJPY 158.95→159.24 yen WEAKER, FXY flat). **Channel 1 thesis materially weakened — "ESR forces UST sale" mechanism not evidenced.** Demoted to deferred-mechanism / structural-backstop. Channel 2 (June BOJ 55-65%) now dominant remaining trigger; Channel 3 dormant on Brent -12%. Carry unwind probs: 7d 22→17, 30d 70→65, 60d 88→83. **SAM-25 threshold-vs-mechanism trap fired in real-time** hours after logging same finding for SAM-26.

**Phase B (PM — boot-doc maintenance pass):** Audited 6 boot-doc cleanup candidates, executed all. Boot context 1,230 → 815 lines (-34%). TIMELINE.md split into `thesis/timeline/{TIMELINE.md, ARCHIVE.md}` at May-11 cut. PREDICTIONS.tsv restructured in-place with `#`-preamble calibration scoreboard (Will pushed back on archive plan — preserved closed predictions as calibration record; that was the best decision of the session). THESIS.md de-duped (Catalyst Sequence resolved + predictions tables stripped; banner refreshed). THESIS residuals: forward catalyst table refreshed, KEY THRESHOLDS Status column stripped, POSITION VIEW collapsed to thesis-level. STATUS.md narrative compressed (40-line prose → 10 bullets; REFERENCE DATA condensed). New `MAINTENANCE.md` at SAM root tracks structural changes (distinct from analytical `thesis/CHANGELOG.md`). Co-located archive convention established (archives next to active doc; root `archive/` is legacy graveyard, do not add). Two commits pushed (b1f7be2a maintenance + beb1c124 workbook).

**Honest retro:** Maintenance pass ~30% behavioral-impact (PREDICTIONS scoreboard + transferable archive convention), ~70% cosmetic. See new finding 2026-05-26 "rank by behavioral impact before line-count impact."

**Position unchanged:** 13 shares + 1 Jun-18 $58C. Sep $60 calls deferred. Stop $55.05.

### NEXT SESSION

**Imminent catalysts:**
1. **🔴 Wed May 27: Sumitomo Life FY2025 ESR** (~15:00 JST / ~2-3 AM ET). IR page sumitomolife.co.jp/about/company/ir/settlement/. **Pattern-confirmation test.** Check: (a) ESR level, (b) decomposition (M&A vs market stress), (c) Symetra/US PC ($10.7B stack) exposure update, (d) JGB unrealized loss, (e) foreign securities mark. If matches Nippon (M&A-driven, foreign book intact) → v1.5 Channel 1 downgrade. If <200% via market stress → Channel 1 reactivates.
2. **🟠 Thu-Fri May 28-29: Tokyo May CPI.** Core-core <1.9% → June BOJ pricing breaks lower from 55-65%.
3. **🟠 Fri May 29: CFTC weekly (May 22 data).** Watch for break of -102K cycle peak.

**Action items:**
1. **First task: pull Sumitomo ESR from IR page**, then synthesis call.
2. **Post-Sumitomo:** if pattern confirms, write v1.5 THESIS update with Channel 1 reframe; CHANGELOG with old/new view; scenario weights 70/25/5 → 75/20/5.
3. **Outbox signal:** prepare consolidated LIQUID 🟡 + HENRY 🟠 — counter-Channel-1 read (CFTC reload + Big 3 ESR + Channel 1 demotion in ONE signal).
4. **Position decision:** Sep $60 calls (Position A authorized) — with Channel 1 deferred, case rests on June BOJ + CFTC reload, less time-sensitive than pre-ESR.

**Hard trigger window:**
- **🔴🔴 Tue Jun 16: BOJ MPM — base case hike.** SAM-21 ~57% (market 55-65%); SAM-24 (25bp @85%).

**Pickup work (deferred):**
- Boot script: intraday-range alert when USDJPY single-day range > 2.5y.
- `usdjpy.py` touch tolerance band (May 6 low 155.05 fails strict ≤155).
- `jgb_auctions.py` TSV-append bug.
- v1.5 CHANGELOG: separate "J-ICS mechanism intact" from "JGB 30Y threshold holds" framing — deferred until Iran MOU durability known.

### PENDING (carry-over)
- v1.5 trigger gate: if Sumitomo prints stress via market losses (<200% mechanism), warrant scenario rebalance to stress case 50/40/10 (currently 70/25/5).
- STRATEGY no-chase rule: Tranche 2 zone $58.00-58.25 forfeited (breached upward May 1). May 21 $57.66 add was NEW zone.

### INFRASTRUCTURE STATUS (persistent)
- Boot scripts: 7/8 green (jgb_auctions append bug; parser fine).
- Workbook auto-pulls current through May 26 boot.py run.
- MOF_INTERVENTIONS catalog: Apr 30 (¥5.48T) + May 6 (¥4.3T). No #3 yet.
- Boot doc structure post-2026-05-26 cleanup: see `MAINTENANCE.md` for the 6-candidate audit pass + conventions established.
