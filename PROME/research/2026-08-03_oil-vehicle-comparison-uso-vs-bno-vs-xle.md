# Oil-long vehicle comparison — USO vs BNO vs XLE, measured live

**Date:** 2026-08-03 (~11:00 ET, market open) · **Author:** PROME · **Prompted by:** Will, "is USO the best expression of this oil long position?"
**Status:** ANALYSIS — no threshold moved, no capital, no spec changed. **Vehicle spec is BRENT's; construction is TERRY's.** This is input to them, not a decision.

⚠️ **All option marks below are ~11:00 ET intraday and MUST be re-pulled at fill** (rule #4, `[[finding_option_marks_need_live_chain]]`). The *conclusion* is expected to be durable; the *numbers* are not.

---

## 1. The decisive test — can each vehicle actually pass leg (b)?

DEPLOY GATE v2 leg (b) = **net debit ≤ 33.0% of spread width** (⇔ R:R ≥ 2.0:1) **from a live chain at fill.**

Priced the card's own structure — long ~5% OTM / short ~12–15% OTM, Sep-18 expiry (46 DTE):

| Vehicle | Spot | Spread | Width | Debit at MID | Debit PAYING THE SPREAD | % of width | Leg (b) |
|---|---|---|---|---|---|---|---|
| **USO** | $121.49 | 128 / 138 | $10.00 | $2.22 (22.2%) | **$2.70** | **27.0%** | ✅ **PASS**, R:R 2.7:1 |
| **BNO** | $47.92 | 50 / 54 | $4.00 | $1.15 (28.7%) | **$1.55** | **38.7%** | ❌ **FAIL**, R:R 1.6:1 |

**This is the whole argument.** BNO passes only if filled at mid — and mid is not reliably achievable in a thin chain. **USO passes on the conservative assumption** (pay the ask on the long, hit the bid on the short).

### Why: chain depth
| | Strikes (Sep-18) | Total call OI | Median bid-ask |
|---|---|---|---|
| **USO** | **103** | **85,454** | **13.5% of mid** |
| BNO | 23 | 9,635 | 20.0% of mid |

USO has ~**9× the open interest** and materially tighter quotes. The strike *granularity* matters independently: 103 strikes lets you actually hit "5% and 13% OTM"; 23 strikes means taking whatever exists and accepting basis drift in the structure itself.

---

## 2. Vehicle beta to the thesis — measured on today's tape

8/2–8/3 delivered a violent one-directional oil move, which is a free natural experiment on what each vehicle actually captures.

| Instrument | 8/3 move | Beta vs Brent |
|---|---|---|
| Brent (BZ=F) | **−7.33%** | 1.00 |
| WTI (CL=F) | −6.27% | 0.86 |
| **USO** | **−5.95%** | **0.81** |
| BNO | −4.88% | 0.67 |
| **XLE** | **−0.89%** | **0.12** |

**★ XLE captures ~12% of the crude move.** The card lists "XLE call spread" as the softer equity-beta alternative. On this evidence it is barely an oil instrument — a crude spike would have to be enormous before XLE calls paid, and you would be carrying broad-equity risk to get there. **Recommend demoting XLE from "alternative" to "not a viable expression of a crude tail."**

⚠️ **Honest limits on this table:** one day, one direction, and equities had their own bid today — so XLE's 0.12 is directionally right but numerically noisy. It is suggestive of a large effect, not a measured beta.

---

## 3. The real flaw — and why switching does not fix it

**The thesis is a Brent story; the vehicle tracks WTI.** Hormuz is the *waterborne* benchmark's problem. WTI is landlocked US crude. So a Hormuz disruption should widen Brent over WTI, and USO — a WTI instrument — structurally **under-expresses the upside it is being bought for**.

**Today's tape confirms the basis is dynamic, not static:** Brent fell **1.06pp more** than WTI on a de-escalation day. The Brent–WTI spread compressed to **$3.83**. Symmetrically, escalation should widen it.

**This matters because the card converts at a fixed basis.** It carries translations like *"USO $165 ≈ Brent ~$118"* and *"break-even USO ~$153.65 ≈ Brent ~$110."* Those assume a static spread. On the exact scenario the trade is built for, the spread moves **against** the conversion — so the table **flatters USO**.

### But BNO does not capture the edge
BNO fell **less** than USO today (−4.88% vs −5.95%) **even though Brent fell more than WTI**. These are futures ETFs, not spot: in a violent front-led selloff the front contract moves most and deferred contracts move less, and the two funds sit at different points on their curves.

So the theoretical Brent advantage **did not show up in realised beta**, while the liquidity cost is **certain and measured** (leg (b) fails). **Paying a known execution cost to chase an unproven basis edge is a bad trade.**

---

## 4. Recommendation

**STAY WITH USO.** The conclusion is unchanged from the card — but it is now *measured* rather than inherited (the vehicle was ratified over XLE by Will on Jun 29 and never re-tested since).

Two items routed to owners, neither actioned by PROME:

1. **→ BRENT (spec owner):** re-derive the Brent→USO translation **at fire time** rather than carrying the fixed conversion. A static basis inside a thesis whose whole mechanism moves the basis is an unforced error. Also consider demoting XLE per §2.
2. **→ TERRY (construction owner):** leg (b) currently **passes on USO with room** (27.0% vs the 33.0% limit) — so if leg (a) fires at today's close, the price test is unlikely to be the binding constraint. Re-price at fill.

---

## 5. Standing caveat the vehicle question does not touch

Vehicle selection is downstream of whether to fire at all. **Will already holds two long-oil positions** — the USO 150/165 Sep-18 call spread (~$300, filled 7/24, Robinhood) and 35 USO shares. **A new long arm deepens the same bet; it does not diversify it.** The concentration flag on TERRY's card (§9) applies: size against the thesis total, not per-card.

And per BRENT's own registered concern, leg (a) is opening **because** oil vol is collapsing on a possible de-escalation — the tape that would kill the thesis. **A better vehicle for a trade that should not be entered is still a trade that should not be entered.**
