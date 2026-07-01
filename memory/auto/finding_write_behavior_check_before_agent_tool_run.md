---
name: finding_write_behavior_check_before_agent_tool_run
description: "Before test-running another agent's tool, grep it for write ops — \"boot kit\" and \"tracker\" scripts mutate their agent's data files, and a verification run becomes an ownership violation"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 1024a372-529b-4a79-a25a-8fceaa7c7976
---

2026-07-01, twice in one session: (1) ran VIOLET's boot.py to verify a cwd fix — it refreshed her FRED caches and VX/COT ledgers (14 workbook files modified); (2) ran CARL's gas_tracker.py to verify a key scrub — it appended a row to his `GAS_TRACKER.tsv`. Both were described as boot/read tools ("live vol surface + catalyst countdown", "tracker"); both write as a side effect. Both mutations were caught in `git status` and `git restore`d before commit — but the second happened AFTER learning from the first, because I checked MARCO's kit for writes and then didn't check CARL's.

**Why:** "boot kit," "tracker," "monitor," "doctor" naming implies read-only, but fleet tools routinely persist what they fetch (cache refresh, TSV append, log write). Another agent's data files are theirs — a verification run that appends a row corrupts their ledger's meaning (a row CARL never ran), and un-restored it would ship in a commit. Doc one-liners are not evidence; VIOLET's step said nothing about writes.

**How to apply:** before executing ANY agent-owned script, grep it for write ops (`open(...'w'|'a')`, `to_csv`, `write_text`, `mkdir`, `mv/rename/unlink`, append `>>`) — 5 seconds. If it writes: verify via `--help`/`--quick`/read-only flags, point its output dir at the scratchpad when the tool allows, or verify the mechanism another way (import a function, not `__main__`). If a run does mutate: `git status` immediately, `git restore` the agent's paths, and disclose. Applied correctly later the same day: `walter_doctor.py` and BRENT `thresholds.py` were grepped read-only before running. Sibling of [[feedback_agent_git_isolation]]; the verification-side cousin of "subagents own their files" (root rule 2).
