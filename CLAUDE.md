# CLAUDE.md

This file provides guidance to Claude Code when working in this repository. **Rules only.** The reasons, incidents, dates and counts behind every rule live in `docs/CANON_PROVENANCE.md` (linked, never auto-loaded); exact amendment history is `git log -p -- CLAUDE.md`.

## What This Is

A multi-agent financial research operation tracking systemic risk transmission. Goal: detect stress early enough to position ahead of consensus. The operator is Will (Eastern timezone).

## How The System Works

All agents run as **Claude Code sessions on Will's current box** — serial multi-machine, desktop ⇄ laptop, ONE at a time (inventory + switching checklist → `PROME/MACHINE_LOCAL.md`) — sharing this git repo.

**Launch each agent from its own directory** (`cd AGENTS/<NAME> && claude`; PROME from `PROME/`). Claude Code auto-loads `CLAUDE.md` by walking *up* from the launch dir, so launching in-folder loads this root file **and** the agent's local `CLAUDE.md`; launching from the repo root loads root only and the agent runs without its domain rules. If an agent seems to be missing its domain rules, check its launch cwd.

- **PROME** (chief of staff / coordinator): assigns decision work, manages state/decision rails, owns Will-facing synthesis. **WALTER owns signal/news routing** (ingest, filter, dedupe, archive, route). Domain agents own domain evidence and judgment. A PROME task packet is the current coordination layer unless it conflicts with Will or higher-priority instructions.
- **Domain agents** run as independent CC sessions, coordinating via inbox/outbox files and via teams-mode `SendMessage` when PROME orchestrates a live session.

Coordination is file-based. **Write to `PROME/inbox/` (repo root — NOT under `AGENTS/`; `AGENTS/PROME/` does not exist and must not be recreated) to request Prome action;** `AGENTS/<NAME>/outbox/*to-PROME*` files are for signal/routing work. Read `AGENTS/<NAME>/inbox/` for incoming signals.

**If a coordinator spawns you (teams-mode):** deliver your result — `SendMessage` it to the coordinator AND write it to your own dir — as your **final action before going idle**. Never idle "holding" without delivering.

**Transmission chain / routing topology:** canonical at `AGENTS/_NETWORK.md` (navigate via `AGENTS.md`; on any disagreement `_NETWORK.md` wins). Follow that surface and your local routing rules; do not reconstruct routes here or in any other mirror (WQ-137: the hand-copied chain that lived here had already diverged from canon — root carries the rule, `_NETWORK.md` carries the topology).

**Roster:** `PROME/ROSTER.md` is the single source of truth for who is active, Tier-2, special, dormant, or retired — plus the exclusion classes ARCHIVE SOURCES · TOOL-CLASS · OFF-FLEET (never launch or audit those as fleet agents) — and for responsibility classes (descriptive, not authority tiers — they change no routing or obligations). Do not re-list membership anywhere else; when a mirror and ROSTER disagree, ROSTER wins. **Potash is triage-only at FERT** (log + flag PROME, no deep-dive) — the full rule is FERT's `CLAUDE.md` §POTASH; read it there.

**Scoped overlaps are intentional** — reconcile shared metrics to one figure, don't silo: CORAL↔MARCO (FL migration/tourism), AEOLUS↔CORAL (FL climate/coastal). **Florida is a top-priority geography for Will.**

**Agent state** lives at `AGENTS/<NAME>/STATUS.md`. **Position truth is off-repo** (Will/broker direct). `FORGE/STATUS.md` is the structured mirror (broker-export refreshed; reconcile vintage lives in its own header, never restated elsewhere; **owner: PROME**; stales between exports). `FORGE/PORTFOLIO.md` is a **FROZEN** Feb-2026 snapshot — historical only. Trade construction = TERRY.

## Critical Rules

1. **Read before editing.** Never call Edit without reading the file in the same turn.
2. **Subagents own their files.** Don't edit a file another agent is updating. Wait for it to finish.
3. **Agent data can be hallucinated.** Verify against SEC filings before trading.
4. **Prices must be live.** Never cite prices from STATUS files.
5. **Trade proposals → Will approves.** Never execute without [Approve].
6. **Puts on green days, calls on red days.** Note when breaking and why.
7. **Roll duration, don't trim size.** Trimming = thesis broken. Rolling = timeline uncertain.
8. **Mechanical before creative.** Rolls, trims, expiries BEFORE new research threads.
9. **Deploy agents then wait.** If you spawn for a decision, wait for outputs.
10. **Close the proposal loop.** Proposal → decision → execution → record in originating agent's STATUS.md.
11. **trash > rm.** Always use trash for deletions.

> *Rules **6–7** are trade-construction rules — canonical owner **TERRY** (`AGENTS/TERRY/RISK_RULES.md`); domain-data agents can skip them. **These numbers are a stable API** (fire-cards cite them) — never renumber or delete.*
>
> ⚠️ ***Two independent numbered lists exist and both are cited by number*** — these root Critical Rules and TERRY's `RISK_RULES.md` Non-Negotiables — and they do not line up. Neither can be renumbered. **Citation discipline:** write **"root rule #6"** or **"Non-Negotiable #6"**, never a bare "rule #6." Applies to cards, packets, memos and commit messages.
>
> *Breaking **root rule #6** is legitimate **only** with the direct measurement that refutes the day-colour proxy, written on the card in figures **before** the fill, with no hard guard relaxed. "The window is closing" is a chase, not a break. Full test → `AGENTS/TERRY/RISK_RULES.md` § "Breaking root rule #6."*

## Output Canon (fleet-wide — single home; agent files cite, don't restate)

**Tables > prose. Numbers > narrative** ("$477.3B (+26% YoY)", not "grew significantly"). **Source + date every claim.** **File > verbal** — work not written to a file in your dir doesn't exist. Agent-specific rules (STATUS line caps, domain caveats) stay local.

**Cost-bearing text & state tokens:** packet ACTION/ASK lines, script output messages, and gate/threshold/kill specs follow `AGENTS/DAEDALUS/BLUEPRINTS/STRICT_TEXT.md`. Machine-read state tokens come from `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md` — new surfaces use canonical tokens; legacy is grandfathered. Prose, thesis docs and Will-facing synthesis are exempt.

## Key Directories

| Path | Purpose |
|------|---------|
| AGENTS/ | All agent domains, STATUS files, knowledge bases |
| FORGE/ | Structured position surface (`STATUS.md`; `PORTFOLIO.md` frozen) + market-data tools, signals, research corpora. Retired ledgers → `FORGE/_archive/` |
| FORGE/timing/ | FROZEN research corpus (bannered 2026-08-09) — cite as history, never current |
| FORGE/tools/market-data/ | Live data CLI: `python3 fetch.py price KRE`, `python3 dashboard.py` |
| memory/ | Daily session notes (YYYY-MM-DD.md); `memory/auto/` = fleet auto-memory |
| PROME/ | Coordinator state (SCRATCH, STATUS, ROSTER, GATES.tsv, DOCKET.tsv, WILL_QUEUE, AUTONOMY) |
| docs/ | AUTO_MEMORY.md (auto-memory git-sync); CANON_PROVENANCE.md (this file's reasons) |

## Git Protocol

Agents share one working directory and branch. **GitHub is the single source of truth.** Pull at session start; **commit locally** at session end; **push is automated at closeout** via `scripts/safe-push.sh` (fast-forward-gated, never force, aborts cleanly if origin has commits we don't) — sound because Will runs ONE machine at a time and closes out before switching.

**`git add` ONLY files inside your own directory** — throughout this protocol "your directory" = `AGENTS/<NAME>/`; **for PROME it is `PROME/`** (substitute accordingly in every recipe below). Never `git add .` or `git add -A`. Shared files (HEARTBEAT, FORGE, root docs) → flag to Prome, don't commit them — for domain agents the ONLY exceptions are the carve-outs below; PROME's own shared-file grants = the Scope note + the Gate C custody paragraph below.

**Carve-outs ①–④ — four fleet-wide self-authorship carve-outs (④ activation-gated); the separate PROME-only Gate C custody grant is the paragraph AFTER them, not a numbered carve-out:**
- **① Self-authored inbox packets:** a packet **you authored** into another agent's `inbox/` is yours to commit **and you must** — an uncommitted packet never reaches the recipient. Commit it explicitly-pathed, recipient named in the subject (`<YOU> -> <RECIPIENT>: <what>`).
- **② Self-authored shared-log rows:** a row **you authored** in a shared cross-agent log (`AGENTS/SIGNALS.md` class) is yours to commit, explicitly path-scoped. Rows others wrote, file restructures, and every other shared/root doc stay excluded.
- **③ Self-authored auto-memory files (`memory/auto/`):** any memory file you authored or appended to — you may **and must** self-commit it. **Why mandatory:** `MEMORY.md` is a shared index that rides out on whoever commits next, while your memory FILE needs a deliberate `git add`; an index row pointing at an absent file is worse than no memory. **Enforcement at closeout:** `python3 scripts/memory_index_check.py --strict --slug <your-memory-name>` (repeat `--slug` per memory; **never bare `--strict`** — that gates the whole fleet index and blocks you on another agent's orphan). `orphan_check.sh` classifies by PATH, so its `[not yours]` label is not an authorship verdict here. Still excluded: others' memory files, regenerating or restructuring `MEMORY.md` (append your row; on a cross-machine conflict keep both, dedup by slug), deleting anyone's memory. **Scoped to `memory/auto/` ONLY — not precedent for any other shared directory.**
- **④ Gate C Kernel shadow paths (inactive unless a `KERNEL/GATE_C_*_ACTIVATION_*.json` packet is LIVE, ALL legs: dated non-DRAFT filename · `authorized_by` Will · current time inside its concrete `window_start`/`window_end` (UTC) · `revoked_at` empty · the window names you):** after Will activates a bounded Gate C pilot, a domain agent may create and commit only a canonical immutable command it authored at `AGENTS/<NAME>/outbox/kernel/submissions/<command_id>.json` (path, embedded `actor_id` and filename must agree; stage and commit that single path; never edit or delete it afterwards). This conveys submission only — never `command.accept`, Kernel custody, editing `KERNEL/`, or research authority over another agent's record.

**Gate C custody (PROME only).** PROME is the sole active acceptance custodian. Under an operator-approved activation packet PROME may explicitly stage and commit only: approved Kernel schemas and policy/registry versions; new accepted events at `KERNEL/shadow/events/YYYY/MM/<event_id>.json`; new rejected receipts at `KERNEL/audit/commands/YYYY/MM/<command_id>.json`; the four registered generated views under `KERNEL/views/`; and the sitting's governance records the approved runbook instructs (activation document incl. its `revoked_at`, sitting rulings, durable transcript, closeout/ruling packets). Accepted events and rejected receipts are **additions-only** — any modification, deletion, rename, overwrite or history rewrite is a blocking integrity failure. Views are generated replaceable projections, not authority, changed only through the registered deterministic renderer. Every stage and commit uses exact file pathspecs — never a submission, result, month directory, `KERNEL/`, `AGENTS/<NAME>/`, or `.rw/` as a directory; never `git add .`, `git add -A`, a computed path list, or `git commit -a`. Kernel tools never commit or push automatically. Before a Kernel commit: prove one active writer, inspect the exact staged paths, run the registered additions-only and durable-result checks, and stop on unrelated staged changes, an unapproved path, `EXCEPTION`, or `UNKNOWN`. A substitute custodian receives no standing grant — Will activates a pre-registered substitute for a named window and perimeter; it uses PROME's identical path limits, records its own `writer_id`, and loses the grant at window end. CI never becomes an acceptance writer. No timeout transfers custody.

**Scope note — who commits what:** **PROME** commits `PROME/`, plus `HEARTBEAT.md` and `FORGE/` PROME-standard, plus Will-gated shared/root docs (root `CLAUDE.md`, `AGENTS.md` core — **get Will's OK first**). Domain agents still flag HEARTBEAT and FORGE to PROME and never commit them. **Auto-push exceptions** (deviations in closeout/push MECHANICS only — no extra commit authority, no path-boundary bypass): TERRY (self-sweeps), WALTER (per `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` §7), YEYOU (manual/branch). Everyone else: own `AGENTS/<NAME>/` dir + auto-push at closeout.

**At session start:** follow "Before pulling" below, then your normal boot.

**At session end:**
1. Commit your files locally ("Before committing" below).
1b. **Orphan check:** `bash scripts/orphan_check.sh <YOUR_NAME>` — read-only advisory. `[likely YOURS]` = packets you authored → commit them (carve-out ①). `[not yours]` = flag to PROME, never sweep.
1c. **Consumer check:** if this session superseded a figure others may cite (threshold, flip level, split, band): `python3 scripts/consumer_check.py --agent <YOUR_NAME> --old <old> --new <new>` and send each 🔴 STALE owner a packet — **never edit their files**. Repeat `--old` ONLY for prior vintages of the SAME figure; different metrics = separate runs or `--from-ledger`. If you superseded one of your OWN figures, also run `python3 scripts/consumer_check.py --agent <YOU> --self --old <old> --new <new>` (the cross-agent scan excludes your dir). Fix by pattern, not by the printed line list; 🟠 CANDIDATE = look, packet only on 🔴; confirm series AND unit first; send nothing on a bare 2-sig-fig figure.
1c-bis. **Ledger nudge:** if your commit set includes `STATUS.md` but none of the ledgers your `AGENTS/<NAME>/workbook/LEDGER_GLOB` file declares: `python3 scripts/ledger_staleness.py --nudge <YOUR_NAME>` — freeze, refresh, or say why not in the commit message.
1d. **Memory-index check:** if you wrote or edited an auto-memory: `python3 scripts/memory_index_check.py --strict --slug <name>` (carve-out ③'s enforcement; exit 1 = commit the file or fix the ignore rule) **and** `bash scripts/check_memory_length.sh` — the boot-loaded index has a hard cap (~200 lines / 25,600 B) past which entries are silently dropped; rc=1 approaching, rc=2 over. **Do NOT compact `MEMORY.md` yourself — flag to PROME.** YEYOU exempt.
1e. **Claim check:** `python3 scripts/claim_check.py --check weekday PROME/DOCKET.tsv PROME/GATES.tsv PROME/WILL_QUEUE.md AGENTS/<YOU>/workbook/CATALYSTS.tsv AGENTS/<YOU>/CALENDAR.md AGENTS/<YOU>/STATUS.md` (omit paths you lack). Flags a weekday asserted beside a date that isn't that weekday. A flag is a prompt to LOOK, never a find-replace — it may be a correctly-labeled quote of a corrected error.
2. **Auto-push** via `scripts/safe-push.sh`. The receipt is the line `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` — a log tail or a bare `Pushed.` is not a receipt.
3. **If safe-push aborts (non-ff), do NOT force.** A non-ff means another SESSION pushed since this clone last fetched — usually a concurrent agent on the SAME box; it is a property of the commit graph, not of file paths, so separate directories cannot prevent it. Recovery: `git pull --rebase --autostash` then re-push — **first check that incoming commits don't touch any dirty path**: `git fetch origin && git diff --name-only "$(git merge-base HEAD origin/master)..origin/master"` against `git status --porcelain` — any overlap ⇒ stop and flag to PROME (the autostash stashes the whole dirty tree, other agents' work included). Rebase rewrites unpushed commit hashes — verify by subject if a hash goes missing. **Escalate to Will only if** the rebase conflicts outside your own dir or non-ff persists through a completed rebase→re-push cycle; bare recurrence is ordinary traffic.

**Before committing** (pathspec pattern — avoids the shared-`.git/index` race):
0. **Run ALL git operations from the repo root:** `cd "$(git rev-parse --show-toplevel)"`. From an agent dir, `git status -- AGENTS/<NAME>/` silently shows nothing — a false-clean check.
1. **Modified files:** `git commit AGENTS/<YOUR_NAME>/<file> -m "..."` — path-scoped, no separate staging.
2. **New untracked files:** `git add <specific files> && git commit <same specific files> -m "..."` — explicit paths only, **never `git add AGENTS/<YOUR_NAME>/` as a directory** (`git add A B C` is atomic: one bad path stages nothing, and in an &&-chain the exit code is the only tell).
3. Optional: `git diff --cached --stat` between add and commit.
4. **Never `git reset HEAD`** — shared index; it is a global unstage.
4b. **Never `git commit --amend`** — amend rewrites whoever holds HEAD, which with concurrent sessions may not be you. A damaged message over a correct tree is documentation debt — note it in the next commit, never rewrite. Write messages via quoted heredoc to a file (`cat > /tmp/msg.txt <<'EOF'` … `git commit -F /tmp/msg.txt`) so nothing shell-expands.
5. **Pre-commit sanity check (mandatory):** `git status -- AGENTS/<YOUR_NAME>/` — no dangling deletions (bash-`mv` residue; use `git mv`), no unstaged new files you meant to include, nothing staged outside your dir.

**Before pulling:**
1. `git status` — check for uncommitted changes **OUTSIDE** your directory.
2. If other agents' directories are modified: **STOP. Do not pull.** Either flag to Will and wait, or commit your work locally, defer the push, and note the pending push in your session notes.
3. If clean outside your files: `git stash push -- AGENTS/<YOUR_NAME>/` → `git pull --rebase` → `git stash pop`.
4. If stash pop fails: `git stash drop` is OK **only if YOUR files are already committed.** Never drop a stash containing other agents' work.
5. Never resolve merge conflicts in another agent's files — flag to Prome.

**Never:** force push, commit outside your directory without instruction (the carve-outs ①–④, the Scope-note grants and the Gate C custody paragraph above ARE standing instruction, each for its narrow scope only), resolve another agent's conflicts, pull when other agents have uncommitted local changes (sole exception: session-end step 3's non-ff recovery, and only after its dirty-path overlap check passes).

## Data Hygiene

- **Ledger staleness — STATUS is canonical truth.** TSV workbook ledgers (KB/VX/FLOW/etc.) and agent-level position / `TRADE.md` surfaces (e.g. `FORGE/STATUS.md`) silently drift behind STATUS — a universal fleet failure mode. Keep each ledger in one of two states, never the silent-rot middle: **(a) FROZEN** — banner `FROZEN <date> — not maintained; STATUS is canonical, do not cite rows as current`, stop maintaining; or **(b) LIVE with a boot-time staleness alert keyed to a content-derived vintage** — preferred signal = the two-clock header `Last real data refresh: YYYY-MM-DD`, which `scripts/ledger_staleness.py` reads first; git-commit time is the fallback, raw mtime last-resort for uncommitted files only. **Never key a NEW freshness/throttle mechanism on mtime** — git sync restamps it, failing false-negative.
- **Research/sources retirement (closeout step):** a file **>60 days old AND not boot-read AND not referenced by a live doc** → `git mv` to your own `AGENTS/<NAME>/archive/` (PROME-owned material → `PROME/archive/`; retired FORGE surfaces keep their own home, `FORGE/_archive/`, per Key Directories). Two clauses: ① the registered artifact of a PENDING dated event (DOCKET/GATES row, unresolved prediction, frozen spec window, expiry) is NOT retirement-eligible however old; ② a reference from an index/inventory/nav surface does not count as "referenced by a live doc" — a qualifying reference is one a live analytical or protocol doc actually travels.
- **Read-cap byte budget:** any surface a boot protocol tells a session to READ WHOLE stays under **32,550 B** — binding above any owner-set number, per surface; owners choose rotation or hot/cold split, never the number. Check: `scripts/read_cap_check.py --agent <NAME>`; canon `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`. (A different constant from the `MEMORY.md` 25,600 B auto-load cap.)
- **Direct Messaging v1:** the ratified messaging overhaul lives under `MESSAGING/`. Live coded routes are allowlisted to **PROME → BRENT** and **PROME → SAM** (`MSG-*.md` at the top level of the recipient's `AGENTS/<X>/inbox/`, read at boot). All other direct routes, inbox boot-auto-triage, outbox-kill and ad hoc replacements remain out of scope; WALTER is unchanged under its BOARD/inbox spec. **Cross-session harness messaging (`SendMessage`/`ListAgents`) is a standing tool for every session** — rules in `MESSAGING/CROSS_SESSION_MESSAGING.md`, read it before first use. Core: messages carry coordination, ARTIFACTS carry content; verify a peer's claim at artifacts before acting; a relayed operator word never clears a Will-gated surface; never route signals around WALTER; at packet-commit with an ASK of a named agent, `ListAgents` and doorbell a live recipient (messaging rule 6); recipient DARK → messaging rule 6b (dark-owner doorbell-PROME branch). Both live in `MESSAGING/CROSS_SESSION_MESSAGING.md` — not this file's numbered rules.

## Tools

- Python venv at `.venv/`
- pdfminer.six: `from pdfminer.high_level import extract_text`
- Market data: `python3 FORGE/tools/market-data/dashboard.py` (see README.md there)

## Reference

**Status key:** 🟢 none | 🟡 monitoring | 🟠 elevated | 🔴 active/critical
