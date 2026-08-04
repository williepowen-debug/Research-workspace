# VIOLET SCRATCH — August 4, 2026 (Tuesday, ~12:30 ET — **PROME-directed proxy session, scoped. Market OPEN, basis TICK. FLAT.**)

> **Scope as given: refresh the dark credit panel at primary, grade the KB-VIO-090 tree against it, say what it changes for the cheap-tail window and the rising-vol design, make sure the 8/5 SOQ grader isn't orphaned, and try to REFUTE PROME's bifurcation read.**
> **🔑 The refresh landed and the escalation case got smaller.** ① **Credit widened while I was blind — my own warning was right.** ② **And the tree that grades it is saturated: BIN-A on all four lines, nothing new fires, six sessions running.** ③ **The clean "CCC alone" story lands on the month-end reconstitution date, where CCC's move distribution is 2.32× wider and BB's is untouched.** ④ **PROME's observation is correct and survives normalization; PROME's HY inference is refuted by index weights (CCC is ~11% of HY).** ⑤ **The cheap-tail window hit ARMING 3/4 on 7/31 and no surface knew — two stacked defects.** ⑥ **MOVE has a print that would un-break my broken confirm and I refused to bank it.**

---

## CHANGES SINCE (7/31 14:05 TICK → 8/4 ~11:25 ET TICK)

| | 7/31 TICK | 7/31 settle | 8/3 settle | **8/4 ~11:25 TICK** |
|---|---|---|---|---|
| VIX | 16.57 | 15.99 | 15.86 | **16.29** |
| VVIX | 90.84 | 91.64 | 90.81 | **89.54** ← **through 90, L1 MET on the tick** |
| VIX3M / ÷VIX | 19.20 / 1.1587 | — | — | **19.05 / 1.1694** ← steepest of the episode |
| VIX9D / ÷VIX | *(not pulled)* | — | — | **14.42 / 0.8852** |
| SKEW | 139.90 [7/30] | 141.23 | **139.96** | *(8/4 print is 17:00)* |
| **CCC OAS** | 🔴 DARK (10.13, 7/29) | — | — | ✅ **10.34 [7/31 data]** — 10.13 → **10.06** → 10.34 |
| **CCC−BB disp** | 🔴 DARK (8.37) | — | — | ✅ **8.61 [7/31 data]** — 8.37 → 8.32 → 8.61 |
| HY / BB / B | 2.87 / 1.76 / 3.03 [7/29] | — | — | **2.85 / 1.73 / 3.04 [7/31]** |
| IG / BBB / EuroHY / EM_HY | 0.81 / 1.00 / 2.64 / 3.11 | — | — | **0.79 / 0.99 / 2.65 / 2.99** |
| MOVE | 74.18 [7/29], no print | — | **80.48 [8/3]** ⚠️ | *(no 8/4 print)* |
| **cheap-tail** | 1/4 [7/30 row] | **3/4 ARMING** *(never written)* | **2/4** *(L4 was false)* | L1 met on the tick |

---

## WHAT I DID

1. ✅ **Refreshed the credit panel at primary and verified it twice, independently.** Raw `api.stlouisfed.org` calls per series **then** `fred_fetch.py --summary` — agreeing to the basis point on all 8. FRED is reachable again; **KB-VIO-170's outage is over.** ⚠️ **Latest published = data-date 7/31. 8/3 and 8/4 are NOT out** — `fred_fetch` itself expected 8/3 and got 7/31. **I did not let a reachable endpoint become a claim about sustain.** → **KB-VIO-172.**
2. ⚠️ **Graded the KB-VIO-090 tree — and the grade is that the tree has nothing left to say.** BIN-A on **all four** lines (CCC 10.34 ≥9.65 · BB **1.73 = 1.73** · HY **2.85 = 2.85** · disp 8.61 ≥8.00). **All four were already tripped on 7/29 (KB-VIO-157) and on 6/25 before that (KB-VIO-107).** A four-line any-one-of-N escalator, saturated for six sessions, cannot distinguish CCC 10.13 from 10.34 from 12.00 — **descriptor, not trigger** (`finding_escalation_line_needs_delta_not_level`). **Defect registered; threshold NOT moved.** Two of the four lines sit *exactly* on their thresholds and un-fire on a 1bp tightening.
3. 🔑 **Found the month-end artifact, and it is the session's real finding.** Over 782 daily changes (2023-08 → 2026-07), on the last business day of the month: **|ΔCCC| 16.44bp vs 7.08bp = 2.32×**, signed **+9.94bp vs −0.34bp**, **P(ΔCCC ≥+20 | month-end) 25.0% vs 2.28%**. Dispersion **3.24×**, signed **+8.56bp**. **The discriminator is that it is series-specific: BB shows none (0.96×)**, HY 1.16×, B 1.20×. That is index **reconstitution**, i.e. a level shift in the *instrument*. **7/31 is that date.** → **KB-VIO-173.**
   - ⚠️ **And I stopped myself from over-claiming it:** after the 8 prior month-end CCC jumps ≥+20bp, **BB/B followed within 5 sessions in 5 of 8.** The artifact is a measurement caution; **it does not license a dismissal.**
4. ✅ **Adjudicated PROME's bifurcation claim — three claims, three verdicts.** → **KB-VIO-174.**
   - **(A) "CCC alone widened" — TRUE**, verified at primary, and **it survives normalization** (CCC +2.07% vs BB −1.70%, IG −2.47%). The lens-inversion PROME flagged as a risk **was checked and did not occur**.
   - **(B) "HY is a CCC story wearing an HY label" — REFUTED.** OLS ΔHY ~ (ΔBB, ΔB, ΔCCC), n=525, **R² 0.9920**, weights sum 1.004 → **BB 0.597 / B 0.301 / CCC 0.106.** CCC's +28bp delivered **+3.0bp** to HY. July widening HY +14bp splits **BB 39% / B 23% / CCC 37%**, and **all three tiers widened** (BB +12, B +14, CCC +64).
   - **(C) "bifurcation not broad stress" — UNDETERMINED**, and 7/31 cannot settle it. **Uniqueness test is the tell:** [ΔCCC ≥+25 & ΔHY ≤+3] occurs **exactly once in 782 obs — 2026-07-31.** A 1-in-782 configuration landing on the one day with a known composition mechanism is more likely the mechanism.
   - 📌 **Pre-registered the discriminator at 45%** — resolves on the **8/7 data print**: TRUE iff BB ≤1.78 **and** B ≤3.09; FALSE iff BB ≥1.83 **or** B ≥3.14; NO-VERDICT between. **Confidence set BELOW the unconditional base rate (67.9%) because the conditional-on-this-setup rate is 37.5% (n=8)** — registering 45% on a claim I argued *for* is the honest number.
5. 🟠 **Found the cheap-tail window at ARMING (3/4) on the 7/31 settle, six days late.** Two stacked defects: **the 7/31 row was never written** (session closed pre-close) and **L4 was reading falsely anyway** — `CATALYSTS.tsv` held **no macro-data row of any kind**, reporting "nearest HIGH/MED 43d" when **NFP July is Fri 8/7, 3 days out** (BLS date confirmed, carried by LABOR). **Root cause is structural: forward-state maintenance prunes on firing and never replenishes** — pruning has a trigger, replenishment has none. Added the 8/7 row, **repaired the ledger** (7/31 ARMING inserted, 8/3 corrected 1/4 → 2/4), **line unchanged at ≤21d.** → **KB-VIO-175.**
6. ⚠️ **MOVE printed 80.48 [8/3] — back through the 75-76 line it broke — and I did not bank it.** `^MOVE` is **incoherent across window lengths**: `5d` returns one bar (8/3), while `1mo`/`2mo`/`3mo`/`6mo` **all end 7/17 at 70.88**. `fetch.py` serves the same value from the same upstream — **one witness in two coats.** **KB-VIO-131 is the precedent: same series, same ~80 level, wrong by a day.** Conf **C3**, vector **held at 2**. → **KB-VIO-176.** 🔑 **This is the number that would let me un-break my own broken confirm, so it got the harder check, not the easier one.**
7. ✅ **Scored two vectors DOWN on my own initiative.** **Credit 5 → 4** on a print that went my way (month-end date · quality sort collapsed · ~11% channel). **GEX dropped to UNSCORED** — HENRY's chain is 4 sessions stale and my own 7/31 SCRATCH told me to refresh or drop. **Denominator 60 → 55; score 24/55.**
8. ✅ **Verified the 8/5 SOQ grader is armed and NOT orphaned — on CONTENT, not existence** (the 7/31 lesson applied). Both `CATALYSTS.tsv` and `CALENDAR.md` carry it, both cite **0.591 @≤10 DTE**, neither carries the retracted 0.28. Added a dedicated STATUS block with the line, the four things it grades, the instrument caveat (**official CBOE SOQ, not the ^VIX open**), and the pre-print tape context.

---

## NEXT SESSION (priority-ordered)

1. 🔴 **RE-PULL FRED FOR THE 8/3 AND 8/4 PRINTS.** They were not published at pull time (~12:3x ET 8/4). **These are the first non-month-end prints after 7/31 and they are the whole ballgame** on whether the CCC move was composition or escalation. ⚠️ **Do not read a cache-served 200 as a fresh print** — confirm the data-date ADVANCED (`finding_partitioned_source_returns_stale_window_at_200`).
2. 🔴 **8/5 — GRADE THE SOQ.** Official **CBOE VIX SOQ**, not the ^VIX open. Line **>20.45**. Score all four items (my fade verdict, my no-re-entry call, TERRY's 0.591 beta, HENRY's steelman). ⚠️ **It will probably resolve in my favour — bank it as a right answer through a partly-repaired premise (KB-VIO-157), not a clean hit.**
3. 🔴 **CORROBORATE MOVE 80.48 AT A SECOND SOURCE.** investing.com's historical table is the one that worked for KB-VIO-131. Need the **7/18 → 8/3 path**, not a spot quote. Until then confirm-3 stays broken and the vector stays at 2.
4. 🟠 **8/7 NFP — the pre-registered credit discriminator resolves on this data print** (publishes ~8/10). Bands are written in KB-VIO-174. **Grade it mechanically; do not re-derive the bands.**
5. 🟠 **The 7/31 15:30 COT was never pulled and is still owed** (report-date 7/28). And the **8/4-data** print is the first that can speak to the yen move.
6. 🟠 **CATALYST-FEED COMPLETENESS is now a standing gap, not a one-off fix.** July CPI (~8/12) is **still not added** — no confirmed date exists in the fleet and inventing one is the defect itself. **Ask LABOR/CARL for the confirmed August macro dates.** ⚠️ **A twin-consistency check cannot detect what is absent from BOTH twins** — this needs an *external* completeness check.
7. 🟡 **The KB-VIO-090 re-base is now a real thesis question.** The tree needs a **delta leg** or a re-based level or it will keep reading BIN-A through anything. **Will-gated thesis bump, not a session call.** ⚠️ **This blocks the rising-vol design (Option 1) from using "credit confirms" as its trigger** — such a trigger would already be firing today at VIX 16.29.
8. 🟡 **Unprocessed inbound, still flagged not consumed:** `inbox/2026-07-30_from-DAEDALUS_stand-down-gate-is-a-ratchet.md` — now **5 days** old, names live thesis territory. **Read it at the next full boot.**
9. 🟡 **HENRY gamma chain** — request a refresh, or the vector stays unscored.

---

## CARRY-FORWARD

- **🔑 A DARK GATE HAS NO OWNER AND NO RE-CHECK TRIGGER.** VIOLET went dark on credit on 7/31, wrote *"do not read the absence of a widening print as an absence of widening"* — **the single best sentence available** — and then **nobody pulled it for six days.** The warning was correct *and* it changed nothing, because it lived in a SCRATCH line rather than in a mechanism. **A DARK state needs a dated re-check obligation on a forward surface, exactly like a prediction does.**
- **🔑 THE DATE A NUMBER PRINTS ON IS PART OF THE NUMBER.** CCC +28bp is a stress signal on 7/28 and an ordinary reconstitution move on 7/31, and **nothing in the value distinguishes them.** The general form: before reading a level as escalation, **ask what the calendar does to that specific series on that specific day** — and check whether the effect is *series-specific*, because a series-specific artifact is a composition tell while a ladder-wide one is a macro tell.
- **🔑 A CONSISTENCY CHECK BETWEEN TWO SURFACES CANNOT SEE WHAT IS MISSING FROM BOTH.** My 7/31 carry-forward was *"existence-parity is not agreement."* This is one rung worse: **the row did not exist at all**, both twins agreed perfectly, and both omitted the entire August macro calendar. **n=4 on this class.** The fix is not a better twin check — it is an **external completeness check** against a source that knows what *should* be there (here, LABOR's own docket, dated 7/31 and sitting in the repo the whole time).
- **⚠️ A FEED THAT ONLY EVER SHRINKS BIASES EVERY GATE BUILT ON IT.** `CATALYSTS.tsv` prunes on firing and never replenishes, so **L4 decays toward ⬜ by construction** and the cheap-tail window reads DORMANT more often than it should. **Any leg keyed to a curated list inherits that list's decay** — the leg was never wrong, the list was.
- **🔑 THE TWO NUMBERS THAT AROSE THIS SESSION BOTH FAVOURED THE ESCALATION CASE, AND BOTH GOT CUT.** Credit printed a new high → **scored down 5→4**. MOVE printed back through a line I had marked BROKEN → **refused, held at 2**. `finding_asymmetric_rigor_counterparty_claims` points inward: **the number that lets you retract needs the same rigor as the one that lets you commit** — and here that meant declining a datum that would have made my own dashboard look better.
- **⚠️ MY CONFIDENCE WAS SET BY THE CONDITIONAL BASE RATE, NOT BY HOW GOOD THE ARGUMENT FELT.** The month-end analysis is the cleanest measurement I have produced in weeks and it *felt* like a 70%. The conditional history (BB/B followed 5 of 8 times) says **37.5%**. **Registered 45%.** A tidy mechanism is not evidence about the world; it is evidence about the instrument.

---

## OPEN HYPOTHESES *(flagged, not actionable)*

- **The July HY widening may be two unrelated processes wearing one index name:** a slow BB/B grind (+12/+14bp over 11 sessions, the majority of HY's move) and a separate CCC-cohort deterioration (+64bp). **If so, the CCC leg is a distressed-issuer story and belongs to LIQUID/BROCK, not to a macro credit read.** Needs issue-level breadth — **asked for four times now** (KB-VIO-107 registered it as the discriminator; KB-VIO-157 records three prior asks).
- **The month-end effect may be exploitable as a de-noising filter, not just a caution:** if CCC's month-end move is largely composition, then a **month-end-excluded CCC series** would be a cleaner credit-to-vol input than the raw one. **Not backtested. Do not use until it is.**
