# SAM THESIS — v1.6 DRAFT 🚧

> **🚧 DRAFT — NOT CANONICAL.** Started 2026-06-18 PM Thu (~5:30 PM ET) under Will-directed v1.6 re-underwrite per PROME+ORC adjudication. **Finalizes post Fri Jun 19 National CPI + RED pass.** Canonical thesis remains `THESIS.md` (v1.5.1+Jun-18-fact-strip) until this draft is approved and renamed.

**Draft Author:** SAM
**Draft Status:** backbone only — structure + analytical pivots + RED-challenge anchors; prose finalize after RED + CPI
**Revisions:**
- 2026-06-18 PM Thu — initial backbone commit (`8e86586f`)
- 2026-06-19 — PROME audit incorporated (5 fixes): (1) USDJPY-call direction bug → corrected to USDJPY-put / JPY-call (long yen = USDJPY DOWN); (2) "no cover post-catalyst" timeframe-conflation → reframed to "no cover INTO catalyst; post-catalyst state unresolved until Sat Jun 20 print"; (3) Pillar 1/3/4 lumped-together claim → split into 3 distinct failure modes (Pillar 1 inverted / Pillar 3 farther from trigger / Pillar 4 stayed loaded but failed-to-fire); (4) RED challenge #4 strengthened from hint to explicit GATE (vehicle modeling proceeds only if RED #1-#3 survive); (5) FXY-vol caveat added (expiry/roll-weird proxy; sanity-check vs second source before committing).
**Fact baseline:** all three Jun-18 verified facts (Warsh-Fed since 2026-05-22; FOMC Jun 17 +40bp 2026 median dot; Iran/US deal SIGNED Jun 17 — HAWK-aligned framing per Step 1.5 reconcile at commit `97701098`)
**Input refs:**
- `THESIS.md` v1.5.1 + Jun-18 facts (canonical until this draft approved)
- `CHANGELOG.md` 2026-06-18 entry (three verified facts + Step 1.5 audit trail)
- `proposals/2026-06-10_v16_rewrite_spec.md` (pre-event v1.6 scope spec)
- `research/2026-06-10_ch010_011_032_responses.md` (RED CH-010/011/032 acceptances)
- LIQUID + HENRY outbox SIGs Jun 18 (commit `b3a54069`)
- HAWK Jun-18 re-mark (commit `c677cd0a`) + Step 1.5 Iran reconcile (commit `97701098`)
- Step 1.5 stop re-arm (commit `48dbf25c`) — single-leg FXY ≤ $55.05 in place

---

## ONE-LINER (v1.6 draft)

**The carry-trade direction-conditional case for being long yen is wrong (or at least directionally inverted) near-term — but the carry-trade CONVEXITY case is intact-to-stronger.** Pillar 1's directional vector flipped across the Jun 16-17 sequence (BOJ +25bp compression < Fed Jun-17 +40bp dot re-widening); BOJ-side normalization-as-priced has been delivered without a violent move; Fed-side cut path is replaced by Fed-HIKE pricing under new Chair Warsh (statement-gutting hawkish). What remains is (a) CFTC at 81% of cycle peak with **no cover INTO the catalyst — post-catalyst cover is UNRESOLVED until the Sat Jun 20 print (Jun 16 data)** (the current -145,818 print is Jun 9 data, released Jun 12, pre-catalyst by definition); (b) Pillar 2 (J-ICS DOMESTIC long-end abandonment) still firing on schedule; (c) the tail-routes (US credit cascade → Fed walk-back, oil/risk-off re-escalation, fresh hawkish-of-pricing BOJ surprise, MOF #3 with cabling intact). **The position narrative re-centers from "structural compression delivers via Channel 2 catalyst" → "carry-trade convexity tail at 81% positioning fuel INTO the catalyst (post-catalyst state pending); modal near-term path bleeds, tail pays if any of the four routes fires."** v1.6's load-bearing question is therefore not "should we be long yen-direction" (answer: not as a near-term directional bet) but **"is the FXY-spot vehicle the right way to express the convexity tail under v1.6, or does FXY-vol / a USDJPY-put (= JPY-call) structure / a JGB-30Y short / something else dominate it?"**

---

## CONVICTION DECOMPOSITION (v1.6 — vs v1.5.1)

| Dimension | v1.5.1 mark | **v1.6 draft mark** | Reasoning |
|---|---|---|---|
| Yen-strengthening direction / level (multi-year) | HIGH | **MEDIUM** (downgrade from HIGH) | Pillar 1 directional vector INVERTED post-Warsh; Pillar 3 moved FARTHER from its <145 trigger (USDJPY 161+); Pillar 4 STAYED LOADED but FAILED to fire (catalyst spent without lighting positioning unwind — different failure mode from the other two). Pillar 2 + structural-LEVEL argument still operate but with weaker convergence under Warsh-Fed-hawkish regime. **RED challenge embedded below** on whether MEDIUM is too generous given the directional vector is broken, the threshold is farther away, and the fuel-load failed-to-fire on its expected trigger. |
| Near-term timing (3-6mo modal path) | MEDIUM | **LOW** | Catalyst spent without firing; no near-term trigger in modal window; cross-pair vindication decoupled Jun 11 (yen-bid-on-risk-off channel temporarily off). 7d/30d/60d carry-unwind buckets shipped to LIQUID/HENRY as ~5-6/17-20/24-28 (down from Sun ~8/23/32). |
| Carry-trade convexity TAIL (60d+) | (not separately graded under v1.5.1) | **MEDIUM-HIGH (NEW separate row) — CONDITIONAL on Sat Jun 20 CFTC print** | CFTC 81% fuel INTO catalyst is asymmetric IF positioning held through. **Post-catalyst cover state UNRESOLVED until Sat Jun 20 print.** Four tail routes intact: Fed walk-back of Jun-17 dots; US-credit cascade → recession → cuts; oil/MOU re-escalation; fresh hawkish-of-pricing BOJ. Severity intact-IF-fuel-held; modal probability of ANY firing in 60d is the unsolved question for v1.6. If Sat Jun 20 shows cover (e.g., breach -125K), this row drops to MEDIUM at most. |
| Position vehicle fit | (assumed FXY-spot+near-call) | **OPEN — load-bearing v1.6 question** | If we're betting convexity not direction, FXY-spot may dominate FXY-vol / spread / JGB-short — or not. See § VEHICLE AUDIT. |

**RED challenge #1 to embed pre-finalize:** is "carry-trade convexity tail at MEDIUM-HIGH" honest, or is it the SAM-historical pattern of "right substance, wrong window" being re-skinned as convexity to preserve the bet? Specifically — name the trigger probability and the magnitude required for the tail to pay vs the carry/theta cost of holding, and show the EV is positive after honest decay assumptions. If you can't, the row should be MEDIUM not MEDIUM-HIGH.

---

## RE-FRAME: COMPRESSION → CARRY-UNWIND TAIL (the v1.6 center)

v1.5.1 narrative: **"yen strengthens via rate-differential compression (BOJ hike + Fed cut path multi-month-tail) and structural pillars."** Under v1.6, the rate-differential compression vector is broken near-term (Pillar 1 inverted; Fed-cut path replaced by Fed-HIKE regime). The structural pillars are not gone but their *directional convergence* is gone.

**v1.6 narrative:** **the carry-trade was structurally over-positioned INTO the catalyst (CFTC 81% of -180K cycle peak, 6 build weeks, no cover INTO catalyst per Jun-9 release Jun-12; post-catalyst cover state UNRESOLVED until Sat Jun 20 print). Positioning was at-peak fuel without a near-term modal trigger — *whether it stays loaded post-catalyst is the v1.6 decision-grade observable.* The thesis is no longer "compression delivers" — it is "asymmetric convexity payoff when ANY of N tail routes fires within an eligibility window, CONDITIONAL on positioning remaining loaded."**

The "N tail routes" are the same triggers in the CH-004 METHOD but the framing is what changes:

| Route | v1.5.1 framing | **v1.6 framing** |
|---|---|---|
| BOJ surprise (hawkish-of-pricing) | Anchor #1 — modal trigger for Channel 2 | Now a residual tail (most of the priced hike mass already burned at Jun 16; only the *next* hike-of-the-cycle surprise or accelerated-QT shock counts) |
| MOF intervention #3 | Anchor #2 — modal Channel 3 path | Live-pending; 48h+ at USDJPY 161+ no strike (Bloomberg intervention alert Wed); CH-011 disorder-not-level read applies; PROBABILITY UPDATED — see § MOF-DECAY |
| Risk-off shock | Anchor #3 — base rate trigger | **Newly the most-watched route** — Aug 2024 precedent operates here. **But:** cross-pair vindication decoupled Jun 11 (yen-bid-on-risk-off went to USD-haven). Channel may be temporarily off; needs vol-spike (not just hawkish-Fed) to re-fire. |
| Fed-cut surprise | Anchor #4 — secondary path multi-month tail | **Now reframed:** tripwire is "walk-back of Jun-17 dot revision" — Powell-era cut-pricing dynamics don't apply under Warsh. Path requires US-credit cascade actually forcing his hand. |
| Oil/MOU escalation | Anchor #5 — Phase 2 yen-bid path | **Step 1.5 update:** deal SIGNED, verification leg OPEN, Hormuz reopening process begun. Phase 1 near-term dormant. Re-escalation risk via Israel-Lebanon/Gaza or Iranian non-compliance with verification leg (esp. HEU dilution + Oman fee admin). Tail-but-thinned. |
| **CFTC residual (positioning cascade)** | Amplifier on triggers + residual gate | **Promoted to load-bearing in v1.6** — the residual term IS the convexity. At 81% peak with no cover, ANY trigger lights a violent move whose magnitude is dominated by positioning unwind, not by the trigger's direct mechanism. This is the asymmetric setup. |

**RED challenge #2 to embed pre-finalize:** the v1.5.1 framing collapsed when its dominant route (Channel 2 / Pillar 1 compression) inverted. What's preventing v1.6 from being the same pattern with a different dominant route? Specifically: name the v1.6 "single-point failure" — what's the analog of "BOJ hike + Fed cut compresses the gap" that, if it falls, takes the whole frame with it? If the answer is "CFTC fuel persists at 81%," then write the explicit threshold at which a cover (e.g., breach below -108K / 60% line) invalidates the frame, and pre-register the disposition.

---

## PILLAR AUDIT (1-4)

Re-derive each v1.5.1 pillar against the Jun 16-17 outcome. Mark ALIVE / WEAKENED / BROKEN per Will's "re-center, not mark down" frame.

### Pillar 1 — Rate differential at multi-decade extreme

**Status: directional vector BROKEN; structural LEVEL ALIVE.**

| Sub-claim | Status | Reasoning |
|---|---|---|
| The *level* of the gap is the carry (structural argument) | ALIVE | ~280-300bp gap still extreme; carries no matter the change-at-meeting |
| Compression delivers near-term via BOJ + Fed convergence | **BROKEN** | BOJ +25bp (Jun 16) < Fed Jun-17 +40bp dot — net gap WIDER post Jun 16-17 |
| Even 25bp BOJ move = ~9% gap compression = "meaningful as confirmation, not full resolution" | ALIVE in math, BROKEN in directional framing — the 9% compression was MORE than offset, so it didn't even count as confirmation |
| Future compression requires Fed walk-back of dots OR BOJ hawkish-of-pricing surprise | NEW (replaces "Fed cuts OR BOJ hikes") | Multi-month tail only; not near-term modal |

**Recommendation for v1.6:** rewrite Pillar 1 as "the LEVEL argument" with the directional-vector claim deleted. The structural carry CAN be unwound by mechanisms other than direct rate compression (positioning unwind, risk-off, etc.) — but Pillar 1 as written conflates the level (alive) with the vector (broken). v1.6 should split them.

### Pillar 2 — J-ICS lifer long-end abandonment (DOMESTIC)

**Status: ALIVE on schedule; only-pillar-still-firing.**

| Sub-claim | Status | Reasoning |
|---|---|---|
| J-ICS makes long-duration JGB purchases punitive for solvency | ALIVE | Regulatory regime unchanged |
| Mid-size lifers (Fukoku, Asahi) pivoted 30/40Y → 10-15Y | ALIVE | Confirmed continuing per Jun-10 JGB 30Y auction softening (BTC 2.936 vs 3.115; tail 2.8bp vs 1.3bp) |
| Lifer absence = cause not consequence of long-end yield blowout | ALIVE | Confirmed by Apr-Jun pattern: 30Y at 3.823% Jun 11 pub → 3.725% Jun 15 pub → 2.613% on 10Y (taper-pause-end-FY2027 absorbed BOJ-hike impact) |
| Pushes BOJ toward normalization OR YCC-style cap | ALIVE | Jun 16 hike delivered normalization side; YCC-cap option still tail |
| **DOMESTIC; does not transmit to foreign-asset selling at lifer-disclosure timescale** | ALIVE — v1.5 finding confirmed (Channel 1 stays DEFERRED) | 4-of-4 institutions grew US credit through 2026 disclosure windows |

**Recommendation for v1.6:** Pillar 2 keeps its status, but its role in the thesis changes — it's the ONLY pillar that supports yen-strengthening through a domestic mechanism independent of the carry trade. In a v1.6 framing focused on carry-convexity, Pillar 2 becomes the *anchor* of the yen-LEVEL story (the JGB-yields → BOJ-pressure → eventual normalization-overshoot path) rather than a *near-term* support. Multi-quarter, not 3-6mo.

### Pillar 3 — Hedge ratio at 14-year low

**Status: ALIVE in fact, WEAKENED in proximity to trigger.**

| Sub-claim | Status | Reasoning |
|---|---|---|
| Hedge ratio 44.4% / 14-yr low | ALIVE | March 2025 data still operative; no fresh print |
| ~55% of foreign bonds (~$370-550B) unhedged | ALIVE | Same |
| Vol-weighted entry USD/JPY 135-145 | ALIVE | Same |
| Mechanical-selling threshold USDJPY <145 | ALIVE | Threshold unchanged |
| Slow-burn delivery via sustained Fed-side compression | **WEAKENED** | Fed-side compression now REVERSED direction; USDJPY moved 161+ (FROM ~159-160 pre-Jun-16) — further AWAY from 145 trigger |

**Recommendation for v1.6:** Pillar 3 status changes from "slow-burn version of Channel 1" to "deep latent — requires a trigger to bring USDJPY through 145, no longer has a tail-wind to do so on its own." Still real, but its delivery now depends on one of the convexity-tail routes firing.

### Pillar 4 — Positioning fuel load near cycle peak

**Status: ALIVE — strongest of the four; the convexity itself.**

| Sub-claim | Status | Reasoning |
|---|---|---|
| CFTC at 63.7% of cycle peak (May 26) | UPDATED → **81.0%** (Jun 9 data, rel Jun 12) | 6 consecutive build weeks; 7,182 short of -153K/85% escalation |
| Amplifier +5pp ON, residual ON | ALIVE | METHOD residual gate triggered through; no cover (-108K untouched) |
| Positioning doesn't trigger unwind — amplifies one when fires | ALIVE | Mechanism intact |
| The fuel load growing INTO a hawkening market is the asymmetric setup | **AMPLIFIED in v1.6 — promoted to load-bearing center (CONDITIONAL on Sat Jun 20)** | Fuel was loaded INTO the catalyst (Jun 9 release Jun 12: -145,818, 81% of peak, 6 build weeks). **Whether it stays loaded post-Jun-16 is unresolved until Sat Jun 20 print (Jun 16 data).** If post-catalyst positioning holds 80%+ with no cover, that's the strongest single confirmation of the convexity-tail frame. If it covers (e.g., -125K → ~70%), the frame WEAKENS. The boot.py Thu "shorts growing" indication reads the Jun 9 tsv — it is NOT a post-catalyst signal. |

**Recommendation for v1.6:** Pillar 4 is the v1.6 thesis center, not a Pillar. Promote to its own section "POSITIONING-CONVEXITY THESIS" with the explicit threshold (cover below -108K invalidates) and the trigger-vs-cover race as the dominant dynamic.

**RED challenge #3 to embed pre-finalize:** "fuel load growing into a hawkening market is the asymmetric setup" is the same logic that argued for the v1.5.1 single-path bet — and Jun 16 *was* the hawkening, and the fuel didn't burn. What's the v1.6 mechanism by which 81% positioning fires WITHOUT the catalyst-mechanism it was supposed to fire on? "Eventually a trigger comes" is not a thesis if the eligibility window is unbounded. Pre-register a trigger-eligibility window (e.g., 90 days from CFTC peak; failure-to-fire by Sep 18 with positioning still 80%+ = thesis-broken).

---

## VEHICLE AUDIT (THE v1.6 LOAD-BEARING QUESTION)

If v1.6 is centered on carry-trade CONVEXITY rather than DIRECTIONAL compression, **the FXY-spot+near-call vehicle may not be the right way to express it.**

| Vehicle | Pros for v1.6 convexity frame | Cons for v1.6 convexity frame | Status |
|---|---|---|---|
| **FXY shares (current — 13 @ $58.32)** | Linear yen exposure; cheap to hold; mechanical Stop available; tracks USDJPY directly | Bleeds in regime-suppressed tape; convexity payoff requires sustained move, not spike; sized as "structural-pillar bet" under v1.5.1 framing | **OPEN — keep, trim, or carve out as tail exposure?** |
| **FXY vol (long FXY ATM straddle / strangle, OTM call)** | Direct convexity exposure; pays on VIOLENT move regardless of direction; potentially cheap if IV is low post-event | Theta decay; **FXY-IV proxy is non-physical at extremes per KB-183 — and the proxy went weird around the Jun-18 expiry/roll**; time-dependent on trigger arrival. **Only model AFTER expiry roll completes + proxy sanity-check vs a second source.** | Modeled in v1.6 *after* proxy sanity-check; do not commit on a single post-event IV print |
| **USDJPY-put / JPY-call structure (long yen DOWN-USDJPY)** *(corrected direction — PROME audit)* | More direct yen-strengthening exposure than FXY; deeper OTM available; bigger payoff in sharp moves | Less liquid in retail-accessible form; bigger spread; harder to scale; FX-options vs FX-futures-options is a separate sub-decision | Worth modeling — note this is the LONG-YEN structure (USDJPY put / JPY call), NOT a USDJPY call (which would be SHORT yen, wrong direction) |
| **JGB-30Y short (or 40Y short)** | Pillar 2 expression — yen-strengthening via DOMESTIC long-end mechanism; uncorrelated with carry-trade unwind timing | Different risk profile; not yen-direction at all; requires margin/structure | Niche — model only if convexity frame elevates Pillar 2 |
| **Spread structures (e.g., 1×2 call ratio, calendar)** | Cheaper convexity; defined risk; can fade premium decay | Capped upside; complex; mid-roll required | Worth modeling |

**v1.6 vehicle question:** does the v1.6 frame favor (a) status quo FXY-spot as tail-exposure with the carry/theta cost accepted, or (b) trim/sell shares + open a vol position to express the same view more efficiently, or (c) hold both (shares + vol overlay)?

**No conviction on this yet.** Need (a) post-CPI FXY IV print (cheap vol = case for vehicle change strengthens); (b) RED challenge on whether convexity-frame is honest (per RED #1 above); (c) Will-decision on risk-budget for any vol-position.

**RED challenge #4 to embed pre-finalize (PROME-strengthened to GATE):** the vehicle-change argument assumes the convexity frame is correct. If v1.6 backbone-tests fail (e.g., RED challenges 1-3 don't survive), the vehicle question is moot — the answer is **"trim or close, not re-vehicle."** **GATE (pre-registered):** vehicle modeling proceeds *only if* RED challenges #1, #2, AND #3 survive intact. If any of the three is broken by RED, this section is closed and the v1.6 finalize decision-set narrows to (a) hold-with-tighter-stop or (b) trim/close. No vehicle-change options propagated to finalize if the frame fails.

---

## MOF-DECAY ANALYSIS

USDJPY at 161+ for 48h+ post-FOMC with NO MOF strike, Bloomberg Wed "Markets Alert for Japan Intervention" — but no action. **MOF response function appears to be decaying** vs the Apr 30 / May 6 pattern (where 160+ in disorderly tape drew immediate strikes).

| Period | USDJPY level | MOF action | Tape state |
|---|---|---|---|
| Apr 30 | 160.70 (intraday peak) | ~¥5.48T strike (~$35B) | Disorderly + post-hold spike |
| May 6 | 157.89 | ~¥4.3T strike (~$28B) | Disorderly + Golden Week thin liquidity |
| Jun 5 (NFP) | 160.20 (Fri intraday peak) | NO strike | Orderly — USD-side macro driver |
| **Jun 9-16 (8+ sessions)** | **160-161+** | **NO strike** | Orderly — blackout active, CH-011 disorder-not-level confirmed |
| **Jun 17 (post-FOMC)** | **160.78 close** | **NO strike (post-blackout)** | Hawkish-Fed-driven move |
| **Jun 18 (24h post-FOMC)** | **161.34** | **NO strike — Bloomberg flagged intervention alert** | Orderly continuation |

**v1.6 analytical question:** is MOF response function decaying because (a) coordination with Bessent/US is now framed as "rate-differential should fix this, not FX intervention" (per Bessent prior statements + Step 1.5-relevant Iran post-deal context); (b) Katayama's "decisive action" verbal is being held back for genuine disorderly moves only (CH-011 confirmed); (c) MOF is letting BOJ do the work post-Jun-16; or (d) decision-paralysis around Ueda still hospitalized?

**Implication for v1.6:** MOF #3 path (anchor #2 in the convexity tail) is THINNER than the Sun Jun 14 ~30% mark implied. Post-event single-leg probability under CH-011 + 48h-no-strike-at-161+ + post-Fed-hawkish framing should re-derive to ~15-20% over a 30d window. **Specific re-mark pending RED pass; will not propagate to LIQUID/HENRY until v1.6 finalizes.**

---

## CFTC FUEL-WITHOUT-TRIGGER ANALYSIS

The single most-load-bearing observable for v1.6 — and the strongest empirical confirmation of the convexity-tail frame OR its falsification, depending on what happens post-catalyst.

**Current state (Jun 9 data, rel Jun 12 — PRE-catalyst):** -145,818 / 81.0% of -180K cycle peak / 6 consecutive build weeks. **No cover INTO catalyst.** **Post-catalyst cover state is UNRESOLVED until Sat Jun 20 print (Jun 16 data).** The boot.py Thu "shorts growing" reads the same Jun-9 tsv — it is NOT a post-catalyst observation. This timing-discipline matters: the v1.6 convexity frame depends on positioning remaining loaded *through* the catalyst, which is what Sat tests.

**Next observable:** Sat Jun 20 release (Jun 16 data). **This is the v1.6 decision-grade observable.**

| Sat Jun 20 print scenario | v1.6 implication |
|---|---|
| Cover (e.g., -125K, drops to ~70% of peak) | Convexity-tail frame WEAKENED — positioning unwinding without a trigger contradicts the "fuel loaded into a regime, waiting for any trigger" narrative |
| Sideways (-145K range) | Frame stays — fuel held through catalyst, awaiting trigger |
| **Further build (-153K + = 85%)** | Frame STRENGTHENED — amplifier escalates +5pp → +8-10pp; max-asymmetric setup |

**Pre-register disposition:** under cover scenario, downgrade v1.6 convexity-tail conviction to LOW; under sideways/build, hold MEDIUM-HIGH (or upgrade) pending RED challenge #3.

**RED challenge #5 to embed pre-finalize:** the "trigger eligibility window" question (per RED #3) maps directly here. If CFTC stays at 80%+ for 90 days without a trigger firing, the convexity-tail frame should be retired — positioning at peak without trigger = "everyone is short and nothing happens" = inefficient bet. Pre-register the window.

---

## CHANNEL RE-CLASSIFICATION (v1.6)

### Channel 1 — Life Insurer Repatriation

**v1.5 status:** DEFERRED structural backstop (multi-year)
**v1.6 draft status:** **DEFERRED — OR RETIRE PENDING NEW MECHANISM?** (open question — LIQUID input invited per Jun-18 SIG)

Evidence for RETIRE:
- 4-of-4 institutions grew US credit through 2026 disclosure windows (Big 3 mutuals + Norinchukin)
- Norinchukin CLO record ¥10.1T +¥1.8T YoY (FY2025 disclosure surfaced Jun 10)
- MOF weekly LT-debt net BUYING continuing through Jun 13
- ESR pressure absorbs via capital actions (M&A) + equity rally + hedge-cost relief, not foreign bond sales

Evidence to KEEP DEFERRED (not retire):
- Hedge ratio still 44.4% / 14-yr low (Pillar 3 framework)
- Structural setup intact at multi-year horizon
- USDJPY <145 mechanical-selling threshold unchanged
- A new shock (JGB 30Y blowout to 4.5%+, ESR <200% via market stress not M&A) is a path back

**RED challenge #6 to embed pre-finalize:** "deferred pending new mechanism" with 4-of-4 disconfirmations and no specified path is functionally equivalent to RETIRED. The honest move is to retire it and re-add IF a new mechanism appears. Anything else is keeping a dead channel on the books to preserve narrative completeness.

### Channel 2 — Carry Unwind

**v1.5 status:** DOMINANT REMAINING NEAR-TERM TRIGGER
**v1.6 draft status:** **CARRY-CONVEXITY TAIL (renamed)** — the channel is now the v1.6 center, but the framing changes from "trigger fires within window" to "asymmetric payoff IF any of N tail routes fires within an eligibility window."

### Channel 3 — BOJ Policy Divergence + US-Japan FX Coordination

**v1.5 status:** REACTIVATED Jun 1 (Iran MOU break); intervention #3 zone live
**v1.6 draft status:** **MOF #3 path DECAYING** (per § MOF-DECAY); FX-coordination still operative but reaction function appears asymmetric — willing to intervene on disorder, not on level. Re-rate to single-leg MOF #3 anchor in convexity-tail at ~15-20%/30d.

### Channel 4 — POSITIONING-CONVEXITY (NEW)

**v1.5 status:** Pillar 4 / amplifier on other triggers
**v1.6 draft status:** **PROMOTED to standalone channel.** This is the v1.6 center.

---

## CROSS-AGENT RE-DERIVATION

Updated network-relevant marks (already shipped to LIQUID + HENRY at commit `b3a54069`; this section is the v1.6 backbone version, finalize after RED):

| Recipient | v1.6 channel update | Action item for them |
|---|---|---|
| LIQUID | Channel 1 disposition (DEFERRED → RETIRE PENDING NEW MECHANISM?) — input invited | Read SIG; respond if disagree; otherwise v1.6 carries the disposition |
| HENRY | Cross-pair vindication DECOUPLED Jun 11 (yen-haven-channel temporarily off); CFTC fuel-without-trigger is the dominant transmission read | Read SIG; track whether the cross-pair channel re-snaps on a VIX-spike scenario |
| BRENT | Iran HAWK-aligned framing already shared via PROME+ORC Step 1.5 reconcile; no additional ship | None — BRENT THESIS v3.1 already operates the correct framing |
| HAWK | No update needed — HAWK's Jun 18 re-mark is the SOURCE of the correct framing | None |
| RED | **v1.6 backbone DRAFT (this file) for RED challenge** | Read this file; deliver CH-NN challenges on the 6 marked spots; pre-finalize gate |
| PROME | v1.6 backbone draft notice + Step 1.5 / network re-mark closeout summary | Already coordinated; v1.6 finalize pings PROME |

---

## POSITION FRAMING (per Will scope — "FXY shares separated as tail exposure from any directional claim")

**v1.5.1 framing:** "13 shares = structural-pillar bet; Jun-18 $58C = catalyst-conditional bet."

**v1.6 draft framing:**

- **13 FXY shares @ $58.32 avg ($798) = CARRY-CONVEXITY TAIL EXPOSURE.** No longer framed as directional/structural-compression bet. Sized small + risk-controlled at FXY ≤ $55.05 single-leg (Step 1.5 re-arm); accepts the modal-direction bleed in exchange for participation in any tail-route firing within the eligibility window (TBD per RED #3).
- **Jun-18 $58C ($40 premium) = RESOLVED, expired worthless today** — catalyst-conditional bet on a hawkish-of-pricing surprise that did not occur.
- **No new sizing decision in v1.6 draft.** Per Will scope: pillar audit + vehicle audit + RED challenge complete BEFORE any sizing rec. Stop is in place at $55.05 single-leg as interim risk-control.

**Pre-registered v1.6 finalize sizing decisions (post-CPI, post-RED):**
1. Retain 13 shares as tail exposure? Or trim?
2. Add a vol-overlay (FXY ATM straddle / OTM strangle)?
3. Replace FXY-spot with USDJPY-put / JPY-call structure or FXY-vol (vehicle change)? *(Note: long yen = USDJPY DOWN = USDJPY put; an FX call on USDJPY would be wrong-direction — PROME audit correction)*
4. Tighten the stop (per Will's Option (b) from Step 1.5)?
5. Define the eligibility window (per RED #3/#5)?

All five are sized decisions; v1.6 backbone defers them all.

---

## OPEN QUESTIONS FOR v1.6 FINALIZE (POST-CPI, POST-RED)

1. **Conviction-decomposition row "Yen-direction MEDIUM" vs "LOW"** — RED #1 challenge: is MEDIUM honest given Pillar 1 directional vector INVERTED + Pillar 3 moved FARTHER from <145 trigger + Pillar 4 STAYED LOADED but failed-to-fire on its expected catalyst (3 distinct failure modes, not 3 of the same)?
2. **v1.6 single-point-failure name** — RED #2 challenge: what's the analog of "compression delivers via Channel 2" that, if it falls, takes the whole frame with it?
3. **Eligibility window** — RED #3/#5 challenge: trigger-eligibility window for the convexity tail (90d? Until next BOJ MPM Jul 31? Until end-CY26?). Pre-register the disposition.
4. **Vehicle decision** — RED #4 challenge (now a GATE): does the v1.6 frame favor (a) FXY-spot status quo, (b) FXY-vol overlay [after expiry-roll proxy sanity-check], (c) USDJPY-put / JPY-call structure (long-yen direction), (d) trim/close? **Gate: (b) and (c) only on the table if RED #1, #2, #3 all survive — otherwise the answer is (a) or (d).**
5. **Channel 1 disposition** — RED #6 challenge: DEFERRED vs RETIRE PENDING NEW MECHANISM; LIQUID input pending.
6. **MOF #3 30d single-leg probability re-rate** — re-derive ~15-20% after RED pass.
7. **CFTC Sat Jun 20 print scenario disposition** — pre-register cover/sideways/build dispositions before reading the print.
8. **Fri Jun 19 National CPI integration** — soft print → BOJ Oct hike repricing softens, Pillar 1 narrower path; hot print → BOJ Oct strengthens, slight Pillar 1 directional re-firing; mixed → minimal v1.6 impact.

---

## SAM-LOCAL CHANGES IF v1.6 ADOPTED

(Surfaces to update on finalize — not in this draft, but pre-listing to avoid Step-1.5-style overclaim during finalize.)

- `THESIS.md` — full rewrite (this draft becomes canonical; current `THESIS.md` archives to `thesis/THESIS_v1.5.1_ARCHIVE.md`)
- `STATUS.md` — banner refresh + drop "Channel 2 dominant remaining trigger" framing + add CARRY-CONVEXITY-TAIL framing
- `CHANGELOG.md` — v1.6 entry: old (v1.5.1 + Jun-18 fact strip + Step 1.5 reconcile + Step 1.5 stop re-arm) → new (re-centered to carry-convexity-tail; pillar audit results; vehicle question; channel re-class)
- `STRATEGY.md` — re-derive Position section; vehicle-question disposition; stop spec interim → potentially tightened
- `TRADE.md` — re-frame position narrative (shares = tail exposure); R:R re-derive
- `PREDICTIONS.tsv` — open new predictions on the four RED-pre-registered eligibility-window thresholds
- `evals/` — re-baseline (v1.6 changes load-bearing structure)
- Cross-agent SIGs — v1.6 update SIG to LIQUID + HENRY when commit
- Auto-memory — process lesson if v1.6 finalize reveals a calibration pattern

---

## DRAFT NEXT STEPS

1. **Tonight after Fri CPI prints** — integrate CPI; address open question #8
2. **RED challenges (6 marked spots)** — spawn RED with this file + the 6 numbered challenges; resolve before finalize
3. **Sat Jun 20 CFTC print** — pre-register disposition before reading; use as v1.6 conviction-gauge
4. **Will-decision items** — 5 sizing decisions (post-RED, post-CFTC); confirm vehicle question is open before drafting vehicle-decision options
5. **v1.6 finalize commit** — rename DRAFT → canonical; archive v1.5.1; PROME ping; LIQUID/HENRY update SIGs; eval re-baseline

---

*🚧 END v1.6 DRAFT BACKBONE — finalize post-CPI + post-RED. Canonical thesis remains `THESIS.md` until this draft is approved.*
