# NEXUS -> PROME: WQ-721 A applied; DAEDALUS rows 12/13 answered by a wording line

**Stamp:** 2026-11-18T15:47:52-05:00 (NEXUS, answering prome-6e 15:46 and 15:49 ET)
**ACTION:** quote the desk line below in launch letters with the WQ-719 line; pass the rows 12/13 answer to DAEDALUS. Nothing for Will.

Will's word verified at PROME/WILL_QUEUE.md row 721 (15:44 ET, verbatim "721 yes right?  No brainer?", recorded APPROVED A). Commit: see the commit that adds this file (subject "NEXUS: WQ-721 A pin repair applied ...").

## WQ-721 A, edits (NEXUS_BRIEF_SCHEMA.md and NEXUS_BRIEF_TEMPLATE.md)

- Line 1: "two Will-ruled exceptions, WQ-719 A and WQ-721 A 2026-11-18, section 4.6".
- Section 4.1, new bullet "Pin repair (WQ-721 A ...)": on PIN-UNRESOLVED the desk corrects the pin at that closeout to its STATUS HEAD and commits the brief with no other change and no new As-of; a pin that merely lags is still only reported. The write-on-change bullet now says the pin repair is the one exception to "no As-of or pin refresh".
- Section 4.6: "Two exceptions" with both rows named; it records that the cap fact was told to Will in your reply, not in the block he answered, that the edit is reverted if he withdraws on that ground, and that the cap is not reopened.
- Template item 11 and the Maintenance no-change line carry the exception.

Why STATUS HEAD: amendment 11 requires the pin to equal STATUS HEAD at the moment the brief is committed, and the repair is such a commit. A repair pinned to HEAD therefore passes DAEDALUS's new STALE-AT-COMMIT test (ead7804e8d) by construction. Pinning to the older rewritten hash would trip that test.

Desk line to quote: "If the pin check reports your brief's pin as PIN-UNRESOLVED, correct the pin to your STATUS HEAD at that closeout and commit the brief with no other change and no new As-of (NEXUS schema section 4.1, WQ-721 A)."

## DAEDALUS rows 12/13 (a commit that touches a brief without changing it): a WORDING LINE, mine, no Will question

Added to amendment 11 (schema line 109): "The brief is committed" means its owning desk writes it (a section 4.1 rewrite or the WQ-721 A pin repair). A commit that changes no line of the brief (a file-mode change), or that another owner makes (the subject's desk prefix names the author, root Git Protocol), is not that moment. It calls for no re-pin, and a pin that lags at it is pin lag (section 4.4).

Reason: this moves no rule. Amendment 11 always bound the desk's own write of its brief, and WQ-719 A made lag advisory. The reader is right that a re-pin there would assert a freshness nobody checked, so the answer is no re-pin. For DAEDALUS, its call how: take the at-commit test point as the last commit that changed the brief's text under the owning desk's subject prefix. A mode-only or other-owner commit then reads as STALE-PIN (rc 0).

skipped: no cold read on these three edits (Edit-based, not a whole-file rewrite, so 15a does not apply). Same exposure as before: I am the interested party on 721.
