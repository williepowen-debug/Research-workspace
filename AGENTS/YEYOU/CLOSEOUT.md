# YEYOU CLOSEOUT

**Created:** 2026-06-24
**Owner:** YEYOU
**Purpose:** Repeatable session-end procedure to maintain consistency across Claude Code YEYOU sessions (manual/branch model; OpenClaw/VPS cut 2026-06-26). Run before `/clear`, `/new`, or session handoff.

> Companion to `AGENTS/YEYOU/CLAUDE.md` (session start) and `AGENTS/YEYOU/SOUL.md` (identity). Follow root `CLAUDE.md` for git protocol details.

---

## When to run

- Before `/clear` or `/new`
- Before stepping away from a long session
- After any session that produced review artifacts worth persisting

Skip for casual one-off exchanges with no artifacts.

---

## Pre-closeout (~1 min)

1. `git status --short` — review what's changed
2. Confirm no other agents have uncommitted work outside `AGENTS/YEYOU/` and `AGENTS/YEYOU/outbox/`. The old `AGENTS/PROME/` tree is archived and no longer a live Prome work surface.
3. Mentally list this session's artifacts: findings, reviews, proposals, handoffs to PROME
4. Check transcript hygiene: if the session produced huge tool dumps, preserve the durable result in files/memory and avoid restating raw output. Prefer compact summaries unless full output matters.
5. Decide closeout scope:

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-day restart for config/tmux/clear/branch; you're coming right back within the hour | `AGENTS/YEYOU/STATUS.md` append 3-5 lines | No |
| **Light** | Short session paused for hours; 1-2 artifacts; audit can wait for end-of-day Standard | `AGENTS/YEYOU/STATUS.md` surgical + `reviews/REVIEW_LOG.tsv` append | Optional |
| **Standard** *(default)* | End-of-thread or end-of-day; multi-artifact session | Chunk 1 + Chunk 2 daily log + Chunk 4 commit; push only if Will approves | Yes, push gated |
| **Heavy** | Pattern-discovery session; new lessons/designs to fold | Standard + auto-memory + design-docs + Chunk 3 residuals | Yes, push gated |

End-of-day always runs at least Standard so the audit trail catches up. 10 Bounces + 1 end-of-day Standard = no audit gap, just a rollup HANDOFF entry covering the day.

**Bounce procedure (the truly minimal):** append 3-5 lines to `AGENTS/YEYOU/STATUS.md` — (a) what just happened, (b) what's pending, (c) next-session entry point. No daily log, no auto-memory, no commit. Total time: ~30 seconds. Use only when you trust the next session will pick up within the hour and you accept the durability risk (no git checkpoint).

---

## Boot↔Closeout symmetry

Closeout is the **write-back tail** of boot. What `CLAUDE.md` reads, this procedure writes back. Each pairing should round-trip on a Standard closeout; a boot-read surface with no closeout write goes stale silently.

| Surface | Boot (read) | Closeout (write-back) |
|---|---|---|
| `AGENTS/YEYOU/STATUS.md` | step 2 | Chunk 1 — surgical update |
| `AGENTS/YEYOU/reviews/REVIEW_LOG.tsv` | — | Chunk 1 — append session log |
| `AGENTS/YEYOU/MEMORY.md` | step 4 | Chunk 2 — durable quirks / false-positive rules only |

**Intentionally one-way (no closeout write-back, by design):**
- `AGENTS/YEYOU/outbox/` — contents are ACKed / routed *inline during the session*, not deferred to closeout.
- Cross-silo reviews — findings are written to `AGENTS/YEYOU/reviews/` and passed to PROME via outbox; PROME reads those directly (not via inbox).

---

## YEYOU Write-Back Contract

Use this as the manual write-back feature. Do not auto-edit every surface; update only the owner doc whose state actually changed.

| If this changed | Write back to | Rule |
|---|---|---|
| Immediate next-session state | `AGENTS/YEYOU/STATUS.md` | Surgical update for Light/Standard/Heavy; Bounce may append 3-5 lines. |
| Session log (findings, reviews, proposals) | `AGENTS/YEYOU/reviews/REVIEW_LOG.tsv` | Append (don't overwrite) for Standard/Heavy; Light skips. |
| Daily activity / file changes | `AGENTS/YEYOU/reviews/REVIEW_LOG.tsv` | Append when review/session-relevant; skip empty hygiene |
| Durable insight / lesson | `AGENTS/YEYOU/MEMORY.md` or auto-memory | Promote sparingly; avoid activity logs. |

**Default:** if no owner state changed, do not write back. State bloat is worse than a quiet closeout.

---

## Chunk 1 — State files (Light / Standard / Heavy; Bounce skips except STATUS append)

### `AGENTS/YEYOU/STATUS.md` — surgical update (not rewrite)

- Update `Updated:` timestamp
- Adjust `Pending Reviews` table — mark completed, add new, update priorities
- Update `Active Reviews` table (✅ / ⚠️ / ❌)
- Update `Next Best Action` — one concrete move

### `AGENTS/YEYOU/reviews/REVIEW_LOG.tsv` — append (not rewrite)

- Append session log entry: timestamp, agent reviewed, finding, priority, status
- Use TSV format (tab-separated values)
- Don't overwrite; append new entries

---

## Chunk 2 — Memory (Standard / Heavy; Light + Bounce skip)

### `AGENTS/YEYOU/reviews/REVIEW_LOG.tsv` — daily/session log

Per `AGENTS/YEYOU/CLAUDE.md` doc-ownership: session detail goes here, not in root `MEMORY.md`.
- Append findings, PASS rows, or session-relevant review/proposal rows.
- Do not overwrite; preserve finding lifecycle history.
- Skip if no review/session-relevant state changed.

### Auto-memory (`~/.claude/projects/.../memory/`) — only if lessons earned

**Save only if:**
- Surprising or non-obvious lesson
- Validates or invalidates a pattern (record from success AND failure)
- Not derivable from current code state
- Not an activity log (those go in `AGENTS/YEYOU/reviews/REVIEW_LOG.tsv` only when review/session-relevant)

**Do NOT save:**
- "Today we did X" recaps
- Code conventions, file paths, architecture (derivable)
- Debugging recipes (commit message is authoritative)

Format: frontmatter (name, description, type) + body. For `feedback` / `project` types include **Why:** and **How to apply:** lines so future-you can judge edge cases. Add a one-line entry to `AGENTS/YEYOU/MEMORY.md` index — never write memory content into the index itself.

**Checkpoint:** if no surprising lessons, skip auto-memory entirely. Memory bloat hurts more than memory absence.

---

## Chunk 3 — Optional residuals (trigger-gated)

Run only if specific triggers fired this session:

- **Doc-ownership drift:** if a file was retired or created, update `AGENTS/YEYOU/CLAUDE.md` doc-ownership table
- **Design-doc feedback:** if a prototype produced learnings, update the relevant design doc OR park as a v_next todo in reviews — pick one home, not both
- **Autonomy change:** if Will granted/revoked permission, update `AGENTS/YEYOU/SOUL.md` change log
- **External-system reference:** if a new external surface was discovered, save as `reference` auto-memory

If none triggered, skip.

---

## Chunk 4 — Git + report (Standard / Heavy; Light optional; Bounce skips)

### Git sequence

```
git status --short                                       # check scope
# modified files — path-scoped commit, NO staging step (never `git reset HEAD`):
git commit -m "YEYOU: <subject>" -- AGENTS/YEYOU/<file> AGENTS/YEYOU/<file>
# new untracked files — atomic add+commit of EXPLICIT paths (never `git add AGENTS/YEYOU/` as a directory):
git add -- AGENTS/YEYOU/<newfile> && git commit -m "YEYOU: <subject>" -- AGENTS/YEYOU/<newfile>
# mixed modified + new files: add only new explicit paths first, then commit all explicit paths:
git add -- AGENTS/YEYOU/<newfile> && git commit -m "YEYOU: <subject>" -- AGENTS/YEYOU/<modified> AGENTS/YEYOU/<newfile>
git pull --rebase                                        # only if push rejected or before push when safe
git push                                                 # only on Will's explicit push call
```

**Never `git reset HEAD`** — shared `.git/index` makes it a global unstage that races concurrent agents (auto-memory `[[finding_pathspec_commit_race_safety]]`, incident `8ac5bf71`). Matches root `CLAUDE.md` "Before committing". **Pushing is a separate gate** — commit locally freely, but push only when Will coordinates it (concurrent agents may have unpushed local commits; `[[feedback_defer_push_coordinate]]`).

**Git pull constraint:** `git pull --rebase` is okay only in a clean/safe flush. Do NOT run `git pull --rebase` during dirty closeout; coordinate via `PROME/GIT_COORDINATION.md`.

Commit message style: subject = `YEYOU: <short one-liner>`; body explains WHY not WHAT when useful. **Option order matters:** put `-m` before `--`; everything after `--` is treated as a pathspec.

If working tree outside `AGENTS/YEYOU/` is dirty (other agents' uncommitted work): commit your work, defer push, and note pending push in `AGENTS/YEYOU/STATUS.md` or `AGENTS/YEYOU/reviews/REVIEW_LOG.tsv`.

### Session summary to PROME

One short message (via outbox):

- **What landed:** 1–2 lines, concrete artifacts
- **What's pending:** anything carrying forward
- **Next session entry point:** one line, points at STATUS

---

## Skip rules

- **`AGENTS/YEYOU/CLAUDE.md`** — **paired with boot step 1.** Surgical update only if doc-ownership drifted; skip otherwise. (YEYOU does not maintain market catalyst framing; that's PROME's job.)
- **`AGENTS/YEYOU/HANDOFF.md`** — cross-runtime YEYOU continuity. Update only when the session changes future YEYOU state; keep it concise and rotate/archive older entries.
- **`AGENTS/PROME/` files** — never. Other agents own their state. Route via outbox if needed (and only with explicit per-instance authorization per the cross-agent-inbox-writes rule)
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
| `AGENTS/YEYOU/STATUS.md` | Surgical update (Bounce/Light/Standard/Heavy) |
| `AGENTS/YEYOU/reviews/REVIEW_LOG.tsv` | Append (Standard/Heavy) |
| `AGENTS/YEYOU/MEMORY.md` | Update only for durable quirks / false-positive rules |
| `~/.claude/.../memory/` (auto-memory) | Selective add only |
| `AGENTS/YEYOU/CLAUDE.md` | Only if doc-ownership drifted |
| Root `CLAUDE.md`, `HEARTBEAT.md`, other shared | Flag to Will; don't auto-edit unless explicitly approved |

---

## Comparison with PROME CLOSEOUT

| Aspect | PROME | YEYOU |
|---|---|---|
| **Primary state surfaces** | SCRATCH, STATUS, ACTIVE_DECISIONS, HANDOFF | STATUS, REVIEW_LOG.tsv |
| **Memory storage** | `memory/YYYY-MM-DD.md` + auto-memory | `AGENTS/YEYOU/MEMORY.md` + review ledger |
| **Git scope** | Root `PROME/` + explicitly scoped root files | Root `AGENTS/YEYOU/` + outbox |
| **Commit examples** | `git commit -m "PROME: <subject>" -- PROME/<file>` | `git commit -m "YEYOU: <subject>" -- AGENTS/YEYOU/<file>` |
| **Push gate** | Will-coordinated flush | Will-coordinated flush |
| **Cross-agent handoff** | Direct read of outbox / live `PROME/` docs | Via outbox → PROME reads directly |
| **Bounce procedure** | Append 3-5 lines to SCRATCH | Append 3-5 lines to STATUS |
| **Skip rules** | `PROME/TODAY.md`, `PROME/HANDOFF.md`, `AGENTS/<other>/` files | `CLAUDE.md` (doc-ownership only), `HANDOFF.md`, `AGENTS/PROME/` files |
| **Symmetry** | Boot ↔ Closeout (write-back tail) | Boot ↔ Closeout (write-back tail) |
| **Chunked updates** | Yes (Chunk 1-4) | Yes (Chunk 1-4) |
| **Pathspec-only commits** | Yes (no `git reset HEAD`) | Yes (no `git reset HEAD`) |

**Key differences:**
- PROME has SCRATCH (narrative), ACTIVE_DECISIONS (decision index), and HANDOFF (cross-runtime continuity); YEYOU has STATUS (state tables) and REVIEW_LOG.tsv (session log).
- PROME's Bounce appends to SCRATCH; YEYOU's Bounce appends to STATUS.
- PROME's cross-agent handoff is direct read of outbox / live `PROME/` docs; YEYOU's cross-agent handoff is via outbox → PROME reads directly.
- PROME's commit examples use root `PROME/`; YEYOU's commit examples use root `AGENTS/YEYOU/`.
- PROME's Skip rules mention `TODAY.md` (market catalyst framing); YEYOU's Skip rules only mention `CLAUDE.md` (doc-ownership drift) and `HANDOFF.md`.

**Key similarities:**
- Both use pathspec-only commits (no `git reset HEAD`)
- Both use behavior-language over hash-pinning in state files
- Both use chunked updates with checkpoints
- Both use `trash` over `rm` for deletions
- Both use `git pull --rebase` before push (when safe, but with constraint during dirty closeout)
- Both use `git push` only on Will-coordinated flush
- Both have Bounce/Light/Standard/Heavy closeout tiers

---

**Status:** ✅ YEYOU closeout procedure is set up and aligned with PROME's protocol, with YEYOU-specific state surfaces (STATUS, REVIEW_LOG.tsv) instead of copied PROME assumptions.
