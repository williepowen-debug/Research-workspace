---
signal_id: "SIG-W-20261119-002"
date: "2026-11-19"
timestamp: "2026-11-19T14:22:41Z"
dispatched: "2026-11-19T14:22:41Z"
source: "Federal Reserve Bank of Philadelphia, Manufacturing Business Outlook Survey November 2026, released Thu 2026-11-19 08:30 ET, https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/mbos/2026/bos1126.pdf"
origin: ["Scheduled release read at the issuer (ISHM docket/CATALYSTS.tsv row 2026-11-19 [PHILLY])"]
action: ["ISHM"]
info: ["HENRY", "CARL", "LABOR", "RED", "VULCAN"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.95
confidence_language: "issuer release read; prior values from the release's own table"
resources: 1
safety_net: "clear"
cluster: "INFLATION_TRANSMISSION"
domain: "INDUSTRIAL_CYCLE"
entities: ["Federal Reserve Bank of Philadelphia", "Manufacturing Business Outlook Survey", "prices received", "new orders", "capital expenditures"]
word_count: 371
dispatch_note: "ROUTING_TABLE INDUSTRIAL_CYCLE row: ISHM ACTION (its catalyst row, band OWED), regional surveys at PRIORITY; INFO HENRY (backup), CARL (prices legs), LABOR (employment index), RED; VULCAN as channel owner for the future capital expenditures leg (core capex vs AI capex, ISHM job J1). CARL and RED INFO by BOARD diff. TERRY BOARD-only."
event_window: "closed"
---
# Philadelphia Fed manufacturing survey, November (released Thu Nov 19 08:30 ET): general activity 6.3 from 20.9 (six-month low, still positive); new orders -0.4 from 4.3 (first negative since May, fourth straight decline); prices paid 58.2 from 43.2 and prices received 47.0 from 40.1 (highest since June 2022); future capital expenditures 18.9 from 34.9 (lowest since February); ISHM reads the regional sign

# Philadelphia Fed Manufacturing Business Outlook Survey, November 2026

**Source read:** the Philadelphia Fed release PDF, https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/mbos/2026/bos1126.pdf (Release Date: November 19, 2026; responses collected Nov 9 to 16; all data seasonally adjusted), fetched 2026-11-19 14:22Z (file time), sha256 d51be6bd74b3641e. Prior values are the release table's 'Previous Diffusion Index' column.

| Current index (SA diffusion) | November | October | Change |
|---|---|---|---|
| General activity | **6.3** | 20.9 | -14.6 (lowest since May) |
| New orders | **-0.4** | 4.3 | -4.7 (lowest since May; fourth straight decline) |
| Shipments | 25.7 | 15.3 | +10.4 |
| Unfilled orders | -4.4 | 2.4 | -6.8 |
| Delivery times | 3.5 | 8.5 | -5.0 |
| Inventories | 5.3 | -12.8 | +18.1 |
| **Prices paid** | **58.2** | 43.2 | +15.0 (highest since April) |
| **Prices received** | **47.0** | 40.1 | +6.9 (highest since June 2022) |
| Employment | 11.6 | 9.1 | +2.5 |
| Average workweek | 11.2 | 7.5 | +3.7 |

**Six months ahead:** general activity 33.6 (little changed); new orders 31.7 (down 5) and shipments 25.4 (down 10), each the lowest in more than a year; employment 24.9 (lowest since February); prices paid 63.3, prices received 62.9; **capital expenditures 18.9, down 16, third straight decline, lowest since February.**

**Special questions (quarterly):** over 42% of firms say customers became more price sensitive since last quarter; 56% expect near-term changes in their industry's costs (44% last quarter) and 79% of those expect competitors to raise prices in response, median within three months (four last quarter).

**For ISHM:** catalyst row 2026-11-19 [PHILLY], regional composite sign, band OWED. October's SA new orders panel on ISHM's STATUS read NY 23.2, Philadelphia 4.3, Richmond -8, KC 3, Dallas 9.3; Philadelphia's November reading is now negative. ISHM's NEXUS brief lists Empire November at 7.8. Kansas City Fed's survey is due later today and WALTER will card it when it lands. **The price legs** (prices received at its highest since June 2022, and the cost-pass-through special questions) bear on the inflation reads of CARL and HENRY; WALTER grades nothing. Next release Dec 17; the Q4 Price and Inflation Expectations Survey is Wed Nov 25.
