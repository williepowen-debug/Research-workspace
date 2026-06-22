# YEYOU — MEMORY

Durable cross-session memory: false-positive rules, per-agent quirks, recurring patterns. **Not** a session recap (that's `STATUS.md`).

---

## False-positive rules (NEVER re-flag these)

*Populate as Will/PROME mark findings WONTFIX. Seeded with quirks already known from the fleet:*

- **DEWEY is stateless by design.** Its `CLAUDE.md` says it keeps **only** `output/INDEX.tsv` — no `STATUS`, `SCRATCH`, `NEXUS_BRIEF`, `thesis/`, predictions, or catalyst docket. Do **not** flag DEWEY for "missing continuity files."
- **RED's STATUS cap is 200 lines**, not 250. RED uses `SCRATCH.md` as its canonical handoff; `LAST_COMPLETION.md` and `archive/handoffs/` are **retired/frozen** — don't flag their absence or staleness.
- **`NEXUS_BRIEF.md` is required for newer agents (CORAL, RED-wave), not all.** Older agents (e.g. REGINALD) don't maintain one — don't flag REGINALD for "missing NEXUS_BRIEF."

## Per-agent quirks

- **Hardening-wave drift is expected, not an error.** Newer agents use `board_log.tsv` for WALTER consumption + symmetric boot/write-back; older agents (REGINALD) use the BOARD diff-scan + outbox model. Both are valid — do **not** flag one agent for "not matching" another's protocol. Only flag an agent against **its own** `CLAUDE.md`.
- **PROME has two homes** (`PROME/` and `AGENTS/PROME/`) and is the one agent allowed to commit to both — don't flag PROME cross-dir commits spanning those two paths.

## Recurring patterns

*(none yet — log patterns you see repeat across agents, e.g. "thesis bumped without CHANGELOG" recurring fleet-wide → candidate for a PROME-level fix, not just per-agent nits.)*
