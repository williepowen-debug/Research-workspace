#!/bin/bash
# verify_push.sh — did MY commit actually reach origin?
#
# WHY THIS EXISTS: `safe-push.sh` printing "Pushed." is not a receipt for YOUR
# work — on a shared repo it can be true about another desk's commits while
# yours stay local (observed live 2026-08-19, twice in one session).
#
# WHY IT IS NOT A ONE-LINER: a bare `git merge-base --is-ancestor <h> origin/master`
# collapses THREE states into one failure. Under concurrent git activity — normal
# here, several sessions share one .git — the remote-tracking ref is momentarily
# unreadable, which is INDISTINGUISHABLE from "my commit is absent." That false
# alarm is how a guard earns being ignored (permanent-red is silent-green
# inverted). So: retry, then report CANNOT-CERTIFY as its own state.
#
# Verify by SUBJECT, not hash: a rebase rewrites unpushed commit hashes, so the
# hash you recorded pre-sweep may no longer exist on any branch.
#
# rc contract (CHECK_STANDARD §9): 0 = on origin · 1 = genuinely NOT on origin
#                                  2 = CANNOT CERTIFY (ref unreadable — NOT proof of failure)
#
# usage: bash verify_push.sh "<commit subject substring>" [ref]
set -u
SUBJ="${1:-}"
REFNAME="${2:-origin/master}"

if [ -z "$SUBJ" ]; then
  echo "usage: verify_push.sh \"<commit subject substring>\" [ref]" >&2
  exit 2
fi

cd "$(git rev-parse --show-toplevel)" || exit 2

for attempt in 1 2 3; do
  git fetch -q origin 2>/dev/null
  if REF=$(git rev-parse --verify -q "$REFNAME"); then
    HIT=$(git log --format="%h %s" "$REFNAME" | grep -m1 -F -- "$SUBJ" | cut -d' ' -f1)
    if [ -n "$HIT" ]; then
      echo "✅ ON ORIGIN as $HIT  ($REFNAME @ ${REF:0:9})"
      exit 0
    fi
    echo "❌ NOT ON ORIGIN — no commit on $REFNAME with subject: $SUBJ"
    echo "   Your work is still local. Do NOT report the session as shipped."
    exit 1
  fi
  sleep 1   # a concurrent session holds the ref; retry rather than cry wolf
done

echo "⚠️  CANNOT CERTIFY — $REFNAME unreadable after 3 attempts (concurrent git activity)."
echo "   This is NOT evidence the push failed. Re-run once the other session settles."
exit 2
