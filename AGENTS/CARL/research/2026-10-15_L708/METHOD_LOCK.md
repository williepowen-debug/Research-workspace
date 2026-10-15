# L708 — CARL leg: method lock (written BEFORE any issuer price or rating was read)

**Written:** 2026-10-14 23:49 ET (`date`), CARL (Claude Code, Opus 5.5, PROME-spawned Tier 1). Rule source, read first and graded on unchanged: `AGENTS/NEXUS/research/2026-10-14_commission_CCC-gap_consumer-attribution.md` (committed adb9e7458, 21:25 ET).

The NEXUS spec fixes hypotheses, sessions, measure and the verdict ladder. It leaves four implementation choices open. CARL fixes them here, before reading any issuer data, so the answer cannot be fitted to them.

| # | Open choice | CARL's fixed choice | Why |
|---|---|---|---|
| 1 | Return series | yfinance auto-adjusted daily Close via the repo `.venv` (dividend/split adjusted = total return proxy), same as VULCAN 10/9 | Spec names VULCAN's method |
| 2 | beta and sigma | OLS of issuer daily return on SPY daily return with intercept, fit window 2026-03-02 to 2026-09-23 inclusive; beta = OLS slope; sigma = sample standard deviation of (r - beta*SPY) over the fit window; z = (r - beta*SPY)/sigma | Spec: "beta and sigma fitted out of sample on 2026-03-02 to 09-23"; the intercept is not subtracted in z because the spec's z has no alpha term |
| 3 | The 10/13 bond session spans the 10/12 bond holiday (equities traded 10/12) | GOVERNING: interval-matched two-day return 10/9 close to 10/13 close, with beta*SPY over the same interval and sigma*sqrt(2). REPORTED BESIDE IT: the one-day 10/13 return. If the two disagree on a session's classification, the session count is shown both ways and the governing one decides | The OAS cell for 10/13 changes from the 10/9 cell; matching the interval is the faithful pairing |
| 4 | "Widening direction" for an equity | z <= -1.0 (equity falls beyond noise). "Within noise" = abs(z) <= 0.3 | Spec section 3 rules 2-3 |
| 5 | Per-issuer count | An issuer "moves" if z <= -1.0 on at least 4 of the 7 primary sessions (10/2, 10/5, 10/6, 10/7, 10/8, 10/9, 10/13); "sits within noise" if abs(z) <= 0.3 on at least 4 of 7 | "at least half of 7" rounds up to 4 |
| 6 | Universe | Consumer-facing, non-lending US issuers with USD HY bonds, rated single-B or CCC by S&P or Moody's (split B/BB counts only if one agency has it at B); rating source + date verified by a sourced search 10/14-15, never from memory. Private issuers are named but have no reachable daily data | Spec section 3 "Issuers" + CARL's row of section 4 |
| 7 | Reachable daily data | an issuer counts toward n only if yfinance returns a complete bar set (no missing sessions) for the fit window and all 12 sessions | Spec rule 1 needs n of reachable issuers |

Secondary window 9/25, 9/28, 9/29, 9/30, 10/1 (5 sessions) *[date typo corrected 2026-10-15 00:01 ET (transcript tool stamp 04:01:34Z), before any z was computed: the lock as committed (commit 2bb208ad9, blob 24b3cf1e6) said 9/26, a Saturday; the spec's 5 sessions 9/25→10/1 are the five FRED cells listed here, verified at BAMLH0A3HYC/BAMLH0A2HYB; no method choice changed. Recovery note 2026-10-15 08:06 ET (`date`): the sha first typed here, 21fef828, names no object in this repository; corrected to the commit that carries the lock]* is reported with the same arithmetic; the primary governs (spec).

Verdict ladder (copied, not paraphrased, from spec section 3): fewer than 2 named issuers with reachable daily data => NO_INSTRUMENT; at least half the named issuers move beyond abs(z) >= 1.0 in the widening direction on at least half the primary sessions => SUPPORTED; at least half the named issuers sit within abs(z) <= 0.3 on at least half the primary sessions => NOT SUPPORTED; otherwise => MIXED. First match governs.
