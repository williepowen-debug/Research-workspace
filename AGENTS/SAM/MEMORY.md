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

### LAST SESSION (2026-05-26 — Big 3 ESR Day 1 + maintenance pass + PROME TRACKER cleanup + Sumitomo pre-watch)

**Day arc:** 4 phases — (A) AM Big 3 ESR resolution → (B) boot-doc maintenance pass → (C) PROME TRACKER cleanup (2-pass) → (D) Sumitomo pre-watch + PROME Phase 1 stability integration.

**Channel 1 verdict (Phase A):** Nippon 195% M&A-driven (-28pt = Resolution Life $10.6B sub) + Meiji 208% manageable. Foreign books in unrealized GAIN at both. Tape priced as capital action (USDJPY 158.95→159.24, FXY flat). **"ESR forces UST sale" mechanism not evidenced.** Channel 1 demoted to deferred mechanism / structural backstop. Channel 2 (June BOJ 55-65%) now dominant remaining trigger. Channel 3 dormant on Brent -12%. Carry unwind probs: 7d 22→17, 30d 70→65, 60d 88→83. SAM-25 threshold-vs-mechanism trap fired in real-time.

**TRACKER cleanup (Phase C):** PROME ask `prome_2026-05-26_insurer_tracker_cleanup_request.md` — replaced crude "ANY ESR <200% → 🔴" rule with mechanism-aware 5-row table; added Channel 1 "downgraded not dead" banner; refreshed key dates + Oct 2025 survey down-weighted. Pass 2 audit (Will-prompted "anything else?") caught 2 actively-wrong items NOT in PROME scope: JGB 30Y "BREACHED" vs STATUS 3.931% retraced (cross-doc conflict); Apr 12 Hormuz blockade section was v1.3-era backwards framing. **New auto-memory:** [[finding_followup_audit_pass]] from this pattern. Completion note to PROME via Convention B outbox.

**Sumitomo pre-watch + PROME Phase 1 signal (Phase D):** Sumitomo not out yet (~10 hrs early at session end). News sweep found: (1) Iran/Hormuz MOU hardened May 23-24 (Trump "largely negotiated"; Axios framework; Munir in Tehran; Tehran obstruction accusation = friction signal); (2) Bessent-Katayama May 19 Bloomberg adds G-7 support framing to Channel 3. PROME signal `prome_2026-05-26_phase1-inversion-stability-may-tbal-lag-test.md` arrived — independently verified v1.4 trade-balance numbers cross-surface (2nd concrete instance of [[finding_cross_surface_validation_pattern]]); raised forward-question on Phase 1 inversion stability. Integrated as TIMELINE Brent-entry extension + Bessent May 19 entry + THESIS § OIL-IN-YEN Phase 1 stability watch + CALENDAR Jun 18-19 routing row. **No STATUS edit** — Will pushed back when I proposed putting narrative into STATUS; routed correctly to TIMELINE/THESIS/CALENDAR. **New auto-memory:** [[feedback_doc_routing_data_drops]] from this catch.

**Commits pushed:** b1f7be2a (maintenance) + beb1c124 (workbook) + 43a1e308 (TRACKER cleanup) + 271f70dd (Sumitomo pre-watch).

**Position unchanged:** 13 shares + 1 Jun-18 $58C. Sep $60 calls deferred. Stop $55.05.

### NEXT SESSION

**Imminent catalyst — IMMEDIATE on boot:**
1. **🔴 Wed May 27: Sumitomo Life FY2025 ESR** (~15:00 JST / ~2-3 AM ET). IR: sumitomolife.co.jp/about/company/ir/settlement/. **Pattern-confirmation test.** Check: (a) ESR level + decomposition (M&A vs market stress), (b) Symetra/US PC ($10.7B stack) update, (c) JGB unrealized loss, (d) foreign securities mark, (e) any explicit foreign-bond reduction language. Routing per new TRACKER table: M&A-style sub-200% → 🟡 counter-thesis; stress-driven sub-200% → 🔴 LIQUID + PROME; 200-220% manageable → 🟠 watch.

**Other near-term:**
2. **🟠 Thu-Fri May 28-29: Tokyo May CPI.** Core-core <1.9% → June BOJ pricing breaks lower from 55-65%.
3. **🟠 Fri May 29: CFTC weekly (May 22 data).** Watch for break of -102K cycle peak.
4. **🟠 ongoing: Iran/Hormuz MOU status.** Binary watch — signing → Brent further collapse + Phase 2 accelerates; Tehran walk → Brent snapback + intervention #3 zone reactivates. Brent +2.3% Tue ($94.53 → $96.71) consistent with friction priced back in.

**Action items:**
1. **Pull Sumitomo ESR from IR page first** — direct PDF read for decomposition (M&A vs stress).
2. **If Sumitomo confirms pattern (M&A-style):** write v1.5 THESIS update with Channel 1 reframe; CHANGELOG with old/new view; scenario weights 70/25/5 → 75/20/5. LIQUID 🟡 counter-thesis signal.
3. **If Sumitomo breaks pattern (stress-driven <200%):** Channel 1 reactivates per new TRACKER 🔴 row; consolidated LIQUID + HENRY 🔴 signal; reconsider scenario weights toward stress case.
4. **Position decision deferred:** Sep $60 calls (Position A authorized) — case rests on June BOJ + CFTC reload + Sumitomo read.

**Hard trigger window:**
- **🔴🔴 Tue Jun 16: BOJ MPM — base case hike.** SAM-21 ~57% (market 55-65%); SAM-24 (25bp @85%).
- **🟠 Jun 18-19: May trade balance** — PROME-framed Phase 1 stability lag-test; mechanism-aware routing in CALENDAR.

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
- Boot doc structure post-2026-05-26 cleanup: see `MAINTENANCE.md` for the 6-candidate audit pass + PROME TRACKER cleanup entries + conventions established.
