# Proposal — Replace CLAUDE.md "Git Protocol" Section (Separate-Clones Architecture)

**Status:** REVIEW-NOT-APPLY draft. Land via Will-and-Prome decision, not unilaterally.
**Author:** SAM, Thu Jun 4 2026 (drafted while context fresh; race-condition incident `8ac5bf7` is the immediate trigger)
**Pairs with:** `2026-06-04_separate_clones_migration_checklist.md`
**Earliest execution window:** post-Jun-16 BOJ MPM (current pre-meeting period is wrong window — too many live decisions)

---

## What this proposal changes

Replaces the entire `## Git Protocol` section in root `CLAUDE.md` (~L37-66 in current version, ~30 lines) with a much shorter section reflecting the separate-clones architecture. Net effect: ~25 lines removed, ~10 lines added.

The proposal does NOT change:
- File ownership boundaries (`AGENTS/<NAME>/` per-agent)
- The "GitHub is single source of truth" principle (this proposal actually realizes that principle for the first time)
- Domain-level coordination (Prome routing for shared files, agent-to-agent signals via inbox/outbox)

---

## Current section (to be replaced)

The current `## Git Protocol` section is structured around a SHARED working directory + SHARED `.git/index`. About 90% of its content is babysitting for that sharing:

- `git reset HEAD` to clear shared staging
- Scoped stash `git stash push -- AGENTS/<NAME>/`
- "STOP. Do not pull if others have uncommitted work"
- "Never resolve another agent's conflicts"
- Three sequential checks before pushing
- Two-option fallback ("Option A: flag Will / Option B: defer push")

**All of this exists because multiple agents reach into ONE `.git/index` file.** With separate clones, none of it is needed.

The Jun 4 race condition (`8ac5bf7` carries HENRY's work under a SAM commit message) is the proximate trigger: both agents followed the existing protocol; the protocol was insufficient because the shared `.git/index` exposes a TOCTOU window between `git diff --cached` and `git commit`.

---

## Proposed replacement section

```markdown
## Git Protocol

Each agent runs in its **own clone** of the repo at `~/agents/<NAME>/`. GitHub is the single source of truth; agents only see each other's work after a push lands and the other pulls.

**Session start:**
```
git pull --rebase
```

**Session end:**
```
git commit AGENTS/<NAME>/<files> -m "..."
git push
# if rejected: git pull --rebase && git push   (retry)
```

Always commit by pathspec (`git commit <path> ...`), never by index (`git add ...; git commit`). Pathspec is race-safe even in your own clone and matches the architecture's intent.

**Owned write-set per agent:**
- Read-write: `AGENTS/<NAME>/` and any path explicitly delegated
- Read-only (via pull only): every other `AGENTS/<other>/`
- Shared files (HEARTBEAT, FORGE/, root configs): route through Prome — never write directly

**What's NOT in this protocol anymore (and why):**
- `git reset HEAD` / `git add` / staging-area discipline — your clone, your index, no race
- `git stash` for cross-agent isolation — nothing to isolate from; other agents' work isn't in your clone
- "Don't pull if others have uncommitted work" — you can't see their uncommitted work; impossible to clobber it
- Resolving other agents' conflicts — rare under disjoint ownership; rebases auto-merge most of the time

**Push collisions are harmless:** GitHub rejects the second push, your agent does `pull --rebase` and retries. Nothing is lost; nothing is mis-attributed (each commit is built in isolation from one agent's files).

**Never:** force-push, push to other agents' files (you can't — your clone doesn't have their write-set), commit shared files (HEARTBEAT, FORGE) without Prome routing.
```

---

## What gets deleted

For audit clarity, the specific lines/concepts removed from current CLAUDE.md `## Git Protocol`:

| Concept | Current text (gist) | Why deletable |
|---|---|---|
| `git reset HEAD` before staging | "clear staging area" | Your clone, your staging — no other agent reaches in |
| Scoped stash | "`git stash push -- AGENTS/<NAME>/`" | No cross-agent state to stash around |
| Three-step staging check | "verify nothing unexpected → `git restore --staged`" | Pathspec commit makes this irrelevant |
| Two-option fallback on dirty tree | "Option A flag Will / Option B defer push" | The dirty-tree case can't happen — your clone is yours |
| "Never resolve another agent's conflicts" | (multiple references) | Conflicts in others' files require their explicit edits to your clone, which won't happen |

Net section length: ~30 lines → ~25 lines, but the cognitive load drops dramatically because the remaining rules are all *necessary*, not *defensive*.

---

## What is preserved (load-bearing under separate clones too)

- File-ownership boundaries (`AGENTS/<NAME>/` write-set per agent)
- "GitHub is single source of truth"
- Domain coordination via inbox/outbox + Prome routing
- No force-push, no commits to shared files without routing

---

## Where I might be wrong

I am proposing changes to my own operating environment, with the side-effect that I work cleaner under them. That bias is real. The Will-and-Prome review IS the bias-check. These are the specific concerns I'd push myself on:

### 1. Cross-agent visibility cost (the main open question)

Today I can `cd ../HENRY` and read HENRY's STATUS.md, KB.tsv, workbook tsvs — including **unpushed** live state. With separate clones, that becomes: **I see HENRY's last PUSHED state only, after `git pull`.**

I claimed in the proposal that this is "likely cleaning up a fragile habit." That framing might be too glib. Honest assessment:

- **Frequency:** I read other agents' files multiple times per session (often during news-sweep synthesis, cross-agent signal preparation, or when integrating something HENRY/BROCK/LIQUID just landed). Not all of those reads need uncommitted state — many just need the last pushed state, which works fine under the new model.
- **The cases that break:** if HENRY is mid-session writing a thesis update and SAM needs to integrate from it RIGHT NOW, today SAM reads HENRY's working tree directly. Under separate clones, SAM has to wait for HENRY to commit + push, then SAM pulls. That introduces a real-time-coordination dependency.
- **The mitigation:** the inbox/outbox protocol already exists for exactly this case — cross-agent signals are supposed to be explicit, not implicit-via-shared-folder-read. So the "habit cleanup" framing isn't wrong, but it does require agents to actually USE the explicit channel rather than the implicit shortcut.

**The migration checklist's first sanity-check item must be: log how often agents read each other's UNcommitted state today, and validate that the inbox/outbox + pushed-state model can cover those cases.** If it can't, the answer might still be "separate clones with extra coordination tooling," not "shared folder is actually fine."

**Worktrees do NOT fix this either.** A worktree per agent still requires the other agent's worktree to be the current branch on disk to be readable — and worktrees can't share `master`, so they're all on different branches. Cross-agent reads under worktrees see committed-to-that-branch state, which still doesn't capture in-flight uncommitted work. Worth flagging so worktrees don't get floated as a fallback that solves the wrong problem.

### 2. I'm under-counting how often races actually happen

Tonight's race is dramatic (mis-attributed commit), but it's the first one I'm aware of in the operation's history. If races happen once every 2-3 months at this rate, the migration cost (cognitive + calendar + setup) may exceed the savings.

**Honest framing for Prome:** *the strength of the case for separate clones depends on race-frequency forecast as the operation scales.* At 5 active agents + 4 SAM sub-agents (today), races are rare-but-real. At 10+ agents, races stop being rare. The proposal assumes the trajectory is "more agents, not fewer" — if that assumption flips, the urgency drops.

### 3. The `.venv` strategy is bigger than this proposal addresses

This document focuses on the git protocol. The `.venv` strategy decision (per-agent vs shared) is deferred to the migration checklist as an open Will-decision at migration time. **I want to flag that I think this is the second-biggest decision behind the proposal itself**, not a minor "rough edge" — get it wrong and either (a) maintenance overhead multiplies by N agents, or (b) you reintroduce a shared-mutable-resource race in a different layer.

### 4. The migration cost is non-trivial in cognitive overhead

The atomic cutover is the right approach (per migration checklist) but it means every agent's launch environment changes simultaneously. That's a coordination cost paid against future races prevented. **I think the trade is worth it, but I am the agent that benefits most from it — Prome's coordination layer eats more of the migration cost than I do, and Prome's review of this proposal is the right check on whether I'm under-counting that cost.**

### 5. I might be wrong about which agent to pilot

The migration checklist proposes RED-first SETUP smoke-test (not live mixed-production). I picked RED because it has minimal cross-agent dependencies. **But that minimal-dependency property means RED is the WORST agent for validating cross-agent coordination changes.** If the goal is to test that the inbox/outbox + pulled-state model handles cross-agent reads cleanly, a more-coupled agent (e.g. LIQUID, which depends on signals from many other agents) would be a better test bed.

However: Will explicitly clarified that RED-first is a SETUP smoke-test (clone + venv + boot + one trivial push), not a coordination test. Under that scoping, RED is fine — coordination testing happens at atomic-cutover via the full set, not in a mixed-production interim. The "RED is too independent" concern lands against testing coordination, which isn't the smoke-test's job.

---

## Recommendation

Land this proposal as a Will-and-Prome decision at the post-Jun-16 calm session. If approved, paired migration checklist executes atomically. If declined or held, **pathspec commits continue as the tonight discipline** — they prevent the immediate race-class for free and don't depend on the architecture decision.

Tonight's `8ac5bf7` mis-attribution is recoverable (HENRY can author a follow-up clarification commit when they boot). The bigger lesson is the *predictability* of the failure under shared-folder + more-agents — that's what this proposal addresses.
