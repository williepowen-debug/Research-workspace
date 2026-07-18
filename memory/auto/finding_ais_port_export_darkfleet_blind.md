---
name: finding_ais_port_export_darkfleet_blind
description: AIS-based port export series (IMF PortWatch et al.) are ~90%+ blind to sanctioned dark-fleet exporters — cannot anchor a strand/collapse trigger; use as refuting veto only
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e420aae3-3998-446c-87b7-00af636a2aa7
  modified: 2026-07-18T21:45:59.346Z
---

An AIS-derived port-export series (IMF PortWatch `Daily_Ports_Data` `export_tanker`, and any similar) **cannot be the trigger for a "exports collapsed / port stranded" gate on a sanctioned exporter** whose cargo moves on a dark/AIS-off shadow fleet (Iran, Russia, Venezuela).

**Why:** the series only sees vessels broadcasting AIS. Empirically (FALCON, 2026-07-18, Kharg Island `port2164`): it prints **literal ZERO for entire NORMAL export months** (Jan/May/Jul-2026 all 0) while Iran exported ~1.5 Mbpd; best month captured ~7% of real throughput. So a "≈0 for ≥N days" or "≤10% of trailing baseline" test is **satisfied by the normal baseline** — near-zero discriminating power, worse than a chokepoint transit count (which PROME had already ruled out at 86.6% crisis-day base rate). Compounding trap: the series is **lumpy per-departure**, so even a non-sanctioned mega-terminal (Ras Tanura) shows export on only ~9/30 days, median 0 — "zero today" is the modal state everywhere.

**How to apply:**
- Never freeze a numeric strand/collapse threshold on an AIS export series for a dark-fleet exporter. Positive-control it against a comparable non-dark terminal AND against known-normal months before trusting a "zero."
- **The one good direction is refuting:** a *nonzero* print (a detected loading) is trustworthy → proves flow is continuing → do-NOT-fire. Wire the tool as a veto (nonzero = refutes strand), not a fire signal.
- **The fire must come from a dark-fleet-capable corroborator:** Kpler / Vortexa / TankerTrackers (satellite + AIS-gap inference), an official export-suspension/seizure declaration, or a facility-specific war-risk/P&I withdrawal. These see what AIS can't; free access = press citations, not a scripted API.
- Also note the ~5–8d publication lag: on a fast event the corroborator (news) leads the data by ~a week.

Load-bearing for GATE-TERRY-006 (Kharg-strand / TRY-FIRE-006). Spec: `AGENTS/FALCON/domain/KHARG_LOADINGS_SOURCE.md`. Related: [[finding_threshold_vs_mechanism]], [[finding_discovery_tool_wrong_slice_false_zero]], [[feedback_pull_live_primary_not_dashboard]].
