#!/usr/bin/env bash
#
# safe-push.sh — fast-forward-gated push for the shared-clone multi-agent repo.
#
# WHY: in the shared single clone, deciding "is it safe to push?" by eyeballing
# `git status` is unreliable — a teammate's push shows as BEHIND 0 because their
# commits are already in the shared LOCAL repo. This hands the one judgment that
# matters — "is my push a clean fast-forward?" — to git instead of an eyeball.
#
# SAFETY MODEL (read this before trusting it):
#   * A push NEVER touches the working tree, so other agents' UNCOMMITTED edits are
#     never at risk. The dangerous op is PULL on a shared tree — this script never pulls.
#   * The ff-check below is ADVISORY. The ACTUAL guarantee is git's own non-fast-forward
#     REJECTION at push time, which also covers the race where another machine pushes
#     between our fetch and our push. We never force, so the worst case is a clean reject.
#   * It sweeps EVERY agent's committed-but-unpushed work (the push-train pattern) — that's
#     correct; step ⑥ prints exactly what is going up. Each commit already carries its author.
#
# AUTHORIZED FOR CLOSEOUT AUTO-PUSH (Will 2026-06-26; premise updated to SERIAL
#   MULTI-MACHINE 2026-07-01 — Will runs ONE box at a time, desktop ⇄ laptop).
#   Supersedes the prior "run manually only" prohibition. Safe to wire into closeout because
#   the ff-gate below FAILS SAFE: if origin has commits this clone lacks (the other box
#   pushed), this ABORTS cleanly (step ④) rather than forcing or pulling a shared tree.
#   A non-ff abort is ROUTINE under serial multi-machine: `git pull --rebase` + re-push.
#   Escalate to Will (per-agent-branches tripwire) only on out-of-dir rebase conflicts or
#   mid-session recurrence — the signatures of two machines running simultaneously.
#   Policy: root CLAUDE.md Git Protocol + PROME/GIT_COORDINATION.md.
#
# Reviewed by SAM (2026-06-22): added the on-branch assertion (#1) + shallow-clone guard (#2).
# Canonical fleet copy (PROME-owned). CARL/scripts/safe-push.sh is the original reference.
#
# Usage: safe-push.sh [--dry-run]      # --dry-run does everything EXCEPT the final push

set -euo pipefail

REMOTE=origin
BRANCH=master
DRY_RUN=0
[ "${1:-}" = "--dry-run" ] && DRY_RUN=1

# ── ① assert we're on the branch we intend to push (catches detached HEAD / wrong branch) ──
#     Fix #1 (SAM): steps below validate HEAD; the push targets BRANCH — assert they're the same
#     so we never validate one ref and ship another.
cur="$(git symbolic-ref --short -q HEAD || true)"
[ "$cur" = "$BRANCH" ] || { echo "ABORT: HEAD is '${cur:-detached}', not '$BRANCH'. Checkout $BRANCH first."; exit 1; }

# ── ② shallow-clone guard (Fix #2, SAM) ──
#     Web/CC containers clone shallow; `merge-base --is-ancestor` can mis-answer on a shallow
#     repo (see finding_shallow_clone_false_fork). It fails SAFE (spurious ABORT, never a bad
#     push) but that's a real false-block — so unshallow first, or refuse with a clear message.
if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
  echo "Shallow clone detected — unshallowing so the fast-forward check is trustworthy…"
  git fetch --unshallow "$REMOTE" || true
  if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
    echo "ABORT: still shallow after --unshallow; the ff-check would be unreliable. Resolve manually."
    exit 1
  fi
fi

# ── ③ refresh just the ref we care about (tighter than `git fetch origin`) ──
git fetch "$REMOTE" "$BRANCH"

# ── ④ the one judgment that matters: is our push a clean fast-forward? (answered by git) ──
if ! git merge-base --is-ancestor "$REMOTE/$BRANCH" HEAD; then
  echo "ABORT: $REMOTE/$BRANCH has commits not in local $BRANCH (likely a cross-machine push)."
  echo "Integrate manually (rebase your own commits) — do NOT auto-pull a shared working tree."
  echo "Missing locally:"
  git --no-pager log --oneline "HEAD..$REMOTE/$BRANCH" | head
  exit 1
fi

# ── ⑤ anything to push? ──
ahead="$(git rev-list --count "$REMOTE/$BRANCH..HEAD")"
[ "$ahead" -eq 0 ] && { echo "Nothing to push (0 commits ahead of $REMOTE/$BRANCH)."; exit 0; }

# ── ⑥ show exactly what's going up (every agent's committed work in the train) ──
echo "Fast-forward: $ahead commit(s) to push to $REMOTE/$BRANCH:"
git --no-pager log --oneline "$REMOTE/$BRANCH..HEAD"

# ── ⑦ push (the only mutating step; pushes the exact validated ref; never touches a working tree) ──
if [ "$DRY_RUN" = "1" ]; then
  echo "[--dry-run] stopping before push."
  exit 0
fi
# ── ⑦b the push's OWN exit code is not the receipt (2026-08-28, NEXUS via PROME): a
#     `! [remote rejected] … cannot lock ref` line printed AND the caller saw rc=0 — either the
#     push status was laundered (a `| tail`/`| head` on the caller side reports the LAST
#     command's rc, HENRY's pipe finding the same day) or the ref race resolved oddly. Either
#     way the only receipt that certifies anything is git's OWN answer to "is my HEAD now an
#     ancestor of the freshly-fetched remote branch?" — so we ask it, after the push, and
#     never print `Pushed.` on a bare exit code. rc contract: 0 confirmed · 1 NOT confirmed
#     (the push output is above; treat it as a failed push and re-run the rebase recipe) · 2 CANNOT-CONFIRM.
#     rc 2 = CANNOT-CONFIRM: the post-push fetch itself failed (network, lock), so neither
#     "pushed" nor "not pushed" is certifiable — a third state, never folded into either
#     (RAV review 2026-08-28: `set -e` was exiting with git's raw status against a 0/1 contract).
push_rc=0
git push "$REMOTE" "HEAD:$BRANCH" || push_rc=$?
if ! git fetch -q "$REMOTE" "$BRANCH"; then
  echo "CANNOT-CONFIRM: git push exited $push_rc, but the post-push fetch of $REMOTE/$BRANCH FAILED — the receipt cannot be issued either way."
  echo "  Re-run scripts/safe-push.sh once the remote is reachable; do not read this as pushed OR as not pushed."
  exit 2
fi
if git merge-base --is-ancestor HEAD "$REMOTE/$BRANCH"; then
  echo "Pushed. CONFIRMED: HEAD $(git rev-parse --short HEAD) is on $REMOTE/$BRANCH (fresh fetch)."
  [ "$push_rc" -ne 0 ] && echo "  (note: git push exited $push_rc but the ref IS on origin — a concurrent train carried it)"
  exit 0
fi
echo "NOT PUSHED: HEAD $(git rev-parse --short HEAD) is NOT on $REMOTE/$BRANCH after the push (git push rc=$push_rc)."
echo "  Do not read any 'Pushed.' above this line as a receipt. Recipe: git pull --rebase --autostash, then re-run."
exit 1
