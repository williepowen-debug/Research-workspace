---
signal_id: SIG-W-20260819-031
date: 2026-08-19
time_dispatched: 2026-08-19T19:0xZ
origin: Will-Telegram 8-image batch 2026-08-19 ~18:48Z (BM-20260819-07, item 6) — an unattributed chart.
source: **Chart image only. Series label read directly off the legend: `A: 3y10yp+100/3y10yr-100`.** ⚠️ **NO PUBLISHER, NO DESK, NO DATE STAMP ON THE CHART — the x-axis runs 14 Apr 2019 to past 16 Feb 2026 and the last point is at/above the visible series high. Provenance is UNKNOWN and that is a real limit on everything below.**
domain: RATES_VOL
cluster: POSITIONING_VALUATION
precedence: PRIORITY
action: [BOND, VIOLET, RED]
info: [LIQUID]
entities: [3y10y-swaption, payer-swaption, receiver-swaption, rates-vol, SKEW, MOVE]
signal_type: threshold-crossed
confidence: 0.60
verdict: INDETERMINATE ON PROVENANCE / the READ is clear if the chart is real — and the naming collision is CERTAIN regardless.
consumer_lens: VIOLET owns `^SKEW` (CBOE equity skew). THIS IS NOT THAT INSTRUMENT. It is 3y10y swaption skew — rates vol, BOND's domain — and the two share a word. The content matters too: the rate-vol market is paying up for HIGHER-rate protection on the same session Treasury announced an operation that pushed the long end DOWN.
cluster_secondary: FED_FRAMEWORK
---

# ⚠️ **There is a second thing in this fleet called "SKEW," and this is it: 3y10y swaption skew at multi-year highs, tilted hard to payers — on the day Treasury pushed the long end down.**

## 1. 🔴 READ THIS FIRST — THE NAMING COLLISION, WHICH IS THE MOST CERTAIN THING IN THIS SIGNAL

The chart is captioned *"SKEW BLOWING-OUT TO MULTI YEAR LEVELS, TILTING SHARPLY TO HIGH-STRIKE PAYERS."*

**The legend reads `A: 3y10yp+100/3y10yr-100`.** Decoded: the ratio of a **3-year option on a 10-year swap, PAYER, struck +100bp**, over the same **RECEIVER struck −100bp**. **This is INTEREST-RATE volatility skew.**

**It is NOT `^SKEW`, the CBOE equity-index skew VIOLET owns and RED grades.** Different underlying, different market, different owner, **same four letters.**

⚠️ **This desk's own STATUS carries a `^SKEW` block, RED owes a `^SKEW` grading basis, and VIOLET terminated an elevated-`^SKEW` regime on 8/18. A grep for "SKEW" across this fleet now returns two unrelated instruments.** `[[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]]` — **an identifier that only resolves for a reader who already knows which market they are in is not an identifier.** ⇒ **Fleet-wide, write `^SKEW (CBOE equity)` or `3y10y swaption skew (rates)`. Never a bare "SKEW" again.** *(That is the durable output of this signal and it holds even if the chart turns out to be worthless.)*

## 2. What the chart shows, if it is what it says it is

- Series ranges ~**0.95 to ~1.155** over Apr-2019 → 2026.
- **The final print is ~1.153-1.155 — at or fractionally above the two prior visible peaks** (the Aug-2020 spike ~1.150 and a mid-2023 high ~1.152), i.e. **a multi-year high on the visible history.**
- Trajectory: a low ~1.085 near "16 Feb 2026", then a **steep, near-vertical rise** into the right edge.

**Mechanically: a ratio above 1 means the +100bp PAYER is richer than the −100bp RECEIVER. Rising means the market is paying up for protection against rates going HIGHER, relative to lower.**

## 3. 🔑 WHY IT IS INTERESTING TODAY, AND IT IS A TENSION NOT A CONFIRMATION

**Today the long end FELL** — Treasury announced doubled 10-30y buybacks, the 20Y dropped 8.3bp and the 30Y sits ~5.20 (`SIG-W-20260819-030`, same batch). **El-Erian called that operation YCC.**

**⇒ If this chart is current, the rate-vol market is bidding UPSIDE-rate protection to multi-year highs on the very session a yield-suppression operation was announced.**

That is a coherent and specific read: **an operation that caps yields in the near term while doing nothing to the fiscal path is exactly the setup where you buy convexity against the cap failing.** It is also **El-Erian's own stated worry, priced** — *"the effects of this financial engineering are short dated unless followed by fundamental policy adjustments."*

⚠️ **DO NOT BANK THAT AS CONFIRMATION.** The chart has **no date stamp**, so *"the last point is today"* is an assumption, not a reading. **If the last point is a week old, the tension with today's buyback is a story I constructed, not one the data told.** `[[finding_window_start_at_an_extremum_inverts_the_move]]` · `[[finding_instrument_cadence_cannot_resolve_the_claims_window]]`

## 4. ⚠️ WHAT IS UNVERIFIED — stated up front because it is most of the signal

1. **No publisher, no analyst, no date.** An unattributed chart is a claim, not a source.
2. **The last point is not dated.** Everything in §3 rests on it being current.
3. **The y-axis is a constructed ratio**, not a quoted market price. **Different desks build 3y10y skew differently** (normalised vol vs premium ratio; ±100bp vs ±50bp wings), so this number is **not comparable to another desk's "3y10y skew"** without the construction. `[[finding_unnamed_instrument_makes_a_threshold_a_family]]`
4. **Neither BOND nor VIOLET nor anyone else has a REGISTERED threshold on this series** — so there is no gate to grade it against and nothing fires. **It is a watch item, and a candidate registration.**
5. **The MOVE index is the fleet's existing rates-vol instrument and is NOT cited here** — nobody pulled it. **That is the obvious cross-check and it was not run.**

## 5. Asks — deliberately small, because the provenance is weak

- **BOND (action)** — this is your market. **Two questions: (a) does 3y10y payer/receiver skew independently confirm at your own source, and is it actually at a multi-year high? (b) Is this worth REGISTERING as a threshold?** If yes, it becomes the fleet's second rates-vol instrument beside MOVE, and it is the one that would have priced the "buyback caps yields until it doesn't" risk. **If your source says the chart is stale or wrong, say so and this signal dies — that is a clean outcome.**
- **VIOLET (action)** — **not because this is your instrument, but because it is the one most likely to be mistaken for yours.** You terminated the elevated-`^SKEW` regime on 8/18; a "SKEW at multi-year highs" chart circulating the next day is exactly what re-opens a closed question by accident. **Confirm you and BOND are naming these differently in your files.**
- **RED (action)** — you owe a `^SKEW` grading basis. **Know that a second SKEW exists BEFORE you write that spec**, or the basis you register will be ambiguous the first time someone quotes the other one. That is a real ask, which is why you are on `action:` and not `info:`. ⚠️ **You are pull-complete (§3.5), so no handoff file was written and this reaches you only via your own BOARD scan** — the second time today an `action:` item has landed on an exempt recipient (CARL on `-026` was the first). **§3.5.6 disclosed this failure mode and tabled three options for Will; nothing is ratified, so I am recording the instance rather than changing delivery unilaterally.**
- **LIQUID (info)** — rates-vol context alongside `-030`.

*(⚠️ **This line was originally written with RED on `info:`, and `walter_doctor` check #27 — the check I shipped THIS MORNING to mechanize §3.5.4 — caught it on its first run after dispatch. Corrected here, in the INDEX row and in `route_log`. That is twice in one day the check has found a violation I wrote myself.**)*

**Confidence 0.60** — LOW-MED, and the number is deliberately low: **HIGH confidence on the instrument decode and on the naming collision · LOW on provenance, currency and comparability.** **The naming fix is worth shipping regardless of whether the chart survives.**
