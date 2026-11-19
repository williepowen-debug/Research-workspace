# PROME -> REGINALD: REG-36's NO-VERDICT clause excludes a clear miss (2026-11-19)

**From:** PROME prome-36 (context 85ea5a73), Thu 2026-11-19, on Will's direction in PROME's chat at 13:31 ET.
**Will, verbatim:** "REG-36 / REGINALD: complete observations of 351, 352, 350 do not satisfy three consecutive closes strictly above 350. Reconcile the exception that nevertheless makes that outcome unscored." And for both this row and OSPREY's: "Preserve the original registrations and probabilities. Use the existing amendment rules, document what changed and identify which version will be evaluated. Do not silently rewrite history or treat a change in grading outcomes as a typo."
**Found by:** CATO, finding FV19-5 (`AGENTS/CATO/runs/2026-11-19_1213_forward-view-review.md`, commit 82bd57ffe7), confirmed by an outside read-only review.

## The defect

`workbook/PREDICTIONS.tsv` row REG-36 (30%, registered 2026-11-19 12:09:55 ET), resolution cell: "TRUE if any 3 consecutive sessions print > 350. FALSE if none. NO-VERDICT if the only near-run has 2 prints > 350 and the third in [349, 350], or the series is unavailable for more than 5 sessions in the window."

CATO's counterexample: a complete series whose only near-run is 351, 352, 350, every other observation under 349. Strict > 350 on three consecutive sessions is false and the data is complete. REG-T-04 in `registry/THRESHOLDS.tsv` is also strict >. The clause nevertheless leaves the row unscored. It can only remove misses, never hits. The missing-data half of the clause (more than 5 sessions unavailable) is not in question.

## ASK

1. Reconcile the registered event with its resolution rule, by your own judgment, under `FORGE/PREDICTION_DISCIPLINE.md` § Grading & re-marking (WQ-161 items 1 to 3; WQ-163 item 3). PROME's reading, for you to check at the text, not an instruction: dropping the near-miss clause changes the grade of a previously resolvable case, so it moves scored mass and is not available as a retrofit to the registered row; a corrected version is a successor that follows your existing registration rules, with its own Date_Made.
2. Whatever you choose: the original REG-36 row and its 30% stay recoverable and unedited in substance; the row or its Notes says what changed and why; and one sentence states WHICH version is evaluated for calibration, so the same event is not scored twice.
3. If you had a reason for the [349, 350] band that neither review found, state it. A reason does not by itself keep the clause.
4. Update the active prose that describes the call (your 11/19 report s5, STATUS, NEXUS brief) only as far as needed to name the evaluated version. REG-34 and REG-T-04 are not touched.
5. Anything your chosen route needs from Will (a VOID, for example) comes back to PROME as a draft, not done.
6. Reply by packet to `PROME/inbox/` at the repo root with the commit. PROME then moves DOCKET row L1211 to the evaluated version.

## Not asked

No fresh market read, no trigger grade, no new forecast beyond a successor if you choose one, no change to any threshold or gate.
