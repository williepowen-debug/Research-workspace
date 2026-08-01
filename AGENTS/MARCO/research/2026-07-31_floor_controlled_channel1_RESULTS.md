# RESULTS — Floor-Controlled Channel-1 Transmission Test

**Run:** 2026-07-31, session 19 · **Spec:** `thesis/PREREG_2026-07-31_floor_controlled_channel1.md` (thresholds fixed before any pull; Amendment 1 logged, control sector forced by availability)
**Data:** BLS CES State & Area, AHE all employees (data type 03), June 2026 vs June 2025, live API. Raw → `research/floor_controlled_raw.json`.

> **AMENDED 2026-07-31 eve (session 20), after a Will-directed PROME audit.** The **verdict is unchanged** — the audit recomputed all 34 DID cells from the committed raw pull and they reproduce exactly, as do the t-statistics and the 7/25 pre-commitment. Three corrections to the layer around the result: **(1)** the pre-registered **FL diagnostic MISSED** and was never scored — now scored below, and the post-hoc reinterpretation it enabled in the outbound CARL packet is retracted; **(2)** the "~6pp detection floor" named the wrong statistic at the wrong scope — restated in finding 3, conclusion strengthened; **(3)** the "3.2pp median within-state swing" reproduces under no definition — withdrawn and replaced with **4.02pp** in finding 4. Everything is now derived in `scripts/fl_diagnostic_score.py`, which reads the committed raw pull and re-prints every figure this document asserts.

## VERDICT: **NULL / NOT CONFIRMED — robust to control-sector choice**

All three pre-registered CONFIRM conditions fail under **both** the primary and the robustness control. The TX null condition fires under both.

| Pre-registered condition | TTU control (primary) | E&H control (robustness) |
|---|---|---|
| c1 · high-immigrant mean DID ≥ +1.5pp | **−1.94pp** FAIL | **+1.25pp** FAIL |
| c2 · DID > 0 in ≥70% of stratum | **33%** FAIL | **33%** FAIL |
| c3 · high−low stratum gap ≥ +1.5pp | **−2.57pp** FAIL | **+1.27pp** FAIL |
| n3 · TX DID ≤ 0 (null trigger) | **−8.01pp** TRIGGERED | **−1.88pp** TRIGGERED |
| **Verdict** | **NULL** | **NULL** |

## The panel

`DID = YoY%Δ AHE(Leisure & Hospitality) − YoY%Δ AHE(control)`, June-over-June. All states below are **federal-minimum ($7.25, no step)** — the statutory floor is non-binding (L&H runs ~$16–18/hr) and did not move, so the Amendment-2 class of confound is removed by construction.

| State | Stratum | L&H YoY | TTU YoY | DID (TTU) | DID (E&H) |
|---|---|---|---|---|---|
| TX | HIGH-imm | −2.58% | +5.43% | **−8.01pp** | −1.88pp |
| GA | HIGH-imm | +5.70% | +3.15% | +2.55pp | +9.73pp |
| NC | HIGH-imm | +3.14% | −2.32% | +5.46pp | −0.60pp |
| UT | HIGH-imm | +1.40% | +1.86% | −0.46pp | −2.60pp |
| OK | HIGH-imm | +1.25% | +6.12% | −4.87pp | +7.63pp |
| KS | HIGH-imm | −1.04% | +5.30% | −6.34pp | −4.78pp |
| TN | low-imm | +0.43% | +1.85% | −1.42pp | −4.86pp |
| AL | low-imm | +4.79% | −2.81% | +7.61pp | +5.38pp |
| MS | low-imm | +4.46% | +2.39% | +2.07pp | −2.62pp |
| KY | low-imm | −3.70% | +3.86% | −7.56pp | −5.28pp |
| SC | low-imm | +3.60% | +4.81% | −1.21pp | +5.44pp |
| WV | low-imm | +1.40% | +5.14% | −3.74pp | +2.05pp |
| IN | low-imm | −1.45% | +1.33% | −2.79pp | −3.82pp |
| LA | low-imm | +8.32% | −3.68% | +12.00pp | +3.56pp |
| *FL* | *diagnostic — floor stepped, NOT scored* | *+8.75%* | *+1.85%* | *+6.89pp* | *+7.38pp* |
| *CA* | *diagnostic* | *+1.93%* | *+4.00%* | *−2.08pp* | *+0.79pp* |
| *AZ* | *diagnostic* | *+2.82%* | *+1.41%* | *+1.41pp* | *+6.81pp* |

National reference: L&H +3.87%, TTU +3.66%.

## FL diagnostic — SCORED: **MISS** *(added 2026-07-31 eve, session 20, after PROME audit)*

**This section did not exist in the session-19 write-up.** The FL cell was printed in the panel above and never scored against the thing it was pre-registered to test. That omission is the defect: a pre-registered diagnostic that goes unscored is available for post-hoc reinterpretation, which is precisely what pre-registration exists to prevent — and it was so reinterpreted, in the outbound CARL packet. Derivation for everything below: `scripts/fl_diagnostic_score.py` (reads the committed raw pull, no re-fetch).

**Pre-registered (`PREREG` §3, line 52):** *"if FL's `DID` ≈ 0 while FL's raw L&H gap was +4.88pp, that independently **confirms** the Amendment 2 explanation."*

**Observed:** FL `DID` = **+6.89pp** (TTU) / **+7.38pp** (E&H) — not ≈ 0, and *larger* than the +4.88pp raw gap it was meant to explain away. **MISS.**

**Why the sign expectation was invalid by the time the test ran — and why that does not rescue it.** The ≈0 prediction depends on the control sector being **floor-matched**: with Retail Trade (low-wage, floor-exposed) as control, a statutory floor step lifts *both* sectors and differences out, leaving `DID` ≈ 0. Amendment 1 replaced Retail with **TTU** — higher-wage, materially less floor-exposed — so a floor effect stays in the treated leg and `DID` should be **positive**, not ≈ 0. The amendment mechanically invalidated the diagnostic's sign expectation. `PREREG` line 114 discusses the floor-match cost of that swap and **does not notice it broke the diagnostic**, and no corrected expectation was written down before the pull. **Scored as MISS, not as a pass under a re-derived expectation.** A sign flip reasoned out after seeing the number is not a prediction.

**Three independent reasons the FL cell cannot carry the floor claim either way:**

1. **It sits inside the design's own noise.** FL is **+1.25 sd** (TTU) / +1.36 sd (E&H) from the panel mean, against a single-state band of ~11.5pp (§ finding 3 below). **Two of the fourteen *scored* states exceed FL under each control** — under TTU those are **AL (+7.61pp) and LA (+12.00pp)**, both *low-immigrant, federal-minimum, no floor step at all.* LA's DID is 74% larger than FL's with no statutory story available. A cell that ordinary heterogeneity reproduces twice over in the control stratum is not evidence.
2. **The June figure is driven by the control leg, not the treated leg.** `+6.89pp` decomposes as **+4.88pp** (FL L&H hot vs national) **+1.81pp** (FL TTU *cold* vs national) +0.21pp (national sector gap). FL's TTU YoY fell **3.52% → 1.85%** May→June; that single control-sector move is what produced the June step-up. A floor story is a claim about the *treated* sector.
3. **It is not stable, contrary to what was asserted downstream.** FL `DID(TTU)` across 2026: **3.84 · 3.42 · 4.76 · 3.58 · 4.07 · 6.89** — a 3.47pp spread, with June **+2.96pp above the Jan–May mean.** Under E&H the spread is wider (2.22 → 7.48). The CARL packet's *"+6.89pp and stable in every month of 2026"* is **false as written**: 6.89 is the June value only, and it is the year's outlier.

**Net.** Amendment 2 remains the **best available** account of FL's raw wage gap — it is a legislated, dated shock ($13→$14 on Sep 30 2025) in the most floor-exposed sector — but that rests on the statute, not on this test. **The test's own pre-registered check of that account MISSED, and the substituted evidence is inside the noise band.** Correct status: *plausible and legislated, not confirmed here.* The level path cannot discriminate either — FL L&H rose Sep→Dec 2025 (22.30→23.36, +4.8%) and Sep→Dec **2024** (21.07→21.98, +4.3%) at a similar rate, and *both* years contain a Sep-30 floor step, so no step-year/non-step-year contrast exists in the window.

**What is unaffected:** the **forward** statutory impulse — FL minimum wage **$14 → $15 on Sep 30 2026, ~7.1%**, Amendment 2 ramp — is a legislated schedule with a date, not an inference from this panel. Nothing here weakens it.

## Four findings, in order of importance

**1. No dose-response in immigrant exposure — and the sign is not even stable.** High-immigrant minus low-immigrant stratum difference is **−2.57pp** with the TTU control and **+1.27pp** with the E&H control. Opposite signs, neither significant (t = −0.82 and +0.43; |t| < 1 both). A real transmission effect should not invert when you swap a control sector.

**2. TX — the cleanest natural experiment available — points the wrong way under both controls, and persistently.** Largest immigrant workforce exposure, most aggressive enforcement, floor frozen at $7.25 since 2009. Its L&H wages grew **slower** than its own control sectors in **all six months of 2026** (DID −6.0 to −8.6pp vs TTU). This is not a single noisy print.

**3. The instrument class is badly under-powered — and the original +4.88pp signal is far below any threshold that applies to it.** *(Restated 2026-07-31 eve, session 20: the session-19 text called ~6pp a "detection floor," which named the wrong statistic and applied it at the wrong scope. Numbers below are derived in `scripts/fl_diagnostic_score.py`; the conclusion is unchanged and strengthened.)*

Cross-state dispersion in `DID` is sd **5.33** (high stratum) / **6.39** (low stratum), pooled **5.88** — this is the "5.3–6.4pp" the original text quoted, and it reproduces. What it implies depends on which statistic you are testing:

| Statistic | Threshold | Meaning |
|---|---|---|
| High−low **stratum-mean difference** (the pre-registered test statistic) | SE 3.14 → **1.96×SE = 6.15pp** | smallest value separable from zero at 95% |
| Same statistic, proper power calculation | **2.80×SE = 8.78pp** | 80%-power minimum detectable effect |
| A **single state's** `DID` vs the panel mean | **1.96 × pooled sd = 11.53pp** | band for reading one cell as unusual |

So the "~6pp" figure was **1.96×SE for a stratum-mean difference** — a significance threshold, not a power MDE, and **not** a rule about individual state gaps. Two corrections follow, both against MARCO's own prior framing:

- **The test was even weaker than stated.** At 80% power this design needed a **~8.8pp** stratum difference to detect. It observed −2.57pp / +1.27pp. The null is a statement about a design that could only ever have seen a very large effect.
- **The FL +4.88pp headline is worse off, not better.** It is a *single-state* gap, so the applicable band is **~11.5pp**, not ~6pp. It sits at roughly **0.4 sd** of ordinary cross-state variation. The 7/25 verdict is unchanged in direction and harsher in degree: that number was never distinguishable from cross-state heterogeneity, independent of the Amendment 2 story.

⚠️ **Scope correction for anyone handed the "gaps under ~6pp are not interpretable" rule** (it went to CARL on 7/31 as a general state-CES caution, and to LABOR alongside the LAB-17 convergence): the 6.15pp figure governs a **stratum-mean difference across 6–8 states in this June-2026 window**, not any state-level CES comparison. For a single state's gap the corresponding band is **~11.5pp**. The general lesson — size the effect against the instrument's own dispersion before reading it as signal — holds; the specific number does not travel.

**4. But these gaps are NOT noise — and that is the real problem.** *(Figures corrected 2026-07-31 eve, session 20. The session-19 text quoted a "median within-state swing of 3.2pp" that **reproduces under no definition** — median 6-month range 4.02, mean range 4.44, median within-state sd 1.48, median |MoM step| 1.29, and the E&H variants 1.23–4.82. The 3.2 figure is withdrawn; the conclusion survives on the correct one, since 4.02pp is still well inside the 5.88pp cross-state dispersion.)*

A stability check (same state, same `DID`, six consecutive months, TTU control, 14 scored states) gives a **median 6-month range of 4.02pp** — i.e. a typical state's `DID` moves less across half a year than states differ from each other at a point in time. **11 of 14 states hold sign in all six months**; the three that cross zero (GA, UT, IN) all sit near it. The tightest cells: TX −6.0 to −8.6 every month, NC +4.7 to +7.0, KY −6.0 to −7.7 — **these are the best-behaved states, quoted as such, not as typical.** So state-level wage gaps measure something real and persistent — it simply **is not immigrant exposure**. Inspection points at industry mix inside the control supersector: **TX, OK and KS are energy states**, where TTU (transportation/warehousing/utilities) tracks the oil & gas cycle. That contaminates the control in precisely the high-immigrant cells, and it is why the E&H control moves TX from −8.01 to −1.88. Persistent state heterogeneity, not sampling noise, is what swamps the effect.

## What this does and does not license

**Does NOT license:** "immigration restriction does not raise wages." This test cannot support that. It is a 14-state, one-window, two-sector design with a ~6pp detection floor.

**Does license:** MARCO has now failed **three** pre-registered attempts to demonstrate Channel-1 transmission — produce CPI (ES-MARCO-08, resolved toward freight), FL wage divergence (falsified by its own panel), and this floor-controlled specification. Per the consequence pre-committed on 7/25, **the correct response is to downgrade the claim, not to hunt a fourth instrument.**

**A structural reason to expect the whole instrument class to keep failing — worth stating, because it argues against further attempts:** CES is an **establishment payroll survey**. The population that withdrew is disproportionately undocumented, and therefore substantially off-payroll or on payroll under identities the survey cannot resolve. The very workers whose exit is the mechanism are the workers CES is least able to observe. A payroll-wage instrument may be structurally incapable of measuring this shock regardless of specification — which reframes three failures from "bad luck with thermometers" into evidence about the measurement problem itself.

## Consequence executed (pre-committed, not decided after the fact)

Per `PREREG` §6, quoting `SCRATCH.md` written 2026-07-25:

- Thesis **v2.8 → v3.0** (MAJOR).
- Channel 1 reclassified: **quantity HIGH / transmission UNDEMONSTRATED.**
- Downstream (CARL cost, LABOR U-3, REGINALD) notified that MARCO does not support Channel-1 *transmission* claims.
- **No fourth instrument hunt.**

## Secondary test — NOT run this session

The H-2A offer-above-AEWR premium (`PREREG` §5) was **not** run. Reason: the `WAGE_OFFER` field carries mixed pay units (median $15.79, mean $93.64) and requires a unit filter before any aggregation; doing it properly is its own pass. Logged as open. Note the standing caution from the pre-registration: **AEWR itself must never be cited as evidence of transmission** — it is an administratively-set floor (and its NASS Farm Labor Survey basis was canceled Aug 2025), so citing a rising AEWR as scarcity would repeat the Amendment 2 error exactly. Only the *spread of offers above* the floor is informative.
