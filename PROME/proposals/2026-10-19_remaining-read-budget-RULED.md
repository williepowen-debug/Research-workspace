# Complete the pending BOOT/root read-budget reduction — authorized draft

Authority: Will asked to fix the issues in the October19 blocker investigation. This is the remaining L745 overlap work and the root-size issue named there. No rule meaning, approval boundary, command or numbered API is changed. Deck remains paused; Helm remains retired.

Review history: BOOT rotation has two prior reads on its October16 partial move, as recorded in proposals/2026-10-16_boot-rotation-PLAN.md. They do not reset. This completion requires a plan and result read; request a named allowance for the result beyond the existing three-read ceiling before installation. Root recipe extraction has no earlier implementation reads. Existing overlap table informs the cuts; this is its concrete diff, not a new broad simplification project.

## Exact root amendment draft (transplant once after plan read)

Replace the body of root **Before committing** through immediately before **Before pulling:** with:

**Before committing** (mandatory for every commit): read and execute `docs/GIT_WORKTREE_PROCEDURES.md` § Before committing in full. It is the canonical continuation of this Git Protocol, including exact pathspecs, shared-index safeguards and message rules. These requirements remain binding; this pointer changes when the recipe is read, not who may commit.

The following exact source block becomes `docs/GIT_WORKTREE_PROCEDURES.md`, preceded only by a title and authority pointer:

**Before committing** (pathspec pattern — avoids the shared-`.git/index` race):
0. **Run ALL git operations from the repo root:** `cd "$(git rev-parse --show-toplevel)"`. From an agent dir, `git status -- AGENTS/<NAME>/` silently shows nothing — a false-clean check.
1. **Modified files:** `git commit AGENTS/<YOUR_NAME>/<file> -m "..."` — path-scoped, no separate staging.
2. **New untracked files:** `git add <specific files> && git commit <same specific files> -m "..."` — explicit paths only, **never `git add AGENTS/<YOUR_NAME>/` as a directory** (`git add A B C` is atomic: one bad path stages nothing, and in an &&-chain the exit code is the only tell).
3. Optional: `git diff --cached --stat` between add and commit.
4. **Never `git reset HEAD`** — shared index; it is a global unstage.
4b. **Never `git commit --amend`** — amend rewrites whoever holds HEAD, which with concurrent sessions may not be you. A damaged message over a correct tree is documentation debt — note it in the next commit, never rewrite. Write messages via quoted heredoc to a file (`cat > /tmp/msg.txt <<'EOF'` … `git commit -F /tmp/msg.txt`) so nothing shell-expands.
4c. **A commit with no pathspec commits WHATEVER THE SHARED INDEX HOLDS** — another session's staged renames included — and `git commit --allow-empty -m "..."` is the dangerous form because it *succeeds either way*, so a "note-only" marker silently sweeps the index. For a marker commit, name a clean tracked path you own: `git commit --allow-empty -F /tmp/msg.txt -- AGENTS/<YOUR_NAME>/STATUS.md` (only that path's changes, if any, are committed). Fallback only: confirm `git diff --cached --name-only` prints nothing immediately before committing — it is check-then-act on a shared index, so prefer the pathspec. *(WQ-96, Will 2026-09-01; cold-read verified empirically.)*
4d. **Commit SUBJECT ≤100 characters — it names the change; receipts, counts, crc figures and provenance go in the BODY** (the heredoc message file of 4b). Path-scoped small commits stay exactly as they are; only the ledger leaves the subject line. *(WQ-171 ①, Will 2026-09-03.)*
5. **Pre-commit sanity check (mandatory):** `git status -- AGENTS/<YOUR_NAME>/` — no dangling deletions (bash-`mv` residue; use `git mv`), no unstaged new files you meant to include, nothing staged outside your dir.


## Exact BOOT amendment

Replace Non-Negotiables with:

## Non-Negotiables

- Root `CLAUDE.md` Critical Rules #4/#5, position-truth canon and Git Protocol bind; PROME/CLAUDE.md Ask-First governs external sends and shared/root edits. Use live prices and the broker book at trade fire-time; FORGE is a stale mirror, never execution authority.
- **No agent edits** unless Will explicitly approves.
- **Shared repo coordination:** when another agent has local/branch work, use `PROME/GIT_COORDINATION.md` before committing, merging, or pushing.
- **Multi-agent orchestration:** before spawning more than one agent, apply `PROME/ORCHESTRATION_PLAYBOOK.md`'s substantive mode split and Runtime mechanics. Each brief carries `PROME/COMPLETION_SPEC.md`; launch preflight and authority remain in `PROME/CLAUDE.md`.

Remove the standalone HEARTBEAT-must-be-read callout: step5 still requires that read. Step5 retains the weekend/repeated-respawn rule and FRED dated-observation requirements. Root/local rules carry prices, trades, sends and Git prohibitions; step0 retains clock, status, cached paths, fetch, ahead/behind and safe-pull instructions. Keep the no-agent-edits clause and shared-repo coordination pointer.

Replace the auto-loaded-context inventory with:

**Context loading:** `PROME/CLAUDE.md` Boot Sequence step 1 governs confirmed injection. Explicitly read `USER.md`; retained-context reuse is decided by `PROME/BOOT_MODULES.md` § Repeat boot. `AGENTS.md` is on-demand for roster/routing.

Keep the following explicit/injected-mode paragraph unchanged. Shorten Doc Ownership to the existing SYSTEM Boot Trust Stack pointer. Replace step0's opening runtime paragraph with:

At the opening report, read and execute `PROME/BOOT_MODULES.md` § Runtime disclosure in full. It retains the capability evidence, coverage and unavailable-control requirements; it is mandatory on every boot.

Append to BOOT_MODULES.md § Runtime disclosure (mandatory every boot):

At the opening report, apply the runtime selection sequence in `PROME/COMPLETION_SPEC.md` and disclose actual discovery, execution, messaging and closeout capabilities; private Artifact ruling access is PAUSED BY WILL (WQ-460), with no Deck-specific probe required using AVAILABLE / UNAVAILABLE / UNKNOWN. Cite this session's tool evidence and discovery coverage; a shell probe cannot establish connector availability. Record gaps and dependent skipped steps in the existing boot receipt, and recheck at use. Apply the capability-specific consequences in `PROME/ORCHESTRATION_PLAYBOOK.md` § Runtime mechanics and canonical launch preflight in `PROME/CLAUDE.md`. Thread-local helpers do not establish fleet presence. Credential presence remains distinct from authentication.

## Acceptance / neighbour checks

Both hot files finish below70% of32,550B, measured by measure.py. Root moved recipe is byte-identical; source heading remains a mandatory pointer, session-end steps and stable numbered rules unchanged. BOOT command sequence, market-data/HEARTBEAT controls, unavailable-capability disclosure and retirement/pause preserved. Every removed mirror has a live canonical carrier. Both boot runners follow the added mandatory module pointer; READS.tsv records the module as scoped already. Check procedure reachability and read-cap, not just parity. Ordinary and overlap = exact carrier mapping; wrong owner = only authorized root/PROME docs; missing = a dead pointer or missing rule blocks acceptance; concurrent = recheck source hashes immediately before install, preserve foreign work. No claimed token/time saving without measurement.

Draft files under /tmp/prome-rotation-draft are review aids; canonical draft text is this record. No hot-file edit or installation yet.

## Measured draft refinement before review

The initial draft left both files above the completion target. Also move the root **Before pulling** block verbatim to the same procedures file; replace its root body with the following mandatory pointer (the root **Never** rules remain unchanged):

**Before pulling:** read and execute `docs/GIT_WORKTREE_PROCEDURES.md` § Before pulling in full, including the dirty-owner stop and scoped-stash conditions.

Exact moved pull block:

**Before pulling:**
1. `git status` — check for uncommitted changes **OUTSIDE** your directory.
2. If other agents' directories are modified: **STOP. Do not pull.** Either flag to Will and wait, or commit your work locally, defer the push, and note the pending push in your session notes.
3. If clean outside your files: `git stash push -- AGENTS/<YOUR_NAME>/` → `git pull --rebase` → `git stash pop`.
4. If stash pop fails: `git stash drop` is OK **only if YOUR files are already committed.** Never drop a stash containing other agents' work.
5. Never resolve merge conflicts in another agent's files — flag to Prome.


Replace BOOT’s duplicated bounded-reader paragraph with the following equivalent instruction:

**Bounded reads (ruling 2026-10-16, A4):** every mandatory document read in steps1–5 uses `python3 PROME/tools/boot_read.py <path>` from repo root, one page per tool output and one document per call. Follow `next_offset` with `--offset <next_offset> --sha256 <sha256>` until `eof: true`; a changed-source refusal means restart that document. The manual's selected sections still determine scope. Never concatenate documents; truncated or harness-persisted output is incomplete beyond text received. Any read not completed to `eof: true` is SKIPPED at step8.

Both root recipe sections remain action-triggered mandatory reads; BOOT step0 retains its stronger no-pull-if-dirty/untracked/staged rule.

Remove the nonprocedural “Goal: become operational fast” tagline; all operating instructions remain.

## Carrier correction before plan read

The existing overlap table overstates two duplicate carriers: step5 preserves weekend orientation but does not carry repeated-respawn hygiene, and the current HEARTBEAT has no explicit FRED citation rule. Retain both in Non-Negotiables as:

- **Repeated same-day respawns:** do not rewrite HEARTBEAT or churn state for hygiene alone; require a real market/system event or user decision.
- **FRED citations:** name observation dates, not retrieval dates.

To make room, replace the Execution order paragraph with the following text, preserving the ordered steps, restriction timing, pause/SKIPPED treatment and manual-over-runner precedence:

**Execution order (ruling 2026-10-16, B1):** step numbers are stable citations, not running order. Run **0 → 1 → 2 → 3 → 4 (STATUS restrictions before any gate-driven act) → step5’s ⚡ ONE-SHOT GATE → 3b → rest of step5 in full (HEARTBEAT · weekend rule · one dashboard pull · five-verdict rules · 5b) → 4b → 6 → 7 → 8 → 9.** Run every active step; WQ460 Deck duties are PAUSED BY WILL, other omitted mandatory steps are SKIPPED under step8. The `/boot` runner (`PROME/.claude/skills/boot/SKILL.md`) follows this order; this manual wins any conflict and the runner must be fixed.

## Plan-reader corrections and explicit review allowance

Will: “Allow completion and result read” (October19 session). This supplies the named additional BOOT result read after its third plan read. Root remains on its first plan/result pair. Reader /root/rotation_completion_plan found two blocking carrier errors: root before-commit pointer must select only § Before committing (not execute the pull recipe), and BOOT’s absolute no-trade-execution prohibition must remain. Both corrected in the exact draft; add `- **No trade execution.**` immediately before No agent edits. No other rule change.

Plan read3 (BOOT)/read1 (root) completed by /root/rotation_completion_plan: two blocking carrier corrections above, no others. Declared advisory residue: BOOT_MODULES header says on-demand/not a boot read; its new explicitly mandatory section is an exception carried by BOOT step0 and both runners. No broad header rewrite after final plan read. Installed after source equality checks against36317f438; result review pending.

Result read4 (BOOT, expressly authorized)/read2 (root): RELEASE0blockers from /root/rotation_completion_plan. Exact recipes/runtime preserved; both pointers correctly scoped; no-trade-execution retained; both hot files below completed-rotation target; read-cap rc0 rotation_due0; runners identical. Read-only sequence/counterexample inspection completed, no advancing boot. Header advisory retained. Reviewer closeout confirmed all findings delivered/no workspace writes/no remaining work.
