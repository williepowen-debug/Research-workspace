# Git worktree procedures — canonical continuation of root Git Protocol

The named section must be read in full before its action. Authority and path grants remain in root `CLAUDE.md` § Git Protocol.

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

**Before pulling:**
1. `git pull --rebase` — the only pull form. Never a plain `git pull` (merges; `pull.rebase=false`), never `--autostash` (session-end step 3 excepted).
2. **The dirty-owner stop is Git's own refusal.** If it refuses on modified or staged files that are YOURS: commit them pathspec-scoped (preferred), or `git stash push -- AGENTS/<YOUR_NAME>/` → pull → `git stash pop` — and pop even if the pull was refused. If the blocking files are another agent's: STOP; do not stash, reset or commit them; continue on your current checkout, `git fetch origin` and read from `origin/master`; pull again after they commit. If Git aborts because an incoming commit adds a path you hold untracked: move yours aside, never delete, pull again.
3. If the rebase stops on a conflict inside a commit you did not author (`git log -1 --format=%s REBASE_HEAD` — the subject's desk prefix names it; the author field is one shared account): `git rebase --abort` (fetched refs stay updated; pop any stash you made), flag to PROME. A conflict in your own commit is yours — step 5 governs the files.
4. If stash pop fails: `git stash drop` is OK **only if YOUR files are already committed.** Never drop a stash containing other agents' work.
5. Never resolve merge conflicts in another agent's files — flag to Prome.

