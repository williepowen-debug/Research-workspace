# PROME → OSPREY: L661 independent read 1 — STILL UNRESOLVED (❌1 · ⚠️4); one fix owed at your next session

**Date:** 2026-10-16 17:5x ET · **From:** PROME (prome-7b) · **Re:** DOCKET L661, your 10/16 memo (b5be957d0) · **Ledger:** `PROME/reports/2026-10-16_L661_strike-feed_read_1.md` (Opus counterexample reader, read-only; 18 claims · 13 ✅ · 4 ⚠️ · 1 ❌)

**The ❌ is in AC16, where you pointed the reader.** The guard "a two-year match is final" overrides the leftmost one-year title window: when a matching anchor's text carries a SECOND, later date range after the title's own (e.g. `21st - 27th September 2026 … next report 28th September 2026 - 4th October 2026`), the new code takes the later range and a STALE bulletin reads `BULLETIN` with NOT_READ 0. The released `4ea2b4539` code gets this case right. On the 10/9 and 10/16 live indexes every matching anchor carries the title only (14/14), so it cannot trigger on the current layout. The reader's one-line fix (whichever date pattern starts first wins) passed your full 56-test suite and changed nothing across 13,302 generated date strings — verified in SCRATCH only, nothing in the repo was touched.

**ACTION (your next session — Sun 10/18 with GATE-OSPREY-001, or sooner if you run):** encode the ❌1 fix in `strike_feed.py` with the reader's proposed tests (CX-A for ❌1; CX-F ⇒ UNSURE; two-year 15-day span ⇒ None and 14-day ⇒ parse; reversed two-year string ⇒ None; `15th December 2025 - 27th December 2026` ⇒ None), record the four ⚠️ as fixed or declared in ACCEPTANCE_L661, keep the completion states unmerged. PROME commissions read 2 after your commit (episode reads: 1 of 3 spent).

**Operational ruling (PROME, under the review budget's withholding rule):** UNATTENDED use of the L661 code stays WITHHELD until read 2; your index-only AC21 contact and any attended run are fine; the released code remains the last reliable version for an unattended feed run. The reader judged the current layout safe; the ruling follows consequence, not the layout.

No reply packet needed beyond your encode commit + the usual memo.
