# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — November 11, 2026, 09:4x EST; catch-up wake (PROME prome-2b, Will 09:24 ET), research only

**Current state:** P1/P2/P3/P4 = 3/5/4/2, composite **14/20**, unchanged. Tape November 5–11: zero prints ≥$1,000, top $641.45 verified November 9 [KB205]; demand limb ≥97% in 30 of 154 hours, letter price-gated this winter [KB206]; spark +$42.51 [KB207]. Grid-equipment figure refreshed (Eaton, GE Vernova, Siemens) [KB208]; SoftBank write-off logged, direction not established [KB209]; B1 T1 re-dated to 2027-01-10/11 Beijing [KB210]. Inbox 13 of 13 [KB211]; COR-20261110-12 NO-OP receipted.

**Remaining:** Closeout when PROME asks (C1–C9; NEXUS_BRIEF not yet folded, push not done). Wake-list review L487 still owed (MISSED October 31). IRAS compliance filing (due November 8) unchecked. November 10–11 prints re-read on the verified feed at next P1 touch. Eaton 10-Q segment backlog dollars unread (SEC archive refuses this box's client).

**Next dated checks:** Weekly coverage ≤ November 18. VULCAN's SoftBank transcript row November 13 (watch). EL26-67 November 16/December 16. Plant orders Wagner November 17, 202-26-40 November 20. WATT-09 outer November 30. Themes review December 1. WATT-13 first boot on/after December 2. BRA window December 9–15, results December 22 (WATT-14/15 grade by December 31). OPSB Ohio gas-plant hearing December 10, ERCOT December 10, PUCT December 17. WATT-16 on/after December 18. EO 14421 December 24. WATT-17 December 31. B1 T1 January 10/11 Beijing. GE Vernova Q4 about late January, Eaton Q4 about early February. Winter gate HELD. **On any boot more than one day after the STATUS cutoff, pull the tape from the cutoff first (L-59).**

**Retained limits:** Demand limb weak both ways (review is Will's through PROME). November 1 cause unknown. Amended RBP docket unread. Hedge shares, active queue total, Appalachian basis, EIA-930 interchange gap carry.

**Persistence / handoff:** Prior pickup verbatim at `archive/SCRATCH_ARCHIVE_2026-11-11_before-catchup.md`. Origin not ahead at boot; foreign dirty tree untouched. Exact-path commits only. Packet `PROME/inbox/2026-11-11_from-WATT_catch-up-read.md`. No trade, card, threshold, spend or Will decision.
