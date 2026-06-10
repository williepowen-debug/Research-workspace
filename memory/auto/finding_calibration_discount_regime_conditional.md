---
name: calibration-discount-regime-conditional
description: An earned calibration discount is conditional on the pricing regime it was earned in — re-derive before applying at a different market-confidence level
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 031cf8c3-f337-4300-9669-e8552f4feefd
---

An "earned discount" (marking below market because you were burned being above it) is regime-conditional evidence. SAM's 23pp Takaichi-ceiling discount was earned by sitting ABOVE a 55-75%-priced market that proved right (SAM-08 @90%, SAM-20 @60%, Apr 2026). Applying it with the market at 98% changes the evidence object: the episodes proved *self*-miscalibration relative to market; the transferred use asserts *market*-miscalibration — something the episodes never tested. A disclaimer like "calibration, not disagreement" doesn't survive operational use: the discounted probability still drives event-EV, scenario weights, and downstream consumers' inputs.

**Why:** Caught by RED 2026-06-10 (CHG-RED-029, pre-BOJ stress-test of SAM). SAM's 75% vs Polymarket 98% implied a 25% hold-branch with no precedent class (no BOJ defiance of >90% pricing this cycle), flowing into event EV (sign-flipping), disposition priors, and LIQUID/HENRY carry-unwind buckets.

**How to apply:** When any agent carries an earned discount/premium vs market pricing, check the market-confidence level at which the lesson was earned vs the level where it's being applied. If they differ materially, re-derive the discount SIZE from scratch — don't transfer it. Related: [[finding_thin_liquidity_prediction_market_discipline]], [[finding_threshold_vs_mechanism]].
