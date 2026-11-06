---
name: feedback_fresh_slate_is_files_then_clear_then_boot
description: Will's desk reset is close out to files, clear, reboot from files; his reason is working room and quality, not a measured capacity limit
metadata:
  type: feedback
symptoms: "do the agents need a reboot", "context spent", "fresh slate", "start from a fresh slate"
---

Will's reset (2026-11-06 18:18 ET, verbatim): "I wanted to make sure their context windows werent overloaded.  Even with the compactions.  They update their files and then the blank slate refresh reads the new files and catch up on context while hopefully having some more fresh context to work with".

**Why:** the desk's files are the truth, so a boot from files beats a window running on compaction summaries. PROME's capacity measurement did not answer his question: idle windows compact about 52 minutes after their last turn, so token counts alone say little about how good a window's memory is.

**How to apply:** when he asks whether a desk needs a reboot, report compaction count and what the summary lost as well as tokens. Sequence is closeout, Will clears, PROME sends a bounded boot message. Never call the reset unnecessary on token counts alone.
