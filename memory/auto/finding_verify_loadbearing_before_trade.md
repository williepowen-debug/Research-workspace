---
name: finding_verify_loadbearing_before_trade
description: de-risk load-bearing figures before trade via a verify→adversarial→propagate workflow; verify the synthesis but route upstream errors to the owning agent; magnitude-verified ≠ claim-verified — also check period, denominator, and attribution
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c162382d-99f3-44d3-97b8-b10c5637e3fb
---

Before a read becomes **trade-load-bearing**, run a **verify → adversarial → propagate** fan-out (a per-item Workflow) over its load-bearing figures:
1. **Verify** each figure against the PRIMARY (EDGAR 10-Q / FDIC Call Report / FRED / BLS / CBO), with source-locator + as-of + ✓/Δ/✗/? verdict.
2. **Adversarial** — an *independent* skeptic re-pulls the SAME primary itself and tries to refute. This is what catches the failure modes a single pass can't: wrong year/quarter, unit traps (bps↔% / $M↔$B), segment-vs-consolidated, and **hallucinated source locators**. One agent verifying itself can't catch its own confabulation; two with separate contexts can.
3. **Propagate** — stamp confirmed corrections into the canonical docs (`[CORRECTED/VERIFIED <date>]` + provenance), and grep derivative sections ([[finding_verification_correction_downstream_propagation]], [[finding_number_carries_threshold_unit_source]]).

Two meta-findings from the 2026-06-26 Tier-1 bank + Tier-2 labor pass:
- **The synthesis layer often filters errors its STATUS-file inputs carry.** The cluster synthesis docs were *cleaner* than the raw agent claims — most labor errors (e.g. a +93K revision SIGN error, a false "<1M openings", a mis-attributed 2.2M) lived upstream in LABOR/CORAL/MARCO STATUS, not the synthesis. So verify the synthesis AND check whether a wrong figure even reached it; **route upstream-owned corrections to the owning agent's inbox — don't edit their files** ([[feedback_cross_agent_inbox_writes]], [[finding_cross_flag_routing]]).
- **A framework whose discriminators absorb a wrong input is validated, not lucky.** Both passes' theses survived because the BUILD/RELEASE + specific-vs-collective discriminators neutralized the errors (e.g. ALLY's release→build sign-flip was non-counting collective anyway) — the same way [[finding_cluster_adversarial_catches_framing]] survives framing overreach.
- **Magnitude-verified ≠ claim-verified — check period, denominator, and attribution as separate axes.** A primary-real number can still carry a mislabeled *period*, a conflated *denominator*, and an *inferred interpretation* dressed as fact. Case (7/4 BROCK+SHADE teams-mode): Athene RS Level-3 "$154.8bn, +49% YoY, 40-43% of assets" — a 3-verifier EDGAR workflow VERIFIED the $154.9bn total but caught that "+49% YoY" was a **15-month** move (12/31/24→3/31/26; true 12-mo = +42%), "40-43% of assets" **conflated FV-assets ($385bn→40%) with total assets ($447bn→35%)**, and the load-bearing "it's AI-credit" *attribution* was **undisclosed/inference** (EDGAR full-text search = zero hits for the AI vehicles; the Athene-landing rested on a Michael Burry round-tripping allegation, and one vehicle — SharonAI — was outright misattributed). Verify magnitude → period → denominator → attribution; a figure can pass the first and fail the rest. [[finding_number_carries_threshold_unit_source]] [[finding_subagent_year_verification]] [[finding_private_by_construction_unverifiable]]

**Why:** agent data is hallucination-prone (repo rule #3, PSEC PIK 8.6%-not-35%); load-bearing figures feed trade thresholds, so a wrong one can mis-fire a path. Adversarial-repull + primary-wins discipline is the cheapest insurance before sizing.

**How to apply:** scope the figure-list inline first, then a per-name pipeline Workflow (verify→adversarial→conditional-propagate). Sub-agents RESEARCH/READ-ONLY — route writes to `proposals/`, never canonical edits, and they leave stray scratch files at the repo root ([[finding_workflow_agent_unprompted_commit]]) so sweep for them before commit. Tier the figures: bank Q1 baselines that thresholds hang on first; macro/regime levels are live-pull-at-trade (rule #4), not worth pre-verifying.
