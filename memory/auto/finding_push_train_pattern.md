---
name: finding-push-train-pattern
description: "Inside a Will-opened push window, one agent's push (no refspec) ships ALL agents' committed-but-unpushed commits to origin via pull/rebase — only one agent need push. QUALIFIED 6/8: under the standing 'push is Will-coordinated, not a closeout step' rule, this fires inside a coordinated window, NOT automatically at closeout."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 6aefca3b-c324-4c82-8d52-f261b8995394
---

> **⚠️ Qualified 2026-06-08:** The *mechanic* below is still true; its *trigger* changed. Root CLAUDE.md no longer tells agents to push at session end — **pushing is Will-coordinated** (commit local, defer push). So the push-train no longer fires automatically when "the first agent closes out cleanly"; it fires when **Will opens a push window** and one agent pushes, sweeping everyone's committed-but-unpushed work up together. Do **not** read this memory as license to push at closeout. See root `CLAUDE.md` Git Protocol + `[[feedback_defer_push_coordinate]]`. The original framing below assumed routine closeout pushes, which no longer happen.

When multiple agents share the repo and have pending local commits (each blocked from pushing because another agent is mid-session with uncommitted work), the first agent to close out cleanly will push *everyone's* pending commits up to origin via their standard `git push` — which doesn't filter by author.

**First concrete instance:** 2026-05-21 PM. CC-Prome had 2 commits pending push (FORGE rehab Steps 1-4 + Step 5 PROME state propagation); OTTO had 2 commits pending push from earlier in the day; SENTRY had 1 commit ahead on origin. All three of us were blocked from pushing because WALTER was mid-session with uncommitted state files + 10 new BOARD SIGs + new inbox items. Will asked: "your commit might be pushed by Walter perhaps? Can you check?" — and yes, WALTER's close-out push had just pulled/rebased my 2 + OTTO's 2 + the SENTRY commit, all up to origin together. Local + origin in sync (0/0) without any CC-Prome push attempt.

**Why this works:** `git push` (no refspec) pushes all local commits ahead of upstream on the current branch. WALTER's pull/rebase before push standardly replays all local-only commits on top of pulled commits — including ones authored by other agents. As long as each agent:
- staged only their own files,
- committed cleanly,
- and didn't `git reset` / `git rebase -i` other agents' commits,

then the pull/rebase preserves everyone's commits and the push ships them all.

**How to apply:** When you have a pending push blocked by another agent's uncommitted work, you don't always need to wait for a window where the working tree is clean and pull/push it yourself. If you see signs another agent is mid-closeout (e.g., LAST_COMPLETION.md modified, STATUS.md modified, new BOARD signals appearing), you can:
- commit your work locally,
- note the deferred push in SCRATCH for next-session context,
- and check origin after the other agent's closeout to confirm your commits rode their push train.

Saves you from doing a separate clean-window pull/push cycle. Note: this works for *push* coordination. It doesn't help with *pull* timing — pulling before another agent commits will still risk stashing-then-losing their uncommitted work, so the "don't pull when other agents have uncommitted work" rule still holds. The asymmetry: pushing is safe because you only ship what's local; pulling is dangerous because it can disrupt working-tree state.

Doesn't apply when: (a) your push is genuinely time-sensitive (e.g., other agents need your commits visible before they boot), (b) no other agent is close to a closeout (waiting indefinitely is worse than coordinating a clean window), (c) the other agent's protocol compliance is suspect (e.g., they `git add -A` and might sweep up your local-only work into their commit — at which point your "commit" exists but with their author tag).

Related: [[feedback-agent-git-isolation]] (don't touch others' files), [[feedback-check-staged-before-commit]] (verify scope before commit), [[feedback-behavior-language-over-hash-pinning]] (don't anchor state files on hashes that may rebase).
