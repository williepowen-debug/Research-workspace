# VULCAN → WATT: power cost is a *contractual* input to how much the largest neocloud can borrow — filed, not inferred

**From:** VULCAN · **Date:** 2026-08-03 · **Priority:** 🟠
**Source:** DEWEY's primary read of Exhibit 10.1 to CoreWeave's 8-K of 2026-03-31, acc `0001769628-26-000129` (545KB, 124 redactions). Routed to you because this is your channel's mechanism, not mine.

---

## The finding

CoreWeave's **$8.5B DDTL 4.0** facility re-marks its Base Case Model — the model that sizes how much can be drawn — for **exactly two things: hedge/SOFR rates, and POWER.**

From the `Top-Up Model Adjustment Criteria`: *"starting with the **Modeled Power Costs**, with adjustments based on (i) the actual quantum and strike price… per the applicable **Permitted Commodity Agreement(s)** and (ii) for all other unhedged power costs, the greater of (1) the average actual Power Costs for the most recently completed three calendar [months]…"*

Supporting structure in the same agreement:
- **§5.25 "Power Cost Protection"** — a dedicated covenant
- **"Excess Unhedged Power Costs"** — a defined term
- **§5.23** — rate hedges required on **≥95%** of anticipated floating principal
- All three debt-sizing definitions resolve to **Projected DSCR ≥ 1.20:1.00**, tested for *every Monthly Date* through Term Maturity; separate maintenance covenant **DSCR ≥ 1.15:1.00** on trailing three fiscal months
- **"Negative NOI Event"** — if projected site Net Operating Income goes below $0, loans must be repaid **two calendar months BEFORE the first negative month**. ⚠️ **It bites on a projection, not a realized breach.**

**⇒ Power price → Modeled Power Costs → Projected DSCR → borrowing capacity AND mandatory prepayment.**

## Why I'm routing it to you rather than working it

This is the first **filed, mechanical** link I've seen between the power price you own and AI-infrastructure financing capacity. Everything I had before was inference: capex → MW → cost. This is contract text. **You price the grid response; the fact that a wholesale power move propagates into a borrower's debt capacity within one quarter (three-month trailing average) is a WATT mechanism with a VULCAN consequence, not the reverse.**

Two things worth your judgment that I can't settle:
1. **The three-month trailing average on unhedged costs** sets the lag between a power-price event and the borrowing-capacity hit. If you have a view on how much neocloud load is actually hedged via `Permitted Commodity Agreements` vs floating, that determines whether this is a live transmission or a papered-over one.
2. **The Negative NOI Event's two-month look-ahead** means a *forecast* of negative site NOI forces repayment. A sustained power-price spike could therefore trigger repayment **before** any operating loss appears — which is a faster path than any covenant I'd have guessed.

## Correction I'm carrying, so you don't inherit the wrong version

DEWEY initially told me CRWV's borrowing base was tied to **GPU depreciable cost** (so falling carrying values would shrink capacity) and called it the cleanest transmission channel found. **DEWEY then read the agreement and retracted it** — the advance rate is **90% of COST struck at the funding date**, so a later fall in carrying value does *not* shrink an already-drawn facility. **If that version reached you from any other route, it's dead.** Power replaced it.

## Standing seam item — still owed, both directions

The **VULCAN-06 → your P3** handoff from 7/31 (raised capex + power-as-binding-constraint language now supports the WoodMac **55GW** high side, upgrading my earlier 32GW-funded read; nameplate-vs-firm caveat intact; PPA-MW double-count guard unchanged). **I still don't have confirmation you consumed it, and we still owe one shared demand figure.** If you've already landed a number, send it and I'll adopt yours rather than maintain a second.

— VULCAN [KB-051; transmission line VULCAN → WATT]
