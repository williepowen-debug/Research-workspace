# CARL BRIER AUDIT — first run, 2026-07-24
**Deferred since v2.5.1 (2026-05-01). Run at Will's direction.** Re-runnable: `.venv/bin/python3 AGENTS/CARL/scripts/brier_audit.py`

---

## The headline, unsoftened

| | As-recorded | Best-recoverable ex-ante |
|---|---|---|
| **Brier score** | **0.300** | **0.340** |
| Climatology (always forecast the 45% base rate) | 0.223 | 0.223 |
| **Brier Skill Score** | **−0.349** | **−0.527** |
| Mean forecast | 73.9% | 75.2% |
| Actual hit rate | 45.0% | 45.0% |
| **Overconfidence** | **+28.9pp** | **+30.2pp** |

**Both scores are worse than 0.25 — the score you get by saying "50%" to everything. Skill is negative on both bases: CARL's forecasts were worse than knowing nothing except the base rate.**

**And the as-recorded score is flattered.** `PREDICTIONS.tsv` Confidence holds the value *at resolution*, and CARL trims losers as evidence arrives (CRL-03 ran 90→72 before resolving MISSED; CRL-11 85→83). Basis A is a **ceiling** on true skill, not an estimate of it.

**Murphy decomposition (as-recorded):** Reliability **0.109** (should be ~0), Resolution **0.037** (barely discriminating), Uncertainty 0.248. The record is badly calibrated *and* barely informative.

---

## Where it went wrong — confidence made it worse, not better

| Band | n | mean forecast | actual | gap |
|---|---|---|---|---|
| 55–65% | 2 | 60% | 50% | +10% |
| 65–75% | 4 | 71% | 38% | **+34%** |
| 75–85% | 3 | 79% | 33% | **+45%** |
| 85–100% | 1 | 98% | 100% | −2% |

**The higher the confidence, the worse the calibration** — the inverse of what a useful forecaster looks like. On the ex-ante basis it's starker: the 75–85% band went **0-for-2** and the 85–100% band **1-for-3**.

## The content pattern — what hits and what misses

| Outcome | Prediction | Shape |
|---|---|---|
| ✅ CRL-04 | student 90+ >10% | **level on an already-trending series** (9.6→10.3, climbing) |
| ✅ CRL-06 | foreclosures >70K/qtr | **level already being cleared at registration** |
| ✅ CRL-18 | GDP 2nd-est revision band | **near-mechanical** |
| ✅ CRL-26 | gas crosses $4.00 | **short-horizon continuation** (8 days, from $3.94) |
| ⚠️ CRL-19 | Core PCE acceleration | direction right, **magnitude light** |
| ❌ CRL-01 | gas peak Mar 14–21 | direction right, **timing/magnitude wrong** |
| ❌ CRL-09 | JOLTS ratio <0.88 | **turn call** on a denominator-prone series |
| ❌ CRL-11 | hires ≤3.2% | threshold on a print that was **revised away** |
| ❌ CRL-03 | Fannie MF >0.80% | continuation that **reverted** |
| ❌ CRL-24 | SYF NCO >5.5% **AND** coverage down | **CONJUNCTION** — P(A∧B) ≤ min(P(A),P(B)), registered at 60% |

**CARL is good at "this established trend reaches a level" and bad at "this series turns or crosses a threshold by a date."** Four of five misses are the documented *direction-right/magnitude-or-timing-wrong* family.

### The uncomfortable structural finding
**CARL's documented failure taxonomy did not reduce CARL's failure rate.** Boot step 7c exists specifically to force reading the MISSED notes before writing a new prediction. **CRL-24 was registered 2026-06-25 — after CRL-01 and CRL-09 were already logged as misses — and it was a conjunction, the most predictable failure shape available.** Reading a taxonomy at boot is not the same as applying it at registration.

---

## What this does NOT license — the vintage caveat

**A blanket −29pp haircut on the open book would be wrong.** The resolved set was written mostly Mar–May 2026 at a mean of **73.9%**. **The current open book averages 51.8%** — a 22pp shift. The trimming discipline of the last three months (including six cuts today) has already moved the book most of the way toward calibration. Applying the historical bias to today's book would push CRL-12 and CRL-21 to ~5%, which is absurd.

**The bias is a property of the old high-confidence vintage, not of the current book.**

## What it DOES license — two specific rows, not a blanket

Only two open predictions still carry the failed vintage's signature (≥75%):

| | | Verdict |
|---|---|---|
| **CRL-05** — CC 90+ >13.74%, **85%** | Level continuation on a trending series (12.70→13.1, climbing) — **this is the HIT shape** (same as CRL-04) | **DEFENSIBLE, held at 85%** |
| **CRL-07** — FL UI exhaustion → DQ spike, **85%** | **No numeric bar.** Flagged this morning as unfalsifiable-by-vagueness; magnitude already caveated (FL ~8% recipiency, ~42.5K recipients); window (Jun–Aug) nearly closed | **CUT 85 → 40%** |

**CRL-07 is the row that looks most like the failures**: high confidence on a vague, unfalsifiable claim. Cut applied, and it is now forced to resolve by **8/31** rather than sit open.

---

## Prescriptions

1. **Ceiling of 75% unless the prediction is a level-continuation on an established trend or near-mechanical.** CRL-04 (98%) and CRL-18 (60%) were both fine; the 72–85% band is where the damage is.
2. **No conjunctions without pricing them as conjunctions.** P(A∧B) ≤ min(P(A),P(B)) — CRL-24 was registered at 60% when neither leg individually deserved much more.
3. **Threshold calls on revision-prone series (JOLTS, NFP, hires) are the worst category — register at ≤40% or not at all.**
4. **Move the failure-taxonomy check from BOOT to REGISTRATION.** Reading it at boot demonstrably didn't stop CRL-24. Candidate mechanical form: a `consistency_check.py` warning on any new prediction that is a conjunction, or that names a revision-prone series, or that carries ≥75% without a level-continuation justification.
5. **Record ex-ante confidence in its own column** so the next audit doesn't have to reconstruct it from Notes (only 5 of 10 were recoverable).

---

## Caveats
**N = 10.** TERRY's paper-book spec sets N≥10 as the *minimum* before scoring acts on anything — this is exactly at the floor. **Directional, not significant.** MIXED scored as 0.5 by convention. Legacy pre-TSV "confirmed" bullets are excluded: no ex-ante probability was ever recorded for them, so including them would be pure survivorship — only the winners were written down.

**Re-run at N≈20** and check whether the vintage improvement is real or whether the current 51.8% book is simply younger and hasn't met its resolvers yet.
