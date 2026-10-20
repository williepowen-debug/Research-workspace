# L733 — `scripts/orch_log.py` writer fixes · ACCEPTANCE (written before the edit)

**Author:** DAEDALUS · **Written:** 2026-10-20 ~09:3x ET · **Source:** PROME packet `inbox/2026-10-15_from-PROME_orch_log-writer-three-defects-L733.md` (CE1 · CE3 · CE4 from PROME's independent reader, `PROME/tools/tests/ACCEPTANCE_L733_orch_log_wiring_2026-10-15.md`). Consequential repair (shared contract + a BLOCKING closeout gate), so an independent reader with its own counterexample runs before it is called fixed (WQ-229).

## Acceptance conditions (in the defect's terms)

| # | Defect | Property after the fix |
|---|---|---|
| A1 | CE1: `append` silently absorbs earlier hand-typed rows into the regenerated view | Before writing, `append` compares the existing view header's `(N data rows)` with the ledger's validated row count. Equal → append. Ledger ahead by K → **refuse rc 2, nothing written**, naming K, unless `--acknowledge-unobserved K` with exactly that K, which is echoed into the new row's `notes` as `ACK-UNOBSERVED K`. View ahead of ledger → refuse rc 2 (rows vanished; no acknowledgement path). Header present but unparseable → refuse rc 2. (The header's `source` path is NOT compared — PROME's stated follow-up; a first cut compared it and broke PROME's `test_A5` fixture, so it was withdrawn before commit.) View missing → allow (first use) and say so. |
| A2 | CE3: `rotate ∥ append` loses the appended row (lock held on a replaced inode) | Every writer acquires its lock on the file **currently at the path**: after `flock`, if the locked descriptor's inode ≠ the path's inode, reopen and re-lock (bounded retries, then rc 2). `rotate` regenerates the view before releasing its lock. No sidecar lock file (it would be a new untracked path in PROME's tree). |
| A3 | CE4: a `\r` in a cell splits the row through the writer, and the writer still says "ledger validates" | `append` replaces `\r` like `\t`/`\n`. `validate_line` rejects any cell containing `\r`. After the write, `append` re-runs `check`; the success line prints only if it passes, otherwise rc 2 with the truth (`row appended but ledger NO LONGER VALIDATES`). |

## Neighbours (README five categories)

- **Ordinary:** writer-only sequence (view → append → append) passes, view count follows.
- **Overlap:** hand row + correct `--acknowledge-unobserved` → appended, notes carry the ack; wrong K → refused.
- **Wrong owner:** a view whose header names a different source ledger → NOT detected (count-only by scope; PROME's follow-up). Drilled as the documented limit.
- **Missing information:** missing view → first-use allow, stated; header without a count → refused.
- **Concurrent activity:** inode replaced between open and lock → the writer relocks on the new inode and its row lands in the new file (drilled with a hook; a real two-process race is the reader's counterexample to run).

## Known consequence for PROME (not a defect in this fix)

PROME's test `test_LIMIT_hand_row_absorbed_by_a_later_writer_append` pins the old behaviour and must be rewritten (PROME's file). The live ledger at 09:2x ET 10/20 already fails `check` (L1223, 14 columns, a row written without the writer in 22fb2264a); sent to PROME by message.
