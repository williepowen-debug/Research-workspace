# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Is

A multi-agent financial research operation tracking systemic risk transmission. Goal: detect stress early enough to position ahead of consensus. The operator is Will (Eastern timezone).

## How The System Works

All agents run as **Claude Code sessions on Will's current box** (serial multi-machine: desktop ⇄ laptop, ONE at a time — machine-local inventory → `PROME/MACHINE_LOCAL.md`), sharing this git repo. (The OpenClaw/VPS platform was cut 2026-06-26 — see `AGENTS/WALTER/design/OPENCLAW_CUTOVER_PLAN.md`.)

**Launch each agent from its own directory** (`cd AGENTS/<NAME> && claude`; PROME from `PROME/`). Claude Code auto-loads `CLAUDE.md` by walking *up* from the launch dir — so launching in-folder loads **both** this root file **and** the agent's local `CLAUDE.md`. Launching from the repo root loads root **only**: the local `CLAUDE.md` is a *descendant* and won't auto-load, so the agent runs **without its own domain instructions** until it happens to read a file in its folder. If an agent seems to be missing its domain rules, check its launch cwd.

- **PROME** (chief of staff / coordinator) runs as a CC session: assigns decision work, manages state/decision rails, and owns Will-facing synthesis via Telegram. WALTER owns signal/news routing.
- **Domain agents** (CARL, REGINALD, SAM, RED, …) run as independent CC sessions. They are not persistently spawned by PROME; they coordinate with PROME and each other via inbox/outbox files — and via teams-mode `SendMessage` when PROME orchestrates a live multi-agent session.

Coordination is file-based. Write to `AGENTS/<NAME>/outbox/` to request Prome action. Read `AGENTS/<NAME>/inbox/` for incoming signals. Prome checks these and routes accordingly.

**If a coordinator spawns you (teams-mode):** deliver your result — `SendMessage` it to the coordinator AND write it to your own dir — as your **final action before going idle**. Never idle "holding" without delivering; it forces the coordinator to chase you.

**Operating model:** Prome is chief of staff, not the universal analyst. Prome owns prioritization, decision rails, state files, operational tasking, and Will-facing synthesis. **WALTER owns signal/news routing**: ingest, filter, dedupe, archive, and route incoming market intelligence. Domain agents own domain evidence and judgment. If Prome sends a task packet, treat it as the current coordination layer unless it conflicts with Will or higher-priority instructions.

**Transmission chain:** LABOR → CARL → REGINALD → market repricing. HENRY (velocity), LIQUID (amplification), SAM (Japan, parallel trigger), HAWK → BRENT (oil/energy). AEOLUS → {BRENT, CORAL, MARCO} (climate → economy). AEOLUS C3 → WATT → {HENRY, CARL} (grid stress → power price → cost). VULCAN → {VIOLET, HENRY, WATT} (AI-capex → concentration/FCF/power demand). {BOND, ZHAO} ↔ MIDAS → {LIQUID, HENRY} (metals: monetary + industrial tells).

**Active agents (verified 2026-06-27; ZHAO reactivated 2026-07-05 — full classification + activity evidence in `PROME/ROSTER.md`):** PROME, WALTER, SAM, VIOLET, BRENT, CARL, LIQUID, RED, REGINALD, HENRY, LABOR, MARCO, BROCK, HAWK, NEXUS, BOND, TERRY, CORAL, ORACLE, SHADE, AEOLUS, ZHAO, **WATT, VULCAN, MIDAS** *(new 2026-07-10/11, DAEDALUS-built — power / AI-semis / metals; reconcile next activity pass, PAT-019)*. **Tier 2 (spawned as needed):** CREED, DEWEY, HANS, OTTO. **Special:** YEYOU (repo-wide reviewer, manual/branch model), DAEDALUS (fleet architect meta-agent — design/structure/maturity/lifecycle, on-demand). *(All agents are Claude Code sessions now.)* *(Dormant / Retired / Archive-source taxonomy → `PROME/ROSTER.md` — the single source of truth for who's live vs. shelved.)*

*Scoped overlaps are intentional — reconcile shared metrics to **one figure**, don't silo: **CORAL↔MARCO** (FL migration/tourism) and **AEOLUS↔CORAL** (FL climate/coastal). **Florida is a top-priority geography for Will.** Agent spinout/promotion provenance (OZK, CORAL, AEOLUS; WAL = next promotion candidate) → `PROME/ROSTER.md`.*

Agent state lives at `AGENTS/<NAME>/STATUS.md`. Position truth is **off-repo** (Will/broker direct — the on-repo `WILL/trading-journal/` photos were removed in the 2026-06 public-prep cleanup); `FORGE/STATUS.md` + `FORGE/PORTFOLIO.md` = the structured mirror (broker-export refreshed, currently stale); trade construction = TERRY.

## Critical Rules

1. **Read before editing.** Never call Edit without reading the file in the same turn.
2. **Subagents own their files.** Don't edit a file another agent is updating. Wait for it to finish.
3. **Agent data can be hallucinated.** Verify against SEC filings before trading. (PSEC PIK was 8.6%, not 35%.)
4. **Prices must be live.** Never cite prices from STATUS files.
5. **Trade proposals → Will approves.** Never execute without [Approve].
6. **Puts on green days, calls on red days.** Note when breaking and why.
7. **Roll duration, don't trim size.** Trimming = thesis broken. Rolling = timeline uncertain.
8. **Mechanical before creative.** Rolls, trims, expiries BEFORE new research threads.
9. **Deploy agents then wait.** If you spawn for a decision, wait for outputs.
10. **Close the proposal loop.** Proposal → decision → execution → record in originating agent's STATUS.md.
11. **trash > rm.** Always use trash for deletions.

> *Rules **6–7** are **trade-construction** rules — canonical owner is **TERRY** (`AGENTS/TERRY/RISK_RULES.md`), applied by TERRY and by PROME when building proposals; domain-data agents (LABOR, SAM, AEOLUS, …) can skip them. **The numbers are a stable API — TERRY fire-cards cite "rule #6" by number, so do not renumber or delete these.***

## Output Canon (fleet-wide — single home; agent files cite, don't restate)

**Tables > prose. Numbers > narrative** ("$477.3B (+26% YoY)", not "grew significantly"). **Source + date every claim** — no naked numbers. **File > verbal** — cross-agent session visibility is restricted; work not written to a file in your dir doesn't exist. *(Consolidated here 2026-07-07, harness-audit strike S1/S4, Will-approved — per-agent restatements removed; agent-specific rules like STATUS line caps and domain caveats stay local.)*

## Key Directories

| Path | Purpose |
|------|---------|
| AGENTS/ | All agent domains, STATUS files, knowledge bases |
| FORGE/ | Structured position surface (`STATUS.md`+`PORTFOLIO.md`) + market-data tools, signals, research/timing corpora. Retired execution ledger + per-trade KRE/WAL/OZK folders → `FORGE/_archive/` |
| FORGE/timing/ | Thesis timing research, convergence timeline, research corpus |
| FORGE/tools/market-data/ | Live data CLI: `python3 fetch.py price KRE`, `python3 dashboard.py` |
| memory/ | Daily session notes (YYYY-MM-DD.md) |
| PROME/ | Coordinator state (SCRATCH, STATUS, ROSTER, GATES.tsv, DOCKET.tsv, AUTONOMY) |
| docs/ | AUTO_MEMORY.md (auto-memory git-sync system) |

## Git Protocol

Agents share one working directory and branch. **GitHub is the single source of truth.** All agents pull at session start and **commit locally** at session end. **Push is automated at closeout via `scripts/safe-push.sh`** (fast-forward-gated, fails safe) — predicated on **serial multi-machine operation**: Will runs ONE machine at a time (desktop ⇄ laptop), closing out + pushing all agents before switching, so origin is always the handoff point (OpenClaw/VPS was cut 2026-06-26; machine-local infra inventory + switching checklist → `PROME/MACHINE_LOCAL.md`). safe-push never force-pushes and **aborts cleanly if origin has commits we don't**, so one agent's closeout push safely sweeps everyone's local commits — the push-train, now automated rather than gated on a manual Will window.

> **`git add` ONLY files inside your own `AGENTS/<NAME>/` directory.** Never `git add .` or `git add -A`. If you need to commit a shared file (HEARTBEAT, FORGE, etc.), flag it to Prome — don't commit it yourself.

**Scope note — readers who aren't a domain agent:** **PROME** commits `PROME/` (its home dir) plus Will-scoped shared/root docs (root `CLAUDE.md`, `HEARTBEAT.md`, `AGENTS.md`, `FORGE/` — get Will's OK first), not an `AGENTS/PROME/` dir. **Auto-push exceptions:** **TERRY** (self-sweeps, live), **WALTER** (architectural, per its `BOARD_CONSUMPTION_SPEC` §7), **YEYOU** (manual/branch, per Auto-push Decision C). All other agents: own `AGENTS/<NAME>/` dir + auto-push at closeout (below).

**At session start:**
1. Follow the "Before pulling" protocol below to sync from GitHub
2. Then proceed with your normal boot sequence

**At session end:**
1. Commit your files locally (follow "Before committing" below).
2. **Auto-push at closeout** via `scripts/safe-push.sh` (ff-gated, fails safe) — wired into your closeout protocol. It sweeps all local commits in one fast-forward push (the push-train, now automated — see auto-memory `finding_push_train_pattern`). *(Lazy-sweep complete 2026-06-27 — all active domain agents are on auto-push; intentional exceptions per the scope note above [TERRY self-sweep, WALTER architectural, YEYOU manual/branch]. Stale-parenthetical fix 7/11, Will-approved.)*
3. **If safe-push aborts (non-ff), do NOT force.** First response: `git pull --rebase`, then re-push — under serial multi-machine this is **routine** (the other machine pushed since this clone last pulled). **Escalate to Will (per-agent-branches tripwire) only if** the rebase hits conflicts outside your own dir, or non-ff recurs mid-session — either means two machines ran simultaneously, which the protocol forbids.

**Before committing:** (pathspec pattern — avoids the shared-`.git/index` race; see auto-memory `finding_pathspec_commit_race_safety`, incident `8ac5bf71` Jun 4 2026)
0. **Run ALL git operations (and `scripts/safe-push.sh`) from the repo root:** `cd "$(git rev-parse --show-toplevel)"` first. Git pathspecs resolve relative to cwd — from an agent's launch dir (`AGENTS/<NAME>/`), `git commit AGENTS/<NAME>/<file>` fails loudly, but **`git status -- AGENTS/<NAME>/` silently shows nothing** (a false-clean pre-commit check). Every `AGENTS/<NAME>/…` recipe below assumes root cwd.
1. **For modified files:** `git commit AGENTS/<YOUR_NAME>/<file> -m "..."` — path-scoped commit, no separate staging step.
2. **For new untracked files:** atomic `git add <specific files> && git commit <same specific files> -m "..."` — explicit paths only, **never `git add AGENTS/<YOUR_NAME>/` as a directory** (sweeps in unintended files).
3. **Optional sanity check** between add and commit on new-file flows: `git diff --cached --stat`.
4. **Never `git reset HEAD`** — shared `.git/index` makes it a global unstage that races against other agents' concurrent stages.
5. **Pre-commit sanity check (mandatory):** before committing, run `git status -- AGENTS/<YOUR_NAME>/`. Confirm: no dangling deletions (bash-`mv` residue), no unstaged new files you meant to include, nothing staged outside your own dir. 5-second guard against the `git mv`-vs-`bash mv` residue class (auto-memory `git_mv_for_inbox_processing`) and the cross-dir-leak class. *(Validated 2026-06-26: on first use this caught 53 foreign pre-staged files mid-race + surfaced a months-old display-copy desync.)*

**Before pulling:**
1. `git status` — check for uncommitted changes **OUTSIDE** your directory
2. If you see modifications in other agents' directories: **STOP. Do not pull.** Other agents' uncommitted work will be lost. Choose one:
   - **Option A:** Flag to Will and wait for instruction
   - **Option B (if Will unavailable):** Commit your work locally and defer the push. Note in your MEMORY.md session notes that a push is pending. Push next session when the working directory is cleaner.
3. If working directory is clean outside your files: proceed with stash/pull/pop
4. `git stash push -- AGENTS/<YOUR_NAME>/` — stash only your files
5. `git pull --rebase`
6. `git stash pop`
7. If stash pop fails: `git stash drop` is OK **only if YOUR files are already committed.** Never drop a stash containing other agents' work.
8. Never resolve merge conflicts in another agent's files — flag to Prome

**Never:** force push, commit outside your directory without instruction, resolve another agent's conflicts, pull when other agents have uncommitted local changes.

## Data Hygiene

Closeout discipline, fleet-wide (ratified 2026-06-26 after a 5-agent architecture review; see `PROME/cluster/2026-06-26_fleet_arch_compare.md`).

- **Ledger staleness — STATUS is canonical truth.** TSV workbook ledgers (KB/VX/FLOW/etc.) **and agent-level position / `TRADE.md` surfaces** (e.g. `FORGE/STATUS.md`) silently drift behind STATUS — a *universal* fleet failure mode. Keep each ledger in one of two states, never the silent-rot middle: **(a) FROZEN** — dead ledger, prepend a banner `FROZEN <date> — not maintained; STATUS is canonical, do not cite rows as current`, and stop maintaining it; or **(b) LIVE with a boot-time mtime staleness alert** (surface "X.tsv stale Nd" at boot, not at closeout).
- **Research/sources retirement (closeout step):** a file that is *>60 days old AND not boot-read AND not referenced by a live doc* → `git mv` to `archive/`. Prevents research-graveyard accumulation.
- **Out of scope (do not build):** outbox-kill / new cross-agent send protocols / inbox boot-auto-triage. File-based messaging is slated for replacement (auto-memory `messaging_overhaul`) — interim is only "stop writing dead outbox files"; route messaging redesign to that effort.

## Tools

- Python venv at `.venv/`
- pdfminer.six: `from pdfminer.high_level import extract_text`
- Market data: `python3 FORGE/tools/market-data/dashboard.py` (see README.md there)

## Reference

**Status key:** 🟢 none | 🟡 monitoring | 🟠 elevated | 🔴 active/critical

**Cost model:** Heavy research on Sonnet, synthesis on Opus. Typical sub-agent: $0.02-0.05. Long research: $0.10-0.20.
