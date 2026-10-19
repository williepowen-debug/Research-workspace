# Primary research and verification

Read October 19, 2026. These sources use different definitions; their numbers are not pooled with the local study.

- [Bespoke, July 23, 2026](https://bespokeinvest.substack.com/p/extreme-price-and-breadth-divergences): twelve prior sessions since 1990 with at least six sectors rising despite negative constituent breadth. Subsequent S&P returns positive in 75% after one month and 83.3% after three; average gains 1.26% and 4.49%. July 3, 2001 was a bad exception. Small sample, overlapping horizons and different sector-level condition; underlying event table not recovered. This is counterevidence to a deterministic single-day bearish interpretation, not a forecast for today.
- [Fang, Qin and Jacobsen, 2014, university-hosted manuscript](https://www.pure.ed.ac.uk/ws/files/16837254/Jacobsen_SSRN_id2449344.pdf): 93 technical indicators including A/D measures, long daily/weekly/monthly samples. Some statistical relationships; economic robustness weakened with risk/cost controls. Not a matched study of index-up/breadth-down sessions. Verified by read-only helper; owner did not independently replicate this paper.
- [Schwab, June 26, 2025](https://www.schwab.com/learn/story/breadth-check-strength-and-weakness-trend-tracker): explains the vulnerability when narrow leaders reverse, including 2023. Illustrative history, not a systematic hit rate.
- [FRED HY notes](https://fred.stlouisfed.org/series/BAMLH0A0HYM2): April 2026 change restricts displayed history to three years. Recovered CSV starts October 20, 2023. October 16 value published October 19. Same-date historical OAS observations cannot be assumed tradable at the equity close.

No verified primary study of the exact index-rising/participation-falling/HY-widening conjunction was found in this bounded search. This is an access/search result, not proof no such study exists.

## Read-only helper receipts

Thread `/root/verify_history`: source review and independent re-derivation of every saved 21/63/126-session outcome; zero return/drawdown mismatches. Confirmed within-arm spacing; cross-arm overlap, proxy mismatch, deterministic selection and credit truncation remain. Found PLAN's “at least20bp” versus initial code's strict `>20`; owner corrected to `>=20`, re-ran analysis and validation. Original and corrected 20bp sensitivity event dates/results unchanged. Helper's posthoc phase check found smaller narrow-sample average returns across all126 starts; owner reproduced it in validate.py. No files changed by helper, no owner grades, explicit no-work-remaining closeout received.

Thread `/root/verify_credit_link`: primary issuer methodology, SEC extraction feasibility, three June30 telecom filings and funding-perimeter verification. No complete market-wide maturity dataset found in the searched repo paths. Explicit no-files/no-work-remaining closeout received. Telecom details are in TELECOM-PILOT.md. These helpers are not domain-owner sessions or evidence of fleet liveness.
