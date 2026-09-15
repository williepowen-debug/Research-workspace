#!/usr/bin/env bash
# Manual CATO session; intentionally no arbitrary Codex flag forwarding.
set -euo pipefail
cato_dir=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
repo_dir=$(git -C "$cato_dir" rev-parse --show-toplevel)
check_only=false
if [[ ${1-} == --check ]]; then
  check_only=true
  shift
fi
if [[ ${1-} == -- ]]; then shift; fi
if (( $# > 1 )); then
  printf '%s\n' 'Usage: launch.sh [--check] ["task"]' >&2
  exit 2
fi
for required in AGENTS.md CHARTER.md CONTINUITY.md; do
  if [[ ! -r "$cato_dir/$required" ]]; then
    printf 'CATO startup file missing: %s\n' "$required" >&2
    exit 1
  fi
done
prompt=${1:-'Follow your startup instructions. Orient to the current work and approvals, then give Will a short status and suggested next step. Do not begin unassigned work.'}
cmd=(codex --model gpt-6-astra --cd "$cato_dir" --add-dir "$repo_dir" --sandbox workspace-write --ask-for-approval on-request --)
if "$check_only"; then
  printf '%q ' "${cmd[@]}" "$prompt"
  printf '\n'
  exit 0
fi
command -v codex >/dev/null || { printf '%s\n' 'Codex is not installed or not on PATH.' >&2; exit 127; }
printf 'Starting CATO · requested model: %s · workspace: %s\n' "${cmd[2]}" "$cato_dir" >&2
exec "${cmd[@]}" "$prompt"
