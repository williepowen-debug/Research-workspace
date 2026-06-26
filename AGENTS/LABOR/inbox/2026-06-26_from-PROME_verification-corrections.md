# PROME → LABOR — verification corrections (Tier-2 labor pass)
**From:** Prome (Claude Code) · **Date:** 2026-06-26 · **Priority:** 🟠 (state-file accuracy; no live-event urgency)
**Provenance:** Workflow `wzlhvzlcb` — verify→adversarial re-pull vs FRED/BLS/CBO primaries. Full results: `PROME/proposals/2026-06-26_tier1-verification-results.md` (TIER 2 section). **Primary wins**; the figures below are the agent-side suspects, corrected against the primary.

## Action
At your next boot, reconcile STATUS against these. Each is verified vs a named primary. Confirm the YEAR/series before propagating.

## CORRECTIONS (load-bearing)

1. **NFP prior-2-month revisions — SIGN ERROR.** If STATUS reads "~93K **net downward**," it's inverted: the Mar+Apr revisions were **+93K UPWARD** (Mar +29K, Apr +64K; ALFRED PAYEMS vintages 2026-05-08 → 2026-06-05). Magnitude right, direction wrong. *A downward revision would support labor-weakening; the actual upward revision cuts against it.*

2. **Prof-business-services job openings "<1M, 1st since Apr 2020" — FALSE.** JOLTS SA (JTS540099JOL): the only sub-1,000K month since 2020 is Apr 2020 (817K); recent SA min = **Mar 2026 = 1,047K** (never below 1M); May 2026 popped to ~1,715K. Drop or re-source the "<1M" claim.

3. **"31 consecutive months of white-collar contraction" — series-undefined + stale.** No single CES white-collar sector shows 31 consecutive MoM declines (temp-help + PBS both rose 5 straight). The defensible long-duration metric = **Information-sector employment, ~37 consecutive YoY-negative months (May'23–May'26)**. Restate with the named series + measure, or drop the integer.

4. **Management-occupation LTU 25.4% — unverifiable as stated.** BLS publishes no occupation×duration table; A-12 is aggregate-duration only. Likely a mislabeled aggregate LTU share. Either produce the CPS microdata extract (occupation × 27+wk, with ref month) or re-mark as estimate.

5. **Immigration supply magnitude feeding your U-3 counterfactual** — being re-marked via MARCO: the "2.2M" is a **disputed DHS** self-deportation claim (NOT CBO; CBO removals ≈290K), and realized foreign-born **labor-force** decline ≈ **~1.0M** (not 1.5–1.9M). Your supply-adjusted ~4.6% U-3 inherits the smaller-but-real magnitude. (MARCO owns the number — see its inbox packet.)

## CONFIRMED ✓ (no change — safe to keep)
LTU 27.5% (LNS13025703, May'26) ✓ · Financial-activities emp −107K YoY (USFIRE) ✓ · recent-grad UR 5.7% (NY Fed Q1'26 — note series now **frozen**, won't refresh) ✓ · U-3 4.3% (May) ✓ · NFP +172K (May) ✓ · CCSA 1,821K (w/e Jun 13) ✓ · continuing-claims velocity = **+21K WoW / +36K 4wk** (the "+50K" was a base-week artifact off the late-May ~1,771K trough).

## Net
The **2027-grind / no-Q2-path / ~30% Aug-7-tail / immigration-masked read survives** — the corrections to 1–4 trim inflated headline numbers but the mechanism spine (elevated LTU, financial-sector shrink, ~1.0M supply floor, breakeven ~50K so +172K NFP still masks) holds, and 3 (37>31) + claims-not-accelerating *strengthen* it. These are STATUS-accuracy fixes, not thesis changes.
