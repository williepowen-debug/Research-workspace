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

Agent sessions keep reading/writing at the same harness path; the bytes live in
`memory/auto/`, so every change is versioned and reconciled through git like any
other file. Claude Code follows symlinks for memory transparently, so this is a
documented, supported pattern — not a hack.

> The known symlink issue (CLAUDE.md parent-discovery when the *working
> directory itself* is symlinked) does **not** apply here: the repo cwd is a
> real directory; only the `memory/` subdir is symlinked.

## Before you start — pre-flight

1. **Close all Claude sessions on both machines.** The migration moves and
   re-links the memory dir; a live session writing mid-migration can race it.
   (`link_automemory.sh` refuses to `--apply` if it sees a running `claude`
   process; `--force` overrides.)
2. **Count files on each machine** so you know the divergence you're merging:
   ```bash
   ls ~/.claude/projects/<slug>/memory/*.md | wc -l
   ```
   If desktop = 80 and laptop = 60, expect ~20 laptop-only files to capture plus
   possibly some files edited on both. **Budget ~30 min for the second-machine
   reconciliation** — that's the highest-friction step.

## One-time setup, per machine

Run on the **desktop first**, then the **laptop**. Dry-run by default; nothing
changes until `--apply`.

```bash
# 1. Preview (safe, changes nothing):
bash scripts/link_automemory.sh

# 2. Apply (backs up first, then re-links):
bash scripts/link_automemory.sh --apply

# 3. Commit the captured memories (let the harness keep curating MEMORY.md):
git add memory/auto
git diff --cached --stat        # verify: ONLY memory/auto/* staged
git commit -m "auto-memory: capture from <machine>"
git pull --rebase && git push
```

On the **second machine**, `git pull` first so the store already holds the first
machine's memories; the script then folds in this machine's local memories on
top, copying any genuinely-different same-named file aside as
`*.conflict-<host>-<ts>.md` for you to merge by hand.

What `--apply` does, safely:
- **Backs up** the existing harness dir to
  `~/.claude/automemory-migration-backup-<host>-<ts>/` before touching anything.
- **Captures** every local memory file not already in the store.
- **Never overwrites**: a same-named file whose contents differ is copied aside
  and reported.
- Replaces the dir with the symlink, then verifies both a **read** and a
  filesystem-level **write** through the link.

### Verifying the write path (the load-bearing assumption)

The script's write check only proves the *OS* follows the symlink — not that
*Claude Code* writes through it. Do the real test once after the first
`--apply`:

> Start an agent session, have it save a test memory, then run `git status`.
> The new file should appear under `memory/auto/`. If it does, the write path
> works end-to-end. If not, switch to the fallback below.

### Verifying the slug

The `<slug>` is the repo's absolute path with `/` → `-` (so
`/home/willi/Research-workspace` → `-home-willi-Research-workspace`). The script
derives it automatically; if the printed `harness:` path doesn't match an
existing dir, run `ls ~/.claude/projects/` to confirm the exact slug (usernames
/ paths can differ between machines).

## Working with two machines simultaneously

You sometimes run agents on both machines at once, so the rules keep conflicts
rare and trivial:

1. **New memory = new file** with a stable, semantic name. Two machines almost
   never create the *same* new filename at the same instant; if they do, it's an
   ordinary git conflict.
2. **Editing an existing memory = append, don't rewrite.** Add a dated bullet
   (e.g. "**+ 2026-06-05 (BRENT):** new corroborating case …") rather than
   reflowing the file. Appends at different points auto-merge.
3. **Let the harness own `MEMORY.md`.** The Claude Code harness maintains this
   index itself, adding a curated one-line entry when an agent saves a memory.
   Don't auto-regenerate it. If a cross-machine merge conflicts on `MEMORY.md`,
   resolve by hand: **keep both sides' entries, then dedup** — if both machines
   added a pointer to the *same* `[[topic-file]]`, collapse it to one line.
4. **`git pull --rebase` before push** (already the repo protocol).

**Failure mode to know:** if both machines edit the **same memory file body**
before either pushes (rare — e.g. you start on desktop, move to laptop, both
touch the same file), git will flag a normal merge conflict *inside that file*
on push. Resolution is manual: open the file, resolve the `<<<<<<<` markers,
re-commit. The append-don't-rewrite rule (#2) makes this nearly never happen.

## Writing memory files — the `symptoms:` line (Will-approved 2026-08-21, Batch A)

New or extended memory files carry a `symptoms:` frontmatter line — grep-bait
phrasings of how the problem presents (e.g. "script always exits 0") — and
searches grep bodies, not just indexes. Forward-only: the existing corpus is not
retro-edited. (Provenance: the memory-retrieval design, PROME `5c66ea63b` →
DAEDALUS dispositions `1e1067253`; the companion cross-index was DECLINED with a
pre-registered re-open trigger — ≥3 false-"searched, novel" claims in a month.)

## The index (`MEMORY.md`) — the harness owns it

`MEMORY.md` is the lean, **always-loaded** index — the harness loads only the
first ~200 lines / 25 KB at boot; topic files load on demand. **The Claude Code
harness maintains this file itself**: when an agent saves a memory it also writes
a curated one-line entry into `MEMORY.md`. We confirmed this live during
migration (a test memory produced both a new `project_*.md` file *and* an updated
`MEMORY.md`).

So we deliberately **do not auto-generate or auto-regenerate the index** — doing
so would strip the harness's curated entries on every commit, and they'd just be
re-added next session (the two would fight each other). Let the harness curate it.

`scripts/gen_automemory_index.py` is kept **only as a manual repair tool** — for
the rare case where `MEMORY.md` gets badly mangled (e.g. an ugly merge conflict)
and you'd rather rebuild a mechanical index from the topic files than hand-fix
it. It is **not** part of the normal flow and there is **no pre-commit hook**.

### Watch the boot-load cap (silent-truncation risk)

Because only the first ~200 lines / 25 KB load at boot, an index that grows past
that **silently drops its tail** — those entries stop loading, with no warning.
Today the index has comfortable headroom (~81 lines), but it accumulates over
time, so catch drift early rather than at the cliff:

```bash
scripts/check_memory_length.sh        # warns at 180 lines, critical at 200
```

Run it at session end, or wire it as a periodic Prome chore. When it warns,
consolidate or retire low-value memories (or split a topic into its own file).

## Existing references keep working

~30 agent docs cite memories via the harness path and via `[[wikilink]]`
markers. After symlinking, that path still resolves (it's now the symlink) and
the wikilinks still name real files, so **no agent docs need editing**.

## Security — what must never go in auto-memory

Auto-memory now lives in **git history, which is permanent**. The repo is
**private** (confirmed June 2026 — `visibility: private`), so this is not public
exposure — but treat every memory file as readable by anyone with repo access,
forever, and uneraseable from history.

**Never write into a memory:** API keys, tokens (Telegram / broker / etc.),
passwords or logins, live account or position dollar amounts, or personal data.
Memories are process/workflow lessons — *how to work* — not a place for secrets
or live numbers. Reinforce **"no secrets / no live PII in memories"** in agent
prompts. Note: `.gitignore` blocks `*secret*`, `*token*`, `*.key`, `.env`, but a
normal memory file won't match those patterns — so this guardrail is **discipline,
not the filter.**

## Fallback (designed and ready, not deployed)

If a future Claude Code version stops following the symlinked memory dir, switch
to hook-based sync — **do not run it alongside the symlink; pick one.** Scripts
are in `scripts/fallback/`:

- `session_start_sync.sh` — SessionStart hook: pull, then mirror repo → harness.
- `stop_sync.sh` — Stop hook: mirror harness → repo, commit & push (no index regen).

Wire them in `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [{ "hooks": [{ "type": "command", "command": "bash scripts/fallback/session_start_sync.sh" }] }],
    "Stop":         [{ "hooks": [{ "type": "command", "command": "bash scripts/fallback/stop_sync.sh" }] }]
  }
}
```

A configurable memory location is also an open Claude Code feature request
(anthropics/claude-code#28276). If it ships, point it at `<repo>/memory/auto`
and drop the symlink.

## Root `CLAUDE.md` amendment — ✅ **RATIFIED 2026-07-27 (Will-approved, applied by BROCK)**

> **STATUS: APPLIED.** This is now **carve-out ③** in root `CLAUDE.md` § Git Protocol; the
> count there reads "the ONLY **three**." The section below is kept as the original proposal
> and its rationale — **the live rule is the one in root `CLAUDE.md`, not this draft.**
>
> **Three changes were made to the suggested wording when applying it:**
> 1. **Mechanism made neutral.** The draft says "git-synced via a per-machine **symlink**."
>    On the machine where this was ratified, `memory/auto/` is a **real directory whose files
>    are hardlinked** to the harness path (verified by inode: `MEMORY.md` = 351667 in both
>    locations). Symlink and hardlink migrations are both described in this doc, so the
>    ratified text says "git-synced to the harness memory path (mechanism → this doc)" rather
>    than baking in a machine-specific detail that would read as false on the other box.
> 2. **Permission upgraded to an obligation** — "may … **and you must**", matching carve-out ①.
>    Permitting the commit does not fix anything if nobody performs it; the failure being
>    fixed is *omission*, not prohibition.
> 3. **Enforcement + a trap added.** The ratified text points at
>    `scripts/memory_index_check.py --strict` (exit 1 on a pointer git will not ship) and
>    warns that **`orphan_check.sh` cannot cover this** — it classifies by PATH, so every file
>    under `memory/auto/` reads `[not yours]` regardless of authorship.
>
> **What forced it:** 2026-07-27 — **six orphaned memories from four agents in one day**, with
> three more appearing while the first three were being fixed. WALTER, VIOLET and BROCK each
> detected the same defect independently within hours.

The root git protocol says agents `git add` only their own `AGENTS/<NAME>/` dir
and flag shared files to Prome. `memory/auto/` is a new shared, **append-only**
zone, so it needs an explicit carve-out. Two sub-decisions for the wording:

- **Who writes?** Auto-memory is harness-level, not agent-scoped, so **any agent
  session** should be allowed to add memory files — not just one agent.
- **Self-commit vs flag-to-Prome?** Recommend **self-commit-permitted**:
  routing every memory write through a Prome approval-gate would defeat the
  point of auto-memory. (Prome can stay aware via the heartbeat.)

Suggested wording to add under "Git Protocol":

> **Auto-memory (`memory/auto/`)** is a shared, append-only zone, git-synced via
> a per-machine symlink (see `docs/AUTO_MEMORY.md`). **Any** agent session may
> `git add` and self-commit files **inside `memory/auto/`** that it created or
> appended to — no Prome approval-gate. **This permission is scoped to
> `memory/auto/` ONLY and must not be cited as precedent for any other shared
> directory** — HEARTBEAT, FORGE, and all other shared files still follow the
> flag-to-Prome rule. `MEMORY.md` is the harness's curated index — don't
> regenerate it; on a cross-machine conflict, keep both entries and dedup by
> topic-file slug. Prefer new files over rewrites; append dated bullets when
> adding to an existing memory.

~~I did not edit `CLAUDE.md` myself — it's the governing shared doc, so it's left
for you (or Prome) to apply.~~

**Superseded 2026-07-27:** Will directed the amendment be applied; BROCK applied it to root
`CLAUDE.md` as carve-out ③ that day. PROME (owner of root `CLAUDE.md`) and WALTER (author of
both this doc and `memory_index_check.py`) were notified by packet the same session.
