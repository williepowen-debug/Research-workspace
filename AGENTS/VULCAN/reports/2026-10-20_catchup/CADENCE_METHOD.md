# GOOGL cadence-method study — final disposition 2026-10-26T22:59:32-04:00

**Method study complete; the failed filing-date bound is retired, not repaired or re-graded PASS.** Keep live SEC collection and issuer-confirmed earnings dates. GOOGL 10-Q is now an exact calendar-quarter-close advisory with descriptive historical lags and an UNGRADEABLE future filing date. It sets no automatic job or additional collection frequency. Other issuer/form policies remain unchanged, including META's unresolved 10-Q failure.

## Evidence and chronological replay

Primary inputs: Alphabet CIK 1652044 submissions JSON and all older index pages, captured October 26 ET. Full scope 33 original 10-Qs, period ends September 30, 2015 through June 30, 2026. The first three observations train the first replay; each later observation is evaluated using earlier observations only. Accessions and every comparison: [CADENCE_ROLLING.tsv](../2026-10-26_residuals/CADENCE_ROLLING.tsv). Frozen script/results and primary manifests live alongside it.

| Candidate | Eligible chronological tests | Misses: actual filing before watch opens | Disposition |
|---|---:|---:|---|
| Expanding minimum lag, existing rule | 30 | 3 (2017 Q2: 4 days; 2018 Q1: 1 day; 2026 Q2: 1 day) | Reject as an earliest-possible filing bound |
| Same-calendar-quarter minimum; at least 3 prior same-quarter observations | 24 | 3 (2018 Q3, 2023 Q3, 2026 Q2: 1 day each) | Seasonality does not solve the record-low problem |
| Exact calendar-quarter-close advisory | 30 | No late opening in this replay; lead 23–34 days | Use as a broad advisory, not predictive accuracy or a new sweep schedule |
| Actual earnings 8-K detection | 30 paired events | Observed by the 10-Q in all 30 cases | Detection evidence only; not a historical announced-schedule backtest |

The newest recent-feed hold-out remains **23 days versus a prior minimum of 24**, using 9 prior filings. Expanding the history does not remove that failure. No offset or tolerance was fitted to make July pass. Comparisons are retrospective research; the choice made after seeing them has no prospective validation claim. Same-quarter minima and quarter-close coverage do not establish a probabilistic filing interval.

An issuer announcement takes precedence for the **earnings event only**. Alphabet's [October 6 primary announcement](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Date-of-Third-Quarter-2026-Financial-Results-Conference-Call-2026-8tpGZsLS6v/default.aspx) specifies October 28 at 4:30 p.m. ET, with the release beforehand. It does not promise a 10-Q filing date. A current announcement cannot retrospectively establish what a historical observer knew; no historical announcement-override hit rate is claimed.

## Operational result

`edgar_watch.py` and boot leg 8 share the GOOGL-specific descriptive policy. The historical FAIL remains printed. The advisory validates March/June/September quarter ends and December fiscal year ends, skips an impossible Q4 10-Q, and reports STALE rather than rolling through an unfiled quarter. Missing or incompatible calendar evidence is UNGRADEABLE. Filing collection, all nine issuers, tiering, suppressed counts and append-only handling are preserved. A passing latest diagnostic cannot silently re-arm the retired bound.

Offline verification: 28 tool guard checks and 7 boot-wiring tests passed, including new early-filing visibility, calendar mismatch, stale-series, annual-gap and no-premature-opening cases. Live GOOGL dry-run returned rc1, retaining the 23-versus-24 FAIL, thin annual-model warning and open quarter-close advisory. No ledger rows were appended. `GOOGL_LIVE_VALIDATION.txt` records this run. Boot for the full desk can still return rc2 because META's separate model failure remains unresolved.

## Prior partial record (superseded, preserved verbatim)

# GOOGL cadence failure — repair decision remains open
October20 live sweep collected all nine issuers but returned rc2 because the held-out GOOGL10-Q arrived23days after period end, before the prior-history minimum24days. Do not widen to23solely to pass; no model repair claimed.

Immediate operating path: live SEC collection and issuer-confirmed event dates continue. GOOGL10-Q predicted window remains UNGRADEABLE; METAOctober21 overrides the model's October27–30. A model estimate is not proof no release can occur earlier.

Bounded next work byOctober23: compare a fixed calendar-quarter/issuer-announced override against the historical-lag estimator using rolling, chronological held-outs; preserve the observed failure. Do not select an offset on this one miss. If coverage cannot be validated, retain descriptive lag history and retire only its promise of an earliest possible filing; collection must still run. Current code remains fail-loud. This document is an unresolved method plan, not a certified new predictor or threshold.
