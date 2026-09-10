---
name: finding_confidence_walk_is_selected_for_on_the_rows_that_carry_the_most_brier_weight
description: Re-pricing a live prediction overwrites its as-made confidence; the rows re-priced are the hardest ones, so the walk lands exactly where Brier weight is heaviest and always flatters.
symptoms: "our Brier looks fine", "as-made vs current confidence", "the ledger says 20% but STATUS said 90%", "confidence column was walked down", "prediction re-priced before it resolved", "scoring vintage", "calibration audit came back clean"
metadata:
  type: feedback
---

**A prediction ledger that stores ONE confidence per row does not store the as-made value — it stores the LAST value, and scoring against it flatters the desk. The bias is not random, because the rows that get re-priced are selected.**

CARL, 2026-09-10, on DAEDALUS's fleet as-made audit (LABOR hit the same thing first: Brier **0.299 → 0.342** on 4 of 12 scored rows).

Ten CARL ledger rows had lost their as-made confidence. Four were **RESOLVED**, so their Brier vintage changed — and **all four moved the same direction, worse**:

| row | outcome | scored at | as-made | ΔBrier |
|---|---|---|---|---|
| CRL-03 | MISSED | 0.72 → .5184 | **0.90 → .8100** | **+0.2916** |
| CRL-06 | CONFIRMED | 0.78 → .0484 | 0.70 → .0900 | +0.0416 |
| CRL-11 | MISSED | 0.83 → .6889 | 0.85 → .7225 | +0.0336 |
| CRL-04 | CONFIRMED | 0.98 → .0004 | 0.88 → .0144 | +0.0140 |
| | | | **sum** | **+0.3808** |

🔑 **The mechanism is entirely benign, which is why nobody catches it.** A desk re-prices a live prediction as evidence arrives — correct behaviour, the thing a calibrated forecaster is supposed to do — and writes the new number into the confidence cell. Nothing is concealed and no one is careless.

⛔ **But the walk is SELECTED FOR.** A prediction that was easy and stayed obvious is never re-priced; its cell still holds the as-made. **The row that got re-priced is the row that was hard, contested, and moved a lot — and that is precisely the row carrying the most Brier weight.** So the corruption is not spread evenly over the ledger; it concentrates on the rows that decide the score. CRL-03 alone is +0.29.

⛔ **And it flatters in BOTH directions, so "the errors cancel" is false.** On the two CONFIRMED rows the stored value sat **above** the as-made (98 vs 88, 78 vs 70); on the MISSED row it sat **below** (72 vs 90). Walking *up* toward a hit and *down* away from a miss are the same reflex — track the evidence — and both shrink the loss. **Do not assume the drift is mean-zero. It has a sign, and the sign is toward looking good.**

✅ **The fix is a column, not a discipline.** Store `as_made_confidence` **immutably** at registration and re-price in a **separate** cell or an append-only chain (`X% [date] (was Y% [date])`). CARL's ledger already had that chain form, and **five of the audit's eighteen flags were the chain working exactly as designed** — the audit tool just read the first percentage and skipped past the history. **A ledger with the chain is auditable; one without it cannot reconstruct the as-made at all** once the STATUS history is gone.

⚠️ **Recovering an as-made is not always possible, and saying so is part of the job.** Three of CARL's ten rows had a `Date_Made` that *precedes* the prediction's first appearance in STATUS, so the earliest recoverable figure is **EARLIEST RECORDED, not as-made**. They were labelled that way in the cell rather than promoted. **Collapsing "recovered" into "proven" is how a calibration audit launders its own uncertainty** — the audit then reports a precise Brier built partly on guesses.

⇒ **Supply corrected INPUTS to whoever owns the scoreboard; do not recompute the aggregate yourself.** The desk whose score is being corrected is the worst-placed party to compute the correction.

Related: `[[finding_instrument_reports_clean_against_the_wrong_reference]]` (the audit tool's own third limit — an ID can be reassigned to a different claim) · `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]` · `[[finding_confidence_priced_against_thesis_not_letter]]`.
