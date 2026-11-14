# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — November 14, 2026, 12:39 EST; Will-directed catch-up in WATT's own window, research only

**Current state (closed 15:10 EST; card SIG-W-20261114-011 filed, no WATT item):** P1/P2/P3/P4 = 3/5/4/2, composite **14/20**, unchanged. Tape November 11–14 11:00: zero prints ≥$1,000, top $607.87 November 13 (unverified), overnight $446.50 November 14; no posting since 105612 [KB212]. Spark +$48.43 [KB213]. Market Monitor Q3: 2029/30 BRA "effectively" ensured at cap, +$5–10B [KB214]. IRAS registry compliance filed November 9; two rehearing requests [KB215]. DOE 202-26-51 is MISO Campbell, no new PJM order [KB216]. Fermi/Amazon 600 MW and vortex/DC Circuit headlines logged, not scored [KB217/218]. Inbox 2 of 2; L487 review done, list kept; DAEDALUS WQ-678 B: five CLAUDE.md trims applied, four declined [KB219].

**Remaining:** Read the two ER26-3515 rehearing requests (what they seek). Verified feed for November 13–14 at next P1 touch. Eaton 10-Q segment backlog dollars unread (SEC archive refuses this box's client).

**Next dated checks:** EL26-67 responses November 16 (answers December 16). DOE PJM plant orders: Wagner November 17, 202-26-40 November 20 (renewal reads). Weekly coverage ≤ November 21. WATT-09 outer November 30. Themes review December 1 (KB217/218 review dates). WATT-13 first boot on/after December 2. BRA window December 9–15, results December 22 (WATT-14/15 grade by December 31). OPSB Ohio gas-plant hearing December 10, ERCOT December 10, PUCT December 17. WATT-16 on/after December 18. EO 14421 December 24. WATT-17 December 31. B1 T1 January 10/11 Beijing. GE Vernova Q4 about late January, Eaton Q4 about early February. Winter gate HELD (AEOLUS owns the vortex). **On any boot more than one day after the STATUS cutoff, pull the tape from the cutoff first (L-59).**

**Retained limits:** Demand limb weak both ways (review is Will's through PROME). November 1 and November 14 overnight spikes, cause unknown. Amended RBP docket unread. Hedge shares, active queue total, Appalachian basis, EIA-930 interchange gap carry.

**Persistence / handoff:** Prior pickup verbatim at `archive/SCRATCH_ARCHIVE_2026-11-14_before-catchup.md`. Origin level at boot; foreign dirty tree (PROME SCRATCH, CALENDAR) untouched. Exact-path commits only. Packet `PROME/inbox/2026-11-14_from-WATT_catch-up-read.md`. No trade, card, threshold, spend or Will decision.
