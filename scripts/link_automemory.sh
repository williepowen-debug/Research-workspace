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
[[ "${1:-}" == "--apply" ]] && APPLY=1

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
    echo "Verify OK: harness path reads through to the repo store."
  else
    echo "Verify FAILED: harness path is not readable. Investigate before trusting it."
    exit 1
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
echo "  python3 scripts/gen_automemory_index.py        # refresh the lean index"
echo "  git add memory/auto"
echo "  git commit -m 'auto-memory: capture from $HOST'"
echo "  git pull --rebase && git push"
