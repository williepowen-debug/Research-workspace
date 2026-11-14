# Independent read 1: intake `--mark` receipt repair (commit 4b590d0c0d, CATO N14-1)

**VERDICT: REJECT, 1 BLOCKING finding (❌ = 1, ⚠️ = 8, ✅ = 8).**

The one blocking finding is narrow (a window of about 2 ms per mark) but real and avoidable. Inside one `--mark` call, the tool checks the receipt, then reads the `--through` batch again and stores the fingerprint of that second read. A collector rewrite that lands between the two reads is stored as acknowledged. It is never replayed, and the day it belongs to is never re-scanned once the next day arrives (CX1). The author named this window as a known residual. It is not inherent to the design: storing the fingerprint the receipt check already verified closes it completely. A three-line change to a scratch copy closes CX1 and still passes the author's 19 catch-up tests (CX1-fix). Everything else the repair claims held under my own counterexamples.

Reader: independent reader 1 (Opus), 2026-11-14 about 14:35 to 14:50 ET. Scope: the fix diff only. Repository read-only; all runs used temporary fixtures under `/tmp`. Scratch: `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c399d57d-9eb0-4dc3-b343-21c0f3e9d0d8/scratchpad/reader/`.

## Assertion ledger

Five fields per row: claim → artifact → command → observed → proposed change.

| # | Mark | Claim | Artifact (file:line) | Command | Observed | Proposed change |
|---|---|---|---|---|---|---|
| L1 | ❌ | A1: a mark succeeds only when every acknowledged batch's bytes are the bytes the scan presented | `AGENTS/WALTER/tools/intake_scan.py:759` (receipt read), `:782` (`mark_pointer` re-parses every batch), `:785` (`last_marked_sha = batch_sha(ptr)`, a fresh read) | `python3 -B cx1_race_inside_mark.py` (rewrite injected inside `mark_pointer`, after the receipt check) | mark rc 0; stored `last_marked_sha` equals the sha of the UNREAD rewrite (True); next-day scan reads only 11/05, prints no "rewritten" health line, and the unread 11/04 is not replayed. Control (same rewrite one step later, after the mark): replayed True | Store the fingerprint the receipt verified, not a fresh read: have `scan_receipt` record the per-batch shas it hashed and write `seen["last_marked_sha"] = <that sha for ptr>`. CX1-fix shows this closes CX1: the stored sha is the read version, the next scan prints the rewrite health line and replays 11/04, and the author's catch-up suite passes 19/19 |
| L2 | ⚠️ | Concurrent window width (asked) | same lines | `python3 -B cx1b_window_width.py` (6 batches × about 97.5 KB, 20 marks) | from the end of `scan_receipt` to the stored `batch_sha(ptr)`: min 1.65 ms, median 1.73 ms, max 3.33 ms. It grows with the number and size of batches `mark_pointer` parses. Live lane sizes not inspected | Closed by L1's change. Earlier batches in the same range have no stored fingerprint at all (by design before this repair), so a rewrite of one inside this window would also be lost. The collector rewrites only the current day's file, so this is residue, not blocking |
| L3 | ✅ | A2: on a mismatch or a missing receipt, exit is non-zero and the state is byte-identical | `intake_scan.py:760-767` (both refusals return 2 before any write; the only write in the mark path is `:786`) | `cx2_multiday_overlap.py`, `cx3_missing_and_malformed.py` | every refusal: rc 2, state bytes unchanged (8 malformed receipts, 7 lane mutations) | none |
| L4 | ✅ | A3: an unchanged lane marks cleanly | — | cx2 "IDENTICAL bytes" case; cx3 zero-alert case; author suite | rc 0 on identical-bytes rewrite (no false refusal); zero-alert printed command → rc 0 | none |
| L5 | ✅ | A4: a rewrite AFTER a successful mark is replayed | `:785`, `rewritten_marked` | cx1 CONTROL | replayed True | none |
| L6 | ✅ | A5: a rewrite of an EARLIER batch, or a batch that appeared or vanished, is refused | `scan_receipt` `:227-236` hashes every batch in `news_batches` | `cx2_multiday_overlap.py` | refused, state unchanged in each case: 11/02 rewritten with an ordinary headline only (no key change); 11/03 vanished; 11/03 appeared; 11/02 became unreadable; 11/02 repaired after being unreadable | none |
| L7 | ✅ | Receipt is over raw bytes, not parsed content; ordering and whitespace distinguish | `:205` `batch_sha` = sha1 of `read_bytes()`; keys `sorted` | cx2 | a whitespace-only rewrite (same JSON) and an item reorder are both refused (fail-closed). No hashed field is excluded. Inputs are delimited `B <path> <sha>\n` / `K <key>\n`; keys from cftc, edgar and treasury are sanitized to `[A-Za-z0-9_]`. A collision needs a newline inside a fred or eia first token (not observed) or a 48-bit sha1 collision | none |
| L8 | ✅ | A6: an empty, default, truncated or stale receipt does not pass | `:760`, `:764` (exact string compare) | cx3 | rc 2 for: empty, uppercase, leading space, trailing newline, 11-char prefix, 13 chars, all zeros, `sha1('')[:12]`. A stale receipt from a superseded scan is refused whenever the scanned set changed (cx2) | none |
| L9 | ⚠️ | A6: nothing in the tool hands over or auto-accepts the current bytes | `intake_scan.py:765` refusal prints `now {receipt}` | cx3 "refusal discloses" | the refusal prints the CURRENT receipt (verified equal to a fresh scan's). Copying it into `--mark` without re-scanning → rc 0. The tool never auto-accepts, but its refusal hands a one-step bypass to an agent operator | Drop `now {receipt}` from the refusal text; say only "re-run the scan" |
| L10 | ⚠️ | "refused … if the lane or its alerts changed" (charter 7e(e), BP 7e(e2)) | `scan_receipt` hashes alert KEYS only; `:315-340` fred `raw` and value are not hashed | cx3 HY case | HY OAS changed from 279.5 to 281.0 under the same key `fred:BAMLH0A0HYM2:red` between scan and mark → mark rc 0. The scan showed a non-qualifying reading; the qualifying one was marked unseen. This is pre-existing onset-key semantics, not a regression, and the instruction text over-claims. Batch bytes (A1) are unaffected | Either add `r["raw"]` to the receipt (one line) or narrow the wording to "its gated alert keys" |
| L11 | ⚠️ | A7: "run the exact mark command the scan printed" executes as written | `intake_scan.py:848` prints `python3 tools/intake_scan.py …`; charter `CLAUDE.md:11` says commands run from the repository root, `:55` scans with `python3 AGENTS/WALTER/tools/intake_scan.py` | `ls tools/intake_scan.py` from the repository root | `No such file or directory`: the exact printed command fails from the root the charter specifies. It fails safe (nothing written) and existed before this commit, but the commit's new wording ("exact command") makes it bite | Print `python3 AGENTS/WALTER/tools/intake_scan.py --mark …` |
| L12 | ⚠️ | A7: the printed command works when the newsweep `saved` path is missing | `:848` with `newest=None` | cx3 "no saved path" | prints `--through None --receipt …`; as written → rc 2 "REFUSED: --through None"; without `--through` → rc 0. Existed before this commit (the old print had the same `None`) | When `newest` is None, omit `--through` from the printed command |
| L13 | ⚠️ | No other documented caller still uses bare `--mark` | `AGENTS/WALTER/tools/walter_doctor.py:322` hint "run tools/intake_scan.py --mark"; `AGENTS/WALTER/design/BOOT_PROTOCOL.md:69` "then `intake_scan.py --mark` to reconcile the baseline" | `grep -rn` over `AGENTS/WALTER` (tools, design, CLAUDE.md), `scripts/`, `PROME/tools` | Both still give the bare form, which is now refused (rc 2, author's R5). Fails safe. Line 69 now contradicts 7e(e2) four lines below. No script or test calls bare `--mark` (the `x_bookmarks` tests are a different tool) | Update both lines to point at the printed command |
| L14 | ⚠️ | A7 order: mark only "after dispositions" | `CLAUDE.md:59` 7e(e) listed before `:61` 7e(h) title skim | read | Executed in listed order, the mark happens before the 7e(h) skim of ordinary titles. Not unsafe for bytes: the skim reads the same bytes, and a later rewrite is replayed (A4). But the receipt does not stop a mark before the skim | Say in 7e(e) "after 7e(d) to 7e(h) dispositions", or move the sentence |
| L15 | ⚠️ | Commit claim: "CATO witness adapted to quote the read receipt: mark rc 2, state unmoved" | `AGENTS/CATO/runs/2026-11-14_intake-mark-witness.py` (last commit 5d228e7bf6, unchanged by 4b590d0c0d) | `python3 -B AGENTS/CATO/runs/2026-11-14_intake-mark-witness.py` | The committed witness crashes with `FileNotFoundError` for `intake_seen.json`, because its bare `--mark` is now refused and writes nothing. That is the fix working, but the run never reaches its verdict. The adapted version is not in the repository (SEARCH-NOT-FOUND in AGENTS/WALTER and AGENTS/CATO) | Commit the adapted witness or attach its output, so the claim can be checked |
| L16 | ✅ | Scan prints the receipt on every operator path | `:841-849` (text), `:798` (`--json` has a `receipt` field) | cx3 zero-alert; author helpers | zero alerts: "gate quiet" shown, per-batch fingerprints and the `--receipt` command printed. JSON carries `receipt`. Liveness missing or unreadable: the scan prints ERROR and no receipt, and `--mark` writes nothing | none (cosmetic: the per-batch `fingerprint` lines print under the `[suppressed …]` heading and read as suppressed items) |
| L17 | ✅ | Refusal precedes every write; no partial write | `:759-768` before `:772-786`; other writes `:549`/`:629` are disposition-only | `grep -n write_text` | only 3 writes; the mark path's single write is after all checks | none |

Note on A2's edges: `--mark` with `liveness.json` missing or malformed returns rc **0** (ERROR printed, nothing written: cx3). This existed before the commit and does not move state. I list it as residue, not a ledger row, because A2 names only a mismatch and a missing receipt.

## Neighbour classes

- **Ordinary:** L4. Unchanged lane, identical-bytes rewrite and zero-alert lane all mark cleanly.
- **Overlap:** L6 and L7 (multi-day, earlier batch, appear and vanish), and L10 (alert value under the same key). Batch plus alert-key change: covered by the author's R5.
- **Wrong owner / other caller:** L13 and L15. No other executable caller of `intake_scan --mark` exists in AGENTS/WALTER, `scripts/` or `PROME/tools`.
- **Missing information:** L8, L12 and L16 (malformed receipt, missing `saved`, missing or malformed liveness). Unreadable batch at both scan and mark → accepted with the pointer held (cx2), as designed.
- **Concurrent activity:** L1 and L2. Two `--mark` processes running at once: not checked.

## My counterexamples (scripts and observed output)

All scripts are in `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c399d57d-9eb0-4dc3-b343-21c0f3e9d0d8/scratchpad/reader/`. They reuse the `CatchUp` fixture from `test_intake_catchup.py` through `common.py`, which asserts that `LANE` is under `/tmp` and `SEEN` is not the live file. Each runs with `python3 -B`.

**CX1: `cx1_race_inside_mark.py`** (output `cx1.out`)
```
mark rc: 0
stored last_marked_sha == sha of UNREAD rewrite: True
next scan batches line: ['[news batches scanned — 1: 2026-11-05..2026-11-05]  (catch-up from last_marked_batch data/2026-11-04/news.json)']
next scan has rewrite health line: False
UNREAD 11/04 replayed: False
CONTROL (rewrite after mark) mark rc: 0 replayed: True
```

**CX1b: `cx1b_window_width.py`** (output `cx1b.out`)
```
batch bytes each: 97501
window ms over 20 marks: min 1.65  median 1.73  max 3.33
```

**CX1-fix: `fixcopy/`** (patched scratch copy of `intake_scan.py`; diff below; output `cx1_fixcopy.out`). The repository file was not edited.
```
> _RECEIPT_SHAS = {}            (module level)
>     _RECEIPT_SHAS.clear(); _RECEIPT_SHAS[b] = batch_sha(b)   (inside scan_receipt, hashed value reused)
<             seen["last_marked_sha"] = batch_sha(ptr)
>             seen["last_marked_sha"] = _RECEIPT_SHAS.get(ptr) or batch_sha(ptr)
---
mark rc: 0
stored last_marked_sha == sha of UNREAD rewrite: False
next scan batches line: ['[news batches scanned — 2: 2026-11-04..2026-11-05]  ...']
next scan has rewrite health line: True
UNREAD 11/04 replayed: True
author's test_intake_catchup.py on the patched copy: OK (19 tests)
```
(The `or batch_sha(ptr)` fallback should not exist in a real fix. If `ptr` is not in the receipt map, that is an error, not a fresh read.)

**CX2: `cx2_multiday_overlap.py`** (output `cx2.out`)
```
earlier batch 11/02 rewritten, ordinary headline only (no key) rc=2 state_unchanged=True REFUSED
earlier batch 11/02 rewritten, whitespace only (same JSON)     rc=2 state_unchanged=True REFUSED
earlier batch 11/02 rewritten, items reordered                 rc=2 state_unchanged=True REFUSED
earlier batch 11/02 rewritten with IDENTICAL bytes (expect accept) rc=0 state_unchanged=False ACCEPTED
batch 11/03 vanished between scan and mark                     rc=2 state_unchanged=True REFUSED
batch 11/03 APPEARED between scan and mark                     rc=2 state_unchanged=True REFUSED
batch 11/02 became unreadable (truncated JSON)                 rc=2 state_unchanged=True REFUSED
batch 11/02 unreadable at scan, repaired before mark           rc=2 state_unchanged=True REFUSED
batch 11/02 unreadable at scan AND at mark (expect accept, ptr held) rc=0 state_unchanged=False ACCEPTED
new day dir 11/05 (news.json) appears, liveness NOT yet updated rc=0 state_unchanged=False ACCEPTED
```
(The last case is correct: 11/05 is outside the scanned set and is not acknowledged, because the pointer stays at 11/04.)

**CX3: `cx3_missing_and_malformed.py`** (output `cx3.out`)
```
malformed receipt empty / uppercase / leading space / trailing newline / 11-char prefix / 13 chars / all zeros / sha1('')[:12]: each rc=2 unchanged=True REFUSED
correct receipt, no --through: rc 0 | warning printed: True
refusal prints current receipt: True | REFUSED: ... (receipt d03b4f732478, now d1de2f1887e1). Re-run the scan ...
copying 'now' value from the refusal (no re-scan) -> rc 0
liveness missing + --mark: rc 0 unchanged True
liveness malformed + --mark: rc 0 unchanged True
zero-alert scan: 'gate quiet' shown: True | printed: batch ... fingerprint 9c70fed7c75a; --mark --through data/2026-11-04/news.json --receipt 04232784e639
zero-alert mark with printed command: rc 0
no saved path: printed: ... --mark --through None --receipt 77c985eeaa26
  executing printed command as written -> rc 2 | REFUSED: --through None but the newest lane batch is now None
  without --through -> rc 0
HY 279.5 -> 281.0 under same key fred:BAMLH0A0HYM2:red between scan and mark: mark rc 0
```

**Baseline (the author's suites, run once):** `test_intake_catchup.py` 19/19 OK; `test_cruise_capital_review.py` 15/15 OK.

## What I did NOT check

- The live lane, live `intake_seen.json`, or real batch sizes. The window figure in L2 comes from a synthetic 97.5 KB batch.
- Whether the collector writes `news.json` atomically. I did not read the Research-Intake source, per the hard limits. A non-atomic write would add a partially written file case, which the receipt would refuse anyway.
- Two `--mark` processes at once, and the non-atomic `SEEN.write_text` (a crash mid-write). Both existed before this commit and are outside the diff.
- `test_gpu_finance_review.py`, `test_boot_repairs.py`, and the `boot_basis_hashes.json` re-hash in the commit.
- In-scan read skew: within one scan run, `collect_alerts` reads the batches, then `scan_receipt` reads them again. I reasoned through it but did not run it. A rewrite in that gap that adds a gated key makes the mark-time receipt differ (refused). One that adds only ordinary headlines binds a receipt to bytes whose ordinary titles the scan never prints anyway. L1's change would let the scan also reuse a single read.
- Whether WALTER's actual session working directory is the repository root or AGENTS/WALTER (L11 rests on the charter's own statement at `CLAUDE.md:11`).

Tree check at finish: `git status --short` shows only ` M PROME/state/ORCH_INFLIGHT.md` and ` M PROME/state/ORCH_LOG.tsv`. Neither was written by this reader (both were already modified at its first status check). The live `AGENTS/WALTER/registry/intake_seen.json` is tracked and byte-identical to HEAD (`git diff --quiet HEAD -- …` exit 0). No bytecode was written after 14:35 ET (`find … -newermt`). This ledger is the reader's only write inside the repository.
