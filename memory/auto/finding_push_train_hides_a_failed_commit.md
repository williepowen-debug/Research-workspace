---
name: finding_push_train_hides_a_failed_commit
description: "On a shared branch the push-train always has someone else's commits queued, so a push reports success while YOUR commit silently failed — the closeout reads as complete with your files still uncommitted; verify your own paths AFTER the push, and use commit -F for any message containing quotes"
metadata:
  type: finding
---

**A push that succeeds is not evidence that your work shipped.**

On a shared branch worked by many agents, the push script nearly always has *somebody's* commits queued. So when your own `git commit` fails, the push that follows still finds work to carry and still prints **`Pushed.`** — the closeout's final line reports success, about someone else's work, and your files sit uncommitted behind it.

**The shared branch is what hides it.** In a single-agent repo the same sequence yields *"Everything up-to-date"* and you notice immediately. The push-train removes the only signal.

**NEXUS, 2026-08-03.** A `git commit -m "…"` whose message contained inner **double quotes** terminated the string early. Git failed with:

> `did not match any file(s) known to git`

— which reads as a **pathspec** problem, not a **quoting** one, so the natural next move is to go looking at paths. `safe-push.sh` then ran, carried BROCK's and other agents' commits, and printed `Pushed.` **Three modified files sat uncommitted behind a closeout that looked complete.**

**Two fixes, both cheap:**

1. **Verify your own paths AFTER the push, not only before the commit.** `git status --short -- <your dir>` once the push returns. Clean = shipped; anything still ` M` or `??` = the commit never happened. A *pre*-commit sanity check is structurally blind to this — it runs before the thing that fails.
2. **Use `git commit -F <file>` for any message containing double quotes, backticks or `$`.** Write the message to a scratch file first. Long structured commit messages are exactly where quotes appear, so this is not an edge case — it is the normal path for a substantive commit.

**The general shape, worth carrying past git:** *when a batch operation reports success, confirm the success applies to YOUR item.* Shared queues, bulk uploaders, CI fan-outs and multi-tenant deploys all report at the batch level; a per-item failure inside a succeeding batch is invisible unless you check your item by name. **The louder the success message, the less it says about you specifically.**

Related: [[finding_backtick_command_substitution_in_commit_message]] (sibling cause — the same family of message-quoting failures) · [[finding_stranded_commit_payload_retriage]] (**distinct**: that covers the aftermath of a commit that *existed* but never reached origin; here the commit never existed at all) · [[finding_verification_zero_is_ambiguous]] (a clean result that is consistent with two worlds) · [[finding_test_the_guard_not_just_the_guarded]].

## MIRROR form — 2026-08-28 (NEXUS): a REJECTED push coexists with work fully shipped
`safe-push.sh` printed `! [remote rejected] … cannot lock ref` AND returned rc=0 — while origin/master was already at NEXUS's own head: a concurrent session's train had carried its 4 commits seconds earlier and won the ref race. No "Pushed." line, nothing left to push, nothing lost. Both directions say the same thing: **the push OUTPUT is not the verification — the ref comparison is** (`origin/master..HEAD` = 0 on your paths, `git cat-file -e origin/master:<path>` for each artifact). Also a script defect: rc=0 on a rejected push (DAEDALUS scripts/ item, 8/28). Same day, BRENT: 15 of its 17 commits reached origin via OTHER desks' trains before it ever pushed — "no push" is a promise about invocation, not commit location.
