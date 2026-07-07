#!/usr/bin/env bash
# session_banner.sh — SessionStart hook: FLAG-NOT-FORCE boot banner.
# Prints repo sync state + env flags into session context. NEVER pulls,
# stashes, or modifies the working tree (root CLAUDE.md dirty-tree rule).
# Fired by .claude/settings.json SessionStart hook; cwd-proof (rev-parse).
set -u

cd "$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0

# Fetch = read-only vs working tree; timeout so a dead network never blocks boot.
timeout 10 git fetch origin --quiet 2>/dev/null
FETCH_RC=$?

set -- $(git rev-list --left-right --count HEAD...origin/master 2>/dev/null || echo "? ?")
AHEAD="${1:-?}"; BEHIND="${2:-?}"

DIRTY=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')

ENV_FLAG=""
if [ -f scripts/env_doctor.py ]; then
    python3 scripts/env_doctor.py --quiet >/dev/null 2>&1 || ENV_FLAG="FAIL"
fi

FLAGS=""
[ "$FETCH_RC" -ne 0 ] && FLAGS="$FLAGS [FETCH FAILED — sync state UNVERIFIED; do not trust 0/0]"
[ "$BEHIND" != "0" ] && [ "$BEHIND" != "?" ] && FLAGS="$FLAGS [BEHIND origin/master by $BEHIND — local state stale; apply the before-pulling protocol, do NOT auto-pull]"
[ "$AHEAD" != "0" ] && [ "$AHEAD" != "?" ] && FLAGS="$FLAGS [AHEAD by $AHEAD unpushed commit(s)]"
[ "$DIRTY" != "0" ] && FLAGS="$FLAGS [DIRTY TREE: $DIRTY path(s) — may be another agent's live work; check ownership before ANY git op]"
[ -n "$ENV_FLAG" ] && FLAGS="$FLAGS [env_doctor FAIL — fix/flag before citing FRED-dependent levels]"

if [ -z "$FLAGS" ]; then
    echo "[boot-banner] repo 0/0 vs origin/master, tree clean, env_doctor OK (flag-not-force: nothing pulled/modified)"
else
    echo "[boot-banner FLAGS]$FLAGS (flag-not-force: nothing pulled/modified — resolve per root CLAUDE.md Git Protocol)"
fi
exit 0
