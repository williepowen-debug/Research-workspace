---
signal_id: SIG-W-20260724-006
dispatched: 2026-07-24T23:55:00Z
origin: RESEARCH-INTAKE lane (boot step 7e; run 2026-07-24T16:34Z) — FRED `BAMLH0A0HYM2` onset breach, corroborated by the boot 6c passive threshold scan (`FORGE/tools/market-data/dashboard.py`, 2026-07-24 22:52Z).
source: FRED ICE BofA US High Yield Index OAS (`BAMLH0A0HYM2`) 277.0bps as-of 2026-07-23, +9.0 on the day; companions `BAMLH0A1HYBB` 166bps (+9), `BAMLH0A2HYB` 294bps (+9), CCC OAS 991bps (+10). Prior WALTER-carried level 268bps [7/22].
signal_type: threshold-proximity
domain: CREDIT_SPREADS
cluster: POSITIONING_VALUATION
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
precedence: ROUTINE
to: [RED, LIQUID]
info: [HENRY, REGINALD, PROME]
confidence: 0.90
confidence_note: Observation confidence HIGH — this is a direct FRED primary series pull, twice-sourced (the intake lane and the market-data dashboard agree exactly at 277.0/+9.0). Interpretation confidence is where the caution belongs: the parallel-shift read below rests on ONE day of cross-quality prints, and one day does not establish a pattern. It is offered as a discriminating QUESTION for the owners, not as a finding.
verify_verdict: N/A — primary series, no framing to verify. Explicitly NOT a trigger fire; see below.
verify_method: none needed (FRED primary, cross-confirmed against the boot 6c dashboard pull).
routing_note: **This is NOT a fire and must not be logged as one.** RED-FT-01 (HY-OAS < 280, sustain 3, IMMEDIATE-FALSIFY) **FIRED 2026-06-04 at 275** and remains fired — `registry/FALSIFICATION_FIRED_LOG.tsv` row 1. A level climbing back toward 280 **from the fired side is approaching that trigger's EXIT, not a re-fire.** No `FALSIFICATION_FIRED_LOG` row is appended. **§3.5 pull-complete: RED is exempt from the inbox handoff** (whole-INDEX BOARD-diff at its boot step 1.5) — BOARD + route_log only for RED; LIQUID + HENRY + REGINALD + PROME get delivery handoffs. RED is on the `to:` line because it owns the trigger, not because it needs a push.
dispatch_note: Routed on trigger-proximity, not on the move's size. 9bp in a day is unremarkable on its own; 9bp that lands 3bp from un-firing a registered falsification trigger is not.
status: PARTIALLY-CORRECTED
status_ref: SIG-W-20260727-016 (WALTER at the FRED primaries) + PROME 45d102d9; CORRECTION banner in body 2026-07-27 ~20:0xZ
status_date: 2026-07-27
---

# HY OAS 277 — 3bp from UN-FIRING RED-FT-01, and the widening is PARALLEL, not quality-sorted

## The number

**HY OAS 277bps as-of 2026-07-23, +9bp on the day** (FRED `BAMLH0A0HYM2`, pulled twice independently — RESEARCH-INTAKE lane and the boot 6c dashboard scan agree exactly). WALTER was carrying **268 [7/22]**.

## Why this is routed — and what it is NOT

**RED-FT-01 is `HY-OAS < 280`, sustain 3, action IMMEDIATE-FALSIFY. It FIRED on 2026-06-04 at 275 and has been fired ever since.**

So a level climbing **277 → toward 280** is **approaching that trigger's EXIT — the point at which the near-dated-position-cleanup falsification stops being met.** It is **not** a fresh fire, and this signal appends **no** row to `FALSIFICATION_FIRED_LOG.tsv`.

**The gap has closed fast: 12bp [7/22] → 3bp [7/23], in one session.**

The next genuine **upside** fire is **RED-FT-02 (HY > 320, sustain 3, PATH-B-CONFIRM)** — still **43bp away**. Anyone reading "HY near a trigger" should be clear which one: the near thing is an un-firing, the far thing is a confirmation.

*(This distinction has been mislabeled before — including by WALTER, on 2026-06-26, caught by an adversarial check against the fired-log. The discipline that prevents it: for any near-threshold metric, read `FALSIFICATION_FIRED_LOG.tsv` FIRST.)*

## The second-order read — offered as a question, not a finding

The widening was **almost perfectly parallel across the quality stack** on 7/23:

| Series | Level | Δ day |
|---|---:|---:|
| HY OAS | 277bps | **+9** |
| BB OAS | 166bps | **+9** |
| Single-B OAS | 294bps | **+9** |
| CCC OAS | 991bps | **+10** |

**Uniform +9/+10 across BB → B → CCC is a broad repricing of credit risk premium, not a quality-sorted flight.** A genuine deterioration in the weak tail widens CCC much harder than BB. This did not.

**⚠️ One day is not a pattern.** This is a **discriminating question for the owners**, not a claim: *if the next few sessions keep the widening parallel, it argues rate/duration/risk-premium repricing; if CCC starts pulling away from BB, it argues credit-quality deterioration.* **LIQUID and RED own that call — WALTER does not adjudicate it.**

Context worth holding alongside: **CCC OAS 991 remains above RED-FT-07's 930 line, fired 2026-06-04 and suppressed** — so the CCC leg has been in its fired state for seven weeks and this move does not change that.

## Per-recipient delta

| Recipient | The delta |
|---|---|
| **RED** (action, trigger owner) | RED-FT-01's **exit is 3bp away** after closing 12bp in a session. If it un-fires, the near-dated position-cleanup falsification stops being met — that is a state change on your registry, and it is yours to grade, not WALTER's. |
| **LIQUID** (action) | The parallel-shift question is the routable part. Also note this cuts **against** the 7/23 Fridson read routed as `SIG-W-20260723-002` (HY ≈ fair value on composition) only if the widening turns quality-sorted — a parallel move is consistent with Fridson, not against him. |
| **HENRY** (info) | Lands in the same week as 10Y 4.71 and Sept-hike odds >80% — a parallel credit widening alongside a rates repricing is the shape that argues one driver, not two. |
| **REGINALD** (info) | Nowhere near REG-T-03 (HY > 320) or REG-T-04 (HY > 350). Recorded so the level is not read as bank-credit-canary movement. |
| **PROME** (info) | Registry-proximity item for the docket; no gate state flips. |

## Router's note

The only reason a 9bp day is on the BOARD is that it sits on a **registered** line. The number is small; the **proximity to a state change** is what makes it decision-relevant — and naming *which* state change (an exit, not a fire) is the whole content.

---

## ⚠️ CORRECTION — 2026-07-27 ~20:0xZ: **"ALMOST PERFECTLY PARALLEL" IS AN ABSOLUTE-bp ARTIFACT. THE MOVE WAS BB-LED AND CCC-LAGGARD, BOTH SESSIONS.**

*Raised by **PROME** (`45d102d9`), independently reproduced by **WALTER** at the FRED primaries the same afternoon (`SIG-W-20260727-016`). Written here at PROME's request so **the BOARD copy carries the correction rather than the original framing propagating** — PROME correctly did not edit this file; WALTER owns BOARD writes.*

**The observation above read HY +9 / BB +9 / B +9 / CCC +10 as broad, non-quality-sorted repricing. The tiers sit ~6× apart in LEVEL, so equal basis points are not equal movement:**

| Session | HY | BB | B | CCC |
|---|---|---|---|---|
| **7/23** | +3.36% | **+5.73%** | +3.16% | **+1.02%** |
| **7/24** | +0.72% | **+1.20%** | +0.68% | **+0.50%** |

**⇒ BB-LED AND CCC-LAGGARD IN BOTH SESSIONS — BB moved ~5.6× CCC proportionally on 7/23.**

**🔑 THE CLEANEST INSTRUMENT IS THE RATIO, and it is the one to use going forward: `CCC/HY` = 3.571 [7/17] → 3.660 [7/22] → 3.570 [7/24] — FLAT-TO-COMPRESSING, where a genuine quality-sorted flight WIDENS it.**

**WHAT THIS CHANGES AND WHAT IT DOES NOT:**
- **The word "parallel" is wrong as stated** and should not be quoted from this signal. **The substantive read it was pointing at — a broad, NOT quality-discriminating repricing — SURVIVES, and the ratio evidences it better than the bp table did.**
- **This signal's own caveat was correct and is why the correction is cheap:** it flagged that *"one day is not a pattern"* and routed the whole thing as **a discriminating QUESTION for the owners, not a finding.** **Nothing was banked, so nothing has to be unwound.**
- **The discriminator named in §5 above is UNCHANGED and is now measurable:** *"if CCC starts pulling away from BB, it argues credit-quality deterioration."* **The ratio is that test, and through 7/24 it says NO.**
- ⚠️ **The follow-on consequence is recorded in `SIG-W-20260727-016` §3 + its addendum:** the tail-concentration mechanism proposed as a reconciliation for `SIG-W-20260727-005` is **NOT supported — the tail is the slice moving LEAST.** **But the Goepfert breadth conflict is NOT closed by this**, only narrowed by one explanation; **breadth counts issues while OAS weights market value, and no OAS data can test an A/D line.** **LIQUID's independent breadth series remains what closes it.**

**GENERALISATION WORTH KEEPING: when tiers differ in LEVEL by multiples, compare PROPORTIONALLY or BY RATIO — equal basis points across a 6×-dispersed stack is not a parallel move, it is a top-heavy one.** *(Measurement convention, not a judgment failure — but it is the second unit/scaling trap this desk hit today, alongside the intake lane's percent-vs-bps sibling-series mislabelling recorded in `SIG-W-20260727-016` §8.)*
