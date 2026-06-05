---
name: put-vs-duration-expression
description: "When tape is regime-suppressed (low VIX, tight spreads, gamma damping), single-name equity puts bleed even when thesis validates substance-side. Duration expressions of the same view (e.g., TLT puts when long-rate channel is open) compound instead. Match the vehicle to the open transmission channel."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6a9a8e5c-357a-496c-9533-e39f59f4376c
---

**The rule:** When a thesis spans multiple transmission channels (substance, spreads, vol, duration), check which channels are *currently open* before picking the trade vehicle. Equity puts on the names you're bearish on are NOT always the right expression — they're often the *worst* expression when tape is regime-suppressed.

**Why:** Tape suppression mechanisms (gamma damping, vol floor, momentum-driven equity rallies, spread compression via institutional carry demand) can hold a name's equity price aloft for quarters even as fundamentals deteriorate visibly. Put buying punishes you brutally for being early because theta + vol-crush + delta-against compound when tape doesn't confirm.

**How to apply:** Before sizing into single-name equity puts on a credit-cycle thesis, ask:
1. **Which transmission channel is currently OPEN?** (HY OAS widening? CCC bifurcation? Duration / 10Y rising? Bank-equity stress?)
2. **Express via the open channel, not the dream channel.** If duration is widening (10Y +bps, TLT down), TLT puts capture the same broad credit-stress thesis with positive carry as long as the channel stays open.
3. **Only use equity puts when their channel is open.** Single-name equity puts require either: (a) the name's equity already breaking down, (b) a binary near-dated catalyst, or (c) extremely long-dated expiries with strike-near-spot to ride out the regime suppression.

**Validated 2026-05-21 BROCK session:** -84% loss on $3,200 BROCK-domain put book (APO/ARES/OWL/HYG, all spot-equity puts) while TLT puts (LIQUID-side duration expression of the same broad credit-stress thesis) +$600 cumulative. Substance side validated (FSK Q1 Max Bear data, NDFI 11× bigger, Ch11 +42%, regulator escalation) — tape side never confirmed because HY OAS never broke 260 and gamma suppression held. Equity-put vehicle was wrong; duration vehicle was right.

**Edge case — long-dated:** APO Dec $95P (210 days, 28% OTM) held a position because the long expiry gives time for the tape channel to open. The Jun residuals (28 days, 25% OTM) are where the asymmetry collapsed completely.

Related: [[feedback_evidence_standalone]], [[feedback_exit_recommendations_need_mark_context]], [[finding_framing_precision_overlay]].
