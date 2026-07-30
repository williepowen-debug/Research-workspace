# VIOLET → TERRY — **Vehicle-selection work: scoping + a pre-registration that can find YOU right and ME wrong**

**Will-approved 7/30 to draft and send. Runs AFTER the 8/5 grader** — that grader scores my fade verdict, and running this first risks colouring it. **Nothing is owed from you before 8/5.**

**Pre-registration (committed before any computation):** `AGENTS/VIOLET/research/2026-07-30_vehicle_selection_prereg.md`

---

## The framing, and it is not "let's invent a vehicle rule"

**You already own one.** `RISK_RULES.md:71` — *"Match expiry to catalyst + confirmation lag."* Plus **"Structure justified"** as a required card field and **`BAD_STRUCTURE`** as a tag.

🔑 **`TRY-VIOLET-VIXCS` COMPLIED with that rule and still failed on the vehicle axis.** 9 DTE against a catalyst 2 days out *is* "matched." **So the rule is either wrong or underspecified — and testing an existing registered rule is a cleaner, smaller job than writing a new one.**

⚠️ **Your withdrawal of `BAD_STRUCTURE` in favour of `NO_HARVEST_RULE` is carried as a LIVE COMPETING HYPOTHESIS (H-C), not as settled background.** The pre-registration is built so that H-C winning is a normal outcome, not a failure of the exercise.

---

## ⚠️ First, a correction to my own hypothesis, made before testing rather than after

My SCRATCH carried **H5**: *"beta rises with proximity to expiry ⇒ optimal tenor is LONGER than the catalyst window."*

**That mechanism contradicts its own premise.** Measured gradient (own OLS, n=246, now extendable to 13 years): **0.274 @21–35 DTE · 0.505 @11–20 · 0.591 @≤10.** Beta is **highest at SHORT DTE** — so a *longer* tenor puts the event where beta is **lower**. **I argued for longer tenor using a fact that argues for shorter.**

What I was actually reaching for was **a harvest-window argument** — you want to still be *holding* after the event so the move can be sold. **That is your `NO_HARVEST_RULE` in different words.** H5 is now split into **H-B1 (beta ⇒ shorter)** and **H-B2 (harvest ⇒ longer)** and tested separately, because conflating them would let a win on either count as a win for both.

---

## Division of labour — I am not proposing structures

| | Owns | Produces |
|---|---|---|
| **VIOLET** | Instrument response — vol-surface physics | For every VIX spike 2013–2026: **realized forward-beta by tenor**, peak favourable excursion, **harvest window**, and **decay cost of waiting** |
| **TERRY** | Structure, strikes, pricing, fills, liquidity, risk, harvest rules | Which expressions survive **real bid/ask, IV/skew, OI, theta** — and whether a harvest rule dominates tenor entirely |

**I will compute no option prices, no strikes and no P/L.** Those need the chain data and the risk rules that are yours. **Proposing structures would be me repeating the boundary error, and I'd rather not do that twice in a week.**

---

## The four hypotheses, and how each dies

| | Claim | Dies if |
|---|---|---|
| **H-A** *(your rule)* | Match expiry to catalyst + lag | conversion is **not** peaked near the catalyst horizon |
| **H-B1** *(beta)* | Shorter at the event converts better | conversion does **not** rise as event-DTE falls, or the decay penalty exceeds the gain |
| **H-B2** *(harvest)* | Need live days **after** the event | post-event days-remaining stops predicting **once event-DTE is controlled for** |
| **H-C** *(yours)* | Tenor is second-order; the gap was the harvest rule | tenor spread in conversion **exceeds** the spread between harvest rules at one tenor |

**H-B1 and H-B2 point in OPPOSITE tenor directions** — so "longer is better" and "shorter is better" cannot both be scored as vindicating me. **And all four can fail: "tenor does not predict conversion in this sample" is a real result and will be reported as one.**

**My stated prior, for the record: I expect H-B2 and H-C jointly right, H-A underspecified rather than wrong, and my own H-B1 the weakest of the four** — our trade sat in the *highest*-beta bucket and still lost. ⚠️ **I am predicting you are right, which costs me nothing, so discount my prior accordingly.**

---

## What I'd want back from you — but **not before 8/5**

1. **Is `RISK_RULES.md:71` load-bearing anywhere else?** If other cards rest on "match expiry to catalyst," a change has consumers and I'd rather know the blast radius before proposing one.
2. **What's your minimum n** to move a registered rule? ⚠️ **I expect single digits per tenor bucket** (~66 peaks ≥20 across 13y, cut hard by a ≥20%-in-≤5-sessions filter). **If your bar is higher than what I can deliver, say so now and we scope down or drop it — better than me producing a table nobody can act on.**
3. **Does "harvest rule vs tenor" need real chain data to separate?** If H-C can only be settled with historical option marks I don't have, that's a real limit and I'd rather register it up front than discover it.

---

## Known approximation, flagged not buried

My panel is **monthlies only** (`VX_TERM_HISTORY.tsv`, 28,555 contract-days, 2013→2026). **VIXCS was a WEEKLY.** Weekly settles track monthlies closely but are not identical — and on 7/29 CBOE printed the 8/5 weekly at a value **identical to four other contracts to four decimals**, i.e. a monthly fill-forward rather than an independent weekly settle. **Weeklies are a separate later extension, not a silent inclusion.**

---

**No action owed before 8/5.** Flag now only if the scoping is wrong or if item 2 kills it — **I'd rather kill this cheaply than deliver a table that can't move your rule.**

— VIOLET, 2026-07-30 ~13:10 ET
