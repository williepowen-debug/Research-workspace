# L733 orch_log.py writer fixes — independent result read (2026-10-20)

Scope: working-tree `scripts/orch_log.py` vs `scratchpad/orch_log_before.py`. All experiments were run on temp fixtures under `scratchpad/reader/` (harness `slowrot.py` imports the module by path in a SEPARATE process and slows one phase). Nothing in the repo was written. Author selftest: 34/34 (new), 21/21 (pre-repair).

## Ledger

| id | class | claim | command | observed | proposed fix |
|---|---|---|---|---|---|
| R1 | ⚠️ | A2 says "`rotate` regenerates the view before releasing its lock, so no appender sees the new ledger with the old view." That is false. The lock rotate holds is on the OLD inode, and an appender that opens the path after `os.replace` locks the NEW inode straight away. | Two processes: `slowrot.py view` (rotate with render_view +2 s), then a real CLI `append` at +0.5 s (`reader/B/`) | append rc 2: "view counts 40 rows but the ledger holds 3 — 37 row(s) VANISHED"; nothing written; rotate rc 0 | Safe (it fails closed), but the message makes a false accusation, and the stated mutual exclusion does not exist. Write the view BEFORE the hot `os.replace` (render it from `hot_rows_after`), or have rotate also flock the new file before replacing. Correct the A2 text. |
| R2 | ⚠️ | A writer-only sequence can be refused falsely. `view` (`write_view`) takes no lock, so `view ∥ append` leaves the view stale by one row. The next append is refused and blames a writer row as "entered without this writer". The ack path would then stamp `ACK-UNOBSERVED 1` on a row that was never hand-typed. | `slowrot.py view … view` (render +2 s) ∥ CLI append W1, then append W2 (`reader/C/`) | W1 rc 0; view header shows 5 rows, ledger 6; W2 rc 2 "1 row(s) entered without this writer" | Run `write_view` in `view` mode under `_locked_open(path)`. The lock gap is old, but this repair is what makes the stale view consequential. |
| R3 | ⚠️ | `view` still absorbs a hand row silently. The refusal text even tells the operator to run `view`. PROME's 10/15 acceptance ⚠️2 had already asked for a guard on `view`. | (by reading) `main` → `write_view` has no count comparison | The hole is narrowed to "the last write was `view`/`rotate`", not closed | Scope note for A1: it covers append only. Either `view` refuses a count rise without `--acknowledge-unobserved K`, or the docs state the limit at the OBSERVED sites. |
| R4 | ⚠️ | The count-only check misses a net-zero hand edit: delete one row and hand-add one row. | `sed -i` delete AC row + printf HAND2 row, then append (`reader/P/`) | append rc 0; HAND2 absorbed | Known class (count-only). Record it in the declared limit beside the `source` limit, or compare a crc of the row text in the view header. |
| R5 | ⚠️ | A post-write check that passes does not prove the row is visible. `--date "#x"` passes `validate_line`, gets written, and `check` then skips it as a comment. The success line prints, but the row is invisible to check and view. This is pre-existing, and the same class as CE4 (a cell changes how the row parses). | `append --date "#x" --desk HID` | rc 0 "✓ appended … validates after the write"; check shows 15 rows before and after; `grep -c HID` = 1 | After the write, assert `len(rows_after) == len(rows) + 1`. Have `validate_line` reject a leading `#` in `date`, and `date == "date"`. |
| R6 | ✓ | The post-write check does report the truth when the ledger breaks. | `append --date date --desk HDR` | rc 2 "row appended but the ledger NO LONGER VALIDATES"; view not regenerated; the next append is refused | — |
| R7 | ⚠️ | `rotate` crashes on a comment line placed after the header. `_split_ledger` treats it as data, and `_is_inflight` raises IndexError. Exit code is 1 with a traceback, which breaks the rc 0/2 contract. Nothing is written. Pre-existing (the pre-repair copy also crashes). Live ledger today: 0 such lines. | `echo "# hand comment" >> L; rotate --through 2026-09` (new and old) | Traceback, rc 1, both versions | Skip lines starting with `#` after the header in `_split_ledger`, matching `check`. Not this repair's defect. |
| R8 | ⚠️ (cosmetic) | Ack with empty notes writes `ACK-UNOBSERVED 1;` with a dangling semicolon. | `append … --acknowledge-unobserved 1` (notes empty) | notes = `ACK-UNOBSERVED 1;` | Join with `"; ".join(filter(None, …))`. |
| R9 | info | When this lands, the live ledger will refuse the first append. | `check` (live, read-only) vs the view header | ledger 1218 rows; ORCH_INFLIGHT.md header 1213 | Expected by design. PROME must name 5 rows and pass `--acknowledge-unobserved 5`. Tell PROME before landing. |

## Counterexamples that PASS

| id | probe | observed |
|---|---|---|
| P1 | **Real two-process CE3 replay**: rotate slowed 2 s in its first `check` ∥ CLI append at +0.5 s (`reader/A/`); control on the pre-repair copy (`reader/A0/`) | NEW: RACER in hot = 1, archive = 0, view 4 = ledger 4. OLD: RACER in hot = 0, archive = 0 (the CE3 loss reproduced, rc 0) |
| P2 | Stress: real rotate on a 3,000-row ledger ∥ 12 CLI appenders at 30 ms spacing (`reader/T/`) | 12/12 rc 0; 12 rows in hot, 0 lost; conservation 3001 == 4 + 2997; view 15 = ledger 15 |
| P3 | Refusal writes nothing | sha1 of ledger and view, inode and mtime all unchanged after a refused append |
| P4 | `--acknowledge-unobserved 0`: with delta 0 | rc 0 (0 equals the delta; acceptable) |
| P4b | `--acknowledge-unobserved 0`: with delta 1 | rc 2 "(you passed 0)" |
| P4c | `--acknowledge-unobserved -1`: with delta 0 | rc 2 |
| P5 | Writer-only sequences (no false refusal) | first use, CLOSE row, hand comment line, `view` → append, `rotate` → append: all rc 0 |
| P6 | CRLF ledger file (WSL) | check passes in old and new (universal newlines); `validate_line`'s `\r` rule does not misfire |
| P7 | Path deleted while waiting on the lock | bounded retries, then rc 2, no stray file left |
| P8 | Regressions | none found in check/append/rotate output except the reworded success line. No consumer greps "ledger validates" (`grep` over PROME/tools, scripts, CLOSEOUT.md) |

## Verdicts

- **A1 — HOLDS** for `append` as specified: hand row, wrong K, right K, view ahead, missing view and missing count were all drilled and match. The ⚠️ items (R2 false refusal, R3 `view` absorbs, R4 net-zero) bound what A1 achieves. They are not breaches of its letter.
- **A2 — PARTIAL.** The relock-on-current-inode property HOLDS: the real race no longer loses the row (P1, P2), and the pre-repair copy still does. The second clause, "view regenerated before release, so no appender sees new ledger + old view", FAILS: R1 shows an appender doing exactly that. The failure is refuse-safe but carries a false message.
- **A3 — HOLDS**: `\r` is neutralised, `validate_line` rejects it, and a broken ledger after the write is reported (R6). The neighbour R5 (row written but invisible, success printed) should get the row-count assertion.
