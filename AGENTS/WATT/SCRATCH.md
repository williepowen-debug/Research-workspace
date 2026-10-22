# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — October 22, 2026, 09:55 EDT; D:L717 re-test, D:L650 grade, inbox drain

**Current state:** P1/P2/P3/P4 = 3/5/4/2, composite 14/20. P1 de-escalated 5→3 October 22 on the registered letter (D:L717 MET): October 15–21 complete tape 0 of 2,008 prints ≥$1,000 (max $471.98 October 16); DOE 202-26-50 lapsed October 16 unrenewed, index newest still 202-26-50; only postings 105575 (Capacity Advisory, not EEA-class) and 105576 (local warning); Inside Lines feed agrees. Watch fact: outage forecast 71.5 GW October 22, above the emergency days. Re-escalation stays on the RED/EEA2 letter.

**Completed:** KB173–176; STATUS/VX/THESIS/TRADE P1 lines; L650 graded (DR-verified figure NOT PUBLISHED; DM2 RTO hourly 162,186 MW HB17 is_verified=False; one figure with AEOLUS); D:L770 carried acts (clocks reconciled, no live mid-2027 residue; 9/17 EEA2 correction consumed, moves no past or current grade); 4 inbox items drained. Report `reports/2026-10-22_DOCKET-L717-P1-retest-L650-grade.md`; captures `sources/2026-10-22/`.

**Next owner checks:** RBP Special MC October 22 09:00–12:00 EPT outcome unread — read public material at next P2 touch. October 23 L546 float and AEOLUS interchange (9/28) remain armed, not done this session. Weekly coverage by October 27; wake-list October 31. IRAS compliance ~November 8 unadjusted (verify legal calendar); EL26-67 November 16 / December 16; WATT-09 outer November 30. B1 November 10–11 Beijing. 2029/30 BRA December 2026, exact day unverified. NERC December 31; winter gate HELD [KB076].

**Retained limits:** Hedge shares, private firm grid rights, active queue total, Appalachian gas basis and settlement roll unknown. Posting-id read cannot tell unissued from withdrawn; DOE negative bounded to the public index. KILL_MEMO historical C1 sentence still flagged, not edited. 2006 record comparator's DR basis unestablished.

**Persistence / handoff:** Prior pickup preserved verbatim in `archive/2026-10-22_L717-retest/` with SHA256 manifest. Commits and push receipt in PROME memo `PROME/inbox/2026-10-22_from-WATT_L717-P1-retest-and-carried-acts.md`. Packets to HENRY and AEOLUS. PROME-spawned Claude Code subagent (session 84affa50); startup pull not run (foreign dirty work at PROME/HENRY); exact-path commits only. No trade, threshold change, spend or Will decision.
