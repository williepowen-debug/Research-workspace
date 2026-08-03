---
name: finding_prereg_verdict_boundary_must_be_a_number
description: "A pre-registration's verdict boundary must be a NUMBER with an explicit NO-VERDICT band; an adjective boundary (\"materially smaller\") silently resolves toward what you already believe"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d96c8581-fca4-4eec-9dd3-ae2ca17cd98a
  modified: 2026-08-03T20:27:51.426Z
---

A pre-registration whose verdict boundary is a **word** is not pre-registered. Write the boundary as a **number**, and include an explicit **NO-VERDICT band**.

**Why:** BRENT froze a behavioral test before a market open: *"materially SMALLER than the analogue ⇒ CORROBORATING; LARGER ⇒ the premium unwinds without me."* It never said how much is "materially." Over fifteen hours the reading ran **64% → 84% → 77% → 67.6% of the analogue**. It graded cleanly at the settle (67.6%), but at the morning's 84% the author would have been **adjudicating the meaning of an adjective after seeing the print** — which is the one thing a pre-registration exists to prevent. Each flip would have *felt* like judgment rather than drift.

The missing NO-VERDICT band is the half people skip: without it, every ambiguous outcome silently resolves toward whatever the author already believed. That is the same defect as a gate with no NEITHER branch — see [[finding_compound_gate_jointly_unsatisfiable]].

**How to apply:** when writing any pre-registration, state the boundary as figures before the window opens — e.g. `≤70% = CONFIRMING · ≥90% = REFUTING · 70–90% = NO VERDICT`. Then ask the well-formedness questions, all of which are answered by *doing* rather than re-reading: **does the instrument actually trade in the grading window · does the threshold have a numeric value · did the "I verified it" claim actually run?** All three defects here were invisible to careful re-reading and instantly visible to a pull or to writing the number down — so the fix is a checklist at authoring time, not reading the draft more carefully.

Distinguish from [[finding_threshold_spec_fails_before_world]], which asks whether a spec *can fire* in the world you are in. This asks whether the spec is *even well-formed*. Related: [[finding_escalation_line_needs_delta_not_level]], [[finding_record_of_an_action_is_not_the_action]].
