# Auto-Memory Migration — Pre-Flight Checklist

Keep this open next to the terminal. Run on the **Ubuntu terminal where your
agents live** (same machine, same user). **Desktop first, fully — including the
load-bearing test — before you touch the laptop.** Each step has a verify; don't
skip the verify. Full background: `docs/AUTO_MEMORY.md`.

---

## 0. Pre-flight (both machines, before anything)

```bash
# Count existing memories on this machine — write the number down.
ls ~/.claude/projects/<slug>/memory/*.md | wc -l        # desktop: ___  laptop: ___
# <slug> = your repo path with / replaced by - (e.g. -home-willi-Research-workspace).
# If unsure, run:  ls ~/.claude/projects/   and use the folder you see.

# See what the actual Claude process is called (the script's guard is best-effort).
ps -ef | grep -i claude | grep -v grep
```

**Close ALL Claude sessions on this machine — including any Telegram/WALTER
session. Actually exit the process; do NOT just `/clear`.** A live session can
make the script refuse (its guard), or race a memory write mid-migration.

---

## 1. Desktop — setup

```bash
cd ~/Research-workspace
git pull                                  # brings in scripts/, memory/auto/, docs/

bash scripts/link_automemory.sh           # DRY RUN — changes nothing
#   VERIFY: "harness:" path matches an existing dir
#           "store:" is <repo>/memory/auto
#           "mode: dry-run"
#           NO "WARNING: a 'claude' process appears to be running"
#           your existing memories listed as "+ capture new"

bash scripts/link_automemory.sh --apply   # backs up first, then links
#   VERIFY: "Backing up original harness dir -> ~/.claude/automemory-migration-backup-..."
#           "Linked: <harness> -> <store>"
#           "Verify OK (read)"  and  "Verify OK (write): filesystem write-through confirmed"
```

---

## 2. Load-bearing test (desktop only, BEFORE the laptop)

This is the one test that proves the harness itself writes through the symlink.

```bash
# In a NEW Claude session, say:  "Remember: testing auto-memory symlink on <date>."
# Let it save the memory (it will name a file). Exit the session, then:
git status memory/auto/
```

- **New file appears under `memory/auto/` → PASS.** Continue to step 3.
- **Nothing new → STOP.** Do not proceed. Roll back (see bottom), then switch to
  the fallback in `scripts/fallback/` (`docs/AUTO_MEMORY.md` → "Fallback").
- **Either way, tell WALTER the result** (paste the `git status` output).

---

## 3. Desktop — finalize (only if the test passed)

Let the harness keep curating `MEMORY.md` — no hook, no generator.

```bash
git add memory/auto
git diff --cached --stat                  # VERIFY: ONLY memory/auto/* staged.
                                          # If anything else: git restore --staged <file>
git commit -m "auto-memory: capture from desktop (git-synced via symlink)"
git pull --rebase && git push
```

---

## 4. Laptop — second machine (AFTER desktop is pushed)

```bash
# Close all Claude sessions on the laptop first.
cd ~/Research-workspace
git pull --rebase                         # gets desktop's memories FIRST

bash scripts/link_automemory.sh           # dry run
#   VERIFY: same as step 1, PLUS "! COLLISION" lines for files that differ from desktop.
#           (# of collisions = your manual-merge budget, ~5 min each.)

bash scripts/link_automemory.sh --apply
#   VERIFY: "ACTION NEEDED — N file(s) differ ..." each kept as *.conflict-<host>-<ts>.md

# Merge each collision by hand:
ls memory/auto/*.conflict-*.md
#   For each: diff it against the original, fold any laptop-side additions into the
#   original (append-don't-rewrite), then delete the .conflict file.
#   NOTE: MEMORY.md may itself be a collision — if so, keep BOTH machines'
#   entries, then dedup any duplicate pointers to the same topic file. It's the
#   harness's curated index; don't regenerate it.

git add memory/auto
git diff --cached --stat                  # VERIFY: only memory/auto/* staged
git commit -m "auto-memory: merge from laptop"
git pull --rebase && git push
```

---

## 5. Post-setup — CLAUDE.md carve-out

```text
# Read the proposed wording: docs/AUTO_MEMORY.md (last section). Decide:
#   (a) any agent session may write?         Recommended: YES
#   (b) self-commit vs PROME-gate?           Recommended: SELF-COMMIT
#   (c) scope-lock: permission applies to memory/auto/ ONLY, not a precedent
#       for other shared dirs (HEARTBEAT/FORGE keep the flag-to-Prome rule).
# Add the carve-out paragraph under "Git Protocol" in CLAUDE.md (or route via PROME).
# Commit: "carve-out: memory/auto/ shared-zone permission"
```

---

## Rollback — if anything goes wrong at any step

```bash
# Use the harness path the script printed (slug differs per machine).
HARNESS=~/.claude/projects/<slug>/memory
BACKUP=$(ls -dt ~/.claude/automemory-migration-backup-* | head -1)
rm "$HARNESS"                 # removes the symlink
cp -a "$BACKUP" "$HARNESS"    # restores the pre-migration real dir
# Back to the original state; sessions write to the real dir again.
# Do NOT delete the backup until you're confident the new setup works.
# (Note: a memory written via the symlink during testing lives in memory/auto/,
#  not in the backup — harmless for a throwaway test memory.)
```
