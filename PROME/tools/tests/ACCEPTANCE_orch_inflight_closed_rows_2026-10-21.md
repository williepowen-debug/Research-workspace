# Acceptance — ORCH_INFLIGHT closure pairing (amended after independent read 2)

Amended before coding the follow-up on 2026-10-21, under Will's exact-path authorization relayed by PROME. This replaces the original substring rule. Independent read 1 returned HOLD on dbed8968c: one desk-wide match could hide unrelated work, asks and time corrections. The original 51 omissions included 10 omissions caused by asks; the original title overstated receipt closure. Read 2 returned HOLD on a9e5fe2d1: the legacy guess could cross dates or a numbering restart and hide another session. This amendment precedes the second follow-up code changes; read 3 remains PROME-owned.

1. Keep every open IN-FLIGHT TOUCH visible unless paired with a strictly later closing row for the EXACT same desk string. File order is mandatory; legacy pairs also require equal dates. Desk aliases never establish pairing. Do not mutate input rows or ledger bytes.
2. A potential closer must end in `-RECEIPT` or be exactly `CLOSE` (case-insensitive token form). Exclude any row whose delivered cell starts TIME-CORRECTION or whose notes contain time_correction_v1=. Do not use CLOSE/RECEIPT substrings. IN-FLIGHT closing rows are still pending and cannot hide earlier work. Also exclude delivered cells starting PENDING, AWAITING or NO RECEIPT (case-insensitive, ignoring leading whitespace).
3. When both sides contain closeout_v1, use the existing PROME/tools/orch_closeout.py structured()/touch_key()/reconcile() validation and explicit resolves/session identity, ownership and chronology rules. A view closure requires a valid terminal receipt result and a closing-form resolution event naming ONE original key. Do not invent resolves links or session identity. Invalid, ambiguous, duplicate-key, missing-link or reopened evidence stays visible. Existing canonical lifecycle logic remains unedited.
4. Legacy fallback applies only when at least one side has no structured payload. A numbered receipt pairs with at most one earlier same-desk IN-FLIGHT row on the SAME DATE whose leading number is strictly lower: choose the highest eligible number, only if unique at that number. Reject a candidate if ANY same-desk TOUCH row strictly between it and the receipt in file order has a leading number less than or equal to the candidate's. Evaluate the restart guard only after establishing the unique highest lower-numbered candidate; a rejected candidate does not break a tie or permit guessing a lower candidate. This includes delivered/non-IN-FLIGHT touches and rows on other dates: a numbering restart makes that older candidate ambiguous. Other desks, unnumbered CLOSE summaries and higher numbers do not create this boundary. Include already-paired candidates in selection so repeated receipts cannot successively consume older rows. If both sides expose structured sessions they must agree; malformed structured evidence cannot fall back to guessed closure. An unnumbered CLOSE needs an explicit valid structured resolution; it has no numeric fallback. Residue is safer than hiding ambiguous work.
5. CE1: 3-REPING, 5-REPING IN-FLIGHT then late 4-REPING-RECEIPT hides only3;5 stays visible. CE2: two1-SPAWN sessions A/B and one explicit receipt forA leavesB visible. Missing explicit links and ambiguous unstructured session prose must not hide either session by desk alone.
6. CE3: spawn plus TIME-CORRECTION CLOSE keeps the spawn; independently test delivered-prefix and notes-marker exclusion. CE5: ARGUS spawn plus new1-CLOSEOUT-AUDIT IN-FLIGHT keeps both. CLOSEOUT-ASK, CLOSEOUT-PING, CLOSEOUT-PLAN and CLOSEOUT-CHECK-ASK close nothing.
7. F1: October20 2-REPING (A), October21 1-SPAWN (B), then B's3-RECEIPT keeps A visible and closes B only. Also test a same-day restart independently of the date guard, both lower and equal leading numbers, including a delivered intermediate TOUCH. F1b: TERRY October5 4-CLOSEOUT-ASK must stay visible after October21 restarted work and5-RECEIPT. F12: a date gap alone keeps the original visible. An unrelated-desk or unnumbered CLOSE intermediate must not block a valid pair.
8. Test valid single-target receipt/CLOSE links; wrong session/owner/key, missing link, malformed payload and invalid chronology; a subsequent valid working correction keeps the original visible. One receipt never hides all earlier same-desk rows. Preserve open, earlier-receipt/later-spawn, exact-desk, no self-close, stable sorting, no double count and byte-unchanged ledger cases.
9. Preserve source count/header and the complete cadence/no-drain suffix byte-for-byte for identical rows/date/window. The only view changes are the first-table rows/count and one honest omission line splitting total omitted N into E explicit resolves links and L legacy pairs (highest lower-numbered same-desk touch, unique at that number, same date, no restart). Counts are disjoint and sum to N, including zero. The line retains asks/time-correction exclusions.
10. Run all four required commands and record exit codes/results:
   - `python3 scripts/orch_log.py --selftest`
   - `PYTHONPATH="$PWD/scripts" python3 -m unittest discover -s scripts/tests -p 'test_orch_log*.py'`
   - `python3 -m unittest discover -s PROME/tools/tests -p test_orch_closeout.py`
   - `python3 scripts/orch_log.py check`
11. Regenerate with `python3 scripts/orch_log.py view`, measure with `python3 PROME/tools/measure.py PROME/state/ORCH_INFLIGHT.md`, and report bytes, shown/omitted counts and unchanged ledger bytes. If above approximately30,000 B, report it; do not weaken pairing or edit/rotate the ledger to fit.
12. Commit as a NEW commit, exact paths only: scripts/orch_log.py, scripts/tests/test_orch_log_closed_rows.py, this acceptance file and PROME/state/ORCH_INFLIGHT.md. No amend, push, lifecycle-owner edit or other path edit. PROME owns independent read3 and publication. Final state is IMPLEMENTED + TESTED, not verified.

## Execution results

IMPLEMENTED + TESTED. Independent read3 remains pending; no verified claim. The same-date and no-numbering-restart conditions apply only to the legacy path; canonical explicit session/resolves reconciliation remains unchanged. Unnumbered CLOSE still requires an explicit valid link. The pending-prefix guard applies to all potential closers, including a contradictory structured receipt.

All required commands exited0:

```text
$ python3 scripts/orch_log.py --selftest
ORCH-LOG SELFTEST ✓ 36/36

$ PYTHONPATH="$PWD/scripts" python3 -m unittest discover -s scripts/tests -p 'test_orch_log*.py'
Ran 38 tests in 0.053s
OK

$ python3 -m unittest discover -s PROME/tools/tests -p test_orch_closeout.py
Ran 27 tests in 0.056s
OK

$ python3 scripts/orch_log.py check
ORCH-LOG ✓ PROME/state/ORCH_LOG.tsv: 1285 data rows × 13 columns, typed cells int-or-EMPTY

$ python3 scripts/orch_log.py view
ORCH-LOG ✓ view regenerated → PROME/state/ORCH_INFLIGHT.md (29449 B, 150 table rows, window 30d)

$ python3 PROME/tools/measure.py PROME/state/ORCH_INFLIGHT.md
PROME/state/ORCH_INFLIGHT.md  29449 B (wc -c)  166 lines (wc -l)  crc32 772516590  crc32-no-final-nl 2966232913
```

Current ledger:85 IN-FLIGHT TOUCH rows,52 shown,33 omitted. Omission split:0 explicit resolves links,33 legacy pairs. The98 cadence rows remain. View29,449 B,551 B below30,000 and3,101 B below32,550. The pre-edit working view was29,444 B; the5 B increase is disclosure wording only. No pairing condition was relaxed for headroom.

Compared saved pre-edit _closed_inflight output with the new pair set on identical current ledger rows:0 of33 omissions changed. Also ran the reader's trace.py with the workspace scripts path and live ledger as read-only inputs: proposed guard simulation reports `pairs affected 0`. Canonical structured reconciliation is unchanged; production currently has no explicit-link omission.

Added nine test methods covering F1, same-day equal/lower restarts independently of the date condition, F1b TERRY, F12 with a date gap alone, file-order restarts with intermediate date differences, unrelated-desk/CLOSE/higher-number non-boundaries, PENDING/AWAITING/NO RECEIPT case/whitespace prefixes, valid explicit overnight completion, and exact split-count arithmetic/wording. Existing CE1–CE5/ask and two-session ambiguity tests remain passing. In F1b, both the old unresolved ask and the newer unpaired spawn remain visible; one receipt closes only the highest eligible reping, never all work in a session.

A first draft revealed that filtering restarted candidates before the uniqueness decision could break the earlier CE2 protection. The final code establishes the unique highest candidate before applying the restart guard; it never uses rejection to break a tie or guess a lower row. The amended acceptance states that conservative behavior explicitly.

Ledger bytes matched the pre-code snapshot and the immediate before/after regeneration: SHA-25668174236bb9d2994426ee7d612f020973760e2a22e644092b3d47820f046179d. No ledger edit, append or rotation occurred. Metadata/source count and the complete cadence/no-drain suffix are byte-identical to both the pre-edit working view and prior renderer on identical input; the generated file equals the new renderer output.

Existing ResourceWarnings for unclosed reads in check/_view_count/append remain outside this bounded repair; tests pass. Legacy prose identities are not authenticated or inferred; the added date/restart guards bound the authorized fallback, while genuinely closed-but-unpaired history remains visible. The view does not establish native liveness or recipient consumption.

Only the four authorized paths are committed, as a new commit. Other PROME/root/memory changes remain untouched. No push, amend, canonical lifecycle edit, or local WALTER state/packet write; this acceptance file and task output are the authorized completion record. PROME owns the third independent read and publication.

Wording correction: read1's fix restored19 rows relative to the original substring view. Ten were genuinely open asks/spawns; the other9 are closed but unpaired records retained as fail-safe residue. They must not be called19 wrongly hidden rows. Lifecycle reconciliation, not weakening the view rule, owns removal of that residue.
