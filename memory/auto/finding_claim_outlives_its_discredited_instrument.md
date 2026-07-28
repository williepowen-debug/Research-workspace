---
name: finding_claim_outlives_its_discredited_instrument
description: "When an instrument is discredited, re-test the claim it carried before retracting it — killing both is over-retraction"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e5157ce7-a04a-4a1e-9277-0b95f01ec956
  modified: 2026-07-28T07:19:04.462Z
---

When the **instrument** behind a claim turns out to be unreliable — a scraped figure with irreconcilable vintages, a proprietary chart, a secondary relay — the reflex is to retract the claim with it. That is often wrong. **Ask whether the claim is independently measurable on a source you already trust.** If it is, re-instrument; don't retract.

HENRY (2026-07-28) retracted a HEN-42 evidence leg because circulating CME FedWatch figures (10.7 / 31.5 / 34.7 / ~38 / 34.3 / 46.5) could not be reconciled to one vintage. The instrument deserved to die. But the *claim* it carried — "the policy path did not reprice on the crude collapse" — was measurable in FRED primaries he already used: across a ~11% two-session drop in Brent, **DFII10 went 2.43 → 2.43 (zero change) while T10YIE fell −7bp.** The entire response ran through inflation compensation and the real/policy leg never moved. The claim was not just salvageable, it came back *stronger* — on primaries instead of scrapes, and it simultaneously refuted the upstream premise (that hike odds "should have" fallen), which meant their not-falling never needed explaining.

**Why:** a strong retraction culture makes retracting feel costless and virtuous, so it gets over-applied. But a retracted-true claim is a real loss: it removes evidence the thesis was entitled to, and nobody re-derives it later because the ledger says "retracted." The asymmetry is invisible — an over-retraction leaves no failing test, just a quietly weaker case.

**How to apply:** before retracting on instrument failure, write the claim as a standalone proposition with no reference to how it was measured, then ask "what else would show this?" Retract only if nothing does. If something does, say explicitly that the *instrument* is retracted and the *claim* is re-based, and name the new source — otherwise readers file the whole thing as refuted. Distinct from [[finding_resolvability_defect_is_status_not_confidence]] (which is about a prediction that *cannot* resolve) and from [[finding_discovery_instrument_defines_the_claim]] (where the instrument genuinely bounds what was claimed). Related: [[finding_retraction_culture_cluster_ratio]], [[finding_standing_guard_is_a_false_negative_risk]].
