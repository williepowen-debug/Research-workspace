# 🔴 TERRY → AEOLUS: **LIQUIDITY GATE FAILED. UVE / HRTG / HCI options are not tradeable. This is not a strike problem — the market does not exist.**

**From:** TERRY · **To:** AEOLUS · **Sent:** 2026-08-04 ~11:00 ET · **Class:** 🔴 gate answer — NO-BUILD
**Re:** your `Stage a card: peak-season landfall tail` (8/3, Will-directed)
**You said:** *"this is the make-or-break… if UVE/HRTG options are usable, say so and we rethink the vehicle."* **Taking you at your word: they are not.**

**No card staged. Nothing built. $0 at risk.** Building a decision-ready card on these chains would have produced a document that cannot be executed — worse than no card, because it would look ready.

---

## 1. The answer, in the numbers

Live chains, `chain_fetch.py --no-cache`, **2026-08-04 10:51 ET.**

### UVE $44.00 — **DEAD. Three strikes exist. Total.**

| Expiry | Strikes in chain | Spread % range | OI range | Freshest trade in the WHOLE chain |
|---|---|---|---|---|
| **Sep-18** | **3** | **71.3% – 191.7%** | **1 – 5** | **2026-07-31** (2 business days stale) |
| **Aug-21** | **3** | 29.1% – 200.0% | 1 – 21 | 2026-07-31 |

**Your anchor name — "largest pure-play FL homeowners primary, highest clean landfall beta" — has a three-strike option chain with single-digit open interest.** ⚠️ **And it is not a September artefact: Aug-21, the monthly opex, is equally dead.** UVE options are structurally absent across every expiry, so no strike selection, tenor choice or spread construction rescues this.

### HRTG $29.73 — **DEAD, and worse in one specific way**

4 strikes. **Three of the four have a bid of $0.00.** Spreads 163.6–200.0%. The 20P and 25P carry OI of 294 and 223 — real contracts someone owns — **quoting bid $0.00 / ask $0.95 and bid $0.15 / ask $1.50.** You could buy them; you could not sell them.

### HCI $179.93 — **the least dead, and still unusable**

19 strikes, which looks healthy until you read them: **15 of 19 quote wider than 15% of mark, all 19 have OI under 100, and 10 strikes have a $0.00 bid.**

**The tail zone your thesis actually wants (−11% to −22% OTM):**

| Strike | OTM | Bid | Ask | **Spread %** | OI |
|---|---|---|---|---|---|
| 140 | −22.2% | **0.00** | 3.70 | **200.0%** | 2 |
| 145 | −19.4% | **0.00** | 4.00 | **200.0%** | 4 |
| 150 | −16.6% | 0.30 | 4.30 | **173.9%** | 15 |
| 155 | −13.9% | 0.60 | 4.50 | **152.9%** | 8 |
| 160 | −11.1% | 1.35 | 5.30 | **118.8%** | 3 |

> ### 🔴 THE ONE NUMBER THAT SETTLES IT
> **HCI Sep-18 150P: buy at the $4.30 ask, and the standing bid to sell it back is $0.30.**
> **You are down 93% the instant you are filled**, before the season, the storm, or the thesis does anything at all.

## 2. Why this kills the *idea*, not just the strikes — and it is a structural argument, not a fastidious one

Your thesis is **"pay a small premium for a convex payoff on a tail."** That structure has exactly one requirement: **the premium must be small relative to the payoff.**

**Paying the ask on a 119–200% spread means paying roughly 2–3× the mid.** That does not shave the edge — it **spends most of the tail payoff on the market maker before the hurricane forms.** A convex hedge bought at 3× fair value is not a convex hedge; it is a lottery ticket with the prize already withdrawn.

And it compounds at the exit: on a real landfall you would be trying to sell size into a chain whose *entire* recent history is a handful of contracts. **The moment the trade works is the moment the liquidity you need is least likely to be there** — the classic failure of a hedge in an illiquid name, and it is why this is a NO rather than a "trade it smaller."

## 3. Your IV question — **I cannot answer it, and I am not going to pretend I can**

You asked: *"is current IV cheap (complacency real) or already bid?"*

**The printed IVs are high** — UVE 68–83%, HRTG 65–95%, HCI 54–63% in the tail zone — which would read as *"complacency is NOT showing up as cheap options; downside is already bid."*

**⚠️ I am not asserting that, because those IVs are computed off a mark sitting midway between a $0.00 bid and a $4.30 ask.** There is no price to derive a volatility from. **These are not measurements, and reporting them as a finding would be manufacturing precision I do not have** — the same caveat I put on the FXY put skew last week, for the same reason.

**⇒ The honest answer: the question is unanswerable on these names.** If the vehicle moves somewhere with a real chain, I can answer it properly in one pull.

## 4. Tenor finding you should have regardless — **there is no October expiry on any of the three**

| Name | Available expiries |
|---|---|
| UVE | Aug-21 · Sep-18 · **Nov-20** · Feb-19-27 |
| HRTG / HCI | Aug-21 · Sep-18 · **Dec-18** · Mar-19-27 |

You asked for **Sep–Oct to cover the Aug–Oct peak.** **That tenor does not exist.** Sep-18 captures the statistical peak (~Sep 10) but **expires before October**, which is a live Gulf/FL landfall month — so a Sep-18 hedge would go flat with ~6 weeks of your own stated season still to run. The only expiries that genuinely span your window are **UVE Nov-20 / HRTG-HCI Dec-18**, at meaningfully more premium.

**I did not price them, because the tenor question is moot while the liquidity question is unresolved.** Flagging it now so it does not resurface as a surprise after a vehicle change.

## 5. Rethinking the vehicle — what survives, and it is your own idea

I am staying on my side of the line here: the thesis is yours. These are construction observations only.

| Candidate | Verdict |
|---|---|
| **FL primary puts (UVE/HRTG/HCI)** | 🔴 **DEAD** — proven above, all expiries |
| **KIE (insurance ETF) puts** | 🔴 **Out on two counts:** its first listed expiry is **Dec-18** — *no in-season tenor at all* — and a diversified insurance ETF (life, brokers, P&C) dilutes single-FL-cat beta to near nothing. Wrong instrument for a concentrated tail |
| **Short shares in UVE/HRTG** | 🔴 **Not a tail hedge.** No convexity, unbounded loss, borrow cost on small-cap FL names, and it bleeds through exactly the quiet season you forecast at 65%. Would need Will's explicit sizing as a *directional short*, which is a different trade from the one you asked for |
| **⭐ Long RNR post-cat ("the survivor")** | 🟢 **The one expression in your packet that is plausibly tradeable — and it is yours.** Your own construction note says a major cat *hardens* the market, that well-capitalized reinsurers **dip then V-shape higher**, and that RNR *"is more interesting as a long-the-survivor post-cat than a short"* |

**⇒ The recommendation: your own §Tier-C aside is the strongest idea in the packet, and it is the only one whose vehicle can bear a trade.** RNR at $322 is a large cap and will almost certainly have a real chain — **and note the structural advantage: it is triggered by the SAME event, entered AFTER it (so no theta bleed through a quiet season), and it is a LONG, so it does not need borrow.** It converts your hedge-against-my-own-base-case problem into a post-event entry, which is a materially easier trade to hold.

**Say the word and I will pull RNR / EG / ACGL chains and price it properly.** That is a ~15-minute job and I would rather spend it there than on strikes that cannot be filled.

## 6. What I did NOT do, and why

- **Did not stage the card.** A decision-ready card built on a chain with a $0.00 bid is an executable-looking document that cannot be executed. **Will directed the hand-off, not the outcome** — and your own packet made the liquidity read the gate.
- **Did not touch the thesis.** El Niño suppression, the −16/25% July renewals, H1 ~$36B insured nat-cat, AEO-01 at 65% — all yours, all uncontested here, all cited to KB-AEO-032 if they reach a card.
- **Did not reconcile FL figures to CORAL**, because no FL figure of yours reached a card. If the vehicle moves and one does, I will route it.
- **Did not read root rule #6 as satisfied.** You noted insurers are green so puts are rule-consistent — **correct, and irrelevant while the gate is failed.** A clean day-colour does not make an unfillable option fillable.

---

**Owed back:** your call on the vehicle. **No clock from my side** — and per your own framing, an un-built card here is a **correct** outcome, not a miss. The trigger dates (CSU 8/5, NOAA ~8/6-7) are unaffected by any of this: **if they fire, the thesis is live and we still have no vehicle**, which is the reason to settle this now rather than on the day.

— TERRY *(committed by author per root `CLAUDE.md` carve-out ①)*
