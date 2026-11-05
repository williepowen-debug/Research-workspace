# Bounded repair: gate069 L4 exact-decimal boundary

Authority: Will's November4 substantive follow-through explicitly includes investigating and correcting this reported defect under existing bounded-repair authority. No threshold, operator, instrument, session calendar, missing-input rule or consequence changes. Existing inclusive equity return <= -15% AND first-published HY change >=5bp remain binding.

reads: 2 (DAEDALUS read 1 WITHHELD 2026-11-04; read 2 RELEASE 2026-11-05 at 303bae4a7, with WQ-603 reading A)
Independent result review remains required before operational release or claiming fixed. Author tests establish IMPLEMENTED / TESTED only. No independent reader has been commissioned in this session.

Acceptance conditions, written before code edit:
1. Interpret supplied raw closes as their decimal representations, with exact comparison of price ratio to the existing inclusive -15% line. The displayed floating return cannot control the grade.
2. 2.40→2.04 with HY+5 must meet; 2.40→2.03 meets and 2.40→2.05 does not. 2.40→2.04 with HY+4 does not. Values infinitesimally above the boundary must not meet (no tolerance widening).
3. ANY ONE of the four existing names can meet. Existing missing HY/equity, date matching, holidays, first-published basis and all L1 behavior remain unchanged.
4. Reconcile old and corrected arithmetic on retrieved raw closes from the letter's September1 adoption through the latest published credit observation. Report changed actual-session results separately from synthetic failures. Later vendor history is not a complete immutable census of previously seen quotes.
5. Keep dependent L4 operational use withheld until consequential-repair independent verification. Unaffected L1/072/HY/funding work proceeds. No frozen row edits.

Neighbour categories: ordinary = reproduction plus immediately lower/higher close and HY+4/+5. Overlap = exactly-equity boundary coincides with exactly-credit boundary and a different qualifying cohort name. Wrong owner = do not add new cohort names or substitute adjusted closes. Missing information = existing missing-bar/HY tests must still fail closed. Concurrent activity = N/A to pure arithmetic comparison (no persistent writes or shared input mutation in function).

Before the operational-withholding edit: the normal CLI must refuse with a nonzero status while independent release is pending. Offline selftests and pure-function author evaluation remain available. This is temporary withdrawal under WQ-229, not a changed gate rule. Removal of the release hold requires the independent result receipt for this exact candidate.

**Hold removed 2026-11-05 after WQ-603 RULED A** (Will in LIQUID's window 10:32 ET, verbatim "603 A"; order confirmed by PROME; DAEDALUS read 2 RELEASE at 303bae4a7). Only the five-line hold block was deleted, and the read path is unchanged. Added after that read: six `main()` cases with stubbed vendor and FRED, and the 128.40→109.14 stored tie. **Those additions are TESTED, not INDEPENDENTLY VERIFIED.** All three mutants fail: literal old line at the call site, 5dp, 2dp.
