---
name: project-automem-symlink-migration
description: Auto-memory symlink migration in active testing as of 2026-06-05; Will is iterating on the symlink-based scheme that makes the per-project memory dir git-trackable via memory/auto/ in the repo
metadata: 
  node_type: memory
  type: project
  originSessionId: 79f62375-9180-4c8c-8406-2e35dcc0fe6e
---

Will is actively working on the auto-memory symlink migration. Testing began 2026-06-05.

**Why:** Per-project memory at `~/.claude/projects/-home-willi-Research-workspace/memory/` is outside the repo by default. Symlink approach makes it reachable from `memory/auto/` in the working tree so memory edits commit alongside code changes and sync across sessions/machines via git.

**How to apply:**
- Treat memory tooling as in-flux for now — don't assume the layout is stable
- The untracked `memory/auto/MEMORY.md` + `memory/auto/feedback_*.md` files in the working tree (visible in git status) are part of this migration, not stray files to clean up
- If asked about symlink wiring, index generation, or memory-dir routing, check `memory/auto/` and the tooling commits (recent: 59dfdf7b, 8d8f71e4) before opining
- Related: [[finding-walter-refactor-pattern]] for sequenced-pass refactor discipline if migration grows multi-file
