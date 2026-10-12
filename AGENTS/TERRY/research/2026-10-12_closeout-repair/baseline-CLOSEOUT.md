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

### 🔴 STATUS banner discipline — **CURRENT STATE ON TOP, ALWAYS. REWRITE IT IN PLACE; NEVER APPEND BELOW IT.**

> **The rule:** `STATUS.md` opens with a single **`★ CURRENT STATE`** block that is **rewritten in place every session**. Dated banners live **below** it, newest-first, and are **demoted, never promoted**. When a session corrects or withdraws a claim, **strike it inline in the banner that made it** *and* make sure the CURRENT STATE block carries the operative version. A struck claim stays visible; it does not stay *first*.
>
> **Why this is a rule and not a preference (RAV review, 2026-07-30).** This file was written append-below-a-dated-banner, so **the first thing any reader saw was by construction the most outdated state.** On 7/30 the ~10:40 banner still led with *"THE LOSS CAME FROM THE ENTRY"*, *"beta CORRECTED 0.53"* and *"MY EXECUTION WAS BEATEN, n=2"* — after later addenda **the same day** had superseded the first two and **withdrawn the third in full.** Three correction passes all appended *below* the wrong text instead of replacing it.
>
> ⚠️ **`boot.py` prints a "STATUS head" block, so the stale banner is literally the first thing the next session reads — and on 7/30 I read past it at my own boot.** That is what makes this a state defect rather than a formatting one: the file's most-read line was its least-current.
>
> ⚠️ **`ledger_sweep.py` CANNOT catch this and must not be extended to try.** Check B matches `(label, value)` pairs — it sees a struck *value*, not *"an old conclusion still appears first"* or *"a prose claim was narrowed."* A regex reaching for those reproduces the bare-numeric false-positive class (~123 hits, 7/30 morning) that made the tool useless. **This is a convention, enforced by write-back; the guard is deliberately not the answer.**

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

### 🔴 MANDATORY, NOT TRIGGER-GATED — run the ledger sweep before Chunk 4

```bash
(cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/scripts/ledger_sweep.py)
```

**Exit 1 = do not close out until it is clean or you have written down why a finding is being left.** It takes ~2 seconds and checks the two things this desk demonstrably cannot do by hand:

- **A. STATE AGREEMENT** — every surface naming a `setup_id` (the card, `SETUPS.tsv`, `setups/INDEX.md`, `TRADE_BOOK.md`) claims the same current state.
- **B. SUPERSEDED-VALUE DRIFT** — a value you corrected (`label ~~old~~ → new`) in a recent commit is not still asserted naked somewhere else.
- **I. INBOX AT CLOSEOUT** *(added 2026-08-27, Will-directed)* — **undrained packets in `inbox/` and `inbox/<AGENT>/`.** ⛔ **ADVISORY, NEVER BLOCKING — and that is deliberate.** **Why it exists:** `boot.py` reports the inbox, but a boot report is a **SNAPSHOT** — packets landing *after* the drain are invisible for the rest of the session and nothing re-checks. **Live instance the day it shipped: SAM delivered a 20-day-owed branch at 10:46, minutes after the boot drain took the inbox 4 → 0, and it surfaced only because Will asked.** The fix could not be *"remember to look again"* (`[[finding_mechanize_the_cap_not_the_ritual]]`), so it went where closeout already stops.
  - **Read the AGE, it is the whole signal:** `UNCOMMITTED` = a peer wrote it and hasn't committed, **in flight right now** · `0d` = landed today, **most likely mid-session — the gap this closes** · **`≥1d` = it SURVIVED A BOOT REPORT, which is a DRAIN failure and the more serious of the two.** *(Age comes from the **git-add commit**, never `mtime` — git sync restamps mtime and it fails FALSE-NEGATIVE, `[[finding_mtime_is_corrupted_by_git_sync]]`.)*
  - ⛔ **NEVER `git mv` a packet to `processed/` just to clear this line.** **An unread packet filed as consumed is strictly worse than one left visible** — it manufactures a false consumption record and the next boot stops shouting. **"Arrived 16:29, consuming next boot" is a legitimate disposition**; state it in the commit message and close out.
  - **This is exactly why it does not block:** if it did, the *cheapest* remedy would be the file-without-reading move above. **A guard whose cheapest remedy is a bad action buys nothing** (`[[finding_gate_calibration_is_a_claim_about_its_remedys_price]]`). ⚠️ **Do not "harden" it into the blocking set later without re-arguing that.**
  - **Scope:** excludes `processed/` at every level and **excludes `inbox/WILL/`** (Will's raw drop zone — a different lane, reported separately by `boot.py`). **5 permanent selftest cases** cover those exclusions, because a false positive here trains the reader to ignore the line, which is the only way an advisory guard dies.

> **Why this is mandatory rather than trigger-gated.** Every entry in the table above is gated on *"did I touch this?"* — and the drift class is precisely the case where **you were sure you had.** On 2026-07-30 this recurred **five times in one session**: the diesel verdict sat CONDITIONAL on three ledgers 45 minutes after the card moved to NO AT THIS PRICE; three VIXCS corrections reached the banners, the card, POSTMORTEMS and MEMORY but not `SETUPS.tsv`, `PAPER_BOOK.tsv` or the STATUS BOTTOM LINE, which went on asserting a **withdrawn** finding as fact; and `TRY-FIRE-006` carried a **12-day-stale** SHELVED on three surfaces after being moved to ARMABLE on two. **Detection was never the gap — invocation was.** A trigger-gated check asks the question whose answer is already wrong.
>
> ⚠️ **Do not silence a finding by widening `COMPATIBLE` in the script.** That is relaxing a guard to make it pass — the same move root rule #6's break test forbids. Either the surfaces disagree (fix them) or the *normalizer* is wrong (fix it, and add the case to `--selftest`).

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
- Trailer: use the model the harness names in-session (currently `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`). *(Corrected 2026-07-26 — this line was pinned to Opus 4.8 and had gone stale; behaviour-language over version-pinning per `feedback_behavior_language_over_hash_pinning`.)*
- **⚠️ Single-quote the `-m` message.** Backticked identifiers inside a double-quoted commit message are **command-substituted and silently deleted** — the commit still succeeds. Watch for `command not found` above the success line. **Never repair it by amending a pushed commit** (force-push is forbidden). See `finding_backtick_command_substitution_in_commit_message`.
- **⚠️ A rename needs BOTH paths in the pathspec.** `git mv a → b` then committing only `b` lands the add and leaves the delete staged — the file then exists at **both** paths in HEAD. See `finding_pathspec_rename_needs_both_paths`.

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
