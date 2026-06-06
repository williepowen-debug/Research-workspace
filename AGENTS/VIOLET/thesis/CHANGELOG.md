# VIX_THESIS Changelog

Old view → new view at each version bump. Major (X) = structural change / phase transition / conviction reversal. Minor (Y) = refinement.

Trigger to log here: any closeout that updates `thesis/VIX_THESIS.md`.

---

## v3.4 — 2026-06-06 (Regime Shift Trade refinement — Path A tagging + DIET disambiguation)

- **Bumped from:** v3.3 (2026-06-06 same-day — 6/5 NFP-shock live test integration; L1-L4 stack discipline; Path A / Path B transmission split; DIET Coiled-Spring Trade added as 3rd pattern).
- **What changed:** Regime Shift Trade entry (lines 275-296 of VIX_THESIS.md) refined to align with v3.3's Path A / Path B framing. (1) Tagged as **Path A specialization** — credit-confirmation required, not a generic regime-shift entry. (2) Added explicit **"vs. DIET Coiled-Spring Trade"** disambiguation note: DIET is the single-signal divergence trade (mechanism-agnostic); Regime Shift Trade is the compound Path A setup (persistent calm + emerging credit + divergence). (3) Added **rare-trigger caveat** — VVIX>120 historically uncommon and especially scarce in the current GEX-suppression era. (4) **Style cleanup:** removed inline strikethrough residue of term-structure-flattening falsification (record lives in Predictions #2); dropped `not KB-VIO-023` negative cross-reference noise.
- **Why:** v3.3 introduced Path A / Path B without retroactively tagging the pre-existing trade entries. Reader scanning the Regime Shift Trade after the v3.3 read couldn't tell which path it belonged to or how it related to the new DIET trade. Tier-3 flag from the v3.3 tightening pass surfaced this; Will-approved revision.
- **Old view:** Regime Shift Trade as a standalone three-condition entry (long calm + credit emergence + VVIX>120 divergence), implicitly Path A but unmarked, with no explicit relationship to the new DIET trade.
- **New view:** Regime Shift Trade explicitly tagged Path A specialization. DIET Coiled-Spring Trade is the single-signal companion; both can be in the watchlist simultaneously but they're not interchangeable. Rare-trigger nature explicitly noted so the watchlist isn't sized as if it fires monthly.
- **Predictions touched:** None (Prediction #3 was already closed INCONCLUSIVE in v3.3; this revision clarifies that the Regime Shift Trade entry condition is structurally different from Prediction #3's standalone threshold).
- **No substantive change** to trade setup, entry, target, stop, or sizing — refinement and documentation only.

---

## v3.3 — 2026-06-06 (6/5 NFP-shock live test integration)

- **Bumped from:** v3.2 (2026-06-01 — DIET coiled-spring + GEX-suppression working hypothesis as live analytical product; R11 dead; imminence read materially weaker than 5/13 / 5/21).
- **What changed:** Three structural integrations from the 6/5 NFP-shock live test: (1) **L1-L4 operational stack discipline** — L1 population framework (KB-VIO-067 DIET backtest) PROMOTED to real-money signal; L2 (KB-VIO-069 absorbed-trap) WRONG-MECHANISM (consensus-miss carve-out pending); L3 (KB-VIO-068 direction-matrix) Q3 PROVISIONAL N=1; L4 (KB-VIO-065 COT) DEMOTED from discriminator to descriptive. (2) **Concentration-unwind as parallel transmission path** (KB-VIO-070/071) — vol event can fire via HENRY-side AI/factor concentration unwind amplifying a non-credit trigger, bypassing the canonical BROCK→LIQUID→VIOLET credit-led chain. Hot-NFP-rate-shock historical universe DEFLATES VIX (16/20 fell/flat 2010-2026); today is OUTLIER because rate-shock alone insufficient — required amplifier. (3) **R12 interrupted-and-resumed regime structure** (KB-VIO-072) — terminated 5/12, vol event fired 6/05 td-18, regime resumed 6/05 same day at 20d-avg 140.16. Sequence doesn't map to KB-VIO-044 historical regime-life-cycle catalogue. New regime classification "elevated SKEW under live vol event" — distinct from "fragility bid in calm."
- **Why:** Clean live test of the 4-layer stack filed 6/1 evening produced a directional hit (VIX +40% on 6/5) AND falsified the regime-context / direction-matrix / compound-confirmation layers (L2-L4) that were tuned to discriminate a different mechanism. KB-VIO-067 L1 paid forward at td-4 of the 60d window exactly as the 19yr backtest base rate predicted. KB-VIO-031 60d window from 4/15 fire RESOLVED HIT at td-58 (Scenario B confirmed: VIX +39.7%). PRE_EVENT_FADE classification (KB-VIO-058) was the wrong framework, not the wrong direction — spike fired but at td-18 lag from regime termination, not R11's td-8 archetype. Trade-decision lens (don't take Episode-17 position) was still correct.
- **Old view:** Population framework, regime context, direction matrix, and compound confirmation as a co-equal 4-layer stack with the regime/direction/compound layers as the operational filters. DIET coiled-spring + GEX-suppression as ASSUMPTION-grade working hypothesis (KB-VIO-062). Standard credit-led transmission chain (BROCK→LIQUID→VIOLET) as the dominant path.
- **New view:** L1 population is the real-money signal; L2-L4 are calibration filters that bypass when the dominant mechanism shifts. Two transmission paths now formal: (A) standard credit-led (still the high-confidence path when conditions match), (B) concentration-unwind parallel (HENRY-side breadth/AI cascade can fire VIX without credit confirmation, with rate-shock or other macro trigger as the spark). DIET signature (KB-VIO-067) is now EMPIRICAL-grade with 19yr backtest (1.0% base rate, 94% hit rate ≥15% VIX rise within 60d).
- **Predictions touched:** #3 VVIX divergence form CLOSED INCONCLUSIVE (threshold 120 not hit on 6/5 but outcome happened via different mechanism — invalidates the threshold-conditional setup). #5 NEW: KB-VIO-067 DIET signature → ≥15% VIX rise in 60d, PARTIAL HIT (5/20-5/29 signature → +40% at td-4). #6 NEW: post-spike SKEW >150 sustained 4+ td → back-to-back vol event within 60d, LIVE (SKEW 152.25 on 6/5). KB-VIO-031 60d window from 4/15 = RESOLVED HIT.
- **Forward gates:** 6/12 May CPI (5td); 6/17 FOMC + SEP + VIX June quarterly expiration.

---

## v3.2 — 2026-06-01 (catch-up: filed retroactively 2026-06-06; the original entry was mislabeled v3.1 — corrected here)

- **Bumped from:** v3.1 (Apr 15 PHASE 2 cluster-analog framework with central-case Scenario B VIX 25-30 + tail VIX 50+ requiring external catalyst + CCC crack).
- **What changed:** Added **diet coiled-spring + GEX-suppression** working hypothesis (KB-VIO-062, ASSUMPTION) as live analytical product. Pattern: SKEW reprices tail while VIX/VVIX are mechanically pinned by record GEX, leaving formal KB-VIO-036 trigger under-firing relative to its 19yr-calibrated 94% hit rate.
- **Why:** Five-to-six consecutive catalyst absorption (FOMC dissents, BOJ dissents, CPI hot, PPI hot, NVDA, +42bps then -20bps rates round-trip) with VIX in a 15-19 band and SPX 5d realized 3.98% — pattern is no longer plausibly random; structural-mechanism explanation is required. R11 PRE_EVENT_FADE analog (the 5/13-5/21 working framework) confirmed DEAD on 6/01 — R12 regime ended 5/12 without VIX firing in the 8td post-termination window.
- **Old view:** R11 analog 36% prior with ~80% relayed-up confidence; PRE_EVENT_FADE → VIX spike 0-8td after regime end was the operative play; trade window 5/26-6/02.
- **New view:** GRADUAL_FADE or POST_EVENT_PERSIST realized. Stage-2 trap framing intact (substance worsens while surface eases) but **imminence read materially weaker** than 5/13 or 5/21. Next firm test: 6/12 May CPI + 6/17 FOMC + 6/17-18 SEP. The diet-coiled-spring hypothesis is the live analytical product but UNBACKTESTED at filing-time; do not size positions on it. *(v3.3 update: KB-VIO-067 backtest on 6/1 PM later upgraded this to EMPIRICAL.)*
- **Predictions touched:** R11 analog (DEAD). R12 termination (CONFIRMED 5/12, not 5/18-20). Episode-17 25C (EXPIRED WORTHLESS 5/19).
- **Forward gates:** 6/05-6/10 R12 regime re-establishment knife-edge; 6/12 May CPI; 6/17 FOMC + SEP. *(v3.3 update: 6/05 knife-edge RESOLVED RE-ESTABLISHED via KB-VIO-072.)*

---

*Created: 2026-06-01 (first changelog entry; backfilled current state. Pre-v3.2 history lives in `VIX_THESIS.md` in-body changelog + research/ + KB.tsv.)*
*v3.3 added: 2026-06-06 (Saturday org session — 6/5 NFP-shock live test integration; mislabel correction on the 6/01 entry from v3.1 → v3.2.)*
*v3.4 added: 2026-06-06 same-day (Regime Shift Trade refinement — Path A tagging + DIET disambiguation + rare-trigger caveat + style cleanup. No substantive trade change.)*
