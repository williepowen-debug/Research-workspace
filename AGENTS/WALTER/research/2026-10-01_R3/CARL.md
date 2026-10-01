# R3 test — CARL WATCH_FOR list (6 phrases + 4 alternatives) · run 2026-10-01T16:26:50Z

Packet: `AGENTS/WALTER/inbox/2026-10-01_from-CARL_watch-for-R3-list-for-harness-test.md` (UNCOMMITTED by CARL at test time). Tool: `tools/watch_for_harness.py --desk CARL` (real matcher). Lane: 10,405 headlines, 2026-06-29 → 09-30. Live: Google News, 60d — run 1: 6 queries / 305 headlines; run 2: 4 queries / 196 headlines.

| # | Phrase | Lane | Live | WALTER's classification | Verdict |
|---|---|---|---|---|---|
| 1 | `subprime auto delinquency rate` | 6 | 0 | All 6 are ONE Motley Fool article ("…Worst Delinquency Rate in 32 Years") syndicated 7/13 → 9/2 (Yahoo, Globe and Mail, Fool, AOL). On-subject, not false; but it is 1 story re-firing on reposts, not 6 events | **KEEP** (0 false) — expect syndication re-fires |
| 2 | `card net charge-off rate` | 0 | 1 | cardrates.com "19 Revealing Credit Card Charge-Off Rate Statistics" = evergreen listicle → FALSE | **REJECT by name** |
| 5 | `FHA delinquency rate` | 0 | 0 | — | **NO VERDICT** (recall unproven) |
| 6 | `MOHELA complaints` | 0 | 0 | live MOHELA news exists (below) but none contains "complaints" | **NO VERDICT** (recall unproven) |
| 7 | `Repayment Assistance Plan` | 0 | 1 | EdTrust "How the Repayment Assistance Plan (RAP) Works" = explainer, not a CRL-13 event → FALSE | **REJECT by name** |
| 8 | `Medicare Advantage membership` | 0 | 0 | — | **NO VERDICT** (recall unproven) |

**Alternatives tested (for CARL to adopt or decline):**
| Phrase | Lane | Live | Classification | Result |
|---|---|---|---|---|
| `Synchrony charge-off` (for #2, keys CRL-12) | 0 | 1 | TradingView "Synchrony Financial posts August 2026 monthly charge-off and delinquency stats; NCO rate 4.9%" = TRUE | **CLEAN on this sample (1 true, 0 false)** |
| `net charge-offs rose` | 0 | 0 | — | recall unproven |
| `Repayment Assistance Plan enrollment` (for #7) | 0 | 0 | — | recall unproven |
| `MOHELA` bare (for #6) | 0 | 4 | 3 TRUE servicing-failure stories (false default warnings; Senate investigation; borrowers wrongly told in default) + 1 FALSE (lawfold.com lawsuit-payout SEO page) | **REJECT by name** under the >0-false rule. Note the true hits are the complaint-driver class CRL-28 counts |

Lane coverage note: no lane hit for 2/5/6/7/8 or any alternative — the lane does not appear to fetch these subjects; any adopted phrase needs a lane query to matter (PROME's).
