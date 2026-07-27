---
name: dirty-path-means-in-flight-not-orphaned
description: "A file showing dirty in `git status` / `orphan_check.sh` says NOTHING about whether its content was delivered — the committed version may already be on origin while a live session edits it further. Never infer 'uncommitted therefore undelivered/not pushed'; check `git log -- <path>` and `git branch -r --contains` before flagging, and flag as 'in flight?' not 'orphaned'."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 0b528b89-85bc-49a3-9abf-522a627a8959
  modified: 2026-07-27T15:56:23.396Z
---

At closeout VIOLET ran `scripts/orphan_check.sh` and correctly did not sweep the `[not yours]` entries — but then **added an inference on top of the flag**: that `AGENTS/BRENT/outbox/2026-07-27_to-PROME_oil-collapse-adjudication.md` was "sitting uncommitted… the one that looks addressed to you."

**The memo was committed at `5db9f236` and verified on `origin/master`.** What the orphan check saw was BRENT's *current* closeout session — legitimately dirty LESSONS/STATUS/TRADE/CATALYSTS plus an **in-flight edit to that same already-delivered memo**. TERRY's check flagged the identical paths ten minutes earlier and drew the same wrong inference. **n=2 in one session, two agents independently.**

**Why the inference fails:** `git status` reports **working-tree divergence from HEAD**, which is a statement about *right now*, not about history. A path can simultaneously be (a) committed, (b) pushed to origin, and (c) dirty — that is the *normal* signature of a live session appending to a file it already delivered. "Uncommitted" and "undelivered" are different predicates, and the orphan tooling only measures the first. The failure is especially easy in a shared working tree, where every concurrently-running agent's in-progress work looks identical to abandoned work.

**How to apply:** when a dirty path outside your dir looks decision-relevant, spend one command before asserting anything about it:

```bash
git log --oneline -1 -- <path>              # does a committed version exist?
git branch -r --contains <hash>             # is that version on origin?
```

Then flag with the right predicate: **"dirty — possibly a live session, worth confirming"**, never "uncommitted, therefore not delivered." If a coordinator is orchestrating, assume dirty foreign paths are in-flight by default — it is the coordinator who knows which agents are running, and it costs them nothing to confirm. **A dirty path means "in flight" as often as "abandoned."**

The correct half of the behaviour still stands and should not be lost in the correction: **flag, never sweep.** The error was in the narration attached to the flag, not the flag itself.

Related: [[finding_concurrent_agents_one_box_is_supported]] · [[finding_stranded_commit_payload_retriage]] · [[feedback_agent_git_isolation]] · [[finding_push_train_pattern]] · [[finding_never_received_is_not_doesnt_hold]] · [[finding_terminated_notice_can_precede_delivery]]
