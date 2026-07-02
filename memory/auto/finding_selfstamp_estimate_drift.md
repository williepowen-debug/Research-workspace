---
name: selfstamp-estimate-drift
description: "Agents write prose timestamps as estimates that run 35-65+ min ahead of the git commit clock; stamp from `date`, trust commit times over prose stamps when reconciling"
metadata: 
  node_type: memory
  type: project
  originSessionId: 84511656-42d2-4441-a559-476c6818930e
---

Agent prose self-stamps ("Last Updated: ~11:30 ET") are often written as *projections* of when the session will finish, not from the clock — and run 35–65+ minutes ahead of the actual git commit times.

Two independent same-day instances (2026-07-02): PROME's laptop closeout stamped "~10:00/~10:45" on work committed 09:04–09:42; LABOR's NFP session stamped "~11:30/~11:45" on commits at 10:49–10:55. LABOR's root-cause confession when fixed: "I estimated instead of running `date`."

**Why:** downstream reconciliation breaks — event sequencing across sessions (corrections, machine switches, cross-agent integration order) gets mis-ordered when prose stamps disagree with commit times, and the data-minute discipline ([[quote-carries-its-data-minute]]) inherits fabricated minutes.

**How to apply:** (1) run `date` before writing any timestamp into a state file — stamp from output, never from an estimate; (2) when reconciling event order, trust `git log --date=format-local` over prose stamps; (3) a >30-min stamp-vs-commit skew is the estimate signature — correct the prose stamp, don't suspect the system clock; (4) fleet-wide template pattern ([[fleet-selfreport-convergence]]) — worth folding into boot/closeout guidance when agents are next touched.
