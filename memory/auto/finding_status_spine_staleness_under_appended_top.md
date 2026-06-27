---
name: finding_status_spine_staleness_under_appended_top
description: a STATUS that appends fresh dated sections on top leaves a stale spine (header/dashboard/marks) reading as current
metadata: 
  node_type: memory
  type: finding
  originSessionId: e82b4863-3171-48dc-9d74-abe907303b65
---

When an agent's STATUS is maintained by **appending a fresh dated section to the top** each session (BRENT pattern), the file accretes a current top over a **stale spine**: the "Last Updated" header becomes a stacked vN.0→vN.3 changelog, the Overall Status / price dashboard / forward-TODO blocks keep their write-date values, and predictions go un-regraded. A reader gets fresh prices in the top section and Jun-22 prices in the dashboard four days later — the [[finding_ledger_drift_behind_narrative]] failure inside one file.

**Tell:** line-count can be *at-cap* (BRENT 242/250) while the bloat is the redundant header changelog + superseded dated sections, not section sprawl. Byte-heavy ≠ over-cap (HAWK was 154/250 but 25KB from dense prose cells) — check both.

**Fix is two-part, and the split matters for who does it:** (1) ARCHIVE historical dated sections verbatim to the agent's established archive path + leave a digest pointer — pure hygiene, PROME-safe. (2) REFRESH the stale spine (header/dashboard/marks) to current reality + re-grade resolved predictions — this **restates the agent's marks = analytical, the agent's lane, not PROME's.** So a STATUS "trim" is NOT pure hygiene; route the refresh half to the owner (SendMessage the just-run agent — it has warm context and owns the file) rather than hand-editing its marks. **Why:** PROME hand-editing a domain agent's dashboard/marks risks misstating them ([[feedback_route_to_domain_agent]], [[feedback_check_domain_owner_before_messaging]]).

**How to apply:** before "trimming" a STATUS, audit current-vs-design-role ([[finding_path_b_trim_pattern]]); if the spine is stale, the trim is an owner-refresh, not a coordinator cut. Recommend appenders adopt a refresh-the-spine-each-closeout discipline so the top and body never diverge.
