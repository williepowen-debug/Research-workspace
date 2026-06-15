# CASE 03 — KRE Rate-vs-Credit Discriminator — RUBRIC

**SCORER ONLY. This file must NEVER enter the runner's context.**

**Role:** GUARDRAIL (baseline PASS expected; success after a change = stays PASS).
**Principle source:** CLAUDE.md "Structural vs war attribution test" — *"If KRE drops DESPITE falling yields (flight to safety), credit story is dominating — flag to REGINALD."* Plus the methodology "Distinguish Margin Trade vs Credit Trade" (margin grinds / credit gaps). CLAUDE.md auto-loads → baseline PASS expected. A FAIL here is a genuine reasoning regression (the principle is in the always-loaded body).

**What the case tests:** the colleague offers a plausible wrong path — "yields fell, so it's a margin/duration move that will grind and find a floor." The discriminator: KRE fell HARD *despite* a flight-to-safety yield drop that should have cushioned banks → the move is **credit-driven**, corroborated by HY widening + the CRE charge-off. Credit trades GAP; margin trades GRIND.

---

## EXPECTED (all must be clearly met for PASS)

- [ ] **Calls it a CREDIT trade, not margin** — rejects the colleague's duration/margin framing.
- [ ] **Keys on the KRE-vs-yields divergence:** KRE down DESPITE falling yields is the tell — falling yields (flight-to-safety) should have bid/cushioned banks; KRE fell anyway ⇒ credit dominating. (Explicitly uses the "down despite falling yields" logic.)
- [ ] **Cites corroborating credit signals:** HY OAS widening +19bps and/or the CRE charge-off/provision as confirmation it's credit, not rates.
- [ ] **Trajectory: GAP, not grind** — credit trades gap (fast/discontinuous); rejects the "grind slowly / yields put a floor under it" expectation.
- [ ] **Cross-agent: flag to REGINALD** (credit-equity transmission / regional-bank credit).

## DO-NOT (any one present → FAIL)

- [ ] Agrees it's a margin/duration trade because yields fell.
- [ ] Says the falling yields will put a floor under / support KRE (misses that KRE fell despite them).
- [ ] Forecasts a slow grind as the base case.
- [ ] Ignores or doesn't reconcile the KRE-down / yields-down divergence.

## Contamination check
Watch for verbatim echo of "down despite falling yields" *as a flagged quote attribution to a rubric* — the concept is fine and expected (it's core HENRY methodology); only an exact lift of rubric-only sentences signals leakage. Low contamination risk on this case.

## Scorer notes
- Core discriminator = EXPECTED #2 (the divergence read). If HENRY reaches "credit trade" without using the KRE-vs-yields logic (e.g. only cites the charge-off), score #2 borderline → lean FAIL: the case specifically tests the *price-action discriminator*, not just reading a headline.
- The "gap vs grind" criterion matters for trajectory — a PASS must reject the colleague's "grinds slowly" framing, not just relabel the driver.
- Bonus (not required): noting the move's speed makes it actionable now vs a slow rate move that can be faded.
