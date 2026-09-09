# BRENT Predictions — Calibration Archive

Full post-mortems for **closed** predictions (CONFIRMED + FAILED + NOT-FIRED-PRECONDITION + RESOLVED-special + PARTIAL + RETIRED). Reference-only — NOT loaded at boot. The live record (date, confidence, status, outcome, one-line lesson) stays in [`PREDICTIONS.tsv`](PREDICTIONS.tsv); the one-line calibration warnings live in that file's scoreboard preamble. This file holds the blow-by-blow that would otherwise bloat the per-row `Notes` column.

Created 2026-06-01 as part of the SAM-aligned predictions architecture (Tier 1 rehab). Each section = one Pred_ID, ordered by ID.

Excluded from calibration math: RETIRED-OUT-OF-LANE (BRT-18) and NOT-FIRED-PRECONDITION (BRT-20, BRT-25) — these are non-resolutions, not hits or misses.

---

## BRT-01

**Brent reaches $100 before Hormuz reopens** | made 2026-03-06 | conf 65% | Q1-Q2 2026 | CONFIRMED 2026-04-17 | TRUE

Resolved Apr 17 on Iran FM "Hormuz completely open" declaration. Brent futures crossed $100 by mid-March (BRT-14 resolved Apr 16), peaked ~$110 Apr 7, Dated Brent ATH $144.42 Apr 7. Whether the Apr 17 declaration counts as true reopening (physical transits still restricted per Lloyd's Apr 16, US blockade intact) or only rhetorical, the temporal ordering is satisfied: price hit $100 weeks before any reopening event.

Seeded from HAWK. Kuwait/Iraq shutdown made $100 a near-certainty per storage math. Calibration: 65% on TRUE was well-calibrated for a chokepoint-geometry call; the storage model held without forced revision. Invalidation condition (Hormuz reopens with Brent <$95) definitively not met.

---

## BRT-02

**Kuwait forced full curtailment within 14 days** | made 2026-03-06 | conf 85% (upgraded from 70%) | By Mar 20 | CONFIRMED 2026-04-16 | TRUE

Resolved on audit Apr 16: STATUS supply-disruption snapshot confirmed Kuwait ~2.58M bpd curtailed, tank tops reached, full shutdown. Hormuz did not reopen, no overland export. Storage model held.

Day-by-day GULF_STORAGE_CRISIS_MAR8 model: 51.60M bbl effective capacity, 2.58 mbpd fill rate, Mar 20 = tank tops. Exact match. Calibration: 85% on TRUE was well-calibrated (upgraded from 70% original); the storage-math model was high-conviction for a reason. Invalidation condition not met.

---

## BRT-03

**UAE curtailment within 25 days** | made 2026-03-06 | conf 80% (upgraded from 60%) | By Mar 31 | CONFIRMED 2026-04-16 | TRUE

Resolved on audit Apr 16: UAE ~1.6M bpd (>50% cut), Fujairah suspended per STATUS. Hormuz did not reopen, no overland export. Storage model held.

Day-by-day model: 59.21M bbl buffer, 1.91 mbpd net build, Mar 31 = tank tops. Fujairah fully disabled accelerated the timeline. Calibration: 80% on TRUE was well-calibrated (upgraded from 60%); Fujairah disabling was the operational hinge.

---

## BRT-04

**US shale production does NOT meaningfully respond (<200K bpd increase) in Q1** | made 2026-03-06 | conf 95% (upgraded from 93% per SIG-009 Apr 16) | Q1 2026 | CONFIRMED 2026-05-31 | TRUE (Q1 window)

THRESHOLD-vs-MECHANISM split.

**LETTER (Q1 window): CONFIRMED.** Q1 closed Mar 31 with no meaningful shale response. Rigs ~545 total / ~410 oil flat-to-down through Q1; trough 407 came post-Q1 in Apr; DUC flat; no Q1 capex adds. The <200K bpd Q1 condition held.

**MECHANISM (forward shale-non-response thesis): WEAKENING.** Post-Q1 rig count climbed 407 trough → 429 (May 29, +22, 7 consecutive weekly gains, >RED-19's 415 upper bound = RED-19 FALSIFIED); FANG + ConocoPhillips broke capex discipline May 4.

Forward shale-response tracking continues in **BRT-26** + THESIS v3.0 risk factors. Resolved CONFIRMED for the Q1 window on 2026-05-31 to avoid a past-dated prediction staying artificially OPEN. The ongoing thesis (downgraded ~60% in STATUS/THESIS) lives in BRT-26. RED-19 falsification confirms the downgrade direction was correct. Calibration: 95% on TRUE for the Q1 window was well-calibrated.

**Lesson:** when a prediction has a hard-dated window AND a forward thesis dimension, resolve the window cleanly and spin off the forward thesis into a new prediction. Avoids past-dated rows sitting artificially OPEN.

---

## BRT-05

**Phase 2 (demand destruction visible in data) does not begin before Q2** | made 2026-03-06 | conf 85% | Q2 2026 | CONFIRMED 2026-04-16 | TRUE

Resolved on audit Apr 16: Q1 closed Mar 31. Per TRACKER, 0/3 Path B triggers fired. EIA gasoline demand Apr 3 was +0.8% YoY (far from -5%). Phase 2 not visible in Q1 data.

Research backing: 20-24 week minimum to -5% YoY even in the 1990 recession; 2026 demand MORE inelastic → timeline stretches.

**NOTE (May 31):** Phase 2 ultimately arrived in Q2 via the SUPPLY-RELIEF / diplomatic channel (MOU pricing, Brent -21% from peak), NOT via demand destruction — Path B still only 1/3. Prediction held; the channel of Phase 2 arrival differed from the mechanism this prediction tested. Calibration: 85% on TRUE was well-calibrated.

**Lesson:** the prediction was about timing (not-before-Q2); the mechanism (demand destruction) wasn't the only Phase 2 channel. Right call for arguably the wrong reason — accept the win but note the channel attribution.

---

## BRT-06

**STNG/TNP benefit from rerouting (ton-mile increase) — tanker rates rise 20%+** | made 2026-02-18 | conf 55% | Q1-Q2 2026 | CONFIRMED 2026-03-04 | TRUE

VLCC WS400+ ($423K/day) confirmed Mar 4. LR2 +169.9%. MR +63.6%. WS400 = roughly 2,000%+ above WS20 baseline, massively exceeds 20% threshold. STNG at $80+, +5.2% from entry.

Migrated from HAWK. War drove tanker rates to ALL-TIME HIGHS — prediction confirmed by orders of magnitude beyond original 20% target. Calibration: 55% on TRUE was conservative in hindsight; could have been 75-80% given the chokepoint geometry. (Invalidation field backfilled 2026-05-31 — original row was missing it.)

**Lesson:** when migrating a prediction from another agent (HAWK→BRENT), apply own-agent confidence calibration rather than inheriting; HAWK was conservative on tanker rates and the 55% migrated forward when BRENT's storage/chokepoint math supported much higher conviction.

---

## BRT-10

**Cheniere Q1 2026 EPS significantly exceeds Wall Street consensus of $3.15** | made 2026-03-06 | conf 78% | Q1 2026 earnings (late April) | CONFIRMED 2026-05-31 | TRUE (adjusted basis)

Cheniere (LNG) Q1 2026 (reported ~May 7): ADJUSTED EPS $4.77 vs consensus $3.91 (+22% beat) — clears both the $3.91 risen-consensus and the original $3.15 bogey. Revenue $5.87B (+8% YoY, beat). RECORD LNG loaded 688 TBtu (+13% YoY) + record 187 cargoes (+11%). FY26 Adj EBITDA guide raised to $7.25-7.75B (+$500M midpoint).

**CAVEAT:** GAAP EPS was -$16.65 (miss) due to non-cash unrealized derivative/IPM marks. The operational thesis (spot-cargo premium) was correct; resolve on adjusted basis.

Spot-cargo premium thesis ($10+ above pre-war JKM) confirmed; consensus had not modeled the spot rally. Calibration: 78% on TRUE was well-calibrated; prediction beat the bogey by ~$1.62 on adjusted basis.

**Lesson:** for earnings-driven predictions, specify GAAP vs adjusted upfront. A row with mixed GAAP-miss / adjusted-beat is otherwise ambiguous and the resolution choice (here: adjusted) carries weight.

---

## BRT-11

**HY Energy OAS remains below 400 bps through Q1 2026 (no credit stress Phase 1)** | made 2026-03-06 | conf 88% | Q1-Q2 2026 | CONFIRMED 2026-05-31 | TRUE (Q1 window)

HY Energy OAS held ~285-300bps throughout Q1 and into late April (2.85% / 285bps Apr 28 [CONF]) — well below the 400bps stress threshold for the entire Q1 window. No E&P credit stress catalyst fired during Phase 1 price strength, exactly as predicted (E&P FCF windfall at $90+ oil).

FORWARD WATCH: oil -20% on the month may start to widen energy-specific OAS in Q2-Q3 — that is **BRT-12** territory, not BRT-11.

Resolved CONFIRMED 2026-05-31 for the Q1 window. OAS stale since Apr 28; LIQUID owns the live read. Calibration: 88% on TRUE was well-calibrated for the Q1 window.

**Lesson:** high-FCF environments (E&P at $90+ oil) suppress upstream credit stress reliably — this is a structural call, not a market-timing call, and the 88% reflected that correctly.

---

## BRT-13

**US retail gasoline reaches $4.00/gallon if Brent sustains above $95** | made 2026-03-06 | conf 70% | April 2026 | CONFIRMED 2026-04-16 | TRUE

Resolved on audit Apr 16: AAA retail US avg $4.108/gal (Apr 15). Has been >$4 for ~2 weeks. Brent sustained >$95 since late March. Breakpoint breached.

Econometric model: $95 Brent + $32 crack = $3.89/gallon late March. $4.00 = demand destruction trigger per behavioral economics.

**MAY 31 UPDATE:** gas peaked ~$4.483 (AAA May 6) / $4.459 (May 27); pass-through lag means Brent -20% should ease pump prices May 31-Jun 14. Confirmed and now peaking/easing. Calibration: 70% on TRUE was well-calibrated.

**Lesson:** crude→pump pass-through models are reliable on the 2-4 week lag; this is the same structural class as BRT-11 (mechanical transmission) and warrants 70-85% confidence on direction.

---

## BRT-14

**30 days of 90%+ Hormuz closure makes Brent $100 near-inevitable** | made 2026-03-06 | conf 80% | By ~Mar 28 (if closure continues) | CONFIRMED 2026-04-16 | TRUE

Resolved on audit Apr 16: Brent futures crossed $100 (peaked ~$110 on Apr 7 pre-ceasefire). Dated Brent hit ATH >$144 midweek Apr 11-14. Blockade Apr 13 pushed futures back to ~$100. No SPR release prevented — SPR down only 4.1M to 409.2M. Hormuz did not reopen before day 30.

Storage math held. $100 became baseline through April. Calibration: 80% on TRUE was well-calibrated.

**Lesson:** chokepoint-duration thresholds (X days of Y% closure) are mechanically reliable when storage math is binding. Companion to BRT-01 — same mechanism, different framing.

---

## BRT-15

**STNG exit trigger fires on naval escort/ceasefire announcement, NOT on physical Hormuz reopening** | made 2026-03-06 | conf 90% | Within days of escort/ceasefire news | FAILED 2026-06-20 | FALSE

**Pre-registered numeric conditional (Jun 12, advisor-verified):** HARDENING = a named Iranian official confirms the framework AND a signing event occurs; WINDOW N = 3 trading days from signing; MAGNITUDE X = STNG −10% cumulative close-to-close from the last pre-signing close. Hardened signing + STNG −10% within 3td → CONFIRMED; hardened + decline <10% → FAILED; no hardening → stays OPEN.

**Resolution (Jun 20):** The hardening gate TRIPPED — the "Islamabad MOU" was signed Jun 17 (Pezeshkian co-signed; Khamenei written assent Jun 18). Over the 3-trading-day window STNG **ROSE** — closed $80.58 Jun 18 (+3.25% day / **+5.79% week**, near its 52-wk high), driven by a Jun-18 Q2-2026 TCE update (LR2 ~$80K/day). STNG went UP, nowhere near the −10% test → **FAILED.**

**Why it failed — the lesson:** the prediction encoded the naive "Hormuz reopens → war-risk premium unwinds → tanker equity collapses" prior. That was wrong on two counts: (1) the reopening is bullish for **ton-mile demand** (vessels resume transiting; product flows normalize) — STNG was treated as a *normalization beneficiary*, not a war-premium casualty; (2) realized product-tanker earnings stayed very strong through the de-escalation. **"A chokepoint reopens" is NOT uniformly bearish for the freight that services it.** It also doubles as the LESSONS #18 sanity check — tankers failing to sell off on an "operational" announcement is itself evidence the market isn't treating the reopening as physically real (the Apr-17 false-dawn fingerprint; here the strait was 0-of-4 operational legs).

**Calibration:** 90% conf on the wrong-direction mechanism = over-confident on a single-mechanism tanker call. The earlier 3-channel reframe (ton-mile-on-return / war-risk / barnacle-clean-fleet-premium, Jun 1) actually anticipated the offsetting forces but the numeric conditional was still written as a one-way short. Anchor: when a position can pay via multiple competing channels, don't write a one-directional threshold.

**Cross-ref:** THESIS v4.0 (Jun 20 phase transition); LESSONS #11/#16/#18.

---

## BRT-18

**Iran faces acute civilian food stress within 45 days from grain/corn import disruption** | made 2026-03-07 | conf 70% | By mid-April 2026 | RETIRED-OUT-OF-LANE 2026-06-01 | (not a resolution — domain mismatch)

**JUN 1 RETIREMENT (per Will):** Formally retired from BRENT prediction book — Iran civilian/food-stress signal sits in HAWK's domain, not BRENT's (oil/energy). BRENT is not the right agent to evaluate civilian-stress mechanism.

Audit Apr 16: timeline hit (Day 45+) with no confirmable acute-stress reporting; Apr 13 blockade re-sealed maritime imports. Beyond that, BRENT lacks the proper data sources (Iran-internal economic/humanitarian reporting, OFAC waivers, NGO assessments).

If HAWK wants to re-spawn equivalent prediction in HAWK's book it remains worth tracking; from BRENT's perspective, retire. **Excluded from BRENT calibration calculations** — retirement is not a resolution outcome, and counting it as either TRUE or FALSE would distort the scoreboard.

**Lesson:** predictions assigned to the wrong domain agent become non-resolvable. Surface domain-mismatch early in the prediction's life rather than letting it sit PENDING for 6+ weeks.

---

## BRT-19

**US munitions constraints force operational shift within 30-60 days: either (a) launch escort ops to end confrontation, (b) escalate to accelerate Iranian capitulation, or (c) begin back-channel pressure on Israel** | made 2026-03-07 | conf 65% | By early April 2026 | PARTIAL 2026-04-16 | OUTCOME-CORRECT / MECHANISM-UNVERIFIED

Apr 8 two-week ceasefire + Apr 13 naval blockade both fit the predicted policy-shift band (the (a) escort/de-escalation AND (b) escalation arcs). Operational shift occurred in the predicted window.

**However:** original mechanism (munitions scarcity as driver) NOT publicly attributed — shift appears driven by talks-failure + political calculus. Direction correct, causal attribution unproven.

HAWK owns causal attribution. Calibration: 65% on TRUE — the directional call was right; the mechanism leg is unresolvable from BRENT's surface. Marked PARTIAL to honestly capture the split (outcome predicted ≠ outcome explained by predicted mechanism).

**Lesson:** when a prediction couples an outcome with a causal mechanism, the outcome can fire on a different cause — that is not full confirmation. Mark PARTIAL rather than CONFIRMED. Companion to BRT-23 (where the same split led to FAILED instead of PARTIAL).

---

## BRT-20

**Even at 50% Hormuz reopening, UAE curtailment extends only to ~April 25 (not averted)** | made 2026-03-07 | conf 75% | April 2026 | NOT-FIRED-PRECONDITION 2026-04-25 | (conditional never armed)

Precondition never satisfied — Hormuz never reopened at any level (50% or otherwise) by Apr 25 deadline.

DEADLINE WINDOW APR 23-25: Hormuz never reopened — Iran ship attacks Apr 22-23, dual blockade persistent, P&I unresumed. UAE curtailment continues per Phase-1 thesis.

Conditional IF-clause not met, so prediction is structurally non-firing rather than confirmed/invalidated. Storage math intact for future reactivation if 50% reopening ever occurs: UAE net build drops to 0.955 mbpd at 50% flow.

**Excluded from calibration** — NOT-FIRED-PRECONDITION cases don't reflect calibration since the predicted scenario never set up. The pre-conditional analysis (UAE storage math) was sound; the bet just never had a chance to fire.

**Lesson:** conditional predictions need explicit handling for "conditional never armed" — different from FAILED (where the condition fired and the prediction missed). Status nomenclature distinction adopted Jun 1 2026.

---

## BRT-22

**Dar es Salaam sulphur spot exceeds $800/t FCA within 30 days if Hormuz closure continues** | made 2026-03-07 | conf 75% | By Apr 7 2026 | RESOLVED — MECHANISM-CONFIRMED / THRESHOLD-UNTESTABLE 2026-06-01 | TRUE (mechanism) / UNTESTABLE (threshold)

**Mechanism dimension — CONFIRMED.** Sulphur-cost transmission is firing on every available signal: Middle East FOB sulphur +207% to $531.50/t (Argus, Jan 29 2026, pre-intensification); Ras Laffan loadings -55% Feb; war-risk premium adds $15-25/MT to delivered cost; global prices "near or above record levels" through the disruption (Argus/S&P/WEF). ME accounts for ~50% of seaborne sulphur trade. The substantive thesis claim (sulphur cost squeezes through to industrial buyers) is intact.

**Threshold dimension — UNTESTABLE.** The specific $800/t FCA Dar es Salaam price print requires Argus terminal access that BRENT does not have. Apr 7 deadline passed without confirming/falsifying the threshold from publicly available data.

**Resolution choice (per Will, 2026-06-01):** Split resolution rather than holding the whole prediction PENDING indefinitely on an untestable threshold. Mechanism dimension is the substantive question; threshold was the falsifiability handle BRENT couldn't observe. Per [[finding_threshold_vs_mechanism]] discipline — when a prediction is testable on one dimension and untestable on another, resolve the testable dimension cleanly rather than smearing the resolution across both.

**Lesson:** when proposing a prediction, separate the mechanism claim (substantive) from the threshold-handle (operational). If the threshold needs paid-data access BRENT doesn't have, either (a) use a free-data threshold proxy, or (b) phrase the prediction as mechanism-only with confidence calibrated to mechanism-confidence not threshold-confidence. Mirror of SAM-25 (TRUE-in-letter / FALSE-in-spirit).

---

## BRT-23

**At least one major DRC SX-EW copper/cobalt operator announces force majeure or significant curtailment within 60 days of Hormuz closure persisting** | made 2026-03-07 | conf 70% | By May 2026 | FAILED 2026-05-31 | TRUE (in letter) / FALSE (mechanism falsified)

**Outcome-vs-mechanism split — outcome occurred via CONFOUND, predicted mechanism FALSIFIED.**

A force majeure DID occur — Glencore declared FM on cobalt supply contracts; DRC cobalt output -39% Y/Y Q1 to 5,800t; copper-first pivot. **BUT** it was driven by the DRC's Feb cobalt EXPORT BAN / 96,600t annual QUOTAS, NOT by sulphur feedstock cost making SX-EW uneconomic.

**Confirming evidence the mechanism is wrong:** cobalt prices are UP ~160% (to ~$57,320/t) on POLICY-driven scarcity — the OPPOSITE of the cost-squeeze/demand-destruction the prediction modeled. The sulphur-cost → SX-EW-uneconomic → FM transmission this prediction tested did not drive the FM.

**Failure mode:** the prediction headline (FM in DRC SX-EW) was technically true in letter but masked by a confounded cause (export policy, not Hormuz sulphur). BRT-22 shows the sulphur-cost channel IS firing on price — but DRC FM was policy-driven, so this specific causal claim does not resolve CONFIRMED.

**Lesson — industrial-transmission failure pattern (cluster with BRT-24):** when a prediction couples an industrial outcome with a specific upstream causal chain, the outcome can fire via a different mechanism (policy, alt-sourcing, mitigation). Mark FAILED rather than CONFIRMED on TRUE-in-letter / FALSE-in-mechanism splits where the predicted mechanism is falsified. Future industrial-transmission predictions need (a) explicit mechanism attribution language ("via X, not Y"), (b) wider confidence bands at 50-60% not 70%, (c) explicit prob-weight of alternative causal paths.

---

## BRT-24

**Taiwan initiates formal industrial power rationing (Stage 2+ load shedding) if Hormuz closure exceeds 30 days** | made 2026-03-07 | conf 65% | By late April 2026 | FAILED 2026-05-31 | FALSE

Window resolved AGAINST. Taiwan Minister of Economic Affairs stated "no power rationing required" (Mar 4); no Stage 2+ load shedding occurred by the late-April deadline.

Taiwan covered the gap via spot LNG + Australian term contracts (secured through Sept) + RECORD US LNG (700K t April, largest month ever, up from 200K t March). Lost all Qatar/UAE cargoes (Apr-May) but avoided rationing. Buffer narrow (~11 days LNG reserve early May).

**Failure mode:** mitigation channel underweighted. The prediction assumed Hormuz >30d closure → industrial rationing as a near-mechanical chain. Reality: Taiwan had alt-sourcing options (US LNG, Australian term, Pacific basin spot) that absorbed the supply shock without rationing. The invalidation condition (sourced spot LNG) is essentially what happened.

**FORWARD RISK REMAINS:** if lost Gulf cargoes not replaced, Taiwan could lose >2 TWh/month (~10% demand) forcing "uncomfortable choices" during the Jun-Sept seasonal demand rise. Forward summer risk is real but outside this prediction's window — track separately if it re-arms.

**Lesson — industrial-transmission failure pattern (cluster with BRT-23):** mitigation channels (alt-sourcing, substitution, inventory buffer) must be explicitly prob-weighted in any industrial-outcome prediction. Calibration: 65% on TRUE was too high; should have been 35-45% given the documented alt-sourcing pathways (US LNG capacity, Australian term flexibility). Same pattern lesson as BRT-23: future industrial-transmission predictions need wider confidence bands + explicit mitigation prob-weighting.

---

## BRT-25

**TSMC issues earnings guidance warning citing "grid reliability" or "power supply" as a risk factor in Q1 2026 results if Taiwan experiences grid events** | made 2026-03-07 | conf 55% | Q1 2026 earnings (April 2026) | NOT-FIRED-PRECONDITION 2026-05-31 | (conditioning grid-event never armed)

Window resolved AGAINST. TSMC Q1 2026 (reported ~Apr 14): RECORD quarter — revenue $35.9B (+6.4% QoQ, beat), GM 66.2%, RAISED FY26 revenue-growth guide to >30% YoY, guided Q2 $39.0-40.2B (+10% QoQ).

Energy/war supply-chain risk was discussed as backdrop commentary ("works closely with Taipower to ensure stable supply"; helium prices doubled), but TSMC did NOT issue a guidance WARNING flagging grid reliability / power supply as a guidance-degrading risk factor — it raised guidance.

**No Taiwan grid events (BRT-24 FAILED — Taiwan avoided rationing entirely), so the conditional trigger never armed.**

Prediction was a disclosure-signal bet; the conditioning grid-event (BRT-24) didn't occur, so BRT-25 is structurally NOT-FIRED-PRECONDITION rather than FAILED. Energy was mentioned in TSMC commentary, but not as a guidance risk warning.

**Excluded from calibration** — conditional never armed.

**Lesson — nested-conditional risk:** BRT-25 was nested on BRT-24 firing. When BRT-24 failed, BRT-25 was structurally precluded from firing. Nested conditionals compound failure risk — should have been written as a standalone (e.g., "TSMC mentions Hormuz / energy supply in Q1 commentary as material risk") rather than gated on a prior prediction that itself was speculative.

---

## BRT-27 — Brent price-consequence conditional on HAW-09 (Iran re-engagement)

**Resolved CONFIRMED 2026-06-13** (conf 55%, made 2026-06-08; price-side met Jun 12, HAW-09 adjudicated CONFIRMED by HAWK Jun 13).

**Prediction (Jun 8 scope-narrowed form):** PRICE-CONSEQUENCE conditional on HAW-09 — Brent retreats to <$92 (front-month) within 5 trading days of HAW-09 partial-or-full confirm (Iran re-engages Pakistan-mediated talks by Jun 15); OR Brent holds $94-100 through Jun 17 if HAW-09 falsifies.

**Outcome:** Confirm-branch. HAW-09 CONFIRMED Jun 13 (Iran re-engaged Pakistan/Qatar channel + Sharif "final agreed text" Jun 12). Brent closed <$92 across the window: Jun 9 $91.45, Jun 10 $93.10, Jun 11 $90.38, Jun 12 $87.20 (first sub-$88 of cycle).

**Lead/lag nuance (honest grading):** The price moved *ahead of* the formal HAW-09 adjudication, not after it. Kinetic-premium decompression ran Jun 8-12 on the broader de-escalation process (Iran-Israel mutual halt Jun 8 PM + dawn-#5 Trump settlement announcement Jun 11 PM); HAW-09 was only formally adjudicated CONFIRMED Jun 13. So the *mechanism* (re-engagement process ⇒ kinetic-premium decompression ⇒ Brent <$92) is confirmed, but the literal "price follows confirm within 5 td" temporal ordering was loose — price anticipated. Sibling of [[finding_threshold_vs_mechanism]] / [[finding_catalyst_path_decoupling]].

**Read-as caveat:** channel-resumed, NOT deal-done. HAWK B-Reopen 32% with resolution bar still pinned to *verified* reopening (traffic recovery); HAW-09 CONFIRMED is the announcement leg only (LESSONS #18 announcement≠barrels). Signature unexecuted, venue wobbling (Geneva vs Vienna) as of resolution.

**Full pre-resolution note (carried from PREDICTIONS.tsv at resolution):**
> JUN 8 SCOPE-NARROW: Restructured from event-shaped to price-consequence per HAWK Jun 8 ask + "one source of truth per metric" — HAWK canonical event call is HAW-09 (conf 35%); BRENT owns the price-side. Date_made bumped to 2026-06-08. Calibration delta resolved: BRENT had been carrying conf 65% on the event (Trump "deal next week" rhetoric overweighted, `[[feedback_trump_rhetoric_tape_not_info]]`) vs HAWK 35%; deferred to HAW-09's 35% for event prob. The 55% conf here is on the CONDITIONAL price reaction given HAW-09 resolves either way (high-confidence price path; the conditional itself rides HAW-09's 35% event prob). Cross-ref: HAW-09; FLOW-HAWK-19 (decoupling regime). PRE-JUN-8 EVENT-SHAPED HISTORY → see PREDICTIONS_ARCHIVE.md#BRT-27 (Jun 1 origin + Jun 7 partial-confirm trend). JUN 12 UPDATE: **PRICE-SIDE MET / HAW-09 PENDING.** Brent closes <$92: Jun 9 $91.45, Jun 11 $90.38 [CONF Yahoo daily closes Jun 12; advisor independent pull exact match]. HAWK book STALE for adjudication (Last Updated Jun 8 09:15 EDT — predates Jun 8 PM Iran-Israel halt AND Jun 11 PM Trump settlement announcement; HAW-09 conf 35% / B-Reopen 12% are pre-event marks). Resolution BLOCKED on HAW-09 adjudication — HAWK spawn decision escalated to Will (advisor verify Jun 12). Do NOT self-grade Iran-re-engagement off news headlines.
