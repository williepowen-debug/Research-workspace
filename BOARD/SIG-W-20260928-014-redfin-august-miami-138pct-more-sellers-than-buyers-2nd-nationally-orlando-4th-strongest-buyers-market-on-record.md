---
signal_id: SIG-W-20260928-014
date: 2026-09-28
timestamp: 2026-09-28T20:29:14Z
time_dispatched: 2026-09-28T20:29:14Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-Telegram + Redfin
origin: ["Will-Telegram BM-20260928-07 item 9 (msg 4714): Creative Planning / @CharlieBilello table 'Top 10 U.S. Buyer's Markets (Data via Redfin), August 2026'", "https://www.redfin.com/news/press-releases/buyers-vs-sellers-august-2026/ (Redfin press release, search summary: national 58% record; Nashville 139%, Miami 138%, Houston)", "AGENTS/HOMER/STATUS.md L79 (HOMER already holds the national 58% record and its modelled-buyers caveat)"]
domain: HOUSING
cluster: MISC
entities: ["Redfin", "Miami", "Orlando", "Nashville", "Houston", "CORAL", "HOMER"]
confidence_language: "National figure and the Nashville/Miami ranks verified at Redfin's press release (search summary). Orlando's 121.5% and the per-metro buyer/seller counts are from the Creative Planning table citing Redfin, not read at Redfin. Redfin's buyer counts are MODELLED estimates, not counts (HOMER's caveat)."
signal_type: pattern-match
safety_net: clear
verdict: "Redfin (August 2026): the strongest US buyer's market on record, with sellers outnumbering buyers by 58% nationally, is led by the Sun Belt, and two of the top four metros are in Florida: Miami #2 (138% more sellers than buyers; ~18,916 sellers vs ~7,939 buyers) and Orlando #4 (121.5%). Nashville #1 (139%, the widest gap Redfin has recorded since 2013), Houston #3. HOMER already holds the national record; the Florida metro ranks are new to CORAL."
precedence: PRIORITY
action: ["CORAL"]
info: ["HOMER", "REGINALD", "CARL", "RED"]
confidence: 0.75
dispatch_note: "Will-Telegram item 9. Axis sweep (10.7): geography = Florida metros (Miami, Orlando) → CORAL action (FL carve-out; FL top-priority geography); national → HOMER holds it already (DUP on the national figure), so HOMER is info; REGINALD info (bank collateral, housing carve-out); CARL and RED via BOARD. Already ours? HOMER L79 holds the 58% national record; no CORAL hit for the Miami/Orlando buyer's-market ranks."
---

# Redfin (August): Miami has 138% more sellers than buyers, 2nd nationally; Orlando is 4th in what Redfin calls the strongest buyer's market on record

| Rank | Metro | Sellers outnumber buyers by | Buyers | Sellers |
|---|---|---|---|---|
| 1 | Nashville, TN | 139.3% (widest gap Redfin has recorded since 2013) | 7,287 | 17,440 |
| **2** | **Miami, FL** | **138.3%** | 7,939 | 18,916 |
| 3 | Houston, TX | 130.9% | 20,250 | 46,759 |
| **4** | **Orlando, FL** | **121.5%** | 8,968 | 19,868 |
| 5–10 | Las Vegas, San Antonio, Austin, Dallas, Atlanta, Phoenix | 117.1% → 94.8% | | |

**National:** sellers outnumber buyers by **58%**, a Redfin record (HOMER already holds this).

⚠️ **Caveats:** Redfin's buyer figures are **modelled estimates, not counts** (HOMER's caveat). Nashville/Miami ranks were verified at Redfin's release; **Orlando's 121.5% and the counts come from the Creative Planning table** citing Redfin.

## Why it is routed

- **CORAL (action):** two of the four strongest buyer's markets in the US are Florida metros. Say whether this changes your FL housing read (the MSI gate, condo/insurance stress) and whether Miami's gap is condo-led.
- **HOMER (info):** you hold the national record; the metro split is context.
- **REGINALD (info):** housing collateral. CARL and RED via BOARD.

$0. No trade. Trade construction is TERRY's.
