# MIDAS — I1 TRACKED-BASELINE DEFECT: THE MEASURED EFFECT

**Written:** 2026-08-23 (Sun, mkts CLOSED) · **Channel:** I1 (copper — Dr. Copper / China) · **Status:** ESCALATION, not a repair. **No band moved. No score moved. Zero capital.**
**Discharges:** the "flagged-not-repaired, mine to escalate **with measured effect**" item open since 2026-08-21 (STATUS open-item 3, SCRATCH carryover). PROME 8/23: *"I'd rather you escalate it early than clean."*
**Reproducible:** `analysis/measure_i1_baseline_drift.py` — pulls the same westmetall series `metals_watch.py` uses and recomputes the band's own denominator as-of past dates.

---

## 1. THE DEFECT IN ONE LINE
The I1 inventory bands grade LME copper stock as a **% above the trailing-2-year rolling median**. That denominator is **TRACKED, not frozen** — so **the same tonnage receives a different grade depending only on the date you grade it.**

## 2. WHAT I ORIGINALLY FLAGGED (8/21) — AND WHY IT UNDERSTATED THE PROBLEM
The flag was raised on **n=1**: the median moved `244,025t → 240,325t`, so the same 8/13 tonnage graded **−14.9% then and −13.6% now**, a **1.3pp** wobble. A second instance appeared on **8/23** (`240,325 → 239,925`). **At n=2 and ~1pp this reads like rounding noise. It is not.**

## 3. THE MEASUREMENT — the denominator, by as-of date
Trailing-2yr rolling median of daily LME copper stock, recomputed exactly as the live band computes it, as of each date (series n=669, 2024-01-02 → 2026-08-21):

| as-of | 2yr median | n |
|---|---:|---:|
| 2026-08-21 | **239,925 t** | 507 |
| 2026-08-19 | 241,650 t | 507 |
| 2026-08-14 | 243,300 t | 507 |
| 2026-08-07 | **249,275 t** | 507 |
| 2026-07-22 | 244,175 t | 507 |
| 2026-06-22 | 227,425 t | 505 |
| 2026-05-23 | 211,900 t | 506 |
| 2026-02-22 | **167,825 t** | 505 |

**⇒ The baseline drifted `167,825 → 249,275 t` = +48.53% in 180 days.**

## 4. THE CONSEQUENCE — same tonnage, different verdict
Holding the measured quantity **completely fixed** and varying only the grading date:

| fixed tonnage | grades from | grades to | **spread** |
|---|---:|---:|---:|
| 204,975 t (8/14 trough) | −17.77% | +22.14% | **39.91 pp** |
| 239,925 t (8/20 mark) | −3.75% | +42.96% | **46.71 pp** |
| 238,575 t (8/21 latest) | −4.29% | +42.16% | **46.45 pp** |

## 5. 🔴 THE DISQUALIFYING RESULT
Registered downside bands: **Yellow +25pp · Orange +50pp · Red +100pp** vs the 2yr median.

> **Worst baseline-only grade swing observed over 180 days: 46.71pp = 187% of the smallest band width.**
>
> **⇒ Baseline drift ALONE can cross the nearest registered band, with the measured quantity never changing.**

It clears Yellow (+25pp) outright and reaches **93% of the way to Orange (+50pp)** on denominator movement alone.

## 6. THE MECHANISM, so the fix is not guessed at
A 730-day trailing window **drops old observations off its far end**. In a series with a strong trend — and LME copper inventory has one — the dropped tail is systematically higher or lower than the incoming data, so **the median moves without any new information about the present.** The 2-day instance shows it cleanly: between as-of 8/21 and as-of 8/23 the window shed two early observations (`n 507 → 505`) and the median fell `239,925 → 238,575 t`, moving that tonnage's grade by **0.56pp on two days in which the tape produced no new print at all.**

## 7. WHAT THIS DOES AND DOES NOT ESTABLISH
- ✅ **Establishes:** a grade computed on this band is **not reproducible** from the tonnage alone. Any registered prediction keyed to it is un-gradeable after the fact unless the as-of date and the baseline value are both recorded in the cell. *(This is why L-13(a) already requires every I1 band call to carry its baseline value + as-of date — that ruling was correct and is doing real work; it just documents the instability rather than removing it.)*
- ✅ **Establishes:** the defect is **not confined to the upside band** escalated as L-13(b). It is a property of the **denominator**, so it is present in the **downside/registered** bands too — the ones currently live.
- ❌ **Does NOT establish** that a rolling baseline is the wrong design. A rolling "normal" is defensible; the problem is a **rolling denominator paired with FIXED band widths**, which lets the band's effective sensitivity change under it.
- ❌ **Does NOT change any current read.** I1 is `1 ⚪ UNSCOREABLE↑` and the conjunction fire (copper −20% AND inventory +100%) is nowhere near. **Nothing fired, nothing un-fired, no score moved.**

## 8. WHY I AM NOT FIXING IT
Every available repair moves difficulty: freezing the baseline, widening the bands, or adding a drift guard each changes when the band fires. **Kill-condition-adjacent I1 specs are simultaneously falsifier and trigger, so `DELEGATION_TIER` test 4 bars a difficulty change in EITHER direction** (the L-20 finding). **This is Will's to rule, exactly as L-13(b) was.** I am supplying the measurement I was asked for and no more.

## 9. OPTIONS, PRICED — for the ruling, not chosen here
| # | Option | Effect | Cost |
|---|---|---|---|
| **A** | **Freeze the baseline** at a dated value, re-based on an explicit schedule | grades become reproducible; drift → 0 between re-bases | the frozen value goes stale in a trending regime; re-base dates become discretionary |
| **B** | **Keep rolling; record baseline + as-of in every call** *(already required by L-13(a))* | preserves reproducibility of the RECORD | does not stop a band firing on drift — documents the problem, doesn't remove it |
| **C** | **Grade against a drift-adjusted band** (band width scales with measured denominator volatility) | sensitivity stays constant as the baseline moves | most complex; a new free parameter to set and defend |
| **D** | **Retire the %-vs-median form**; grade on absolute tonnage vs a dated reference | eliminates the denominator entirely | loses the "vs normal" normalisation the band exists for |

**No recommendation offered on difficulty.** If a preference is wanted, ask and I will supply one **as an escalation, not a self-ruling** — L-20's whole point is that I cannot express a preference about this class of boundary and have it count.

## 10. ROUTING
**PROME → Will queue.** Companion to **L-13(b)** (the discriminated upside band, ruled 8/21 as a design constraint, no build). ⚠️ **New scope this adds: L-13(b) treated the gap as an upside-blindness problem; this measurement shows the denominator defect is in the LIVE DOWNSIDE bands as well.** → **KB-059**.
