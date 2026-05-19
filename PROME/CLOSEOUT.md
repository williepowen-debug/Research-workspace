# PROME CLOSEOUT

**Created:** 2026-05-18
**Owner:** Prome (CC surface — Claude Code)
**Purpose:** Repeatable session-end procedure to maintain consistency across CC-Prome sessions. Run before `/clear`, `/new`, or session handoff.

> Companion to `PROME/BOOT.md` (session start) and `PROME/CLAUDE.md` (CC-Prome bootstrap). Follow root `CLAUDE.md` for git protocol details.

---

## When to run

- Before `/clear` or `/new`
- Before stepping away from a long session
- After any session that produced state changes worth persisting

Skip for casual one-off exchanges with no artifacts.

---

## Pre-closeout (~1 min)

1. `git status --short` — review what's changed
2. Confirm no other agents have uncommitted work outside `PROME/` and `AGENTS/PROME/` (per root CLAUDE.md "Before pulling")
3. Mentally list this session's artifacts: proposals decided, files written, prototypes run, decisions made
4. Decide closeout scope:

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-day restart for config/tmux/clear/branch; you're coming right back within the hour | SCRATCH addendum (3-5 lines) | No |
| **Light** | Short session paused for hours; 1-2 artifacts; audit can wait for end-of-day Standard | SCRATCH full rewrite + STATUS surgical | Optional |
| **Standard** *(default)* | End-of-thread or end-of-day; multi-artifact session | All Chunk 1 + Chunk 2 daily log + Chunk 4 commit/push | Yes |
| **Heavy** | Pattern-discovery session; new lessons/designs to fold | Standard + auto-memory + design-docs + Chunk 3 residuals | Yes |

End-of-day always runs at least Standard so the audit trail catches up. 10 Bounces + 1 end-of-day Standard = no audit gap, just a rollup HANDOFF entry covering the day.

**Bounce procedure (the truly minimal):** append 3-5 lines to `PROME/SCRATCH.md` — (a) what just happened, (b) what's pending, (c) next-session entry point. No STATUS, no HANDOFF, no daily log, no auto-memory, no commit. Total time: ~30 seconds. Use only when you trust the next session will pick up within the hour and you accept the durability risk (no git checkpoint).

---

## Chunk 1 — State files (Light / Standard / Heavy; Bounce skips except SCRATCH addendum)

### `PROME/SCRATCH.md` — full rewrite

- **What just happened:** bullet list of session accomplishments
- **Current git state:** behavior-language (e.g., "clean, synced to origin"), NOT hash references — hashes decay 2–3 commits within 48h
- **Next planned work:** concrete entry point for next session
- **Cautions:** in-flight items, fragile state, known-stale assumptions

### `PROME/STATUS.md` — surgical update (not rewrite)

- Update `Updated:` timestamp
- Adjust `Pending Work` table — mark completed, add new, update priorities
- Update `Active Decision Layer` table (✅ / ⚠️ / ❌)
- Update `Next Best Action` — one concrete move

### `PROME/CLAUDE_CODE_HANDOFF.md` — append session entry (Standard / Heavy only)

CC-Prome audit-trail role. Light skips — audit rolls up at end-of-day Standard. NOT the place for session narrative (that's SCRATCH).
- **What landed** — one-line referents per artifact; point at SCRATCH/memory for headlines
- **Files edited** — compact list (PROME scope + any agent-inbox writes with PROVENANCE note)
- **Decisions Will made this session** (retrospective audit; helps future-Prome avoid re-asking)
- **Decisions needed from Will** (forward-looking; usually a one-line pointer to SCRATCH's live carries)
- **Risks / blockers**
- **v_next design inputs** (any new pattern feedback returned by sub-agents)
- **Next suggested work** (one-line pointer to SCRATCH, not a full restate)
- **Rules held to** (autonomy / scope verification)

**Doc-ownership separation (canonical homes):**
- **SCRATCH** = session narrative + next-session entry point (full headlines, "what just happened")
- **STATUS** = state tables only (agent health, Pending Work status, Active Decision Layer freshness); no narrative
- **HANDOFF** = CC-Prome audit trail (files, decisions, rules); references SCRATCH for narrative

**Checkpoint:** if any of these three files restate the same fact, drop it from STATUS and HANDOFF, keep it in SCRATCH. Cross-reference rather than duplicate.

---

## Chunk 2 — Memory (Standard / Heavy; Light + Bounce skip)

### `memory/YYYY-MM-DD.md` — daily session log

Per `BOOT.md` doc-ownership: daily session detail goes here, not in root `MEMORY.md`.
- Create if doesn't exist for today
- Bullet log: what was done, files changed, prototypes tested, key decisions
- Append (don't overwrite) if multiple sessions land on the same date

### Auto-memory (`~/.claude/projects/.../memory/`) — only if lessons earned

**Save only if:**
- Surprising or non-obvious lesson
- Validates or invalidates a pattern (record from success AND failure)
- Not derivable from current code state
- Not an activity log (those go in `memory/YYYY-MM-DD.md`)

**Do NOT save:**
- "Today we did X" recaps
- Code conventions, file paths, architecture (derivable)
- Debugging recipes (commit message is authoritative)

Format: frontmatter (name, description, type) + body. For `feedback` / `project` types include **Why:** and **How to apply:** lines so future-you can judge edge cases. Add a one-line entry to `MEMORY.md` index — never write memory content into the index itself.

**Checkpoint:** if no surprising lessons, skip auto-memory entirely. Memory bloat hurts more than memory absence.

---

## Chunk 3 — Optional residuals (trigger-gated)

Run only if specific triggers fired this session:

- **Doc-ownership drift:** if a file was retired or created, update `PROME/BOOT.md` doc-ownership table
- **Design-doc feedback:** if a prototype produced learnings, update the relevant design doc OR park as a v_next todo in SCRATCH — pick one home, not both
- **Autonomy change:** if Will granted/revoked permission, update `PROME/AUTONOMY.md` change log
- **External-system reference:** if a new external surface was discovered, save as `reference` auto-memory

If none triggered, skip.

---

## Chunk 4 — Git + report (Standard / Heavy; Light optional; Bounce skips)

### Git sequence

```
git status --short                  # check scope
git reset HEAD                      # clear pre-staged
git add PROME/<specific-files>      # explicit paths only, never -A or .
git diff --cached --stat            # sanity check
git commit -m "PROME: <subject>"    # subject line + body if needed
git pull --rebase                   # only if push rejected
git push
```

Commit message style (per recent history): subject = `PROME: <short one-liner>`; body explains WHY not WHAT; include `Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>` trailer.

If working tree outside `PROME/` is dirty (other agents' uncommitted work): commit your work, defer push, note pending push in `memory/YYYY-MM-DD.md` per root CLAUDE.md.

### Session summary to Will

One short message:
- **What landed:** 1–2 lines, concrete artifacts
- **What's pending:** anything carrying forward
- **Next session entry point:** one line, points at SCRATCH

---

## Skip rules

- **`PROME/TODAY.md`** — usually skip; STATUS designates `FLEET_SCAN.md` as its replacement surface for CC-Prome
- **`PROME/HANDOFF.md`** — Telegram-Prome handoff. Only update if this session's changes affect Telegram-Prome continuity (rare for pure CC work)
- **`AGENTS/<other>/` files** — never. Other agents own their state. Route via inbox if needed (and only with explicit per-instance authorization per the cross-agent-inbox-writes rule)
- **Root `CLAUDE.md` / shared files** — flag to Will, don't auto-edit. Will-approval gates the change.

---

## Cross-session behavioral rules

- **Behavior-language over hash-pinning** in state files (hashes go stale within 48h)
- **Verify state before propagating** — check ground truth, don't restate from prior surface text
- **Chunked updates** — sequence with checkpoints, don't batch 4–5 file edits in one pass
- **`trash` over `rm`** for deletions

---

## File-ownership reference

| File | Closeout action |
|---|---|
| `PROME/SCRATCH.md` | Full rewrite |
| `PROME/STATUS.md` | Surgical update |
| `PROME/CLAUDE_CODE_HANDOFF.md` | Append entry |
| `memory/YYYY-MM-DD.md` | Create or append |
| `~/.claude/.../memory/` (auto-memory) | Selective add only |
| `PROME/BOOT.md` | Only if doc-ownership drifted |
| `PROME/AUTONOMY.md` | Only if autonomy changed |
| `PROME/FLEET_SCAN.md` | Don't touch at closeout; refreshes on demand |
| `PROME/ORCHESTRAL_LAYER_DESIGN.md` | Only if prototypes produced feedback |
| `PROME/TODAY.md` | Usually skip |
| `PROME/HANDOFF.md` | Only if Telegram-Prome continuity affected |
| Root `CLAUDE.md`, `HEARTBEAT.md`, other shared | Flag to Will; don't auto-edit |
