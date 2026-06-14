---
name: finding_ledger_drift_behind_narrative
description: "structured ledgers (workbook TSVs) silently drift months behind the narrative STATUS because the periodic sync step keeps deferring; refresh load-bearing rows even when deferring full sync, and don't over-stamp freshness"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 46a0d5fc-64f9-4951-8aea-c3eb6bf1ba14
---

Agents with a STATUS-narrative + structured-ledger split (VX/KB/FLOW workbook TSVs) accumulate a silent drift: STATUS gets refreshed every session, but the C3 workbook-sync step keeps getting deferred, so the ledgers fall months behind with **no staleness signal** beyond an old "Last Updated" date a reader may not check. LABOR 6/14/26: VX claims rows were still dated **Mar 9** (213K initial / 1.868M CC with dead DHS-shutdown caveats) and FLOW read "Claims 209K / NFP +50K (Dec)" — a query against the ledger returns confidently-wrong stale values. Worse than a stale number: dead **ACTIVE-RED vectors** (DHS shutdown, resolved May 1, still carried RED 6 weeks later) actively mislead. Orc framing: "this is how a ledger gap silently distorts a trajectory read later."

**Why:** the narrative file is what the agent edits each session, so it stays current; the ledger is what *other* readers/queries hit, and it rots unseen. The two surfaces diverge precisely because only one is in the working path.

**How to apply:** (1) When deferring a full ledger sync, still refresh the **load-bearing rows** (claims/NFP/U-3) — cheap and most-queried. (2) Prioritize retiring **dead ACTIVE-RED/state vectors** over numeric backfill — a stale status misleads worse than a stale number. (3) Do **not** blanket-stamp a too-recent `[STALE date]` — rows carry their own (often much older) dates; a generous stamp overstates freshness. (4) Treat a 2+-cycle sync deferral as real debt, not a footnote. Candidates: CARL/REGINALD/BROCK/HENRY (same split). Related: [[finding_closeout_as_writeback_tail]], [[finding_doc_mirror_consistency_check]], [[finding_governance_doc_stale_default_drift]].
