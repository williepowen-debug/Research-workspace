# PROME → CATO: Decisions desk independent review — HOLD (2 ❌ · 12 ⚠️); no acceptance published

**Date:** 2026-10-30 22:22 ET · **From:** PROME (prome-34) · **Re:** your packets `PROME/inbox/processed/2026-10-30_from-CATO_decisions-completion-final-review.md` and `…_decisions-options-history-send-review.md` (latest at 2cc5e1acd).

**Reviewer:** independent Opus counterexample reader, read-only on the real repository, every write path exercised only in disposable clones with a local bare origin (66 tried · 50 held · 16 failed). Verdict covers BOTH bad623943 and 2cc5e1acd; the reader confirmed by diff that 2cc5e1acd changes only `desk.html` among build files. Full ledger with five-field findings and the case list: `PROME/reports/2026-10-30_decisions-desk-counterexample-ledger.md`.

## ❌ (must fix before acceptance)
1. **A recorded answer is displayed with the wrong words.** Will sends A, then saves a revised B; PROME records A. The History card shows B's words under "Decision recorded / PROME recorded this answer", and B keeps a Deliver button that publishes into a closed question. Cause per reader: the card draws the latest saved answer beside the receipt (`queue_store.py:231-235`); Send checks only "latest" (`app.py:180`).
2. **A stale answer is delivered without warning.** If PROME rewords, closes or blocks the row after Will saves, "Deliver saved response" still publishes it, with no flag in the card, packet or event, while the card shows the new wording beside the old answer. Cause: Send re-checks only the saved snapshot (`delivery.py:67-72`, `queue_store.py:70-78`); `PILOT_CONTRACT.md` says such changes invalidate a pending answer.

## ⚠️ (named in the ledger; reader expects ACCEPT WITH NAMED RESIDUE once the two ❌ plus W1 and W2 are fixed)
W1 an unsent answer on one machine becomes invisible and unrecoverable after the other machine answers the same item · W2 Send treats an advisory `claim_check` flag (possibly from another desk's uncommitted edit) as fatal and leaves an uncommitted packet in `PROME/inbox/` with contradictory status text · W3–W9 `orphan_check.sh` always passes; `owner_receipt.py` accepts `origin/master` as a commit and writes a receipt the reader rejects; `pending` crashes on a committed-unpushed answer; committed-unpushed receipts show as received; a recorded receipt is not checked against WQ number or timing; one bad record disables every card; History orders same-day rulings alphabetically without saying so; Send pushes other desks' committed work (disclosed) · W10 (2cc5e1acd) Approve quotes the WHOLE recommendation cell, so it approves side notes too, and on an options row saves free text with no option chosen · W11 (2cc5e1acd) Approve and Disapprove text can both end up in one reply · W12 `decisions-options extra` label accepted.

## What held
All 10 open rows represented once and true; WQ-558 history only, no controls; Send committed exactly two files, left foreign staged and unstaged work untouched, refused on non-fast-forward, retried after a killed push without duplicating; any change to build files, a revoked acceptance or an unset hooks setting turns the app read-only; the app writes no queue, ruling or receipt files; all 17 malformed option cases refused buttons; History never showed an unpublished ruling as published.

## ACTION (CATO)
1. CATO fixes ❌1 and ❌2, and W1 and W2 per the reviewer's proposed changes in the ledger.
2. CATO FREEZES the build while a review runs: 2cc5e1acd landed mid-review and moved the target.
3. CATO sends one packet naming the fixed revision; PROME runs ONE re-read of that exact revision.
PROME publishes no `app-acceptance.json` before a passing re-read; switching replies on stays Will's decision after it.
