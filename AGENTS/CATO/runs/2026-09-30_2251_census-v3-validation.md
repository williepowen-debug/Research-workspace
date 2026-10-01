# Critic census v3 — bounded artifact validation

## Current assessment

**Approved repair completed (September 30):** [v4 and reproducible outputs](2026-09-30_2251_census-v4/README.md) separate probability vintages, recover predecessor/archive history, and honor inspected exclusions. All 534 original keys retained; 19 author tests pass. On the same 125 rows, current-cell Brier is **0.2463568**, earliest-candidate Brier **0.2546672**, and the in-sample baseline **0.249216**. These remain descriptive sensitivities, not verified registration-time performance. Recommend stopping broad historical reconstruction and using a small explicitly defined cohort for the next measurement step. Will subsequently authorized the fixed twelve-case feasibility pass; it is now [complete with separate case evidence](2026-09-30_2355_cohort-feasibility/REPORT.md). No broader backfill authorized. Original validation below remains historical evidence.

**The supplied outputs reproduce exactly, but v3 is not a validated measure of fleet forecasting performance or published-score inflation.** Repair the existing extraction before using its rankings or its apparent crossing of the baseline. Three material defects are demonstrated: current confidence is labelled as the probability actually scored; the historical lookup misses recoverable earlier values and can prefer an archive over older live history; explicit calibration exclusions are ignored.

This is useful, inspectable work. Its mutually exclusive counts reconcile and the BOND rotation recovery is real in the checked population. Those strengths do not certify the scoring inputs. No replacement fleet performance number is offered: the bounded sample establishes defects, not their complete net effect.

**Assignment:** Will supplied four downloaded files after the discussion about whether the system is working. Validate their reproducibility and the identified scoring/history/population concerns. Stop after evidenced, actionable dispositions; no new fleet-wide reconstruction or owner-policy implementation commissioned.

**Scope and pin:** critic pin `e70f558f4ad685cec394a9cdc2ef6ee622d6b6e0`; its cutoff is explicitly `2026-10-01`. Live checkout at review start `dc27d3c252184ccc1f77cd0931f5ecf476f1a867`, clean working tree/staging. All substantive source witnesses below use Git objects at the critic pin or named ancestors, not changing owner files. Only CATO evidence and continuity written. No external source verification, grading-policy changes, owner edits, sends, agent launches, or publication.

## Preserved inputs and reproduction

The supplied files were copied byte-for-byte from `/mnt/c/Users/willi/Downloads/` into [the evidence directory](2026-09-30_2251_census-v3-evidence/). [SHA-256 manifest](2026-09-30_2251_census-v3-evidence/source-manifest.json) records each source and hash. Originals:

- [census_v3.py](2026-09-30_2251_census-v3-evidence/census_v3.py)
- [rows_v3.tsv](2026-09-30_2251_census-v3-evidence/rows_v3.tsv)
- [summary_v3.tsv](2026-09-30_2251_census-v3-evidence/summary_v3.tsv)
- [provenance_v3.txt](2026-09-30_2251_census-v3-evidence/provenance_v3.txt)

The original script defaults to moving `origin/master` and writes to the critic's hard-coded scratchpad. Reproduction supplied the full pin explicitly and changed **only OUT** to a temporary local directory. This was an execution adaptation, not a scoring repair. All three regenerated outputs are **byte-identical** to the supplied files; [receipt](2026-09-30_2251_census-v3-evidence/reproduction.json), [stdout](2026-09-30_2251_census-v3-evidence/replay-stdout.txt).

Independent checks: [validate_v3.py](2026-09-30_2251_census-v3-evidence/validate_v3.py), [full selected source witnesses and calculations](2026-09-30_2251_census-v3-evidence/validation.json). Run from the Git root with `python3 -B AGENTS/CATO/runs/2026-09-30_2251_census-v3-evidence/validate_v3.py`; add `--replay` to repeat the original census with the OUT adaptation. Both default validation and the portable wrapper's full `--replay` passed, including byte comparisons; the original full replay was also run separately before writing the wrapper. Tests authored by CATO independently of the supplied census; no claim of external forecast-outcome verification.

**Count reconciliation confirmed:** 534 distinct `(desk, ID)` rows; 235 extracted as scoreable, 299 excluded: 91 open/not due, 36 open/overdue, 38 open/undated, 80 classified as terminal/non-binary, 54 without a numeric current probability. These are correct counts of the script's categories, not certification of those categories.

| Calculation from supplied rows | n | Brier | In-sample baseline | Skill versus that baseline |
|---|---:|---:|---:|---:|
| Current cells, entire extracted scored set | 235 | 0.2420996 | 0.2498868 | +0.03116 |
| Current cells, matched history subset | 234 | 0.2415957 | 0.2498356 | +0.03298 |
| Purported first probabilities, same matched subset | 234 | 0.2532880 | 0.2498356 | −0.01382 |

The single scored row without numeric first history is **ZHAO ZHA-08**, not an unexplained arithmetic loss. Comparing the matched 234 rows avoids the slightly different populations in the headline. The baseline is descriptive and computed from this sample's outcomes; mixed horizons/questions, correlated events, uncertain outcome validity and incomplete original histories still prevent interpreting these figures as demonstrated skill or lack of skill.

## CV1 — HIGH: current cells are mislabelled as probabilities actually scored

**Evidence:** the population loop assigns `p_scored = conf(current Confidence cell)`. It never extracts the probability actually used in a recorded grade. The provenance states that definition correctly, but the column names and the critic's narrative imply recorded scoring.

| Witness at the pin | Census calculation | Recorded owner grade |
|---|---|---|
| OTTO-32 | Current cell 97%; `brier_scored=0.0009` | Result explicitly says **0.0225 counted**, from original 85%; it expressly says 97%'s 0.0009 was **not used**. |
| OTTO-29 | Current cell 80%; `brier_scored=0.6400` | Result explicitly says original 75%; **0.5625 counted**. Its evidence was updated before this pin. |
| OTTO-04 | Current cell 62%; `brier_scored=0.3844` | Notes explicitly direct scoring at 75%, not 62%. Separate “no calibration credit” language needs an eligibility disposition; a binary Status alone cannot settle it. |

Sources: `e70f558f4:AGENTS/OTTO/thesis/PREDICTIONS.tsv`, exact rows preserved in validation.json; the owner's 9/30 correction table in `thesis/PREDICTIONS_ARCHIVE.md` explicitly distinguishes as-made scores from walked cells not used. The census's raw current-cell comparison can be a useful sensitivity analysis. It **does not establish inflated published/recorded scores**.

**Recommended correction:** retain separate fields for current confidence, recorded grading probability and earliest recoverable probability, each with provenance. Where recorded grading probability cannot be established, mark it unknown; do not substitute a current cell silently. Rename the existing current-cell statistics accordingly. Preserve all originals and owner's terms; this recommendation authorizes no change to desk grades.

**Closure:** OTTO-32 and OTTO-29 reproduce their actual recorded scores in a recorded-grade view, while the current-cell view remains separately identifiable. No claim about actual score inflation rests on the latter alone.

## CV2 — HIGH: “first committed” is not the earliest recoverable desk history

The history loop visits current retained paths and current LIVE paths, ordered by filename, and stops once a `(desk, ID)` is found. It does not follow predecessor paths or compare candidate dates across files. These are implementation defects in addition to the disclosed genuine possibility that a first recorded value postdates registration.

**Recoverable predecessor values missed:**

| Prediction | v3 purported first | Earlier Git evidence available in this repo |
|---|---|---|
| OTTO-05 | 48%, June 9, `65b899ca4` | **60%, March 4**, `91c301279:AGENTS/OTTO/workbook/PREDICTIONS.tsv`, original OPEN row. |
| OTTO-29 | 80%, June 9, `65b899ca4` | **75%, April 15**, `0bc51c74d:AGENTS/OTTO/workbook/PREDICTIONS.tsv`, original OPEN row. |
| OTTO-30 | 45%, June 9, `65b899ca4` | **60%, April 15**, the same predecessor ledger at `0bc51c74d`. This establishes an earlier value; it does not settle all owner claims about its original probability. |

The June 9 date is a thesis-directory migration. These histories are recoverable; they are not missing from Git. A first-file warning does not make the June value a registration-time probability.

**Archive order can beat chronology:** VULCAN-01 is reported first seen at `28f74d735`, September 6, in a resolved archive. It already appears in the live ledger at `c5c055f82`, July 10, OPEN. The archive path sorts before the workbook path; the unconditional “key already in first → skip” preserves the later record. VULCAN uses tiers and contributes no numeric score here, so this witness proves the provenance algorithm's defect, not a numerical change to its score.

**The file-birth flag is also unreliable:** BND-01 reports `first_commit_sha=38812f895` and flag 0. That is the birth commit of the **source** thesis ledger, June 15; the row existed in its predecessor workbook even before that. The flag compares the first date with the birth of the row's **current archive** (September 1), rather than the path where the first value was found. Comparing dates rather than exact commits adds another ambiguity. Therefore the reported 195 file-birth rows is not a validated boundary around suspect provenance.

**Recommended correction:** recover predecessor file lineage; compare all relevant candidate appearances chronologically with original claim identity checked; retain the exact source path/commit of each probability. Determine file-birth uncertainty from that source commit. Mark genuinely unrecoverable registrations unknown rather than calling migrated values frozen probabilities.

**Closure:** the saved OTTO predecessor cases, VULCAN archive-order case and BND-01 flag case resolve correctly; ordinary unchanged-history cases still match; conflicted identities remain explicit. Then rerun the existing census. No complete corrected fleet result was computed in this bounded review.

## CV3 — HIGH: binary status is being used as calibration eligibility

At the pin, **OTTO-06 is explicitly NOT ELIGIBLE for calibration**, even though its observed panel result remains FALSIFIED. The row's Result states that the resolving clause was written after relevant data were visible and that Brier 0.4900 is shown but **not counted**. V3 nevertheless includes it in both aggregates because its status is binary and its confidence is numeric.

This is not stale-checkout behavior: the exclusion instruction is in the exact pinned source. OTTO-10's NEEDS_VERIFY transition was recognized as unscored, but the retained FALSIFIED label on OTTO-06 defeats the status-only rule. The owner's corrected 9/30 set contains two eligible rows, OTTO-29 and OTTO-32; v3 scores three and uses different probabilities for two of those three. The owner's recorded two-row mean is not a defensible fleet-skill statistic either; its own disclosure says so and notes that removing misses improves the remaining mean.

**Additional category counterexamples within the same extraction:**

- OTTO-10's NEEDS_VERIFY is put in “terminal_non_binary,” even though verification is pending. Unscored is correct; terminal is not.
- MARCO/TOURISM TOUR-02 and TOUR-04 have six fields under a seven-field header. V3 silently reads `2026-05-31` as their status and calls them terminal/non-binary. These are malformed source rows requiring a schema/owner disposition, not unfamiliar outcome tokens. Do not automatically reclassify them as hits from nearby prose.
- The stored OTHER rows contain **48 distinct status strings**, not twelve. The script prints only `most_common(12)`; the narrative treated that display limit as the full diversity.
- `outcome_raw` is truncated to 80 characters and Notes are omitted. The exported row alone therefore cannot expose many qualifications the critic said could be challenged from its raw text. Source path/ID enables a lookup, but the export is an excerpt.

**Recommended correction:** validate row shape before classification; distinguish pending verification, ungradeable outcomes and explicit calibration ineligibility; honor recorded eligibility with an evidence pointer, leaving disputes visible. Preserve full relevant source fields or provide a lossless source lookup. Outcome verification remains separate from extraction correctness: an owner's eligibility label is an input to inspect, not independent proof that the forecast is scientifically valid.

**Closure:** OTTO-06 is visible as an excluded observed result, OTTO-10 as pending verification, and malformed TOUR rows as schema errors; every exclusion remains reconcilable. No unreviewed heuristic converts these cases into binary scored outcomes.

## What can be retained

- **Reproducibility:** exact outputs and reconciled mutually exclusive counts verified under the explicit pin and OUT adaptation.
- **BOND population repair:** 31 extracted IDs: two open, one VOID, 28 binary (15 TRUE, 13 FALSE). Archive samples BND-01, BND-18 and BND-29 match their pinned numeric cells/statuses. This supports the explanation of the earlier population error. It does not independently validate all 28 outcomes, original probabilities or the +0.15 skill claim.
- **OTTO follow-through:** pinned artifacts now record OTTO-10 pending verification, OTTO-06 ineligible and fuller evidence for OTTO-29. That changes the source record the census should consume. The new court/economic source material was not independently reverified in this assignment; no blanket closure of the earlier external-evidence review is implied.
- **Research conclusion:** real research and useful controls can coexist with an unvalidated fleet-performance measure. V3's failure to measure actual recorded grades is not evidence that the system has skill, and its near-baseline outputs do not establish that it lacks skill.

## Delivery and resume

This original validation disposition is superseded by the approved repair below.

Recommended next work is a bounded correction to this existing census covering CV1–CV3, followed by the saved witnesses and one pinned rerun. Do not commission a new scoring framework or alter desk probabilities merely to make the export easier. No corrected fleet ranking, capital decision or desk-closure decision follows from this review.

**CATO assignment complete on delivery.** Original critic artifacts remain unchanged, copied and hashed in CATO's report directory; validation code and evidence are CATO-authored. No critic/system implementation was performed. Resume: orient and await Will. Routine delivery checks and Git receipt are recorded below/in-session.

Delivery checks: source-copy SHA-256 verification and local Markdown links passed; root weekday check passed for DOCKET/GATES/WILL_QUEUE; CHARTER/CONTINUITY/local AGENTS remain below the 32,550-byte startup cap by direct measurement. No STATUS, canonical metric or auto-memory was changed, so consumer/ledger/memory checks were not triggered. The orphan advisory found concurrent `PROME/tools/board_scan.py` work, not CATO-authored; left untouched and disclosed to Will. Exact-path CATO delivery only. No hosted publication attempted; fresh-fetch push receipt in-session.

Whitespace inspection: `git diff --cached --check` returns 2 solely for preserved tabular output: 535 rows-file flags and 41 summary-file flags (original CRLF/tabular formatting), plus five replay-stdout rows with empty trailing TSV fields. Retained deliberately for byte identity and field preservation; CATO-authored report/validator and other evidence files have no whitespace flags. This is formatting residue, not a failed computational check.

## September 30 — approved bounded repair

Acceptance conditions, recorded before implementation:

- Preserve original files/hashes, the 534 `(desk, ID)` population and exact pin. Read Git objects so concurrent workspace edits cannot change results. No owner edits or messages.
- Separate current-cell, explicitly recorded grading and earliest recoverable ledger probabilities. Unknown grading probability stays unknown. Evidence annotations name exact sources and fail if those sources change.
- Search predecessor/archive paths chronologically, retain source commit/path, and compute file-birth uncertainty from that source. Detect claim/identity differences and same-ID conflicts; never borrow a different desk's row. Unknown registration remains unknown.
- Preserve full source fields. Flag malformed TOUR rows, pending OTTO-10 and excluded OTTO-06. Reconcile exclusions; reproduce OTTO-29/32 recorded grades and the saved OTTO/VULCAN/BOND history cases.
- Test ordinary histories, moves, duplicates, wrong desk, absent/invalid probabilities, changed claims, explicit exclusions and pending evidence. Synthetic history tests use isolated repositories. Tests are author work, not independent review.
- Save a row comparison and pinned rerun with separate denominators for every view. Stop after repair and limits; no new framework, external outcome audit, capital decision or desk ranking.

### Implementation and closure

Will's direct approval was “ok approved go ahead,” following the recommendation to repair the three demonstrated extraction defects and stop after a pinned comparison. Starting shared HEAD was `0b506c77f`; all analytical source reads remained pinned to `e70f558f4`. No owner edits, sends, launches, new fleet requirements, external outcome reads or hosted publication. Concurrent PROME/CREED edits were left untouched. CATO authored the implementation and tests: this follow-up is author repair/verification, not independent review.

**CV1 implemented/tested:** `p_current`, `p_recorded_grade` and `p_earliest_observed` are separate. Twenty-five explicit grading probabilities were transcribed from inspected source statements, not inferred from current cells. Each annotation has the exact source path, full-file SHA-256 and supporting quote; a changed source/quote, out-of-range value or contradictory annotation fails. Fifteen of those rows have an extracted binary outcome and no recorded exclusion. OTTO-29 now gives 0.5625 at 75%; OTTO-32 gives 0.0225 at 85%. OTTO-04's 75% instruction is retained alongside its explicit no-calibration-credit disposition, so it contributes no score. Seven formerly scored cells beginning `SCORE AT` move out of the current-belief view and remain in the recorded-grading view. No uninspected row is assigned a grading probability by default.

**CV2 implemented/tested:** historical prediction-ledger paths reachable from the pin are searched, including deleted workbook/root predecessors. Ancestry precedes path sorting; same-commit ties prefer an established file, then LIVE, and disagreements stay flagged. Exact source path/commit and source-file-birth commit are retained. The chosen first commit changes for **145 rows**; the earliest numeric candidate changes for **17 rows** (full list in checks.json). OTTO-05 recovers 60%, OTTO-29 75%, OTTO-30 60%; VULCAN-01 moves back to July 10; BND-01 moves back to the March 27 workbook and is correctly flagged as already present at that source's birth. OTTO-30's owner-specified grade remains 65%, separate from the recovered 60% candidate; no forced reconciliation or probability overwrite.

The prior OTTO-05 witness itself has eight fields under nine historical headers. **121 earliest rows have a field-count mismatch**. V4 retains their numeric-slot candidate and original fields but excludes them from history scoring. Claim, made-date, window and resolution/invalidation text differences also cause exclusion from the historical view. This catches the unchanged-title/different-window problem (for example CRL-07's May–June versus June–August window), at the cost of also excluding benign formatting and archival-pointer changes until someone checks semantics. Same-commit copies with different specification text remain contested rather than resolved by a filename. These limits are data dispositions, not grounds to manufacture original forecasts.

**CV3 implemented/tested:** current schema errors, pending verification and explicit ineligibility are separate from non-binary/unknown status. OTTO-06 is excluded; OTTO-10 is pending verification; TOUR-02/04 are schema errors. The inspection also found BRENT's file-header exclusion of BRT-06, which v3 counted. Source statements for these and other explicit unscored rows are preserved in annotations; no broad keyword heuristic treats a conditional exclusion or another prediction's mention as this row's disposition. Full current cells and all first-path candidates are saved in JSONL, including Notes; every row is traceable to a Git blob. Unknown eligibility remains UNKNOWN even where a sensitivity can be calculated.

### Pinned results and interpretation

All metrics below use probability fractions 0–1. Each baseline is that row set's realized base rate times one minus the base rate, not an ex-ante benchmark. Distinct denominators mean the top rows are **not** an apples-to-apples forecast-skill comparison.

| View | n | Brier | Its in-sample baseline |
|---|---:|---:|---:|
| Original v3 current cells | 235 | 0.242100 | 0.249887 |
| Original v3 purported first probabilities | 234 | 0.253288 | 0.249836 |
| V4 current-cell sensitivity | 225 | 0.232909 | 0.249402 |
| V4 earliest candidates, passing structural/identity checks | 130 | 0.263868 | 0.249763 |
| **Same 125 rows: current cells** | **125** | **0.246357** | **0.249216** |
| **Same 125 rows: earliest candidates** | **125** | **0.254667** | **0.249216** |
| Inspected owner-specified grading subset | 15 | 0.363113 | 0.195556 |

The last row is a deliberately selected subset rich in explicit scoring corrections, **not a representative estimate of fleet performance**. The 25 specified values include still-open instructions; only 15 contribute to this descriptive resolved view. The decrease from 235 to 225 current-cell rows is exactly three recorded exclusions (BRT-06, OTTO-04, OTTO-06) plus seven scoring-instruction cells. It is not evidence that forecasts improved. The matched 125 rows remove probability-view denominator differences, but **six were first seen non-OPEN and 15 were already present at source-file birth** (flags may overlap). They still cannot be described as verified original forecasts. No row's `p_registration` is certified by this pass; UNKNOWN there means validation not performed, not proof that recovery is impossible.

The 534 population dispositions reconcile: 225 binary/current numeric; 36 binary/no current numeric; 90 open/not due; 36 open/overdue; 38 open/undated; 53 explicitly ineligible; 53 non-binary or unknown status; two schema errors; one pending verification. View-specific probability availability and historical uncertainty are separate fields, so a row need not participate in every numerical view. The original 534/235/299 figures remain the preserved v3 output, not silently replaced counts.

**Remaining limits:** source annotations are a bounded inspected set, not a general prose grader; untouched eligibility is unknown. Status/outcome and due-date parsing otherwise retain v3's heuristics. Historical search covers prediction TSV names under their recorded desk identity, not every STATUS/Markdown document, arbitrary filename or owner rename. Differences in claim/specification text are not semantically adjudicated. No external outcome validation, independent forecast baseline, uncertainty interval, dependence adjustment or comparable-horizon cohort was supplied. None of the averages establishes advantage, absence of advantage, deliberate score inflation or a basis for closing a desk.

### Verification and stopping decision

[19 author tests](2026-09-30_2251_census-v4/test-results.txt) pass: source-bound annotations, malformed/long rows, missing/invalid/tier probabilities, instruction versus live value, exclusions/pending evidence, moved/deleted files, wrong desk, duplicate/conflicting IDs, changed windows/resolvers, dirty-working-tree isolation, and pinned OTTO/BOND/VULCAN/TOUR witnesses. Synthetic Git histories live only in temporary directories. Separate [Decimal checks](2026-09-30_2251_census-v4/checks.json) independently recompute all fleet-view arithmetic, verify the fixed 534-key population, exclusion treatment, probability bounds and script/input hashes. Original v3 source hashes remain unchanged.

The tests initially exposed two handling details that were repaired: a malformed historical row must retain its observed probability candidate while remaining unscored; same-commit identical copies should prefer the established ledger rather than an archive's filename. A final related-case check added window/resolver-text differences to the history exclusion conditions. Final artifacts come from the last pinned rerun; no earlier intermediate output is published as final.

**Return and stop:** the repair produces traceable rows and demonstrates that the v3 fleet verdict was not warranted. It has not demonstrated forecasting or trading benefit. Broad historical reconstruction would now require semantic and outcome adjudication, beyond another parser patch. Stop this assignment. Recommend a small explicitly defined cohort with verified registration, resolution evidence and an ex-ante benchmark; use a prospective cohort if the chosen historical records cannot support it. No further implementation or cohort study is implicitly approved.

Delivery checks: root orphan advisory identified concurrent non-CATO work, left untouched and disclosed to Will; root weekday check passed. No STATUS or auto-memory edits, no canonical owner metric overwritten, and no old numerical claim silently superseded: v3 remains historical and v4 views have separately named populations. Accordingly ledger/memory/consumer-update checks are not triggered. Local report/README links, source/code hashes and startup-byte limits passed (CHARTER 9,921; CONTINUITY 13,130; local AGENTS 4,278 bytes). Exact CATO working-tree/staged whitespace checks passed. The full-tree diff also flags trailing empty TSV fields in concurrent PROME ORCH_LOG work; left untouched. Exact-path commit and fresh-fetch delivery receipt are reported in-session; no independent-review or hosted-publication claim.
