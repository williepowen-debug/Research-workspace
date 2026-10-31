# Decisions desk: independent counterexample review

Reviewer: independent Opus counterexample reader for PROME. Written 2026-10-30 22:20 ET (from `date`).
Targets: CATO `bad623943` (full review) and `2cc5e1acd` (Approve and Disapprove buttons, added mid-review).
Every write path ran only in disposable clones under `.../scratchpad/desk-review/c/`, each with a local bare `origin` (`remote.git`, `r4.git`, `rv.git`, `rx.git`, `ry.git`, `rz.git`, `rh.git`, `ru.git`). The acceptance file and the review fixture exist only in those bare remotes. Harness: `tools/h.py`, `tools/opt.py`, `tools/btn.js`.

## Revision check (`bad623943` → `2cc5e1acd`)

`git diff --stat bad623943 2cc5e1acd`: of the build files, only `mvp/desk.html` changed (+7/−2). No byte changed in `app.py`, `queue_store.py`, `delivery.py`, `options.py`, `history.py`, `owner_receipt.py`, `pilot_files.py`, `store.py`, `server.py`, `willq_view.py`, `safe-push.sh` or the hooks. The `desk.html` hash in `release-review.json` changed to match. In `2cc5e1acd`, `render()` still draws "Your saved response" from `c.last` beside the integrated receipt, so ❌1 applies to both revisions. Every backend finding applies to both. W10 and W11 apply only to `2cc5e1acd`.

Baseline: CATO's 79 tests pass in a clone. That is not evidence for this review. The build hashes in the clone match `release-review.json`.

## Counterexamples: 66 tried · 50 held · 16 failed

| # | Case | Result |
|---|---|---|
| 1 | All 10 OPEN rows of the real `WILL_QUEUE.md` appear once each. Independent pipe split: question, type, due date, recommendation, Notes and the full row all match. 8 HANDS and 2 DECISION. | HELD |
| 2 | Closed WQ-558: History card, integrated receipt, no answer controls | HELD |
| 3 | Send end to end: HTTP capability, save, export, exact two-path commit, safe-push, fresh-fetch confirmation, state `delivered`. A foreign staged file and a foreign unstaged edit are left untouched. | HELD |
| 4 | Non-fast-forward: refused ("committed locally; publication not confirmed"). Retry refused. After a manual `pull --rebase`, the retry delivers. | HELD |
| 5 | Sync while local work has diverged: fetches only, does not rebase | HELD |
| 6 | App killed before commit, then retry | HELD |
| 7 | App killed after commit, mid-push (uncertain publish), then reopen and retry: idempotent, no duplicate packet | HELD |
| 8 | Two windows sharing one state: the second fresh answer is refused | HELD |
| 9 | Two instances in one tree with separate states: the fork is caught and the second delivery refused | HELD (but see W1 and W7) |
| 10 | Desktop and laptop: an undelivered local answer plus a later answer from the other machine | FAILED (W1) |
| 11 | Delivering a superseded earlier answer: refused | HELD |
| 12 | Integrated receipt on a superseded answer: the card shows the wrong answer as recorded | FAILED (❌1) |
| 13 | A later answer is delivered after the question was integrated | FAILED (❌1) |
| 14 | `desk.html`, `safe-push.sh`, `pre-commit`, `willq_view.py` or `history.py` changed while running: save and deliver refused | HELD (5 cases) |
| 15 | `core.hooksPath` unset: read-only | HELD |
| 16 | New process started with a changed build file: read-only | HELD |
| 17 | Working-copy edit to the acceptance file: read-only | HELD |
| 18 | Acceptance revoked on origin, then sync: read-only, delivery refused | HELD |
| 19 | An advisory `claim_check` flag in a dirty PROME file | FAILED (W2) |
| 20 | Answer saved, then PROME rewords the row and publishes: the old-terms answer is delivered with no flag | FAILED (❌2) |
| 21 | Answer saved, then PROME closes the row: delivered to a closed question | FAILED (❌2) |
| 22 | Answer saved, then the row is marked `⛔ waits`: delivered | FAILED (❌2) |
| 23–25 | Valid options block: buttons shown, no default, choice saved word for word (`display/2`). An unknown choice ID is refused. A free-text reply carrying a choice ID is refused. | HELD (3) |
| 26–42 | The options source refuses buttons in each of these cases: wrong row hash · wrong WQ ID · HANDS row · MIXED row · duplicate IDs · one choice · extra field · pointer under `AGENTS/` · pointer under `PROME/decisions/` · subdirectory pointer · missing file · two blocks · block nested in `~~~~` · block in a list · wrong schema · source committed but not pushed · dirty source | HELD (17) |
| 43–44 | Info string `decisions-options extra` and a tilde fence are both accepted (CommonMark first word) | HELD (note W12) |
| 45 | History: a RULED file committed locally but not pushed is not shown | HELD |
| 46 | History: a local edit is labelled "not published yet" | HELD |
| 47 | History: a locally deleted file is labelled the same way | HELD |
| 48 | History: a symlinked RULED file is refused and listed as an error | HELD |
| 49 | History: a one-paragraph RULED file renders | HELD |
| 50 | History: order within one date | FAILED (W8) |
| 51 | Orphan receipt: whole desk read-only | HELD |
| 52 | Forged response hash in a receipt: card error | HELD |
| 53 | Integrated receipt whose evidence is unpublished: card error | HELD |
| 54 | `owner_receipt.py --ruling-commit origin/master`: helper writes a receipt the reader rejects | FAILED (W4) |
| 55 | Integrated receipt citing an unrelated RULED file, with `at` set before the answer was saved: shown as "Decision recorded" | FAILED (W6) |
| 56 | Receipt committed but not pushed: shown as "Received by PROME" | FAILED (W6) |
| 57 | Integrated receipt without confirmation evidence: refused | HELD |
| 58 | `owner_receipt.py pending` with one committed but unpublished event: crashes | FAILED (W5) |
| 59 | The app never writes the queue, rulings or receipts: `acknowledge` raises, and every Send commit touches exactly two paths | HELD |
| 60 | (`2cc5e1acd`) One click on Approve or Disapprove makes zero API calls; it only opens the editable dialog | HELD |
| 61 | (`2cc5e1acd`) Disapprove sets action `reply`, `choice_id` null, so no alternative is selected | HELD |
| 62 | (`2cc5e1acd`) Approve on a row that has an options block | FAILED (W10) |
| 63 | (`2cc5e1acd`) Approve quotes the whole recommendation cell, including side claims | FAILED (W10) |
| 64 | (`2cc5e1acd`) "Other response" opened after a verdict draft | FAILED (W11) |
| 65 | (`2cc5e1acd`) Edited Disapprove draft, then Approve: one reply contains both | FAILED (W11) |
| 66 | (`2cc5e1acd`) Diff shows no backend file changed | HELD |

## Findings

### ❌1: an integrated receipt on a superseded answer shows the wrong answer as recorded, and the later answer can still be sent to the closed question

- **Claim:** after PROME integrates answer A, and Will has since saved B (which supersedes A), the History card shows B's words under "Your saved response", next to "Decision recorded" and "PROME recorded this answer. No further answer is needed." PROME actually recorded A. B also keeps its "Deliver saved response" button, and delivering it succeeds.
- **Artifact:** `queue_store.py:231-235`: `last = events[-1]`, and `receipt = integration or …`. `desk.html` `render()` (`bad623943`:23; `2cc5e1acd`:26) draws `c.last` beside `c.receipt`. `app.py:180` checks only that the event is the latest. `delivery.py:67-69` validates only the event itself, not whether the question is still open.
- **Command:** clone `c6` (`tools/h.py`): save A → deliver → save B (supersedes A) → `owner_receipt.py prepare A integrated … --write`, commit, push → `GET /api/display` → `POST /api/deliver` with B.
- **Observed:** `group: History | receipt for: A | last shown: "Actually B: keep copies per item." | can_respond: False`. Delivering B returned 200 "Delivered to PROME's inbox."
- **Proposed change:** when an integration exists, show the integrated event as the recorded answer. Label any later events "saved after PROME recorded the decision, not delivered". `deliver()` refuses any event on a unit whose chain contains an integrated receipt. Add a regression test that asserts the displayed words come from the event named by `receipt.response_id`.

### ❌2: Send does not check that the saved answer's terms are still current

- **Claim:** "Save on this computer" followed by a later "Deliver saved response" publishes an answer whose queue row has since been reworded, closed or blocked. No flag appears on the card, in the packet or in the event. The card shows the current terms beside the older answer, so the screen implies the answer concerns terms it never saw. `PILOT_CONTRACT.md` (acceptance properties) says changes to the live queue row invalidate a pending answer. The queue Send path does not enforce this.
- **Artifact:** `delivery.py:67-72`: `validate()` → `queue_store.validate_reply` (`queue_store.py:70-78`) checks the row only at the event's own `source_commit`, not against the current published row. `app.py:175-186`: `can_deliver` is desk-wide, and card errors (row missing) do not block it. `queue_store.py:215-226` uses current terms for the card.
- **Command:** clone `o0u`: choose B → PROME publishes a rewording ("Thu Dec 31 (NO LONGER recommended)") → sync → deliver. Clone `xu`: `report_done` on 547 → PROME removes the row → sync → deliver. Clone `yu`: reply on 559 → PROME adds `⛔ waits: FALCON` → sync → deliver.
- **Observed:** all three returned 200 "Delivered to PROME's inbox." In the closed-row case the card itself showed the error "Published/current queue item unavailable", while `can_deliver` stayed True.
- **Proposed change:** in `deliver()`, under the lock, compare the event's `queue_row` (and option text, if any) with the current published row. If they differ, or the row is closed or blocked, refuse: "Terms changed since you saved this; review and save again". The saved answer is kept. On the card, show the saved snapshot's terms beside a saved answer, with a "terms have changed" notice.

### Warnings (⚠️)

**W1. A desktop/laptop fork wedges the desk and hides the saved answer.**
- **Claim:** an answer saved but not delivered on one machine, plus an answer delivered from the other machine, puts the first machine into "Conflicting branches" after sync. Every card goes read-only and the local answer is not displayed. There is no in-app path to deliver it, discard it or reconcile.
- **Artifact:** `queue_store.py:174-199` (`restore` → `chain`); `app.py:112-119` and `149-151`.
- **Command:** clones `c5D` and `c5L`.
- **Observed:** desk errors `['WQ-559: Conflicting branches…']`, `can_deliver False`, 0 respondable cards, 559 `last=None`.
- **Proposed change:** scope the error to that WQ. Show both answers. Offer "keep the published one / replace it with this one" as a superseding save. At minimum, display the local answer.

**W2. An advisory `claim_check` flag blocks Send.**
- **Claim:** Send treats `claim_check` rc 1 (the tool is "advisory, never blocks") as fatal. It scans other owners' working copies, including dirty uncommitted edits. On failure it leaves an untracked packet in `PROME/inbox/`, and the UI says "Saved safely. Delivery needs attention: Save not confirmed (CalledProcessError)", which contradicts itself.
- **Artifact:** `delivery.py:85-112`; `server.py:315-316`.
- **Command:** clone `c12`, with a fixture weekday flag in a dirty `GATES.tsv`.
- **Observed:** HTTP 503; `?? PROME/inbox/decisions-…-from-CATO.md` left behind.
- **Proposed change:** run `claim_check` on the packet only, or treat rc 1 as advice. Write the packet only after the checks pass. Map a failed subprocess to a clear "saved, not delivered: <check> failed" message.

**W3. `orphan_check.sh` can never fail.**
- **Claim:** `orphan_check.sh` always exits 0 and its output is discarded, so this "required check" certifies nothing.
- **Artifact:** `delivery.py:113-114`; `scripts/orphan_check.sh:60,90`.
- **Command:** read the script.
- **Observed:** `exit 0` on every path.
- **Proposed change:** drop it, or parse its output. The pathspec commit is the real guard.

**W4. The receipt helper writes a receipt the reader rejects.**
- **Claim:** `owner_receipt.py` accepts symbolic refs (`origin/master`, `HEAD`) for evidence and writes an immutable receipt that the reader then rejects permanently ("must be pinned").
- **Artifact:** `owner_receipt.py:372-377` against `pilot_files.py:430`.
- **Command:** clone `zu`, R4.
- **Observed:** helper rc 0; the card then shows the error "Receipt evidence must be pinned".
- **Proposed change:** require 40-hex commits in `prepare`.

**W5. `owner_receipt.py pending` crashes on one unpublished event.**
- **Claim:** `pending` crashes on any committed but unpublished event, which blocks PROME's whole intake list.
- **Artifact:** `owner_receipt.py:352-361`, `400-408`.
- **Command:** clone `zu`, R8.
- **Observed:** rc 1, `ValueError … Committed regular file missing`.
- **Proposed change:** report that event as "unpublished" and continue.

**W6. Receipt display trusts unpublished receipts and unchecked integrations.**
- **Claim:** receipts are read from HEAD, so an unpublished receipt shows as "Received by PROME" or "Decision recorded". An integrated receipt is not checked against the WQ, the ruling text or time order: R5 cited an unrelated ruling, with `at` set in 2020, before the answer was saved.
- **Artifact:** `pilot_files.py:403-446`.
- **Command:** clone `zu`, R5 and R6.
- **Observed:** `card_receipt=received`, and `integrated` with no error.
- **Proposed change:** read receipts at `origin/master`, or label them "local". Reject `at` earlier than `saved_at`. Record in the acceptance that the WQ match is left to PROME's judgment.

**W7. One bad record anywhere disables every card.**
- **Claim:** one bad record anywhere (an orphan receipt, a pointer on a HANDS row with no saved events, a fork) disables every card and every delivery. This fails closed, but it also blocks unrelated answers.
- **Artifact:** `app.py:105-119`, `149-151`.
- **Command:** R1; v3; case 9.
- **Observed:** respondable 0.
- **Proposed change:** scope errors to the WQ involved. Keep the desk-wide block only for errors about receipt or event integrity.

**W8. History order within a date is not chronological, and the page does not say so.**
- **Claim:** within a single date, History is sorted alphabetically in reverse, not chronologically, and the on-page scope text does not say so. Example: WQ-549 (11:17 ET) is listed below WQ-550 (10:46 ET).
- **Artifact:** `history.py:182-183`.
- **Command:** `tools/dump.py` on the real tree's clone.
- **Observed:** the order shown in `rep.json`.
- **Proposed change:** add "ordered by file date; same-day order is not answer order" to the `scope` string.

**W9. Send pushes the whole committed backlog (disclosed).**
- **Claim:** one Send click publishes every committed but unpushed fleet commit (the safe-push train). The review dialog discloses this.
- **Artifact:** `delivery.py:126`; `desk.html` review text.
- **Command:** read the code.
- **Observed:** as designed.
- **Proposed change:** none required. Keep it as named residue in the acceptance.

**W10 (`2cc5e1acd` only). Approve quotes too much, and on an options row it skips the explicit choice.**
- **Claim:** Approve quotes the whole recommendation cell, so approval covers side claims too. The real WQ-556 cell includes "The separate predictive leg … stays WALTER's by 11/06 (DOCKET L334)". On a row with an explicit options block, Approve saves free text with `selected_choice: null` instead of choosing the option PROME recommends.
- **Artifact:** `desk.html` `2cc5e1acd`:23-25 (`hasRecommendation`, `verdictWords`, `openVerdict`).
- **Command:** `node tools/btn.js desk-2cc5.html`.
- **Observed:** note is `"I approve PROME's recommendation as shown:\n**Rec A.** $0; … The separate predictive leg stays WALTER's by 11/06."`, with `action reply` and `chosen null`.
- **Proposed change:** on an options row, map Approve to `choose` only when PROME's block names a recommended ID; otherwise hide Approve. Ask PROME to keep the Rec cell to the decision itself, or label the quote "PROME's full recommendation text, including its side notes".

**W11 (`2cc5e1acd` only). The verdict text carries over and can contradict itself.**
- **Claim:** the verdict prefix stays in the draft and appears under "Other response", whose title reads "Your response". If Will edits the prefix, a later Approve keeps both "I approve…" and "I disapprove…" in one reply, and that reply can be saved and sent.
- **Artifact:** `desk.html` `2cc5e1acd`:25 (prefix stripping is exact-match only).
- **Command:** `node tools/btn.js`.
- **Observed:** the pending note holds both verdicts.
- **Proposed change:** keep the verdict as a separate field, not note text. Clear it under "Other response". Refuse Review when both verdict phrases are present.

**W12 (minor). The options block accepts a longer info string than the README describes.**
- **Claim:** `decisions-options extra` is accepted, although the README says "exactly one … `decisions-options` fenced JSON block".
- **Artifact:** `pilot_files.py:117`.
- **Command:** v11d.
- **Observed:** buttons shown.
- **Proposed change:** document the first-word rule, or require the exact info string.

## Plain judgment

The Send transport is careful. It commits exact pathspecs, leaves foreign work alone, fails closed on non-fast-forward, makes retries idempotent, goes read-only on any build change or revocation, and never writes the queue, rulings or receipts. No path lets an app answer become Will's ruling without PROME's own receipt and evidence; the matching chat confirmation remains PROME's assertion, as disclosed.

It is not yet safe for real replies. Two defects can put a wrong or stale answer in front of Will or PROME as if it were current. ❌1: after a revised answer, the History card shows the wrong answer as the one recorded. ❌2: a saved answer is delivered after its question was reworded, closed or blocked, with no warning. Both fixes are small and local (`deliver()` currency and integration check; card shows the integrated or saved terms). After those, plus W1 and W2, ACCEPT WITH NAMED RESIDUE (W3–W12) would be appropriate.

**Verdict:** HOLD, for `bad623943` and for `2cc5e1acd`.

## Real repository: no change by this reviewer

`git status --porcelain` in `/home/willi/Research-workspace` was empty at start (21:57 ET) and empty at the end. HEAD moved during the review because of other sessions' commits: `9f8fd0e81` (PROME), `2cc5e1acd` (CATO) and `c0687f8b7` (ORACLE). None is mine.
