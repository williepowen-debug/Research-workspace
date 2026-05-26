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

### CHANGES SINCE LAST SESSION (May 21 → May 26)

1. **Japan April CPI MISS (May 22)** — core 1.4% vs 1.7% consensus / 1.8% prior; core-core 1.9% vs 2.2%; 3rd consecutive month below 2% target. Subsidies absorbing oil passthrough. **SAM-27 (<2.0%) CONFIRMED TRUE.**
2. **Brent -12% to $94.53** on Iran/Hormuz MOU optimism (Pakistan mediating; deal rumor-tier, no signed text). Phase 2 (war wind-down → safe-haven yen) being priced.
3. **CFTC net short REBUILT to -93,905** (May 19 data, May 22 release) — +18,803 WoW, 3rd straight build week, now 92% of -102,059 Apr 28 cycle peak. Build = new shorts (+25K), not long liquidation = directional re-engagement.
4. **JGB 30Y retraced 4.000% → 3.931%** on oil + dovish CPI. **SAM-26 tracking FALSE within 1 week.** Mechanism (J-ICS) intact; threshold not durable.
5. **USDJPY 159.19 → 158.95** — only modest yen strength despite Brent -12%. CFTC corroborates: positioning offset, not deal-conviction.
6. **No MOF/BOJ/Bessent jawbone May 22-25** — Channel 3 dormant. Bessent May 12 affirmation remains live overhang.
7. **June BOJ swap pricing 74% → ~55-65%** (Polymarket 59.5%) post-CPI. ING maintained base case ("subsidy + base-effect noise").

### LAST SESSION (May 25-26 — Boot sync + Big 3 ESR Day 1 update)

**Phase A (May 25 PM):** Boot from 7:30 PM. boot.py 8.7s, 7/8 green. Three follow-up searches (CFTC, ESR scheduling, BOJ OIS + jawboning). 3-pass writeback (STATUS/CALENDAR, TIMELINE/PREDICTIONS, MEMORY). Pushed clean; push-train carried PROME 6/18 cluster commit.

**Phase B (May 26 AM — Big 3 ESR Day 1):** Nippon 195% + Meiji 208% disclosed 15:00 JST. Verified Nippon decomposition via direct PDF read (gaiyo p.7 ESR waterfall): -28pt driven by Resolution Life $10.6B M&A subsidiarization, NOT market stress. Both insurers' foreign books in unrealized gain. Market priced as capital action (USDJPY 158.95 → 159.24 yen WEAKER, FXY flat). Updated STATUS / CALENDAR / TIMELINE / PREDICTIONS / MEMORY to reflect Channel 1 thesis materially weakened, scenario weights deferred pending Sumitomo Wed May 27. Carry unwind probs: 7d 22→17, 30d 70→65, 60d 88→83. THESIS / CHANGELOG NOT updated yet — v1.5 deferred to post-Sumitomo.

**Synthesis insight:** The threshold-vs-mechanism finding logged 2026-05-25 fired in real-time on SAM-25 — hours after writing it. SAM-25 prints TRUE literally (Nippon <200%) but FALSE in spirit (no forced rebalance). Same pattern as SAM-26 but on a level-breach not a level-hold. Pattern recognition working; need to update prediction-writing template to bake in mechanism qualifiers.

**Channel re-weighting (current understanding):** Channel 1 (life insurer repatriation) demoted to "deferred mechanism / structural backstop." Channel 2 (carry / BOJ) now dominant remaining trigger. Channel 3 (intervention) defused on Brent collapse. CFTC -93,905 still primary asymmetric fuel, but for a Channel 2 fire now.

**No position change.** 13 shares + 1 Jun-18 $58 call unchanged from May 21 entry. Stop $55.05.

### NEXT SESSION

**Imminent catalysts:**
1. **🔴 Wed May 27: Sumitomo Life FY2025 ESR** (~15:00 JST / ~2-3 AM ET). Watch sumitomolife.co.jp/about/company/ir/settlement/. **The pattern-confirmation test.** If matches Nippon (capital-action-not-market-stress + foreign book intact) → Channel 1 v1.5 downgrade language warranted. If <200% via market stress → Channel 1 reactivates. Sumitomo's Symetra/US PC exposure is the wild card — $10.7B PC stack stress could surface here even if ESR headline looks manageable.
2. **🟠 Thu-Fri May 28-29: Tokyo May CPI.** Leading for June national. Core-core slip below 1.9% → BOJ pricing breaks lower from 55-65%.
3. **🟠 Fri May 29: CFTC weekly (May 22 data).** Watch for break of -102K cycle peak (new fuel high) or sudden cover.

**Action items:**
1. **First task next session: pull Sumitomo ESR result from IR page.** Check for: (a) ESR level, (b) decomposition (is the move M&A/capital-action like Nippon, or market-stress?), (c) Symetra/US PC exposure update, (d) JGB unrealized loss, (e) foreign securities mark.
2. **Post-Sumitomo synthesis call:** if pattern confirms (capital action driver), write v1.5 THESIS update with Channel 1 reframe. Update CHANGELOG with old/new view. Adjust scenario weights 70/25/5 → 75/20/5.
3. **Outbox signal bundling:** prepare LIQUID 🟡 signal (not 🔴) — counter-Channel-1 read for the May 22-26 window. Their UST demand thesis from Japanese repatriation needs same nuance. Bundle CFTC reload + Big 3 ESR + Channel 1 demotion into ONE consolidated signal. HENRY 🟠 mirror.
4. **Position eve check:** Sep $60 calls (Position A authorized) decision after Sumitomo. With Channel 1 deferred, the Sep $60C entry case rests more heavily on June BOJ hike + CFTC reload — less time-sensitive than pre-ESR.

**Hard trigger window:**
4. **🔴🔴 Tue Jun 16: BOJ MPM — base case hike.** SAM-21 ~57% (market 55-65%). SAM-24 (25bp @85%) still tracking.

**Pickup work (deferred):**
- Boot script enhancement: intraday-range alert when USDJPY single-day range > 2.5y (May 12 intervention-miss lesson).
- `usdjpy.py` touch tolerance band (May 6 low 155.05 fails strict ≤155).
- `jgb_auctions.py` TSV-append bug (auction parses fine; only append crashes).
- CHANGELOG candidate for v1.5: separate "J-ICS mechanism intact" from "JGB 30Y threshold holds" framing — deferred until durability of Iran MOU is known.

### PENDING (carry-over)
- v1.5 trigger gate: if Big 3 mutual ESR prints stress (<200% any), warrant scenario rebalance toward stress case 50/40/10 (currently 70/25/5).
- STRATEGY no-chase rule: Tranche 2 zone $58.00-58.25 was breached upward May 1; per rule forfeited at that level. May 21 $57.66 add was NEW entry zone, not a chase.

### INFRASTRUCTURE STATUS (persistent)
- Boot scripts: 7/8 green May 25 (jgb_auctions append bug; parser fine).
- Workbook auto-pulls: JGB_YIELDS May 22 (30Y 3.931% retraced), CFTC_JPY -93,905 May 19 (3rd build week), MOF_FLOWS May 10-16 (net buying), FXY_OPTIONS May 21.
- MOF_INTERVENTIONS catalog: Apr26 (¥5.48T) + May26 (¥4.3T). No #3 this week.
- STRATEGY.md canonical decision doc; STATUS scenario matrices subordinate.
