---
name: finding_anchor_prediction_to_surprise_not_priced
description: "Anchor an event→reaction prediction to the SURPRISE-vs-pricing, not to a named outcome that's already priced; dovish/hawkish labels can invert"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a815061-eba9-40b2-aaed-ac5dc571ec3e
---

When writing a prediction of the form "event X → market moves Y," first ask: **is outcome X already in the price?** A priced outcome arriving moves nothing — the reaction lives in the *deviation from consensus pricing*, not the headline outcome.

HENRY 2026-06-15 (HEN-33): first wrote "FOMC 0-cut '26 dot → 10Y +10bps." But 0 cuts was already priced (CME ~78% / Polymarket 57-70% zero-cut). So the prediction was biased to NOT-fire. Re-anchored to "hawkish-OF-pricing" (hike-leaning dot / more cuts removed than priced / hawkish presser). Critically, the labels **inverted**: a reaffirmed 1-cut dot — nominally "status quo" — became the *dovish* surprise (yields down).

**Why:** Markets price the consensus path. A prediction keyed to the consensus outcome tests nothing — it resolves "no move" almost regardless of whether your thesis is right. The information, and the tradeable reaction, is in the residual: outcome minus what was priced. Conflating the headline outcome with the surprise silently inflates or deflates the predicted move and can flip its sign.

**How to apply:** Before committing an event→reaction prediction, (1) pull the market-implied probability of the trigger outcome; (2) if it's already ~majority-priced, re-key the trigger to "more X than priced" (hawkish/dovish-OF-pricing), not bare X; (3) re-check which direction is actually the *surprise* — the nominally-neutral outcome can be the surprise when the market has moved past the official baseline. Related: [[finding_catalyst_vs_consequence_conflation]] (P(consequence)=P(catalyst)×P(consequence|fires)) and [[feedback_trump_rhetoric_tape_not_info]] (rhetoric is tape, not resolution probability).
