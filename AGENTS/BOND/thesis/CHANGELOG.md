# BOND THESIS — Changelog

Version history for `thesis/THESIS.md`. Newest first. Bump rules: **major (X.0)** = regime change / conviction reversal / channel restructure; **minor (X.Y)** = refinement, threshold update, prediction resolution. Every entry logs old view → new view.

---

## v1.1.9 — 2026-08-27 (later — Will rules the kill-scope question v1.1.8 left open; the legs EXTEND, prospectively)

**Old view → new view:** v1.1.8 adopted the MATRIX_V2 legs for the **escalation matrix** and deliberately left the **thesis kill** untouched, with the scope question flagged to Will and no action pending → **Will ruled the legs EXTEND to the kill's composition-failure test.** There is now **ONE composition-failure definition on this desk**: *indirect below that tenor's own trailing-12 **15th percentile**, sufficient alone*, with **dealer dropped as a bearish criterion**. Conviction unchanged. No position moved. $0.

**Will's word:** *"go with your rec"* — on PROME's presentation of WILL_QUEUE row 93. Canonical record: `PROME/proposals/2026-08-27_matrix-v2-kill-scope-RULED.md`.

**The three ruled parts**
1. **EXTENDED, PROSPECTIVELY** — governs matrix AND kill for auctions graded **from 2026-08-27 forward**.
2. **HISTORY PRESERVED** — the 18 consecutive benign resolutions since 7/9 are **not re-scored**; they stand as graded under the definition that graded them.
3. **DUAL-PRINT** — both definitions reported side by side until the kill next evaluates (~9/8–9/10 cluster), so the difficulty shift is on the face of the record.

**Live state under both, as encoded in STATUS**
| Definition | Test | State |
|---|---|---|
| OLD (retained for the dual-print) | ind < trailing-12 MIN **AND** dlr > MAX | 18 consecutive benign since 7/9; no failure at any tenor |
| NEW (in force 8/27 forward) | ind < trailing-12 **15th pctile**, standalone | n=1 — the 8/27 7Y printed **60.78%** vs its **57.24%** bar, clean by **+3.54pp** |

**The two definitions agree on today's state**, and the counterfactual on the three dark-session prints was **computed, not asserted** (`I'` would have fired on none: 2Y +10.26pp · 2Y-R +10.44pp · 5Y +2.03pp clear). **So the re-definition changes no live verdict — luck, not vindication.**

🔴 **Direction disclosed, because this is the change that needs it.** The new test is **strictly easier to fire** — the bar rises (7Y 56.42 → 57.24) *and* the dealer conjunct that vetoed it is removed — **and the kill firing is what CONFIRMS this desk's own standing bear thesis.** BOND halted on precisely this and asked rather than ruling it; the ruling record names the halt as part of why the ruling is clean.

⛔ **What was NOT extended — flagged to PROME, not self-ruled.** Three live uses of "composition failure" sit outside "matrix AND kill" and were left governed by the OLD conjunctive test:
- the **TLT-put ADD re-arm** (`TRADE.md`) — an *add* gate on a live position under Will's standing 7/16 NO-ADD; loosening it is the same direction-of-benefit problem, one hop over;
- the **outbound cross-agent trigger** (`CLAUDE.md` signals table, `PROTOCOL.md`) — a routing spec that tells LIQUID/ZHAO what BOND is claiming;
- **`grade_auction.py`** — still computes the old conjunctive test; **unpatched deliberately.** Until the kill next evaluates, the tool's print *is* the OLD-definition half of the dual-print — **useful, and not the authority.** Patch owed before the old print retires.

**Untouched:** the kill's other legs (BTC <2.3, SOFR−IORB positive), every frozen pre-registration (`BND-18/19/20` grade on their own frozen letters), the composite, and every score.

**Late same-day addendum (no version bump — a caveat attached to existing evidence, no thesis change, no threshold moved).** Channel 4's evidence cell carried daily Kim-Wright term premium as *"~83% of the 10Y move"* with no denominator. Recomputed across four windows at the FRED primary (`KB-BND-204`): the share is a ratio over a **3bp** 10Y move, and the same statistic returns **337%** on 7/13→8/25 (10Y +2.0bp) and **220%** on June (10Y −3.0bp) — noise wearing a percentage sign. ⇒ **The cell now carries KW-TP in bp (+2.5bp) with the share demoted and the denominator stated.** The substantive claim is unchanged: 7/13→8/07 is a long-end-led bear steepener (2Y −7bp, 30Y +9bp), which is the term-premium signature on this desk's own falsifier, and `C-36` remains Will-ruled **CONTESTED ~50%**. ⚠️ **Recorded because the rule was issued to RED first and applied here second** — a caveat sent outward and not encoded inward is the asymmetry this desk logs.

---

## v1.1.8 — 2026-08-27 (the Will-ruled MATRIX_V2 adoption is EXECUTED; the 8/25–27 cluster graded)

**Old view → new view:** the escalation matrix's auction leg could only escalate through a **conjunctive** composition-failure test (indirect below trailing-12 MIN **AND** dealer above MAX) whose base rate is near zero by construction → **indirect alone, at the per-tenor 15th percentile, now fires 🟠 standalone**, and **dealer is no longer a bearish criterion at all**. Conviction unchanged. No threshold moved on any live position. No composite move.

**What landed**
- ✅ **§1 + §3c ADOPTED**, executing Will's 2026-08-20 ruling (*"Approved on both - implement per your rec"*). Registered **PRE-PRINT** against the 1PM 8/27 7Y: `I'` fires at **indirect <57.24%** of competitive accepted (trailing-12, 2025-08-28 → 2026-07-28, n=12). Dealer retained as **descriptive** and as a contrarian-**bullish** note >18%. Full working → `analysis/2026-08-27_MATRIX_V2-adoption_and_8-25-27-cluster-grade.md`; `KB-BND-173`.
- **Convention resolved rather than picked.** §3d specifies %-of-**offering**; this desk grades %-of-**competitive-accepted**. Both computed: **57.15 vs 57.24 — a 0.09pp gap**, because competitive accepted is 99.75–99.90% of offering at all twelve 7Y auctions. Adopted on competitive-accepted; a print inside that band is reported CONVENTION-DEPENDENT and graded both ways.
- **The 8/25–27 cluster graded** — 8/25 2Y, 8/26 2Y-reopening, 8/26 5Y, all 🟢 CLEAN, no cover marker, no composition failure. **17 consecutive benign coupon resolutions since 7/9** (14 as recorded 8/21, +3). `KB-BND-172`.
- **`BND-18` TRUE** (+0.03, and the same print is −0.00 against the trailing-12 *mean* — a thin hit, reported as thin). **`BND-19` FALSE**, broken on the 5Y leg **by 0.24pp**, all three legs recorded as the registration requires. **`KB-BND-092` closed REFUTED-AND-MOOT** on LIQUID's pre-registered B2 branch, frozen 3 days before the print (`KB-BND-177`).

**What was NOT done, and why — the three that matter**
1. 🔴 **The thesis kill's dealer leg is UNTOUCHED.** Read widest, "drop dealer as bearish" would strip it from the kill — **making this desk's own bear thesis easier to confirm.** Escalation-matrix scoring ≠ licence to loosen a **kill criterion on a live position** in the author's favour; `TRY-FIRE-004` is live. **Flagged to Will as a question; no action pending.**
2. 🔴 **The adoption was owed at the pre-registrations PLURAL and TWO of four printed un-adopted** (desk dark 8/24–8/26). Rule is **forward-only** per §3d's own audit rail and was **not** back-applied. **Counterfactual computed, not asserted: `I'` would have fired on none of the three.** The slip changed no verdict — **luck, not vindication.**
3. ⚠️ **The rule's bite is uneven and the adoption did not predict it.** `I'` sits above the trailing-12 min by **+4.84pp (2Y) / +0.82pp (7Y) / +0.24pp (5Y)** — at the 5Y it barely loosens anything. **One rule, three strictnesses** ⇒ the 9/4 base-rating **must report per tenor, never pooled** (`KB-BND-174`).

**Two live-value defects removed from this durable doc, found while editing it.** The Status line declared THESIS *"deliberately carries none"* of the live values two sentences after carrying **"29 consecutive `DGS30` sessions"** — a figure **retracted 2026-08-15** and standing at **36** when found — plus a stale **−14.3%** dealer drawdown (live −14.8%). Both replaced by pointers to STATUS. ⚠️ **The disclaimer is what made it dangerous: it stops the reader checking.**

**Still owed:** MATRIX_V2 **base-rating by 9/4** (Will-ruled, per tenor) · quarterly percentile-snapshot table in `monitors/AUCTION_HEALTH.md` by 10/1 · a direct-take base rate for 2Y reopenings (`KB-BND-175`) · **(c) BTC-confirmatory-only remains genuinely HELD, not ruled.**

---

## v1.1.7 — 2026-08-21 (Will-tasked audit of THESIS: four corrections, one of them a superseded GOVERNANCE state)

**No conviction change. No threshold moved. No channel added or removed.** This is a corrections release, and the corrections are listed worst-first.

**1. 🔴 A SUPERSEDED GOVERNANCE STATE — the worst of the four, and it is not a number.** The v1.1.4 adoption note recorded legs **(a)** *indirect at the per-tenor 15th percentile, sufficient alone* and **(b)** *drop dealer as a bearish leg* as **⏸️ HELD, "none has been base-rated."** **Will RULED implement on 2026-08-20** — verbatim *"Approved on both - implement per your rec"* (DAEDALUS MATRIX_V2 structure review): **§1 = drop dealer-as-bearish entirely, §3c = indirect sufficient ALONE at the 15th per-tenor percentile**, both landing at the **8/25–27** auction-cluster pre-registrations. **A durable doc carrying a dead governance state is worse than one carrying a stale number: a reader will re-check a level, and nobody re-checks whether a ruling landed.** *(c) BTC-confirmatory-only remains genuinely HELD.*
   🔴 **AND THE SEQUENCE IS THE POINT — caught on a same-session double-check of this very correction, not on the first pass.** The ruling has TWO dated items, not one gated on the other: **ADOPT §1/§3c at the 8/25–27 pre-registrations** *and* **DELIVER the base-rating by 9/4.** **That deliberately INVERTS this desk's standing base-rate-first default**, and the v1.1.4 text preserved in THESIS still reads *"the hit-rate and separation measurement is owed before any of (a)/(b)/(c) ships"* — **a precondition the ruling supersedes.** My first correction said only "no longer HELD" and left that contradiction standing for a reader to hit. The measurement is still owed — **by 9/4, after adoption, not before it.**
   ⚠️ **OPEN ITEM, flagged rather than quietly skipped:** BOND pre-registered `BND-18/19/20` for this cluster on 8/21 **without** adopting §1/§3c. Those are BOND's own predictions and are unaffected — **but the ruled MATRIX_V2 adoption is separate and still owed before 8/25.**

**2. A PREMISE ASSERTED IN THE BODY THAT THIS FILE'S OWN HEADER HAD ALREADY QUALIFIED.** *"Regime clarification (7/6): no Fed backstop at the coupon/long end"* stood flat in the ACTIVE EPISODE section while the v1.1.6 version note at the top already recorded that `VX-BND-16` fired on 8/19 and that long-end absorption is **no longer entirely private/foreign/dealer** from 9/9. **Upstream qualification present, in-place amendment absent** — the same shape DAEDALUS flagged on `NEXUS_BRIEF` the same day, and the third file found carrying it. Qualified in place; still *threshold fired, mechanism NOT confirmed.*

**3. FR2004 vintage 8/05 → 8/12, in TWO places (lines 52 and 107) — the 7th and 8th surfaces found a print behind.** One was missed by the very guard built that morning: `check_fr2004` scanned the live surfaces and **skipped the durable docs.** Coverage extended to `THESIS`/`PROTOCOL`/`CLAUDE.md` the same session, and the extension immediately found the 8th. **The derived figure was stale too** (−17.1% off peak; live −20.9%) — a derived figure does not inherit a level fix.

**4. The thesis-kill's SOFR−IORB leg still cited `+1bp on one print`.** It fully reversed — **+1 [8/17] → 0 [8/18] → −3 [8/19] → −2 [8/20]** — so the funding leg is **no longer met on its letter and all three kill legs are un-met simultaneously.** STATUS and TRADE were corrected on 8/21; this durable doc was not.

**Also:** prediction scoreboard re-mirrored (`BND-18/19/20` were registered 8/21 and missing here — the same mirror break found on `STATUS.md` hours earlier), and the retired **`FAILED`** token annotated (the ledger canonicalised on **`FALSE`**; carrying two tokens for one state silently breaks every count of resolved outcomes, calibration included).

**What was checked and found CLEAN:** the no-live-values rule — **zero date-stamped numbers in the whole document**, with both the KEY THRESHOLDS and POSITION VIEW sections explicitly delegating live readings to STATUS. That discipline held.

---

## v1.1.6 — 2026-08-20 (VX-16's RED trigger FIRED — the long-end buyback cap was lifted; one load-bearing premise now qualified)

**One structural change and one confirmation. No conviction move.**

**1. 🔴 `VX-BND-16`'s registered RED trigger FIRED on 2026-08-19 and this document did not know it for a day.** Treasury `sb0607` **doubled** the long-end liquidity accept cap, **$2bn → ≥$4bn/op** (10-20y AND 20-30y nominal, window 9/9→11/4), verified at the primary. The vector read score 1 and `TRADE.md` still said *"($2B cap held.)"* until 2026-08-20; found by DAEDALUS's Will-directed structure review.

**Graded the way this desk is built to grade: THRESHOLD FIRED, MECHANISM NOT CONFIRMED.** The measurable clause is met, so `VX-BND-16` moves **1 → 4**. The interpretive clause in the same trigger cell — *"YCC-lite / stealth long-end suppression"* — is **rejected on the letter**: capped size, dated window, **no yield target**, no unlimited commitment. YCC's defining feature is an elastic quantity pledged at a price; this is a fixed-ish quantity with no price. Adopted premise: **liquidity-support on the letter, yield-reactive in timing.** Flip conditions **F1/F2/F3** registered, none resolved. ⚠️ **Spec defect named: the trigger FUSES a measurement with its interpretation in one cell**, so "did it fire?" has no clean answer — scored **4, not 5**, because 5 would import a label rejected on evidence the day before (`KB-BND-099` class; re-cut goes into the 8/25–27 cluster under the Will-ruled MATRIX_V2 adoption).

**⇒ THE THESIS CONSEQUENCE, which is real regardless of the label.** This document's post-QT section argued that with the Fed buying only T-bills, **long-end absorption is entirely private/foreign/dealer** — no coupon backstop. **From 9/9 that is no longer true.** An official bid sits in 10-30y through 11/4. The premise is **QUALIFIED, not removed**: the bid is capped, dated and small against the stock (~$32–40bn over the window vs a $31.45T stock and $16B per tenor per month), so it is a flow nudge, not a backstop. But "entirely" was doing work in the argument and it is no longer accurate. **It also contaminates curve-shape attribution for policy-path-vs-term-premium from 9/9 — which is precisely why HEN-42 must resolve on schedule (8/29) and must not extend.**

**2. The 14th straight benign demand resolution, and the strongest single one.** The 8/20 30Y TIPS reopening (`912810US5`, $8B) cleared with **indirect 84.45% of competitive accepted — the highest of the 7 held 30Y TIPS** (prior max 78.30) — with **BTC 2.82** (prior max 2.78) and **dealers at 2.10%, BELOW the prior MINIMUM of 2.49.** `BND-17` **RESOLVED TRUE, +8.28pp**. This was the cleanest real-money referendum available on the real-yield level, taken with **DFII10 at 2.41**, near the top of its post-2023 range: **real money did not balk at the level.** ⚠️ *Superlative scope: series 30Y TIPS · basis %-of-competitive-accepted · window 2023-02-16→2026-08-20 · n=8. 30Y TIPS predate 2023 — the earlier window is UNCHECKED, not unavailable. `re-test: 2026-09-20`.*

**3. ⚠️ A CALIBRATION SIGNAL THAT BEARS ON THIS THESIS AND IS RECORDED HERE RATHER THAN BURIED IN THE PREDICTION BOOK.** Two consecutive auction pre-registrations landed on the **wrong side of a benign outcome, both in the same direction**: `BND-14` FALSE at 60% (over-confident bearish, 8/19) and `BND-17` TRUE at 45% (under-confident benign, 8/20). **This desk keeps pricing auction demand WEAKER than it prints.** n=2 is not a verdict and nothing is adopted on it — but the thesis's own discriminator (composition failure) has now failed to fire **14 consecutive times**, and the standing question raised to Will on 8/20 is whether that run is information about the **EXPRESSION** rather than noise. **Registered as an open question, deliberately not resolved here.** Natural adjudication point: **8/29**, when T6 and HEN-42 both resolve.

**No conviction change. No threshold moved. Composite 12/35 unchanged.**

---

## v1.1.5 — 2026-08-20 (sub-channel 6(a) MEASURED; the v1.1.4 blocker found discharged)

**Two changes, neither a conviction move.**

**1. Channel 6(a) 'global term-premium correlation' is measured for the first time, and it is WEAK for Japan.** Prompted by SAM's CH-016 scope defect (their two-hypothesis test cannot see a global common factor). BOND's first attempt — rank of cumulative Δ across sovereigns over a window — **failed as an instrument**: 7 one-week windows gave 7 distinct orderings and the HORIZON flipped the conclusion (`KB-BND-148`). **The diagnosis was that the estimator, not the data, was broken:** rank discards magnitude, so near-tied legs shuffle on noise, and the lookback was a free parameter that let the analyst pick the answer.

**Replaced with a factor decomposition on DAILY changes** (n=239 aligned days, 2025-08→2026-08; DM factor = mean standardized daily Δ of US/EA/UK 10Y, Japan excluded from the factor so the test is not circular):
  · **R²: US 66.6% · EA 77.8% · UK 78.6% · JP 6.8%** — betas 3.74 / 3.21 / 4.88 vs **JP 0.92** bp per 1σ
  · pairwise daily-Δ correlation **JP–US 0.11** vs **EA–UK 0.74**
  · episode 7/13→8/18, three-way split of Japan's **+14.8bp**: drift **+13.3** · **common factor only +1.6** · idiosyncratic ~0
⚠️ **A non-synchronous-trading artifact was hypothesised and REFUTED** — lagging Japan to the prior US session makes correlations *worse*, not better. The decoupling is real.
⚠️ **Caveats that travel:** this is the **10Y**, while channel 6 names the **super-long** — a proxy, not the thing itself. Episode window n=24. Betas assume stability over the estimation year. AU excluded (weekly file cadence).
⇒ **Consequence:** a global common factor is a weak explanation for a JGB move and correspondingly weak as a channel into the US long end. **This CONTRADICTS BOND's own 8/20-morning read** ('Japan below the DM median ⇒ evidence toward a common factor'), which was a one-week rank artifact and is retracted (`KB-BND-145` → CORRECTED, `KB-BND-148`).

**2. The v1.1.4 ADOPTION-NOTE blocker was itself stale (n=3 of the class).** It held (a)/(b)/(c) + the VX-01 revert-rule on *"the 370-row corpus is stale to 2026-05-28 and carries a destructive-write defect."* **Both halves false:** 390 rows through **2026-08-13**, refreshed 8/18 21:44, and **structurally intact** (uniform width, zero ragged rows, proper terminator). **The base-rating has been unblocked since 8/18 and nobody knew.** ⚠️ **Nothing adopted** — the base-rating is real work, still owed. Same shape v1.1.4 itself fixed for FR2004.

---

## v1.1.4 — 2026-08-18 (staleness sweep: the 8/10 regime downgrade was MISSING from this document for 8 days; an internal contradiction, a stale unavailability blocker, and a hardcoded-single-tenor kill gate all fixed)

**Trigger:** Will-tasked full staleness sweep of every BOND core document, run after a boot found the long end at a 19-year high and the August refunding ungraded.

**⚠️ The headline is a process failure, not a market call: `STATUS.md` carried the 8/10 C-36 downgrade and THESIS did not.** For **8 days** the durable document — the one a reader consults for the standing argument — asserted "policy-path-led" as settled canon, including an explicit instruction *"do NOT restate this as term premium."* The desk had already moved that label to **CONTESTED ~50%.** *(Flagged as a risk in the 8/15 closeout — "THESIS has not been read end-to-end since 7/28 and the 8/10 downgrade may not be reflected in it — flagged, not assumed." It was not reflected. The flag was right and the verification was owed a session earlier.)*

| # | Old view | New view | Basis |
|---|---|---|---|
| 1 | **Label:** "real-rate / higher-for-longer (policy-path-led)", stated as corrected canon; readers instructed not to say "term premium" | **CONTESTED ~50%**, banner at the top of the file; the do-not-say-term-premium instruction **suspended** | 8/10 forum, Will-ruled in-session |
| 2 | Channel 4 posture: policy-path-led, term premium "flat over the move" | **Driver disputed and window-dependent.** 7/6→7/13 belly-led flattener (policy path — stands for its window); **7/13→8/07 long-end-led STEEPENER with term premium ≈83% of the 10Y move** | FRED `THREEFYTP10` (daily Kim-Wright), added to the dashboard 8/18 |
| 3 | Status line: *"dealer long-end inventory is at a record"* | **Record retired; long-end stock −14.3% off the 6/24 peak** | ⚠️ **This CONTRADICTED item 1 of the same document, which had recorded the record as unwound on 7/28.** An internal contradiction that survived 21 days |
| 4 | Thesis kill + TLT re-arm: **"indirect <56.4% AND dealer >13.2%"** | **Indirect below the tenor's own trailing-12 MIN and dealer above its MAX** — stated as the rule | ⚠️ Those were the **7Y** cut-offs, hardcoded as if general, **directly beside the file's own instruction not to reuse the 7Y numbers.** The 10Y's indirect min is 63.95% and the 30Y's is 59.52% — the 7Y bar applied to them is simply the wrong bar |
| 5 | Dealer-absorption downgrade: *"UNSCOREABLE — no FR2004 print pulled since the 6/17 as-of; 5 owed. The vector is blind"* | **Fired 7/28; scoreable weekly and current through the 8/05 as-of** | ⚠️ **A stale unavailability blocker, live for 21 days after the gap closed** — telling every reader, this desk included, that a working scriptable instrument was unavailable. **n=2 with the `PROTOCOL.md` FR2004 line fixed 8/15** |
| 6 | Credit: "re-activated, quality-INDISCRIMINATE" | **Fully round-tripped** — HY 268 → 287 → **267**, below where it started; the CCC tail's "new highs" clause also gone (1024 → 1012) | FRED direct, 8/14 |
| 7 | Working model: **eleven straight** benign tests | **Twelve** — the August refunding ($125B, 8/11–8/13) cleared with **no composition failure at any tenor**, the 30Y clearing **5.216%, highest since 2001**, clearing its own failure bar by **7.33pp** | TreasuryDirect primaries, graded 8/18 (5 days late) |
| 8 | Prediction scoreboard ended at BND-11 | **BND-12 FALSE · BND-13 TRUE · BND-01 FAILED**, and the book is **EMPTY** — zero OPEN predictions with T6/T7 running on frozen text | `thesis/PREDICTIONS.tsv` |

**Spec changes: two of five adopted, three held — see the ADOPTION NOTE in THESIS §EXIT/FALSIFICATION.** Adopted **(d)** mandatory residual branch and **(e)** per-leg margin at resolution — both pure discipline, no calibration risk. **Held (a)/(b)/(c)** because all three change *what fires* and **none has been base-rated**, and the corpus that would base-rate them (`data/auction_history_*.csv`, 370 rows) is **stale to 2026-05-28 with a known destructive-write defect.** Refresh → base-rate → then adopt or reject. Also held: the VX-01 revert-rule speed question, now **n=2** (VX-01 round-tripped 2→3→2 in 11 hours on 7/28; the dealer trigger fired and was unfired by the next print on 8/18).

**No conviction change, no position change.** TLT puts HOLD, no add; Will's 7/16 NO-ADD stands; composite unchanged 12/35 with no vector moved. **The label is CONTESTED and BOND has not moved it — that is forum/Will-gated, and the 8/10 ruling carries an explicit guard-rail against exactly the conflation this new evidence invites.** Routed to HENRY (HEN-42 resolves 8/29 on the same question) and PROME.

---


## v1.1.3 — 2026-07-28 (falsifier RE-SPECIFIED after a self-caught mis-specification; oil→breakeven confirmed out-of-sample; credit re-activated)

**Triggers:** HENRY's 7/28 challenge that the joint HEN-42 falsifier "passed on its letter but not on its evidence" + the 7/27 2Y+5Y grade off TreasuryDirect primaries + a 12-item mail drain that surfaced two stale load-bearing values on BOND's own surfaces.

> ### ⚠️ AMENDMENT, same day (~04:45 ET) — two things this entry got wrong about itself
>
> **(a) Item 1 below was not true of the file when it was written.** The bump declared the falsifier apparatus "re-specified from tail-keyed to composition-keyed" after only the THESIS *header* had been changed. A full read that afternoon found **three tail-keyed gates still live** in the body — the thesis kill, the TLT-put re-arm, and the KEY THRESHOLDS table. They are fixed now, so the claim is true *retroactively*, but it was **a version bump that described intent rather than the artifact.** Recorded because the CHANGELOG's whole job is to be checkable against the file.
>
> **(b) The replacement is itself defective, and I found out from my own backtest.** `proposals/MATRIX_V2_DRAFT_prome-spawned.md` — APPROVED DESIGN, May-2026, never implemented — rests on a **323-coupon-auction backtest (2023-01 → 2026-05, TLT 5d outcomes)** and says: **`dealer >12%` is wrong-signed as a bearish trigger** (dealer>20% median TLT 5d **+1.45%**, contrarian-bullish), and **indirect is the single best signal, sufficient ALONE, at the 15th per-tenor percentile.** The v1.1.3 gates use **dealer >13.2% as a bearish leg**, make **indirect conjunctive**, and set indirect at the trailing-12 **minimum** — **all three push the gate toward NOT firing.**
>
> **So v1.1.3 traded an *unfireable* apparatus for a *hard-to-fire* one.** The direction of the residual bias is toward confirming the policy-path call BOND already holds, which is the worst possible direction for it to run in. **The 7/28 7Y pre-registration is NOT being edited** (registered as `BND-13`, routed to HENRY/NEXUS); the challenge is logged pre-print in `analysis/2026-07-28_grade_…` §4b with the resolution rule fixed in advance. **v1.1.4 will adopt the 15th-percentile indirect rule with `I'` sufficient alone and drop dealer as a bearish criterion — after the 7Y grades, so the change cannot be accused of being fitted to the print.**
>
> ### 📉 (c) SAME-DAY ADDENDUM (~06:00 ET) — a core structural leg was retired, and it cuts against this thesis
>
> **The FR2004 data gap was closed and it was self-inflicted** — a stale API series break returning HTTP 200 with data ending 2024-07-02, not an access limit (KB-BND-096). Four of five owed prints recovered, and they retire a premise this document has carried since June.
>
> **Old view:** "the dealer backstop is **record-thin** — FR2004 long-end inventory at fresh all-time highs, →4 trigger armed," listed as leg 1 of the three things keeping this a WATCH.
> **New view:** the record **unwound** — 11-21Y **−17.4%** off its 6/24 peak (77.4 → 63.9 as-of 7/15), long-end total **−9.0%** across four consecutive accelerating weekly declines — and it unwound **benignly**, into exceptional indirect demand with SOFR-IORB negative. **Benign distribution, not forced de-risking.** Vector 3 → 2 on the pre-registered condition; "→4 ARMED" disarmed; composite 14 → **13/35**.
>
> **Why this is a thesis-level entry and not just a score change:** "record dealer stock + no Fed coupon backstop" was the pairing that made the long end look structurally fragile. **The Fed half is still true; the dealer half is not.** The demand-hole scenario is **less pre-positioned than every BOND surface asserted for six weeks**, and the correction arrived only because a self-inflicted data gap was finally audited rather than escalated again.
>
> Also corrected: the 6/17 $74.6B this thesis called "the fresh all-time record" was **one week early** — 6/24 at $77.4B was the true peak, never observed because the series was unreadable at the time.
>
> **No version bump for this** — v1.1.4 is reserved for the post-7Y falsifier adoption and will carry both changes together, so the exit apparatus and the structural read move in one reviewable step rather than two partial ones. *(Deliberate: v1.1.3 was itself a bump that described intent ahead of the artifact — see (a). Not repeating that.)*

**Refinement (no conviction change — TLT puts HOLD/no-add unchanged; composite 12/35 → 14/35):**

1. **★ FALSIFIER APPARATUS RE-SPECIFIED — tail-keyed → composition-keyed.** Old view: the HEN-42 joint falsifier was *belly indirect <55% AND 2Y outright TAIL >2bp AND dealer >18%*. **New view: that specification was defective and its non-firing is NOT evidence.** It anchored the DENY branch on a **2Y tail**, which a term-premium story structurally cannot produce (term premium produces a *strong front* plus concession further out — which is exactly what printed on 7/27). The branch could therefore only have fired in a world where the thesis was already wrong for some *other* reason: it passed **by construction, not by evidence.** The defect is BOND's as the falsifier's author; HENRY accepted it in good faith. Instance of `finding_confidence_priced_against_thesis_not_letter` landing on the author rather than the acceptor. **All future auction-keyed legs are specified on COMPOSITION (indirect % and dealer % of competitive accepted) and are TAIL-FREE by construction**, because TreasuryDirect publishes no when-issued yield and a tail is therefore *unscoreable from primaries* — a structural limit, not a per-session data gap (VX-BND-09). Replacement 7/28 7Y pre-registration adds an explicit **"confound wins → defer"** branch, since FOMC-eve event risk and term premium predict the **same** thin cover and **different** composition. KB-BND-089.

2. **Oil→breakeven channel CONFIRMED OUT-OF-SAMPLE.** Old view: the arm's insulation from the Mideast book was argued from a *backward* decomposition (KB-080/088) plus CARL's forward-CPI weld — both in-sample. **New view: directly tested and passed.** Across a ~11% two-session collapse in Brent ($100.50 [7/23] → ~$90.57 [7/27]), **DFII10 held 2.43 → 2.43 — literally zero — while T10YIE fell −7bp and T5YIFR −3bp.** The entire rates response ran through inflation compensation; the real/policy leg did not move. An oil shock is a *breakeven* event, not a policy-path event, and the falsifier's shift from "oil retrace" to "dovish Fed repricing" (v1.1.2) is now empirically earned rather than inferred. Also resolves a fleet dispute without recourse to contested CME scrapes. KB-BND-091.

3. **Credit vector RE-ACTIVATED; "credit is inert" retired.** Old view: "credit inert — not the story" (HY ~275, flat). **New view: HY OAS 268 → 279 in two sessions off a nine-session range that never moved >5bp**, CCC to 996, IG to 80. The move is **absolute-parallel and proportionally largest at the TOP of the stack** (BB +7.0% > single-B +3.9% > CCC +1.5%) ⇒ **quality-INDISCRIMINATE repricing, not a credit-discriminating selloff** — so it does *not* upgrade the default-cycle read, but it does end the "credit is not the story" framing. HY market function 1 → 2. KB-BND-090.

4. **Third hypothesis registered for thin auction cover (neither policy-path nor term-premium).** The Treasury cash-futures basis trade shrank **~$1.3T → ~$1.0T** since January. Withdrawing repo-levered cash-Treasury bid produces **thin cover with intact composition** — precisely the 7/27 5Y signature — because the departing bidder is neither foreign/custodial nor a dealer. Held open as a live alternative so auction reads are not forced into the policy-path/term-premium binary. Logged ESTIMATE; LIQUID owns the call. KB-BND-092.

5. **Process/hygiene:** two load-bearing values on BOND's own surfaces were found stale (HY OAS carried 26 days; the FOMC "~90% hold" prior off by ~25pp), both surviving because their values were *plausible*. Promoted fleet-wide as `finding_plausible_stale_value_evades_review`. Also promoted `finding_claim_outlives_its_discredited_instrument` after finding HENRY had over-retracted a sound claim when its instrument failed. **Durable-doc rule enforced:** this THESIS no longer carries live levels or composite scores — those live in STATUS only.

---

## v1.1.2 — 2026-07-18 (term-premium label CORRECTED → real-policy-path; EU-sovereign reconcile)

**Triggers:** RED's flag-to-verify (routed via PROME 7/17) — is "term-premium channel CONFIRMED" honest net of the 2Y/policy component? + LIQUID EU-sovereign reconcile (Will-approved 7/17) + CARL diesel-weld consume.

**Refinement (no conviction change — TLT puts HOLD/no-add unchanged; composite 12/35 unchanged):**
1. **★ Channel-4 label corrected: "term premium" → "real-rate / higher-for-longer (policy-path-led)."** Old view: the 10Y's hold ≥4.50 was a "term-premium channel." New view: the arm-completing +14bp move (7/6→7/13) was **real POLICY PATH, not a term-premium expansion** — decisive tell is the curve shape, a **belly-led bear-flattener** (5Y +16 > 10Y +14 > 30Y +11; 30Y−10Y −3bp, long end LAGGED) = the *opposite* of a term-premium expansion (which steepens, long-end-led). Three-bucket decomposition of the +14bp: inflation-comp +2bp (~14%, T10YIE), real policy path ~+11-13bp (~80-90%, DGS2 +13 · DFII5 +12 = DFII10 +12 parallel), real term premium ~0 to +1bp (~0-7%). **86%-real is correct but real ≠ term-premium.** LEVEL vs MOVE distinction: ACM 10Y TP +0.73% [Jul-2026, positive first time since 2023] elevated in the *level* but flat over the *move*. Falsifier sharpened: dovish Fed repricing (FOMC 7/28-29), not oil-retrace — already stress-tested (cool June CPI+PPI didn't break it). Route-out to PROME for HEARTBEAT amendment. KB-BND-080.
2. **CARL diesel-weld folded (KB-CARL-338).** Forward Aug-Sept core-CPI feed rides structural legs (Russia ban ~8/3, distillate base, sticky freight), not Hormuz → arm **doubly insulated from the Mideast book** (backward decomposition + forward inflation feed); TERRY §9 concentration flag softened both ways. KB-BND-081.
3. **EU-sovereign reconcile w/ LIQUID CLOSED.** Canonical peripheral spreads-to-Bund [7/17, TE 10Y]: BTP-Bund 83 / Bono-Bund 47 / GGB-Bund 71 / OAT-Bund 79 — all benign/convergence-tight. Owner split: BOND = sovereign-curve spreads + ECB/TPI mechanics; LIQUID = EU-bank→US xccy-funding transmission (the contagion channel; Bund-flight is a haven/tightening effect, not the vector). ONE pre-registered trigger: BTP-Bund >200bp sustained. VX-19. KB-BND-082.

---

## v1.1.1 — 2026-07-06 (QT-framing reconciliation + reconciled BND-11 grade methodology)

**Triggers:** PROME QT-framing fix-packet (Will-authorized); teams-session reconciliation of the 7/9 refunding grade with LIQUID (absorption) and SAM (JGB leading indicator).

**Refinements (no conviction change — TLT puts HOLD/no-add unchanged; composite 12/35 unchanged):**
1. **QT-framing corrected fleet-wide-consistent.** QT **ended Dec-1-2025** (FOMC Oct-29-2025); post-QT the Fed buys **T-bills via RMPs, not coupons** → **no Fed backstop at the coupon/long end.** Fixed the stale "QT still active" line in `domain/sources/AUCTION_FRAMEWORK_from_LIQUID.md` and reconciled the framing across STATUS (Fed b/s row + MBS "passive runoff" → paydowns-reinvested-into-bills), THESIS (ACTIVE EPISODE regime clarification), VX-17. This **sharpens** the demand-hole thesis — the one buyer who could paper over a weak long-end auction is structurally absent. KB-BND-069.
2. **BND-11 grade reconciled to ONE figure with LIQUID + folded in SAM's JGB leading indicator.** New spec `BND11_REFUNDING_PREREG_2026-07.md`. ONE metric = 30Y indirect (%-of-competitive-accepted) vs June-6/11 60.0%; the "masked hole" (clean-but-composition-soft) scores BND-11 TRUE yet escalates. JGB 30Y 7/7 = a term-premium *correlation* pre-arm (not flow) → moves the term-premium/tail leg, not the indirect-composition leg → conditional prior shift (firm ~73 / soft ~66 / weak ~58% benign), can't fire an acute marker alone, gated on US-10Y-7/8 confirmation. Circularity discipline: JGB / 30Y-level / thin-bid = one term-premium root, not independent votes. KB-BND-070.
3. **Live refresh (7/6):** 30Y at the 5.00 threshold line intraday (a poke; BND-12 needs 5 closes); DFII10 2.25 (ticking toward the 2.5 re-arm); 10Y 4.48; credit inert (HY 275 / IG 75 / CCC 971). Stale-fix: HYG June put expired → HYG puts closed; THESIS Status line de-dated to point at STATUS.
4. **Carried to next session:** FR2004 as-of-6/24 print (released 7/2) not retrievable this session (NY Fed API caps pre-2026 in-env) — registered as a next-session pull; dealer-absorption →4 trigger stays ARMED, half-met.

---

## v1.1 — 2026-07-01 (long-end re-engagement + JGB-FX channel + mandate extension)

**Triggers:** 11-day gap sweep (6/20→7/1); three predictions resolved (BND-02 FAILED, BND-04 FALSE, BND-10 VOID); a new transmission channel; a Will-approved coverage extension.

**Old view (6/20):** the hawkish FOMC bear-flattened — risk migrated to the front-end (HENRY's lane); BOND's long-end anchored; the one escalating vector was DFII10 (real-rate side); TLT puts on the "wrong tape."

**New view (7/1):**
1. **The long end is re-engaging, phase III** — 30Y 4.97 (+11bp/2d), globally synchronized: domestic hawkish-data repricing (JOLTS beat, ISM prices 73, Dec-hike ~79-82%) **co-firing with a JGB super-long rout** (6/30: 30Y JGB +8.8bp; weakest 20Y JGB auction since May-2025 on 6/25; rinban step-down effective 7/1). NOT real-rate-led this time (DFII10 peaked 2.29 → 2.20): policy-repricing + global term premium. Long-end vector 2→3; composite 11→12/35.
2. **New channel 6 — Global long-end / JGB-FX:** window evidence shows JGB↔UST *duration decoupling* (weak JGB 20Y auction → USTs rallied 4 sessions), so the armed leg is **FX-routed**: yen at a 40-year low (162+), record ¥11.7T intervention spent, Mimura verbal warning 7/1 — *actual* MOF intervention = mechanical UST reserve selling. Built from SAM's 6/30 signal + independent verification (their baseline was one session stale — pre-rout).
3. **Demand composition rotating:** June cluster cleared (6th straight benign — BND-11 arms the 7th test at the 7/7-9 refunding) but indirects fell <60% at 2Y/7Y with 13-21pp m/m slides, absorbed 1:1 by directs. VX-08/13 → 3. Dealer long-end stock at a **fresh record** ($74.6B 11-21Y, 6/17) — →4 trigger ARMED; 7/2 print + 7/9 30Y decisive.
4. **Falsified legs cleaned up:** issuance-freeze mechanism resolved FAILED (Apr-Jun was an AI-capex issuance BOOM — April HY $40B, record June IG); CLO-AAA canary FALSE (BSL never near SOFR+160; MM near-miss S+158). Warsh MBS-sales supply leg deferred to 2027 ("years, not months," Sintra) — removed as near-term amplifier. Oil→breakevens re-arm bar proven HIGH (live kinetic Iran exchange 6/25-28 bought only ~2-6bp of breakeven).
5. **Mandate extension integrated (6/27 SIG):** + MBS/housing-finance/FHLB advances (VX-17/18) and Eurozone rates (VX-19 — ECB is HIKING: first hike since 2023 on 6/11, OAT-Bund widening). EU leg starts at watch-level 2.

**No conviction change:** TLT puts HOLD/no-add — gates pre-registered (BND-11/12; DFII10 >2.5; 30Y >5.0 ×5 + weak auction), none fired. But the tape rotated from working *against* the expression (bear-flattener) to working *toward* it (global steepening tilt into a supply gauntlet with a record-thin dealer backstop).

---

## 2026-06-20 — intra-v1.0 POV note (no version bump)

**Trigger:** the live post-refunding gate resolved — 6/16 20Y, 6/17 FOMC, 6/18 TIPS.

**POV pivot (refinement, not reversal):** the hawkish surprise hit the **front-end, not the long-end.** The Warsh FOMC (6/17) delivered a hawkish pivot (dot median +40bp to 3.8, core PCE +60bp to 3.3, 9/18 see a hike) but the curve **bear-FLATTENED** — 2Y +15bp, **30Y flat at 4.93** — the *inverse* of the supply/term-premium bear-*steepener* the thesis is built around. The long end **held below thresholds through a hawkish Fed**, and the 6/16 20Y printed **STRONG** (BTC 2.75, best in 3mo) → **BND-09 FALSE** (5th straight benign auction-stress resolution). Net: "expensive, not broken" is *strengthened* — even a hawkish catalyst couldn't break the long end.

**What this changes:** (1) the term-premium re-fire *failed its cleanest test* — the TLT-puts add-case weakens (a bear-flattener is the wrong tape for a duration short; TLT rallied). (2) The one BOND-domain vector now *escalating* is the **real-rate side (DFII10 2.23, +7, rising)** — re-framed as the cleanest single re-arm metric (watch → 2.5), displacing the nominal-threshold watch. (3) Confound logged: an Iran interim-peace/oil-down signal 6/17 aided the long-end anchoring, so it is not purely a clean-FOMC read. **No conviction change** — composite 11/35 flat; TLT puts HOLD/no-add.

---

## v1.0 — 2026-06-15 (first formal thesis doc)

**Change:** Migrated the durable thesis out of STATUS.md prose into a standalone `thesis/` structure (THESIS.md + CHANGELOG.md + PREDICTIONS.tsv), matching the mature peer pattern (BRENT/SAM/CARL). STATUS.md is now pure live-state (dashboard, convergence matrix, catalysts, compact exits, bottom line); the durable read, transmission channels, full exit/falsification, and position rationale live in THESIS.md.

**State captured at v1.0:**
- Regime: 🟡 WATCH — "expensive, not broken." The May–June long-end term-premium episode (BND-07) fired, mean-reverted, re-fired into the June refunding, and relaxed once the refunding cleared.
- Conviction: TLT puts HOLD/no-add; short-credit not supported; composite 11/35.
- Evidence: June refunding cleared (10Y strong, 30Y soft-orderly) → BND-08 FALSE; working model held 4 straight resolutions (BND-05 F · 06 T · 07 T · 08 F).

**No conviction change** — structural migration, not a thesis revision. View unchanged from the 6/9 STATUS regime read; restated in durable form and refreshed to the post-refunding tape.

---

## Pre-v1.0 — historical arc (reconstructed from STATUS / PREDICTIONS; not versioned at the time)

Provenance for the thesis predating this doc:
- **BND-07 episode (May):** long-end leg fired — 30Y >5.0 ~9 sessions + 10Y >4.5 for 6 (5/14–5/27). Threshold TRUE, but resolved as an **episode, not a one-way break** [[threshold_vs_mechanism]] — term premium gave back into early June.
- **TIPS-vs-nominal correction (5/21):** the 5/21 "10Y reopening" was a 10Y *TIPS* reopening (CUSIP 91282CPU9), not nominal — conflation corrected in the 6/9 STATUS; the add-gate keyed to it was mis-specified (moot).
- **"Expensive, not broken":** established across the May refunding / 20Y / TIPS reads — the long end clears demand at price; term-premium digestion, not mechanical failure.
- **Dealer-backstop-thin (6/9):** NY Fed FR2004 (5/27) — dealer long-end inventory near/at record; buyback long-end offer/accept ~13x. Dealer-absorption vector → 3.

*Reconstructed for continuity; historical context, not contemporaneous version entries.*
