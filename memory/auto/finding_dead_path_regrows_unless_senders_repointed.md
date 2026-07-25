---
name: finding_dead_path_regrows_unless_senders_repointed
description: "Archiving or deleting a shared path (inbox, queue, drop dir) does nothing if the SENDERS still write to it — fix the writers and the docs that instruct readers to service it, or it regrows silently."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f7beb44e-7301-4b3e-b05f-59099c68ca43
  modified: 2026-07-25T00:54:42.737Z
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
