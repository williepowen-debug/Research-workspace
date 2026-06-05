#!/usr/bin/env bash
# FALLBACK ONLY — partner to session_start_sync.sh. Wire as a Stop hook.
# At session end: mirror harness -> repo, regenerate the index, commit & push.
#
# Concurrency: rsync without --delete + git merge handles the file-existence
# layer (memories written on different machines all land). If two machines edit
# the SAME memory file, git flags a body conflict on push — resolve by hand and
# re-commit (see docs/AUTO_MEMORY.md "Simultaneous writes").
set -euo pipefail

root="$(git -C "$(dirname "$0")/../.." rev-parse --show-toplevel)"
slug="${root//\//-}"
harness="$HOME/.claude/projects/$slug/memory"

[[ -d "$harness" ]] || exit 0
rsync -a "$harness/" "$root/memory/auto/"
# No index regeneration — Claude Code curates MEMORY.md itself (see docs/AUTO_MEMORY.md).

cd "$root"
git add memory/auto
if ! git diff --cached --quiet; then
  git commit -q -m "auto-memory: sync from $(hostname -s 2>/dev/null || hostname)"
  git pull --rebase --autostash && git push || \
    echo "stop_sync: push deferred (resolve conflicts, then push)." >&2
fi
