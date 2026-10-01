## 2026-10-01 — DAEDALUS → PROME: WQ-252 options memo for the Tue 10/06 crack contract-month sitting (DOCKET L472 → L471)

**ACTION:** PROME puts this memo in front of Will at the 10/06 sitting (L471); Will chooses one basis; PROME registers it on HEN-46 F1 and on GATE-TERRY-VLO-HELD-01 leg A. Needed-by: 2026-10-14.
**Priority:** 🟠 — the choice decides whether one held position (1 VLO share, filled $412.00 on 9/18) keeps a live price exit after 10/14.
**Owner of the choice:** Will. DAEDALUS (gate-basis owner) prepared the options. HENRY is conflicted on every remedy, because each one moves the line in its favour or against it. TERRY inherits the result. **This memo moves no threshold and contains no trade view. $0.**
**Measurements:** `AGENTS/DAEDALUS/runs/2026-10-01_WQ252_CRACK_STEP_MEASUREMENTS.md` (the full September table, the script and the expiries). These are DAEDALUS's own pulls from a single vendor (yfinance named contracts). **HENRY's per-candidate measurements are due to DAEDALUS on Mon 10/05** (HENRY STATUS calendar). Where they differ from these figures, PROME shows both and names the source of each.

### The whole story first
The crack spread is the refining margin on diesel: heating-oil futures times 42, minus crude futures. Two lines hang on it. **$95 means "stand down" and $90.16 means "thesis dead"** (HENRY's HEN-46 diesel-squeeze row). Those two lines are only **$4.84 apart**. In September, the gap between the November and December contracts **averaged $4.60 a barrel, with a median of $4.72 and a range of −$0.03 to +$7.24.** So moving the measurement one month along the curve shifts the reading by about the whole width of the band. **On 7 of the 21 September sessions, November and December sat on opposite sides of $95.** On those days, the choice of month alone decided the grade. **This has already decided a live outcome once.** On 9/25 the November pair settled at **$94.998**, under $95 by $0.0018, so F1 fired and both staged VLO shares stood down (GATE-TERRY-VLO-SCALE, terminal). **December read $95.02 that day and would not have fired.**

The sitting is not choosing a number. It is choosing **which contract month the existing lines are read on after 10/14**, when HENRY's November-only basis expires.

### What the ruling governs (live consumers after 10/14)
| Consumer | Line(s) | What happens if no month is set |
|---|---|---|
| **GATE-TERRY-VLO-HELD-01 leg A** (the ONE held VLO share) | settle < **$90.16** ⇒ SELL rec | **Leg A is SUSPENDED after 10/14.** The share keeps only its policy legs B1–B3. ⚠️ **This is the most consequential consumer, because it is the only one attached to money.** |
| HEN-46 F1 (HENRY's falsifier) | < $95 stand down · < $90.16 dead | F1 has no basis from 10/15 to the Q3 prints (AAL/LUV, late Oct; row backstop 10/31) |
| HEN-F3 **successor** (optional; WQ-344 rider) | crack < $95 within 10 sessions after the 10/31 ban expiry | It can only be registered at this sitting, and only if Will wants the falsifier alive. Its window runs ~11/02–11/13. |
| GATE-TERRY-VLO-SCALE | — | **Not affected.** It is terminal. If Will's optional CME check revives it (the 9/25 NY Harbor ULSD Nov settle ≥ 4.4622), it lives only to 10/14, on November, and expires before the new basis starts. |

### Hard constraint every option must respect
⚠️ **The crude leg of a month stops trading about 10 days before the heating-oil leg.** CLX26 expires **10/20** and HOX26 **10/30**. CLZ26 expires **11/20** and CLF27 **12/21** (vendor `expireDate`). **A matched November pair cannot be read after 10/19.** December covers every consumer above (10/20 → 11/19) with no further roll.

### Today's levels (2026-10-01 12:17 ET — intraday last trades, NOT settlements, single vendor)
| Month | Crack | Room to $95 | Room to $90.16 |
|---|---:|---:|---:|
| Nov | $102.38 | +$7.38 | +$12.22 |
| Dec | $98.02 | +$3.02 | +$7.86 |
| Jan | $95.61 | +$0.61 | +$5.45 |

So what: today no line is in play on November or December. **The curve slopes down** (the market prices later months lower), so every later month reads closer to the lines. That is why the choice of month is a choice about how easily the lines fire.

### The options, each costed against the measured step
"Step" = the jump in the graded number at the switch = Nov minus Dec on the switch day. September distribution: **median $4.72, interquartile range $4.22–$6.13, min −$0.03, max $7.24**; live today $4.36.

| # | Option | Switches needed to cover 10/15→11/19 | Cost at the switch | Which way it cuts on HEN-46 | Other costs |
|---|---|---|---|---|---|
| **A** | **Fixed next month:** December matched (HOZ26×42 − CLZ26) from 10/15 | 1 (10/15) | Graded number drops by the step, ~$4–5 typical, $7.24 worst seen | **Against the thesis:** the reading moves toward both lines | For 4 sessions (10/15–10/19) the graded month is not the front month while November still trades |
| **A′** | **One fleet schedule keyed to expiry** (BRENT's form, already adopted for Brent lines and FORGE, L461): a month governs through the settle of the session before its EARLIER leg's last trade. ⇒ Nov through 10/19, Dec 10/20 → 11/19, Jan from 11/20 | 1 (10/20) | Same step as A, 3 sessions later | Against the thesis, as in A | **Extends HENRY's November fix by 3 sessions past 10/14.** That needs Will's word because it is a letter change. In return, no two desks read different months on the same day (BRENT 9/28: on Brent, `BZ=F` read December while FORGE and STATUS quoted November, ~$7.5 apart). |
| **B** | **Forward-adjusted series:** grade Dec + k, where k = (Nov − Dec) on the switch day, frozen | 0 visible steps | None on the series, but k locks in whatever the curve's shape was on one day (in September it ran from −$0.03 to $7.24) | **For the thesis, by k (~$4.4 at today's spread):** the graded number reads about $4 higher than the real December margin | The graded number is no longer a price anyone can trade. k must be registered once and is arbitrary to the day it is struck. |
| **C** | **Wider separation:** require the crossing to persist (e.g. 2 consecutive settles), or move a line | as A/A′ | Persistence: a one-session delay to every fire. Moving a line: **HENRY's threshold, not offered here** | For the thesis (harder to fire) | Even the $4.84 band is narrower than the worst step ($7.24). Persistence does not remove the step; it only filters one-day crossings. |
| **D** | **Roll-window rule (BRENT's second clause), paired with A or A′:** a crossing that exists on only one of the two months within ±2 sessions of the switch is recorded as roll-induced and neither fires nor un-fires a line | adds no switch | A ~5-session window per switch where a crossing seen on one month only is recorded, not acted on | Neutral in design. In practice it delays a fire that shows on one month only. | Under VLO-HELD-01's "UNKNOWN never defaults to a fire" rule, a real crossing inside the window waits up to 2 sessions |

### DAEDALUS design read (labelled; the choice is Will's)
From a gate-design standpoint, **A′ + D** has the fewest moving parts. It uses one schedule the fleet already runs. Every graded number is a real, tradable margin. Nothing is back-filled. The step's effect is confined to a named window where it is recorded rather than acted on. **Its cost, stated plainly:** in a downward-sloping curve it grades about $4–5 lower than option B, so it is **more likely to fire HENRY's falsifier and the VLO share's sell rec than option B is.** B is the option that keeps the lines in November's terms. It also makes the graded number a construction rather than a price. If Will's view is that **the lines were drawn for November specifically**, B is the honest choice. If his view is that they were drawn for **"the front of the curve"**, A′ is.

### Known-unknowns that could change the choice
1. ⚠️ **Which contracts the $90.16 line was calibrated on — INFERRED, not verified.** $90.16 reproduces exactly on the continuous series (`HO=F×42 − CL=F`) at the 7/23 close. Under the standard NYMEX calendar that was most likely **August heating oil against September crude, a mismatched pair.** HENRY's 9/14 record says "calendar-matched at every calibration observation". The expired contracts are no longer served, so DAEDALUS cannot settle this. **Either way, the line was set on the front of the curve, about $8.75 above where the November pair stood that same day ($81.41).** If the line is meant to travel with the front, the argument favours A′. If it is meant to stay tied to one month, it favours B. Question packeted to HENRY today.
2. ⚠️ **None of these figures are CME settlements.** Our tools are blocked from CME. The vendor's finalized row matched the settlement window to ≤$0.10 on 3 sessions (HENRY, 9/24). **The step figures are DAEDALUS's single-vendor pulls.** HENRY's and TERRY's measurements (due 10/05) are a second perimeter. A disagreement between them is information.
3. The continuous series cannot be used as a fallback. On 9/29–9/30 it read **$116–118 against November's $100–106**, because during the ~10-day window when the crude leg has rolled and heating oil has not, it pairs October heating oil with November crude.

### Owed to this memo
- **HENRY:** per-candidate step measurements by Mon 10/05 (its own calendar) and the answer on the calibration pair.
- **TERRY:** has delivered no measurements as of 12:2x ET on 10/01. Its stake is the VLO-HELD-01 leg-A consequence of each option, specifically how many sessions each option leaves leg A blind.
- **PROME:** fold both into the sitting deck and show disagreements side by side.

COMPLETION (memo-scoped): STATUS done · CHANGED this memo + `AGENTS/DAEDALUS/runs/2026-10-01_WQ252_CRACK_STEP_MEASUREMENTS.md` · RESULT 5 options costed against the September step (median $4.72, 7/21 sessions straddle $95) · GAPS HENRY/TERRY measurements (due 10/05); calibration-pair identity INFERRED · WILL_NEEDS the 10/06 choice · FOLLOW-UP PROME folds the desk measurements.
