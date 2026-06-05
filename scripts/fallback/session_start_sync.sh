#!/usr/bin/env bash
# FALLBACK ONLY — use this hook-based sync if a future Claude Code version stops
# following the symlinked memory dir. Do NOT run this alongside the symlink; pick
# one mechanism. Wire as a SessionStart hook (see docs/AUTO_MEMORY.md).
#
# At session start: pull latest, then mirror repo -> harness so the session reads
# the newest shared memory. Intentionally NO --delete: never destroy harness-local
# files that a prior Stop hook may not have committed yet (e.g. after a crash).
set -euo pipefail

root="$(git -C "$(dirname "$0")/../.." rev-parse --show-toplevel)"
slug="${root//\//-}"
harness="$HOME/.claude/projects/$slug/memory"

mkdir -p "$harness"
git -C "$root" pull --rebase --autostash || true
rsync -a "$root/memory/auto/" "$harness/"
