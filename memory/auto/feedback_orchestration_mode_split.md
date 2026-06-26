---
name: feedback_orchestration_mode_split
description: multi-agent sessions — split fan-out (Workflow) from live orchestration (teams-mode) before spawning; see ORCHESTRATION_PLAYBOOK
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2f3024fd-7864-49b7-9956-726f4d2a90ff
---

Before spawning >1 agent, decide the MODE. **Mode A — fan-out** (a `Workflow` script): tasks independent + templated + no Will-decision between steps + synthesis specifiable up front (inbox sweeps, self-reports, mechanical applies, parallel verification of independent claims). **Mode B — live orchestration** (named teams-mode + `SendMessage`): cross-agent dependency resolves mid-flight, Will-decisions between rounds, or emergent direction (ownership routing, handoffs, amendments). Default to fan-out for the parallel-identical part, live only for the decision spine. Most sessions are hybrid: scout inline → fan-out the bulk → live-orchestrate the decisions. Full doc: `PROME/ORCHESTRATION_PLAYBOOK.md`.

**Why:** 2026-06-26 debrief — ~70% of that session's agent-work (5 self-reports, 5 inbox sweeps, 5 Tier-1 applies) was Mode-A work run as Mode B: babysat 5 live agents, chased idle ones who finished without delivering, ate shared-`.git/index` races. Mode-splitting gets the same output ~2× cheaper and far quieter for Will.

**How to apply:** (1) run the decision test before spawning; (2) put the deliver-before-idle contract in every spawn prompt (agents must `SendMessage` + file their result as the last action, never idle "holding"); (3) go QUIET to Will while agents work — surface only a decision, a consolidated result, or a blocker, never idle-relay; (4) write-heavy parallel work → Workflow or `isolation: worktree`, not N live committers. Links to [[finding_fleet_selfreport_convergence]], [[finding_workflow_concurrency_529]], [[feedback_parallel_spawn_independent_agents]].
