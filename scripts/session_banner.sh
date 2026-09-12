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

# ⚠️ THE RC MUST NOT GO THROUGH A PIPE. Until 2026-09-12 this line read
#   DIRTY=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
# and `$?` after a pipeline is the LAST command's status — `tr`'s, never git's. A failing
# `git status` therefore produced DIRTY=0 and this script printed the ALL-CLEAR line
# ("tree clean") over a dirty tree, in the SessionStart hook of every session in the fleet.
# Found by the DOCKET L294 origin-proof sweep (behavioural drill: `GIT_SHIM_FAIL=status` against
# a repo with 5 dirty paths → "tree clean"). Note the asymmetry that made it survive: the ORIGIN
# legs of this same script were already correct (FETCH_RC captured on its own line; the "? ?"
# sentinel for rev-list) — only the leg whose rc travelled through a pipe was wrong.
# Same mechanism as the pipeline-`$?` class this sweep was chartered on.
STATUS_OUT=$(git status --porcelain 2>/dev/null); STATUS_RC=$?
DIRTY=$(printf '%s' "$STATUS_OUT" | grep -c . || true)

ENV_FLAG=""
if [ -f scripts/env_doctor.py ]; then
    python3 scripts/env_doctor.py --quiet >/dev/null 2>&1 || ENV_FLAG="FAIL"
fi

FLAGS=""
[ "$FETCH_RC" -ne 0 ] && FLAGS="$FLAGS [FETCH FAILED — sync state UNVERIFIED; do not trust 0/0]"
# "?" = rev-list couldn't resolve HEAD...origin/master (renamed branch/ref, unborn
# HEAD): sync state is UNKNOWN, never let it fall through to the all-clear line.
{ [ "$AHEAD" = "?" ] || [ "$BEHIND" = "?" ]; } && FLAGS="$FLAGS [SYNC STATE UNVERIFIED — ahead/behind vs origin/master unresolvable; do not trust clean]"
[ "$BEHIND" != "0" ] && [ "$BEHIND" != "?" ] && FLAGS="$FLAGS [BEHIND origin/master by $BEHIND — local state stale; apply the before-pulling protocol, do NOT auto-pull]"
[ "$AHEAD" != "0" ] && [ "$AHEAD" != "?" ] && FLAGS="$FLAGS [AHEAD by $AHEAD unpushed commit(s)]"
[ "$STATUS_RC" -ne 0 ] && FLAGS="$FLAGS [git status FAILED — dirty-tree state UNVERIFIED; do NOT trust 'tree clean', check ownership manually before ANY git op]"
[ "$DIRTY" != "0" ] && FLAGS="$FLAGS [DIRTY TREE: $DIRTY path(s) — may be another agent's live work; check ownership before ANY git op]"
[ -n "$ENV_FLAG" ] && FLAGS="$FLAGS [env_doctor FAIL — fix/flag before citing FRED-dependent levels]"

if [ -z "$FLAGS" ]; then
    echo "[boot-banner] repo ${AHEAD}/${BEHIND} vs origin/master, tree clean, env_doctor OK (flag-not-force: nothing pulled/modified)"
else
    echo "[boot-banner FLAGS]$FLAGS (flag-not-force: nothing pulled/modified — resolve per root CLAUDE.md Git Protocol)"
fi
exit 0
