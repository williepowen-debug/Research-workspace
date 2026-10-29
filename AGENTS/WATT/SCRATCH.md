# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — October 29, 2026, 13:4x EDT; weekly coverage + inbox drain + ISHM custody (Will's "go" 13:31 ET)

**Current state:** P1/P2/P3/P4 = **5**/5/4/2, composite **16/20**. P1 re-escalated 3→5 on the registered RED letter: October 27 18:50–19:00 EPT ran $2,026.73/$1,970.77/$2,297.21 (unverified 5-min) with demand 97.9–99.8% of trailing-24h peak; verified HB18 $719.87. No emergency posting, no 202(c), retraced by 19:15; October 28–29 quiet [KB181/182]. KILL_MEMO C1 not fired.

**Completed:** Weekly coverage WQ295 (2 days late). Inbox 30/30: board_log + KB185, files moved to processed. Grid-equipment custody ACCEPT under WQ-506, charter scope line, KB184. Packets to ISHM, HENRY, AEOLUS, PROME. R1 COR-20261029-07 NO-OP (d47ab7bc2). Lesson L-59. Report `reports/2026-10-29_WATT_SWEEP.md`.

**Next owner checks:** **P1 de-escalation grade on first boot on/after November 4** (KB-149 letter, window October 28–November 3; a re-fire restarts it; DST November 1 = 300 stamps). PROME asked to register it. **On any boot more than one day after the STATUS cutoff, pull the DM2 tape from the cutoff first (L-59).** Wake-list October 31. RBP outcome November 5 (pjm.com reachable again). Weekly coverage ≤ November 5. IRAS compliance ~November 8 unadjusted (verify). B1 November 10–11. EL26-67 November 16/December 16. WATT-09 outer November 30. Eaton/GE Vernova figure at next issuer print. 2029/30 BRA December 2026. Winter gate HELD.

**Retained limits:** No posting found, and posting ids cannot tell unissued from withdrawn. Tape gaps 10/24 17:45–18:10 and 10/27 15:30–16:05 could hide a RED run. The demand limb is a weak discriminator in shoulder season: disagreement recorded, threshold unchanged. No PJM cause published for 10/26–27. Earlier limits carry (hedge shares, active queue total, Appalachian basis, EIA-930 interchange gap, KILL_MEMO historical C1 sentence flagged).

**Persistence / handoff:** Prior pickup preserved verbatim in `archive/2026-10-29_weekly-coverage/` with SHA256 manifest. Startup pull refused on WALTER's dirty registry files; origin not ahead. Exact-path commits only. Instrument idea (boot scans the tape since the last cutoff) sent to PROME, not built. No trade, threshold change, spend or Will decision.
