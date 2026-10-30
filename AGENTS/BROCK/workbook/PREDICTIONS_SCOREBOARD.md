# BROCK Predictions Scoreboard

**Updated:** 2026-10-30 17:16 ET — RE-SCORED on all 15 resolved predictions (DAEDALUS profile refresh item 2; recomputed by BROCK from the two ledgers, reproducing the 7/09 n=10 figures exactly). **The 7/09 calibration read below is SUPERSEDED: its sign has flipped.** Resolved rows through 7/09 live in `PREDICTIONS_ARCHIVE.tsv`; later resolutions (BRK-02, 10, 22, 27, 30) stay in place in `PREDICTIONS.tsv` (the archive move is retired, not owed). Update this file at every resolution (closeout 7a).

## SCORE — CURRENT (n=15, 2026-10-30)

| Set | Came true | Brier (mean) | Baseline |
|---|---|---|---|
| **All resolved (n=15)** | **8 / 15 = 53%** | **0.254** | 0.25 (coin-flip) |
| Through 7/09 (n=10) | 7 / 10 = 70% | 0.216 | 0.25 |
| Since 7/09 (n=5) | 1 / 5 = 20% | 0.331 | 0.25 |

**Since 7/09:** BRK-27 FALSE-on-letter (60%) · BRK-30 TRUE (65%, calibration ≈0, LESSONS #32) · BRK-02 FALSE (75%) · BRK-22 FALSE (60%) · BRK-10 FALSE (50%). All four misses were bearish calls at ≥50%.

**Current calibration read:** overall Brier is now slightly WORSE than a coin flip. The 7/09 advice to "lean into" structural bear calls and not anchor them low (CALIBRATION READ first bullet, TAKEAWAYS #1) is **WITHDRAWN**: the later sample went the other way on exactly those calls. n=15 is still small; the honest read is "no demonstrated edge on dated bear calls", and new bearish predictions at ≥60% need a named instrument and an inversion test at registration (STANDING TRAPS 7). BRK-06 PARTIAL is excluded from both counts.

---

## 7/09 READ (n=10) — SUPERSEDED, kept as history

---


| Hit rate | Brier (mean) | Baseline |
|----------|--------------|----------|
| **7 / 10 = 70% correct** | **0.216** | 0.25 (coin-flip) |

**Confirmed correct (7):**
| ID | Call | Conf | Outcome |
|----|------|------|---------|
| BRK-03 | ≥1 major BDC triggers redemption gate | 55% | ✅ massively exceeded (13+ gates) |
| BRK-05 | Shadow default rate acknowledged by a rating agency | 50% | ✅ Fitch 9.2% cohort + Apollo Zito "marks are wrong" |
| BRK-08 | Blue Owl reduces/exits hyperscale DC exposure | 35% | ✅ OBDC II frozen, forced $1.4B sales, CoreWeave syndication failed |
| BRK-21 | National Dentex defaults at Apr-26 maturity | 75% | ✅ added to OBDC non-accrual Q1 |
| BRK-28 | HY OAS→260 OR APO>$130 sustained by 6/30 | 50% | ✅ APO leg fired (>$130 ×5 on the $35B Broadcom deal) |
| BRK-01 | PSEC dividend cut again or rating downgrade | 60% | ✅ dividend-cut leg fired ($0.045→$0.035, -22.2%, 5/7/26 8-K); ratings leg N/A (both downgrades pre-window) |
| BRK-24 | Analyst/media publishes Athene FY2025 statutory analysis by Q2 | 55% | ✅ Eisman/Gober (3/2, Benzinga/Yahoo/AOL) + "THE HOLE" Substack (4/4) — 6/8 audit sweep MISSED an already-published event |

**Missed (3):**
| ID | Call | Conf | Why it missed |
|----|------|------|---------------|
| BRK-14 | ≥1 of MSFT/GOOG/META/AMZN/NVDA cuts FY capex | 40% | ❌ all RAISED/maintained (META +$10B guide, GOOGL +107%) — AI-capex boom; **conf was correctly LOW** |
| BRK-09 | HRZN merger terms worse / NAV floor broken | 60% | ❌ closed at announced NAV-for-NAV terms; **premise was factually INVERTED** — MRCC merged into HRZN, not vice-versa |
| BRK-29 | 2nd alt-mgr PE-evergreen gate within 30d of Partners Group | 30% | ❌ clean window close 7/4, no 2nd PE-wrapper gate (ADS 6/23 was a credit fund, doesn't count); **conf was correctly LOW** |

**Partial / mixed (2, kept active):**
- **BRK-06** (neocloud credit event, 45%) — PARTIAL: Blue Owl walked CoreWeave/Oracle + failed $4B syndication, no outright default yet.
- **BRK-27** (non-traded BDC NAV markdown >5% in Q1, 60%) — MIXED: OTF −4.85% (just under), forced-mark cascade confirmed in spirit, strict >5% threshold barely not met. Classic threshold-vs-mechanism.

---

## CALIBRATION READ

- **Under-confident on the structural thesis.** The 5 correct calls averaged 53% confidence but **all came true** — BRK-08 at 35% fully confirmed, BRK-03 at 55% "massively exceeded." The core transmission thesis (gates → sponsor distress → default acknowledgment → disclosure cascade) verified MORE reliably than the confidence implied. **Lean into directional structural calls; they've earned a higher prior.**
- **The two misses are different species:**
  - **BRK-14 = good discipline.** A macro-contrarian call (capex *peak/cut*) against a secular tailwind (AI buildout) — correctly carried LOW conf (40%) and correctly missed. The MISS is itself thesis-*supporting* (capex re-accelerating = more AI-infra lending demand).
  - **BRK-09 = a premise error, not a calibration error.** 60% conf, but the underlying framing (HRZN acquired by Monroe, terms worse) was factually **inverted** — caught only at resolution. The fix isn't lower confidence; it's **verifying the premise at creation** (per LESSONS #7 ownership-chain + finding_verification_correction_downstream_propagation), not at resolution.
- **Brier 0.216** edges the 0.25 coin-flip baseline; with n=10 still noisy but improving on the 0.244 n=7 read. BRK-01/BRK-24 landed correct at moderate confidence (good); BRK-29's correctly-low 30% conf on a miss pulls Brier down further (a well-calibrated low-conf miss helps the score, unlike BRK-09's overconfident wrong-premise miss). Direction of the read (structural calls under-priced, premise-sourcing is the error surface) holds.
- **BRK-24 is a process-failure catch, not a calibration lesson.** The qualifying event (Eisman/Gober, 3/2/26) predated the 6/8 audit sweep by ~3 months, yet the sweep recorded "zero external analysis" and RE-ARMED at lower confidence (65%→55%) on a false negative. The miss wasn't in the prediction — it was in the verification sweep not searching hard enough for an already-public event. Echoes LESSONS #17 (verify filing status, don't carry "pending" forward without a real check) at the media-monitoring layer.
- **BRK-29 is a ledger-hygiene catch, not a new finding.** Substantively graded LAPSE on 7/4 (STATUS/NEXUS_BRIEF/LAST_COMPLETION all cited it correctly) but the PREDICTIONS.tsv row itself sat Status=OPEN for 5 days past its own resolve date — a "said it but didn't file it" gap, caught only by the 7/9 self-sweep's explicit resolve-date scan. **Takeaway: a narrative grade in STATUS text is not a substitute for updating the ledger row — both must happen at resolution time, not just one.**

## TAKEAWAYS (feed into next prediction-writing)
1. ~~Structural/cascade calls hit and were under-priced → don't anchor them too low.~~ **WITHDRAWN 10/30** — see SCORE — CURRENT.
2. **Premise-verify at creation for any call naming a specific deal/entity mechanic** (HRZN direction was the failure mode), not just at resolution.
3. **Low-conf macro-contrarian calls against a secular tailwind are healthy** even when they miss (BRK-14) — keep the confidence honest and low.
4. **"Publication-exists" predictions need an actual targeted search at every audit, not just a general sweep** — BRK-24's false-negative RE-ARM (6/8) shows a passive "did anything cross my desk" scan can miss a named, findable, already-published event. For monitoring-type predictions, run an explicit targeted query (named principals + topic) at every disposition check, not just a general news skim.
5. **Grading a prediction in prose (STATUS/NEXUS_BRIEF) does not resolve it — the PREDICTIONS.tsv row must be moved/updated too.** BRK-29 sat OPEN in the ledger for 5 days after being correctly called LAPSE everywhere else. Add a boot-time check: any row whose Resolve_Date has passed should be either dispositioned this session or explicitly re-armed with a new date — never silently carried.

---

*Resolved-row detail: `PREDICTIONS_ARCHIVE.tsv`. Active OPEN/PARTIAL forecasts: `PREDICTIONS.tsv` (12 OPEN + 2 PARTIAL as of 7/9). Update this scoreboard whenever a prediction resolves.*
