---
name: feedback-doc-routing-data-drops
description: "When fresh research data comes in mid-session, ask \"snapshot or narrative?\" before placing it — narrative goes to TIMELINE, snapshot to STATUS only"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9f3a6359-35c9-4f29-8945-9ec052342b61
---

When fresh research (news, search results, sub-agent output) lands mid-session, the default landing zone for the **narrative** is TIMELINE (or THESIS for structural shifts, CALENDAR for forward dates), **not** STATUS. STATUS only owns the current-value snapshot (price tables, threshold status, probabilities, position details).

**Why:** SAM CLAUDE.md doc-ownership table already states this rule explicitly. But under time pressure on a fresh-data sweep, the natural reflex is "everything new goes into STATUS." Will pushed back on 2026-05-26 when I proposed putting MOU framework hardening + Bessent G-7 refresh + Phase 1 stability watch into STATUS — that data was 80% narrative/forward-question, only 20% snapshot. Correct routing was: narrative → TIMELINE, structural refinement → THESIS subsection, forward date → CALENDAR row, STATUS edit → none (intraday drift was noise).

**How to apply:** When a research pass produces new items, before editing any file, sort each item:
- **Is it a current-value tick or threshold-status change?** → STATUS market-data table
- **Is it an event narrative (what happened, when, why it matters)?** → TIMELINE entry or extension
- **Is it a structural refinement (channel mechanism, threshold definition)?** → THESIS subsection
- **Is it a forward date with thresholds?** → CALENDAR row
- **Is the "snapshot" part within a few bps/cents of the existing STATUS values, or hours old?** → skip the edit, let the next boot.py refresh handle it

The discipline: pause and route by category before opening any file. Don't default to STATUS just because it's the most-edited doc.

Related: [[finding_walter_refactor_pattern]] (similar STATUS-as-snapshot discipline).
