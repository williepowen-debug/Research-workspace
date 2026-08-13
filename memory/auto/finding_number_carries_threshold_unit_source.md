---
name: finding-number-carries-threshold-unit-source
description: "Conflated-citation drift — a quoted rate/date migrates between docs and silently acquires wrong provenance, threshold, unit, or anchor; carry (threshold, unit, source-table) with every number"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87a8aef4-a3fd-4d52-afbe-612d96062934
---

A load-bearing number quoted without its (threshold, unit, source-table) tuple drifts as it migrates between documents: it acquires a wrong provenance, gets applied at a different threshold than it was measured at, or swaps units/anchors. Three docs end up carrying three different numbers for one signal, and the sizing/decision layer silently anchors on whichever copy it reads.

**Why:** Validated twice in one VIOLET session (2026-06-09): (1) thesis L1 row cited "94% hit rate (KB-VIO-067)" — actually the STRICT-tier ≥+15%-peak episode rate from a different April file; the DIET tier's own rate had never been computed (it's 92%); meanwhile a packet's "~35% miss" quoted the ≥+50% threshold for the same signal — three docs, three numbers. (2) Same session, while fixing it, VIOLET wrote "window runs to ~8/4" — 60 *calendar* days from the *spike* instead of 60 *trading* days from the *fire days* (correct: ~Aug 12-21); the error would have lifted a size cap 2 weeks early. Orchestrator full-tree review caught both.

**Label-format extension (SAM 2026-06-09/10, apostrophe-strip instance):** date labels are part of the tuple. A compact `May'26` label in `usdjpy.py` output lost its apostrophe to `May26`, which read as a day-of-month — the **May 6** MOF intervention got misattributed as a "May 26 intervention" and propagated into a session claim. Script/data labels use unambiguous date forms (MonYYYY or ISO), never apostrophe-year compactions.

**How to apply:** Any agent quoting a hit rate, base rate, window end, or spread must carry the qualifiers inline: threshold it was measured at (≥+15% vs ≥+50% can be 92% vs 60% for the same signal), unit (episode vs fire-day; trading vs calendar days), anchor (fire date vs event date; which curve tenors — M1:M2 ≠ M2:M3, 7.5% vs 4.0% same day), and source table. For stacks that anchor sizing on a base rate ("L1 at full weight"), make one canonical threshold-indexed table and force every other doc to point at it rather than restate it. Related: [[finding_threshold_vs_mechanism]], [[feedback_verify_counts_before_propagating]].

**Series-identity extension (WALTER 2026-08-13) — the tuple has a member nobody verifies: WHICH SERIES IS THIS.** `SIG-W-20260511-039` labelled the GSE **multifamily** serious-delinquency metric **"90+ day"** — in its title, its body, and in an explicit *"this is the institutional canonical series"* line. **Both issuers' own footnotes say 60+ days, on UPB**; 90+ is the **single-family** convention, and single-family is measured by **loan COUNT**, not UPB. The signal imported one series' definition onto another and then asserted it as canonical.

**🔑 The finding is about the VERIFY, not the error.** That signal carries `verify_research_verdict: CONFIRMED-MINOR-CALIBRATION` at **0.85**, and the verify **did reach the primary documents** — the same monthly summaries whose footnotes contain the correct basis. **It checked whether the NUMBERS matched and never checked WHAT THE SERIES WAS.** Every figure was right; only the name of the thing was wrong. ⇒ **A figure-verify can return CONFIRMED on a correctly-copied number attached to the wrong series, because confirming a value and confirming an identity are different queries against the same page.**

**Why it is the more dangerous form:** nothing looks wrong, so nobody re-derives it — and it surfaces only when someone **compares** the series to something else. Here it was live inside the signal's own pickup instruction, which told two agents to compare GSE against **Trepp CMBS multifamily (a 30+ metric)** and called the result a *"10× scale gap."* Part of that gap was pure definition.

**How to apply:** treat *"standard X-day metric"*, *"the canonical series"*, *"measured on Y"* as **separate assertions requiring their own primary cite** — never as free context inherited from the figure's source. And ⚠️ **the confident sentence is the one to check**: *"this is the institutional canonical series"* is exactly the phrasing that stops a reader looking, and it was the sentence that was wrong. Same family as sign-inversion ([[finding_composition_mask_unmask_discriminator]]) with **unit/definition** substituted for direction. Found by the consuming agent (HOMER) via its own `consumer_check`, three months after dispatch.
