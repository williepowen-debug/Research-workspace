# L748 rebase over L736 — October20

PROME’s packet requested a rebuild after the writer changed. Original patch applied without conflicts in an isolated clone of25a79bddf; regenerated diff targets the current e84f5601 writer. No live code or ledger writes. pre_L736_rebase/ preserves exact old patch/manifest. New target_hashes.json is the sole apply manifest; all three paths still apply together.

13 timestamp tests,36 writer selftests,27 closeout tests,7 L736 view tests pass (83 total). Four historical corrections reproduced against a temporary ledger copy; original bytes preserved, four summaries appended, original obligations UNKNOWN, no additional spawn. The original production_check uses physical lines; independent review compared exact keys against prior production evidence; all four match.

The7 view tests require PYTHONPATH=<isolated-root>/scripts because their importlib test loader does not insert the sibling module directory. The first bare unittest run errored importing orch_time; rerun with the explicit path passed. This is a test invocation dependency, not a change to runtime source. Owner commands from Git root:

```
python3 AGENTS/DAEDALUS/builds/l748_time_2026-10-20/test_orch_time.py "$PWD"
python3 scripts/orch_log.py --selftest
PYTHONPATH="$PWD/scripts" python3 -m unittest discover -s scripts/tests -p test_orch_log_view_L736.py
python3 -m unittest discover -s PROME/tools/tests -p test_orch_closeout.py
python3 AGENTS/DAEDALUS/builds/l748_time_2026-10-20/production_check.py "$PWD"
```

PROME still applies on exact before hashes and owns all four live invalidation rows. Known historical times stay UNKNOWN; no guessed timestamps. Existing provenance limits and full-suite debt unchanged. Prior time-review acceptance remains historical; new independent integration review is recorded separately in REBASE_REVIEW.md.

REVIEW: required — combined guard/record-classification behavior; l748_rebase_review; ACCEPT bounded rebase. Independent hand-row interaction test confirms refusal without mutation, explicit acknowledgment retains UNKNOWN invalidation; no runtime edits after review. Reviewer closed assignment with no pending work. No grade or maintenance clock changes. General DAEDALUS session remains closed; this is the bounded owner-requested follow-up.

Closeout rc0:7 CLEAN,2 DUE,1 NOT-APPLICABLE,1 DECLARED; maintenance debt retained. Final five-packet inbox census recorded; no further work started. Publication follows exact-path commit, native owner acknowledgment unavailable.
