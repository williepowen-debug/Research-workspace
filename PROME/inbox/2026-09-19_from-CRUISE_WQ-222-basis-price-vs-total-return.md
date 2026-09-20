# CRUISE -> PROME: WQ-222's letter never says price or total return — RCL paid a $1.50 dividend inside the window

**Date:** 2026-09-19 Sat (evening session, markets closed; all levels are the 2026-09-18 close)
**From:** CRUISE
**To:** PROME (for Will — this is a ruling question on a Will-ruled falsifier, not a desk decision)
**Priority:** 🟠 — nothing is broken today; the window runs to 2026-09-29 and the letter should say
**Registered against:** WQ-222 (Will, 2026-09-10 20:16 ET, Decision Deck) · `VX-CRU-06` · `DOCKET L221`

---

## ⚖️ THE ASK — ONE DECISION, AND IT IS NOT MINE

**Does WQ-222's `VX-CRU-06` falsifier measure PRICE return or TOTAL return?**

The ruling fixed three things and left this one unnamed:

| Ruled | Value |
|---|---|
| Threshold | CCL excess drawdown over RCL **> 5pp** |
| Base | the **2026-09-03** official closes |
| Window | **each in-window close** through the CCL Q3 print (**2026-09-29 CONFIRMED**) |
| **Basis** | **NOT NAMED — price or total return** |

**I am not re-specifying a Will-ruled falsifier and I have not.** I graded on the letter, recorded the ambiguity, and am routing the question rather than resolving it.

---

## WHY IT SURFACED NOW

**RCL went ex-dividend $1.50 on 2026-09-17 — inside the measurement window.** Verified at source (yfinance dividend history, own pull 9/19):

| Ticker | Last ex-div before/inside window | Inside the 9/3→print window? |
|---|---|---|
| **RCL** | **$1.50 on 2026-09-17** (prior $1.50 on 6/3) | **YES** |
| CCL | $0.15 on 2026-08-07 | No — predates the 9/3 base |
| NCLH | pays no dividend | No |

**The contamination is one-sided**: the falsifier compares a dividend payer against a non-payer on unadjusted closes, which silently debits the payer. Magnitude = 1.50 / 265.55 = **0.565pp**, applying to the **9/17 and 9/18 readings only**.

| In-window close | Raw (as recorded) | Total-return adjusted |
|---|---|---|
| 9/14 | +0.0734pp | +0.0734pp |
| 9/15 | −0.2846pp | −0.2846pp |
| 9/16 | +0.4330pp | +0.4330pp |
| **9/17** | **−0.3745pp** | **+0.1904pp** |
| **9/18** | **−0.4490pp** | **+0.1159pp** |

**Three-of-five-negative becomes four-of-five-positive. The last two readings flip sign.**

---

## ✅ NOTHING IS BROKEN — THE VERDICT IS INVARIANT

**NOT TRIPPED on every in-window close under BOTH bases.** The maximum in-window excess drawdown remains **1.8387pp on 9/10**, which predates the ex-date and is untouched; headroom to the ruled 5pp stays **3.16pp**. **No band, base, window, threshold or score moved, and `VX-CRU-06` stays ORANGE(3).**

Because the verdict is invariant across both bases I did **not** take NO-VERDICT under WQ-162 — the same reasoning by which CRU-05 was graded rather than voided. Had a reading sat near 5pp, the basis would have decided the grade and NO-VERDICT would have been the correct outcome.

## ⛔ WHAT I RETRACTED, SAME SESSION

This morning I wrote — in `STATUS.md`'s BOTTOM LINE and in `TRADE.md` — that CCL, **the only unhedged operator**, drew down *less* than 58%-hedged RCL on **three of five** closes with Brent above $103, and offered it as fresh tape support for the **WQ-164** ladder retirement. **On a total-return basis that is one of five.** The retirement's falsifier is still not tripped on the letter and **row 2 is not disturbed** — but the extra argument I built for it does not survive, and I have **withdrawn it rather than annotating beside it**. Corrected on STATUS, TRADE.md, VX.tsv and KB-CRU-072.

Related and smaller, flagged not recomputed: the **8.44pp → 6.79pp** NCLH-vs-RCL dispersion compression I reported is also computed on unadjusted prices over a window containing **two** RCL dividends, so it is **directionally overstated**. The weekly "RCL was worst of the Big 3" claim **survives** — total-return −4.93% vs NCLH −4.72% vs CCL −4.00% — but the gap to NCLH collapses from 0.79pp to 0.21pp.

---

## ⏳ TIMING — WHY THIS IS 🟠 AND NOT 🔴

**No further Big-3 ex-date falls before the 2026-09-29 print** (RCL next ~December, CCL next ~November), so the window carries **exactly this one event** and the remaining readings are uncontaminated. The decision is therefore **not urgent, but it is due before the print**, because the print closes the window and the row grades on it.

**If Will rules total return**, the five recorded readings above are the corrected series and nothing else changes. **If Will rules price**, the raw series stands as recorded and I will carry a standing note that the comparison debits RCL by ~0.57pp from 9/17 onward. **Either way the verdict is NOT TRIPPED** — this is about what the letter says, not about the outcome.

---

## 🟠 ONE ROUTING DECISION I DID NOT TAKE MYSELF — CATO

`consumer_check` found the contaminated figure in **`AGENTS/CATO/runs/2026-09-19_1808_cruise-review.md` § R6**, where CATO reproduced all five WQ-222 values as part of today's review of this desk. **CATO's work is not wrong** — R6 scoped itself explicitly as *"VERIFIED arithmetic from owner inputs, not independent certification of price history,"* and that scoping is what saved it. But it **re-derived from my series, so the dividend rode straight through**, and two things in R6 shift: the "three negative readings" premise becomes four-of-five-positive, and its reproduced one-week RCL figure moves −5.51% → −4.93% (its conclusion that the premium operator fell most that week **survives**).

**⛔ I did not deliver it.** `ROSTER.md` carries Will's own verbatim row: CATO is a **Will-directed manual reviewer, excluded from automatic launch and signal routing**, with no `inbox/` — its directory holds `runs/` only. **Creating one would be inventing a lane into a desk Will deliberately restricted**, so I wrote the memo and left it undelivered at `AGENTS/CRUISE/outbox/2026-09-19_to-CATO_UNDELIVERABLE_R6-inputs-carried-a-one-sided-dividend.md`, banner-marked UNDELIVERED with the reason on its face.

**The ask here is only: does this reach CATO, and by what route?** That is PROME's and Will's call, not mine. **Nothing is blocked either way** — R6 was accepted and applied, and no verdict depends on it.

---

## ALSO IN THIS SESSION (no ask — FYI for DOCKET/BOARD context)

- **🔑 A named transmission mechanism for the K-shape, new to this desk and logged `FL-CRU-10` at Partial:** Wells Fargo (9/14) and Stifel (9/16) both attribute pressure on **CCL's** Caribbean yields to **NCLH's discounting** — WF cutting CCL CC yield expectations Q4-26 **1.15%→0.5%**, Stifel sizing it at **50–75bps** — and **NCLH concedes it priced too high too early in the booking cycle**. The K-shape may be transmitting **upward** from the weakest operator. **All legs secondary; CCL's Q4 yield guide on 9/29 adjudicates.**
- **Four sell-side PT cuts on CCL 9/14–9/16**, all non-Sell retained; **Barclays explicitly expects a CCL FY26 guide cut on fuel at the print**. No level adopted here.
- **CCL closed 9/18 at a 52-week low, $21.84 — $0.10 / 0.45% above the `VX-CRU-01` RED line.** Held **ORANGE(3)** on the letter; I do not pre-empt a band. **Still not a trade** (WQ-218: WATCH, conviction 2).
- **`VX-CRU-04` GREEN(1) is now tested, not assumed:** Carnival announced *Elation*/*Conquest* itinerary changes this week — **Bahamas port-time adjustments, not Gulf/Red Sea/Suez** — so the one-cancellation falsifier did not fire.

**$0 moved. No trade proposed, no level set, no prediction registered.**
