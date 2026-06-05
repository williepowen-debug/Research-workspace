---
name: finding-revival-boot-doc-sweep
description: "When reviving an agent stale 30+ days, sweep boot docs (CLAUDE.md, MEMORY.md, CALENDAR.md, STRATEGY.md, IDENTITY.md, USER.md) alongside STATUS — staleness compounds across all of them, not just the dashboard"
metadata: 
  node_type: memory
  type: finding
  originSessionId: ed01e692-59de-4d0c-9976-4e70baf5de20
---

When reviving an agent that has been stale 30+ days, the STATUS refresh is necessary but not sufficient. Boot-up docs go stale alongside STATUS — hardcoded "Current" threshold values, calendar weeks past, NEXT SESSION items pointing at resolved drills, FILES tables referencing archived files, and historical-thesis docs whose projected paths didn't play out.

**Why:** STATUS captures the live state, but boot docs encode the entry context the next session reads to orient. A fresh STATUS sitting behind a CLAUDE.md with "HY OAS Current: 298" (when actual is 280) means the next-boot agent re-reads stale framing on its way to STATUS. Compounding effect: stale boot docs → contaminated mental model → potentially misreads STATUS too.

**Concrete LIQUID-2026-05-18 example:**
- CLAUDE.md KEY THRESHOLDS table all 5 rows hardcoded to Apr values
- CLAUDE.md had a literal broken search-and-replace artifact ("All mail lives in removed:") undiscovered for 40+ days
- CALENDAR.md three sections (This Week / Next Week / Month Ahead) all in the past
- STRATEGY.md "HY OAS in 300-320 range (current: 312)" — current is 280
- MEMORY.md "NEXT SESSION" pointed at the resolved SOFR Apr 17-21 playbook drill
- USER.md "Key Dates" all March

**How to apply:**
After STATUS is refreshed on revival, do a separate audit pass:
1. CLAUDE.md — fix any embedded "Current" values; check FILES table against actual files; look for broken text
2. MEMORY.md — promote current → prior, draft new current, refresh next-session items
3. CALENDAR.md — roll past-week sections into Resolved; populate forward
4. STRATEGY.md — refresh "current" numbers; check position assessments
5. IDENTITY.md, USER.md — Current Focus and Key Dates
6. Historical analysis docs — flag any whose projected path didn't play out

Commit boot-doc sweep separately from STATUS refresh. The two commits read more cleanly that way and the boot-doc sweep is grep-able as a recurring revival pattern.

Related: [[finding-revival-proxy-pattern]] (Step 4 of orchestral layer); [[feedback-verify-counts-before-propagating]] (verify before propagating dates/numbers, especially for forward calendar items the proxy didn't fetch live).
