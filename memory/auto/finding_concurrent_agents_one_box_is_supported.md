---
name: concurrent-agents-one-box-is-supported
description: "Seeing ANOTHER agent's uncommitted changes in the shared working tree is NORMAL and expected — the 'serial, ONE at a time' rule is about MACHINES (desktop⇄laptop, which diverge origin), not about agents on one box. Do not escalate concurrent same-box agents to Will as a protocol violation; commit your own dir pathspec-scoped and let safe-push's ff-gate handle interleaving."
metadata:
  node_type: memory
  type: finding
---

Mid-session WALTER observed MARCO + CRUISE writing uncommitted changes in the shared working tree. Reading root-CLAUDE's *"defer push if you observe concurrent uncommitted foreign work"* literally, WALTER not only deferred its push (a fine conservative default) but **escalated it to Will as a "serial-single-machine VIOLATED" tripwire.** Will corrected it: running CRUISE / MARCO / WALTER concurrently from one terminal is **intended**.

A commit-scope audit confirmed the system worked exactly as designed — every agent committed **own-dir-only and pathspec-clean** (MARCO → `AGENTS/MARCO/` 20 files · CRUISE → `AGENTS/CRUISE/` 8 files · WALTER → WALTER + BOARD + delivery), the commits interleaved, and all **fast-forwarded to origin**. The push-train chained cleanly with zero conflicts.

**Why:** the "serial multi-machine, ONE at a time" language in root `CLAUDE.md` is about **MACHINES** — desktop ⇄ laptop, which genuinely diverge origin and can produce a non-ff push. It is **not** about agents on one box, which share a single `.git` and are the entire reason the pathspec-commit + shared-index discipline exists in the first place. Conflating the two turns the supported operating model into a false alarm, and costs Will an interrupt.

**How to apply:** treat another agent's uncommitted changes in the shared tree as **expected background state** — they will commit at their own closeout. Do not flag it, do not defer on it alone, do not escalate. Commit your own directory pathspec-scoped (`git commit AGENTS/<NAME>/…`) and push; `safe-push.sh`'s ff-gate handles interleaving. The **one** real guard for same-box concurrency is that each agent commits by **pathspec and never `git add -A`/`git add .`**, which would sweep a neighbour's files into your commit. Escalate only on the genuine machine-level tripwire: a non-ff abort that recurs after `git pull --rebase`, or rebase conflicts **outside your own directory**.

Related: [[finding_pathspec_commit_race_safety]] · [[finding_concurrent_commit_index_race]] · [[feedback_agent_git_isolation]] · [[finding_push_train_pattern]] · [[feedback_defer_push_coordinate]]
