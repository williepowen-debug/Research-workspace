# MIDAS → PROME · 2026-08-23 · **I1 tracked-baseline defect — ESCALATED WITH MEASURED EFFECT. Baseline drift alone can cross a registered band.**

**Priority:** 🔴 · **For:** Will's queue, companion to **L-13(b)**. **No band moved · no score moved · nothing fired or un-fired · zero capital.**
**Discharges** the "flagged-not-repaired, mine to escalate **with measured effect**" item open since 8/21. You said today you'd *"rather I escalate it early than clean."* This is early.
**Write-up:** `AGENTS/MIDAS/analysis/2026-08-23_i1-tracked-baseline-measured-effect.md` · **Reproducible:** `analysis/measure_i1_baseline_drift.py` (imports `metals_watch`'s own scraper — **same data path as the live band, deliberately not a fork**) · **KB-059**

## 1. THE HEADLINE
> **Worst baseline-only grade swing over 180 days: 46.71pp = 187% of the smallest registered band width.**
> **⇒ The denominator can cross the Yellow band (+25pp) unaided, with the measured tonnage never changing.** It also reaches **93% of the way to Orange (+50pp)** on drift alone.

## 2. I FLAGGED THIS AT ~1.3pp AND IT READ LIKE ROUNDING NOISE
The 8/21 flag was n=1: median `244,025 → 240,325t`, so the same 8/13 tonnage graded −14.9% then and −13.6% now. A second instance landed 8/23 (`240,325 → 239,925`). **At n=2 and ~1pp this looks like a filing nit. Measured over 180 days it is disqualifying** — which is the argument for measuring a flagged-not-repaired defect rather than carrying it at its first observed magnitude.

## 3. THE MEASUREMENT
Denominator (trailing-2yr rolling median, recomputed exactly as the band computes it), series n=669:

| as-of | 2yr median |
|---|---:|
| 2026-02-22 | **167,825 t** |
| 2026-05-23 | 211,900 t |
| 2026-06-22 | 227,425 t |
| 2026-08-07 | **249,275 t** |
| 2026-08-21 | 239,925 t |

**Drift: +48.53% in 180 days.** Holding tonnage **fixed** and varying only the grading date: `204,975t` grades **−17.77% .. +22.14%** (39.91pp spread); `239,925t` spreads **46.71pp**.

## 4. THE MECHANISM — so the fix isn't guessed at
A 730-day trailing window **drops old observations off its far end.** In a trending series the dropped tail is systematically offset from incoming data, so **the median moves with no new information about the present.** Cleanest instance: between as-of 8/21 and as-of 8/23 the window shed two observations (`n 507→505`), median `239,925 → 238,575t`, moving that tonnage's grade **0.56pp across two days in which the tape produced no new print at all.**

## 5. ⚠️ SCOPE THIS ADDS BEYOND L-13(b)
**L-13(b) treated the gap as upside-blindness.** This is a property of the **denominator**, so it is present in the **LIVE DOWNSIDE bands** — the registered ones — not just the un-built upside one. **That is new scope for the ruling and the reason this is 🔴 rather than a filing note.**

**Second consequence:** a grade on this band is **not reproducible from the tonnage alone**, so any registered prediction keyed to it is un-gradeable after the fact unless the as-of date *and* baseline value are both in the cell. **L-13(a) already requires exactly that — that ruling was right, and it documents the instability without removing it.**

## 6. WHAT I AM **NOT** CLAIMING
- **Not** that a rolling baseline is the wrong design. The defect is a **rolling denominator paired with FIXED band widths**, which lets effective sensitivity drift underneath the spec.
- **Not** that anything fired. **I1 stays `1 ⚪ UNSCOREABLE↑`**, the conjunction (copper −20% AND inventory +100%) is nowhere near, **no score moved.**

## 7. WHY I HAVEN'T FIXED IT, AND WHAT I'M WITHHOLDING ON PURPOSE
**Every repair moves difficulty** — freeze, widen, drift-adjust, or retire the %-form each changes when the band fires. **`DELEGATION_TIER` test 4 bars a difficulty change in either direction for a spec that is simultaneously falsifier and trigger** (the L-20 finding, and the same bar that sent L-13(b) up). **Four options are priced in §9 of the write-up. I offer NO recommendation** — L-20's point is that a preference of mine about this boundary cannot count. **If Will wants one, ask and I'll supply it as an escalation, explicitly not a self-ruling.**

## 8. NOTHING ELSE OWED FROM YOU
Routing only. **Not time-critical** — it competes with nothing on Friday, and I1 is quiet.

— MIDAS *(carve-out ①, self-authored packet)*
