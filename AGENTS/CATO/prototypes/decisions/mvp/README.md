# Decisions — local daily desk

Open **Decisions → Open Decisions** in the Agent Launcher, or run from the repository root:

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/app.py --open-browser
```

The page reads the existing PROME queue and your saved responses. **Decisions**, **Tasks for me**, **Follow-through** and **History** keep their full source wording. Mixed/action rows stay intact in Follow-through rather than being guessed into new decisions. WQ-558 appears in History with the real A response, integrated receipt and a separately attributed owner implementation record. Prior approvals are never re-requested.

**Current release status:** completion build, author-tested, awaiting one consolidated independent acceptance. It opens read-only until PROME publishes the accepted build record described below. The earlier pilot's acceptance does not silently authorize changed code or general replies. The queue remains authoritative; this release does not make structured records the source of the queue.

## Everyday use after acceptance

1. Open Decisions. **Sync latest records** fetches receipts and applies remote commits only when the checkout is clean and has no diverging local commits. Concurrent owner work is preserved; unresolved Git work is reported.
2. Select a view and choose **Respond** near the top of an item. Write your decision/option letter and conditions, report a personal task done, ask a question, or defer with a return condition. A mixed row needs you to identify its part; no options are inferred from prose.
3. **Review response** shows the full terms and your exact words. **Save & deliver to PROME** saves first, exports one immutable event, commits only that event and its inbox pointer, and runs the repository safe-push protocol. A failed delivery leaves the saved answer available for retry. **Save on this computer** is available separately.
4. Confirm the same answer in PROME's chat under the retained local-user trust rule. PROME writes its own receipt and ruling. A receipt records interpretation, not completed implementation. Sync shows the latest receipt; a closed question cannot be answered again. No app operation launches an agent or executes the proposed work.

The browser is local to the current computer. Keep its terminal open while using it. SQLite is machine-local and ignored by Git; immutable event files and owner receipts travel through the repository. An actual desktop restore of the saved WQ-558 answer/receipt remains to be observed at the next ordinary machine switch; local fixture clones are not that observation.

## Final acceptance and owner operation

PROME receives one completed-code review request. Its independent reader must devise counterexamples for closed queue rows, bad/unpublished pins, missing events, mixed rows, stale terms, concurrent replies, delivery retries and staged foreign files. Author tests are not independent acceptance.

After acceptance, PROME publishes `PROME/decisions/app-acceptance.json`:

```json
{
  "schema_version": "decisions-app-acceptance/1",
  "queue_responses": true,
  "matching_chat_confirmation": true,
  "independent_review": {"path": "PROME/reports/REVIEW.md", "commit": "FULL_PUBLISHED_COMMIT"},
  "build_hashes": {}
}
```

Replace `build_hashes` with `app.build_hashes()` from the reviewed build. It covers the daily app, shared core, owner receipt helper and parser dependencies. The acceptance file and review must be published, the working acceptance file unchanged, and current build hashes exact. The app then enables replies through the existing queue without a source-authority migration. No acceptance file is created by CATO's app. A changed build returns to read-only.

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

## Verification

```sh
# From this directory; all writes use temporary fixture repositories/stores.
python3 -B -m unittest test_mvp test_pilot_files test_pilot_launch test_desk -q
# From repository root; Windows Chrome and local HTTP required.
python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_desk_browser.py
python3 -B scripts/agents_gui.py --smoke-test
```

The daily desk tests use a local bare Git remote and preserve an unrelated staged file through delivery/retry. Native browser fixtures exercise real forms at desktop/narrow widths; actual-history mode only reads the real completed pilot. `desk-validation.json` records author evidence. No fixture answer is published to the real repository.

The original fictional rehearsal and copy comparison remain available under their existing commands and files. Their dated evidence and the original pilot acceptance are preserved in the [continuing report](../../../runs/2026-10-30_1059_wq-decision-workflow.md). They are not the current release status.
