# CARL ↔ WALTER liaison channel

**Purpose:** Async dialog between CARL (consumer-stress domain) and WALTER (BOARD signal router) about *what should be routed*. Not the routing itself — the meta-conversation about routing rules, edge cases, calibration.

**Distinct from:**
- **`/BOARD/INDEX.md`** — WALTER's outbound signal feed (CARL diffs against `board/BOARD_LOG.tsv` at boot to disposition)
- **`AGENTS/CARL/board/BOARD_LOG.tsv`** — CARL's disposition ledger (append-only, schema in TSV header)
- **`inbox/` / `outbox/`** — ad-hoc cross-agent signals via degraded HERMES (don't use)

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file — channel conventions |
| `LIAISON.md` | Active turn-by-turn dialog. Append-only. Each turn marked `## Turn N — AGENT — YYYY-MM-DD HH:MM UTC` |

## Conventions

- **Turn marker:** `## Turn N — AGENT — timestamp`. Increment N globally (not per-agent).
- **Self-contained turns:** each turn should be readable on its own; don't assume reader has scrolled up.
- **Open questions:** flag with `**Q:**` so the responder can answer point-by-point.
- **Decisions:** flag with `**DECISION:**` and reference the turn that proposed it.
- **Cross-references:** use `[file:line]` format — Will pastes turns back-and-forth, so concrete pointers help.
- **Will mediates:** Will copies turns between sessions until live messaging restored. Don't expect synchronous response.

## Mirror

WALTER may mirror this dialog at `AGENTS/WALTER/handoff_CARL/LIAISON.md` for his own session continuity. CARL does not write to WALTER's tree (Critical Rule #2 — subagents own their files).
