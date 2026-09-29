---
name: feedback_prediction_market_data_is_oracles_domain
description: Prediction-market / priced-probability data (Fed path, CPI, geopolitical odds) is ORACLE's domain — read ORACLE's dated figure and message ORACLE; do not re-derive or carry your own copy
metadata:
  type: feedback
symptoms: "priced probability of a Fed hike", "Kalshi/Polymarket odds", "a forecaster consensus quoted as a market price", "my STATE file carries a stale market-implied %", "no desk carries a live number"
---

**Prediction markets belong to ORACLE (roster: DOMAIN ACTIVE, `AGENTS/ORACLE/STATUS.md`).** A desk that needs a priced probability (Fed path, CPI brackets, event odds) should read ORACLE's dated figure and cite it with ORACLE's timestamp and venue, or ask ORACLE via SendMessage. It should not pull Kalshi/Polymarket itself and carry a private copy that goes stale. Caring about and tracking the number is still right; owning the feed is not.

**Why:** Will, 2026-09-29, to LIQUID: *"we do have another agent that handles prediction markets (Oracle). This doesnt mean you should not care or track them, but you can use Oracles data and communicate with her if it helps us."* The same morning LIQUID's STATUS carried "~85% post-CPI [9/14]" as history while ORACLE held a live Oct-hike figure (64.5% PM / 63.0% Kalshi [9/28 13:48Z]), and ORACLE's own table noted "no desk carries a live Oct number". A private stale copy plus the owner's live one is the two-copies defect.

**How to apply:** cite as "ORACLE [venue, timestamp]" in state files, one place only. When a gate or rule of yours keys on a priced probability, ask ORACLE for the reading at grade time, and name the venue. Never substitute one central bank's probability for another's (the T6 BOJ-vs-Fed trap). Related: [[finding_thin_liquidity_prediction_market_discipline]] · [[finding_anchor_prediction_to_surprise_not_priced]] · [[finding_summary_section_merges_what_the_body_separates]].
