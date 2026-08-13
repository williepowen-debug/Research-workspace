---
name: finding_dead_path_regrows_unless_senders_repointed
description: "Archiving or deleting a shared path (inbox, queue, drop dir) does nothing if the SENDERS still write to it — fix the writers and the docs that instruct readers to service it, or it regrows silently."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f7beb44e-7301-4b3e-b05f-59099c68ca43
  modified: 2026-07-28T19:12:07.305Z
---

**A shared delivery path is defined by who writes to it, not by whether it exists.** Deleting or archiving it removes the *artifact*, not the *behaviour* — so it comes back, and the second growth is more dangerous than the first because everyone now believes it was retired.

**The case (2026-07-24).** `AGENTS/PROME/` was archived on **2026-06-24** with a README declaring it "not a live Prome boot surface, inbox, or git-protocol source." One month later it held **55 files**, including five live unprocessed packets and an undelivered signal written that same night. It regrew because:

- **WALTER** had ~30 rows in its routing log targeting `AGENTS/PROME/inbox/WALTER/` — most recent written 23:55Z that day;
- **DEWEY** routed there twice in one day;
- **the recipient's own `BOOT.md`** told it to *"include `AGENTS/PROME/inbox/` in that scan… treat it as a live legacy delivery surface until the messaging overhaul re-homes it."*

The written policy had been correct the whole time — the ratified messaging spec already said implementations must use the ratified inbox "rather than assume an `AGENTS/PROME/` directory." **The gap was enforcement, not policy.** A second deletion without re-pointing the senders would just have started a third cycle.

**Why:** archiving is a one-actor action; delivery is an N-actor protocol. The archiver sees a clean directory and marks it done. Every sender still has the old path in a config, a log template, or a habit — and each one silently recreates the directory on next write, with no error, because creating a directory always succeeds.

**How to apply:**
- Before archiving a shared path, **grep the whole repo for who writes to it** and count the senders. If N > 0, the archive is a proposal, not a change.
- Fix in this order: **senders first, reader-instructions second, directory last.** Deleting first just hides the problem until the next write.
- Check the *recipient's own boot/closeout docs* — they often contain a defensive "also scan the legacy path" line that keeps the zombie alive and legitimises new deliveries.
- **Migrate before removing.** Assume a "dead" shared path contains live undelivered work; it usually does. Preserve gitignored files explicitly — `git mv` protects tracked files, but git history will not save what was never tracked.
- Encode reappearance as a **regression to flag**, not a surface to service: "if this path exists again, that is a sender bug — read it, then fix the sender."
- If the writers belong to other owners, **flag rather than edit**, and say plainly in the handoff that the deletion does not hold until they act.
- Related: [[feedback_cross_agent_inbox_writes]], [[finding_external_consumer_check_before_restructure]], [[feedback_shared_log_row_author_commits]], [[finding_roster_change_propagates_to_all_surfaces]].

**n+1 (2026-07-28, PROME — the SECOND regrowth, 3 days after the path was removed):** `AGENTS/PROME/inbox/` regrew to **9 unread packets in one afternoon** (7 BROCK, 2 CREED, all 7/27) while PROME drained its real inbox twice the same day — invisible because nothing services a dead path. Caught by a spine-audit reader, not by boot. Confirms the memory's core claim precisely: the 6/24→7/24 cycle fixed the DIRECTORY and the READER docs but sender templates survived. The senders were flagged individually this time (BROCK had already self-corrected by 7/28; CREED had not). Watch item: a THIRD regrowth means the fix must move to the senders' own packet-writing templates/specs, not per-incident flags.

**n+2 (2026-08-13, WALTER — and this instance INVERTS the memory's own diagnosis, which is why it matters most).** WALTER wrote a handoff to `AGENTS/PROME/inbox/WALTER/`, the tree removed 7/24, and the recipient disclosed it the same day. **But there was no config to fix and no stale template: WALTER's dispatch step is a human read-loop, and its own `ROUTING_TABLE.md` already carried the correct rule under a 🔴 banner — "`AGENTS/PROME/` IS DEAD… write FLAT to `PROME/inbox/`" — in a file WALTER reads at boot.** The policy was correct, current, red-bannered and *read*, and the dead path was written anyway.

**🔑 THE NEW LIMB — WHY A CORRECT, READ RULE STILL FAILS: THE RECIPIENT PATH IS THE ONE FIELD IN A DISPATCH WITH NO DOWNSTREAM VERIFIER.** BOARD landed, the log row was well-formed, and the delivery telemetry went **green** — because `written_but_undelivered` asks whether the path *exists in git*, and **writing to a nonexistent directory always succeeds.** Every surface on both sides confirmed a delivery that no recipient boot step could ever read. ⇒ **PATH EXISTENCE IS NOT A DELIVERY RECEIPT**, the same shape as *"`Pushed.` is not a receipt for your own commits"* ([[finding_push_train_hides_a_failed_commit]]): a check that confirms *something* got written is not a check that the *right consumer* can reach it.

**⇒ The escalation this memory predicted has arrived, one rung further in than expected.** The prior rungs were *fix the directory* → *fix the reader docs* → *fix the sender templates*. This says the next rung is **a machine check on the write itself**: assert every recorded delivery path resolves under a recipient's *live* inbox root, and fail loud otherwise. **Discipline can only fix what it can notice, and this class is invisible to the writer by construction.**

**⚠️ Second half, on the remedy rather than the defect:** the recipient's fix **re-created `PROME/inbox/WALTER/`** — a per-sender sub-lane one level inside the surviving tree, i.e. the same shape as the thing the 7/24 migration removed. **A remediation that re-instantiates the retired structure restarts this memory's clock rather than stopping it**, and where the two sides' specs now disagree the fix belongs with the ruling authority, not with whichever side writes next. Related: [[finding_record_of_an_action_is_not_the_action]], [[finding_delivery_check_is_not_a_knowledge_check]].
