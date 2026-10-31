# Decisions desk: independent counterexample re-check of `f7b03a732`

Reviewer: independent Opus counterexample re-checker for PROME. Written 2026-10-31 09:48 ET (from `date`).
Target: CATO code commit `f7b03a732cf4f745b581bc6929cbe968631a4708` (frozen by `PROME/inbox/2026-10-30_from-CATO_decisions-hold-repair-frozen.md`). Prior ledger: `PROME/reports/2026-10-30_decisions-desk-counterexample-ledger.md`.

Method: every write path ran only in disposable clones under `.../scratchpad/desk-recheck/c/`. Each scenario had its own bare `origin` under `.../desk-recheck/r/`, copied from `base.git`. That bare repository is `f7b03a732` plus two scratch-only commits: a fixture review file, and an acceptance file built from `release-review.json`'s `activation_template`. The scratch acceptance check returns `accepted() → (True, '')`. Harness: `tools/h.py`, plus `tools/s1.py` to `s9b.py` and `tools/btn2.js`. CATO's tests were not used as evidence.

## Counterexamples: 59 tried · 50 held · 9 failed

| # | Case | Result |
|---|---|---|
| F1 | `release-review.json` at `f7b03a732`: all 20 named hashes match the files at that commit; `build_hashes` = `activation_template.build_hashes` | HELD |
| F2 | `git log f7b03a732..origin/master` over the mvp directory, launcher, `willq_view.py`, and every hashed script, hook and `render.py`: 36 commits since the freeze (origin tip `747e854da`, from a read-only `ls-remote`), none of them touching a build file | HELD |
| F3 | `app.build_hashes()` at `f7b03a732` equals the manifest | HELD |
| R1 | All 10 open rows of the frozen `WILL_QUEUE.md` (463 422 477 531 31 548 495 556 547 559) appear exactly once; desk has no errors | HELD |
| R2 | WQ-558 shown under History only, no answer controls | HELD |
| X1a | Original ❌1 (save A → deliver → save B → PROME integrates A): card shows A's words as recorded, group History | HELD |
| X1b | Original: delivering B afterwards is refused | HELD |
| X1c | New: A→B→C, A and B delivered, receipt on B. Card shows B as recorded; A and C listed separately | HELD |
| X1d | New: delivering C afterwards is refused | HELD |
| X1e | New: a new save after integration is refused | HELD (but the wording is wrong, see W-D) |
| X1f | New: restore on a fresh clone with fresh state shows B recorded and History | HELD |
| X1g | New: receipt on A arrives after B was delivered. A is shown as recorded; B is labelled "delivered · not the recorded answer" | HELD |
| X1h | New: integration lands on origin, Will does not sync, and delivers B. The deeper `deliver()` guard refuses ("PROME already recorded an answer") | HELD |
| X1i | New: `needs_clarification` receipt on A, then B is saved; B delivers | HELD |
| X1j | New: A is integrated while PROME keeps WQ-559 OPEN with a reworded follow-up question. The card stays in History showing the old terms; the new question is invisible and cannot be answered | FAILED (W-C) |
| Y1–Y3 | Original ❌2 cases (reword, close by moving to RECENTLY DONE, add `⛔ waits`), then sync and deliver: all refused, and the card shows the block | HELD (3) |
| Y4 | New: change only the Notes cell on origin, no sync: refused | HELD |
| Y5 | New: flip only the Rec cell from A to B, then sync: refused | HELD |
| Y6 | New: change the row, then revert it exactly: delivery allowed (no false block) | HELD |
| Y7 | New: PROME edits WILL_QUEUE in the shared tree (uncommitted): refused, and the foreign edit is preserved | HELD |
| Y8 | New: options file text changes while the row stays byte-identical: refused | HELD |
| Z1 | New race: PROME edits the shared working tree during the weekday check: refused | HELD |
| Z2 | New race: PROME commits a reword in the shared tree during the weekday check: refused | HELD |
| Z3 | New race: a second clone closes WQ-559 on origin during the weekday check. The answer is committed locally and safe-push rejects it (non-fast-forward). The ordinary closeout (`pull --rebase` + `safe-push.sh`) then publishes the answer to PROME's inbox for the closed question, and the packet carries no staleness flag | FAILED (W-A) |
| Z4 | New race: the same closure lands between the final check and safe-push. Same outcome as Z3 | FAILED (W-A) |
| S8 | New: the ❌2 repair's own recovery path. Stale A is refused ("review and save again"); B is saved superseding A; delivering B fails with 409 "Missing predecessor", and every later revision fails the same way | FAILED (❌R1) |
| V1 | New: "Save on this computer" A, revise to B, deliver B: 409 "Missing predecessor" | FAILED (❌R1) |
| V2 | New: revise again to C and deliver: 409 "Missing predecessor" | FAILED (❌R1) |
| V3 | Delivering the superseded A instead: refused | HELD |
| V4 | New, HANDS row: save `defer` locally, then `report_done` and Send: 409 "Missing predecessor" | FAILED (❌R1) |
| V0 | Control: the same V1 flow at the previous revision `2cc5e1acd` (its own scratch acceptance) delivers B with 200, so V1 is a regression introduced by `f7b03a732` | HELD at `2cc5e1acd` |
| W1a | Fork (desktop delivers A, laptop holds unsent B, laptop syncs): both exact answers visible; only WQ-559 blocked | HELD |
| W1b | Fork: delivering laptop B is refused | HELD |
| W1c | New: during the fork, another item (556) can still be saved and delivered end to end (CATO had tested only that it was respondable) | HELD |
| W1d | New: during the fork, PROME integrates desktop A. The laptop shows A as recorded and B as not recorded | HELD |
| W1e | New: laptop reopened with a fresh state. Local B is not shown (it was machine-local only; its untracked export file survives) | HELD (as disclosed) |
| W2a | New: a required check cannot read its input (`GATES.tsv` mode 000). Result: 503 "Response remains saved; delivery is unconfirmed", no packet created, answer kept | HELD |
| W2b | A weekday flag in a dirty foreign `GATES.tsv`: delivered, the advice is shown, the commit has exactly 2 paths, and the dirt is preserved | HELD |
| W2c | New: the commit-time hook (`account_guard`) refuses the commit. Result: an opaque 503 "(CalledProcessError)". The packet and the response are left STAGED in the shared index. Revising the answer then fails with "Missing predecessor" | FAILED (W-B, and ❌R1) |
| W10a–d | New: the options row shows no Approve or Disapprove; `openVerdict` on an options row opens nothing; an empty scope refuses; the saved words are only "I approve: <scope>" plus "Conditions:"; zero API calls before Send | HELD (4) |
| W11a | New: Approve with the condition "but I disapprove of lever (c)" is refused as contradictory (conservative) | HELD |
| W11b | New: Approve, then toggle the action select away and back. The verdict is silently dropped, but the dialog title still reads "Approve a specific decision", and the saved words are just "go ahead" | FAILED (W-E, minor) |
| W11c | New: an Approve draft followed by "Other response" excludes the verdict | HELD |
| W11d | New: a scope typed under Approve carries into Disapprove (it is visible in review) | HELD (note) |
| W11e | New: free text containing both phrases is refused | HELD |
| R3 | Send commits exactly its 2 own paths; a foreign staged file and a foreign unstaged edit are untouched | HELD |
| R6 | No Send commit touches `WILL_QUEUE`, `proposals/` or `decisions/receipts/` | HELD |
| R4c | Clicking Deliver again on a delivered answer makes no duplicate commit | HELD |
| R4 | Unrelated origin commit (non-fast-forward): refused, a retry without rebase is refused, and after `pull --rebase` the answer is delivered exactly once | HELD |
| R5a–c | `desk.html` changed mid-run, a new process on the changed build, and `safe-push.sh` changed mid-run: all read-only and saves refused | HELD (3) |
| R7 | Acceptance revoked on origin with no sync: deliver refused; read-only after sync | HELD |
| R6b | `QueueStore.acknowledge` raises: the app cannot write receipts | HELD |

## Findings

### ❌R1 (new, a regression): any answer that supersedes a never-delivered answer can never be delivered, and this includes the ❌2 repair's own "review and save again" path

- **Claim:** `deliver()` now rebuilds the answer chain only from the event itself plus answers committed at HEAD and origin. A predecessor that was saved on this computer but never committed (because Will used "Save on this computer", because a stale answer was refused, or because a check or commit failed) is therefore "missing". `chain()` raises "Missing predecessor" for the revision and for every later revision. The card meanwhile reports `can_deliver: True` with no block and shows the "Deliver saved response" button. The item is wedged in the app for good: the old answer is refused as superseded, a new answer with no predecessor is refused ("Another response exists"), and there is no in-app recovery. The 503 and 409 wording ("Sync and retry") does not explain the wedge. The same flow delivered at `2cc5e1acd`.
- **Artifact:** `delivery.py:72-86` (`events = {event["id"]: event}` plus HEAD/origin only, then `chain(...)` at :86); `queue_store.py:261` (card `can_deliver` computed from the local chain, which does include the predecessor); `pilot_files.py:281-282` (`Missing predecessor`).
- **Command:** `tools/s7.py` (V1, V2, V4), `tools/s8.py` (S8), `tools/s7prev.py` (V0 control at `2cc5e1acd`).
- **Observed:** V1 `409 Missing predecessor`; V2 the same; V4 (HANDS) the same; S8: stale A refused ("review and save again") → B saved, card `can_deliver True, block ''` → deliver B `409 Missing predecessor`. V0 at `2cc5e1acd`: `200 Delivered`.
- **Proposed change:** in `check_queue_delivery`, also load this WQ's locally restored events (the QueueStore chain the card was built from, passed in from `app.operate`) before calling `chain()`. Keep the three refusals: latest-only, integrated receipt, current terms. An undelivered local predecessor is not published, and the delivered event's `supersedes` already names it, so no extra file needs committing. Add regression tests for: save-local → revise → Send; stale refusal → re-save → Send; hook refusal → revise → Send; with V3 (superseded A is still refused) and W1b (fork is still refused) as neighbours.

### Warnings (⚠️)

**W-A. A change that lands on origin during Send's checks is not refused; the answer is committed locally, and the routine closeout publishes it to the closed question. The handoff claim "checks again … before publication" overstates this.**
- **Claim:** only the first check (`delivery.py:125-128`) fetches. The later checks at `:144`, `:157` and `:170` compare against the stale local `origin/master`. If origin changes in that window, the app commits, safe-push rejects the push (non-fast-forward), and the app says "Saved and committed locally; publication not confirmed. CATO must reconcile Git." The commit then sits on shared master. Any agent's ordinary closeout (`pull --rebase` + `safe-push.sh`) publishes the packet to PROME's inbox with no staleness flag. Afterwards the card shows "delivered" plus a "Saved terms are no longer current" notice. A same-tree PROME edit during the checks IS refused (Z1, Z2).
- **Artifact:** `delivery.py:136-144`, `:157`, `:170-177`.
- **Command:** `tools/s5.py adv-origin`, `tools/s5.py prepush-origin`.
- **Observed:** Z3 and Z4 both give "committed locally". After the closeout: origin has the packet, WQ-559 is closed on origin, and the packet mentions no stale terms.
- **Why ⚠️, not ❌:** the window is seconds long and needs a push from another clone or machine during Send. Under serial single-machine operation PROME edits the same tree, and those edits are caught. The event carries its own saved `queue_row`, and PROME still needs the matching chat confirmation.
- **Proposed change:** fetch inside `exact_working_files()` before the final check. Write the saved row's sha256 into the packet text with the line "if the current row differs or is closed, treat as stale". In the "committed locally" message, tell Will that a later closeout will publish the commit and that he should not confirm it in chat if the terms changed. Name this in the acceptance residue.

**W-B. A commit-hook refusal leaves the packet and the response staged in the shared index, with an opaque message.**
- **Claim:** `git add` (`delivery.py:164`) runs before a commit that a hook can refuse (`:167`). The `CalledProcessError` becomes "delivery is unconfirmed (CalledProcessError). Sync and retry", which is wrong: retrying can never pass, because the event is immutable. Both paths stay staged (`A `). Combined with ❌R1, revising the answer cannot be delivered either. Also note: per `scripts/account_guard.py`'s docstring the repository is PUBLIC (INFERRED, not checked), so Send publishes Will's free-text words publicly; the guard catches only labelled or known account numbers.
- **Artifact:** `delivery.py:158-168`; `server.py:77-78`.
- **Command:** `tools/s6.py` W2c (note "account no. •5678" — PROME redacted the reviewer's synthetic 8-digit test number to its last four at commit: the repo is public and the account guard refused the full form).
- **Observed:** 503; staged `AGENTS/CATO/decisions/queue-responses/<id>.json` and `PROME/inbox/decisions-<id>-from-CATO.md`.
- **Proposed change:** on commit failure, unstage only the app's own two paths and remove a packet created by this attempt. Report "saved, not delivered: the repository refused the commit: <hook stderr>; revise the answer". In the review dialog, tell Will that delivered words are published to the repository.

**W-C. An integrated answer hides a still-OPEN row under the same WQ ID.**
- **Claim:** once any receipt for a WQ is `integrated`, the card is forced into History with the integrated snapshot's terms and "PROME recorded this exact answer. No further answer is needed", even when `WILL_QUEUE.md` still has that WQ OPEN with new terms. No second card is shown. This is not a regression (the same logic existed at `bad623943`), but it breaks "every open row represented once and true" whenever PROME keeps a row open after integrating.
- **Artifact:** `queue_store.py:232-234`, `:248-256`.
- **Command:** `tools/s2.py` X1j.
- **Observed:** 1 card, History, old question text, `can_respond False`.
- **Proposed change:** if a current OPEN row exists and differs from the integrated snapshot's `queue_row`, show a notice "still open in PROME's queue with changed terms; answer in chat", or show the current row read-only. Otherwise make it a named PROME rule: integrating closes the row, and follow-ups take a new WQ ID.

**W-D. Refusal wording blames acceptance.** "Daily responses await final acceptance; this view is read-only" is returned for an item that is closed or integrated (X1e) and for a mid-run build change (R5a), not only before acceptance. Artifact: `queue_store.py:266-267` with `app.py:168-170`. Proposed change: pass the card's actual reason through.

**W-E (minor). The verdict is dropped silently on an action switch.** After Approve, toggling the action select clears the verdict (`desk.html:33`), but the title stays "Approve a specific decision". The saved words are only the conditions ("go ahead"). The review screen shows the exact words, so the risk is limited. Proposed change: reset the title in `onchange`, or refuse review while the title and verdict disagree.

## Declared residue (W1 chooser, W3–W9, W12): judgment

None of it is ❌-class for a first live use by one operator who still has to confirm in chat. Every item either fails closed or affects only PROME's own intake tooling:
- **W1 chooser:** a fork blocks only that WQ (W1a–W1d). Both answers stay readable; chat is the fallback.
- **W3:** advisory only; the exact pathspec commit is the real guard, and it held (R3).
- **W4/W5:** PROME tooling, so PROME's intake must read the packets and events directly, not rely on `pending`.
- **W6:** needs a PROME procedure rule: push the ruling before committing an integrated receipt, and check that the receipt's WQ and time match.
- **W7:** fails closed.
- **W8:** labelling only.
- **W9:** disclosed (and see the public-repository note in W-B).
- **W12:** cosmetic.
- **Desktop/laptop restore:** still unobserved and should stay named.

## Verdict for `f7b03a732`

**HOLD.** There is one ❌ (❌R1, a regression in the main reply path that also defeats ❌2's own recovery), plus 5 ⚠️ (W-A to W-E). The two original blockers are otherwise repaired: ❌1 held across all 9 of its variants, and ❌2's refusals held across all 10 non-race variants. After a ❌R1 fix and a targeted re-read of ❌R1 and its neighbours (V0–V4, S8, W2c, W1b), **ACCEPT WITH NAMED RESIDUE** (W-A to W-E plus the declared W1/W3–W9/W12 items) would be appropriate.

## Plain judgment

Will cannot yet safely start using replies. The good news: the two things that went wrong last night are fixed. The app now shows the answer PROME actually recorded, and it refuses to send an answer whose question was reworded, closed or blocked. I tried 19 variants of those two problems, and every non-race one held. Sending is still careful: it commits only its own two files, leaves other desks' work alone, fails safely when the remote has moved, and goes read-only when its files change or PROME withdraws acceptance.

The repair broke something basic. If Will saves an answer without sending it and then changes his mind, the changed answer can never be sent. The button says it can be sent, but the app refuses with "Missing predecessor". The same trap catches the recovery the app itself tells him to use when a question's wording has changed ("review and save again"). Nothing wrong reaches PROME, but the item is stuck in the app and he would have to answer in chat.

The fix is small and local. Once it is in and briefly re-checked, the app is reasonable to switch on, with chat confirmation still required. There is also one narrow, cross-machine timing case in which a stale answer could reach PROME's inbox after an ordinary closeout. Chat confirmation and the saved terms inside the answer file cover that case for now.

## Real repository

`git status --porcelain` in `/home/willi/Research-workspace`: **empty at start** (09:24 ET) and **empty at end** (09:49 ET). In between, another session's uncommitted PROME work appeared (GATES, SCRATCH, WILL_QUEUE, WQ_LEDGER, ORCH_LOG, an inbox rename, an archive file) and that session then committed it. HEAD moved to `747e854da` and beyond through other sessions' commits. None of these changes is mine. This reviewer wrote nothing in the real repository and ran no fetch, push, Send or safe-push against it; its only remote access was one read-only `git ls-remote`.
