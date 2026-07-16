# WATT — SCRATCH (next-session pickup)

**2026-07-16 — THIRD SESSION (PROME-spawned, Will-directed): EEA-1 ESCALATION ADJUDICATED.**

The thing WATT was built to catch fired, and the answer was **🟠 HOLDS, not 🔴**.

- **PJM-RTO NERC EEA-1 (#105399)** — first WATT-observed emergency-class posting. **Effective 00:01–23:59 on 7/16** (forward-issued for the whole operating day, no end time — *not* a stale 7/15 posting; corrected PROME's framing by pulling the detail page). Plus 5 local load-relief warnings + HLV Warning.
- **Official DM2 LMP leg 5 went live and earned its keep day one:** caught **$410.55 @11:30 EPT** same-day, retraced to **$90.08 @14:55**. The biweekly proxy would have surfaced it ~2wk late — exactly the 7/12-flagged blind spot. **PJM_API_KEY item CLOSED.**
- **Verdict rationale:** EEA-1 is one rung *below* the pre-registered EEA2+ Red bar; $410.55 ≪ $1,000; demand 92.1% < the 97% Orange bar. **Decisive evidence — a 1,500h EIA-930 pull showed this episode is MILDER than 7/1–7/3 on all three axes** (159,046 vs **162,648 MW**; EEA-1 vs **EEA2**; $410 vs **$574**) and is **rolling over** (daily peaks: 126,711 → 141,765 → 151,116 → **159,046 (7/15)** → 154,690 (7/16)). WATT scored that bigger episode 🟠; scoring this one 🔴 = drift.
- **C3 read:** chain **CONFIRMED as mechanism, NOT firing as cost** — a ~4h spike that retraced is a rounding error vs an 8.66¢/kWh industrial bill. P1 spikes aren't the cost channel; **P2 is** (annual cadence). For HENRY: FCF power-cost input **unchanged**; **curtailment risk strengthens** (§202(c) bites at EEA2, and PJM is one rung away twice in 14 days).
- **P1 3→4, composite 12→13/20. Status color 🟠 unchanged. No deploy-posture change.**
- **Routed:** AEOLUS + HENRY direct inbox notes (🟠). VULCAN/CARL/REGINALD/BRENT via NEXUS_BRIEF (curated — outbox stays empty; 🟠 doesn't earn a fleet push). Report: `reports/2026-07-16_eea1-adjudication.md`. KB-WATT-026..031, VX-WATT-P1 rescored, FL-WATT-01 rewritten, L-09..L-12 logged.

**▶ PICK UP HERE (next session, in priority order):**

1. **⚠️ TOP — WILL-FLAGGED, still open: the 7/3 EEA2 is INHERITED and UNVERIFIED** (KB-AEO-018, from HENRY's provisional tenure; KB-WATT-031). It under-props THREE conclusions: WATT-02's n=1 recurrence anchor, the §202(c) curtailment precedent, and the "Episode A was worse" comparison this adjudication rests on. Root rule #3 — **must not carry a trade until verified against a PJM primary.** PJM's board retains only ~15 recent postings → needs an archive-grade pull. Recommended to PROME 7/16; **also asked HENRY** (if he has the 7/3 primary in his archive, it closes cheaply). **Check whether either came back.**
2. **WATT-02 stays OPEN — do NOT bank today's EEA-1 as a hit.** The bar is **EEA2+** (resolve 9/7). Today was a near-miss one rung short. This is the exact "don't bank an unpassed forecast" trap; it will be tempting next boot.
3. **Predictions due:** **WATT-05 (7/20** — FERC informational report on large-load/DC interconnection reform), **WATT-04 (7/23** — EIA Electric Power Monthly, May-26 data, industrial ≥8.66¢), **WATT-03 (8/2** — proxy ≥$500 recurrence), **WATT-06 (8/15 — NEW)**. Resolve as dates pass; none were resolvable 7/16.
4. **~7/21 — the biweekly EIA wholesale file should finally carry 7/13–7/17 delivery prints.** This is the **first real cross-check between leg 4 (daily-wtd proxy) and leg 5 (official 5-min)**: does the $410.55 5-min max show up as an elevated daily-wtd print for deliv 7/15 or 7/16? Two price series that should agree — a coherence test worth doing deliberately.
5. **VULCAN-06 discriminator (7/22–7/31 megacap cluster)** — the 32-vs-55 GW resolution clock for P3. Watch VULCAN's read; **reconcile-to-one, don't duplicate**. WATT prices whatever MW lands.
6. **Reconcile the "1-year-early" finding** (PROVISIONAL, KB-WATT-029): PJM hit 162,648 MW (7/02) vs its own **2027**-forecast peak of 160,451 MW. **Not like-for-like** — EIA-930 hourly-avg vs PJM instantaneous coincident peak; mismatch runs *conservative* so it only strengthens. Confirm vs PJM's published 2026 summer peak (PJM Load Forecast Report, ~Jan-2027). **This is the session's keeper finding — don't let it rot into a naked number.**
7. **Full EIA-923 PJM-fleet heat-rate derivation** — still open, still low urgency (HR 7.0→8.0 swing ≈$3/MWh at $3 gas).

**⚠️ RATE LIMIT (standing):** PJM key is **non-member tier = 6 calls/min**. `power_watch.py` spends **1 call/run**. **Never loop the instrument; no ad hoc DM2 pulls.** This session spent exactly 1.

**Open dependencies (not WATT's to do):** PROME/HENRY → 7/3 EEA2 primary verification (item 1); VULCAN → 7/22–7/31 cluster read (VULCAN-06); Will → nothing pending (PJM_API_KEY closed 7/16).
