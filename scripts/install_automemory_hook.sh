#!/usr/bin/env bash
# Install the auto-memory index-regen pre-commit hook on THIS machine.
# Git hooks live in .git/hooks (not version-controlled), so run this once per
# clone. Idempotent. Refuses to clobber an unrelated existing hook.
set -euo pipefail

root="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
src="$root/scripts/hooks/pre-commit"
dst="$root/.git/hooks/pre-commit"

chmod +x "$src"

if [[ -L "$dst" ]]; then
  echo "pre-commit already symlinked -> $(readlink "$dst"). Re-pointing to $src."
  ln -sf "$src" "$dst"
elif [[ -e "$dst" ]]; then
  echo "A non-symlink pre-commit hook already exists at:"
  echo "  $dst"
  echo "Not overwriting. Add this line to it manually so the index stays in sync:"
  echo "  python3 \"$root/scripts/gen_automemory_index.py\" && git add \"$root/memory/auto/MEMORY.md\""
  exit 1
else
  mkdir -p "$(dirname "$dst")"
  ln -s "$src" "$dst"
  echo "Installed pre-commit hook -> $src"
fi
