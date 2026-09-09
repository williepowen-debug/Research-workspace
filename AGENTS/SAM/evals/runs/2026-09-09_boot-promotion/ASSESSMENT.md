# Boot promotion decision — September 9, 2026

**Do not promote.** Two actual fresh-session rounds failed Case 02. The original live `CLAUDE.md` was restored byte-for-byte after the separate orientation acceptance check. Both trial surfaces, inputs, responses, session manifests and results remain reviewable here. This is a completed validation attempt with a failed promotion gate, not a passed startup release.

## Case applicability and frozen criteria

The original Case 02 rewards an unconditional no-return-at-higher-yields/J-ICS capital-strain explanation. That conflicts with the approved July 2/11 and September 8 owner corrections in THESIS: economic-value solvency includes liabilities, duration-short insurers can benefit from higher rates, and statutory impairment is a separate constraint. Classified **CASE-BUG**, not a new failure of the historical runner. Its original inputs, rubric and May results remain intact. Version 1.2 was written before the first response and retained unchanged through the rerun. Its historical date is correctly Friday, May 15. The suite still has two cases.

## Actual runs

| Surface | Case 01 | Case 02 v1.2 | Decision |
|---|---|---|---|
| Candidate 1, `fb28c158…` | PASS | FAIL: criteria 3/4 | Strengthen general measurement distinctions, then rerun both |
| Candidate 2, `db508c914…` | PASS | FAIL: criterion 5 | Hold promotion; preserve diagnosis and restore original |

Candidate 1 scoring is in [first-pass-assessment.md](first-pass-assessment.md). Candidate 2 Case 01 meets the unchanged seven criteria: M&A discrimination, no Channel 1 fire, foreign unrealized gains, qualified SAM-25 outcome, benign tape, hold/no September add, and threshold-versus-mechanism reasoning. Its unsupported assertion that an acquisition would not be unwound and its proposed tape-only successor rule are additional weaknesses; neither proposal was adopted.

Candidate 2 Case 02 improves the asset/liability explanation and correctly refuses to identify auction buyers. **Criterion 5 is not met:** it discusses political ceilings and possible rate decisions but never makes BOJ intervention conditional on disorder/transmission. Borderline or absent criteria fail under the frozen rubric. Separately, it reverses the currency sign of a foreign exit from yen assets, asserts too much from the absence of a BOJ statement, and invents numerical future watch conditions. These defects reinforce the hold; they were not retroactively added to the rubric to manufacture a failure. No directional trade was recommended.

Diagnosis: lesson present but incompletely applied. Candidate 2 made the general measurement distinctions explicit; another immediate prompt tweak would not establish dependable judgment. Next trial should address policy-reaction and cross-border transaction direction explicitly, with the same frozen cases and a newly identified surface. Do not reopen the rubric merely to obtain a pass.

## Runner isolation and provenance

All four scored responses came from fresh Claude Code 2.1.267 sessions launched in the actual SAM directory, default `claude-opus-4-7`, with tools disabled and only the fenced INPUT on stdin. Native project/auto-memory loading was retained. **Exact auto-memory entries are not enumerated by the CLI and remain unknown**; do not describe this as an audited memory inventory. There were no tool reads of state or rubrics. Scorer review found no distinctive rubric-only leakage; ordinary domain terms and INPUT question ordering are not leakage evidence.

The earlier sandbox launch failed API connectivity and was interrupted without a response; empty attempt files are not scored runs. `.live` and `.rerun` files identify the actual four responses. Read `.response.json` for public text/tool/usage evidence; full raw event hashes are recorded there. Actual UUIDs are in `results.tsv` and manifests. CLI-reported costs are run-specific, not this entire Codex session's cost.

## Orientation acceptance

Fresh session `6eb6d43d-bdd5-4d25-8cc7-14409f6303b6` read **21/21 parts** on Candidate 2. The scorer independently checked returned content hashes, index/source hash pairs and every end marker; [coverage receipt](orientation-coverage.json). All workbook TSVs and predictions hashed identically before/after. It identified LOW/no successor/flat book, three OPEN predictions, source-vintage gaps, the 40Y obligation and the estimated infrastructure reminder. One shell-loop attempt was denied; it recovered by reading every part separately. No market writer, inbox action or external message ran.

This check preceded research writebacks, so its BOJ/funding gaps describe the then-current STATUS snapshot, not the later completed refresh. Operational acceptance **PASS** does not override the judgment **FAIL**. Original CLAUDE SHA256 restored: `9f32c0ae5859ca402ff29b10f9c9a31a8833eb013c2c3bc56470eaaf08db12bd`. Explicit `boot.py --orient` remains available.
