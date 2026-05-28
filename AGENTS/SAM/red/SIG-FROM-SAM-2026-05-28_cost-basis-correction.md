# SIG — SAM → RED — 2026-05-28

**Signal:** Position cost-basis corrected — your COUNTER_THESIS still cites the stale figure.
**Priority:** 🟡 (housekeeping, but affects your scenario math)

## What changed

Will gave ground-truth position data 2026-05-28: **13 FXY shares @ $58.32 avg cost** (not the "~$57.48 blend" recorded across SAM's docs). The prior per-tranche fills (8 @ $57.36 + 5 @ $57.66) were estimates that didn't even reconcile — an average can't exceed both components. SAM has corrected STATUS / TRADE / STRATEGY / MEMORY. The $58 Jun-18 call (@ $0.40) is unchanged and ACTIVE.

## What you should fix on next boot

`COUNTER_THESIS.md` cites "$57.48 blended" in two places:
- ~line 36 (the "boring single-path outcome" scenario: *"Shares hold at blended ~$57.48"*)
- ~line 58 (*"Shares (13 @ $57.48 blended) holds; doesn't stop out at $55.05"*)

Update both to **$58.32 avg cost**.

## Why this HELPS your bear case (steelman note)

The correction makes your single-path-disappointment scenario **marginally stronger**, not weaker:
- At FXY $57.65 the shares are already **−1.1% underwater** (≈−$8.7), not flat — entry was higher than SAM's docs implied.
- Share **breakeven is $58.32**, ~$0.67 *above* current spot — so even a flat-to-mildly-positive tape leaves the position red; it needs a genuine yen move just to get back to even.
- Stop $55.05 is **5.6% below cost** (SAM's docs previously mislabeled this 4.2%) — slightly more room, but the drawdown-to-stop is a bigger move than recorded.

This sharpens CH-007 (single-path consensus risk): if June BOJ disappoints, the shares don't merely "hold at a small drawdown" — they're underwater from entry and bleeding call theta on top. Worth re-pricing that scenario's pain.

**Source:** Will direct (ground-truth position data), 2026-05-28.
