---
name: finding_near_dated_vol_spread_misses_the_spot_spike
description: A near-dated VIX spread settles on the FORWARD (beta ~0.28 to spot), so the spot spike you bought can arrive in full and the structure still loses.
metadata:
  type: feedback
---

**Set strikes against the DERIVED FORWARD, not spot — and if the derivation says the forward barely moves, that must change the structure, not just the payoff estimate.**

**Why:** TERRY's `TRY-VIOLET-VIXCS` (4× VIXW Aug-05 20C/25C, filled 7/27/26 @ $0.70) was built to catch a pre-FOMC vol spike. **The spike arrived in full** — VIX 17.45 → 20.88 intraday, **+13.45%** on the 7/29 settle, first >20 settle of the episode, VVIX to a new episode high. **The trade still lost 38.8% (−$111.60).**

VIX options settle on the **forward**, and at ~9 DTE that forward carried **beta ≈0.28 to spot** (derived by put-call parity: at entry spot ran 19.49→19.85 while the 8/5 forward moved only 19.5→19.6). A +13.45% spot move barely lifted the number that actually prices the option. Between fill and exit the forward went **19.6 → 18.82**, so moneyness **deteriorated from +2.0% to +6.3% OTM *after* the event we bought had already happened.**

**The aggravating detail — this is the real lesson.** TERRY *derived the forward at entry, wrote the diagnosis on the card* (*"the low beta undercuts my own spike-capture argument for the near-dated expiry"*), **downgraded the payoff estimate for it — and left the strikes and expiry unchanged.** Identifying a structural flaw and then not letting it change the structure is worse than never finding it: it produces a documented, confident, wrong trade.

**How to apply:**
- If the thesis is a **SPOT** move, either buy enough tenor that forward beta is near 1, or set strikes against the **derived forward**. Deriving it is not enough — the derivation must be allowed to change strikes, expiry, or the decision to trade at all.
- **Check that TRIGGERS and PAYOFF live on the same variable.** This card's §6 management triggers were written on **spot** (`VIX ≥23`) while the payoff lived on the **forward**. The same mismatch was flagged 7/27 as an *entry*-guard defect ([[finding_guard_scope_expires_at_the_fill]]) — it was never only an entry-guard issue.
- Generalizes beyond VIX to any derivative on a term structure (VX, futures-settled indices, commodity strips): **spot is not the underlying, the forward is.**
- Related: [[finding_option_marks_need_live_chain]], [[finding_threshold_level_is_a_measurement_not_a_constant]], [[finding_number_carries_threshold_unit_source]].
