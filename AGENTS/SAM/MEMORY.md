# SAM MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate.*

---

## Feedback
- [2026-03-31] Will values boot transparency — wants to know what SAM read, in what order, and whether the process is working well. Don't just orient silently; confirm orientation.
- [2026-03-31] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-01] Key dates were getting buried in STATUS.md. Will approved CALENDAR.md as standalone living doc — pure table format, forward-looking only, pruned weekly. Added to boot sequence as step 5.
- [2026-04-02] When explaining complex financial mechanics, Will needs the simplified version first. Start with the plain-English punchline, then layer in detail only if asked. He asked for a re-explain on hedge ratios/repatriation spiral — the second attempt (simpler) landed, the first (detailed) didn't.
- [2026-04-02] Will uses Perplexity for deep research and shares outputs. Treat Perplexity data as high-quality but verify framework logic independently. Will explicitly asked SAM to validate the vol/options framework rather than accepting it uncritically.
- [2026-04-11] **Script-defined alert thresholds MUST match THESIS scenario bucket definitions** — not invented independently. Built `mof_flows.py` with arbitrary thresholds and reported MOF flows at "crisis pace" when actually in "stress case." Fixed to calibrate at ¥1.4T elevated / ¥3.5T stress / ¥14T crisis. **Lesson:** scripts using THESIS scenario vocabulary must cross-reference THESIS.md.
- [2026-04-11] Will prefers intellectually honest corrections over doubling down. Lean toward restraint on thesis-level updates; one data point rarely justifies 15-25pp probability shifts.

## Findings
- [2026-05-12] **Read intraday extremes, not just closes — Apr 30 intervention misread.** May 3 STATUS logged Apr 30 yen move as "Tokyo session reprice of Apr 28 BOJ hawkish hold" (USDJPY 159.60 → 157.19). Reality: Apr 30 high 160.70, **intraday low 155.55** (5.15-yen range one session) — characteristic intervention. MOF confirmed ~¥5.48T move via BOJ reserve data within days; SAM didn't cross-check intraday data or web news. Lesson: (1) any 2+ yen close-to-close move on a non-event day deserves cross-source verification, (2) boot scripts focus on close-to-close which masks intervention; **add intraday-range alert when single-day range > 2.5y**, (3) "natural reprice" should rarely be the first hypothesis when the move size is implausible for the named catalyst. Plus, the boot's `usdjpy.py` directional touch logic uses strict `low <= level` — May 6 low 155.047 didn't pierce 155 so the catalog shows "no MOF" for 155 even though intervention #2 was that day. Tolerance band is a future fix.
- [2026-04-24] **Channel 1 hedged-vs-unhedged nuance — candidate v1.4 refinement.** Japanese insurers rotating WITHIN foreign bonds (reducing unhedged, increasing hedged credit) rather than net-cutting. Reconciles Feb TIC (Japan UST +$53.8B) with MOF ITS residents-selling. Aggregate TIC may never confirm thesis cleanly. Wait for ESR disclosures May 15 before refining.
- [2026-04-24] **SAM-19 miss exposes two error types.** (1) Setup mismatch — conflated super-long JGB avoidance with foreign bond cuts. (2) Model oversimplification — binary cut/not-cut framing missed mix-shift behavior.
- [2026-03-31] PROME's SCRATCH.md is the single most useful file at boot for system-wide context.
- [2026-03-31] EUR/JPY went unmonitored for 8 weeks and blew through 175 to 183. Cross-pair yen weakness can be a blind spot when USD/JPY dominates attention.
- [2026-03-31] SocGen ¥7.5T "buying" figure from web searches was from 2025, not 2026 — always verify article dates on flow data.
- [2026-05-03] **Sub-agent fresh-context usability tests surface gaps invisible to the builder.** Spawn fresh-context agent with realistic decision question + scoped context restriction, ask for honest gaps. ~30s/test, high-yield. Re-applicable to any future SAM build/refactor.

## References
- [2026-04-11] **Primary data sources wrapped by `AGENTS/SAM/scripts/`.** `boot.py` for morning refresh. One-off: `jgb_yields.py`, `jgb_auctions.py`, `cftc_jpy.py`, `mof_flows.py`, `fxy_options.py`, `thresholds.py`, `catalyst_countdown.py`, `usdjpy.py`. Source URLs in scripts and CLAUDE.md boot step 7.
- [2026-04-07] FORGE toolkit + yfinance commands in CLAUDE.md boot step 7.
- [2026-03-31] MOF ITS release schedule: mof.go.jp/english/policy/international_policy/reference/itn_transactions_in_securities/schedule.htm
- [2026-03-31] JGB auction calendar: mof.go.jp/english/policy/jgbs/auction/calendar/index.htm
- [2026-04-02] Vol/options sources: CME CVOL (JPVL), Barchart FXY OI, Investing.com risk reversals. FXY OI auto-captured by `fxy_options.py`.

## Session Notes

### CHANGES SINCE LAST SESSION (May 12 → May 21)

1. **JGB 30Y BROKE 4.000% (May 15)** — first time. Peak 4.205%. 10Y at 2.77% (29-yr high). **Driver: J-ICS-induced lifer long-end abandonment** (not high-yields-attract-buyers reflex). v1.4 thesis driver.
2. **USDJPY 157.61 → 159.19** — inside intervention #3 zone (159+). Driver is rate differential + fiscal supply + lifer absence, NOT trade or flow data.
3. **Q1 GDP +2.1% ann beat** (May 19). June BOJ on track. EWJ-put contraction trigger did NOT fire.
4. **Dai-ichi FY2025 ESR ~220%** (May 13-15) — resilient but least-representative of Big 4. Big 3 mutuals (Nippon, Meiji Yasuda, Sumitomo) print May 25-29 — primary test.
5. **April trade balance ¥+301.9B SURPLUS** (May 21) — Phase 1 mechanism INVERTED by blockade volume collapse (crude imports -64% YoY, ME -67%, lowest since 1979). v1.4 thesis finding.
6. **CFTC short cover REVERSED** — re-loading as USDJPY pressed 159.
7. **FXY $57.66** — drifted below May 12 $58.00 limit. Better entry available than originally planned.

### LAST SESSION (May 21 — v1.4 thesis bump + full doc sync)

Will requested boot + parse domain updates. Boot complete (9.3s, all 8 green). Discovered three mechanism-level findings warranting v1.4: (a) J-ICS lifer abandonment as JGB 30Y driver, (b) Phase 1 inversion under blockade, (c) Bessent affirmation promoted to Channel 3 pillar.

**Updates shipped:**
- `thesis/THESIS.md` → v1.4 (status line, Channel 1 new subsection, Channel 3 expansion, Oil-in-Yen revision, thresholds, catalyst sequence resolved/forward, risk factors, falsified predictions)
- `thesis/CHANGELOG.md` → v1.3 → v1.4 audit entry with old/new view table
- `STATUS.md` → full rewrite for v1.4 state
- `thesis/TIMELINE.md` → added May 13-21 resolved cluster; updated branch points table
- `CALENDAR.md` → pruned past; refreshed forward window (May 22 CPI, May 25-29 Big 3 ESR, intervention #3 watch, structural Channel 1 monitors)
- `thesis/PREDICTIONS.tsv` → added SAM-25 (Big 3 mutual ESR <200% @40%), SAM-26 (JGB 30Y holds ≥4.0% through BOJ @70%), SAM-27 (April CPI core <2.0% @75%)

**Position executed (May 21):** +5 shares FXY at ~$57.66 → 13 total (blended entry $57.48). +1 June 18 $58 call @ $0.40 ($40 cost). Will chose pre-CPI entry for IV protection rather than my post-CPI recommendation — legitimate trade-off (IV could expand on hot CPI surprise). Sep $60 calls (Position A) authorized but not executed; revisit post-CPI. Stop $55.05 unchanged.

**Research sub-agents spawned (parallel):** ESR disclosures, Q1 GDP, April trade balance, April CPI preview. All four delivered. Phase 1 inversion was the most thesis-significant finding.

### NEXT SESSION

**Position followup:**
1. **Check FXY $58.00 limit fill status** — if filled (FXY dropped below $58 on May 13-21), confirm position and entry blend. If not filled, re-evaluate against current $57.66.
2. If Will approves add at $57.66, update TRADE.md "Active Positions" header to 12 shares; flag FORGE update to Prome (don't edit FORGE directly per CLAUDE.md cross-directory rule).

**Imminent catalysts:**
1. **🔴 Fri May 22: Japan April national CPI** — Tokyo leading 1.5%; consensus 1.7% core. Soft = fades June BOJ pricing 74% → 60-65%. SAM-27 @75% on <2.0%.
2. **🔴🔴 May 25-29: Big 3 mutual ESR (Nippon, Meiji Yasuda, Sumitomo)** — PRIMARY Channel 1 test. SAM-25 @40% on any <200%.
3. **🟠 ongoing: USDJPY 159+** — intervention #3 trigger zone. SAM-23 @75% (intervention #3 before BOJ).
4. **🟠 ongoing: JGB 30Y >4.0%** — SAM-26 @70% (holds through June BOJ).

**Hard trigger window:**
5. **🔴🔴 Tue Jun 16: BOJ MPM — BASE CASE HIKE.** SAM-21 (70% / market 74%). SAM-24 (25bp @85%).

**Pickup work (deferred):**
- Boot script enhancement: intraday-range alert when USDJPY single-day range > 2.5y (May 12 intervention-miss lesson)
- `usdjpy.py` touch tolerance band (May 6 low 155.05 currently fails strict ≤155)
- THESIS audit pass 2 cleanup — items deferred from May 3 session

### PENDING (carry-over)
- STRATEGY no-chase rule: Tranche 2 zone $58.00-58.25 was breached upward May 1; per rule, forfeited at that level. Adding at $57.66 is a NEW entry zone, not a chase of the original.
- v1.5 trigger gate: if Big 3 mutual ESR prints stress (<200%), would warrant scenario rebalance to stress case 50/40/10 (currently 70/25/5).

### INFRASTRUCTURE STATUS (persistent)
- Boot scripts: 8/8 green (9.3s May 21).
- Workbook auto-pulls: JGB_YIELDS May 20 (30Y BREACHED 4.0%), MOF_FLOWS May 10-16 (net buying), CFTC_JPY (SHORT BUILD reversal), FXY_OPTIONS May 21, USDJPY May 21.
- MOF_INTERVENTIONS catalog: Apr26 (¥5.48T) + May26 (¥4.3T).
- CATALYSTS.tsv (needs sync to v1.4 — deferred to next session).
- STRATEGY.md canonical decision doc; STATUS scenario matrices subordinate.
