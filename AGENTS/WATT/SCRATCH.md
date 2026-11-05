# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — November 5, 2026, 18:4x EST; D:L866 grade + WQ-596 + WQ-622 A + inbox drain (WQ-623 bounded session, PROME prome-96)

**Current state:** P1/P2/P3/P4 = **3**/5/4/2, composite **14/20**. D:L866 MET: P1 5→3 on the letter [KB191]. November 1 00:25–00:35 verified $2,015 run met price only at 92.6–91.1% of trailing peak, no posting, cause unknown [KB192]. Inbox clean after this session: 25 of 25.

**Completed:** Grade and report `reports/2026-11-05_DOCKET-L866-P1-retest.md`. WATT-14 BRA at cap 88%, WATT-15 shortfall over 6,831 MW 45%, WATT-16 RED November 6–December 15 55%, WATT-17 ERCOT resumes energization by December 31 45% (f81c49135, before results). Six `combo:` themes KB199–204, charter step 6a. KILL_MEMO A2. Verified feed closed the carried tape gaps, the blank-id limit and the September 17 replay limit [KB193/194]. L-61.

**Next owner checks:** WATT-13 first boot on/after December 2. WATT-16 first boot on/after December 18. WATT-14/15 results December 22, grade by December 31. WATT-17 December 31. **On any boot more than one day after the STATUS cutoff, pull the tape from the cutoff first (L-59); use the verified feed once published (L-61).** Weekly coverage ≤ November 12. Wake-list review L487 MISSED October 31, do next session. IRAS compliance November 8 (Sunday, rollover unchecked). B1 November 10–11. EL26-67 November 16/December 16. Plant orders Wagner November 17, 202-26-40 November 20: watch only. WATT-09 outer November 30. Theme reviews December 1, 2, 15, 18, 18, 23. ERCOT December 10, PUCT December 17. EO 14421 December 24. Eaton/GE Vernova Q3 prints unread. Winter gate HELD.

**Retained limits:** Demand limb weak both ways: recorded, threshold unchanged, review is Will's through PROME. Drill read as not EEA-class, stated at KB193. November 1 cause unknown. Amended RBP docket and requested order date unread. Earlier limits carry (hedge shares, active queue total, Appalachian basis, EIA-930 interchange gap).

**Persistence / handoff:** Prior pickup preserved verbatim at `archive/SCRATCH_ARCHIVE_2026-11-05_before-L866.md`. Fetch clean, origin not ahead at boot; ahead 2 were others' commits. Exact-path commits only. PROME's closeout ask pending at writing. No trade, threshold change, spend or Will decision.
