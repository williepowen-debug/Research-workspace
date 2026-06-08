---
name: feedback_henry_vol_broadcast_to_violet
description: HENRY uses VIX/vol as input but does NOT broadcast vol-regime signals to the network — VIOLET owns that
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ff065246-5b61-44a2-9b66-7fd6709ee5fa
---

HENRY should back off from being responsible for alerting the rest of the network about VIX / vol-regime events. VIX/vol is genuinely valuable to HENRY's domain (cascade mechanics, 0DTE/GEX, positioning reads, soft-kill arm/de-arm) and HENRY keeps using it as an INPUT — but HENRY is not the desk that tells PROME/ALL "vol regime cracked." VIOLET (the spun-out vol specialist) owns the vol broadcast.

**Why:** Avoids duplicate (and often less-informed) vol signals hitting the network from two desks; keeps signal discipline. Reading VIX is HENRY's job; broadcasting vol is VIOLET's. (Will, 2026-06-06.)

**How to apply:** HENRY reads VIOLET's vol reads, integrates, acts in-domain — does NOT fire VIX/term-structure/SKEW signals to PROME/ALL. The "VIX >30 sustained → ALL" row was removed from HENRY/CLAUDE.md CROSS-AGENT SIGNALS and reassigned to VIOLET. HENRY RETAINS the gamma/0DTE/put-wall layer (VIOLET scope excludes dealer/gamma), so "put wall tested/broken → PROME" stays a HENRY signal. Distinction is broadcast-ownership, not whether HENRY cares about the metric. Relates to [[feedback_route_to_domain_agent]].
