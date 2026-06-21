# LIQUID CLOSEOUT

**Created:** 2026-05-20
**Owner:** LIQUID agent (Claude Code)
**Purpose:** Repeatable session-end procedure to maintain consistency across LIQUID sessions. Run before `/clear`, `/new`, or session handoff.

> Companion to `CLAUDE.md` SPAWN PROTOCOL (session start). Follow root `CLAUDE.md` for git protocol details. Tier model mirrors `PROME/CLOSEOUT.md` for cross-agent vocabulary consistency.

---

## When to run

- Before `/clear` or `/new`
- Before stepping away from a long session
- After any session that changed state, refreshed data, or fired a cross-agent signal

Skip for casual one-off exchanges with no artifacts. **Live-event override:** if a regime-moving print / active catalyst window is in progress, DEFER the full write-back — snapshot STATUS as a working dashboard and keep EXECUTE open until the event stabilizes (mirrors CLAUDE.md SPAWN PROTOCOL step 6).

---

## Pre-closeout (~1 min)

1. `git status --short` — review what's changed
2. Confirm no other agents have uncommitted work outside `AGENTS/LIQUID/` (per root CLAUDE.md "Before pulling"). If dirty: per "Agent Git Isolation" rule, commit local and defer push.
3. Mentally inventory session artifacts:
   - **Did I pull fresh tape?** → dashboard cells need refresh
   - **Did any threshold breach?** → cross-agent signal candidate (CLAUDE.md table)
   - **Did a prediction resolve?** → PREDICTIONS.tsv update
   - **Did I produce a durable finding?** → KB.tsv entry candidate
   - **Did I touch positions/proposals?** → STATUS Active Positions/Proposals
   - **Did this session add a non-obvious lesson?** → auto-memory candidate
4. Decide closeout tier:

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-session restart; coming back within the hour | MEMORY.md CURRENT block addendum (3-5 lines) | No |
| **Light** | Short session paused for hours; 1-2 artifacts; audit can wait for end-of-day | STATUS surgical + MEMORY surgical | Optional |
| **Standard** *(default)* | End-of-thread or end-of-day; multi-artifact session | Chunk 1 + Chunk 2 (if triggered) + Chunk 5 | Yes |
| **Heavy** | Pattern-discovery session; durable findings; structural shift | Standard + Chunk 3 + Chunk 4 (auto-memory) | Yes |

End-of-day always runs at least Standard so the audit trail catches up.

**Bounce procedure:** append 3-5 lines to MEMORY.md CURRENT SESSION block — (a) what just happened, (b) what's pending, (c) next-session entry point. No STATUS, no commit. Total time: ~30 seconds. Use only when next session picks up within the hour and you accept the durability risk (no git checkpoint).

---

## Chunk 1 — State (Light / Standard / Heavy)

### `STATUS.md` — surgical update (not rewrite)

- **Header:** `Last Updated:` stamp + status emoji (🟢/🟡/🟠/🔴) match current risk read
- **Dashboards (3 separate):** Credit / Domestic Plumbing / Foreign Official — refresh any cells touched this session. Don't mix categories (per CLAUDE.md DASHBOARD STRUCTURE rule).
- **Thresholds table:** current values vs trigger levels
- **Cross-Domain Signals:** this session's findings, routed to target agents
- **Active Proposals / Active Positions:** reflect any cuts, rolls, holds
- **Danger Windows + Watch:** forward-only (drop resolved windows)
- **Line count:** <250 (CLAUDE.md rule). If over: prune to `archive/` or `domain/sources/`.

### `MEMORY.md` — session block rotation

- Promote previous CURRENT SESSION → PRIOR SESSION (rename heading)
- Write new CURRENT SESSION block: **Context** (1 line), **Delivered** (bullets), **Open follow-ups**
- Update NEXT SESSION list — remove completed items, add deferred items
- **Durable Findings:** append ONLY if new structural insight survives the current episode (most sessions: no append)

### `CALENDAR.md` — event-gated

Touch only if dates rolled forward, new windows added, or events resolved. Most sessions: skip.

---

## Chunk 2 — Workbook (trigger-gated)

Touch only the rows below that this session actually changed.

| File | Trigger to touch | Action |
|---|---|---|
| `workbook/KB.tsv` | Session produced a durable finding (structural, not episode) | Append KB-LIQ-NNN row with date/category/tag/fact/source/conf/status/stale_by/notes. Cross-link to source file if applicable. |
| `workbook/PREDICTIONS.tsv` | A prediction resolved (achieved, falsified, expired) | Update Status / Date_Resolved / Outcome / Notes |
| `workbook/CATALYSTS.tsv` | A dated catalyst was added, resolved, or its date shifted | Add/update/retire the row; keep `CALENDAR.md` (human twin) in sync — no event-set divergence; run `scripts/boot.py --selftest` to validate |
| `workbook/KILL_MEMO_HY_OAS_260.md` | Trigger ladder thresholds changed or a trigger fired | Update tier rows; mark fired triggers |
| `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` | Q1 BDC marks landed or new mark divergence | Update OBDC/ARCC/BXSL/MAIN rows |
| `workbook/FLOW.tsv` / `workbook/VX.tsv` | A registry entry was touched (status change, new vector) | Surgical row update |
| `workbook/AUCTION_FRAMEWORK.md` / `TIC_FRAMEWORK.md` / `CUSTODIAL_VELOCITY_PROTOCOL.md` | Methodology changed (rare) | Surgical edit |

**Don't auto-touch** at closeout: `domain/sources/`, `archive/`, `thesis/`. Those are reference layers.

---

## Chunk 3 — Cross-agent signals (trigger-gated)

If a 🔴 or 🟠 cross-agent threshold breached this session (per CLAUDE.md CROSS-AGENT SIGNALS table):

1. **Write outbox file:** `outbox/YYYY-MM-DD_to-[target]_[short_description].md` using the standard format (headline / detail / source / priority).
2. **Append to `AGENTS/SIGNALS.md`:** `| DATE | LIQUID | TARGET | 🔴/🟠 | Description |` row.
3. HERMES sweeps outboxes and delivers. **Never write directly to another agent's inbox** (per "Cross-Agent Inbox Writes Exception-Only" memory rule).

If no threshold fired this session: skip entirely.

---

## Chunk 4 — Auto-memory (Heavy only, selective)

Save to `~/.claude/projects/-home-willi-Research-workspace/memory/` only if:
- Surprising or non-obvious lesson
- Pattern validated or invalidated (record from success AND failure)
- Not derivable from current files (KB.tsv is the right home for durable findings within LIQUID; auto-memory is for cross-agent / cross-session lessons about *how to work*)
- Not an activity log

**Do NOT save:**
- "Today we did X" recaps
- Framework details that belong in `workbook/KB.tsv`
- Debugging recipes (commit message is authoritative)
- File paths, code conventions, architecture (derivable)

Format: frontmatter (name, description, type) + body. For `feedback` / `project` types include **Why:** and **How to apply:** lines.

If no surprising lessons: skip.

---

## Chunk 5 — Git + report (Standard / Heavy; Light optional; Bounce skips)

### Git sequence (pathspec-scoped — **never `git reset HEAD`**, shared `.git/index`)

**Modified files** — path-scoped commit, no separate staging step:
```
git status --short                                       # check scope; note dirty OUTSIDE LIQUID/
git commit AGENTS/LIQUID/<file> [<file2> ...] -m "LIQUID: <subject>"
```

**New untracked files** — atomic add+commit, explicit paths (never `git add AGENTS/LIQUID/` as a directory — sweeps unintended files):
```
git add AGENTS/LIQUID/<specific-new-file>
git diff --cached --stat                                 # optional sanity: nothing unexpected
git commit AGENTS/LIQUID/<specific-new-file> [...] -m "LIQUID: <subject>"
```

- **Never `git reset HEAD`** — shared index makes it a global unstage that races other agents' concurrent stages (root CLAUDE.md; incident `8ac5bf71`, memory `finding_pathspec_commit_race_safety`).
- **Push is Will-coordinated — defer by default.** Commit locally; note any pending push in the MEMORY CURRENT block. A session-end push races other agents' unpushed commits on the shared branch; in a Will-opened window one agent's push sweeps everyone's committed work (`finding_push_train_pattern`).

Commit-message style: `LIQUID: <short one-liner>` subject; body explains WHY when non-obvious; `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` trailer.

**If working tree outside LIQUID is dirty** (other agents' uncommitted work): commit your work locally, **defer push**, note pending push in MEMORY CURRENT block (per root CLAUDE.md Option B + "Agent Git Isolation" memory rule). Next session pushes when working tree is cleaner.

### Session summary to Will

One short message:
- **What landed:** 1–2 lines, concrete artifacts
- **What's pending:** anything carrying forward
- **Next session entry point:** one line, points at MEMORY NEXT SESSION

---

## Skip rules

- **`AGENTS/<other>/` files** — never edit. Route via `outbox/` if cross-agent signal needed (per Chunk 3).
- **Inbox processing** — only on inbox-spawn task (per CLAUDE.md MAIL rule). Don't sweep `inbox/` at closeout.
- **`HEARTBEAT.md`** — flag to Prome via outbox; never commit yourself (per root CLAUDE.md scope rule).
- **Root `CLAUDE.md`, `AGENTS/SIGNALS.md` structure changes, `FORGE/`** — flag to Will/Prome; don't auto-edit.
- **`thesis/`, `domain/sources/`, `archive/`** — don't auto-touch at closeout. These are reference layers; touch only when explicitly working on them.

---

## Cross-session behavioral rules

- **Behavior-language over hash-pinning** in state files (hashes go stale within 48h)
- **Verify state before propagating** — check ground truth, don't restate from prior surface text
- **Read before editing** — never `Edit` without `Read` in the same turn
- **Chunked updates** — sequence with checkpoints; don't batch 4–5 file edits in one pass
- **`trash` over `rm`** for deletions

---

## File-ownership reference

| File | Closeout action |
|---|---|
| `STATUS.md` | Surgical (header / 3 dashboards / thresholds / signals / proposals / positions / windows) |
| `MEMORY.md` | Promote CURRENT→PRIOR + new CURRENT + update NEXT |
| `CALENDAR.md` | Event-gated — only if dates roll or events resolve |
| `IDENTITY.md` / `STRATEGY.md` / `USER.md` / `CREDIT_THRESHOLDS.md` | Don't auto-touch; revise only when scope/thesis shifts |
| `thesis/THESIS.md` / `thesis/CHANGELOG.md` / `thesis/TIMELINE.md` | Don't auto-touch; thesis-rewrite sessions only |
| `workbook/KB.tsv` | Append only if durable finding (most sessions: skip) |
| `workbook/PREDICTIONS.tsv` | Only if a prediction resolved |
| `workbook/CATALYSTS.tsv` | Sync with `CALENDAR.md` on any dated-catalyst add/resolve (boot countdown reads it); `boot.py --selftest` to validate |
| `workbook/KILL_MEMO_HY_OAS_260.md` | Only if trigger ladder changed |
| `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` | Only if Q1 marks landed |
| `workbook/FLOW.tsv` / `workbook/VX.tsv` | Only if registry entry updated |
| `workbook/AUCTION_FRAMEWORK.md` / `TIC_FRAMEWORK.md` / `CUSTODIAL_VELOCITY_PROTOCOL.md` | Only if methodology changed (rare) |
| `outbox/` | Trigger-gated — only if cross-agent threshold fired |
| `AGENTS/SIGNALS.md` (root) | Append only on cross-agent threshold breach |
| `~/.claude/.../memory/` (auto-memory) | Selective; Heavy tier only |
| `domain/sources/`, `archive/` | Don't auto-touch |
| `AGENTS/<other>/` | Never |
| Root `CLAUDE.md`, `HEARTBEAT.md`, `FORGE/` | Flag to Will/Prome; don't auto-edit |
