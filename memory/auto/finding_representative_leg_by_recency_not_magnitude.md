---
name: finding_representative_leg_by_recency_not_magnitude
description: "A dashboard that summarizes a multi-element series by picking the max-VALUE element silently surfaces stale/settled members and hides the live one; select the representative by recency/status, not magnitude."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8ec4ba19-06f2-4973-928f-04a5d5f28741
  modified: 2026-07-24T16:26:27.365Z
---

When a tool collapses a multi-leg/multi-element series to ONE representative row, selecting by **magnitude** (max value) silently surfaces a stale or already-settled member and hides the live one.

**Concrete case (ORACLE, 2026-07-24):** `polymarket.py pull` picked each daily "on <date>?" event's leg by max probability. Old settled legs sit at 100% YES, so the max-prob pick was ALWAYS a stale settled leg — the two Iran daily war-tempo events read ⛔RESOLVED on the dashboard every session while their current-week legs were live (~50%/day). A live war-widening signal was hidden for several sessions; only a manual `event <slug>` drill-down revealed it, and only because Will asked "have we updated all markets?"

**Why:** magnitude and relevance are orthogonal axes (cf. [[finding_magnitude_ranked_discovery_blind_to_deep_slow]]). For a time-series the relevant representative is the CURRENT element (by date/status), not the biggest.

**How to apply:** when picking one representative from a series, select by **recency/status** (nearest-current unresolved element), not by max value — BUT only for genuine time-series. Distribution/component sets (buckets that all resolve together — CPI/unemployment ladders) genuinely want the MODAL (max-prob) element, and by-date CUMULATIVE ladders want the headline date. Discriminate the series type first (ORACLE: regex on "on <Month> <day>" leg text, ≥3 legs) and only switch the daily on-date case; a blanket change regresses the others. Related: [[feedback_pull_live_primary_not_dashboard]] — the dashboard's own summarization logic can be the thing that's stale.
