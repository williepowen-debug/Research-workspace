# MIDAS-08 — REGISTRATION: the M1 successor test. Did the crowded gold spec long unwind into a −6.35% week?

**Registered 2026-09-02 ~15:4x ET — BEFORE the 2026-09-04 15:30 ET CFTC release.** Deliberate, and the reason is the whole point: the conditioning fact is already visible and the answer is not.

## 1. Why this row exists

**M1 sits at 4 and has no live test.** MIDAS-06 graded TERMINAL 8/31 and its upgrade-trigger cell reads *"CONSUMED — any further M1 escalation needs a NEW registered test."* Since then the desk has accumulated **unregistered observation** about M1 — BOND's 9/1 breakeven tension, the gold basis work, the COT crowding — and none of it can move a score, correctly, because none of it was registered in advance.

**The question is the one this desk and BOND both explicitly declined to rule on 9/2:** is gold's premium **spec-funded** or not? MIDAS's own pre-registered falsifier (COT #3) fired *against* the desk's read on 8/28 — net/OI **56.86%**, Δ **+2.17pp**, composition **CHASED** (NC long **+20,257**, NC short **−888**, OI **+21,697**), 99.8th percentile. That established *"a meaningful part of the 8/19 residual is spec flow"* — and explicitly **not** how much, and **not** that it survives.

## 2. ⚠️ THIS IS A ONE-LEG FORECAST, NOT A 2×2 — and saying so is the honest design

The first sketch was a 2×2 over {positioning unwinds / holds} × {gold holds / falls}. **That is wrong, and the flaw is instructive: both legs are as-of 2026-09-01, so the PRICE leg is ALREADY OBSERVED.** A branch set that treats a known quantity as a forecast dimension manufactures the appearance of a harder test than it is.

⇒ **The price move is a FROZEN CONDITIONING FACT, stated here, not a branch:**

> **`GCZ26` (front, named per WQ-91): 4,694.50 [close 2026-08-25] → 4,396.40 [close 2026-09-01] = −6.350%.**
> The COT reporting window (as-of Tue → as-of Tue) is exactly 2026-08-26 → 2026-09-01.

**Only the positioning response is unknown.** The test is therefore sharp precisely *because* the price leg is settled: **a 99.8th-percentile crowded long was handed a −6.35% week. Did it run?**

## 3. Empirical basis for the boundary — measured, not chosen by feel

Source: `sources/cot_gold_history_2010_2026.tsv` (COMEX full-size gold, code 088691, legacy futures-only), frozen 2026-08-28.

**Full sample, weekly Δ net/OI, n=867 (2010-01-05 → 2026-08-18):**
`p1 −7.86 · p5 −5.47 · p10 −3.97 · p25 −1.92 · p50 −0.03 · p75 +1.78 · p90 +4.19 · p95 +5.80 · p99 +9.16` · mean **+0.011** · sd **3.315** · min −12.69 · max +15.26.

**Conditional on the PRIOR week ≥ 56.0% — ⚠️ n=7 ONLY, over 16.6 years:**
`−2.80 · −1.82 · −1.70 · −1.03 · −0.85 · −0.17 · +0.80` — mean **−1.081**, median **−1.029**; **6 of 7 negative (86%)**, 4 of 7 ≤ −1.00pp (57%), **1 of 7 ≤ −2.00pp (14%)**.

⛔ **n=7 IS TOO SMALL TO CARRY A THRESHOLD AND I AM NOT LETTING IT.** This desk has already published one base rate off a too-short inherited window and had to correct it (KB-042: *"0 of 19, never observed"* → 1.81% on the full series). **The boundary below is therefore taken from the FULL-sample distribution (n=867); the conditional set is reported as context with its n stated, and is not load-bearing.**

## 4. THE FROZEN LETTER — branches are MECE per WQ-142

**Measured quantity:** Δ net/OI (pp) = [net/OI, as-of **2026-09-01**] − **56.8600%** [as-of **2026-08-25**, frozen baseline, from the 2026-08-28 release].

| Branch | Condition (half-open; **boundary owner named**) | Reading | Consequence |
|---|---|---|---|
| **(a) UNWIND CONFIRMED** | **Δ ≤ −2.00pp** *((a) owns −2.00)* | The crowded long ran into the decline ⇒ spec flow was a **marginal price-setter**, not just present | **M1 4 → 3** |
| **(b) INDETERMINATE** | **−2.00pp < Δ < +1.00pp** *(open both ends)* | Bleed or drift; no clean read at this resolution | **M1 holds 4.** No change |
| **(c) CROWDING HELD OR EXTENDED** | **Δ ≥ +1.00pp** *((c) owns +1.00)* | Spec held/added **through a −6.35% week** ⇒ conviction money, not hot money | **M1 holds 4**, and the **COT #3 impeachment is materially WEAKENED** — recorded, **not** scored |
| **(d) NO-VERDICT** *(declared catch-all)* | Vintage not published by **2026-09-08**; OR `cot_gold.py` totals reconciliation fails; OR the in-row as-of ≠ 2026-09-01; OR contract code 088691 absent/relabelled | Instrument failure, **not** a market result | **No change.** Re-register or retire |

✅ **MECE:** (a) ∪ (b) ∪ (c) covers ℝ with no overlap; (d) is the declared catch-all for non-observation. **No observation can fall outside the set** — the defect WQ-142 was ruled against (2.40 sat in both MIDAS-06 (a) and (d); gold $4,050–$4,340.70 with DFII10 ≥2.40 fit no branch).

⛔ **The WQ-142 NARROW band (2.37–2.43) is NOT attached, deliberately and not by omission: this row references no DFII10 leg.** The band is registered as an admissible print set only on DFII10-referenced rows.

**Pre-registered branch masses** (sum 1.00): **P(a) = 0.40 · P(b) = 0.40 · P(c) = 0.18 · P(d) = 0.02.**
⚠️ **P(a)=0.40 DEPARTS FROM THE 14% CONDITIONAL BASE RATE AND THE REASON IS STATED SO IT CAN BE JUDGED:** the conditional set is n=7 of *ordinary* crowded weeks, whereas this window carries a **−6.35% price shock** and a composition already measured as **CHASED** — chasing money is weak money. **If (b) or (c) fires, that departure was wrong and this note is the evidence of it.**

## 5. Resolution

**Date:** Friday **2026-09-04**, after the **15:30 ET** CFTC post. **Instrument:** `python3 cot_gold.py --expect 2026-09-01` — ⛔ **never grade the first response after 15:30**; the raw file serves last week's vintage on a clean 200 (`finding_partitioned_source_returns_stale_window_at_200`). Exit 3 = WAIT, poll. Totals reconciliation (OI == TotRept+NonRept, both sides) must PASS before any position number is read.
**Contract:** COMEX full-size gold, code **088691**, legacy futures-only. Micro gold is a different code and corrupted 6 of 15 weeks on this desk's first pull (KB-036).
**Confidence tier:** **PROVISIONAL** — the boundary is a full-sample percentile, but the *conditional* evidence for mean-reversion from crowded levels is n=7.

## 6. If falsified — the action, written before the result

**If (c) fires**, my published line *"a meaningful part of the 8/19 residual is spec flow"* must be **re-read in public as too strong**, and the 8/28 COT #3 grade recorded as a falsifier that fired on a configuration which then **failed to behave like one**. ⇒ Write it plainly on STATUS and route the correction to BOND, which adopted that carve-out verbatim on 9/1. **A falsifier that fails to fire is information about my falsifier, not a vindication of my read.**

**If (a) fires**, it does **NOT** retroactively validate MIDAS-06 or re-open MIDAS-07, and it does **not** establish that *all* of the premium is positioning — only that spec flow was a marginal price-setter over one week. **M1 → 3 is the letter's own prescribed consequence, not a re-rate.**
