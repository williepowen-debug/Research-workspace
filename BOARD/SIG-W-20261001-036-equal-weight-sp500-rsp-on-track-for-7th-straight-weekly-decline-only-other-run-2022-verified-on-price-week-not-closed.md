---
signal_id: SIG-W-20261001-036
date: 2026-10-01
timestamp: 2026-10-01T22:06:25Z
time_dispatched: 2026-10-01T22:06:25Z
timestamp_note: stamped from `date -u` at write, not typed
source: Will-Telegram
origin: ["Will via Telegram 2026-10-01 ~22:03Z, BM-20261001-08 item 6: @dailychartbook 5:29 AM 10/1/26 (RSP consecutive weekly declines chart)", "WALTER check: yfinance RSP weekly closes, pulled ~22:2xZ 10/01"]
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
cluster_secondary: CONSUMER_STAGFLATION
entities: ["RSP", "equal-weight-SP500", "RSP-SPY-relative"]
confidence: 0.80
confidence_language: the six completed down weeks are WALTER-verified on price; the 7th week closes Fri 10/2; the 'only other time was 2022' claim is Daily Chartbook's and was not checked
signal_type: context
safety_net: clear
verdict: "Equal-weight S&P 500 (RSP) has closed lower six straight weeks (8/17 through 9/21: $222.77 to $211.11, yfinance price closes) and is at $209.00 in the week of 9/28 as of Thu 10/1, on track for a 7th. Daily Chartbook says the only other 7-week run was in the 2022 bear market. The RSP/SPY relative line is near its all-time low."
precedence: ROUTINE
action: ["HENRY"]
info: ["VIOLET", "RED"]
dispatch_note: "Index-mechanics / breadth -> HENRY per the MARKET_VOL index-mechanics row. The week is not closed; a Friday up-close voids the 7th. RED pull-complete."
---

# Equal-weight S&P 500 (RSP) on track for a 7th straight weekly decline; the only other run was 2022 (per Daily Chartbook)

**Short version:** RSP has closed lower **six weeks running** and sits lower again this week, as of Thursday.

| Week of | RSP close (price) |
|---|---|
| 8/10 | $222.77 |
| 8/17 | $221.67 |
| 8/24 | $220.69 |
| 8/31 | $219.00 |
| 9/07 | $214.87 |
| 9/14 | $212.29 |
| 9/21 | $211.11 |
| **9/28 (open, Thu 10/1)** | **$209.00** |

Daily Chartbook (10/01) says the only other 7-week run since 2004 was in the **2022 bear market**, with RSP/SPY relative performance "hovering near all-time low."

## Caveats
- **The week is not closed.** A Friday close above $211.11 voids the 7th. Friday is NFP.
- **Price closes, not total return.** Dividends could change a marginal week.
- The **"only other time was 2022" claim is Daily Chartbook's**; WALTER did not check the full history.

## Requested action
HENRY: log the breadth run against your index-mechanics lines and grade the 7th week at Friday's close. VIOLET, RED: information only.
