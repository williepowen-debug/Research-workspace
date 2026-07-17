---
name: automem-hardlink-inplace-edit
description: "auto-memory link model UPDATED — ~/.claude/.../memory is now a DIRECTORY SYMLINK to the git-tracked memory/auto/ (not per-file hardlinks); the Write tool is safe and the old in-place-edit requirement is superseded. Slug kept for continuity."
metadata:
  node_type: memory
  type: finding
  originSessionId: e6ba185e-df2d-4315-a224-788f942d6823
---

**Superseded 2026-07-01 (verified).** The auto-memory link model changed. `~/.claude/projects/<project>/memory/` is now a **directory symlink** to the canonical git-tracked `memory/auto/` — `readlink` confirms the symlink, and `MEMORY.md` shows `nlink=1` (inode 52899). It is **no longer per-file hardlinks** (the Jun-27 state this finding originally documented, inode 86976).

**What this means now:** both paths resolve to the *same file via one directory*, so **any write tool is safe** — an atomic `Write` (write-temp-then-rename) to `memory/auto/X.md` is immediately visible at `~/.claude/.../memory/X.md` because it *is* the same directory. The old guidance — "edit in-place with `>`/`>>` to preserve the inode, `ln` the second path for new files, remove both directory entries to prune" — **no longer applies**; it was correct only under the pre-migration hardlink model.

**Why the change is safe:** a directory symlink resolves at path-lookup time, so it always points at the current file regardless of atomic rename. There is no second hardlinked inode to desync.

**How to apply (current):** write / edit / create / delete `memory/auto/` files with normal tools (the `Write` and `Edit` tools are fine); the symlink makes the `~/.claude` load path track them automatically. A **new** memory file needs a `memory/auto/MEMORY.md` index pointer + a git commit — and note these live **outside `PROME/`**, so commit them explicitly at closeout (see `PROME/CLOSEOUT.md` Chunk 4). *(Absorbed [[project_automem_symlink_migration]] 2026-07-17, Will-approved — that slug is now a tombstone anchor; `docs/AUTO_MEMORY.md` is the canonical doc.)*

*(Filename/slug retained for reference-continuity; the "hardlink" in the name is historical.)*
