---
name: pathspec-commit-race-safety
description: "Use `git commit <pathspec>` for modified files and atomic `git add <files> && git commit <same files>` for new files; never `git reset HEAD`. Required when multiple agents share a `.git/index`. Peers' staged/committed work seen during concurrent operation is EXPECTED, not an anomaly — commit only your own paths, leave theirs untouched."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 110e9b3c-07c3-4222-87b9-57e8595e4580
---

When multiple agents share one working directory and one `.git/index`, the staging area is a global shared resource. Operations that touch the index — especially `git reset HEAD` — can clobber another agent's pending stages between their `git add` and their `git commit`. This was the mechanism behind mis-attributed commit `8ac5bf71` (Jun 4 2026): SAM ran the standard `git reset HEAD` + `git add AGENTS/SAM/MEMORY.md`, verified with `git diff --cached --stat`, then committed — but HENRY's concurrent process ran its own `git reset HEAD` + `git add AGENTS/HENRY/...` in the window between SAM's verify and SAM's commit. SAM's commit then captured HENRY's staged files under SAM's commit message.

**Why:** the shared `.git/index` is one file. Any agent's `git reset HEAD` un-stages every agent's pending stages. The standard protocol (reset → add → verify → commit) has a window between verify and commit where another agent can clobber. The protocol is correct under the assumption of single-agent operation; it fails as soon as agents are concurrent.

**How to apply:**

- **For already-tracked files you've modified:** use `git commit AGENTS/<NAME>/<file> -m "..."` directly. Pathspec commit captures working-tree content, bypasses the staging area entirely — race-safe regardless of what other agents do to the index.

- **For new (untracked) files:** `git add <specific files> && git commit <same specific files> -m "..."`. The atomic chain minimizes the staging-area window; the pathspec on commit means even if another agent stages something in the microsecond between `add` and `commit`, your commit only takes the named files. Use explicit file paths, never directory wildcards (`git add AGENTS/<NAME>/` can race-collide; `git add AGENTS/<NAME>/specific_file.md` cannot).

- **Never use `git reset HEAD`** in a shared-index environment. If you have stuff staged from a previous operation and want to start over, either commit the staged stuff (pathspec or otherwise) or leave it alone. Reset is the race trigger.

- **Verification step is optional** under pathspec discipline. `git diff --cached --stat` between add and commit is the canonical sanity check, but pathspec commits are race-safe with or without it.

**When this stops mattering:** the architectural fix is separate clones per agent (each with its own `.git/index`). Under that model, `git reset HEAD` is local-only and can't clobber anyone. See [[SAM proposals 2026-06-04 separate clones]] (review-not-apply drafts in `AGENTS/SAM/proposals/`). Until that migration lands, pathspec is the interim discipline.

**Pre-existing protocol that this refines:** [[feedback_agent_git_isolation]] ("never stash/commit other agents' files") and [[feedback_check_staged_before_commit]] ("run git diff --cached before committing"). Both rules are still valid but insufficient on their own — the `8ac5bf71` race happened despite both being honored, because the discipline assumed a non-concurrent model. Pathspec discipline closes the gap.

**Validated:** Jun 4 2026 — caught and corrected `8ac5bf71` race within minutes; SAM session-closeout MEMORY.md re-committed cleanly via `git commit AGENTS/SAM/MEMORY.md -m "..."` as `6c7d840b`. Subsequent commit `afc12c40` (proposal-file additions) used the atomic add+commit pattern for new files with explicit paths — clean, no collision despite BROCK being concurrently active.

**Interpretation during live concurrent operation (added 2026-07-05, Will correction to NEXUS):** the pre-commit sanity check (`git status -- AGENTS/<YOU>/`, and the wider index view) will routinely surface OTHER agents' staged AND committed work when they are online and working — **this is the EXPECTED, healthy state of concurrent multi-agent operation, NOT an anomaly and NOT evidence a peer's discipline is slipping.** The check's job is to keep YOUR commit clean (commit only your own paths via pathspec), not to health-audit peers. Do NOT: characterize a peer's staged files as a problem, `git reset` them, commit them, or flag them as a lapse. Correct response = commit your own files by pathspec, leave theirs staged/committed untouched; their committed work rides the next push-train ([[finding_push_train_pattern]]) and they push it at their own closeout ("committed work can be pushed as part of a push train" — Will). **Concrete (2026-07-05):** NEXUS's sanity check surfaced ~100 RED files staged mid-session (RED draining a 98-file WALTER inbox backlog); NEXUS's pathspec commit correctly ignored them and RED committed its own work moments later — zero damage. The error was purely interpretive (calling it an anomaly / "discipline slipping"), not mechanical. **Corollary:** the "serial single-machine (desktop⇄laptop)" model in root CLAUDE.md is about MACHINES; multiple AGENTS run concurrently on one machine and share the index — so foreign entries in `git status` are the norm, not the tripwire (the tripwire is safe-push aborting non-ff, which means a 2nd MACHINE pushed).

Cross-agent transferable: applies to ANY agent operating in the shared-folder environment (SAM, HENRY, BROCK, BRENT, CARL, REGINALD, OZK, RED, LIQUID, HENRY, HAWK, BRENT, NEXUS, and any future agents). Should propagate via auto-memory + root CLAUDE.md update.

---

### n+1 — the exemption that defeats the rule: `--allow-empty` with no pathspec (LABOR, 2026-08-27)

**The pathspec rule survives every commit that has files, and dies on the one that doesn't.**

At closeout I recorded a note-only commit:

```
git commit --allow-empty -F /tmp/msg.txt      # ⛔ no pathspec
```

**Result: it swept another agent's staged rename into my commit, and pushed it.** Content intact, tree correct — but their archive move is now recorded under my unrelated closeout message, permanently.

> ★ **"Empty for me" is not "empty for the index."** `--allow-empty` does not mean *commit nothing*; it means *commit what is staged, and don't complain if that's nothing*. On a shared `.git/index` with concurrent sessions, **`--allow-empty` with no pathspec is functionally `git commit -a`.**

**Why the habit fails exactly here and nowhere else:** every *normal* commit has files, so you write the pathspec automatically. **A note-only commit has no files to name — so the parameter that carries the safety silently has nothing to hold, and dropping it feels not just harmless but grammatical.** The rule is obeyed 100% of the time it is visible and 0% of the time it isn't.

**Fix — one of:**
- `git commit --allow-empty -- AGENTS/<YOU>/ -F msg` — keep the pathspec even when it matches nothing. **The pathspec is the guard, not the target.**
- Better: **don't use empty commits for notes at all.** Append the note to a file you own and commit that file by path. A note nobody can `git show --stat` is weak documentation anyway.
- **Always `git show --stat HEAD` after any commit you did not pathspec** — that is what caught this, one command too late to prevent it and just in time to report it.

⚠️ **Do NOT try to repair it:** no `--amend` (rewrites whoever holds HEAD, and it may be pushed), no `reset` (global unstage on a shared index), no revert-and-redo into another agent's tree. **A wrong message over a correct tree is documentation debt — note it, tell the owner, never rewrite it.**

*(Companion: `[[finding_concurrent_commit_index_race]]`. The general shape is `[[finding_guard_correctness_and_wiring_are_independent]]` — the guard was correct and, in this one call, simply not wired in.)*

**The RECEIVING end, from the desk it happened to (TERRY, same incident, cited with permission).** The write-up above is sender-side only. **The victim cannot see this in `git status`.**

The symptom presents as ***"my staged work vanished without a commit of mine"*** — which reads like a **lost stash**, not like someone else's commit. What actually exposed it:

```
git ls-tree HEAD -- <your path>     # file is ALREADY at its new location
git diff --cached                   # ...and nothing is staged
```

**That disagreement — present in HEAD, absent from the index — is the signature.** `git status` is clean and tells you nothing, because from git's point of view nothing is wrong: the work *was* committed, just not by you.

> ★ **If staged work disappears with no commit of yours, check `git log -- <your path>` for someone ELSE's commit before concluding you lost a stash.** The default hypothesis (I dropped it) sends you looking in the wrong place, and the reflex cure for a lost stash — re-stage and re-commit — would have produced a **duplicate** here.

**And the generalisation TERRY drew, which is stronger than the `--allow-empty` framing:** *"I have nothing staged"* is **never a property you can establish by introspection** on a shared index. **The pathspec does not describe your intent — it bounds what the index is allowed to hand you.** Any pathspec-less commit is functionally `git commit -a` against whoever else is mid-stage on this box.

*(Both ends annotated their own commits: the sweeping commit is named in the receiving desk's next message so `git log` on the affected path has a pointer. **Annotate from both ends — the reader lands on whichever one they grep first.**)*
