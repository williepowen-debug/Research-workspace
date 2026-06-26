---
name: finding_fleet_selfreport_convergence
description: "N agents self-reporting architecture in a common template independently converge on the same issues → fix at the fleet-standard layer, not per-agent"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 2f3024fd-7864-49b7-9956-726f4d2a90ff
---

Ask N domain agents to self-report their folder architecture + processes in a COMMON template, then synthesize: the independent reports converge on the same short list of strengths and frictions. That convergence is the signal — the issues are structural fleet properties, not per-agent quirks — so the high-leverage fix is a few fleet-wide standards (a closeout-protocol addendum, a STATUS standard) rather than N separate cleanups.

**Why:** 2026-06-26 fleet arch review (CARL/REGINALD/LABOR/BROCK/SHADE). All 5 independently flagged: TSV workbook ledgers lag STATUS (universal), STATUS bloat, dead outbox, no research-retirement policy, git-mv residue. Each had also independently invented a *piece* of the ideal (SHADE §-section STATUS + §0 boot-delta, LABOR boot/closeout symmetry + boot.py, CARL PREDICTIONS.tsv falsifiers, REGINALD 11-col board_log, BROCK BRK-NN triggers) — so cross-pollination beats reinvention.

**How to apply:** for fleet introspection use a fixed template (folder-map / canonical-docs / data-layer / processes / self-assessment / top-3-ideas) + write-to-file + a ≤120-word reply; domain agents own the self-report, the coordinator owns the compare/contrast synthesis. Codify convergent fixes as shared standards, and **validate by use before locking** — the ratified pre-commit git-status guard caught 4 real problems (index race, a months-old desync, 2 residue catches) on its first day. Links to [[finding_closeout_as_writeback_tail]], [[feedback_route_to_domain_agent]].
