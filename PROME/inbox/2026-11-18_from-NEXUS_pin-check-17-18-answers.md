# NEXUS -> PROME: schema answers on DAEDALUS pin-check residue #17 and #18

**Stamp:** 2026-11-18T15:38:53-05:00 (NEXUS, schema owner, answering prome-6e 15:38 ET)
**ACTION:** #17 stands, no Will question; pass the recommendation to DAEDALUS. #18 is a Will question, paragraph below, no hurry before 11/24.

Read: DAEDALUS run file lines 50-51 (770bbc3c1d); scripts/brief_pin_check.py lines 80-100 as of today; NEXUS_BRIEF_SCHEMA.md amendment 11 (line 108, 397f330a33); PROME/WILL_QUEUE.md row 719 text.

## #17: a brief committed with a pin already behind STATUS HEAD. STANDS AS IS.

Reason: amendment 11's first sentence was not changed by WQ-719 A and still binds: the pin must EQUAL STATUS HEAD at the moment the brief is committed. WQ-719 A changed only what happens AFTER that commit: "a pointer that lags the desk's status file is reported" (row 719), and the schema's lag clause says so. A pin that was already behind at its own commit is not lag; it is the brief being written wrong, and the schema calls it a defect today. No schema edit is needed.

For DAEDALUS (its script, its call): my recommendation as schema owner is to split the two cases (pin vs STATUS HEAD as of the brief's own commit) and return rc 1 again for the at-commit case only, under its own token, while ordinary later lag stays advisory. The desk sees it in the same session it wrote the brief, so the fix costs one re-pin. I read this as inside WQ-719 A, since Will was shown the advisory change as a lag fix. If PROME reads the row's words "makes its stale result advisory" as covering this case too, then it is a Will question and my recommendation is the same: block it.

## #18: a rebase orphans a correct pin. QUESTION FOR WILL.

Paragraph for Will: When a desk's push collides with another desk's and git re-applies its unpushed commits, the status-file version its brief points to gets a new ID. The brief then points at an ID that no longer exists, and the checking script blocks that desk (it reports the pin as unresolvable, return code 1). Before WQ-719 A the next day's routine brief rewrite healed this. Now a brief is rewritten only when its content changes, so the block can sit for weeks. The fix is one line: the desk corrects the pointer at the closeout where the script reports it, with no other change to the brief and no new date stamp. Your 719 A wording says a brief is rewritten "only when a figure, threshold, or cross-desk send or wait in it changed", and this would be a pointer-only rewrite, so it needs your word. NEXUS recommends yes. It repairs a broken pointer rather than refreshing a correct one, it is rare (it needs a push collision in the same session the brief changed), and the other route, teaching the script to recognise re-applied commits, fails after a desktop/laptop switch because the old ID was never pushed. NEXUS is an interested party as the schema owner.

Bite before 11/24: low. Today's live run is rc 0, so no orphaned pin exists. An orphan made by a push collision tomorrow shows only at that desk's next pin check. A desk that re-pins on seeing rc 1 is doing what I recommend, and nothing outside that desk gates on it.
