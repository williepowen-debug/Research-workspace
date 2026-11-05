# November 2 December-contract settlement, fallback read
BRENT, 2026-11-04 21:02 EST. Asked by SIG-W-20261104-077 and PROME 2026-11-04 21:00 ET. BRENT grades nothing; TERRY owns GATE-TERRY-VLO-HELD-01.

**Answer: no CME page was read. cmegroup.com blocks this box and was not approached. Every reachable public fallback gives HOZ26 $4.4216/gal and CLZ26 $96.46/bbl for November 2, crack $89.2472/bbl, $0.9128 below $90.16.**

| Source, observation read | Stated | Implied or stated Nov 2 value |
|---|---|---|
| DTN, Nov 3 08:38 CST (quote 09:04 EST): ULSD Dec +$0.0390 to $4.4606 | change on prior settle | HOZ26 4.4216 |
| DTN, same: WTI Dec −$1.38 to $95.08 | change on prior settle | CLZ26 96.46 |
| DTN, Nov 3 14:59 CST: ULSD Dec +$0.1090, +2.47%, settle $4.5306 | change on prior settle | HOZ26 4.4216; 0.1090/4.4216 = 2.465% |
| DTN, same: WTI Dec −$0.37, −0.38%, settle $96.09 | change on prior settle | CLZ26 96.46; 0.37/96.46 = 0.384% |
| Investing.com heating oil table, header NYFZ6, row Nov 02 2026 | close 4.4216, volume 51.28K | HOZ26 4.4216; volume ties to the vendor HOZ26 row 51,284 |
| Vendor daily rows, re-pulled 2026-11-05 02:00Z | close | HOZ26 4.4216 (WALTER, TERRY), CLZ26 96.46 |

**Controls.** PASS: DTN Nov 2 09:12 EST change base gives HOZ26 4.6761 and CLZ26 104.12 for October 30, equal to the CME PRELIMINARY pair. PASS: Investing.com October 23 row 4.7870 equals CME FINAL.
**Failed control, kept visible:** DTN's October 23 15:00 CDT article says WTI December "settle at $103.51"; CME FINAL was $103.27 ($0.24 apart). DTN's same-day settle wording is not reliable. The method above uses the prior-settle base of the NEXT day's quotes, a different quantity, and it is the part that matches.

**Limits.** These are derived from secondary publishers, not an exchange read. They probably share the exchange's feed, so agreement is one lineage, not independent confirmation (LESSONS #1). Preliminary versus final is not distinguished; the Nov 3 09:04 EST base was published the morning after settlement. To reach $90.16, HOZ26 would need to be $4.4433 (2.2 cents higher; corrected from a hand-typed $4.4467 in commit 0910d70ac2) or CLZ26 $95.55 ($0.91 lower).
Failed fallbacks: Barchart HOZ26 and CLZ26 (HTTP 202, empty); TradingCharts (404); Stooq (JavaScript challenge, not defeated).
Sources: https://www.dtnpf.com/agriculture/web/ag/news/world-policy/article/2026/11/03/oil-dips-volatile-trade-amid-us · https://www.dtnpf.com/agriculture/web/ag/news/world-policy/article/2026/11/03/oil-us-election-jitters-offsets-gulf · https://www.dtnpf.com/agriculture/web/ag/news/world-policy/article/2026/11/02/oil-sinks-6-hormuz-diplomacy-gathers · https://www.dtnpf.com/agriculture/web/ag/news/world-policy/article/2026/10/23/oil-hits-multi-month-highs-middle · https://www.investing.com/commodities/heating-oil-historical-data
