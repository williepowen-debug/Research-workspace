# TERRY CLOSEOUT

**Created:** 2026-06-26
**Owner:** TERRY (Claude Code)
**Purpose:** repeatable session-end write-back so state survives across sessions. Run before `/clear`, `/new`, or handoff.

> Companion to `CLAUDE.md` (session start) + root `CLAUDE.md` (git protocol). Tier model mirrors LIQUID/PROME CLOSEOUT for cross-agent vocabulary.

---

## When to run

- Before `/clear` or `/new`, or stepping away from a long session.
- After any session that changed state, built a card/tool, or reviewed a trade.
- Skip for casual one-off desk chat with no artifacts.
- **Live-event override:** if a print/trigger window is firing, DEFER full write-back — snapshot STATUS as a working dashboard, keep the card open until the event stabilizes.

---

## Pick a tier

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-session restart within the hour | MEMORY Current-Session addendum (3–5 lines) | No |
| **Light** | Short paused session; 1–2 artifacts | STATUS surgical + MEMORY surgical | Optional |
| **Standard** *(default)* | End-of-thread/day; multi-artifact | Chunks 1 + 2 + 4 | Yes |
| **Heavy** | Built tooling / durable finding / structural shift | Standard + Chunk 3 (auto-memory) | Yes |

---

## Chunk 1 — State

**`STATUS.md` (surgical, not rewrite):** header stamp + 🟢/🟡/🟠/🔴; refresh the live-state sections —
what's BUILT, what's EXERCISED, what's PENDING, cards fired count, open Will-decisions. Keep it HONEST live state, not a "created ✅" checklist. <120 lines.

**`MEMORY.md` (lean):** update the Current-Session block (Delivered / Pending); refresh Next-Session list (drop done, add deferred); append a **Durable Finding ONLY if** it's a new structural lesson that survives the episode (most sessions: no append). Promote a heavy Current-Session block to a one-line digest rather than letting it grow into a log.

---

## Chunk 2 — Cards / tooling / ledgers (trigger-gated — touch only what changed)

| File | Trigger to touch | Action |
|---|---|---|
| `setups/*.md` | A card was built, fired, or invalidated | Update its ZONE 2 / decision / status; a fired card's outcome → POSTMORTEMS when it closes |
| `TRADE_BOOK.md` / `SETUPS.tsv` | A setup was proposed/resolved | Append/update the summary row |
| `POSTMORTEMS.md` | A Terry-reviewed trade CLOSED | Add a postmortem using the template (tag + lesson) |
| `grade_config.json` | A Q1 baseline/threshold/trap changed | Surgical edit; re-run `grade_print.py --selftest` |
| `scripts/*.py` | A script changed | Re-run its `--selftest`; note result in the commit |
| `daytrading/*` | A day-trading session was reviewed | Per `daytrading/README.md` (its own loop) |

**Don't auto-touch:** `archive/`, `charts/`, `RISK_*.md`, templates (revise only when the method changes).

---

## Chunk 3 — Auto-memory (Heavy only, selective)

Save to `memory/auto/` only for a surprising/non-obvious *how-to-work* lesson, or a validated/invalidated pattern — not an activity recap, not framework detail (that's MEMORY Durable Findings), not derivable file/code facts. If nothing surprising: skip.

---

## Chunk 4 — Git + report (Standard/Heavy; Light optional; Bounce skips)

Git is **pathspec-scoped** (shared `.git/index` — see root CLAUDE.md):
- **Modified:** `git commit AGENTS/TERRY/<file> -m "TERRY: <subject>"`
- **New:** `git add AGENTS/TERRY/<specific-file> && git commit AGENTS/TERRY/<same-file> -m "TERRY: <subject>"` — explicit paths, never `git add AGENTS/TERRY/` as a dir.
- **Never `git reset HEAD`** (global unstage race).
- **Push is Will-coordinated — defer by default.** Commit locally; note pending push in MEMORY Current-Session. In a Will-opened window one agent's push sweeps everyone's committed work.
- Trailer: `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.

**Report to Will/Prome:** what landed (concrete) · what's pending · next entry point (points at MEMORY Next-Session).

---

## Skip / never rules

- `AGENTS/<other>/` — never edit; route cross-agent via `outbox/` (🔴 only — outbox restraint).
- `FORGE/`, root `CLAUDE.md`, `HEARTBEAT.md` — flag to Will/Prome; don't auto-edit. (Approved cards land in FORGE at execution = a Will/FORGE step.)
- Runtime outputs (`scripts/.cache/`, `grades/`) are gitignored — never commit.
- `trash`/`gio trash` over `rm`. Read before Edit. Chunk multi-file updates.
