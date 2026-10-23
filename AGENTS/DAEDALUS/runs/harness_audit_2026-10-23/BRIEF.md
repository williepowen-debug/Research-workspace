# Harness Audit #3 — reader brief (DAEDALUS, 2026-10-23)

Repo root: /home/willi/Research-workspace. Read-only against the repo: NEVER edit, stage or commit any repository file. Your only write is your own ledger file at the scratchpad path your prompt names.

## What a "harness" is
The instruction layer each desk boots from and closes out with: `AGENTS/<NAME>/CLAUDE.md`, any standalone `CLOSEOUT.md` or `OPERATIONS.md`, PROME's BOOT/CLOSEOUT/CLAUDE/SYSTEM/AUTONOMY/ORCHESTRATION_PLAYBOOK, and root CLAUDE.md, AGENTS.md and USER.md. One-off `research/*/CLOSEOUT.md` task files are OUT of scope.

## The criterion (ratified 2026-07-07; the method is in AGENTS/DAEDALUS/HARNESS_AUDIT_2026-07-07.md §1–3 — read §3)
Keep a step only if it is ALL of:
- (a) an ACTION or behaviour gate;
- (b) not already mechanized (a script does it);
- (c) not owned elsewhere (not a restatement of root canon or another owner's rule).
Every candidate gets one verdict: KEEP · STRIKE · REWRITE.

## Canon contradictions — always report, ranked high
- Git safety: anything weaker than root CLAUDE.md § Git Protocol and docs/GIT_WORKTREE_PROCEDURES.md. Examples: git add . / -A, an unscoped commit, amend, reset HEAD, a restore over another desk's directory, force, a pull with foreign dirty paths, "escalate on a bare non-ff recurrence" (root says ordinary traffic).
- Signals routed around WALTER (root: never).
- Self-authored inbox packets left uncommitted (root carve-out ① says the author must commit them).
- Expiry, sell or roll reminders to Will (root USER.md § No expiry nagging, 2026-10-20).
- Trade execution or approval language weaker than root rules #5 and #10.
- A file another file says is canonical, contradicting it.

## Your two jobs
1. **Re-test the 2026-10-08 changelist lines for your files at HEAD.** The changelist is AGENTS/DAEDALUS/runs/2026-10-08_HARNESS_CHANGELIST.md (summary); line detail is in _A.md and _B.md beside it. For each line ID that names one of your files, give a verdict:
   - FIXED — cite the HEAD line that resolves it;
   - STILL-LIVE — quote the HEAD line;
   - CHANGED — the text moved or became a different problem; say what;
   - CANNOT-LOCATE.
2. **Audit the delta since BASE** = commit 3d47a7d9d (2026-10-08 16:49 ET). For each of your files, run `git diff 3d47a7d9d HEAD -- <file>` and apply the criterion and the contradiction list to every ADDED or CHANGED instruction line. For a file created after BASE, read it whole. A file over ~50 KB: read it in chunks and record the ranges you covered.

## Ledger format (markdown; write it incrementally so a crash keeps partial work)
- Header: your reader name, the files in scope with byte sizes, and coverage per file (FULL-DIFF / WHOLE / PARTIAL with ranges).
- Table A, changelist re-test: `line_id | file:line@HEAD | verdict | evidence quote (≤25 words)`.
- Table B, new findings: `id | file:line@HEAD | class (GIT-SAFETY / ROUTING / CARVE-OUT / EXPIRY / TRADE / CANON-CONTRADICTION / DUPLICATE / HISTORY-IN-STEP / MECHANIZED / STALE-POINTER / OTHER) | verdict KEEP/STRIKE/REWRITE | quote ≤25 words | proposed direction (one line) | strongest refuter you considered`.
- Then a short "where I could be wrong" section.

Rules:
- Quote exactly. Line numbers at HEAD.
- Never claim a file was read whole if it was not.
- A clause that is stricter than root and safe is KEEP, with a note.
- Do not propose new scripts or new rules; only strike, rewrite or point at canon.
- Severity honesty: a duplicate is LOW; a git-safety weakening is HIGH.
