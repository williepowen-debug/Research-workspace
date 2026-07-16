---
name: subdir-launch-hooks-dont-fire
description: Claude Code hooks (SessionStart etc.) configured in the repo-root .claude/settings.json do NOT execute for sessions launched from subdirectories (CC bug
metadata: 
  node_type: memory
  type: project
  originSessionId: af89c537-8ddb-4b88-9a9c-599c7a687961
---

**Finding (2026-07-16, PROME banner-hook debug):** The SessionStart boot banner (built 7/6, root `.claude/settings.json`) never fired across 7 sessions. Script verified fine (manual rc=0); config in the documented location. Root cause = Claude Code bug [#10367] "Hooks Completely Non-Functional in Subdirectories" (closed as not-planned, still present in CC 2.1.211): hooks don't execute when `claude` launches from a repo subdirectory — which the fleet protocol REQUIRES (`cd AGENTS/<NAME>/ && claude` to auto-load local CLAUDE.md).

**Why:** CC keys the session's *project* to the launch cwd, not the git root — evidence: session scratchpad/project IDs are keyed `-Research-workspace-PROME`, and CC writes `settings.local.json` into `PROME/.claude/`. Root-level hook config is loaded-per-docs but not executed per the bug.

**How to apply:** Any hook meant to fire for an agent session must live in (or be mirrored into) the LAUNCH DIRECTORY's own `.claude/settings.json` (e.g. `PROME/.claude/settings.json` — fix attempt 1, commit `e580462f`, verify at next PROME boot). If that verifies, fleet-wide propagation = per-agent-dir `.claude/settings.json` mirrors (DAEDALUS/Will decision). Fallback candidate: user-scope `~/.claude/settings.json` (machine-local, → [[machine-local]] inventory concerns per `PROME/MACHINE_LOCAL.md`). Never conclude "the hook script is broken" without running it manually first — [[finding_verify_runtime_context_before_tool_broken]].
