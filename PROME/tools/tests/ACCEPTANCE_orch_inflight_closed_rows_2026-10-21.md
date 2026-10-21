# Acceptance — ORCH_INFLIGHT closed-row omission

Written before implementation on 2026-10-21. Authority: Will's bounded task relayed by PROME. State after implementation is IMPLEMENTED + TESTED; independent verification belongs to PROME.

Only the generated view changes. Never edit or rotate ledger rows for this task.

1. An IN-FLIGHT TOUCH without a later closing row remains in the IN-FLIGHT table.
2. A later ledger row for the exact same desk string closes earlier IN-FLIGHT rows when its touch contains RECEIPT or CLOSE (case-insensitive). Test receipt suffix variants and the CLOSE summary token. The view omits those earlier rows and prints one explicit omitted-row count with the reason, including zero.
3. Desk matching is exact: a differently spelled, qualified, case-changed or whitespace-changed desk string cannot close the original desk's row.
4. Later means later file position, not date sorting. An earlier receipt cannot close a later spawn. Reopened spawns stay listed; a row cannot close itself. A later-position receipt works even with an older date.
5. Repeated receipts do not double-count omitted rows. A non-closing touch or close-related text in another column does not close a spawn. Filtering never mutates input rows.
6. Regenerating a temporary view leaves the temporary ledger byte-for-byte unchanged. The production regeneration also compares ledger bytes before/after; concurrent append activity must be reported separately from this writer's behavior.
7. Preserve the source ledger row count, generated metadata, existing visible-row sort/order and formatting. Preserve the complete last-drained section and no-recent-drain section byte-for-byte for identical input, date and window. Omission adds only its explanatory line besides the changed IN-FLIGHT count/table.
8. Run and report these exact checks, including exit codes:
   - `python3 scripts/orch_log.py --selftest`
   - `PYTHONPATH="$PWD/scripts" python3 -m unittest discover -s scripts/tests -p 'test_orch_log*.py'`
   - `python3 -m unittest discover -s PROME/tools/tests -p test_orch_closeout.py`
   - `python3 scripts/orch_log.py check`
9. Regenerate with `python3 scripts/orch_log.py view`, then run `python3 PROME/tools/measure.py PROME/state/ORCH_INFLIGHT.md`. Report before/after bytes, remaining IN-FLIGHT rows, omitted count and exact October21 OZK/RED/FERT/BROCK/LABOR/PROME-reader outcomes against ledger evidence.
10. Inspect readers under PROME/tools, scripts and WALTER boot. Distinguish consumers of current open-touch visibility/cadence from consumers requiring historical lifecycle evidence; the ledger remains the latter's source.
11. Commit only scripts/orch_log.py, the new scripts/tests test, this acceptance file and PROME/state/ORCH_INFLIGHT.md. Do not push. No ledger, charter, lifecycle rule or unrelated work is changed.

Execution results will be appended after the implementation and required checks.

## Execution results — IMPLEMENTED + TESTED

All acceptance conditions passed. PROME's independent read remains pending.

Required command results (all exit 0):

```text
$ python3 scripts/orch_log.py --selftest
ORCH-LOG SELFTEST ✓ 36/36

$ PYTHONPATH="$PWD/scripts" python3 -m unittest discover -s scripts/tests -p 'test_orch_log*.py'
Ran 17 tests in 0.047s
OK

$ python3 -m unittest discover -s PROME/tools/tests -p test_orch_closeout.py
Ran 27 tests in 0.070s
OK

$ python3 scripts/orch_log.py check
ORCH-LOG ✓ PROME/state/ORCH_LOG.tsv: 1282 data rows × 13 columns, typed cells int-or-EMPTY

$ python3 scripts/orch_log.py view
ORCH-LOG ✓ view regenerated → PROME/state/ORCH_INFLIGHT.md (27579 B, 130 table rows, window 30d)

$ python3 PROME/tools/measure.py PROME/state/ORCH_INFLIGHT.md
PROME/state/ORCH_INFLIGHT.md  27579 B (wc -c)  146 lines (wc -l)  crc32 3759042870  crc32-no-final-nl 3572652070
```

The scripts unittest command emitted ResourceWarning messages for existing unclosed reads in orch_log.py at lines 105, 165 and 217. These did not fail tests; those existing reads were left outside this view-only change.

Production view: 32,299 B → 27,579 B (4,720 B reduction; 4,971 B below the 32,550 B boot cap). Original 83 IN-FLIGHT rows → 32 remaining, 51 explicitly counted as omitted. The reported 130 table rows includes the unchanged 98 cadence rows.

Ledger bytes matched both the pre-implementation snapshot and the immediate before/after regeneration snapshots. SHA-256: bdac19a5353102c41fa02a50b4de36e77c16cda11048059a8ef5c0ee46fc6e10. No ledger write or rotation was performed.

Loaded the saved original renderer from /tmp and compared it with the new renderer on identical production rows, date and window. The first three metadata lines and the entire suffix starting at `## Last drained>0` (actual heading contains Markdown backticks) were byte-identical. The regenerated file equals the new renderer output. Input immutability and stable visible-row order also pass the synthetic tests.

All 23 targeted October21 IN-FLIGHT rows are omitted:

| Exact desk | Omitted touches | Later closing touches |
|---|---|---|
| OZK | 1-SPAWN, 3-REPING, 5-REPING | 2-CLOSEOUT-RECEIPT, 4-REPING-RECEIPT, 6-REPING-RECEIPT |
| RED | 1-SPAWN, 3-REPING, 5-REPING | same receipt sequence |
| FERT | 1-SPAWN, 3-REPING, 5-REPING | same receipt sequence |
| BROCK | 1-SPAWN, 3-REPING, 5-REPING | same receipt sequence |
| LABOR | 1-SPAWN, 3-REPING, 5-REPING | same receipt sequence |
| PROME-reader (canon-spacing-plan-read) | 1-SPAWN | 2-CLOSEOUT-RECEIPT |
| PROME-reader (canon-spacing-result-read) | 1-SPAWN | 2-CLOSEOUT-RECEIPT |
| PROME-reader (docket-lines-read1) | 1-SPAWN | 2-CLOSEOUT-RECEIPT |
| PROME-reader (action-owed-read1) | 1-SPAWN | 2-CLOSEOUT-RECEIPT |
| PROME-reader (action-owed-read2) | 1-SPAWN | 2-CLOSEOUT-RECEIPT |
| PROME-reader (firetime-delta-read1) | 1-SPAWN | 2-CLOSEOUT-RECEIPT |
| PROME-reader (firetime-delta-read2) | 1-SPAWN | 2-CLOSEOUT-RECEIPT |
| PROME-reader (firetime-delta-read3) | 1-SPAWN | 2-CLOSEOUT-RECEIPT |

Each closing receipt is later in file position and matches the desk string exactly. All original rows remain in the ledger.

## Reader compatibility

Searched with `rg -n 'ORCH_INFLIGHT\.md|render_view' PROME/tools scripts AGENTS/WALTER/CLAUDE.md AGENTS/WALTER/design/BOOT_PROTOCOL.md -g '*.py' -g '*.md'` and inspected the matching consumers.

- WALTER CLAUDE.md boot 9b reads open touches and last drained>0 cadence. Closed historical spawns are unnecessary; the complete cadence section is preserved. The boot-protocol reference is a historical incident, explicitly superseded.
- PROME/tools/prome_gate.py check_orch_log_observed consumes the first three lines' source ledger row count, not the IN-FLIGHT table count. All 1,282 source rows remain counted. Its closeout check invokes orch_closeout.py, which reads the ledger directly.
- scripts/orch_log.py _view_count and append/guarded_view use source-count metadata, preserved unchanged. Existing selftests and scripts/tests/test_orch_log_view_L736.py pass.
- scripts/orch_time.py only supplies the view path to the canonical append writer during invalidation; it does not consume historical first-table rows.
- PROME/tools/tests/test_orch_log_wiring_L733.py and its acceptance document describe or fixture the source-count header, preserved unchanged. They do not require the omitted rows.

No inspected consumer depends on the omitted rows. The rule is deliberately the requested literal touch substring rule: CLOSEOUT-PING also contains CLOSE. This projection is not native liveness or authenticated receipt evidence, and exact desk matching does not infer session identities.

Only the four authorized paths are included in the task commit. No push; PROME owns the independent read and push.
