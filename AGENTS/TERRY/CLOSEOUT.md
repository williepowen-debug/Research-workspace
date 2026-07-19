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
| `PAPER_BOOK.tsv` | A card reached would-fire state this session (any card — auto-fill is independent of Will's approval) | Log the paper-fill row + set `will_decision` (APPROVED/PASSED/NO-DECISION). Fill = ask-for-buys/bid-for-sells at the trigger timestamp + wide-spread penalty + auditable `entry_basis`, **never mid** — full rule in `PAPER_BOOK_DESIGN.md` §Fill rules. PAPER only, survivorship rule (never delete a losing row). |

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
- **Push: TERRY self-sweeps at closeout** (named live auto-push exception in root canon). Run `scripts/safe-push.sh` from the repo root — ff-gated, fails safe, never force-pushes. One push sweeps everyone's committed work (the push-train).
- **✅ Push-success check (mandatory):** after safe-push, confirm `git rev-list --left-right --count origin/master...HEAD` = `0 0`. **If it's not 0/0, the push did NOT land — you're in the non-ff branch below. Do not report "pushed" until you've seen 0/0.**
- Trailer: `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.

### If safe-push aborts non-ff — pick the branch by the state of the tree (validated 2026-07-17)
The old "just `git pull --rebase`" advice **fails when other agents have uncommitted work**, because rebase refuses on a dirty index/tree and a pull can clobber their changes. Branch first:

- **A) Working tree clean outside `AGENTS/TERRY/`** → `git pull --rebase` then re-push. Routine under serial multi-machine.
- **B) Foreign uncommitted work present** (other agents' staged/unstaged/untracked files — the common case) → **do NOT pull/rebase in place.** Two options:
  - **B1 (defer, lowest risk):** commit locally, leave the push. Note the pending push + the local SHA in MEMORY (`## Current Session` Status line). It sweeps on the next clean push. Root protocol Option B.
  - **B2 (push now, isolated worktree — use when the work must go live this session):** replay local commits onto origin without touching the main tree:
    1. `git worktree add --detach <tmp outside repo> <local-HEAD-sha>`
    2. in it: `git rebase origin/master` (replays ALL local-ahead commits — yours + any other agent's unpushed commits = the push-train; disjoint dirs → clean)
    3. `git push origin HEAD:master` — **fast-forward, never `--force`** (destroying another agent's committed origin work is a hard-stop; stacking on top preserves everyone)
    4. back in main: `git reset --soft origin/master` (moves the branch pointer only — leaves the foreign index/tree untouched)
    5. `git worktree remove <tmp>`
  - **⚠️ Post-realign verification (B2, mandatory):** `reset --soft` can leave the main tree *behind* origin on a foreign dir → a **staged deletion of another agent's committed work** (2026-07-17: BRENT's file showed staged-`D`). Confirm `0 0` vs origin AND scan `git status --short` for any `D `/`M ` on a dir you didn't touch; `git restore --source=HEAD --staged --worktree -- <that dir>` to materialize origin's version. Never leave a behind-origin staged-D for someone to accidentally commit.
- **🚩 Desync detection → flag Will:** if foreign "uncommitted" changes turn out to already match origin (`git diff origin/master -- AGENTS/<other>/` is empty — the work was committed from another machine), that's a **two-machine overlap**, which serial multi-machine forbids. Say so in the report; don't silently absorb it. Escalate (per-agent-branches tripwire) if non-ff recurs mid-session or a rebase conflicts outside `AGENTS/TERRY/`.

**Report to Will/Prome:** what landed (concrete) · what's pending · next entry point (points at MEMORY Next-Session) · **any push deferral or two-machine desync observed.**

---

## Skip / never rules

- `AGENTS/<other>/` — never edit; route cross-agent via `outbox/` (🔴 only — outbox restraint).
- `FORGE/`, root `CLAUDE.md`, `HEARTBEAT.md` — flag to Will/Prome; don't auto-edit. (Approved cards land in FORGE at execution = a Will/FORGE step.)
- Runtime outputs (`scripts/.cache/`, `grades/`) are gitignored — never commit.
- `trash`/`gio trash` over `rm`. Read before Edit. Chunk multi-file updates.
