---
signal_id: "SIG-W-20261127-007"
date: "2026-11-27"
timestamp: "2026-11-27T22:12:56Z"
dispatched: "2026-11-27T22:12:56Z"
source: "census.gov/econ/indicators/2026/advance_report2610.pdf; dallasfed.org/research/pce; stlouisfed.org economic-conditions-survey-results (page, no figures) and Kobeissi chart; time.com 2026-11-27; insee.fr IR263; bls.gov laus.nr0; FRED SOFR, IORB 2026-11-27T21:58:41Z; search summaries for item 7"
origin: ["census.gov advance_report2610.pdf (read by helper)", "dallasfed.org/research/pce (read by helper)", "X bookmarks @DeItaone, @PeterSchiff, @FirstSquawk, @KobeissiLetter (image opened), @spectatorindex, @unusual_whales, @Polymarket", "TIME 2026-11-27 (fetched by helper)", "INSEE IR263 (read by helper)"]
action: ["CARL", "ISHM", "REGINALD"]
info: ["HENRY", "LIQUID", "LABOR", "HANS", "CORAL", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "indicator"
confidence: 0.8
confidence_language: "confirmed: items 1, 2 at the issuer; 3 a chart of the issuer's survey; 5 and 7 corrected framing"
resources: 1
safety_net: "clear"
cluster: "INFLATION_TRANSMISSION"
domain: "TARIFF_TRADE"
entities: ["Census Bureau", "goods trade deficit", "wholesale inventories", "Dallas Fed", "trimmed mean PCE", "St. Louis Fed", "Economic Conditions Survey", "BEA", "Q3 GDP", "INSEE", "France", "SOFR", "IORB", "muni VRDO"]
word_count: 512
dispatch_note: "PRIORITY rather than the data-day IMMEDIATE default: a late catch-up of a release with no registered trigger, read at the issuer; owners next read Mon 11/30. ACTION CARL (trade, inflation), ISHM (inventories, imports), REGINALD (8th District lending). RED, PROME by BOARD diff."
event_window: "open"
---

> ⚠️ **PARTIALLY CORRECTED by SIG-W-20261127-010:** the 'front-running' so-what is withdrawn: capital goods were +$13.4B of the +$21.1B import jump (+80% y/y), and the Section 301 proposals came 11/25, after October.
# US data catch-up (missed by the 11/27 day calendar pass): Census October advance goods deficit $149.5B, widest since March 2025 per relay (Sept $135.1B; exports $215.8B, imports $365.3B, SA; released Fri 11/27 08:30 ET; wholesale inventories +0.9%, retail +0.8%); Dallas Fed trimmed mean PCE October 2.8% 1-month annualized, 2.4% 6-month and 12-month (11/25); St. Louis Fed 8th District bankers (11/17 edition): loan demand net -30% vs +11%, delinquency net +28%; France Q3 is -0.1% (flash), not -0.2% recession

# US and other data from Will's bookmarks (calendar catch-up)

| # | Item | Read | Verdict | Owner |
|---|---|---|---|---|
| 1 | **Census Advance Economic Indicators, October 2026 (CB26-195), Fri 11/27 08:30 ET:** goods deficit **$149.5B**, +$14.4B from $135.1B; exports $215.8B (+$6.7B), imports $365.3B (+$21.1B); SA, not price-adjusted. Wholesale inventories $1,023.4B, +0.9% m/m (+8.5% y/y); retail $893.2B, +0.8% (+5.1% y/y); Sept revised retail to +0.7%, wholesale to +0.8%. Next 12/28. Relay (Schiff): largest October deficit on record, third-largest month after Jan and Mar 2025 | issuer PDF read (helper) | CONFIRMED | CARL (TARIFF_TRADE), ISHM |
| 2 | **Dallas Fed trimmed mean PCE, October:** 1-month annualized 2.8%, 6-month 2.4%, 12-month 2.4%; updated 11/25 (with BEA's October PCE), next 12/23 | dallasfed.org read (helper); the 'prior 3.0%' not verified | CONFIRMED | CARL |
| 3 | **St. Louis Fed Economic Conditions Survey (8th District), banking, 11/17 edition** (Kobeissi chart, opened): net % higher minus lower, current quarter: loan demand **-30%** (previous quarter +11%, expected next quarter -7%); delinquency **+28%** (prior +25%); credit standards +13% tighter (prior +6%) | chart attributed to St. Louis Fed; issuer figures sit in an xlsx not read | REPORTED; 11/17 edition, 10 days old | REGINALD, CARL |
| 4 | Trump (Truth Social 11/26, TIME 11/27): calls BEA's Q3 GDP revision to 4.3% annualized from 3.4% a 'massive, and purposeful, error' and 'fake Economic Numbers, just prior to the Election' | TIME page (helper) | CONFIRMED; the post is about the 11/25 second estimate and the Nov 3 midterms already held; no evidence offered | HENRY, CARL |
| 5 | 'France's economy shrinks 0.2% in Q3; plunges into recession' (@spectatorindex, @Polymarket) | INSEE first estimate (10/30): Q3 **-0.1%**, Q2 0.0%; Q1 was -0.2%; the 11/27 detailed estimate not retrieved | **CORRECTED-FRAMING: -0.2% and 'recession' unsupported by the flash**; card 20261127-002 carried France by title | HANS |
| 6 | BLS state unemployment, October (released 11/20): CT 5.1%, CA 5.0%, MI 5.0%; Florida 4.3% from 4.4% | BLS release summary | DUP for Florida (card 20261120-003, LABOR graded); other states not new | LABOR, CORAL |
| 7 | 'Banks to pay $400M in muni bond price-fixing trial' (@FirstSquawk 16:11Z) | search summaries: banks NEAR a settlement of more than $400M in the Philadelphia-led federal class action on variable-rate demand bond remarketing (JPMorgan, Morgan Stanley, Goldman named); no signed settlement found | CORRECTED-FRAMING: reported near-settlement | CARL (muni) |
| 8 | SOFR 5 bp above IORB (@gamesblazer06) | FRED: SOFR 3.95 [11/25], IORB 3.90 | CONFIRMED; REG-T-08 (>15 bp) not met | LIQUID |

- **Calendar:** items 1 and 2 were not in HENRY's ECON_CALENDAR or PROME's DOCKET; WALTER's 11/27 day pass recorded 'US none scheduled'. Logged as a miss in research/2026-11-27_evening-boot/CALENDAR-RECONCILIATION.tsv.
- **So what:** the import surge plus inventory build reads as front-running or restocking ahead of tariff changes (ISHM's real-demand-or-borrowed question); it subtracts from Q4 GDP tracking. The 8th District loan-demand swing is the sharpest in the chart and supports a credit-demand slowdown read, on one regional survey.
