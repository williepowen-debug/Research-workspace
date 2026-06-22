---
name: finding_workflow_scratch_crash_recovery
description: a crashed /deep-research (or any Workflow) session leaves sub-agent outputs recoverable in /tmp task scratch — salvage before re-running
metadata: 
  node_type: memory
  type: finding
  originSessionId: 09e30781-0aec-4b05-a735-6920f23899ff
---

When a `/deep-research` or Workflow session is booted/crashes mid-run, the sub-agent (task) outputs persist on disk and are recoverable — don't assume the work is lost or re-run the whole fan-out.

Location: `/tmp/claude-1000/<munged-cwd>/<session-uuid>/tasks/<id>.output` (munged-cwd = the agent's working dir with `/`→`-`). These are the raw data-gathering outputs (fetched source text, grep dumps, filing extracts) — i.e. the EXPENSIVE source-discovery+fetch step. 0-byte `.output` files = sub-agents killed before producing (often the synthesis stage). Strip nulls with `tr -d '\0'` for readability.

**Why:** source-gathering is ~70% of a deep-research run's cost; the synthesis is cheap to redo. Salvaging the scratch turns a full re-run into "synthesize + fill the few gaps."

**How to apply:** on a "we got booted mid-research" report — BEFORE re-running — `find /tmp/claude-1000 -path '*<AGENT>*' -name '*.output' -mtime -1`, copy survivors into the agent's `output/_recovered_<date>_<topic>/`, harvest the evidence, then only re-run gap-fill searches + synthesis. /tmp can be swept, so preserve into the repo first. Relates to [[finding_closeout_as_writeback_tail]] (save artifacts incrementally) and [[finding_workflow_concurrency_529]].
