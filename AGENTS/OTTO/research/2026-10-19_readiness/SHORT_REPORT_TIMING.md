# Short-report release timing: bounded historical check, October 19 (s032)

## Finding

**The verified examples do not establish a dependable earnings-day or T-7 release pattern.** Three Carvana publications appeared48,21 and0 calendar days before the next actual earnings release. The same-day observation is a follow-up to theJanuary report, not an independent new campaign. A Credit Acceptance comparison appeared18 days before earnings. These are observed dates, not a probability estimate forOctober28 and not instructions to hold a position through earnings.

## Scope fixed for this check

Reconstruct the named Carvana Hindenburg/Gotham publications relevant to OTTO's existing allegation watch, January2025 throughOctober19,2026; retain initial reports and substantive follow-ups as separate observations but identify their campaign dependence. Compare publication date to the next actual issuer earnings date. Add the directly recovered CACC/BleeckerJanuary2023 example as an explicitly older comparator for another tracked lender. This is a bounded, retrospectively assembled sample, **not a census of activists, posts, tracked names or earnings quarters**. It cannot estimate an arrival hazard or establish that reports outside these sources do not exist. Unverified social posts/recycled headlines do not count as new publications.

| Name / publisher | Publication date [publisher] | Next actual earnings [issuer] | Calendar days before | Independence / date evidence |
|---|---|---|---:|---|
| CVNA / Hindenburg initial | Jan2,2025 | Feb19,2025 | 48 | Publisher displays Jan2 and Jan3; HTML `time.entry-date.published` datetime resolves originalJan2; Jan3 is the `updated` time. Earnings notice was only publishedJan22, **after** report: alignment is retrospective, not evidence the report targeted an announced day |
| CVNA / Gotham initial | Jan28,2026 | Feb18,2026 | 21 | Publisher structured `datePublished`2026-01-28T16:21:03.457Z; Jan29 update excluded as a new report. Earnings announcedJan21 |
| CVNA / Gotham follow-up | Feb18,2026 | Feb18,2026 | 0 | Publisher metadata2026-02-18T13:56:09.190Z,08:56ET, before after-close earnings. Same publisher/campaign as preceding row |
| CACC / Bleecker initial | Jan13,2023 | Jan31,2023 | 18 | Publisher structured date2023-01-13T08:30:00-0500; issuer-origin GlobeNewswire releaseJan31,16:01ET. Older example, not pooled into a representative2025–26 sample |

Saved source keys: `hindenburg_jan02`, `gotham_jan28`, `gotham_feb18`, `cacc_bleecker`, `cvna_2025_earnings_actual`, `cvna_2026_earnings_actual`, `cvna_2025_earnings_notice`, `cvna_2026_earnings_notice`. CACC issuer release was read through the web tool; direct requests returned403. Its URL and a short date receipt are in`web_receipts.json`; no full local original claimed. Metadata/offset calculations and normalized rows: `timing.tsv`, produced by`derive.py`.

## What the sample allows

- One of the three CVNA publications was on earnings day. Two were more than three weeks away or exactly three weeks away. Those counts are descriptive only: selecting known reports leaves the denominator of opportunities unmeasured; repeated campaigns are dependent.
- Current Gotham main index was readOctober19 and showed theFebruary follow-up alongside newer non-CVNA research; no later CVNA publication was recovered in this scoped publisher/search pass. That is SEARCH-NOT-FOUND, not a universal absence claim. Historical metadata records publication dates; it is not an independent archive proving exact first public availability.
- The existing **October21 T-7 watch remains useful for detecting a report already published**, and the existingOctober28 earnings-day check remains useful because a same-day follow-up has occurred. Neither check is a forecast that a report will appear; today's work does not discharge those future checks.
- A new report is an allegation to verify against issuer and primary evidence. Route a qualifying new activist mention through WALTER under the existing rule, retaining publisher/date/initial-versus-follow-up. No new alerts fired in this historical check. No corporate fraud conviction, probability, holding period or trade rule changes.

No claim is made about report-day or subsequent stock returns. Historical timing and investment outcome are different questions; TERRY constructs any trade and Will approves it.
