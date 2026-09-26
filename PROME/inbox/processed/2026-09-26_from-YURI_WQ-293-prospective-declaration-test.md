# YURI → PROME · 2026-09-26 15:2x ET · WQ-293: prospective public-declaration test (YUR-004) — PROPOSED, ready for Will's word

**Full text:** `AGENTS/YURI/research/2026-09-26_WQ-293_YUR-004_declaration-test-PROPOSED.md` §1. It is written as one letter for Will to approve word for word (commit `5bf10bb90`). It is **not registered**: the id `YUR-004` is reserved, and `INTENT_LEDGER.tsv` is untouched.

**The letter in eight lines:**
1. **Question.** Does the Russian state PUBLICLY DECLARE a mobilisation, with an act dated 2026-09-26 to 2026-10-31? A MISS means "no public declaration at the declaration sources". It never means "no decision occurred".
2. **Instrument.** A presidential decree or an equivalent named legal act (a presidential order or a federal law) whose **title** declares or orders mobilisation. The model is Указ № 647 of 21.09.2022.
3. **Declaration sources.** (a) the pravo presidential block, read in number order; (b) kremlin.ru, the presidential news feed with /acts/news as a variant. Both are read over plain http.
4. **Window baseline.** № 680 (25.09), read live at 19:09Z today with 0 mobilisation titles. Any act above № 680 is inside the window.
5. **Checkpoints.** 9/30 (the new Duma sits) · Friday reads on 10/02 (shared with YUR-003), 10/09, 10/16, 10/23 and 10/30 · final grade 10/31 (L432 end), with coverage re-reads through 11/02.
6. **CONFIRM ⇒ HIT.** A qualifying act dated in the window, found at (a) or (b).
7. **MISS.** Needs continuous number coverage of (a), date coverage of (b) across the window, and zero qualifying titles. If a source still has uncovered dates on 11/02, the row resolves **STUCK**. It never resolves MISS on one source, and it never stays OPEN forever.
8. **Guards on every read.** Each grade line carries *"mil.ru unread (… HTTP 000) · restricted gap numbers unread · no OCR · implementation leg DECLARED GAP"*. The autumn-conscription decree, preparation or reservist-training titles, martial law and № 419 are kill-on-sight: they never confirm.

**Earlier grade preserved, not re-graded.** YUR-001 stands as **"NOT-DECIDED · PERIMETER PARTIAL (window 09-19→09-25)"**. It records only that no instrument appeared at the reachable primaries. It is not certainty that no mobilisation decision occurred in that window, because mil.ru, five unpublished numbers and the scanned bodies went unread. YUR-004's window starts above № 680, so it never re-reads YUR-001's dates.

**One thing PROME should know before presenting.** kremlin.ru returned **000 on six host/scheme variants today** (19:1xZ), after returning 200 on 9/25. Source (b) is intermittent, and that is why clause 7 (STUCK, not OPEN-forever) exists. rg.ru is named as an unchecked candidate substitute and is not proposed.

**Also drained:** the WQ-295 packet. Cadence is declared **WEEKLY** and 7 WATCH_FOR candidates were sent in `PROME/inbox/2026-09-26_from-YURI_cadence-and-watch-terms.md`. The packet assumed a list existed, and none did.

$0 · no trade · no threshold · convergence Score unchanged (2).

## COMPLETION — YURI — 2026-09-26
STATUS: ✅ DONE
CHANGED: AGENTS/YURI/research/2026-09-26_WQ-293_YUR-004_declaration-test-PROPOSED.md, AGENTS/YURI/STATUS.md, AGENTS/YURI/board_log.tsv, AGENTS/YURI/inbox/processed/2026-09-25_from-PROME_…WQ-295.md (moved), PROME/inbox/2026-09-26_from-YURI_cadence-and-watch-terms.md, this memo
RESULT: YUR-004 prospective declaration test written as a 10-clause approvable letter (window: acts above № 680, 9/26→10/31; 7 read dates; CONFIRM/MISS/STUCK defined; mil.ru named on every grade line); YUR-001 preserved verbatim with a does-not-establish sentence; inbox 1/1 drained (cadence WEEKLY, 7 watch phrases).
GAPS: kremlin.ru 000 on 6 variants today (was 200 on 9/25), so the test has only one live source today; clause 7 handles this. mil.ru unreachable (implementation leg, declared). No OCR, so title-level reads only.
WILL_NEEDS: WQ-293: approve the §1 letter word for word, or amend it; also the YUR-001 disposition (VOID-superseded with the reading preserved, or leave OPEN).
FOLLOW-UP: On approval, YURI registers YUR-004 in INTENT_LEDGER and PROME re-points DOCKET L432 to it. First read 9/30. WALTER live-tests the 7 phrases.
