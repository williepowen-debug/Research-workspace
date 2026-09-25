# L417 gate-citability, round 2: independent reader ledger (read-only, Opus)

**NOT VERIFIED: 2 ❌ · 8 ⚠️ · 12 ✅.** The live figure IS verified (0 hits over 22 files, 18 of 18 LIVE rows read). Both ❌ are defects in the correction itself. Both are local fixes of a few lines, but under the read budget this was the allowed third read, so the choice between fix and declared residue is PROME's (or Will's).

**What I ran.** All scripts are in the scratchpad:
- `counterex.py`: CE1–CE10 from round 1, now also printing read/live/unread/short.
- `counterex_r2.py`: R2-1 to R2-12, new this round.
- `hdr_drift.py`: sends a drifted GATES.tsv header through `guard(check_gates_tsv)` using a temporary ROOT.
- `live_cmp.py` and `errpath.py`, re-run.
- The README one-liner, run verbatim.

The boot gate was NOT run and nothing in the repo was written.

**Test counts.** `grep -c 'def test_'` gives 15 in test_prome_gate_citability_L417.py and 7 in test_prome_gate_gates.py. Both suites pass under `-W error::ResourceWarning` (Ran 15 OK · Ran 7 OK).

---

## ❌ (2)

**❌1: The header-drift assertion suppresses the existing BLOCKING legs, including FIRED-UNEXECUTED (a condition 9 regression)**
- **Claim.** The new `GATES_COLS` assertion raises `RuntimeError` inside `check_gates_tsv` before `scan_gates_rows` records anything. A rename in a column that only the citability leg uses (col 10 `definition_surface`) therefore stops the `GATES fired-unexecuted`, `token vocabulary` and `review_by` BLOCK legs from being evaluated. Before the fix none of those legs depended on col 10, so this is new. It breaks condition 9 ("the other `scan_gates_rows` legs are untouched"). It also breaks the gate's own ERROR contract at prome_gate.py:84–86: "Checks that do not need the missing input still run; isolation is per-check."
- **Artifact.** prome_gate.py, `check_gates_tsv`: the `hdr = next(…)` / `raise RuntimeError(f"GATES.tsv header drift …")` block, which sits before `o = scan_gates_rows(rows, today)`.
- **Verification.** `python3 $S/hdr_drift.py $S`, case A: header col 10 renamed `definition_home`, plus a `FIRED-UNEXECUTED 9/25` row appended.
- **Observed.** The ONLY record is `ERROR | check_gates_tsv DID NOT RUN | RuntimeError: GATES.tsv header drift: column 10 …`, with rc 2. The fired row is never reported. The one BLOCK the gate says "must never leave a session" (prome_gate.py:1442 comment) turns into "could not establish" and does not name the fired gate. It is loud, so this is not a silent miss, but it lowers an existing BLOCKING leg's output from "the fired gate, by name" to "check did not run".
- **Proposed change.** Move the header assertion into `record_gate_citability`, or pass `hdr` in and record `ERROR "GATES gate-citability — header drift"` there, AFTER the six existing legs have recorded. Only the citability leg should go dark on citability-column drift. Also replace `test_header_drift_is_loud` with a test that calls the real code path (see ⚠️4).

**❌2: Directory pointers are still missed silently in two shapes, so the ❌1 fix is incomplete**
- **Claim, mechanism (i), prefix allowlist.** `_DEF_DIRLIKE` only recognises `AGENTS|PROME|FORGE|KERNEL/…`. A directory-style pointer under any other top-level directory is neither read nor reported: `FORUM/`, which two LIVE rows already use for their letters (NEXUS-SEAT-01 and OP-SCALE-01), `memory/`, `docs/`, `scripts/`, `MESSAGING/`. The same applies to a `.txt`/`.json` letter under those roots. The row is not in UNREAD, no ERROR is recorded, and rc is 0.
- **Claim, mechanism (ii), directory check only runs when no file was found.** A cell naming a readable summary file AND a directory pointer to the actual letter counts as READ. The coverage line then reports it as read while its letter was never opened. This is the exact defect ❌1 named ("reports clean for a letter it never read"), and this time the new coverage line certifies it.
- **Artifact.** prome_gate.py: `_DEF_DIRLIKE = re.compile(r"(?<![\w./-])(?:AGENTS|PROME|FORGE|KERNEL)/[\w./-]*")`, and `if not got_file:` guarding the directory check in `scan_gate_citability`.
- **Verification.** `python3 -W error::ResourceWarning $S/counterex_r2.py $S`:
  - R2-1: surf `FORUM/review (letter)`, token in `FORUM/review/letter.txt`.
  - R2-2: `memory/auto (slug x)`.
  - R2-12: `FORUM/review/letter.txt`.
  - R2-3: `AGENTS/X/CLEAN.md (summary) + letter at AGENTS/Y/workbook (KB-Y-2)`, where KB-Y-2 in `AGENTS/Y/workbook/KB.tsv` carries `realisation UNKNOWN` and the state is `LIVE — ARMED`.
- **Observed.**
  - R2-1, R2-2 and R2-12 each give `viol=[] unreach=[] read=0/1 unread=[]`, detail `… 0 of 1 LIVE rows' letters read`, with no UNREAD name, no ERROR and rc 0.
  - R2-3 gives `viol=[] unreach=[] read=1/1 unread=[]`, detail `0 hits over 1 files · condition cells: 0 · 1 of 1 LIVE rows' letters read`. A real violation on an ARMED row reads as clean AND as fully covered.
  - The live ledger is not affected today. My scan of the 18 LIVE cells found no directory-like token beside a file and no non-allowlisted directory pointer. LIQUID KB.tsv and FLG TRIGGERS.tsv carry 0 tokens (`grep -cE`).
- **Proposed change.**
  - (i) Derive the prefix set from the repo instead of a fixed four: `{d.name for d in root.iterdir() if d.is_dir() and not d.name.startswith('.')}`. This picks up FORUM, memory and docs, and still skips the prose noise found in live cells (`8/28`, `registry/`, `letter/threshold/state` in BRENT-COT-35B's cell, because `8`, `registry` and `letter` are not top-level directories).
  - (ii) Run the directory check whether or not a file was found. A directory pointer beside a readable file becomes a named ADVISE ("also names X — confirm the letter is in the file(s) read") rather than an ERROR. That avoids false-ERRORs on a prose mention like `owner AGENTS/X/ desk` (R2-10).
  - Add R2-1 and R2-3 as tests.

## ⚠️ (8)

**⚠️1: The coverage count can over-count; "read" and "UNREAD" overlap**
- **Claim.** `read += 1` is set as soon as ANY file on the row passes `is_file()`. It is not reduced when a second path on the same row is missing, or when the file later fails `read_text` (OSError). A row can therefore appear in both K and UNREAD.
- **Artifact.** prome_gate.py, `scan_gate_citability`: `if got_file: out["read"] += 1`, and the per-file `except OSError` branch, which appends to `unreachable` only.
- **Verification.** R2-4 (`AGENTS/X/CLEAN.md + AGENTS/X/MISSING.md`); `errpath.py` (a chmod-000 letter).
- **Observed.** `1 of 1 LIVE rows' letters read · UNREAD: G-O` and `1 of 1 LIVE rows' letters read · UNREAD: G-L`. The ERROR row and rc 2 are correct, but the coverage sentence contradicts itself.
- **Proposed change.** Compute `read = live − len(unread)`, excluding rows with nothing to read (see ⚠️3). A row counts as read only if every path it names was read.

**⚠️2: The duplicate-gate_id fix over-reaches and blames a row that never cites the file**
- **Claim.** The fix checks every LIVE row with that gate_id, not every row that CITES the file.
- **Artifact.** `for row in (x for x in live if x[gi] == g)` in the hit loop.
- **Verification.** R2-5: row 1 `G-D`, `LIVE / NOT ARMED —`, cites UNVER.md; row 2 `G-D`, `LIVE —`, cites CLEAN.md only.
- **Observed.** `VIOLATIONS: G-D → AGENTS/X/UNVER.md`. This fails loud, but the violation is attributed to a row whose letter is clean.
- **Proposed change.** Key `files[p]` on row index, not gate_id.

**⚠️3: A NONE/prose row or a README-only row lowers K without being named, so K<N is not a tell**
- **Claim.** In both cases, `NONE | …` (legitimate under condition 5) and a row whose only surface is `PROME/GATES_README.md`, the row counts in N but not in K, and it is never named. A reader of `17 of 18 read` cannot tell a legitimate NONE from an unread letter. The README-only row is arguably an unread letter: the README is never a letter, so that row has no readable home.
- **Artifact.** The `elif not any(…): out["read"] += 0` branch, which is dead code (`+= 0`).
- **Verification.** R2-6 and R2-7.
- **Observed.** `0 of 1 LIVE rows' letters read` with no name in either case.
- **Proposed change.** Name them separately (`· no letter file (NONE/prose): G-N`) and treat README-only as unread. Delete the dead branch.

**⚠️4: The header-drift test is tautological and does not exercise the gate**
- **Claim.** `test_header_drift_is_loud` re-implements the assertion loop inline against `G.GATES_COLS`. It would still pass if the assertion were deleted from `check_gates_tsv` (`[[finding_test_the_guard_not_just_the_guarded]]`). Also, `if hdr:` skips the assertion when no `gate_id` header line exists. That case is acceptable: `hdr_drift.py` case B shows `token vocabulary` BLOCKs on the header-as-data row.
- **Artifact.** test_prome_gate_citability_L417.py:111–118.
- **Verification.** Read the test.
- **Observed.** The only code it calls is `G.GATES_COLS`.
- **Proposed change.** Test through the real path, as `hdr_drift.py` does: a temporary ROOT with a drifted GATES.tsv, `guard(check_gates_tsv)`, then assert on the records. Once ❌1 is fixed, also assert that `GATES fired-unexecuted` still records.

**⚠️5: The whole-file false-BLOCK exposure grew from 4 to 7 rows, and the declared residue count is stale**
- **Claim.** Re-pointing LIQ-069 and LIQ-072 at `AGENTS/LIQUID/workbook/KB.tsv` and FLG-T08 at `AGENTS/FLG/workbook/TRIGGERS.tsv` adds three rows scanned against a WHOLE shared ledger. A token written on ANY KB-LIQ row now false-BLOCKs 069 (ARMED) and 072. It also cross-attributes: a token on KB-LIQ-076's row is blamed on 069 and 072, never on 076, because 076 cites a `.md` file. The residue block still says "four live rows exposed".
- **Artifact.** GATES.tsv col 11 for the three re-pointed rows; ACCEPTANCE_…L417.md:26 (⚠️6 residue).
- **Verification.** R2-9: `AGENTS/Y/workbook/KB.tsv (KB-Y-1)` with the token on row KB-Y-2.
- **Observed.** `VIOLATIONS: G-T → AGENTS/Y/workbook/KB.tsv (realisation UNKNOWN)` for a clean KB-Y-1.
- **Proposed change.** Update the residue count to seven: FALCON-001, CORAL-MSI-01, FERT-G3, BRENT-COT-35B, LIQ-069, LIQ-072, FLG-T08. Longer term, when a `.tsv` path is followed by a row id (`KB-LIQ-069`, `T-08`), scan only that row. Every re-pointed cell already carries the row id.

**⚠️6: Unrelated failures are labelled "directory-style pointer", and residue ⚠️3 is stale**
- **Claim.** A `.json` letter under `AGENTS/`, or a bare basename, is reported as `(directory-style pointer, no letter file)`, which is the wrong reason. Residue ⚠️3 ("`.json`/`.txt`/`.MD` are not path-like to the regex") is now half-true: `AGENTS/X/spec.json` is an ERROR (CE3), while `FORUM/…/letter.txt` is silent (R2-12, folded into ❌2).
- **Artifact.** The directory branch's label string; ACCEPTANCE_…L417.md:26.
- **Verification.** CE3 and CE10 in counterex.py.
- **Observed.** `AGENTS/X/spec.json (directory-style pointer, no letter file)`.
- **Proposed change.** Label it `(path-like, no .md/.tsv letter file)` and re-word residue ⚠️3.

**⚠️7: Bare row-id second homes beside a `.md` path; which one holds the letter is UNKNOWN**
- **Claim.** GATE-LIQ-076 is `DEALER_POSITIONING_NEXUS_WATCH.md (KB-LIQ-076)` and GATE-LIQ-079 is `FUNDING_SEIZURE_GATE_SCOPED.md (KB-LIQ-079)`. If the canonical letter is the KB row, the leg reads the wrong home. This is INFERRED from the cell shape, which matches the re-pointed 069/072 cells.
- **Artifact.** GATES.tsv, definition_surface for those two rows.
- **Verification.** A regex scan of the live cells for `KB-[A-Z]+-\d+`.
- **Observed.** Row ids appear beside a `.md` path on LIQ-076 and LIQ-079 (and on 069/072/FERT-G3, whose paths point at the KB file). The substance is clean today: LIQUID KB.tsv is read and carries 0 tokens.
- **Proposed change.** Ask the owner (LIQUID) which home holds the letter. Record the answer in the cell. Do not decide it from the shape.

**⚠️8: A short row's condition cell is not scanned**
- **Claim.** A SHORT row (fewer than 11 cells) is routed to ERROR before its condition cell (col 3, which is readable) is checked. A `LIVE —` short row with a token in its condition cell therefore gives rc 2 with no violation named. It stays loud (rc 2, row named), but the BLOCK reason is lost.
- **Artifact.** The `if len(r) <= di: out["short"].append(r[gi]); continue` branch.
- **Verification.** CE4 and `test_reader_ce4_short_row_is_error_not_silent` (the test asserts only ERROR).
- **Observed.** `viol=[] … short=['G-SHORT']`.
- **Proposed change.** Scan `r[ci]` before the `continue` whenever `len(r) > ci`.

## ✅ (12)

| # | Claim | Artifact | Verification | Observed |
|---|---|---|---|---|
| ✅1 | Both suites green | test_prome_gate_citability_L417.py; test_prome_gate_gates.py | `python3 -W error::ResourceWarning -m unittest …` | Ran 15 OK; Ran 7 OK; `grep -c` gives 15 / 7 |
| ✅2 | Condition 9 live figure, one-liner | GATES_README.md:31 | one-liner run verbatim from the repo root | `0 hits over 22 files · condition cells: 0` |
| ✅3 | Condition 9 live figure, the leg | prome_gate.py `scan_gate_citability` | `python3 $S/live_cmp.py` | `0 hits over 22 files · condition cells: 0 · 18 of 18 LIVE rows' letters read`, unreachable `[]`, the same 22 paths as the one-liner (`same True`), 0 short rows |
| ✅4 | The re-pointed cells land on the letters | AGENTS/LIQUID/workbook/KB.tsv:70 (KB-LIQ-069) and :73 (KB-LIQ-072); AGENTS/FLG/workbook/TRIGGERS.tsv:14 (T-08) | `grep -n` | present; 0 tokens in either file |
| ✅5 | CE1 (directory pointer under AGENTS) is now ERROR and named | counterex.py | re-run | `unread=['G-DIR']`, `UNREAD: G-DIR` |
| ✅6 | CE2 (duplicate gate_id, same file) is now a violation | counterex.py | re-run | `VIOLATIONS: G-DUP → AGENTS/X/UNVER.md` (see ⚠️2 for the over-reach) |
| ✅7 | CE3, CE4 and CE10 are now ERROR and named | counterex.py | re-run | `unread=['G-JSON']`, `['G-SHORT']`, `['G-BASE']` |
| ✅8 | CE7 `./PROME/GATES_README.md` is excluded by resolved path | `_never_scan` | re-run | `viol=[] files=0` |
| ✅9 | An unreadable file is caught INSIDE the leg; it no longer reports "check_gates_tsv DID NOT RUN" | per-file `except OSError` | `errpath.py` | `ERROR 'GATES gate-citability — LIVE row letter NOT READ' … G-L → A/locked.md (PermissionError)`, rc 2 |
| ✅10 | No line-ending flip in GATES.tsv | PROME/GATES.tsv | `grep -c $'\r'` on HEAD and on the working tree | 0 / 0 |
| ✅11 | A `§` pointer (`see AGENTS/X/STATUS.md §3`) is read (whole file) and counted read, consistent with the declared residue ⚠️6. A prose-only mention of an agent directory (`see AGENTS/X/ register`) is an ERROR, which is loud and correct under condition 5. `NONE \| … (M-09 successor)` is not an error. | counterex_r2.py R2-8, R2-11, R2-7 | re-run | as stated (R2-8 false-BLOCKs on §7's token, per the residue) |
| ✅12 | Carried-over behaviour is as declared. CE5 (FIRED-UNEXECUTED out of scope), CE6 (line wrap), CE8 (absolute path; read-only) and CE9 (whole-file section scan) are unchanged and match residue ⚠️4, ⚠️5 and ⚠️6. The README MECHANISED clause and the one-liner's silent-drop caveat are present, and the trailing "is DOCKET L417" instruction is folded. | counterex.py; GATES_README.md:31 | re-run; read | as stated (the MECHANISED clause does not yet mention coverage or short rows; cosmetic) |

## Counterexamples this round (my own)
- **Silent misses of a real violation:** R2-1 (`FORUM/` directory pointer), R2-2 (`memory/`), R2-12 (`FORUM/…/letter.txt`) and R2-3 (a file plus a directory pointer, counted READ on an ARMED row). These are ❌2.
- **Loud but mis-stated:** R2-4 (read/unread overlap), R2-5 (duplicate gate_id blames a clean row), R2-9 (`.tsv` row pointer false-BLOCK), R2-6 and R2-7 (K<N with no name).
- **Regression in an existing leg:** `hdr_drift.py` case A (FIRED-UNEXECUTED suppressed by header drift). This is ❌1.
