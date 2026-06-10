---
name: finding_catalyst_path_decoupling
description: "Level trigger ≠ path trigger — a pre-registered conjunction anchored on an assumed catalyst path can be hit via a different upstream path; that invalidates the path-dependency, not the level read. SAM-23, 2 windows Jun 2026"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 832e5586-d2db-4af7-95b3-28041b997fb1
---

When a framework anchors mark-up/mark-down conjunction triggers on an assumed catalyst path (SAM-23: MOU break → oil rally → yen-weak → USDJPY upside → MOF intervention), a different upstream path hitting the same downstream level invalidates the path-dependency **without invalidating the level read itself**. Distinguish explicitly: a **level trigger** fires if the level is met by any path; a **path trigger** fires only if the upstream sequence holds intact. Specify which kind each pre-registered trigger is at write time.

**Why:** Two empirical decouplings in one week (SAM, Jun 2026): (1) Fri Jun 5 — USDJPY tagged 160.20 (the MOF #3 hard trigger) via a US-side NFP shock (+172K vs 85K, DXY +0.66%), not via the yen-side MOU/oil path the framework assumed; cross-pairs showed the yen STRENGTHENING vs everything except USD. (2) Tue Jun 9 — Brent broke its pre-registered line (China demand + walk-back rumors) WHILE USDJPY held above 160 — the oil-leg and USDJPY-leg moved opposite to the assumed chain. In both windows the pre-registered conjunctions correctly gated against false re-rates, but the framework's path assumption was empirically dead: intervention probability is HIGH at USDJPY 160+ regardless of upstream driver (level-driven), so the SAM-23 mark held via the level read even as the path decoupled.

**How to apply:** At trigger write time, label each pre-registered trigger level-driven or path-driven. When a level fires via an unassumed path: hold the mark per the level read, log the path-decoupling, and re-anchor the framework (CHANGELOG) rather than mechanically applying conjunctions whose legs encode a dead path. Transferable to any agent anchoring probability marks on assumed catalyst chains — LIQUID (UST flows), HENRY (carry unwind), BROCK (auction stress).

**Sibling:** [[finding_threshold_vs_mechanism]] — division of labor: that finding grades *predictions* (threshold fired on the wrong mechanism → TRUE-in-letter/FALSE-in-spirit); this one specs *triggers* (level met via the wrong path → re-anchor the trigger, keep the level read). Related: [[finding_thin_liquidity_prediction_market_discipline]].
