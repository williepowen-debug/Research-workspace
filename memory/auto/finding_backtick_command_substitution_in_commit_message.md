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

Sits with [[feedback_check_staged_before_commit]] and [[finding_pathspec_rename_needs_both_paths]] — the class of git mistakes that report success while quietly doing the wrong thing.
