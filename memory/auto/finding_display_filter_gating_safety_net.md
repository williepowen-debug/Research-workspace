---
name: finding-display-filter-gating-safety-net
description: "A boot-summary keyword/priority filter written for forward sections silently gates the past-due safety net too — low-priority FIRED items vanish, and a fixed look-back window ages out unswept ones. Audit compact-mode filters against every section they touch (OTTO boot 7/25: 3 of 4 fired catalysts hidden, a 5th aged out)"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 53f77d69-be8e-4391-a23f-6461969b9141
  modified: 2026-07-25T16:03:35.845Z
---

Boot kits typically render sub-script output in a **compact mode** that prints only "interesting" lines — matched by priority glyphs (🔴/🟠/⚠️) or keywords. That filter is written with the *forward* sections in mind (upcoming catalysts, due predictions), where a priority marker is always present. When the same filter is applied to a **past-due / already-fired** section, it stops being a display choice and becomes a **correctness gate on a safety net**.

**Why (OTTO, 2026-07-25).** Boot after a 21-day gap reported **one** recently-fired catalyst. Running the sub-script directly showed **four** — the three hidden rows carried 🟡 priority and matched no keyword. One of them was the **First Brands creditor-vote deadline**, a direct dependency of the agent's highest-conviction open prediction. A **fifth** (Q2 bank earnings, the last forward-discovery input for another prediction) had already aged out of a hard-coded `PAST_RETENTION = 10` day window. Two independent defects, both in the mechanism that exists specifically to stop fired catalysts going unswept — and both invisible, because the boot printed a confident, clean-looking summary either way.

**The two failure shapes, both worth checking for:**
1. **Severity-gated safety net.** A fired low-priority catalyst is still an *unswept* catalyst. Severity determines how much it matters, not whether you're told it happened. Never make past-due surfacing conditional on priority.
2. **Fixed look-back vs. actual cadence.** A constant like "last 10 days" encodes an assumption that the agent runs at least that often. Spawn-gated / Tier-2 agents routinely don't. **Derive the window from the last closeout** (e.g. `STATUS.md` mtime + grace, floored and capped) so it self-widens exactly when the agent has been away — which is precisely when things were missed.

**How to apply.**
- When adding or editing a compact/summary filter, enumerate **every section** of the wrapped output it will touch, and ask per-section whether omission is merely quieter or actually *lossy*. Make the filter section-aware (sticky "print everything in this block") rather than one global keyword list.
- Set defaults by **asymmetric cost**: re-showing an already-swept row costs a line of noise; hiding an unswept one costs a catalyst. Document the asymmetry in the docstring so a future tidy-up doesn't "optimize" it back.
- **Verify by differential**: run the wrapper and the sub-script side by side after any filter change and diff the row counts. The defect is invisible from the wrapper alone — a filtered boot looks identical to a clean one.
- Sub-agent coverage does not protect you here. OTTO has a dedicated docket-steward sub-agent for exactly this failure class; the miss was re-introduced one layer up, in the orchestrator that renders its output.

Related: [[finding_boot_closeout_hardening_recipe]], [[finding_mechanize_the_cap_not_the_ritual]], [[finding_fail_loud_on_incomplete_data]], [[finding_passive_surface_rot_push_not_dashboard]].
