---
name: finding_partitioned_source_returns_stale_window_at_200
description: "A versioned/partitioned data source returns HTTP 200 for a stale partition — it looks like a data limit, not a bug, and survives re-attempts"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e5157ce7-a04a-4a1e-9277-0b95f01ec956
  modified: 2026-07-28T08:40:31.535Z
---

Many data APIs partition their history into **versioned segments** — "series breaks", vintages, dataset generations. Query a stale segment and you get **HTTP 200 with real, correct-looking data that simply stops** at that segment's end date. No error, no warning, no empty response. **The failure presents as a property of the source ("their API only goes to 2024") rather than as a bug in your query**, which is why it survives re-attempt after re-attempt.

BOND, 2026-07-28: FR2004 dealer positions had been carried as an "env-blocked data gap" for **six weeks**, with five prints owed, re-attempted on three separate sessions and finally **escalated to the user as an owed data-source problem**. The NY Fed primary-dealer API partitions by series break; the query was pinned to `SBN2022` (ends 2024-07-02), so it returned a clean 200 with data stopping in mid-2024 — which read exactly as *"the API caps pre-2026."* The live break was `SBN2024`. Resolving the break **at runtime** returned every owed print in one call. A second instance of the same class sat behind it: the bucket key was `PDPOSGSC-G7L11`, and the plausible zero-padded guess `G07L11` returned **200 with an empty series** rather than a 404.

The cost was not just delay. The vector resting on that data (dealer absorption) held an elevated score and an ARMED trigger on a six-week-old observation, and its pre-registered downgrade condition was ungradeable the entire time. When the data arrived, it **fired the downgrade** and removed a leg from the standing thesis — so the gap had been quietly protecting a stale bearish read.

**Why:** an error you can attribute to someone else's system stops feeling like something to debug. "Their API is limited" is a complete-sounding explanation, so the path never gets audited — and a 200 gives you nothing to argue with.

**How to apply:** when a source appears to have a hard recency limit, **check whether it is partitioned before believing the limit** — list its segments/vintages and resolve the current one at runtime rather than hardcoding. Never hardcode a segment id. Treat **200-with-empty** and **200-that-stops-early** as *failures to raise*, not as answers. And escalate only after auditing the path: an escalation raised on a self-inflicted failure spends the escalation and buries the real fix. Related: [[finding_audit_resolution_path_before_reattempt]] (the blocker is the path, not the data), [[finding_stale_executable_exits_clean]] (the script-side twin — hardcoded constants exiting rc=0), [[finding_fail_loud_on_incomplete_data]].
