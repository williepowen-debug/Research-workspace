---
signal_id: SIG-W-20260819-002
date: 2026-08-19
time_dispatched: 2026-08-19T03:2xZ
origin: Will-Telegram 8-image batch 2026-08-19 ~02:59Z, items 6/7/8 of 8 (batch BM-20260819-01). Three screenshots of the SAME chart — @zerohedge 8/17 7:41 PM ET ("Diesel crack hits record $102"), @HormuzLetter 8/17 11:21 PM ET ("record $102.20"), and a third capture of the zerohedge post inside a quote-stack. WALTER re-derived the spread from futures rather than accepting any of the three.
source: **WALTER's own `fetch.py` pull, 2026-08-19 ~03:1xZ.** Front-month NYMEX heating oil `HO=F` and WTI `CL=F` daily closes; crack computed as `HO x 42 - CL`. 8/17: 4.44 x 42 - 84.50 = **$101.98/bbl**. 8/18: 4.38 x 42 - 84.82 = **$99.14/bbl**. Gasoline crack `RB=F x 42 - CL`: 8/17 = $52.84, 8/18 = $42.44. Cross-check: the posted chart's own legend reads **101.931** for 8/17, against WALTER's independently computed 101.98 — agreement to ~$0.05 on a $102 number, which validates the METHOD and therefore the 8/18 figure derived the same way.
domain: OIL_ENERGY
cluster: INFLATION_TRANSMISSION
precedence: IMMEDIATE
action: [TERRY, BRENT]
info: [HAWK, CARL, HENRY, MARCO, RED]
entities: [HO=F, CL=F, RB=F, VLO, TRY-BRENT-DIESEL, diesel-crack, gasoline-crack, XLE]
signal_type: threshold-crossed
confidence: 0.85
verdict: CONFIRMED-AT-OWN-DERIVATION, with two corrections to the originating claims
consumer_lens: TERRY holds `TRY-BRENT-DIESEL` (VLO as refiner proxy) at verdict "NO AT THIS PRICE" — a verdict priced explicitly against a $82.70/bbl crack read on 7/24 closes. The crack has since moved ~+$17 to ~+$19. The card's gate is a PRICE gate, so the level is the card. BRENT owns the sizing and the 3-2-1 blend; HAWK owns the refinery-outage mechanism this is the clean instrument for.
cluster_secondary: IRAN_HORMUZ
corrects: SELF
---

# 🔴 **The record diesel crack is REAL — I re-derived it at $101.98 — and TWO things are wrong with how it is travelling: it has ALREADY given back $2.84, and the GASOLINE crack collapsed $10.40 in the same session. "Energy pass-through" is the wrong frame; this is distillate-specific.**

## 1. The claim, verified independently

The three posts assert a record US diesel crack of "$102" / "$102.20". **I did not take the number on report.** Computed from front-month futures closes, `HO x 42 − CL`:

| Date | `HO=F` | `CL=F` | **Diesel crack** |
|---|---|---|---|
| 2026-08-13 | $4.25 | $81.25 | $97.25 |
| 2026-08-14 | $4.28 | $82.40 | $97.36 |
| **2026-08-17** | **$4.44** | **$84.50** | **$101.98** ⬅ the record |
| **2026-08-18** | **$4.38** | **$84.82** | **$99.14** ⬅ **already off it** |

**The posted chart's own legend reads `101.931`.** My independent derivation lands at `101.98`. **Two methods, one number** — the record is real and the instrument is what it says it is.

## 2. 🔴 CORRECTION #1 — the level is not current, and it is a MONDAY high being read on a WEDNESDAY

Both posts are timestamped **Monday 8/17 evening** (zerohedge 7:41 PM ET, HormuzLetter 11:21 PM ET). **They were correct when written.**

**By Tuesday 8/18's close the crack was $99.14 — $2.84 off the record.**

This is precisely the distinction VIOLET taught this desk on 8/18 and it is worth restating in its inverted form: **a DATED observation does not rot — but the UNDATED derivative of it does.** "The diesel crack hit a record $102 on 8/17" remains true forever. "**The diesel crack is at a record**" became false roughly 20 hours after it was written. Anyone reading these posts today, unstamped, inherits the second sentence.

**⇒ Cite `$101.98 [8/17 close]` and `$99.14 [8/18 close]` together. Never the record alone.**

⚠️ **Labeled data caveat:** the 8/18 futures bars carry unusually thin volume (`HO=F` 1,170 vs a ~35-40k norm; `CL=F` 10,869 vs ~190-250k), and the 8/14 and 8/17 bars report **identical** volumes on all three contracts — a duplication artifact in the feed. **The 8/18 direction is corroborated independently** by `^OVX` −10.87% and `RB=F` −7.49% the same session, so I am confident in the SIGN and approximately in the SIZE, less so in the last decimal.

## 3. 🔴 CORRECTION #2 — the $102.20 figure is not supported by the chart posted beneath it

@HormuzLetter's headline says **$102.20**. **The chart in that same post reads `101.931`.** The post contradicts its own evidence by $0.27.

Trivially small in dollars, and stated anyway, because **the number that travels is the headline, not the legend** — and this one is already one hop from its source. @HormuzLetter's body text is also **verbatim** zerohedge's ("Industrial economy either grinds to a halt or consumers about to be hit with the biggest energy pass through in history"), posted 3h40m later. **Two accounts, one channel.** Do not count this as two-source corroboration; the corroboration in this signal comes from my own derivation, not from the second post.

## 4. 🔑 THE FINDING — diesel and gasoline VIOLENTLY diverged, which breaks the framing both posts use

Both posts extrapolate to a general energy cost shock: *"food is about to get a lot more expensive… everything moved by truck or ship will drive inflation higher"* / *"the biggest energy pass through in history."*

**The gasoline crack, same instrument family, same two sessions:**

| Date | `RB=F` | **Gasoline crack** | **Diesel crack** | Spread between them |
|---|---|---|---|---|
| **2026-08-17** | $3.27 | **$52.84** | $101.98 | $49.14 |
| **2026-08-18** | $3.03 | **$42.44** | $99.14 | **$56.70** |
| Δ 1 session | **−7.49%** | **−$10.40** | −$2.84 | **+$7.56 WIDER** |

**The gasoline crack fell four times as hard as the diesel crack in a single session, and the gap between them widened by $7.56 to $56.70.**

⇒ **This is not a general energy pass-through. It is a DISTILLATE dislocation, and gasoline is going the other way.** The consumer-facing pump channel that "food gets more expensive / everything by truck" implies runs substantially through **gasoline**, which just got *cheaper* relative to crude. The channel that IS tightening is diesel/heating oil — freight, ag equipment, rail, marine, and heating ahead of winter.

**This matters because it is a testable discriminator between two mechanisms:**
- A **demand-side / general-inflation** story would lift both cracks together. **It did not.**
- A **supply-side, refinery-specific, distillate-yield** story lifts distillate and can leave gasoline behind. **That is what the tape shows.**

**And that second mechanism is the one already on this desk's record.** HAWK's `KB-HAWK-234` natural experiment (Russia 2026: ~11 refiners struck, crude exports at post-invasion highs while **diesel/gasoil loadings collapsed to 234 kbpd vs ~817 kbpd 2025-avg**) concluded: *a refinery outage does not remove barrels from the world — it re-routes them from the product pool to the crude pool. **CRUDE-BEARISH, PRODUCT-BULLISH.*** And the anchor's own 7/27 §8 named the instrument in advance: ***"The clean instrument is CRACKS AND DIESEL, not flat crude."***

**⇒ The instrument this desk pre-registered as the clean test just printed a record, and its gasoline control did not. WALTER does not grade the thesis — BRENT and HAWK do — but the pre-registration and the print should be read together, because that is the condition under which a confirmation is actually earned rather than assumed.**

## 5. TERRY gate — 🚦 QUALIFIES on T-1, and the card's own gate is a price gate

`SETUPS.tsv` read directly this session:

> **`TRY-BRENT-DIESEL`** — instrument **VLO (refiner proxy for diesel crack)**, direction long/crack-widening.
> **verdict:** *"NO AT THIS PRICE (was CONDITIONAL 7/26 → 7/30 live-marks sync; NOT-BEFORE-LOADINGS-READ added 7/30 13:15)"*
> **status:** *"NO AT THIS PRICE / SCOPE-DELIVERED — unarmed, $0 at risk"*
> **notes:** *"★ VERDICT: thesis CONFIRMED and strengthening, channel CROWDED, entry COMPROMISED — 'not at Monday's price'. LIVE-CHECKED BRENT'S METRICS (7/24 closes): **diesel (HO) crack $82.70/bbl** = ABOVE their cited ~$80; blended 3-2-1 $59.07…"*

**T-1 is satisfied on its face:** the card is live (not terminal), its instrument IS the diesel crack, and **its verdict is explicitly and only about the LEVEL** — *"not at Monday's price."* The level it was priced against is **$82.70 [7/24]**. It is now **$99.14 [8/18 close]**, having touched **$101.98 [8/17]**. **That is +$16.44 to +$19.28 on the number the verdict was written against.**

**T-3 also applies independently:** US markets are closed as this dispatches (~23:2x ET 8/18).

⚠️ **WALTER states the level and the gate; WALTER does NOT propose, re-rate, or re-arm anything.** A card that said "no at this price" against a price that has moved $17 is a card whose *stated premise* has changed — **whether that makes it better or worse is TERRY's ruling, not mine.** It cuts both ways on the card's own logic: the thesis leg strengthens, and *"channel CROWDED / entry COMPROMISED"* plausibly gets **worse**, not better, at a record with 962K views on the zerohedge post alone. **The crowding leg and the thesis leg move in opposite directions here, and the card already named both.**

Also flagged for TERRY's read: the card's **`NOT-BEFORE-LOADINGS-READ`** condition (added 7/30 13:15) intersects the Hormuz/Yanbu loadings picture, which moved again today — see `SIG-W-20260819-003`.

## 6. What is NOT established

- **No causal attribution.** I have not established WHY the distillate crack is at a record. Refinery outages, Russian product loss, seasonal heating build, low OECD distillate inventory, and freight demand are all live candidates and I am not adjudicating among them. **BRENT and HAWK own the mechanism.**
- **"Record" is asserted by the source and is consistent with the posted chart's visible history back to Dec-2025 only.** I have NOT verified it against a multi-decade series. **The chart shown covers ~9 months.** Treat "record in history" as UNVERIFIED and "highest in the visible 9-month window, by a clear margin" as CONFIRMED.
- **The $102.20 vs 101.931 discrepancy** (§3) is unresolved in the source's favour — my derivation supports the chart, not the headline.
- **`VLO` closed $350.05 (+0.82%) on 8/18** — the proxy did NOT sell off with the crack's give-back. Noted, not interpreted.
