# BOND THESIS — v1.1.4

**Version:** 1.1.4 (2026-08-18 — **staleness sweep: the 8/10 C-36 downgrade was MISSING from this document entirely for 8 days, an internal contradiction on dealer inventory is fixed, a stale UNSCOREABLE blocker is removed, and the thesis-kill gate is re-specified from hardcoded-7Y to per-tenor.** Partial adoption of the v1.1.4 spec changes pre-committed 7/28 — see ADOPTION NOTE below. Prior v1.1.3 2026-07-28, v1.1.2 2026-07-18.)
**Last Updated:** 2026-08-18 by BOND

> # ⚠️ REGIME LABEL: **CONTESTED (~50%), NOT CONFIRMED**
>
> **This document asserted a settled "policy-path-led" label for 8 days after the desk itself downgraded it.** On **2026-08-10** (Financial-Conditions forum, Will-ruled in-session) **C-36 / "policy-path-led" moved from CONFIRM (~80-85%) to CONTESTED (~50%)** — and **no part of that ruling reached this file until 2026-08-18.** `STATUS.md` carried it; the durable document did not. **That is the more serious failure of the two, because THESIS is what a reader consults for the standing argument.**
>
> ⚠️ **Every "policy-path-led" statement below is therefore CONTESTED, not canon** — including the v1.1.2 instruction *"do NOT restate this as term premium."* **That instruction is suspended.** It was correct when written and is no longer safe to apply as a rule.
>
> **★ New evidence 2026-08-18, pointing further AWAY from the policy-path label.** FRED publishes `THREEFYTP10` — a **daily** Kim-Wright 10Y term premium, the instrument this desk's own 8/10 scope claim required and did not have (it had been running on ACM's *monthly* series, which by construction cannot speak to any single week). On the daily series, **7/13 → 8/07: 2Y −7bp · 10Y +3bp · 30Y +9bp, with term premium +2.5bp ≈ 83% of the 10Y move** — a **long-end-led bear STEEPENER**, which is the signature this desk's own 7/18 falsifier assigns to **term premium**, and the exact opposite of the belly-led bear-flattener that justified the policy-path label.
>
> **The honest reading is that the regime ROTATED after mid-July — not that the 7/18 call was wrong for its own window (7/6→7/13), where it stands.**
>
> ⛔ **BOND has NOT moved the label and will not move it unilaterally.** The 8/10 ruling is Will-ruled and carries an explicit guard-rail against conflating "the channel is uncovered" with "the label resolved to term-premium." Three caveats also travel with the new instrument: it is a **model** output (level never reconcilable against ACM's), it **lags** (8/07 latest — the 8/11–17 surge to a 19-year high is unmeasured on it), and it is **n=1 model**. ⇒ **This is evidence for a label conversation, forum/Will-gated. Routed to HENRY, whose HEN-42 resolves 2026-08-29 on the same question.**
**Status:** 🟡 WATCH, **escalating** — **"expensive, not broken"** still holds, and as of 2026-08-18 it holds through **the hardest supply test of the quarter**: the **August refunding ($125B, 8/11–8/13) cleared with NO composition failure at any tenor** — indirect at/above each tenor's trailing-12 median at all three, dealers at or below median, and the **30Y clearing 5.216%, the highest 30Y auction yield since 2001.** Cover markers have fired (7/27 5Y, lowest BTC since Sept-2022) without the mechanism failing once. The long end remains engaged (`^TYX` **closed 5.31 on 8/17 — a 19-year high**; 29 consecutive `DGS30` sessions >5.00%), and — post-QT (ended Dec-1-2025) — **there is no Fed coupon backstop** (RMPs buy T-bills, not coupons), so long-end absorption is entirely private/foreign/dealer. ⚠️ **CORRECTED 8/18 — this line previously read "dealer long-end inventory is at a record," which CONTRADICTED item 1 of this same document, where the record is recorded as retired and unwound.** The record is **gone**: long-end inventory **−14.3% off its 6/24 peak**. Composition has NOT broken at any tenor tested since 7/9. ⚠️ **Credit: the 7/23–24 re-activation FULLY ROUND-TRIPPED** — HY is now *below* where that episode began. See item 3, rewritten. *(All live levels, scores and the convergence matrix → `STATUS.md`. This document deliberately carries none.)*
**Conviction:** Duration-short (TLT puts) **HOLD, no add** — the add-gates are pre-registered and **none has fired.** Short-credit **NOT supported** (primary market open, zero pulled deals) — but the "credit is inert" premise is retired and the HY vector is live again.

---

## CORE THESIS

BOND owns the **market-structure transmission layer** — how the bond market's own functioning (Treasury auctions, dealer balance sheets, corporate issuance, curve shape, the credit→equity lead) transmits or absorbs systemic stress. The job is to detect when the bond market stops **clearing** and starts **breaking**.

**The durable read is "expensive, not broken."** Through the May–July 2026 long-end repricing, every demand test — the May refunding, 5/20 20Y, 5/21 10Y TIPS, the June refunding, the 7/9 30Y reopen, the 7/22–23 cluster, and the 7/27 2Y+5Y — **cleared at price**. Yields are elevated on a **real-rate / higher-for-longer (policy-path) repricing** *(label corrected v1.1.2; do NOT restate this as "term premium" — that framing was retired and the correction is empirically verified by the real curve moving belly-led on its own)*, not by a mechanical demand hole. That distinction is the whole thesis: a repricing is a slow digestion the market absorbs; a demand hole (failed auctions → forced dealer warehousing → funding stress) is the fast, systemic path. To date it is the former.

**The discriminator is COMPOSITION, not the headline cover** *(hardened v1.1.3)*. The 7/27 5Y is the worked example and the reason this distinction earns its keep: it printed the **lowest bid-to-cover since Sept-2022** — a genuine threshold breach that fired a pre-registered trigger — while **indirect demand rose with duration and dealers were not stuffed.** Cover thinned; mechanism held. A thin cover with intact composition is a *price* concession; a demand hole requires **indirect falling AND dealers absorbing.** Grade every auction on that pair, never on the cover alone, and **never on a tail** — a tail is unscoreable from primaries (no when-issued published), so no gate may be keyed on one.

**The June refunding confirmed the read.** The 10Y (6/10) printed **strong** — BTC 2.57, indirect 78.2%, primary-dealer take just 9.4% (dealers barely absorbed); the 30Y (6/11) printed **soft but orderly** — BTC 2.33 (held above 2.3), indirect 59.8%. No demand hole; yields *rallied* post-auction. [CONF TreasuryDirect, 6/10–6/11]

**Three things keep this a WATCH (escalating), not a stand-down** *(items 2 and 3 rewritten v1.1.3 — they had been asserting the opposite of the current read)*:
1. **The long end is absolutely elevated and sustained** (live levels → STATUS) — **but the "record-thin dealer backstop" leg is RETIRED as of 7/28 and this item is now the WEAKEST of the three.** The FR2004 gap was closed (it was a stale API series break, not an access limit) and the record has **unwound**: as of the **8/05** as-of (3 further prints recovered 8/18), 11-21Y is **−17.1%** off its 6/24 peak and long-end total **−14.3%**, including a **−$9.3B single week to 8/05 — the largest weekly drawdown of the window.** **The benign reading is now CONFIRMED rather than assumed:** that drawdown is dealers clearing balance sheet *ahead of* the 8/11–13 refunding, **which then cleared with indirect at/above trailing-12 median at all three tenors and dealers at median.** The monitor's forced-de-risking branch requires weak auctions and/or SOFR-IORB positive; **the auctions were firm**, so distribution it is. Vector downgraded 3→2, "→4 ARMED" disarmed. **Stated plainly because it cuts against this thesis: dealers now have more capacity than BOND claimed for six weeks, so the demand-hole scenario is *less* pre-positioned than the standing write-up asserted** (KB-BND-096).
2. **The demand composition is rotating, and the June fade did NOT extend.** The June belly cluster faded hard (two of three tenors <60% indirect) — but every tenor tested since 7/9 has held or risen, and on 7/27 indirect **rose with duration** (2Y → 5Y). *Rotation to domestic directs, not a hole* — and the fade is not, so far, a trend. This is the leg most likely to turn, which is why every auction is graded on composition.
3. **Credit RE-ACTIVATED and then FULLY ROUND-TRIPPED — this item has now been rewritten in three consecutive versions and the churn is itself the finding.** v1.1.2 said credit was inert; v1.1.3 (7/28) said it had re-activated quality-*indiscriminately*; **v1.1.4 records that the whole episode reversed.** HY ran 268 → **287 (7/29 cycle high)** → **267**, i.e. *below where it started* and back near the 263 trough, while IG never participated in either direction. **"Credit re-activated" is retired at the index level.** What survived longest was the narrower claim — a quality-**discriminating** tail, CCC breaking 1000 to 1024 while the index retraced — **but that too has partly given back (1012), so the "making new highs" clause no longer holds either;** only the CCC/HY *ratio* made a fresh high (3.79x), and it did so because HY fell faster, not because CCC rose. Access unimpaired throughout: **zero pulled deals**, ~$56B of IG priced in the week to 8/14 without spread disruption. ⚠️ **The lesson to carry, not the level: this desk has now made and retired a credit call twice in three weeks off index prints that round-tripped. Credit is not currently a BOND signal, and saying so is worth more than a third rewrite.**

*(New in v1.1: the global leg — Japan's super-long demand vacuum — is channel 6 below. In the 6/20–7/1 window it transmitted via co-timing, NOT duration flows; the armed transmission risk is MOF FX intervention → mechanical UST reserve selling.)*

---

## TRANSMISSION CHANNELS

| # | Channel | Mechanism | Structural posture (regime-level) | Consumes / Feeds |
|---|---|---|---|---|
| 1 | **Auction health** | Demand hole → dealer warehousing → repo demand → funding stress | Below-median but **clearing at price** | → LIQUID, ZHAO |
| 2 | **Credit issuance / HY function** | OAS blowout → issuance freeze → refi wall → forced selling | **Access intact (zero pulled deals) but spreads re-activated 7/23** off a month-long flat range — and **quality-INDISCRIMINATE**, so the old "macro calm + bifurcation caveat" posture is retired: this is a repricing, not the CCC tail leading | → HENRY, REGINALD, BROCK |
| 3 | **Dealer capacity** | Inventory stock → backstop capacity → forced de-risk in a selloff | ⚠️ **RECORD RETIRED (7/28, figures refreshed 8/18)** — long-end stock **−14.3% off the 6/24 peak**, unwound *benignly* into firm auction demand. Dealers have **more** capacity than this desk claimed for six weeks, so the demand-hole scenario is **less** pre-positioned, not more. Auction *flow* benign. | → LIQUID, ZHAO |
| 4 | **Long-end / duration** ⚠️ **LABEL CONTESTED — see the banner at the top of this file** | Duration repricing, **driver disputed.** *(a)* **7/6→7/13** was a belly-led bear-**flattener** (30Y lagged) = higher-for-longer real **policy path**, term premium flat over the move — correct **for that window.** *(b)* **7/13→8/07** is a long-end-led bear-**STEEPENER** (2Y −7bp, 30Y +9bp) with daily Kim-Wright term premium at **~83% of the 10Y move** — the **term-premium** signature, on this desk's own falsifier. **⇒ The regime appears to have rotated; the label is CONTESTED ~50% and is NOT BOND's to resolve alone.** | Elevated, orderly (^MOVE *falling* into 19-yr-high yields), oil-independent (breakevens +3bp across a +33bp 30Y move) | → HENRY, LIQUID, NEXUS |
| 5 | **Credit-leads-equity (Hamilton ~3mo lead)** | HY OAS widens → precedes equity drawdown | **Inactive** — moves are equity-vol-led, not credit-led | → HENRY, VIOLET |
| 6 | **Global long-end / JGB-FX transmission** *(added v1.1)* | JGB super-long demand vacuum → (a) global term-premium correlation, (b) yen collapse → MOF FX intervention → mechanical UST reserve selling | **Armed via the FX leg, not duration competition** — window evidence shows JGB↔UST duration decoupling; the binding link is intervention risk | ← SAM; → HENRY, LIQUID |

*Live levels AND live state (colour scores) owned by STATUS (dashboard + convergence matrix); this column is the durable, regime-level structural read only — no dated numbers, to avoid drift.*

**Coverage extension (Will-approved 6/27, integrated 7/1):** BOND additionally owns **MBS/housing-finance + FHLB advances** (the rates↔housing relay and the regional-bank funding backstop — coordinate with REGINALD) and **Eurozone rates** (bund curve + ECB shocks — rates leg; LIQUID owns EU credit). Baselines + thresholds live in VX-BND-17/18/19 and the STATUS new-coverage panel; these feed the existing channels rather than adding new headline vectors until they earn matrix weight.

---

## ACTIVE EPISODE — long-end leg, phase III **established and sustained** *(was "forming"; it formed)*

**Timeline:** 30Y >5.0 for ~9 sessions + 10Y >4.5 for 6 (5/14–5/27) → **BND-07 TRUE** → mean-reversion → real-rate-led re-fire into the June refunding → relaxed post-refunding → the 6/16–6/18 gate resolved AGAINST a re-arm (20Y STRONG, hawkish FOMC bear-*flattened*: front-end +15bp, 30Y flat — BND-09 FALSE) → mid-window rally to a 7-week 10Y low (4.38, 6/26–29) → **phase-III re-fire 6/30–7/1**: +11bp/2d to 30Y 4.97 in a globally-synchronized move (JOLTS beat + ISM prices + Warsh Sintra + JGB super-long rout + supply concession into 7/7–9). → **July: the long end did NOT relax.** The 30Y went on to close above 5.00 for 8 consecutive sessions (7/7→7/16) and has now held above 5% for the longest stretch since 2007, while the 10Y sustained its arm line and the real leg made series highs. Each threshold firing has still been an **episode, not a one-way break** [[threshold_vs_mechanism]] — and that assumption survived its hardest test: **BND-12 resolved FALSE** (the threshold fired, the mechanism held). *(This sentence previously read "BND-12 pre-registers it at 65% for July" — a forward-looking claim about a prediction that has since resolved.)*

**Read (rewritten v1.1.3 — the 7/01 version of this paragraph said the real-rate leg was NOT the driver; that is now falsified and inverted):** (1) the leg is **domestic and real-rate-led, not imported** — the real curve moves belly-led on its own, and the arm has now survived an **out-of-sample oil test** (a ~11% crude collapse moved breakevens only, leaving the real leg flat), so Japan/JGB co-firing is a *correlation amplifier*, not the driver; (2) the **demand microstructure is softer but has NOT broken** — cover has thinned at the belly (a pre-registered trigger fired) while indirect participation has held or risen at every tenor tested since 7/9 and dealers have not been stuffed once; (3) **dealer long-end stock has UNWOUND from its record — the pre-registered downgrade fired 7/28** (11-21Y −17.4% off the 6/24 peak; long-end −9.0% over four consecutive weeks), and it unwound **benignly**, into strong end-demand rather than through forced liquidation. The "record dealer stock + no Fed backstop" pairing that made the long end look fragile is **half gone**: the Fed backstop is still absent, but the dealer inventory overhang is not. The genuine *break* still needs what it always needed: **a composition failure at a coupon auction** (indirect falling AND dealers absorbing) or a sustained threshold hold paired with funding stress. Warsh's active-MBS-sales supply leg stays deferred to a 2027 lane ("years, not months") — not a near-term amplifier.

**A third explanation is deliberately held open** *(v1.1.3)*: the cash-futures **basis trade shrank ~$1.3T → ~$1.0T**, and withdrawing repo-levered auction bid produces thin cover with intact composition — the 7/27 signature — without being either policy-path or term-premium. Auction reads must not be forced into that binary. LIQUID owns the call.

**Regime clarification (7/6): no Fed backstop at the coupon/long end.** QT **ended Dec-1-2025** (FOMC Oct-29-2025 decision; NY Fed 251210a). Post-QT the Fed **is** buying — but **T-bills** via Reserve Management Purchases (+ reinvesting MBS principal into bills), **not coupons.** So Fed purchases do **not** absorb 20Y/30Y supply — the coupon/long-end demand read is **unaffected by Fed buying**, and the 7/9 30Y reopen is absorbed entirely by private/foreign/dealer bids. This *sharpens* the demand-hole thesis: the one buyer who could paper over a weak long-end auction is structurally absent. *(Corrected across BOND surfaces 7/6 per PROME fix-packet + LIQUID KB-LIQ-070; KB-BND-069.)*

**BND-11 grade methodology (7/6, reconciled across three overlays — full spec `BND11_REFUNDING_PREREG_2026-07.md`, KB-BND-070):** (1) **LIQUID (absorption):** BOND + LIQUID grade the 7/9 30Y to **ONE figure — 30Y indirect as %-of-competitive-accepted vs the June-6/11 60.0% benchmark**; a *mechanically-clean* print (no tail, firm BTC) with indirect <55% + directs/dealers backfilling is the **masked demand-hole** (scores BND-11 TRUE but escalates the thesis). (2) **SAM (JGB leading indicator):** the JGB 30Y auction 7/7 (~2 days ahead) is a **term-premium *correlation* pre-arm, not a flow-seller** — it moves the US 30Y term-premium/tail leg, is near-silent on the indirect-composition leg (different buyer base), so it shifts the 7/9 prior only conditionally (weak JGB → benign ~58%) and **cannot fire an acute marker alone**; gated on US-10Y-7/8 confirmation. (3) **Circularity discipline:** JGB / 30Y-level / thin-bid are **one term-premium root, not independent votes** — don't double-count.

---

## EXIT / FALSIFICATION

> ⚠️ **RE-SPECIFIED 2026-07-28 (v1.1.3).** Every gate below was previously keyed on an **auction tail**. A tail requires the when-issued yield at the bid deadline and **TreasuryDirect does not publish it** — so those gates were **unscoreable from primaries by construction** and could never have fired on evidence. *(This is the same defect that made the HEN-42 joint falsifier pass by construction. The v1.1.3 header claimed this apparatus had been re-specified; on a full read it had not been — the header was corrected before the body. Fixed here.)* **All gates are now COMPOSITION-keyed and tail-free.**

**1. Thesis kill (exit all duration shorts):**
- A genuine auction **demand hole** = a **composition failure** — **indirect below the auctioned tenor's own trailing-12 MINIMUM *and* dealer above its trailing-12 MAXIMUM** — **AND** BTC <2.3 **AND** SOFR-IORB positive outside quarter-end. Mechanical failure, not repricing.
  ⚠️ **RE-SPECIFIED 2026-08-18. This gate previously hardcoded "indirect <56.4% AND dealer >13.2%" — which are the *7Y* trailing-12 cut-offs — while the KEY THRESHOLDS table three sections below instructed readers to "re-derive the cut-offs per tenor, don't reuse the 7Y numbers blindly."** The document was contradicting itself, and the contradiction ran in the dangerous direction: **the 7Y bar applied to a 10Y or 30Y auction is simply the wrong bar** (the 10Y's trailing-12 indirect min is 63.95%, the 30Y's is 59.52%, against the 7Y's 56.4%). The gate is now stated **as the rule, not as one tenor's instance.**
  **(NOT FIRING, and not narrowly: the August refunding cleared with indirect ABOVE median at all three tenors — the 30Y clears its own failure bar by 7.33pp. SOFR-IORB is +1bp on one print, inside its −3/+1 monthly range, and the leg is conjunctive so it cannot fire alone. Live → STATUS.)**
- OR 10Y back below **4.15** sustained 3 sessions with clean auctions → the repricing thesis is spent.

**2. Position-specific:**
- **TLT puts:** kill if 10Y <4.15 AND 30Y <5.0 for 3 sessions AND a clean refunding. **Re-arm conditional-add only on a composition failure at a coupon auction — indirect below that tenor's trailing-12 min AND dealer above its trailing-12 max** *(per-tenor, re-specified 8/18 with the thesis kill above — it had inherited the same hardcoded 7Y numbers)* *(was: "a fresh real tail >1.5bp + weak indirect <60%" — the tail leg was unscoreable and the 60% indirect leg was mis-calibrated, since 59.24% printed on 7/27 with demand plainly intact)*.
- **HYG puts:** June leg expired; stay closed — reopen only on HY OAS reclaiming 300 with velocity.

**3. Convergence downgrade (trim/de-escalate):**
- Long-end vector → 2 when 10Y <4.5 **AND** 30Y <5.0. ⚠️ **NOT currently met** — the "✅ met 6/15" stamp that sat here read as though the condition were live; both legs have been decisively breached since. Live → STATUS.
- Dealer absorption → 2 when the next FR2004 shows long-end inventory off the highs. **✅ FIRED 2026-07-28; the vector is scoreable and current through the 8/05 as-of.**
  ⚠️ **STALE-BLOCKER REMOVED 8/18. This line read "UNSCOREABLE — no FR2004 print pulled since the 6/17 as-of; 5 owed. The vector is blind" for 21 days after the gap actually closed on 7/28.** It was telling every reader — including this desk at boot — that a live, weekly, scriptable instrument was unavailable. **Same defect class as the `PROTOCOL.md` FR2004 line fixed on 8/15 (n=2), and the same class as the retired auction-tail: a document asserting an unavailability that has ceased to be true.** Pull it with `monitors/fr2004_fetch.py`; it resolves the API series break at runtime.

**★ v1.1.4 ADOPTION NOTE — partial, and the partiality is deliberate.**
Five spec changes were pre-committed on 2026-07-28 "for next session" and went **three sessions unadopted.** This version adopts **two of five** and explains why the other three are held:
- **✅ ADOPTED (d) — every branch set must carry a RESIDUAL branch.** No pre-registration ships again with a gap that leaves a plausible print ungradeable. (`BND-13` landed **0.03pp** from exactly that hole.)
- **✅ ADOPTED (e) — the margin must be stated on every leg at resolution**, so a knife-edge leg and a 13pp leg are never reported as the same verdict.
- **⏸️ HELD (a) indirect at the per-tenor 15th percentile, sufficient alone · (b) drop dealer as a bearish leg · (c) BTC confirmatory only.** **All three change what FIRES, and none has been base-rated.** Adopting a recalibration without first measuring its hit rate and separation against history is the precise defect this desk keeps logging (`finding_base_rate_the_threshold_before_building_it` — *"don't build it" is a real answer*). **The 370-row `data/auction_history_*.csv` corpus that would base-rate them is stale to 2026-05-28 and carries a known destructive-write defect (DAEDALUS, 8/17).** ⇒ **Refresh the corpus first, then base-rate, then adopt or reject.** Held, not dropped.
- **⏸️ HELD — VX-01 revert-rule speed** (one auction round-tripping a state vector). Now **n=2**: `VX-BND-01` round-tripped 2→3→2 in 11 hours on 7/28, and on 8/18 the dealer-absorption trigger fired on 11–21Y and was unfired by the very next print. **Two instances of the same shape is enough to design against, but the fix is a rule change and belongs with the base-rating above.**

**4. Time-based:**
- Each coupon-auction cluster (refunding weeks + 20Y/TIPS) is a mandatory re-grade of auction-health + long-end vectors.
- 60-DTE review on any options position.

---

## KEY THRESHOLDS (live values owned by STATUS)

*Live readings for every threshold below are in `STATUS.md` (dashboard) — the "State" snapshot column was removed to stop cross-doc drift.*

| Metric | Threshold | Implication |
|---|---|---|
| HY OAS | >350 / >500 | Issuance freeze / forced selling |
| HY OAS | >300 ×3 sess | Credit watch reopens |
| 5Y BTC | <2.3x | **Cover marker — NOT by itself a demand hole.** *(Empirically corrected 7/28: this line used to read "demand hole — mechanism stressed." The 7/27 5Y printed **2.28 and the mechanism did not fail** — indirect rose with duration, dealers were not stuffed. A cover breach escalates the vector; only a composition failure kills the thesis.)* NB: secular BTC decline ~3.0→2.5 per GAO, so 2.3x sits just under the new norm. |
| **Auction composition** | **indirect below the tenor's trailing-12 MIN _and_ dealer above its trailing-12 MAX** (of competitive accepted) | **End-demand weakness — THE demand-hole test.** ⚠️ **Stated as the RULE since 8/18; it previously read "indirect <56.4% AND dealer >13.2%" — the *7Y* instance — directly beside its own instruction not to reuse the 7Y numbers.** Current per-tenor mins/maxes (trailing-12, n=12): **3Y** 53.99 / 19.50 · **10Y** 63.95 / 16.16 · **20Y** 55.17 / 17.59 · **30Y** 59.52 / 17.46 · **7Y** 56.42 / 13.14. **Re-derive at each grade — these drift.** |
| ~~Auction tail~~ | ~~>2bp + dealer spike~~ | ❌ **RETIRED 7/28 — UNSCOREABLE.** No when-issued published by TreasuryDirect; a tail cannot be graded from primaries. Wire-reported tails are `[med-conf]`, recordable in notes, and **may never fire a gate.** |
| DFII10 (10Y real) | >2.5% sustained | Real-yield stress regime |
| T5YIFR (5Y5Y fwd) | >2.5% sustained | Inflation expectations unanchored |
| 10Y / 30Y | >4.5 / >5.0 held 5 sess + weak auction | Escalate long-end to 4 |
| SOFR-IORB | positive, sustained >+5bp | Auction stress → repo |
| Treasury buyback long-end accept-cap | **lifted** | YCC-lite / stealth long-end suppression → TLT-puts event |

---

## POSITION VIEW (live marks owned by STATUS/FORGE)

| Position | Posture | Why |
|---|---|---|
| **TLT puts** | **HOLD, no add** | *(Rationale rewritten v1.1.3 — it read "yields eased; adding here chases a relaxing move," which describes June and is the opposite of the current tape.)* The arm has **deepened**, not relaxed: the 10Y has held its line since early July, the 30Y is in its longest run above 5% since 2007 (**29 consecutive sessions**, with `^TYX` closing **5.31 on 8/17 — a 19-year high**), and the real leg is at a **post-2023 high** ⚠️ *(NOT a "series high" — that label was retracted 8/15 as wrong three ways: the all-time DFII10 max is 3.15 in 2008 and 133 pre-2026 observations exceed the 2026 max; `KB-BND-108`)*. **The reason not to add is not that the move faded — it's that no pre-registered add-gate has fired**, and the nearest (DFII10 >2.5) is single-digit bp away. Adding ahead of a fired gate is the discipline this book exists to enforce. TLT puts remain the cleaner vehicle than equity puts for a duration short [[feedback_put_vs_duration_expression]]. |
| **HYG puts** | Closed (June leg expired) | Credit transmission still absent at the *level*, but the "inert" premise is retired (v1.1.3): HY has re-activated off a month-long flat range, **quality-indiscriminately** — a repricing, not a credit-led move, and market access is unimpaired (zero pulled deals). Reopen the thesis only on **HY OAS >300 with velocity**. Live levels → STATUS. |
| **Credit-equity lead** | Inactive watch | Reactivate on HY OAS +75–100bp from trough while VIX <20. |

---

## PREDICTION SCOREBOARD (full set in `thesis/PREDICTIONS.tsv`)

BND-02 FAILED (issuance BOOM, not freeze) · BND-03 FAILED · BND-04 FALSE (CLO AAA never through SOFR+160; MM near-miss S+158) · BND-05 FAILED · BND-06 TRUE (HY <300 through May) · BND-07 TRUE (threshold fired; episode not break) · BND-08 FALSE · BND-09 FALSE (6/16 20Y STRONG) · **BND-10 VOID** (kinetic Iran events 6/25–27 met the pre-registered void clause; substantively, neither yield leg breached — recorded, not scored). **BND-12 FALSE** (7/18 — 30Y closed >5.00 for 8 consecutive sessions; **threshold FIRED, mechanism intact**, the model's hardest test passed the right way) · **BND-13 TRUE** (7/28 — 7Y cleared on frozen branch B, no composition failure) · **BND-01 FAILED** (resolved 8/15, 15 days late — HY never reached 350; window max 287, zero observations at or above the line, mechanism never engaged). ⚠️ **THE BOOK IS EMPTY as of 2026-08-15 and remains empty — zero OPEN predictions, with T6 and T7 running on frozen text. Nothing in the live regime is currently falsifiable on a BOND-authored instrument, and that is a standing gap, not a clean slate.** Working model — *auctions clear at price; composition holds* — has now held **twelve straight** benign tests (the twelfth being the **August refunding, 8/11–8/13, graded 8/18**) (BND-05/08/09 + 6/16 20Y + 6/18 TIPS + 6/23–25 cluster + **BND-11 7/9 refunding NOT FIRED** + 7/22 20Y-R + 7/22 40Y JGB + 7/23 10Y TIPS + 7/27 2Y + 7/27 5Y). *(Count was stuck at "seven straight" and undercounted the entire 7/22–7/27 run — corrected 7/28.)* ⚠️ **The 7/27 5Y is the one that earns an asterisk, not a discount:** it broke a pre-registered cover threshold (BTC 2.28) while its composition held, which is exactly the distinction the working model asserts — the model's *first real test*, passed. The other half of the model — *cash credit decoupled from the duration move* — is **no longer clean**: credit re-activated 7/23 and now moves with the broad repricing. · **BND-11 TRUE** (7/9 refunding cleared without a hard marker; indirect surged 77.7%). · **BND-12 FALSE** (resolved 7/18: 30Y closed >5.00 for 8 consecutive sessions 7/7→7/16 — threshold FIRED, but mechanism intact [BND-11 benign] = "expensive intensified, still not broken" per [[threshold_vs_mechanism]]; the sustained 30Y level = elevated term-premium LEVEL [ACM +0.73], while the arm MOVE was policy-path — consistent w/ the v1.1.2 relabel). **OPEN: BND-01** only (HY 350 by end-July) — **will resolve FAILED at the 7/31 close**; the gap is ~70bp and the current widening is nowhere near that pace. Live level → STATUS.

---

## CROSS-AGENT LINKS

| Direction | Agent | What flows |
|---|---|---|
| → LIQUID | Auction stress → repo demand; dealer-capacity exhaustion | 🔴/🟠 |
| → HENRY | Credit-equity lead; rate-expectations / term-premium read | 🟠 |
| → REGINALD | Issuance freeze → bank funding stress | 🔴 |
| → ZHAO | Auction weakness → foreign-demand-hole confirmation | 🟠 |
| ← LIQUID | SOFR/repo stress, reserve scarcity, energy-HY OAS | — |
| ← ZHAO | TIC, foreign UST flows | — |
| ← HENRY / HAWK | Vol regime, macro prints / geopolitical flight-to-quality | — |
| ↔ SAM | JGB long-end / BOJ / yen-intervention ↔ BOND's US-term-premium transmission read (channel 6) | 🟠 |
| ↔ REGINALD | FHLB advances → regional-bank funding backstop (new coverage) | — |

---

*Living document. Update when: a vector changes state, a prediction resolves, a threshold breaches, or the episode transitions. Version bump — major (X) = regime/conviction change; minor (Y) = refinement. Audit trail in `thesis/CHANGELOG.md`. Live levels owned by STATUS; one source of truth per metric.*
