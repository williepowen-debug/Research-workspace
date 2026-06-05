---
name: shallow-clone-false-fork
description: Web/CC session containers clone shallow — git merge-base then falsely reports unrelated histories + huge divergence; unshallow before trusting ahead/behind
metadata: 
  node_type: memory
  type: finding
  originSessionId: 9fe6fa60-1e2d-4ddd-baf5-e13312cf2917
---

Claude-Code web-session containers (and some CC environments) clone the repo **shallow** (a `.git/shallow` graft file is present). When shallow, `git merge-base` / `git rev-list --left-right` falsely report **NO common ancestor + massive divergence** — e.g. "53 ahead / 50 behind, unrelated histories" when the branch is really just **3 ahead / 1 behind** master. This reads as an alarming fork that isn't real.

**Fix:** at boot, before trusting ANY ahead/behind, merge-base, or divergence reading:
```
git rev-parse --is-shallow-repository
# if true:
git fetch --unshallow origin
```
Then re-run the comparison. Don't panic at apparent forks in web/CC sessions — verify the clone depth first.

**Why:** first hit 2026-05-28 during a SAM branch/PR resolution — the "false fork" nearly triggered an unnecessary reconciliation. Transferable to any agent/session in a shallow container. Relates to [[feedback_verify_counts_before_propagating]] (verify ground truth before acting on a scary-looking state reading).
