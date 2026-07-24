# VIOLET — NEXUS Brief

**As of:** 2026-07-23 ~18:30 ET (Will-directed session — sit-rep + pre-registration + instrument build) | **STATUS commit:** see STATUS.md footer.

> **⚡ 7/23 PM ADDENDUM (two instruments registered, both pre-catalyst):** (1) **KB-VIO-123 — crack-vs-fade branch map LOCKED** before COT 7/24 + FOMC 7/29, so both get graded against a pre-committed tree rather than a post-hoc read. Confirm side weighted: **fresh credit widening HIGHEST** (CCC past ~9.9-10.0 / disp >8.3 as a NEW escalation, not stuck-wide — my primary per KB-VIO-088), then COT persist/deepen + MOVE extend; the shared-surface legs (VVIX→120, inversion <1.0 settle, VIX>20 settle) rank MED. Fade side: VIX<18 / VVIX<100, contango rebuild, COT reversal, MOVE back through 70-72, credit un-trip, or FOMC absorbed (**the base-rate outcome — GEX-absorption has eaten every catalyst this cycle, counter 0/5**). (2) **KB-VIO-124 — cheap-tail window ALERT built** (`scripts/cheap_tail.py`, boot-wired): an *operator-decision* surface, NOT a gate — flags the complacency floor where convex tails are cheapest AHEAD of a dated event (VVIX≤90 · VIX≤16 · SKEW≥140 · catalyst ≤21d). Backtest 4.04% of history (31 episodes 2007-) = rare, not a bleed machine; would have fired 7/6-7/10, correctly **DORMANT 2/4 today**. It is the deliberate inverse of the confirmation gate — the two bracket the decision. **SKEW recomputed:** 150.19 [7/22 close], **20d-avg 146.68**, p97, **>150 sustain 2/4** toward prediction #6 re-arm — flagged NOT-yet-meaningful (7/1 arm broke 2/4, 6/5 broke 1/4; the filter has refused both). Tail firming *with* the front-end = confirming, not diverging.

> **⚡ 7/23 INTRADAY (THE 7/21 DIVERGENCE RESOLVED UP — front-end rejoined the stress):** Over 7/22-7/23 the equity-vol FRONT END that faded toward complacency Monday (VIX 17.05) re-firmed UP to rejoin the elevated tails/cross-asset: **VIX ~19.86** (+2.81, back at the 20 line), **VVIX 105.29 RE-CROSSED the >100 watch line** (from 96.34), **VIX3M/VIX 1.071 RE-COMPRESSED toward the 1.0 inversion line** (from 1.149 — Monday's re-steepening reversed), **SKEW 150.19 🔴** (held >150 through the round-trip). **Vol did NOT fade down to meet calm — calm caught up to the stress.** The INDEPENDENT stress vectors all remain firing: **MOVE ~74.67 [7/21, latest web] re-open FIRED** (68.48→70.88→72.66→74.67), **credit Bin-A** (CCC 9.77/disp 8.17 [7/20]), **OVX/VIX 3.55/p97.6 FIRE** (held through the re-firm), **COT lev-money 7/14 pct3y 99.4 extreme-long** (unchanged); JPY carry **CALM** (MOF 7/22 passed clean, USDJPY 163.82, no unwind). **Read: FOUR of five independent vectors on the stress side simultaneously = the strongest independent-confirm alignment of this de-compression, and the shared-antecedent equity-vol surface has now JOINED that stress rather than diverging from it. STILL short of a confirmed crack — the two completing legs are NOT met: term-structure has not INVERTED (1.071, needs <1.0) and VIX has not broken >20 into RISING_VOL (both close). Strengthening-candidate loading directly into FOMC 7/29 (4 td), inside a buyback blackout + the 7/29-8/1 megacap earnings cluster.** ⚠️ Surface values are intraday TICK (pre-settle); SKEW/credit T-1; COT 7/14 (next read Fri 7/24). KB-VIO-122.
>
> **⚡ 7/21 (DIVERGENCE SHARPENED — prior read, now resolved UP by 7/23):** Front-end faded (VIX 17.05, VVIX 96.34 <100, VIX3M/VIX 1.149 re-steepened) WHILE tails/cross-asset firmed (SKEW 151.66, MOVE ~74.67 EXTEND, credit Bin-A wider, OVX FIRE deepened). The rates-vol-led divergence got its first full-day test and widened — then closed the bearish way two sessions later. GATE-VIO-116 re-open FIRED 7/21 AM (MOVE 72.66 [7/20] verified, >72.41 F1). Consequence = fold-into-TRY-FIRE-004 (FILLED, 30× TLT Sep-30 77P live), NO new standalone trade.
>
> **⚡ 7/17 lineage (compressed):** de-compression off the 7/10 complacency floor (VVIX crossed 100, contango flattening) — ONE shared-antecedent surface signal; COT 2nd read GRADED DEEPENING (KB-VIO-121, pct3y 99.4 extreme-long) = positioning channel confirmed; OVX canary BUILT+FIRING (KB-VIO-120); jpy_vol canary LIVE (KB-VIO-117). Full trail: STATUS + KB-VIO-118/120/121.

**Status:** 🟠 v3.6 — **the 7/21 front-end/tail divergence resolved to the UPSIDE: the equity-vol surface re-firmed to rejoin the independent stress vectors (MOVE re-open FIRED, credit Bin-A, OVX FIRE, COT extreme-long).** As of 7/23, four of five independent vectors are on the stress side simultaneously — the strongest alignment of this de-compression — and the shared-antecedent equity-vol surface has now joined it (VIX ~20, VVIX >100, term-structure re-compressing toward inversion). What keeps it a strengthening-candidate rather than a confirmed crack: no actual term-structure inversion (1.071, needs <1.0) and no VIX break >20. Both close. FOMC 7/29 (4 td) = the catalyst path. No position; re-open consequence = fold-into-004 (FILLED), no new standalone trade (TERRY owns shape, Will approves).

**Domain:** VIX / vol term structure / SKEW / VVIX / credit-to-vol transmission timing; broadcasts vol-regime to HENRY/LIQUID/RED; receives from BROCK/HENRY/HAWK/LIQUID/SAM/BRENT.
**Early-warning layer:** `AGENTS/VIOLET/CANARY_MAP.md` v1.1 (jpy_vol + OVX Tier-1 LIVE; action-gates canonical in `PROME/GATES.tsv`).
**Thesis version:** v3.6 (unchanged — surface read + inbox processing, not a thesis event).

---

## VIEW

- **The divergence-closure direction is the story.** On 7/21 the split read as front-end-says-calm / tails-say-stress. It closed by the FRONT-END rising to meet the stress, not the tails falling to meet calm — the bearish resolution. This is the first instance in this de-compression of that closure direction; it means the equity-vol surface is no longer diverging from the independent stress but *confirming* it (with the shared-antecedent caveat that VIX/VVIX/term-structure/SKEW are one surface, not four signals).
- **Four of five independent vectors firing simultaneously** (credit 🔴, MOVE 🔴, COT 🔴, OVX 🔴; only JPY 🟢 calm) is the strongest independent alignment of the cycle — this is the fleet-relevant discriminator, not the correlated equity-vol gauges.
- **Two crack-completing legs, both close:** term-structure inversion (VIX3M/VIX <1.0; at 1.071) and a VIX>20 break (at 19.86). Either would flip the read from strengthening-candidate to confirmed. FOMC 7/29 is the obvious trigger — inside a buyback blackout and the 7/29-8/1 megacap earnings cluster.
- **Two-layer complacency frame intact + concentration stack thickening:** WALTER flow layer (Citadel 3.5× dip-buying, record option premium, 45.8% HH allocation) + SOX bear market (SIG-007) + dealer long-gamma halved (SIG-009) + $1.65T off-B/S hyperscaler debt (SIG-002) + SMCI Q4 prelim (SIG-008) = the Path-B concentration-fragility context under the vol layer, loading into megacap earnings.

---

## CALIBRATION

- **Conviction (decomposed):** direction-MEDIUM/HIGH for a developing complacency-unwind (now front-end-confirmed, not single-surface) · timing-MEDIUM (dated trigger = FOMC 7/29, 4 td; COT 7/24 mid-week) · level-LOW/MEDIUM (VIX at 19.86, at the >20 boundary but not through). No position — a strengthening-candidate with two unmet legs doesn't clear the bar, and the re-open consequence is already expressed via 004 (long TLT puts = long rates-vol/convexity).
- **Discipline this session:** the shared-antecedent rule held — the equity-vol re-firm is read as ONE surface signal rejoining the independent stress, not four fresh confirms. The 7/21 divergence read was not banked as directional; it was tracked to its resolution (which went the other way). MOVE re-verified against web before asserting the re-open state.
- **Cross-agent tensions:** **None active this cycle.** (SAM JPY-vol seam split accepted; HENRY gamma-flip is an accepted ±err free-tracker input [now STALE 5d — flagged for refresh]; WALTER SIG-002/008 are INFO, action=VULCAN, no conflict.)

---

## CROSS-DOMAIN

**SENDING:**

| To | Signal | Priority | Mechanism it triggers |
|----|--------|----------|-----------------------|
| **HENRY / RED / NEXUS** | **The 7/21 front-end/tail divergence resolved UP** — VIX ~20 + VVIX re-crossed 100 + term-structure re-compressing toward inversion = the equity-vol surface rejoined the independent stress (MOVE/credit/OVX/COT). Strengthening-candidate; missing legs = actual inversion (<1.0) + VIX>20 break, both close. Treat the equity-vol gauges as ONE surface (KB-VIO-122). | 🟠 | HENRY: pairs with the neg-gamma flip-band amplification (refresh SPX flip level, HENRY 7/16 stale). RED: adversarial check on "front-end rejoined, strengthening-candidate." |
| **BOND / NEXUS** | **MOVE re-open stays FIRED (~74.67 [7/21, latest web]);** 7/23 print not yet posted (web ~1-session lag). The rates-vol channel confirms the equity-vol re-firm. | 🟠 | Rates substance BOND's; VIOLET owns the vol-transmission read + the gate. Consequence = fold-into-004 (live), no new trade. |
| **BRENT / HAWK** | **OVX canary held FIRE through the equity-vol re-firm (KB-VIO-120):** OVX/VIX ratio 3.55 (p97.6), OVX 70.36 (p95.5) = oil-vol→equity-vol transmission channel LOADED at a near-full-history extreme. | 🟠 | You own the oil substance behind the elevated OVX; VIOLET flags the transmission channel loaded (context, not an action-gate). |
| **SAM** | jpy_vol MOF 7/22 **passed clean** (KB-VIO-117): USDJPY 163.82 weakened, no carry unwind; RV p9.8 CALM; IV/RV 2.75× event premium not yet fully collapsed. | 🟠 | Your MOF substance + VIOLET transmission gauge reconcile. Watch IV/RV collapse toward 1× (risk-passed) vs hold into FOMC/BOJ. |
| **PROME / NEXUS** | The VIX-complacency leg of "nothing has broken" now has the front-end joining the positioning asterisk — VIX at the 20 boundary + VVIX>100 + COT pct3y 99.4 extreme-long while price-of-vol only just re-firms. | 🔴 | Feeds fleet synthesis; the de-compression's strongest independent alignment yet, loading into FOMC 7/29. |

**WAITING FOR:**

| From | Input | Expected | Why it matters |
|------|-------|----------|----------------|
| CFTC (self-pull) | next COT (report-date 7/21) | Fri 7/24 3:30 | Does the DEEPENING (pct3y 99.4) persist, deepen further, or unwind? Mid-week discriminator before FOMC; grades against KB-VIO-123. |
| **HENRY** ⏳ | **Is dealer gamma SHORT into FOMC 7/29** + is SPX still at the flip band? (7/16 read STALE 7d; WALTER SIG-009 flagged long-gamma halved +16.2→+6.2bn) | **requested 7/23 via PROME** | **The pivotal input.** Short-gamma into the decision = the amplifier that turns a routine FOMC into a Path-B cascade — and the one read that would flip VIOLET from observe-and-let-004-carry to justifying a fresh non-duplicative tail add. |
| **LIQUID** ⏳ | **Is CCC/disp widening FRESH or stuck-wide at Bin-A?** (level alone can't distinguish) | **requested 7/23 via PROME** | Fresh credit widening is VIOLET's **highest-weight confirm** (KB-VIO-088 primary). A stuck-wide Bin-A is setup, not trigger. |
| VULCAN | S1 Path-B capex quantification | ahead of 7/29-8/1 megacap stack | Sets the NDX-SPX IV-dispersion canary line; now has SIG-002/008 data. |

---

## FORWARD CATALYSTS (next 2-6 weeks)

| Date | Event | Threshold / Signal |
|------|-------|---------------------|
| 🔴 Jul 24 3:30 | CFTC COT (report-date 7/21) | pct3y 99.4 extreme-long — persist / deepen / unwind? |
| 🔴 Jul 29 | FOMC (no SEP, Warsh) | The two crack legs: VIX>20 break + term-structure inversion (<1.0). Fed-HIKE regime follow-through; blackout-thinned tape. |
| 🟠 Jul 29-Aug 1 | Megacap earnings cluster | Concentration/Path-B; VULCAN S1 seam. |
| ⚪ Aug 19 | VIX August expiration | Standard monthly. |
| ⚪ Sep 16 | FOMC + SEP + VIX Sep quarterly | ~priced path. |

**Dominant near-term tail:** whether FOMC 7/29 (or its run-up) completes the crack — VIX>20 settle + term-structure inversion — or the front-end fades again (Monday's move in reverse).

---

*Brief format: NEXUS_BRIEF schema (R3 + amendment 7). VIOLET is a MEDIUM cross-domain agent. This refresh (7/23, full-session): 7/21 divergence resolved UP (front-end rejoined stress; four of five independent vectors firing; two crack legs unmet = strengthening-candidate); MOVE re-open stays FIRED; crack-vs-fade tree LOCKED pre-catalyst (KB-VIO-123); cheap-tail operator-alert BUILT + boot-wired (KB-VIO-124); SKEW 20d-avg recomputed (146.68, sustain 2/4); HENRY + LIQUID reads requested via PROME; 2 WALTER AI-capex INFO signals consumed. Cross-agent tensions: None active.*
