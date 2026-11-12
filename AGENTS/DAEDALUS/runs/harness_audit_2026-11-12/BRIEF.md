# Harness re-test, provider switch (Codex to Claude Opus 5.5) — reader brief (DAEDALUS, 2026-11-12)

Repo root: /home/willi/Research-workspace. Pinned HEAD: 29d4ac658b (other desks keep committing; read the working tree and quote line numbers as you find them). Read-only against the repo: NEVER edit, stage or commit any repository file. Your only write is your own ledger file at the path your prompt names.

## Why this pass exists
Will ruled (WQ-654 A, 2026-11-07) that a switch between model providers counts as a model upgrade and triggers an unconditional re-test of the fleet's instruction layer. DAEDALUS ran on Codex (OpenAI) through 2026-11-09 and runs on Claude Opus 5.5 now; desks run on either runtime. The pass is narrowed: **removals and simplifications only (Will's WQ-577, 2026-10-31: no additions unless he asks), plus git, authority and trade-path contradictions, read across every charter whether changed or not.** Will's standing direction (USER.md, 2026-10-31): fewer checkers and rules; propose retiring controls that do not earn their keep.

## What a "harness" is
The instruction layer a desk boots from and closes out with: `AGENTS/<NAME>/CLAUDE.md`, standalone `CLOSEOUT.md`/`OPERATIONS.md`/`AGENTS.md`/`BOOT_PROTOCOL.md`/worker `AGENT.md`, sub-agent charters, PROME's BOOT/CLOSEOUT/CLAUDE/SYSTEM/AUTONOMY/ORCHESTRATION_PLAYBOOK/BOOT_MODULES/CLOSEOUT_PROCEDURES/COMPLETION_SPEC, and root CLAUDE.md, AGENTS.md, USER.md, docs/GIT_WORKTREE_PROCEDURES.md.

## The criterion (ratified 2026-07-07; read AGENTS/DAEDALUS/HARNESS_AUDIT_2026-07-07.md §0)
A step earns its inline place only if ALL hold: (a) it is an ACTION or behaviour gate (history, provenance, incident stories fail (a)); (b) not already mechanized (a script does it); (c) not owned elsewhere (not a restatement of root canon or another owner's rule). **Model-change leg:** re-test (a) against a current strong model — instructions that exist because a weaker model would not do X unprompted (read-before-edit hand-holding, repeated ⚠️ blocks saying the same thing, style nagging) fail (a).
Verdicts: KEEP · STRIKE · REWRITE (a REWRITE must make the text shorter or simpler, never longer; no new rule, no new check, no new step).

## Always report, ranked HIGH
- **Git safety** weaker than root CLAUDE.md § Git Protocol and docs/GIT_WORKTREE_PROCEDURES.md: `git add .`/`-A`, a directory add, an unscoped commit, `--amend`, `reset HEAD`, `stash` of others' work, force, plain `git pull`, escalating a bare non-ff recurrence, committing outside one's own directory beyond the carve-outs.
- **Authority**: a desk granting itself approval, execution or shared-file commit rights that root, PROME/AUTONOMY.md or ROSTER do not give; a relayed word treated as Will's approval on a gated surface.
- **Trade path** weaker than root rules #5 and #10 (proposal → Will approves → record), any execution language, and expiry/sell/roll reminders to Will (USER.md § No expiry nagging, 2026-10-20).
- **Routing**: market signals routed around WALTER; self-authored inbox packets left uncommitted (carve-out ①).
- **Runtime assumption** (new this pass): a step that only works on one runtime without saying so — e.g. requires Claude-only tools (SendMessage, ListAgents, Agent/Task, hooks) or Codex-only mechanics — where root/COMPLETION_SPEC say to detect tools rather than assume them.
- **Stale invoker**: a step that tells the desk to run a check PROME retired on 2026-10-31 (WQ-578: boot fire-time scan, agent-freshness line, handwritten-calendar coverage, HEARTBEAT chain check, boot/closeout symmetry, DOCKET row-cap, pipe-rc hook) or a script/path that no longer exists (check with `ls`/`git ls-files`).
- **Canon contradiction**: a file another file names canonical, contradicted.

## Your job
Read each file in your scope WHOLE (a file over ~50 KB: in chunks; record ranges and the final line covered). For every instruction line that fails the criterion or hits a HIGH class, write a ledger row. Do not list KEEP lines unless a KEEP is a deliberate stricter-than-root clause worth noting. Prefer the lines that cost the most to read for the least behaviour (long ⚠️ history blocks inside steps, triple restatements).

## Ledger format (markdown; write it incrementally so a crash keeps partial work)
- Header: reader name, each file with byte size and coverage (WHOLE / PARTIAL with ranges, final line read).
- Findings table: `id | file:line | class (GIT-SAFETY / AUTHORITY / TRADE / ROUTING / CARVE-OUT / RUNTIME / STALE-INVOKER / CANON-CONTRADICTION / DUPLICATE / HISTORY-IN-STEP / MECHANIZED / MODEL-OBSOLETE / OTHER) | severity HIGH/MED/LOW | verdict STRIKE/REWRITE | quote ≤25 words | proposed direction (one line, shorter text) | strongest refuter you considered`.
- Per-file one-line summary: approximate bytes a strike/rewrite would save.
- A short "where I could be wrong" section.

Rules: quote exactly; never claim a whole read that did not happen; a clause stricter than root and safe is KEEP; severity honesty (a duplicate is LOW, a git-safety weakening is HIGH); do not propose new scripts, rules or steps. Do not message anyone; just write the ledger and reply with a ≤15-line summary (counts by class and severity, every HIGH row in one line each).
