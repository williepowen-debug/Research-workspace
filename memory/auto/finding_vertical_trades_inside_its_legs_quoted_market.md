---
name: finding_vertical_trades_inside_its_legs_quoted_market
description: A vertical spread fills inside the sum of its legs' quoted markets, so pricing the order off leg mids is systematically too generous — open in the aggressive third of the net bracket.
metadata:
  type: feedback
---

**On a spread where both legs are liquid, open the order in the AGGRESSIVE THIRD of the net bracket, not at the net mid. Mid is the floor of your opening ask, not the start.**

**Why:** the legs offset for the market maker, so a vertical trades **inside** the sum of its legs' quoted markets. Quoting the order off leg mids imports both legs' full quoted width into your limit and hands the spread away.

**Measured, n=2, same position, both directions — Will's limit beat TERRY's both times and both filled:**

| | TERRY proposed | Will worked | Result |
|---|---|---|---|
| Entry 7/27/26 | $0.75 limit | **$0.70** | filled at mark, never walked up |
| Exit 7/30/26 | start $0.40 (net mid), floor $0.31 | **$0.45** | filled — **+$20 on 4 lots** |

At the exit the quoted **leg** spreads were ~25% (20C 0.53/0.68, 25C 0.17/0.22) giving a net bracket of 0.31–0.51 around a 0.40 mid. TERRY opened at the mid reasoning *"don't get cute for 2 cents when the underlying is falling 11%/day."* **That was wrong** — urgency is an argument for walking the limit *fast*, not for opening it low. The fill came 5¢ above the recommended start and moved realized P/L from an estimated −47% to **−38.8%**.

**How to apply:**
- Both legs OI >5,000 → **open in the aggressive third of the net bracket**, then walk toward mid/bid on a timer.
- Keep the walk-down **fast** when the underlying is moving against you (2¢ every ~4 min) — speed is the correct response to urgency, not a worse starting limit.
- Never price a multi-leg order by naively differencing the legs' mids; bracket it (long-bid − short-ask ⟶ long-ask − short-bid) and start high in that bracket.
- ⚠️ **Corollary on estimates:** a P/L estimate built off leg mids is biased pessimistic for a seller. State the bracket, not a point.
- Related: [[finding_option_marks_need_live_chain]], [[finding_fill_in_principle_vs_final_approve_pattern]].
