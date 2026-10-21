# L628 summons re-verification — 2026-10-20 Codex

Pinned base `f36cd5d0bcb35f6ca42a6d1abe13d2a6465a1d9d`; isolated clone `/tmp/daedalus-l628-bxzb9pgo/repo`. Live source bytes matched base at verification. Existing patch unchanged, applied only to clone. `.venv/bin/python3` from source environment; no dependency installation or live PROME edits.

| Check | Before | After |
|---|---|---|
| Full discover | 956 tests;8 failures;2 errors;3 skipped | 972 tests;8 failures;2 errors;3 skipped |
| L548 targeted | not installed | 16/16 pass, ResourceWarning as error |
| Patch apply check | rc0 | applied rc0 |

Failure/error IDs identical; no new failing ID. Full output preserved in `2026-10-20_codex_before.txt`, `_after.txt`, `_targeted.txt`. Some suite tests print nested test summaries; reported counts above are the final outer unittest summaries. This is no whole-suite clean claim. Historical L737 is not presumed to explain every failure; exact current failures follow.

- ERROR: test_the_order_is_commit_then_verify_then_push_then_publish (test_review_mechanism_WQ240b.Repro5_GenerationBeforeFreeze.test_the_order_is_commit_then_verify_then_push_then_publish)
- ERROR: test_spawn_list_fail_closed (unittest.loader._FailedTest.test_spawn_list_fail_closed)
- FAIL: test_clean_desk_is_clear_to_brief (test_agent_freshness_L294_F4.PreSpawnStopFailsClosed.test_clean_desk_is_clear_to_brief)
- FAIL: test_no_check_errored (test_gate_isolation_L294_F7.CleanFixturePasses.test_no_check_errored)
- FAIL: test_rc_is_0 (test_gate_isolation_L294_F7.CleanFixturePasses.test_rc_is_0)
- FAIL: test_verdict_says_pass (test_gate_isolation_L294_F7.CleanFixturePasses.test_verdict_says_pass)
- FAIL: test_no_bare_check_call_sites_remain (test_gate_isolation_L294_F7.NoFabricatedDefaults.test_no_bare_check_call_sites_remain)
- FAIL: test_q1_one_snapshot_so_a_row_appended_between_reads_reaches_neither_output (test_helm_size_split.HelmSnapshotTests.test_q1_one_snapshot_so_a_row_appended_between_reads_reaches_neither_output)
- FAIL: test_LIMIT_hand_row_absorbed_by_a_later_writer_append (test_orch_log_wiring_L733.ObservedCheck.test_LIMIT_hand_row_absorbed_by_a_later_writer_append)
- FAIL: test_the_runner_matches_the_manual_order (test_review_mechanism_WQ240b.Repro5_GenerationBeforeFreeze.test_the_runner_matches_the_manual_order)

Hashes: `target_hashes.json` → `reverified_2026-10-20_codex`. PROME must compare live before hash immediately before apply, run targeted tests and arrange its named CATO post-apply read. Prior independent patch/rebase reviews remain as recorded; no new code or fresh independent result-review claimed here.
