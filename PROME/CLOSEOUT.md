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
   - **Light:** state files only (SCRATCH + STATUS + handoff). For short sessions with one or two artifacts.
   - **Standard:** state files + daily log + commit. Default.
   - **Heavy:** standard + auto-memory + design-doc updates + residual cleanup. For sessions that produced new patterns or learnings.

---

## Chunk 1 — State files (mandatory)

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

### `PROME/CLAUDE_CODE_HANDOFF.md` — append session entry

Per `PROME/CLAUDE.md` spec:
- What changed
- Files edited (compact list)
- Decisions needed from Will
- Risks / blockers
- Next suggested work

**Checkpoint:** flag if any of these three files restate the same fact (doc-ownership violation). Pick one home and reference from the other two.

---

## Chunk 2 — Memory (selective)

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

## Chunk 4 — Git + report

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
