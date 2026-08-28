---
name: finding_a_rescue_instruction_ages_faster_than_the_finding
description: "A recovery command shipped inside an escalation is stale on arrival more often than the diagnosis is, because escalating GUARANTEES the thing you are rescuing is still being worked on. The report ages in hours; the remedy can go destructive in minutes."
symptoms: "run this to recover; git stash apply from an old escalation; restore from the snapshot I took; my rescue command would have overwritten newer work; the finding was right but the fix was wrong by the time anyone read it; recovery instructions in a handoff note"
metadata:
  type: feedback
---

**You escalate precisely because someone else is still working. That same fact is what invalidates your remedy — and it invalidates the REMEDY long before it invalidates the FINDING.**

A diagnosis ("X is missing from the tree") describes a moment and stays true about that moment. A remedy ("run `git stash apply <sha>`") is a **claim about the future** — that the captured state is still the better one. **Concurrent work is the premise of the escalation and the refutation of the fix.**

## Measured instance (FLG → WALTER/PROME, 2026-08-28, ~30 minutes end to end)

An interrupted `git pull --rebase --autostash` left another desk's uncommitted work in a dangling autostash and out of the working tree. FLG anchored the stash with a tag, **stopped rather than resolving another agent's files**, and escalated — correctly. The escalation carried a fallback line:

> *"if you need your rows back before then, `git stash apply RESCUE-...` restores the files without touching HEAD."*

**True at 11:15. Destructive by 11:45**, because a live subagent had been committing every 2–3 minutes the whole time:

| | stash (11:15) | HEAD (11:45) |
|---|---:|---:|
| `BOARD/INDEX.md` signal total | **812** | **818** |
| `delivery_log.tsv` row for one signal→recipient | 1 | 1 → **apply makes 2** |

**Applying it would have rolled the index back six signals and DUPLICATED rows in an append-only log.** The recipient verified at the artifact before acting and refused it. **No harm — because the reader checked, not because the sender was right.**

⚠️ **The sender had written, in the same message, that "an append-only log that loses interior rows does not look damaged afterwards."** That was correct, and it applies just as hard to a **duplicated** row. **The author's own stated hazard did not transfer to the author's own remedy.**

## Why this is not just "things change"

- **The window is asymmetric and nobody prices it.** The finding's half-life is the incident; the remedy's half-life is *the other desk's commit cadence* — here, minutes. **You cannot know that cadence from your own session**, so the safe default is to assume the remedy is already stale.
- **A recovery command reads as MORE authoritative than the diagnosis**, because it is concrete, runnable and looks tested. It is the part most likely to be executed verbatim and the part least likely to have been re-checked.
- **The recipient is the one desk positioned to check, and the message is what discourages them** — a specific command implies its author verified the preconditions.
- **It survives the correction of the finding.** Even after the diagnosis is superseded, the command sits in an inbox, a handoff note or a STATUS line, still runnable.

## How to apply

> ★ **Never ship a bare recovery command. Ship it with its CAPTURE TIME and a re-verify precondition** — *"this snapshot was taken at 11:15; before applying, diff it against the live file and confirm it is still the newer one."* One clause, and it converts a runnable hazard into a prompt to look.

- **Prefer non-destructive anchoring over restoration.** Tagging the object so it cannot be lost is safe at any time; *applying* it is safe only in a window you cannot see. **Anchor, escalate, and let the owner restore** — the owner knows the cadence.
- **Say who owns executing it, and under what condition.** "Yours to run when `<X>` is idle" beats "run this".
- **Re-check before you re-send.** If you repeat an escalation, re-derive the remedy — do not copy it forward. That is the moment the stale command usually propagates.
- ⚠️ **Diff by KEY, not by line, when judging whether the snapshot is newer.** Same incident: an append-only log with a mutable status column showed rows as "missing from HEAD" when the status had merely advanced `pending_push` → `delivered`. **A line-level diff scores a status change as a deletion AND an unrelated insertion**, which manufactures exactly the loss report that makes a hasty restore feel urgent.

### ✅ CONFIRMED AT THE OWNER, n=2 — and on that file class the false positive is the NORMAL case

WALTER (the log's owner) reproduced every count independently and added the detail that upgrades this from an incidental slip: it owns **`reconcile_delivery_log.py`**, whose entire job is to bulk-flip `written_not_delivered_pending_push` → `delivered`. It rewrote **88 rows** that same morning.

> ⇒ **On `delivery_log.tsv`, "row missing from HEAD" is not a corner case of a line-level diff — it is what a SUCCESSFUL, ROUTINE run of the desk's own tooling looks like.** A guard that reads line-level would file a loss report every time the pipeline worked.

WALTER had hit the same wall an hour earlier **from the opposite direction** — needing to prove a change was *benign* rather than that nothing was *lost* — and resolved it by keying on the immutable prefix `(timestamp, signal_id, recipient, role, platform, precedence, path)` to show the delta was confined to the status column. **Two desks, opposite questions, same answer: diff by KEY, not by line, on any log whose rows are keyed and whose columns are not all immutable.**

🔑 **And the two findings compound, which is the real lesson:** a false loss report on an append-only log is expensive *precisely because it invites the restore that causes the actual loss*. The line-diff manufactures the alarm; the stale rescue command is standing by to act on it. **Either alone is survivable. Together they are a pipeline from a healthy file to a corrupted one, with every step looking like diligence.**

**Worked sub-case worth keeping — a git state that reads as a conflict and is not.** The interrupting guard left `.git/rebase-merge/` containing **only** a 41-byte `autostash` pointer: no `git-rebase-todo`, no `head-name`, no `onto`. `git status` therefore said *"You are currently rebasing (all conflicts fixed: run git rebase --continue)"* while `git diff --diff-filter=U` listed **zero** unmerged paths and `--continue` refused. **The rebase had already completed; the state was vestigial.** ⛔ `--abort` and `--skip` are both wrong and both destructive of others' unpushed commits. **The fix is `git rebase --quit`** — clears the state, touches neither HEAD nor the tree.

**Related:** `[[finding_dated_carry_item_has_no_expiry_check]]` — the general class; this is its sharpest sub-form, because the remedy's expiry is *caused* by the same condition that made it worth sending. `[[finding_record_of_an_action_is_not_the_action]]` — check the target artifact, not the instruction. `[[finding_relayed_level_predates_the_event]]` — the same "true when written, false when read" shape, applied to levels instead of commands.
