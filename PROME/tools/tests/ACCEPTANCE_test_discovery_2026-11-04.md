# ACCEPTANCE CONDITIONS — PROME test-discovery integrity, 2026-11-04

**Written before edits.** Scope: test code only. No production spawning behavior, operational contract, dependency or checker changes.

1. **Fail-closed checks execute under both entry points.** `test_spawn_list_fail_closed.py` no longer exits during import. Its original 15 assertions run unchanged in substance under standalone unittest and aggregate discovery; any failed assertion fails the suite. A zero-check import is not accepted.
2. **Fixture state is restored.** `test_spawn_list_desk_commit_attribution_L455.py` restores the original `spawn_list.ROOT` even if fixture setup or a test fails. The subsequent open-export test reads the live repository root, not the deleted temporary fixture. Production `spawn_list.py` remains unchanged.
3. **File handles close.** `test_docket_open_query_L368.py` reads DOCKET through a context manager or another explicit close; `-W error::ResourceWarning` stays enabled.
4. **Substantive coverage survives.** The individual fail-closed, attribution, open-export and DOCKET-query suites pass. Aggregate discovery has zero unexpected failures/errors and reports the expected L910 size failure separately until that obligation is resolved.
5. **No test side effects on the live tree.** Existing fixture isolation remains; the Git status after the run contains no new test-created repository files.

## Neighbours considered

- **Ordinary:** standalone and discovery entry points both execute the checks.
- **Overlap:** the attribution fixture followed by open export is the required order-sensitive case; failure during fixture setup still restores ROOT.
- **Wrong owner:** no production file or other desk's file changes.
- **Missing information:** a failed assertion or unreadable fixture must fail loudly, never produce a zero-check pass.
- **Concurrent activity:** no shared live-state writes; temporary repositories and context-managed files only.

## Completion note

**IMPLEMENTED · TESTED.** Standalone suites pass: 15 fail-closed assertions in one subtest-covered unittest case · 22 attribution tests · 14 open-export tests · 9 DOCKET-query tests. The attribution fixture's missing ROOT restoration caused the export failure; production `spawn_list.py` is unchanged. Aggregate discovery: **1,144 tests, OK; 4 skipped; 1 expected failure** (the registered L910 CLOSEOUT-size obligation). No unexpected failure, import error or ResourceWarning remains. No independent reader was used; these self-contained test-only repairs required no production or shared-contract change.
