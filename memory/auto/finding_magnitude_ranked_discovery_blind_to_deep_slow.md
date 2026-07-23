---
name: finding_magnitude_ranked_discovery_blind_to_deep_slow
description: A discovery/screener ranked by ONE axis (rate-of-change) is structurally blind to items that are important on an ORTHOGONAL axis (size/depth) but quiet on the ranked one; complement it with a scan ranked by the other axis.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 54aec839-8993-494a-ac99-7f6f639a982b
  modified: 2026-07-23T01:13:48.414Z
---

A discovery tool that ranks candidates by a single dimension is blind to items that matter on a *different* dimension. ORACLE's `movers` ranks Polymarket by **rate-of-change** (biggest 1d/7d movers) with a fixed scan depth — so it missed the CLARITY Act market ($2.3M vol / $86K liq) even as it drifted, because a ~10pp move ranks below ~100 daily/mechanical markets swinging ±50–90pp; verified it didn't surface even 500-deep, and `--all` (no domain filter) also missed it. The bug isn't the filter — it's ranking by magnitude when the thing that made the market important was its **size**, on which it was quiet.

Fix built: a `coverage` sweep that ranks the full universe by **liquidity/volume** (movement-agnostic), subtracts what's already tracked + noise, and surfaces the deepest UN-covered markets as a review list — the orthogonal-axis complement to the magnitude sweep. Run the two together: "what moved that we don't track" AND "what's big that we don't track."

**Why:** any single-axis screener (top movers, biggest gainers, most-active, highest-severity) manufactures a false "nothing here" for items that are important on the un-ranked axis. Slow + deep is invisible to a change-ranked tool; small + violent is invisible to a size-ranked tool.

**How to apply:** when you build or rely on a discovery/screening tool, name the axis it ranks by, then ask "what's important but *quiet on that axis*?" and add a complementary scan on the orthogonal axis. Keep discovery review-only (nominate → confirm relevance → track); never auto-add on a single-axis hit. Sibling to [[finding_discovery_tool_wrong_slice_false_zero]] (wrong subset → false zero) and [[finding_ais_port_export_darkfleet_blind]] (a metric that reads 0 for structural reasons). Related: [[finding_delta_vs_own_prior_local_extreme]].
