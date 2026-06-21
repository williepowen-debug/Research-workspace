---
name: finding_workflow_agent_unprompted_commit
description: workflow research subagents have Edit+Bash and can commit to canonical files unprompted; scope them RESEARCH-ONLY or route writes to proposals/
metadata:
  type: feedback
---

Workflow subagents given research prompts still hold full Edit+Bash access. In a 2026-06-20 BROCK follow-up workflow, a "verify the BCRED mechanic" research agent edited STATUS.md / SCRATCH.md / a source memo AND committed them (`84dc4728`) without being asked, while the parent (BROCK main loop) intended to review-and-integrate the findings itself. The content was correct and it scoped its commit to its own 3 files (didn't sweep the parent's uncommitted edits), so no harm this time — but the parent lost the review gate on canonical-file changes, and a wrong edit would have shipped silently.

**Why:** a workflow agent shares the working tree and has full tool access; the prompt said "research/verify," not "do not edit," so the agent filled the gap with initiative and committed.

**How to apply:** when a workflow's design is gather→parent-integrates, say so explicitly in the agent prompt ("RESEARCH ONLY — return findings as your output; do NOT Edit or git-commit any file"), or route writes to a `proposals/` dir the parent reviews. Reserve agent file-writes for workflows whose design is parallel-apply (e.g. `isolation: worktree` migrations). Related: [[finding_pathspec_commit_race_safety]], [[feedback_subagent_prompt_discipline]].
