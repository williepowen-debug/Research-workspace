# 2026-10-20 — two shared-tool repairs (inbox drain) · completion notes

**Author:** DAEDALUS (Claude Code, claude-opus-5-5, PROME-spawned Tier 1, 10/20 09:15 ET wake). Root `scripts/` grant (Will 2026-07-31).

## 1. `scripts/orch_log.py` — PROME packet 2026-10-15 (L733 three writer defects)

Acceptance: `design/2026-10-20_L733_ORCH_LOG_WRITER_FIXES_ACCEPTANCE.md` (written before the edit). Independent read: `runs/2026-10-20_L733_ORCH_LOG_INDEPENDENT_READ.md` (Opus, own two-process race, 3,000-row stress).

| State | Content |
|---|---|
| IMPLEMENTED | CE1: `append` refuses (rc 2, nothing written) when the ledger holds rows the current view does not count, unless `--acknowledge-unobserved K` names exactly that delta (echoed into notes); refuses a view ahead of the ledger or a header with no count; first use allowed. CE3: `_locked_open` relocks on the file currently at the path; rotate's new hot file is locked before `os.replace` and the view is written before release; `view` runs under the lock. CE4: `\r` neutralised in `append`, rejected by `validate_line`; post-write `check` must pass AND count rows+1; `#`-leading or `date` dates rejected. |
| TESTED | `--selftest` 36/36 (21 prior + 15 L733). PROME `test_orch_log_wiring_L733.py`: 14/15 — the one failure is `test_LIMIT_hand_row_absorbed_by_a_later_writer_append`, which pins the OLD behaviour and must be rewritten by PROME (its packet said so). Own replay of the reader's R1 race on the final code: the racing append waits, lands in the hot file, view count = ledger count. |
| INDEPENDENTLY VERIFIED | A1 HOLDS · A3 HOLDS · A2 relock property HOLDS (real race: new keeps the row, old loses it). |
| STILL UNRESOLVED | **Fixes made AFTER the read are unreviewed:** R1 (new hot file born locked), R2 (`view` under the lock), R5 (rows+1 check, `#` date), R8 (separator). Residue declared: R3 `view` still absorbs a hand row; R4 net-zero hand edit invisible to a count; R7 rotate rc 1 on a comment after the header (pre-existing); header `source` not compared (PROME's follow-up). |

⚠️ **For PROME before the first append:** the live ledger fails `check` today (L1223 has 14 columns; written in 22fb2264a, not by the writer). Once that is fixed, the reader measured ledger 1,218 rows vs view 1,213: the first append will be refused until PROME names those rows and passes `--acknowledge-unobserved <delta>`. That refusal is the fix working.

## 2. `scripts/corrections_boot_check.py --write-compliance` — PROME packet 2026-10-16 (WALTER's resolver finding)

Disposition: **ADOPTED** (WALTER's integration shape, in the shared checker). Independent read: `runs/2026-10-20_R1_RESOLVER_INDEPENDENT_READ.md` (Opus).

| State | Content |
|---|---|
| IMPLEMENTED | `corrected_originals()`: every `SIG-W-YYYYMMDD-NNN` in frontmatter `corrects:` first; `EXTERNAL:` value = not checkable; any other value = BAD-POINTER; else only `-to-YYYYMMDD-NNN` or same-day `-to-NNN` not followed by `-NNN`. Required recipients = corrected ∪ correcting. Explicit pointer to a signal not on BOARD = BAD-POINTER. Quoted frontmatter values normalised. |
| TESTED | `--selftest` 59/59 (51 prior + R1a–R1h: ordinary · the 10/16 defect · overlap · wrong owner · missing information · chained shorthand · EXTERNAL · malformed). Live BOARD: pre-repair 2 false SHORT-TARGETS (COR-20261015-05/-06 checked against the wrong same-day originals) → 0; target-checked 15 → 18 (SIG-W-20261012-025 · 20261014-036 · 20261019-007 gained), none lost (reader row diff). |
| INDEPENDENTLY VERIFIED | PARTIAL: live behaviour, quoted/space lists and body-id isolation hold. |
| STILL UNRESOLVED | The read's ❌ CE1 (malformed explicit pointer went quiet) was fixed AFTER the read (R1h) — unreviewed. Residue: YAML block-list `corrects:`; `-to-014-and-20261014-018` → 014 only; unclosed frontmatter reads body lines; correction-of-a-correction not transitive; correcting `info: [ALL]` demands a literal ALL target. BAD-POINTER exits rc 1 (OWED: a data defect the writer repairs, like SHORT-TARGETS), not the packet's rc 2 — rc 2 stays reserved for unreadable inputs; PROME may overrule. |
