---
name: finding_backtick_command_substitution_in_commit_message
description: "Backticked identifiers inside a double-quoted `git commit -m` message are command-substituted by the shell and silently deleted from the message — use single quotes, and never force-push to repair it"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 50ea2e02-b8c9-4172-80ec-6ccbade2129b
  modified: 2026-07-26T19:09:13.820Z
---

**A `git commit -m "...backtick-quoted `identifier`..."` runs the backticked word as a shell command.** The command fails, bash prints `command not found` to stderr, **the commit still succeeds**, and the word is **silently replaced by an empty string** in the stored message.

**The case (2026-07-26, TERRY).** A commit message referencing schema fields as `` `lane` `` and `` `antecedent` `` produced two `command not found` lines. The commit went through and the pushed message read *"every row records an  (copied from"* and *" splits paper-vs-real fills"* — both identifiers gone. **The files were entirely correct; only the message was damaged.** Easy to miss because the commit reports success and the stderr noise scrolls past above it.

**Why it bites this fleet specifically:** commit messages here routinely name files, columns, and script identifiers, and markdown habit puts those in backticks. Same hazard class as [[finding_printf_format_tsv_append_corruption]] — a shell metacharacter surviving into a quoted string.

**Disciplines:**
1. **Single-quote the message** (`-m '...'`), or drop the backticks and write the identifier bare. Bare is usually better in a commit message anyway.
2. **Watch for `command not found` in the commit output.** It is the only signal, and it appears *before* the success line.
3. **Do NOT repair it by amending a pushed commit.** `--amend` + push requires a force-push, which the repo protocol forbids outright. A cosmetically-damaged message with correct file content is not worth rewriting shared history — note it and move on.
4. Same applies to `$(...)`, `$VAR`, and `!` inside double-quoted messages.

## n=2 — RECURRED 2026-08-18 (TERRY, same desk, 23 days later), and the attempted REPAIR was far worse than the defect

Backticked identifiers in a `git commit -m "..."` again produced `command not found` and again silently deleted the phrase from the stored message. **Discipline #1 is knowledge this desk already had and did not apply under batch tempo** — the same *"the failure is tempo, not knowledge"* pattern [[finding_concurrent_commit_index_race]] records for its own variants. *(Third instance, same session: the inline `python3 -c "..."` written to document this very finding was itself backtick-substituted. The hazard is the DOUBLE-QUOTED shell string, not `git` — it applies to every command, and the fix is a quoted heredoc `<<'EOF'` or single quotes.)*

**⚠️ Discipline #3 needs widening, and this is the durable half.** It said: do not repair a **pushed** commit by amending. The repair attempt **rewrote a CONCURRENT AGENT'S commit**, because HEAD moved between the `git log -1` that read the message and the `--amend` two seconds later. 🔴 **And I initially recorded that commit as UNPUSHED — it was NOT. VIOLET had already pushed it (verified: `git merge-base --is-ancestor` ⇒ YES). I amended a PUBLIC commit.** So discipline #3's "pushed" caveat did not merely need widening — **it applied all along and I misread which case I was in.** On a shared repo where commit-and-push are fused in one call, **"unpushed" decays as fast as "mine," and you cannot tell either by looking at your own shell history.** Full incident, damage assessment and the `git reset --soft` repair → [[finding_concurrent_commit_index_race]] **n=5**.

**⇒ The rule is now simply: DO NOT AMEND to fix a cosmetic message defect, pushed or not.** Get the message right the first time (single-quote it, or write identifiers bare); if it lands damaged and the FILES are correct, note it and move on. The message is documentation; the tree is the work.

Sits with [[feedback_check_staged_before_commit]] and [[finding_pathspec_rename_needs_both_paths]] — the class of git mistakes that report success while quietly doing the wrong thing.

## n=3 — RECURRED 2026-08-21 (MARCO, a DIFFERENT desk, 3 days after n=2), compound-identical

**Both halves repeated exactly.** A `git commit -m "..."` message containing `` `total` `` was command-substituted, printing `total: command not found` and storing *"KB reproduces to the cent on ."* Then the repair attempt — `git commit --amend -F msgfile --only -- <my path>` — **rewrote a CONCURRENT AGENT'S commit**, because DAEDALUS committed in the ~90 seconds between my commit and my amend. HEAD was no longer mine, and `--amend` does not ask.

⚠️ **This memory already said, in bold, exactly what not to do.** It was not consulted, because it sits in the COLD index and nothing in the commit path greps it. **The knowledge existed in the fleet, in a file written for this, and the failure happened anyway — for the third time, at the third desk.** That is now the load-bearing fact about this finding: *documenting it has twice failed to stop it.*

**What was different, and it is the useful part — the REPAIR.**
- n=2 hit a **pushed** commit and repaired with `git reset --soft`, which cannot restore the original hash.
- n=3 hit an **unpushed** commit whose **tree was byte-identical** to the original (`git diff <orig> <rewrite> --stat` ⇒ empty; only the message differed, and `--only` had narrowed nothing because my path had no pending change). With an identical tree, a clean global `git status`, and nothing built on top, **`git reset --hard <original-hash>` restores the ORIGINAL COMMIT OBJECT — same hash, same message, same author date.** Any reference the other agent recorded still resolves. **That is strictly better than `--soft` and is the repair to reach for when those three preconditions hold.**
- **Verify the preconditions in this order, before touching anything:** ① `git diff <orig> <rewrite> --stat` is EMPTY (no work dropped — `--amend` with a pathspec CAN drop files from someone else's commit), ② `git status --porcelain` is globally empty (`reset --hard` discards uncommitted work belonging to every agent, not just you), ③ nothing is committed on top. If ① fails you are repairing lost work, not a message.

**⇒ Hardened rule, and it is now mechanical rather than advisory: `--amend` is a HEAD-relative operation on a branch where HEAD is not yours to assume.** Between reading a hash and amending it, any of ~30 sessions may commit. **Do not amend on this repo. At all. For any reason.** A damaged message with a correct tree is documentation debt; an amend is a history rewrite of whoever happens to hold HEAD.

**And the prevention, since the message-side rule keeps not working:** write commit messages through a **quoted heredoc to a file** (`cat > msg.txt <<'EOF'` … `git commit -F msg.txt`). A quoted heredoc disables ALL shell expansion — backticks, `$(...)`, `$VAR`, `!` — so the class cannot occur, and no discipline has to be remembered under tempo. n=3 used a heredoc for the *repair* message and it was the only part that worked correctly.
