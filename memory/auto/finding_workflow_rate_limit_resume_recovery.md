---
name: finding_workflow_rate_limit_resume_recovery
description: "A /deep-research or Workflow killed mid-run by a session rate limit is recoverable without a full re-run — resume the Workflow from cache (needs args re-passed) + re-spawn any plain-Agent leg that died, with a return-partial guardrail"
metadata: 
  node_type: memory
  type: finding
  originSessionId: cb850d17-5aa7-48f3-a41d-56fcd6c45a8a
---

When a `/deep-research` fan-out (or any `Workflow`) is killed mid-flight by a **session rate limit** (429 "You've hit your session limit · resets HH:MM"), don't re-run from scratch after the reset — recover surgically:

1. **Resume the Workflow from cache:** `Workflow({scriptPath: "<path>", resumeFromRunId: "<runId>", args: "<same args>"})`. Completed agents replay from cache; only the rate-killed steps (failed verify votes + the synthesis) re-run. On a 110-agent run this replayed ~73 cached and cost only the tail.
   - **Gotcha:** resume-from-scriptPath **still needs `args` re-passed** — without it the script's `args` is undefined and it errors `"No research question provided"` (a wasted round-trip). The scriptPath+resumeFromRunId alone is NOT enough for arg-driven scripts.
2. **Re-spawn any plain `Agent` leg that died** — a background `Agent` (unlike a Workflow) has **no resume**; if it died mid-work it returned no structured result (verify: its transcript tail shows the 429, and `agents_error`/last-message confirm). Re-spawn fresh, and add a **return-partial guardrail** to the prompt: "prioritize the highest-value items first; if budget runs short, return what you have with explicit gaps rather than dying mid-work." (The first attempt died trying to be exhaustive on all 5 banks; the re-spawn with WAL/OZK-first + return-partial completed all 5.)
3. **Before recovering, salvage what completed** — read the Workflow's `.output` result block: even a failed run returns the claims that were verified before the limit (13 confirmed 3-0 in the live instance), and you can synthesize those yourself (that's the owner's job anyway). Write them to the draft so nothing is lost if the session dies again. Commit the partial as a clearly-marked WIP checkpoint (crash-safe). See [[finding_workflow_scratch_crash_recovery]].

Live instance: DEWEY prompt-13 (2026-07-10) — both engines killed mid-run; base-rate fan-out resumed to a clean full synthesis, leg-1 bank pull re-spawned to completion, zero data lost. Relates to [[feedback_subagent_prompt_discipline]] (the return-partial guardrail) and [[finding_workflow_concurrency_529]] (the other main workflow-failure mode).
