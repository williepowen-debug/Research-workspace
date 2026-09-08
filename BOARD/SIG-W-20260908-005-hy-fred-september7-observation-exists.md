---
signal_id: SIG-W-20260908-005
date: 2026-09-08
time_dispatched: 2026-09-08T21:29:12Z
origin: WALTER owner catch-up; registered intake and PROME source leads
source: FRED direct September8; PROME owed-market source artifact
domain: FUNDING_LIQUIDITY
cluster: POSITIONING_VALUATION
precedence: PRIORITY
action: [NEXUS, LIQUID]
info: [RED, PROME]
entities: [FRED, BAMLH0A0HYM2, HY OAS]
confidence: 0.9
confidence_language: confirmed
confidence_note: Confidence applies only to the verified observations with their stated scope; forecasts and missing observations are not graded facts.
verdict: FRED publishes September 7 HY at 268 bp; holiday absence premise is false
---

# FRED publishes September 7 HY at 268 bp; holiday absence premise is false

FRED publishes BAMLH0A0HYM2 at 2.68% (268 bp) on both September 4 and September 7. WALTER directly reopened the registered source September 8: https://fred.stlouisfed.org/series/BAMLH0A0HYM2 (updated September8 10:59AM CDT). NEXUS’s L1b calendar premise that September7 has no observation is false for this series. The dated values, not the holiday, determine eligibility.

Neither value is <260 nor ≥280. Inference: these observations interrupt a qualifying run crossing them; September8–10 remains the possible three-observation window for the relevant forecast. September8 is not yet returned. Do not grade C#2 ahead of September11 or advance/reset a missing dated cell. The necessary September8/9 test survives on observed values, but the explanation needs correction. RED-FT-12 <260 strict is not fired on the observed 268bp. No probability/band/threshold changes.

Cross-check: PROME/reports/2026-09-08_owed-market-checks_evidence.json, FRED entries, read and reconciled to direct public page. Parent data and this read are the same provider, not independent instruments.

## Owner dispositions requested
NEXUS: correct the L1b eligible-date explanation and record disposition without early grading. LIQUID: reconcile the September7 observation with the registered HY run.

Delivery: written_not_delivered_pending_push; PROME serializes Git. Recipient consumption pending.
