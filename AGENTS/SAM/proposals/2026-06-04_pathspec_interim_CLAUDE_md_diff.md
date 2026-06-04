# Proposal — Root CLAUDE.md "Git Protocol" Interim Update (Pathspec Discipline)

**Status:** REVIEW-NOT-APPLY preview. Apply via Will-or-Prome decision, NOT unilaterally — root `CLAUDE.md` is a shared file outside any agent's owned write-set.
**Author:** SAM, Thu Jun 4 2026
**Pairs with:**
- `2026-06-04_separate_clones_CLAUDE_md_section.md` (post-Jun-16 architectural migration — bigger replacement)
- `2026-06-04_separate_clones_migration_checklist.md`
- Auto-memory `[[finding_pathspec_commit_race_safety]]` (lesson + WHY)

**Scope:** This is the **interim** update — keeps the shared-folder architecture but eliminates the `git reset HEAD` race that mis-attributed commit `8ac5bf71`. The bigger separate-clones migration is a future, separate decision.

---

## What changes

Replace the existing `**Before committing:**` block in root CLAUDE.md (currently L70-74) and add a `git reset HEAD` line to the `**Never:**` block (currently L88). The rest of the `## Git Protocol` section (pull discipline, file-ownership rule, etc.) stays as-is.

**Net effect:** ~5 lines removed, ~10 lines added. Very small surgical change.

---

## Diff

### Section to REMOVE (current L70-74)

```markdown
**Before committing:**
1. `git reset HEAD` — clear staging area
2. `git add AGENTS/<YOUR_NAME>/` — stage only your files
3. `git diff --cached --stat` — verify nothing unexpected
4. If unexpected files: `git restore --staged <file>`
```

### Section to ADD (replaces L70-74)

```markdown
**Before committing — use pathspec commits, never `git reset HEAD`:**

`git reset HEAD` operates on the **globally shared** `.git/index`. If another agent is concurrently staging files in their `AGENTS/<other>/` path, your `reset HEAD` un-stages their work — and their next `git add` can clobber yours. This is what mis-attributed commit `8ac5bf7` (Jun 4 2026) — SAM's MEMORY.md was clobbered by HENRY's concurrent staging.

**For modified (already-tracked) files:**
```
git commit AGENTS/<YOUR_NAME>/<file> -m "..."
```
Pathspec commits capture the file's current content directly — no staging area involved. Race-safe.

**For new (untracked) files:**
```
git add <specific files> && git commit <same specific files> -m "..."
```
Atomic add + pathspec commit. The `git add` step is unavoidable for untracked files, but pathspec commit on the same explicit file list prevents another agent's concurrent `add` from sneaking in.

**Verification (optional):**
```
git diff --cached --stat
```
Use to verify if you want a sanity check, but pathspec commits are race-safe with or without it.

**Never use `git reset HEAD`** — it's the race-trigger. If you have stuff staged from a previous operation and want to start over, just commit the staged stuff (pathspec or otherwise), or leave it alone — but don't `reset HEAD`.
```

### Line to MODIFY (current L88)

**Current:**
```markdown
**Never:** force push, commit outside your directory without instruction, resolve another agent's conflicts, pull when other agents have uncommitted local changes.
```

**Replacement:**
```markdown
**Never:** force push, `git reset HEAD` (shared-index race trigger), `git add .` or `git add -A` (sweeps other agents' work), commit outside your directory without instruction, resolve another agent's conflicts, pull when other agents have uncommitted local changes.
```

---

## What does NOT change

- The **`## Git Protocol`** section header
- The opening framing: "Agents share one working directory and branch. **GitHub is the single source of truth.**"
- The blockquote: "`git add` ONLY files inside your own `AGENTS/<NAME>/` directory."
- The **At session start** block
- The **At session end** block
- The **Before pulling** block (stash + pull + pop discipline) — pull-side race is less acute and the protocol still works as-is
- The Key Directories table, Tools section, Reference section

All of those remain intact.

---

## Rationale

### Why this is interim, not final

The full architectural fix is **separate clones per agent** (post-Jun-16 migration; see paired proposals). Under that architecture, the entire `## Git Protocol` section gets simpler (no shared `.git/index` to race on). This interim update keeps the shared-folder model and just removes the worst race-trigger.

### Why pathspec specifically

`git commit <path>` builds the commit from the file's working-tree content, NOT from the staging area. Even if another agent has staged different files in the global index between your file-edit and your commit, pathspec ignores the staging area entirely and commits exactly what's in your specified path's working tree.

The atomic add+commit for new files has a *microsecond* race window (between the `git add` and `git commit`), but that window is several orders of magnitude smaller than the previous protocol's window (which spanned `git reset HEAD` + `git add` + `git diff --cached --stat` + `git commit`). In practice the atomic pattern is safe.

### Why not just "use pathspec when concerned"

Discipline rules work best when they're unconditional. "Use pathspec when other agents might be active" requires every agent to (a) know who's active, (b) judge concurrency risk, (c) remember to switch protocols. Always-pathspec is one fewer thing to think about, with no downside.

### What this does NOT solve

- **Untracked file commits still have a micro-window** between `git add` and `git commit`. Mitigation: keep that window minimal (single `&&` chain in bash). Acceptable risk under shared-folder; eliminated under separate clones.
- **Pull-side races** (stash + pull-rebase + pop). Less acute because pulls are explicit and infrequent; existing pull discipline still applies. Separate clones eliminate this too.
- **Shared-file commits** (HEARTBEAT, FORGE, root CLAUDE.md itself). Routing through Prome still required.

---

## Application instructions (for Will or Prome)

1. Verify the working tree is clean (`git status` shows nothing modified, nothing untracked in `AGENTS/`)
2. Apply the two edits above to root `/home/willi/Research-workspace/CLAUDE.md`
3. Commit by pathspec: `git commit CLAUDE.md -m "Git protocol: replace git reset HEAD with pathspec discipline (interim; addresses 8ac5bf7 race)"`
4. Push: `git push`
5. Next time any agent boots, they'll pull this change and read the new protocol

**Race-safety during the application:** since CLAUDE.md is a single file at repo root, the atomic-write + pathspec-commit pattern applies directly. No `git add` needed (CLAUDE.md is already tracked), so the only window is between `git commit CLAUDE.md` and `git push` — and a push collision is harmless (`git pull --rebase && git push` retry handles it).

---

## Where I might be wrong

1. **The interim might be unnecessary if separate-clones migration happens soon.** If Will + Prome decide to migrate within a week of this proposal, the interim CLAUDE.md change adds churn for ~1 week of benefit. Counter: the interim is still load-bearing during the pre-migration window because BROCK and possibly other agents will run sessions in that window; one race-incident per week is enough to make the change worthwhile.

2. **The replacement section is longer than the original.** I added ~5 lines explaining WHY (the `8ac5bf7` callout, the shared-`.git/index` mechanism). Could be cut to 5 lines if Will prefers terseness. My read: the "WHY" is what stops agents from regressing to old habits; worth the extra lines.

3. **I'm proposing changes to a shared file.** Standing rule: agents don't unilaterally commit shared files. This is a **proposal**, not an application — Will or Prome owns the apply step. I want to be explicit about that.

4. **There might be agents whose own per-agent CLAUDE.md duplicates the git protocol verbatim** rather than referencing the root. If so, those would need parallel updates. I haven't audited; worth a quick `grep "git reset HEAD" AGENTS/*/CLAUDE.md` before applying.

---

## Recommendation

Apply this interim update tonight or next session. The paired auto-memory entry (`finding_pathspec_commit_race_safety.md`) propagates the lesson to every agent's auto-load context at next boot, providing belt-and-suspenders coverage even before CLAUDE.md is updated.
