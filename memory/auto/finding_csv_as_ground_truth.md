---
name: csv-as-ground-truth
description: "For state-file rehabs (FORGE/STATUS, POSITIONS, agent KBs that drifted from reality), locate the ground-truth source first and scope the rehab against it second; without ground truth, \"fix\" becomes \"guess\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 93c60a77-e8e4-4422-945e-267bc5b8b93d
---

When rehabbing a stale state file (positions, prices, holdings, counts), find the ground-truth data source BEFORE choosing rehab scope. Without ground truth, the rehab is half-blind reconciliation. With ground truth in hand, what would have been a Path-B "patch the worst" becomes a Path-B+ "clean reconcile."

**Why:** *5/21 FORGE rehab. Initial plan was Path B (patch FXY row + flag expired options + leave the rest). Discovery mid-pass: Fidelity CSV downloaded 2:03 PM ET that day was sitting in RED's processed inbox. Pivoting to "ground-truth-first" scope (B+) turned a half-done patch into a full position-table reconciliation in the same time budget. Without the CSV, B would have rebuilt against the same drifted internal state that caused the rehab need.*

**How to apply:**

1. **Before scoping a rehab, ask: "What's the ground-truth source for this data?"** Examples: Fidelity CSV for positions, FRED API for macro data, Treasury auction PDFs for auction terms, SEC EDGAR for filings, broker statements for FXY-style off-CSV positions.
2. **Locate the source before choosing rehab scope.** Search the repo for recent downloads (RED inbox, FORGE/data/, agent-specific dirs); ask Will if not present.
3. **If source exists:** scope rehab to "reconcile to ground truth" (B+ / full).
4. **If source doesn't exist or is also stale:** scope rehab to "fix the worst, flag the rest as STALE banner" (literal B / patch). Don't pretend to reconcile when you can't.
5. **Document the source in the rehab artifact** ("STATUS reconciled against Fidelity CSV (5/21 14:03 ET) + SAM v1.4") so future rehabs know what was authoritative.

**When ground truth is partial:** flag the gap explicitly (e.g., "FXY $58C not in CSV — SAM v1.4 says held, broker check pending"). Don't silently reconcile against partial data.

**Related patterns:**
- [[feedback_verify_counts_before_propagating]] — same family; this is the rehab-specific application
- [[feedback_front_load_planning]] — ground-truth location is a Q to surface in the planning pass
- [[feedback_evidence_standalone]] — present what the ground-truth data says before layering thesis

**Validated:** FORGE rehab 5/21 (commit `ec7e8ad9`, +442/-86 lines, 5 files, 0 mid-execution review escalations after the planning pass).
