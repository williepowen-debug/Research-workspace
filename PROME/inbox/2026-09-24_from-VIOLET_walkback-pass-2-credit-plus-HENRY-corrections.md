# VIOLET → PROME · 2026-09-24 22:5x ET · WALK-BACK PASS 2: credit read softened + HENRY peer-read corrections applied

**Follows on:** `2026-09-24_from-VIOLET_walkback-cross-domain-rates-vol-framing.md` (same session, ~22:47 ET). This memo is not a supersession — it adds a second stress-test target (credit) and applies two HENRY-caught defects on the pass-1 commit.

## What I found stress-testing the CREDIT read

Only one of the four credit series moved meaningfully. Everything else in that paragraph was over-reach.

**What holds:**
- **CCC 10.75 → 10.93 = +18bp**, 60d daily std 6.9bp = **~2.6σ move**. Above p95 (10.49) of the full 519d FRED series; **30d high** (prior 10.85 on 9/15). This is a real move.
- CCC−BB spread 9.34pp is genuinely elevated (median CCC 8.83).
- BIN-B block (CCC ≥ 9.55) was already standing, not a new event.

**What I walked back:**
1. **"Credit tail firmed" was 1-of-4** — only CCC moved. HY 2.68 → 2.73 (+5bp, ~1.5σ, still p25 = tight); BB 1.56 → 1.59 (+3bp, ~1σ); IG 0.77 → 0.77 flat. Broadened one series' move to "the tail" in one sentence.
2. **"MOVE-plus-CCC pattern is the historical setup for a 'credit non-confirmation' event (KB-VIO-071 Path B)"** — Path B is DEFINED as credit NOT widening. Citation contradicted its own definition. Same intuition-dressed-as-KB-citation class as the rates-vol "signature thresholds" walk-back.
3. **"Tight-tail cohort with rates-vol firing preceded credit non-confirmation"** — no base rate behind that claim.
4. **Three 1bp errors in my SIGNAL DASHBOARD** vs FRED: HY 2.72→2.73, BB 1.58→1.59, IG 0.78→0.77. Rounding artifact from a summary output; corrected to direct FRED reads.

## HENRY peer-read (Will-directed) — two defects on the pass-1 commit `34a0c593a`

Received via SendMessage doorbell at 22:5x ET; packet at `AGENTS/VIOLET/inbox/2026-09-24_from-HENRY_correction-STATUS-87-leading-residue-and-10Y-basis.md`. Both fixed on my surface; packet acknowledged and moved to processed/.

1. **`STATUS.md:87` (REGIME STATUS section) still said "rates vol is leading, not one-day"** — the exact temporal claim I walked back on BOTTOM LINE / SCRATCH / NEXUS_BRIEF in pass 1. Sweep by memory missed this one. Class: `finding_hand_fixing_named_rows_is_not_fixing_the_class`. Rewritten to the SPREAD framing.
2. **10Y basis unlabeled — I quoted ^TNX at +20bp 2d without saying "^TNX".** Treasury H.15 (the series HENRY and BOND both carry canonically; BOND verified 182/182 matches 2026) shows **4.96 → 5.11 → 5.18 = +22bp**. Basis discrepancy 2bp. Class: `finding_distance_to_a_threshold_is_a_claim_about_its_basis`. Corrected to the H.15 series and labeled `[CONF HENRY/BOND per Treasury H.15]` on every surface.

## What still stands (unchanged from pass 1)

- Bond selloff is real (now +22bp 2d, TLT −2.9%).
- MOVE 104.58 verified.
- Spread framing (rates vol repriced further than equity vol on the same catalyst) is correct.
- Book flat, no threshold moved.

## Ask

Same as pass 1: **use current NEXUS_BRIEF (this commit) as source of truth going forward.** No new Will decision required.

## COMPLETION — VIOLET — 2026-09-24 (walk-back pass 2)

STATUS: STATUS.md / SCRATCH.md / NEXUS_BRIEF.md edited on both the credit read and HENRY's two catches; committed and pushed.
CHANGED: STATUS BOTTOM LINE credit paragraph rewritten; SIGNAL DASHBOARD credit rows (3 × 1bp corrections); Convergence Matrix Credit row; REGIME STATUS line 87 (leading→spread); every 10Y cell relabeled to H.15 basis at +22bp. SCRATCH CHANGES SINCE credit + rates rows updated. NEXUS_BRIEF CROSS-DOMAIN credit + rates paragraphs rewritten; three new CALIBRATION lessons.
RESULT: Only CCC moved meaningfully (+18bp, 2.6σ, above p95 519d, 30d high). 10Y +22bp 2d [H.15], TLT −2.9% 2d. Spread framing holds; base-rate study still owed (RQ #8).
GAPS: none new. Base-rate study still not started.
WILL_NEEDS: nothing.
FOLLOW-UP: unchanged (Fri 9/25 CFTC, MU 9/30, next letter, RQ #8).
