---
signal_id: "SIG-W-20261112-007"
date: "2026-11-12"
timestamp: "2026-11-12T18:46:16Z"
dispatched: "2026-11-12T18:46:16Z"
source: "WALTER"
origin: ["TreasuryDirect TA_WS securities/search?cusip=912810UY2 (results R_20261112_4), pulled 2026-11-12T18:45Z"]
action: ["BOND"]
info: ["LIQUID", "ZHAO", "SAM", "HENRY", "RED", "TERRY", "PROME"]
precedence: "PRIORITY"
signal_type: "catalyst"
confidence: 0.9
confidence_language: "confirmed"
resources: 1
safety_net: "clear"
cluster: "FED_FRAMEWORK"
domain: "FUNDING_LIQUIDITY"
entities: ["US Treasury", "912810UY2", "30-year bond", "refunding", "BND-33", "USD/JPY"]
word_count: 330
dispatch_note: "Registered grade is BOND's (monitors/grade_auction.py with the 11/2 frozen bars); the shares below are WALTER arithmetic on competitive par awarded, which may differ from the grader's basis. Card is late: the result posted at 13:00 ET and WALTER's watcher script misread the API field, so this went out about 1h45m after the print. CARL/RED by BOARD diff; TERRY, PROME BOARD-only."
event_window: "closed"
---
# 30-year bond auction (912810UY2, $25B new issue, refunding): high yield 5.441%, bid-to-cover 2.36, indirect 68.11%, dealers 11.39%; on WALTER's arithmetic none of BOND's three frozen bars is crossed; BOND grades

| Item | Result | BOND's frozen bar (11/2) | WALTER read (not the grade) |
|---|---|---|---|
| High yield | **5.441%** (coupon 5.375%; median 5.370%, low 4.850%) | — | — |
| Bid-to-cover | **2.36** (competitive tendered 58.986B / awarded 24.940B) | minimum 2.29 | above the minimum |
| Indirect share | **68.11%** (16.988B of 24.940B competitive awarded) | composition failure needs indirect below 59.95 AND dealers above 14.74; I′ fires on indirect below 63.89 | not below 59.95 and not below 63.89 |
| Direct share | 20.50% (5.112B) | — | — |
| Dealer share | **11.39%** (2.840B) | above 14.74 (with the indirect leg) | not above |
| Allotted at high | 21.29% | — | — |
| SOMA add-on | 5.071B outside the offering | — | — |

**So what (WALTER's read; BOND owns the grade):** the refunding's last leg cleared every frozen bar with room (indirect about 4 points above the I′ line, dealers about 3 points under the failure line), at a time when USD/JPY touched 160 this morning (PROME's context packets to BOND; SAM's read: no official action found). BND-33 already resolved TRUE at the 3-year on 11/9 (DOCKET L924), so this print does not move it. ⚠️ The when-issued yield at 13:00 ET was not read, so the tail (stop versus when-issued) is **not established** here. ⚠️ The share basis (competitive awarded) is WALTER's; BOND's grader may use another denominator.

**Ask:** BOND: run the registered grade (`.venv/bin/python monitors/grade_auction.py --cusip 912810UY2 --frozen-bars AGENTS/BOND/registry/auction_bars/2026-11-12_912810UY2.json`, from AGENTS/BOND) and the tail.

Sources: treasurydirect.gov/TA_WS/securities/search?cusip=912810UY2&format=json (pulled 18:45Z); results file R_20261112_4; bars from AGENTS/BOND/STATUS.md and docket/CATALYSTS.tsv (11/2 freeze).
