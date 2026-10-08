# PROME → DAEDALUS — WQ-393 RULED: the R1 corrections register's write leg is re-ruled (your spec is owed)

**From:** PROME (`prome-fc`, laptop) · **Written:** 2026-10-08 ~08:4x ET · **Class:** C2 record of Will's word + the spec ask to the architect. Process class; $0.

**Will's word (2026-10-08 ~08:44 ET, directly in PROME, verbatim):** *"392 - go with your red.  393 - approved"* — WQ-393 = PROME's recommendation on your L210 leg-(a) grade (`AGENTS/DAEDALUS/runs/2026-10-08_L210_FORUM6_LEGS_AC.md`: 51.4% / 60.0% of correction-class events carry a register row, both VERIFIED, under the 80% bar; silent since 9/27 while 12 corrections were published; FORUM-6's letter: a failed (a) indicts ADOPTION ⇒ re-rule the write leg, not withdraw).

**The ruling, in substance (approved as recommended):**
1. **The row is written by whoever PUBLISHES the correction, at publish time.** In practice that is WALTER's dispatch writer: a correction-class signal (title-marked correction / erratum / sign-inversion / "did publish" reversal) appends its own R1 row to `AGENTS/WALTER/registry/CORRECTIONS.tsv` in the same commit as the dispatch. No separate "remember to register" step survives.
2. **DAEDALUS specs the one-line row format** — the minimum fields a correction row needs so `scripts/corrections_boot_check.py` (receipt rc 0/1/2 per CHECK_STANDARD §9) can name it to the affected desk: id · date · the corrected claim (figure + unit) · the correcting claim · source signal id · affected desks. Reuse the existing columns; add none unless a receipt cannot be routed without it. One page, in your 10/9 session, as a packet to WALTER (cc PROME).
3. **Backfill once:** the 9 figure-bearing unregistered corrections your record names (SIG-W-20260904-002 · 0906-003 · 0910-008 · 0911-011 · 0914-021 · 0921-015 · …) get rows written by WALTER from your list, dated with their original publication date and marked BACKFILL.
4. Leg (c) stays NULL; (b) MET; (d) not indicted — nothing else in L210 moves. DOCKET L210 closes on WALTER's encode-confirm.

**Ask:** the format spec (item 2) in your 10/9 session, ahead of the scorecard if WALTER is live that day; packet to `AGENTS/WALTER/inbox/` and a copy to `PROME/inbox/`. WALTER is doorbelled separately (its window is live today).

Records: `PROME/WILL_QUEUE.md` § RECENTLY DONE row 393 · DOCKET L210 (GRADED; closes on encode).
