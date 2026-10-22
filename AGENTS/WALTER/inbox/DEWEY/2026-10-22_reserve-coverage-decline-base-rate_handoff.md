# DEWEY → WALTER handoff · 2026-10-22 · state NEW

**Report:** `AGENTS/DEWEY/output/2026-10-22_reserve-coverage-decline-base-rate.md`
**Commission:** `REQ-DEWEY-20261022-003` (discovery under Will's standing direction, 483e72c07). Close the DEEP_RESEARCH_FLAGGED_LOG row.
**Stubs landed (create-only, this commit):** REGINALD (action) · GIBBS, CREED, WAL, OZK, FLG, RED (info) · PROME (info, `PROME/inbox/`).

**Kill conditions at intake: did NOT fire.** (1) REGINALD and GIBBS hold no ≥2-downturn coverage-decline study; their coverage mentions are current-quarter or single-bank. (2) FDIC history is retrievable: the BankFind API serves bank-level call reports for 1984Q1–2026Q2, verified by DEWEY.

**Headline for routing:**
- (a) Pre-registered trigger (NPL ratio up AND coverage down, YoY, $10–100B band): a ≥25bp charge-off rise followed within 4Q in **2/10 episodes vs 25% unconditionally**, so no lift. There is modest lift at 8Q (5/10 vs 36%; provisions 7/10 vs 49%). Every charge-off hit is pre-CECL, from about 3 cycles, and one episode moves a rate 8–10pt.
- Cycles: caught 2007–10 (6Q lead) and 2001–02; missed 1989–90 (nominal band); false alarm 2015–16; **2023–26 unresolved: on 10 straight quarters with charge-offs flat at 0.35% → 0.36%.**
- (c) **NO:** the banks whose coverage fell most did not lose most (2007–10 ρ = −0.064; the largest-decline quintile had the lowest failure rate). The problem-loan RISE carries the signal (ρ ≈ +0.46).
- Placement: DEWEY's Q2 call-report coverage, EGBN 88.5% and VLY 123.3%, does not match the company figures relayed in SIG-012 (109%, ~131%). Both are shown, separately. CECL makes pre-2020 comparisons overstate today's cushion.
- Collateral defense: at 2008–13 failed banks, C&D severity was 53% and CRE 39%, and 15 of 19 were under-reserved. Failed-bank denominator.

**Do-not-relay-as:** "the coverage decline predicts losses" or "the coverage decline is harmless". The rise in problem loans is what history supports, and the current episode is open. **Rerun owed after ~10/30**, when the Q3 call reports land.
