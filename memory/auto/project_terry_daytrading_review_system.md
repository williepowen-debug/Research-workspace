---
name: project_terry_daytrading_review_system
description: TERRY runs a standing day-trading review loop (AGENTS/TERRY/daytrading/) — Will wants trades tracked regularly to understand mistakes
metadata: 
  node_type: memory
  type: project
  originSessionId: 9531205e-3824-4c50-b34c-454b84c5c0ba
---

Will runs a discretionary **day-trading experiment** (0DTE QQQ scalping + short-dated single-name option bets), **separate from the thesis put-book** in FORGE. As of 2026-06-23 he wants TERRY to review it **"somewhat regularly"** to track trades and understand his mistakes.

System lives at `AGENTS/TERRY/daytrading/`: `PROFILE.md` (living rulebook + 5 enforceable rules + named tendencies), `JOURNAL.md` (append-only narrative, newest on top), `LEDGER.tsv` (per-review metrics for trend-tracking), `README.md` (the loop + intake).

**Why:** the value is the longitudinal loop — are the named leaks shrinking review-over-review — not any single writeup.

**How to apply:**
- When Will pastes a trade log and asks for a day-trading review: reconstruct realized P&L by instrument thread (cash-flow method: Σsells−Σbuys per passed-expiry bucket), mark open positions vs live closes, score against the 5 rules, append to JOURNAL + LEDGER, and **flag repeat mistakes** (same leak two reviews running).
- **Push for a broker history/positions CSV export, not just the activity feed** — the feed hides assignment outcomes and roll strikes, which forced Session 1's P&L into a +$719→+$3,336 *range* instead of a number. See [[finding_option_marks_need_live_chain]] and [[feedback_position_cost_basis_not_authoritative]].
- Session-1 fingerprint: edge = react-and-exit + single-name down-reads on flush days; leaks = overnight holds lose, naked short premium booked as "income," 0DTE churn, buying calls/premium after the move. Edge is **unproven** (5 sessions, one a crash) — leaks are reliable.
