#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# orphan_check.sh — closeout guard against ORPHANED CROSS-AGENT PACKETS.
#
# THE PROBLEM: the fleet pathspec rule ("git add ONLY files inside your own
# AGENTS/<NAME>/") means a packet you write into ANOTHER agent's inbox falls
# outside your own commit scope. Path-scoped closeout commits therefore CANNOT
# sweep it, and it stays untracked — single-copy, on one machine. Under serial
# multi-machine operation the recipient never receives it and NOBODY IS TOLD.
#
# Evidence it recurs (HENRY audit 2026-07-23): 350 cross-agent packets added in
# 45 days, 41 (~12%) not introduced by their own sender's commit; 30 commits in
# 90 days explicitly describing an on-behalf rescue. A remedy already exists
# (root protocol routes out-of-dir commits to PROME) but it is DETECTION-
# DEPENDENT — it needs someone to notice. This is the missing detector.
#
# USAGE:  bash scripts/orphan_check.sh <AGENT_NAME>
# Exit 0 always (advisory, never blocks a closeout). Read-only: no writes,
# no staging, no commits — it only looks and reports.
#
# ADOPTED fleet-wide 2026-07-23 (Will-approved; PROME review + 4-case test):
# root CLAUDE.md Git Protocol carve-out ratified same session — self-authored
# packets in a recipient's inbox are the sender's to commit. Built by HENRY
# (origin memo: AGENTS/HENRY/outbox/2026-07-23_to-PROME_cross-agent-packet-
# orphaning-protocol-gap.md). Wired into root CLAUDE.md "At session end" 1b.
#
# KNOWN HEURISTIC EDGES (both fail in the SAFE direction — the file is still
# surfaced and routed to PROME either way):
# - Router-authored relays ("from-X-via-PROME") classify [not yours] for the
#   router (PROME); the fallback instruction is flag-to-PROME = the router.
# - Paths containing spaces mangle in the awk $NF split; fleet packet
#   filenames never contain spaces.
# - PROME's home dir is PROME/ (not AGENTS/PROME/), so a PROME run lists
#   PROME's own in-flight files as [not yours]; PROME is also the flag-to
#   target, so it reads its own report. Domain agents are unaffected.
# ---------------------------------------------------------------------------
set -euo pipefail

ME="${1:?usage: orphan_check.sh <AGENT_NAME>   (e.g. orphan_check.sh LIQUID)}"
cd "$(git rev-parse --show-toplevel)"

# Every uncommitted path outside my own agent dir (deduped — porcelain emits a
# rename/delete pair as two lines for the same file).
HITS=$(git status --porcelain | awk '{print $NF}' | grep -v "^AGENTS/${ME}/" | sort -u || true)

if [ -z "$HITS" ]; then
  echo "✓ orphan check clean — nothing uncommitted outside AGENTS/${ME}/"
  exit 0
fi

# Heuristic for "authored by me": the fleet packet convention is
# YYYY-MM-DD_from-<SENDER>_<slug>.md  /  YYYY-MM-DD_to-<TARGET>_<slug>.md
MINE=$(echo "$HITS" | grep -iE "_from-${ME}_|_to-[A-Z]+_.*${ME}|/${ME}_" || true)
OTHER=$(echo "$HITS" | grep -ivE "_from-${ME}_|_to-[A-Z]+_.*${ME}|/${ME}_" || true)

echo "⚠️  uncommitted files outside AGENTS/${ME}/:"
[ -n "$MINE" ]  && echo "$MINE"  | sed 's/^/     [likely YOURS] /'
[ -n "$OTHER" ] && echo "$OTHER" | sed 's/^/     [not yours]    /'

if [ -n "$MINE" ]; then
  cat <<MSG

🔴 THE FLAGGED FILES LOOK LIKE PACKETS YOU AUTHORED.
   If you do not commit them they never reach the recipient, and the recipient
   is never told anything was sent. Committing files you authored into another
   agent's inbox is the ONE sanctioned exception to the pathspec rule.

   git add <paths> && git commit <paths> -m "${ME} -> <recipient>: <what>"
MSG
fi

if [ -n "$OTHER" ]; then
  echo ""
  echo "ℹ️  The [not yours] entries are someone else's work — do NOT commit them."
  echo "   Flag to PROME (or Will) rather than sweeping them into your commit."
fi

exit 0
