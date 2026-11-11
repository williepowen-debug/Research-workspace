# intake_scan.py news catch-up repair — acceptance conditions (written before the edit)

**Authority:** WQ-676, Will 2026-11-11 14:16 ET via PROME prome-2b ("A repair"). Repair only; the one-time re-read of the 10/19, 10/20, 10/25, 10/27 and 11/07 batches is HELD until PROME confirms Will's reading.
**Defect:** `collect_alerts()` reads the four news classes (NEW_ALERT and NEW_WATCH as per-batch counts; NEW_WATCH_HIT and DEVELOPMENT per item) only from liveness `newsweep.saved`, the newest batch. A batch replaced before a WALTER run is never scanned. Measured: 5 of 30 batches 10/12–11/10 with no scan evidence, 85 of 610 class items (upper bound).
**Repair:** read every `data/<day>/news.json` newer than `last_marked_batch` (stored by `--mark` in `intake_seen.json`) up to and including the newest, and emit the same records. No new state file, no new queue, no new check.

## Acceptance cases (each must hold; executable in `tools/test_intake_catchup.py`)

1. **Install, no replay:** an `intake_seen.json` without `last_marked_batch` scans ONLY the newest batch, exactly as before.
2. **Catch-up:** with `last_marked_batch` = batch D1 and batches D2, D3 newer (D3 newest), the scan emits per-item WATCH_HIT and DEVELOPMENT records from D2 AND D3, and per-batch NEW_ALERT / NEW_WATCH count records for D2 (from the file) and D3, with the existing key formats (`news:WATCH_HIT:<sha12>`, `news:DEVELOPMENT:<sha12>`, `news:<CLASS>:data/<day>/news.json`).
3. **No re-read of the marked batch or older:** nothing from D1 or earlier is emitted once D1 is marked.
4. **Pointer at newest:** `last_marked_batch` equal to the newest batch scans the newest batch only (current behaviour: still-true keys suppressed, nothing new).
5. **--mark advances:** `--mark` stores `last_marked_batch` = the newest batch path and keeps the existing reconcile of `seen` unchanged in semantics.
6. **Unreadable older batch fails loud:** an unreadable batch in the range yields a `news:UNREADABLE:<path>` record; other batches still scan.
7. **Bad pointer fails loud, never silent:** an unparseable or nonexistent pointer falls back to the newest batch only AND prints a visible MED health line saying catch-up is OFF.
8. **Unchanged elsewhere:** FRED, EIA, CFTC, EDGAR, Treasury records, the cruise and GPU queues, and the existing test files pass unchanged.
9. **Visible range:** the text report states which batches were scanned (count and first..last).

## Review
An independent reader (fresh context, not WALTER's session) reads the diff against these nine cases before it is called fixed. Verdict recorded in `REVIEW.md` here.

## Added after the independent read (REVIEW.md, VERDICT: FAIL; fixes in `intake_scan_fixes.diff`)
10. **Scan and mark on different lane states (F1):** `--mark --through <batch the report showed>` is refused, nothing written, if the newest lane batch changed; the report prints the exact command. `--mark` without `--through` still works and prints a WARNING.
11. **Case 7 completed (F2):** a parseable pointer whose file is missing falls back to the newest batch, consistent with the MED line.
12. **Unreadable batch (F3):** `--mark` stores the pointer just before the first unreadable batch in the range, so a repaired file is scanned next time.
13. **Pointer ahead of the lane (F4):** MED health line; `--mark` never moves the pointer backward.
14. **Missing saved path (F5):** the pre-repair NEW_ALERT and NEW_WATCH count records are still emitted. **Enumeration (F6):** only YYYY-MM-DD day dirs count; an unreadable data/ dir is a MED line; day dirs without news.json inside the range are a LOW line.
Test strength (F7): test_3 uses four batches and asserts an item the old newest-only code could not emit; test_2 asserts the marked batch is absent. Note (F8a): the newest batch file is now always read, so per-item records appear even if `by_class` undercounts them.
