# LIQUID — Thesis Changelog

## v2.0 — 2026-05-19
**Major revision after 32-day staleness gap (Apr 16 → May 18) and channel-migration finding.**

### What changed
- **Narrower active scope.** v1.0 implied LIQUID owned the full Treasury-market story (auctions, yields, foreign flows). v2.0 explicitly narrows LIQUID's active monitoring to: repo plumbing, credit spreads, public-BDC mark catch-down, APO co-trigger, basis-trade structural tracking. Yield curve and granular auction mechanics are flagged for BOND-primary (when active).
- **Channel migration as a first-class concept.** New §1 + §4 framing: the bear thesis transmits through whichever channel is currently active, and channel migration is normal (not thesis-abandonment). Operationally grounded in KB-LIQ-052: the Apr→May gap saw PLUMBING resolve mechanical (KB-LIQ-051) and DURATION become the active leg.
- **Bilateral credit framework.** v1.0 had only an escalation ladder upward (320 → 350 → 400). v2.0 adds the kill side: **260 KILL** with a five-rung trigger ladder (workbook/KILL_MEMO_HY_OAS_260.md), plus the **APO >$130 ×3 sessions co-trigger** (HEARTBEAT line 80). Reflects the squeeze-resolution path being a real risk worth its own kill condition.
- **Gamma-suppression caveat added.** New epistemic warning (§5, §9) — positive gamma may suppress VIX / HY OAS even while substance accumulates. Cross-verify too-calm prints during loud-substance windows. Origin: 5/14 Will/Prome signal.
- **BOND interface added.** New cross-agent receive line in §8 for when BOND stands up. Yield curve / term-premium / dealer positioning migrate to BOND-primary; LIQUID retains FOI-flow and basis-trade legs at the thesis level.
- **Channel-kill vs full-thesis-kill distinction.** v1.0 framework was monolithic. v2.0 explicitly: each channel can kill independently; full abandonment requires multiple legs failing concurrently.
- **Stagflation trap reinforced.** Brent $110.57 + 30Y 5.168% concurrent on 5/19 is the textbook configuration. Doc updated to cite current reinforcement, not just Mar 10 + Apr 7–8 double-confirmation.

### What stayed
- "Plumbing fragility — three structural buffers gone" remains the core frame.
- Three failure legs (Fed rate-control / FOI demand hole / basis trade) preserved as the structural setup. Re-labeled A / B / C and given current-transmission status, but the legs themselves are unchanged.
- Stagflation trap as structural finding.
- LIQ-01 (HY OAS 320 confirmation) preserved as the upside trigger.
- Kill condition logic on the macro side (Fed liquidity facilities, FOI resumption, ceasefire + oil) preserved.

### Drivers of the revision
1. **32-day gap (Apr 16 → May 18)** — exposed that LIQUID's primary channels can go dormant while the bear thesis continues firing through outside-domain channels.
2. **30Y broke 5% sustained** (May 5 = 5.046, first since 2007; 5/19 = 5.168 fresh life-high) — duration-channel transmission is real and current, not theoretical.
3. **APO co-trigger fired 5/12, missed for ~6 sessions** — exposed the operational risk of trigger-watch going dormant during agent staleness (new durable finding in §9).
4. **BOND agent scaffold created** (`AGENTS/BOND/`, May 2026) — formalizes the future migration of yield curve / market-structure scope out of LIQUID.
5. **Stage 3 PC narrative recognized** (Mar 25 inflection) + **FSK Q1 NAV -9.9%** (5/18) — moves Stage 3→4 transmission from "thesis projection" to "active watch."

### What this revision did NOT do
- Did not retire `STATUS.md`, `STRATEGY.md`, `MEMORY.md`, `KB.tsv`, or `KILL_MEMO_HY_OAS_260.md`. THESIS.md is the conceptual frame; operational layer untouched.
- Did not hand off any scope to BOND. BOND scaffold exists but is inactive; v2.0 names the interface but LIQUID retains all current active scope until BOND stands up.
- Did not change the position-level playbook in STRATEGY.md. Bilateral 320/260 framework was already there; v2.0 just elevates it from playbook-rule to thesis-doc.

---

## POV Pivots (intra-version)

> Reverse-chronological log of significant LIQUID point-of-view shifts that didn't trigger a full thesis-doc revision. Captures the trajectory of reads that would otherwise be lost when STATUS.md is pruned of historical narrative. Each entry: prior view → revised view, with the trigger that forced the update and the durable anchor (KB entry / file) where the finding now lives.

### 2026-08-23 — ★ Two legs graded DOWN on their own evidence; Leg C measured directly for the first time. Conviction 61% → **56%**

*(Logged 2026-08-23 after DAEDALUS falsification-sweep #2 flagged this file at 59 days. The gap was real and it mattered: **the X1 LIQUID half actually TAGGED during it** — the one event this thesis is built around — **and the log has no entry for it.** That is the standing falsification-logging item against this desk, and this entry is the repair. Entries below are what should have been written between 6/25 and now.)*

**What moved, in the order it happened:**

- **7/17 — Leg-A oil-beta path graded MISS (KB-LIQ-080).** The formal 7/11-12 Hormuz closure delivered the exact stagflation setup the pre-registration named (Brent $76→$86, +13%, 10Y ≥4.50) and HY **did not widen** (flat 267-272). Later **reframed by BRENT and accepted**: *"oil→**blended**-HY beta is weak, and the blend is the wrong instrument"* — a **masking** result, not a null. Bear-negative for the path; neutral for the leg.
- **7/27 — BROCK's wrapper-leads half FAILED independently**, and has not been revisited since. **This is the load-bearing one for X1**: X1 is CONJUNCTIVE, so with this half down **no HY level alone can fire it.** 🔴 **CONTESTED as of 2026-08-23 — do not read this half as settled DOWN.** BROCK's 7/27 failure was on **HY tranche decomposition**; my **BDC-mark card (KB-LIQ-083) graded CONFIRM tonight** on filing-primary Q2 10-Qs (5 of 6 NAVs down; 4 of 4 measurable FV/Cost down; the only name up on both is **MAIN, the pre-named control**) — and CONFIRM's own consequence is *arms the wrapper-leads half*. **Two instruments, one conceptual half, opposite answers; BROCK adjudicates (KB-LIQ-099).** ⚠️ **I retract my own stronger phrasing that X1 "cannot fire whatever the tape does" — that was said before I opened my own card.** Nothing fires today regardless: X1 needs HY >280 and HY is 275 [8/20]. *(This bullet was written earlier the same evening and is corrected in place rather than rewritten — the over-strong version is what I said to DAEDALUS and it should stay visible.)*
- **7/29 — ★ THE X1 LIQUID HALF TAGGED FOR THE FIRST TIME. HY OAS 287bps, sustain 3-of-3 (281→284→287).** The event the whole ladder exists for.
- **7/30 — …and it was ATTRIBUTED TO BETA (KB-LIQ-091), which is why the tag was bear-NEGATIVE on net.** The +19bp decomposes **68–84% broad DM HY beta · 15–30% AI/data-center · ~0% bank/CRE (HIGH confidence) · energy unmeasured.** ⇒ **The level fired on a mechanism the ladder was not built for.** A trigger that fires for the wrong reason is worse than one that doesn't fire, because it spends credibility without delivering information.
- **8/3 — the 280 line BROKE and has not been recrossed** (275bps [8/20], 13 sessions under). X1 un-armed on the level.
- **8/21-23 — ★ Leg B REPRICED, and this is the largest single change in this entry.** ZHAO **withdrew** the China-rotation mechanism on direct measurement (TTM: Treasuries −$91.3B **and Agency −$40.3B — both SOLD**; rho −0.025, n=41). The demand-hole refutation drops from **four independent ways to three + one conditional**, and the survivor holds only because **markets added back ~$107.3B** against −$118.9B of sales. ⚠️ **So Leg B's counter-evidence changed from STRUCTURAL to CONDITIONAL-ON-MARKETS-RISING — it dissolves in exactly the state where the leg would matter.** *(This cuts bear-POSITIVE for Leg B: the leg is less refuted than it was.)*
- **8/23 — ★★ Leg C (basis trade) MEASURED DIRECTLY for the first time (KB-LIQ-095).** June TIC splits foreign **official −$45.40B** against **non-official +$23.15B**: the demand hole is being **filled by a different holder class** — sticky/unlevered/mandate-driven replaced by price-sensitive/levered/repo-financed. **Leg C has been carried as an inference from leverage magnitude since v1.0; this is the first time the *substitution itself* is in the data.** ⛔ And it comes with a detector correction: **auction indirect % cannot see it** (bid-channel tag, not holder-class tag) ⇒ **the leg should be expected to surface as a funding/repo event, not a failed auction.**
- **8/23 — Leg C's nearest live hypothesis REFUTED (KB-LIQ-098).** BOND's KB-BND-092 (basis withdrawal caused the 7/27 5Y thin cover) fails twice: cause absent (pre-auction 5Y leveraged short change **−1.4% = the median of 19**) *and* mechanism does not transmit (**n=3 large cuts → median BTC 2.340 vs 2.350 otherwise**; the largest cut in the sample was followed by a **dead-median** cover with the 2nd-highest indirect on record). Bear-negative: a proposed transmission path for Leg C does not work.

**Net conviction: 61% → 56% (−5).**
- **−4 from the 7/29-30 pair.** The single most bear-constructive event available — the X1 half tagging — **arrived and graded as beta.** That is a substantive downgrade of the *transmission* claim, not of the tape.
- **−2 from BROCK's wrapper-half failure**, which makes X1 unreachable by any level alone.
- **−1 from KB-098**, removing a Leg-C transmission path.
- **+2 from Leg B/C.** Leg B's refutation weakened (bear-positive), and Leg C moved from inference to measurement — **a leg you can measure is worth more than a leg you assert, even at the same probability.**
- ⚠️ **Capped at −5 deliberately.** The structural roots are intact and one is at a live trip: **CCC >1000 continuously**, CCC−BB **872**, and a **verified +100bp like-for-like AI-credit repricing at issuer level** (CRWV DDTL 5.0→5.5, KB-LIQ-094). **What died in this window were PATHS, not the setup.** The honest description is **a narrower thesis with fewer live paths and one newly-measurable leg** — lower confidence, higher variance, not abandonment. Channel-migration frame (v2.0 §1/§4) intact and doing exactly the work it was written for.

**⚠️ Registered against myself:** three of the four downgrades come from evidence **I generated and graded as losses** (KB-080 MISS, KB-091 beta attribution, KB-098 refutation). That is the intended behaviour, and it is also the reason to check whether I am now over-correcting — **the counter-check is that the tape has not made a new low in CCC and the tail gap has not compressed**, so the structural read is not being contradicted, only the transmission stories.

**Anchored in:** KB-LIQ-080/091/094/095/096/097/098 · `analysis/2026-07-30_hy-attribution.md` · ZHAO packets 2026-08-21 (both, Will-ruled) · `workbook/DEALER_POSITIONING_NEXUS_WATCH.md` 8/23 grade · STATUS 8/23.

**⛔ Not done here, and owed: THESIS.md itself is still v2.0 (header 6/25) and its §3 Leg B/C text now understates both changes.** This entry logs the POV movement; **a v2.1 cut is a separate job.** Flagged rather than silently done, because re-versioning the thesis is not a changelog edit.

### 2026-06-25 — Conviction re-marked 60 → 61: anchor (FOMC) resolved; bear concentrated into a firming credit root widening toward its X1 confirm
- **Prior view (6/23, in THESIS):** Conviction 60% "held," explicitly *marked pending FOMC 6/17* — the acute credit-kill threat receded (HY bounced 263→265) but the structural root firmed to offset. Open Questions still posed FOMC 6/17 as the live conviction resolver.
- **Revised view:** FOMC RESOLVED (hawkish hold, no Fed put, dots hike-leaning, Warsh balance-sheet review reinforcing Leg A — KB-LIQ-060), so the anchor is gone; re-derived on the current board. **Argued both ways.** FOR the bear: the credit leg is now widening toward its OWN confirm-trigger (HY 263→**276** [6/24], 4bp from the >280 X1-decoupling) — a cleaner setup than the 6/23 kill-bounce; the structural root FIRMED (CCC-BB **798**, KBRA 2.3% record default, BDC non-accruals rising) with two fresh legs — the APO-broke-<$130 alts-crack (PC→public candidate) and the sector-wide PC 5%-cap redemption wall (MS PIF / Apollo ADS / Blue Owl OCIC-OTIC). AGAINST: the energy leg INVERTED (Brent ~$74, deflationary → the stagflation trap is one-legged); funding plumbing is CALM — the 6/24 metals selloff adjudicated a positioning WASHOUT, not a liquidity crunch (SOFR-IORB −3, CP-TBill +0.12, SRF $0); the duration leg needs a GROWTH break it doesn't have (KB-060); and the **X1 decoupling is still UNFIRED** — wrappers flat (BIZD $12.26), HY 4bp short, so the root stays single/macro and the widening is BETA not credit-substance recognition (KB-LIQ-062).
- **Net +1 → 61:** the load-bearing root (credit bifurcation) is firming AND the headline is now moving toward the confirm side rather than bouncing at the kill — directionally bear-constructive; capped small (not large) because the move is unconfirmed beta, three other legs are inverted/dormant, and the X1 conjunction hasn't fired. **Held to +1 (from a proposed +2) per Will/Prome calibration (6/25):** the two genuinely-new macro facts since 6/23 — energy inverting to a disinflationary force + the 6/24 metals selloff resolving as a washout that *confirms* calm plumbing — cut bear-NEGATIVE and roughly offset the new bear legs (APO<$130, PC redemption wall), and the credit widening is beta not substance (KB-062); so the move reads CONCENTRATED / higher-variance, not more-confident. Channel-migration frame intact — the thesis concentrated into the live credit channel rather than weakening.
- **Conviction:** 60 → 61.
- **Falsification standing:** CCC-BB <~400 falsifies the bifurcation (at 798); HY <260 sustained ≥3 fires the credit kill (16bp away, receded); the X1 decoupling confirms on HY>280 sustained AND BROCK wrapper-basket-leading (the named conviction resolver); ~7/25 Q2 BDC marks = the transmission confirm-or-falsify; June CPI 7/14 = the growth/disinflation test.
- **Trigger:** FOMC-anchor resolution + the 6/24 HY print (276) + the 6/24 WALTER intake (metals-washout adjudication + PC redemption wall) + APO breaking <$130.
- **Anchored in:** THESIS 6/25 header + Open Questions, KB-LIQ-060/061/062, STATUS 6/25, KILL_MEMO two-sided ladder.

### 2026-06-23 — Bear coiled tighter: headline kill receded, structural/substance roots firmed
- **Prior view (6/20, in STATUS):** "bear grinding the WRONG WAY on every active channel — risk-on/decoupling overwhelming the book; only the structural pins survive." HY OAS 263 = 3bps from the 260 soft-kill, compressing toward it; Trigger A one print away.
- **Revised view:** the acute credit-kill threat RESOLVED BENIGN — HY bounced off the 263 one-print low (266/266/265), TRIGGER A never fired, cushion back to 5bps stable. But the bear FIRMED, not weakened: (1) CCC-BB tail WIDENED to 791, the calm-senior/wide-tail signature replicating *simultaneously* across the HY index, the first European CLO 2.0 rated-tranche default (Bain Class F→D), and govvie term premium (2Y highest since Feb-25); (2) substance firmed (BROCK: KBRA default 2.3% record, BDC non-accruals up, wrapper recognition leaking); (3) a NEW AI/semi positioning unwind cracked the alts/PC complex (APO/ARES; HENRY HEN-35) = the candidate PC→public transmission. Headline channels (HY index, funding) stayed calm; vol + duration ticked the bear's way at the margin. The live load-bearing root is now the **credit-bifurcation tail**. Excess-liquidity "negative first since 2021" bear-re-arm validated NOT live (net Fed liquidity stable). Athene FABN canary = margin compression on the PC funding engine (not a PC positive).
- **Conviction:** held 60 — the kill-threat receding (a downside risk to the bear) offsets the structural firming.
- **Trigger:** 6/23 boot data refresh (FRED 6/22) + 6-agent cross-agent synthesis (HENRY/VIOLET/SAM/HAWK-BRENT/BROCK/NEXUS) + WALTER board lane.
- **Falsification standing:** CCC-BB <~400 falsifies the bifurcation (at 791); HY <260 sustained ≥3 closes fires the credit kill; the ~7/25 Q2 BDC marks are the named transmission confirm-or-falsify.
- **Anchored in:** STATUS 6/23 (Thesis-Kill Proximity + Dashboards), KB-LIQ-061 (Bifurcation_Signature_Replicates_Cross_Asset), MEMORY 6/23.

### 2026-06-17 — FOMC duration-transmission INVERTED: credible-hawkish Fed rallies the long end
- **Prior view (pre-staged FOMC_TIC_DECISIONTREE):** Hold + hawkish dots → 30Y re-establishes >5.00 (the long end sells off on higher-for-longer).
- **Revised view:** the mapping INVERTED. The hawkish-of-pricing dot flip (2026 median ~3.80; 9/18 see a hike by YE) repriced the FRONT end (2Y +16bps, largest Fed-day move since Mar-2008) while the LONG end RALLIED on anti-inflation credibility (30Y −2, toward the <4.90 unwind). The surprise hit rate-path expectations at the front, NOT the term premium at the back. A credible-hawkish Fed can RALLY the long end; the duration leg now needs a GROWTH break (not an inflation print) to re-fire.
- **Trigger:** FOMC 6/17 (Warsh debut, hawkish HOLD 3.50-3.75 unanimous; bear-flattener 2Y+16/30Y−2).
- **Anchored in:** KB-LIQ-060 (Credible_Hawkish_Rallies_Long_End), STATUS FOMC section, TIMELINE.

### 2026-06-12 — Duration regime re-derived from raw series; conviction 65% → 60%
- **Prior view (5/19 → 6/8, carried in STATUS/THESIS):** duration channel "ACTIVE — 30Y >5% sustained, 10Y >4.50 sustained" since the 5/18-5/19 regime break; on 6/8 written as the thesis's strongest leg ("matured from spike to regime").
- **Revised view:** the "sustained" framing was wrong from 5/28 onward. FRED-canonical record: 11 straight 30Y closes >5% (5/12–5/27, peak 5.18) — the TIMELINE bear test DID fire — then decay to a **5.00-pivot oscillation** (sub-5 closes 5/28–6/4 and 6/11; 10Y below 4.50 on 8 of 13 closes 5/26–6/11). Pre-registered unwind test (<4.90 sustained) untouched. The channel is oscillating between "durable" and "unwinding," testing the downside into FOMC 6/17. Companion reads, same pass: **Leg B is tenor-bifurcated** (June refunding: 10Y reopen indirect 78.2% STRONG vs 30Y 59.9% / dealer 14.7% SOFT-but-cleared, market rallied through it); **stagflation third test inconclusive-to-weak** (Brent −$22 → long end round-tripped to ~flat vs the 5/14 base; both anchors carried); **APO co-trigger fired 6/11 on closes (6/9–6/11) but is NOT Trigger C** — HY widened 274→280 into and through the fire window, concurrency fails; **oil-CPI loop REVERSED** (Brent $90.38 close 6/11 vs $110.59 peak) while May CPI printed hot on the lag (4.18% YoY).
- **Conviction 65 → 60, argued both ways:** confirming — PC substance accelerating (BROCK Stage 2→3, gate cluster, 3 div cuts, 6% default), stagflation texture (hot CPI + claims 210k→229k), JPY 4 closes >160, long-bond auction softness (dealer 14.7%). Weakening — duration decay (the leg my hold-at-65 leaned on), Brent co-driver gone, HY 20bps from the kill, belly demand strong (78.2%). Net −5. FOMC 6/17 is the named resolver: 30Y re-engages >5% or breaks toward the 4.90 unwind test.
- **Trigger:** coordinator-layer review (Orc) flagged the 6/11 closes (30Y 4.951 / 10Y 4.463); full-series recomputation then showed the error predated 6/11 — the 5/28–6/4 sub-threshold stretch had gone unrecorded by the agent (6/8) AND initially by the reviewer. Review loop surfaced three undeclared-basis variants in one day: FRED-vs-CBOE (yield edges), accepted-vs-announced (auction %s), adjusted-vs-raw (the agent re-graded APO's May streak on yfinance's dividend-adjusted default and "found" a 5/11 dip that never printed — raw record: **ten straight closes >$130, 5/8–5/21**, ex-div 5/19, caught by Orc 6/12).
- **Falsification standing:** 30Y >5% for ≥5 consecutive closes re-establishes the regime framing; <4.90 sustained fires the unwind branch.
- **Anchored in:** STATUS Dashboard 2 (corrected rows + source canon: FRED H.15 canonical, CBOE proxy), THESIS §3/§4/§5/§6/§9 (6/12 restamp), KB-LIQ-052 (framing flagged for re-derivation), auto-memory `finding_circular_corroboration_via_state_file` (extended).

### 2026-05-20 — Foreign-demand-canary refined
- **Prior view:** long-end break 5/13–5/19 (10Y 4.59, 30Y 5.12+ for 4 sessions, TLT fresh lows) was the foreign-buyer-exit canary firing; next leg would be auction-mechanism failure (BTC <2.50, indirect <55%, tail >2bps).
- **Revised view:** demand hole **compresses price** (term-premium digestion, expensive); it does **not break auction mechanism** under current conditions. Foreign demand shows up at the price the macro demands; term premium ratchets higher per absorption.
- **Trigger:** 5/20 20Y NEW issue ($16B, CUSIP 912810UV8) prints indirect 67.7% (strong), tail 0bp (stopped on screws), dealer 9.4% (clean) — under maximally-loaded macro (JPY 159+, Brent $111+, 30Y 5.12+ sustained).
- **Falsification standing:** tail >2bps confirmed by 2nd source would reverse. 5/21 10Y reopening Leg 2 is the corroboration test.
- **Anchored in:** KB-LIQ-057.

### 2026-05-19 — APO co-trigger watch went dormant during agent staleness
- **Prior view:** HEARTBEAT line 80 reassessment triggers (APO >$130 for 3 sessions OR HY OAS <260 sustained) were being watched; agent would notice if either fired.
- **Revised view:** Trigger-watch can go silently dormant during multi-session staleness. APO crossed >$130 on 5/8 and the co-trigger fired on 5/12 (Day 3). LIQUID was stale Apr 16 → May 18 (32 days); the trigger lived for ~6 sessions before live-tape re-verify caught it on 5/19. **Pattern:** on revival, don't trust the proxy's narrative summary alone — pull live values for every named threshold in HEARTBEAT line 80 and verify day-counts. A proxy synthesizing inbox items can cite "APO >$130" as macro context without computing the trigger ladder.
- **Trigger:** 5/19 live tape re-verification + APO 10-day yfinance pull showed Day 7 (now Day 9 as of 5/20).
- **Anchored in:** MEMORY.md Durable Findings; reinforced by 5/19 PM #1 session log.

### 2026-05-18 — Active transmission channel migrated PLUMBING → DURATION
- **Prior view (Apr 16):** SOFR-IORB +7bps breach was the next active channel; structural-vs-mechanical confirmation pending; plumbing dashboard yellow-flashing.
- **Revised view:** SOFR-IORB breach resolved mechanical (tax-day TGA build, not structural leak). The next leg fired through **10Y / TLT / Brent-reflation** instead. Bear thesis transmits through whichever channel is currently active; channel migration is normal, not thesis-abandonment.
- **Trigger:** 32-day gap revival showed 10Y 4.29 → 4.59 (+30bps), TLT $86.28 → $83.56, Brent $98 → $109, while SOFR normalized to 3.55% and SOFR-IORB re-flipped to -10bps.
- **Anchored in:** KB-LIQ-051 (SOFR resolved mechanical), KB-LIQ-052 (Duration regime break May 2026). Elevated to thesis-doc-level concept in v2.0 §1 + §4.

### 2026-04-16 — SOFR-IORB first cycle breach added as plumbing watch
- **Prior view (Apr 10):** Path A (squeeze resolution) winning. LIQ-01 at 290bps, 30bps below 320 trigger. Credit dashboard green. No active plumbing concern.
- **Revised view:** Plumbing dashboard yellow-flashing — SOFR 3.72 vs IORB 3.65 = +7bps positive (first cycle breach). Zero-RRP buffer thesis being tested in real time. Pending structural-vs-mechanical confirmation Apr 17-20.
- **Trigger:** Apr 15 SOFR print; 6-day swing of +11bps on SOFR (Apr 9 3.57 → Apr 15 3.72).
- **Resolution (May 18):** mechanical, not structural. Tax-day TGA build. KB-LIQ-051. The episode generated the now-durable pattern: 1-day SOFR-IORB sign flip on tax-day mechanics is NOT structural confirmation; apply same skepticism to quarter-end / settlement-window single-print breaches.

### 2026-04-10 — Path A (squeeze resolution) confirmation
- **Prior view (Mar/early-Apr):** HY OAS at 346 post-Q-end (Apr 1), bear thesis tracking the LIQ-01 confirmation path toward 320bps. Credit transmission active.
- **Revised view:** Path A (seasonal squeeze unwind) winning. HY OAS reverted 346 → 285 over 2 weeks. Credit/VIX divergence resolved. PC Stage 3 cascade public-equity sentiment decelerating (APO +15.9% over 6 days, BIZD +4.9%).
- **Trigger:** Apr 1 → Apr 10 tape; sustained HY OAS compression below 290.
- **Anchored in:** Durable Signals Log "HY OAS post-Q-end reversion" entry (preserved in KB.tsv lineage). Became the precondition that the *Apr 16 SOFR breach* read against.

---

## v1.0 — 2026-04-08
**Initial thesis document created.**
- Extracted core thesis from STATUS.md, CREDIT_THRESHOLDS.md, IDENTITY.md
- Triple failure point framework documented
- Transmission channels cataloged with current status
- Stagflation trap DOUBLE CONFIRMED (Mar 10 + Apr 7-8)
- Key thresholds and invalidation conditions defined
