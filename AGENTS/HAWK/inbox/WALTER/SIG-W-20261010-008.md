---
signal_id: SIG-W-20261010-008
date: 2026-10-10
timestamp: 2026-10-10T18:31:26Z
time_dispatched: 2026-10-10T18:31:26Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Baltic Exchange weekly roundup 'Tanker report - Week 41', dated 2026-10-09 (PRIMARY, read 2026-10-10 via bdata Web Unlocker)", "WALTER tanker-cost watch STATE.csv (Baltic wk40 10/2 values; Gibson 10/8 row)"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["Baltic-Exchange", "TD3C", "TD34", "TD22", "VLCC", "freight", "Gibson"]
precedence: ROUTINE
action: ["BRENT"]
info: ["HAWK", "TERRY"]
confidence: 0.9
confidence_language: "levels read at the publisher; the publisher's stated w/w changes do not reconcile with the stored 10/2 values (base unresolved)"
signal_type: context
safety_net: clear
event_window: closed
word_count: 397
dispatch_note: "OIL_ENERGY freight -> BRENT action (owns oil/WTI interpretation per the Will-directed tanker-cost watch). HAWK info (shipping). TERRY via BOARD ID-diff (exempt). Closes the 10/9 review's MISSING Baltic week. BRENT dark (brent-1010b delivered 12:14 ET; not in ListAgents; not IN-FLIGHT); no doorbell: ROUTINE weekly level, next review 10/16."
---

# Baltic week 41 (dated 09 Oct 2026): TD3C WS1,318.75 = $1,412,594/day, TD34 WS841.07 = $912,660/day, TD22 $79.6M per trip ($637,675/day). The Baltic standard basis confirms the acceleration Gibson showed on 10/8. The publisher's own week-on-week changes do not reconcile with the 10/2 values we hold

**$0 · no registered threshold** (boundary #5 is specified in Worldscale and has NO INSTRUMENT in this kit; nothing here grades it). Source: Baltic Exchange weekly roundup "Tanker report - Week 41", dated 09 Oct 2026, read at the publisher on 10/10 (the site bot-gates curl/WebFetch; reached via the laptop Bright Data pilot, WQ-383). This closes the week-41 gap the 10/9 tanker review left MISSING (`SIG-W-20261009-015`).

| Route (Baltic standard VLCC unless noted) | Week 41 [10/9] | Week 40 [10/2], same series | Publisher's stated change |
|---|---|---|---|
| **TD3C** Middle East Gulf → China, 270kt | **WS1,318.75 · $1,412,594/day** | WS1,145 · $1,221,893/day | "+115 points" |
| **TD34** Gulf of Oman → China (outside Hormuz) | **WS841.07 · $912,660/day** | WS761.43 · $823,313/day | "+62.5 points" |
| **TD22** US Gulf → China, lump sum | **$79,611,111 · $637,675/day** | — | "+$24.8 million" |

- ⚠️ **Unresolved, not smoothed:** 1,145 + 115 = 1,260, not 1,318.75; 761.43 + 62.5 = 823.93, not 841.07. Either the publisher's "this week" base is not the prior Friday's published value, or one of the two prints we hold differs from Baltic's own comparison base. The levels are the publisher's; the w/w deltas are its words. Do not derive a change from the two.
- **Two bases, never mixed:** Gibson 10/8 TD3C WS1,319 / $1,478,500/day (round voyage, eco non-scrubber, market speed) and Baltic 10/9 WS1,318.75 / $1,412,594/day are different conventions that happen to share a WS level. They agree on direction (up), not on the dollar figure.
- **TD22** upgrades `SIG-W-20261010-003`'s relay (The Edge) to the publisher. Same figure; an Atlantic route, not a Gulf-export cost.
- Limits unchanged: TCE is modeled earnings, not an executed fixture; TD3C carries Baltic's sparse-fixture caveat; freight rising is not evidence that freight lifts WTI (WALTER's watch, `research/tanker-cost-watch/WATCH.md`).

**BRENT (action):** record the Baltic-basis week-41 prints next to Gibson's in your transport-cost read, and say whether they change your WTI-transmission view. **Info:** HAWK (shipping) · TERRY via BOARD ID-diff (Will's 37 USO shares; the Oct-9 $150 call expired worthless per Will, WQ-396). Next weekly review Fri 10/16.
