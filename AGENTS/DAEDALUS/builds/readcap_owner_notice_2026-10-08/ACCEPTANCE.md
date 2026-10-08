# L530 open leg — read_cap_check OWNER-DIRECTED NOTICE · acceptance conditions (written BEFORE code, WQ-229)

**Written:** 2026-10-08 08:2x ET (DAEDALUS fork, PROME `prome-fc` wake). **Row:** `PROME/DOCKET.tsv` L530, open leg *"a path declared whole in READS.tsv by ANY reader is measured for its OWNER"*, reconciled with `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` rule 15 (the read is counted in the READER's perimeter; *"a breach found there emits an OWNER-directed notice"*).

**Defect, in its own terms:** rule 15 promises the owner a notice when another desk's declared whole read of the owner's file breaches. The instrument has no such channel: the breach prints only in the READER's run (and turns the READER's rc red), while the OWNER — the only desk that can rotate the bytes (rule 4) — runs `--agent OWNER` and never sees the file. Live 2026-10-08 08:3x ET: `--agent WALTER` shows `🟠 AGENTS/HANS/registry/THRESHOLDS.tsv 33,544 B 103% of budget (whole · WALTER:6b)`; `--agent HANS` (heuristic perimeter, 0 READS.tsv rows) never names the file.

## Conditions (each must hold after the change)

| # | Condition |
|---|---|
| A1 | `--agent X` prints an OWNER-DIRECTED NOTICE section listing every READS.tsv `READ` row whose `reader` ≠ X, whose mode is cap-bearing (`whole`/`programmatic`, not RETIRED), and whose path (or, for a CLASS row, each expanded member) lies under X's home. Each line carries: path, bytes, % of budget, the grade() band/mark, and every foreign `reader:step` that loads it. |
| A2 | The notice is NOT cap-bearing in X's perimeter: X's measured count, over-budget count, over-cap count and **rc are unchanged by default** on every desk (rule 15 keeps the count where the context is paid). |
| A3 | Reuse, never a second parser: the notice reads the manifest through the existing `load_reads()`, expands CLASS rows with the SAME member expansion `declared_reads()` uses (factored into one helper both call), and grades with the existing `grade()`. |
| A4 | Overlap: a file X ALSO reads itself (in its declared or heuristic perimeter) appears ONCE — in X's own table, annotated `ALSO read whole by <reader:step>` — and is not repeated in the notice. Two foreign readers of one file → one notice line naming both. |
| A5 | Wrong owner: READS.tsv has no `owner` column today (header verified 2026-10-08). Owner = the desk whose home contains the path. If an `owner` column is ever populated and it disagrees with the path (owner names X but the path is not under X's home, or the path is under X's home but owner names another desk), the row is printed as an OWNER/PATH DISAGREEMENT finding and is NOT silently attributed either way. Files under `AGENTS/X/sub_agents/<S>/` belong to sub-agent S, not X. |
| A6 | Missing information: manifest unreadable/absent at notice time → the section prints `UNKNOWN` (never a clean "no foreign readers" line) and the machine line carries `owner_notices=UNKNOWN`. A concrete foreign row whose file is missing on disk prints as `DOES NOT EXIST — the reader's manifest defect`, never as 0 B. |
| A7 | Clean case watched (CHECK_STANDARD §3): a desk with no foreign cap-bearing reads prints one explicit clean line naming what was scanned. |
| A8 | Machine line: keys ADDED, none renamed or reordered among existing keys except that the two new keys sit before `charter_bytes`, which stays LAST (rule 20 leg R20 unchanged). `owner_notices=<n|UNKNOWN>` and `owner_notices_over_budget=<n|UNKNOWN>`; assessed=0 lines carry 0. |
| A9 | Opt-in variant `--owner-notice-blocking` (OFF by default, `--agent` only): a foreign-read file of X at 🟠/🔴 makes X's rc ≥1; notice UNKNOWN makes it 2. It prints that it is a **CANON QUESTION for PROME/Will** (it would move rule 15's verdict onto the owner) and is not adopted by this patch. |
| A10 | Existing suite unchanged in meaning: the 112 existing selftest legs pass; new legs are added inside `--selftest` with frozen tempdir fixtures and `EXPECTED_LEGS` moves in the same edit; the new legs FAIL on the unpatched file and PASS on the patched one. `AGENTS/DAEDALUS/tests/test_read_cap_catchup_20261003.py` passes before and after. |
| A11 | Live rc for `--agent HANS`, `CREED`, `WALTER`, `DAEDALUS` identical before/after (default mode); HANS's run names THRESHOLDS.tsv in the notice. |

## Neighbours (WQ-229 five categories)
- **Ordinary:** HANS THRESHOLDS read whole by WALTER:6b → one notice line, 🟠, rc unchanged (A1/A2/A11).
- **Overlap:** owner also declares/scans the file → annotated once in its own table (A4); a foreign CLASS row and a foreign concrete row on the same file → one line, both readers.
- **Wrong owner:** owner column vs path disagreement (A5); sub-agent subtree excluded from the parent (A5).
- **Missing information:** manifest UNAVAILABLE → UNKNOWN, fail-closed wording (A6); concrete foreign file missing on disk (A6); a foreign CLASS row matching 0 members contributes nothing (its empty-class verdict belongs to the reader's own run, unchanged).
- **Concurrent activity:** N/A for the code path — the check is read-only and re-reads the manifest at run time; a manifest edited between the desk's own read and the notice read can only yield UNKNOWN (A6), never a silent clean. No lock or state file is introduced.
