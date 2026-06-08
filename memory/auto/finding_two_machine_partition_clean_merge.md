---
name: finding-two-machine-partition-clean-merge
description: Running the agent fleet across two machines on one shared GitHub branch merges cleanly IF agents stay in their own AGENTS/<NAME>/ dirs and no agent is double-run across machines; disjoint dirs make cross-machine rebases conflict-free by construction
metadata: 
  node_type: memory
  type: finding
  originSessionId: 141e10be-bcd0-4cf8-874e-178bfa137697
---

**Validated 2026-06-08 — first full two-machine merge.** Will runs the fleet split across a desktop and a laptop sharing one `origin/master`, to spread load (5+ agents on one box crashes it). The day's merge: 23 desktop commits (CARL/BRENT/REGINALD/BROCK/HAWK) vs 21 laptop commits (PROME + OTTO + MARCO + LABOR). `comm -12` of the two changed-file sets was **empty → disjoint → rebase cannot conflict** (a conflict requires the same file changed on both sides). Rebase of 21 onto 23 + fast-forward push went clean, zero conflicts, no force.

**Why it works:** agents only ever write inside their own `AGENTS/<NAME>/` directory (+ PROME owns root/FORGE/PROME/memory). Two machines editing different agents' dirs literally cannot collide. Cross-machine coordination happens purely through origin (push/pull) — a machine is effectively a "separate clone" at coarse granularity.

**The operating rules that keep it clean (how to apply):**
1. **Partition agents by machine.** Give each agent a home machine. **Never run the same agent on both at once** — same dir + two writers is the *only* way to manufacture a real conflict.
2. **Push is Will-coordinated, not per-session** (root reconciled 6/8). Agents commit locally and bank up; sync in batches at natural boundaries, not continuously. Cuts the human-referee tax.
3. **Sync sequence:** quiesce one machine (agents finish + commit), then `git pull --rebase` + push; the other pulls. Verify disjoint via `comm` and tree-clean before the rebase; stage the merge (fetch → conflict-check → rebase → verify → push) with gates before the irreversible push.

**Caveats:** the friction people *blame* on the two-machine split is actually (a) multiple agents sharing one working tree *per machine* (within-machine races: commit-under-you, dirty-tree-blocks-pull) and (b) manual coordination overhead — neither caused by the split. Pathspec commits mitigate (a)'s index race but NOT the working-tree races; **separate-clones-per-agent** (post-Jun-16 migration) is the real fix that removes within-machine friction too. Two-machines-partitioned is a strong interim. Related: [[finding_pathspec_commit_race_safety]], [[feedback_defer_push_coordinate]], [[finding_push_train_pattern]].
