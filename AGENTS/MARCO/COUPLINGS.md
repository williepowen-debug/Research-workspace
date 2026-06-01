# MARCO — COUPLINGS

Cross-agent and cross-vector coupling edges MARCO depends on or feeds. Per SPAWN PROTOCOL step 8: update when edges change. An edge is a *directional dependency* — "X's state changes my read of Y" — not just a shared topic.

**Last updated:** 2026-05-31 (session 8 — created; first edge MARCO↔BRENT freight-input)

---

## Active edges

### MARCO ↔ BRENT — freight/diesel input cost → produce prices (DECAYING)

- **Type:** input-cost transmission, *decaying / mean-reverting* (NOT a fixed structural line).
- **Direction:** BRENT (crude/diesel/freight cost) → MARCO Channel 1 produce-price thermometer.
- **Mechanism:** diesel and freight are a direct input cost into produce (harvest, refrigerated trucking, distribution). An oil-war spike lifts produce prices independent of the ag-labor shock — confounding MARCO's labor→produce read.
- **State (2026-05-31, from BRENT files):**
  - Crude path: $87.51 (Apr 17 low) → **$116.55 (May 5 peak)** → **$92.05 (May 29, −19% on the month)**.
  - Distillate inventories ~**11% below 5-yr avg** (structurally tight — diesel won't fall 1:1 with crude).
  - Retail pump $4.459/gal (May 27); Brent −20% **should reach pump May 31–Jun 14** (2-4 wk lag).
  - Distillate (freight) demand +4.8% YoY — trucking volume running hot, not collapsing.
- **Why it matters to MARCO:** this is *why* the produce spike is confounded (thesis v2.1). The freight contribution was a **spike-window pulse** (late-Apr/early-May) feeding the Apr CPI F&V +6.1% print — and it is **now reversing.** That decay is the basis of the dated falsification test ES-MARCO-08: if produce CPI holds while diesel relief flows through (June/July), freight wasn't load-bearing and labor re-weights up.
- **Caveat:** edge strength is asymmetric — structurally tight distillate means freight relief is **partial and lagged**, not a clean reversal. Don't over-attribute a future produce softening to diesel alone.
- **Source:** `AGENTS/BRENT/STATUS.md`, `AGENTS/BRENT/demand_destruction/TRACKER.md` (their single-source dashboard), `AGENTS/BRENT/research/DIESEL_CRACK_ANALYSIS.md` (Mar — historical crack-spread context). MARCO decomp: `domain/sources/PRODUCE_ATTRIBUTION_DECOMP_2026-05-31.md`.
- **Maintenance trigger:** revisit when (a) June/July CPI resolves ES-MARCO-08, or (b) crude breaks out of the $75-100 band (BRENT's deal/snapback binary) — a kinetic snapback to $100+ would re-arm the freight co-driver.

---

## How to use

1. An edge belongs here only if another agent's state *changes MARCO's read* — directional dependency, not shared topic.
2. Update the **State** line with dates when the upstream agent's data moves.
3. When an edge resolves (test fires, dependency breaks), note the outcome and archive the edge to a Resolved section.
4. New/changed edges also get flagged in closeout step 8.
