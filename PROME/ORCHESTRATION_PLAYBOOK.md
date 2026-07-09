# ORCHESTRATION PLAYBOOK
**Created:** 2026-06-26 | **Owner:** Prome | **Companion to:** `PROME/ORCHESTRAL_LAYER_DESIGN.md` (fleet-scan/ranking layer)
**Purpose:** Operating rules for running a multi-agent session. Read when Will says "let's orchestrate" / before spawning >1 agent. Born from the 2026-06-26 debrief: the orchestration layer works, but we were paying live-orchestration prices for fan-out work and absorbing a fragile-concurrency tax.

---

## The core rule: MODE-SPLIT

Every multi-agent task is one of two modes. **Decide the mode BEFORE spawning.** Mixing them is the #1 source of wasted cost and operator-attention tax.

| | **Mode A — Fan-out execution** | **Mode B — Live orchestration** |
|---|---|---|
| **Tool** | `Workflow` (deterministic script) | teams-mode `Agent` (named) + `SendMessage` |
| **Use when** | tasks are independent, templated, no Will-decision between steps, collection/synthesis specifiable up front | cross-agent dependency resolves mid-flight, Will-decisions between rounds, next step depends on what an agent surfaces |
| **Coordinator role** | author script, collect, synthesize | route, decide, relay, iterate |
| **Concurrency** | serialized by the runtime → no git index races | N concurrent committers → index races (mitigate) |
| **6/26 examples** | the 5 arch self-reports, 5 inbox sweeps, 5 Tier-1 applies | gate-cluster ownership pivot, BROCK↔SHADE handoff, the CARL amendment |

**Decision test — use Mode A (fan-out) if ALL are true:**
- [ ] tasks are independent (no agent needs another's mid-flight output)
- [ ] the prompt is templated/near-identical across agents
- [ ] no Will-decision is needed *between* sub-steps
- [ ] you can specify the collection + synthesis up front

**If ANY is false → Mode B (live).** When unsure, default to Mode A for the parallel-identical part and Mode B only for the decision spine.

> **6/26 lesson:** ~70% of the agent-work (self-reports, sweeps, applies) was Mode-A work run as Mode B — I babysat 5 live agents, chased idle ones, and ate index races for tasks a Workflow would have serialized and collected cleanly. Mode-split that work and the same output is ~2× cheaper and quieter.

---

## Most sessions are HYBRID

Don't pick one mode for the whole session. The common shape:

1. **Scout inline** (Prome, no agents) — list the work, find the owners, scope the diff.
2. **Fan-out the parallel part** (Mode A / Workflow) — fire N templated tasks, collect to files, synthesize.
3. **Live-orchestrate the decision spine** (Mode B) — route emergent findings, present Will-decisions, handle handoffs/amendments.

6/26 done right would have been: scout → **Workflow** the triage + sweeps + arch-reports + Tier-1 applies → **live** only for the gate-cluster routing, the BROCK/SHADE spin-ups, and the addendum approval.

---

## Model tiering (Fable-orchestrated fleet — Will-approved 2026-07-08)

When PROME runs on a top-tier model (Fable 5), **judgment concentrates up, volume delegates down.** Domain agents spawn as subagents/workflows with explicit `model:` overrides instead of Will launching separate interactive sessions. This is the old "research on Sonnet, synthesis on Opus" cost doctrine, one tier up.

| Tier | Model | Work |
|---|---|---|
| Orchestrate/decide | PROME on Fable 5 | Synthesis, adversarial verify of load-bearing claims, trigger-adjudication sign-off, regime/HEARTBEAT/DOCKET/canon writes, cross-agent routing, everything Will-facing |
| Domain judgment | `sonnet` (default) | Domain-agent spawns: evidence gathering + first-pass adjudication, written to their own dirs |
| Load-bearing exception | `opus` | Adjudications where a wrong call moves positioning (e.g., a fired trigger's re-arm call) |
| Mechanical | `haiku` | Fetches, grep/inventory sweeps, staleness checks, formatting, workflow readers |

**Quality rails — stricter, not looser, at lower tiers:**
- **Tight task packets:** every spawn states scope, files to read first (own `CLAUDE.md` + `STATUS.md` — subagents don't auto-load them), today's date explicitly, deliverable format, deliver-before-idle. Web tools need ToolSearch loading — say so in the prompt.
- **Structured outputs** (Workflow `schema`) wherever the result is data.
- **Load-bearing findings get a Fable-level primary-source check** before touching canon, firing a trigger, or routing cross-agent — mandatory, not judgment-call.
- **Escalation valve:** contradictions / ungrounded hedging from a lower-tier agent → PROME pulls that specific question up inline; fallback = re-run higher (still cheaper than running everything big).
- **Git:** spawned agents commit only their own `AGENTS/<NAME>/` dirs (or leave commits to PROME's closeout sweep). Never shared/root files.
- **Context economics:** PROME delegates file-dump reading (Explore/agents) and keeps Fable tokens for synthesis — that's where the cost asymmetry pays.

**Not delegated down, ever:** trigger sign-off, X1/regime state changes, routing decisions, Will-approvals, Telegram sends, HEARTBEAT/DOCKET writes.

---

## Operating disciplines (apply in BOTH modes)

### 1. Report-delivery contract (fixes the chase-the-idle-agent defect)
Every agent's **last action before idling = deliver its result.** Never go idle "holding" without delivering. Two acceptable channels:
- **Live (Mode B):** `SendMessage` the report to the coordinator as the final step.
- **Fan-out (Mode A):** write to a known file (`AGENTS/<NAME>/<TASK>_REPORT.md`) + a ≤120-word reply; coordinator batch-collects. *(Workflow's `schema` option enforces this automatically — the agent's return value IS the structured result.)*

Put this line in every spawn prompt: *"Deliver your result (SendMessage + file) as your final action before idling — do not idle without delivering."*

### 2. Relay discipline — GO QUIET while agents work
Prome surfaces to Will only: **(a)** a decision Will must make, **(b)** a consolidated result, **(c)** a blocker. **Do NOT relay** idle pings, "holding for X", or per-agent acknowledgments. Batch N agent reports into ONE synthesis, not N relays. *(6/26: dozens of "X is idle / holding" turns were pure operator-attention tax.)*

### 3. Right-size the agent count
The synthesis is the coordinator's job. Don't spawn an agent for work you'll redo. Match N to the *actual* parallelism, not to the number of agents that exist.

### 4. Concurrency / git hygiene
- **Mode A (Workflow) serializes** the agent lifecycle → avoids the shared-`.git/index` race entirely. Prefer it for any write-heavy parallel work.
- **Mode B (live, N concurrent committers)** → index races, dangling deletions, foreign pre-staged files. Mitigations: the canonical **pre-commit `git status -- AGENTS/<NAME>/` check** (root CLAUDE.md), staggered commits, or `isolation: worktree` per agent. A non-trivial Mode-B session is **standing evidence for the separate-clones / worktree migration** (deferred decision — SAM's proposal); log it.

### 5. Triage-first for domain work
Spawn domain agents on a **report-before-execute** mandate so Will directs what gets actioned. Worked well 6/26 — keep it.

### 6. Route to the domain OWNER, not the adjacent agent
Cross-domain findings go to the agent that owns the domain, even if another surfaced it. ([[feedback_route_to_domain_agent]], [[feedback_check_domain_owner_before_messaging]]). 6/26's single biggest value-add: routing the gate-cluster to BROCK (owner) instead of CARL (transmission-adjacent) surfaced 3 more gates + the compounding mechanic + the insurer-lender pathway.

---

## Anti-patterns (seen 6/26 — don't repeat)
- **Fan-out work run as live teams-mode** → babysitting, idle-chasing, index races. Use a Workflow.
- **Agents idling without delivering** → wasted round-trips pinging "where's your report?"
- **Relaying every idle notification to Will** → attention tax with no decision content.
- **Amendment racing execution** → I sent an amendment after CARL had already executed → reversions. In live mode, confirm an agent is *holding* (not mid-execute) before sending follow-on scope; or fan-out the corrected task fresh.
- **N agents committing concurrently to the shared tree** → residue/duplicates. Serialize (Workflow) or worktree-isolate.

---

## Quick checklist before spawning
1. **Scout done?** Do I know the work-list, the owners, the diff?
2. **Mode?** Run the decision test → Mode A (fan-out/Workflow) for the parallel-identical part, Mode B (live) only for the decision spine.
3. **Delivery contract** in every prompt? (deliver-before-idle)
4. **Will-decisions identified** up front so I can batch them, not drip them?
5. **Concurrency safe?** Write-heavy parallel → Workflow or worktree, not N live committers.
6. **Go-quiet plan:** what's the *next* thing worth interrupting Will for?

---

## Related
- `PROME/ORCHESTRAL_LAYER_DESIGN.md` — fleet-scan / ranking / revival-proxy layer (the *what to work on*; this doc is the *how to run it*).
- Auto-memory: [[finding_fleet_selfreport_convergence]], [[finding_workflow_concurrency_529]], [[feedback_parallel_spawn_independent_agents]], [[feedback_named_spawn_teams_mode]], [[feedback_warm_parked_agent_collision]].
