---
name: finding_broken_conjunction_leaves_its_other_legs_unrecorded
description: "when a registered conjunction resolves NOT-MET on one leg, the remaining legs become scoreless — and scoreless is exactly what nobody writes down, so the ledger silently keeps only the half that scored; log every leg's evidence regardless of the conjunction's outcome"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5f8e3d38-4381-4276-a0e8-78ea6d830a3c
  modified: 2026-08-20T18:40:54.903Z
---

A registered conditional of the form *"if A and B, then move the weight"* resolves NOT-MET the moment A fails. That resolution is correct and no weight is owed. **But B still printed, and B's evidentiary content survives the conjunction's failure — while its SCORE does not.** Because grading is what triggers a write-up, the leg that decided the outcome gets recorded across every surface and the surviving leg reaches none of them.

**Measured instance (RED, 2026-08-20).** A staffing-canary conditional — *"RHI and KFRC positive 2 consecutive quarters → raise the Soft-Landing weight"* — broke on the RHI leg. That was graded within days and propagated to five surfaces (prediction ledger, ML row, STATUS, scorecard, CHANGELOG). KFRC printed three days later and reached **none of them for 24 days**: tech-staffing revenue +4.0% YoY *accelerating* from +0.2% the prior quarter, direct-hire placements +27.6% YoY, three consecutive quarters of growth, with the domain owner cutting a related prediction on it. **The recorded leg ran with the book; the unrecorded leg ran against it.**

**Why:** the asymmetry is structural, not motivated, which is what makes it hard to see. A broken conjunction is *closed* — and closed items stop generating write-ups. So the selection filter is "did this leg change the score?", and in a bear book the legs that fail to change a bear score are disproportionately the bull-side ones. The ledger ends up holding the half of a two-sided test that agreed with you, **assembled entirely by correct individual decisions.** No step in the chain is wrong; the aggregate is biased. This is the mirror of refusing to score silence as vindication: there, an absent datum was wrongly read as support; here, a present datum is never read at all.

**How to apply:** (1) **when a conjunction resolves NOT-MET, explicitly log every other leg's actual result before closing the row** — its score is void, its evidence is not; (2) at any pre-registration with ≥2 legs, write the disposition instruction into the row itself ("on a broken conjunction, record the surviving legs' prints"), because the row is the only thing still being read when the break happens; (3) audit for this by direction — count how many recorded resolutions ran WITH your thesis versus against it, since the failure mode produces a ledger that looks diligent and reads one-sided; (4) route the surviving leg to whatever dated decision it genuinely informs rather than scoring it ad hoc — evidence that arrives outside a scoring window is an INPUT to the next committed decision, not a licence to re-mark early. Related: [[finding_count_what_published_before_reading_the_verdict]], [[finding_compound_gate_jointly_unsatisfiable]], [[finding_enumerated_mechanism_test_hides_a_completeness_claim]], [[finding_ledger_drift_behind_narrative]].
