# L736 writer follow-through — October20

Completed DAEDALUS writer remedy for item7: standalone `orch_log.py view` refuses positive/negative count mismatch and malformed baseline, under the existing current-inode lock. Positive mismatch names the exact delta and legitimate next append acknowledgment; view cannot accept an ignored nonzero acknowledgment. Equal/missing baseline renders; missing explicitly disclaims provenance. No live PROME ledger/view writes.

Prior October20 post-review fixes R1/R2/R5/R8 independently verified with counterexamples and concurrent processes. New7 tests and existing36 selftests pass. Independent final review ACCEPT at source SHA256e84f5601735ab85a97931d4c2b57f1f62e7d2b81ef9119f1f0ae5d87f1429aac; raw report `2026-10-20_L736_FOLLOWTHROUGH_READER_REPORTS.md` (same directory). Acceptance `../design/2026-10-20_L736_VIEW_ACCEPTANCE.md`.

REVIEW: required — changed guard scope; reader l736_review inspected acceptance, code delta, CLI dispatch and consumer contracts; own refusal/recovery probes and both races pass; APPLIED refusal-only remedy. No post-review source edits.

Limits: count-neutral edits, missing-view initialization, rotate/internal write_view still cannot establish provenance; source comparison remains PROME’s. Invalid rows must be repaired before rendering. An already-committed row whose view write failed may require a legitimate next append or evidence-based owner repair; no invented event to clear an alarm. Full L736 is OPEN: owner procedure/gate/test edits and tier definition remain. No tier enum imposed before PROME publishes a single canonical definition.

Consumer packet tells PROME to replace blanket check→view recovery, revise old absorption fixture, and state the L675 interaction. Existing root CHECKS row updated; original cell recoverable in prior Git revision. Runtime Codex/OpenAI; repository root resolved explicitly. Native fleet transport unavailable; durable packet is notification pending consumption, not acknowledgment. Shared WALTER cache paths prevented start pull; no foreign state touched.
