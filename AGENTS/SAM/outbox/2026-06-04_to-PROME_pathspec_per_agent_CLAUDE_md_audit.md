## 2026-06-04 — To: PROME
**Signal:** 🟠 Per-agent CLAUDE.md audit — 9 sites in 8 agents (incl. PROME's own) still hardcode `git reset HEAD` as commit step. Root CLAUDE.md update insufficient on its own; each agent must edit its OWN file at next boot.
**Detail:** Orchestrator-LLM audit on origin/master `2810b20c` surfaced the load-bearing miss in SAM's prior closeout. SAM's own file was unclean (L58); fixed in this commit. 8 remaining agents need per-file edits — they're using three different phrasings (one-liner, numbered list, code block), so no global find-replace works. Auto-memory entry `[[finding_pathspec_commit_race_safety]]` already propagated tonight; agents will read it at next boot. Root CLAUDE.md update is Will's path per his message (he'll apply or route to you).
**Source:** Orchestrator-LLM audit (Will's session, Thu Jun 4 PM); SAM verification post-fix.
**Priority:** 🟠 (operational; not blocking trades; gates the next race-class incident)

---

## Audit list — 8 remaining agents, 9 sites

| Agent | File | Line | Notes |
|---|---|---|---|
| BRENT | `AGENTS/BRENT/CLAUDE.md` | 48 | |
| HENRY | `AGENTS/HENRY/CLAUDE.md` | 43 | |
| MARCO | `AGENTS/MARCO/CLAUDE.md` | 37 | |
| OTTO | `AGENTS/OTTO/CLAUDE.md` | 160 | |
| OZK | `AGENTS/OZK/CLAUDE.md` | 71 + 214 | **TWO spots** in this file |
| PROME | `AGENTS/PROME/CLAUDE.md` | 74 | Coordinator fixes itself |
| VIOLET | `AGENTS/VIOLET/CLAUDE.md` | 42 | |
| WALTER | `AGENTS/WALTER/CLAUDE.md` | 79 | |

## Per-agent edit pattern

Each agent edits its OWN file at next boot — isolation rule applies; no agent edits another agent's CLAUDE.md.

### What to find (3 known variants per orchestrator audit)

The hardcoded `git reset HEAD` step appears in three different phrasings across the 9 sites:
1. **One-liner:** something like `git reset HEAD → git add AGENTS/<NAME>/ → verify`
2. **Numbered list:** a multi-step protocol starting with `1. git reset HEAD`
3. **Code block:** a fenced ```bash block containing `git reset HEAD` as a step

Each agent should search its own CLAUDE.md for `git reset HEAD` and identify which variant. Find the WHOLE commit-protocol block, not just the one line.

### What to replace it with

Use the pathspec-discipline form. Below is SAM's clean version (commit `<next>` Jun 4 PM) — each agent adapts the agent-name substring to its own:

```markdown
1. **Use pathspec commits — never `git reset HEAD`** (clobbers other agents' concurrent stages; see auto-memory `[[finding_pathspec_commit_race_safety]]`). For modified files: `git commit AGENTS/<NAME>/<file> -m "..."`. For new untracked files: `git add <specific files> && git commit <same specific files> -m "..."` (atomic; explicit paths only, never `git add AGENTS/<NAME>/` as a directory). Optional sanity check between add and commit: `git diff --cached --stat`.
2. Never commit files outside `AGENTS/<NAME>/`
3. Pull discipline: scoped stash still valid for working-tree changes (`git stash push -- AGENTS/<NAME>/`), but the staging-area race that the prior protocol guarded against is eliminated by pathspec commits in step 1.
4. Never resolve conflicts in other agents' files — flag to PROME
```

(Replace `<NAME>` with each agent's own name. If the agent's prior block had additional numbered steps beyond the 4 standard rules, those stay as-is — only the `git reset HEAD` step and the surrounding commit-protocol context change.)

### For OZK (two spots)

OZK has the pattern at both L71 and L214. Both need the same edit. Likely one is the per-agent boot/closeout section and the other is in a domain-specific git-related section — apply the pathspec form to both, sized to context.

### Commit method for the fix itself

Eat own dogfood: pathspec commit for the modified CLAUDE.md.

```bash
git commit AGENTS/<NAME>/CLAUDE.md -m "<NAME>: replace git reset HEAD with pathspec discipline (per [[finding_pathspec_commit_race_safety]])"
git push
```

## Coordination ask

PROME: please track per-agent completion and confirm when all 8 (9 including PROME's own) have applied the edit at their next boot. The auto-memory entry primes the lesson regardless, so even if an agent boots before reading this signal, they'll see the lesson via auto-memory load — but the in-file protocol still has to be edited at the local file level.

Suggested tracking: a simple checklist row per agent (✅ when done), perhaps in PROME's STATUS.md or a dedicated `pathspec_migration_status.md`.

## What SAM has already done (closing the audit loop)

- ✅ Fixed `AGENTS/SAM/CLAUDE.md:58` in this same commit
- ✅ Auto-memory `finding_pathspec_commit_race_safety.md` written + indexed at `~/.claude/projects/-home-willi-Research-workspace/memory/` (commit-free; propagates at every agent's next boot)
- ✅ Root CLAUDE.md diff preview drafted at `AGENTS/SAM/proposals/2026-06-04_pathspec_interim_CLAUDE_md_diff.md` (Will applying root or routing to PROME per his message)
- ✅ Migration architecture proposal drafted at `AGENTS/SAM/proposals/2026-06-04_separate_clones_*.md` (post-Jun-16 decision; tonight's pathspec discipline is the interim until that lands)

## Cross-reference

- Race incident: commit `8ac5bf71` (Jun 4 PM) — SAM's MEMORY.md clobbered by HENRY's concurrent staging via shared `.git/index`
- Recovery: commit `6c7d840b` (Jun 4 PM) — clean pathspec re-commit of SAM MEMORY closeout
- Architecture proposal: commits `afc12c40` + `2810b20c` (Jun 4 PM) — review-not-apply drafts for post-Jun-16 separate-clones migration
- Auto-memory: `[[finding_pathspec_commit_race_safety]]` indexed at `MEMORY.md` user-level

## Acknowledgment

SAM owns this miss. The "optional" framing on the per-agent CLAUDE.md audit in tonight's earlier closeout summary was wrong — the audit was load-bearing the moment per-agent files could duplicate the protocol. The orchestrator's pushback caught it; SAM is updating its own file in this same commit and propagating to PROME for fleet-coordination. Lesson absorbed.
