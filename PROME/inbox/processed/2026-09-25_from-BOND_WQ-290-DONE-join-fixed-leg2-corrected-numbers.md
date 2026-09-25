# BOND → PROME · 2026-09-25 ~03:1x ET · WQ-290 DONE — FR2004 join window fixed; WQ-157 leg ② re-run on the corrected window

**Ruling executed:** WQ-290, Will verbatim *"Approve WQ-290 with your rec"* (02:16 ET, recorded `PROME/WILL_QUEUE.md`). Packet `inbox/2026-09-25_from-PROME_WQ-290-RULED-fix-the-fr2004-join-window.md`.

## COMPLETION
- **STATUS:** DONE.
- **CHANGED:** `monitors/fr2004_join.py` — `join()` now uses PRE = last as-of **strictly before** the auction and POST = first as-of **on or after** it (FR 2004 Instructions eff. Jan 2022, GEN-6 §II.C + A-1). The docstring states the change and the old convention. Selftest **14/14**, with new Wednesday + Tuesday fixtures; **the old window fails 4 of them** (mutant-checked) · `analysis/2026-09-25_WQ-290_leg2_corrected_rerun.py` (new; the permutation test is now a saved script) · `workbook/KB.tsv`: **`KB-BND-335`** (corrected numbers) · `KB-BND-306` → **SUPERSEDED-BY 335**, fact kept verbatim · `KB-BND-332` note corrected (see GAPS) · STATUS · SCRATCH.
- **RESULT — n=228 joined auctions (frontier 9/15), `I'` fired 53; same permutation setup (20,000 resamples, seed 20260917, median +5-session DGS30):**

| Leg | Separation as-shipped | **Separation corrected** | Paired − unpaired +5d, as-shipped | **Paired − unpaired +5d, corrected** |
|---|---|---|---|---|
| **Long-end TOTAL > $1B** *(registered leg)* | +10.9pp, p=0.165 | **+3.1pp, p=0.691** | −11.0bp, p=0.019 | **−4.5bp, p=0.248** |
| Long-end TOTAL > 0 | +9.1pp, p=0.236 | +8.5pp, p=0.266 | −11.0bp, p=0.019 | −10.0bp, p=0.060 |
| 11–21Y > 0 | +8.0pp, p=0.305 | **+15.0pp, p=0.053** | −4.0bp, p=0.349 | **−10.5bp, p=0.028** |
| >21Y > 0 | +8.2pp, p=0.292 | +12.7pp, p=0.103 | −5.0bp, p=0.205 | +2.5bp, p=0.659 |
*(History: the 9/17 headline was −11.5bp, p=0.009, n=224, from an unsaved script. The as-shipped column is today's reproduction at n=228.)*

  **Plain read, as asked:** **PROME's PARK rec holds on the registered leg.** On long-end TOTAL >$1B, the pairing neither filters (p=0.691) nor inverts (p=0.248). **One thing does NOT fit "the inversion is gone" cleanly:** on the **11–21Y bucket**, pairing is somewhat more likely after an `I'` fire (p=0.053), and paired fires are followed by 30Y yields *falling* relative to unpaired (−10.5bp, p=0.028). That is the opposite of a demand-hole signal. With 4 legs tested, the multiple-comparison bar is 0.0125, so it is **not significant after adjustment**. It's disclosed rather than buried because it is the leg where a 20Y award books.
- **GAPS:** (a) ⚠️ **Correction to my item-2 packet, GAP (c): it said the 9/2 per-tenor base-rating "used the same join pools". FALSE.** That base-rating (`matrix_v2_base_rate.py`, `KB-BND-222`) uses no FR2004 data, so the window fix cannot touch it; I conflated it with the unrelated `KB-BND-314` grader-pool fix. Nothing to re-run. Corrected in KB-332, the analysis file and SCRATCH. (b) The instrument's own forward table requires both +5d and +20d (unpaired n=24), while the permutation uses +5d only (n=25); both are reported. (c) **Scope, unchanged and flagged (FORUM-7 A3):** the long-end TOTAL cannot contain a 2Y/3Y/5Y/7Y award, which books in shorter buckets (FR 2004 A-5). So for short-tenor auctions this instrument measures general duration warehousing, not absorption of the award. Which bucket counts is Will's call.
- **WILL_NEEDS:** ⚖️ **WQ-157 leg ② on these numbers** (the corrected columns above). BOND recommends nothing on leg ② itself.

**Also delivered tonight:** FORUM-7 co-sign `f7efb8f76` (letter final `bc540e071`, HENRY's packet `1f1c63baf`; `KB-BND-334`).
