> Saved verbatim by PROME (prome-34) at 16:32 ET 2026-10-31 from the re-checker's ledger in the session scratchpad. Its harness scripts (`tools/*.py`), raw results and disposable clones lived in that scratchpad and are not preserved. Outcome: HOLD, not installed (DOCKET L897; WILL_QUEUE 579).

# Decisions WQ-570 focused repair: independent re-check (the one authorized focused re-check)

Reviewer: independent focused re-checker for PROME (WQ-570 A). Start 2026-10-31 15:55:51 EDT, end 16:22:58 EDT after clone cleanup (times from `date`).
Target: CATO candidate `1296e8bcb5ab3c8ea3e1c3750de05fa2f417b556`, tree `6cc6bf487809c6bfaf76d5b43fb60ef67ce99c8b`, parent `a859a531d`.

## Method and re-verification
- Package `AGENTS/CATO/prototypes/decisions/candidates/2026-10-31-wq570-focused/`: SHA-256 of bundle, candidate.patch, focused.patch = manifest; bundle head = commit; tree = packet; focused.patch (index lines aside) = `git diff a859a531d 1296e8bcb`.
- 22 manifest build hashes = the candidate's blobs = `release-review.json` `activation_template`. The 12 root pins equal the real working tree at 15:55 ET (they no longer do at 16:18 ET, see Installation).
- `desk-focused/base.git` = hardlinked bare copy of PROME's repro clone at the candidate + two scratch-only plumbing commits: fixture review `e1a023f6e`, fixture acceptance from `activation_template` `949d7ea1f`. `accepted()` returned True (smoke test: limit '', can_deliver True).
- Every scenario: own bare origin `desk-focused/r/<name>.git` (`--shared`), own full clone `desk-focused/c/<name>`; `git remote -v` asserted local before every Send/Sync/push. Real app over HTTP (`tools/h.py`, adapted from the earlier harness). Scripts: `tools/a1.py a2.py a3.py a4.py b1.py b2.py b3.py cc.py dd.py`, fixtures `tools/shadow.py`, `tools/h2.py`. Raw results: `out/results.jsonl`. CATO's 124 + 38 author checks were not used as evidence.

## Cases: 53 tried · 47 held (6 of them observations of already-named residue) · 6 failed

| # | Case | Result |
|---|---|---|
| A1.1 | S5j2 re-run: unpinned `post-commit` (commits inside the sparse set) only on origin, shared tree busy (foreign staged + unstaged) | HELD: 409 "Unreviewed publication hook refused: post-commit"; nothing on origin; hook never ran; shared status/index/HEAD unchanged; no temp residue |
| A1.2 | unpinned `prepare-commit-msg` only on origin | HELD (same) |
| A1.3 | unpinned `reference-transaction` only on origin (would run on the private fetch) | HELD (refused before hooks enabled) |
| A1.4 | symlinked hook entry (mode 120000) only on origin | HELD |
| A1.5 | NON-executable `post-commit` only on origin | HELD: ignored by rule, exact pair sent, hook never ran |
| A1.6 | unpinned executable hook in the SHARED `scripts/githooks` | HELD: refused, nothing published |
| A2.D1 / D3 / D4 | edited `claim_check.py` (text + exit 1) / `orphan_check.sh` that commits / `claim_check.py` that rewrites a queue row | HELD: desk read-only ("Build differs"), Send refused, edited code never ran, no commit, queue untouched |
| A2.D1c | same edit committed (unpushed) | HELD (read-only) |
| A2.D5 ×2 | control edits to the two repinned files | HELD (read-only); A2.0 restore → accepted again |
| A3.1 | W-I re-run: origin pre-receive sleeps 128 s, real 120 s timeout | HELD: 409 after 124.4 s "Response saved; publication status unknown. Sync before retrying or confirming in chat. TimeoutExpired" |
| A3.3–A3.5 | immediate retry while the first push is still in flight; then later retry | HELD: retry delivered; exactly ONE reply commit with exactly the pair on origin; later retry "Already delivered"; no temp residue |
| A4.1 | clean shared tree | HELD: exact pair; shared master fast-forwarded; message says so |
| A4.2 | W-H re-run: busy shared tree | HELD: exact pair; foreign work, index and HEAD untouched; message "Shared checkout preserved: 7e931d7c9, 0 ahead / 1 behind origin/master 8af99b9cf; tracked work is pending … use Sync" |
| A4.3–A4.4 | next desk closeout push after a busy-tree Send | as named residue: `safe-push` rc 1, incoming = the pair only; `pull --rebase` (no autostash) once the owner saved → push rc 0 |
| A4.5 | W9: already-committed owner commit on shared master | as named (W9): rides the push; see ⚠️ W-R on wording |
| B1a | unpinned `scripts/hashlib.py` at origin, imported by the PINNED account guard via the PINNED pre-commit, stages a third path | HELD: 409 "Publication must change exactly the two selected response/packet paths; refused" |
| B1b | same entry point pushes a side branch with new content | **FAILED**: 200 success; origin gained `refs/heads/shadow-b` |
| B1c | same entry point sets `push.followTags` + annotated tag | **FAILED**: 200 success; Send's OWN push carried `refs/tags/shadow-c` |
| B1d | same entry point starts a background process that moves master to an extra commit after the reply commit | **FAILED**: origin got the reply commit + `EXTRA-d`; app said 409 "Publication is not exactly one response commit; refused"; card says "delivered" |
| B1e | same entry point stages a third path and installs a one-shot `post-commit` that hides it behind a replace ref, then deletes itself | **FAILED**: 200 success, receipt "One response commit, exactly the two selected paths, and published pair verified after fetch."; origin's real reply commit `b6791e21c` changes THREE paths (pair + `scripts/EXTRA-e.md`), confirmed with `--no-replace-objects` on origin and in the shared clone |
| B2 | unpinned `scripts/argparse.py` in the SHARED tree (arrived by a normal pull), imported by the re-pinned weekday check during Send | **FAILED**: 200 success, same receipt; origin got `SHADOW-S commit during Send` + the pair; shared `PROME/WILL_QUEUE.md` left modified (D3 + D4 reopened) |
| B3.U1–U10 | `exact_pair_commit` on crafted commits: control; third file; mode change; gitlink; symlink third path; event path as symlink; merge commit; split across two commits; deletion of a similar file with `diff.renames=copies`; event committed 100755 | HELD (U10 accepted: bytes exact, mode only; not graded) |
| B3.U11 | third path hidden by a replace ref | **FAILED** (accepted as exact; the mechanism of B1e) |
| C.1–C.5 | R1 never-sent predecessor; hook refusal with synthetic digits (`98765432`, labelled synthetic); recovery with •5432; recorded answer E shown, later F refused; stale terms refused then H on new terms | HELD (C.3 by a scoped grep: digits absent from decisions/inbox paths at origin, shared HEAD and index; the 4 unscoped hits are pre-existing base data files) |
| D.1a–d | event-only half publication | HELD: card blocked with the replacement instruction, `can_respond` true; Send refused, nothing published; replacement Y sends exactly its pair; X's bytes on origin unchanged, X's words shown under earlier answers, Y supersedes X, local exports unchanged |
| D.2a–c | packet-only half publication | HELD: same; Z's local export byte-identical and shown |
| D.3 | intake after both replacements | both replacements "ready"; superseded X listed "needs_clarification … not delivered" (⚠️ W-S) |

## Findings: ❌ 2 · ⚠️ 2 new (minor)

### ❌ X-1. Unreviewed code from origin still runs inside Send's private publication checkout and changes what Send's own push publishes while Send reports exact success
- **Claim:** README "Private publication rejects unknown executable hooks and changed pinned helpers before enabling hooks"; receipt "One response commit, exactly the two selected paths, and published pair verified after fetch"; PROME properties 1 and 2.
- **Artifact:** `mvp/delivery.py:197-198` (sparse set materializes ALL of `/scripts/` from the base); `scripts/githooks/pre-commit` runs `python3 scripts/account_guard.py`, so Python resolves `import hashlib, re, subprocess` from the base's `scripts/` first; `delivery.py:176-187,305,311,332` (exactness checked with `rev-list`/`show`/`diff-tree` inside the same checkout, which honour `refs/replace`; `git push` sends the real objects); `delivery.py:315` (push honours the checkout's `push.followTags`); `delivery.py:333` checks only that the commit is an ancestor of origin/master.
- **Command:** `tools/b1.py` (fixture `tools/shadow.py`), `tools/b3.py` U11, mechanics `tools/b0_gitmech.sh`.
- **Observed:** B1e: 200 + the receipt above; origin reply commit `b6791e21c` changes 3 paths. B1c: 200; tag published by Send's own push. B1b: 200; side branch published during Send. B1d: extra commit published, reported "refused". B1a (third path staged without hiding): correctly refused.
- **Precondition:** an unpinned Python file named like a stdlib module in `scripts/` at the publication base (one commit by any desk to the public origin) — the same class as S5j2's planted hook. The same file would also run at every desk commit through the shared pre-commit hook, so the exposure is fleet-wide, but it defeats exactly what this repair claims.
- **Proposed change (each closes this ❌, none adds a parallel checker):** materialize only the pinned transport files (exact paths, not `/scripts/`) and refuse anything else under the private `scripts/`; set `PYTHONSAFEPATH=1` for Send's subprocesses (Python 3.12 here; hooks inherit it); push with `--no-follow-tags` and refuse if the private clone holds `refs/replace/*` or tags; move the after-fetch exactness check to the SHARED repository with `--no-replace-objects` (origin/master's new commits over the pre-push origin = the verified reply commit, diff = exactly the pair) plus one `ls-remote` showing no new ref but master.

### ❌ X-2. The re-pinned weekday check still executes unpinned code in the shared root before the base is fixed; a commit made then rides Send's push (D3 and D4 reopened)
- **Claim:** README "The date and orphan advisory implementations are repinned under WQ-570 because they execute with publication access"; PROME property 3 (cannot write the shared tree or add to the commit).
- **Artifact:** `delivery.py:274-276` (`python3 scripts/claim_check.py` with cwd = shared root, so `scripts/` is first on `sys.path`); `:277-278` (`base = delivery_base(repo)` read from shared HEAD AFTER the advisories; HEAD and index are not recorded before them).
- **Command:** `tools/b2.py`.
- **Observed:** 200, "One response commit, exactly the two selected paths…"; origin received `3d6966741 SHADOW-S commit during Send` + `1e4ebfe75` pair; shared HEAD moved during Send; shared `PROME/WILL_QUEUE.md` left modified.
- **Proposed change:** run the advisories as `python3 -I`; record shared HEAD and the index tree before them and refuse if either changed when the base is fixed.

### ⚠️ W-R (wording). The success receipt says "One response commit, exactly the two selected paths" while the same push also published W9 riders (A4.5: `PROME: local unpushed note` rode with no mention). Name riders in the result, or say "plus N already-committed workspace commits".
### ⚠️ W-S (noise, W-N class). After a replacement, intake still lists the superseded half-published answer as "needs_clarification: Published response lacks its exact inbox packet; not delivered" (D.3), and a packet-only answer's packet stays in `PROME/inbox` pointing at an unpublished response. Fail-closed; no wrong answer passes.

Carried, re-observed as named: W-H busy-tree lag (A4.3), W9 (A4.5). W-K, W-M..W-Q not re-run. Everything else asked for held: properties 1–4 against hooks, edited advisories, timeout, busy tree; R1, recorded answer, stale terms, hook-refusal recovery, synthetic guard; the replacement path keeps the original words byte-for-byte.

## Installation: what it still requires (do not install this candidate: verdict HOLD)
- **W-L:** at 16:20 ET origin/master holds NO queue reply events and NO `decisions-*` inbox packets (only the integrated WQ-558 pilot), so nothing is delivered-but-unreceived today. Re-list at install time (`git ls-tree -r origin/master AGENTS/CATO/decisions/queue-responses/` against receipts): the live app can deliver until then. Receiving writes new receipt files only. Saved-but-unsent answers on Will's machine (local state, not opened) will read "Saved terms are no longer current" after install because `desk.html` changes; Will re-saves; the old events/exports are not altered.
- **W-P:** at 16:20 ET nothing staged under the reply paths, no unpushed commit touches them, `queue-responses/` absent in the working tree. Re-run at install: `git diff --cached --name-only` and `git log origin/master..HEAD --name-only` must show nothing under `AGENTS/CATO/decisions/queue-responses/`, `AGENTS/CATO/decisions/responses/`, `PROME/inbox/decisions-*`. A non-empty result blocks install for owner reconciliation; unstaging, `git rm` or trashing reply exports is the one step that could lose a real saved answer, so none of it is done implicitly.
- **Pinned-root drift (new):** at 16:18 ET the real working tree has `scripts/githooks/pre-commit` modified (WQ-578 G1 #41, docket row cap retired). It is pinned by this candidate AND by the live acceptance (`7da0c8e6…`): while that edit stands the live app is read-only (fail-closed, no answer altered), and an install would have to pin bytes this re-check did not review. WQ-578 G3 may also touch `claim_check.py` (pinned). Settle those files before freezing the next candidate.
- **W9 at install:** the real master was 3 commits ahead of origin at 15:55 ET; unpushed commits ride the first Send.
- Then: apply the 15 candidate paths (none changed on real master since base), publish `PROME/decisions/app-acceptance.json` pinning the installed bytes with `independent_review` at its full commit, re-run "Open Decisions" once.

## Verdict
**HOLD.** ❌ 2 (X-1, X-2). ⚠️ 2 new minor (W-R, W-S). The four targeted properties hold against every case in the original ledger and against the hook-form variants; they fail against unreviewed code that reaches Send through Python import resolution of the pinned helpers, and the in-checkout exactness check can be blinded by that code. The proposed changes are small and replace checks rather than add them.

## Real repository: untouched by this reviewer
Start `git rev-parse HEAD` = `5fa82213ce11dd3f1045c6504d47763712197038` (15:55:51 ET). End = `a88c01e3ed18b5ae75b53e4cc5effccdd383e736` (16:22:58 ET, unchanged since 16:18); the four new commits are other sessions' (PROME f29c9b0e5, afbbfa709; WALTER 7bf36fa9a, a88c01e3e). The `scripts/githooks/pre-commit` modification is not this reviewer's.
This reviewer wrote, staged, committed, stashed, reset, checked out and pushed nothing there, and ran no app, Send, Sync, intake or safe-push there. Access: `cat`/`sed`/`grep`/`ls`/`find`/`sha256sum`; `git rev-parse`, `status` (first call without `GIT_OPTIONAL_LOCKS=0`, so Git may have refreshed its stat cache; content unchanged), `config --get/--list`, `log`, `show`, `diff`, `ls-tree`, `tag -l`, `for-each-ref`, `bundle list-heads`. One `git fetch --dry-run` was run there at ~16:19 ET by mistake; checked afterwards: no new pack or loose objects since 16:18:50, `FETCH_HEAD` unchanged (16:00:00, another session), refs unchanged. Will's Decisions local state was not opened; no real answer, receipt, ruling or acceptance was created. All writes ran in `desk-focused/` scratch clones with local bare origins; the clones were deleted afterwards (tools/ and out/ kept).
