---
signal_id: "SIG-W-20261119-013"
date: "2026-11-19"
timestamp: "2026-11-19T16:51:47Z"
dispatched: "2026-11-19T16:51:47Z"
source: "WebSearch 2026-11-19 before 16:51:38Z (Newsquawk, FX.co, Trading Economics headlines; pages not read); ISHM workbook/PRINTS.tsv KCFED 2026-10 row; kansascityfed.org unreachable (curl exit 28)"
origin: ["ISHM docket/CATALYSTS.tsv row 2026-11-19 [KCFED]"]
action: ["ISHM"]
info: ["HENRY", "CARL", "RED"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.6
confidence_language: "secondary headlines only; issuer page unreachable from this box"
resources: 1
safety_net: "clear"
cluster: "INFLATION_TRANSMISSION"
domain: "INDUSTRIAL_CYCLE"
entities: ["Federal Reserve Bank of Kansas City", "Tenth District Manufacturing Survey", "composite index"]
word_count: 244
dispatch_note: "ISHM ACTION (its catalyst row; it already plans an issuer recheck Nov 20, so ROUTINE). INFO HENRY, CARL, RED per the INDUSTRIAL_CYCLE row. Blocked primary in the headline per the 11/17 practice. CARL and RED INFO by BOARD diff. TERRY BOARD-only."
event_window: "closed"
---
# Kansas City Fed manufacturing, November (released Thu Nov 19 11:00 ET), PRIMARY NOT REACHED: kansascityfed.org times out from this box (curl exit 28, twice; ISHM hit the same this morning); secondary reports say the composite rose to 18 from 11 and the month-over-month manufacturing index to 23 from 16; October's 11 matches ISHM's issuer-verified record; ISHM reads the sign at its Nov 20 recheck

# Kansas City Fed Manufacturing Survey, November 2026 (secondary figures only)

**The primary was not read.** kansascityfed.org did not answer from this laptop (curl timed out at 120 s about 11:02 ET and at 25 s before 16:51:38Z; exit code 28). ISHM recorded the same route limit this morning (STATUS 11:28 ET: 'Kansas City NOT-READ, route-limited, recheck November 20'). **Will: if a desk is to act on these numbers before Nov 20, please open the Kansas City Fed's November release in your browser and paste the headline table.**

**What secondary sources say (search summary, pages not read):**

| Series | November | October | Source |
|---|---|---|---|
| Composite index | 18 | 11 | Newsquawk headline 'US Kansas Fed Composite Index (Nov) 18 (Prev. 11)' |
| Manufacturing index (month over month) | 23 | 16 | Newsquawk headline; FX.co 'climbs to 23 in November' |

Trading Economics headline: 'KC Fed Manufacturing Index at Highest Since April 2022' (which series, not read).

**Date check:** the October composite of 11 matches ISHM's PRINTS.tsv row KCFED 2026-10 (first-published 11, PRIMARY-VERIFIED at the issuer, released 2026-10-22), so these headlines are the 2026 release, not November 2025. WALTER did not see components (new orders, prices).

**For ISHM:** catalyst row 2026-11-19 [KCFED], regional composite sign (band OWED). On secondary figures the sign is positive and accelerating, against Philadelphia's slowdown (card 002, new orders -0.4) and Empire at 3.0 (ISHM STATUS). ISHM grades from the issuer at its recheck.
