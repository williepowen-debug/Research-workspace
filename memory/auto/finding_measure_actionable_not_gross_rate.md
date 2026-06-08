---
name: finding_measure_actionable_not_gross_rate
description: "When instrumenting fallback/escalation/error signals, measure the actionable sub-category, not the gross rate — gross rate mispenalizes highly-connected nodes that legitimately generate healthy volume"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b52fd1c9-857d-4e81-80ca-85f0d0ccc7fb
---

When you build an instrument to detect a failing node (a bad brief, a flaky service, a noisy agent), **measure the one sub-category that actually means "this node is failing" — never the gross event rate.** Decompose the signal by *cause* first, then meter only the actionable cause.

Concrete origin (NEXUS_BRIEF fallback instrumentation, 2026-06-07): NEXUS falls back from a brief to raw STATUS for four reasons — `stale` (agent didn't refresh), `convergence` and `uncertainty` (NEXUS legitimately drilling cross-agent threads = healthy), and `brief-gap` (brief was fresh but inadequate). Only **`brief-gap` rate** is the quality signal. Metering *total* fallback rate would have flagged exactly the best agents as worst: a Type-B-rich / highly-connected node (e.g. BRENT, with a live multi-domain cascade) legitimately generates high `convergence` drill-down volume — that's the system working, not failing.

**Why:** Connectivity and healthy activity inflate gross counters. A node that does the most valuable cross-cutting work trips the most healthy escalations, so a gross-rate alarm inverts the ranking — it punishes the hubs you most want to keep. The signal you want is buried inside the legitimate volume until you split by cause.

**How to apply:** Before shipping any rate-based health/escalation metric, ask "what are the *causes* of this event, and which one is the only one that's bad?" Log the cause per event (append-only), roll up by the actionable category alone, and explicitly document that the healthy categories must NOT be read as defects. Keep thresholds provisional until real data sets them (measurement-before-thresholds). Corollary from the same work: a cross-agent synthesis schema must be stress-tested on *both* heavy axes — single-deep-catalyst (SAM) and many-shallow-edges (BRENT) — because each surfaces gaps the other can't (BRENT's multi-hop-cascade gap was invisible to SAM's pilot). Related: [[finding_shared_antecedent_independence_test]].
