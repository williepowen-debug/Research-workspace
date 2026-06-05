---
name: finding-teams-mode-iterative-tasks
description: "Teams-mode SendMessage earns over synchronous Agent spawn when the task is iterative + context-leveraging (refinement loops, multi-round proposal/refine, watching-an-event-resolve); for batch propose-only single-turn work, synchronous spawn is equivalent. Default bias should be SendMessage for iterative; reach for it explicitly because the default mental model is synchronous spawn."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 2ca46311-2089-497f-b2d4-f84fbc8641c1
---

When deciding between SendMessage to a live mailbox-mode agent and a fresh synchronous `Agent` spawn, the deciding factor is whether the task **leverages already-loaded context** in the live agent.

**Use SendMessage when:**
- The task is a **refinement** of the agent's prior output (the agent already holds its spec, its prior proposal, and the discussion that produced it).
- The task is **iterative** (multi-round propose → refine → finalize). Each round in SendMessage costs only the delta; each round via fresh spawn re-pays the full prime cost.
- The task is **event-watching** — agent spawned at boot, pinged when an event resolves to integrate the outcome without re-briefing.
- The agent's spec + MEMORY files are non-trivial (>~3KB combined) and the spawn re-prime cost is meaningful.

**Use synchronous Agent spawn when:**
- The task is **batch propose-only single-turn** — agent reads state, produces report, exits. No follow-up expected.
- The agent's spec is small enough that re-prime cost is negligible.
- You want isolation between runs (no transcript continuity carryover).

**Bias correction (load-bearing — this is the real finding):** the default mental model defaults to synchronous spawn ("agent runs to completion → returns → I integrate"). Reaching for SendMessage requires explicit prompt — *"is this task iterative or context-leveraging?"* — before defaulting to spawn. Without that prompt, even use cases that obviously fit SendMessage (refinement loops on a propose-only agent that's still alive) get re-spawned out of habit.

**Validated 2026-06-02 on SAM's KOYOMI:** two-round spec amendment via SendMessage (initial proposal → refinement with merged trigger + decline-memory clause). Round 2 cost ~80s + ~30K tokens vs full re-spawn ~115K tokens. The teams-mode value showed up specifically on round 2 — round 1 (initial proposal) would have been equivalent via synchronous spawn. The cost-benefit flips as soon as a second round is needed; predicting that need upfront is the bias to correct.

**Transferable to:** any agent that uses sub-agents with mailbox-mode (KURA / KOYOMI / METSUKE pattern; future similar sub-agents in CARL / REGINALD / BROCK / HENRY). Also applies when SAM spawns peer agents in teams-mode for iterative work.

Related: [[finding_subagent_memory_split]] (the MEMORY-pair architecture is what makes spawning + re-spawning cheap in the first place; without MEMORY, every spawn is a re-prime regardless of teams-mode); [[feedback_named_spawn_teams_mode]] (naming a spawn triggers mailbox-mode in the first place); [[finding_teams_mode_domain_agent_spawn]] (named-spawn works; this finding refines *when* to use the addressability).
