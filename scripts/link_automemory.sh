#!/usr/bin/env bash
# link_automemory.sh — make Claude Code auto-memory git-synced via symlink.
#
# Points THIS machine's harness auto-memory dir
#     ~/.claude/projects/<repo-path-slug>/memory
# at the in-repo store
#     <repo>/memory/auto
# so auto-memory pulls / pushes / merges through git like the rest of the system.
#
# SAFE BY DEFAULT: prints a plan and changes nothing. Pass --apply to execute.
# On --apply it backs up any existing harness memory dir BEFORE replacing it,
# and NEVER overwrites a differing memory file: collisions are copied aside as
# *.conflict-<host>-<ts>.md and reported for manual merge.
#
# Run once per machine (desktop, laptop). Idempotent.

set -euo pipefail

APPLY=0
FORCE=0
for a in "$@"; do
  case "$a" in
    --apply) APPLY=1 ;;
    --force) FORCE=1 ;;
    *) echo "unknown arg: $a (use --apply and/or --force)"; exit 2 ;;
  esac
done

canon() { ( cd "$1" 2>/dev/null && pwd -P ); }

REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
TARGET="$REPO_ROOT/memory/auto"
SLUG="${REPO_ROOT//\//-}"                       # /home/willi/X -> -home-willi-X
HARNESS="$HOME/.claude/projects/$SLUG/memory"
HOST="$(hostname -s 2>/dev/null || hostname)"
TS="$(date +%Y%m%d-%H%M%S)"
BACKUP="$HOME/.claude/automemory-migration-backup-$HOST-$TS"

echo "repo:     $REPO_ROOT"
echo "store:    $TARGET"
echo "slug:     $SLUG"
echo "harness:  $HARNESS"
echo "mode:     $([[ $APPLY -eq 1 ]] && echo APPLY || echo dry-run)"
echo
echo "NOTE: if 'harness' above doesn't match an existing dir, list ~/.claude/projects/"
echo "      to confirm the exact slug for this machine, then re-run."
echo

# Best-effort guard: refuse to migrate while a Claude session may be writing
# memory (avoids racing the move+symlink against an in-flight write). NOTE: this
# is best-effort only — Claude Code may run under node/electron and not match
# 'claude', so ALWAYS confirm sessions are closed manually too.
if command -v pgrep >/dev/null 2>&1 && pgrep -fi '[c]laude' >/dev/null 2>&1; then
  echo "WARNING: a 'claude' process appears to be running on this machine."
  echo "         Migrating now can race a mid-session memory write."
  if [[ $APPLY -eq 1 && $FORCE -eq 0 ]]; then
    echo "         Close all Claude sessions and re-run, or pass --force to override."
    exit 1
  fi
fi

mkdir -p "$TARGET"

# --- already linked correctly? -------------------------------------------------
if [[ -L "$HARNESS" ]]; then
  if [[ "$(canon "$HARNESS")" == "$(canon "$TARGET")" ]]; then
    echo "OK: harness memory already points at the repo store. Nothing to do."
    exit 0
  fi
  echo "WARNING: harness memory is a symlink to: $(readlink "$HARNESS")"
  echo "         That is not the repo store. Resolve manually; refusing to touch it."
  exit 1
fi

# --- reconcile an existing real dir into the repo store ------------------------
collisions=()
if [[ -d "$HARNESS" ]]; then
  echo "Found existing real memory dir — reconciling into the repo store:"
  while IFS= read -r -d '' f; do
    base="$(basename "$f")"
    dest="$TARGET/$base"
    if [[ ! -e "$dest" ]]; then
      echo "  + capture new : $base"
      [[ $APPLY -eq 1 ]] && cp -p "$f" "$dest"
    elif ! cmp -s "$f" "$dest"; then
      side="$TARGET/${base%.md}.conflict-$HOST-$TS.md"
      echo "  ! COLLISION   : $base  (kept as $(basename "$side"))"
      collisions+=("$base")
      [[ $APPLY -eq 1 ]] && cp -p "$f" "$side"
    else
      echo "  = identical   : $base"
    fi
  done < <(find "$HARNESS" -maxdepth 1 -type f -name '*.md' -print0)

  if [[ $APPLY -eq 1 ]]; then
    echo "Backing up original harness dir -> $BACKUP"
    cp -a "$HARNESS" "$BACKUP"
    rm -rf "$HARNESS"
  fi
fi

# --- create the symlink --------------------------------------------------------
if [[ $APPLY -eq 1 ]]; then
  mkdir -p "$(dirname "$HARNESS")"
  ln -s "$TARGET" "$HARNESS"
  echo "Linked: $HARNESS -> $TARGET"
  if [[ -d "$HARNESS" && -r "$HARNESS" ]]; then
    echo "Verify OK (read): harness path reads through to the repo store."
  else
    echo "Verify FAILED: harness path is not readable. Investigate before trusting it."
    exit 1
  fi
  # Filesystem-level write-through check. NOTE: this only proves the OS follows
  # the symlink — it does NOT prove Claude Code writes through it. Do the real
  # test next (see the script's closing notes).
  tw="$HARNESS/.write-test-$HOST-$TS"
  if echo ok > "$tw" 2>/dev/null && [[ -f "$TARGET/$(basename "$tw")" ]]; then
    rm -f "$tw"
    echo "Verify OK (write): filesystem write-through confirmed."
  else
    rm -f "$tw" 2>/dev/null || true
    echo "WARNING: filesystem write-through test failed — investigate before trusting it."
  fi
else
  echo
  echo "(dry-run) Re-run with --apply to perform the actions above."
fi

# --- report --------------------------------------------------------------------
if [[ ${#collisions[@]} -gt 0 ]]; then
  echo
  echo "ACTION NEEDED — ${#collisions[@]} file(s) differ between this machine and the repo:"
  printf '  - %s\n' "${collisions[@]}"
  echo "Each was preserved as *.conflict-$HOST-$TS.md in the store. Merge by hand, then delete the .conflict copy."
fi

echo
echo "Next:"
echo "  cd \"$REPO_ROOT\""
echo "  bash scripts/install_automemory_hook.sh         # auto-regen index on commit"
echo "  python3 scripts/gen_automemory_index.py          # refresh the lean index"
echo "  git add memory/auto"
echo "  git commit -m 'auto-memory: capture from $HOST'"
echo "  git pull --rebase && git push"
echo
echo "REAL write test (the load-bearing one): start a Claude session, have it save"
echo "a test memory, then 'git status' — the new file should appear under memory/auto/."
echo "If it does, the symlink write path works end-to-end. If not, use the hook-based"
echo "fallback in docs/AUTO_MEMORY.md."
