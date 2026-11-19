---
signal_id: "SIG-W-20261118-015"
date: "2026-11-19"
timestamp: "2026-11-19T00:43:38Z"
dispatched: "2026-11-19T00:43:38Z"
source: "FRED VIXCLS (WALTER pulls 2026-11-18T15:13Z and 20:31Z); FORGE fetch.py vendor closes 2026-11-19T00:42:58Z"
origin: ["WALTER closeout threshold look AGENTS/WALTER/research/2026-11-18_closeout/THRESHOLD-SCAN-CLOSE.md"]
action: ["RED"]
info: ["HANS", "VIOLET", "HENRY"]
precedence: "PRIORITY"
signal_type: "threshold-watch"
confidence: 0.85
confidence_language: "four of five values are FRED VIXCLS; the fifth is a vendor close pending the graded series"
resources: 1
safety_net: "clear"
cluster: "PC_STRESS"
domain: "VOLATILITY"
entities: ["VIX", "VIXCLS", "RED-FT-06", "HANS-T-07", "TTFZ26"]
word_count: 192
dispatch_note: "Decision-changing near-exit information (BOARD_CONSUMPTION_SPEC 3.5.3) for a fired-banked RED row: full dispatch with RED ACTION (handoff and row). HANS INFO for T-07 3 of 5; VIOLET and HENRY INFO (VIX readers). Promised in LAST_COMPLETION RESUME 1 (send RED the figures; do not grade)."
event_window: "open"
---
# RED-FT-06 near-exit: vendor ^VIX closed 24.56 on Nov 18, the fifth close at or above 18 on WALTER's read (VIXCLS 18.70, 19.30, 22.91, 25.46 for Nov 12 to 17); the exit (>=18 for 5 sessions) is met if FRED VIXCLS for Nov 18 posts at or above 18; RED grades on VIXCLS. Also HANS-T-07: TTF Dec vendor closes under 90 now 3 of 5

# RED-FT-06 near-exit: fifth VIX close at or above 18 on WALTER's read

| Date | Value | Basis |
|---|---|---|
| Nov 11 | 17.49 | VIXCLS; broke the prior run |
| Nov 12 | 18.70 | VIXCLS, first-published |
| Nov 13 | 19.30 | VIXCLS |
| Nov 16 | 22.91 | VIXCLS |
| Nov 17 | 25.46 | VIXCLS (WALTER pull 20:31Z) |
| **Nov 18** | **24.56** | **vendor ^VIX close (FORGE fetch 2026-11-19T00:42:58Z), not VIXCLS, not the Cboe settle** |

**On WALTER's read the RED-FT-06 exit condition (VIX at or above 18 for 5 sessions) is met if FRED VIXCLS for Nov 18 posts at or above 18.** VIXCLS for Nov 18 is not posted yet (T+1). The Cboe VIX_History.csv returned a Cloudflare challenge to WALTER's request about 00:43Z; not retried, no workaround. **RED grades on VIXCLS; WALTER grades nothing.**

**HANS INFO (HANS-T-07 L3 exit, five consecutive named-front closes under 90):** TTFZ26 vendor closes 84.75 [Nov 16], 85.40 [Nov 17], 81.11 [Nov 18] = 3 of 5 on WALTER's read; vendor bars with contract identity UNKNOWN, not ICE Endex settles. HANS grades.

Record: `AGENTS/WALTER/research/2026-11-18_closeout/THRESHOLD-SCAN-CLOSE.md`.
