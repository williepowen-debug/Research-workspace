---
name: finding-catalyst-vs-consequence-conflation
description: Probability-shaped signals derived from catalyst probabilities silently inflate when transcribed as consequence probabilities — require the explicit P(consequence | catalyst fires) conditional
metadata: 
  node_type: memory
  type: finding
  originSessionId: 018343d2-0037-48ce-ae5b-d6149d8a5486
---

**Rule:** When an agent ships a probability-shaped signal derived from a catalyst, the headline number must use the full conditional structure:

```
P(consequence) = P(catalyst fires) × P(consequence | catalyst fires)
```

NOT `P(consequence) ≈ P(catalyst fires)`. Being right about whether the catalyst fires is a different question from whether the consequence follows.

**Why:** Catalyst probabilities are tracked carefully because the catalyst is the observable, dated event (rate decision, OPEC meeting, payrolls print, election). Consequence probabilities (volatility, repricing, unwind, contagion) are less observable and tempting to anchor on the catalyst — but the conditional is often well below 1.0:

- A *fully-priced* catalyst can deliver with no consequence (market already absorbed it)
- A catalyst can fire and reverse same-day (intervention spike + reclaim; "buy the rumor, sell the news")
- The consequence may require *more than* the catalyst (positioning fuel load, second trigger, regime confirmation)
- The catalyst may fire in the wrong direction (dovish-surprise produces the opposite sign vs hawkish-surprise)
- Consequence often needs a CONDITIONAL conditional: P(consequence | catalyst fires AND positioning loaded) ≠ P(consequence | catalyst fires)

**How to apply:**

- When shipping any probability-shaped signal to another agent or to Will, audit: is this catalyst-prob, consequence-prob, or conflated?
- If you can't write out `P(catalyst) × P(consequence | catalyst)`, the number isn't auditable
- Trigger to suspect conflation: the headline probability matches a single catalyst's probability (e.g. consequence ≈ 70% when the BOJ hike is also 70%; cascade ≈ 65% when the redemption-peak month is also priced 65%)
- Conditional sources to draw from: prior resolutions in your own PREDICTIONS log ("CH-003 says intervention spike-reverses same-day"), historical precedent base rates, named positioning/fuel-load amplifiers, RED-style adversarial challenges to the chain
- Cross-agent disclosure should label "decomposed estimate" not "true probability" when the conditional involves judgment-set anchors

**Related discipline:**

- **Symmetric honesty:** a pure enumerated union over named channels can be falsely precise on the *downside* too. Add a small principled residual for unattributed paths if the precedent has any (e.g. Aug-2024-style cascades where the named trigger doesn't fully explain the violence). Size it state-dependently with an explicit gate — don't let it codify as a permanent floor.
- **Don't backsolve:** let the bottom-up land where it lands. If the honest decomposition disagrees with the prior headline, publish the gap and mark down explicitly. The willingness to disagree with your own prior headline is the value of the decomposition.
- **Distinct from [[finding_threshold_vs_mechanism]]:** that finding warns about thresholds firing on wrong mechanism (TRUE-in-letter, FALSE-in-spirit). This one warns about catalyst-prob being silently transcribed as consequence-prob even when both numbers would be well-anchored individually.

---

**War-story (SAM, 2026-06-03):** Carry-unwind probabilities (7d/30d/60d) had been shipping to LIQUID and HENRY across the v1.5 thesis window as "P(carry unwinds)." RED challenge CH-004 flagged them as conviction levels, not probabilities. Decomposition into the conditional structure revealed two structural errors in the prior buckets:

1. **Catalyst-prob → consequence-prob conflation:** SAM-21 (BOJ hike June 70%) and SAM-23 (MOF intervention #3 72%) were being implicitly transcribed as carry-unwind probabilities. They're not. A fully-priced hike (market ~88%) doesn't unwind on delivery — only the hawkish-on-size/path tail subset does. An intervention that spike-reverses same-day doesn't unwind.

2. **Conditional ignored own resolved evidence:** MOF #3 `P(unwind | fires)` was anchored ~0.50, in direct contradiction of CH-003 (Apr 30 + May 6 interventions both spike-reversed same-day, net ~zero on sustained unwind; pure FX intervention can't fix the rate gap). Rebased to 0.20.

Bottom-up decomposition (5 named trigger channels × explicit conditionals + state-dependent residual gated on CFTC > 60% of cycle peak + judgment-labeled overlap discount for joint-escalation tail) landed:

| Bucket | Prior (catalyst-anchored) | Decomposed | Δ |
|---|---|---|---|
| 7d | 15% | 14% | ~unchanged (catalysts outside window) |
| 30d | 70% | 37% | **−33pp** |
| 60d | 80% | 49% | **−31pp** |

Yen-direction conviction (HIGH) unchanged — only the probability of triggering was overstated. The mismeasurement was structural and was shipping to two downstream agents for weeks. Logged as MEASUREMENT CORRECTION (not view change) to prevent misreading as thesis softening; cross-agent signals led explicitly with "correction, not softening." RED CH-004 closed.

**Key process detail:** Will's pushback on the first seeded anchors was decisive — the naive decomposition still tried to backsolve toward 70% by inflating one conditional (MOF #3 at 0.50). Forcing the conditional to honor CH-003 (0.20) made the bottom-up land at 34-37% instead of 54-70%. The willingness to publish the disagreement is what made the finding real.
