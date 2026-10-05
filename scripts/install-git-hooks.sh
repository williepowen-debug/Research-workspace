#!/usr/bin/env bash
# Install only into a clone with no conflicting hook setup. Safe to repeat.
set -eu
root=$(git rev-parse --show-toplevel) || exit 1
cd "$root"
[ -f PROME/ROSTER.md ] || { echo 'git-hooks: wrong repository; NOT installed' >&2; exit 1; }
for hook in commit-msg pre-push; do
    [ -x "scripts/githooks/$hook" ] || { echo "git-hooks: $hook missing/not executable; NOT installed" >&2; exit 1; }
done
rc=0
hp=$(git config --get core.hooksPath) || rc=$?
[ "$rc" -le 1 ] || { echo "git-hooks: config read failed rc=$rc; NOT installed" >&2; exit 1; }
if [ "$rc" -eq 0 ]; then
    [ "$hp" = scripts/githooks ] || { echo "git-hooks: existing core.hooksPath='$hp' preserved; fleet hooks NOT installed" >&2; exit 1; }
    exit 0
fi
default=$(git rev-parse --git-path hooks) || exit 1
for existing in "$default"/*; do
    case "$existing" in *.sample) continue ;; esac
    if [ -f "$existing" ] && [ -x "$existing" ]; then
        echo "git-hooks: active default hook '$existing' preserved; fleet hooks NOT installed" >&2
        exit 1
    fi
done
git config --local core.hooksPath scripts/githooks || { echo 'git-hooks: config write failed; NOT installed' >&2; exit 1; }
echo 'git-hooks: installed scripts/githooks (commit-msg, pre-push)'
