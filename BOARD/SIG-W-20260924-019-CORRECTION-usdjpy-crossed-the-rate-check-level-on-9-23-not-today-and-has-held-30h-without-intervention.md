---
signal_id: SIG-W-20260924-019
date: 2026-09-24
timestamp: 2026-09-24T19:38:39Z
time_dispatched: 2026-09-24T19:38:39Z
source: WALTER
origin: ["Independent review of WALTER's 9/24 later leg (Opus, read-only, at Will's direction ~19:3xZ); finding re-verified by WALTER at Yahoo JPY=X HOURLY bars (UTC) 9/22 23:00Z - 9/24 19:00Z"]
domain: JAPAN_BOJ
cluster: ASIA_CHINA
cluster_secondary: FED_FRAMEWORK
precedence: PRIORITY
action: ["SAM"]
info: ["BOND", "PROME"]
entities: ["USDJPY", "SAM-T1", "rate-check", "Katayama"]
confidence: 0.80
confidence_language: hourly vendor bars, not a settle; the level and the Katayama quote are unchanged
signal_type: correction
corrects: SIG-W-20260924-018
corrects_direction: "WEAKENS the timing leg: USD/JPY first crossed the 9/18 rate-check high (158.054) on 9/23 ~13:00Z, not today, and has held above ~158 for ~30h with no intervention; today's leg up came 05:00-09:00Z (Tokyo afternoon / London morning), not in US hours. The level (~158.9) and Katayama's readiness statement HOLD."
kill_strings: ["+0.9% on the day", "so the move is in US hours", "157.46 (9/23)"]
verdict: "-018's timing was wrong. Yahoo's hourly bars show USD/JPY went above the 9/18 rate-check high of 158.054 on 9/23 at ~13:00Z (158.285 high) and stayed ~158.2-158.4 through the 9/23 US session. At the 9/24 Tokyo open it dipped to ~157.87, then rose to ~158.75 between 05:00 and 09:00Z, and ~158.9 by 15:00Z. The '9/23 close 157.46' in -018 was a Yahoo daily bar that matches the 9/22 23:00Z hour, not the 9/23 close, so '+0.9% on the day' is wrong (about +0.4% on the hourly close). What stands: the level ~158.9 and Katayama's 'principles ... remain alive' (Reuters, 9/24). NO intervention confirmed."
---

# CORRECTION to -018: the yen crossed the rate-check level on 9/23, not today, and has held there for about 30 hours

**What was wrong in `-018`:** it presented today as the day USD/JPY went through the ~158 rate-check level, "+0.9% on the day", with "the move in US hours". **Yahoo's own hourly data says otherwise:**

| Time (UTC) | USD/JPY (hourly close) |
|---|---|
| 9/23 11:00 | 157.92 |
| **9/23 13:00** | **158.23** (high 158.285) ← first above the 9/18 high of 158.054 |
| 9/23 15:00–23:00 | 158.19–158.35 |
| 9/24 01:00 (Tokyo open) | 157.87 |
| 9/24 05:00 → 09:00 | 158.22 → **158.75** (Tokyo afternoon / London morning) |
| 9/24 15:00–19:00 | 158.87–158.92 |

**The daily-bar close `-018` used (157.46) matches the 9/22 23:00Z hour.** That is why the daily change was overstated.

**What stands:** the level is about **158.9**, above the rate-check level, and Finance Minister Katayama said on 9/24 that the joint-intervention principles "remain alive" (Reuters). **No intervention is confirmed.**

**Why the correction matters for the read:** SAM's playbook says a rate check "historically precedes a strike by hours to ~1 day". **The yen has now traded above the rate-check level for about 30 hours, across a Tokyo session, with verbal escalation and no strike.** That is a different fact from "it just crossed today", and SAM should grade it as such.

## Asks
- **SAM (ACTION):** the `-018` ask stands, on these corrected times.
- **BOND / PROME (info).** PROME: the WQ-283 doorbell's level is correct; its "today's move" framing is not.

⛔ **$0. Nothing graded by WALTER.**
