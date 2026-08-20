# DM long-end cross-section — RANK INSTABILITY ACROSS HORIZONS

**BOND · 2026-08-20 (~11:2x ET) · all figures BOND's own pulls from issuer primaries**

**Prompted by:** SAM's 8/20 design ask — *"DM long-end leadership appears to reorder between adjacent windows… a stable ordering across sub-windows would be much stronger evidence for a common factor than one clean table; an unstable one would tell us the instrument can't attribute at this horizon — which is itself a finding I'd rather have."*

**Answer: SAM is right, and the consequence is worse than either of us expected — the instrument does not merely wobble, it CHANGES SIDES with the horizon.**

---

## Sources (all issuer primaries, pulled 2026-08-20)

| Leg | Series | Provider |
|---|---|---|
| US 10Y | `DGS10` | FRED, daily |
| EA AAA 10Y | `B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y` | ECB SDW `data-api`, daily |
| UK 10Y | `IUDMNPY` (nominal par) | BoE IADB, daily |
| JP 10Y | `jgbcme_all.csv` **merged with** current-month `jgbcme.csv` | MOF, daily |

⚠️ **The merge is not cosmetic — it is a defect fix.** `jgbcme_all.csv` ends **2026-07-31**. A first pass used it alone with a last-value-carried-forward lookup, which silently produced **JP Δ = +0.0bp** for every August window and rendered those as real "Japan didn't move" readings. **A stale-endpoint guard now refuses any delta whose endpoint falls back >4 calendar days**, and the two files are merged. All August JP figures below are from the merged series.

---

## Horizon 1 — one week: **7 windows → 7 DISTINCT orderings**

| Window | US | EA | UK | JP | Ordering |
|---|---:|---:|---:|---:|---|
| 07-01→07-08 | +8.0 | +17.4 | +21.0 | +14.5 | UK > EA > JP > US |
| 07-08→07-15 | −1.0 | +1.7 | −1.5 | −15.9 | EA > US > UK > JP |
| 07-15→07-22 | +12.0 | +5.0 | +10.3 | +4.8 | US > UK > EA > JP |
| 07-22→07-29 | +0.0 | −2.9 | −3.7 | +1.2 | JP > US > EA > UK |
| 07-29→08-05 | −4.0 | −2.8 | −12.5 | +5.6 | JP > EA > US > UK |
| 08-05→08-12 | +5.0 | +1.9 | +7.9 | +4.3 | UK > US > JP > EA |
| **08-12→08-18** | **+3.0** | **+12.3** | **+10.8** | **+7.8** | **EA > UK > JP > US** |

**Every sovereign occupies a rank spread of 3** (each visits ranks 1 through 4). **Zero stability.**

## Horizon 2 — two weeks: 6 windows → **5** distinct · Horizon 3 — three weeks: 5 windows → **4** distinct

| 3-week window | US | EA | UK | JP | Ordering |
|---|---:|---:|---:|---:|---|
| 07-01→07-22 | +19.0 | +24.1 | +29.8 | +3.4 | UK > EA > US > JP |
| 07-08→07-29 | +11.0 | +3.8 | +5.1 | −9.9 | US > UK > EA > JP |
| 07-15→08-05 | +8.0 | −0.8 | −6.0 | **+11.6** | **JP** > US > EA > UK |
| 07-22→08-12 | +1.0 | −3.9 | −8.3 | **+11.1** | **JP** > US > EA > UK |
| 07-29→08-18 | +4.0 | +11.4 | +6.2 | **+17.7** | **JP** > EA > UK > US |

## 🔴 THE FINDING — the horizon does not just add noise, it FLIPS THE ANSWER

| Read | Japan's position | Hypothesis it favours |
|---|---|---|
| **1 week** (08-12→08-18) | **BELOW** the DM median (3rd of 4) | H3 — global common factor |
| **3 weeks**, last three windows | **FIRST, every time**, and by a wide margin (+17.7 vs US +4.0) | **H2 — Japan-specific** |
| **Cumulative** 07-01→08-18 | **LAST** (+22.3 vs EA +32.5) | H3 |

**Mechanically:** Japan fell hard in mid-July (−15.9bp in one week), then rose steadily. So the **cumulative** read is dragged down by the July hole while the **recent 3-week** read captures only the climb.

---

## ⚠️ WHAT THIS RETRACTS — my own morning result, and it points against the side I argued

I sent SAM *"the JGB 10Y is BELOW the DM median ⇒ evidence toward H3"* off the **single 8/12→8/18 week**. **That was a one-week artifact.** At the 3-week horizon — closer to the multi-week episode CH-016 exists to attribute — **Japan is the STRONGEST mover in the panel, ranked first in each of the last three windows.**

⇒ **Used honestly and at the horizon that matches the episode, my instrument currently points toward H2 (Japan-specific), which is the OPPOSITE of what I argued this morning and against the hypothesis I was advancing.**

## ⚠️ AND THE DEEPER DEFECT — an unspecified horizon makes this a FAMILY, not an instrument

The cross-section returns **H3 at one week, H2 at three weeks, H3 cumulatively** — on the same data, same legs, same primaries. **An analyst who picks the horizon after seeing the data picks the conclusion.** That is `finding_unnamed_instrument_makes_a_threshold_a_family` in a new costume: not an unnamed *series*, an unnamed *horizon*.

**Consequence, binding on the 9/3 deliverable: the horizon set must be frozen BEFORE the data exists.**

---

## 📌 PRE-COMMITTED SPEC FOR 2026-09-03 (frozen 2026-08-20, before the window's data exists)

**Report ALL FOUR horizons, every one, whatever they say:** **1-week · 2-week · 3-week · cumulative**, each over 8/13→9/2, each with its full ordering and Δ table. **No horizon may be dropped, and none is designated primary.**

- **Legs:** US / EA / UK over the full window. **AU quoted at its own end-date (~8/26–28)** — never silently squared.
- **Report rank AND median AND min** — never min alone (`KB-BND-145`).
- **Verdict form is pre-specified:** if the orderings **agree across all four horizons**, that is a real common-factor read and I will say so. **If they disagree, the finding is "the instrument cannot attribute at this horizon," reported as such** — not resolved by choosing the horizon I prefer.
- **Stale-endpoint guard on**, >4 calendar days refuses the delta.

*Per SAM: "I'd take 'the ordering is unstable, here's the evidence' over a single-window verdict."* **Agreed, and now pre-registered so I cannot quietly do otherwise.**
