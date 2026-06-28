---
name: workflow-subagent-repo-sandbox
description: "Workflow subagents are sandboxed to the repo working tree; pass in-repo paths (not ~/.claude or /tmp) and hardcode script values rather than relying on args binding."
metadata:
  node_type: memory
  type: finding
  originSessionId: e6ba185e-df2d-4315-a224-788f942d6823
---

A `Workflow` memory-trim audit (Jun 27 2026, laptop) returned `classified: 0` on its first run, with only the consolidate agent spawning (`agent_count` 1, no classifier transcripts). Two compounding causes: (1) the `args` object passed via `Workflow({args:{...}})` did **not** bind inside the script, so `args.count` was `undefined` → `Math.ceil(undefined/15)` = `NaN` → `Array.from({length: NaN})` = `[]` → `parallel([])` spawned **zero** classifier agents; and (2) the paths handed to the agents (`/home/willi/.claude/projects/.../memory` and a `/tmp/...scratchpad/` manifest) are **outside** the repo working tree, which the subagents are sandboxed to — so even had they spawned, they couldn't read either. The main loop (not sandboxed) read those paths fine, which masked the bug. The re-run hardcoded in-repo absolute paths (`/home/willi/Research-workspace/memory/auto/...`) and constants in the script body, and worked (178 classified, 13 agents).

**Why:** workflow subagents run with the repo as their accessible root (like `Explore`/`general-purpose` agents) — `~/.claude`, `/tmp`, and other paths outside the repo are not readable. And `args` binding is not reliable for control-flow-critical values: an `undefined` propagates silently into `NaN`/empty-array and you get a no-op phase with **no error**.

**How to apply:** (1) For any file a workflow subagent must read, use an **in-repo** path — stage a manifest inside the repo if needed (`memory/auto/` is in-repo). (2) **Hardcode** loop counts / paths / batch sizes in the script body rather than reading them from `args`, especially anything that sizes a `parallel()`/`pipeline()` array. (3) Sanity-check fan-out: `agent_count == 1` on a multi-batch `parallel()` means the array was empty (NaN/0 length) — inspect the journal/transcripts before trusting a `classified: 0`. Relates to [[finding_workflow_concurrency_529]] and [[finding_workflow_scratch_crash_recovery]].
