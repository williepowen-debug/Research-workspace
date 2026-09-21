---
signal_id: SIG-W-20260921-008
date: 2026-09-21
timestamp: 2026-09-21T16:1xZ
time_dispatched: 2026-09-21T16:1xZ
source: WALTER
origin: ["Will-Telegram 6-image batch 2026-09-21 ~15:14Z, item 2 of 7 (batch BM-20260921-02): @jasongoepfert (SentimenTrader), with a StockCharts panel stamped 19-Sep-2026"]
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
precedence: PRIORITY
action: ["HENRY", "RED"]
info: ["VIOLET", "LIQUID", "NEXUS", "PROME"]
entities: ["SPX", "SPY", "pct-above-200DMA", "net-new-highs-lows", "SentimenTrader", "Jason-Goepfert"]
confidence: 0.55
confidence_language: the CHART's visible values are read directly off the capture; the 100-year superlative and the 1973/1999 analogs are NOT verifiable from what is shown and WALTER does not hold the underlying composite
signal_type: thesis-confirmation
resources: 1
safety_net: clear
word_count: 690
verdict: "Jason Goepfert (SentimenTrader): 'We've never in almost 100 years seen breadth this bad' — S&P near highs with many more stocks at lows than highs, the share of stocks in long-term uptrends plunging, and 'the only remotely similar setups were January 1973 and November 1999.' ⛔ THE SUPERLATIVE IS NOT SHOWN BY THE CHART BENEATH IT. The visible panels read % of stocks above the 200-day MA = 52.00 and net highs-minus-lows = −4.40, neither of which is a 100-year extreme on its face. The claim rests on a composite WALTER does not hold. Routed as a NAMED CLAIM to the desks that own breadth and adversarial review, NOT as an established fact."
---

# Goepfert says breadth is the worst in 100 years, with 1973 and 1999 as the only analogs — and the visible chart does not show it

## THE CLAIM

**@jasongoepfert (SentimenTrader)**, captured 2026-09-21 ~11:42:

> *"We've never in almost 100 years seen breadth this bad. The S&P \$SPY is knocking on new highs but there are (many) more stocks at lows than highs. The percentage of stocks in long-term uptrends is plunging. **The only remotely similar setups were January 1973 and November 1999.**"*

🔑 **The two named analogs are the payload.** January 1973 is the top of the Nifty-Fifty market before a ~48% drawdown; November 1999 is four months before the dot-com peak. **Naming those two dates is a regime claim, not a breadth observation** — and it is the kind of claim that moves positioning if believed.

## ⛔ WHAT THE CHART ACTUALLY SHOWS — AND IT IS NOT OBVIOUSLY A 100-YEAR EXTREME

Read directly off the StockCharts panel in the capture (stamped **19-Sep-2026**):

| Panel | Value |
|---|---|
| `$SPX` S&P 500 Large Cap Index (daily) | Open 7657.17 · High 7657.17 · Low 7650.50 · **Close 7650.50** · Chg +12.74 (+0.17%) |
| **S&P 500 Percent of Stocks Above 200-Day Moving Average** | **52.00** |
| **Net New Highs − New Lows Percent** | **−4.40** |

🔴 **52% of stocks above their 200-day average is middling, not a 100-year extreme.** Net new highs minus lows at **−4.40%** with the index near a high is a genuine **divergence** — but the visible panels do not, on their own, support *"never in almost 100 years."*

⇒ **The superlative rests on a composite Goepfert has and WALTER does not.** ⛔ **That is not an accusation that the claim is wrong** — SentimenTrader's whole business is long-history breadth composites and it plausibly has the series. **It is a statement that the evidence shown does not establish the claim made**, and the two must not be conflated.

⚠️ **A 100-year claim also has a survivorship and definitional problem no chart can settle:** index membership, listing counts and what counts as a "new low" are not constant across 1929→2026, so *"never in almost 100 years"* is a claim about a **reconstructed** series whose construction is the whole argument. **Ask for the construction before adopting the conclusion.**

⚠️ **Minor basis note, flagged not resolved:** the chart is stamped **19-Sep-2026, a Saturday.** Most likely the platform is labelling the last bar or the generation date; the SPX close of 7650.50 is consistent with our own SPY 769.20 [9/21 live, +0.99%] at the usual ~10× ratio. **Not load-bearing, but the date on the capture is not a trading day.**

## RECIPIENT ACTIONS

**HENRY — ACTION.** Index mechanics, breadth and market structure are yours. **The ask: do your own breadth series agree that this is an extreme, and on what construction?** Specifically — is *"percentage of stocks in long-term uptrends"* a series you carry, and does the divergence show up on it? ⛔ **WALTER is not asking you to grade Goepfert; it is asking whether OUR instruments see the same thing**, which is the only version of this question this desk can answer.

**RED — ACTION.** This routes to you on the **thesis-confirmation meta row**, and deliberately: **it is a claim that flatters the bear case, which is exactly the class this desk should be hardest on.** ⚠️ **An extreme-absolute superlative from a credible source with an unshown denominator is the shape that gets adopted because it is congenial** (`[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`). **The ask: is there a registered RED trigger this bears on, and if not, does the 1973/1999 analog claim deserve one — or is it unfalsifiable as stated?**

**VIOLET — info.** Breadth deterioration under a rising index is a vol-regime input, not a vol-regime reading.
**LIQUID — info.** Narrowing leadership is the equity-side counterpart to spread breadth, which is your `FUNDING_LIQUIDITY` HY-breadth lane (*an index that stays calm while breadth deteriorates is invisible to both OAS-level triggers by construction* — the same shape, a different market).
**NEXUS — info.** A named regime analog is cluster-narrative material; **WALTER does not re-mark any `PRED-NN`.**
**PROME — info** (BOARD ID-diff; pull-complete).

## ⛔ NOTHING FIRES

**No registered threshold moved, no sustain count changed, no score changed, $0.** No band on this board keys on breadth. ⚠️ **Stated so the gap stays countable: if the strongest bear-side observation available today cannot trip anything we have registered, that is an instrument gap, and closing it is HENRY's or RED's proposal and Will's ruling — not WALTER's.**

## CROSS-REFS

`SIG-W-20260919-001` (off-RTH fill-forward — the same desks, the instrument-basis family) · `RED-FT-06` (VIX `<16 s5`, FIRED-BANKED; `^VIX` 14.64 [9/21 live], exit `≥18 s5` at 0 — **the vol complex is nowhere near confirming a breadth-driven regime change**) · `RED-FT-10` (SKEW `≥150 s4`, 148.10 [9/18 close], 0-of-4).
