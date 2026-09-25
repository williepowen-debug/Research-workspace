---
name: finding_a_stamp_written_from_narrative_drifts_from_the_wall_clock
description: A time stamp typed from the session's sense of elapsed time drifts from the wall clock by 15–40 minutes; three desks did it in one day. Take the clock in the same command that writes the stamp.
metadata:
  type: feedback
symptoms: "stamp says 22:0x but date says 21:39" · "~17:0x ET is WRONG by ~15 min (written from an estimate, not date)" · "its ~17:3x stamp was written ahead of the clock" · a masked-minute stamp that is later than the file's mtime · a packet stamped after the commit that carries it
---

**Fact.** On 2026-09-24 three desks stamped artifacts from the narrative clock instead of the wall clock: PROME wrote 22:xx across seven files while `date` read 21:39 (a 40-minute drift over a 40-minute session — the estimate ran at ~2× real time); HENRY's F1-basis packet to TERRY was stamped ~17:0x and was wrong by ~15 minutes (HENRY found it by re-running `date`); SAM's first STATUS pass said ~17:3x and was committed at 16:57. n=3 desks, one day; PROME's own SCRATCH already carried the caution *"take the clock (`NOW:` or `date`) IN THE SAME COMMAND that writes any stamp"* and it did not hold across a long tool-heavy stretch with no user prompt (the `NOW:` hook line arrives only on a user prompt; teammate messages and tool results carry none).

**Why:** a stamp typed from memory of "when I started" plus a felt duration is a claim about the world with no instrument behind it, and the error compounds silently: every later stamp inherits the earlier drift. A wrong stamp is not cosmetic — it re-orders events in the record (a packet stamped after the commit that carries it; a "later leg" that reads as earlier than a peer's delivery) and a reader cannot tell it from a right one.

**How to apply:** never type a clock. In a Bash edit, compute the stamp from `datetime.now()` (or `date`) INSIDE the same command that writes it, and mask minutes to `HH:Mx` only from that value. When a stretch runs on tool results and teammate messages alone (no `NOW:` line), run `date` before the first stamp of every write pass. If a stamp is found wrong before commit, fix it in place and say so in the file; after commit, correct in place with a note — never amend.

Related: [[finding_a_correction_pass_is_unreviewed_work]] (the fix pass is where the second wrong stamp lands) · [[finding_record_of_an_action_is_not_the_action]].
