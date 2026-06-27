---
name: finding_migration_tally_inventory_incomplete
description: a fleet migration's self-reported "N/M done" over-counts when the INVENTORY itself is incomplete — unlisted items are never swept AND never counted as missing; verify by reading the actual files
metadata:
  type: finding
---

A multi-file/fleet migration that tracks completion as a tally ("18/21 agents flipped") has a failure mode beyond miscounting a known set: **the inventory (denominator) can itself be incomplete.** Items that were never on the list never get swept — and, crucially, never get counted as *missing* either, so the tally reads "done" while the work isn't.

**Concrete (2026-06-27 auto-push migration):** PROME logged "18/21 CLAUDE.md flipped, complete." A later verification audit (reading every agent's actual file) found **7 still on the old protocol** — and 3 of those (VIOLET/REGINALD/BROCK) were **never in the migration's Tier-3 inventory at all**, so the lazy-sweep structurally could not reach them. The "18/21" was banked as truth without anyone re-reading the files.

**Why:** a running tally is a proxy for "did the work happen," and proxies drift from ground truth. An incomplete inventory makes the proxy *doubly* unverifiable — you can't even enumerate what's missing from the count.

**How to apply:** for any migration/sweep with a completion claim, before calling it done, **enumerate the target set from ground truth (the actual files/dirs), not from the migration's own inventory**, then diff. A cheap `grep`/script over the real surface (e.g. "which CLAUDE.md still contain the old phrase") beats trusting the plan's checklist. Extends [[feedback_verify_counts_before_propagating]] — the new angle is that the *set definition* itself is a thing to verify, not just the count over a trusted set. Pairs with [[finding_fleet_selfreport_convergence]] (self-reports converge on real issues, but self-reported *completeness* is not verification).
