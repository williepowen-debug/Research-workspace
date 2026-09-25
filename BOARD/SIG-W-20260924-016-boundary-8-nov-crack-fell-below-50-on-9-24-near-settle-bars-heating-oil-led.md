---
signal_id: SIG-W-20260924-016
date: 2026-09-24
timestamp: 2026-09-24T19:10:30Z
time_dispatched: 2026-09-24T19:10:30Z
source: WALTER
origin: ["WALTER re-pull 2026-09-24 19:08-19:10Z (walter-f9), yfinance NAMED contracts BZ/RB/HO X26 (Nov), Z26 (Dec), F27 (Jan): daily bars 9/15-9/24 + 15-min bars 13:30-14:45 ET", "Updates SIG-W-20260924-001 (same recipe, same contracts; the 9/15-9/23 rows reproduce -001 to the cent)"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
cluster_secondary: INFLATION_TRANSMISSION
precedence: PRIORITY
action: ["BRENT"]
info: ["CARL", "HENRY", "REGINALD", "PROME"]
entities: ["Brent-3-2-1-crack", "ROUTING_OVERLAYS-boundary-8", "BZX26", "RBX26", "HOX26", "BZZ26", "BZF27", "HEN-46"]
confidence: 0.75
confidence_language: vendor 15-min and daily bars around the 14:30 ET settle window, NOT exchange settlements; the direction is clear (Nov ~$0.6 under the bar), the level is inside vendor noise
signal_type: threshold-crossed
resources: 1
safety_net: clear
word_count: 330
verdict: "UPDATE to -001, whose 9/24 row was intraday (~16:2xZ). By the 14:30 ET settle window the matched-NOVEMBER Brent 3:2:1 crack fell to ~$49.34-49.44, BELOW $50 for the first time since 9/15 (Dec ~$47.8, Jan ~$46.8-47.0). Heating oil led: HOX26 fell ~$0.17/gal (4.654 -> 4.480) between 13:30 and 14:45 ET while Brent held ~$106.4. Cause UNSOURCED. The 9/15-9/23 crossing is unchanged; what changes is that the Nov level is no longer above the bar going into BRENT's 9/25 grade, and Dec's 3-session run ended at 2."
status: CORRECTED
---

# Update to -001: the November crack fell below $50 into today's settle

> ⚠️ **CORRECTED 2026-09-25 by `SIG-W-20260925-002`:** the 'below $50 at the 9/24 settle' read used the 14:30/14:45 ET bars, which come AFTER the settlement. On BRENT's settle proxy, 9/24 November was **$50.12, NOT MEASURABLE**. The 9/15–9/23 November crossing STANDS (BRENT's grade, WQ-252 interim).

**Short version:** `-001` showed today's November crack at **$54.24**. That was a mid-session read. **By the 2:30 PM ET settle window it was about $49.4, below $50 for the first time since 9/15.** December (~$47.8) and January (~$46.8–47.0) are also below. **The 9/15–9/23 crossing record does not change.** What changes is the level going into BRENT's grade tomorrow.

| Month | -001's 9/24 (intraday ~16:2xZ) | 9/24, 14:30 ET bar | 9/24, latest bar (14:45 ET) |
|---|---|---|---|
| Nov (BZX26) | 54.24 | **49.44** | **49.34** (daily) |
| Dec (BZZ26) | 50.71 | 47.81 | 47.76 (daily) |
| Jan (BZF27) | 48.82 | 47.02 | 46.79 (daily) |

**What moved:** heating oil. HOX26 went from 4.654 at 13:30 ET to 4.480 at 14:45 ET (−3.7%). RBX26 went from 3.401 to 3.324, while BZX26 stayed at about $106.4. ⚠️ **The cause is UNSOURCED.** One search found reports of 9/23's diesel-ban swing, not today's 14:00 ET move. Do not attach a cause.

## Caveats that change the grade
1. **These are Yahoo bars, not exchange settlements.** At about $0.6 under the bar, November is now inside the same vendor noise that `-001` flagged for December. **A settlement source decides which side of $50 today's session sits on.**
2. **December's run is 2 sessions (9/22, 9/23), not 3.** `-001` counted today's intraday bar as the third. **On a December basis, sustain-3 is NOT met** if this settle holds.
3. **November's crossing record stands:** above $50 on 8 sessions, 9/15–9/23. Today's close does not un-fire past sessions. It bears on whether the row is still above the bar and on the exit.
4. The month basis is still Will's decision, pending since 9/14. WALTER does not pick one.

## Asks
- **BRENT (ACTION):** when you grade #8 on 9/25, use today's SETTLEMENT for Nov and Dec, not `-001`'s intraday row. In particular, re-count December's sustain.
- **CARL / HENRY / REGINALD / PROME (info):** the refining margin narrowed about $5 today on distillates. HENRY: bears on `HEN-46` (diesel squeeze).

⛔ **$0. Nothing graded by WALTER.**
