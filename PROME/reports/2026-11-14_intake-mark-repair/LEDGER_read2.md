# Independent read 2 (follow-up): intake `--mark` correction 7f317a5e18

**VERDICT: REJECT, 1 BLOCKING finding (❌ = 1, ⚠️ = 3, ✅ = 12).**

The correction does what it says about the stored fingerprint: `last_marked_sha` is now the value the receipt check verified, and read 1's CX1 race is closed. Every passing property from read 1 still holds, R6 to R8 fail on 4b590d0c0d and pass now, the printed command runs as written, and the held-pointer path behaves correctly in all four variants I tried.

One hole of the same kind is left. **Which batches the pointer advances over** is still decided by a second read made after the receipt check: `mark_pointer` re-parses every batch with `read_batch_items`. A batch that was missing or unreadable at the scan, and still at the mark's receipt check, can become readable in that gap. The pointer then moves onto it or past it, even though the scan never presented its content, and the content is never scanned afterwards (CX-A, CX-B). This is narrower than L1. It needs a batch that is unreadable at both reads and then repaired inside a window of a few milliseconds within one process. It also existed in 4b590d0c0d; read 1 did not name it and this correction did not open it. Even so, it meets the stated blocking test (unread bytes recorded as acknowledged), and claim C1's "no second read" does not hold for the pointer. A fix of about ten lines on a scratch copy closes both cases and passes the author's 22 tests. The fix judges readability from the same bytes the receipt hashed.

Reader: independent follow-up reader 2 (Opus), 2026-11-14, about 14:40 to 14:55 ET. Scope: the diff of 7f317a5e18 only. The repository was read-only. Every run used a temporary fixture under `/tmp` (the `CatchUp` fixture, or a scratch copy whose `LANE` points at a scratch lane). The live lane and the live `intake_seen.json` were never touched. Scratch: `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c399d57d-9eb0-4dc3-b343-21c0f3e9d0d8/scratchpad/reader2/`.

## Assertion ledger

Five fields: claim → artifact (file:line at 7f317a5e18) → command → observed → proposed change.

| # | Mark | Claim | Artifact | Command | Observed | Proposed change |
|---|---|---|---|---|---|---|
| M1 | ❌ | C1: "`--mark` stores the fingerprint the receipt check verified, with no second read of the file"; property: a mark never acknowledges bytes the scan did not present | `AGENTS/WALTER/tools/intake_scan.py:764` (receipt read) → `:787` `mark_pointer` → `:296` `read_batch_items(b)` (a second read, which decides how far the pointer moves) → `:788-790` | `python3 -B cxA_missing_newest_appears_in_window.py`; `python3 -B cxB_unreadable_middle_repaired_in_window.py` (each injects the change inside `mark_pointer`, after the receipt check) | **CX-A:** 11/04 is missing at the scan and at the receipt check (the fingerprint prints as `None`), then appears in the gap. Mark rc 0; pointer → 11/04; `last_marked_sha: None`. When the next day arrives, the scan reads only 11/05 and the hit in 11/04 is never surfaced, with no health line. Control, where the file appears just after the mark: pointer held at 11/03 and the hit surfaced. **CX-B:** 11/03 is `{broken` at the scan (shown as unreadable) and at the receipt check, then repaired in the gap. Mark rc 0; the pointer jumps past 11/03 to 11/04, and the repaired hit in 11/03 is never surfaced. Control with no race: pointer held at 11/02 (author's F3). | Decide readability from the bytes `scan_receipt` hashed (one read gives both the sha and the parse), have `mark_pointer` use that map, and treat a `None` sha as unreadable. Scratch patch `fixcopy.diff`: CX-A then holds at 11/03 and replays 11/04; CX-B holds at 11/02 and surfaces the hit; author suite 22/22; CX-C and CX-E unchanged (`fixcopy.out`). Return the map from `scan_receipt` rather than using a module global as my scratch copy does. |
| M2 | ⚠️ | C8: BOOT_PROTOCOL 7e(e2) "The pointer never moves backward and stops before an unreadable batch"; "the stored `last_marked_sha` is the fingerprint the receipt check verified" | `AGENTS/WALTER/design/BOOT_PROTOCOL.md:73` | read, plus CX-A and CX-B | Under M1 the pointer passes a batch that was unreadable in the receipt. The "verified" fingerprint can be `None` (CX-A), which turns off rewrite detection for that batch (`rewritten_marked` returns None when there is no stored sha). Every other part of the wording matches the tool. | Holds once M1 is fixed. No separate edit needed. |
| M3 | ⚠️ | C4: the receipt binds each alert's key and raw reading deterministically | `intake_scan.py:240-242` | `python3 -B cxD_command_as_written_and_determinism.py` | Same receipt across 4 `PYTHONHASHSEED` values, with fred, eia, cftc, edgar (nested dict) and treasury alerts and float-like readings. No raw value contains a clock or an age: a liveness re-run with the same alerts still marks (rc 0), so failing closed does not make the tool unusable. Residue: `.replace("\n", " ")` makes a raw `a b` and `a\nb` hash the same (True). That is harmless for a reading but not strictly the bytes. | none (note only) |
| M4 | ⚠️ | Out of the diff, noted only: the receipt does not bind an alert's ROUTE | `intake_scan.py:367-372` `_edgar_route(cid)` reads `data/*/edgar_8k.json`, which is not hashed | read | A change of an EDGAR filing's `route_to` between the scan and the mark would pass the receipt. The instructions claim only "key or reading", so they are accurate. This is older than both commits. | none here; owner's call whether a route belongs in the receipt |
| M5 | ✅ | C1 on the stored sha: the stored value equals the receipt's own value | `:788-790` | author R6; `cxC` | R6 passes; mark#2 in CX-C stores exactly the sha of the bytes just scanned | none |
| M6 | ✅ | C2: a pointer outside the fingerprinted set is refused, state unchanged | `:796-798` | `cxE` (patched `mark_pointer` returns `data/2026-10-01`) | rc 2, state bytes unchanged. As written, `mark_pointer` only returns a member of `batches` or `last_marked`, so this branch is defensive and cannot be reached without the patch. | none |
| M7 | ✅ | C2 edges: empty batch list, `--through` older than `last_marked`, saved path None | `:787-798`, `:769` | `cxE` | `saved` missing with a stored pointer: rc 0, pointer and sha kept. With no pointer: rc 0, no pointer keys written. `--through` 11/02 when the pointer is at 11/04: rc 2, unchanged, no receipt disclosed. | none |
| M8 | ✅ | C3: a held pointer keeps the right fingerprint; a rewrite neither replays forever nor is silently missed later | `:791-794` | `python3 -B cxC_held_pointer_rewrite_cycle.py` | Same-day newest rewritten (rw1), scanned and marked: stores the rw1 sha (not the old one). Rescan with no change: no rewrite line. A later rw2 is detected and its hit shown. C3b (older marked batch rewritten, next batch unreadable): pointer held ON it with the presented rewrite's sha, and a later rewrite is re-scanned. C3c (the held batch rewritten into unreadable bytes): stores the unreadable bytes' sha, and once it is repaired it is re-scanned and the hit surfaced. C3d (pointer ahead, F4): pointer and stored sha `feedfacecafe` kept. | none |
| M9 | ✅ | C4/R7: a changed reading under the same key is refused | `:240-242` | author R7 | passes now, fails on 4b590d0c0d | none |
| M10 | ✅ | C5: no refusal path discloses the current receipt | `:766-773`, `:797` | `cxE` | Stale-receipt, no-receipt, `--through`-mismatch and older-`--through` refusals: none contain the current receipt. The `--json` scan still carries `receipt`, but that is a scan, not a refusal. | none |
| M11 | ✅ | C6: the printed command runs as written from the repository root and omits `--through` when the saved path is missing | `:861-863` | `python3 -B cxD_command_as_written_and_determinism.py` (a scratch copy at `fakeroot/AGENTS/WALTER/tools/`, `LANE` → scratch lane, run from `fakeroot`); `ls AGENTS/WALTER/tools/intake_scan.py` from the real repository root | With saved: `python3 AGENTS/WALTER/tools/intake_scan.py --mark --through data/2026-11-04/news.json --receipt 62c2e4bec0c4` → rc 0 verbatim. With saved missing: `... --mark --receipt f213a98c5110` → rc 0. The real path exists from the repository root. | none (cosmetic: the module docstring at `:22-29` still shows `tools/intake_scan.py`; it is not in this diff) |
| M12 | ✅ | C7: R6, R7 and R8 each FAIL on 4b590d0c0d and pass now | `AGENTS/WALTER/tools/test_intake_catchup.py:238-272` | old scanner extracted to `reader2/old/`; `python3 -B -m unittest test_intake_catchup.CatchUp.test_R{6,7,8}…` (output `c7_old.out`); current suite `python3 -B test_intake_catchup.py` | Old: R6 FAIL (`'18eb2080b0d4' != '6a4b8874afaf'`), R7 FAIL (`0 != 2`), R8 FAIL (the current receipt was found in the refusal text); whole old suite 19 pass, 3 fail. Current: 22/22 OK. | none |
| M13 | ✅ | Read 1 property: a refusal exits non-zero and leaves the state byte-identical | `:766-773` | `cxE` | rc 2 and bytes unchanged on all 4 refusal paths, and on the earlier-batch rewrite (P4) | none |
| M14 | ✅ | Read 1 property: an unchanged lane marks cleanly | — | `cxE` P2; `cxD` | rc 0 | none |
| M15 | ✅ | Read 1 property: a rewrite after a successful mark is replayed | `rewritten_marked` | `cxE` P3 | 11/04 re-scanned and its hit surfaced after the day moved on | none |
| M16 | ✅ | C8: other instruction text matches the tool | `AGENTS/WALTER/CLAUDE.md:59` 7e(e); `BOOT_PROTOCOL.md:69`; `walter_doctor.py:322` | read; grep for other callers of `scan_receipt` | All three point to the exact printed command and the "key or reading" scope. The only caller of `scan_receipt` is `main` (`:764`); tests use `main` through argv, so the change in return shape affects nothing else. | none |

## My counterexamples (scripts and observed output)

All files are in `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c399d57d-9eb0-4dc3-b343-21c0f3e9d0d8/scratchpad/reader2/`. `common2.py` imports the repository's `test_intake_catchup.CatchUp` fixture and asserts that `LANE` and `SEEN` are under `/tmp`. Every run used `python3 -B`.

**CX-A: `cxA_missing_newest_appears_in_window.py`** (`cxA.out`)
```
scan receipt: b7665cde2514 | fingerprint lines: ['  data/2026-11-04/news.json  None']
mark rc: 0 | last_marked_batch: data/2026-11-04/news.json | last_marked_sha: None
hidden hit key recorded as seen: False
next scan batches: ['data/2026-11-05/news.json']
next scan surfaces the hidden hit: False
next scan health mentions 11/04: []
CONTROL mark rc: 0 | pointer: data/2026-11-03/news.json | next batches: ['data/2026-11-04/news.json', 'data/2026-11-05/news.json'] | hidden hit surfaced: True
```

**CX-B: `cxB_unreadable_middle_repaired_in_window.py`** (`cxB.out`)
```
scan shows 11/03 unreadable: True
mark rc: 0 | last_marked_batch: data/2026-11-04/news.json | sha: 6a4b8874afaf
next scan batches: ['data/2026-11-05/news.json']
repaired 11/03 hit ever surfaced: False
CONTROL (no race) rc: 0 | pointer: data/2026-11-02/news.json
```

**CX-C: `cxC_held_pointer_rewrite_cycle.py`** (`cxC.out`): all held-pointer variants are correct (M8).

**CX-D: `cxD_command_as_written_and_determinism.py`** (`cxD.out`): printed command verbatim → rc 0 with and without a saved path; one receipt across 4 hash seeds; newline/space collapse True (M3, M11).

**CX-E: `cxE_regressions_and_edges.py`** (`cxE.out`): read 1 properties P1 to P4, C2 edges, C5 disclosure (M6, M7, M10, M13 to M15).

**Fix check: `fixcopy/` + `fixcopy.diff`** (`fixcopy.out`): a scratch copy with readability taken from the receipt's own read. CX-A: pointer held at 11/03, next scan `['…11-04…', '…11-05…']`, hit surfaced True. CX-B: pointer held at 11/02, 11/03 re-scanned, hit surfaced True. CX-C and CX-E: identical results. Author suite on the copy: 22/22 OK. The repository file was not edited.

## Neighbour classes

- **Ordinary:** M14 and M11 (unchanged lane; printed command).
- **Overlap:** M8 (held pointer on a rewritten batch; pointer ahead), M9 and M3 (reading under the same key).
- **Wrong owner / other caller:** M16 (no other caller of `scan_receipt`); M4 (route not bound, older than both commits).
- **Missing information:** M7 (saved None, empty batch list, no pointer); CX-A (newest file missing).
- **Concurrent activity:** M1 (CX-A, CX-B). Two `--mark` processes at once: not checked.

## What I did NOT check

- The real width of the M1 window on live batch sizes. I did not measure it. Read 1 measured about 1.7 ms median on a synthetic 97.5 KB batch for the same gap, so INFERRED: a few milliseconds. Also not checked: whether the live collector or `git pull` can actually leave a batch missing or unreadable across both the scan and the mark. M1's real-world likelihood therefore rests on that unknown; the mechanism is VERIFIED.
- The author's declared residue: the earlier-batch window (L2), a mark with liveness missing returning rc 0, the double read inside the scan, and the "@sha" suffix re-alert. None of them tripped in my runs.
- `test_cruise_capital_review.py`, `test_gpu_finance_review.py`, `test_boot_repairs.py`, the `boot_basis_hashes.json` re-hash, and the committed witness under `research/2026-11-14_intake-receipt/`.
- Two concurrent `--mark` processes, and a crash during the non-atomic `SEEN.write_text`.
- `python3 AGENTS/WALTER/tools/intake_scan.py` against the real repository root. I ran only the scratch copy, because the real one reads the live lane.

Repository state at the end: `git status --short` shows ` M PROME/state/ORCH_INFLIGHT.md` and ` M PROME/state/ORCH_LOG.tsv`. I did not write either file; they are presumably the lead's in-flight orchestration records. My only write is this ledger.
