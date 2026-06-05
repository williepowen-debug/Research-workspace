# memory/auto — git-synced auto-memory store

This folder is the **single source of truth** for Claude Code auto-memory across
every machine that runs agents in this repo (desktop, laptop, …).

Each machine's harness path —
`~/.claude/projects/<repo-path-slug>/memory` — is a **symlink** to this folder.
Claude reads and writes auto-memory at that path as usual; because it resolves
here, every change rides the normal git pull/push/merge flow and all machines
converge. No more parallel, unmergeable memories.

## Contents

- `MEMORY.md` — the lean, always-loaded index. **Generated** by
  `scripts/gen_automemory_index.py`; do not hand-edit.
- `feedback_*.md` — behavioral corrections (how to work).
- `finding_*.md` — patterns / methodological insight.
- `project_*.md` — initiative state.

Referenced elsewhere in the repo via `[[wikilink]]` markers (e.g.
`[[finding_threshold_vs_mechanism]]`), which name the file minus `.md`.

## Setup & rules

See `docs/AUTO_MEMORY.md` for one-time setup on each machine, the
simultaneous-write rules, and troubleshooting.
