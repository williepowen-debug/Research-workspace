---
name: feedback_pull_live_primary_not_dashboard
description: "On data refreshes, pull load-bearing figures from the live primary source, not dashboard.py/sibling-STATUS which read repo state files"
symptoms: "fredgraph csv is missing the newest row", "FRED shows last week's value", "curl and the dashboard disagree on the latest OAS date", "fixed-URL poll fires late"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4472d6d3-eb59-4266-a975-b0bdada7f704
---

On a data refresh, pull the load-bearing figures from their **live primary source**, not from `dashboard.py --compact` or sibling STATUS files — those read from **repo state files**, so they feel live but can be hours/days stale and only as fresh as the owning agent's last write.

**Why:** HENRY's 6/9 refresh pulled equity/vol live (yfinance via `fetch.py`) but took the credit print — the single most load-bearing number of the week — from `dashboard.py`, which sources HY/CCC from REGINALD/LIQUID STATUS in the repo. Will flagged it: "we should pull live figures over relying on the repo for your refreshes." The dashboard values happened to be correct that day, but the point value masked the daily path (credit blipped to weekly highs on NFP day, then retraced) that a direct FRED pull revealed.

**How to apply:** Credit (HY/CCC OAS) → `curl -s "https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=YYYY-MM-DD&_=$(date +%s)"` (HY) / `id=BAMLH0A3HYC` (CCC) — gives the full daily series, not a point value. ⚠️ **Keep the `&_=<epoch>` cache-buster (added 2026-09-30 at LIQUID's flag, KB-LIQ-139):** the CDN caches PER EXACT URL (max-age up to 600s, observed serving days-old rows), so a fixed URL can return a copy without the newest observation — [[finding_negative_reachability_is_a_claim_about_your_request]]. Equity/vol → yfinance `fetch.py`. Sibling STATUS / dashboard is the **fallback only** when the primary source is down (FRED was 503'ing 6/3; cleared by 6/9). Reinforces [[feedback_position_cost_basis_not_authoritative]] and the "don't cite own STATUS for live prices" rule.

**Refinement validated LIQUID 6/8:** the split is sharper than "distrust the dashboard" — `dashboard.py`'s **FRED-sourced rows (HY/CCC/SOFR/yields) are reliable** (matched a direct FRED pull to the bp), but its **yfinance-sourced rows (equity/FX/commodity) lag** because they come via repo state files. Concrete payoff: dashboard showed APO $127.57; live yfinance showed $129.93 → $131.55 *re-crossing the $130 reassess-trigger* — a load-bearing trigger-state change the stale dashboard masked (also Brent $93.43→$89.95, BIZD un-cracking $12.50). So: take FRED rows from the dashboard if needed, but ALWAYS re-pull equity/FX/commodity figures live before cementing them into a mirror doc — especially any figure sitting near a trigger line. The double-check *before* propagation is what caught it.
