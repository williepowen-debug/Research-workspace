# BRENT — position review, harvest and persistence

Reconciled 2026-09-08 under Will’s approved BRENT cleanup. Supersedes: the corresponding rule containers in TRADE.md; no capital authority, levels or discretionary permission added. Binding excerpts below are preserved verbatim; dated examples retain their original dates. Full provenance and superseded wording: [before-image](../archive/2026-09-08_cleanup/TRADE.md). [Inventory](../workbook/TRADE_OBLIGATIONS.md).

Read this whole file BEFORE every BRENT position review, holding/exit recommendation or proposal. First read current holdings and pending receipts in [TRADE.md](../TRADE.md). Specific Will-approved rules for existing holdings take precedence over generic playbook mechanics. The following off-ramp harvest rules govern an off-ramp position, not the existing long-call holdings.

## BH-01 — Harvest precedence

**All three are hard rules, not guidance. Whichever fires first, governs.**


## BH-02 — H1 announcement clock

| **H1** | **HARD TIME STOP — exit in full no later than day+9, MEASURED FROM THE ANNOUNCEMENT (not from entry). ⚑ ANCHOR RULED BY WILL 2026-07-31.** *(Was "8 trading sessions after entry" — retired as a dated record: with half/half sizing that literal reading gave two entries two clocks and stretched maximum position life to day+10.)* | Trough was at **7 sessions after entry**; a stop at 8 captured **−7.8% of the −8.1% maximum = 96% of the available move.** |
> **⚑ WHY ANNOUNCEMENT-ANCHORED, and the consequence that must not be rediscovered as a defect: the two tranches get UNEQUAL holding periods — tranche 1 (day 0) has 9 sessions, tranche 2 (day+2) has 7. That is INTENDED.** The later tranche is an **add to a position Leg C has already confirmed**, and the anchor exists because **the MOVE is on a clock, not the FILL.** The n=1 evidence supports it: the historical case **troughed ~day 9 and had fully round-tripped by day 20**, so reversal risk attaches to **elapsed time since the announcement**, not to when I happened to add. **This is the tighter of the two readings** — chosen deliberately, consistent with H1 being the rule I said I would defend hardest at n=1.


## BH-03 — H2 profit harvest

| **H2** | **PROFIT TARGET — take ≥ HALF off at −7.0% on Brent from entry.** | Locks the bulk of the move at the point the historical case was near its low, without needing to call the exact bottom. |


## BH-04 — H3 reversal exit

| **H3** | **STOP — exit in FULL on any close back ABOVE the entry level.** | The round-trip has begun. In the historical case the move went from −2.4% (day 15) to **+13.1% (day 20)** — the reversal was fast and did not give a second chance. |


## BH-05 — Harvest calibration limitation

**⚠️ CALIBRATION LIMIT, ON THE RECORD: H1/H2 are calibrated on n=1** — one qualifying event in the whole sample. **H1 is the rule I would defend hardest at n=1**, because it does not try to find the top; it only refuses to hold past a known reversal zone. If it is wrong it costs upside, not capital. **H2 and H3 are more fittable and should be re-examined after any real fire.**


## BH-06 — Persistence: reconcile by leg

- `WAR-RISK-HALVES`: RETIRED August 7; no feed and no defensible anchor. Do not grade or resurrect it. Evidence: REGISTRY row of that name.
- `STAGE-A-AIS`: RETIRED August 7; the named real-time feed never existed.
- `KILL-LEG2-TRANSIT`: RETIRED by Will August 21 on instrument grounds; **premise not refuted**. Successor `KILL-LEG2-JWC-LISTING` is an asymmetric standing negative, with delisting **prompt-only**, never automatic exit. It measures underwriting appetite, not barrels. The throughput question remains unmeasured. [Ruling](../../../PROME/proposals/2026-08-21_kill-leg2-transit-respec-RULED.md).
- P&I resumption: the original 25-trading-day notice observation was not individually retired in the records inspected. It survives as an observation obligation. A notice is not proof of physical reopening.
- **UNRESOLVED applicability:** the original institutional exit joined a now-retired war-risk test to P&I. No inspected amendment explicitly rewrites that compound exit, and the old short-retention transit test has the opposite direction from the retired long-thesis falsifier. The cleanup must not silently equate them. Retain the original letters below as unresolved obligations; before a new off-ramp proposal, BRENT reconciles them with the August 21 ruling and brings only any remaining policy choice to Will. Do not turn a missing source into a pass, a failure, or a fresh automatic kill. H1/H2/H3 continue to govern a position on their own terms.

## BH-07 — Original persistence letters awaiting applicability reconciliation


| Leg | Own response time | **Window** | Observation basis |
|---|---|---|---|
| Aggregate Hormuz transits >~35/day sustained | days (hulls are queued and waiting) | **10 trading days** | real-time AIS leading; PortWatch/Lloyd's confirming (4-6d lag) |
| **War-risk premium halves** | **2-4 weeks** — underwriters require confirmed de-escalation before repricing | **25 trading days (~5 wks)** | broker quotes via Marsh/Platts/Lloyd's List |
| **P&I resumption notice** | weeks to OCCUR (risk-committee gated) — but **same-day to OBSERVE** once issued | **25 trading days** | club circular / Lloyd's List, same-day recognition |

**🔻 THE KILL TEST — this is what stops the re-spec from being a net loosening, and it is NEW (BRENT-added 7/29, flagged as an addition, vetoable):** if **NEITHER** war-risk halving **NOR** a P&I resumption notice has fired **by its own window**, the de-escalation was **not institutionally real** — the paper moved and the underwriters never agreed. **Cut the position rather than ride it**, on the same one-line [Approve/No] authority as the fill.

> ### 🔻 **KILL-TEST LEG 2 — THE TRANSIT TEST, MOVED HERE FROM STAGE-A ENTRY. WILL-RATIFIED 2026-07-31.**
> **If aggregate Hormuz transits have NOT reached >~35/day on ≥2 consecutive days within 10 TRADING DAYS of the announcement, the de-escalation was not PHYSICALLY real → CUT the position**, same one-line [Approve/No] authority.
> - **Threshold unchanged from the retired entry leg** (>~35/day, ≥2 consecutive days) — **nothing was loosened; it was re-phased.** Window = the **10 trading days** the Stage-B persistence table already carried for this exact metric.
> - **Observation basis:** real-time AIS leading; PortWatch/Lloyd's confirming (4-6 day lag).
> - **⚠️ This is now an INDEPENDENT second kill condition, not an alternative to the institutional one.** Leg 1 (war-risk / P&I) tests whether the de-escalation was **institutionally** real; Leg 2 tests whether it was **physically** real. **Either one failing is sufficient to cut.**
> - **On the Jun-17 analogue this test would have PASSED** (transits hit 51/50 on 6/24-25 = day+5, comfortably inside 10 td) — so moving it out of entry did **not** cost the one trade that worked, and it would still have policed it. *(Rationale: v1's broken window meant the slow legs never graded anything at all. Lengthening them alone would make a **short**-arming gate strictly easier to satisfy — fixing a latency bug must not quietly increase willingness to short. Converting them from dead entry-legs into a live post-entry kill test makes the net change **tighter**, not looser: v1 had no post-entry test of any kind.)*


The table and original exit letters immediately above are evidence of the unresolved obligation, not authority to reactivate retired instruments. The per-leg dispositions in BH-06 govern how they may be used today.

## BH-08 — COT sizing, current successor

The canonical frozen letter and current grade are the `COT-FUEL-35B` row in [REGISTRY.tsv](../workbook/REGISTRY.tsv). Read that complete row before sizing, plus the [registration evidence](2026-08-12_35b-COT-successor-band-N1-build.md). Raw shorts and OI-share are both gating; disagreement or deadband gives NO-VERDICT and base-case sizing. It is never an entry trigger. Frozen median unit and base do not roll with each print. No numerical size beyond the existing cap is invented here.

The old `COT-FUEL` numbers and their August 11 REVERT letter are retired as a numerical test. The successor computes its own joint state at each print; do not carry a prior SPENT grade through a current NO-VERDICT. This operational rule follows the successor’s own per-print default, not an assumed transfer of every clause attached to the old threshold. Non-claims travel: no out-of-sample test, n=0 genuine physical reopenings, no demonstrated price prediction, and each grade’s observation vintage.

## BH-09 — Exposure and conversion

BRENT reports exposure facts and independence; TERRY owns sizing. Recorded oil expressions share crude-direction exposure; line count does not establish diversification. Recompute concentration from current holdings and dated, consistent marks before quoting it. September 2 marks in the archive include two October calls before the later holding correction and are not a current sleeve valuation. Read BG-08 before translating any USO level into Brent. STNG is tracked, not held.

Historical proposed tickets and one-off colour exceptions are not standing orders. Broker inventory, orders, bid and execution receipts must be checked at the relevant decision. No recorded unknown sale price or refiner fill should be inferred or re-requested contrary to the current holdings instructions.

## BH-10 — Dated mark-monitoring rider

✅✅ **DECISION-RELEVANT MARK DELTA — RESOLVED 2026-08-27 ~11:12 ET, WILL RULED IN-SESSION VIA PROME RELAY: FILL STATUS = CONFIRMED UNFILLED, 8/21 SELL-ONE IS SUPERSEDED BY DELIBERATE OPERATOR HOLD.** Will's exact words: *"I want to wait. I do think this ride isn't over yet."* ⇒ **The 8/21 SELL-ONE ruling is now a HISTORICAL DECISION SUPERSEDED by an 8/27 HOLD ruling on the SAME leg** — read as a thesis-conviction hold, NOT a lapsed unexecuted order and NOT a re-open of the roll question. ⛔ **THE LEG NO LONGER CARRIES THE FILL-STATUS QUESTION.** ⚠️ **The concentration flag stands** — Will's HOLD is thesis-conviction WITH the concentration flag standing (per PROME relay verbatim), not a dismissal of it. **The $465/contract of harvest opportunity that degraded between Will's 8/21 ruling and today is a REAL OPPORTUNITY COST that will not be recovered on this leg unless it moves back to the 8/21 mark** — but that opportunity cost is the OWNERSHIP DECISION MADE, not an execution failure. ⛔ **Prior TRADE.md/SCRATCH/PROME framing carried "fill status unclear" — CORRECTED IN PLACE and left visible** rather than reworded, per L23-class discipline (a correction propagates cleanly when the prior claim stays visible). ★ **MARK TRACKING CONTINUES.** Material moves either direction → packet PROME per standing 8/27 arrangement (mark refresh on Fri 8/28 dual-grade session anyway; earlier if the leg moves ≥±$1.50/contract from 8/26 last-trade $5.70).


The 8/27 HOLD and two-contract context are superseded by the current position mirror. The embedded ±$1.50 mark-watch rider has no inspected explicit retirement; retain as a dated monitoring obligation, not a sale trigger or automatic outbound-send authority. Reconcile applicability at the next relevant position review using the owner card.

## BH-11 — Receipt and starter boundaries

The September spread’s original ~$300 fill remains an approximate recorded basis; no exact broker receipt was established by this cleanup. Keep any receipt question scoped to that leg and subordinate to current owner instructions. The declined pre-trigger convex starter remains declined; reopen only if Will requests it (original TRADE Decisions on Record, June 29). One-off July green-day insurance approval is not standing permission to repeat the ticket.

## BH-12 — Do not blend transit series

> ⚠️ **DO NOT CONVERT 39/week INTO 5.6/day AND COMPARE IT TO THE 88/day `n_total` BASELINE. My own `HORMUZ_TRANSIT_BASELINE.md` §1 forbids exactly this — *"never blend series."*** Lloyd's counts completed **transits** with an Iranian-linked classification; PortWatch counts **vessel observations in a chokepoint polygon**; the two disagree materially (PortWatch logs 42 over just 7/20–7/23 against Lloyd's 39 for the full seven days). **What IS valid is Lloyd's WoW ratio, because it is internal to one series — and that ratio is −52%.**


## BH-13 — Retired source exclusions

> ⛔ **REFUSED, AND NAMED SO NOBODY PROMOTES THEM LATER: `straits.live`, `hormuzstraitmonitor.com`, `hormuztracking.com`.** They return fresh-looking dated counts ("12 transits in the past 24h, 6 tankers"), **and my own 7/21 STATUS already killed this class as F6-unreliable trackers recycling stale March data.** A source I have retired does not become reliable because today I want a fresh number (`[[finding_claim_outlives_its_discredited_instrument]]` in reverse — the instrument stays discredited).


## BH-14 — AIS undercoverage caveat

> ⚠️ **THE HONEST COUNTER, AND IT CUTS AGAINST MY VERDICT — STATED FOR THAT REASON.** The region has documented **GPS jamming, AIS spoofing and vessels going dark**, and Lloyd's itself reports **shadow-fleet vessels increasingly filling the gaps left by mainstream operators.** **Every count above is therefore biased DOWN, and a real recovery led by dark transits would be partially invisible to all four sources** (`[[finding_ais_port_export_darkfleet_blind]]`). **This is the strongest available argument against my read and I cannot fully retire it.** What it does *not* explain: Lloyd's non-Iranian, mainstream-operator series fell **−27%** on its own, and that cohort is the one that would have to return for a normalization to be real.


## BH-15 — Single-outlet source restriction

> ⚠️ **SOURCE FLAG I MUST DECLARE AGAINST MY OWN CITATION: WALTER caught The National's 8/3 oil piece contradicting itself in one paragraph ("rose 5.09%" / "5.09 per cent lower") and asserting "Brent traded below its prewar $72 last month," which is FALSE against our own record — recycled June copy.** **I cite The National (7/17) as one source for the war-risk 7.5-10%-of-hull / $3-10M-per-transit figure in item (iii).** **That figure does NOT fall with this** — it is carried independently by **Marsh via S&P Global (7/22)**, **Al Jazeera (7/23)** and **Lloyd's List (LL1156586)**, and the insurance reporting is a different piece from the sloppy price piece. **But the outlet is now on notice on my surface, and if it ever becomes the SOLE claimant for a number I use, that number does not ship** (`[[finding_claim_outlives_its_discredited_instrument]]` — the claim survives on other sources; the instrument's reliability does not). ⚠️ **NOT GRADED — the verdict is the 2:30 PM ET settle**, and it gets an intraday cross-check before anything is banked (PROME's CL=F daily-low artifact 8/2; **and my own BZ=F daily bar today returned OPEN 89.38 ABOVE HIGH 84.65, internally impossible — Brent daily OHLC is unusable this session**).


BH-12–BH-15 retain the source/basis restrictions. Their prices, observations and descriptive judgments are dated August 3, not current measured facts. A later series repair requires evidence; this migration supplies none.

## BH-16 — Historical verification debt

> **FRED `OVXCLS` (CBOE's official daily-close series) matches my feed EXACTLY on every prior day it publishes: 7/27 60.62 · 7/28 57.15 · 7/29 67.59 · 7/30 63.44 · 7/31 63.04 — 5 for 5, including the 63.04 the whole gate distance was measured from.** ⚠️ **FRED has NOT yet published 8/3** (it lags a day). **So the INSTRUMENT is validated; TODAY'S VALUE is single-source.** ⇒ **Re-verify 57.20 against `OVXCLS` at next boot.** *(`[[finding_loadbearing_number_must_be_reproducible]]` — a number that governs capital gets a second witness, even retroactively.)*


The gate is retired, so BH-16 is evidence debt before reusing its old grade, not a live OVX deployment test or a request to re-grade the retired gate.

## Lesson reconciliation (2026-09-08)

L05/L22/L23/L25: use dated live instruments, actually run verification, name contracts and investigate request/identity failures; old examples above never certify current execution inputs. L11/L16/L18/L19: announcement entry, sign-blind liveness and physical retention have different roles; apply the approved paired T/C and the explicit retired-instrument limits. L15: structural 60–90 DTE and off-ramp 21–35 DTE remain distinct; holding-specific rulings take precedence. L21: no new threshold, re-arm, measurement substitute or timing relaxation is registered by this migration; joint and trigger-conditional testing is still required before a successor. L06/L08/L09/L10: no new crack, inventory, product-supplied or quota grade is made here. Those lessons remain applicable when their evidence is used; a crude premise does not prove product supply or actual OPEC delivery. No lesson is overridden by this cleanup.

L17: any spare-capacity claim reused in a proposal must be checked against physical deliverability; the dated OPEC references above do not certify current usable spare capacity.
