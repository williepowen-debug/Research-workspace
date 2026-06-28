---
name: automem-hardlink-inplace-edit
description: "memory/auto/ files are hardlinked to the loaded ~/.claude memory index (same inode); edit MEMORY.md in-place via shell >/>> to preserve the inode — a rename-replace write breaks the hardlink and the loaded copy goes stale."
metadata:
  node_type: memory
  type: finding
  originSessionId: e6ba185e-df2d-4315-a224-788f942d6823
---

The in-repo `memory/auto/MEMORY.md` and the loaded `~/.claude/projects/<project>/memory/MEMORY.md` are the **same inode** (hardlinked — verified inode 86976 on Jun 27 2026), and likewise for the topic files. So a write to one updates the other, which is how an in-repo edit reaches the index that actually loads at boot. But this only holds if the write is **in-place** (truncate + write). A tool or command that writes-to-temp-then-renames (the typical `Write`/atomic-save pattern) creates a **new inode** and repoints only the directory entry you wrote — the other hardlink keeps the old inode, so the two copies silently diverge and the loaded copy stays stale.

**Why:** `>`/`>>` redirection opens the existing file with `O_TRUNC`/`O_APPEND` and writes into the existing inode, preserving every hardlink. Rename-replace (`mv tmp dest`) unlinks the old entry and points the name at a fresh inode, severing the hardlink for that path only.

**How to apply:** (1) To rewrite the index, compose to a scratch file then `cat scratch > memory/auto/MEMORY.md` (belt-and-suspenders: also `>` the `~/.claude` path); verify the inode is unchanged (`stat -c %i`). (2) To append entries, use `>>`. (3) To **prune** a topic file, remove **both** directory entries (the `memory/auto/` copy AND the `~/.claude/.../memory/` copy) — removing one leaves the inode alive via the other. (4) To **add** a new memory, write it then `ln` the second path so both locations share the inode (loaded AND git-tracked). Relates to [[project_automem_symlink_migration]] and [[finding_workflow_subagent_repo_sandbox]].
