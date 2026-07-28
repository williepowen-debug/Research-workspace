---
name: finding_plausible_stale_value_evades_review
description: A stale value that lands inside the believable range survives review indefinitely; an implausible one gets caught the first session
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e5157ce7-a04a-4a1e-9277-0b95f01ec956
  modified: 2026-07-28T07:19:21.382Z
---

Staleness is not caught by the date tag — it is caught by the value *looking wrong*. So the stale numbers that survive are precisely the ones that still look reasonable. **A stale value sitting inside the plausible range is more dangerous than an obviously broken one, because nothing ever prompts the re-pull.**

BOND, 2026-07-28, two in one session. (1) The STATUS dashboard carried `HY OAS 275 [CONF FRED, 7/2]` for **26 days**. The real print had gone 268 → 279; 275 sat between the 263 trough and the truth, so every session it read as current. The row was tagged with its own vintage and the tag was read past every time. (2) The same surface carried "FOMC HOLD ~90% priced (FedWatch 7/16)" while the live figure was ~65% hold / ~34% hike — a **~25pp** error on the week's largest event, surviving because "the Fed holds" is always plausible.

**Why:** review is driven by surprise, and a plausible number generates none. The date tag is inert — it is *data about* the value, not the value, so it doesn't trip the reflex that a weird number does. This is the sibling of [[finding_silent_blank_evades_review]] (a blank outlives a wrong value): here a *plausible* value outlives an *implausible* one, by the same mechanism — neither presents an anomaly to notice.

**How to apply:** don't audit dashboards by scanning for values that look wrong; audit by **age**. Sort load-bearing rows by their source date and re-pull anything past its cadence regardless of whether the number seems fine — "it still looks about right" is the symptom, not the all-clear. Highest risk after a dark period, and worst on **slow-moving series** (credit spreads, policy odds, quarterly stocks) where a stale value stays plausible for weeks. Pair with [[feedback_pull_live_primary_not_dashboard]] and note that [[finding_mtime_is_corrupted_by_git_sync]] means file mtime won't save you — derive vintage from the row's own source tag and treat that tag as a deadline, not a footnote.
