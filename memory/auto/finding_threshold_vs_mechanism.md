---
name: threshold-vs-mechanism
description: "Falsifiable predictions must separate \"mechanism intact\" propositions from \"threshold sticks/breaches\" propositions; threshold-only predictions can resolve TRUE-in-letter / FALSE-in-spirit when cross-currents or alternate mechanisms drive the same numeric outcome"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: daa31902-e370-4371-ae3b-ae1989ba7228
---

When writing falsifiable predictions about levels, ratios, or thresholds, split the proposition explicitly into two layers: (a) the underlying **mechanism** the prediction is meant to flag (e.g., "forced insurer rebalancing", "lifer long-end abandonment driving JGB 30Y blowout"), and (b) the **observable threshold** (e.g., "ESR <200%", "JGB 30Y holds ≥4.0%"). Resolve against both. A threshold can fire on a different mechanism than the one the prediction was designed to flag, producing a literally-correct-but-substantively-wrong "TRUE." Same problem inverted: a threshold can retrace while the mechanism stays intact, producing a literally-wrong-but-substantively-correct "FALSE."

**Why:** Three independent instances across SAM and BRENT mid-2026 fired the same trap:
- *SAM-26 (level-hold trap):* Predicted JGB 30Y holds ≥4.0% through BOJ event. Broke 4.0% May 15 on J-ICS lifer long-end abandonment (correct mechanism), then retraced to 3.931% within one week on oil collapse + dovish CPI even though insurers did NOT return as buyers. Prediction tracking FALSE on the threshold; mechanism intact.
- *SAM-25 (level-breach trap):* Predicted any Big 3 mutual ESR <200% (designed to flag forced-selling pressure). Nippon printed 195% May 26 — but driven by Resolution Life M&A subsidiarization (-28pt) capital deployment, not market stress. Foreign book in unrealized GAIN. Market priced as capital action (yen WEAKER post-print). Prediction TRUE-in-letter, FALSE-in-spirit.
- *BRT-23 (level-breach trap, cross-agent confirmation):* Predicted at least one DRC SX-EW copper/cobalt operator declares force majeure within 60 days of Hormuz closure (designed to flag sulphur-cost feedstock squeeze). Glencore DID declare FM on cobalt May 2026 — but driven by DRC Feb cobalt EXPORT BAN / 96,600t annual quotas, NOT Hormuz sulphur cost. Cobalt prices UP ~160% on POLICY-driven scarcity (opposite of cost-squeeze the prediction modeled). Prediction TRUE-in-letter, FALSE-in-spirit. Resolved FAILED 2026-05-31 (BRENT). First non-SAM instance — confirms the pattern crosses domains (Japan insurance → oil/commodity industrials).

All three failures shared a root: threshold-only language couldn't discriminate the intended mechanism from coincidental ones.

**How to apply:** When drafting a new falsifiable prediction, ask: "What would make this resolve TRUE for the wrong reason?" and "What would make this resolve FALSE while the underlying thesis stays right?" If either is plausible, rewrite as two sub-predictions: a *mechanism* prediction ("J-ICS-driven lifer abandonment of 30Y continues — measured by Y") and a *threshold* prediction ("level X breached/held through event Z absent oil/Fed/intervention shocks"). For capital-ratio predictions specifically (ESR, ICS, SCR), always prefix with "*due to market losses / forced rebalance*" or split into "stress-driven sub-200%" vs "capital-action sub-200%" — the intent of these predictions is forced-selling flags, not generic ratio movement. Transferable to any agent writing predictions about yield levels, FX levels, contract counts, capital ratios, or other numeric thresholds.

**Sibling:** [[finding_catalyst_path_decoupling]] — division of labor: this finding grades *predictions* (threshold vs mechanism at resolution); that one specs *triggers* (level-driven vs path-driven at write time — a level met via an unassumed path invalidates the path, not the level read).
