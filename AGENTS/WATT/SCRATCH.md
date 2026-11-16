# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — November 16, 2026, 14:22 EST; PROME assignment (Will's word 13:45 ET), HOLDING for PROME

**State:** P1/P2/P3/P4 = 3/5/4/2, composite **14/20**, unchanged. **Built:** `tape_scan.py` boot leg (acceptance `proposals/2026-11-16_TAPE_SCAN_ACCEPTANCE.md`, tests `tests/test_tape_scan.py` 22 of 22; replay 10/24–10/28 finds the 10/27 18:50–19:00 fire as graded 10/29) [KB220]. Charter boot line and FILES rows updated (PROME class C4; PROME verifies). STATUS carries the machine-read line `**Tape cutoff (machine-read):** 2026-11-14T11:00 EPT`; **move it forward whenever a later tape is read**, or the scan rescans (harmless) from the old point.
**Blocker:** PJM Data Miner 2 refuses the key, HTTP 401 with empty body, every call from 14:12 ET November 16 (worked November 14; key file unchanged since November 5). Live tape scan = UNKNOWN for November 14 10:00 to now; the demand limb was met in 7 of those 52 hours [KB220]. Key holder: Will, via PROME. No new key or account from this desk.
**Inbox:** 1 of 1 drained (WALTER SIG-W-20261116-005, KB221; board row).
**Remaining:** once DM2 answers: run `boot.py` (the scan reads from the cutoff), grade any run by the letter on the verified feed, move the cutoff line. Read the two ER26-3515 rehearing requests. Eaton 10-Q segment backlog dollars unread. Closeout only when PROME asks (heavy mode: tooling change).

**Next dated checks:** EL26-67 responses November 16 (answers December 16). DOE PJM plant orders: Wagner November 17, 202-26-40 November 20. Weekly coverage ≤ November 21. WATT-09 outer November 30. Themes review December 1 (KB217/218/221). WATT-13 first boot on/after December 2. BRA window December 9–15, results December 22 (WATT-14/15 by December 31). OPSB December 10, ERCOT December 10, PUCT December 17. WATT-16 on/after December 18. EO 14421 December 24. WATT-17 December 31. B1 T1 January 10/11 Beijing. GE Vernova Q4 late January, Eaton Q4 early February. Winter gate HELD (AEOLUS).

**Retained limits:** Demand limb weak both ways (review is Will's through PROME). November 1 and November 14 overnight spikes, cause unknown. Amended RBP docket unread. Hedge shares, active queue total, Appalachian basis, EIA-930 interchange gap carry. Ledger staleness flags FLOW/PREDICTIONS/TRADE +9 days behind STATUS: content unchanged since their last edit (no score, mechanism or prediction moved).

**Persistence / handoff:** Prior pickup verbatim at `archive/SCRATCH_ARCHIVE_2026-11-16_before-tape-scan.md`. No pull, no push (GitHub lookups failing; PROME's instruction). Foreign dirty tree (CATO, CREED) untouched. Exact-path commits only. No trade, card, threshold, spend.
