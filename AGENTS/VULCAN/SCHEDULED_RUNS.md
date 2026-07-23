# VULCAN — SCHEDULED AUTONOMOUS RUNS (cloud routines)

*Cloud routines auto-grade the 7/29-31 earnings cluster. Each is a one-time run (fires once, auto-disables). Model: Opus 4.8. Tools incl. WebSearch/WebFetch + EDGAR. They commit to AGENTS/VULCAN/ and push via safe-push. Set up 2026-07-22 (Will-directed). Manage: https://claude.ai/code/routines*

| Run | Fires (UTC / ET) | Routine ID | Grades |
|---|---|---|---|
| 1 | 2026-07-30 15:00Z / 11am ET | `trig_01RDqC6giUfRYrpGP9KSNWJq` | MSFT+META (7/29 AMC): VULCAN-09 partial (fall-on-raise?), VULCAN-10 (MSFT FY27 color), VULCAN-07 partial (MSFT 10-K + META 10-Q useful-life), capture FY26 guides |
| 2 | 2026-07-31 15:00Z / 11am ET | `trig_01QvrXDdLoUwWzTWFAzJmvQE` | AMZN (7/30 AMC) + FINALIZE VULCAN-01 (agg vs $710-725B), VULCAN-06 (S3 power), VULCAN-09 (3-name reaction); VULCAN-07 if AMZN 10-Q filed |
| 3 | 2026-08-03 15:00Z / 11am ET | `trig_01BL6okavCSvaWgvH5XMJSHX` | BACKSTOP — AMZN 10-Q useful-life catch → VULCAN-07 final. No-ops if VULCAN-07 already resolved |

**If you (VULCAN) boot manually during 7/30-8/3:** check whether the day's routine already ran (PREDICTIONS.tsv statuses + recent commits) before re-grading — avoid duplicate work. The routines push to origin, so their results arrive via git pull.
**Caveat:** cloud runs are effectively a second machine — if Will is also running the box, safe-push fails-safe (aborts non-ff); the routines are instructed to pull --rebase + retry. Low conflict risk (VULCAN-only files).
