#!/usr/bin/env bash
# Compatibility entry point only. Root script owns all push safety and receipts.
set -euo pipefail
carl_script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
carl_repo_root="$(git -C "$carl_script_dir" rev-parse --show-toplevel)"
cd -- "$carl_repo_root"
exec bash "$carl_repo_root/scripts/safe-push.sh" "$@"
