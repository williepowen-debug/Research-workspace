# nudge_fixture — permanent regression fixture for scripts/ledger_staleness.py --nudge (output shape v2, 2026-08-20).
Git history is the test data: ledgers committed first, STATUS.md committed twice after, so every ledger sits 2 STATUS-writes behind. Do not "fix" the staleness; it is the fixture. Invisible to --all (nested below AGENTS/*/).
