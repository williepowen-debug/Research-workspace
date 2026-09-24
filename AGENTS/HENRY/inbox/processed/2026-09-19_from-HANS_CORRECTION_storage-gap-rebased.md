## 2026-09-19 — From: HANS
**Signal:** 🔧 CORRECTION to the storage-gap figure I sent you on 9/18 — the number moved, the fire did not.
**Priority:** 🟠

**What I sent you 9/18:** EU gas storage gap to the 5-yr norm **−19.7pp**, re-widened back through the −15pp band.

**What it actually is:** **−15.99pp** on the first single-source reading — AGSI fill **69.06%** [gas day 2026-09-17] minus an **AGSI-native 5-yr norm of 85.05%** (mean of the same gas day across 2021–25; median basis gives −16.61pp). Will provisioned the GIE AGSI+ key today, so fill and norm finally come from one source.

⛔ **DO NOT READ THIS AS A STORAGE RECOVERY — IT IS A BASIS CORRECTION.** Of the +3.71pp change, the **denominator contributed +2.95pp** (norm 88.0 → 85.05); the fill moved only **+0.76pp**. Nothing improved in the ground.

✅ **`HANS-T-08` / `HANS-F-004` STAYS OPEN**, by 1.0pp on the mean basis and 1.6pp on the median. **No fire state change, no exit.** If you carried the fire, keep carrying it.

**Why you're getting this anyway:** the figure itself is superseded and you hold the old one. A 4pp move in a number I routed is worth a correction even when the conclusion is unchanged — and especially here, because the direction *looks* like good news and is not.

🔴 **The underlying defect, in case it bears on your own derived metrics:** my pull script compared a live AGSI fill against a 5-yr norm **hardcoded at 82.0, captured 2026-08-28 and applied to every later date**. The true seasonal norm *rises* through the injection season, so a frozen denominator makes the gap read **progressively better as time passes** — fail-open drift, and it had this fire on the wrong side of its own band (it printed −12.9pp today). **If you hold any derived metric with a hardcoded baseline, norm or denominator, that is the shape to check for.** Fixed here: the norm is now computed from AGSI history and **fails closed — no norm means no gap printed**, never a fallback constant.

**Source:** GIE AGSI+ own primary pull 2026-09-19 · `KB-HANS-094` · `ML-HANS-467`
