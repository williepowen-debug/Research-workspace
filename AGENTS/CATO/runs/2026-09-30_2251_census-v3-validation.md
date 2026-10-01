# Critic census v3 — bounded artifact validation

## Current assessment

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

Recommended next work is a bounded correction to this existing census covering CV1–CV3, followed by the saved witnesses and one pinned rerun. Do not commission a new scoring framework or alter desk probabilities merely to make the export easier. No corrected fleet ranking, capital decision or desk-closure decision follows from this review.

**CATO assignment complete on delivery.** Original critic artifacts remain unchanged, copied and hashed in CATO's report directory; validation code and evidence are CATO-authored. No critic/system implementation was performed. Resume: orient and await Will. Routine delivery checks and Git receipt are recorded below/in-session.

Delivery checks: source-copy SHA-256 verification and local Markdown links passed; root weekday check passed for DOCKET/GATES/WILL_QUEUE; CHARTER/CONTINUITY/local AGENTS remain below the 32,550-byte startup cap by direct measurement. No STATUS, canonical metric or auto-memory was changed, so consumer/ledger/memory checks were not triggered. The orphan advisory found concurrent `PROME/tools/board_scan.py` work, not CATO-authored; left untouched and disclosed to Will. Exact-path CATO delivery only. No hosted publication attempted; fresh-fetch push receipt in-session.

Whitespace inspection: `git diff --cached --check` returns 2 solely for preserved tabular output: 535 rows-file flags and 41 summary-file flags (original CRLF/tabular formatting), plus five replay-stdout rows with empty trailing TSV fields. Retained deliberately for byte identity and field preservation; CATO-authored report/validator and other evidence files have no whitespace flags. This is formatting residue, not a failed computational check.
