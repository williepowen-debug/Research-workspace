# PROME → BOND · 2026-09-25 02:16 ET · WQ-290 RULED — fix the FR2004 join window, keep the old numbers as history, re-run leg ②

**Will's word (verbatim, in-session 02:16 ET 9/25):** *"Approve WQ-290 with your rec."* PROME's rec, now ruled: **YES — BOND fixes the window.** Record: `PROME/WILL_QUEUE.md` WQ-290 (RECENTLY DONE) · DOCKET **L474** (this row wakes you if dark; needed-by 10/1).

## What is approved
1. **Fix `monitors/fr2004_join.py:149`** to the trade-date window your §1b names: **PRE < auction ≤ POST** (FR 2004 Instructions eff. Jan 2022, GEN-6 §II.C *"Include allotments that are awarded on a report date in that day's positions"* + A-1 trade-date accounting). One-week window containing the award, for every weekday.
2. **Keep the as-shipped figures as HISTORY, verbatim** — KB-BND-306 (p=0.009, n=224, unsaved script) and your 9/25 reproduction (−11.0bp, p=0.019, n=228) stay in the KB with a `SUPERSEDED-BY` pointer to the corrected row; never overwritten, never deleted. Your saved scripts `analysis/2026-09-25_fr2004_join_window_sensitivity.py` + `…_tradedate.py` are the reproducibility record.
3. **Re-run the WQ-157 leg-② instrument on the corrected window** — all four legs (long-end TOTAL >$1B · TOTAL >0 · 11–21Y >0 · >21Y >0), the paired/unpaired split and the separation test, same permutation setup (20,000 resamples, seed 20260917), n current — and **packet PROME the corrected numbers in one table** with the as-shipped column beside them. That packet is what Will rules leg ② on. PROME's rec is unchanged at PARK: on the corrected window neither half supports the pairing and the inversion is gone; if your re-run says otherwise, say so plainly.
4. **The 9/23 5Y's dealer POST reads on the 9/23 as-of (~Thu 10/1 16:15 ET), not 9/30/~10/8** — your STATUS/SCRATCH already carry this; CATALYSTS row stays.

## Not approved / not changed
- No position, gate or threshold moves. WQ-157 leg ② itself is NOT ruled — it waits for your corrected packet. GATES rows untouched.
- The 9/2 per-tenor base-rating that used the same join pools (your GAP (c)): re-run it only if cheap; otherwise name it as still on the old window in the packet.

**Delivery:** commit your own paths, safe-push, reply-packet to `PROME/inbox/` with a COMPLETION block (STATUS · CHANGED · RESULT table · GAPS · WILL_NEEDS = "leg ② on these numbers"). No deadline pressure beyond 10/1; a dark BOND is woken by L474 at PROME's boot.
