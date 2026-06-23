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
# DO NOT wire this into closeout or a git hook. Run it MANUALLY, inside a push window Will
# has opened — automating it recreates the "automatic session-end push" the protocol forbids.
#
# Reviewed by SAM (2026-06-22): added the on-branch assertion (#1) + shallow-clone guard (#2).
# Placement: CARL/scripts/ reference copy; PROME owns fleet-wide promotion (these fixes ride along).
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
git push "$REMOTE" "HEAD:$BRANCH"
echo "Pushed."
