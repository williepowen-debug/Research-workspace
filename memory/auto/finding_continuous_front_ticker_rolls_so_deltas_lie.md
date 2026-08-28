---
name: finding_continuous_front_ticker_rolls_so_deltas_lie
description: Continuous front-month tickers (=F) silently switch contracts — a LEVEL survives the roll, a DELTA or SPREAD across it is fabricated, and a COEFFICIENT fitted on it is attenuated toward zero in the direction that flatters the thesis.
symptoms: "same ticker returns two different closes for one date"; "fast_info previousClose disagrees with the daily bar"; "vendor history and live quote are on different contracts"; "daily volume collapsed to a few hundred lots on a liquid future"; "flat O=H=L=C bar with the same volume as yesterday"; "headline % move is an artifact of the roll"; "my WoW/crack/spread printed a move the market did not make"
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

---

**⚠️ THE THIRD FACET — a continuous ticker's HISTORY and its LIVE bar can be on DIFFERENT contracts AT THE SAME TIME, and the cheapest detector is the VOLUME column, not the price.** The "detect the roll by matching the continuous close against each candidate contract" rule above assumes the alias means **one** contract per date across the whole series. It can mean two at once.

**Measured 2026-08-28 (MIDAS), on the instrument a frozen prediction was about to grade against.** `GC=F` returned **three** different values for **one date, 2026-08-27**:

| asked for | 8/27 value | volume | what it actually was |
|---|---|---|---|
| `GC=F` daily-history bar | **$4,609.70** | **1,051** | the **expiring** contract, `O=H=L=C` flat |
| `GCZ26.CMX` daily-history bar | **$4,664.00** | **151,459** | the real front month |
| `GC=F` `fast_info.previousClose` | **$4,631.40** | — | a **third** basis, unidentified |

**Spread $54.30 = 1.18% on a single date, nothing erroring.** `GC=F`'s 8/28 bar then returned **identical OHLC *and volume*** to `GCZ26.CMX`'s own 8/28 bar ⇒ its **history was stitched to the dying contract while its current bar was the new front month**, putting a **~$55 contract gap inside the series at the exact session boundary being graded across.**

**The volume column answered it with no contract codes at all:** `GC=F`'s 8/19–8/27 bars carried **311–1,336** lots against `GCZ26`'s **151,459–250,482**. *A ~1,000-lot day on the world's most liquid gold future is not the front month.*

**Rules for this facet:**
- **Pull VOLUME beside price on any continuous ticker and sanity-check it against the instrument's known liquidity.** Cheapest contract-identity test there is — needs no contract codes and no roll calendar, so it works on **first contact with an unfamiliar ticker**, which is exactly when facet-2's matching method is unavailable.
- **Check the live quote and the daily history separately.** They can disagree; `fast_info.previousClose` can be a third answer again. Never assume one pull characterises the series.
- **A flat `O=H=L=C` bar carrying a duplicated volume figure is a dying-contract tell, not a quiet session.** ⚠️ **Prompt to look, never a verdict** — in this same pull *both* tickers reported identical volume for 8/26 and 8/27, so duplicated volume can also mean a partly carried bar on a healthy contract.

**⚠️ n=2 IN ONE DAY, ACROSS TWO COMMODITIES AND TWO DESKS — this is a vendor-wide property, not one desk's quirk.** The same morning, WALTER found `BZ=F` had rolled Oct→Nov between sessions, making a headline **−1.98%** Brent move a **~1.2pp roll artifact** against a like-for-like **−0.75%** — *and* found its own published 8/26 "close" was a **live tick from the next session** (a slide published as −8.5% that was really −6.94%). **Gold and Brent, metals desk and routing desk, inside 24 hours.** The two failure modes travel together because both are triggered by the same thing: **pulling a futures series near a session boundary or a roll and trusting the label.**

**The pairing rule:** whenever you catch a roll artifact, also check whether the bar you are holding is a **settled close or a live tick** — and vice versa. They co-occur, they compound (a live tick *from the next contract*), and each one alone reads as a plausible market move.
