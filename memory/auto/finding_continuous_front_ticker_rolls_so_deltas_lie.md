---
name: finding_continuous_front_ticker_rolls_so_deltas_lie
description: Continuous front-month tickers (=F, cont. contracts) silently switch contracts; a LEVEL survives the roll, a DELTA or SPREAD across it is fabricated.
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

**Generalization:** any auto-advancing pointer — front-month futures, "latest vintage", rolling N-day windows, `LIMIT 1` on a re-keyed series — has this shape. **The identity of what you are measuring changed while the name stayed the same.** Sibling of [[finding_derived_metric_across_vintages_biases_toward_stale_leg]] and [[finding_cross_entity_comparison_needs_same_perimeter]]; the twin where the *label* rather than the *perimeter* moves is [[finding_bypass_turns_a_flow_proxy_into_a_routing_metric]]. Related: [[finding_number_carries_threshold_unit_source]], [[finding_ohlc_verify_before_session_claims]].
