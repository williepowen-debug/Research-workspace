---
name: feedback_defer_push_coordinate
description: Push is automated at closeout via ff-gated safe-push.sh (single-machine) — commit with pathspec, then let safe-push sweep the train; abort-on-non-ff is the cross-machine tripwire
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 00ec0950-e775-4a07-8003-3c090c4b2848
---

**UPDATED 2026-06-26 — policy flipped from manual "defer push" to auto-push.** The OpenClaw/VPS 2nd machine was cut 2026-06-26, removing the cross-machine non-ff hazard that the manual-coordination ceremony existed to guard against. Push is now **automated at closeout** via `scripts/safe-push.sh` (ff-gated, fails safe). This now **AGREES with** root `CLAUDE.md` Git Protocol (both say auto-push at closeout) — the old "this overrides root" inversion is retired.

**Why the ceremony existed (history, still the safety model):** Concurrent agents share ONE working tree and ONE branch. The genuine hazard was always **cross-MACHINE** non-ff races — origin moving under us while a 2nd machine (the VPS) pushed. Same-machine multi-session concurrency is handled by git serialization + the push-train (one push sweeps everyone's local commits — a *feature*, not a bug). `safe-push.sh` encodes the safety: it never force-pushes, never pulls a shared tree, and **aborts cleanly if origin has commits we don't**. So even if a 2nd machine ever returns, auto-push degrades to a clean refusal, not corruption. (Validated 2026-06-08: CARL's premature manual push during concurrent BROCK/HAWK/PROME work was the failure mode the *manual* model couldn't prevent but ff-gated safe-push does.)

**How to apply:** At session end, commit with **pathspec** (`git commit AGENTS/<NAME>/<file>`; new files `git add <specific files> && git commit <same files>`) — **never `git reset HEAD` or `git add <dir>`** ([[finding_pathspec_commit_race_safety]]). Then run `scripts/safe-push.sh` as the closeout tail (or let your wired closeout call it). **If it aborts non-ff, do NOT force — flag Will; that's the 2nd-machine tripwire** ([[finding_forced_update_rebase_churn]]). Exceptions: **YEYOU** stays manual/branch (reviewer model); agents not yet lazy-swept simply commit-local and ride the next agent's auto-push. See [[finding_push_train_pattern]] + `PROME/AUTOPUSH_MIGRATION_PLAN.md`.
