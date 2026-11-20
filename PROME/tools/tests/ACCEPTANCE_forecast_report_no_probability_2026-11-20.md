# Acceptance — the forecast report lists new calls logged with no probability, 2026-11-20

reads: 1 of 3 (one result read; no plan read)

Authority: WQ-716 (Will 2026-11-17 21:15 ET), DOCKET L1188 item 4: `PROME/tools/forecast_report.py` lists every call first logged on or after 2026-11-18 with no probability, by desk. A flag when the scorer runs; no rejection at commit.

Defect: a call logged without a probability can never be scored, and nothing shows the gap until the call resolves. Will's 11/19 words ask for forward views with probabilities where helpful; the report is where the fleet's unscorable new calls become visible.

Written before any edit to the tool.

Properties:
1. Ordinary: when the report runs with the git record, it prints one section listing, by desk in alphabetical order, each row whose call was first committed to a prediction ledger on or after 2026-11-18 and which carries no usable probability now. Open rows are included: that is the point. The section states its count, and says "none" when there is none.
2. Overlap:
   - a row first committed before 2026-11-18 is not listed, whatever it lacks;
   - a row with a usable probability now is not listed (the report's existing reading of the Confidence and Prediction cells decides "usable"; a range read as a midpoint counts as usable);
   - a row whose ID was reused for a different call is dated from the first committed version of the CURRENT call (the report's existing `current_call` reading), so an old ID given to a new call after the cut is listed and an old call is not;
   - a row with no committed version (written today, not yet committed, or the history is unreadable) cannot be dated: it is counted in one line as not dated and is not listed as new;
   - with `--no-history` the section says it was skipped and lists nothing;
   - every existing figure, table and line of the report is unchanged: the section is added, nothing is recomputed;
   - the report still exits 0 and edits no ledger.
3. Wrong owner: N/A as a test. The listing names desks and row IDs; it grades and scores nothing, and no desk's file is touched.
4. Missing information: a desk ledger with no Confidence column lists its new rows (no probability is no probability). A row with an empty ID is skipped as the report already does.
5. Concurrent activity: N/A, a read-only report.

Declared limits before the build:
- "First logged" is the first commit holding the call in a prediction ledger the report reads. A call stated earlier elsewhere reads later than it was; a ledger the report does not read is not seen.
- A probability written in a form the report cannot read counts as none and is listed.
- A listing is a prompt to the desk, not a defect in its work: some calls are deliberately unquantified (Will 11/19: no mandatory odds).

## Disposition 2026-11-20 13:31 ET (WQ-229 states)

IMPLEMENTED · TESTED (selftest PASS, four new cases; before the read the author found and fixed a dating error: rows in a ledger that gained its confidence column late were read as new, so the date is now the row ID's first appearance in any committed version) · INDEPENDENTLY VERIFIED by one Opus reader: every property it could test is met; the full report output differs from the committed version's by the new section only (4 added lines); its own scan of every tracked prediction ledger's git history found 9 IDs first appearing on or after 2026-11-18, the 3 listed and 6 with readable probabilities, none missed and none wrongly listed · STILL UNRESOLVED: the residue below. Nothing was changed after the read.

Declared residue (reader's flags, none fixed here):
- ⚠️ All 3 rows listed on 2026-11-20 carry a probability a person can read and the report cannot: HENRY HEN-64 (Confidence `0.40`, a bare decimal) and VULCAN-193 and VULCAN-194 (a tier word, ASSUMPTION or PROVISIONAL, in the confidence cell, with `P(TRUE) = 0.20` and `0.15` in the prediction text; the reading stops at the tier word). This is the declared limit "a form the report cannot read counts as none", and it is also a scoring gap: these calls would go unscored at resolution. It belongs to the scorer repair, DOCKET L1168, and is noted on that row. Until then the listing reads as "no probability the report can read".
- A reused row ID is not seen as a new call when neither the old nor the new call has a probability and Date_Made is empty or unchanged.
- An ID duplicated inside one ledger would be listed twice; no registry ledger has one today.
- Not tested: a commit late in the evening Eastern, a row moving between a live ledger and an archive after the cut, markdown ledgers, the `--write` path.
