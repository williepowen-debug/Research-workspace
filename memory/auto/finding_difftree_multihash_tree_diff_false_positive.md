---
name: finding_difftree_multihash_tree_diff_false_positive
description: git diff-tree with two commit hashes diffs TREE-to-TREE (sweeps in interleaved foreign commits) — use per-commit `git show --name-only` for scope gates; error class = false alarms only
metadata:
  type: reference
---

`git diff-tree --no-commit-id --name-only -r <A> <B>` does NOT list "files touched by commits A and B" — it diffs A's tree against B's tree, so every commit landed *between* them (by anyone) appears in the output. In a shared repo with concurrent agent writers this makes multi-hash diff-tree scope checks fire false positives: on 2026-07-12 a HOMER two-commit check "showed" WATT files because WATT's commit sat between HOMER's two.

**Correct scope-gate:** per commit, `git show --name-only --oneline <hash> | tail -n +2 | grep -v '^AGENTS/<NAME>/'` (empty = clean). One hash per invocation.

**Error-class asymmetry (why past verdicts stood):** the mistake only ADDS foreign files to the output — it can produce false alarms, never false accepts. Any CLEAN verdict from the multi-hash form remains valid; only non-clean results need re-checking per commit.
