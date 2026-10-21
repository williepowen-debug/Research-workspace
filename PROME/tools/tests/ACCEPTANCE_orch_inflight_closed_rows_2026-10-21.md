# Acceptance — ORCH_INFLIGHT closure pairing (amended after independent read 1)

Amended before coding the follow-up on 2026-10-21, under Will's exact-path authorization relayed by PROME. This replaces the original substring rule. Independent read 1 returned HOLD on dbed8968c: one desk-wide match could hide unrelated work, asks and time corrections. The original 51 omissions included 10 omissions caused by asks; the original title overstated receipt closure. That implementation is not verified.

1. Keep every open IN-FLIGHT TOUCH visible unless paired with a strictly later closing row for the EXACT same desk string. Neither dates nor desk aliases establish pairing. Do not mutate input rows or ledger bytes.
2. A potential closer must end in `-RECEIPT` or be exactly `CLOSE` (case-insensitive token form). Exclude any row whose delivered cell starts TIME-CORRECTION or whose notes contain time_correction_v1=. Do not use CLOSE/RECEIPT substrings. IN-FLIGHT closing rows are still pending and cannot hide earlier work.
3. When both sides contain closeout_v1, use the existing PROME/tools/orch_closeout.py structured()/touch_key()/reconcile() validation and explicit resolves/session identity, ownership and chronology rules. A view closure requires a valid terminal receipt result and a closing-form resolution event naming ONE original key. Do not invent resolves links or session identity. Invalid, ambiguous, duplicate-key, missing-link or reopened evidence stays visible. Existing canonical lifecycle logic remains unedited.
4. Legacy fallback applies only when at least one side has no structured payload. A numbered receipt pairs with at most one earlier same-desk IN-FLIGHT row whose leading number is strictly lower: choose the highest eligible number, only if unique. Include already-paired candidates in selection so repeated receipts cannot successively consume older rows. If both sides expose structured sessions they must agree; malformed structured evidence cannot fall back to guessed closure. An unnumbered CLOSE needs an explicit valid structured resolution; it has no numeric fallback. Residue is safer than hiding ambiguous work.
5. CE1: 3-REPING, 5-REPING IN-FLIGHT then late 4-REPING-RECEIPT hides only3;5 stays visible. CE2: two1-SPAWN sessions A/B and one explicit receipt forA leavesB visible. Missing explicit links and ambiguous unstructured session prose must not hide either session by desk alone.
6. CE3: spawn plus TIME-CORRECTION CLOSE keeps the spawn; independently test delivered-prefix and notes-marker exclusion. CE5: ARGUS spawn plus new1-CLOSEOUT-AUDIT IN-FLIGHT keeps both. CLOSEOUT-ASK, CLOSEOUT-PING, CLOSEOUT-PLAN and CLOSEOUT-CHECK-ASK close nothing.
7. Test valid single-target receipt/CLOSE links; wrong session/owner/key, missing link, malformed payload and invalid chronology; a subsequent valid working correction keeps the original visible. One receipt never hides all earlier same-desk rows. Preserve open, earlier-receipt/later-spawn, exact-desk, no self-close, stable sorting, no double count and byte-unchanged ledger cases.
8. Preserve source count/header and the complete cadence/no-drain suffix byte-for-byte for identical rows/date/window. The only view changes are the first-table rows/count and one honest omission line explaining paired receipt/CLOSE rules and exclusions, including a zero count.
9. Run all four required commands and record exit codes/results:
   - `python3 scripts/orch_log.py --selftest`
   - `PYTHONPATH="$PWD/scripts" python3 -m unittest discover -s scripts/tests -p 'test_orch_log*.py'`
   - `python3 -m unittest discover -s PROME/tools/tests -p test_orch_closeout.py`
   - `python3 scripts/orch_log.py check`
10. Regenerate with `python3 scripts/orch_log.py view`, measure with `python3 PROME/tools/measure.py PROME/state/ORCH_INFLIGHT.md`, and report bytes, shown/omitted counts and unchanged ledger bytes. If above approximately30,000 B, report it; do not weaken pairing or edit/rotate the ledger to fit.
11. Commit as a NEW commit, exact paths only: scripts/orch_log.py, scripts/tests/test_orch_log_closed_rows.py, this acceptance file and PROME/state/ORCH_INFLIGHT.md. No amend, push, lifecycle-owner edit or other path edit. PROME owns independent read2 and publication. Final state is IMPLEMENTED + TESTED, not verified.

## Execution results

IMPLEMENTED + TESTED. Independent read2 is pending; this is not a verification claim. The original substring rule has been replaced in code, tests and this acceptance file.

All four required commands exited0:

```text
$ python3 scripts/orch_log.py --selftest
ORCH-LOG SELFTEST ✓ 36/36

$ PYTHONPATH="$PWD/scripts" python3 -m unittest discover -s scripts/tests -p 'test_orch_log*.py'
Ran 29 tests in 0.052s
OK

$ python3 -m unittest discover -s PROME/tools/tests -p test_orch_closeout.py
Ran 27 tests in 0.042s
OK

$ python3 scripts/orch_log.py check
ORCH-LOG ✓ PROME/state/ORCH_LOG.tsv: 1283 data rows × 13 columns, typed cells int-or-EMPTY

$ python3 scripts/orch_log.py view
ORCH-LOG ✓ view regenerated → PROME/state/ORCH_INFLIGHT.md (29408 B, 150 table rows, window 30d)

$ python3 PROME/tools/measure.py PROME/state/ORCH_INFLIGHT.md
PROME/state/ORCH_INFLIGHT.md  29408 B (wc -c)  166 lines (wc -l)  crc32 3575868920  crc32-no-final-nl 1279683598
```

The scripts tests still emit existing unclosed-file ResourceWarnings from check/_view_count/append. Those existing reads are outside this repair.

The current ledger contains84 IN-FLIGHT TOUCH rows:52 shown,32 omitted. The corrected view is29,408 B,592 B below30,000 and3,142 B below the32,550 B cap. The pre-follow-up working view was27,739 B. Correct pairing restores19 rows hidden by the old rule, including all10 ask-based omissions. The other9 are unpaired/ambiguous lifecycle histories or receipt tokens that do not meet the terminal-suffix rule; none were forced closed for headroom.

The header/source count and complete cadence/no-drain suffix are byte-identical both to the pre-follow-up working view and the dbed8968c renderer on identical current input. Only the IN-FLIGHT table/count and explanatory line change. The98 cadence rows remain. The whole regenerated file equals render_view output.

Production ledger bytes matched both the pre-code snapshot and the immediate before/after view snapshots: SHA-256 0c6b4da2ab28c96b1da39a6ef0a2341e1980a12edd1abce204ad243aa02ca7c3. No edit, append or rotation of the ledger occurred. Existing foreign ledger changes relative to HEAD are excluded from the commit. The view is regenerated from that current validated ledger, as requested.

Counterexamples were also run from the independent reader's ce.py against the actual workspace module via runpy, explicitly confirming orch_log.__file__. CE1 leaves5-REPING, omits3; CE2's unstructured session prose keeps both spawns visible (ambiguous identity), while the new structured CE2 test closes onlyA; CE3 keeps spawn; CE4 keeps spawn and pending ask; CE5 keeps both ARGUS rows; CE7 keeps the desk variant. CE6's2-NO-RECEIPT still matches the expressly requested terminal-RECEIPT form; it is not a substring exception added by this repair. A direct invocation initially imported the reader's sibling scratch copy of orch_log.py; it was corrected by explicitly loading the workspace module before runpy. No scratch-copy result is treated as amended acceptance.

Structured pairing calls the existing canonical reconcile() unchanged, including identity, chronology and time-invalidation validation. A missing explicit resolves link, duplicate original key, invalid payload, working correction or multiple-target event remains visible. Unnumbered legacy CLOSE rows have no lower-number comparison and remain visible. One legacy receipt selects one unique highest lower touch; already-paired candidates prevent duplicate receipts consuming successively older work. These are conservative visibility choices, not new ledger lifecycle authority.

Reader compatibility: the source-count metadata used by append/guarded_view/prome_gate remains unchanged; orch_time's CLOSE time-correction path is explicitly excluded from the closing set. WALTER9b/13 now retains the counterexample running/unknown rows. Canonical orch_closeout code and its27 passing tests are unedited. No native liveness or receipt-authentication claim is made.

Only the four authorized paths belong to the new follow-up commit; no push or amend. PROME owns the next independent read and publication. No additional completion packet, local charter or WALTER session anchor was edited under this exact-path task.

