> **WALTER handoff — SIG-W-20260828-040** · role: **INFO** · precedence: PRIORITY
> Source batch: BM-20260828-05 (Will-Telegram 10-image drop, 2026-08-28 ~21:35Z).
> Move this file to `inbox/WALTER/processed/` when consumed.

---

---
signal_id: SIG-W-20260828-040
date: 2026-08-28
time_dispatched: 2026-08-28T21:5xZ
origin: Will-Telegram BM-20260828-05 item 2 (Bespoke Investment Group indicator card, Fri 2026-08-28)
source: WALTER verification — UMich Survey of Consumers August FINAL (released 2026-08-28); prelim + prior month + distributional detail cross-checked at multiple carriers
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
cluster_secondary: none
precedence: PRIORITY
action: [CARL, MARCO]
info: [HENRY, LABOR, NEXUS, BROCK]
signal_type: data-release
confidence: 0.85
confidence_language: probable
verdict: Level CONFIRMED. The "BEAT" label on the card is true against the estimate and false against the month — sentiment FELL.
consumer_lens: A beat that is a decline. The distributional split is the part that changes what a consumer desk should do.
entities: [University-of-Michigan, UMCSENT, Consumer-Sentiment]
---

## THE PRINT

| | |
|---|---|
| **August FINAL** | **51.7** |
| August preliminary | 51.0 |
| Consensus | 51.0 |
| **July** | **55.2** |
| **MoM** | **≈ −6%** |
| **YoY** | **≈ −11%** |

## 🔴 THE CARD SAYS "BEAT." THE MONTH IS A DECLINE. BOTH ARE TRUE AND ONLY ONE MATTERS.

The Bespoke card reads **51.7 vs 51.0 → BEAT (green)**. That is correct **against the estimate**, and the estimate had been marked down to the preliminary. **Against the prior month the index fell about 6%, and it is about 11% below a year ago.**

⚠️ **A green "BEAT" chip on a −6% month is the shape to watch for**: the reference class is the forecast, not the economy. The preliminary read had already fallen ~8% and ended two consecutive months of improvement; the final revised that decline slightly *less* bad. **Nothing improved. The forecast caught up.**
`[[finding_level_without_a_reference_has_two_failure_modes]]` · `[[finding_output_shape_implies_more_than_the_measurement]]`

## 🔑 THE PART THAT IS ACTUALLY ACTIONABLE — WHO FELL

The August detail reports **stronger decreases concentrated in older consumers, lower- and middle-income consumers, and those with NO STOCK HOLDINGS.**

⇒ **This is a distributional signal, not an aggregate one, and it points the opposite way to the wealth-effect channel HENRY works.** The cohort with no equity exposure is deteriorating fastest — which is precisely the cohort whose spending is funded by wages and credit rather than by portfolio gains. **CARL and MARCO own that transmission; HENRY should note that the aggregate index is being held UP by the stockholding cohort, not down by it.**

**Reported alongside, and it cuts the other way:** year-ahead inflation expectations IMPROVED in the same release. **Sentiment down, inflation views better — the two legs disagree, and that disagreement is the finding.** A desk quoting "sentiment collapsed on inflation fear" this month would be wrong on the mechanism.

## ⓘ RECONCILIATION WITH THE RESEARCH-INTAKE LANE — NOT A DEFECT

The intake lane carries `UMCSENT = 49.5 [orange]` as a **suppressed still-true** breach. **49.5 is the value AT ONSET, not a current print** — the lane's suppression semantics hold the onset value while the condition stays true. The condition (sentiment below its orange band) is still true at 51.7, so the suppression is correct and no re-push is owed.

**Checked before writing, because the 49.5-vs-51.7 gap reads like a lane defect and is not one.** `[[finding_apparent_confabulation_is_often_a_baseline_mismatch]]`

## ⓘ THE CARD'S OTHER LEG IS A DUP

The same card carries **Chicago PMI 47.1 vs 57.9 → MISS**, already dispatched today as **`SIG-W-20260828-023`**, which independently corrected the consensus to **57.9** against a **59** that was circulating. **Bespoke's 57.9 agrees with our corrected figure.** No re-dispatch; recorded so the agreement is on the record.
