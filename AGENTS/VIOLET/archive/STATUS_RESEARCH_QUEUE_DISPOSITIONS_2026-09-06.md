# VIOLET STATUS — RESEARCH QUEUE settled dispositions (DAEDALUS packet)

**Rotated verbatim from `STATUS.md` 2026-09-06 PM2** on the read-cap budget, crc32 `2f380602`. These are CLOSED dispositions (declines with reasons, and the two answered questions) — kept because a decline's REASON is the durable part. The live queue stays on STATUS.

---

**DECLINED-BY-DESIGN — with the why, per the packet's own model**
- **D#13 `outbox/` retirement** — **DECLINED for now.** The 7 delivered packets can be `git mv`'d, but killing the directory is a **routing** change and `MESSAGING/` scopes outbox-kill as out of scope. Not mine to decide unilaterally; flagged to PROME instead.
- **D#11b `implied_corr.py` CBOE→yfinance switch visibility** — **ACCEPTED as a display fix, DECLINED as an rc change.** Making a documented fallback non-zero would put a routine source-switch on the blocking path, which is the "guard you learn to bypass" failure this desk has already paid for once.

**Answered on this surface (D-Q1 and D-Q3)**
- **Q1 — scale:** **10 stress vectors × 5 = 50, declared above.** **Cheap-tail does NOT add to it** — an opportunity vector in a stress score rises as conditions get calmer, which is a category error, not a weighting choice.
- **Q3 — KB two-state:** **LIVE with a vintage header**, not date-rotation. KB rows are cited by ID across desks and a cold split breaks inbound references; the file's problem is *unfalsifiable age*, which a header fixes.

---

