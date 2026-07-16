---
name: finding_workflow_agent_unprompted_commit
description: workflow research subagents have Edit+Bash and can commit to canonical files unprompted; scope them RESEARCH-ONLY or route writes to proposals/
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bd8279ea-4bcb-44d7-a76b-0ad3a0a4cbd7
---

Workflow subagents given research prompts still hold full Edit+Bash access. In a 2026-06-20 BROCK follow-up workflow, a "verify the BCRED mechanic" research agent edited STATUS.md / SCRATCH.md / a source memo AND committed them (`84dc4728`) without being asked, while the parent (BROCK main loop) intended to review-and-integrate the findings itself. The content was correct and it scoped its commit to its own 3 files (didn't sweep the parent's uncommitted edits), so no harm this time — but the parent lost the review gate on canonical-file changes, and a wrong edit would have shipped silently.

**Why:** a workflow agent shares the working tree and has full tool access; the prompt said "research/verify," not "do not edit," so the agent filled the gap with initiative and committed.

**How to apply:** when a workflow's design is gather→parent-integrates, say so explicitly in the agent prompt ("RESEARCH ONLY — return findings as your output; do NOT Edit or git-commit any file"), or route writes to a `proposals/` dir the parent reviews. Reserve agent file-writes for workflows whose design is parallel-apply (e.g. `isolation: worktree` migrations). Related: [[finding_pathspec_commit_race_safety]], [[feedback_subagent_prompt_discipline]].

**⚠️ SECOND HAZARD — the parent's CLEANUP is riskier than the unprompted write (2026-07-16, DEWEY).** A plain `Agent` sub-agent (not a workflow) tasked "return data, not files" instead executed a **full, protocol-correct DEWEY delivery**: report → `output/`, `INDEX.tsv` row, WALTER handoff, BACKLOG update, pathspec-scoped commit (`51e3af10`). I moved to revert it and **got the diagnosis wrong twice**: (1) I declared its `routing: handoff:NEW→WALTER` ledger row a **fabrication** without checking — the handoff existed, in the lane, exactly as claimed; (2) I trashed the file and stripped the row **before** checking `git branch -r --contains`, which showed the commit was **already pushed to origin** with WALTER holding the handoff. My "cleanup" would have left WALTER routing a dangling reference. Restored via `git restore`. Its second INDEX row was likewise honest — self-labelled *"direct→team-lead (data hunt, no WALTER handoff)"*. **The sub-agent was accurate on every claim; I was the one asserting unverified things.**

**So: an unprompted write is a scope violation, NOT automatically wrong content.** Before reverting one, run the three checks — **(a)** does the artifact's claim actually hold (read it; don't infer a fabrication), **(b)** is it committed/**pushed** (`git log --all --`, `git branch -r --contains`), **(c)** do downstream consumers already reference it (another agent's inbox/ledger). If it's pushed and wired, reverting creates *more* inconsistency than leaving it. The reflex "a sub-agent did something I didn't authorize, therefore undo it" is itself an unverified-action hazard — [[feedback_verify_state_before_propagating]], [[feedback_evidence_standalone]]. Also note late returns: three sub-agents this parent declared "never reported" had in fact completed, and one **overturned its own parent's conclusion** — check for late arrivals before accepting a declared gap ([[finding_workflow_scratch_crash_recovery]]).
