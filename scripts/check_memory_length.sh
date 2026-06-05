#!/usr/bin/env bash
# check_memory_length.sh — guard against silent auto-memory index truncation.
#
# The Claude Code harness loads only the first ~200 lines / 25 KB of
# memory/auto/MEMORY.md at boot; anything past that is silently dropped (no
# warning). This catches the index BEFORE that cliff so entries don't quietly
# stop loading. Run at session end, or wire it as a periodic Prome chore.
#
# Exit codes: 0 = ok, 1 = approaching cap (warn), 2 = over cap (critical).
set -euo pipefail

root="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
idx="$root/memory/auto/MEMORY.md"
[[ -f "$idx" ]] || { echo "no MEMORY.md at $idx — nothing to check."; exit 0; }

lines=$(wc -l < "$idx")
bytes=$(wc -c < "$idx")
soft_lines=180; hard_lines=200; hard_bytes=25600

echo "MEMORY.md: ${lines} lines, ${bytes} bytes (boot-load cap ~${hard_lines} lines / ${hard_bytes} bytes)"

if (( lines >= hard_lines || bytes >= hard_bytes )); then
  echo "CRITICAL: index is at/over the boot-load cap — entries past the cap are NOT loaded at boot. Compact now." >&2
  exit 2
elif (( lines >= soft_lines )); then
  echo "WARNING: index approaching the boot-load cap. Consolidate or retire low-value memories soon." >&2
  exit 1
fi
echo "OK: comfortably under the cap."
