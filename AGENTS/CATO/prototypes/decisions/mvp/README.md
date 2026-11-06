# Decisions — local daily desk

Open **Decisions → Open Decisions** in the Agent Launcher, or run from the repository root:

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/app.py --open-browser
```

The page reads the existing PROME queue and your saved responses. **Decisions**, **Tasks for me**, **Follow-through** and **History** keep their full source wording. Mixed/action rows stay intact in Follow-through rather than being guessed into new decisions. History now includes **Recently decided**: the 20 newest dated, published `PROME/proposals/*-RULED.md` files by filename date, with literal owner wording and all corrections available. A ruling file can contain several WQ decisions; this is not a complete chat ledger and is not sorted by inferred answer times. WQ-558's saved A, receipt and separately attributed implementation remain below these records. Prior approvals are never re-requested.

**Installed status (October 31, 2026):** Will explicitly waived the further WQ-579 independent review and directed installation of tested candidate `bbf134770`. Acceptance is based on that operator approval and author tests, not a new independent verdict. The published acceptance record preserves the original review reference as historical evidence and separately records the waiver. Chat confirmation remains required for every answer. Reopen Decisions after this update; the queue remains authoritative.

## November 6 — plain-language explanations

The live application code now reads an optional `decisions-brief/1` block from the existing published `decisions-options` source. Question, what changes, recommendation, conditions and choices appear once; evidence stays expandable. Conditions remain visible. Supporting document links use the source commit on GitHub. Briefs do not generate choices, reopen closed items or change the queue's authority.

The original `/2` answer snapshot already preserves the entire source document, so it also preserves the exact brief shown. No new response dialect or delivery path is introduced. A source edit invalidates a pending answer through the existing text binding. Brief and option IDs accept the producer's integer or string form; booleans refuse. Missing or malformed briefs fall back to full terms on that card. A date-expired brief is hidden and the full explanation opens with a notice; the still-current explicit choices remain usable, per PROME's proposed date-only behavior. Wrong row bindings continue to refuse responses under the existing options reader. Historical saved briefs remain historical and do not expire out of their saved record.

**Activation remains with PROME:** [ready installation patch](../releases/2026-11-06-briefs/activation.patch) connects the still-open WQ-632 brief and refreshes the existing enablement record. WQ-599 and WQ-635 are no longer OPEN and are not reintroduced. This patch is prepared, not applied by CATO: PROME owns the concurrently active queue and acceptance record. No additional independent review is requested under Will's direct-live instruction. The prior shared `scripts/claim_check.py` change had already disabled replies before this work; the patch reconciles its inspected current bytes too. Reopen Decisions after the owner publishes activation. Until then the application remains read-only and unconnected cards retain their full queue wording.

Matching PROME-chat confirmation and prior W-S/legacy-pilot limits remain. Changes are author-tested, not independently reviewed; ordinary-use benefit is unmeasured.

## Everyday use after acceptance

1. Open Decisions. **Sync latest records** fetches receipts and applies remote commits only when the checkout is clean and has no diverging local commits. Concurrent owner work is preserved; unresolved Git work is reported.
2. On a decision without explicit options, **Approve** and **Disapprove** open a scope field: name the specific decision you mean and add conditions separately. The full recommendation stays reference text; it is never copied wholesale into your approval. Switching verdicts keeps your conditions and replaces the generated verdict; **Other response** clears the verdict. A response containing both “I approve” and “I disapprove” cannot proceed to review until clarified. Where PROME supplies explicit choices, use those choice buttons; no recommended option ID is inferred from prose. None is preselected. Tasks use **Respond**. Mixed rows require you to name the part you mean.
3. **Save & deliver** saves the exact reviewed answer, then prepares its selected response and inbox packet in a temporary publication checkout. It checks current terms and local history before and after commit, pushes with the existing Git safeguards, and verifies both artifacts after fetching. A refusal leaves no candidate commit or staged reply on shared master. An uncertain push says so; retry first checks for an already-published pair. Only these two paths are committed by Send; other already-committed owner work can still travel in the push. The shared working tree advances only if clean and safe to fast-forward, without overwriting ignored files. Otherwise delivery is complete and current owner work stays in place until Sync/reconciliation. Failed checks keep the saved answer. Weekday findings remain visible advice; failed execution blocks Send. Never-sent answers stay in ignored local state.
4. Confirm the same answer in PROME's chat under the retained local-user trust rule. PROME writes its own receipt and ruling. A receipt records interpretation, not completed implementation. History shows the exact event named by an integrated receipt; other saved answers remain separately labelled with their own terms and delivery state. A closed question cannot be answered again. No app operation launches an agent or executes the proposed work.

The browser is local to the current computer. Keep its terminal open while using it. SQLite is machine-local and ignored by Git; immutable event files and owner receipts travel through the repository. An actual desktop restore of the saved WQ-558 answer/receipt remains to be observed at the next ordinary machine switch; local fixture clones are not that observation.

## Final acceptance and owner operation

**This upgrade:** Will's explicit October 31 WQ-579 review waiver supersedes the further-review prerequisite below for candidate `bbf134770` only. The legacy `independent_review` field points to the actual original-release review, labelled historical; `acceptance_basis` and `operator_approval` identify the current authority. No review result was invented and no runtime integrity check was disabled. Later acceptance changes retain their own applicable authorization.

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

PROME can check all published answers and prepare received receipts with one command:

```sh
# Read-only report (fetches published state; no receipt writes):
python3 -B AGENTS/CATO/prototypes/decisions/mvp/owner_receipt.py pending
# PROME owner action: mechanical checks plus idempotent received receipts:
python3 -B AGENTS/CATO/prototypes/decisions/mvp/owner_receipt.py intake --write
# Optional single-item scope:
python3 -B AGENTS/CATO/prototypes/decisions/mvp/owner_receipt.py intake --event-id EVENT_ID --write
```

Intake checks the exact published packet/event, latest observable published chain, current queue/option wording and existing receipts. A malformed item is reported separately; unchanged valid items remain inspectable. Unpublished HEAD-only events are excluded. Private drafts on another computer are unknowable, and disconnected published histories require reconciliation. Reports name the fetched revision; rerun before acting if the question or published answers have changed. `received` means the mechanical intake passed; it is neither Will's confirmation, a ruling nor completed work. Concurrent/repeated intake preserves one immutable received receipt, including before its owner commit. The command never commits, pushes, rules or edits the queue.

The existing `prepare EVENT_ID STATE` command remains for explicit owner dispositions. It prints JSON by default; `--write` creates an immutable receipt. For `integrated`, supply `--ruling-path`, `--ruling-commit`, `--confirmation-path`, and `--confirmation-commit`; references must resolve under PROME/proposals at published commits, and the ruling path ends in `-RULED.md`. The helper does not decide whether wording semantically matches: PROME must verify exact answer, conditions and matching chat confirmation, publish the ruling first, then write/commit integration. No automatic ruling or confirmation waiver was added.

## Data and rollback

- Original supervised-pilot events: `AGENTS/CATO/decisions/responses/` (unchanged).
- Daily queue replies: `AGENTS/CATO/decisions/queue-responses/`, dialect `decisions-queue-response/1`; exact published queue row and displayed terms retained.
- Owner receipts: `PROME/decisions/receipts/<event_id>/` (unchanged contract).
- Delivery pointer: `PROME/inbox/decisions-<event_id>-from-CATO.md`; processing may move it to `processed/`.
- Local stores: `local-state/queue-<WQ>.sqlite3`, ignored `local-state/exports/` backups and the original `wq558.sqlite3`. Never-sent legacy exports in `decisions/queue-responses/` are now ignored without deleting or publishing them. Only explicit Send force-adds its selected pair inside its temporary checkout.

To disable responses, open with `--preview` or have PROME revoke its acceptance record. Do not delete or move response/receipt history. Restore an earlier application revision only together with its compatible acceptance; never rewrite saved events. Legacy `pilot_launch.py` retains its original acceptance pin and correctly refuses this changed core. Use `app.py` for the new desk.


## Review freeze and retained limits

`release-review.json` pins the installed WQ-579 build and records Will's subsequent review waiver. The frozen-package history below describes the handoff before that waiver. The handoff names the exact candidate commit and portable bundle. The WQ-570 recheck held its four prior repairs but found X-1/X-2, so 1296e8bcb remains uninstalled. Will authorized the WQ-579 repair, one further focused recheck owned by PROME, and installation with matching acceptance if it passes. Will chose to retain chat confirmation for every answer (WQ-571 A). Author tests do not grant acceptance.

The fingerprint retains answer/receipt code, source parsing, rendering, Git publication, hook installation, hooks, account guard and draft-ignore rules. The date and orphan advisory implementations are repinned under WQ-570 because they execute with publication access. Their commands still run on each new Send with the existing contract: weekday exits 0/1 are complete (1 reports advice), other exits fail; orphan must finish successfully and returns its output. No root-required safeguard was removed. A changed critical dependency still disables replies pending reacceptance.

W-F/W-G, the W-A stranded-commit consequence, W-B shared staging on hook refusal, and W5 whole-scan failure on unpublished events are repaired in this candidate under author tests. Shared-HEAD rollback is never used. Legacy unpublished reply commits already on shared master are refused for explicit owner reconciliation; this candidate does not erase earlier mistakes. Publication still has a final check-to-push interval: a local change after the final check can occur after the send boundary. PROME must check latest delivered answer/current question and obtain matching chat confirmation before ruling. A remote advance refuses without leaving a candidate on shared master.

Remaining named limits: manual fork/disconnected-history reconciliation (W1); advisory orphan rather than enforcement (W3); symbolic receipt-reference preparation (W4); unpublished HEAD receipt display and missing semantic/time checks in legacy integration (W6); some integrity errors can block the desk (W7); same-day ruling filename order (W8); other committed owner work can ride a push (W9); permissive option fence (W12); reused integrated WQ hidden in History (W-C); some misleading refusal text (W-D); action-menu/verdict-title mismatch (W-E). Published responses with unavailable private predecessors stay readable with an explicit gap notice; disconnected chains are never guessed. Actual desktop/laptop restore and ordinary-use productivity remain unobserved.

The temporary publication checkout materializes only the selected pair, hook/push scripts and repository marker; it retains the complete Git tree. A busy shared tree may remain behind after successful delivery. Sync applies published records when current owner work permits; it does not take over another desk's edits. Malformed artifacts quarantined by intake remain visible for owner reconciliation; the tool cannot infer their missing contents or ownership. Ordinary performance and repeated use remain observations, not author-test claims.

## Verification

```sh
# From this directory; all writes use temporary fixture repositories/stores.
python3 -B -m unittest test_mvp test_pilot_files test_pilot_launch test_desk test_desk_review test_revision_delivery test_batch test_focused test_import_isolation -q
# From repository root; Windows Chrome and local HTTP required.
python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_desk_browser.py
python3 -B scripts/agents_gui.py --smoke-test
```

The daily desk tests use a local bare Git remote and preserve an unrelated staged file through delivery/retry. Native browser fixtures exercise real forms at desktop/narrow widths; actual-history mode only reads the real completed pilot. `desk-validation.json` records author evidence. No fixture answer is published to the real repository.

The original fictional rehearsal and copy comparison remain available under their existing commands and files. Their dated evidence and the original pilot acceptance are preserved in the [continuing report](../../../runs/2026-10-30_1059_wq-decision-workflow.md). They are not the current release status.

## WQ-570 focused repair

One new commit must change exactly the selected response and packet paths; verify parent, commit count, paths and bytes before push and after fetch. Private publication rejects unknown executable hooks and changed pinned helpers before enabling hooks. Timeouts without fetched publication evidence are unknown, including a delayed push that subsequently lands. A busy checkout is preserved and reports exact ahead/behind state and recovery instructions. It may still require owner recovery before later desk pushes.

An incomplete earlier publication cannot satisfy the literal two-changed-path contract. Its Send button is disabled: save a replacement version, then explicitly Send its new pair. The original answer remains readable. No old reply export is staged or erased by installation. PROME must reconcile pending delivered answers and staged/committed legacy exports first (W-L/W-P). Other W-H through W-Q findings remain explicitly recorded in release-review.json; this is not a broad second review.

Author evidence: 123 Python checks passed in the full run; its single loopback-socket test was sandbox-blocked and passed on an isolated rerun (124 distinct checks total). Eight are targeted counterexamples. Native Chrome: 38 assertions, including replacement after partial publication. No real reply was sent.

## WQ-579 import isolation repair

X-1: the private publication checkout materializes exact pinned transport paths rather than the whole scripts directory. It disables hooks before checkout, rejects replacement refs/tags and unexpected materialized scripts, and verifies real Git objects with replacement objects disabled. Python helpers use isolated imports; subprocess environments also exclude Python search-path overrides and protect stdin Python in inherited hooks. Safe-push receives a transient Git configuration override `push.followTags=false`, inherited by its Git children; the fleet safe-push script itself is unchanged. Existing remote tags are preserved.

After fetch, the shared repository verifies the single child commit, exactly two paths and exact bytes. One captured remote-reference inventory per observation requires only master to move to that commit; extra branches, tags or commits cannot receive an exact-success receipt. Concurrent legitimate remote changes can also produce a reconciliation message after the pair was delivered. This is a bounded observation, not a transaction against later remote writers or a sandbox against arbitrary same-user code.

X-2: the weekday advisory runs with `python3 -I`. The publication base and shared HEAD/index tree are captured before advisories; HEAD/index movement refuses without resetting owner work. The shared pre-commit hook isolates both remaining Python calls. Its dormant row-cap block is removed under the existing WQ-578 approval, in this candidate only; install the hook and matching acceptance together.

W-R: the success receipt names pre-existing committed work carried by the push. W-S survives: superseded half-published answers can still be reported as needing clarification. All previous named limits remain; PROME must reconcile W-L/W-P before installing. Eleven new versioned regression cases include real production helpers, positive controls proving planted imports execute without isolation, origin-only shadow files, Python environment injection, shared-state races, replacement-object deception, tag-following, extra remote publications and shared post-fetch verification. Fixtures never publish real answers. See release-review.json for current test results and Will’s subsequent explicit waiver of the further recheck.
