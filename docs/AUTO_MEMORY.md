# Auto-Memory — git-synced across machines

## The problem this solves

Claude Code auto-memory lives at a harness path **outside the repo**:
`~/.claude/projects/<repo-path-slug>/memory/`. It is auto-loaded at every agent
boot. Because it is outside git, it never pulls/pushes/merges — so when agents
run on more than one machine (desktop **and** laptop), each machine grows its
own divergent memory that no other machine can read or merge.

Everything else in this system already solves "keep all machines in sync" via
git ("GitHub is the single source of truth"). This brings auto-memory under the
same umbrella.

## The fix: symlink the harness dir into the repo

The harness path becomes a **symlink** to an in-repo store:

```
~/.claude/projects/<slug>/memory   ->   <repo>/memory/auto
```

Claude keeps reading/writing at the same harness path; the bytes live in
`memory/auto/`, so every change is versioned and reconciled through git like any
other file. Claude Code follows symlinks for memory transparently, so this is a
documented, supported pattern — not a hack.

> The known symlink issue (CLAUDE.md parent-discovery when the *working
> directory itself* is symlinked) does **not** apply here: the repo cwd is a
> real directory; only the `memory/` subdir is symlinked.

## One-time setup, per machine

Run on the **desktop first**, then the **laptop**. The script is dry-run by
default and changes nothing until you pass `--apply`.

```bash
# 1. From inside the repo, preview what will happen:
bash scripts/link_automemory.sh

# 2. If the plan looks right, apply it:
bash scripts/link_automemory.sh --apply

# 3. Refresh the lean index and commit the captured memory:
python3 scripts/gen_automemory_index.py
git add memory/auto
git commit -m "auto-memory: capture from <machine>"
git pull --rebase && git push
```

On the **second machine**, `git pull` first so the store already holds the first
machine's memories; the script then folds in the second machine's local
memories on top.

What `--apply` does, safely:
- **Backs up** the existing harness dir to
  `~/.claude/automemory-migration-backup-<host>-<ts>/` before touching anything.
- **Captures** every local memory file not already in the store.
- **Never overwrites**: a same-named file whose contents differ is copied aside
  as `*.conflict-<host>-<ts>.md` and reported, so you merge it by hand.
- Replaces the dir with the symlink and verifies it reads through.

### Verifying the slug

The `<slug>` is the repo's absolute path with `/` → `-` (so
`/home/willi/Research-workspace` → `-home-willi-Research-workspace`). The script
derives it automatically, but if the printed `harness:` path doesn't match a dir
that already exists, run `ls ~/.claude/projects/` to confirm the exact slug for
that machine (usernames/paths can differ between desktop and laptop).

## Working with two machines simultaneously

You said agents sometimes run on both machines at once, so the rules are built to
make conflicts rare and trivial to resolve:

1. **New memory = new file.** A new `feedback_*/finding_*/project_*.md` with a
   stable, semantic name. Two machines almost never create the *same* new
   filename at the same instant; if they do, it's an ordinary git conflict.
2. **Editing an existing memory = append, don't rewrite.** Add a dated bullet
   (e.g. "**+ 2026-06-05 (BRENT):** new corroborating case …") rather than
   reflowing the file. Appends at different points auto-merge; only same-line
   rewrites conflict.
3. **Never hand-edit `MEMORY.md`.** It is generated. If git ever flags a
   conflict on it, take either side and just re-run
   `python3 scripts/gen_automemory_index.py` — the output is deterministic from
   the topic files present.
4. **Standard git discipline still applies:** `git pull --rebase` before push
   (already the repo protocol). Memory additions are append-only by design, so
   rebases land cleanly in the common case.

## Why the index is generated and must stay lean

Claude Code loads only the **first ~200 lines / 25 KB of `MEMORY.md`** at boot;
topic files are read on demand. So `MEMORY.md` is a terse one-line-per-entry
index produced by `scripts/gen_automemory_index.py`. The generator warns if the
index approaches the load cap — that's your signal to consolidate or retire
low-value entries.

## Existing references keep working

~30 agent docs cite memories via the harness path
`~/.claude/projects/-home-willi-Research-workspace/memory/` and via `[[wikilink]]`
markers. After symlinking, that path still resolves (it's now the symlink) and
the wikilinks still name real files, so **no agent docs need editing**.

## Troubleshooting / fallback

- **Harness recreates a real `memory/` dir over the symlink on boot.** If a
  future Claude Code version does this (it currently doesn't), switch to the
  hook-based variant: a `SessionStart` hook copies `memory/auto/` → harness path,
  a `Stop` hook copies back and commits. Same git-sync outcome without a symlink.
- **A configurable memory location** is an open Claude Code feature request
  (anthropics/claude-code#28276). If it ships, point it straight at
  `<repo>/memory/auto` and drop the symlink.

## Proposed root `CLAUDE.md` amendment (needs Will's review)

The root git protocol says agents `git add` only their own `AGENTS/<NAME>/` dir
and flag shared files to Prome. `memory/auto/` is a new shared, **append-only**
zone, so it needs an explicit carve-out. Suggested wording to add under "Git
Protocol":

> **Auto-memory (`memory/auto/`)** is a shared, append-only zone, git-synced via
> a per-machine symlink (see `docs/AUTO_MEMORY.md`). Any agent may `git add`
> auto-memory files **it created or appended to**. Never hand-edit `MEMORY.md`
> (generated — re-run `scripts/gen_automemory_index.py`). Prefer new files over
> rewrites; append dated bullets when adding to an existing memory.

I did not edit `CLAUDE.md` myself — it's the governing shared doc, so it's left
for you (or Prome) to apply.
