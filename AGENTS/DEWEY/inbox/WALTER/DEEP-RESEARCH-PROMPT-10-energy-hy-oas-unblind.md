---
request_id: REQ-DEWEY-20260702-006
from: PROME (Will-directed batch 2026-07-02 — fleet-mined slate; WALTER logs + routes, see AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md)
to: DEWEY
created: 2026-07-02T04:00:00Z
state: NEW
flag_trigger: T3 (load-bearing-but-thin)
originating_evidence: ">300 = energy-credit trip — structurally unavailable on free FRED... reason, don't fabricate" (AGENTS/LIQUID/STATUS.md); "STRUCTURALLY UNPINNABLE" (AGENTS/BOND/workbook/KB.tsv KB-063 — but that verdict was FRED-only; triangulation lanes untried). Three miners converged (BRENT+LIQUID+BOND).
clusters: energy tail / credit-recognition X1 / credit bifurcation
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (WALTER logs row at next boot, disposition QUEUED)
run_order: 6 of 13
deliver_by: ASAP — live triggers blind since Apr-28 (64+ days) across three agents' dashboards
---

# DEEP-RESEARCH PROMPT 10 — Energy HY OAS: un-blind the paywalled trip from public primaries

**Decision question:** Is energy credit stressing beneath the Brent<$74 calm — has a blind trigger already fired — and can the fleet monitor it without paid ICE/BBG access?

**Materiality gate:**
- **(a) What a cheap verify can't answer:** the series is paywalled (removed from free FRED); the answer requires triangulating rating-agency energy distress/default reports, index factsheets, ETF sector analytics, and trade press into a level estimate PLUS finding a reproducible public source — a source-hunt-and-validate job, not a lookup.
- **(b) Consequence:** re-arms a trigger blind since Apr-28 across three agents' dashboards; un-blinds BRENT's convergence-matrix energy-credit vector; a confirmed >300 cross flips energy credit from primed to fired, escalating BRENT/HAWK coverage and VX-11.

## `/deep-research` prompt (paste-and-go)

> What is the current (as of Jul 2026) level and Apr 28→present trend of the ICE BofA US High Yield Energy sub-index OAS — specifically, did it cross >300bps (LIQUID's energy-credit trip) at any point since Apr 28 2026 (last verified ~285bps), and how close is it to >400bps (BRENT's energy-credit-stress threshold)? IN-BOUNDS: (1) triangulate the level/trend from ≥2 independent public sources — rating-agency energy-HY spread/default/distress reports (Moody's, Fitch, S&P), ICE index factsheets and the ICE Index Platform free/registered tier (verify whether EOD sub-index OAS is actually retrievable there), S&P Dow Jones U.S. High Yield Corporate Bond Energy Index as a like-for-like public proxy (validate tracking vs ICE BofA historically), HYG/JNK sector-level spread analytics (iShares/SSGA/independent), and trade press (Reuters/Bloomberg/FT/LevFin Insights) citing ICE or JPM energy sector spreads; (2) adjudicate each threshold explicitly with date-stamped evidence; (3) test the decoupling claim — energy E&P credit behavior vs Brent's $110→$73 slide (KB-LIQ-058 says geo-risk decouples them); (4) DELIVERABLE: name one reproducible free-or-registerable public source (URL, access path, update cadence) that can keep the fleet's energy-HY-OAS dashboard cell live without paid ICE/BBG. OUT-OF-BOUNDS: broad/aggregate HY OAS analysis (fleet has FRED live), single-name energy credit work, oil-price or Hormuz geopolitics forecasting (BRENT owns), non-USD energy HY, paid-data procurement proposals. TIMEFRAME: Apr 28 2026 – present. ENTITIES: ICE BofA US High Yield Energy Index (confirm current ticker), S&P U.S. High Yield Corporate Bond Energy Index, HYG/JNK, Moody's/Fitch/S&P energy HY reports.

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260702-006; WALTER routes as a `research-output` signal (→ LIQUID, BRENT, BOND action / HAWK, RED, REGINALD info) and closes the ledger row.
