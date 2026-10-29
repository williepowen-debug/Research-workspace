# PROPOSAL — the pull rule: make `git pull --rebase` the one form, and let Git's refusal be the rule
**Written 2026-10-29 12:1x ET (PROME prome-5c).** Origin: DEWEY, in its Will-launched window 11:37–11:46 ET (relayed by Will to PROME 12:05 ET). Status: **PROPOSAL — awaiting Will's word; plan read owed before any canon edit** (`PROME/CLAUDE.md` § Canon drafts live in the ruling record). Process class: ONE change (root canon + its two carrier manuals in one edit set).

## What is true today (verified at the artifacts, 12:1x ET)
1. `git config pull.rebase` = `false` in this clone, so a **plain `git pull` MERGES**. A merge pull with a dirty tree succeeds whenever the incoming commits do not touch the dirty paths — it does not refuse. DEWEY's claim is correct.
2. **`git pull --rebase` refuses whenever ANY tracked file is modified or staged, whoever owns it** ("cannot pull with rebase: You have unstaged changes" / "Your index contains uncommitted changes"). Untracked files do not block it. That refusal is exactly the protection the root rule wants, applied mechanically.
3. Root `CLAUDE.md` § Git Protocol "Never" list (L105) says: *pull when other agents have uncommitted local changes (sole exception: session-end step 3's non-ff recovery, and only after its dirty-path overlap check passes)*. `docs/GIT_WORKTREE_PROCEDURES.md` § Before pulling steps 1–2 say: check for changes outside your directory; if any, **STOP. Do not pull.** `PROME/BOOT.md` step 0 says: *If dirty/untracked/staged, do not pull.*
4. Read literally, (3) blocks every pull on a busy box — today 11 WALTER cache directories are untracked, and desks read "untracked ⇒ do not pull" as a protocol breach to report (DEWEY reported one yesterday and one today; both false alarms). The fleet memory `finding_concurrent_agents_one_box_is_supported` already says concurrent same-box desks are intended.
5. **18 desk `CLAUDE.md` files carry a bare `git pull` boot line, and every one of them says "follow the pull protocol in root CLAUDE.md."** They defer to root. Fixing root fixes the fleet; no 18-file sweep is needed. DEWEY may change its own line (C4 class: no authority, route or threshold moves; PROME verifies).

## The change (exact text; one edit per file, same sitting, after the plan read and Will's word)

### A. Root `CLAUDE.md` L105 — replace the clause `pull when other agents have uncommitted local changes (sole exception: session-end step 3's non-ff recovery, and only after its dirty-path overlap check passes)` with:
> pull with a plain `git pull` (this clone's `pull.rebase` is `false`, so a plain pull MERGES around other agents' dirty files instead of refusing) or with `--autostash` outside session-end step 3's non-ff recovery. **`git pull --rebase` is the one pull form.** Git refuses it while ANY tracked file is modified or staged, whoever owns it; that refusal IS the rule, never an error to work around — stop, never stash, reset or commit another agent's work, `git fetch origin` and read what you need from `origin/master`, pull again after they commit. A rebase that stops on a conflict in a commit you did not author ⇒ `git rebase --abort`, flag to PROME. Untracked files (caches, drafts) never block a pull.

### B. `docs/GIT_WORKTREE_PROCEDURES.md` § Before pulling — replace steps 1–3 with:
> 1. `git pull --rebase` — the only pull form. Never a plain `git pull` (merges; `pull.rebase=false`), never `--autostash` (session-end step 3 excepted).
> 2. If Git refuses because of modified or staged files: **STOP — the refusal is the protocol working.** If the blocking files are yours, commit them pathspec-scoped and pull again. If they are another agent's, do not stash, reset or commit them; `git fetch origin` and read from `origin/master`; pull again after they commit.
> 3. If the rebase stops on a conflict inside a commit you did not author: `git rebase --abort` and flag to PROME. Your own uncommitted files may be tucked away first with `git stash push -- AGENTS/<YOUR_NAME>/` → `git pull --rebase` → `git stash pop` (your paths only).
Steps 4–5 unchanged.

### C. `PROME/BOOT.md` step 0 — replace `If clean/safe, git pull --rebase. If dirty/untracked/staged, do not pull; read local continuity first and ask/triage.` with:
> `git pull --rebase` (root Git Protocol: the one form). If Git refuses on modified or staged files, that is the rule working: do not stash or pull another way; fetch, read `origin/master`, note the deferred pull in the boot report. Untracked files never block.

## What does NOT change
Pathspec commits only · never force · never resolve another agent's conflicts · session-end step 3's non-ff recovery and its dirty-path overlap check (the only place `--autostash` is allowed) · the carve-outs · ONE machine at a time (`MACHINE_LOCAL.md`) — that rule is about machines, not desks.

## Why this is a tightening, not a loosening
The current rule asks every agent to run a judgment check ("are other agents' directories modified?") that Git already runs mechanically and more completely (it also catches staged files and files outside `AGENTS/`). The current rule's literal reading on untracked files produces false alarms that train desks to ignore it. After the change, the only pulls that remain possible are the one that cannot sweep anyone's work.

## Neighbours considered (WQ-229)
ordinary: clean tree ⇒ rebase pull as today · overlap: your own dirty files AND another desk's ⇒ Git refuses; commit yours, still refused until theirs commit — correct · wrong owner: a desk's rebase replays another desk's unpushed local commits (hash rewrite) — already accepted at root step 3 ("verify by subject"); conflict inside such a commit ⇒ abort, never resolve (new step 3) · missing information: `pull.rebase` unset on a fresh clone behaves the same (Git 2.43 warns and merges by default) — the rule names the form explicitly so the config does not matter · concurrent: two desks pulling at once — Git's index lock serializes; a refusal is retried, never forced.

## Reads
Plan read: PENDING (Sonnet coldreader, WQ-447; one read on this record). Result read: PENDING (one, after the single edit). Will's word: PENDING.
