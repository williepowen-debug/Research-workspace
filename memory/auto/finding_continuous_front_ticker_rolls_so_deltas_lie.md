---
name: finding_continuous_front_ticker_rolls_so_deltas_lie
description: Continuous front-month tickers (=F) silently switch contracts — a LEVEL survives the roll, a DELTA or SPREAD across it is fabricated, and a COEFFICIENT fitted on it is attenuated toward zero in the direction that flatters the thesis.
metadata:
  type: reference
---

A continuous front-month symbol (`CL=F`, `HO=F`, `RB=F`, and every "front month"/"continuous contract" feed) **is not one instrument — it is a pointer that silently re-points to the next contract at the roll.** The value is correct on both sides. **The DIFFERENCE across the roll is not a market move; it is the calendar spread between two different contracts.**

**Measured, 2026-08-20 (BRENT):** `CL`, `HO` and `RB` all rolled Sep→Oct on the same session. Cracks computed as `HO=F × 42 − CL=F` printed **gasoline −$10.71** and **diesel −$3.97**. Same-contract truth: gasoline **−$1.74** (Sep) / **−$0.49** (Oct); diesel **−$0.98** / **+$0.03**. **Both September contracts closed UP.** The entire −$10.71 was the summer→winter RVP grade spread (Sep−Oct RBOB = $10.79/bbl). Two desks propagated it as a demand event; one had already told a third desk a derived number off it.

**Why it evades review:** nothing errors, both endpoints are real prints, the formula is right, and the move is large enough to look like news but not so large it reads as corrupt. It arrives **exactly when a seasonal or structural spread is widest** — which is when it is most likely to be mistaken for the very signal you are watching for.

**Rules:**
- **A LEVEL off `=F` is fine. A DELTA, SPREAD, WoW, YoY or ratio across a roll window is not.** Name the contract (`HOU26`/`CLV26`) or state the basis and check the roll.
- **Detect the roll, don't assume it:** match the continuous close against each candidate contract's close for the same date. Whichever matches is what the alias meant that day.
- **Danger dates are predictable** — every expiry; seasonally worst where grade/spec changes at the roll (RBOB summer→winter in late Aug, again in spring).
- **Cross-contract level gaps are structural, not directional.** Sep gasoline crack $49.14 vs Oct $40.17 is ~$9/bbl of RVP spec, every year. A YoY or WoW comparison straddling it is meaningless in both directions.

**⚠️ THE SECOND FACET — a COEFFICIENT fitted on a rolled series is ATTENUATED, and the bias has a predictable sign you can check against your own interest.** The rules above catch a single delta across a single roll. They do not catch what many small roll gaps do to a *regression*: they are noise in the dependent variable, so the fitted slope is biased **toward zero** (errors-in-variables). **Measured 2026-08-21 (MIDAS):** the gold/real-yield beta used as a load-bearing magnitude test — *"a −6bp yield move explains only +0.31% of a +2.83% gold move, so the rest is a debasement premium"* — was **−0.0514 %/bp on `GC=F`** but **−0.0634 %/bp on unrolled `GLD` over identical dates** (n=655; R² 0.0231 vs 0.0354). **23% steeper.** Contamination across 5,394 overlapping sessions: the two series' daily returns differ by >1.0pp on **5.6%** of days and **disagree in SIGN on 13.0%**.

**Why this one is worse than a bad delta:** the figure **reproduces perfectly on its own series**, so every re-derivation confirms it and nothing looks wrong. And the bias is **directional with respect to the analyst's thesis** — an attenuated beta understates what the control variable explains, therefore **overstates the unexplained residual**, which is exactly the quantity an analyst is usually arguing *for*. A flat "the data is noisy" caveat hides that the noise is not neutral.

**Rules for this facet:** re-fit any load-bearing coefficient on an **unrolled proxy** (ETF, spot, or a single stitched contract) before publishing it · **report both** and say **which direction the error flatters** · treat sign-disagreement rate, not just magnitude, as the contamination measure — 13% of days pointing opposite ways will not show up in a correlation summary.

**Generalization:** any auto-advancing pointer — front-month futures, "latest vintage", rolling N-day windows, `LIMIT 1` on a re-keyed series — has this shape. **The identity of what you are measuring changed while the name stayed the same.** Sibling of [[finding_derived_metric_across_vintages_biases_toward_stale_leg]] and [[finding_cross_entity_comparison_needs_same_perimeter]]; the twin where the *label* rather than the *perimeter* moves is [[finding_bypass_turns_a_flow_proxy_into_a_routing_metric]]. Related: [[finding_number_carries_threshold_unit_source]], [[finding_ohlc_verify_before_session_claims]].
