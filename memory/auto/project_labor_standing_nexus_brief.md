---
name: project_labor_standing_nexus_brief
description: "LABOR now maintains a standing NEXUS_BRIEF.md (Tier-1 treatment), refreshed every closeout — not Tier-2 \"skip\""
metadata: 
  node_type: memory
  type: project
  originSessionId: 1cdcff3f-0ef5-483b-a7bb-738464843581
---

As of 2026-06-16, LABOR maintains a standing `AGENTS/LABOR/NEXUS_BRIEF.md`, refreshed at **every** closeout (AS-OF + STATUS-commit pin re-bump even on no-change sessions, per the NEXUS schema §4.1 write-back discipline).

**Why:** Will explicitly overrode the locked schema's Tier-2 scoping of LABOR ("you aint no tier 2 agent... just stale for a bit"). LABOR sits at the HEAD of the core transmission chain LABOR→CARL→REGINALD→HENRY, so its CROSS-DOMAIN SENDING edges have real Type-B connective-tissue value — exactly what the brief format exists to surface.

**How to apply:** Treat the brief as a required closeout artifact (mirror of STATUS write-back). Keep the pin = STATUS HEAD so NEXUS's mechanical stale-check (§4.4a) reads FRESH. Protect CROSS-DOMAIN + CALIBRATION first under any cap pressure. NEXUS is updating `BRIEFS_MAP.md` to add the LABOR row / Tier-1 treatment (their file — don't edit in place; flag via footer/outbox). Related: [[finding_nexus_brief_drafting_cross_check]], [[finding_closeout_as_writeback_tail]].
