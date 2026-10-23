# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — October 23, 2026, 01:05 EDT; D:L789 touch (L546 float, AEOLUS interchange, RBP carry, inbox drain)

**Current state:** P1/P2/P3/P4 = 3/5/4/2, composite 14/20, unchanged. October 22 complete day max $79.98, 0 ≥$500 despite the 71.5 GW outage forecast; October 23 through 00:50 EPT quiet (max $39.93, demand 88.7% of 24h peak, 0 emergency-class postings) [KB179]. Re-escalation stays on the RED/EEA2 letter.

**Completed:** L546 graded DONE: `power_watch.py` read_pjm_demand rounds demand % to printed 1 dp before compare, 5/5 edge tests, `sources/2026-10-23/test_l546_demand_pct.py` [KB178]. AEOLUS interchange test run at EIA-930: on 9/16–17 PJM imported from TVA, exported to MISO below 9/15's level, net interchange ~0 on 9/17, so export pull is NOT SUPPORTED and the outage-driven read stands [KB177]; packet to AEOLUS 579588e3c. CYPHER boundary confirmed, packet 7f94e64f4. 3 inbox items drained [KB180]. Report `reports/2026-10-23_DOCKET-L789-touch.md`.

**Next owner checks:** RBP consultation outcome CARRIED to November 5 (next Special MC) or PJM's section 205 filing, whichever comes first. pjm.com returned 403 on October 23. Weekly coverage by October 27. Wake-list October 31. IRAS compliance ~November 8 unadjusted (verify legal calendar). EL26-67 November 16 / December 16. WATT-09 outer November 30. B1 November 10–11 Beijing. 2029/30 BRA December 2026, exact day unverified. NERC December 31. Winter gate HELD [KB076].

**Retained limits:** Hedge shares, private firm grid rights, active queue total, Appalachian gas basis and settlement roll unknown. EIA-930 pair flows do not reconcile to TI (+3.2 to +6.2 GW). The posting-id read cannot tell unissued from withdrawn. The KILL_MEMO historical C1 sentence is still flagged, not edited. L546 fix: author-tested only, not independently verified.

**Persistence / handoff:** Prior pickup preserved verbatim in `archive/2026-10-23_L789-touch/` with SHA256 manifest. Commits and push receipt are in the PROME memo `PROME/inbox/2026-10-23_from-WATT_L789-touch.md`. PROME-spawned Claude Code subagent (prome-e7 spawn). Startup pull not run: foreign dirty work at PROME/ and AGENTS/VOCABULARIES.tsv, and origin was not ahead. Exact-path commits only. No trade, threshold change, spend or Will decision.
