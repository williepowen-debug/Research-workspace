# BROCK Predictions Scoreboard

**Updated:** 2026-06-20. Tracks resolution outcomes + calibration for falsified/confirmed predictions. Resolved rows live in `PREDICTIONS_ARCHIVE.tsv`; OPEN/PARTIAL/tombstones stay in `PREDICTIONS.tsv`. Full per-prediction detail (invalidation, notes) is in the archive — this is the summary scoreboard.

---

## SCORE (fully-resolved, n=7)

| Hit rate | Brier (mean) | Baseline |
|----------|--------------|----------|
| **5 / 7 = 71% correct** | **0.244** | 0.25 (coin-flip) |

**Confirmed correct (5):**
| ID | Call | Conf | Outcome |
|----|------|------|---------|
| BRK-03 | ≥1 major BDC triggers redemption gate | 55% | ✅ massively exceeded (13+ gates) |
| BRK-05 | Shadow default rate acknowledged by a rating agency | 50% | ✅ Fitch 9.2% cohort + Apollo Zito "marks are wrong" |
| BRK-08 | Blue Owl reduces/exits hyperscale DC exposure | 35% | ✅ OBDC II frozen, forced $1.4B sales, CoreWeave syndication failed |
| BRK-21 | National Dentex defaults at Apr-26 maturity | 75% | ✅ added to OBDC non-accrual Q1 |
| BRK-28 | HY OAS→260 OR APO>$130 sustained by 6/30 | 50% | ✅ APO leg fired (>$130 ×5 on the $35B Broadcom deal) |

**Missed (2):**
| ID | Call | Conf | Why it missed |
|----|------|------|---------------|
| BRK-14 | ≥1 of MSFT/GOOG/META/AMZN/NVDA cuts FY capex | 40% | ❌ all RAISED/maintained (META +$10B guide, GOOGL +107%) — AI-capex boom; **conf was correctly LOW** |
| BRK-09 | HRZN merger terms worse / NAV floor broken | 60% | ❌ closed at announced NAV-for-NAV terms; **premise was factually INVERTED** — MRCC merged into HRZN, not vice-versa |

**Partial / mixed (2, kept active):**
- **BRK-06** (neocloud credit event, 45%) — PARTIAL: Blue Owl walked CoreWeave/Oracle + failed $4B syndication, no outright default yet.
- **BRK-27** (non-traded BDC NAV markdown >5% in Q1, 60%) — MIXED: OTF −4.85% (just under), forced-mark cascade confirmed in spirit, strict >5% threshold barely not met. Classic threshold-vs-mechanism.

---

## CALIBRATION READ

- **Under-confident on the structural thesis.** The 5 correct calls averaged 53% confidence but **all came true** — BRK-08 at 35% fully confirmed, BRK-03 at 55% "massively exceeded." The core transmission thesis (gates → sponsor distress → default acknowledgment → disclosure cascade) verified MORE reliably than the confidence implied. **Lean into directional structural calls; they've earned a higher prior.**
- **The two misses are different species:**
  - **BRK-14 = good discipline.** A macro-contrarian call (capex *peak/cut*) against a secular tailwind (AI buildout) — correctly carried LOW conf (40%) and correctly missed. The MISS is itself thesis-*supporting* (capex re-accelerating = more AI-infra lending demand).
  - **BRK-09 = a premise error, not a calibration error.** 60% conf, but the underlying framing (HRZN acquired by Monroe, terms worse) was factually **inverted** — caught only at resolution. The fix isn't lower confidence; it's **verifying the premise at creation** (per LESSONS #7 ownership-chain + finding_verification_correction_downstream_propagation), not at resolution.
- **Brier 0.244** edges the 0.25 coin-flip baseline; with n=7 it's noisy, dragged up by BRK-08 under-confidence and BRK-09 overconfidence-on-a-wrong-premise. Direction of the read (structural calls under-priced, premise-sourcing is the error surface) holds.

## TAKEAWAYS (feed into next prediction-writing)
1. **Structural/cascade calls (gates, default-acknowledgment, sponsor distress) hit and were under-priced** → don't anchor them too low.
2. **Premise-verify at creation for any call naming a specific deal/entity mechanic** (HRZN direction was the failure mode), not just at resolution.
3. **Low-conf macro-contrarian calls against a secular tailwind are healthy** even when they miss (BRK-14) — keep the confidence honest and low.

---

*Resolved-row detail: `PREDICTIONS_ARCHIVE.tsv`. Active OPEN/PARTIAL forecasts: `PREDICTIONS.tsv` (14 OPEN + 2 PARTIAL as of 6/20). Update this scoreboard whenever a prediction resolves.*
