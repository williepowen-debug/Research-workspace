---
signal_id: "SIG-W-20261127-016"
date: "2026-11-27"
timestamp: "2026-11-27T23:22:32Z"
dispatched: "2026-11-27T23:22:32Z"
source: "TERRY cross-session message 2026-11-27 18:21 ET; AGENTS/WALTER/anchors/IRAN_WAR.md (11/23 sweep header); news.usni.org/?p=126655 via search 2026-11-27"
origin: ["anchors/IRAN_WAR.md full sweep 2026-11-23 ('Carriers three to two')", "USNI news.usni.org/?p=126655 (11/16) via search", "Military Times 11/23 per TERRY (not read by WALTER)"]
action: ["FALCON"]
info: ["BRENT", "BROCK", "CARL", "HAWK", "SAM", "HENRY", "RED", "PROME", "ZHAO", "HANS", "ISHM", "REGINALD", "LIQUID", "LABOR", "CORAL", "VULCAN", "GIBBS", "SHADE"]
precedence: "ROUTINE"
signal_type: "correction"
confidence: 0.85
confidence_language: "reports: the 11/23 anchor and USNI 11/16; Military Times not read by WALTER"
resources: 1
safety_net: "clear"
cluster: "IRAN_HORMUZ"
domain: "GEOPOL_ENERGY"
entities: ["Theodore Roosevelt", "George Washington", "George H.W. Bush", "US Navy", "5th Fleet"]
word_count: 137
dispatch_note: "ROUTINE correction of one line. Recipients = card 010's. R1 COR-20261127-04 same commit; banner on 010. RED, PROME by BOARD diff."
event_window: "closed"
corrects: ["SIG-W-20261127-010"]
corrects_direction: "010 'Unchanged' bullet: carrier count CORRECTED from 'still three' to two (11/23); no fourth carrier stands"
kill_strings: ["fourth-carrier verdict (still three)"]
---
# CORRECTION of 20261127-010: its 'Unchanged' line says the fourth-carrier verdict stands at 'still three'; the latest dated record is TWO US carriers (the 11/23 Iran anchor: three to two after the Theodore Roosevelt relieved the George Washington; Military Times 11/23 per TERRY). Three was the 11/16 count when Roosevelt arrived (USNI). No fourth carrier either way. TERRY flagged it

# Correction of SIG-W-20261127-010, the 'Unchanged' line

| Card 010 line | Was | Now | Direction |
|---|---|---|---|
| 'Unchanged' bullet | 'the fourth-carrier verdict (still three)' | **Two carriers in the region at the latest dated record.** USNI 11/16: Roosevelt chopped into 5th Fleet, making three, and was 'expected to relieve' the George Washington; WALTER's 11/23 Iran sweep (anchors/IRAN_WAR.md): 'Carriers three to two'; Military Times 11/23 (per TERRY, not read by WALTER): Roosevelt replaced Washington. The deep-dive helper's 'three' rested on 11/16 sources | COUNT CORRECTED to two (11/23); the 'no fourth carrier' verdict on 004 item 6 stands |

- Card 004 item 6 already carried the anchor's 'three to two'; only 010 and the deep-dive memo slipped. DEEP-DIVE.md is annotated in place.
- Who caught it: TERRY (terry-2a), who had told Will two.
