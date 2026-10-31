# Decisions work-reduction batch: independent counterexample review (read 1 of 1)

Reviewer: independent counterexample reviewer for PROME (read 1 of 1 for this change).
Start: 2026-10-31 12:55:07 EDT (from `date`). End: 2026-10-31 13:51:07 EDT (from `date`).
Target: CATO candidate `a859a531d42f706cec3817c0a53907cbd49b0166`, tree `825366d353c8a2f55a1ec59f751e1daba19713e3`, parent `3a9e489ba2acd3aa4e448f6c497caa14bca4ae82`, fetched by this reviewer from `AGENTS/CATO/prototypes/decisions/candidates/2026-10-31-work-reduction/candidate.bundle`.

**Method.** `desk-batch/base.git` = an unlinked copy of PROME's review clone plus my own fetch of the bundle, with two scratch-only commits on the candidate: a fixture review (`dd6268e7d`) and an acceptance built from `release-review.json` `activation_template` (`defcf25ec`); `app.accepted()` returned `(True, '')`. Every scenario had its own bare origin under `desk-batch/r/` (local; `git remote -v` asserted local before every Send, Sync and push) and its own full clone under `desk-batch/c/`; app temp files went to `desk-batch/tmp/<scenario>`. Drivers: the real app over HTTP (`tools/h.py`) and, for injections inside `deliver()`/`intake()`, an in-process driver (`tools/ip.py`, `out/ip_intake.py`). Scenario scripts: `tools/s1.py` … `tools/s9.py`, `s5x.py`, `s5l.py`, `s5h.py`, `s5j.py`, `s5late.py`, `s6*.py`, `s7*.py`, `s2c.py`. Raw results: `desk-batch/out/results.jsonl`. CATO's 116 + 38 checks were not run or used as evidence. The only synthetic account-like number used is shown here as •5432.

## Re-verification

| Check | Result |
|---|---|
| SHA-256 of `candidate.bundle`, `candidate.patch`, `confirmation-proposal.md` vs `manifest.json` | all three match |
| Bundle head / tree / parent | match the packet |
| 20 `build_hashes` vs the bundle commit's files; `release-review.json` `build_hashes` = `activation_template.build_hashes` = manifest | 20/20 match; all equal |
| Real `master` commits since base on the 14 candidate paths | none; under `scripts/` only `firetime_allowlist.tsv` (unpinned) changed (`adaa6fe20`) |
| Real working tree vs candidate pins | differ only in the 5 changed app files and the new `AGENTS/CATO/decisions/.gitignore` (absent live); every pinned dependency already equal |
| Fingerprint vs live `PROME/decisions/app-acceptance.json` (= live `release-review.json`) | removed: `scripts/claim_check.py`, `scripts/orphan_check.sh`; added: both `.gitignore` files; changed: `app.py`, `delivery.py`, `desk.html`, `owner_receipt.py`, `queue_store.py`; 13 unchanged |

## Counterexamples: 76 tried · 57 held · 19 failed

(FAILED = the counterexample exposed a limit; every one is graded ⚠️ below. No ❌.)

| # | Case | Result |
|---|---|---|
| 1 | Clean tree Send: one commit, exactly the event + packet, event bytes = saved export; shared HEAD fast-forwarded; no temp residue; card "delivered" (S1) | HELD |
| 2 | New export lands in ignored `mvp/local-state/exports/`; nothing under `queue-responses/` (S1) | HELD |
| 3 | Never-sent export not staged by `git add AGENTS/CATO/` nor by `git add -A` (S1) | HELD |
| 4 | Busy tree (foreign staged new file + foreign unstaged edit): exactly the pair; foreign work untouched; shared HEAD not moved; Sync only fetches (S2a) | HELD |
| 5 | After a busy-tree Send, the next desk's closeout `safe-push.sh` aborts non-fast-forward and needs root step 3 `pull --rebase --autostash` (S2a.5–6) | FAILED (⚠️ W-H) |
| 6 | Owner's unpushed commit on shared master rides Send's push; review dialog discloses it (S2b) | HELD (W9 as disclosed) |
| 7 | PROME commits locally during Send after the base is fixed: only the pair is published; shared master diverges; PROME's push then needs a rebase (S2c) | HELD (knock-on in W-H) |
| 8 | A tracked event file under the new ignore pattern still shows as modified (S2c.3) | HELD |
| 9 | Post-commit refusal: a 2nd Decisions process saves newer C during B's publication commit → B refused; origin, shared HEAD and shared index unchanged, no residue; an unrelated desk closeout push then publishes nothing of B; C sends afterwards (S3a) | HELD |
| 10 | Post-commit refusal: PROME edits the same row in the shared tree during the commit → refused; unrelated closeout push publishes nothing of it (S3b) | HELD |
| 11 | Post-commit refusal: acceptance revoked on origin during the commit → refused; nothing published (S3c) | HELD |
| 12 | Post-commit refusal: origin advances right after the commit → refused; nothing published (S3d) | HELD |
| 13 | Non-fast-forward at push → "not published", nothing left behind; retry → exactly one reply commit (S3e) | HELD |
| 14 | Push succeeds, then safe-push raises `TimeoutExpired` → app verifies and reports delivered (S3f) | HELD |
| 15 | Push succeeds, then the verification fetch fails → "publication status unknown"; retry → "Already delivered", one commit (S3g) | HELD |
| 16 | Push outlives the real 120 s timeout (origin pre-receive 128 s, real app, no patching) → app says "not published … No reply commit was left on shared master"; the pair lands on origin seconds later (S5late) | FAILED (⚠️ W-I) |
| 17 | R1: never-sent A → B → Send B: only B's pair; A's words absent from origin (S4.1) | HELD |
| 18 | Hook refusal (labelled synthetic account number) → 409 with hook text; shared index and HEAD unchanged; no residue (S4.2) | HELD |
| 19 | Recovery after refusal: D sends exactly its pair; the synthetic digits are absent from reply, packet and receipt paths at origin, shared HEAD and shared index (S4.3, scoped re-check) | HELD |
| 20 | Recorded answer: E delivered, F saved, PROME integrates E → card shows E's words in History; Send F refused (S4.5) | HELD |
| 21 | Stale terms: HANDS row reworded on origin → Send refused "review and save again"; H saved on the new row sends with it (S4.6) | HELD |
| 22 | Event-only (event committed by hand, no packet) → card "published without inbox packet" with recovery Send; intake not received; recovery commits only the packet (S5a) | HELD |
| 23 | Packet-only → card "saved"; Send commits only the event (S5b) | HELD |
| 24 | Packet moved to `processed/` (R100, as PROME does) → still delivered; retry "Already delivered"; intake finds it (S5c) | HELD |
| 25 | PROME holds an unpushed local commit that moves an earlier, already-published decisions packet to `processed/` → every Send refused "An earlier unpublished reply commit needs owner reconciliation" (S5e) | FAILED (⚠️ W-K) |
| 26 | Two Decisions processes Send at once → second refused "Another Decisions window is synchronizing"; it sends afterwards (S5h.1–2) | HELD |
| 27 | SIGKILL during the publication push → push completes; reopen; retry "Already delivered", one commit; no stale lock (S5h.4) | HELD |
| 28 | After that SIGKILL the private clone stays in TMPDIR (7 MB, alternates into the shared object store) and is never cleaned (S5h.3) | FAILED (⚠️ W-Q) |
| 29 | Unpinned `post-commit` hook arriving from origin that commits a file outside the sparse set → nothing extra published (S5j) | HELD |
| 30 | Unpinned `prepare-commit-msg` hook staging a file (outside and inside the sparse set) → nothing extra published (S5j, S5j2) | HELD |
| 31 | Unpinned `post-commit` hook arriving from origin that commits a file inside the sparse set (`scripts/…`) → its commit is pushed with the pair; Send still reports "Exact published response and packet verified" (S5j2) | FAILED (⚠️ W-J) |
| 32 | Shared master diverged from origin → Send refused; nothing published (K1) | HELD |
| 33 | Legacy committed (unpublished) reply on shared master → every Send refused for owner reconciliation (L1.2) | HELD |
| 34 | That legacy reply's card says "committed. Delivery is incomplete; use Deliver saved response"; Deliver always refuses (L1.1) | FAILED (⚠️ W-K) |
| 35 | An unrelated desk closeout push publishes the stranded legacy reply (L1.4) | FAILED (⚠️ W-P) |
| 36 | Legacy staged pair in the shared index: Send publishes only its own pair; staged pair untouched; Sync refuses (L2.1–3) | HELD |
| 37 | A CATO own-dir closeout (`git commit -- AGENTS/CATO/` + push) publishes the staged legacy event without its packet; the card then offers recovery Send (L2.4–5) | FAILED (⚠️ W-P) |
| 38 | Legacy untracked export becomes ignored, is not deleted, status clean (L3.0, E4) | HELD |
| 39 | Post-publication refresh will not overwrite an ignored legacy export of the same event (claim held); it then says "use Sync after current desk work is reconciled" with no desk work; Sync fast-forwards (L3.1–2) | HELD (wording note) |
| 40 | Sync over an ignored local file with different bytes at an incoming path overwrites it (L3.3). Pre-existing `pull --rebase`; same event ID means same bytes, so no realistic loss | HELD (outside batch claims; note) |
| 41 | `pending` writes no working-tree file; status, HEAD and branches unchanged (only `FETCH_HEAD`) (I1) | HELD |
| 42 | `intake --write` writes one received receipt; a repeat keeps exactly one (I2) | HELD |
| 43 | Intake never commits; it writes only receipts plus `mvp/local-state/intake.lock` (CATO's ignored directory) (I3) | HELD |
| 44 | Receipt is received-only: no ruling, confirmation or confirmed-hash fields (I4) | HELD |
| 45 | Three concurrent `intake --write` processes → one receipt (I5) | HELD |
| 46 | Old uncommitted `prepare … received --write` receipt (random ID) preserved; no second file (I6) | HELD |
| 47 | Old uncommitted `needs_clarification` receipt → intake refuses, no new file (I7) | HELD |
| 48 | Committed-but-unpushed received receipt → no duplicate (reason reads "terminal or duplicate") (I8) | HELD (wording in W-N) |
| 49 | Superseded published answer → "superseded"; the latest is ready (I9) | HELD |
| 50 | An unsent revision saved on THIS machine does not stop its published predecessor becoming ready (I10) | FAILED (⚠️ W-O) |
| 51 | A HEAD-only newer reply commit is ignored; its published predecessor gets a received receipt (I11) | FAILED (⚠️ W-O) |
| 52 | Published reword → needs_clarification, no receipt (I12) | HELD |
| 53 | PROME's in-progress working-tree reword → needs_clarification (I13) | HELD |
| 54 | Reword then exact revert → received (no false block) (I14) | HELD |
| 55 | Any `desk.html` change (as an install makes) → every delivered-but-unreceived answer refused "Terms changed" (I15) | FAILED (⚠️ W-L) |
| 56 | Malformed published items: invalid JSON, wrong filename, forged sibling are each reported on their own row (I16) | HELD |
| 57 | …but a bad sibling under the same WQ blocks the valid answer, with a reason that names the valid answer (I16) | FAILED (⚠️ W-N) |
| 58 | Row reworded between the locked re-check and the receipt write → received (I17) | FAILED (⚠️ W-M) |
| 59 | Published state changes between listing and lock → no write, "rerun" (I18) | HELD |
| 60 | Disconnected published chain (A local, B sent, C refused, D sent) → B and D needs_clarification; reason says "Conflicting branches" for a gap (S4.7) | HELD (fail closed; wording in W-N) |
| 61 | The real, integrated WQ-558 pilot is reported "needs_clarification: … not delivered" in every `pending`/`intake` (S4.7, I16) | FAILED (⚠️ W-N) |
| 62 | Options row: choose A and Send; intake ready (O1–O2) | HELD |
| 63 | Option meaning changed after delivery → intake refuses (O3) | HELD |
| 64 | Edited `claim_check.py`: app stays accepted (by design); Send runs it; its arbitrary text ("PROME recorded your answer as: B (Sat Jan 2)") appears in the post-delivery message (D1) | FAILED (⚠️ W-J) |
| 65 | `claim_check.py` exits 3 → Send refused, answer kept (D2) | HELD |
| 66 | `orphan_check.sh` edited to commit → its commit rides Send's push (D3) | FAILED (⚠️ W-J) |
| 67 | `claim_check.py` edited to rewrite another queue row → Send proceeds, shared `WILL_QUEUE.md` left modified; pair exact (D4) | FAILED (⚠️ W-J) |
| 68 | Control: editing pinned `scripts/githooks/pre-commit` → read-only (D5) | HELD |
| 69 | Control: editing pinned `AGENTS/CATO/decisions/.gitignore` → read-only (D5) | HELD |
| 70 | Control: editing pinned `mvp/.gitignore` → read-only (D5) | HELD |
| 71 | Control: editing pinned `scripts/account_guard.py` → read-only (D5) | HELD |
| 72 | Install rehearsal: an already-running old-build process goes read-only when files change (E2) | HELD |
| 73 | Installed candidate stays read-only until its acceptance is published (E3) | HELD |
| 74 | After install, an old-build saved answer and an old-build delivered answer are both flagged "Saved terms are no longer current … Terms changed" although the question did not change (E4) | FAILED (⚠️ W-L) |
| 75 | After install, revise and Send → exactly the new pair; the legacy export is kept and ignored (E5) | HELD |
| 76 | After install, intake of the old-build delivered answer → needs_clarification "Terms changed" (E6) | FAILED (⚠️ W-L) |

## Findings: ❌ 0 · ⚠️ 10 (W-H to W-Q, new)

### ⚠️ W-H. A Send while the shared tree is busy leaves shared master behind origin; the next closeout push by any desk then aborts and needs the root step-3 autostash recovery
- **Claim:** "Clean shared trees can fast-forward … busy trees remain intact pending Sync." That holds. What is unstated: Send now pushes from a private clone, so after any busy-tree Send the shared master lags origin by the reply commit. Every desk's next `safe-push.sh` aborts non-fast-forward until someone runs `git pull --rebase --autostash` (root step 3, which stashes every desk's dirty work). The accepted release pushed from shared master and never created this lag. The live tree is normally busy (WALTER and PROME had modified tracked files at review start).
- **Artifact:** `mvp/delivery.py:185-193` (`refresh_after_publication`), `:229` (`delivery_base`), `:264` (push from the private clone).
- **Command:** `tools/s2.py` (S2a.5–6); `tools/s2c.py`.
- **Observed:** S2a.5 `safe-push` rc 1, "ABORT: origin/master has commits not in local master … Missing locally: 24463d21e CATO -> PROME: deliver Decisions response b538c20aed96". The incoming set held only the pair. `pull --rebase --autostash` + `safe-push` gave rc 0. S2c: ahead/behind 1/1; first push rc 1, rc 0 after rebase.
- **Proposed change:** name it in the residue and in closeout guidance ("after a Decisions Send, one non-fast-forward is expected; the incoming set is the reply pair only"). Optionally, have the app fast-forward shared master when only untracked or ignored files are present, or have `safe-push.sh` recognise a pair-only incoming set.

### ⚠️ W-I. A push still in flight at the 120 s timeout is reported as definitely "not published", then lands on origin
- **Claim:** "It verifies the published pair after fetch, including ambiguous push outcomes." For a push that outlives the timeout, the app fetches once, immediately. It then tells Will "not published … No reply commit was left on shared master". `safe-push.sh`'s own contract says a killed run is CANNOT-CONFIRM. The repo is public (per `account_guard.py`), so Will can be told his words were not published when they were.
- **Artifact:** `mvp/delivery.py:263-276`; `scripts/safe-push.sh:37-41`.
- **Command:** `tools/s5late.py`: a local bare origin with a 128 s `pre-receive` hook; the real app over HTTP, not patched.
- **Observed:** 409 after 123.0 s: "Response saved; exact response and inbox packet are not published. No reply commit was left on shared master. Retry after reconciliation. TimeoutExpired". 20 s later, origin held exactly the pair. The card said "saved" until a retry, which answered "Already delivered".
- **Proposed change:** on `TimeoutExpired`, a killed run, or safe-push rc 2, return the existing "publication status unknown; Sync before retrying or confirming in chat". Say "not published" only for safe-push rc 1 plus a confirmed absence after fetch. Optionally re-fetch after a short delay.

### ⚠️ W-J. Code outside the fingerprint runs inside Send and can add to what Send publishes; Send's exactness check confirms only that the pair is present
- **Claim:** point 3, "only the date/orphan advisory implementation hashes leave the acceptance fingerprint … hook … rules stay pinned"; README, "Only these two paths are committed by Send". In fact only three named hooks are pinned and compared. Any other executable in `scripts/githooks/` at the publication base runs in the private checkout, including one that exists only on origin and was never checked out locally. The two unpinned advisories run in the shared root, under the transport lock, between the two currency checks and before `delivery_base` reads HEAD. After the commit, `deliver()` checks the pair's bytes at HEAD. It never checks that `base..HEAD` is one commit touching exactly two paths.
- **Artifact:** `mvp/delivery.py:161-162` (sparse set includes all of `/scripts/`), `:177-181` (six named files compared), `:225-229` (advisories before `delivery_base`), `:254-262` (presence-only checks); `mvp/app.py:25-32`.
- **Command:** `tools/s5j.py` (S5j2); `tools/s7.py`, `tools/s7b.py` (D1–D4).
- **Observed:**
  - S5j2: origin received "EXTRA via post-commit" (`scripts/EXTRA-post-commit.md`) on top of the pair commit. The app answered 200, "Exact published response and packet verified after fetch".
  - D1: a message after delivery read "Advisory findings (delivery completed): Weekday check: PROME recorded your answer as: B (Sat Jan 2)".
  - D3: origin received "orphan autocommit (fixture)" plus the pair.
  - D4: shared `PROME/WILL_QUEUE.md` was left modified.
  - In every case the pair's bytes, the answer shown as Will's and `accepted()` were unaffected.
- **Grade, ⚠️ not ❌:** PROME's test is met literally. Both removed files are shelled out to on the delivery path, and D3 shows that a changed `orphan_check.sh` adds to what Send pushes. I grade ⚠️ for four reasons:
  - No change to either file can alter the delivered pair, the words shown as Will's answer, or the acceptance check.
  - The push side effect is the accepted W9 mechanism: committed work rides the push.
  - The same changed tool acts at every desk's closeout (steps 1b and 1e) regardless of this app.
  - The hook gap already existed: the accepted release ran the same hook directory.
  If PROME applies its rule literally, this item alone converts the verdict to HOLD.
- **Proposed change:**
  - Before pushing, assert that `git rev-list --count base..HEAD` is 1 and that `git diff --name-only base HEAD` is exactly the pair.
  - Fix `delivery_base` and record HEAD, the index and the remote config before the advisories run; refuse if any of them changed.
  - Refuse when `scripts/githooks/` at the base holds an executable outside the pinned set, or commit with a hooks directory that holds only the pinned hooks.
  - Show advisory output as quoted tool output, apart from the delivery result.

### ⚠️ W-K. False "earlier unpublished reply commit" block, and a Deliver button that cannot work
- **Claim:** "Legacy unpublished reply commits already on shared master require explicit owner reconciliation." The check also matches PROME's ordinary unpushed processing commit (a `git mv` of an already-published `decisions-*` packet into `processed/`), so Will's Sends are blocked until PROME pushes. For a real legacy commit, the card tells Will to "use Deliver saved response", but Deliver always refuses.
- **Artifact:** `mvp/delivery.py:230-232` (the diff over `PROME/inbox`; the regex matches `processed/decisions-…`); `mvp/desk.html` `renderAnswer` (any state other than delivered or saved shows "Delivery is incomplete; use Deliver saved response").
- **Command:** `tools/s5x.py` (S5e); `tools/s5l.py` (L1.1).
- **Observed:** S5e: 409 "An earlier unpublished reply commit needs owner reconciliation; Send will not publish it implicitly" for an unrelated item. L1.1: `{"delivery": "committed", "card_can_deliver": true}`, then the same 409.
- **Proposed change:** treat as legacy only an added reply or response file, or an inbox packet whose event is not on origin. Exclude renames of published packets into `processed/`. While the block applies, hide Deliver and name who must reconcile.

### ⚠️ W-L. App build identity is part of the "unchanged terms" test: any `desk.html` change, including this install, fails every delivered-but-unreceived answer
- **Claim:** intake checks "unchanged question/options". The comparison does use the right reference: the event's own saved row and options, validated at its `source_commit`, against the current published, working-tree and HEAD row. It also compares `presentation_sha256` with the `desk.html` hash in the checkout where the check runs, and that is not a question term. After any `desk.html` change, delivered answers fail intake with "Terms changed since this answer was saved". Their cards show "Saved terms are no longer current", although the question did not change. The README covers only unsent saved answers ("may need re-review").
- **Artifact:** `mvp/queue_store.py:137` (`current_source`), `:145` (`check_current_snapshot`); `mvp/owner_receipt.py:88`.
- **Command:** `tools/s6b.py` (I15); `tools/s8.py` (E4, E6).
- **Observed:** I15: a one-byte `desk.html` commit, then needs_clarification. E4: delivered X carried the block "Saved terms are no longer current. Terms changed since this answer was saved; review and save again". E6: intake for X gave the same result.
- **Proposed change:** before installing, have PROME receive every answer delivered under the old build, or list those answers for Will to re-send. When only the presentation differs, say "the Decisions app changed since this answer was saved". Consider leaving presentation identity out of intake's terms test, since the event already records what was shown.

### ⚠️ W-M. Intake check-to-write interval
- **Claim:** intake checks the latest chain and unchanged terms, "then writes only received receipts". A row reworded between the locked re-check and the write still produces a received receipt.
- **Artifact:** `mvp/owner_receipt.py:158-168` (`inspect_event` under the lock, then `write_received`, with no check afterwards).
- **Command:** `out/ip_intake.py reword` via `tools/s6c.py` (I17).
- **Observed:** status "received"; receipt written; the row was reworded.
- **Proposed change:** re-run `check_current_snapshot` after the write, and flag or remove the uncommitted receipt if it fails. Otherwise, name it next to Send's check-to-push interval. PROME's ruling step re-checks the row in any case.

### ⚠️ W-N. Intake isolation and wording
- **Claim:** "`pending` … isolates bad items." Parse failures are isolated. A malformed but parseable sibling under the same WQ blocks the valid answer, and the reason names the valid answer. Separately:
  - the real integrated WQ-558 pilot is always reported as "needs_clarification: Published response lacks its exact inbox packet; not delivered", because its packet has the pilot's own filename;
  - a committed-but-unpushed received receipt is reported as "Receipt already terminal or duplicate received state";
  - a history gap is reported as "Conflicting branches".
  All of these fail closed. The cost is noise that PROME will learn to ignore.
- **Artifact:** `mvp/owner_receipt.py:60-62` (packet test before the terminal-receipt test), `:69-81` (one bad sibling raises for the whole WQ), `:36-38`.
- **Command:** `tools/s6c.py` (I16); S4.7; `tools/s6.py` (I8).
- **Observed:** the valid 556 answer got "Queue response hash mismatch" (the sibling's defect). The valid 559 answer got "Published response filename disagrees with its identity" (the sibling's defect). `383f964c` got "…not delivered" on every run.
- **Proposed change:** name the offending sibling's path in the reason. Test terminal receipts before the packet, or recognise the pilot's packet. Word a gap differently from a fork, and "committed, not pushed" differently from "terminal".

### ⚠️ W-O. Intake does not consult this machine's own unsent revisions or HEAD-only newer events
- **Claim:** README: "Private drafts on another computer are unknowable." Drafts on this computer are not consulted either. A saved unsent revision, or a newer reply commit at HEAD, does not stop its published predecessor from becoming ready or being received.
- **Artifact:** `mvp/owner_receipt.py:66-84` (the chain is built from `origin/master` only).
- **Command:** `tools/s6b.py` (I10, I11).
- **Observed:** I10: A2 "ready" while A3 (which supersedes A2) was saved locally. I11: B1 "received" and receipt written while B2 (which supersedes B1) was committed at HEAD.
- **Proposed change:** reword the limit as "unsent drafts and unpushed commits on any computer, including this one". Optionally report, without blocking, when local exports or HEAD hold a newer event for the WQ. Chat confirmation remains the backstop.

### ⚠️ W-P. Install precondition: the ignore rule does not neutralise staged or committed legacy reply files
- **Claim:** "legacy unsent exports are ignored without deletion"; legacy unpublished reply commits "require explicit owner reconciliation". Ignoring does not unstage a staged legacy pair (left by the old release's W-B). A routine own-dir closeout then commits and pushes the staged event without its packet. A legacy committed reply is published by any desk's closeout push. Send's block prevents neither.
- **Artifact:** `AGENTS/CATO/decisions/.gitignore` (affects untracked files only); `mvp/delivery.py:230-232` (blocks Send only).
- **Command:** `tools/s5l.py` (L1.4, L2.4).
- **Observed:**
  - L1.4: `safe-push` rc 0, and A's event was on origin.
  - L2.4: `git commit -- AGENTS/CATO/` plus a push put C's event on origin without its packet. The card then showed "published without inbox packet" with a Deliver button.
  - Mitigation: a W-B pair stems from an account-guard refusal, so the same guard would normally refuse that closeout commit too.
- **Proposed change:** add an install checklist. `git diff --cached --name-only` and `git log origin/master..HEAD --name-only` must show nothing under `AGENTS/CATO/decisions/queue-responses/`, `AGENTS/CATO/decisions/responses/` or `PROME/inbox/decisions-*`. In the real repo at review start, `queue-responses/` was absent and no such path was staged. Optionally, the app could report staged reply paths in the shared index.

### ⚠️ W-Q (minor). Crash residue
- **Claim:** "Failed commits die with this private clone." After a SIGKILL, the private clone survives in TMPDIR, and nothing removes it. It is 7 MB, has `objects/info/alternates` into the shared object store, and its push URL is the real origin.
- **Artifact:** `mvp/delivery.py:222`.
- **Command:** `tools/s5h.py` (S5h.3).
- **Observed:** `decisions-send-_ia3ygba` was still present after reopening and a successful retry.
- **Proposed change:** at startup, remove stale `decisions-send-*` directories, or name this in the residue.

### Notes (no grade)
- **Point 3 boundary, item by item:**
  - Neither removed file is imported, and neither is used by `accepted()`, `intake` or `pending`.
  - Both are run by `deliver()`, with cwd set to the shared root, before the private checkout exists.
  - Their exit codes gate Send in the fail-closed direction (D2). Weekday rc 1 output is shown after delivery.
  - Every other runtime dependency remains pinned: `willq_view.py`, `render.py`, the hooks, the account guard, safe-push, install-hooks and both ignore files (D5 controls held).
  - `jsonschema` (imported by `render.py`) was never pinned. That predates this candidate.
- Intake writes its lock file into CATO's ignored `mvp/local-state/`, and its CLI `git fetch` updates the shared repo's remote-tracking refs.
- Previously named residue was not re-run, except W9 (row 6) and the repairs of W-F (rows 9–12) and W-G (rows 2–3, 22). That residue covers W1, W3, W4, W6–W9, W12, W-C–W-E, disconnected history and device restore.

## Installation: what it requires, and hazards (rehearsed in `tools/s8.py`)

- **Requires:** apply candidate commit `a859a531d` (14 files, all under `AGENTS/CATO/`). It applies cleanly: no real-master commit since the base touched those files, and only the packaging commit `86578df24` touched the candidate directory. PROME must then publish a new `PROME/decisions/app-acceptance.json` whose `build_hashes` equal `app.build_hashes()` of the installed bytes (the 20 in `activation_template`), with `independent_review` pinned to the published review at its full commit. Until both land and are pushed, the app is read-only. That fails closed: rows 72–73.
- **Saved drafts:** every unsent answer saved under the old build is blocked as "Saved terms are no longer current" until Will re-saves it. Re-saving and sending works (row 75).
- **Delivered but not yet received answers:** they fail intake after install (W-L). Receive them before installing, or list them for Will to re-send.
- **Legacy exports:** none exist on the live machine now (`AGENTS/CATO/decisions/queue-responses/` absent at review start; no staged decisions paths). Any created before install are kept and ignored (row 38). Staged or committed legacy reply files are not neutralised (W-P), so run that check at install time.
- **Event and receipt history:** paths are unchanged. The new ignore rules do not untrack anything (row 8), and the tracked WQ-558 pilot event stays tracked.
- **Launcher:** the launcher (`scripts/agents.json`, `scripts/agents_gui.ps1`) changed on real master during this review (`886ec45c4`, `a3f2c24d4`, `eb1e5a0a3`). These files are not pinned and the Decisions entry is not in their diffs, but the candidate's reused prior launcher smoke predates them. Re-run "Open Decisions" once after install.

## Point 4: is the confirmation boundary understandable, and what is missing

The two choices are clear. "Keep confirmation everywhere" against "an explicitly eligible routine class is authoritative on Send". So is the rule that eligibility follows consequence rather than the HANDS/DECISION label, and so is the always-confirm list. The proposal is also candid about the local-account trust limit and about having no classifier. Consequences Will is not shown:

1. **The class may be empty on today's queue.** Read against the proposal's own exclusions, none of the 10 OPEN rows at the candidate tree looks eligible (INFERRED, my reading, not a classification).
   - Excluded as accounts, credentials or access: 531, 495, 31, 422.
   - Excluded as a positions screenshot: 548.
   - Excluded because each releases desk work: 547, 463, 477.
   - Excluded as a frozen prediction-letter date: 559.
   - Excluded as a standing routing rule: 556.
   The benefit should be stated as an expected count, not assumed.
2. **An authoritative Send publishes to a public repository.** The review dialog says "publishes", not "publicly". Under confirmation, Will can keep sensitive context in chat; under app authority, the published words are the record.
3. **"Uncertain delivery cannot be integrated automatically" cannot be enforced from PROME's side.** In W-I the app tells Will "not published" while PROME receives a normal-looking packet. PROME cannot see the app's uncertainty.
4. **A Send publishes more than the answer.** It carries other committed workspace work (W9) and anything unpinned code adds (W-J). Under app authority, Will's click becomes the trigger for that publication too.
5. **Only the latest Sent answer would count.** A newer revision that is saved but unsent has no effect, and intake does not look at it (W-O). The proposal also needs a rule for a revision sent after PROME has acted on an eligible answer.
6. **App updates force re-answering.** Answers delivered before a `desk.html` change fail intake (W-L). Under app authority, that re-answer burden recurs with every UI change.
7. **Cross-machine gaps block the item, not just the confirmation.** Disconnected published histories leave the item blocked for manual reconciliation on any machine, and on a fresh one the card itself is wedged (final ledger T9).

Missing implementation detail Will should know: "explicitly marked eligible" needs a structured, row-hash-bound field, like the options block. Otherwise eligibility is PROME's assertion at ruling time. The proposal says a scoped change is still needed; it should also say that review and acceptance of that change are required before any answer is treated as authoritative.

## Verdict

**ACCEPT WITH NAMED RESIDUE.** ❌ 0. ⚠️ 10 new (W-H to W-Q), plus the candidate's own named list.

The core claims held. A refused Send leaves nothing on shared master or in the shared index, including post-commit refusals followed by an unrelated closeout push, non-fast-forward, hook refusal, and push-then-timeout or push-then-fetch-failure. Drafts stay ignored; event-only and packet-only states recover; and the recorded-answer, stale-terms and R1 invariants all re-held. Intake writes exactly one received-only receipt under retries, concurrency and old receipts, never commits, and rejects superseded and stale answers.

Before acceptance is published:
- add W-H to W-Q to `retained_residue`;
- correct the "ambiguous push outcomes" and "Only these two paths are committed" wording (W-I, W-J);
- run the W-L and W-P install steps.

W-J is the item PROME may grade differently under its literal rule; if it does, the verdict is HOLD.

## Real repository: untouched by this reviewer

This reviewer wrote, staged, committed, stashed, reset, checked out and pushed nothing in `/home/willi/Research-workspace`. It ran no app, test, Send, Sync, intake or safe-push there.

Its access to the real repository was reads only:
- `cat`, `ls`, `sha256sum`;
- `git log`, `show`, `diff`, `ls-files`, `grep`, `merge-base`, `rev-parse`, `bundle list-heads`;
- one `git fetch` *from* the bundle file into the scratch `desk-batch/base.git`;
- `git status` at the start, as instructed. Git may refresh its stat cache during `status`, but content is unchanged. At the end it ran with `GIT_OPTIONAL_LOCKS=0`.

Will's real Decisions state (`mvp/local-state/`) was not opened. No real answer, receipt, ruling or acceptance was created. Every write ran in `desk-batch/` clones with local bare origins.

- **Start (2026-10-31 12:55:07 EDT):** `git rev-parse HEAD` = `fe8a41f199555921cd92a52cd0ae570ea52ad0d6`. `git status --porcelain -- AGENTS/CATO PROME`: ` M` on `PROME/SCRATCH.md`, `PROME/WILL_QUEUE.md`, `PROME/registry/WQ_LEDGER.crc`, `PROME/registry/WQ_LEDGER.tsv`, `PROME/registry/corrections_receipts.tsv` and `PROME/state/firetime_dispositioned.tsv`; `??` on `AGENTS/CATO/prototypes/calendar/`, `PROME/archive/WILL_QUEUE_ROWS_2026-10-31_rolloff.md` and `PROME/reports/2026-10-31_firetime-pickup-flags-disposition.md`.
- **End (2026-10-31 13:51:07 EDT):** `git rev-parse HEAD` = `8113bfea86cf95db2f784f7f08ee43ed40fe928e` (the start HEAD is an ancestor). `git status --porcelain -- AGENTS/CATO PROME`:

```
 M AGENTS/CATO/runs/2026-10-26_2115_agent-launcher.md
 M PROME/AUTONOMY.md
 M PROME/CLAUDE.md
 M PROME/state/ORCH_INFLIGHT.md
 M PROME/state/ORCH_LOG.tsv
 M PROME/tools/prome_gate.py
 M PROME/tools/spawn_list.py
?? PROME/proposals/2026-10-31_wq295-R2-encode-RULED.md
```

Every difference between start and end comes from other sessions' commits and edits (WALTER, CATO launcher and calendar, PROME, NEXUS, ISHM, HENRY; `git log fe8a41f19..HEAD`). None is this reviewer's.

Scratch footprint: about 79 GB of disposable clones under `desk-batch/c/`. They are left in place as evidence and can be removed at PROME's discretion.
