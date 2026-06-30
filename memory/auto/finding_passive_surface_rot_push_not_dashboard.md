---
name: finding_passive_surface_rot_push_not_dashboard
description: "passive shared surfaces rot read-side; gate the push, don't replace it with a dashboard"
metadata: 
  node_type: memory
  type: finding
  originSessionId: d57ee8fe-0139-4656-99e7-3fc535618b68
---

When deciding how agents should consume a data feed/lane, the instinct to "maintain a dashboard instead of pushing signals to inboxes" (to avoid push-spam) is a **known failure mode in this system**: a passive shared surface that requires recipients to *remember to read it* rots on the **READ** side and goes write-only.

Evidence (two retirements): **COP** (the network one-pager / shared-awareness dashboard) was paused ~2.5 months unread and retired 2026-06-28. **BOARD v0.1** (recipients scan an INDEX for rows naming them) went write-only ~2 months — a real BRENT/HAWK signal was "published" but delivered to nobody. The pattern WALTER converged on instead: **per-recipient PUSH (create-only handoff files) + telemetry on the consumption gap** (`delivered_but_unconsumed`) so the gap can't rot silently.

**Why:** the noise concern is real, but its fix is **significance-gating the push** (+ de-dupe on *onset/change, not persistence*), NOT swapping push for a passive surface. A dashboard is fine for *orientation/glance state* (nothing must-not-miss depends on someone reading it → no rot risk), never for the event channel.

**How to apply:** when someone proposes "just maintain a dashboard," ask: does anything **must-not-miss** depend on a recipient reading it? If yes → push it, gated + telemetried (reuse WALTER's `BOARD_CONSUMPTION_SPEC` delivery lane, don't reinvent). Dashboard only for glance state, and only if auto-generated + freshness-stamped (COP rotted partly because its refresh was manual). Cite the COP / BOARD-v0.1 precedent. Applied 2026-06-30 to the RESEARCH-INTAKE consumer wiring (chose gated-delivery option A over a dashboard). Related: [[project_research_intake_collection_lane]], [[project_messaging_overhaul]].
