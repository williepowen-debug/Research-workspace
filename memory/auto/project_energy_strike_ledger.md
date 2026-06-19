---
name: project_energy_strike_ledger
description: "HAWK maintains a unified cross-theater energy-infrastructure strike ledger (STRIKES.tsv + SUMMARY.md); one table, theater column, not per-theater silos"
metadata: 
  node_type: memory
  type: project
  originSessionId: 511b6a9e-2036-4540-b47f-1a040d76736b
---

Created 2026-06-18 (HAWK + Prome review). HAWK maintains a per-attack ledger of material energy-infrastructure strikes at `AGENTS/HAWK/domain/energy-strikes/STRIKES.tsv` (16-col, one row per attack) + `SUMMARY.md` (living index, patterns, metric discipline). Seeded with 22 RU-UA (Ukraine→Russia oil infra) + 4 GULF-IRAN rows.

**Invariant (Prome):** ONE unified table with a `theater` column (RU-UA / GULF-IRAN) + `attacker` column — NOT per-theater files. The cross-theater unified table is what makes cross-theater observation possible (e.g. Russia campaign peaked the week Iran signed its MOU 6/17). **Do NOT assert a causal "regime rotating" — two independently-driven conflicts moving opposite in 72h is coincidence + analogy, no shown mechanism (dropped in the revised SUMMARY after ORC pass).** `FacilityOperator` ≠ attacker.

**Metric discipline:** "% capacity offline" must be a sourced as-of aggregate (e.g. Energy Intelligence ~1/3 ≈ 2.14M bpd mid-June), NEVER the sum of the Capacity column (double-counts repaired + reduced-not-offline). `Status` is point-in-time; `ReturnToService` closes the loop. Ledger is a material SUBSET (materiality bar), not an exhaustive attack count.

KB keeps lean synthesis rows ([[feedback_carl_kb_architecture]] push-down pattern): KB-HAWK-185 (May record month), KB-HAWK-186 (June). Refined-products/crack price consequence routes to BRENT. Refresh, don't retire ([[finding_refresh_not_retire_perentity_profiles]]).
