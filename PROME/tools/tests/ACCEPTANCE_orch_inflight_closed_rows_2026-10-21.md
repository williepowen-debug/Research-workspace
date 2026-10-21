# Acceptance — ORCH_INFLIGHT closure pairing (amended after independent read 3)

Amended before coding the follow-up on 2026-10-21, under Will's exact-path authorization relayed by PROME. This replaces the original substring rule. Independent read 1 returned HOLD on dbed8968c: one desk-wide match could hide unrelated work, asks and time corrections. The original 51 omissions included 10 omissions caused by asks; the original title overstated receipt closure. Read 2 returned HOLD on a9e5fe2d1: the legacy guess could cross dates or a numbering restart and hide another session. Read 3 returned HOLD on ee5be7a1c for G1/G1b: a same-number PENDING or DELIVERED touch before the live candidate was omitted from the uniqueness test. This amendment precedes the post-final-read code change. State: IMPLEMENTED + TESTED; post-final-read fix, NOT independently verified.

1. Keep every open IN-FLIGHT TOUCH visible unless paired with a strictly later closing row for the EXACT same desk string. File order is mandatory; legacy pairs also require equal dates. Desk aliases never establish pairing. Do not mutate input rows or ledger bytes.
2. A potential closer must end in `-RECEIPT` or be exactly `CLOSE` (case-insensitive token form). Exclude any row whose delivered cell starts TIME-CORRECTION or whose notes contain time_correction_v1=. Do not use CLOSE/RECEIPT substrings. IN-FLIGHT closing rows are still pending and cannot hide earlier work. Also exclude delivered cells starting PENDING, AWAITING or NO RECEIPT (case-insensitive, ignoring leading whitespace).
3. When both sides contain closeout_v1, use the existing PROME/tools/orch_closeout.py structured()/touch_key()/reconcile() validation and explicit resolves/session identity, ownership and chronology rules. A view closure requires a valid terminal receipt result and a closing-form resolution event naming ONE original key. Do not invent resolves links or session identity. Invalid, ambiguous, duplicate-key, missing-link or reopened evidence stays visible. Existing canonical lifecycle logic remains unedited.
4. Legacy fallback applies only when at least one side has no structured payload. A numbered receipt pairs with at most one earlier same-desk IN-FLIGHT row on the SAME DATE whose leading number is strictly lower: choose the highest eligible number, only if unique among ALL same-desk, same-date TOUCH rows before the receipt at that number, in ANY delivered state. The entire prefix counts, including rows before the selected candidate. Reject the pair when more than one such row exists; do not guess another target. Reject a candidate if ANY same-desk TOUCH row strictly between it and the receipt in file order has a leading number less than or equal to the candidate's. Evaluate the restart guard only after establishing the unique highest lower-numbered candidate; a rejected candidate does not break a tie or permit guessing a lower candidate. This includes delivered/non-IN-FLIGHT touches and rows on other dates: a numbering restart makes that older candidate ambiguous. Other desks, unnumbered CLOSE summaries and higher numbers do not create this boundary. Include already-paired candidates in selection so repeated receipts cannot successively consume older rows. If both sides expose structured sessions they must agree; malformed structured evidence cannot fall back to guessed closure. An unnumbered CLOSE needs an explicit valid structured resolution; it has no numeric fallback. Residue is safer than hiding ambiguous work.
5. CE1: 3-REPING, 5-REPING IN-FLIGHT then late 4-REPING-RECEIPT hides only3;5 stays visible. CE2: two1-SPAWN sessions A/B and one explicit receipt forA leavesB visible. For structured pairs, missing explicit links keep work visible. Legacy identity limitations F2/G2/G3/G4 remain declared below; prose identity is not authenticated. G1/G1b: a same-day session B1-SPAWN logged PENDING or DELIVERED before live A1-SPAWN, followed by B2-RECEIPT, must keep A visible. Test both states and distinct trigger/session prose.
6. CE3: spawn plus TIME-CORRECTION CLOSE keeps the spawn; independently test delivered-prefix and notes-marker exclusion. CE5: ARGUS spawn plus new1-CLOSEOUT-AUDIT IN-FLIGHT keeps both. CLOSEOUT-ASK, CLOSEOUT-PING, CLOSEOUT-PLAN and CLOSEOUT-CHECK-ASK close nothing.
7. F1: October20 2-REPING (A), October21 1-SPAWN (B), then B's3-RECEIPT keeps A visible and closes B only. Also test a same-day restart independently of the date guard, both lower and equal leading numbers, including a delivered intermediate TOUCH. F1b: TERRY October5 4-CLOSEOUT-ASK must stay visible after October21 restarted work and5-RECEIPT. F12: a date gap alone keeps the original visible. An unrelated-desk or unnumbered CLOSE intermediate must not block a valid pair.
8. Test valid single-target receipt/CLOSE links; wrong session/owner/key, missing link, malformed payload and invalid chronology; a subsequent valid working correction keeps the original visible. One receipt never hides all earlier same-desk rows. Preserve open, earlier-receipt/later-spawn, exact-desk, no self-close, stable sorting, no double count and byte-unchanged ledger cases.
9. Preserve source count/header and the complete cadence/no-drain suffix byte-for-byte for identical rows/date/window. The only view changes are the first-table rows/count and one honest omission line splitting total omitted N into E explicit resolves links and L legacy pairs (highest lower-numbered same-desk touch, unique among same-desk same-date touches at that number, no numbering restart between them). Counts are disjoint and sum to N, including zero. The line retains asks/time-correction exclusions.
10. Run all four required commands and record exit codes/results:
   - `python3 scripts/orch_log.py --selftest`
   - `PYTHONPATH="$PWD/scripts" python3 -m unittest discover -s scripts/tests -p 'test_orch_log*.py'`
   - `python3 -m unittest discover -s PROME/tools/tests -p test_orch_closeout.py`
   - `python3 scripts/orch_log.py check`
11. Regenerate with `python3 scripts/orch_log.py view`, measure with `python3 PROME/tools/measure.py PROME/state/ORCH_INFLIGHT.md`, and report bytes, shown/omitted counts and unchanged ledger bytes. If above approximately30,000 B, report it; do not weaken pairing or edit/rotate the ledger to fit.
12. Commit as a NEW commit, exact paths only: scripts/orch_log.py, scripts/tests/test_orch_log_closed_rows.py, this acceptance file and PROME/state/ORCH_INFLIGHT.md. No amend, push, lifecycle-owner edit or other path edit. PROME owns publication. State: IMPLEMENTED + TESTED; post-final-read fix, NOT independently verified. No fourth read is implied or commissioned.

## Declared residue (read 3)

These are evidence limitations of legacy inference, not additional code repairs authorized by this task. Only explicit resolves links, with stable canonical identity and valid chronology, can unambiguously resolve the following cases:

- **F2 — structured receipt without resolves:** an unstructured original can be legacy-paired with a structured receipt lacking resolves; its prose session identity cannot be reliably compared with the payload session. A wrong-session omission remains possible in this shape.
- **G2 — continued numbering:** independent sessions that continue numbering without a restart are indistinguishable from one session's normal1-SPAWN /2-DELIVERED /3-RECEIPT sequence. A wrong-session omission remains possible.
- **G3 — desk-string drift:** an original logged under a qualified desk string and its receipt under an unqualified desk string can cause the receipt to pair with another session's row. Exact desk comparison cannot recover the alias or intended target.
- **G4 — unnumbered CLOSE-only session:** an intervening CLOSE summary provides no numbered TOUCH restart, so the legacy path cannot identify the second session and can pair its later numbered receipt with older work.
- **K1 — late duplicate receipt:** an older-numbered duplicate receipt between a reping and its receipt looks like a restart and leaves the completed reping visible.
- **K2 — same-number DELIVERED companion:** the all-state uniqueness/restart guards keep the completed original visible when a same-number companion exists.
- **K3 — midnight crossing:** a legacy spawn/receipt crossing dates remains visible; validated explicit links may close overnight work.
- **K4 — PENDING prefix on a completed receipt:** text such as Pending items carried; CLOSED remains excluded by form and leaves completed work visible.

K1–K4 are fail-safe visibility costs. F2/G2/G3/G4 are remaining legacy identity ambiguities, including possible wrong-session omissions; they must not be represented as guarantees of liveness safety. This task does not write or invent ledger links. Explicit resolves reconciliation belongs to the canonical lifecycle owner. The earlier19 restored rows remain10 genuinely open asks/spawns plus9 closed-but-unpaired fail-safe records, not19 wrongly hidden rows.

## Execution results

IMPLEMENTED + TESTED; post-final-read fix, NOT independently verified.

Applied the reader's one-condition probe immediately after selecting the unique highest-numbered legacy IN-FLIGHT candidate: count ALL earlier same-desk, same-date TOUCH rows at that number, whatever their delivered state, and reject when more than one exists. Canonical explicit reconciliation and the earlier guards are unchanged.

All required commands exited0:

```text
$ python3 scripts/orch_log.py --selftest
ORCH-LOG SELFTEST ✓ 36/36

$ PYTHONPATH="$PWD/scripts" python3 -m unittest discover -s scripts/tests -p 'test_orch_log*.py'
Ran 41 tests in 0.056s
OK

$ python3 -m unittest discover -s PROME/tools/tests -p test_orch_closeout.py
Ran 27 tests in 0.060s
OK

$ python3 scripts/orch_log.py check
ORCH-LOG ✓ PROME/state/ORCH_LOG.tsv: 1287 data rows × 13 columns, typed cells int-or-EMPTY

$ python3 scripts/orch_log.py view
ORCH-LOG ✓ view regenerated → PROME/state/ORCH_INFLIGHT.md (29571 B, 150 table rows, window 30d)

$ python3 PROME/tools/measure.py PROME/state/ORCH_INFLIGHT.md
PROME/state/ORCH_INFLIGHT.md  29571 B (wc -c)  166 lines (wc -l)  crc32 2303424183  crc32-no-final-nl 2536974261
```

Current ledger:86 IN-FLIGHT TOUCH rows,52 shown,34 omitted, all34 legacy /0 explicit. Compared against the saved ee5be7a1c renderer on identical current rows: the omitted set is identical,0 pairs change. The98 cadence rows remain. The view is29,571 B,429 B below30,000 and2,979 B below32,550. Only the disclosure wording changes on identical input.

Added G1 and G1b as distinct tests, with different triggers and session prose so the guard is tested independently of duplicate-key handling. Both PENDING and DELIVERED rows before the live candidate now block pairing. Added a positive control that another desk/date does not count against uniqueness. All prior38 tests remain passing. Ran the reader's ce3.py with runpy after explicitly loading the workspace orch_log module: G1 and G1b both print PASS; other probes are the declared residue above, not claims of repaired cases.

Production ledger bytes match the pre-code snapshot and immediate before/after view snapshots: SHA-256643ef9a660220592d052e1d7a087357f90f80982e42d3ec95d20a5c1528fc21b. No ledger edit, append or rotation occurred. The source/header and complete cadence/no-drain suffix are byte-identical to the pre-edit working view and the previous renderer on the same rows. The generated file equals the new renderer output.

Existing unclosed-file ResourceWarnings in check/_view_count/append remain outside this bounded change; tests pass. State remains IMPLEMENTED + TESTED; post-final-read fix, NOT independently verified. No additional reader is inferred or commissioned.

Only scripts/orch_log.py, scripts/tests/test_orch_log_closed_rows.py, this acceptance file and regenerated PROME/state/ORCH_INFLIGHT.md are included in the new commit. No push, amend, lifecycle-owner edit, local WALTER anchor update or unrelated edit. Existing foreign working changes are untouched. PROME owns publication and the disposition of declared residue.
