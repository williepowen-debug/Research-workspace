# WATT — EEA-1 Escalation Adjudication (2026-07-16)

**Session:** third WATT session, PROME-spawned (Will-directed), ~3:05–3:40 PM ET 2026-07-16.
**Question put to WATT:** PJM posted an emergency-class alert (NERC EEA-1, PJM-RTO #105399) and the official-LMP leg caught a $410.55 intraday spike. **Is WATT's 🟠 now 🔴?**

## VERDICT: 🟠 HOLDS. Not 🔴.

**The escalation is real and is the first emergency-class posting WATT has ever caught live — but it is a strictly milder episode than the one WATT already scored 🟠 two weeks ago, and it clears no Red band.**

Red requires (pre-registered, `CLAUDE.md` §THRESHOLDS): **EEA2+ / Load Shed / §202(c)**, **OR** RT LMP **≥$1,000**, **OR** a reserve-shortage posting. None met:

| Red bar | Observed today | Verdict |
|---|---|---|
| Emergency posting ≥ **EEA2** / load shed / §202(c) | **EEA-1** Alert (one rung below EEA2), PJM-RTO #105399 [PJM emergencyprocedures.pjm.com, posting detail pulled 7/16 15:10 ET] | **not met** |
| RT LMP ≥ **$1,000**/MWh | today max **$410.55 @11:30 EPT**; latest **$90.08 @14:55 EPT** [PJM DM2 `rt_unverified_fivemin_lmps`, PJM-RTO, 7/16] | **not met** — Yellow band (≥$150) |
| Demand → reserve-shortage posting | **92.1% of 24h peak** (146,552 MW @7/16 18Z vs 159,046 MW @7/15 22Z) [EIA-930] | **not met** — Yellow band (≥90%), *below* the ≥97% Orange bar |

## The finding that decides it: this episode is SMALLER than the 7/1–7/3 one

WATT pulled a full 1,500-hour EIA-930 window (2026-05-15 → 2026-07-16) rather than trusting the instrument's 24h frame. That reframes the escalation:

| | **Episode A: 7/1–7/3** | **Episode B: 7/15–7/16 (now)** |
|---|---|---|
| Peak demand (EIA-930 hourly avg) | **162,648 MW** @7/02 22Z | **159,046 MW** @7/15 22Z |
| Emergency posting | **EEA2** (7/3, inherited KB-AEO-018 — *see caveat*) | **EEA-1** (7/15 16:25 EPT, #105399) |
| Price | **$574.04**/MWh wtd-avg, deliv 7/02 [EIA ICE proxy] — Orange | **$410.55**/MWh 5-min max @11:30 EPT [PJM DM2] — Yellow |
| WATT status at the time | **🟠** | **🟠 (holds)** |

Episode B is lower on **all three** axes — demand, posting severity, price. WATT scored Episode A at 🟠. Scoring Episode B 🔴 would be band drift, not evidence.

**Within-episode direction is easing, not escalating:** daily peak ran 126,711 MW (7/12) → 141,765 → 151,116 → **159,046 (7/15)** → **154,690 (7/16, rolling over)**; price retraced from $410.55 @11:30 to $90.08 @14:55 EPT the same day [EIA-930 + PJM DM2, pulled 7/16 15:05–15:15 ET].

## Correction to the framing in the tasking

PROME's note (and the task packet) described #105399 as "posted 7/15 16:25, **still on the board**." The posting detail says something different and more precise — WATT pulled `/ep/pages/viewposting.jsf?id=105399` directly:

> "A Maximum Generation Emergency/Load Management Alert - Capacity Emergency - NERC EEA 1 has been issued **from 00:01 on 07.16.2026 through 23:59 on 07.16.2026**." [PJM posting #105399, retrieved 2026-07-16 15:10 ET]

It is **not** a stale 7/15 posting lingering on a board — it is a **forward-issued alert covering the whole of today's operating day**, with no Effective End Time set (unlike the local load-relief warnings, which carry explicit end times, e.g. #105400 ended 7/15 20:38). *This makes it more live than the tasking implied, and yet still not Red* — because severity, not staleness, is what the Red band tests.

**Severity ladder note (why EEA-1 ≠ EEA2):** PJM's ladder is Alert → Warning → Action. EEA-1 = "all available generation resources in use" — an *advance* capacity-emergency alert. EEA2 = load-management procedures actually in effect / reserves cannot be met. WATT's Red band is deliberately set at EEA2+ because that is where load actually gets curtailed — the point at which the §202(c) data-center-curtailment precedent (set 7/3) becomes live.

## Prediction resolution — WATT-02 is a NEAR-MISS, still OPEN

**WATT-02** ("≥1 more PJM **EEA2+** or §202(c) event before Labor Day 2026", resolve 9/7) — an EEA-1 does **not** resolve it. The bar is EEA2+. **Stays OPEN.** Flagging explicitly because this is exactly the "don't bank an unpassed forecast" trap: the posting is emergency-class, feels like a hit, and is one rung short. **WATT-03/04/05** (resolve 8/2, 7/23, 7/20) all not yet due. No prediction resolves this session.

## What DOES escalate: the structural read (P2/P3), not the live-stress read (P1)

The genuinely new, thesis-relevant finding is not today's spike — it's the demand *level* the spikes are happening at:

> **PJM's own 20-yr forecast puts the 2027 summer peak at 160,451 MW** [PJM Inside Lines, pub 2026-01-14]. PJM's actual demand hit **162,648 MW on 2026-07-02** and **159,046 MW on 2026-07-15** [EIA-930]. **PJM is running at its own 2027-forecast summer peak, in July 2026 — one year early — and calling emergency-class postings to get through it (2 episodes in 14 days).**

*Like-for-like caveat (mandatory):* EIA-930 is **hourly-average MW** at the BA level; PJM's forecast peak is an **instantaneous coincident** MW. These are not the same measure. The mismatch runs **conservative** — instantaneous peak ≥ hourly average — so the actual 7/02 instantaneous peak was **≥162,648 MW**, which only strengthens the comparison. Treat the 1-year-early claim as **PROVISIONAL** until reconciled against PJM's own published 2026 summer-peak figure (PJM Load Forecast Report, ~Jan-2027). Reconcile-to-one-figure: WATT is canonical for the power number; AEOLUS/HENRY should cite this, not re-derive it.

This is the **mechanism-vs-thermometer** discipline doing its job: today's $410.55 print is the confounded **thermometer** (a hot day). The demand level arriving a year ahead of PJM's own forecast, against a capacity stack that cleared at cap twice and 6,623 MW short for 27/28, is the **mechanism**.

## C3 READ (AEOLUS climate → WATT grid-stress → power price → cost)

**The C3 chain is CONFIRMED as a mechanism and NOT firing as a cost event.**

- **Chain intact, and now same-day observable.** Heat episode → demand +25% in 3 days (126,711 MW 7/12 → 159,046 MW 7/15) → RTO-wide capacity-emergency alert (EEA-1, active all 7/16) + 5 local load-relief warnings (DOM ×2, BGE/PECO, BGE/PPL, DPL) → LMP $410.55. Every stage dated and sourced. **This is the first time WATT has watched the full C3 chain fire in real time** — the 7/1–7/3 episode was only reconstructed ~2 weeks later off the biweekly EIA proxy. Leg 5 (official DM2 LMP, wired by PROME today) is what closed that blind spot; it earned its keep on day one.
- **But it does NOT reach cost.** The price event is a **~4-hour intraday spike that retraced the same session** ($410.55 @11:30 → $90.08 @14:55 EPT). Against an industrial retail backdrop of **8.66¢/kWh** [EIA, 2026-04, ~2mo lag], a few hours at $410/MWh on a ~$60–90/MWh baseline is a rounding error in a monthly bill. **P1 spikes are not the cost channel.** The cost channel is **P2** — capacity cleared at cap ($329.17 for 26/27, $333.44 for 27/28) — which pass-throughs on an *annual* cadence, not a heat-day cadence.
- **Therefore, for HENRY's AI-capex FCF input:** today's event changes the **power-cost line item by ~nothing**. What it changes is the **reliability/curtailment risk** attached to data-center load — which is where the 7/3 §202(c) precedent (PJM can curtail ≥50 MW data centers) actually bites. **The FCF-relevant read is unchanged; the curtailment-risk read strengthens.**
- **Spark spread (P4) confirms, doesn't compress:** **+$52.18/MWh** (power $72.38 deliv 7/08 vs Henry Hub $2.886, 7/16; HR 7.0 = EIA benchmark) [power_watch leg 4]. Heat stress **widens** the spread — gas is the marginal price-setter and captures the scarcity rent. No compression signal. *(Vintage mismatch flagged by the instrument: power leg 7/08 vs gas leg 7/16 — biweekly file lag; not a same-day spread.)*

## SCORING

**P1: 3 → 4** ("active"). Justified by: first WATT-observed live emergency-class posting; RTO-wide; active for the full 7/16 operating day; second emergency episode in 14 days. **Explicitly NOT 5** — the pre-registered upgrade trigger is "EEA2+ **OR** RT LMP >$1,000 sustained 2+ intervals," and neither is met. The band label reads "active *and escalating*"; honesty requires noting the *within-episode* direction is **easing** (demand rolled over 7/15→7/16, price retraced same-day). The "escalating" half is carried by **episode frequency** (2 in 14 days at ~160 GW), not by today's intra-episode direction. **Composite 12/20 → 13/20.**

**Agent status color: 🟠 (unchanged).** Note the precedent: P2 has scored 4 🔴 since 7/10 while agent status stayed 🟠 — channel score ≠ agent status. No deploy-posture change.

## ROUTED

| To | What | Priority | Why |
|---|---|---|---|
| **AEOLUS** | C3 confirmed as mechanism, not firing as cost; full chain dated; reconcile the demand figure to WATT's | 🟠 | C3 price-confirmation is AEOLUS's standing ask |
| **HENRY** | FCF power-cost input **unchanged**; curtailment-risk read **strengthens**; the 1-year-early demand finding (HEN-36 coupling) | 🟠 | HENRY owns the AI-capex FCF node |
| **VULCAN / CARL / REGINALD** | via `NEXUS_BRIEF.md` — no new domain news for them this session (P2 pass-through unchanged, P3 unchanged pending VULCAN-06) | curated | outbox is 🔴-crisis-only; this isn't a crisis |

Outbox stays empty by protocol (`CLAUDE.md`: "Outbox = crisis-only (🔴 async); NEXUS_BRIEF = curated sync every closeout"). 🟠 does not earn a fleet push.

## FLAGGED FOR WILL (WATT does not decide these)

1. **No deploy-posture change is being proposed.** 🟠 holds; nothing here changes position sizing or timing. Stated explicitly so silence isn't read as a soft escalation.
2. **The 7/3 EEA2 is INHERITED, NOT WATT-VERIFIED** (KB-AEO-018, from HENRY's provisional tenure). It is load-bearing — it's the n=1 anchor for WATT-02's recurrence case, the §202(c) precedent, *and* the "Episode A was worse" comparison that this adjudication rests on. Per root rule #3 (agent data can be hallucinated), **this should be verified against a PJM primary before it carries any trade.** WATT did not verify it this session (PJM's board only retains ~15 recent postings; it needs an archive/FOIA-grade pull). **Recommend PROME task this** — it is cheap and it under-props three separate conclusions.
3. **PJM API rate limit respected:** non-member tier = 6 calls/min; this session spent **1** DM2 call (the instrument's own). No ad hoc LMP pulls, no looping.

## NEW PREDICTION REGISTERED

**WATT-06** (P1, PROVISIONAL, resolve **2026-08-15**): ≥1 **additional** PJM-RTO emergency-class posting (**EEA-1 or higher**) with an effective date between 2026-07-17 and 2026-08-15.
- *Criteria:* a Max Gen Emergency / Load Management Alert (EEA-1) or above, PJM-RTO region, on emergencyprocedures.pjm.com.
- *If falsified:* two episodes clustered in one July = heat-clustered, **not** a structural cadence → P1 stays thermometer-not-mechanism; −conf on the "reserve margin is chronically tight" read; P1 re-scores 4 → 3.
- *Why it's the right test:* WATT-02 tests **severity** (EEA2+ by 9/7). WATT-06 tests **cadence** at a lower severity bar. Cadence is what discriminates "hot summer" from "structurally short grid" — and cadence is the thing the new same-day leg-5 instrument can now actually measure.
- *Independence caveat:* WATT-06 and WATT-02 share a **summer-heat antecedent** — they are not independent confirmations. Count the shared root once.

## BOTTOM LINE

PJM issued its first RTO-wide capacity-emergency alert of WATT's tenure (EEA-1, active all of 7/16) and the newly-wired official-LMP leg caught a $410.55 intraday spike same-day — a real escalation, and a clean first live test of the C3 chain. **It does not make WATT 🔴:** the episode is milder than the 7/1–7/3 one on demand, posting severity, and price, and it is already rolling over. **The signal worth keeping is structural, not acute** — PJM is hitting its own 2027-forecast summer peak in July 2026 and calling emergencies to do it, which is a P2/P3 story, not a P1 spike story. P1 3→4, composite 13/20, status **🟠 holds**.
