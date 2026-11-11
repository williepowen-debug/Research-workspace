# WQ-639 — prepared release, not installed

**Status:** independent review completed with **BLOCK (IR-639-1)**: replacement patches lack an enforced queue precondition. [Unedited review and closure condition](independent-review/report.md). Candidate remains uninstalled; bounded correction and focused independent recheck precede activation. Will directed CATO to work without burdening PROME on November 11. No live application, queue, options source, acceptance, hook, response or receipt was changed, and no desk was launched/notified. The installed chat-required fallback remains live.

## Result

- One `author_card.py` command accepts WQ ID and explicit choices/recommendation/context/conditions, then creates the option source, queue-pointer patch and binding/preimage manifest in a new artifact directory. It changes no owner files or Git state. PROME applies/publishes the two source files at its normal owner touch. Existing sources require explicit replacement; a stale patch refuses.
- New options `/3` / display `/3` binds decision terms while tolerating operational Notes changes. Question, type, dates, recommendation, hold state, source pointer, choices, policy, locked context and conditions remain binding. Old sources and historical answers remain strict; no response migration or retroactive authority.
- The actual old WQ-558 pilot already had an integrated receipt and no clarification demand. Browser inspection found disabled approval controls still showing; the candidate removes recommendation controls from recorded answers while retaining history. No owner receipt or answer was rewritten.

Full contract and command example: [OWNER_GUIDE.md](OWNER_GUIDE.md). The command intentionally prepares a patch rather than mutating PROME's active queue or publishing on its behalf. Source-authoring completeness remains owner judgment: material restrictions must be in the question, choices, context or conditions, not solely operational Notes.

## Frozen contents and reproduction

`manifest.json` identifies base `9cc3bfd7bf` (full SHA inside), all nine candidate source/test/doc paths, exact hashes and live-acceptance preimage. `candidate.patch` is the full change; `build-hashes.json` is the complete candidate runtime map, not a delta. Do not copy it into live acceptance before review. The isolated author tree is `/tmp/cato-wq639-20261111`; the durable patch reconstructs it independently.

From a separate checkout at the manifest base: apply `candidate.patch`, then run in `AGENTS/CATO/prototypes/decisions/mvp`:

```sh
python3 -m unittest -q test_batch test_briefs test_desk test_desk_review test_focused test_import_isolation test_intake_shape_review test_mvp test_pilot_files test_pilot_launch test_revision_delivery test_wq638 test_wq639 test_wq641
python3 test_wq639_browser.py
```

The browser test requires Windows/WSL and Chrome, uses disposable fixture repos, and reads the real pilot through a responses-disabled preview with disposable state. It never creates a real response. Normal `unittest discover` also imports an older top-level browser runner; use the explicit module list above to keep those lanes separate.

## Evidence and limitations

- 239 Python tests passed (`python-tests.txt`), including 10 new WQ-639 tests and preserved real producer row/source from the published November 6 WQ-639 response. Tests cover actual fake-repo delivery/restore after unpublished, locally committed and published Notes changes; meaningful changes/refusals; wrong version; stale patches; input validation; explicit migration; historical replay.
- 18 native Chrome checks passed (`browser-results.json`): desktop/narrow exact options and visible conditions, recommendation eligibility, chat confirmation, no fabricated answer, layout; actual integrated pilot retains its history and has no response/resend controls. Fixture screenshots are included; inspected desktop layout.
- Initial blanket suite run had two execution errors: sandbox loopback denial and a browser module's import-time Windows access. Explicit authorized rerun passed. Native browser's two-second Windows probe disconnected during slower real-history reads, producing `BrokenPipeError` in the log; all final DOM checks completed and passed. No live production transport failure is inferred from those test-probe disconnects.
- A small post-run test-only edit suppresses the expected duplicate-output-directory CLI error from stderr; runtime code and tested assertions are unchanged. Owner-guide prose was completed after the checks. Manifest covers final bytes.
- No independent acceptance, installed improvement, live wake or ordinary-use benefit claimed. Changed HTML hash will require fresh review of any still-unsent older response; preserve original words/history. Runtime `/1` and `/2` replay stays unchanged.

## One bounded independent read, then activation

Required by the existing [runtime owner contract](../../mvp/WQ638.md): “Install requires ... one independent read without blockers, exact candidate hashes, published review and acceptance”. The general accepted-release contract also makes changed build hashes read-only. No new gate is introduced here and no review was requested from busy PROME.

Reader should apply this patch to the pinned base and devise its own counterexample: Notes hiding a hold or material restriction, same-ID question/options change, pointer swap, source/queue publication skew, source-replacement collision, legacy answer replay and stale publication. Review the semantic contract that Notes are operational only for opt-in /3 cards, and verify that no invented authority or overwritten owner work follows. One targeted read, not a renewed general app audit.

After a nonblocking verdict, installation/acceptance must preserve `app_only_enabled: false`, matching chat confirmation, exact hashes and published review reference. Do not install notification hooks. Review/install/source-publication remains one bounded owner-coordinated release step; no real decision is fabricated as a test. Live notification proof and any later removal of chat confirmation remain separate with PROME.
