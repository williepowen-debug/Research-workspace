---
name: project-automem-symlink-migration
description: Auto-memory is wired into the repo at memory/auto/ (migration complete/stable since ~2026-06-05); memory edits commit alongside code and sync via git
metadata: 
  node_type: memory
  type: project
  originSessionId: 79f62375-9180-4c8c-8406-2e35dcc0fe6e
---

Auto-memory symlink migration is **COMPLETE and stable** (live since ~2026-06-05). Kept as an anchor for docs that reference it ([[project_messaging_overhaul]] and HENRY/CARL planning docs).

**Why:** Per-project memory at `~/.claude/projects/-home-willi-Research-workspace/memory/` is outside the repo by default. The in-repo mirror at `memory/auto/` makes memory edits commit alongside code and sync across sessions/machines via git.

**How to apply (current reality):**
- The layout is **stable** — `memory/auto/*.md` are normal tracked files; the index is `memory/auto/MEMORY.md`. (Superseded the earlier "in-flux / don't assume stable" guidance.)
- Daily logs go in `memory/YYYY-MM-DD.md`; durable lessons in `memory/auto/<slug>.md` + a one-line index entry.
