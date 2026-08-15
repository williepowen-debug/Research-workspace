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

# Load canonical caps SHARED with scripts/memory_index_check.py so the two
# guards can never disagree on what "the cap" is (born 2026-08-14 off DEWEY's
# 8/12 flag: same file read "82%" and "77%" in the same closeout).
caps="$(dirname "$0")/harness_caps.env"
[[ -f "$caps" ]] || { echo "MISSING: $caps — the shared caps file the guards read." >&2; exit 2; }
# shellcheck disable=SC1090
source "$caps"

lines=$(wc -l < "$idx")
bytes=$(wc -c < "$idx")
hard_lines="$MEMORY_HARNESS_CAP_LINES"
hard_bytes="$MEMORY_HARNESS_CAP_BYTES"
soft_lines=$(( hard_lines * MEMORY_WARN_PERCENT / 100 ))
# soft_bytes ADDED 2026-08-03 (DAEDALUS, scripts/ break-fix). There was a soft tier for
# LINES and none for BYTES, so the WARNING could not fire on this file's actual growth
# mode: measured today it sat at 19027/25600 bytes = 74% of the binding cap but 23/200
# lines = 12%, and the script printed "OK: comfortably under the cap". The 2026-07-31
# three-tier restructure is what changed the growth mode — rows are now long single
# lines, so the file grows in bytes, not lines, and the only tier watching bytes was the
# CRITICAL one at 100%. PAT-074: the guard's PASS was silent about the dimension that binds.
soft_bytes=$(( hard_bytes * MEMORY_WARN_PERCENT / 100 ))
pct_lines=$(( lines * 100 / hard_lines )); pct_bytes=$(( bytes * 100 / hard_bytes ))

echo "MEMORY.md: ${lines} lines (${pct_lines}% of ${hard_lines}), ${bytes} bytes (${pct_bytes}% of ${hard_bytes}) — boot-load cap"

if (( lines >= hard_lines || bytes >= hard_bytes )); then
  echo "CRITICAL: index is at/over the boot-load cap — entries past the cap are NOT loaded at boot. Compact now." >&2
  exit 2
elif (( lines >= soft_lines || bytes >= soft_bytes )); then
  echo "WARNING: index approaching the boot-load cap (${pct_lines}% lines / ${pct_bytes}% bytes). Consolidate or retire low-value memories soon." >&2
  echo "         Root CLAUDE.md: agents must NOT compact this file — flag to PROME (Will-ruled 7/28)." >&2
  exit 1
fi
# Never assert "comfortably" without the number that would contradict it.
echo "OK: under the cap (${pct_lines}% lines / ${pct_bytes}% bytes; warns at 80%)."
