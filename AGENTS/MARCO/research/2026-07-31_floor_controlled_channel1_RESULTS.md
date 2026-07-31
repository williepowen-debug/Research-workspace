# RESULTS — Floor-Controlled Channel-1 Transmission Test

**Run:** 2026-07-31, session 19 · **Spec:** `thesis/PREREG_2026-07-31_floor_controlled_channel1.md` (thresholds fixed before any pull; Amendment 1 logged, control sector forced by availability)
**Data:** BLS CES State & Area, AHE all employees (data type 03), June 2026 vs June 2025, live API. Raw → `research/floor_controlled_raw.json`.

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

## Four findings, in order of importance

**1. No dose-response in immigrant exposure — and the sign is not even stable.** High-immigrant minus low-immigrant stratum difference is **−2.57pp** with the TTU control and **+1.27pp** with the E&H control. Opposite signs, neither significant (t = −0.82 and +0.43; |t| < 1 both). A real transmission effect should not invert when you swap a control sector.

**2. TX — the cleanest natural experiment available — points the wrong way under both controls, and persistently.** Largest immigrant workforce exposure, most aggressive enforcement, floor frozen at $7.25 since 2009. Its L&H wages grew **slower** than its own control sectors in **all six months of 2026** (DID −6.0 to −8.6pp vs TTU). This is not a single noisy print.

**3. The instrument class has a detection floor of ~6pp — larger than the signal that started all this.** Cross-state dispersion is sd ≈ 5.3–6.4pp, giving a minimum detectable stratum difference of **~6pp**. **FL's original +4.88pp headline — the number promoted to primary Channel-1 instrument on 7/25 — sits below this design's detection floor.** It was never distinguishable from ordinary cross-state heterogeneity, independent of the Amendment 2 story. That is a harsher verdict on the 7/25 episode than the one issued at the time: the instrument was not merely confounded, it was under-powered to begin with.

**4. But these gaps are NOT noise — and that is the real problem.** A stability check (same state, same DID, six consecutive months) shows **median within-state swing of only 3.2pp**, with states holding sign consistently: TX −6.0 to −8.6 every month, NC +4.7 to +7.0, KY −6.0 to −7.7. So state-level wage gaps measure something real and persistent — it simply **is not immigrant exposure**. Inspection points at industry mix inside the control supersector: **TX, OK and KS are energy states**, where TTU (transportation/warehousing/utilities) tracks the oil & gas cycle. That contaminates the control in precisely the high-immigrant cells, and it is why the E&H control moves TX from −8.01 to −1.88. Persistent state heterogeneity, not sampling noise, is what swamps the effect.

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
