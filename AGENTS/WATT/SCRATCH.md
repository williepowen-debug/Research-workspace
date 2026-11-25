# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — November 25, 2026; PROME C9 commission 11:35 ET (prome-77; WALTER 09:43 ET read, card SIG-W-20261125-017)

**State:** P1/P2/P3/P4 = 3/5/4/2, composite **14/20**, unchanged. **Delivered:** AI power demand read `research/2026-11-25_ai-power-demand-read.md` [KB225]: equity repricing only on the record (power and equipment names −10 to −21% over November 20/24/25 vs SPY −6.8%, XLU −0.6%); contracted record still growing at the late-October prints; CRA for PJM: supply binds by 2030; no named November cancellation found (bounded). Section 301 power-equipment sizing, ASSUMPTION grade [KB226]. Inbox drained: 0 top-level + 14 WALTER [KB227], board_log rows, five corrections receipted. Packets: TERRY tradeability read (no card); PROME delivery `PROME/inbox/2026-11-25_from-WATT_ai-power-demand-read.md`.
**Blocker:** PJM Data Miner 2 refuses the key, HTTP 401, since 14:12 ET November 16 (still at boot 11:36 ET November 25). WILL_QUEUE 695, Will's hands. Tape November 14 11:00 to now UNKNOWN. WATT-13 (December 2) cannot be graded without it. No new key or account from this desk.
**Flagged to PROME:** WQ-735 honest-client-name packet never reached WATT, but `power_watch.py` sends a Chrome User-Agent to emergencyprocedures.pjm.com and the EIA wholesale xlsx; not switched (WQ-735's test-first condition is PROME's).
**Remaining:** once DM2 answers: run `boot.py`, grade any run on the verified feed, move the cutoff, read the November 17–19 and 24–25 cold mornings, try verified hourly January–February 2025. Read the PJM fast-energization FERC filing, the ER26-3515 rehearing requests, DOE Wagner and 202-26-40 renewals, Eaton 10-Q segment backlog, LBNL large-load forecasting report (November 11, unread).

**Next dated checks:** WATT-09 outer November 30. Themes review December 1. WATT-13 first boot on/after December 2 (key-dependent). ERCOT Batch Zero December 10, OPSB December 10, PUCT December 17. BRA window December 9–15, results December 22 (WATT-14/15 by December 31). EL26-67 answers December 16. PJM LAS December 18 (final 2027 large-load adjustments). WATT-16 on/after December 18. EO 14421 December 24. WATT-17 December 31. Section 301 comments January 5, hearing January 25. B1 T1 January 10/11 Beijing. GE Vernova Q4 late January, Eaton Q4 early February. Hoover review April 30, 2027. Winter gate HELD (AEOLUS).

**Retained limits:** Dominion and Exelon Q3 figures are secondary reads; the cost sizing is rules of thumb. Demand limb on a winter morning is not a stress reading (KB222). November 1 and November 14 overnight spikes, cause unknown. Hedge shares, active queue total, Appalachian basis, EIA-930 interchange gap carry. Ledger staleness flags FLOW/PREDICTIONS/TRADE behind STATUS: content unchanged (no score, mechanism or prediction moved).

**Persistence / handoff:** Prior pickup verbatim at `archive/SCRATCH_ARCHIVE_2026-11-25_before-ai-demand-read.md`. No pull (foreign dirty tree: HOMER and other desks' staged work untouched). Exact-path commits only; no push (PROME pushes). No trade, card, threshold, spend.
