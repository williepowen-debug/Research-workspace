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
