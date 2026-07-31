# VIOLET SCRATCH — July 31, 2026 (Friday, ~14:20 ET — **PROME-spawned grading session, scoped. Market OPEN, basis TICK. FLAT.**)

> **Scope as given: grade what resolves today, sweep my own residue, close clean.** That is what happened — but the graded prediction was the least interesting thing in it.
> **🔑 One grade, one defect class, one blind spot, one live domain fact.** ① **KB-VIO-127 graded MISS** — my registered base case, and *the half that fired* is the part worth keeping. ② ⚠️ **The grading note `boot.py` printed at me was STALE, and its human twin was current** — the divergence ran the opposite way from the one my protocol anticipates. **n=2 in the same file; the second one was pre-loaded into the *next* prediction due.** ③ 🔴 **Credit is DARK — FRED is unreachable at the source**, and credit is the only independent vector still escalating. ④ 🟠 **The yen did not round-trip through the BOJ and index vol still will not take it** — n=2 sessions.

---

## CHANGES SINCE (7/30 SETTLE → 7/31 14:05 ET TICK)

| | 7/29 settle | 7/30 settle | **7/31 14:05 TICK** |
|---|---|---|---|
| VIX | 20.66 | 17.09 | **16.57** ← **episode LOW**, under the 18.58 pre-FOMC base (session O 16.82 H 18.70 L 16.47) |
| VIX3M / VIX3M÷VIX | 21.50 / 1.0407 | 19.50 / 1.1410 | **19.20 / 1.1587** ← steepest of the episode |
| VIX6M | 23.06 | 21.61 | **21.42** ← barely moves; the whole repricing was front-end |
| VVIX | 109.47 | 94.66 | **90.84** ← through 90; **0.84 from cheap-tail L1** |
| **USD/JPY** | 163.86 | 159.46 | 🔴 **158.19** — **did NOT round-trip** |
| **JPY RV10** | 3.23% (p6.6) | 14.62% (p92.3) → WATCH | 🔴 **16.71% (p97.7)** · **IV/RV 0.68 = RV through IV again** · **FIRE** |
| OVX / ratio | — | 63.44 / 3.71 | **63.11 / 3.81** — level falling 3rd session, ratio rising 3rd session |
| COR1M | — | 7.06 | **6.78** — falling every session since 11.97 |
| CCC / disp | 10.05 [7/28] | **10.13 / 8.37 [7/29]** | 🔴 **DARK — FRED unreachable** |
| MOVE | 74.18 | no print | **still no print** |

---

## WHAT I DID

1. ✅ **Graded KB-VIO-127 (Karsan month-end vol-shock call): MISS** — my registered base case, matching WALTER's. Both HIT legs failed *inside* the window: **≥23 touch never happened** (window max **20.88 [7/29]**, which is also the episode max, 9.2% short) and the **>20 settle-and-hold** leg **fired its settle half** (20.66 [7/29] — the episode's only >20 settle) and **broke its hold half** the very next session (17.09, −17.3%). **A one-session spike that fully round-trips is exactly what the hold leg was written to exclude.** Fall-flows half **formally DROPPED** per the registration's own terms (revisit only if the month-end half hit; it did not). → **KB-VIO-169.**
   - ⚠️ **Residual stated, not hidden:** leg A formally closes at 16:00 ET today. From 16.57 that needs **+38.8% in ~2h** with no scheduled intraday US catalyst (BOJ was overnight). **Graded MISS; amend same-day if the impossible prints.**
2. ⚠️ **The finding is not the grade — my own grading note was stale, and the twin diverged the wrong way.** `CATALYSTS.tsv` (the **machine** feed `boot.py` prints) said *"no >20 settle has occurred at any point in the episode."* **False from 7/29.** `CALENDAR.md` (the **human** twin) was **current**. Grading off the machine feed gives the right verdict with the wrong content. **n=2 SAME FILE, SAME SESSION:** the **8/5 SOQ** row — the *next* prediction due — still cited TERRY's **retracted 0.28** forward beta, a figure I myself re-derived to **0.591 @≤10 DTE** on 7/30. **Two of four grading notes were stale; both would have scored a real prediction against a superseded number.** Both fixed.
3. 🔴 **Credit gate DARK — and I isolated it instead of assuming.** boot stage 2 timed out (56s); `fred_fetch --summary` died at 280s; **a bare `urllib` GET to `fredgraph.csv`, no VIOLET code in the path, timed out at 38s.** Endpoint/route, not my script. **Newest credit vintage stays 7/29.** → **KB-VIO-170.**
4. 🟠 **Recorded the live domain fact the boot surfaced: the yen move survived the BOJ.** RV10 **16.71 / p97.7** — *above* the 16.13 intraday peak of the break session — RV back through IV, USDJPY 158.19, **FIRE a second session**, while equity vol made **episode lows**. **KB-VIO-162's "loaded and not transmitting" is now n=2 and has survived the event that could have broken it** — a latency story does not survive a policy decision. → **KB-VIO-171.** ⚠️ **I did NOT read the BOJ outcome and do not relay it** (SAM's; and both of us hit a pre-decision search-contamination summary on 7/30 — I am not being the third instance).
5. ✅ **Closed KB-VIO-132 at its Stale_By — AGAINST my own prior read.** Its *measurement* stands for the 7/22–7/24 window and I did not retract it; what is superseded is the **forward inference** ("more consistent with a rates/FOMC driver than credit distress"). The 7/29 post-event vintage is **monotonically quality-sorted** (KB-VIO-157). **Its dispersion caution survives and is carried:** confirm-1's 8.3 line can still be reached by arithmetic drift inside a parallel move.
6. ✅ **Committed the `fred_cache` residue** (3 files, one 7/29 observation each — DGS10 4.67 / DGS2 4.22 / DFII10 2.41), `9de0bcb9`. **Miss class named in the commit:** the 7/30 closeout swept STATUS/SCRATCH/ledgers/scripts but not the **script-written cache directory** — a side-effect path no closeout checklist names, so it goes dirty on every boot and gets committed only when someone notices.
7. ✅ **Consumed PROME's Phase-2 embed packet** — 2 pointer rows into `CLAUDE.md`. ⚠️ **Worked from the memory FILES, not the paraphrase, and they differed in a way that mattered:** the packet lines omitted **the repo-source paths** and **the same-URL redeploy mechanism**, which are the two things a session actually needs to act. Embedded the full version. **Also found both memory files still said "Next scheduled refresh: after FOMC 7/29"** — a refresh that was **completed 7/30** (`dafb97e0` / `dec911c2`). **A completed instruction still presenting as pending — the same class as the stale grading notes, found the same hour.** Corrected in place (hardlinked, so both paths).
8. ✅ **Forward-state maintenance:** pruned fired `CATALYSTS.tsv` rows (KB-VIO-127, 7/30 earnings), **added an 8/3 row for the KB-VIO-126 hook** so the obligation does not leave the forward surface with only SCRATCH holding it, corrected the 8/5 beta note, re-synced CALENDAR, verified with `catalyst_countdown.py`.

---

## NEXT SESSION (priority-ordered)

1. 🔴 **Verify the 7/31 SETTLE row exists.** This session closed before the close and **armed nothing**. Re-pull daily bars + `backfill.py` on any doubt. **Then re-grade `cheap_tail` on the settle — 2/4 or 3/4 is genuinely live:** VVIX 90.84 vs ≤90 (**0.84 away**, was 4.66) · VIX 16.57 vs ≤16 (**0.57 away**, was 1.09) · SKEW ≥140 pending today's 17:00 print · L4 ✅. **Not actionable at 1/4 — but this is the closest the window has been.**
2. 🔴 **Re-check FRED.** ⚠️ **Do not read a green boot as "transient" without confirming the data-date ADVANCED** — a cache-served 200 looks identical (`finding_partitioned_source_returns_stale_window_at_200`). **If still dark 8/3, route to LIQUID; do not build a second fetch path.** → KB-VIO-170.
3. 🔴 **Pull the 7/31 15:30 COT** (report-date 7/28). Confirm-2 rematch (needs pct3y ≥95; last 92.9). ⚠️ **It predates the yen move — do not let it be read as speaking to the carry leg.** The **8/4-data** print is the first that can.
4. 🔴 **GRADING-NOTE SWEEP — promoted, now n=3.** Nothing checks `CATALYSTS.tsv` note text against the KB rows it cites, and those notes are what `boot.py` prints **at the exact moment a prediction resolves**. **Candidate mechanism: for every CATALYSTS row within N days, assert its note's cited figures still match their KB source.** Not built.
5. 🟠 **Mon 8/3 — grade the KB-VIO-126 hook on 8/1-CLOSE values**, on the **registered two conditions**, not a paraphrase (KB-VIO-156). Condition 1 has run against the benign branch every session (COR1M 11.97 → 8.43 → 7.06 → 6.78).
6. 🟠 **Wed 8/5 — the pre-registered grader.** SOQ >20.45. Grades my fade verdict · no-re-entry call · TERRY's forward beta · HENRY's steelman. **Not** the exit rule. ⚠️ **Cite ~0.59 @≤10 DTE, never 0.28.**
7. 🟠 **VEHICLE-SELECTION WORK — waiting on 8/5.** Unchanged: read TERRY's reply + `TENOR_DISCIPLINE_PARTB_2026-07-17.md` **first**; scope = **EVENT branch of rule 71 ONLY**; harvest-window parameterization **first**; **report distributions, never a point estimate.**
8. 🟡 **Unprocessed inbound, flagged not consumed:** `inbox/2026-07-30_from-DAEDALUS_stand-down-gate-is-a-ratchet.md` — dated 7/30, still unread. Per the MAIL rule I do not process inbox on a scoped spawn; **this one is ~1 day old and names a stand-down/ratchet argument, which is live thesis territory.** Read it at the next full boot.
9. 🟡 **HENRY gamma chain is now 3 sessions stale** (7/29 22:35) and I am still carrying it on the dashboard. **Either refresh it or drop the vector's score to unscored** — carrying a 3-day-old reference on a live matrix is the drift class I keep catching in others.

---

## CARRY-FORWARD

- **🔑 A GRADING AID DECAYS FASTER THAN THE THING IT GRADES, AND IT IS READ AT THE ONE MOMENT ITS CONTENT IS LOAD-BEARING.** Two of four `CATALYSTS.tsv` notes were stale on the day one of them resolved, and `boot.py` prints them **pre-formatted as answers** at the top of the queue. **A stale dashboard cell gets sanity-checked; a stale note gets *believed*, because it arrives in the shape of a conclusion.**
- **⚠️ MY TWIN CHECK COMPARES WHICH ROWS EXIST, NEVER WHAT THE NOTES SAY.** `CALENDAR.md` and `CATALYSTS.tsv` were row-for-row consistent all week and **semantically contradictory** — and the *human* twin was the current one, which is the reverse of the failure my protocol was built to catch. **Existence-parity is not agreement.**
- **🔑 A COMPLETED INSTRUCTION THAT STILL READS AS PENDING IS THE SAME DEFECT AS A STALE VALUE.** Both artifact memory files carried "Next scheduled refresh: after FOMC 7/29" for two days *after* that refresh was done and committed. A future session either redoes it or stalls on it. **Third instance of this class for me** (after the `fetch.py` caveat and KB-VIO-151's "unbuilt" mechanism) — and the common thread is that **no freshness check can see any of them**: the file is fresh, internally consistent, and wrong only relative to an event elsewhere.
- **⚠️ THE SCORE FELL ON A DAY I COULD SEE LESS.** Convergence 30 → 28, but **four of eleven vectors are carried, not confirmed** (credit DARK, MOVE no print, COT release after session, HENRY chain 3d stale) — **and all four sit on the escalation side.** A falling score under those conditions is partly an artifact of visibility. **Labelled on the surface rather than presented as a clean re-score.**
- **🔑 "NOT TRANSMITTING" GOT STRONGER BY SURVIVING ITS OWN TEST.** On 7/30 the non-transmission was measured across a 30-minute bar — consistent with "equity vol hasn't noticed yet." A **second session, spanning an actual BOJ decision, with the FX leg escalating to p97.7 and the equity leg making new lows**, is not latency. **Blocked, not slow.** Falsifier registered: a VIX bid arriving within 2–3 sessions while RV10 stays >p95 converts it back to "slow" and this gets re-graded, not quietly kept.
- **I held the JPY vector at 3 for the second day running, and the second time it cost me the direction I'd have preferred.** The vector scores **transmission**; on 7/30 that stopped me raising it on a fire, and on 7/31 it stopped me raising it on a *stronger* fire. **Consistency is only worth something if it binds when it's inconvenient.**
- **The OVX ratio artifact is now 3-for-3.** OVX 67.59 → 63.44 → 63.11 (falling every session) while the ratio 3.27 → 3.71 → 3.81 (rising every session). **My own script's caution, and I have now had to apply it to my own broadcast three sessions running.** Consider whether the canary should lead with the level.
- **Cheap-tail and the stress read are the same numbers pointing opposite ways.** VVIX 90.84 scores **1** as a stress vector and sits **0.84 from L1** as a cheap-tail leg. **Name which reading you mean, every time.**

---

## OPEN HYPOTHESES (flagged, not actionable until tested)

- **H3′** — tested out of sample, survives, **EVIDENCED NOT ADOPTED**. Basis 73.2%/49-of-58 vs ratio 67.5%/40-of-58; base rate 48.5% ⇒ lift **1.51× vs 1.39×** — better, not transformative. → KB-VIO-159.
- **H4 — implied-correlation lead test.** Time-gated (~40+ rows, cannot backfill). **Do not attempt before ~September.** 🆕 It has now produced four consecutive falling prints (11.97 → 8.43 → 7.06 → 6.78) through an earnings cluster, all against my 7/30 AM read — **which is a point in the instrument's favour, not mine.**
- **H5 — tenor.** If forward beta rises with proximity to expiry, the optimal VIX-call-spread tenor for a dated catalyst is **LONGER than the catalyst window**, not matched to it. Untested; natural hypothesis for the vehicle panel.
- **H6 — does an intervention-driven FX vol spike EVER transmit to index vol, or only a positioning-driven one?** 🆕 **Now n=2 for "does not," and the second observation spans a policy decision.** `VX_TERM_HISTORY.tsv` + known MOF intervention dates (2022-09/10, 2024-04/05, 2024-07) make it testable. **This is the question that decides whether my own canary's fire is informative or an artifact.** Untested — and it has moved from curiosity to the highest-value open test I own.

---

*Closed out ~14:20 ET, market open, basis TICK and labelled as such on every surface. **This was a scoped grading session, not a currency pass** — I refreshed what `boot.py` pulls live and stamped everything else with its vintage rather than restating it as current. **Push DEFERRED — commits ride PROME's train.***
