# Independent read 3 (final): intake `--mark` correction 151ed8b216

**VERDICT: REJECT, 1 BLOCKING finding (❌ = 1, ⚠️ = 4, ✅ = 11). The ❌ predates this commit (it is present, with identical output, at 7f317a5e18). The commit's own diff is correct.**

What the diff claims holds. `mark_pointer` no longer reads anything. Readability and the stored fingerprint now come from `scan_receipt`'s single read. R9 and R10 fail on 7f317a5e18 and pass now, and the other 22 tests pass on both. For every fixture I built, the receipt of an unchanged lane is the same before and after the commit.

**Class answer.** After the receipt is computed, no read of lane or state data is left on the `--mark` path at HEAD before the state write. That member of the class is closed. One member remains, and it sits **before** the receipt. In both the scan and the mark, `collect_alerts` reads each batch once (`intake_scan.py:423`) to build what is displayed and the seen keys. `scan_receipt` then reads the same file **again** (`:243`) to build the fingerprint, the stored sha and the readable map. A rewrite between those two reads produces a scan that shows version A while the receipt and the printed fingerprints bind version B. A mark using that receipt then succeeds and stores sha(B), so B is never replayed. The rewrite only has to leave every gated alert's key and reading unchanged; for example, it can change a watch hit's owner (CX3-1). A small patch that reads each batch once and feeds the same bytes to the display and the receipt closes it (diff below; tested by me only, so it is unreviewed).

Reader: independent reader 3 (Opus), 2026-11-14, about 14:58 to 15:20 ET. The repository was read-only. Every run used a temporary fixture lane under `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c399d57d-9eb0-4dc3-b343-21c0f3e9d0d8/scratchpad/reader3/` with `LANE`, `SEEN` and `LIVENESS` patched. The live lane and the live `intake_seen.json` were never read or touched. Scratch copies: `old/` = 7f317a5e18 scanner, `new/` = 151ed8b216 (identical to HEAD a18d9c7052 for `AGENTS/WALTER/tools/`, checked with `git diff 151ed8b216 HEAD --stat -- AGENTS/WALTER/tools/` → empty), `patched/` = new + my patch.

## Class question: every read after the receipt and before the state write (HEAD, `main()`)

| Line (HEAD) | What it reads | Influences the write? |
|---|---|---|
| 778 | `scan_receipt`: the receipt read itself (each batch's bytes, once) | Yes: `receipt_shas` → `last_marked_sha` (807); `receipt_readable` → the pointer (801) |
| 779-790 | Argument checks; `newest`, `args` are in memory (from 755/764) | Only as refusals; no I/O |
| 796 | `_now_utc()` (the clock) | Yes, as timestamps only (`updated`, first-seen of new keys); no lane data |
| 797-800 | `seen`, `prev`, `recs`: in memory (loaded at 762 and 767, before the receipt) | Yes, but no read happens here |
| 801 → 306-319 | `mark_pointer`: `readable.get`, `_day` (regex). **No file I/O** (checked by reading it; R9/R10 inject a rewrite inside it with no effect) | Yes: the pointer, from the receipt's own read |
| 802-811 | `receipt_shas`, `last_marked`, `marked_sha`: in memory | Yes, no read |
| 812 | `SEEN.write_text`: the write | n/a |

**No member of the class remains after the receipt.** The remaining member comes **before** the receipt, and its result is written:

| Line (HEAD) | Read | Feeds |
|---|---|---|
| 767 → 417-423 | `collect_alerts` → `news_batches` (directory listing again) → `read_batch_items(batch)`: **read 1** of each batch's bytes | Everything displayed (route lines, owners, phrases, UNREADABLE alerts), the K lines of the receipt (key + raw only), and the seen keys written at 798 |
| 418 | `batch_sha(batch)` for the rewritten-marked suffix: read 1b | The `@sha` key suffix |
| 772-776 | `health` → `news_search_coverage` (reads saved plus up to 10 earlier batches, imports the lane's `newsweep_config`); `pointer_health` (exists checks); `batch_sha(rb)` for the health line | Display only; not written |
| 778 → 241-252 | `scan_receipt`: **read 2** of each batch | B lines of the receipt, the printed fingerprints, `last_marked_sha`, the pointer |

**Can the operator be shown A while the receipt binds B? Yes (CX3-1).** If a rewrite lands between read 1 and read 2 of the scan, the operator sees A's alerts next to B's fingerprint and a receipt over (sha(B), alerts(A)). At the mark, both reads see B. If alerts(B) == alerts(A) by key and raw, the receipt matches, the mark exits 0 and stores sha(B), and B is never replayed. Any rewrite that adds or changes a gated key or reading is refused (control variant), so the hole admits only alert-equivalent rewrites. Those include **a changed `watch_hits` owner or phrase**, which is displayed as the route, and DEVELOPMENT owners/entity. The window runs from read 1 of a batch to read 2 of the same batch. On a synthetic 10 × 300-item lane (no `newsweep_config`) I measured a median of 4.8 ms and a maximum of 9-12 ms for the oldest batch, and a median of 0.9 ms for the newest. On the live lane `news_search_coverage` adds a module import and up to 11 file parses inside the window; I did not measure that (the live lane is off-limits) and estimate it at tens of milliseconds. The condition is a second writer to the lane clone (a `git pull` from another session) during one scan's window. The same double read is present at 7f317a5e18 with identical output, so this commit did not introduce it.

## Assertion ledger

claim → artifact → command → observed → proposed change

| # | Mark | Claim | Artifact (HEAD) | Command | Observed | Proposed change |
|---|---|---|---|---|---|---|
| N1 | ❌ | Property: a mark never records as acknowledged any batch content other than what the dispositioned scan presented. C3's "so the scan's view and the mark's view cannot differ" | `intake_scan.py:423` (display read) vs `:243` (receipt read); `:798`, `:807` (write) | `python3 -B cx3.py new` (CX3-1; `cx3_new.out`); same with `old` | **owner-change:** the scan displays `-> CYPHER [WATCH_HIT [CYPHER:'x']]`, while the printed fingerprint is sha(B) (B = same title, `watch_hits [['BROCK','secret']]`). Mark rc 0, `last_marked_sha == sha(B)`; the next scan suppresses the key and its owner is now BROCK, but the text output never prints a suppressed key's owner, so BROCK is never routed. **saved-batch NEW_ALERT added** (liveness unchanged): rc 0, sha(B) stored, the headline is never surfaced. **control (new WATCH_HIT in B):** rc 2, state unchanged. `old` gives identical output, so the problem predates this commit. | Read each batch once and feed those bytes to the display, the receipt and the mark (patch below). With the patch: all three variants are refused (rc 2, state unchanged) and the printed fingerprint is sha(A); the author's 24 tests pass, as do cruise 15/15 and gpu 3/3 |
| N2 | ✅ | C1: `scan_receipt` reads each batch once and returns (receipt, shas, readable) | `:241-252` | read; CX3-2 | One `read_bytes` per batch inside `scan_receipt`; the triple is returned. Scope: true of `scan_receipt` only, not of the scan (N1) | none |
| N3 | ✅ | C2: `mark_pointer` never re-reads; there is no fresh-read fallback | `:306-319` | read; `unittest test_intake_catchup` (R9, R10 inject a change inside `mark_pointer`) | No I/O in the function; `readable.get(b, False)` treats a missing key as unreadable (fail closed). Every batch in `batches` has a key, because `scan_receipt` iterates the same list | none |
| N4 | ✅ | C3: one readability rule, the same results as the old `read_text` rule | `:189-204` | `python3 -B cx3.py new` / `old` (CX3-2) | 15 shapes: zero-byte, UTF-8 BOM, invalid UTF-8, UTF-16, `[]`, `{"items": null}`, `{"items": {}}`, `{}`, `"x"`, CRLF inside a string, lone CR as whitespace, 100k-deep nesting, `[NaN]`. The display error column and the pointer are identical between old and new; new `receipt_readable` agrees with the display read on the same bytes in every case. Old `read_text`'s newline translation makes no difference: a raw CR is rejected inside a JSON string either way and is whitespace outside one | none |
| N5 | ✅ | C4: a missing file gives sha None and counts as unreadable, and the pointer holds | `:242-251`, `:312` | CX3-3; R9 | Deleted between the scan and the mark: rc 2, state byte-identical. Deleted inside the mark before its receipt read: rc 2, byte-identical. No other 12-hex value appears in either refusal | none |
| N6 | ✅ | C5: R9 and R10 fail on 7f317a5e18 and pass now; the other 22 pass on both | `test_intake_catchup.py:274-306` | `old/`, `new/` scratch copies with the 151ed8b216 test file: `python3 -m unittest test_intake_catchup` | old: FAILED (failures=2), exactly R9 and R10; new: 24 OK; repository HEAD: 24 OK | none |
| N7 | ✅ | C6: an unchanged lane's receipt is the same before and after the commit | `:247-252` | `python3 -B cx3_c6.py` (`cx3_c6.out`, `cx3_c6_nofred.out`) | Equal for 5 fixtures: plain catch-up, unreadable middle, zero alerts, rewritten marked batch, install with no pointer | none |
| N8 | ✅ | An unchanged lane marks, including with zero alerts, using the printed command verbatim | `:868-870` | `cx3_c6.py` (copies the last line of the text scan) | rc 0 in all 5 fixtures; zero alerts (no fred, empty `by_class`) rc 0, pointer → newest | none |
| N9 | ✅ | A post-mark rewrite replays; an earlier-batch rewrite is refused | `:257-273`, `:775` | `cx3_c6.py` | Post-mark rewrite of the newest batch: the next scan surfaces `late hit` and prints the "rewritten" health line. A KNOWN-only rewrite of 11/03 between the scan and the mark: rc 2, state byte-identical | none |
| N10 | ✅ | A mixed range stops before the unreadable batch and surfaces the rest later | `:306-319` | CX3-4 | 11/03 is broken inside 11/01→11/05: the pointer holds at 11/02 with a stored sha. The next scan re-reads 11/03-11/05. After 11/03 is repaired, its hit surfaces as new while 11/04 and 11/05 are suppressed (already routed); the next mark → 11/05 | none |
| N11 | ✅ | The readable map with `--through` omitted, an empty range, and a held pointer | `:801-811` | CX3-5 | Omitted: pointer → newest with the sha of its bytes. Pointer at newest: unchanged with a correct sha. Pointer ahead (11/09): held, stored sha kept | none |
| N12 | ✅ | No refusal prints a usable receipt | `:780-792` | CX3-3, `cx3_c6.py` | No 12-hex value other than the quoted one in any refusal | none |
| N13 | ⚠️ | Residue, outside the diff and predating it: a malformed batch crashes the scan, so the lane cannot be marked until the batch is fixed | `:530` (`cruise_capital_queue` catches OSError, ValueError, AttributeError, not TypeError or RecursionError); `:433` (`it.get` on a non-dict item) | CX3-2 | `{"items": null}` in any day since 11/03: the scan crashes (TypeError), so no receipt is printed. `{"items": [NaN]}`: the scan AND the mark crash (AttributeError), and the state is unchanged. 100k-deep nesting: the scan crashes (RecursionError). Old behaves the same. Not rated blocking: it needs malformed collector output, fails loud, and writes nothing | Owner's call: catch `Exception` per day in the two queues and skip non-dict items in `collect_alerts`, each as an UNREADABLE line |
| N14 | ⚠️ | R9 and R10 now inject at a point with no I/O | `test_intake_catchup.py:276-285` | read | They guard against `mark_pointer` regressing to a read, but no test covers the display-vs-receipt read (N1) | Add a test that injects the rewrite before `scan_receipt` during the scan (CX3-1 shape) |
| N15 | ⚠️ | The receipt binds key + raw, not owners or labels (read 2's M4, extended) | `:249-251` | CX3-1 | This is why N1's alert-equivalent rewrite passes. Without the race, a byte change is caught by the B line. With N1 patched, the residue is only that owners are not themselves bound, which is harmless when one read feeds everything | none if N1 is patched |
| N16 | ⚠️ | The patch's own limits | patch below | `cx3.py patched`, the author's suites | `rb` (which batch counts as the rewritten marked batch) is still decided by an earlier `batch_sha` read (`news_batches`/`rewritten_marked`), and the rb health line still re-reads. Both affect labels and display only; the bytes hashed and written are the snapshot. With the patch, CX3-3's "deleted inside the mark" marks rc 0, because the injection lands after the single read and the mark acts on bytes identical to the scan's; that is correct, not a regression. The patch is my own: not independently verified | Reviewer of the fix: try your own counterexample |

## Counterexamples (scripts in `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c399d57d-9eb0-4dc3-b343-21c0f3e9d0d8/scratchpad/reader3/`)

- **CX3-1** `cx3.py` (in-scan double read; `cx3_new.out`, `cx3_old.out`, `cx3_patched.out`). Wraps `s.scan_receipt` so the rewrite lands after `collect_alerts` and before the receipt read, runs the text scan, and copies `--receipt` from the printed command. HEAD output:
  ```
  [owner-change] displayed route line(s): ["  PRIORITY  ACTION -> CYPHER  [WATCH_HIT [CYPHER:'x']]"]
  [owner-change] displayed fingerprint line has shaB=True shaA=False
  [owner-change] mark rc=0; state changed=True; last_marked_batch=data/2026-11-04/news.json last_marked_sha=244d5a004eca (== shaB: True)
  [owner-change] next scan ... new keys=[]; owners of T hit in suppressed=[['BROCK']]
  [saved-batch NEW_ALERT added] mark rc=0; ... (== shaB: True)
  [control: new WATCH_HIT added] mark rc=2; state changed=False
  ```
  Patched: `shaB=False shaA=True`, and all three variants give rc 2 with the state unchanged.
- **CX3-1w** window: `first-batch window ms median=4.8 max=9.0; newest-batch window ms median=0.91` (HEAD; old 5.1/12.4/0.85).
- **CX3-2** C3 edge cases (table in N4): the old and new columns match row for row.
- **CX3-3** deletion between the scan and the mark, and inside the mark: rc 2, state byte-identical, both refusals print no other receipt.
- **CX3-4** unreadable middle in a multi-day range, then repaired (N10).
- **CX3-5** readable map variants (N11).
- **cx3_c6.py** receipt equality between old and new, the printed command run verbatim, and the replay/refusal checks (N7-N9).

## Proposed patch (against 151ed8b216 `AGENTS/WALTER/tools/intake_scan.py`; tested as above, not independently reviewed)

```diff
@@ -186,15 +186,31 @@
-def read_batch_items(batch):
+def read_batch_items(batch, snap=None):
     """(items, error). ONE reader for the scan and --mark (follow-up note 1): valid JSON that is
-    not an object with an `items` list counts as unreadable in both places."""
+    not an object with an `items` list counts as unreadable in both places. With `snap`, the bytes
+    come from that one read (read 3), never a fresh read."""
     try:
-        return _items_from_bytes((LANE / batch).read_bytes()), None
+        raw = snap[batch] if snap is not None and batch in snap else (LANE / batch).read_bytes()
+        if isinstance(raw, Exception):
+            raise raw
+        return _items_from_bytes(raw), None
     except Exception as e:
         return None, type(e).__name__
 
 
+def snapshot_batches(batches):
+    """{batch: bytes or the read's exception}: the ONE read per batch that the display, the receipt
+    and the mark all use (read 3: the display had its own read before the receipt's)."""
+    out = {}
+    for b in batches:
+        try:
+            out[b] = (LANE / b).read_bytes()
+        except (OSError, TypeError) as e:
+            out[b] = e
+    return out
+
+
@@ -229,7 +245,7 @@
-def scan_receipt(batches, recs):
+def scan_receipt(batches, recs, snap=None):
@@ -239,10 +255,13 @@
     for b in batches:
-        try:
-            raw = (LANE / b).read_bytes()
-        except (OSError, TypeError):
-            raw = None
+        if snap is not None and b in snap:
+            raw = None if isinstance(snap[b], Exception) else snap[b]
+        else:
+            try:
+                raw = (LANE / b).read_bytes()
+            except (OSError, TypeError):
+                raw = None
         shas[b] = hashlib.sha1(raw).hexdigest()[:12] if raw is not None else None
@@ -319,7 +338,7 @@
-def collect_alerts(live, last_marked=None, marked_sha=None):
+def collect_alerts(live, last_marked=None, marked_sha=None, snap=None):
@@ -414,13 +433,17 @@
     rb = rewritten_marked(saved, last_marked, marked_sha) if saved else None
-    for batch in news_batches(saved, last_marked, marked_sha):
-        sfx = f"@{batch_sha(batch)}" if batch == rb else ""  # rewritten marked batch: fresh count keys
+    for batch in (list(snap) if snap is not None else news_batches(saved, last_marked, marked_sha)):
+        if snap is not None:
+            sb = None if isinstance(snap[batch], Exception) else hashlib.sha1(snap[batch]).hexdigest()[:12]
+        else:
+            sb = batch_sha(batch)
+        sfx = f"@{sb}" if batch == rb else ""  # rewritten marked batch: fresh count keys
@@
-        items, err = read_batch_items(batch)
+        items, err = read_batch_items(batch, snap)
@@ -764,7 +787,8 @@
     batches = news_batches(newest, last_marked, marked_sha)
-    recs = collect_alerts(live, last_marked, marked_sha)
+    snap = snapshot_batches(batches)
+    recs = collect_alerts(live, last_marked, marked_sha, snap)
@@ -775,7 +799,7 @@
-    receipt, receipt_shas, receipt_readable = scan_receipt(batches, recs)
+    receipt, receipt_shas, receipt_readable = scan_receipt(batches, recs, snap)
```

A side effect: `collect_alerts` iterates the same `batches` list that `main` hashed, which removes the second `news_batches` directory listing as well. Called without `snap` (existing tests, other callers), behaviour is unchanged.

## What I did NOT check

- `test_boot_repairs` against the patch: it fails to import in a scratch copy at HEAD as well as with the patch (it needs `walter_doctor` and the repository's `FORGE/tools/market-data/dashboard.py` path). That is an environment failure unrelated to the correction. I did not run it inside the repository, to stay read-only.
- The live window: not measured, because the live lane is off-limits. The tens-of-milliseconds figure is an estimate.
- Whether anything other than WALTER's own `git pull` writes the lane clone on this host (I saw no crontab entry for it; other sessions or tools were not surveyed).
- Concurrent `--mark` runs by two sessions racing on `intake_seen.json` (the state file is read at 762, before the receipt, and is not bound into it except through the pointer).
- `_edgar_route`'s reads of `edgar_8k.json` (read 2's M4) and the liveness fields that are not alerts (health): display or route only, not re-tested.
- Python versions other than the host's `python3`.
