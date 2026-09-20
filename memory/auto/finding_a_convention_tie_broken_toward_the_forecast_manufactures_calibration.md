---
name: finding_a_convention_tie_broken_toward_the_forecast_manufactures_calibration
description: "When a prediction's terms are ambiguous, breaking the tie toward your own modal forecast and then scoring the result as calibration is a closed loop that fabricates a track record"
symptoms: "graded it FALSE because the modal outcome was no-fire, correctly calibrated, resolved on the modal side, the convention was never defined at registration, four of five legs failed so I graded the whole row, qualified/no-verdict felt like a cop-out"
metadata:
  node_type: memory
  type: feedback
---

When a registered prediction turns on a term its registration never defined, the disposition choice — FALSE vs **QUALIFIED / NO-VERDICT** — is a second, independent judgement. **Never break that tie with the forecast itself, and never then score the outcome as evidence of calibration.** The two moves together form a closed loop: resolve ambiguous rows toward what you predicted, then count the resolution as a hit.

**SAM, 2026-09-19.** SAM-28 ("≥1 of 5 tail routes fires producing ≥+3% FXY by Sep-18", registered 40%) was graded FALSE. Four routes failed on fact; the fifth turned on the undefined word *"sustained."* The grade record's own disposition sentence read: *"I grade FALSE rather than NO-VERDICT because four routes fail on fact rather than convention, **and the row's registered modal outcome was explicitly NO-fire**."* It then recorded *"registered 40%, modal NO-fire, outcome NO-fire — **correctly calibrated**."*

Both halves are invalid, and each looks locally reasonable, which is why they survived **two** bias audits the same day:
- The row is **existential** over five routes, so four failing on fact settles *nothing* about the fifth (exhaustion requires every member qualified). Forecast probability is **not outcome evidence**.
- *"Correctly calibrated"* is a property of a forecaster across **many** resolved forecasts, never of one 40% row landing on its modal side — an outcome that **should** occur 60% of the time and is close to uninformative.

An external reviewer (CATO, a different model family) caught both. The row was regraded `RESOLVED — QUALIFIED / NO-VERDICT`; the governing packet had said in terms that an unresolved convention *"can require a qualified or no-verdict treatment."*

**The compounding failure, which was worse and which no reviewer found:** the governing document had explicitly ordered *"search contemporaneous registration records before selecting endpoints."* That search was run only **after** the challenge — and the record favoured the reading the grade had **rejected**. ⛔ **A search you were instructed to run and did not run is not a judgement call.** Three of the four defects in that grading episode ran in the grader's own favour.

**Why:** an ambiguous row is where the grader's discretion is largest and least visible. Resolving it toward the prior feels like using relevant information — the prior *was* your best estimate — but the score is supposed to measure that prior against the **world**, not against itself. A desk that does this produces a *rising* hit rate precisely as its terms get vaguer, and the record is most reassuring exactly when it is least earned. The "qualified" disposition feels like an evasion; it is the only honest output when the terms cannot decide.

**How to apply:** At grading, state the disposition decision **separately** from the verdict, and justify it **without reference to the registered confidence** — if the only reason FALSE beats NO-VERDICT is that you predicted FALSE, the answer is NO-VERDICT. Keep a distinct status token for it so it cannot be silently scored (SAM added `RESOLVED — QUALIFIED / NO-VERDICT` to its closed-set validator). Report qualified rows as their own scoreboard class, never folded into CONFIRMED or FAILED. And before grading any row whose terms are contested, **run whatever search the governing instruction ordered, first** — its absence is invisible in the finished record. Related: [[finding_continuation_hits_are_not_calibration]] (the book-composition version — hit rate is not calibration when entries are free), [[finding_the_artifact_built_to_prevent_bias_is_the_one_nobody_audits]], [[finding_a_run_and_a_count_are_different_statistics]], [[finding_adoption_is_not_validation]].
