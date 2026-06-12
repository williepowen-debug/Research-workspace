---
name: finding-subagent-year-verification
description: "Before citing any web-pulled metric as load-bearing, confirm the YEAR explicitly from the primary source; aggregator articles silently reference prior-year prints"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a3eea73-de11-4e0a-b697-cd55245b5120
---

Before citing any web-pulled metric as load-bearing, confirm the year explicitly from the primary source — publication date OR explicit year-stamp on the cited number. Relative phrasing ("May print", "latest data") is INSUFFICIENT. If the primary source isn't fetchable, the metric stays in OPEN QUESTIONS until verified.

**Why:** CARL/HOMER Jun 8 2026 — HOMER round 1 cited "Trepp May 6.57% -46bps reversal" from an aggregator article that was actually referencing May **2025**, not 2026; this drove a CRL-03 invalidation argument that was wrong. Disambiguator round caught it via fresh primary searches. **Validated Jun 9:** STUE spawned with the rule pre-embedded in its prompt — all first-round web-pulls (NY Fed / Liberty Street / Wolf Street / CRS / College Investor) survived audit; the follow-up needed only methodology disambiguation, not error correction.

**How to apply:**
- Embed the rule in web-pulling sub-agent prompts at spawn time (cheapest point of enforcement).
- Aggregator/secondary articles re-surfacing old data without year-stamps are the main vector — go to the primary before banking a number.
- Transferable to any agent's web-pulling sub-agents (BRENT/SAM/REGINALD/HENRY).

Related: [[feedback-verify-existence-external-primaries]], [[feedback-pull-live-primary-not-dashboard]], [[finding-number-carries-threshold-unit-source]].
