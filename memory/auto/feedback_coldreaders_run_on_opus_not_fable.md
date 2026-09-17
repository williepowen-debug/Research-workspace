---
name: feedback_coldreaders_run_on_opus_not_fable
description: Will's standing instruction (n=2, 9/2 and 9/17) — spawn EVERY subagent on Opus, never on Fable: domain-desk sessions included, not only cold readers; pass model: "opus" on each Agent call, since general-purpose inherits the parent's model.
metadata:
  type: feedback
symptoms: "cold reader spawned as fable", "coldreader model", "which model for subagents", "Fable limit killed a subagent", "spawning these all as FABLE", "burn up our tokens", "spawn your subagents as OPUS"
---

**Will, 2026-09-02 13:09 ET, verbatim:** *"we definitely need you to spawn cold readers as OPUS and not FABLE."*

**Why:** Fable is the scarce, rate-limited tier (an 8/31 Fable usage limit killed a subagent mid-closeout); a blind cold read is a mechanical verification job that Opus does fully, and running ten of them on Fable in one afternoon (the 9/2 HEARTBEAT split) burned the budget the operator needs for the coordinator itself.

**How to apply:** the `coldreader` agent definition (`.claude/agents/coldreader.md` + the PROME copy, parity-gated) carries `model: opus` since 9/2 — spawning by `subagent_type: coldreader` inherits it. For any other verification-class spawn (cold reads, executing strangers, census readers) pass `model: "opus"` explicitly. Do not default a subagent to the parent's model when the task is verification rather than judgment. Related: [[feedback_front_load_planning]].

**Will, 2026-09-17 08:52–08:53 ET, verbatim (second instance — the rule GENERALIZES):** *"hey you are spawning these all as FABLE? You are going to burn up our tokens"* · *"You need to spawn your sugagents as OPUS please."*

**What happened:** on the 9/17 post-crash boot PROME spawned NINE domain-desk sessions (HAWK · BOND · VIOLET · LABOR · DAEDALUS · MARCO · ZHAO · BRENT · CARL) as `subagent_type: general-purpose` with NO `model` override — `general-purpose` has no model pin, so every one inherited the parent's model (Fable). Only the `coldreader` spawns ran on Opus, because that agent definition pins it. The 9/2 memory's own "How to apply" said *"do not default a subagent to the parent's model when the task is verification rather than judgment"* — which read as permission to run judgment desks on Fable. That reading is dead.

**Rule as it now stands:** **every `Agent` call passes `model: "opus"`** — domain desks, recovery sessions, drains, verifiers, all of them. Fable is the coordinator's tier only. A desk whose task needs Fable is a Will decision, asked before the spawn. **Also:** a session that plans to WAIT hours for a scheduled print (BOND on a 13:00 auction) is closed out and re-spawned at the print, never held open. Related: [[finding_two_phase_spawn_grader_contract]] · [[feedback_front_load_planning]].
