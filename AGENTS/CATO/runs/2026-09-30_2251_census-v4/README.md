# Census v4 — bounded CATO repair of the critic's v3

**Use this as an inspectable extraction and sensitivity analysis, not a validated fleet performance score.** Pin `e70f558f4ad685cec394a9cdc2ef6ee622d6b6e0`, cutoff `2026-10-01`, same 534 desk/ID keys and source files selected by v3. Original files remain unchanged in [v3 evidence](../2026-09-30_2251_census-v3-evidence/). Findings, authorization and disposition: [continuing report](../2026-09-30_2251_census-v3-validation.md#september-30--approved-bounded-repair).

Run from the Git root (full ancestor objects must be available):

```bash
python3 -B AGENTS/CATO/runs/2026-09-30_2251_census-v4/census_v4.py --out /tmp/cato-census-v4-replay
python3 -B AGENTS/CATO/runs/2026-09-30_2251_census-v4/check_outputs.py /tmp/cato-census-v4-replay
CATO_CENSUS_OUTPUT=/tmp/cato-census-v4-replay python3 -B -m unittest discover -s AGENTS/CATO/runs/2026-09-30_2251_census-v4 -p test_census_v4.py -v
```

The command reads Git objects and writes only the specified output directory. It never edits owners, changes Git history, sends messages or schedules work. Expected local runtime is several minutes, depending on repository/cache speed. The original path/outcome/date helper functions are retained from v3; probabilities, history, provenance and grading treatment are repaired here.

| Artifact | Purpose |
|---|---|
| [rows_v4.tsv](rows_v4.tsv) | One row per original desk/ID; probability vintages, source pointers, flags and disposition |
| [summary_v4.tsv](summary_v4.tsv) | Separate denominators/baselines for each view; alphabetical desks, not rankings |
| [comparison_v3_v4.tsv](comparison_v3_v4.tsv) | Every original row's old/new probability and classification |
| [sources_v4.jsonl](sources_v4.jsonl) | Full current fields and earliest candidates from every searched source path; no 80-character truncation |
| [annotations.json](annotations.json) | Explicit grading/eligibility statements inspected by CATO, each with source hash and exact quote |
| [provenance_v4.json](provenance_v4.json) | Pin, input/code hashes, searched/excluded paths, counts and limits |
| [checks.json](checks.json) | Separate Decimal arithmetic, coverage checks and changed historical values |
| [test-results.txt](test-results.txt) | 19 author tests, all passed; no independent reviewer claimed |

Probabilities and Brier scores use **fractions 0–1**. `UNKNOWN` is missing evidence, never zero. `p_current` reads a numeric current cell; a cell beginning `SCORE AT` is a grading instruction and is not relabelled as a live belief. `p_recorded_grade` means an explicit owner-specified grading probability, including instructions for open rows. It does not itself mean a grade occurred. The reviewed annotations identify 25 such values; 15 rows have binary statuses and no recorded exclusion. That deliberately selected subset is not representative of the fleet. Other rows remain unknown even if an uninspected narrative elsewhere might establish a value.

`p_earliest_observed` is the numeric value at the earliest recovered ledger occurrence. All historical `AGENTS/**/PREDICTIONS*.tsv` paths reachable from the pin are considered, including deleted predecessors. Snapshots/derived paths identified by the inherited file rules are excluded. Ancestry orders appearances before path names; same-commit ties prefer an established file, then LIVE. Conflicting same-commit candidates remain flagged. This is not a search of every historical STATUS/Markdown document or arbitrary ledger basename, nor a reconstruction of old owner renames.

Rows with malformed earliest schemas, conflicting IDs, or different claim/date/window/resolution/invalidation text are excluded from historical scoring. Text differences can be benign formatting or archival moves; they require semantic review, not an automatic verdict that the forecast changed. A numeric slot in a malformed first row is retained as a candidate, with its full fields, but not scored. File-birth uncertainty is calculated against the actual source commit/path. Earlier appearances with no numeric value are not silently replaced by later numeric marks.

**No row is certified as a registration-time forecast by this repair.** `p_registration` remains UNKNOWN; this means that validation was not performed, not that registration can never be recovered. The history views still include some rows first seen after resolution and some present at file birth. They are sensitivity calculations only.

Unknown eligibility stays explicit; it is not upgraded to eligibility because the outcome is binary. Explicit exclusions, pending verification and malformed current rows cannot contribute to any Brier view. Remaining outcome/date classifications retain v3's heuristics. External evidence, correlated events, differing horizons and exclusion selection remain unverified. Every displayed baseline is computed from that same subset's realized outcomes, not an available-at-registration forecast benchmark.
