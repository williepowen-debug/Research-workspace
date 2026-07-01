---
name: feedback_defer_push_coordinate
description: Push is automated at closeout via ff-gated safe-push.sh (serial multi-machine) — pathspec commit, let safe-push sweep the train; non-ff abort = routine rebase, escalate only on simultaneous-use signatures
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 00ec0950-e775-4a07-8003-3c090c4b2848
---

**UPDATED 2026-07-01 — premise corrected to SERIAL MULTI-MACHINE (Will).** Will runs desktop ⇄ laptop, ONE machine at a time: every agent closed out (= pushed) before switching, so origin is always the handoff point. This replaces both the pre-6/26 manual "defer push" ceremony and the 6/26 "single-machine" framing. Machine-local infra (creds, timers, venv) does NOT travel — that's `PROME/MACHINE_LOCAL.md`'s inventory, a separate concern from git safety.

**Why the safety model holds:** the genuine hazard was always **simultaneous** cross-machine pushes (the old OpenClaw/VPS case). Serial use eliminates it by construction. Same-machine multi-session concurrency is handled by git serialization + the push-train (one push sweeps everyone's local commits — a *feature*). `safe-push.sh` still never force-pushes and **aborts cleanly if origin has commits we don't** — under serial multi-machine that abort usually just means "the other box pushed since this clone last pulled."

**How to apply:** at session end, commit with **pathspec from repo root** (`cd "$(git rev-parse --show-toplevel)"` first — pathspecs are cwd-relative; from an own-dir launch cwd, `git status -- AGENTS/<NAME>/` SILENTLY false-passes; root CLAUDE.md "Before committing" step 0). Never `git reset HEAD` or `git add <dir>` ([[finding_pathspec_commit_race_safety]]). Then safe-push as the closeout tail. **Non-ff abort → do NOT force; `git pull --rebase` + re-push (routine).** Escalate to Will (per-agent-branches tripwire) ONLY on out-of-own-dir rebase conflicts or mid-session recurrence — signatures of two machines running at once, which the protocol forbids ([[finding_two_machine_partition_clean_merge]], [[finding_forced_update_rebase_churn]]). Exceptions: **YEYOU** manual/branch (reviewer model). See [[finding_push_train_pattern]].
