# Decisions — local daily desk

Open **Decisions → Open Decisions** in the Agent Launcher, or run from the repository root:

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/app.py --open-browser
```

The page reads the existing PROME queue and your saved responses. **Decisions**, **Tasks for me**, **Follow-through** and **History** keep their full source wording. Mixed/action rows stay intact in Follow-through rather than being guessed into new decisions. History now includes **Recently decided**: the 20 newest dated, published `PROME/proposals/*-RULED.md` files by filename date, with literal owner wording and all corrections available. A ruling file can contain several WQ decisions; this is not a complete chat ledger and is not sorted by inferred answer times. WQ-558's saved A, receipt and separately attributed implementation remain below these records. Prior approvals are never re-requested.

**Current release status:** accepted and live on October 31, 2026. PROME's final independent read accepted `4955b465f` with named residue and no blocker; acceptance was published under WQ-564 A at `9b5ed5994`. Matching chat confirmation remains required. Any fingerprinted code/dependency change returns the app to read-only until fresh acceptance. The queue remains authoritative; this release does not make structured records the source of the queue.

## Everyday use after acceptance

1. Open Decisions. **Sync latest records** fetches receipts and applies remote commits only when the checkout is clean and has no diverging local commits. Concurrent owner work is preserved; unresolved Git work is reported.
2. On a decision without explicit options, **Approve** and **Disapprove** open a scope field: name the specific decision you mean and add conditions separately. The full recommendation stays reference text; it is never copied wholesale into your approval. Switching verdicts keeps your conditions and replaces the generated verdict; **Other response** clears the verdict. A response containing both “I approve” and “I disapprove” cannot proceed to review until clarified. Where PROME supplies explicit choices, use those choice buttons; no recommended option ID is inferred from prose. None is preselected. Tasks use **Respond**. Mixed rows require you to name the part you mean.
3. **Review response** shows the full terms and your exact words. **Save & deliver to PROME** saves first, exports one immutable event, commits only that event and its inbox pointer, and runs the repository safe-push protocol. Like ordinary repository closeout, the push also carries other already committed work on master; the review screen states this. Foreign staged/unstaged work is not committed by Send. A failed or uncertain delivery leaves the saved answer available for retry. Only the latest eligible response can be delivered through the app. Send fetches once, then checks that fetched published state and current working terms, option text, competing replies and integrated receipts before creating the packet and again before committing/pushing. Later checks do not refetch origin; a remote change during Send remains the named W-A race. Changed, closed, blocked or already recorded items refuse delivery while preserving the saved answer. Weekday findings remain visible advice; failure to run a required check reports “saved; not delivered”. **Save on this computer** is available separately. Revisions can supersede never-sent versions: Send reads the current local response chain as well as committed history at each guard. It publishes only the selected event and its packet; it does not publish earlier private drafts.
4. Confirm the same answer in PROME's chat under the retained local-user trust rule. PROME writes its own receipt and ruling. A receipt records interpretation, not completed implementation. History shows the exact event named by an integrated receipt; other saved answers remain separately labelled with their own terms and delivery state. A closed question cannot be answered again. No app operation launches an agent or executes the proposed work.

The browser is local to the current computer. Keep its terminal open while using it. SQLite is machine-local and ignored by Git; immutable event files and owner receipts travel through the repository. An actual desktop restore of the saved WQ-558 answer/receipt remains to be observed at the next ordinary machine switch; local fixture clones are not that observation.

## Final acceptance and owner operation

PROME receives one completed-code review request. Its independent reader must devise counterexamples for closed queue rows, bad/unpublished pins, missing events, mixed rows, stale terms, concurrent replies, delivery retries and staged foreign files. Author tests are not independent acceptance.

Under WQ-564 A, after the final independent review returns ACCEPT or ACCEPT WITH NAMED RESIDUE with no blocking finding, PROME publishes `PROME/decisions/app-acceptance.json`:

```json
{
  "schema_version": "decisions-app-acceptance/1",
  "queue_responses": true,
  "matching_chat_confirmation": true,
  "independent_review": {"path": "PROME/reports/REVIEW.md", "commit": "FULL_PUBLISHED_COMMIT"},
  "build_hashes": {}
}
```

Replace `build_hashes` with `app.build_hashes()` from the reviewed build. It covers the daily app, options/history readers, shared core, owner receipt helper, parser dependencies, safe-push/check/install helpers and the standard Git hooks/account guard. `core.hooksPath` must be `scripts/githooks`. The acceptance file and review must be published, the working acceptance file unchanged, and current build hashes exact. An already-running process also refuses writes if those files change; reopen after an update. The app then enables replies through the existing queue without a source-authority migration. No acceptance file is created by CATO's app. A changed build returns to read-only. These are local-user checks, not protection from a malicious process on the same account or a global lock on concurrent Git writers.

## Explicit option source (PROME authors; CATO only reads)

For a single open `DECISION` row, PROME may append this exact pointer inside its Notes cell:

```text
<!-- decisions-options: PROME/proposals/YYYY-MM-DD_example.md -->
```

That Markdown proposal must contain exactly one top-level `decisions-options` fenced JSON block:

```decisions-options
{
  "schema_version": "decisions-options/1",
  "wq_id": "901",
  "queue_row_sha256": "SHA256_OF_EXACT_QUEUE_ROW_WITH_POINTER_WITHOUT_NEWLINE",
  "choices": [
    {"id": "A", "label": "Do the named task", "meaning": "Only this task, subject to the stated conditions.", "consequence": "The owner performs the task."},
    {"id": "B", "label": "Decline", "meaning": "Do not perform this task.", "consequence": "No change."}
  ]
}
```

This is a documentation example, not a registered decision. Obtain the exact row through `queue_store.open_rows(queue_text)[wq]["row"]`; hash its UTF-8 bytes with SHA-256. Publish the row and source together. Each ID is unique, with 2–20 choices; all four choice fields are required. A changed row requires a matching hash update. The published and current source bytes must agree. A broken pointer/block/hash is an error, never permission to guess choices or fall back to an unbound selection. MIXED/ACTION/HANDS rows cannot attach options: PROME must first make their decision scope explicit.

The new snapshot dialect `decisions-queue-display/2` includes the exact option source text, path, commit and choices alongside the original queue row. The immutable event remains `decisions-queue-response/1`; legacy `/1` snapshots and free-text events retain their original validation. The selected choice object is saved verbatim, with separate operator conditions. This supplemental block does not generate or replace the queue and does not adopt the wider `wq-record` source-authority migration. PROME's final acceptance must cover this option contract before use.

History displays each published ruling's opening paragraph and full text, including embedded follow-up decisions and corrections. Unpublished local changes are labelled while the published record remains visible. App answer save time and PROME receipt time are separately labelled in Eastern time; neither is relabelled as the time Will spoke. No ruling, time or completed-work conclusion is extracted heuristically.

PROME can inspect new replies with:

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/owner_receipt.py pending
python3 -B AGENTS/CATO/prototypes/decisions/mvp/owner_receipt.py prepare EVENT_ID received
```

`prepare` prints JSON by default. `--write` is for PROME's owner action only: it creates one immutable receipt, never commits or pushes. For `integrated`, supply `--ruling-path`, `--ruling-commit`, `--confirmation-path`, and `--confirmation-commit`; both references must resolve under PROME/proposals at published commits and the ruling path ends in `-RULED.md`. The helper does not decide whether the wording actually matches; that is PROME's judgment. PROME changes the queue and publishes the ruling first, then writes/commits its receipt. Receipt states remain received, needs_clarification, rejected_stale and integrated; no completed-work state is invented.

## Data and rollback

- Original supervised-pilot events: `AGENTS/CATO/decisions/responses/` (unchanged).
- Daily queue replies: `AGENTS/CATO/decisions/queue-responses/`, dialect `decisions-queue-response/1`; exact published queue row and displayed terms retained.
- Owner receipts: `PROME/decisions/receipts/<event_id>/` (unchanged contract).
- Delivery pointer: `PROME/inbox/decisions-<event_id>-from-CATO.md`; processing may move it to `processed/`.
- Local stores: `local-state/queue-<WQ>.sqlite3` and the original `wq558.sqlite3`.

To disable responses, open with `--preview` or have PROME revoke its acceptance record. Do not delete or move response/receipt history. Restore an earlier application revision only together with its compatible acceptance; never rewrite saved events. Legacy `pilot_launch.py` retains its original acceptance pin and correctly refuses this changed core. Use `app.py` for the new desk.


## Review freeze and retained limits

`release-review.json` pins the accepted code and dependencies. Final read 3 is complete; its ledger is `PROME/reports/2026-10-31_decisions-desk-final-ledger.md`. No further review of this episode is authorized without Will's named approval. A later repair must return for fresh acceptance; do not casually edit fingerprinted files on the live installation.

A cross-machine answer fork now preserves both exact answers visibly and blocks only that item's new saves/delivery. Its minimum recovery is copying the originals for owner reconciliation; an in-app branch chooser is not implemented. Other integrity errors may still disable all cards. The independent ledger's retained warnings also cover symbolic receipt-reference input, unpublished-event intake, unpublished receipt display and missing receipt-time/semantic validation, same-date History ordering, and permissive option-fence info strings. These remain named acceptance residue, not repaired claims. Standard Send pushes other already committed work as disclosed. The orphan tool is advisory; its output is returned in the delivery check record, and exact pathspec commits enforce file scope.

A fresh store may begin with a published response whose never-sent predecessor is unavailable. That published answer remains readable/respondable with a visible history-gap notice; the immutable predecessor ID is preserved. A missing predecessor of an unpublished response still blocks delivery. Disconnected segments (for example, sent A → private B → sent C on a computer lacking B) are preserved but require reconciliation; the app does not guess the missing link or silently select a branch.

The October 31 re-check's W-A through W-E remain named: a concurrent remote update can leave a stale answer committed for later shared publication; a failed commit hook leaves the app's paths staged; an integrated WQ reused for a new question stays in History; some refusal messages wrongly mention acceptance; changing the action menu can leave a verdict title after clearing its verdict. PROME adopts direct packet/event reads instead of the pending helper, and publishes its ruling before committing an integrated receipt. Each response still requires matching chat confirmation. These procedure choices are owner-reported, not CATO runtime verification.

## Verification

```sh
# From this directory; all writes use temporary fixture repositories/stores.
python3 -B -m unittest test_mvp test_pilot_files test_pilot_launch test_desk test_desk_review test_revision_delivery -q
# From repository root; Windows Chrome and local HTTP required.
python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_desk_browser.py
python3 -B scripts/agents_gui.py --smoke-test
```

The daily desk tests use a local bare Git remote and preserve an unrelated staged file through delivery/retry. Native browser fixtures exercise real forms at desktop/narrow widths; actual-history mode only reads the real completed pilot. `desk-validation.json` records author evidence. No fixture answer is published to the real repository.

The original fictional rehearsal and copy comparison remain available under their existing commands and files. Their dated evidence and the original pilot acceptance are preserved in the [continuing report](../../../runs/2026-10-30_1059_wq-decision-workflow.md). They are not the current release status.

**Final-review residue:** W-F broadens W-A: a refusal after the app commits can leave that refused answer on shared master, publishable by the next Send or any desk's push. The local-history guarantee holds before commit, not through its race window. W-G: never-sent exports are untracked and not ignored under `AGENTS/CATO/decisions/queue-responses/`; a manual commit can publish them and falsely show delivery without an inbox packet. **CATO must never commit these files by hand or by directory; only the app's explicit Send owns those commits.** W-F/W-G repair is deferred to a later pass, with fresh acceptance required. PROME reports checking each packet's latest answer and current question before acting, in addition to matching chat confirmation.
