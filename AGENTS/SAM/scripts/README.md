# SAM boot commands

Run from the repository root using `.venv/bin/python3 AGENTS/SAM/scripts/boot.py`.

| Command suffix | Behavior |
|---|---|
| `--orient` | Read-only index of bounded context parts. No market calls or workbook writes. |
| `--orient --part N` | Emit one indexed part, at most 14,000 content bytes, with source/content hashes and an end marker. Read every part before claiming orientation complete. |
| `--predictions` | Read-only OPEN-row report, verbatim conditions/notes, deadline reminders and scheduling gaps. No grades. |
| `--tools` | Generated script inventory; nonzero on missing wiring or undocumented tools. Lists the imported context helper too. |
| no suffix | Market refresh. Existing scripts can write their workbooks. Includes prediction reminders and inventory checks. |
| `--quick` | Market refresh with **only options skipped**. Other market writers still run. |
| `--verbose` | Show complete child stdout/stderr during market refresh. |
| `--report /absolute/new-file.jsonl` | Choose a new raw report path; existing files are never overwritten. Monitoring only. |

The live CLAUDE startup order remains in force pending fresh-session eval of the [candidate patch](../proposals/2026-09-09_boot-protocol.patch). These explicit commands are available now. Orientation is context recovery; a request for market analysis still requires appropriate source refreshes.

## Orientation contract

The index is deliberately **not** one giant output that a tool can silently truncate. Read numbered parts separately with enough output allowance for a 14KB UTF-8 part plus metadata. Verify each `END PART` and match its source/content hashes to the index. If any source hash changes between reads, generate a new index and re-read the affected source's parts. A manifest is not proof that its content was read.

Selection: THESIS current header, pillar audit, full probability-method/channel section, oil-in-yen and thresholds; STATUS header/latest session, market data, probability vintage, intervention limits, thresholds, watch list, position and predictions; CALENDAR owner-maintained forward and beyond-six-week sections; latest two TIMELINE blocks; whole MEMORY; prediction calibration warning and all OPEN conditions/notes. The historical preamble session log and closed rows stay reference-only. Rubrics, gated RED bodies, inbox actions and archives are excluded.

Missing/duplicate required sections, ambiguous ordering, oversized lines and malformed prediction rows fail visibly. The calendar selection uses the owner's forward section, not inferred dates from decorative prose; reconcile stale rows before treating it as a current schedule. Scheduling gaps remain visible and return nonzero while OPEN conditions are still shown.

## Monitor semantics and failure records

USDJPY watch levels are observations; they do not confirm a mechanism or authorize a trade. FXY and continuous Brent remain context quotes without trading thresholds. Previous-close/undated quotes retain their identity and cannot generate a crossing. Timestamped regular-market observations carry the vendor clock; no arbitrary new age cutoff or execution-price certification is implied. JGB 30Y/40Y levels alone do not identify insurer stress or forced sales.

Live CFTC normalization uses the corrected −188,077 record (June 26, 2007); `CFTC_JPY.tsv` deliberately retains its declared −180,000 legacy percentage basis. Weekly short-cover percentage is `-change_short / (current_short - change_short) * 100`; the alert remains strictly above 10%. Gross positions and open interest require interpretation; the script does not declare an unwind from them.

Each normal run creates `reports/boot-runs/<UTC>_<id>.jsonl` with complete child stdout/stderr, exit/reason, elapsed time, stored-vintage diagnostics and final status. Failures never enter the “completed” summary branch; timeout output survives. Independent legs continue. A nonzero child, inventory drift or prediction-reader gap makes the overall exit nonzero. Stored dates and execution success do not certify market freshness. Options skip requires at least four unique future expiry rows for today; completeness does not certify their quote quality.

## Prediction reminders

Canonical terms and grades remain in `thesis/PREDICTIONS.tsv`. `docket/PREDICTION_SCHEDULE.json` maps IDs to reminder dates, timezones and boundary caveats, tied to SHA256 of the original Prediction/Timeframe/Notes fields (canonical sorted compact JSON). A new OPEN ID without a mapping or changed terms prints a scheduling gap. Update the sidecar only after checking the actual row; never alter a prediction to silence a reminder. Exact times absent from original terms remain unresolved, not invented.

## BOJ review and validation

Run `.venv/bin/python3 AGENTS/SAM/scripts/boj_ois.py --prepare-review` to save publisher HTML, original PNG, manifest and blank transcription. Complete the human review and follow [BOJ ingestion instructions](../workbook/BOJ_OIS_README.md). Preparation writes evidence only, never quote rows.

Offline regression suite:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python3 -m unittest discover -s AGENTS/SAM/scripts/tests -v
```

These deterministic tests do not substitute for SAM's separate fresh-session judgment eval.
