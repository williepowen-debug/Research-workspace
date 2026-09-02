---
name: feedback_coldreaders_run_on_opus_not_fable
description: Will's standing instruction — spawn coldreader (and similar verification) subagents on Opus, never on Fable; the coldreader agent definition now pins model: opus.
metadata:
  type: feedback
symptoms: "cold reader spawned as fable", "coldreader model", "which model for subagents", "Fable limit killed a subagent"
---

**Will, 2026-09-02 13:09 ET, verbatim:** *"we definitely need you to spawn cold readers as OPUS and not FABLE."*

**Why:** Fable is the scarce, rate-limited tier (an 8/31 Fable usage limit killed a subagent mid-closeout); a blind cold read is a mechanical verification job that Opus does fully, and running ten of them on Fable in one afternoon (the 9/2 HEARTBEAT split) burned the budget the operator needs for the coordinator itself.

**How to apply:** the `coldreader` agent definition (`.claude/agents/coldreader.md` + the PROME copy, parity-gated) carries `model: opus` since 9/2 — spawning by `subagent_type: coldreader` inherits it. For any other verification-class spawn (cold reads, executing strangers, census readers) pass `model: "opus"` explicitly. Do not default a subagent to the parent's model when the task is verification rather than judgment. Related: [[feedback_front_load_planning]].
