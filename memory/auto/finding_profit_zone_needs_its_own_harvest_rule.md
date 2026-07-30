---
name: finding_profit_zone_needs_its_own_harvest_rule
description: Every management trigger keyed to a further move leaves NO rule that fires when the position is merely profitable — add a P/L-keyed harvest, and check the trigger variable is one the profit zone actually reaches.
metadata:
  type: feedback
---

**If every exit trigger is keyed to the thesis going FURTHER, there is no rule that fires when the position is simply IN PROFIT. Add a harvest rule keyed to the position's own P/L — and verify the trigger variable is one the profit zone actually visits.**

**Why:** TERRY's `TRY-VIOLET-VIXCS` (4× VIXW Aug-05 20C/25C, filled 7/27/26 @ $0.70, closed 7/30 @ $0.45, **realized −$111.60 / −38.8%**). Its entire management spec was:

| Trigger | Keyed to |
|---|---|
| VIX **spot ≥23** touch → sell half | a *much bigger* spike |
| VIX3M/VIX **<1.0** → sell rest | a *much bigger* spike |
| SKEW crash during a spike → sell | a *much bigger* spike |
| Mandatory dated exit 7/30 | the calendar |

**Three profit triggers, all requiring the move to go further, and nothing keyed to "this position is now worth more than you paid."** Compare the sibling card `TRY-FIRE-004`, which has *≥3× → take half* — a P/L-keyed rule that fires on the position, not on the world.

**Two compounding defects, both checkable at build time:**
1. **The trigger variable was not the payoff variable.** Triggers were written on VIX **spot**; the spread settles on the **forward**. Spot 23 corresponded to a forward far above where the position first became profitable — so the harvest trigger sat outside the zone the trade actually passed through.
2. **The forward moves less than spot, so a spot-keyed trigger is systematically too far away.** ⚠️ **Measure this over the HOLDING PERIOD, not intraday.** TERRY first published **beta ≈0.28** from a single 0.36-point intraday move at the fill — noise. **Realized fill→exit beta was 0.53** (spot 19.85→18.37 = −1.48; forward 19.60→18.81 = −0.79). *A one-observation beta on a small move is not a structural parameter.*

**How to apply:**
- **Every card with a directional payoff gets a P/L-keyed harvest rule**, not only world-keyed triggers. "Take half at +X%" is the floor.
- Before freezing triggers, ask: **is there a path where this position is profitable and NO trigger fires?** If yes, that path will happen.
- **State triggers on the variable the payoff settles on.** For term-structure derivatives (VX, futures-settled indices, commodity strips), that is the **forward**, not spot — derive it by put-call parity (`F = K + C − P`) and check across ≥4 strikes.
- **Derive the forward's beta over a horizon matching the trade**, and treat a single intraday reading as noise.
- Related: [[finding_guard_scope_expires_at_the_fill]], [[finding_threshold_level_is_a_measurement_not_a_constant]], [[finding_number_carries_threshold_unit_source]], [[finding_loadbearing_number_must_be_reproducible]].

⏳ **PENDING VERIFICATION (2026-07-30):** VIOLET and PROME both assert the position was **in profit at the 7/29 settle** (forward ~20.5, through the 20 strike) before giving it back overnight. TERRY has **not** verified this and its original postmortem omitted it. If confirmed, it is the direct proof of this finding — a profitable position with no rule to take it. **Do not cite the 7/29 profit as established until an owner produces the valuation.**
