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

### CHANGES SINCE LAST SESSION (May 3 evening → May 12 morning)

1. **MOF Intervention #1 (Apr 30) ~¥5.48T ($35B)** — first since Jul 2024. SAM's May 3 STATUS mis-attributed as "Tokyo session reprice." Corrected May 12.
2. **MOF Intervention #2 (May 6, Golden Week) ~¥4.3T ($28B).** Combined ~¥10T ($63.5B) — largest round since 2022.
3. **Bessent-Katayama Tokyo meeting May 11-12.** "Constant and robust" FX coordination affirmed; Katayama: actions per Sept joint statement. First US public affirmation of Japan FX intervention. **New thesis vector** (Channel 3 augmentation candidate).
4. **CFTC cover signal (May 8 release, May 5 data).** Net short -102,059 → -61,738 (-39.5%). FIRST cover signal of cycle. **SAM-22 FAILED.**
5. **Brent $107.74 (+3.4% today).** Phase 1 oil reasserting after weekend de-escalation.
6. **FXY $58.26.** BELOW May 3 level ($58.44). Tranche 2 hard trigger fired but dip faded.

### LAST SESSION (May 12 morning — intervention catch-up + position regret + thesis update)

Will mentioned possible intervention at boot. Web search confirmed: TWO interventions ($63.5B total) + Bessent affirmation today. SAM's May 3 read of the Apr 30 move was wrong — labeled it "natural Tokyo reprice" when intraday 5.15-yen range was the intervention signature.

**Updates shipped:**
- `scripts/usdjpy.py` MOF_INTERVENTIONS catalog: added 2026-04-30 (Apr26 ¥5.48T) and 2026-05-06 (May26 ¥4.3T). 160-touch now correctly tags "MOF Apr26."
- `thesis/TIMELINE.md`: corrected Apr 30 entry; added Golden Week intervention + Bessent meeting entries.
- `STATUS.md`: rewrote to reflect intervention + cover + Bessent + position regret. Carry unwind probs 12/70/88 (was 20/72/90).
- `CALENDAR.md`: forward gaze refreshed; intervention watch added.
- `thesis/CHANGELOG.md`: 2026-05-12 entry — correction logged, no thesis bump (v1.3 holds per restraint lesson).
- `thesis/PREDICTIONS.tsv`: SAM-22 FAILED FALSE; added SAM-23 (intervention #3, 75%) and SAM-24 (June 25bp not 50bp, 85%).

**Position decision (May 12):** Limit at $58.00 for +4 shares (→ 12 total). Recorded in TRADE.md and STATUS.md. Live indefinitely; re-evaluate June 1 if no fill.

**Deeper sweep (May 12 PM):** Found broader Bessent agenda (3-day trip pre-Beijing summit, critical minerals + AI + $550B investment + BOJ + Iran), prior pro-hike stance, BofA contrarian view, Trump-Iran-ceasefire-doubts driving Brent +3.4%, Trump-Xi May 14-15 wildcard. Updated TIMELINE, STATUS, CALENDAR, CHANGELOG. No thesis bump.

**Push coordination (May 12 PM):** First push (AM commit `25567657`) clean. Second push (Bessent sweep `bd032212`) initially rejected — WALTER was mid-session routing April CPI 3.8% signal. Will coordinated: WALTER finished + pulled-rebased + pushed, and my Bessent commit went up cleanly with WALTER's via rebase. **Workflow lesson:** when push is rejected by remote-divergence with another agent's uncommitted work, defer to operator coordination; rebase-via-other-agent's-pull can resolve cleanly without my direct intervention.

### NEXT SESSION

**Position followup:**
1. Check fill status (FXY $58.00 limit, +4 shares) — Will placed order
2. If filled: confirm new position size (12 shares), entry blend, update TRADE.md "Active Positions" header. Flag FORGE update to Prome (don't edit FORGE directly per CLAUDE.md cross-directory rule).
3. If not filled by June 1: re-evaluate trigger conditions — has Brent settled? Is intervention #3 plausible? Or has FXY drifted such that the $58.00 limit is too aggressive vs market price?

**Imminent catalysts (this week):**
1. **🔴 Thu May 14: Q1 GDP prelim + MOF ITS weekly (Apr 26-May 2)** — GDP is EWJ trigger if contraction; MOF first full post-intervention week is key flow read
2. **🔴 Fri May 15: FY2025 ESR disclosures begin** — PRIMARY Channel 1 test, hard trigger if Big 4 <200%
3. **🟠 Fri May 15: CFTC JPY release** — continuation cover vs re-build

**Hard trigger window:**
4. **🔴🔴 Tue Jun 16: BOJ MPM — BASE CASE HIKE.** SAM-21 (70% / market 74%). SAM-24 (25bp not 50bp, 85%) tracks.

**Background watches:**
- **Intervention #3 watch:** USDJPY 159+ retest. Bessent affirmation removes diplomatic friction. SAM-23 (75%).
- **Brent direction:** $107.74 today (+3.4%). Through $115 = Phase 1 escalates → intervention #3 likely; through $100 = Phase 2 path.
- **JGB long end:** 30Y/40Y pending boot pull (last MOF Apr 30 — Golden Week + early May data may show further drift).

**Pickup work (lower priority):**
- **Boot script enhancement:** add intraday-range alert when USDJPY single-day range > 2.5y (the May 12 intervention-miss lesson)
- **`usdjpy.py` touch tolerance:** consider tolerance band on level matching so May 6 low 155.05 maps to "MOF May26" for 155 (today shows "no MOF" because strict ≤155 fails on 155.05)
- **THESIS audit pass 2 cleanup** — 7 items deferred from May 3 session (line 37 "at current ~160", line 100 collision window, NEW— tags, etc.)

### PENDING (carry-over)
- v1.4 thesis decision gate: ESR disclosures May 15 (hedged/unhedged nuance — SAM-19 lesson). Plus Bessent vector — wait for second confirmation (intervention #3 with US backing, or SWAP line, or rate-coordination signal).
- STRATEGY no-chase rule: Tranche 2 zone $58.00-58.25 was breached upward May 1; per rule, forfeited. Re-add at hard trigger or new defined zone.

### INFRASTRUCTURE STATUS (persistent)
- Boot scripts: 8/8 green. CFTC SHORT COVER alert fired for first time this cycle.
- Workbook auto-pulls: JGB_YIELDS May 11, MOF_FLOWS Apr 19-25 (next Thu May 14), JGB_AUCTIONS Apr 30, CFTC_JPY May 5 (BIG SHIFT), FXY_OPTIONS May 12, USDJPY May 11.
- **NEW: MOF_INTERVENTIONS catalog updated** — Apr26 (¥5.48T) + May26 (¥4.3T) added. 160-touch now tags "MOF Apr26."
- CATALYSTS.tsv synced to v1.3 thesis.
- STRATEGY.md canonical decision doc; STATUS scenario matrices subordinate.
