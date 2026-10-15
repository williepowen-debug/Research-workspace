# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — 2026-10-15 08:2x ET; L692/L693 graded and recorded (PROME Tier-1 wake → crash recovery, prome-73)

**Source boundary:** PJM board (ids 105552–105574 read; dashboard 10/15 08:06 ET), DM2 tape 10/12–10/14 complete + 10/15 to 08:00, DM2 outages (executed 10/12–10/15), EIA-930, DOE 202-26-50 PDF + 2026 index (10/15 08:07 ET), PJM M-13 rev 98. P1/P2/P3/P4 **5/5/4/2**, composite 16/20. No trade, threshold, gate letter or prediction changed.

**Completed:** L692 — L654 full-day leg CLOSED (10/12 max $845.48, 0 RED; 202-26-50 issued 10/12). PJM's **5th emergency 10/13–14** (EEA-1 ×2, Pre-Emergency DR ×4, 202-26-50 10/13–16); **RED re-fire 10/13** (29 consecutive ≥$1,000, max $2,327.04, ~108 GW load, ~61 GW out). L693 — de-escalation **NOT MET**. C1/C2/C3 NOT-FIRED. KB-047 hedge inference withdrawn (KB-152). Whole inbox drained (13 files incl. the crash brief). Records: KB-147…155, VX P1, FLOW FL-WATT-08, TRADE P1/P4, STATUS, LESSONS L-55…57, report `reports/2026-10-15_DOCKET-L692-L693_PJM-emergency-clear-day-grade.md`. Packets HENRY/AEOLUS/VULCAN and PROME memo `PROME/inbox/2026-10-15_from-WATT_L692-L693-grade.md` — see that memo for commit shas and push receipt.

**Crash note:** the 10/14–15 session died at 03:08 ET with most records drafted only in /tmp; recovered from its transcript and re-verified (report § Crash recovery; L-57). Its over-claiming pickup is archived verbatim as the second block of `archive/SCRATCH_ARCHIVE_2026-10-15_before-L692-L693.md`.

## NEXT OWNER TOUCH — registered event work, not automatic monitoring

1. **202-26-50 lapse, 23:59 10/16:** confirm no renewal at the DOE index; renewal or any new EEA-class posting re-dates the clock.
2. **P1 de-escalation re-test, first boot ≥10/22:** clear calendar days 10/15–10/21 (no EEA-class posting, no new PJM §202(c), no RED re-fire). PROME asked to register the DOCKET row. No early 5→3. Outage forecast 65.0–68.1 GW/day through 10/21 (KB-155) — watch fact.
3. **9/17 EEA-2 re-adjudication (historical):** KB-122 recorded Emergency DR in BGE/PEPCO/DOM with "no EEA-2 found" via a fact-sheet mapping; M-13 rev 98 §2.3.2 ties EEA2 to Emergency LM reductions. No current score depends on it. Lead: Inside Lines "PJM Reviews September Hot Weather Operations" (10/12), unread.
4. **FERC:** registry compliance filing due ≈11/8 (30 days from 10/9); EL26-67 responses 11/16, answers 12/16; WATT-09 outer 11/30.
5. **Other clocks:** battery recheck ≥10/19; weekly cadence by 10/19; deferrals (L546 float, AEOLUS interchange, KB-034 metered-vs-DR) 10/23; wake-list review 10/31.

**Unresolved owner carry:** hedged/floating exposure owed to VULCAN (no longer tilted to "material", KB-152); 6.5 GW gap; Appalachian basis/NG=F settlement clock; ERCOT Cal-27 discriminator; 8/13–8/16 spark cause.

**Operational continuity:** this window = Claude Code subagent of session 16d245b5-0cb3-4174-b43d-e76c4903c384 (PROME-spawned); do not reuse. Startup pull not run (foreign dirty tree incl. staged renames); exact-path commits only.
