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

**n+1 (2026-08-05, BRENT cloud EIA routine):** the misread escalated a level further — "BEHIND 50 / AHEAD 50, no common ancestor" was reported to PROME as a suspected **upstream force-push/history rewrite**. Desktop verification: the "stale" local master tip (`5df3377`) was an ordinary ancestor of HEAD, 886 commits back (a 7/30 cached container clone), and the local reflog of origin/master showed zero forced updates. **New tell: near-SYMMETRIC ahead/behind counts ≈ the fetch depth, not real divergence** — real concurrent-session divergence is almost never symmetric. A rewrite hypothesis needs one cheap check from any full clone: `git merge-base --is-ancestor <stale-tip> origin/master`. BRENT's local fix (`git checkout -B master origin/master`) was safe; nothing was wrong upstream.
