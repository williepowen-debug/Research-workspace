# Decisions desk: final independent counterexample read (read 3 of 3) of `4955b465f`

Reviewer: independent Opus counterexample reviewer for PROME. Written 2026-10-31 11:07 ET (from `date`; started 10:47 ET).
Target: CATO commit `4955b465f0e4fef8ee567023e4bd8a32787c61a3`, frozen by `PROME/inbox/2026-10-31_from-CATO_decisions-r1-frozen-final-review.md`. Prior ledgers: `PROME/reports/2026-10-30_decisions-desk-counterexample-ledger.md` (read 1) and `PROME/reports/2026-10-31_decisions-desk-recheck-ledger.md` (read 2).

Method: every write path ran only in disposable clones under `.../scratchpad/desk-final/c/`. Each scenario had its own bare `origin` under `.../desk-final/r/`, copied from `desk-final/base.git`. That bare repository is `4955b465f` (fetched read-only from the real repository) plus two scratch-only commits: a fixture review (`1e0d339bf`) and an acceptance file built from `release-review.json`'s `activation_template` (`b844c2ae7`). `app.accepted()` returns `(True, '')` there. Harness: `desk-final/tools/h.py` (read 2's HTTP driver, repointed), `common.py`, `s1.py`–`s6.py`, plus `ip.py`, an in-process driver. `ip.py` simulates a second Decisions process saving into the same state database at a chosen point inside Send. CATO's tests were not used as evidence. No synthetic account number appears below except as its last four digits (•4321).

## Counterexamples: 50 tried · 46 held · 4 failed

| # | Case | Result |
|---|---|---|
| F1 | All 20 `build_hashes` in `release-review.json` at `4955b465f` match the files at that commit, in the real working tree and at real `origin/master` | HELD |
| F2 | `build_hashes` equals `activation_template.build_hashes` | HELD |
| F3 | `git log 4955b465f..origin/master` (5 commits at 10:47) and `4955b465f..HEAD` (at 11:06), over the mvp directory, `scripts/`, the launcher and `willq_view.py`: no commit touches a build or dependency file | HELD |
| F4 | A scratch acceptance from the template is accepted by `app.accepted()` | HELD |
| T1 | **R1 (the never-sent-predecessor bug), decision row:** save A locally, revise to B, Send B → 200 | HELD |
| T1b | The Send commit contains exactly 2 paths: B's response file and B's inbox packet | HELD |
| T1c | Never-sent A is not on origin, and its words appear nowhere in `origin/master` (`git grep`) | HELD (my first grep term was too common; re-checked with a unique string) |
| T1d | Sending the superseded A afterwards is refused | HELD |
| T2 | B delivered, then C saved and sent: 200, 2 paths | HELD |
| T2b | Re-sending B after C is refused | HELD |
| T3 | A→B→C all saved locally: Send B refused, Send C 200 | HELD |
| T3b | A and B both stay local | HELD |
| T3c | Card afterwards: C delivered, A and B listed as "saved", no error | HELD |
| T4 | Task row (WQ-547): a local `defer` revised to `report_done`, then Send: 200, 2 paths, defer stays local | HELD |
| T4b | Task row: delivered `report_done` revised to a question, then Send: 200 | HELD |
| T5 | Stale-terms recovery: A saved, row reworded on origin, sync, Send A refused ("review and save again"), B saved on the new terms superseding A, Send B: 200. B carries the new row text and A is not published | HELD |
| T5b | Row closed after A was saved: Send A refused, and a replacement is refused | HELD (refusal wording is W-D) |
| T6 | Hook-refused commit recovery: A's words contain an `acct` label plus an 8-digit synthetic number (•4321). Send A gets 503 and A's two files stay staged (W-B). B is saved superseding A, and Send B gives 200 with exactly B's 2 paths; the number is not on origin | HELD |
| T7-advisory | A newer local C is saved by a second process during Send B's weekday check: B refused, nothing committed, then C sends | HELD |
| T7-postcommit-branch | C is saved after B's packet is written but before staging: B is refused and not published, but B's packet stays untracked in `PROME/inbox/` after C is delivered | HELD (B not published; orphan packet noted under W-F) |
| T7-commit | **C is saved during `git commit` of B: B is refused ("Only the latest saved response…"), but B's commit stays on local master (ahead 1). Sending C then pushes both. B's packet reaches PROME's inbox** | **FAILED (W-F)** |
| T7-push | C is saved during safe-push of B, after B's final check: B is published, C stays local and later sends | HELD (C came after B was sent) |
| T7-commit-terms | **PROME edits `WILL_QUEUE.md` in the shared tree during Send's commit: B is refused ("Queue terms changed…"), but B is committed locally** | **FAILED (W-F)** |
| T7-commit-terms-b | **An unrelated desk closeout (own-file commit + `safe-push.sh`) then publishes the refused, stale B to PROME's inbox** | **FAILED (W-F)** |
| T8 | Fresh clone and fresh state after B was sent (A private): the card shows B and the notice "Earlier saved versions are unavailable on this computer; their words are not inferred". A's words appear nowhere in the display JSON, and there are no desk errors | HELD |
| T8b | A's ID appears only as B's immutable `supersedes`, with no A event | HELD |
| T8c | On the fresh clone, revise B→C and Send: 200, 2 paths | HELD |
| T8d | On the fresh clone, a save that supersedes the unavailable private A is refused | HELD |
| T8e | On the fresh clone, a second root (`supersedes: null`) is refused | HELD |
| T8f | Back on the original machine after the laptop's C: sync shows the A→B→C chain intact, no error | HELD |
| T9 | Disconnected published segments (A private, B sent, C private, D sent), fresh clone: B and D are visible, the card is blocked for reconciliation, Send and save are refused, and C's words are absent | HELD (the wording "Conflicting saved answers" describes a gap, not a fork; cosmetic) |
| T9b | During that block, another item (WQ-556) still saves and sends | HELD |
| T9c | The original machine is unaffected | HELD |
| T10 | An unpublished B whose predecessor row was removed from the local database: not treated as a root. It is refused with "Missing predecessor" and the desk fails closed | HELD |
| T10b | B committed but not pushed, fresh state, predecessor missing: not a root, fails closed (W7) | HELD |
| G1 | A and B both delivered, receipt on A: the card shows A's words as recorded, in History; B is listed as delivered | HELD |
| G1b | After integration, Send B and a new save are both refused | HELD (wording is W-D) |
| G1c | A private, B sent and integrated, fresh clone: B shown as recorded, A's words absent | HELD |
| G2 | Integration on origin without sync: Send of a newer B is refused | HELD |
| G3a | An uncommitted shared-tree reword before Send is refused, and the foreign edit is preserved | HELD (my harness's assertion stripped the leading status space; the observed status is ` M PROME/WILL_QUEUE.md`) |
| G3b | A published row change, no sync: refused | HELD |
| G3c | Options row: choice B revised locally to choice A, then the option text changes on origin: Send refused | HELD |
| G3d | The replacement saved under the new option text sends with the new meaning | HELD |
| G4 | A foreign staged file and a foreign unstaged edit are untouched; the commit has exactly 2 own paths | HELD (same assertion artefact as G3a; observed `A ` and ` M` preserved) |
| G7 | No Send commit touches `WILL_QUEUE`, `proposals/` or `PROME/decisions/`. The only app write sites are the response export, a temp candidate file, and the inbox packet | HELD |
| G5 | Non-fast-forward is refused, a retry is refused, and after `pull --rebase` the answer is delivered exactly once (one packet commit on origin); the never-sent A stays local | HELD |
| G6 | A build file changed mid-run: Send and save refused, desk read-only | HELD (wording is W-D) |
| S1 | **A CATO-style closeout sweep commits and pushes the untracked export of the never-sent latest B. The card then reports "delivered" ("Your response reached PROME's inbox"), and the UI hides the Deliver button, but no packet exists** | **FAILED (W-G)** |
| S1b | Sending through the API after the sweep still delivers the packet | HELD |
| S1c | After the sweep, a fresh clone shows no words of the private A | HELD |

## Findings: ❌ 0 · ⚠️ 2 (new: W-F, W-G)

### ⚠️ W-F. A refusal raised after Send's commit leaves the refused answer committed on shared master, and the next push by anyone publishes it. This covers a newer local answer during the commit and a PROME same-tree edit during the commit, so CATO's handoff claim is falsified in a sub-second window. That claim: "An older selected answer cannot pass after a newer local answer appears during checks."

- **Claim:** `deliver()` commits at `:176` and then re-runs `check_queue_delivery` inside `exact_working_files()` at `:179`. If that check fails, the `ValueError` is raised after the commit. The commit is not undone, and the message does not say a commit exists. The commit sits on shared `master`. Will's next Send pushes it, and so does any agent's ordinary closeout (`safe-push.sh` sweeps committed work, W9). PROME's inbox then receives the older or stale answer with no staleness flag. Read 2's W-A covered this consequence only for origin changes; Z1/Z2 established same-tree refusals only before the commit.
- **Artifact:** `AGENTS/CATO/prototypes/decisions/mvp/delivery.py:172-181` (pre-commit check `:172`, commit `:176`, post-commit check `:179`); `queue_store.py:143-151`; `app.py:191-193`. Second, smaller window: a refusal at `:172` comes after the packet is written at `:167-170`, which leaves an untracked packet in `PROME/inbox/` (T7-postcommit-branch).
- **Command:** `desk-final/tools/s2.py` (modes `commit`, `postcommit-branch`) and `s2b.py` (mode `commit-terms` plus an unrelated closeout). `ip.py` injects the second process's save, or PROME's tree edit, at the `git commit` call. A hooked 2-file commit took 0.30 s in a scratch clone.
- **Observed:** T7-commit: `deliver_B: REFUSED … Only the latest saved response`, `ahead_behind 1/0`, card `event_delivery` shows B as `committed`, and after Send C `B_published: true`. T7-commit-terms: `REFUSED … Queue terms changed`, B committed locally. An unrelated closeout push then published B (rc 0, B in `PROME/inbox` on origin).
- **Why ⚠️, not ❌:** the consequence is identical to the accepted W-A residue, and so are the mitigations. The window is the length of one `git commit` (well under a second). It needs either two Decisions processes (the launcher's "Open Decisions" does start a new process on the same default state each click) or PROME writing the queue in that instant. The published event carries its own `queue_row` and the explicit `supersedes` chain. PROME may record nothing without Will's matching chat confirmation of that exact answer. No wrong answer can be recorded silently. It can only arrive in the inbox.
- **Proposed change:** (1) On any failure after `:176`, undo only the app's own unpushed commit: if `HEAD` is that commit and is not on origin, `git reset --soft HEAD^` and then `git restore --staged -- <its 2 paths>`. Also remove a packet this attempt created. (2) Until then, say so: "Committed locally; it will publish on the next push. Do not confirm it in chat." (3) Extend the named residue W-A to read "any post-commit refusal (newer local answer, same-tree terms edit, acceptance/build change) or remote change". (4) PROME intake procedure: before acting on a packet, check that the event is the head of its published chain and that its `queue_row` equals the row at intake. Otherwise treat it as superseded or stale.

### ⚠️ W-G. Never-sent answers sit as untracked, un-ignored files in CATO's own directory. An ordinary CATO closeout sweep would publish Will's unsent words to the public repository, and the card would then claim the answer reached PROME's inbox.

- **Claim:** every save writes `AGENTS/CATO/decisions/queue-responses/<id>.json` into the shared working tree, and nothing ignores it (`git check-ignore` returns nothing). `orphan_check.sh CATO` is silent about it, because it reports only paths outside `AGENTS/CATO/`. A CATO session's `git status` shows it as CATO's own uncommitted file. R1 now makes never-sent predecessors routine: every revise-before-send leaves one behind. If such a file is committed outside the app, `delivery_state()` checks only the response file, not the packet. It returns `delivered`, the card says "Your response reached PROME's inbox", and the Deliver button is hidden, although no packet exists.
- **Artifact:** `queue_store.py:105-120` (export at save), `delivery.py:19-28` (`delivery_state`), `desk.html:29` (`renderAnswer`: delivered text and button condition).
- **Command:** `desk-final/tools/s6.py`; also `git check-ignore -v` and `bash scripts/orphan_check.sh CATO` in clone `c/t3`.
- **Observed:** S1 `["delivered", can_deliver true, packet_on_origin false]`. The API Send still works (S1b). The orphan check printed "clean" while 2 never-sent exports existed.
- **Why ⚠️, not ❌:** it needs a commit outside the app that breaks the app's design. No app path commits a never-sent export (T1c, T3b, T6 and G5 all held). PROME's chat confirmation still gates any recording.
- **Proposed change:** keep unsent exports under the ignored `mvp/local-state/`, or add an ignore rule and stage with `git add -f` only inside `deliver()`. Make `delivery_state` require the packet too. Interim: add one line to CATO's charter or README: "never commit `AGENTS/CATO/decisions/queue-responses/` by hand; the app owns it".

### Notes, no new grade

- W-B confirmed unchanged (T6): A's two files stay staged with an opaque 503. With R1 fixed, replacement now recovers.
- W-D confirmed: "Daily responses await final acceptance" appears for closed (T5b), integrated (G1b) and build-changed (G6) items.
- T9's disconnected-segment card says "Conflicting saved answers"; the case is a history gap. This is cosmetic and inside the disclosed limitation.
- W-A was not re-run. Its trigger is now broadened by W-F.

## Restore neighbour (CATO's deliberate behaviour): judgment

It held in every probe. It never displayed or published unpublished words (T8, T8b, T9, G1c, S1c). It never let an unpublished predecessor through: an unpublished, or committed-but-unpushed, event with a missing parent is refused or fails closed (T10, T10b). Forking from the unavailable private predecessor, or starting a second root, is refused (T8d, T8e). Disconnected segments block only their own item (T9, T9b). The root exception is keyed to the exact bytes at `origin/master`, so it cannot be satisfied by a local or HEAD-only file.

## Named residue: judgment for first live use (one operator, chat confirmation required)

The residue is acceptable, provided W-F and W-G are added to the named list and to PROME's intake procedure. W-A (now broadened by W-F) needs the PROME intake check proposed above. W-B and W-D–W-E are recoverable or cosmetic. W-C needs PROME's rule that integrating closes the row or that follow-ups take a new WQ ID. W1, W3–W9 and W12 stand as read 2 judged them. Each one fails closed or affects only PROME's own intake tooling. Actual desktop/laptop restore remains unobserved and stays named.

## Verdict for `4955b465f`

**ACCEPT WITH NAMED RESIDUE.** ❌ 0. ⚠️ 2 new (W-F, W-G), plus the existing W-A–W-E, W1, W3–W9, W12, and the disconnected-history limitation. ❌R1 is repaired: decision and task revise-before-send, stale-terms recovery, refused-commit recovery and fresh-clone revision all send exactly 2 files, and never-sent predecessors stay local. Read 2's holds all re-held. Before acceptance is published, the acceptance residue list must name W-F and W-G. CATO's handoff sentence "an older selected answer cannot pass after a newer local answer appears during checks" is true only up to the commit. It is false for the sub-second commit window, and it must not be repeated as a guarantee.

## Real repository

`git status --porcelain` in `/home/willi/Research-workspace`:
- At start (10:47 ET), SAM's uncommitted work: ` M` on `AGENTS/SAM/{MEMORY.md, MEMORY_ARCHIVE.md, STATUS.md, board_log.tsv, docket/CALENDAR.md, docket/CATALYSTS.tsv, thesis/CHANGELOG.md, thesis/timeline/TIMELINE.md, workbook/CFTC_JPY.tsv}`, 8 staged renames of SAM inbox items into `processed/`, and untracked `AGENTS/SAM/research/outputs/2026-10-31_boj/`.
- At end (11:06 ET): **empty**. SAM committed its work (`957fd380e`), and PROME committed `ab824b84a` and `a3bef4461`.

None of these changes is mine. This reviewer wrote, staged, committed and pushed nothing in the real repository, and ran no Send, sync or safe-push against it. Its only real-repository access was reads (`git show`, `git log`, `sha256sum`, `git check-ignore`) and one read-only `git fetch` of `4955b465f` *from* it into the scratch bare repository.
