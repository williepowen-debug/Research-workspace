# Acceptance — the forecast scorer reads three ways desks state a probability that it skipped, 2026-11-20

reads: 1 of 3 (one result read; no plan read)

Authority: DOCKET L1168 (the outside audit's scorer repairs, Will 2026-11-16) and its notes of 11/19 (WATT) and 11/20 (the reader of the L1188 listing). Taken as the next step inside that approved repair (done-without-asking class C11); the effect on the fleet score is measured and reported to Will the same day. A new episode: the 11/17 repair's acceptance file said probability parsing was unchanged, and this changes it.

Defect, checked at the code and the ledgers on 2026-11-20 before writing this: `prob()` in `PROME/tools/forecast_report.py` returns "no probability" for calls whose desk plainly stated one.
- D1. A confidence cell holding only a decimal (`0.40`). HENRY writes its 11/2026 calls this way: HEN-60 to HEN-64, two of them decided.
- D2. A confidence cell holding a confidence TIER word, PROVISIONAL or ASSUMPTION, with the probability at the start of the prediction text as `P(TRUE) = 0.20` or `P(TRUE | a verdict) = 0.60`. The function stops at the tier word. VULCAN-188 to 194, two decided. VULCAN's and WATT's charters define these words as evidence tiers (EMPIRICAL / PROVISIONAL / ASSUMPTION), not as "do not score".
- D3. The same tier words with the prediction text opening `PROBABILITY 88%.` WATT-14 to 17, all open.
These calls are left out of the fleet score and, from today, listed as having no probability.

Written before any edit to the tool.

Properties:
1. Ordinary: `prob()` returns the stated value for D1 (the cell is a decimal above 0 and below 1 and nothing else), D2 and D3 (the tier word is PROVISIONAL or ASSUMPTION and the prediction text carries `P(TRUE...) = 0.x` anywhere, as the function already reads it for an empty cell, or OPENS with `PROBABILITY n%`).
2. Overlap:
   - UNSCORED, NOT SCORED, UNASSIGNED, `(unstated)` and a lone dash stay "no probability" whatever else the cell or the prediction text holds: those are the desk saying do not score (CARL's `NOT SCORED — NO-VERDICT ... (Was: 70%)` rows stay out);
   - a tier word with no stated probability in the prediction text stays "no probability" (MIDAS's and most of VULCAN's and WATT's tier rows);
   - after a tier word, a percentage elsewhere in the CONFIDENCE cell is not read (the cell's free text may hold other figures); only the two prediction-text forms are;
   - a percentage in the prediction text that is not the opening `PROBABILITY n%` is never read as the probability (thresholds such as "above 4.60%" stay thresholds);
   - a decimal of 0, 1 or more, or a decimal with other text in the cell, is not read by D1 (`0.40 (was 0.55)` is not this form);
   - every cell the function read before returns the same value as before: the 16 existing selftest cases, and on the live ledgers no row that had a probability changes it;
   - the same reading applies to every committed version in a row's git record, so first-logged values and timing classes for the newly read rows come from their own history.
3. Wrong owner: no desk ledger is edited; DAEDALUS's registry and scorecard are not edited. The tool reads.
4. Missing information: an empty confidence cell with no stated form in the prediction text stays "no probability". A stated value outside 0 to 1 is not a probability.
5. Concurrent activity: N/A, a read-only report.

The measured effect is part of the acceptance: the result section states, from two runs of the tool on the same commit, the scored count and fleet Brier before and after, and names every row whose reading changed.

Declared limits before the build:
- Only these three forms are added. Other unread cells (BROCK 6, FERT 10, VIOLET 10 and a few more on 2026-11-20) are not examined here.
- Whether a desk MEANT a tier-word call to be scored is read from its charter's definition of the tier words, not asked of the desk. HENRY, VULCAN and WATT are told by packet at their next wake.
- Report 1 is not re-run (Will 2026-11-05). The change shows in report 2 (12/04).

## Result and disposition 2026-11-20 13:37 ET (WQ-229 states)

IMPLEMENTED · TESTED (selftest PASS, 22 new cases) · INDEPENDENTLY VERIFIED by one Opus reader from the data, with both versions of `prob()`: over the 669 live rows, 15 change, all from no probability to the value the desk wrote (HEN-60 to 64, VULCAN-188 to 191, 193, 194, WATT-14 to 17), no other row changes and no row that had a value changes it; over 1,027 distinct confidence and prediction pairs in every committed version, none that read a number reads a different one or none · STILL UNRESOLVED: the residue below. Nothing was changed after the read.

Measured effect, two runs on one commit (the reader's and the author's agree): decided calls scored 291 to 295 of 375; fleet Brier 0.227 to 0.226; timing class BEFORE 35 to 39; the no-probability listing 3 calls to 0. The four newly scored decided calls, each checked by the reader at its ledger row: HENRY HEN-60 HIT at 0.50, HEN-62 HIT at 0.60, VULCAN-188 HIT at 0.60, VULCAN-191 MISS at 0.35.

Declared residue (reader's flags, all on made-up inputs with no instance in any ledger or its history; none fixed):
- A tier word FOLLOWED by a do-not-score word (`PROVISIONAL UNSCORED`, `ASSUMPTION — NOT SCORED`) with a stated probability in the prediction text is read. Property 2's first bullet holds only when the cell STARTS with the do-not-score word.
- A bare decimal cell now wins over a `P(TRUE) = x` in the prediction text (`0.40` with `P(TRUE) = 0.70` read 0.7 before, 0.4 now). The "every earlier value unchanged" bullet holds on all real data, not on this form.
- After a tier word, `P(TRUE) = x` is read anywhere in the prediction text and wins over an opening `PROBABILITY n%`; a prediction text that quotes an earlier call's `P(TRUE)` would be read as this call's.
- `PROBABILITY 100%` reads as 1.0 while a bare `1.0` cell is not read.
- HEN-60 now appears under LOOK because its outcome note names the start of a 200-session window (2026-02-03); a prompt, a false one here.
- Not tested: the `--sample` and `--write` paths, ledgers outside the registry.
