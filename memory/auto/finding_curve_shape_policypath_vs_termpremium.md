---
name: finding_curve_shape_policypath_vs_termpremium
description: Split a nominal long-yield MOVE into policy-path vs term-premium by CURVE SHAPE — belly-led bear-flattener = policy-path, long-end-led bear-steepener = term-premium. "Real yield" is NOT "term premium."
metadata:
  type: reference
---

When a nominal long yield (10Y) rises and you need to label the *driver*, first split nominal into real vs breakeven (ΔDFII10 vs ΔT10YIE) — but do NOT stop there. **"Real" ≠ "term premium."** A real-yield move splits again into (a) expected real *policy path* and (b) real *term premium*, and the discriminator is **curve shape**, not the real/BE split:

- **Belly-led bear-FLATTENER** (5Y ≳ 10Y > 30Y; 10Y−2Y ~flat; 30Y−10Y compresses — the long end LAGS) → **policy-path repricing** (higher-for-longer, hawkish-hold). The 2Y co-moving (rising through even a cool inflation print) is the confirming witness; a front end sitting *above* the funds rate prices no cuts.
- **Long-end-led bear-STEEPENER** (30Y > 10Y > 5Y; long end LEADS) → **term-premium expansion** (supply/duration-risk compensation).

**LEVEL ≠ MOVE.** A term-premium *level* can be structurally elevated (e.g. ACM 10Y TP positive) — that explains why a yield sits high and won't rally — while the recent *move* is driven by policy path. Don't stamp a true level fact onto the delta: "term premium is elevated" (level) does not license "the move was a term-premium channel" (driver). Decompose the delta on its own curve shape.

**Why it matters:** the label picks the falsifier. A policy-path move falsifies on a dovish Fed repricing (front-end/belly real rates fall) — testable at the FOMC and robust to oil/inflation surprises. A term-premium move falsifies on supply relief / demand return (auctions, QT, foreign buyers). Mislabeling routes you to watch the wrong catalyst.

**Provenance:** BOND, 2026-07-18 — the 10Y's +14bp arm-completing move (7/6→7/13) was mislabeled "term-premium channel" in fleet canon; the belly-led bear-flattener (5Y +16 > 10Y +14 > 30Y +11, 30Y lagged) proved it was ~80-90% real policy path, ~0-7% term premium. Relabeled to "real-rate / higher-for-longer (policy-path-led) channel"; Will-approved into HEARTBEAT amendment #1. Related: [[finding_threshold_vs_mechanism]], [[finding_catalyst_vs_consequence_conflation]], [[finding_decouple_idiosyncratic_from_systemic_leg]], [[finding_composition_mask_unmask_discriminator]].
