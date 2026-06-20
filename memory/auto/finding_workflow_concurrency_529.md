---
name: finding-workflow-concurrency-529
description: "concurrent Workflow runs + live sibling agents overload the account API (529); cap parallelism, degrade to inline/sequential"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 855d0a48-34a1-4e39-a457-ea027412c9b0
---

Running two background Workflows at once (a re-launch on top of one still grinding) **plus** a sibling agent live in another window (BRENT) overloaded the shared account API — sweep sub-agents died with `API Error: 529 Overloaded`. On HAWK's 6-theater boot-sweep (Jun 20 2026), 4 of 6 theater agents 529'd in each run; only the lower-priority theaters survived while Iran/Hormuz (the most important) failed both times.

**Why:** each workflow agent is a full model loop doing several web searches; 6+ concurrent × 2 workflows × a live sibling exceeds what the account tolerates. The workflow retries then drops the agent to `null`, so you silently lose theaters — and the ones you lose are random, not the least important.

**How to apply:** (1) never launch a second Workflow while the first is still running — check task status / `TaskStop` the redundant one first; the re-launch doesn't replace, it stacks. (2) When other agents are known-live (Will says "X is up in another window"), keep your own fan-out modest. (3) On a 529 storm, **degrade gracefully**: stop the swarm and finish the gaps **inline/sequentially** with direct WebSearch from the main loop (single calls 529 far less than a concurrent fleet) — this is the right adaptation even under ultracode, since the mandate is exhaustive+correct, not maximal concurrency. (4) Harvest partial results from the runs that DID complete (journal/result files) before re-running — don't redo theaters you already have. Relates to [[feedback_parallel_spawn_independent_agents]] (parallelism is good *within* capacity).
