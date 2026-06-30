# PROME CLOSEOUT

**Created:** 2026-05-18
**Owner:** Prome
**Purpose:** Repeatable session-end procedure to keep Prome's state files consistent across sessions. Run before `/clear`, `/new`, or session handoff.

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
2. Confirm no other agents have uncommitted work outside `PROME/` and any explicitly scoped paths for the session. The old `AGENTS/PROME/` tree is archived and no longer a live Prome work surface.
3. Mentally list this session's artifacts: proposals decided, files written, prototypes run, decisions made
4. Check transcript hygiene: if the session produced huge tool dumps, preserve the durable result in files/memory and avoid restating raw output. Prefer compact summaries unless full output matters.
5. Decide closeout scope:

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-day restart for config/tmux/clear/branch; you're coming right back within the hour | SCRATCH addendum (3-5 lines) | No |
| **Light** | Short session paused for hours; 1-2 artifacts; audit can wait for end-of-day Standard | SCRATCH full rewrite + STATUS surgical | Optional |
| **Standard** *(default)* | End-of-thread or end-of-day; multi-artifact session | All Chunk 1 + Chunk 2 daily log + Chunk 4 commit + `safe-push.sh` | Yes, auto-push |
| **Heavy** | Pattern-discovery session; new lessons/designs to fold | Standard + auto-memory + design-docs + Chunk 3 residuals | Yes, auto-push |

End-of-day always runs at least Standard so the audit trail catches up. 10 Bounces + 1 end-of-day Standard = no audit gap, just a rollup HANDOFF entry covering the day.

**Bounce procedure (the truly minimal):** append 3-5 lines to `PROME/SCRATCH.md` — (a) what just happened, (b) what's pending, (c) next-session entry point. No STATUS, no HANDOFF, no daily log, no auto-memory, no commit. Total time: ~30 seconds. Use only when you trust the next session will pick up within the hour and you accept the durability risk (no git checkpoint).

---

## Boot↔Closeout symmetry

Closeout is the **write-back tail** of boot (auto-memory `[[finding_closeout_as_writeback_tail]]`). What `BOOT.md` reads, this procedure writes back. Each pairing should round-trip on a Standard closeout; a boot-read surface with no closeout write goes stale silently.

| Surface | Boot (read) | Closeout (write-back) |
|---|---|---|
| `HANDOFF.md` | step 1 | Chunk 1 — append/rotate concise continuity entry when session affects future Prome state |
| `SCRATCH.md` | step 2 | Chunk 1 — full rewrite |
| `TODAY.md` | step 3 | Chunk 1 — surgical if date/catalysts moved (Standard+) |
| `ACTIVE_DECISIONS.md` | step 4 | Chunk 1 — surgical if a decision moved |
| `STATUS.md` | step 5 | Chunk 1 — surgical |
| `memory/YYYY-MM-DD.md` | on-demand | Chunk 2 — create/append |

**Intentionally one-way (no closeout write-back, by design):**
- `FLEET_SCAN.md` — conditional boot read; refreshed *on demand* by the fleet-scanner subagent, never at closeout.
- COMM mailbox + inbox / agent-outbox scan — ACKed / routed *inline during the session*, not deferred to closeout.

---

## Prome Write-Back Contract

Use this as the manual write-back feature. Do not auto-edit every surface; update only the owner doc whose state actually changed.

| If this changed | Write back to | Rule |
|---|---|---|
| Immediate next-session state | `PROME/SCRATCH.md` | Full rewrite for Standard/Heavy; Bounce may append 3–5 lines. |
| Cross-runtime continuity / decisions Will made | `PROME/HANDOFF.md` | Concise top entry only if future Prome needs it; keep latest 3–5 live. |
| Non-terminal decision state | `PROME/ACTIVE_DECISIONS.md` | Surgical row update; if unknown, mark `DEFERRED` / reconcile, never infer execution. |
| Agent/system health or work queue | `PROME/STATUS.md` | Surgical update; avoid repeating TODAY/HEARTBEAT market narrative. |
| Date/catalysts/operator checklist | `PROME/TODAY.md` | Surgical update only when date/gates/tasks moved. |
| Regime/thresholds/near gates | `HEARTBEAT.md` | Update after regime-level changes or when >48h stale during market week. |
| Daily activity / file changes | `memory/YYYY-MM-DD.md` | Append durable session log. |
| Durable insight / lesson | `MEMORY.md` or auto-memory | Promote sparingly; avoid activity logs. |

**Default:** if no owner state changed, do not write back. State bloat is worse than a quiet closeout.

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

### `PROME/ACTIVE_DECISIONS.md` — surgical update (only if a decision moved)

Boot-readable decision index (**paired with boot step 5**). Update a row whenever a non-terminal decision changed this session — new decision, state transition (DRAFT→PROPOSED→WILL_APPROVED), owner change, backstop met, executed/closed. Skip if no decision moved. Without this write-back the index silently goes stale — boot reads it but nothing refreshes it.

### `PROME/HANDOFF.md` — append/rotate concise continuity entry (Standard / Heavy only)

Cross-runtime Prome continuity role. Light skips unless future Prome state materially changed. Keep latest 3–5 entries live; archive older entries to `PROME/archive/`. NOT the place for full session narrative (that's SCRATCH / daily memory).
- **What landed** — one-line referents per artifact; point at SCRATCH/memory for headlines
- **Files edited** — compact list only when relevant
- **Decisions Will made this session** if they affect future behavior
- **Decisions needed from Will** if still active
- **Risks / blockers**
- **Next suggested work** (one-line pointer to SCRATCH, not a full restate)
- **Rules held to** (autonomy / scope verification)

**Doc-ownership separation (canonical homes):**
- **SCRATCH** = session narrative + next-session entry point (full headlines, "what just happened")
- **STATUS** = state tables only (agent health, Pending Work status, Active Decision Layer freshness); no narrative
- **HANDOFF** = concise cross-runtime continuity; references SCRATCH/memory for detail

**Checkpoint:** if any of these three files restate the same fact, drop it from STATUS and HANDOFF, keep it in SCRATCH. Cross-reference rather than duplicate.

---

## Chunk 2 — Memory (Standard / Heavy; Light + Bounce skip)

### `memory/YYYY-MM-DD.md` — daily session log

Per `BOOT.md` doc-ownership: daily session detail goes here, not in root `KERNELS.md` (the thesis-spine reference).
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
git status --short                                       # check scope
# modified files — path-scoped commit, NO staging step (never `git reset HEAD`):
git commit -m "PROME: <subject>" -- PROME/<file> PROME/<file>
# new untracked files — atomic add+commit of EXPLICIT paths (never `git add PROME/` as a directory):
git add -- PROME/<newfile> && git commit -m "PROME: <subject>" -- PROME/<newfile>
# mixed modified + new files: add only new explicit paths first, then commit all explicit paths:
git add -- PROME/<newfile> && git commit -m "PROME: <subject>" -- PROME/<modified> PROME/<newfile>
./scripts/safe-push.sh                                   # AUTO-PUSH at closeout — ff-gated, fails safe (Will 6/26, single-machine)
```

**Never `git reset HEAD`** — shared `.git/index` makes it a global unstage that races concurrent agents (auto-memory `[[finding_pathspec_commit_race_safety]]`, incident `8ac5bf71`). Matches root `CLAUDE.md` "Before committing".

**Auto-push at closeout (Will 2026-06-26, single-machine).** Run `./scripts/safe-push.sh` as the closeout tail — it ff-gates the push and safely sweeps the push-train (`[[finding_push_train_pattern]]`). It **fails safe**: a non-fast-forward ABORT = a second machine pushed → stop, do not force, flag to Will (the tripwire that single-machine was violated). The script never pulls/touches a shared working tree, so other agents' uncommitted edits are never at risk. *CANONICAL since 2026-06-26 — soak passed, Tier-1 promoted: root `CLAUDE.md` + `PROME/GIT_COORDINATION.md` + `[[feedback_defer_push_coordinate]]` all say auto-push-at-closeout. Lazy-sweep COMPLETE 2026-06-27 (18/21 agent CLAUDE.md flipped; 3 deliberate holdouts: TERRY self-sweep, WALTER architectural, YEYOU manual). See `PROME/ROSTER.md` + `PROME/AUTOPUSH_MIGRATION_PLAN.md`.*

Commit message style: subject = `PROME: <short one-liner>`; body explains WHY not WHAT when useful. **Option order matters:** put `-m` before `--`; everything after `--` is treated as a pathspec.

Other agents' uncommitted work outside `PROME/` does NOT block the push — `safe-push.sh` pushes only committed work and never touches the tree. It will sweep any other agent's committed-but-unpushed commits (the push-train — expected/correct). Only a non-ff abort stops it (cross-machine push → flag to Will).

### Session summary to Will

One short message:
- **What landed:** 1–2 lines, concrete artifacts
- **What's pending:** anything carrying forward
- **Next session entry point:** one line, points at SCRATCH

---

## Skip rules

- **`PROME/TODAY.md`** — **paired with boot step 2.** Surgical update if the date rolled or catalysts/levels changed (Standard+); skip on Bounce/Light. (Earlier guidance treated `FLEET_SCAN.md` as a CC replacement surface, but TODAY is still read at boot and drives day/week framing — keep it current.)
- **`PROME/HANDOFF.md`** — cross-runtime Prome continuity. Update only when the session changes future Prome state; keep it concise and rotate/archive older entries.
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
| `PROME/ACTIVE_DECISIONS.md` | Surgical if a decision moved (boot step 5 pair) |
| `PROME/HANDOFF.md` | Append/rotate concise cross-runtime continuity entry when needed |
| `memory/YYYY-MM-DD.md` | Create or append |
| `~/.claude/.../memory/` (auto-memory) | Selective add only |
| `PROME/BOOT.md` | Only if doc-ownership drifted |
| `PROME/AUTONOMY.md` | Only if autonomy changed |
| `PROME/FLEET_SCAN.md` | Don't touch at closeout; refreshes on demand |
| `PROME/ORCHESTRAL_LAYER_DESIGN.md` | Only if prototypes produced feedback |
| `PROME/TODAY.md` | Usually skip unless date/catalysts/levels moved |
| Root `CLAUDE.md`, `HEARTBEAT.md`, other shared | Flag to Will; don't auto-edit unless explicitly approved |
