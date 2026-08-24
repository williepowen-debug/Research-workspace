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
    # ⚠️ AGE-SCOPED SINCE 2026-08-23, AFTER THIS GUARD RETURNED A FALSE GREEN ON ITSELF.
    # The old line was `git log --format="%h %s" REF | grep -m1 -F -- "$SUBJ"` over ALL of
    # history, which makes it a SUBSTRING-EXISTENCE test ("has anyone ever committed this
    # phrase?") and NOT the question it is asked ("did MY work reach origin?").
    # Live failure: a commit failed with `error: pathspec ... did not match any file(s)`,
    # nothing was pushed, and this script printed "✅ ON ORIGIN as bcee6fe34" — matching an
    # EARLIER COMMIT FROM THE SAME DAY (126 minutes old) whose subject happened to contain
    # "the 8/28 cut list".
    # It certified work that did not exist. That is the precise failure the whole script was
    # written to prevent (see the header: "the `Pushed.` line is not a receipt for YOUR work"),
    # reproduced one layer in — PAT-050, and the guard's own v1 failing on first real use.
    # Fix: match with the commit DATE, and refuse to certify on a match older than MAXAGE.
    # An old match is not a failure and not a pass; it is CANNOT-CERTIFY, because the honest
    # statement is "a commit with this subject exists but it is not this session's".
    # DEFAULT 1h, and the number is derived from the TOOL'S DOCUMENTED USE, not from what
    # made a test pass: this runs IMMEDIATELY after safe-push at closeout, so the commit it
    # is asked about is SECONDS old. An hour is already ~3600x slack.
    # ⚠️ My first cut of this fix used 24h and DID NOT CATCH THE LIVE FALSE GREEN — the
    # stale match was only 126 MINUTES old (an earlier commit from the same day, not the
    # "days-old" one I had assumed). I checked the actual age instead of trusting the story
    # I had already written, which is the same move this whole guard exists to enforce.
    MAXAGE=${VERIFY_PUSH_MAX_AGE_SECS:-3600}
    HITLINE=$(git log --format="%h%x09%ct%x09%s" "$REFNAME" | grep -m1 -F -- "$SUBJ")
    if [ -n "$HITLINE" ]; then
      HIT=$(printf '%s' "$HITLINE" | cut -f1)
      HITTS=$(printf '%s' "$HITLINE" | cut -f2)
      NOW=$(git log -1 --format=%ct "$REFNAME" 2>/dev/null || echo "$HITTS")
      AGE=$(( NOW - HITTS ))
      [ "$AGE" -lt 0 ] && AGE=0
      NMATCH=$(git log --format="%s" "$REFNAME" | grep -c -F -- "$SUBJ")
      if [ "$AGE" -gt "$MAXAGE" ]; then
        if [ "$AGE" -ge 86400 ]; then AGEH="$((AGE/86400))d"; elif [ "$AGE" -ge 3600 ]; then AGEH="$((AGE/3600))h"; else AGEH="$((AGE/60))m"; fi
        echo "⚠️  CANNOT CERTIFY — subject matched $HIT, but that commit is $AGEH old"
        echo "   (older than the $((MAXAGE/60))m window). A commit with this subject EXISTS on"
        echo "   $REFNAME; it is not evidence THIS session's work was pushed."
        echo "   Re-run with a subject unique to this commit, or check 'git log -1'."
        exit 2
      fi
      [ "$NMATCH" -gt 1 ] && echo "⚠️  note: $NMATCH commits on $REFNAME match this subject — newest shown"
      echo "✅ ON ORIGIN as $HIT  ($REFNAME @ ${REF:0:9}, committed $((AGE/60))m ago)"
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
