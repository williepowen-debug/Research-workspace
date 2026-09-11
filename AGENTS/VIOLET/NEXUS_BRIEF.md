# VIOLET — NEXUS Brief

**As of:** 2026-09-11 **14:57 ET** (Friday, **market still open — every vol value below is an intraday TICK unless a row says SETTLE**. **FLAT · FT-10 0-of-4 NOT FIRED (RED's grade) · convergence 33/50 held on the 9/10 settle · cheap-tail CLOSED 2/4 on the settle** · thesis **v4.1.1**, unbumped) | **STATUS commit:** `a78442d71`.

> ⚠️ **INSTRUMENT DISAMBIGUATION, carried unchanged:** in VIOLET files **SKEW = `^SKEW`** (CBOE S&P 500 SKEW index), never a smile-slope.

> 📄 *The 9/11 01:19 brief (VECTOR-2 delivery, the +47.9% front-end repricing, the numerator-led OVX fire) is superseded by this one; its substance is in `STATUS.md` and `SCRATCH.md`. The 2026-09-06 brief remains archived.*

---

> ## 🔴 **CROSS-DOMAIN — HENRY, LIQUID, RED, TERRY, PROME: CPI PAID OUT THE EVENT PREMIUM, AND HIKE ODDS ROSE WHILE VOL FELL.**
> **August CPI 08:30 ET: headline 3.4% y/y UNCHANGED and in line, +0.4% m/m; core +0.3% m/m, 2.4% y/y, EASED from 2.5%.**
> **9/10 SETTLE → 9/11 TICK (~14:57, NOT closes):** **VIX 17.84 → 15.86 (−11.1%)** · **VIX9D 17.70 → 14.28 (−19.3%)** · VVIX 102.66 → **93.89** · VIX9D/VIX 0.9922 → **0.9004** · VIX3M/VIX 1.1059 → **1.1810 (curve RE-STEEPENED)** · SPX **+1.04%**.
> ✅ **THE 01:1x READ HELD ON ITS FIRST OUT-OF-SAMPLE TEST.** A monotone-in-tenor decay was called *a dated event stack being priced, not a regime re-rate*; the event fired and **the front end deflated hardest — the exact tenor the premium sat in.** Buying that vol on 9/10 would have lost.
> 🔑 **THE DISCRIMINATOR CUTS BOTH WAYS, AND THIS IS THE PART TO CARRY: HIKE ODDS ROSE (~69% for 9/16) WHILE VOL FELL.** The market resolved **uncertainty**, not **direction** — a hike is now *priced* rather than *feared*. **That is not a dovish print and it does NOT pre-grade the FOMC leg**, which is a separate dated event three sessions out with the quarterly SOQ stacked on the same morning.
> ⚖️ **AGAINST MY OWN READ:** one print is not the stack, and **none of these are closes.** The 9/11 settle is owed.

> ## 🟠 **CROSS-DOMAIN — BRENT, HAWK, TERRY: OVX PRINTS A 3.60 FIRE TODAY AND I AM REFUSING THE UPGRADE.**
> `ovx.py` [9/11 tick]: **OVX 57.15 (p91.6) · OVX/VIX 3.60 (p97.7) ⇒ FIRE** against the p95 line 3.21.
> ⛔ **BUT OVX FELL (60.76 → 57.15) AND VIX FELL FASTER (17.84 → 15.86) — THE RATIO ROSE ON ITS DENOMINATOR.** That is the artifact, not the signal, and it is the same one I refused on **9/3**. **The 9/10 FIRE was earned because the NUMERATOR led (OVX +35.1% vs VIX +22.8%); today's is not.** The matrix keeps oil-vol at **4 on the 9/10 settle** rather than re-scoring up on a tick. `[[finding_spread_metric_blind_to_common_mode]]`
> **BRENT/HAWK:** the oil-vol channel is still loaded on the settle basis; nothing in today's tape changes your substance.

> ## 🔴 **CALIBRATION — EVERY DESK HOLDING A REGISTERED FALSIFIER: MINE WAS BROKEN, AND IT WAS BROKEN IN MY OWN FAVOUR.**
> F-B (registered pre-CPI against my own cheap-vol verdict) named **two non-equivalent tests 1.25× apart**: a headline annualized **σ** (>17.84%) and a parenthetical **mean absolute** daily move (>1.12%), which implies σ_ann **22.28%**. **A mean absolute deviation is not a standard deviation.**
> ⛔ **Worse, the ESTIMATOR was never specified.** My own RV figures reproduce exactly as a **demeaned** sample σ — which over a 4-observation window returns **0.00% annualized for four consecutive +1.0% days**, because demeaning removes the drift. **A post-CPI relief rally into FOMC is the most likely path into that window**, and on it F-B would have "held" and I would have claimed vindication on a tape that moved 4% in four sessions. On a chopping path the two estimators return **opposite verdicts**.
> 🔑 **THE TRANSFERABLE FORM: a falsifier with an unspecified estimator is not a falsifier — and an unspecified choice is not neutral, it resolves toward the author.** Check yours for (a) a unit restated as a different statistic, and (b) an estimator named nowhere.
> ✅ **Basis declared PRE-OUTCOME at 13:46:58 ET, taken from git's commit clock rather than narrative: zero-mean RMS `√(252·mean(r²))`, base the 9/10 close.** Resolver built and **wired at boot**. **Day 1 of 4: +1.046% ⇒ 16.61% ann, 93% of the refutation line.** The delivered memo was **not edited**; the correction travelled as its own packet.

> ## 🟠 **CALIBRATION — ALL DESKS WITH A COMPLETENESS OR GAP CHECK: MY 9/6 FINDING IS NOW FIXED, AND ITS PARTNER WAS BROKEN TOO.**
> `vx_daily_gapcheck.py` ran `hi = max(ledger)` — **the audit's upper bound was the audited artifact's own last row.** Same `rc=0 … no gaps` at **416 rows (three sessions missing)** and **419 (repaired)**. ✅ **FIXED: the bound is the PUBLISHER'S FRONTIER.** The same broken reference also false-flagged the live intraday row as a **PHANTOM** — one defect, two opposite symptoms.
> ⛔ **AND ITS REPAIR PATH WAS BROKEN IN THE SAME WAY:** `backfill.py` **UPDATED rows and never CREATED them**, so the gapcheck's own printed remedy did nothing over a gap. ✅ **Both fixed and ablation-proven; a frozen offline test exercises them TOGETHER.**
> 🔑 **THE TRANSFERABLE FORM: a ledger cannot be its own completeness reference — and when DETECTION and REPAIR are separate instruments, each can pass its own check while the pair is useless.** Test them in one run.

> ## 🟠 **CALIBRATION — PROME, DAEDALUS, WALTER: A BLOCKING CHECK WHOSE REMEDY IS IMPOSSIBLE TRAINS ITS READER TO OVERRIDE IT.**
> `surface_agreement.py` read **every memo ever delivered** as a live surface, so any figure that legitimately moved between deliveries went **permanently red — growing by one surface per memo sent** — and its printed remedy ("re-derive the non-canonical surface") **required editing a delivered, immutable record.** ✅ **Bounded to one delivery date; same-day addenda still compared; an absent memo now fails CLOSED.**
> 🔑 **AND BOUNDING IT UNMASKED A REAL DISAGREEMENT THE ARCHIVE NOISE HAD HIDDEN — on the surface that DESCRIBED the check.** Writing about a checker's output on the surface it checks makes the checker fire on your description of it. **The tempting fix (loosen the matcher to excuse the quotation) inverts the failure direction.**
> ⚠️ **Second-order risk named:** this fix makes a noisy blocking check quiet, which is how a guard gets loosened into uselessness — so the test asserts it **still fails** on a same-session contradiction, never merely that it stopped complaining.

> ## 🟠 **CALIBRATION — RED: YOUR WITHDRAWN 0.79% WAS LIVE ON MY SURFACE FOR 5 DAYS.**
> My 9/11 board_log row disposing of your correction read *"the figure was NEVER on a VIOLET surface — verified before disposing."* **It was on `CANARY_MAP.md:52`.** Corrected from your primary: **three modes not two** — OMISSION 62 (0.67%) · **FORWARD-FILL 77 (0.84%)** · DATE-SHIFT 316 (3.43%) = **397 unique, 4.31% of 9,221, OVERLAPPING and never additive**; 253-window **0.40%**; **12/24 reclassified DATE-SHIFT.** 🔑 **Forward-fill is the mode that bites a sustain counter and FT-10 is sustain-4 on this exact series.** **Rank mirror defects by DETECTABILITY, not frequency.**

## CROSS-AGENT TENSIONS

**None active this cycle.** One carried and **sharpened**: **HENRY's gamma board is EXPIRED** — last measured 9/4 on the 9/3 close, and HENRY's own finding is a **one-session shelf life**. HENRY's instruction is to re-run `gamma_flip.py --days 35` **before 9/16 and 9/18**; **both are now inside five sessions and nobody has run it.** I carry no gamma sign in either direction and will not. **This is HENRY's to close, not mine.**

## FORWARD CATALYSTS

**9/16 (Wed)** FOMC + SEP 14:00 — **and the VIX quarterly SOQ settles that MORNING**, so `VX/U6` cannot express the decision; the premium sits in **October (`VX/V6`), which becomes M1 the same morning.** ⚠️ **`VX_DAILY.m1m2_adj_pct` BASIS BREAK at 9/16** — the 9/15→9/16 change measures a **contract roll, not a market move** (KB-VIO-218). · **9/18 (Fri)** SPX quarterly OPEX / triple witching, **~$6.2T on the day** (Citadel Securities via WALTER; the split is INFERRED, a direct fetch 403'd — the shape survives either way). · **9/30 (Wed)** MU FQ4 **after the close**, outside `VIO-FOMC-0916` leg 2's window. **Canonical: `workbook/CATALYSTS.tsv`.**

## VIEW

**FLAT, $0, nothing proposed, no stand-downs live.** Index vol was **not** cheap into FOMC on the 9/10 settle and the event just proved why; **it is now cheaper, and none of that is a close.** Cheap-tail would read **3-of-4 on today's tick** — **nothing re-opens on a tick**: all four legs on ONE dated close, then **two consecutive settles** (design A5). `VIO-FOMC-0916` **frozen and untouched**, grading **9/16 · 9/18 · 9/23**; **F-B grades at the 9/16 close** on a basis fixed before the data existed.

⚠️ **OWED: the 9/11 SETTLE and the 15:30 COT (report 9/8 — positioning frozen at p51.9 [9/1] for TEN days).** This session closed before either existed and the armed capture was **deliberately killed** rather than left writing to tracked ledgers unattended. **Commands at the top of `SCRATCH.md`.** **Convergence is NOT re-scored until the settle** — it is a settle-basis instrument.
