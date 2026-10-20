# October 20 monitor repairs — acceptance before editing

Authorized by Will: “yes lets fix this now”, following `reports/2026-10-20_owed-work-and-gaps.md`.

1. Auction comparisons use the published two-decimal bars, strict on every leg. Exact equality never fires; just below/above behave correctly. Preserve raw benchmark values as audit evidence. A grade-time recomputation cannot silently substitute for the snapshot in force: accept an explicit identity-checked frozen-bars JSON; without it label results AUDIT ONLY. No economic threshold, historical grade, routing scope or thesis state changes.
2. Commit offline command-path regression tests for L410 A1–A6, including corrupt latest reopening versus stale original, valid pending reopening, loader reconciliation and repeated loads. Obtain an independent reader of the final code; preserve the October 1 partial review as history, append the new evidence.
3. Buyback rendered packet states the original-issue-date rank's dated 1/53 base rate (2024-06-05 through 2026-09-24), preserving the >50% cut and all verdict calculations.
4. Remove live-looking HYG-skew request/trigger text from CDX monitor and tool. State the August 23 retirement and duration confound; do not build a new feed or claim true CDX coverage.

Verification: repository venv; durable offline tests, existing grader/buyback selftests, independent adversarial read, heavy closeout. System Python lacks required research packages; use root `.venv/bin/python`. Other desks' dirty files remain untouched; pull deferred.

## Final results

| State | Result | Evidence |
|---|---|---|
| IMPLEMENTED | Complete | Published 2dp STRICT comparison on all legs; explicit frozen JSON target/provenance/date/n validation; rolling audit separated; corrupt latest identities retained for refusal. F2 output vintage corrected; retired HYG leg removed from live trigger/request text. |
| TESTED | PASS | `monitors/test_monitor_repairs.py`:18/18, with many boundary/malformed-input subcases; `2026-10-20_monitor-repairs_tests.txt`. Grader existing38/38 (`2026-10-20_grader-selftest.txt`); buyback existing0fail (`2026-10-20_buyback-selftest.txt`). |
| INDEPENDENTLY VERIFIED | PASS within stated scope | `2026-10-20_monitor-repairs_REVIEW.md`; final grader SHA25685f1681006bfdb6189b81f3a3df86e1476b1a1c49453c0dfffbf9375be878261. Five reviewer-found failure classes repaired and independently rechecked. |
| UNRESOLVED | Historical/data limits only | October1 A2 byte-identical output not reconstructed; approved October20 output/rounding changes intentionally differ. No full-series20Y tool exists; any future one must use invalid-row guard. True CDX/authenticated feed, ratio duration confound, event-time TIPS, HY access census and governance deferrals remain open. |

The current valid-row nominal methodology is preserved; invalid/missing/nonfinite inputs now fail closed. No research threshold, historical verdict, thesis state, routing scope or capital decision changed. Old generic grader invocations now print AUDIT ONLY; a registered post-print grade requires `--frozen-bars`.

Production examples from any cwd, resolving relative paths at Git root:

```
/home/willi/Research-workspace/.venv/bin/python /home/willi/Research-workspace/AGENTS/BOND/monitors/grade_auction.py --cusip 912810UX4 --frozen-bars AGENTS/BOND/registry/auction_bars/2026-10-21_912810UX4.json
/home/willi/Research-workspace/.venv/bin/python /home/willi/Research-workspace/AGENTS/BOND/monitors/grade_auction.py --cusip 91282CRR4 --frozen-bars AGENTS/BOND/registry/auction_bars/2026-10-22_91282CRR4.json
```

These inputs transcribe existing October15 freezes, not new thresholds or outcomes. Month-end nominal snapshots still need freezing at announcement. No automatic snapshot selection or historical regrading was added.

Closeout: heavy tier; full runner and freeze transcript at `../registry/closeout_runs/2026-10-20.transcript.md`. Other desks' dirty files untouched; no pull. No new Will decision. Internal closure packet to PROME saved under root carve-out①; delivery/consumption not inferred from file creation.
