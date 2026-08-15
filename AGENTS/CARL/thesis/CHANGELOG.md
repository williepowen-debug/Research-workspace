# CARL CHANGELOG

Tracks all changes to THESIS.md and PREDICTIONS.tsv. Reverse chronological. Each entry documents what changed, why, and the old view vs new view. This is the audit trail.

**Versioning convention:**
- THESIS: `vX.Y` — major (X) = structural thesis change (new mechanism, thesis break, conviction reversal). Minor (Y) = refinement (updated evidence, threshold adjustment, vector upgrade/downgrade).
- PREDICTIONS: changes logged by Pred_ID.

---

## 2026-08-15 (Sat) — **FULL-THESIS KILL RULE RE-SPEC DRAFTED (row 44, option b) · guard-#4 correction: Q1 WAS revised · no score change, 53/70 holds**

**No version bump — the re-spec is DRAFTED, not live.** THESIS.md:397-398 keeps the as-written rule in force with a pending-ratification pointer. Will ratifies before it goes live.

- **ROW 44 ENCODED -> `thesis/KILL_RULE_RESPEC_2026-08-15.md`.** Authority: `PROME/proposals/2026-08-12_rule-batch-RULED.md` (batch approval off PROME recs; carries Will's authority, not his individual attention). **Leg 2 re-keys from the CC 90+ balance SHARE to the quarterly transition rate INTO 90+ for credit cards** (HHDC `Page 14 Data`). Leg 1 (claims <220K, 8+ wks) untouched per the "no threshold moved in the same edit" rider. **Needed ~9/30.**
- **RIDER 2 / `CHG-RED-045` ANSWERED IN THE SPEC TEXT.** RED's condition was that any **dollar** leg must be symmetric or it is a ratchet. **Answer: no dollar leg is registered** - the re-spec *replaces* the measure rather than *adding* a conjunct, so the enter-1-of-N/exit-all-N asymmetry does not arise. Symmetry shown on the letter: the re-spec **fires in a state the old rule cannot** (share flat-or-rising on denominator growth while inflows fall). **And it does not rescue CARL on the case that prompted it - applied to Q2, flow fell 7.10->6.97%, so it returns decline #1 of 2, identical to the as-written rule. The kill stays 1-of-2 under both.**
- **RIDER 1 (shadow grade) built into §6** - at the ~Nov Q3 print both verdicts get recorded side by side before either is acted on; an as-written fire that the re-spec misses is escalated, not absorbed.
- **⚠️ GUARD #4 CORRECTION - the 8/11 card graded it wrong. Q1 WAS revised.** The Q2 report's own footnote: *"2026Q2 report includes a revision to 2026Q1 credit card balances outstanding."* Q1 CC balance **$1.2520T (Q1 report) -> $1.2420T (Q2 report), -$10B**; total debt likewise -$10B. **The Q1 CC 90+ SHARE (13.1200%) and the Q1 CC FLOW into 90+ (7.1000%) were NOT revised.** Recorded as a dated §8 addendum on the frozen card; the original ✓ verdict stays visible per the freeze rule.
  - **Grade survives intact:** CRL-05 resolves on the share (unrevised, -20bps exact); the discriminator cell rested on transitions (unrevised). Both quarters had in fact been pulled from the Q2 xlsx, so the *substantive* half of guard #4 was honored - the **reporting** half (*"and say so"*) was answered with its opposite.
  - **⚠️ One headline figure is now vintage-dependent:** *"delinquent dollars ROSE $0.23B"* is derived (share x balance) and inherits the revision. **Same-vintage +$0.23B (ROSE, correct); cross-vintage -$1.08B (FELL). The sign reverses.** Balance growth halves cross-vintage (+$21.0B/+1.69% -> +$11.0B/+0.88%). **Always cite the $0.23B with "same-vintage (Q2 report)" attached.**
  - **Mechanism of the guard failure, and it is reusable:** every figure in the supporting reconcile list was read out of the **Q2** report and checked against a baseline itself sourced from the **Q2** report. **A revision check that reads only the new vintage is circular by construction** - it cannot detect a revision and returns ✓ at full confidence. Detecting one requires opening the OLD report.
  - **The error and the fix are the same finding:** this measurement is exactly why the re-spec keys leg 2 to flow rather than dollars - a dollar leg carries a **$10B revision against a $0.23B signal (43x)**, and its verdict would depend on which vintage the grader opened.
- **RED's §3 adjudication of the Q2 counter-reads ADOPTED** (`CHG-RED-045`): the *"$40B out of 120+ late vs $43.5B into severely derogatory"* leg is **DROPPED entirely** - severely-derogatory paper is already-realized loss, the exhaust, and cannot carry a forward claim; the **denominator rebuttal is conceded to fail** (balances grew +1.69% against falling real DPI, limits +$85B, HELOC up a 17th quarter - deflating distress by distress-driven borrowing understates distress). **What survives is transitions**, which is independently why the re-spec keys there.
- **⚠️ RED's unresolved challenge CARRIED, not waved:** CARL asserted mortgage transitions were *"not obviously affected"* by the Fed-stated servicer-transfer reporting gap **without verifying it**. Now known: the CC flow series was unrevised across the Q1->Q2 pair, and **the caveat appears nowhere in the Q2 data workbook** (all sheets searched) - its provenance is the PDF prose, not held locally. **Still unknown: whose book went missing, hence the sign of any bias.** Owed before ratification: re-pull the Q2 PDF and quote the caveat verbatim with its scope. **If it reaches card reporting, the re-spec's instrument inherits a sign-unknown bias and Will must be told before ratifying.**
- **No score change - 53/70 (76%) holds. Zero capital, zero thresholds moved, no confidence moved.**

---

## 2026-08-11 (Tue eve) — **Q2 2026 HHDC GRADED against the frozen card: CRL-05 85→20 (materially adverse) · CELL B (ambiguous) · CRL-21 position action = HOLD — no score change, 53/70 holds**

**Session shape:** the un-masked discriminator print landed and was graded against `thesis/HHDC_Q2_2026_GRADING_CARD.md` (frozen 2026-07-24, 18 days early) + its three addenda. Primary pulled direct — `HHD_C_Report_2026Q2.pdf` + `.xlsx`, newyorkfed.org (WebFetch 403 → curl + browser-UA, the documented route). Header confirms *"2026:Q2 (RELEASED AUGUST 2026)"* — year-trap cleared. **Guard 4 satisfied: Q1 was NOT revised** (13.1→13.12% is precision; 4.8→4.76%, $18.784T, 59.16K foreclosures, 10.34% student 90+ all reconcile to the locked baseline).

- **CRL-05 (CC 90+ breaches 13.74% GFC peak) → ⚠️ MATERIALLY ADVERSE, 85% → 20%. STAYS OPEN, resolves Q3 (~Nov), timeframe NOT extended a third time.** **CC 90+ = 12.92%, −20bps from 13.12% — the first decline off the 15-year high.** Lands in the card's 12.0-13.09% band whose pre-committed consequence was *"cut 85 → ≤55"*; taken to 20 because ≤55 is a ceiling, not a target, and the arithmetic is harsher: confirming by the registered Q3 endpoint now needs **+82bps in one quarter**, against a largest-recent-quarterly-rise of **+42bps** (25:Q4→26:Q1) and a print that just went −20bps.
- **⚠️ Denominator guard (addendum 3) applied — and it does NOT rescue the prediction.** The **entire** 20bps share decline is denominator growth: seriously-delinquent CC **dollars ROSE $0.23B** ($162.95B → $163.18B) while CC balances grew **+$21B (+1.7%)**. The numerator did not improve. CRL-05 is written on the SHARE, the share fell, and the cut stands on its own letter — the decomposition is logged as a separate structural read, **not** as relief. ([[finding_confidence_priced_against_thesis_not_letter]])
- **DISCRIMINATOR → CELL B (AMBIGUOUS), called ambiguous and not favourable, per the card's own words.** **A fails** (bureau did not deteriorate). **C fails on its THIRD CONJUNCT** — CC transitions are MIXED, not falling: flow into 30+ **ROSE** 8.61→8.69% while flow into 90+ fell 7.10→6.97%; **auto (7.72→7.87 / 2.97→3.00) and mortgage (3.76→3.95 / 1.48→1.52) transitions rose on BOTH legs.** **D fails** (bureau improved 20bps vs issuers' 39-40bps QoQ). **→ CRL-20 HELD at 45, explicitly not scored as support in either direction; Q3 is the tiebreak.**
- **⚠️ CARD SEAM DEFECT — recorded, not resolved silently.** Cells B (*"flat ±20bps"*) and C (*"down ≥20bps AND…"*) BOTH have their first condition satisfied at exactly −20bps; the print landed on the seam. C's conjunction is the disambiguator and it fails, so B governs. **4th instance of the threshold-spec class** ([[finding_threshold_spec_fails_before_world]]) and the first to arise from two of my OWN cells overlapping. Logged as card §8 addendum.
- **CRL-21 POSITION CONSEQUENCE = HOLD** (Will's 7/24 ruling, card addendum: cell B → hold). **No trim, no duration extension**; revisit at the ~Oct vintage leg. The Aug-21 expiries are therefore a standalone TERRY/Will decision, no longer card-driven.
- **NO SCORE CHANGE — 53/70 holds.** Card §0 pre-committed that no vector can move on this print alone, and **V1's registered downgrade trigger (<12.0% for 2 consecutive quarters, THESIS.md:290) is not touched by 12.92% — the V1 clock does NOT start.** The card §2 band's looser *"starts the V1 two-quarter downgrade clock"* phrasing **contradicts the registered trigger**; the registered trigger governs and the contradiction is logged as an addendum rather than quietly picked (same class as the 8/3 card-vs-matrix coexistence lesson).
- **🔴 SURFACED TO WILL — the registered FULL-THESIS KILL RULE is now one print from firing.** `THESIS.md:398`: *"Claims <220K sustained 8+ weeks AND CC 90+ DQ declines 2 consecutive quarters."* Initial claims **199K**, 4-wk MA ~202,750 (LABOR: lowest since Sep-1969) = **leg 1 reads SATISFIED**; Q2 is **decline #1** on leg 2. A second decline at the Q3 print fires it. Its adequacy was already flagged as a ROADMAP OPEN QUESTION on **2026-05-03** — three months before this print, so raising it is not post-hoc — but **rewriting a kill rule in the quarter it approaches firing is not a call CARL takes alone.** Routed to Will: leave as written and let Q3 grade it, or commission the re-spec now with the rewrite pre-registered BEFORE the Q3 data.
- **Guards, run as a checklist (card §4):** 1 seasonality — not invoked. 2 stock-vs-flow — logged as genuinely MIXED, not confirmation. 3 VantageScore — not raised. 4 Q1 unrevised ✓. 5 **chart-only guard RESOLVED FROM A REAL DATUM:** the published data file gives auto 90+ exactly — **Q1 = 5.60%**, confirming the BOARD-relay figure UNCONFIRMED since 7/12 and its +39bps Q4→Q1 acceleration (Q2 eases to 5.49%); closes the 30-day ROADMAP thread without eyeballing a chart. 6 **credit supply expanded again** — CC limits +$85B to $5.559T, HELOC balances 17th consecutive quarterly rise → RED containment list. 7 one print is one print.
- **Two counter-reads NOT banked as support — routed to RED to press instead (card §7.6):** (a) **$40B drained out of 120+ late while $43.5B moved INTO severely derogatory** (1.754→1.987%, +23bps) with **bankruptcies +10.3%** (124.0→136.8K) — the aggregate 3bps "improvement" (4.76→4.73%) is composition; the terminal bucket grew and the pipeline is resolving into loss, not curing; (b) **mortgage carries a Fed-stated reporting caveat this quarter** (balances −$74B *"mostly due to a servicer transfer gap… otherwise it would have stayed flat"*), so mortgage SHARES are suspect while mortgage TRANSITIONS — which rose on both legs — are not.
- **Secondary reads (card §5, logged not score-bearing):** student 90+ **stock** rose 10.34→10.60% while flow into 90+ **collapsed** 10.86→7.83% (2nd consecutive sharp decel: 16.19→10.86→7.83) = **cohort exhaustion, not reacceleration** → STUE. New foreclosures 59.2→55.2K → HOMER. Third-party collections 4.98→4.88% of consumers but **average amount +2.4% to $1,577** (fewer people, bigger balances) → DOC. Auto originations' median credit score **fell 7 points** = credit quality of new auto loans worsening at origination. KB-382.
- **Source-text discrepancy flagged, not propagated:** the report's summary prose says CC limits rose *"$85 billion (1.1%) … in the first quarter"* — internally inconsistent with its own data sheet ($5.474T→$5.559T = +$85B = **+1.6%**, Q1→Q2). Data sheet used; prose flagged.

## 2026-08-10 (Mon LATE eve, 2nd session) — **CRL-16 RESOLVED → ❌ MISSED (forced call) + sub-agent orchestration wave rulings — no score change, 53/70 holds**

**Session shape:** Will-directed sub-agent orchestration wave (5 parallel Sonnet spawns: STUE/GIG/POLLY/DOC/POP, run per PROME's ORCHESTRATION_PLAYBOOK — mode-B live wave, no-git spawns, CARL sweep at closeout). Frozen HHDC card untouched.

- **CRL-16 (regional-bank Q2'26 SB-related provisions +25% YoY, reg. 60% 4/9, final mark 35%) → MISSED, forced call 8/10 ahead of the 8/31 deadline.** Basis (POP SV-2026-08-10-01): the named series is UNPUBLISHED — none of HBAN/ZION/OZK discloses an SB-related provision line (**3rd instance of the unpublished-metric spec-defect class** after CRL-22-v2 ELV BCR guide + Fitch ATR; lesson: Check D verifies declaration, not PUBLISHABILITY — registration-time precheck candidate). Graded on the mechanism's observable links, which ran the INVALIDATION direction: ZION (the row's own "transparent SB metrics" name) $3M/"benign"; HBAN criticized-assets DECLINING; OZK +29.5% CRE-attributed. HBAN +28%/OZK +29.5% totals cross the bar but were declined as an unlabeled proxy swap. Corroborating: Sub-V July +24% YoY = 4th consecutive decel month. KB-379.
- **VX-GIG-3.08 (Dave provisioning) CRITICAL→NORMAL — RATIFIED** (GIG ledger): the Will-pre-registered Dave-Q2 persist-vs-revert test resolved REVERT (+151%→+14.3% YoY). Invalidation registered: Q3 re-accel >+70%. KB-380. GIG-P03/P06 marked DUE-UNRESOLVED (Gridwise annual-only ×3 checks) — re-instrumentation owed at parent.
- **POLLY final gate-fired refresh + demote to dossier-mode RATIFIED** (Will-approved sequencing, gate = Q2 P&C prints): P05 82→90 (HOLDS, ALL 83.3/PGR 87.3 H1), P02 72→55 (CA FAIR net-add decel ×3 qtrs — reverses April raise), P03 60→85 (Citizens 278K flat). Dossier carry list in SV-POLLY-2026-08-10-01. KB-381.
- **DOC:** FLOW.tsv FROZEN (last rotting non-frozen sub-agent ledger closed); DOC-P04 CONFIRMED (rural closures 206 > 200, Chartis Feb-2026 — public 6mo, unintegrated; process miss logged in its SV); medical debt aligned to DEWEY-C4 (~$195B central); Med-CPI 2.0% YoY 3-mo low, DOC-P03 35→30.
- **STUE:** 3 inbox packets drained (VASP category error, monotone-law strike, CRL-14→28 residue ×6 surfaces); Treasury Phase 1 verify INCONCLUSIVE (no primary; 8/7 "Default Resolution Hub" = infrastructure, not confirmation — docket 8/13 row re-scoped); MOHELA WebFetch 403 → CARL ran the documented curl+UA route same night: docket SILENT through 8/10, last entry #54.
- **No parent confidence changes beyond the CRL-16 resolution. No vector/score moves — 53/70 holds.**

## 2026-08-10 (Mon eve) — **THESIS v2.6.5: V16 Employment 3→4 EXECUTED + V2 instrument RE-POINTED — 52→53/70 (76%)**

**V16 Employment Structural Rot 3→4 (Will-approved live in-session).** The Jul-2 re-arm (v2.6.1, ARMED with resolver *"July NFP negative OR another sharp-decel-with-down-revision"*) resolved on its own letter — **both branches at once**: July NFP **−23K = first negative print of the cycle** (BLS USDL-26-1291, primary pulled direct) AND **−103K down-revisions** (May 129→63K, June 57→20K). 3-mo avg +20K/mo; AHE 3.2% YoY (lowest since May 2021); LFPR 61.4% (−0.7pp since Jan, BLS's own sentence). Honest splits carried: local-gov-edu −50K excluded as FISCAL (LABOR base-rate ruling); retail trade −19K (club/supercenters −21K) = the K-shape-axis datum; still rot-not-break (layoffs 1.1% flat; survey layer thawed). **Old→new: V16 3→4; 52→53/70; histogram 4-row 8→9 / 3-row 5→4; critical avg 3.83→3.92.** New downgrade branch written *provisional* (2-consecutive-bounce mirror of the Jun-6 cut basis — Will review at next matrix pass). Surfaces: THESIS header/§5/matrix/histogram/commentary/upgrade-path/evolution + STATUS overall/matrix/histogram/total/NOW/bottom-line + this entry. KB-376.

**V2 instrument RE-POINTED (Will-approved, docketed decision ~8/10):** registered instrument moves off the **blocked Fitch ATR** (4th month unpublished; two stale-vintage recirculation traps, KB-375) onto **OTTO's 7-deal SEC 10-D panel**. Leg arithmetic NOT transplanted (fixed panel ≠ index — deal-level YoY conflates seasoning): operational leg spec OWED via the CARL↔OTTO discriminator thread before the ~8/17 filings, surfaced to Will before registration. TTM<6.0% leg RETIRED as index-specific; cure-reversal leg carries; until registered the panel reads directionally (currently: post-trough climb both tiers = downgrade NOT firing). KB-378.

**Evolution-list repair:** the v2.6.4 bullet was missing from THESIS §Thesis Evolution (8/3 omission) — added retroactively alongside v2.6.5, marked as an 8/10 addition.

**No prediction confidence changes.** Corrections applied to KB-152 (Tricolor cooperators 1→3, trial 1/25/27), KB-364 (AHE trajectory descriptors retired — LABOR supersession), KB-366 (CVNA −7.4% realized, not −16/20%; hook re-registered ~8/17), KB-371 (MU resolver ~late-Sept, not 8/4; iPhone BOM magnitude add), KB-372 (Russia runs ~3.6M bpd, lowest since May 2002). KB-377 registers the live tariff regime (Sec-301 effective 7/24; Canada 338 effective 8/19) — reverses the "USTR missed its deadline" framing on CRL-23's second conjunct. BOARD 48-signal backlog cleared (41 REFERRED / 4 INTEGRATED / 3 INFO_ONLY; reconcile 0/0).

---

## 2026-08-03 (Mon) — **THESIS v2.6.4: V5 Gas Squeeze 3→4 EXECUTED — 51→52/70 (74%)**

**The pre-authorization fired.** Will's 7/31-eve conditional (*"still ≥$4.00 at Monday 8/3's window close → EXECUTE 3→4, no further ask; retrace <$4.00 first → hold 3"*) was verified against its two registered instruments and **the condition was MET**:

| Instrument | Reading | Obs date | vs $4.00 |
|---|---|---|---|
| AAA daily national regular | **$4.095** | 2026-08-03 (live pull) | ✅ +9.5¢ |
| FRED GASREGW weekly | **$4.001** | w/e 2026-07-20 | ✅ +0.1¢ |
| FRED GASREGW weekly | **$4.096** | w/e 2026-07-27 | ✅ +9.6¢ |

Two consecutive FRED weeklies ≥$4.00 and rising; **no sub-$4.00 daily reading anywhere in the 7/20→8/3 window** (7/24 $4.105 · 7/31 $4.106 · 8/3 $4.095), so the retrace branch never armed. Diesel **$5.364 [8/3]** at a fresh high. **Old view:** V5=3 ("watching — the gas leg of the cost squeeze is relieving," v2.6 Jun 22). **New view:** V5=4 ("firing, with room to escalate") — the bottom-60 energy cost squeeze is re-engaged, with 2026 the first year ever to record two separate $4.00 surges.

**⚠️ Two honesty notes recorded on the move, neither of which changes the arithmetic:**

1. **Spec coexistence.** The V5 matrix cell's *own* v2.6 re-arm language named only a kinetic/price path (*"Brent $105-110 + pass-through"*). **Brent is $82.77 [8/3 live] — on that literal trigger V5 would NOT have re-armed.** The gate that actually fired is the later, dated, explicitly-superseding 7/16-card sustained-cross path Will ratified 7/31. Recorded in the cell rather than silently resolved; the stale price-route language is now moot (a re-arm-to-4 trigger cannot apply to a vector already at 4), so **no trigger was rewritten.**
2. **The move is one-sided by DEFAULT, not by judgment.** The opposite-signed consumer-credit **DOWNGRADE candidate stayed ARMED** because *both* of its instruments failed to deliver on its own dated day: **Fitch ATR Apr/May/Jun 2026 are still not publicly available** (4th consecutive month; subscription index, secondary coverage frozen at March) and the **Q2 HHDC had not been released** (media advisory still unposted as of 8/3). **+1 is the honest arithmetic of what resolved; it is not a net read of the cycle** — the down-leg is pending, not refuted.

**⚠️ V5-at-4 may be a short tenancy, and the trigger for that is ALREADY REGISTERED — no new threshold was set.** The 1-month fast-table carries *"AAA pump retreats below $4.00 sustained 2 weeks → V5 −1 immediate (4→3)."* That trigger is **live-at-risk from day one**: WTI **−7.29% to $78.50** and Brent **−8.16% to $82.77** [both 8/3 live] on the 8/2 de-escalation headline, with Brent round-tripping **$100.19 (7/23) → $90.12 (7/31) → $82.77 (8/3) = −17.4% off the peak.** At CARL's registered **17-18d** crude→pump lag the break reaches the pump **~8/20**, against only **9.5¢** of cushion. Logged as a dated watch on an existing rail, not as a new spec.

**Surfaces touched (Check B):** THESIS header + V5 row + score header + histogram + commentary; STATUS overall line + gas row + histogram + total + narrative; this CHANGELOG; docket row pruned; NEXUS_BRIEF. KB-373.

---

## 2026-07-31 (evening, 2nd pass) — CRL-28 REGISTERED · CRL-14 RETIRED (Will: "yes register")

**CRL-28 (50%, OPEN):** MOHELA SAVE→RAP harm signature via **CFPB complaint rate** — 60-day rolling avg ≥2× baseline (≥55/day vs ~27/day June base) at any point Oct 1 2026–Sep 30 2027. Instrument declared (CFPB Consumer Complaint Database API — verified public, company-filterable). Single threshold, no conjunction (passes Check-G tier-1); re-base check passed at Date_Made (current ~28.4/day ≈ baseline). Caveats pre-registered: publication lag; **shrinking-book denominator (confirm = conservative, miss reads against it)**; CFPB-continuity instrument risk (halt → STUCK). Invalidation: never >1.5× through Sep-2027 with transition complete → operational-failure leg refuted.
**CRL-14 → RETIRED, superseded by CRL-28.** Final 55%/STUCK, **NOT scored** (resolvability defect; excluded from Brier — retiring an unresolvable row is a status action, not a calibration event). **Doc 54 PACER pull parked as a dated addendum in TRADE.md at Will's direction** (file stays retired; the boot-read reminder lives in SCRATCH AWAITING-WILL).

## 2026-07-31 (evening) — TWO WILL RULINGS recorded (proposal loop closed, root Rule 10)

1. **V5 3→4 PRE-AUTHORIZED CONDITIONAL (option a):** if the pump is still ≥$4.00 at Monday 8/3's window close, CARL **executes** the upgrade (51→52/70) at next session with no further ask; a retrace below $4.00 first = sustain fails, V5 holds 3. Recorded in STATUS gas row + docket. *Not executed — score unchanged until the condition verifies against the 8/3 FRED weekly + AAA daily.*
2. **CRL-14 RETIRE+REPLACE APPROVED (option a):** successor to be a genuinely new, mechanically-resolvable claim (CFPB-complaint instrument, ~50%, window through Q3-2027) — **draft presented to Will for review before registration** per the standing promise; CRL-14 stays STUCK until the successor registers, then retires. Re-base trap honored (a delinquency-worded re-base was already true at Date_Made — forbidden). Doc 54 PACER pull (~$0.30) remains an open Will action, no deadline. The 7/24 HHDC-card cell ruling (CRL-21 capital) stands unamended.

## 2026-07-31 (same session, ledger changes) — CRL-14 55%/STUCK (Will-approved) · CRL-13 window compressed · sleeve +2 legs under CRL-20 · HHDC re-dated to 8/4-8/11

- **CRL-14: 65→55%, OPEN→STUCK** (STUE 7/25 packets, Will-approved; applied 7/31). Resolvability defects (270-day default clock puts any Jul-1-caused default ~Jul 2027, past the window; the AFT litigation is in a **settlement stay** that forecloses the attribution instrument) are booked in **Status**, not Confidence — only the ~10pt genuine world-update (wave-1 no-spike + the ~1.3M/qtr cure channel) is priced. **Retracted:** the "May 28 status conference" (no such docket entry — aggregator artifact). **Open Will decisions:** retire+replace with a measurable successor (~50%, Q3-Q4 2027, non-litigation instrument); Doc 54 PACER pull (~$0.30).
- **CRL-13: notes updated** — notice window compressed ~3mo (all notices by 12/31/26; auto-enrolls to ~Mar 2027); Oct-1 first-tranche framing unchanged; mildly supportive. Confidence held 75%.
- **CRL-05: breach window re-dated** — HHDC prints **8/4-8/11** (PROME cadence case), not "~8/15" (unconfirmed Saturday). Frozen card untouched; two dated addenda added (window + pre-registered interpretive cautions: cascade ≤⅓ of gap per STUE/DEWEY; stock-vs-flow divergence definitional, cuts both ways). **Fitch ATR refresh pulled forward to 8/3.**
- **Paper sleeve: PS-0006 (short SYF) + PS-0007 (short COF) opened under `pred_id=CRL-20`** — unblocked by REGINALD's 7/25 boundary ruling (surface split adopted; standing notify-rule live). ALLY = judgment non-entry (CRL-21 at 25%, NCO leg dead = antecedent too weak). **TERRY's antecedent-diversity gate adopted**: scoring needs N≥10 closed AND ≥3 distinct pred_ids.
- **KB-085 → STALE** (HAWK FLOW-15 retraction: the Gulf→Taipower→TSMC→electronics-CPI chain falsified for 2026; successor is a low-probability tail).
- Data integrated same session (no prediction moves): ECI Q2 (KB-364), June PCE savings 2.7% (KB-369), UMich July final, claims refresh, CRMT (KB-365), CVNA Q2 (KB-366), DEWEY C4 phantom-debt revision (KB-367 — CLAUDE.md band updated), MARCO FL min-wage correction (KB-368 — Sep-30 docket row).

## 2026-07-31 — FOMC 7/28-29 GRADED (2 days late; fleet offline for the print) — L2 modal MISSED, V12 holds 5. No score change; 51/70 holds

**What:** Graded the pre-registered language priors in `thesis/FOMC_JUL28-29_CARL_CONSUMER_LEG.md` (§6 appendix added) off the **full 20pp preliminary presser transcript** (federalreserve.gov PDF, incl. Q&A — RED's same-night grade used the opening statement only and flagged the gap; closed here).

**Outcome:** 9-3 hawkish hold; **L1 (pass-through/broadening) realized**. My modal **L2 look-through 40% ❌ MISSED — negated verbatim in Q&A** ("we're not looking through them and saying, oh, they don't matter"); RED's 30% wins the recorded dispute. L3 (10%) / mixed (12%) / **L4 cohort language (15%)** all correctly low — **zero distributional content in 20pp, including a declined "average household" final question**; L4-NO logged as thesis-consistent per pre-registration. **V12 HOLDS 5** per the pre-registered table (L1 confirms the anchor; un-fire path receded: 3 hawkish dissents, "no soft target," Sept odds 77%, 30Y 19-yr high).

**Calibration (logged for 7c):** "my argument, their number" — §1 of my own leg doc contained the exact reason L2 wouldn't repeat (6/17's look-through was delivered into a *falling* pump) and I priced L2 modal anyway; RED used my argument at the right weight. Same overconfidence-where-I-have-a-preferred-outcome family as the Brier findings. KB-CARL-363.

**Five inbox items had arrived mid-session and were caught only because the closeout sweep re-listed the inbox** — the exact lesson logged earlier in the same session. Two were time-sensitive and one contained Will's decisions.

### Will's rulings — proposal loop CLOSED (Critical Rule 10)
- **CRL-21's position-action commitment → DEFERRED to the ~8/15 HHDC and DECIDED BY THE FROZEN CARD'S CELLS.** *[EDITORIAL 7/31, PROME audit: "~8/15" was the belief at ruling time — the release window was corrected 7/31 to **8/4-8/11, modal Tue 8/4** (a Saturday-date tell); **the ruling binds to THE PRINT, whenever it lands**, and the Aug-21 expiries session follows it — which if it lands 8/4 means ~17 days of runway to expiry, not ~6. Original text preserved as audit trail.]* Cell D → full commitment (trim 25% + duration to Q2-2027+); cell C → duration-extension half only; cells A/B → hold to the ~Oct vintage leg. TERRY constructs; the Aug-21 expiries (OZK ×5, KRE ×3, WAL ×1) are handled in the same post-8/15 session. **Recorded as a dated ADDENDUM to the frozen grading card, not an edit** — because the cells now move *capital*, not just confidence, which is a material change the freeze rule exists to surface.
- **V5 3→4 → decide at the ~8/3 sustained-window close** per CARL's own 7/16 card. No early bump.

### Fleet date correction adopted (RED S25b)
**July CPI = Wed 8/12, not 8/13. August CPI = Fri 9/11, not ~9/10. Sept CPI = 10/14.** Source: OMB/White House PFEI CY2026 schedule, with usinflationcalculator concurring. *(Tooling: `bls.gov` 403s to WebFetch **and** to curl with a browser UA — use the OMB PDF with `pdftotext -layout`.)* Propagated across docket TSV + CALENDAR + FOMC leg + KB-357 + STATUS + NEXUS_BRIEF.

**Two facts in there are not housekeeping:** the **September FOMC carries an SEP and fresh dots; July does not** — so "the Fed signals at the next meeting" must point at September; and **the August CPI lands inside the Fed blackout** (opens Sat 9/5), loading repricing risk onto the September meeting itself.

**RED verified my arithmetic independently off a different series and it is STRONGER than I reported:** spot Brent (no retail-lag assumption) June avg $85.40 vs July $83.3-85.0 = **−0.4% to −2.5%, negative on every plausible final-week path.** Three independent derivations across two supply-chain layers, with RED's as the load-bearing one.

### ❌ My hike-now inference WITHDRAWN — RED rejected it on sequencing and was right
I wrote that the base-effect correction "cuts the other way too," giving a hike-now Warsh a better case. **Wrong.** *"The operative print is not the next one the Committee sees. It is the last one before the next decision."* Ladder: **8/12 soft → 9/11 hot → 9/15-16 FOMC**, decisive print ~4 days before a meeting that carries an SEP. **Waiting is cheap and the evidence lands on schedule — the correction RAISES hold-and-point-at-September and LOWERS hike-now.** Struck through in the FOMC leg with RED's reasoning in place, not deleted. RED moved S1 52→54, S4 23→21.

**RED also found a second error I missed, in their own object:** CHG-028 is a *core/services* falsifier and cannot resolve on the first *headline-energy* print in any month — fixing the date alone would have left the channel mismatch intact. Plus rockets-and-feathers means August energy prints hot in *both* branches, so it isn't evidence either way.

### A self-inflicted error worth recording
My first date-propagation pass **blanket-replaced "8/13"→"8/12" across all files — silently rewriting RED's verbatim quote inside my own document**, making their framework appear to say something it doesn't. Caught on read-back and restored. **A date-correction sweep must never rewrite quoted text: the quote stays wrong and the correction goes beside it.**

### RED's rationalization test — ACCEPTED, and re-pointed at instruments that exist
RED pre-registered: *"if the ~8/15 HHDC prints benign-or-better and V2 does not go 4→3, I file that as a scored rationalization finding against CARL."* Their framing, adopted: **the test is not today's decision but whether the arming is a COMMITMENT or a QUEUE.**
**Their grading condition inherited the exact defect they warned me about** — V2 does not resolve on the HHDC (no subprime series). Re-pointed and accepted on both: **Fitch ATR ~8/10 → V2** · **CC 90+ on the ~8/15 HHDC → CRL-05/V1**.

### Owed, not integrated (KB-362 — recorded so "read" is not mistaken for "handled")
- **LABOR:** AHE +3.5% is composition-contaminated by the ~720K labor-force exit — if right, CARL's "wages ~keeping pace" counter-signal is weaker than logged and the real-wage K-shape may *understate* the squeeze. Clean test: **ECI Q2, Fri 7/31**.
- **DEWEY (ACTION, CRL-05):** does student-loan delinquency *cause* the CC 90+ breach? **Read before 8/15** — if causal rather than co-moving, the frozen card's discriminator cells may need a causal caveat.

---

## 2026-07-24 (FIFTH PASS, Will-directed) — **BRIER AUDIT RUN. The record is bad: Brier 0.300/0.340, NEGATIVE skill, +28.9pp overconfident.** One surgical cut (CRL-07 85→40); no score change

**Deferred since v2.5.1 (2026-05-01). Now run, and re-runnable:** `scripts/brier_audit.py` · full report `thesis/BRIER_AUDIT_2026-07-24.md` · KB-CARL-361.

### The number, unsoftened
| | As-recorded | Ex-ante (best recoverable) |
|---|---|---|
| Brier | **0.300** | **0.340** |
| Climatology (always say 45%) | 0.223 | 0.223 |
| **Skill** | **−0.349** | **−0.527** |
| Mean forecast vs actual | 73.9% vs **45.0%** | 75.2% vs 45.0% |

**Both worse than 0.25 — the score for saying "50%" to everything. Skill is NEGATIVE on both bases: the forecasts were worse than knowing only the base rate.** And the as-recorded number is *flattered*, because Confidence is stored at resolution and CARL trims losers before they resolve (CRL-03 ran 90→72, CRL-11 85→83). **Basis A is a ceiling on true skill.**

Murphy: Reliability **0.109** (should be ~0), Resolution **0.037** (barely discriminating).

### Confidence made calibration WORSE
55-65% +10pp · **65-75% +34pp** · **75-85% +45pp** · 85-100% −2pp. Ex-ante, the 75-85% band went **0-for-2** and 85-100% went 1-for-3. **That is the inverse of a useful forecaster.**

### The content pattern
**Hits are "established trend reaches a level"** (CRL-04, CRL-06, CRL-18, CRL-26). **Misses are "series turns or crosses a threshold by a date"** (CRL-01, CRL-09, CRL-11, CRL-03) — four of five in the documented direction-right/magnitude-or-timing-wrong family, plus CRL-24, a **conjunction** priced at 60% when P(A∧B) ≤ min(P(A),P(B)).

### The uncomfortable structural finding
**CARL's documented failure taxonomy did not reduce CARL's failure rate.** Boot step 7c exists precisely to force reading the MISSED notes before writing a new prediction — and **CRL-24 was registered 2026-06-25, after CRL-01 and CRL-09 were already logged as misses, as a conjunction: the most predictable failure shape available.** Reading a taxonomy at boot is not applying it at registration. **Prescription: move the check from boot to registration**, candidate mechanical form in `consistency_check.py`.

### What the audit does NOT license — and the action taken instead
**A blanket −29pp haircut would be wrong.** The bias belongs to the **Mar-May vintage** (resolved-set mean 73.9%); the **current open book averages 51.8%**. Three months of trimming — including six cuts earlier today — already moved it most of the way. A wholesale haircut would push CRL-12/CRL-21 to ~5%.

**So the action was surgical.** Only two open rows still carry the failed vintage's signature (≥75%):
- **CRL-07 → CUT 85 to 40, and forced to resolve by 8/31.** It fits the *failure* shape: no numeric bar (flagged the same day as unfalsifiable-by-vagueness), magnitude already caveated (FL ~8% recipiency), window nearly closed.
- **CRL-05 → HELD at 85.** It fits the *hit* shape: level-continuation on an established trend (12.70→13.1, climbing), the same shape as CRL-04/06/26.

### Caveats
N=10 — exactly at TERRY's N≥10 scoring floor. **Directional, not significant.** MIXED=0.5 by convention. Legacy pre-TSV "confirmed" bullets excluded: no ex-ante probability was recorded, so including them would be pure survivorship. **Re-run at N≈20** to test whether the vintage improvement is real or the current book is merely younger.

---

## 2026-07-24 (FOURTH PASS, Will-directed) — **CRL-27 REGISTERED** (equity leads credit) + **CARL consumer-book design v0.1 proposed**. No score change; 51/70 holds

### CRL-27 — new prediction, 55%, resolves Q1-2027
**EQUITY LEADS CREDIT:** the consumer-discretionary equity weakness is a *leading* indicator of consumer-credit deterioration, not a de-rating driven by something else.
**Confirms** by Q1-2027 if CC 90+ breaches 13.74% **OR** ≥2 of {ALLY, COF, SYF} accelerate ≥+25bps QoQ for 2 consecutive quarters.
**Fails** if credit stays clean while the equity weakness persists — the equities were pricing something else and the lead reading is **dead, not early**.
**VOID** if the equity weakness reverses first (no information about leading — explicitly *not* claimable as a win).

**Registered rather than adopted as a framing, and the reason matters:** Will observed that consumer stocks may break first. As a *framing* that would rescue CARL from every credit miss — the exact move refused on the morning of the same day, when CRL-24 was graded a clean MISS on a 0-of-4 cycle. **A claim that would excuse the thesis has to be dated and falsifiable or it is not a claim.**

**Pinned baseline** (1y to 7/24 vs SPX +14.7%): XLY −20.3pp · COF −25.5pp · SYF −19.2pp · AXP −16.3pp · CRMT −107.9pp — **while credit printed clean** (CC 90+ 13.1%, COF NCO −39bps *with a $662M release*, SYF under ceiling, ALLY −40bps, AXP flat, retail control +0.5% 6th gain). That divergence *is* the prediction.

**Theoretical coherence, previously undrawn:** the masking framework asserts issuer credit is survivor-biased and LAGS. If true, equity — forward-discounting on the same cohort — should LEAD credit by roughly the masking lag. **CARL had never derived that from its own thesis.**

**⚠️ Pre-registered complication so it cannot be quietly dropped:** a 21-name breadth test (mega-cap-uncontaminated) confirms the weakness is real and mostly **absolute**, not an AI-rotation artifact — **but the cross-section does NOT sort on the K-shape axis.** Auto aftermarket, the classic *defensive* trade-down winner, is down hardest (**AZO −44pp, ORLY −30pp, AAP −23pp**) while premium/aspirational is UP (**YETI +28.6pp, WSM +5.8pp**). CARL's own STATUS carries AZO domestic SSS +4.1% as a defensive counter-channel; the tape says the opposite. **So it may be a broad consumer de-rating rather than cohort stress — which is exactly what leg (b) failing would establish.** KB-CARL-360.

**Monotonicity, deliberate:** CRL-27's credit leg (≥2 of 3) is strictly weaker than CRL-20 (≥3 of 4, same date, 45%), so ≥45% is required; 55% set accordingly.

### CARL consumer book — design v0.1 PROPOSED (`thesis/CARL_BOOK_DESIGN.md`)
**Nothing live; approval gates every element.** Scoped to consumer equities where CARL owns the evidence — explicitly **NOT** regional banks. Contains: the evidence *and* the complication that cuts against it (§2b); scope in/out; the **SYF/COF/ALLY split needing REGINALD's agreement**; a four-condition entry gate (registered prediction + declared instrument + reachable + TERRY constructs + Will approves); bias controls including a **tripwire** (holding a position + adverse data + no confidence move = reportable event); and **Phase 1 as a paper sleeve in TERRY's existing `PAPER_BOOK_DESIGN.md`**, with graduation criteria that require CARL to explain the AZO/ORLY anomaly before capital.

**Recorded honestly in the doc:** CARL argued *against* a book earlier the same day and reversed on evidence. The reversal is in §2, not buried — if the evidence is wrong, so is the design.

### Tooling — two live defects in the day-old checks, both fixed not tolerated
1. **Check E's `(source, series)` string-match gap is not theoretical.** CRL-27 vs CRL-20 is exactly the pair E exists for, and E **did not group them** because the source strings differ on constituent list (3 names vs 4). Set-valued thresholds are outside its reach; handled manually and recorded.
2. **Mirror-parser false positive:** writing the STATUS ID cell as `| **CRL-27** *(NEW 7/24)* |` made the row read as UNMIRRORED. **Fixed** with a tolerant leading-ID match for mirror tables only (canonical TSV stays strict); regression-tested.

Second and third instances in one session of a checker's own usability defect producing a misleading result (after B5 flagging legitimate history). Same principle applied each time: **a checker that produces false positives gets ignored, and an ignored checker is worse than none.**

---

## 2026-07-24 (THIRD PASS, Will-approved) — **THESIS v2.6.3: V2 downgrade trigger RE-SPECCED seasonality-matched.** No score change; 51/70 holds

### The change
| | |
|---|---|
| **Old (retired)** | Fitch ATR drops below **6.5% for 2 consecutive months** OR cure mechanism reverses across 3 trusts |
| **New (v3)** | Fitch ATR **same-month YoY ≤0bps for 2 consecutive months** *(seasonality-matched)* **OR** **TTM average <6.0%** *(currently 6.25%, rising)* **OR** cure reverses across 3 trusts |

Upgrade-to-5 condition unchanged (all relevant trusts terminal). **V2 stays at 4.**

### Why — retired as a SPEC ERROR, not a threshold miss
The ATR series carries a **known annual March-April tax-refund dip that Fitch names explicitly** ("seasonal tax refunds supported a temporary improvement", and calls it "short lived"). A raw-level `<6.5% ×2 months` rule therefore fires **most springs on seasonality rather than mechanism** — and it demonstrably did this year: **Mar-26 printed 6.11%, below the old line, while the seasonally-matched read (Jan-26 6.90% vs Jan-25 6.45% = +45bps YoY) said the mechanism was still deteriorating.** Firing V2 4→3 off that would have been a downgrade caused by tax refunds.

This is the **4th instance in 8 days** of the spec-failure class (`finding_threshold_spec_fails_before_world`) and **the first on a VECTOR trigger** rather than a prediction — same seasonality limb that killed CRL-22 v1 and forced the RED diesel-crack falsifier rewrite (crack vs 5-yr seasonal norm, not absolute level).

### How it surfaced
The 7/24 Fitch refresh — run because the Phase-4 instrument work exposed that **V2's score had been resting on a ~6-month-stale January print.** Recovering the series (Dec-25 6.74 → Jan 6.90 → Feb 6.80 → **Mar 6.11**) is what revealed both the staleness *and* the seasonal defect. KB-CARL-359. **Apr-Jun still owed from the Fitch primary** (subscription; secondary stops at March) — docket 8/10; leg (a) needs two matched months, leg (b) a current TTM.

### Surfaces synced
THESIS (matrix row 2, version header, in-file changelog) · STATUS (matrix mirror cell, subprime-auto row, thesis-version refs, BOTTOM LINE) · NEXUS_BRIEF (version + recent-pivot, flagged fleet-relevant: **any agent with a raw-level threshold on a seasonal series has this exposure**). `consistency_check.py` A/B/D/E: **0 hard** — Check B confirmed the 14-vector matrix, mirror, histogram and 3 current-score assertion sites all still agree at 51/70 through a thesis-version bump.

---

## 2026-07-24 (SECOND PASS, Will-directed) — HHDC card FROZEN · CRL-22 **v3** (the causal inversion) · scoped FOMC leg · POP demoted; **two coherence bugs found by writing things down early**

Will directed four items after the catch-up pass. All four done. **The two most valuable outputs were errors caught by the act of pre-registering**, not by new data.

### 1. NY Fed Q2 HHDC grading card — **FROZEN 22 days early** (`thesis/HHDC_Q2_2026_GRADING_CARD.md`)
Will insisted on this one, and it earned its keep immediately. The card locks Q1 baselines, CRL-05 outcome cells, a **4-cell survivor-pool-vs-healing discriminator** with pre-committed consequences (cells **C and D pre-commit to "masking losing" and "masking refuted"**), seven named guards against my own failure modes, and a grading protocol. Freeze rule: no edits, only dated addenda.

**⚠️ COHERENCE BUG #1 — I had armed the downgrade candidate against the wrong instrument.** On the first pass I wrote that a **V2 (Subprime Auto 60+) 4→3** candidate "resolves on the ~8/15 HHDC."
- **V2's own registered trigger is Fitch ATR <6.5% for 2 consecutive months** — a monthly ABS index, not the HHDC.
- **The HHDC publishes no subprime auto series at all**, only blended. A blended series cannot resolve a subprime-specific vector — *the same composition error the masking framework itself rests on.*
- V1 (CC 90+) is what the HHDC bears on, and its trigger is **<12.0% for 2 consecutive quarters**. Q1 is 13.1%.
- **Therefore: no vector can be downgraded on the 8/15 print alone under existing triggers.** Stated in the card in advance, so a same-print score move would require Will to authorize a *new* trigger rather than one being invented after the data.
- **Exposed gap:** the V2 score rests on a **January 2026** Fitch ATR reading (6.90%), now ~6 months stale — the weakest link in the whole matrix, and invisible while I was pointing at the wrong instrument. **Docket row added 8/10 to refresh it before the HHDC.**

Third instance in eight days of a threshold failing on its **specification** rather than on the world (`finding_threshold_spec_fails_before_world`).

### 2. CRL-22 → **v3** (Will delegated the authorization) — the defect was deeper than v1 or v2
Drafting v3 required a UNH baseline, and pulling it broke the whole design: **UNH Q2-2026 MCR 86.7% vs Q2-2025 89.4% = −270bps YoY IMPROVEMENT**, which UNH attributes to *"benefit design and pricing discipline, member mix"* and explicitly to **"planned exits from unprofitable ACA individual and Medicare Advantage markets."**

**The culling mechanism CAUSES the margin improvement.** The harder insurers shed unprofitable ACA/MA/Medicaid members, the better the MCR prints. So **any threshold specified on insurer margin deterioration is structurally anti-correlated with the K-shape Selection mechanism it was built to detect.** v1 (seasonality artifact) and v2 (a guide ELV does not publish) were each independently mis-specified — but **both inherited this deeper error: they measured the counterparty's P&L instead of the consumer outcome CARL actually claims.**

**v3 measures the consumer side.** Fires if **A** and (**B** or **C**): **A** — combined UNH+ELV membership −≥1.5M FY25-end→FY26-end in ACA/Medicaid/MA (running start: ~1.0M in Q2 alone); **B** — CMS 2027 effectuated enrollment −≥8% YoY *or* uninsured rate +≥1.0pp; **C** — same-quarter YoY MCR/BCR ≥+100bps at either issuer in 2 of Q3-26/Q4-26/Q1-27. Resolves **Q1 2027**. **Confidence 60% — set for the new claim, NOT inherited from v2's 45.**
- **V28 RAF AND-gate retired** — an AND-gate on an item with unpublished timing is exactly what made v2 unfireable.
- **Attribution caveat pre-registered:** Leg B can fire on the ACA subsidy cliff rather than insurer culling. If it does while A is weak, grade **CONFIRMED-BUT-MIS-ATTRIBUTED** and say so.
- **Reachability discipline (the CRL-21 lesson):** Leg C is 2-of-3 — re-check after every quarterly print whether the remainder can still satisfy it. KB-CARL-358.

### 3. FOMC 7/28-29 — scoped leg only (`thesis/FOMC_JUL28-29_CARL_CONSUMER_LEG.md`)
Per Will: write the consumer/CPI language leg, **consume** RED-20 / BOND's falsifier map / VIOLET's crack-vs-fade tree, do not build a fourth rates tree. Contributions:
- **A correction to a shared fleet premise.** RED-20 states the meeting *"defers everything to the July CPI (8/12), where the $100 oil actually lands."* It doesn't — July gasoline CPI prints **~−2.6% MoM** (June avg $4.050 running downhill vs July ~$3.95). The oil lands in **August CPI, 9/11**. That makes the S1 deferral **four weeks longer** than the tree assumes, and simultaneously strengthens the S4 hike-now case. **RED's CHG-028 (8/12 decision tree, due 8/6) needs re-scoping.** Routed 7/24.
- **A third language cell** RED's oil binary collapses: **L2 "look-through"** (the 6/17 framing) is neither "upside inflation risk" nor "growth tax" — it is a deliberate *exclusion* of energy from the reaction function, **V12-confirming but not hawkish-escalating**. Modal at 40%. The live question: that line was delivered into a *falling* pump and has never been tested against a rising one.
- **L4 cohort listen** — does Warsh bring distributional language into the presser himself? The Beige Book has said "increasingly bifurcated" twice; the Chair has not. Would be the highest-information sentence of the meeting for this thesis. **Bias guard pre-registered** (it's the outcome I want, so the qualifying conditions are written down now).
- **Pre-registered priors as a falsifiable object:** L2 40 / L1 35 / L3 10 / mixed 12; L4 15% scored independently. **§3 concedes the aggregate data does not force my preferred framing** — which is why L3 sits at 10%.

### 4. POP — refresh-then-demote EXECUTED, then demoted (`sub_agents/POP/state_vectors/SV-POP-2026-07-24-01.md`)
Gate (Jul-24 Sub-V sunset) fired; ran at parent level (POP not spawned; rule #10 write-down).
- **POP-P01 ❌ MISSED** — commercial Ch-11 H1-2026 **4,589 vs 3,595 = +28%** (June +29%) against a **>40% sustained** bar. Direction right, magnitude wrong.
- **POP-P02 ❌ MISSED at 80%** — **NFIB Optimism June 97.4, +2.1, "nearing its 52-year average of 98.0."** The Apr-17 upgrade 65→80 was taken off a single March 95.8 print: **upgrading into the reversal.** Most expensive miss in the set.
- **POP-P03 70→15%** — Sub-V H1 +50% but monthly **decelerating** (Feb +91% → Q1 +67% → May +36% → June +28%); >+80% by Q3 needs a sharp reacceleration.
- **⚠️ COHERENCE BUG #2 — a monotonicity violation across the parent and sub-agent ledgers.** POP-P06 (SBA 7(a) default **>5%** by Q4-26) sat at **50%** while CARL's CRL-15 (**>6.5%**, same series, same date) sat at **65%**. Impossible: >5% is strictly implied by >6.5%, so P(>5%) ≥ P(>6.5%). Neither ledger was wrong on its own terms — **nobody was reading them together.** Fixed both: **POP-P06 → 55, CRL-15 → 35.**
- **CRL-17 55→40** — the small-business surface is a genuine counter-signal: level high, **rate-of-change easing**. Reported as such rather than buried.
- POP **DEMOTED to dossier-mode**; owed ad-hoc items carried (P04 QSR pull, IEEPA rate tags, ML field drift).

### Net
**No score change — 51/70 still holds.** Nothing this pass was new market data; it was specification, coherence, and pre-registration. Confidence changes: **CRL-22 45→60 (re-spec, new claim)**, **CRL-15 65→35**, **CRL-17 55→40**. KB-345..358. STATUS held at the 250 cap (15 superseded/stale rows retired across both passes). `consistency_check.py`: 0 hard drift.

---

## 2026-07-24 — Q2 EARNINGS CLUSTER GRADED: CRL-26 ✅ CONFIRMED / CRL-24 ❌ MISSED; 6 confidence cuts + 1 re-arm; KB +10; **no THESIS version bump, 51/70 holds** (two opposite-signed vector candidates opened)

**Session shape:** 6-day gap (7/18 → 7/24). Five past-due docket rows integrated & pruned. The week split the thesis: the **energy/cost-squeeze leg fired**, the **credit-conversion leg resolved against the framework**. Score held deliberately — see "Why no score move" below.

### PREDICTIONS — resolutions
- **CRL-26 → ✅ CONFIRMED** (70% conf, clean hit). FRED GASREGW **$4.001 w/e 7/20**; GasBuddy daily touched $4.00 on 7/20; AAA **$4.09** by 7/23. Crossed inside the pre-registered 7/17-20 window from $3.943 at pre-reg (7/16); neither invalidation leg tripped. **Structural datum beyond the threshold: 2026 is the first year ever to reach $4.00 in two separate surges** (De Haan/GasBuddy) — a base-rate break, not just a level. V5 3→4 requires ~2wk sustained (window closes ~8/3) and remains a **Will decision** per the 7/16 card §3.
- **CRL-24 → ❌ MISSED.** SYF Q2 card NCO **5.43%** — below the >5.5% leg; fails on its own invalidation clause. **Honest split recorded:** the pre-registered discriminator (ACL coverage direction) *did* fire thesis-direction — 10.42% → **10.09%**, −33bps QoQ — but coverage fell **alongside** 30+ DQ improving 4.54→4.16% and a **raised** FY26 EPS guide ($9.10-9.50 → $9.25-9.50) and record purchase volume $49.6B. The benign "reserves normalising to a genuinely better book" reading fits the whole print, not the "reserve build < charge-off burn" reading the discriminator was built to detect. **Coverage leg explicitly NOT banked as partial confirmation.** Confirm-legs failed in the *opposite* direction: **ALLY retail-auto NCO 1.57% (−40bps QoQ)**, **COF domestic-card NCO 4.71% (−39bps QoQ)** with a **$662M allowance RELEASE** to 5.02% coverage.

### PREDICTIONS — confidence changes (6 cuts, 1 re-arm)
| ID | Old → New | Reason |
|----|-----------|--------|
| **CRL-21** | 60 → **25** | **Leg-1 failed and the NCO leg is now arithmetically unreachable in-window.** Spec needs ALLY NCO ≥+30bps QoQ for *two consecutive* quarters by Q3-2026 = Q2 **and** Q3; Q2 printed −40bps, so no Q3 outcome satisfies it. Only the vintage-projection OR-leg survives (~Oct). ⚠️ **Pre-registered POSITION-ACTION commitment on failure** (conf −25-30pp + trim shorts 25% + extend duration to Q2-2027+): **confidence leg applied; trim/duration legs SURFACED TO WILL, NOT EXECUTED** — not yet formally triggered because resolution waits on the vintage leg. |
| **CRL-20** | 75 → **45** | Q2 checkpoint: **0 of 4 names confirming**, all three reporters moved *away*. Both 2-consecutive-quarter clocks restart at zero. Two more quarters like this invalidates masking on its own terms and validates CONTAINMENT — which is what the prediction was written to allow. |
| **CRL-12** | 55 → **20** | Q2 was the **company-guided seasonal NCO peak** and came in *under* the ceiling at 5.43%; FY EPS guide raised. FY >6.0% would need a >150bps H2 collapse. Effectively receding to dead; formal read Jan-2027. |
| **CRL-23** | 70 → **45** | Both builder baselines moved against it in one week. **DHI FQ3 GM 20.7%** (beat the 19.7-20.2% guide; Q4 guide *raised* to 20.5-21.0%) on **"lower stick and brick costs"** = construction-cost deflation actively offsetting tariff input cost. **PHM Q2 GM 25.0%**, +60bps sequentially, above the 24.1% floor — the guided low point was beaten. Demand weakness is appearing in **volume** (PHM closings −8%, revenue −11%), not margin. Second conjunct also weakened: USTR **missed** its 7/20 Sec-301 deadline and **Sec-122 expired 7/24**. |
| **CRL-22** | 55 → **45** | **SPEC DEFECT #2 — v2 has no live firing path.** ELV **reported 7/15, not 7/22** (docket date wrong) and **publishes no FY benefit-expense-ratio guide** — not in the release, not on the call — so "ELV raises FY26 BCR guide above 90.2%" can never fire; the UNH leg already reads counter. **Re-spec v3 = Will decision.** Trim not kill because the *mechanism* is corroborated: ELV Q2 BCR 89.7% (+80bps YoY), cost drivers "will persist through the balance of 2026," Medicaid margin −1.75% trough, membership −469K (+ UNH −525K). |
| **CRL-16** | 60 → **35** | Due window is now; early Q2 consumer-lender prints run against it (COF *released* $662M; ALLY's build is CECL-on-growth). Not the SB provision channel it names — directional only. **Force a call by 8/31 rather than let it sit stale-OPEN.** |
| **CRL-08** | 28 → **45** ↑ | **RE-ARM.** The 7/2 "dead-deepened" mark was priced off Brent ~$70 / gas $3.838 and that regime is gone: Brent **settled $100.19 on 7/23** after the 7/22 *Encelia* attack + Red Sea declared zone (GATE-FALCON-001 leg-1 fired); retail $4.001 → $4.09; **gap to $4.50 now ~41¢ vs 66¢**. The 7/2 kill-reason — a real kinetic that price fell *through* — has reversed. Held at 45 not higher: Brent gave back ~$4 on 7/24; the re-arm path required *both* waiver-lapse (waiver runs to 8/21) and Doha collapse; and $4.50 needs another $10-15/bbl *held* through the lag. **Timeframe extended Jun-Jul → Aug-Sep with a stated reason** rather than left stale-OPEN (boot-7b discipline). |

### Why no score move (51/70 holds) — and what was armed instead
Every adverse datapoint this session is an **issuer** print, and the framework's central claim is that issuer books are survivor-biased. Moving vectors on issuer data — in *either* direction — is the exact unfalsifiability error CRL-20/21 were written to prevent. So the falsification was taken **at the prediction layer** (six cuts above, which is where the discipline belongs) and **two opposite-signed vector candidates were opened against dated, un-masked resolvers**:
- **V5 Gas Price Squeeze 3→4 (UP)** — resolves on the ~8/3 sustained-cross test; **Will decision**, pre-reserved by the 7/16 card.
- **V2 Subprime Auto 60+ 4→3 (DOWN)** — **ARMED** on the Q2 issuer sweep, resolves on the **~8/15 NY Fed Q2 HHDC**, the bureau-wide measure. That print is now the most load-bearing test on the board: it discriminates "consumer healing" from "survivor-pool optics."

**Counter-pairing that keeps the mechanism honest:** borrower-side burden hit records in the *same* quarter lender losses improved — Edmunds Q2: underwater-trade-in monthly payment **$944** (record, +$167/mo), average negative equity **$6,884** (Q2 record), **29.6%** of trade-ins underwater, trade-in age 4.0 yrs (Q2 record). Burden-vs-loss divergence *is* the masking mechanism; what missed were the loss **thresholds**.

### RED S24 lag-attribution poke — ADOPTED (verdict: survives as an estimate, no killing defect)
Four refinements + one dated experiment + one figure re-stamp, all banked into KB-CARL-338 / the STATUS diesel row:
1. **Band the lag 12-24d** (17-18d was n=1 on the May *gasoline* cycle); grade leg-2 as a range (retail-visible ~$0.06-0.14, still-loading ~$0.25-0.35) instead of a point pair.
2. **Shock-layer split (the structural point):** 17-18d is a *crude→retail* lag, valid for leg-2 (Hormuz) but **not for leg-1, which is a product-layer shock** — rack reprices off spot product in ~5-10d. So leg-1's crack contribution is **mostly already in the pump**; the escalation peak arrives **sooner, not bigger**.
3. **Rockets-and-feathers *strengthens* the core-feed claim** (recorded honestly, as RED reported it): retail falls slower than it rises, so the $4.65-4.90 de-escalation floor arrives later than symmetric arithmetic implies and the **Aug CPI window catches more elevated price in the de-escalation branch**.
4. **Falsifier sharpened:** "crack normalizes" must be measured **vs its 5-year seasonal norm**, not an absolute/June level — Aug-Sept is the seasonal distillate build and firms cracks regardless of war legs, so as written the leg could never fire.
5. **★ Pre-registered natural experiment (docket rows added):** the 7/17→7/23 crude leg ($88.10→$100.19, +$12/bbl ≈ +$0.29/gal input) should land in EIA weekly on-highway diesel **8/3-8/17, peak ~8/10** — converting the gasoline-transfer *estimate* into a diesel-native *measurement*.
6. **Figure re-stamp:** leg-1 refining loss **~42.7% → ~30% [EST, band 25-35%]**, GS-excluded per OSPREY canon KB-OSPREY-011. Direction of the leg unaffected (export ban + −71% products-loadings collapse carry it). KB-CARL-332 restamped.

### ⚠️ Self-correction found mid-session (NEXUS routing, HENRY origin) — July CPI base effect
**My 7/16 framing was wrong and I had already repeated it in this morning's draft:** *"the crossing lands inside the July CPI reference month, so July energy flips sharply positive → headline deflationary→hot in one month."* That is a **level-vs-monthly-average error.** CPI measures the monthly *average*; **June averaged $4.050** because the month ran downhill ($4.305 → $3.831), while **July-to-date averages $3.878** — even a ~$4.15 final week leaves July at **~$3.95, roughly −2.6% MoM.** **July gasoline CPI prints NEGATIVE with the pump above $4 and rising.**

Consequences, now pre-registered so neither CARL nor RED can score them wrong later: **(a) an 8/12 soft gasoline print is a BASE EFFECT, not a mechanism failure**; **(b) the real oil-passthrough test is AUGUST CPI (9/11)**, starting from $4.10+ against a $3.95 base. Both dates added to the docket. KB-CARL-357.

**Provenance worth noting:** HENRY derived this 7/23; NEXUS routed it into my inbox *during* this session (a packet I had already swept to `processed/` before reading — caught by the pre-commit `git status` check). **I recomputed it from my own FRED GASREGW weeklies rather than adopting it** — the two agree, and mine is marginally stronger. This is the second time this session that a mechanical check caught something a read-through missed (the first: `consistency_check.py` on the stale-open CRL-24 mirror row).

### Session facts (KB-345..357) + corrections
KB-345 gas $4 cross · KB-346 SYF Q2 · KB-347 ALLY Q2 · KB-348 COF Q2 · KB-349 Edmunds negative-equity · KB-350 builder Q2 GM · KB-351 ELV Q2 (+ date correction) · KB-352 AXP Q2 · KB-353 Sec-301/Sec-122 gap · KB-354 war-risk insurance leg. KB-332/338 amended for the RED poke.

**Corrections logged:** (a) **ELV reported 7/15, not 7/22** — the docket carried a wrong date and the 7/18 STATUS note treated an already-released print as a forward catalyst; the 7/18 pass IR-confirmed the card/builder dates but not the insurer one, and only the unchecked one was wrong. (b) **"~42.7% of Russian refining capacity" is off canon** — Ukraine-General-Staff self-report, false precision; band 25-35%.

**STATUS hygiene:** 8 superseded/stale rows retired to hold the ≤250 cap (May CPI headline/core/food-at-home, Apr Core PCE, Apr Real Consumer Spending, GDP Q4-2025, closed-negative May Medical-Care-CPI watch, Feb unemployment-duration). All survive in KB.tsv. `consistency_check.py`: **0 hard drift** (it caught CRL-24 left stale-open in the STATUS mirror — second live catch since the 7/18 build).

---

## 2026-07-18 — CRL-22 RE-SPEC v2 (Will-approved) + CRL-06 Q2-actuals annotation + KB +10; no THESIS version bump, 51/70 holds

### PREDICTIONS
- **CRL-22 re-specified v2 (Will-approved), conf 60→55.** POLLY primary-verify (SV-POLLY-2026-07-18-01, EDGAR) found the v1 H2-weighted-avg legs (UNH ≥85.4% / ELV ≥88.3% over Q1+150bps) are **seasonality artifacts** — UNH's own FY26 guide (88.1%±25bps vs H1 avg ~85.3%) implies H2 ~90.9%, so the trigger fires mechanically in ANY year; simultaneously the FY guide IMPROVED 88.8→88.1 = stress mechanism NOT corroborated. Old: H2 weighted-avg level legs. New: **guide-revision-direction legs** (UNH RAISES FY26 MCR guide >88.1%±25 / ELV RAISES FY26 BCR guide >90.2%), V28 RAF AND-gate unchanged. v1 legs retired-not-failed (spec error, not a thesis event). Conf-trim reason: UNH guide-improvement is live counter-evidence. Baseline conflict resolved same pass: Q1 83.9% CORRECT; press "lowest MCR in 8 qtrs" refuted vs 8-K.
- **CRL-06 (CONFIRMED 7/16) — Q2 actuals annotated:** ATTOM H1 (rel 7/16, HOMER primary-verified): Q2 clears 70K on starts (~82-88K) AND filings (115,714), NOT REO (~14K) = 2nd consec qtr on the defining metric. REO-conversion sub-watch RESOLVED same print: conversion ACCELERATING (timeline 563d lowest since 2013; June REO +23% YoY reaccel) — cure-and-delay hypothesis dropped.
- **CRL-24/21/20/12/23 — pre-registered fire/hold lines staged** in `domain/sources/2026-07-18_q2-earnings-prep.md` for the 7/21 four-name cluster (SYF 6:00am / ALLY 7:30am / DHI pre-open / COF 4:05pm AMC; PHM 7/22; AXP 7/24 — dates IR-confirmed, docket corrected).
- **CRL-26 (gas $4.00 by 7/20):** pending at $3.992 (7/18 boot); STATUS mirror row added (consistency_check.py Phase-1 first live catch).
- **CRL-10 (62% unchanged):** DEWEY fork reconciled vs KB-333 — no collision; three-channel food decomposition canonized (KB-339). DTN 7/15 flip-check: no fertilizer re-arm at retail.

### Session facts (KB-335..344) + hygiene
ATTOM H1 · UNH Q2 · Beige Book July (bifurcation language retained, 2nd consec edition) · diesel weld decomposition (RED fix — Aug-Sept core feed rides structural/sticky legs, NOT Hormuz) · food three-channel reconcile · **June retail discriminator ✅ GRADED** (headline +0.2% vs control +0.5% = May gas-padding confirmed as pre-registered) · Fed G.19 May revolving −$5.3B/−4.71% SAAR · CRMT going-concern · BofA prime-card counter-tell · container freight (relay-tier, AEOLUS reconcile flagged). **BOARD 99-signal backlog cleared** (85 REFERRED / 9 INTEGRATED / 5 INFO_ONLY; 2 CARL overrides). SYF one-figure reconcile CLOSED w/ REGINALD (guide-cut = Apr-21 action; prior guide was 5.5-6.0% RANGE, "was 6.0%" corrected).

## 2026-07-10 PM — THESIS v2.6.1 → v2.6.2: Independence map (additive, no score move) + workbook dedup + CRL-08 two-series annotation

### THESIS — v2.6.2 (minor: additive structural handle; Fable orchestration session, DAEDALUS docket #2+#3)
**Author:** CARL. **Score unchanged 51/70.**
- **Independence map added** (matrix-adjacent block, mirrored one-line in STATUS): shared antecedents tagged — NY Fed HHDC source-pair (V1/V4), energy co-root (V5, V7-leg, V12-leg), labor co-root (V6/V16), K-shape lens (V8); 6 single-root IND. Reading rule: 14 vectors ≈ ~10 effectively independent roots; shared-root shocks scored as one root moving (Jun-22 paired-move discipline codified). Landed as a block, not an in-table column — cell richness preserved (PAT-015 pushback noted to DAEDALUS).
- **Verify-by-reading result:** the VX-CARL-1.01/VX-CARL-CC-01 duplication was workbook-level ONLY — the matrix has exactly ONE CC vector, so DAEDALUS docket #3's "rescore the composite — expect it to move" was wrong; **no score move from the dedup.**
- **Mirror sync:** STATUS V16 evidence cell was still at Jun-6 framing — synced to the Jul-2 "re-arm ARMED, held" state (L85 sub-item a, partial; THESIS-side V6/V8/V10/V11/V13/V14 reason-cell text refresh still open in ROADMAP).

### WORKBOOK (VX.tsv, frozen-ledger disposition edits + KB ref hygiene)
- **VX-CARL-CC-01 → SUPERSEDED** (pointer to VX-CARL-1.01); load-bearing content (CRL-05 >13.74% Q2-Q3 window ~mid-Aug; KB-096/243 SYF anchors) verified carried into survivor Notes.
- **VX-CARL-1.01 bands re-cut** to ranges `<8% / 8-11% / 11-13.74% / ≥13.74%` — closes the 13–13.74% orange/red dead zone (ROADMAP L85 sub-item c).
- **VX-CARL-HSG-03 duplicate ID** (bonus find — two vectors shared one ID): Realtor list-price row renumbered → **VX-CARL-HSG-06**; Existing-Home-Sales keeps HSG-03.
- **KB.tsv:** 3 Vector refs repointed CC-01→1.01 (KB-096/155/243; conservative ref-cleanup, Statuses preserved).

### PREDICTIONS — CRL-08 annotation (no conf change, stays 28%)
- **Two-series reconciliation** (GIG WP-4 parent item C1): EIA weekly $4.500 wk-of-May-11 (single obs) vs AAA daily $4.564 May-21 (<1wk above) — both single-point crosses, neither sustained 2wk → May "first-cross-not-sustained" grading STANDS on both series. GIG-side history reconciled same day. (CRL-07 magnitude caveat = already in ledger since Jun-22, no-op.)

### HYGIENE — Ally raw-10-K retention (DAEDALUS EOD find A)
- `domain/sources/ally/10k_fy2024|fy2025/` HTMLs (17.4MB) **trashed** — no live doc cited them (all refs → RECLASSIFICATION_AUDIT_FY2025.md, kept); never git-committed (verified); EDGAR accessions recorded in the audit's provenance note.

---

## 2026-07-10 — PREDICTIONS: CRL-10 trim 75→62 (DEWEY food-supply fork) + docket CPI-7/14 add (no thesis version change)

### PREDICTIONS — CRL-10 re-mark (prediction-confidence only; no vector score move)
**Author:** CARL (Will-directed C1 from PROME 7/10 audit; integrates DEWEY food-supply-CPI fork, landed f1f53939).
- **CRL-10 (Food CPI YoY >4.0%, Q4 2026): 75% → 62% (TRIM, not kill).** The fertilizer INPUT path turned disinflationary on the latest vintage — urea peaked April (US-retail ~$858 / intl >$850/mt WB Pink Sheet) then rolled over hard through June (intl $453, −41% MoM; US-retail $718, −13%); WASDE Jul-10 crop farm-prices UNCHANGED; the elevated F&V CPI (+6.74% YoY, May) is a LAGGING Q4-25/Q1-26 winter-freeze base-effect surfacing via FSA designation-lag, NOT a fresh in-window supply collapse. Near-term supply-push to >4% faded → the path to threshold now leans on Q4 tails rather than current momentum. **Kept alive (mechanism intact — [[finding_threshold_vs_mechanism]], trim not kill):** (a) all fertilizer prints PRE-DATE the 7/8 Hormuz re-escalation → supply-rail RE-ARMED (QAFCO ~14% global urea offline since Mar-4; June decline fragile); (b) strengthening El Niño (very strong ≥+2.0°C likely OND-2026; circulated "+3°C" REFUTED — conflated Niño-1+2); (c) tightening grain stocks (lowest US wheat production since 1970/71). Timeframe unchanged; next read June CPI 7/14.
- **Data correction (STATUS urea row):** prior "$585/T May-1" was basis-inconsistent (NOLA/wholesale or UAN mislabel; correct US-retail May ~$820-860) → corrected to DEWEY's reconciled DTN-retail / WB-Pink-Sheet series (Apr peak → June rollover).
- **ENSO cite:** no CARL file carried the refuted "+3°C" figure — no-op (precautionary DEWEY flag verified clean).

### DOCKET (A1) — added June CPI 7/14
Added `2026-07-14 June CPI` to `docket/CATALYSTS.tsv` + `docket/CALENDAR.md` (both had been 8d unmaintained; earliest row was 7/15). CPI 7/14 is the near-term hinge (V12 inflation / CRL-10 / gas pass-through / core→FOMC); boot's `docket_countdown.py` now surfaces it. BLS schedule verified (7/14 8:30 ET).

---

## 2026-07-02 — THESIS v2.6 → v2.6.1 (Will-approved): V3 Fannie MF 4→3 (CRL-03 invalidated), net 52→51/70 + prediction resolutions

### THESIS — version bump v2.6 → v2.6.1 (minor: single vector downgrade on a pre-registered trigger firing, Will-approved)
**Author:** CARL (executed on Will's explicit approval, full catch-up sweep — gather workflow wng35yy0d, 7 research-only agents).

**Old → New:**
- **V3 Fannie MF DQ → GFC: 4 → 3** (⬇️). Rationale: **CRL-03's own pre-registered downgrade trigger fired.** Fannie MF serious DQ May 0.58% (Apr 0.64% → May 0.58% = 2nd consecutive month <0.65%, primary Monthly Summary Table 7; 2026 series Jan 0.73/Feb 0.74/Mar 0.78/Apr 0.64/May 0.58). Gap to the 0.80% GFC peak WIDENED to 22bps and is moving away. Honored the pre-registration — did NOT override with an extend-and-pretend rationale (which would have been the temptation, and which the trigger exists precisely to prevent). The GFC-approach mechanism in the GSE MF book is not firing → "watching, elevated." CRE/MF stress isn't gone (Trepp CMBS MF 7.71% ATH still diverges — different book), so the vector drops to 3, not off.
- **V16 Employment Structural Rot: HELD at 3 (re-arm ARMED).** June NFP +57K (vs ~110K cons) + −74K revisions (May 172→129K, −25%) revised away the Jun-1-5 strength that justified V16's own 4→3 cut. Held at 3 NOT because the case is weak but because June is single-month and doesn't hit the literal "NFP negative" trigger (it's sharp-decel-positive). July NFP (~Aug 7) resolves. Single-month-skepticism discipline applied ([[feedback_single_month_subcomponent_skepticism]]).

**Net score: 52/70 → 51/70 (73%).** Honest −1 — a housing/CRE resolver died this cycle. Histogram: 4-group loses V3 (8→7); 3-group gains V3 (5→6). Still 🔴🔴 CRITICAL.

**Why a −1 and not a paired hold:** unlike Jun-22 (V12↑/V5↓ genuine opposite-sign moves), this cycle V3's downgrade is rule-fired/clean while the offsetting V16 re-arm is real but single-month and short of its literal trigger — so the disciplined call is V3 down now, V16 armed-but-held. The truthful read: housing/CRE + gas legs eased while the consumer-income/employment core re-softened.

### PREDICTIONS — resolutions & re-marks (Jul 2)
- **CRL-03 → MISSED** (resolved 2026-07-02). Fannie MF May 0.58% = 2nd consecutive <0.65%; invalidation rule fired exactly as written. Confidence held 72% into the print.
- **CRL-11 → MISSED** (resolved 2026-07-02). May JOLTS hires rate 3.3% (unchanged); Apr's 3.2% REVISED UP to 3.3% on the same release. No 2nd sub-3.2% print ever held — series moved away from the ≤3.2% threshold. Same revision/denominator failure family as CRL-09.
- **CRL-08: confidence 40% → 28%** (re-arm, not miss). Jun 25-28 was a GENUINE kinetic escalation (tanker strikes, US airstrikes, Iran missile on a Kuwait base) yet Brent FELL through it to ~$70; gas $3.838. One clean escalation → wrong-direction price = −12pp. Re-arm now needs sanctions-waiver revoked AND Doha collapse with Brent >$85-90.
- **CRL-14: SPLIT (mechanism live / threshold STUCK).** MAJOR CORRECTION — ED paused ALL involuntary collections (AWG + Treasury Offset) Jan 16 2026 INDEFINITELY; the "Jul 15 collections restart" catalyst is contradicted (NY Fed May 12 + CBS Jul 2 confirm on-hold). Default-accrual mechanism firing (9.16M Apr). Treasury Phase 1 (~500K) is servicing custody, not enforcement.
- **CRL-13: timeframe refined** — SAVE→RAP notices began on schedule Jul 1 but are staggered in waves through Mar 2027 (non-selectors auto-enroll ~90d after each individual notice); Oct 1 = first-tranche read, not final N.

**Files:** THESIS.md (version stamp + score header + What's-Forecast Fannie line + V3/V16 matrix cells + histogram + commentary + upgrade-path + Thesis-Evolution entry), PREDICTIONS.tsv (CRL-03/11 MISSED + CRL-08/12/14 re-marks), this CHANGELOG, STATUS.md (top-line + Overall + Fannie MF/HPI/labor/UMich/gas/HY-OAS rows + matrix mirror + histogram + DANGER-WINDOW NOW + predictions table + BOTTOM LINE), KB.tsv (+ new rows), board/BOARD_LOG.tsv (+40 dispositions), docket (prune 6 fired + collections-restart STUCK + Aug-21 waiver-expiry), ROADMAP.md, NEXUS_BRIEF.md (re-pin), SCRATCH.md (rewrite). **Data caveat:** BLS/FRED primary returned 403 (sandbox network block) — labor/sentiment figures secondary-corroborated (multi-source); Fannie MF + gas were primary-verified.

---

## 2026-06-22 PM-2 — THESIS v2.5.2 → v2.6 (Will-approved): paired vector re-score V12 4→5 + V5 4→3, net 52/70 held

### THESIS — version bump v2.5.2 → v2.6 (minor: paired vector re-score, Will-approved)
**Author:** CARL (executed on Will's explicit approval of the paired move surfaced in the Jun-22 catch-up).

**Old → New:**
- **V12 Stagflation Trap / Fed Locked: 4 → 5** (⬆️, first vector ever at 5). Rationale: FOMC Jun-17 (new Chair **Warsh**'s first meeting) graded hawkish-relative — dots flipped to a HIKE (2026 median 3.4%→3.8%, 9/18 pencil hikes) on a **stagflationary SEP** (GDP 2026 2.2%↓ / PCE 3.6%↑↑ / Core PCE 3.3%); Warsh "look through energy." The "locked out of easing" mechanism is now **fully fired** — the Fed is tightening into a slowdown under a hard-money Chair (multi-meeting reaction function, not a one-print event). The prior 4-score hurdles (monthly Core PCE TTM >3.0%, UMich 5-10Y triangulation) are **superseded** by harder evidence: the Fed's OWN 3.6% PCE projection + hike-bias. **Bias-against-5 discipline preserved via an explicit un-fire condition:** reverts to 4 only on a Warsh dovish pivot (a 2026 cut returns to the dots OR presser credibly signals easing, 2 consecutive meetings). Residual "could actually hike" = escalation of degree within a sprung trap, not a higher mechanism state.
- **V5 Gas Price Squeeze: 4 → 3** (⬇️). Rationale: the gas leg of the multi-vector cost-squeeze is **relieving** — gas $3.929 falling 5th wk (−62¢ from peak), **Islamabad MOU Jun-17 waived Iran oil-export sanctions** (structural supply add), CRL-08 re-breach-via-price dead-reinforced (55→40). Mechanism intact (energy→bottom-60) but the input turned tailwind; level still elevated (+$1/gal YoY, diesel high) → "watching, elevated." Re-arm to 4 on Hormuz re-closure WITH enforcement.

**Net score: 52/70 (74%) UNCHANGED.** The +1 (V12) and −1 (V5) offset exactly. Histogram shifts: 5-group {V12} (was empty), 4-group drops V5+V12 (10→8 vectors), 3-group gains V5 (4→5 vectors). This is **rebalancing, not weakening** — the bear thesis's stagflation leg hardened while its gas-cost leg eased. Still 🔴🔴 CRITICAL.

**Why now (vs the V16-offset framing):** the Jun-6 v2.5.2 V16 4→3 downgrade was explicitly logged as "offset by a V12-hardening *candidate*." The FOMC Jun-17 hawkish-relative grade under Warsh **realizes** that candidate. The simultaneous V5 relief is the genuine counter-current (RED-honest) that keeps the net flat.

**Files:** THESIS.md (version stamp + score-section header + 5-def [now 1 at 5] + V12/V5 matrix cells + histogram + commentary + upgrade-path + Thesis-Evolution entry), STATUS.md (Overall + top-line + V12/V5 cells + histogram + 5-def + total note), this CHANGELOG, NEXUS_BRIEF.md (re-pin), ROADMAP.md (open thread → RECENTLY RESOLVED). No PREDICTIONS change (score move is vector-level, predictions unaffected).

---

## 2026-06-22 PM — 6-day catch-up sweep (gather workflow w95yzkviz): FOMC Jun-17 graded HAWKISH-RELATIVE under NEW Chair Warsh; V12 4→5 + V5 4→3 paired v2.6 candidates (net 52/70 held); CRL-08 trim 55→40; CRL-07 magnitude caveat; 32 BOARD signals + 4 releases integrated; no thesis version bump (v2.5.2 holds)

### Macro-regime change (not a thesis edit, but load-bearing context)
**Kevin WARSH is Fed Chair — Jun 17 was his FIRST meeting** (Powell now a voting member). A Warsh-led Fed is structurally harder-money than Powell's; "Fed locked, no relief coming" is now a multi-meeting reaction-function reality, not a one-print event. Validates auto-memory `finding_boot_sweep_macro_regime_context` (boot baselines don't cover Fed-Chair/leadership changes — bake a regime check into boot). The boot did not catch this; the FOMC gather did.

### FOMC Jun-17 GRADE → HAWKISH-RELATIVE (CARL pre-registered modal 45% — clean hit)
HOLD 3.50-3.75% unanimous 12-0, but **dots flipped to a HIKE**: 2026 median 3.8% (Mar 3.4%; 9/18 pencil hikes, 1 cut; 17/18 inflation-risk-up); 2027 3.6%. **Stagflationary SEP:** GDP 2026 2.2% (−0.2), UR 4.3%, PCE 3.6% (+0.9), Core PCE 3.3% (+0.6). Warsh "look through energy." Market: 2Y +11-16bp (biggest Fed-day since Mar-2008), 30Y >5.00% (highest since 2007), CME hike-by-2026 47%→77%. Graded against the pre-registered tree in `FOMC_PACKET_2026-06-17.md` §3 (§6 grading stub filled). Honored pre-registration: **V12 held 4, conviction sharply UP, v2.6 upgrade (4→5) RE-ARMED** — the energy-driven UMich 5-10Y 3.4% retrace caveat that had blocked auto-upgrade is now overridden by the Fed's OWN 3.6% PCE projection (committee not believing the disinflation). KB-CARL-298.

### THESIS — no version bump (v2.5.2 holds); two OFFSETTING v2.6 score candidates flagged for Will
- **V12 Stagflation Trap / Fed Locked: 4→5 candidate.** Strongest single V12 confirmation in thesis life (FOMC published a stagflationary SEP + flipped to a hiking bias under a hard-money Chair). Held at 4 today per FOMC-packet pre-registration (a 4→5 = thesis-version v2.6, warrants its own review).
- **V5 Gas Price Squeeze: 4→3 candidate.** Gas $3.929 (5th wk down), Islamabad MOU Jun 17 WAIVED Iran oil-export sanctions (structural supply add), CRL-08 dead-reinforced. The gas-squeeze leg is genuinely RELIEVING (counter-current to the bear thesis; mechanism intact, input turned tailwind) — RED-honest downgrade.
- **Net: 52/70 HELD** (V12↑ and V5↓ offset). Both surfaced as the paired v2.6 score-review for Will to adjudicate, rather than silently moving the headline.

### PREDICTIONS.tsv
- **CRL-08 55→40% (re-arm + trim).** Iran oil sanctions waived + gas −5wk + Brent near pre-war = P(Brent→$105-110 in window) materially lower (−15pp). Re-arm not MISS (pass-through intact). GIG corroborates via independent EIA series (peaked $4.50 May 11, reverted).
- **CRL-07 85% HELD + magnitude caveat.** Wave-1 cliff timing confirmed NOW (Jun 24); but FL ~8% recipiency (~42.5K active) means the income cliff is small in absolute terms — load-bearing transmission is the gig-supply-surge channel (DoorDash $100M subsidy), not aggregate UI dollars. Magnitude resolves on DQ-conversion 30-60d post-cliff.
- **CRL-03 72% HELD** — decisive Fannie MF May print drops ~Jun 26 (Q2-window resolver; Apr 0.64% = month-1 of the <0.65%-2mo invalidation).
- **CRL-23 70% HELD** — NAHB June (price-cutters 35%, incentives 62%, traffic 25) + national builder-overhang ~2x existing reinforce the compression baseline; FY27 tariff leg still the actual test.

### Integrations (data + signals)
- **4 fired releases:** Retail Sales May (+0.9% headline / control +0.7% / gas-padded; forced-consumption at 2.6% savings), NAHB June 35 (14th mo <40, traffic 25), Existing Home Sales May 4.17M (bounced >4.0M but low-velocity, weakest cycle appreciation), Sweet v. McMahon FIRED (~30-36K discharge emails Jun 15 — small K-shape relief pulse). KB-CARL-296/297.
- **Student-loan defaults ~9.2M Apr — CLIMBING wall** (6.0M Aug→7.7M Dec→9.16M Apr, Bloomberg), reframes CARL's static-stock view. KB-CARL-299. New CRL-prediction candidate on next NY Fed HHDC.
- **32 BOARD signals dispositioned** (Jun 18-22): 3 INTEGRATED CARL-lead (consumer-discretionary K-shape SIG-621-005, student-loan SIG-621-012, builder-overhang SIG-621-013), 29 REFERRED (FL→CORAL, energy→HAWK/BRENT, bank/CRE→REGINALD, vol→HENRY, Japan→SAM, private-credit→BROCK). KB-CARL-300/301. 0 undispositioned remaining.
- **GIG refreshed** (66d gap): driver oversupply confirmed, Dave Q1 1.69% survivorship-biased (provision +151% YoY), FL UI magnitude-constrained, gas receding. SV-GIG-2026-06-22-01.

---

## 2026-06-14 PM — Sun data sweep + ORC echo-verify: energy decoupling reverses V12 expectations channel; CRL-08 re-test FIRED & FAILED (trim 70→55); LEN FQ2 guide-cut integrated; UMich May-final backfill; no thesis version bump

### PREDICTIONS.tsv — CRL-08 70→55% (re-arm + trim); CRL-23 LEN datapoint (conf held)
**Author:** CARL (Sun Jun 14 sweep; graded by ORC via primary-source recomputation before write).

**Sweep (new data Jun 11-14, scoped by mechanism/falsification not topical):**
1. **LEN FQ2 (rel Jun 11):** GM 15.6% (−220bps YoY from 17.8%), EPS $1.24 (−31% YoY), ASP $371K (−5%), orders −4%, incentives 12.9% (Q1 14.1%), constr-cost −7%, **FY26 delivery guide CUT ~85K→82-83K** ("interest rates + geopolitical uncertainty"), stock −4.9% Jun 12. *ORC caught the guide-cut as the market-mover I'd missed in first pass; verified vs LEN release.* Read = K-shape demand biting NOW (volume cut, margin defended), bounded to RATES not energy (cut came with Brent already ~20% off peak → energy relief underway didn't stop it). CRL-23 datapoint, conf 70% HELD (refines baseline; FY27 tariff GM leg still ahead).
2. **UMich June prelim (rel Jun 12):** sentiment 48.9 (+9%, first rise 4mo); 1Y 4.6% (eased from May Final 4.8%); **5-10Y 3.4% RETRACED below 3.5% Fed red line** from May FINAL 3.9% spike ("erasing May's jump"). Survey window late-May→Jun 10 = early-June gas relief; Jun 7-10 kinetic was INSIDE window yet long-run exp fell = strengthens decoupling. *Backfilled May finals (5-10Y 3.9 / sentiment 44.8) into STATUS ledger — they were never integrated, hiding the spike-and-retrace.*
3. **Energy decoupling (BRENT corr Jun 13):** Brent ~$87 FALLING (not "$94-95 climbing" — STATUS row was wrong, now a referenced value `[CONF BRENT Jun 12 $87.20]`). Kinetic Jun 7-10 primary-confirmed but crude fell through it. Pump $4.074 Jun 14, falling 4th wk.

**CRL-08 — re-arm + trim 70→55%:** registered fresh-kinetic trigger fired & failed; Brent decoupled down to $87, moving away from the $105-110 transmission zone. Per threshold-vs-mechanism: pass-through INTACT (RBOB sticky, crack $42.55) → re-arm not MISS; but P(gas $4.50)=P(Brent→$105-110)×P(pass-through) and the dominant path to the input just closed → −15pp (ORC flagged silent-flat-hold as the generous read). Not zeroed — July window + Hormuz/refinery tails.

**Net synthesis:** energy disinflation is reversing the V12 expectations channel (5-10Y back below red line, sentiment bouncing) while core/PPI-6.5%-pipeline stagflation stays intact. FOMC 6/16-17 spine stays V12: energy→expectations-retrace→core-sticky; near-term hike pressure eased on the EXPECTATIONS leg. **No score move, 52/70 holds.**

**ORC review folded in:** (a) CRL-08 trim not silent-hold; (b) LEN bounded to rates-not-energy (don't read a housing-demand turn into a marginal wallet tailwind); (c) UMich May-final ledger backfill; (d) decoupling-arrow phrased "gas relief through early June" not "$4.07→expectations"; (e) Brent as referenced value not CARL-owned row. Deferred (ORC): convergence-matrix stale evidence cells (V1 12.70%/1.04pp vs live 13.1%/0.64pp; V3/V4/V5/V12) → ROADMAP backlog (no score move, not gating); exact LEN mgmt "4.2% energy" quote is release-sourced not transcript (KB row to cite release + note rates-paired).

---

## 2026-06-11 AM — May CPI graded vs pre-registered sheet (2/5 hits); May PPI 6.5% YoY record-goods print; CRL-08 re-test condition MET on Iran re-ignition; CRL-10 pull-forward caveat withdrawn; no thesis version bump

### PREDICTIONS.tsv — CRL-08 re-test live; CRL-10 timeline reverts to baseline
**Author:** CARL (Jun 10 CPI was past-due at boot — no Jun 10 session ran; graded against the Jun-9 SCRATCH pre-registered sheet, which was written before the print and counts as pre-registration).

**CPI May grade (pre-registered 5-row sheet from Jun-9 SCRATCH):**
1. Headline +0.5% MoM → V12 hardens: **HIT** (+0.5%/4.2% YoY, accel from 3.8%).
2. Core +0.4% → Fed-no-cut locks: **MISS** — Core +0.2% MoM, HALVED from Apr. Apr "breadth widening" did not extend; symmetric single-month caveat applied before banking "core contained."
3. Food at Home +0.5% 2nd consec → CRL-10 75→85%: **MISS** — FaH +0.1%. CRL-10 holds 75%, Q4 baseline reinstated, possible-Q3 caveat withdrawn from Timeframe column.
4. Hospital MoM ≤0 → DOC care-avoidance 2nd-print: **MISS** — +0.7% sign-flip back up. CPI-pricing channel watch closed negative; NIPA channel unaffected. 3rd single-month-skepticism validation. KB-CARL-293.
5. Energy MoM small-pos → CRL-08 intact: **HIT on direction, magnitude exceeded** (+3.9% MoM, >60% of headline increase).

**Net read:** energy-led headline stagflation, NOT core broadening. V12 splits: headline/expectations channel hardening (4.2% feeds UMich Jun prelim 6/12 vs 3.5% 5-10Y red line) while core-breadth channel softened. This headline/core divergence is the FOMC Jun 16-17 tension. No score move.

**May PPI (rel Jun 11):** +1.1% MoM / 6.5% YoY highest since Nov 2022; final-demand goods +2.8% MoM largest-ever in series (80% = energy +10.7%; wholesale gasoline +23.4%); core +0.4% below cons; services +0.3%. Hormuz-closure wholesale transmission → Jun-Jul CPI pipeline. KB-CARL-292; VX-CARL-MACRO-05 4.0→6.5 RED.

**CRL-08:** pre-registered fresh-Iran-kinetic re-test condition MET Jun 7-10 (US strikes on Iran day 2 + IRGC Hormuz near-total closure + Bab al-Mandab activation; BOARD SIG-W-20260610-001/-002 dispositioned REFERRED→BRENT/HAWK). Pump $4.129 Jun 11 still falling; Brent ~$94-95 well below the ~$105-110 transmission zone for a $4.50 re-breach. Conf 70% holds; Timeframe updated May-Jun→Jun-Jul. Fire only on registered condition ($4.50+ sustained 2wk) per pre-registration discipline.

**Failure-pattern check (step 7c):** the FaH and core misses are the inverse of CRL-01/CRL-19 (direction right, magnitude light) — here the pre-grade over-extrapolated a single hot month. Same family: single-month moves carry too much weight at write time in both directions.

---

## 2026-06-09 PM — STUE follow-up: CRL-04 methodology asterisk DROPPED; Treasury Phase 1 cadence resolved directionally; no thesis version bump

### PREDICTIONS.tsv — CRL-04 CONFIRMED* → CONFIRMED
**Author:** CARL (STUE SendMessage follow-up after morning integration).

**Workflow notes:**
- **Follow-up bundle to STUE** (mailbox-mode resume) on two morning OPEN QUESTIONS: (Q1) NY Fed VantageScore 4.0 methodology backcast and (Q2) Treasury Phase 1 full-scope schedule. Both decision-led for Jun 16-17 FOMC packet framing. ~20-min STUE round-trip.
- **Q1 verdict — Answer (C) effectively:** NY Fed 90+ DQ rate is **balance-based** (delinquent $ ÷ total $), independent of credit-scoring methodology. VantageScore 4.0 transition (Liberty Street Economics May 12 2026 primary quote: "*Starting with this report, the figures and analysis that depend on credit scores will shift to using VantageScore 4.0*") applies ONLY to credit-score-band distributional cuts on report pages 6-9. Wolf Street May 12 2026 cross-confirms 90+ DQ as a balance ratio. The 9.6% Q4 2025 → 10.3% Q1 2026 (+70bps) move is fully apples-to-apples. **Methodology asterisk dropped** in PREDICTIONS.tsv CRL-04 row, STATUS Student Loan 90+ DQ row, and STATUS PREDICTIONS Resolved table.
- **Q2 verdict — directional cadence resolved:** CRS report R48962 + ED Mar 2026 internal reporting (Inside Higher Ed Mar 19 2026; Washington Times Mar 20 2026: "starting with fewer borrowers and ramping up more gradually rather than 'turning the floodgates on'"). **Cadence framing: ~500K Jul-Sep launch → gradual scale-up → full ~9M defaulted likely 12-24mo rollout into 2027.** Phase 2 (non-defaulted) trigger date NOT public. No quarterly numbers published. STATUS Defaults row expanded with cadence + implication line ("not a Jul-1 cliff, multi-quarter rolling load Q3 2026 → Q1 2027").

**Net analytical state:**
- **CRL-04 disposition cleaner than morning:** confidence on threshold breach raises 95% → 98%; flow-vs-stock single-print flag (transition rate INTO 90+ DQ dropped 16.2% → 10.9%) preserved separately — that's a different question and unaffected by today's methodology resolution.
- **FOMC packet reframe:** CRL-04 line item can be presented WITHOUT methodology caveat. Treasury phasing line: lead with "500K Jul launch + multi-quarter ramp through 2027" rather than "9.2M transferred." Both are cleaner framings than morning version.
- **Asterisk residual:** STUE's own STATUS thesis paragraph still carries old methodology-asterisk wording (line 27 of STUE/STATUS.md). Minor; flag for STUE next pass.

**Lessons:**
1. **Mailbox-mode SendMessage follow-up earns its keep** for narrow decision-led follow-ups where the agent already has context. ~20-min round-trip vs full re-spawn. Validates [[finding_teams_mode_iterative_tasks]] with a third datapoint (HOMER Jun-8 disambiguator + STUE Jun-9 morning + this PM follow-up).
2. **The morning asterisk was the right call given session-time information** — without the Liberty Street primary quote, methodology-asterisk-pending-Q2 was the conservative framing. The PM follow-up tightened it from "conservative" to "clean," not from "wrong" to "right." Worth distinguishing.
3. **Treasury Phase 1 cadence is now directionally framed** but full schedule still TBD pending Phase 2 spec. If FOMC packet ships before that resolves, "12-24mo rollout into 2027" is the durable framing.

---

## 2026-06-09 — STUE sub-agent refresh integrated; CRL-04 CONFIRMED* (threshold breached, magnitude 2nd-print pending); Treasury Phase 1 scope corrected; SAVE→RAP operationally confirmed; no thesis version bump

### PREDICTIONS.tsv — CRL-04 OPEN-NEAR CONFIRMED → CONFIRMED*
**Author:** CARL (Will-directed STUE spawn, Opus, after 53-day refresh gap).

**Workflow notes:**
- **STUE spawned (Opus, single-shot)** after 53-day STATUS staleness — STUE-domain catalysts (Sweet Jun 15, AFT/MOHELA May 28, SAVE→RAP Jul 1) had passed or were imminent without sub-agent-level integration. Three load-bearing findings, two STATUS corrections, 5 honest OPEN QUESTIONS.
- **Discipline applied:** year-stamping confirmed primary source for every web-pulled metric (per [[finding_subagent_year_verification]] candidate, codified post-HOMER Jun-8 catch); threshold-vs-mechanism separated cleanly; single-month skepticism preserved on Q1 transition-rate drop; no invented numbers (items NOT confirmable went to OPEN QUESTIONS file, not STATUS).

**CRL-04 disposition:**
- **CONFIRMED\*** — NY Fed Q1 2026 QHDC (rel May 12 2026) prints student loan 90+ DQ at **10.3%**, first primary-source >10% reading.
- **OLD view (Apr 17):** OPEN-NEAR CONFIRMED at 98%. "~9.8% FICO Spring 2026" cited as latest; threshold-crossing imminent Q2.
- **NEW view (Jun 9):** Threshold MET on direction (95% conf on breach). Magnitude carries 2nd-print asterisk — NY Fed shifted scoring methodology this release (Equifax Risk Score 3.0 → VantageScore 4.0). Mechanism unambiguously intact (+2.6M Q1 defaults + 1M Q4 2025 = 3.6M cumulative DRG transfers; >17% of borrowers 90+ DPD at least once since repayment resumed; avg defaulter age 38.9 vs 36.4 pre-pandemic).
- **STATUS correction:** prior CARL STATUS Apr-17 "FICO Spring 2026 9.8%" was a derivative cite; primary FICO Spring 2026 doc reads 11% Oct 2025. NY Fed Q1 2026 10.3% is now the operative number.
- **Mixed internal:** transition rate INTO 90+ DQ (4Q sum) DROPPED 16.2% → 10.9% same release. Stock-up/flow-decelerating split needs Q2 (~Aug) to disambiguate (on-ramp slack residual vs seasonal vs cohort exhaustion). Does NOT invalidate breach.
- **Asterisk convention** matches CRL-02 (also CONFIRMED* on rounding/magnitude caveat with direction robust).

**Non-prediction integrations:**
- **Treasury Phase 1 scope correction.** Prior CARL STATUS framed "~9.2M defaulted borrowers transferred" at Mar 19 Phase 1 launch. Multiple Mar-Apr 2026 primary sources (Inside Higher Ed, US News, Washington Times) reframe Phase 1 launch as **~500K defaulted accounts** managed by Treasury "this summer" / July 2026. Material order-of-magnitude refinement on operational-capacity story — absorbing 500K is plausible, 9.2M in one go was not. Remaining ~8.7M Phase 1 timing in OPEN QUESTIONS.
- **SAVE→RAP Jul 1 operationally GO.** ED sent **Round-2 "courtesy" emails** to ~7M SAVE borrowers late-May / early-Jun 2026 (College Investor, June 2026 + ED press + tateesq.com cross-confirm). Schedule confirmed: starting Jul 1, servicers issue 90-day notices in waves every 2 weeks; non-selectors auto-enrolled in Standard / Tiered Standard at Oct 1. ~$1.5-2.0B/mo spending destruction begins Jul 1 = ~$5-7B Q3 consumer drag.
- **CRL-13 / CRL-14 unchanged.** SAVE non-selection (CRL-13 at 75%) holds — empirical baseline 30-47% unchanged. MOHELA-caused defaults (CRL-14 at 65%) holds — May 28 status conference held without public ruling = absence-of-news is non-information.
- **5 OPEN QUESTIONS surfaced** (STUE/OPEN_QUESTIONS_2026-06-09.md): AFT/MOHELA May 28 outcome (court-docket pull needed), Sweet Jun 15 notice mailing status, NY Fed methodology backcast availability, FSA Q1 2026 release status, Treasury Phase 1 full-scope vs initial-wave.

**STATUS.md mutations:** Student Loan 90+ DQ row refreshed (9.8% derivative → 10.3% primary NY Fed Q1 2026, with methodology asterisk); SAVE Transition row reframed (Round-2 courtesy already sent — operational GO); Sweet row notes refresh (Jun 15 deadline pending, no public mailing confirmation yet); MOHELA row (May 28 conf held no ruling); +2.6M Q1 2026 defaults flow row added (Liberty Street Econ); Treasury Phase 1 scope corrected; Recently Fired digest extended to include Jun 9 STUE integration.

**FOMC packet (Jun 16-17) line items:**
- CRL-04 BREACHED (primary-source, fresh, threshold-crossing real-economy stress data point)
- SAVE→RAP operational-GO (22-day-forward Q3 consumer spending drag begins)

**Lessons:**
1. **STUE-level disambiguator pass not needed** — first-round web-pulls survived year-stamping audit (unlike HOMER round-1 Jun 8). Discipline now codified in STUE's own conduct + the four hard rules in CARL's spawn prompt.
2. **Treasury Phase 1 scope error originated in CARL STATUS, not STUE** — would have lived indefinitely without sub-agent fresh-eyes pass. Auto-memory candidate: when accreting catalysts off press releases (vs primary policy docs), occasional sub-agent re-audit catches drift.
3. **CRL-04 is the 4th formally-resolved CRL prediction** (CRL-01 MISSED, CRL-02 CONFIRMED*, CRL-09 MISSED, CRL-18 CONFIRMED, CRL-19 MIXED, now CRL-04 CONFIRMED*). 6 of 23 resolved; 2/6 are asterisked direction-right/magnitude-light pattern (CRL-02 + CRL-04). Add to calibration record.

---

## 2026-06-08 PM — DOC + HOMER sub-agent refresh integrated; CRL-03 mechanism reframed (extend-and-pretend); 4 new VX rows; no thesis version bump

### PREDICTIONS.tsv — no changes; CRL-03 confidence HELD 72%
**Author:** CARL (Will-directed sub-agent refresh; 3 spawn rounds incl. error-correction round).

**Workflow notes:**
- **DOC spawned (round 1)** to refresh healthcare-cost-stress dashboard ahead of Wed Jun 10 CPI + Jun 16-17 FOMC. Returned 3 SVs + STATUS refresh.
- **HOMER spawned (round 1)** to refresh housing-stress dashboard for Jun 16-30 cluster. Returned with CRL-03 invalidation lean (72% → 30%) citing Trepp CMBS MF May "6.57% (-46bps reversal)" as cross-confirmation of Fannie Apr -14bps direction.
- **HOMER round 2 (disambiguator)** sent to test extend-and-pretend hypothesis (REO completions + mod activity + MF FC pipeline). **HOMER self-caught a year-misread**: the Trepp "-46bps reversal" was **May 2025**, not 2026. Actual Trepp CMBS MF Apr 2026 = **7.71% NEW ATH (+56bps MoM)**. Series did NOT cross-confirm — they diverged. Round 1's invalidation argument collapsed.
- **HOMER round 3 (cleanup)** sent to purge round-1 framing from HOMER's files + codify year-verification discipline. SV-01 moved to `corrected/` with corrected-header; STATUS audited end-to-end (5 additional contamination sites fixed beyond the masthead); calibration rule added: *"Before citing any web-pulled metric as load-bearing, confirm the year explicitly from the primary source — relative phrasing ('May print') is INSUFFICIENT. If primary source isn't fetchable, the metric stays in OPEN QUESTIONS until verified."*
- **The disambiguator pass earned its keep.** Round 2 wasn't sent to catch an error — it was sent to test a hypothesis. Agent self-corrected by going to fresh sources. Auto-memory promotion candidate: **sub-agent year-verification discipline** (transferable to BRENT/SAM/REGINALD/HENRY web-pulling sub-agents). Deferred per `memory/auto/` flux.

**CRL-03 analytical state:**
- **Held at 72%** (no change). Mechanism intact; "extend-and-pretend" regime now Trepp-documented (Feb 2026 CMBS DQ drop was driven by mods on 5 office + 4 mall loans, 1mo-3yr extensions). Fannie Apr -14bps best explained by mod/extension activity, not borrower resolution.
- **Threshold rule NOT redefined** (Will decision — clean falsifiability > mid-flight rule changes). Instead, added 2 shadow-tracker VX rows to catch what the headline misses.

**Workbook mutations:**
- VX.tsv +4 rows: VX-CARL-MF-03 (Trepp MF watchlist share — extend-and-pretend shadow), VX-CARL-MF-04 (CMBS MF special-servicing transfer rate — extend-and-pretend shadow), VX-CARL-HSG-03 (Realtor.com median list price YoY — housing-deflation leading edge, -2.4% YoY May = steepest since 2017), VX-CARL-HC-01 (Mercer employer benefits cost +6.7% 2026 = 15-yr high, top-40% transmission channel).

**STATUS.md mutations:**
- Multifamily section reframed (Fannie MF + CMBS DQ rows): mechanism INTACT via extend-and-pretend; status color split 🟠 headline / 🔴 mechanism.
- Housing additions (HOMER): 30Y mortgage refreshed Apr 30 6.30% → Jun 4 6.48%; NAHB HMI Apr 34 → May 37 (bounce not recovery, 25th consec <50); +Realtor.com list price -2.4% YoY (leading edge); +ICE Active FC 276K +32% YoY (above Mar 2020 pre-pandemic for 2nd consec mo); +MBA Q1 NDS 4.44% (FHA + VA FC inventory at decade-plus highs); +Redfin 47% sellers/buyers gap Apr (narrowing from 49% end-2025 peak — softens "demand fading" framing).
- Healthcare additions (DOC): +Mercer +6.7% benefits row (V14 candidate); +ACA mid-year attrition realizing (effectuated -17% nat'l / -21% federal-marketplace Feb→Apr 2026; avg premium $113 → $178); +Medical Care CPI Apr 2.5% YoY (hospital MoM -0.3% sign flip = Wed Jun 10 watch anchor); +NIPA care-avoidance row (Q1 GDP largest single contributor to consumer-services downward revision).
- Trims to stay at 250 cap: WTI / Russia AN / Initial Claims wk-5/16 / Avg Weekly Hours / EPOP / FL Condo Inventory / Auto Insurance CPI / Tariff Burden — all either stale, low-signal, or absorbed into successor rows.

**Docket mutation:**
- **LEN FQ2 date corrected Jun 16 → Jun 11** (4:00 PM ET, verified). HOMER round-2 catch; CATALYSTS.tsv + CALENDAR.md updated.

**Net thesis impact:** zero score moves. v2.5.2 holds. V14 reinforcement candidate (Mercer benefits-cost as top-40% transmission) staged for Jun 16-17 FOMC score-decision packet, NOT moved today on single primary-via-aggregator signal.

**Lessons:**
1. **Sub-agent year-verification discipline gap** — needs codification at the network level (HOMER own-spec now has it; not yet promoted to siblings).
2. **Disambiguator pass earned its keep** — iterative SendMessage > single-shot spawn for load-bearing claims. Already validated in auto-memory `finding_teams_mode_iterative_tasks`; this is another datapoint.
3. **HOMER's "extend-and-pretend" framing** is the right way to read Trepp's regime commentary going forward — preserved in CMBS row Notes.

---

## 2026-06-08 — Consistency pass: STATUS↔PREDICTIONS drift reconciled (7 rows)

### PREDICTIONS.tsv — 2 rows updated; STATUS.md — 5 rows updated; no THESIS version bump
**Author:** CARL (Will-directed boot cleanup; surfaced by Jun-8 boot-side consistency check — first time the new step-15 mirror check ran retroactively).
**Trigger:** Boot scan compared STATUS PREDICTIONS table vs `thesis/PREDICTIONS.tsv` and found 7 drift cases. SCRATCH (Jun 6) had reported step-15 CLEAN, but only verified the CRL-15/16/17 drift it was actively closing — pre-existing drift on other rows went unchecked. Mirror-direction rule: canonical (TSV) wins where canonical is current; where STATUS holds a newer analytical update that never propagated back to TSV, update TSV + log here.

**TSV-canonical-wins → STATUS updated to match (no analytical change):**
- **CRL-04** confidence 95% → **98%** (Apr 17 reprice on FICO Spring data was never mirrored to STATUS).
- **CRL-06** confidence 70% → **78%** (Apr 17 reprice on Q1 ATTOM 82,631 FC starts was never mirrored).
- **CRL-11** confidence 85% → **83%** (Mar 31 minor reprice was never mirrored).
- **CRL-13** confidence 70% → **75%** (Apr empirical-baseline validation reprice was never mirrored).
- **CRL-22** timeframe "FY27 (early 2027)" → **"Q4 2026 / Q1 2027"** (TSV specificity was never mirrored).

**STATUS-newer → TSV updated to match + logged here (analytical work recovered):**
- **CRL-05** confidence 82% → **85%** (5/22 PM reprice on Q1 2026 NY Fed HHDC: CC 90+ DQ printed 13.1% = 15-yr HIGH, gap collapsed 1.04pp → 0.64pp, NY Fed researchers cite subprime-driven K-shape converging downward = direct mechanism confirmation in primary data). This reprice was applied to STATUS at the time but never propagated to PREDICTIONS.tsv or CHANGELOG. Now canonical.
- **CRL-10** confidence 70% → **75%** + timeframe "Q4 2026" → **"Q4 2026 (possibly pulling forward to Q3)"** (5/12 reprice on Apr CPI Food at Home +0.7% MoM — pulling forward vs baseline; wheat 107yr low + urea + tariff transmission now visible on shelves earlier than expected). Same propagation gap — STATUS-only at the time. Now canonical. Single-month skepticism caveat added — needs May CPI (Jun 10) Food at Home confirmation before treating as load-bearing pull-forward.

**No score / thesis impact.** Net analytical-state change: zero (this reconciles the books, doesn't move the books). Mechanism: drift accumulated because the May 22 and May 12 in-session updates to STATUS predictions table didn't flow back to TSV/CHANGELOG (closeout discipline gap pre-dating the Jun-6 Phase-1+2 hardening).

**Lesson (auto-mem candidate):** the new step-15 consistency check needs to run on FULL row coverage at every closeout, not only on rows actively being modified that session — otherwise drift accumulated from prior sessions stays invisible. Add to Phase-3 `scripts/consistency_check.py` as a row-by-row diff vs. text-grep approach. *(Filed against closeout-hardening Phase 3 thread in ROADMAP.)*

---

## 2026-06-06 — Jun 1-5 data wall: V16 4→3 EXECUTED (v2.5.2, Will-approved), V12 hardened

### THESIS v2.5.1 → v2.5.2 (minor refinement — vector downgrade, mechanism intact)
**Author:** CARL (Will-approved same session). **Score: 53/70 → 52/70 (74%). Still 🔴🔴 CRITICAL.**
- **V16 Employment Structural Rot 4 → 3, re-anchored.** Acute legs reversed on Jun 1-5 wall (JOLTS 0.91→1.03 inversion gone; 3-mo NFP avg 48K→188K on +93K revisions; UR 4.3% held) — those were *acute-break* anchors that never belonged in a "rot not break" vector. Structural-freeze legs survived + got cleanest confirmation (hires fell 5.1M as openings jumped +731K; ISM Svc Emp 47.9 contracting 3rd mo; duration 25.7wk / LFPR 61.9%). Mechanism intact, escalation path receded → "watching, elevated" not "firing w/ room to escalate." **Re-arm to 4** if next JOLTS re-inverts OR next NFP negative w/ down-revisions; drop to 2 if hires >3.8% + ISM Svc Emp >50 + duration <22wk.
- **Offset:** V12 (Stagflation/Fed-Locked) hardened same week (Waller + sticky ISM Prices Paid 82.1/71.3 + AHE 3.4%<CPI 3.8% + "no Fed cut") = active v2.6 upgrade candidate. **Net conviction ~flat — rebalancing, not weakening.**
- **⚠️ CONTEMPORANEOUS COUNTER-VIEW (recorded for honesty, surfaced during the Jun-6 cross-machine fork reconciliation):** an *independent* CARL pass (laptop, commit `5f8e975b`, Jun 5) integrated the **identical 5 prints** and reached the OPPOSITE conclusion — *"structural rot not acute break exactly fits the print shape → V16 reinforced, HOLD at 4. Score impact: none net."* Both passes agree the structural-freeze/internals legs survive; they split on whether the strengthening headline = **step down** (acute escalation path receded — this v2.5.2 view, Will-approved) vs **hold** (mechanism intact — Jun-5 view). Kept 4→3 per Will (Jun 6); **flagged for re-examination at the Jun 16-17 FOMC/SEP convergence review**, where the V12/score pass is already scheduled. Two independent passes disagreeing on this vector by 1 point is itself a calibration signal — neither side is clearly wrong.
- **Files:** THESIS.md (header v2.5.2 + matrix row + histogram 53→52 + vector #5 prose re-anchor + version-history v2.5.1/v2.5.2 entries + load-bearing commentary), STATUS.md (matrix mirror + histogram + total + overall line). PREDICTIONS.tsv: CRL-11 supportive note (prior). CRL-09 stays MISSED.

### Original integration note (Jun 1-5 data wall, V12 hardened)
**Author:** CARL (Will-directed data-gap integration; STATUS was 8d stale, boot docket caught 6 unintegrated catalysts).
**Trigger:** ISM Mfg May (Jun 1), JOLTS Apr (Jun 2), DG Q1 (Jun 2), ISM Svc May (Jun 3), BLS May NFP (Jun 5).

**What moved — V16 (Employment Structural Rot, scored 4):**
- **Old view:** acute labor deterioration tracked via JOLTS inversion (0.91→0.95→~0.98), persistent downward NFP revisions, 3-mo avg ~48K.
- **New data:** JOLTS Apr openings 7.6M / **ratio 1.03 = inversion BROKEN** (highest since Jan 2024); May NFP +172K with **Mar/Apr revised +93K UP** (214K/179K) → 3-mo avg ~188K. The downward-revision pattern REVERSED.
- **Disposition:** V16 anchors broke → **DOWNGRADE REVIEW 4→likely 3**, NOT executed unilaterally (vector-score change moves convergence total 53/70; thesis-level → Will weighs in). Flagged in STATUS matrix + DANGER WINDOW. **Surviving V16 legs:** JOLTS hires FELL to 5.1M (openings-up/hires-down divergence = structural-freeze signal, CRL-11 SUPPORTIVE), ISM Svc Employment 47.9 (contracting 3rd mo), duration/LTU.

**What hardened — V12 (Stagflation Trap / Fed Locked, scored 4):**
- ISM Mfg Prices Paid 82.1 + **ISM Svc Prices Paid 71.3 (highest since Aug 2022, oil/diesel-driven)** = cost-side broadening. AHE +3.4% YoY < CPI ~3.8% = real-wage decline continues. Strong labor + sticky prices "crushes Fed-cut hopes" → Waller-pivot / Oct-hike modal reinforced.

**Mechanism note:** v2.5.1 mechanism is *cost squeeze, NOT employment detonator* — so strong-labor data does NOT falsify the core thesis; it reinforces V12 (Fed can't cut → squeeze prolonged). The casualty is the V16 acute-rot leg. **Counter-case honesty:** the soft-landing / CONTAINMENT alt-hypothesis gains genuine support on acute-employment legs → staged for RED (handoff_RED).

**PREDICTIONS.tsv:** CRL-11 note updated (SUPPORTIVE, 83% held). CRL-09 stays MISSED (now confirmed harder — inversion anchor gone). No other mutations.

---

## 2026-05-29 — CRL-18 CONFIRMED (GDP Q1 2nd est) + CRL-08 re-armed OPEN (gas un-sustained)

### PREDICTIONS.tsv — 2 rows, no THESIS version bump
**Author:** CARL (Will-directed 5/28-print resolution session)
**Trigger:** BEA GDP Q1 2nd estimate (May 28) + AAA pump re-check (May 29).

**CRL-18 OPEN → ✅ CONFIRMED (Date_Resolved 2026-05-28):**
- Predicted (May 1, 60% conf): Q1 GDP 2nd est revises advance 2.0% down 0.2-0.4pp into 1.6-1.8%.
- Actual: **+1.6%, -0.4pp** — landed at the bottom edge of the predicted band. Clean hit at 60% conf.
- Drivers (CARL-domain): consumer SERVICES decline led by healthcare (Census QSS) + private inventory drawdown (mfg+retail); goods (recreation/vehicles) revised UP = forced/trade-down pattern.
- **Stagflation signature in one release:** real growth revised DOWN while Core PCE prices revised UP to 4.4% ann. (from 4.3% advance); headline PCE 4.5% held. Realized core PCE 4.4% >> UMich 5-10Y 3.5% red line → **V12 (Stagflation Trap) hardens further post-Waller.**

**CRL-08 — FIRST-CROSS-NOT-SUSTAINED, re-armed OPEN (confidence 92% → 70%):**
- AAA $4.391 (May 29) = -17.3¢ from $4.564 peak (May 21), ~11¢ below the $4.50 threshold.
- Breach window ~May 21-26 (5-6 days at/above $4.50) decisively failed the 2-wk sustained requirement; Memorial Day spike fully reverting.
- Mechanism INTACT, threshold UN-sustained → prediction stays OPEN (re-armed), re-test requires fresh Iran-kinetic re-spike. No V5 score upgrade. Brent -10% from 5/5 peak transmitted in reverse at ~17-18d lag (empirically consistent both directions this cycle).
- Threshold-vs-mechanism discipline applied (cf. [[finding_threshold_vs_mechanism]]): threshold retraced but mechanism held → re-arm, not MISS.

**CRL-09 — OPEN → ❌ MISSED (Date_Resolved 2026-05-05, caught 5/29):**
- Predicted (Mar 31, 73% conf): JOLTS Mar openings/unemployed ratio drops <0.88 (from 0.91 Feb).
- Actual: **0.95** (6.866M openings / 7.239M unemployed, rel May 5) — direction-wrong, ratio ROSE; crossed the prediction's own 0.93 invalidation line.
- Cause = the exact risk pre-flagged in the prediction's Notes: denominator (unemployed) shrank on LFPR effects, raising the ratio even as openings fell -56K. Calibration note: the failure mechanism was identified at prediction time but the central case was kept anyway.
- V16 (Employment Structural Rot) mechanism intact via other legs (hires 3.5% below pre-COVID, duration 25.7wk, LFPR 61.9%) — this is a threshold MISS, not a thesis break.
- **Process note:** caught by the NEW boot-time PREDICTIONS due/stale scan (CLAUDE.md SPAWN PROTOCOL step 7, added 5/29). Had sat OPEN-but-stale 24 days. First run of the new step found a real one.

**Apr PCE (Personal Income & Outlays, rel May 28, also grabbed 5/29):** Core PCE **3.3% YoY** (+0.2% MoM) = cycle high, accel from Mar 3.2%; headline PCE 3.8% YoY (+0.4% MoM). Savings rate **2.6%** (-100bps from Mar 3.6%); Real DPI -0.5% MoM (5th neg, accelerating); personal income flat 0.0%; Real PCE +0.1%. = buffer-exhaustion deepening + savings-funded-forced-consumption mechanic intensifying. No prediction resolved (CRL-19 was Mar, already MIXED) — STATUS data integration only.

**CRL-03 — REPRICE 90 → 72% (Fannie MF DQ April reversal):**
- Apr 2026 MF serious DQ **0.64%** (rel May 27) = −14bps MoM. Updated trajectory: Feb 0.74% → Mar **0.78%** (2bps from the 0.80% GFC breach — closest approach yet) → Apr 0.64%.
- Series nearly breached in March then pulled back hard. ⚠️ Apr 0.64% is **month 1 of CRL-03's own invalidation window** ("<0.65% for 2 consecutive months") — if May (rel ~Jun 26) also <0.65%, CRL-03 invalidates.
- Threshold-vs-mechanism: MF DQ is lumpy (single large-loan workouts swing it); CRE/MF-stress mechanism intact (CMBS MF DQ ATH 7.15%, $270B+ debt wall) → threshold pushed out + confidence cut, not thesis break. STATUS Fannie row 🔴→🟠.
- **Process note:** surfaced by the new docket past-due flag (boot step 7a) on its QA pass — the docket flagged Fannie as stale, the check revealed the data had moved against the prediction.

**No THESIS.md change.** V12-hardening evidence accumulating across THREE 5/28-29 datapoints (Waller pivot + GDP Q1 stagflation composition + Apr monthly Core PCE 3.3%); formal V12 score-upgrade review + possible v2.5.2 minor still pending Jun 16-17 SEP per OPEN THREAD.

## 2026-05-03 PM7 — Workbook hardening: VX P1 + KB ref integrity + SCHEMA Option A + VX dedup P4

### Structural workbook work — 4 files touched, 1 commit (3b47901f)
**Author:** CARL (Will-driven session, post-PM6 grocery squeeze refresh)
**Trigger:** Will request to audit VX.tsv current status. Audit surfaced 9 distinct issues; Will approved P1 (Status canonicalization + Delegated_To split + tombstone drops), then dangle cleanup, then Option A SCHEMA expansion, then P4 (dup consolidation).

**P1 — VX Status enum canonicalization + Delegated_To split (replicates KB Item #2a precedent):**
- Added `Delegated_To` column to VX.tsv (11→12 cols, matches KB schema enum: STUE/HOMER/GIG/PHAN/POLLY/POP/DOC or empty)
- Migrated 9 `DELEGATED TO HOMER` rows: split Status overload — assigned proper threshold-color (per band-match + WORKBOOK DISCIPLINE rule for ambiguous cases) + Delegated_To=HOMER. Threshold-color assignments: 2.01 GREEN (approaching Yellow), 2.02 GREEN [FLAG range value], 6.04 ORANGE, 6.05 ORANGE, 6.07 ORANGE, 6.08 ORANGE [FLAG categorical], MF-02 ORANGE, NAR-01 RED, HSG-02 RED.
- Normalized 3 RED-BREACHED → RED (1.04 Subprime Auto, SENT-01 UMich, MACRO-08 ISM Prices Paid) — preserved "BREACHED" in Notes.
- Normalized 1 YELLOW-borderline → YELLOW (MACRO-01 GDP 2.0%) with [FLAG] for May 28 second-est revision risk.
- Dropped 3 CONSOLIDATED tombstones (1.06 Student Loan Conditional, 6.01 CC 90+ NY Fed, ABS-15 Subprime Auto) — but FIRST updated 3 KB rows that referenced them (KB-055/060: 6.01→1.01; KB-059: dropped redundant ABS-15) per discipline.
- Result: 120→117 rows, Status enum clean (RED/ORANGE/YELLOW/GREEN/PENDING only).

**Dangle cleanup — KB→VX integrity pass:**
- Post-P1 verification surfaced 5 pre-existing dangling KB→VX refs (PM4/PM5 sessions wrote refs that didn't match canonical IDs). Verified-by-reading-target before each rewrite.
- KB-271 `VX-CARL-RETAIL` → `VX-CARL-6.10` (Retail Control Group, verified match)
- KB-272 `VX-CARL-MORTG-RATE` → `VX-CARL-HSG-01` (30-Yr Mortgage, verified match)
- KB-272 `VX-CARL-MBA-PURCH` → blanked (no MBA VX vector exists; backlog item)
- KB-273 `VX-CARL-CB-EXPECT` → `VX-CARL-SENT-02` (CB Expectations, verified match)
- KB-274 `VX-CARL-FOMC-RATE-PROXY` → blanked (FOMC vector deferred per ROADMAP)
- Result: 0 dangling KB→VX refs.

**Option A — SCHEMA Vectors-col formal expansion:**
- Audit surfaced 52 KB rows with 118 "off-spec" Vectors-col entries — 95 of which (Vector_N + CRL-NN) were semantically valid but unrecognized by SCHEMA enum. Pure mechanical replacement (Option B: Vector_N → VX-CARL-XXX anchors) would have lost thesis-vector + prediction-ref granularity.
- SCHEMA.tsv Vectors col `allowed_values` formally expanded to: `VX-{AGT}-NN, Vector_N, CRL-NN, FLOW-{AGT}-N.NN, {SUBAGT}-PNN, BRT-NN, →AGENT, or empty`. Description expanded to explain each ref type's purpose + KB-NNN restriction (DerivedFrom only).
- Then fixed only the 9 truly-broken refs: KB-031 (`STATE_DIFFUSION.tsv` filename dropped), KB-232/233/234 (5× `VX→AGENT` typos → `→AGENT`), KB-264/268 (KB-CARL-253 moved Vectors→DerivedFrom), KB-271 (`K-SHAPE` redundant tag dropped).
- Result: 521 refs all SCHEMA-recognized, 0 off-spec.

**P4 — VX dup consolidation:**
- Pair 1 (BNPL Late Rate): VX-CARL-1.03 (Mar 27, LendingTree, 0 KB refs, stale orphan) confirmed true dup of VX-CARL-BNPL-01 (Apr 17, Richmond Fed, 8 KB refs hooked in). Dropped 1.03.
- Pair 2 (Medical): Verification revealed VX-CARL-1.08 ($88-140B range incl. phantom debt) and VX-CARL-MED-01 ($88B narrow CFPB-reported point) measure subtly DIFFERENT things — disagreed on Status (YELLOW vs GREEN) because of band-cross from upper of range. Per WORKBOOK DISCIPLINE rule "if you can't write one threshold that meaningfully measures all bundled rows, they don't belong in one vector" — chose Will-approved Option A: rename to expose distinction. MED-01 → "Medical Collections (CFPB narrow)"; 1.08 → "Medical Debt Total (incl. phantom estimate)". Cross-reference Notes added to both.
- Result: 117→116 rows.

**Final integrity (cumulative):**
- VX: 116 rows × 12 cols, 0 col-count anomalies, Status enum {RED 42 / ORANGE 36 / GREEN 15 / YELLOW 14 / PENDING 10}, Delegated_To {empty 107 / HOMER 9}.
- KB: 273 rows unchanged, 0 dangling KB→VX, all 521 Vectors-col refs SCHEMA-recognized.
- SCHEMA: Vectors-col allowed_values formalized to multi-level ref system.

**Files touched:**
- `workbook/VX.tsv` (P1 schema expand + 9 migrations + 3 normalizations + 3 tombstones + 1 P4 drop + 2 P4 renames)
- `workbook/KB.tsv` (3 P1 ref-rewrites + 4 dangle rewrites + 7 Option A truly-broken fixes)
- `workbook/SCHEMA.tsv` (Vectors col allowed_values + description expanded)
- `ROADMAP.md` (+2 backlog adds: MBA Apps VX vector decision; CARL Status enum hardening sibling to Item #5)

**Backlog adds (ROADMAP investigations backlog):**
- MBA Apps VX vector decision — KB-272 covers MBA Composite/Purchase/Refi but no VX vector tracks them. Decision needed: create VX-CARL-MBA-APPS or accept informational-only.
- CARL Status enum hardening — VX schema not formal in SCHEMA.tsv (only KB schema is). Item #5 was demoted because col-bleed was artifactual, but Status enum + threshold-direction would benefit from formal definition. Pairs with Item #3 validator promotion.

**Open finding:**
- STUE/CLAUDE.md still has stale `VX-CARL-1.06: CONSOLIDATED — use SL vectors below` line. Sub-agent doc — flagged for Will rather than edited per Critical Rule #2 (subagents own their files).

---

## 2026-05-03 PM3 — CRL-19 RESOLVED (direction-correct/magnitude-light)

### PREDICTIONS: CRL-19 OPEN → MIXED
**Author:** CARL (STATUS staleness audit Cluster 1 refresh, May 3 PM3)
**Trigger:** BEA Mar PCE released Apr 30 with Q1 GDP advance (earlier than ~May 30 anticipated) — CRL-19 data now available.

**Outcome:** Mar Core PCE YoY 3.2% (KB-CARL-270). Predicted 3.3-3.5%. Direction CORRECT (acceleration from Feb 3.0% confirmed at +20bps), magnitude LIGHT (10bps below floor; predicted +30-50bps acceleration, actual +20bps). Strict-def: MISSED floor. Direction-only Brier good; magnitude Brier poor.

**Pattern:** Same disposition as CRL-01 (gas pump peak Mar 14-21 — direction right, magnitude wrong). Two of CARL's predictions now in MIXED/MISSED with direction-right/magnitude-low. Calibration question: are CARL predictions systematically over-magnitude or are these isolated cases?

**Vector #12 implication:** Bridge HOLDS — 3.2% monthly is consistent with 4.3% Q1 annualized via base-effect math (Jan/Feb low base lifts Mar print modestly). Stagflation Trap thesis itself unchanged. Calibration warning, not thesis warning.

**Files touched:**
- `thesis/PREDICTIONS.tsv` — CRL-19 Status OPEN → MIXED, Date_Resolved 2026-05-03, Outcome populated
- `STATUS.md` — CRL-19 row removed from Open table, added to Resolved table; Core PCE Monthly row updated to Mar 3.2% (was Feb 3.0%)
- `workbook/KB.tsv` — KB-CARL-270 logged BEA Mar release with full mechanism breakdown
- `workbook/VX.tsv` — VX-CARL-MACRO-07 Notes updated with bridge resolution

---

## 2026-05-03 — v2.5.1: MASKING FRAMEWORK NARROWED 6→4 + K-SHAPE/TARIFF SECTION + CRL-22, CRL-23

### THESIS v2.5 → v2.5.1
**Author:** CARL (response to external helper LLM stress test, Will-mediated review session May 3)
**Action:** Refinement. Masking framework breadth claim narrowed from 6 issuers to 4; reclassified UNH/ELV and DHI/PHM mechanisms into a sibling section (K-shape Selection + Tariff Transmission Confirmations); added two new predictions classified honestly as Vector #12 and Vector #10 transmission tests, NOT masking falsifications.

### TRIGGER

External helper LLM stress test of v2.5 cross-industry data masking framework (loaded into CARL `User Input/CARL KB_VECT convo.md`). Helper's pass 1: 3 mechanisms tight (ALLY/COF/RITM), 1 mixed (SYF), 2 loose (UNH/ELV, DHI/PHM); recommend downgrading breadth claim. Helper's pass 2 (after Will pushback "any worth here?"): found concrete content underneath UNH/V28 + DHI/tariff; recommended re-articulation + 2 new CRLs preserving 6-issuer breadth. CARL review of pass 1 vs pass 2 verdict: pass 1 was the more honest read; pass 2 over-corrected on weak pushback and stretched mechanism labels to preserve breadth. Substance check:

- **UNH/ELV "10% cost-trend pricing + V28 RAF unresolved"** — real H2 2026 risk, but NOT masking in the ALLY sense. MA carriers price entire 2026 plan year via CMS bid; defensive 10% pricing isn't a structural mechanism deferring visibility on the current book. V28 RAF is industry-wide regulatory determination, not company-specific masking. RITM uses an accounting rule to defer DQ recognition on its own borrowers — UNH is making a forward revenue assumption.
- **DHI/PHM "$10,900/home tariff hits FY27"** — real, sized, dated. But it's inventory cost-flow timing — materials bought pre-tariff work through COGS first. Mechanical, not management choice. ACL build (COF) IS deferred recognition; tariff cost lag is supply-chain physics.
- **Active-adult vs first-time mix shift** — genuine ALLY-analog (top of K transacting, bottom frozen) but it's K-shape selection, not masking — the helper's own proposed clarifying note correctly distinguishes this.

The helper's CRL-22 and CRL-23 are well-formed predictions (specific thresholds, invalidation criteria, position-action commitments) and worth adding regardless. But classifying them as masking falsifications would conflate three different mechanisms.

### CHANGES

**Change 1 — Cross-Industry Data Masking table narrowed 6→4 issuers.**
- Retained: ALLY, COF, RITM (tight masking — accounting/composition/securitization choices in the issuer's own book defer P&L recognition).
- Retained with caveat: SYF — ACL hedge leg is masking (forward-risk tell despite improving NCO); survivor-pool (Home & Auto -3.7%) explicitly flagged as K-shape selection, not masking. Only the ACL leg has the deferred-visibility property.
- Relocated: UNH/ELV → K-shape Selection + Tariff Transmission section (new, see below). DHI/PHM → same section.
- Meta-pattern definition tightened: "industry-specific *accounting/securitization choice within the issuer's own book*" (was "industry-specific accounting/structural mechanism" — too permissive, allowed pricing assumptions and supply-chain timing in).
- Added explicit note distinguishing masking vs K-shape selection.
- Crying-wolf X-thresholds simplified to 1 tier (credit issuers, 20bps); insurer/builder threshold removed since those mechanisms relocated.
- Boundary case rewritten to align with credit-issuer-only scope.

**Change 2 — New section: K-shape Selection + Tariff Transmission Confirmations.**
- UNH/ELV sub-section: K-shape selection (Vector #8 transmission via membership culling) + insurer pricing/regulatory contingency (Vector #12 transmission via cost-trend pricing + V28 RAF). Explicit "why not masking" reasoning. CRL-22 test.
- DHI/PHM sub-section: tariff transmission timing (Vector #10 + tariff regime durability) + active-adult selection (Vector #8 via demand-side cohort divergence). Explicit "why not masking" reasoning. CRL-23 test.
- "Why this section exists separately" rationale articulating the three-way distinction (masking / K-shape selection / tariff transmission timing) and why conflation breaks falsifiability.

**Change 3 — "What's Confirmed" rows for builder K-shape and insurer transmission re-tagged with "(selection, not masking)" and pointer to CRL-22/CRL-23.**

**Change 4 — Falsification structure unchanged for masking framework.** CRL-20 and CRL-21 still test the 4-issuer scope (ALLY, COF, SYF, RITM). Their thresholds remain valid since the 4-issuer scope was what they were originally designed against — the v2.5 rhetorical breadth ("5+ industries") was already implicitly testing the 4-issuer credit/servicer cluster.

### NEW PREDICTIONS

**CRL-22 — H2 2026 insurer MLR re-acceleration, 60% confidence:** UNH MCR H2 weighted ≥85.4% (+150bps) OR ELV BCR ≥88.3% (+150bps) AND V28 RAF final adverse. Tests Vector #12 + V28 regulatory contingency. NOT a masking framework falsification. Failure → insurer-side conviction -20pp; K-shape transmission story to credit issuers needs re-rating.

**CRL-23 — FY27 builder GM compression, 70% confidence:** DHI Q1 FY27 GM ≤17.5% OR PHM Q1 FY27 GM ≤22.0% AND tariff regime ≥10% effective sustained through Q4 2026. Tests Vector #10 + tariff regime durability. NOT a masking framework falsification. Failure → builder-side conviction -25pp; revisit demand-side weakness framing.

### HONEST CONVICTION COMMENTARY

The v2.5 masking framework promotion (May 1) was probably overconfident in its breadth claim. External review surfaced that "5+ industries, same meta-pattern" was rhetorical breadth not load-bearing evidence — only 4 issuers had genuine deferred-visibility mechanisms. Same calibration discipline applied to v2.5 score recalibration (58/60 → 53/70 = ~60% calibration + ~40% legitimate conviction reduction) now applied to the masking framework breadth: 6 issuers → 4. The narrowing does not weaken the bear thesis — UNH/ELV cohort culling and DHI/PHM tariff timing are still thesis-supportive observations with their own falsification structure (CRL-22/CRL-23). What the narrowing does is preserve falsifiability: CRL-20/CRL-21 now test what they were designed to test (credit/servicer issuer accounting choices), not a heterogeneous mechanism bundle that a CONTAINMENT critic could pick apart.

### FILES AFFECTED

| File | Change |
|------|--------|
| `thesis/THESIS.md` | Masking table narrowed 6→4 with SYF caveat; meta-pattern + boundary case rewritten; K-shape selection vs masking note added; new section "K-shape Selection + Tariff Transmission Confirmations" inserted between masking framework and Path C; "What's Confirmed" insurer/builder rows re-tagged; "What's Forecast" table adds CRL-22, CRL-23. |
| `thesis/PREDICTIONS.tsv` | +CRL-22, +CRL-23 (24 rows total). |
| `thesis/CHANGELOG.md` | This entry. |
| `workbook/KB.tsv` | KB-CARL-265 logging the v2.5.1 refinement. |
| `ROADMAP.md` | v2.5.1 hardening list updated; this item moved to RECENTLY RESOLVED. |

### ACKNOWLEDGMENT OF EXTERNAL REVIEW

Helper LLM's stress test (pass 1) was directionally correct. Helper's pass 2 over-corrected and the resulting draft would have preserved a 6-issuer table whose footnote contradicted its rows. CARL took the substance of helper's CRL-22 and CRL-23 drafts (good predictions) but classified them honestly as Vector #12 and Vector #10 transmission tests rather than masking falsifications. Architecturally aligned with how v2.5 already separates "thesis-internal mechanism puzzles" (CARL) from "counter-narrative observations" (RED) — same discipline applied here at the framework level.

### KB ROW LOGGED

- **KB-CARL-265** — v2.5.1 thesis refinement (masking framework narrowed 6→4 + K-shape/tariff section + CRL-22, CRL-23)

---

## 2026-05-01 — v2.5: PATH C ACTIVE + CROSS-INDUSTRY DATA MASKING + ARCHITECTURAL REALIGNMENT + 58/60 → 53/70 RECALIBRATION

### THESIS v2.4.1 → v2.5
**Author:** CARL (multi-stage drafting May 1 — r1/r2/r3 with two rounds of external review feedback integrated)
**Action:** Major refinement. Three structural changes plus architectural realignment with RED. Convergence rescaled from 58/60 (97%) → 53/70 (76%) — ~60% calibration discipline + ~40% legitimate conviction reduction.

### TRIGGER

Q1 2026 consumer earnings cycle (Apr 17 – May 1) materially complete. Mandatory thesis review per exit rules (Q1 consumer earnings = April 2026). Pattern across SYF/COF/UNH/DHI/PHM/ALLY/Rithm/Case-Shiller integrations: each issuer reports headline-clean while underlying cohort/composition deterioration is structurally embedded but not yet visible in P&L because of an industry-specific accounting/structural mechanism. ALLY composition-masking framework (KB-CARL-225) generalizes.

Plus: Q1 ATTOM REO conversion (+45% YoY) + bank Q1 provision builds (COF $230M, SYF +36bps to 10.42%) + Rithm advance receivable -$224M / -7.3% QoQ + builder K-shape explicit on call (DHI/PHM) = pre-specified Path C activation triggers from CHANGELOG v2.4 satisfied.

### THREE STRUCTURAL CHANGES

**Change 1 — Cross-industry data masking promoted from KB-225 to thesis-level methodology.**
- Generalizes across 5+ industries via different mechanisms but same META-pattern (12-24mo P&L visibility lag)
- Industries + mechanisms: ALLY (composition shift + CLN routing), SYF (survivor-pool), COF (ACL hedge + auto subprime mix), Rithm (FHA mod reclassification), UNH/ELV (membership culling + bronze-plan shift), DHI/PHM (one-time benefits + active-adult mix)
- Methodological commitments: decompose first, headline second; aggregate-only counter-data downgraded; standing cross-agent methodology; trade duration extends to Q1 2027+
- Falsification windows specified: **CRL-21 (Q3 2026 intermediate)** + **CRL-20 (Q1 2027 outer)**
- Crying-wolf X-threshold placeholders: 20bps for credit issuers, 50bps for non-credit (refinement deferred to standalone working doc)

**Change 2 — Path C ACTIVATING-RED → ACTIVE-RED (PROVISIONAL).**
- Pre-specified v2.4 trigger (Q1 bank earnings cluster confirming Path C provision build) satisfied
- Four channels confirmed: REO conversion + bank provision build + servicer stress + builder K-shape
- PROVISIONAL caveat: COF/SYF Q1'24/Q1'25 counterfactual baselines PENDING_VERIFY before promotion to FIRM
- Operational consequence specified: provisional = 50-75% bank-side put allocation; firm = full allocation; downgrade to ACTIVATING-RED if baseline shows normal seasonal

**Change 3 — Convergence matrix rescaled and architecturally aligned (12 → 14 vectors).**
- 5-definition tightened to "fully fired, no further upside in mechanism"
- V8 + V9 merged into single K-Shape Converging vector (eliminated double-count)
- V13 Federal Fiscal Capacity Stress added (score 3, supporting context)
- V14 Upper-Decile Wealth Stress added (score 3, supporting context)
- V15 Refi-Window dropped — counter-signal territory belongs to RED
- V16 Employment Structural Rot added (was load-bearing claim but missing from scored matrix)
- V2 Subprime Auto downgraded 5 → 4 (strict-definition: EART terminal but AMCAR/SDART have cushion)
- Multiple other 5s rescaled to 4s under tightened definition

### ARCHITECTURAL REALIGNMENT (the second-order finding)

External review surfaced that CARL was running its own internal red team in parallel with system-level RED agent. Counter-Evidence section in THESIS, plus `red_team/` folder (COUNTER_LOG, SOFT_LANDING, CONTAINMENT) duplicated work that belongs in RED's domain.

Action:
- `red_team/` folder moved to `handoff_RED/` (May 1, commit 3d0bdf75)
- THESIS Counter-Evidence section stripped, content staged at `handoff_RED/COUNTER_EVIDENCE_FROM_THESIS.md`
- Puzzles section trimmed: counter-narrative observations (prime mortgage stable, auto insurance cooling, savings rate, prime card stable) routed to RED. Thesis-internal mechanism puzzles (claims-duration paradox, HAROT prime, Path C provisional) retained in CARL.
- HY OAS reframed: was counter-evidence, now masking-thesis CONFIRMATION (public spreads lagging tranche-level stress is exactly what masking framework predicts)
- CARL CLAUDE.md FILES table updated: red_team/ row replaced with handoff_RED/ pointer ("Do NOT maintain; awaiting RED pickup")

### CONVERGENCE MATRIX

| # | Vector | v2.4 | v2.5 | Note |
|---|--------|------|------|------|
| 1 | CC 90+ DQ → GFC | 4 | 4 | Holds |
| 2 | Subprime Auto 60+ | 5 | **4** ⬇️ | Strict-def fix |
| 3 | Fannie MF DQ → GFC | 4 | 4 | Holds |
| 4 | Student Loan 90+ | 5 | **4** ⬇️ | Rescaled |
| 5 | Gas Price Squeeze | 5 | **4** ⬇️ | Rescaled |
| 6 | UI Exhaustion Wave | 5 | **4** ⬇️ | Mechanism unverified |
| 7 | FL Triple Squeeze | 4 | 4 | Holds |
| 8 | K-Shape Converging *(merged 8+9)* | 5+5 | **4** ⬇️ | Merge + magnitude caveat |
| 10 | Foreclosure Acceleration | 5 | **4** ⬇️ | Rescaled |
| 11 | SB Bankruptcy + Owner Income | 4 | **3** ⬇️ | Rescaled |
| 12 | Stagflation Trap / Fed Locked | 5 | **4** ⬇️ | Rescaled (TTM not crossed) |
| 13 | Federal Fiscal Capacity Stress | — | **3** | NEW supporting |
| 14 | Upper-Decile Wealth Stress | — | **3** | NEW supporting |
| 16 | Employment Structural Rot | — | **4** | NEW (was missing) |

V9 merged into V8. V15 (Refi-Window) dropped (RED domain). Total: **53/70** (76%).

### NEW PREDICTIONS

**CRL-20 — Q1 2027 outer falsification, 75% confidence:** at least 3 of {ALLY, COF, SYF, RITM} show NCO/DQ acceleration breaking the "headline clean" pattern. Specific: ALLY consumer auto NCO ≥+30bps QoQ for 2 consecutive quarters; COF Card NCO ≥+25bps QoQ for 2 consecutive quarters; SYF NCO breaks above FY26 ceiling 5.5%. Failure → masking thesis invalidated, CONTAINMENT validated.

**CRL-21 — Q3 2026 intermediate falsification, 60% confidence:** by Q3 2026, NCOs at ALLY/COF/SYF have begun visible inflection AND vintage-loss projections for FY2025/FY2026 vintages ≥+50bps above FY2023 vintage at comparable seasoning. Position-action commitment on failure: confidence -25-30pp + trim short positions 25% + extend duration to Q2 2027+.

### NEW SECTIONS

- **Cross-Industry Data Masking Framework** (with industry-mechanism inventory + falsification windows + crying-wolf operational thresholds + boundary case)
- **Path C — Activation Status** (with provisional/firm/downgrade-target operational distinction table)
- **Trade Duration Implications** (KRE/WAL Dec 2026 vs thesis Q1 2027+ gap; Path A roll structure recommendation; flag to FORGE/REGINALD)
- **Puzzles / Anomalies** (3 thesis-internal mechanism puzzles)
- **Fast Early-Warning Kill Mechanism** (1-month conviction-update triggers; HY OAS asymmetry tiered)

### HONEST CONVICTION COMMENTARY

Score 58/60 (97%) → 53/70 (76%) decomposes:
- ~60% calibration: matrix expansion, 5-definition tightened, V8/V9 merge, V2 strict-def
- ~40% legitimate conviction reduction: V6/V8/V12 honestly downgraded based on evidence gaps + multiple PENDING_VERIFY items

Not "calibration honest, not thesis weakening" — that was rhetorical sleight of hand in r1/r2 drafts. Honest framing: prior 58/60 was probably overconfident. V6, V8, V12 were never really at 5 on the evidence base. 53/70 is closer to true conviction we should have had all along. Both better calibration AND recognition of prior overconfidence.

The thesis is still CRITICAL. Every load-bearing vector (1-12 + 16) is at 4. No vector at 3 or below in the bear-thesis core.

### COUNTER-EVIDENCE / RED-AGENT NOTE

Under v2.5, aggregate-only counter-data is explicitly downgraded unless paired with cohort decomposition. Counter-narrative tracking is RED's domain — see `handoff_RED/`. Interface contract pending; ad-hoc until RED-CARL handshake protocol document written.

### REVIEW PROCESS NOTE (multi-stage drafting)

v2.5 was drafted in 3 revisions over ~6 hours with 2 rounds of external LLM review:
- r1 (commit c0e06744): initial draft, 12-vector matrix, 58/60 → 54/60
- r2 (commit 36c1e5f3): 13 reviewer critiques addressed; matrix expanded 14 vectors; rescaled
- r3 (commit 036c7247): architectural realignment after Will surfaced RED agent existence; 12 additional structural fixes; honest conviction reframe

Worth carrying forward as practice — thesis-level changes benefit from external review before promotion to canonical.

### STATUS DASHBOARD CHANGES (pending)

STATUS.md mirror updates: convergence matrix table (12 vectors → 14, scores rescaled, total 58/60 → 53/70), header banner (overall capsule), predictions table (+CRL-20, +CRL-21), counter-evidence section removal pointer.

### KB ROW LOGGED

- **KB-CARL-263** — v2.5 thesis statement (Path C ACTIVE + cross-industry data masking + 53/70 recalibration)

### NEXT REFRESH

- v2.5.1 hardening: PENDING_VERIFY items 1-9 (UMich triangulation, foreclosure 2019 baseline, Path C counterfactual, X-threshold operationalization, Brier audit, CONTAINMENT prior audit, COF/SYF candor puzzle, trade duration roll plan, RED-CARL interface)
- Q3 2026 — CRL-21 intermediate falsification window
- Q1 2027 — CRL-20 outer falsification window

---

## 2026-05-01 — LIVE OIL/PUMP REFRESH + CRL-08 REPRICE 78→92%

### NO THESIS VERSION BUMP
**Author:** CARL (live tactical refresh — Brent/WTI/AAA pump 2 trading days stale per >24hr rule)
**Action:** Brent path Apr 30 intraday $126 NEW HIGH (above Apr 29 $115); May 1 pullback to $107-110 on Iran updated peace proposal + Trump WPR 60-day deadline today. **AAA pump $4.392 May 1 — pump pass-through ACCELERATED beyond model**, gap to CRL-08 $4.50 threshold collapsed to $0.108. **CRL-08 reprice 78→92%**. KB-CARL-258 (Brent path), KB-CARL-259 (pump acceleration). VX-CARL-GAS-01 added.

### KEY DATA POINTS
- **Brent**: Apr 30 close $114.66, intraday peak $126 (NEW HIGH). May 1 8:45am ET $116.10 → intraday $107-108 range. 18d move from $98.18 (Apr 13) = +$10-12 / +10-12%.
- **WTI**: ~$106 May 1 (above $105, second weekly gain). Brent-WTI spread $2-4 = compressed (typical $5-10) reflecting physical-spot tightness.
- **AAA Pump**: $4.392 May 1 (+9.2¢ overnight vs Apr 30 $4.300, +33.3¢ WoW vs Apr 24 $4.059, +37.7% YoY vs $3.187). 5 states >$5.
- **Iran cluster**: WPR 60-day deadline TODAY (admin claims "terminated", Republicans defer, Democrats push back, no statutory pause-on-ceasefire); Iran updated peace proposal in Pakistani mediation; Hormuz blockade BOTH WAYS persists; rial -15% Apr 27-29 record low.
- **Hormuz**: per fxleaders 9.1 mbd shut-ins (~9% global supply), single-source un-verified — IEA OMR / EIA STEO needed.

### MECHANISM FINDING
Pump pass-through ACCELERATED — Brent breakout Apr 28-30 transmitted to retail in 3-4 days vs typical 2-4 week lag. Three explanatory channels:
1. Wholesale pre-positioning ahead of summer driving season (Memorial Day inventory pull-forward)
2. Refinery margin compression on diesel divergence (KB-CARL-253) — refiners running yields toward gasoline because they cannot pass distillate cost upstream
3. Hormuz blockade physical-spot tightness creating immediate spot-to-rack pricing

### PREDICTION CHANGE
**CRL-08** (Gas $4.50+ national avg, May-Jun 2026): **78% → 92%**
- Gap to threshold collapsed from $0.27 (Apr 29) to $0.108 (May 1)
- At overnight pace breaches May 2-3, at weekly pace by May 4-5
- 92% not 95%+ because: Iran peace proposal acceptance scenario (Brent collapse to $80-90, 10-15% probability) + behavioral demand destruction at $4.50+ + Trump WPR resolution pressure
- 92% not 85% because: gap collapsed, Brent $107+ + Hormuz blockade structural, Memorial Day premium incoming, Apr 19 conditional firmly in "breaks" branch

### THESIS / VECTOR IMPACT
**Vector #5 (Gas Price Squeeze):** intensity reinforced (already 5/5)
- Behavioral demand destruction at $4.50+ becomes next testable threshold; CARL prior assumption "$4.30+ behavioral breakpoint" may need revision upward if visible consumption maintains through $4.50 cross

**Vector #12 (Stagflation Trap):** energy-side CPI loading reinforced
- May/Jun gasoline +33% YoY adds ~30bps to headline CPI directly + secondary food/transit pass-through
- Fed pure-locked compounded

### STATUS DASHBOARD CHANGES
- Header timestamp + Overall capsule: refreshed with multi-thread May 1 PM integration
- Gas Pump row: $4.229 → $4.392 with full pace data
- Brent row: $110.38 → $107-110 May 1 range, with Apr 30 $126 intraday note
- WTI row: $106.51 → ~$106 May 1
- Iran Cluster Resolution row: WPR deadline + peace proposal + blockade-stalemate
- Predictions table CRL-08 row: 78 → 92% with full rationale

### KB / VX ROWS LOGGED
- **KB-CARL-258** — Brent path May 1 + Iran cluster + WPR deadline
- **KB-CARL-259** — Pump pass-through acceleration mechanism (3-4d vs 2-4wk)
- **VX-CARL-GAS-01** — AAA National Pump (newly tracked row, RED status, $4.392)

### NEXT REFRESH
- Daily AAA pump (track threshold breach if/when it happens)
- Weekly EIA inventory print (Wed) — distillate/gasoline stocks
- Weekly Brent close — sustainability test
- Mid-month IEA OMR — verify Hormuz shut-in numbers

---

## 2026-05-01 — RITHM/NEWREZ Q1 2026 INTEGRATION (NON-BANK SERVICER FRAMEWORK REINFORCED)

### NO THESIS VERSION BUMP
**Author:** CARL (3-day catch-up of Apr 28 print, was Danger Window PENDING)
**Action:** Rithm Q1 2026 integrated. Prior mgmt forecast "DQ will reverse in Q1" QUIETLY DROPPED — replaced by Newrez President Silverstein with "stable QoQ + FHA flatten via FHA modification guidelines normalization." Bear case INTACT but with explicit 12-24mo modification-accounting-cushion caveat added to thesis. Non-bank servicer stress framework REINFORCED. KB-CARL-257.

### KEY READS

**Headline financials (strong):**
- Revenue $1.38B (beat $1.25B cons)
- EAD $289.6M / $0.51 EPS
- Origination $15.5B (-18% QoQ, +31% YoY)
- BV/share $12.51
- NewRez total servicing UPB $850B (incl $257B 3rd-party)

**Credit (the watch metric — soft retraction):**
- Silverstein: "delinquencies remain stable quarter-over-quarter and the FHA delinquencies flattened as we normalize the impact of the new FHA modification guidelines"
- "Stable" ≠ "Reverse" — original forecast quietly dropped, no specific FHA DQ rate disclosed (opacity tell on the metric mgmt walked back), no Q2 DQ guidance

**Balance-sheet signals:**
- Servicer advances receivable: $2,866M Q1 vs $3,091M Q4 = **-$224M / -7.3% QoQ**
- MSR fair value mark loss: -$204M Q1 vs -$422M Q4 = **losses HALVED QoQ**

### THE ACCOUNTING TELL

"Normalize the impact of the new FHA modification guidelines" = HUD/Ginnie 2025 streamline-modification guidance allows trial-modified borrowers to be reclassified to current within 90-180 days, removing them from DQ rolls without underlying borrower performance improvement. Effects:
- Optical DQ smoothing for 12-24 months as new modification cohorts work through
- Advance receivable reduction without credit improvement (modification reclassifies need away)
- Headline DQ optics LAG underlying stress

### THESIS / VECTOR IMPACT

**Vector #10 (Foreclosure Acceleration):** UNCHANGED at 5/5
- Pipeline conversion thesis intact via Q1 ATTOM REO +45% YoY / FL +108%, NOT Rithm optic
- Bank-side will see underlying stress before optical DQ catches up

**Non-bank servicer stress framework:** REINFORCED
- Rithm "stable via mod-accounting" = directionally WEAKER input than "improving"
- PennyMac FHA DQ 7.5% (+160bps QoQ, KB-CARL-prior) remains cleaner stress proxy
- Bridge test: PennyMac Q1 (late Apr/early May) — does PennyMac FHA DQ continue rising despite same accounting tailwind, or also "stabilize"? Differential = signal on whether mod-accounting is universal cushion or NewRez-specific

**Path C (Housing → Banks):** transmission live; bank-side is the cleaner read

### COUNTER-EVIDENCE (RED-style flag)
- Headline beat was strong (revenue +10% vs cons, EAD beat)
- Market may take RITM print bullishly, pricing headline optics NOT modification-accounting nuance
- Stock-price action could diverge from underlying credit thesis for several quarters before pipeline visibly turns
- This is a counter-evidence input for any "RITM short" trade idea — the optical-cushion timeline is real and front-loads the thesis-vs-tape divergence

### STATUS DASHBOARD CHANGES
- Non-Bank Servicer Stress row: appended Rithm Q1 detail
- Danger Window Apr 28 row: marked Rithm RESOLVED, Case-Shiller still PENDING
- Apr 28 Rithm earnings row: struck-through with RESOLVED note

### KB ROW LOGGED
- **KB-CARL-257** — Rithm Q1 2026 integration with full modification-accounting cushion framework

### NEXT REFRESH
- Late Apr / early May — PennyMac Q1 (bridge test for mod-accounting universality)
- Q3 2026 — Rithm/Newrez Q2 (does "stable" hold?)

---

## 2026-05-01 — APR 30 GDP Q1 ADVANCE INTEGRATION (VECTOR #12 HARDENED)

### NO THESIS VERSION BUMP
**Author:** CARL (Will-directed catch-up of Apr 30 BEA print, was Apr 29 PM2 SCRATCH PRIORITY-1)
**Action:** Apr 30 BEA Q1 2026 GDP advance integrated. Headline 2.0% real (vs 2.3% cons / vs 1.3% GDPNow Apr 7) softens "stall speed" framing 0.7pp. **But realized Q1 NIPA inflation PCE +4.5% / core PCE +4.3% / GDP-domestic-purchases price index +3.6% data-confirms UMich un-anchoring (1Y exp 4.7%, 5-10Y 3.5%) — Vector #12 (Stagflation Trap / Fed Locked) HARDENED via realized inflation, not just expectational.** Q4 2025 revised down 0.7→0.5% on annual revision. STATUS dashboard updated, 3 KB rows added, ROADMAP thread closed.

### KEY READS

**Headline:**
- Real GDP Q1 2026: **+2.0% annualized** (advance estimate)
- vs consensus 2.3% (miss by 0.3pp)
- vs Atlanta Fed GDPNow Q1 final 1.3% (Apr 7 anchor — beat by 0.7pp)
- GDPNow stale anchor; Q2 GDPNow next replacement read

**Inflation (the real signal):**
- PCE price index Q1 NIPA: **+4.5% annualized**
- Core PCE Q1 NIPA: **+4.3% annualized**
- GDP price index gross domestic purchases: **+3.6%**
- Reference: Feb 2026 monthly Core PCE was 3.0% YoY — Q1 NIPA 4.3% reflects Jan/Feb/Mar re-acceleration that monthly YoY had not yet fully priced
- Bridge: March monthly core PCE (release ~May 30) should accelerate from Feb 3.0% YoY toward 3.3-3.5% to be consistent with Q1 NIPA 4.3% annualized

**Q4 2025 revision:**
- 1.4% (1st est) → 0.7% (3rd est) → **0.5% (annual revision Apr 30)**
- Cumulative downward revision -0.9pp from initial print
- Pattern: aggregate data systematically over-states near-term resilience, revises down as more granular source data incorporates

**Composition (K-shape signal):**
- Drivers: equipment (information-processing-heavy = AI capex), intellectual property products, inventory build
- Drags: residential AND non-residential structures (housing transmission live both sides)
- Services PCE driver: **healthcare-led** (forced consumption, non-discretionary cost-push)
- AI capex concentration via equipment + IPP pairs DIRECTLY with META + MSFT capex prints AMC Apr 30 (BOARD SIG-029-004) — feedback loop: if hyperscalers guide capex DOWN, Q1 2.0% headline driver hollows out for Q2

### THESIS / VECTOR IMPACT

**Vector #12 (Stagflation Trap / Fed Locked):** REINFORCED
- Score unchanged (already 5/5 max)
- Qualitative intensity HIGHER — UMich expectations un-anchoring is now data-backed not panic-spike
- Fed reaction function: cut blocked (4.3% core PCE ratifies un-anchoring), hike blocked (2.0% growth + ATL sentiment)
- 1970s analog confirmed: Fed loses inflation credibility → term premia widen → mortgage rates sticky high regardless of Fed front-end direction → housing transmission compounds (Vector #10 reinforcement via term-premium channel)

**Vector #10 (Foreclosure Acceleration):** secondary reinforcement
- Q1 GDP residential structures DRAG = housing transmission empirically live in NIPA, not just micro data
- Term-premium channel from Vector #12 = sustained mortgage-rate stickiness even if Fed cuts

**Two new predictions booked from this print:**
- **CRL-18** (60%, May 28 resolves) — Q1 2026 GDP second estimate revises advance 2.0% down by 0.2-0.4pp into 1.6-1.8% range. Pattern basis: Q4 2025 cumulative -0.9pp revision (1.4 → 0.7 → 0.5).
- **CRL-19** (70%, ~May 30 resolves) — March 2026 monthly Core PCE YoY accelerates from Feb 3.0% to 3.3-3.5% range. Bridge test for Q1 NIPA 4.3% annualized consistency.

CRL-09 (JOLTS Mar) and CRL-12 (SYF FY26 NCO) unrelated to this print.

### STATUS DASHBOARD CHANGES
- Header timestamp: Apr 29 PM2 → May 1 ~14:00 UTC
- "Overall" capsule: prepended May 1 GDP capsule
- GDP Q4 2025 row: 0.7% → 0.5%
- GDPNow Q1 row REPLACED with **Real GDP Q1 2026 (advance) 2.0%** + new **PCE Q1 NIPA 4.5%** + **Core PCE Q1 NIPA 4.3%** + **GDP Price Index Q1 3.6%** rows (+3 net rows)
- Vector #12 row: "REINFORCED May 1" tag added with realized PCE evidence
- Convergence summary line: May 1 reinforcement note added

### KB ROWS LOGGED
- **KB-CARL-254** — GDP Q1 2026 advance 2.0% headline + composition (Vector #10 + #12)
- **KB-CARL-255** — Q1 NIPA inflation PCE 4.5% / core 4.3% (Vector #12 hardening)
- **KB-CARL-256** — Q4 2025 GDP revision 0.7 → 0.5% (revision pattern flag)

### NEXT REFRESH
- May 28 — BEA second estimate for Q1 2026 (revision risk -0.2 to -0.4pp per pattern)
- May 30 — March monthly core PCE (bridge test for Q1 NIPA 4.3% consistency)
- Jun 26 — BEA third estimate Q1 2026

---

## 2026-04-29 (PM2) — AAA LIVE PUMP REFRESH + DIESEL DEMAND DIVERGENCE

### NO THESIS VERSION BUMP
**Author:** CARL (PRIORITY-1 from Apr 29 PM SCRATCH — close stale pump data window)
**Action:** Stale Apr 17 pump data refreshed live. CRL-08 78% reprice confirmed on track inside model. New K-shape finding logged: diesel-vs-gasoline divergence as freight demand destruction signal. STATUS dashboard updated. KB-CARL-252, KB-CARL-253 logged.

### LIVE DATA CONFIRMATION

**Gas Pump (CRL-08 confirmation):**
- AAA national regular: **$4.229 / gal** (Apr 29 live)
- vs prior STATUS print $4.076 (Apr 17): **+$0.153 / 12 days**
- Pace: yesterday $4.176 → +5.3¢ overnight; week-ago $4.020 (+$0.21 / 7d); month-ago $3.980 (+$0.21 / 30d); YoY $3.161 (+$1.07 / +33.8%)
- Brent pass-through completion: ~40% of crude move (+$12 / +12.5%) absorbed in pump (+$0.21 / +5.0%) — textbook 2-4wk lag still in pipeline
- **CRL-08 78% holds** — gap to $4.50 threshold = $0.27, 30d pace = $0.21, on track inside Apr 29 AM reprice model. Live print is confirmatory, not deflective.

**Diesel (NEW K-SHAPE FINDING):**
- AAA national diesel: **$5.464 / gal** (Apr 29 live)
- vs prior STATUS print $5.608 (Apr 13 EIA): **DOWN -$0.144 / -2.6%** despite Brent breaking $98 → $110+ same window
- Week-ago $5.489 (-$0.025 falling); month-ago $5.406 (+$0.058 mildly higher but rolling)
- **The signal: diesel falling while gasoline rises = freight/business-side demand destruction.** Distillate-weighted to trucking, freight rail, ag diesel, marine bunker — leading-edge business-cycle indicators. When refiners cannot pass distillate cost upstream and shift yields toward gasoline, soft distillate demand is the residual explanation.
- **Direct K-shape signal:** consumer-side pump rises (cost squeeze on bottom 60%) + business-side diesel falls (demand pullback on freight/ag) firing simultaneously and in opposite directions. Vector #9 (K-Shape Converging Downward) reinforced via business-side extension.

### CONVERGENCE MATRIX

- **Vector #5 (Gas Price Squeeze): 5/5 unchanged.**
- **Vector #9 (K-Shape Converging Downward): 5/5 unchanged** — but qualitatively reinforced via diesel divergence as new business-side demand-destruction confirmation.
- **Score: 58/60 held.**

### NEXT TRIGGERS

- **Diesel sustained 4+ weeks soft while Brent stays $100+:** would significantly strengthen freight-demand-destruction interpretation. Track ATA truck tonnage, Cass Freight Index, EIA distillate stocks (Wed weekly), refinery utilization.
- **Pump weekly refresh:** continue live AAA tracking; Memorial Day (May 25) seasonal premium expected to add $0.10-0.15.
- **CRL-10 (Food CPI):** ag-diesel softening could partially offset urea/wheat input cost — minor counter-signal, watch for compounding effects.

---

## 2026-04-29 (PM) — CRL-08 REPRICE ON BRENT BREAKOUT + CEASEFIRE-BRANCH RESOLUTION

### NO THESIS VERSION BUMP
**Author:** CARL (Step 4 of Apr 29 catch-up — Brent → CRL-08 reprice)
**Action:** CRL-08 confidence 65% → 78%. Mirror updated in STATUS.md predictions table. KB-CARL-248 logged.

### PREDICTION UPDATE

**CRL-08 — Gas pump prices hit $4.50+ national avg by May-Jun 2026**
- **Confidence: 65% → 78%**
- **Timeframe unchanged: May-Jun 2026**
- **Rationale (binary-branch resolved + Brent breakout):**
  - Apr 19 prior structure was conditional: 80% if Apr 21 ceasefire breaks, 30% if it holds, blended to 65% pre-resolution.
  - Apr 21 ceasefire did NOT resolve cleanly. Apr 24 contradictory diplomacy (Araghchi Islamabad, Trump talks-relaunch frame vs IRGC-Raja denial); WTI dropped to $94.40 on talks-hope then breakout.
  - **Apr 28-29: Brent $110.38 close / $115 intraday — 8-session streak, highest since June 2022, IEA on-record "largest supply shock on record" framing.** Cluster intensified, did not de-escalate.
  - Pass-through math: Brent +$12 from $98 → +$0.25-0.30/gal pump in 2-4wks → from $4.076 baseline → ~$4.30-4.40 in steady state before further oil moves. Closing $0.42 gap requires Brent sustained $110+ AND (refiner margin expansion via distillate tightness OR Memorial Day seasonal +$0.10-0.15 OR another $5-8 leg from kinetic event).
- **Why 78% not 85%+:**
  - $0.42 gap still meaningful — needs more than just current Brent staying flat
  - MS/Piper Sandler counter-frame (KB-CARL-236) valid: US net-exporter + 1.8% aggregate gas share caps structural multiplier
  - Demand destruction at $4.30+ retail moderates further moves
  - Brent $115 was intraday spike; close $110.38; 8-week sustainability not yet proven
  - Trump talks-relaunch optics could re-emerge (Witkoff/Kushner reportedly to Pakistan)
- **Why 78% not 65%:**
  - Binary conditional has effectively fired toward "breaks" branch
  - Cluster intensifying not resolving (Iranian rial -15% in 2 days, USS Pinckney shadow-fleet intercept Apr 26, Merz "no exit strategy" Apr 28)
  - IEA "largest supply shock on record" framing is uncharacteristic escalation language for that body
- **Invalidation unchanged.**

### CONVERGENCE MATRIX

- **Vector #5 (Gas Price Squeeze): 5/5 unchanged.** Already maxed; reprice reflects probability not vector score.
- **Score: 58/60 held.** No vector flips.

### NEXT TRIGGERS

- **Pump pass-through validation:** AAA daily refresh needed — pump $4.076 (Apr 17 stale) likely already $4.20-4.30 area on Brent $110.
- **Brent sustainability test:** does $110+ hold through next week, or pull back on talks-hope re-emerging?
- **May UMich + CPI:** validates inflation expectations un-anchoring vs noise; pairs with CRL-08 transmission read.
- **Memorial Day weekend (May 25):** organic seasonal premium kicks in — natural test of pump trajectory.

---

## 2026-04-29 — APR 21 EARNINGS CATCH-UP SYNTHESIS (10-day-late processing)

### NO THESIS VERSION BUMP
**Author:** CARL (catch-up after 10-day session gap; sub-agents POLLY + HOMER + SYF/COF research fork)
**Action:** Three earnings clusters processed retroactively. CRL-12 confidence revised DOWN 77→55%. STATUS dashboard +6 new rows (SYF/COF Q1, DHI Q2, PHM Q1, UNH Q1, ELV Q1). Convergence unchanged at 58/60.

### PREDICTION UPDATES

**CRL-12 — SYF FY2026 NCO exceeds 6.0% guidance ceiling**
- **Confidence: 77% → 55%**
- **Rationale:** SYF Q1 NCO 5.42% (-96bps YoY); SYF revised FY2026 guidance DOWN to <5.5% (well below 6.0% threshold CRL-12 requires). Headline path requires fresh credit loosening or material macro deterioration to overshoot. Survivor-pool caveat retained (Home & Auto receivables -3.7% YoY, active accounts -0.7%, ACL ratio BUILT +36bps to 10.42% despite clean headline = mgmt hedging forward risk). CFPB late-fee reinstatement remains tail risk that could push NCO back up. K-shape composition-masking (KB-CARL-243/244) confirmed on the ALLY framework.
- **Why not lower than 55%:** macro deterioration acceleration (gas $4.50+, food CPI Q3) could still pressure NCO into Q3-Q4 even on the cleaner book; ACL build signal preserves ~one-quarter pull-forward risk. 50% would imply CRL-12 has lost most of its load-bearing weight; 55% reflects still-meaningful but reduced probability.
- **Invalidation unchanged.**

### EVIDENCE UPDATES (no prediction-level changes)

**SYF/COF Q1 2026 (Apr 21):**
- SYF as above. COF Domestic Card NCO 5.1% (-109bps YoY) clean headline; **Auto book is the ALLY analog** — originations +21% YoY w/ "slightly higher subprime mix" admitted by management; $155M Consumer Banking ACL build + $230M total ACL build citing "potential downside scenarios." Discover acquisition: legacy book contracting -1.2% via prior tightening; replacement originations 8% on COF platform now → ~100% by Q3 2026 (forward NCO will reflect COF near-prime standards).
- KB-CARL-243 (SYF actuals), 244 (SYF ALLY scorecard), 245 (COF actuals), 246 (COF ALLY scorecard).

**DHI Q2 FY2026 (Apr 21) + PHM Q1 2026 (Apr 23):**
- DHI GM 20.1% reported / 19.7% normalized — beat 19.0-19.5% guide on litigation/warranty benefit + cost control, NOT price recovery. ASP -3% YoY $361,600. Cancellations 16% — "vast majority mortgage qualification failure." First-time 65% of closings. FY26 closings TRIMMED -500.
- PHM GM 24.4% MISS (-310bps from 27.5% Q1'25). Incentives +290bps to 10.9%. Q2 GM guided 24.1-24.4% = sequential compression. **PHM management names "K-shape" explicitly on call** — active adult orders +14% YoY, first-time flat.
- **CRITICAL:** $10,900/home tariff cost NOT in 2026 margins; FY27 hit. Current builder margins are the **pre-tariff floor**.
- Vector #10 (Foreclosure Acceleration) reinforced via new-home channel — cancellations are mortgage-qualification failures (consumer stress, not preference shift).

**UNH Q1 (Apr 21) + ELV Q1 (Apr 22):**
- UNH MCR 83.9% (vs 84.8% Q1'25; est ~85.5%) — NO MLR breach. MA membership -965K Q1 (FY guide ~-1.3M loss). FY adj EPS guide raised to >$18.25. DOJ investigation ongoing.
- ELV BCR 86.8% (+40bps YoY) — NO breach. Adj EPS $12.58 BEAT (vs $11.03 est). FY guide raised to >$26.75. $935M one-time CMS accrual (RA dispute, compliance Jul 31).
- **MA cost trend ~10% embedded in 2026 pricing** at both carriers (vs historical 3-5%) — re-acceleration thesis PARTIALLY CONFIRMED. V28 RAF recalibration unresolved → H2 2026 MLR re-acceleration risk.
- Mechanism note: insurer beats driven by membership culling + repricing → bronze-plan ACA shift = high-deductible trap activating = consumer-side stagflation transmission, **Vector #12 intact** (insurance is transmission channel, not clearing mechanism).

### CROSS-DOMAIN SYNTHESIS (KB-CARL-247)

K-shape WIDENING confirmed simultaneously across three independent earnings prints:
- **SYF**: bottom-of-K borrowers EXITING the book (survivor-pool); not recovery
- **PHM**: management explicitly labels "K-shaped economy" on call; active adult +14% YoY while first-time flat = top-of-K still buying, bottom frozen
- **POLLY (UNH/ELV)**: bronze-plan ACA shift = high-deductible trap activating in real time; MA cost trend re-acceleration ~10% (vs 3-5%)

Convergence Vector #9 (K-Shape Converging) remains 5/5. The earnings cluster did NOT contradict this; it provided three independent confirmations from credit-card, builder, and insurer angles. Aggregate "improvement" data continues to mask cohort-level deterioration.

### CONVERGENCE MATRIX

- **Vector #10 (Foreclosure Accel)**: 5/5 unchanged. New-home cancellations (DHI 16%, PHM 13%) "mortgage qualification failure" framing reinforces pipeline conversion thesis.
- **Vector #12 (Stagflation Trap)**: 5/5 unchanged. POLLY high-deductible trap + UMich Final 5-10Y inflation expectations 3.5% (un-anchoring deepened) = consumer-side stagflation confirmation.
- **Score: 58/60. Held.**

### NEXT TRIGGERS

- **CRL-08 reprice (gas $4.50+):** pending Brent breakout integration (Step 4 of this session).
- **CRL-05 (CC 90+ DQ >13.74% GFC):** SYF survivor-pool dynamic raises a structural question — if the worst SYF borrowers are exiting (book/charged off), where does the 12.7%→13.74% delta come from? Possible answer: prime/near-prime migration. CRL-05 mechanism shifts from subprime-deeper to prime-down. Confidence not changed pending Q1 NY Fed HHDC data (mid-May).
- **CRL-15/16/17:** SB and POP-driven predictions unchanged; no new earnings input.

---

## 2026-04-19 (PM) — BOARD SIGNAL INTEGRATION (Apr 17–19 WALTER dispatches)

### NO THESIS VERSION BUMP
**Author:** CARL (BOARD/INDEX.md integration pass — 15 CARL-relevant signals out of 30)
**Action:** Evidence update only. Convergence unchanged at 58/60. No vector score change. Two new rows in STATUS Macro/Energy (Qatar LNG, Iran Day-Cluster). One counter-frame logged to RED team. One prediction confidence adjusted.

### TRIGGER

Will directed CARL to use `BOARD/INDEX.md` as a pull-source while the file-based messaging overhaul is pending. 30 dispatches since Apr 17 PM#3 closeout. Highest-load signals: SIG-021 (MS oil-shock 1990-vs-2026 counter-framework), SIG-030 (Qatar LNG verified ~20% global offline since Mar 2), SIG-024/028/029 (Iran 8-channel escalation day-cluster Apr 18–19 + Netherlands LCP-O Apr 20).

### PREDICTION UPDATES

**CRL-08 — Gas pump prices hit $4.50+ national avg**
- **Confidence: 60% → 65%**
- **Timeframe: "extended from Apr 5" → "May-Jun 2026 (extended from Apr 5)"**
- **Rationale:** Apr 8 ceasefire had dropped confidence 80→60% (oil crashed 15% to $98). Three new loadings reverse some of that cut: (a) Qatar LNG verified ~20% global supply offline since Mar 2 via Iranian drone strikes on Ras Laffan + Mesaieed + QatarEnergy force majeure (KB-CARL-234); (b) Apr 18–19 8-channel Iran escalation day-cluster (KB-CARL-235); (c) Netherlands LCP-O activates Mon Apr 20. Apr 21 ceasefire expiry is a BINARY event — conditional probabilities: 80% on May-Jun $4.50 if ceasefire breaks, 30% if it holds. Bump held at 65% (not 70%) to honor the MS/Piper Sandler counter-frame's legitimate US net-exporter asymmetry (see RED team entry below).
- **Invalidation unchanged.**

### RED TEAM — MS/PIPER SANDLER OIL-SHOCK COUNTER-FRAME LOGGED

SIG-021 (MS 6-row 1990-vs-2026 comparison + Piper Sandler "gas matters less" note, 1.8% aggregate consumer spending share, US net-exporter since 2020, "real economy strong," "financial conditions liquid"). Logged to `red_team/COUNTER_LOG.md` with three-point rebuttal:

1. **Aggregate-masking (core CARL K-shape rebuttal):** 1.8% is population-weighted; bottom 60% gas share is ~4-5% of disposable income at $4.08. The K-shape IS the thesis — aggregate comfort is NOT the transmission channel.
2. **"Real economy strong":** Headline, not cohort. JOLTS 0.91 (inverted), LFPR 61.9%, UMich 47.6, FICO Spring 2026 -62pt avg, 9.2M student loan default cohort — all fire independently of any gas move.
3. **"Financial conditions liquid":** Masks structured-credit cracking — EART Class E CE breached (Apr 16), CMBS MF DQ 7.15% ATH (Trepp Mar), AFRMT BNPL composition degrading.

**Outcome:** Counter-frame does NOT change convergence score or CRL-05/CRL-08 confidence (beyond the explicit cap on the CRL-08 bump). Logged as legitimate dampener on magnitude, not invalidator of mechanism. Cached for recall next time MS/Piper material appears.

### KB ENTRIES ADDED (6)

- KB-CARL-234: Qatar LNG ~20% global offline since Mar 2 (A2 EMPIRICAL, 0.97 confidence via WALTER verify-research)
- KB-CARL-235: Iran 8-channel escalation day-cluster Apr 18–19 (A2 EMPIRICAL)
- KB-CARL-236: MS/Piper Sandler oil-shock counter-frame (B2 ASSUMPTION)
- KB-CARL-237: Institutional positioning extreme — not retail (B2 EMPIRICAL)
- KB-CARL-238: China Shock 2.0 info-only, attenuated US channel (A2 EMPIRICAL, stays ZHAO-owned)
- KB-CARL-239: KRE vs XLF counter-framing info-only (C3 EMPIRICAL, stays REGINALD-owned)

KB row count: 233 → 239.

### STATUS.md CHANGES

- Header block: Apr 19 BOARD integration note + ceasefire binary framing
- Macro/Energy section: +Qatar LNG row (🔴, verified since Mar 2), +Iran Day-Cluster row (🔴, 8 channels Apr 18–19)
- Cross-agent WAR row: updated with Netherlands LCP-O Apr 20 and ceasefire Apr 21 binary

### AWARENESS GAP CLOSED

Qatar LNG disruption in force since Mar 2 2026 was not previously in CARL STATUS or KB despite being a material multi-vector cost-squeeze loader (gas/LNG/industrial input). Gap identified via SIG-030 verify-research; filed KB-CARL-234 + STATUS row.

---

## 2026-04-17 (PM) — v2.4.1: PAYMENT HIERARCHY TIMELINE PUSHED (ALLY Q1 COUNTER-EVIDENCE + AUDIT)

### THESIS v2.4 → v2.4.1
**Author:** CARL (post-ALLY Q1 earnings + CARL-performed FY2024/FY2025 10-K reclassification audit)
**Action:** Minor refinement. Convergence unchanged at 58/60. No vector score change. Mechanism-level revision to payment hierarchy pathway timing.

### TRIGGER

Ally Financial Q1 2026 earnings (Apr 17): retail auto NCO 1.97% (-17bps QoQ), 30+ DQ 4.6%, 5th/4th consecutive quarter of YoY improvement respectively. Guidance maintained. Mgmt: "consumer behavior is resilient." Stock up. First real-time test of payment hierarchy cascade claim (prime/near-prime auto = next domino after subprime 60+ DQ breached 6.9% ATR) — headline test result: **CLEAN**, four consecutive quarters improving.

### AUDIT PERFORMED

Pulled ALLY FY2024 10-K (EDGAR acc 0000040729-25-000006, filed 2025-02-19) and FY2025 10-K (acc 0000040729-26-000005, filed 2026-02-25). Ran forensic comparison against REGINALD's regional bank reclassification framework (Layers 1-3: Memo Item 3, NDFI-in-C&I, sub-category reclassification) adapted to auto-lender toolkit (A-G: HFI→HFS, whole-loan sales, FDM/TDR, runoff segmentation, mix shift, reserve release, CLN/securitization routing). File: `domain/sources/ally/RECLASSIFICATION_AUDIT_FY2025.md`.

**Findings — NOT present:** HFI→HFS dumping, TDR re-aging, runoff/legacy segmentation, new line-item taxonomy, NDFI-analog hiding place, dealer/floorplan stress (floorplan shrinking).

**Findings — PRESENT (composition masking, not accounting fraud):**
- Used retail S-tier origination mix: **40% → 37%** (-3pp FY2024 → FY2025)
- Nonprime exposure (FICO<620): **9.7% → 10.1%** (+40bps, +$0.4B to $8.6B)
- ACL: **$3.7B → $3.5B** (-$224M / -6%) = reserve release into mix downgrade (Layer F)
- CLN issuance: **$0.77B → $1.1B** (+43% YoY), reference pools $7B → $10B (Layer G)
- Originations +11% YoY into worsening mix

### MECHANISM REVISION

**Old view (pre-Apr 17 2026):** Payment hierarchy — subprime → near-prime → prime auto — transmission in 1-2 quarters. ALLY Q1 was the first real test; expected to show early signs of near-prime migration (NCO ticking up, DQ stopping improvement).

**New view (v2.4.1):** Headline Ally Q1 is composition-driven, not genuine improvement:
- **Seasoning:** FY2024 higher-FICO originations rolling into 2026 NCO window (lower losses)
- **Mix routing:** Shift from used retail toward new retail (slower loss curve at same FICO)
- **Tail-risk routing:** CLN/securitization expanded +43% YoY, exporting first-loss tail to ABS investors

The FY2025 origination cohort is **like-for-like worse** than FY2024 — deterioration is embedded in the book, not yet in the P&L. The 18-24 month vintage seasoning lag means FY2025 loss window opens **2H 2026 and Q1 2027**.

**Payment hierarchy thesis NOT invalidated — TIMELINE PUSHED.** Near-prime P&L stress window moves from Q1-Q2 2026 to 2H 2026 / Q1 2027.

### CROSS-THESIS IMPLICATIONS

**K-shape within auto credit (new refinement):** Subprime ABS cracking (EART Class E CE breached Apr 16, AMCAR ~2mo, SDART ~7mo) co-exists with near-prime headline-clean = intra-credit K-shape. ABS monoline stress is localized; doesn't migrate up-quality automatically — it migrates via seasoning of the near-prime vintage being originated *now* under looser standards, which plays out with a ~18 month lag.

**Counter-signal containment:** The "Ally Stable 🟢" row in STATUS (Feb 10-D data) is CONFIRMED and EXTENDED, not overturned. But "stable" at headline ≠ "clean" at cohort. STATUS must distinguish the two.

**REGINALD handoff:** Auto-lender reclassification framework (KB-CARL-225) translates their 3-layer bank framework. CLN routing = structural analog of their C&I hiding place. Sent as outbox signal.

### PREDICTION UPDATES

**CRL-05 — CC 90+ DQ breaches 13.74% (GFC peak)**
- **Confidence: 85% → 82%** (mild reduction on headline/cohort distinction)
- **Rationale:** Student loan cascade still adding +0.5-1.0pp pathway, multi-vector cost squeeze intact — these don't require near-prime auto migration to work. But ALLY counter-evidence weakens the "consumer credit generally migrating up-quality" framing at the headline level. Cohort-level deterioration (nonprime share growing) preserves the thesis, just shifts the visibility window later.
- **No change to invalidation criteria.**

**CRL-02 — Subprime Auto 60+ DQ crosses 7.0%** (already CONFIRMED*)
- **Confidence: no change.** Subprime stress is independently confirmed; Ally near-prime data irrelevant to this cohort.

### NEW FRAMEWORK ENTRY

**Auto-lender reclassification methodology** (KB-CARL-225): 7-lever translation of REGINALD regional bank framework. Apply to SYF (Apr 21), COF (Apr 21), AXP (Apr 23). For SYF: no used-car tail, but CLN/mix shift via CareCredit vs Private Label segmentation potentially applicable.

### DANGER WINDOW UPDATE

Added: **Q1 2027** — FY2025 origination cohort full seasoning window. Near-prime auto P&L stress realization if thesis holds. If NCO/DQ deteriorate on unchanged macro at this point, thesis REACTIVATES HARD at the headline level.

---

## 2026-04-17 — v2.4: FORECLOSURE PIPELINE CONVERTING + CREDIT CASCADE EXECUTING

### THESIS v2.3 → v2.4
**Author:** CARL (via Apr 15 data processing — STUE + HOMER sub-agents)
**Action:** Minor refinement. Vector #10 (Foreclosure) upgraded 4→5. Convergence 57/60 → **58/60 CRITICAL**. Two mechanism confirmations added.

### CONVERGENCE MATRIX — Vector #10 Upgrade
| Vector | Change | Reason |
|--------|--------|--------|
| #10 Foreclosure Acceleration | 🔴 4 → 🔴🔴 **5/5** | ATTOM Q1 2026 (rel Apr 16): **Q1 REO completions 14,020 (+45% YoY)**. Previously the 878K 90+/FC pipeline was ACCUMULATING (inflow > outflow). Q1 2026 is first quarter at-scale CONVERSION — cure collapse (-40%) now translating to actual completions. Regime change, not incremental. FL Q1 REO +108% YoY (greatest nationally). Q1 filings 118,727 (+26% YoY). March monthly 45,921 filings (+18% MoM). |

### PREDICTION UPDATES

**CRL-04 — Student Loan 90+ DQ breaches 10%**
- **Confidence: 97% → 98%** (OPEN-NEAR CONFIRMED)
- **Evidence:** FICO Spring 2026 (data Apr 17): SL DQ rate now ~9.8% (up 25% from 7.9% Apr 2025). 6.1M borrowers with SL DQ reported Feb-Apr, avg score drop -69pts (25% saw -100pt+).
- **Counter-signal (minor):** Sweet v. McMahon Apr 15 ruling triggers ~271K tradeline deletions — credit RECOVERY for bounded cohort (~3% of defaulted borrowers). Directionally opposite but magnitude insufficient to move aggregate.
- **Near-term test:** NY Fed Q1 2026 QHDC (~May-Jun).

**CRL-06 — Foreclosures exceed 70K/quarter**
- **Confidence: 70% → 78%**
- **Evidence:** Q1 2026 ATTOM: 82,631 FC starts (already >70K on starts basis), 118,727 filings (+26% YoY), 14,020 REO (+45% YoY). Depending on threshold interpretation, may be CONFIRMED at starts level. Q2 projection likely higher on FL judicial lag.

### NEW MECHANISM / FLOW ENTRY

**FLOW-CARL-12.04 — Foreclosure Pipeline → REO Conversion → Bank Loss Realization (Path C Activation)**
- **Status:** ACTIVATING-RED (new)
- **Pathway:** Borrower 90+ DQ → cure rate collapse → foreclosure filing → legal process 3-12mo → REO completion → actual loss realized → NCO line → earnings hit → bank tightens → consumer denied. Non-bank servicer variant: Ginnie advance drain → warehouse line stress → potential failure (MFS UK template).
- **Why it matters:** Path C (Housing → Banks) previously theoretical, now mechanically active. Q1 bank earnings cluster (Apr 17-28: CFG/PNC/RF/FITB/MTB) = first visibility window for provision build on mortgage/CRE.

### STUDENT LOAN VECTOR CONFIRMATIONS

- **Sweet v. McMahon Apr 15 deadline MISSED** — DOE did not comply. Auto Full Relief triggered for ~170K non-Exhibit C borrowers. Combined with Exhibit C (missed Jan 28 ~170K), total ~271K. Self-executing, no stay. NOT thesis invalidation (court-compelled, bounded cohort).
- **SAVE judicially dead** — 8th Cir Mar 10 reversed + entered final judgment. Dual-elimination (legislative WFTCA Jul 2025 + judicial Mar 2026). Jul 1 transition locked.
- **AFT v. MOHELA in discovery** — Next status conf May 28. Three concurrent class actions active.

### NEW VECTORS (VX)

- **VX-CARL-HSG-05** — Foreclosure Pipeline Quarterly REO Completions (14,020 Q1 2026, RED)
- **VX-CARL-BLDR-01** upgraded to RED (HMI 38 → 34, breaches <40 threshold; new tariff cost shock +$10,900/home)
- **VX-CARL-HSG-01** updated (PMMS 6.37% → 6.30%)
- **VX-CARL-SL-02** updated (SL 90+ DQ ~9.8% per FICO Spring 2026)
- **VX-CARL-6.06** updated (FL Q1 REO +108% YoY, judicial state completion wave)

### KB ENTRIES ADDED

KB-CARL-215 through KB-CARL-221 (7 entries): Sweet v. McMahon ×2, DOE motion context, SAVE judicial death, FICO Spring 2026 cascade, MOHELA discovery, NAHB HMI April, ATTOM Q1 Foreclosures.

### HONEST ASSESSMENT

**Strengthened:** Mechanism confirmations — pipeline conversion (HSG), credit cascade execution (SL), Vector 10 upgrade defensible (not self-inflicted).
**Unchanged:** Market-transmission leg (HY OAS 294bps tight, SPX not in crisis, JPM Q1 benign). Complacency gap persists or widens.
**Counter-signal:** Sweet ruling produces credit RECOVERY for ~271K — directionally opposite the cascade. Small but directionally notable.

### TRIGGER FOR NEXT VERSION BUMP

- Q1 bank earnings cluster (Apr 17-28) confirming Path C provision build → v2.5 with full Path C activation upgrade.
- OR SYF Q1 Apr 21 breaching >6% NCO → credit cascade confirmed at issuer level.
- Reversal criterion: bank earnings downplay stress AND SYF NCO <5.0% → thesis mechanism questioned.

---

## 2026-04-14 — v2.3: FED LOCK MECHANISM + SUBPRIME AUTO CURE COLLAPSE CONFIRMED

### THESIS v2.2 → v2.3
**Author:** CARL (via WALTER inbox processing + ABS drill-down)
**Action:** Major thesis refinement. Vector #12 Stagflation Trap added. Convergence 51/55 → **57/60 CRITICAL**.

### CONVERGENCE MATRIX — Vector #12 Added
| Vector | Change | Reason |
|--------|--------|--------|
| #12 Stagflation Trap / Fed Locked | **NEW** 🔴🔴 5/5 | WALTER CPI/UMich signal integrated (Apr 10 data): UMich Apr preliminary 47.6 — RECORD LOW (biggest MoM drop in series). 1Y inflation exp 4.8% (+100bps), 5-10Y exp UN-ANCHORING at 3.4% (Fed red line breached). CPI Mar +3.28% YoY headline, +2.61% core. Mechanism: Fed cuts now validate un-anchoring → inflation-negative, not stimulus. Cannot cut (expectations), cannot hike (sentiment ATL). 1970s Volcker analog. RED Stagflation Spiral upgraded. HENRY "Fed cuts pushed H2 2027" reinforced. |

### KEY EMPIRICAL CONFIRMATIONS (Apr 14)
- **Subprime auto cure collapse confirmed industry-wide.** SDART 2024-1 (30+ DQ -43bps, CNL +26bps), EART 2024-2 (-177bps/+52bps deep subprime), AMCAR 2024-1 (-175bps/+24bps). HAROT 2024-2 prime control stable. Pattern: DQ bucket draining to charge-offs, not cures. EART already at projected terminal CNL (13.06%). KB-CARL-207, KB-CARL-210.
- **Discover ABS structure dissolved.** DCMT filed Form 15-12G Dec 19 2025 post-CapOne merger. DCENT in defeasance. Removed from abs_monitor. CC data now rolls into COMET. KB-CARL-208, KB-CARL-209.

### PREDICTIONS
No new predictions added — existing CRL-01 through CRL-17 remain appropriate. Notes updated on CRL-05 (cascade confirmation), CRL-08 (FL crossed $4). Future drill-down (#2 CNL trigger proximity) may generate CRL-18.

### KB Added (Apr 14: 7 entries)
KB-CARL-204 (UMich record low), KB-CARL-205 (CPI Mar), KB-CARL-206 (inflation expectations un-anchoring), KB-CARL-207 (SDART Feb loss acceleration), KB-CARL-208 (Discover deregistration), KB-CARL-209 (COMET baseline), KB-CARL-210 (cross-trust cure collapse confirmation).

### Cross-Agent Signals
- Previously sent: CARL → REGINALD (non-bank servicer warehouse exposure, Apr 13 — delivered Apr 14)
- Convergence bump to 57/60 should be propagated to PROME next spawn

---

## 2026-04-13 — HY OAS COMPRESSION + NON-BANK SERVICER RESEARCH + KB ARCHITECTURE

### THESIS v2.2 (refinement, not version bump)
**Author:** CARL (script-driven data refresh + research drill-downs)
**Action:** Major data refresh + structural finding on non-bank mortgage servicer transmission pathway.

### KEY FINDINGS
- **HY OAS complacency gap widening.** Spreads collapsed 346→294bps in 10 days (ceasefire Apr 8 = -18bps single session, plus NFP headline beat). Now BELOW 300bps elevated threshold while student loan defaults hit 9.2M, CMBS MF DQ reached ATH 7.15%, existing home sales approached <4.0M RED. Market split: JPM AM/Marks bullish ("tight justified"), Goldman 45% recession/Cambridge/Wellington/UBS warning on complacency. CARL interpretation: structural demand (CLO/pension/ETF flows) + index survivorship bias masking fundamental deterioration. Late-2007 analog (HY 260bps June → 800+ Nov). KB-CARL-200.
- **Non-bank mortgage servicer stress accelerating.** PennyMac FHA DQ spiked 5.9→7.5% single quarter Q4 2025, advance expenses +14%. GAO-26-107436 (Feb 2026): 35% of 550+ non-banks have high debt, only 30% profitable in 2022-23 downturn. **Ginnie Mae has NO stagflation stress test** — our thesis environment is the untested scenario. loanDepot $107.5M net loss, pledging GNMA MSR income. Lakeview (18% DQ)/Freedom (15.5%) private black boxes. MFS UK collapse (Feb 2026, Barclays $669M loss) = warehouse contagion template. Ginnie advance obligation asymmetry (advance until FINAL resolution) converts FHA DQ pipeline to cumulative cash drain. KB-CARL-202, KB-CARL-203, KB-HMR-046 through 052.

### Infrastructure Built
- 7-script CARL monitoring suite operational (thresholds, gas_tracker, consumer_pulse, catalyst_countdown, housing_pulse, abs_monitor, boot)
- abs_monitor expanded 4→6 issuers (added Exeter, Ally, GMF/AmeriCredit). 17 trusts tracked. SoFi excluded (private/144A).
- KB Migration Chunk 1 DONE: 44 housing entries delegated CARL → HOMER. HOMER KB 35→52 entries. Cross-domain claims retained in CARL.

### Cross-Agent Signal
- **CARL → REGINALD outbox:** Non-bank servicer warehouse line exposure. Request: check WAL/FHN/TCBI warehouse exposures, JPM Q1 warehouse commentary. Delivered Apr 14.

### KB Added (Apr 13: 5 entries)
KB-CARL-200 (HY OAS compression), KB-CARL-201 (CPI Energy +12.5%), KB-CARL-202 (non-bank transmission), KB-CARL-203 (Ginnie Mae no stagflation test), plus 7 HOMER entries on non-bank servicer research.

---

## 2026-04-09 — POP DEEP DIVE: INVISIBLE INCOME + BANK PIPELINE + NEW CONVERGENCE VECTOR

### CONVERGENCE MATRIX Updated
**Author:** CARL (via POP deep dive synthesis)
**Action:** New vector #11 added. Matrix expanded from 10 vectors (50pt) to 11 vectors (55pt). Score 47/50 → 51/55.

| Vector | Change | Reason |
|--------|--------|--------|
| #11 SB Bankruptcy + Owner Income | **NEW** 🔴 4/5 | POP deep dive confirmed: (1) Subchapter V +67% YoY BREACHED, Ch.11 +37%. (2) Owner income destruction refined to $73-145B annually ($83-165B tariff-adjusted) across two channels: active salary cuts (BofA 32%) + chronic income suppression. (3) SBA 7(a) defaults 3.7% (12-yr high). (4) 59% personal guarantees → business failure converts to consumer credit event. This is an explicit vector that was previously implicit in employment rot. Now measurable with leading indicators. |

### PREDICTIONS Added
| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-15 | **NEW** 65% | SBA 7(a) defaults exceed 6.5% by EOY 2026. Currently 3.7%, consensus 6.5-7.5%. Tariff acceleration + EIDL burden + elevated rates. |
| CRL-16 | **NEW** 60% | Regional bank Q2 2026 earnings show SB provision increases >25% YoY. Default lag model: tariff stress → charge-off = 9-12mo. Q2 = first window. |
| CRL-17 | **NEW** 55% | SB owner income destruction exceeds $100B annualized by Q3 2026 (tariff-adjusted). Wide confidence range — no survey measures cut magnitude. |

### KB Added (8 entries: KB-CARL-166 through KB-CARL-173)
Key entries: Owner income destruction refined estimate (166), CFPB primary earner data (167), S-corp distribution gap (168), SBA defaults (169), tariff importer burden (170), SubV +67% (171), regionals $600B SB loans (172), OZK NCO 1.18% (173).

### VX Added (2 vectors at CARL level)
- VX-CARL-POP-01: SB Owner Income Destruction — RED ($73-145B annually, invisible to BLS/payroll)
- VX-CARL-POP-02: SB Bankruptcy Pipeline — RED (SubV +67% BREACHED, SBA defaults 12-yr high)

### FLOW Added (2 cascades at CARL level)
- FLOW-CARL-11.01: Tariff → SB margin → owner comp → consumer spending (ACTIVE-RED)
- FLOW-CARL-11.02: SB stress → regional bank SB loan losses (WARMING-ORANGE, Q2-Q3 visibility)

### Source Documents
- POP/domain/sources/INVISIBLE_INCOME_DEEP_DIVE.md (610 lines, 32 sources)
- POP/domain/sources/SB_BANK_PIPELINE_DEEP_DIVE.md (338 lines, 46 sources)

---

## 2026-04-06 — STUE FIRST SPAWN: CASCADE AMPLIFIER FINDING + CRL-05 UPGRADE

### PREDICTIONS Updated
**Author:** CARL (via STUE analysis)
**Action:** CRL-05 confidence upgraded 72% → 82%. Two new predictions added (CRL-13, CRL-14).

| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-05 | 72% → **82%** | CC 90+ DQ GFC breach. STUE cascade analysis: student loan credit score destruction (-87 to -171 pts, NY Fed data) cascades into CC DQ. 10-12M borrowers face score damage → 3-5M cascade into CC 30+ DQ → est. +0.5-1.0pp to CC 90+ rate. This is an ADDITIONAL pathway to GFC breach beyond cost squeeze. Two independent mechanisms now identified: (1) multi-vector cost squeeze, (2) student loan credit score cascade. |
| CRL-13 | **NEW** 70% | SAVE non-selection rate >35%. Based on Oct 2023 precedent + MOHELA failures. 2.6M+ face $0→$407/mo payment cliff. |
| CRL-14 | **NEW** 65% | MOHELA-caused additional defaults >500K from July 1 transition. Servicer operational capacity near-zero for clean transition. |

**Key analytical finding:** Student loan vector is a **cascade amplifier**, not just a standalone 5/5 convergence score. It raises the effective impact of CC (Vector 1), subprime auto (Vector 2), K-shape convergence (Vector 9), and foreclosure acceleration (Vector 10) through the credit score destruction channel.

### STUE STATUS.md Updated
**Action:** Comprehensive refresh with Spawn 1 data pulls.
- SAVE: "ending" → **"REPEALED BY LAW"** (Working Families Tax Cuts Act)
- Added: ED final guidance Mar 31, Tiered Standard Plan option, 8.8M forbearance (6.5M SAVE), Exhibit C deadline MISSED (auto full relief), 25% of all borrowers DQ (3x pre-pandemic), 1,800+ colleges flagged, payment shock quantified ($0→$407/mo), spending destruction ($1.5-2B/mo), non-selection rate estimate (30-45%), Senate opposition to Treasury transfer
- Upgraded status: 🔴 → 🔴🔴 CRITICAL

### New KB Entries
KB-CARL-155 through KB-CARL-157 (HH spending-income scissors, BofA spending-by-income tier, Minneapolis Fed K-shape publication).

### Data Pruning
- KB-CARL-029: ACTIVE → SUPERSEDED (by KB-145)
- ML-CARL-SL-01: ACTIVE → SUPERSEDED (by KB-145, STUE owns detail)
- ML-CARL-SL-02: ACTIVE → SUPERSEDED (Ninth Circuit resolved, KB-149)
- VX-CARL-1.06: RED → CONSOLIDATED (into SL-01 through SL-07)
- VX-CARL-SL-03: "ENDING" → "REPEALED BY LAW"

**Old view:** Student loan at 5/5 max, standalone vector. SAVE "ending" Jul 1.
**New view:** Student loan at 5/5 AND cascade amplifier for Vectors 1/2/9/10. SAVE REPEALED BY LAW. CC GFC breach pathway now dual-mechanism (cost squeeze + credit score cascade). CRL-05 is the upgraded conviction call.

---

## 2026-04-04 — STUDENT LOAN VECTOR REFRESH: 4→5, STUE ACTIVATED

### THESIS Updated (minor, no version bump — convergence upgrade)
**Author:** CARL
**Action:** Student loan convergence vector #4 upgraded 4→5 (max). Convergence score 46→47/50. STUE sub-agent created.

**What changed:**
1. **FSA Data Center (Dec 2025, Mar 13 release):** 7.7M borrowers in default on $180B. +2.5M since Sep 2025. Active repayment 31+ DQ rate: 18.6% by dollar (vs 12.7% Dec 2019 — 46% worse). <40% of borrowers in repayment.
2. **~25% DQ rate:** Protect Borrowers/TCF analysis — 25% of borrowers with payment due are behind. 7.9M entered delinquency in first 3Q 2025. Projection: 13M in default by EOY 2026.
3. **SAVE ending Jul 1:** Settlement with Missouri. 7.5M borrowers get 90 days to select new plan. Non-selectors → 10-year standard plan (payment shock). RAP launches Jul 1.
4. **MOHELA failures:** 2.5M missed bills → 800K manufactured delinquencies. Wait times 7-50x peers. ~2M credit report errors. $7.2M DOE penalty.
5. **Treasury transfer (Mar 19):** Phase 1 — 9M defaulted borrowers to Treasury. Legal authority disputed.
6. **Sweet v. McMahon:** 205K automatic discharges (Ninth Circuit rejected DOE delay Mar 25). Minor positive, drop in bucket.

**Old view:** Student loan 90+ DQ at 9.6%, trending toward 10%. Vector score 4/5. SAVE enjoined, forbearance holding. Passive monitoring.
**New view:** Mass default event actively executing. 7.7M in default, 25% DQ, servicer failures amplifying, SAVE ending forces 7.5M into repayment Jul 1, Treasury transfer creating chaos. Vector score 5/5 (max). STUE sub-agent activated for dedicated tracking.

### PREDICTIONS Updated
| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-04 | 88% → **95%** | Student 90+ DQ >10%. FSA confirms 7.7M default, ~25% DQ, 18-29 cohort at 21%. SAVE ending Jul 1. Near-certain on next NY Fed release. |

### New KB Entries
KB-CARL-145 through KB-CARL-151 (7 entries covering FSA update, DQ rate, SAVE settlement, Treasury transfer, Sweet v. McMahon, MOHELA failures, demographic concentration).

### New VX Entries
VX-CARL-SL-05 (Borrowers in Default), VX-CARL-SL-06 (Treasury Transfer), VX-CARL-SL-07 (Servicer Failure). Existing SL-01 through SL-04 upgraded ORANGE→RED.

---

## 2026-04-03 — NFP MARCH: HEADLINE MASKS STRUCTURAL ROT

### PREDICTIONS Updated
**Author:** CARL
**Action:** Confidence adjustments on 3 predictions after NFP Mar +178K headline beat.

| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-05 | 75% → **72%** | CC 90+ DQ GFC breach. Headline beat removes single-month employment catalyst, but Feb revised to -133K, LFPR 61.9%, real wages near zero. Multi-vector cost squeeze now primary driver, not employment break. |
| CRL-09 | 75% → **73%** | JOLTS Mar <0.88. NFP +178K could imply some hiring channels reopened (healthcare, construction), but Kaiser return is one-time and LFPR collapse means denominator may shrink. |
| CRL-11 | 85% → **83%** | Hires rate ≤3.2%. NFP establishment survey shows hiring in healthcare/construction/transport, but Kaiser is one-time. LFPR collapse suggests discouraged workers exiting, not broad hiring. |

**Old view:** NFP -92K (Feb) was the employment catalyst accelerating consumer stress conversion.
**New view:** NFP Mar +178K headline removes acute employment break narrative but internals (LFPR 61.9%, Feb revised -133K, wages 3.5% YoY) confirm structural rot. Mechanism unchanged — cost squeeze is primary, not employment detonator. Timeline: no change to Q2-Q3 stress window.

**No THESIS version bump.** Thesis structure unchanged. Evidence base shifts slightly (employment less acute, but structural rot deepens). All load-bearing vectors intact.

---

## 2026-04-03 — FILE STRUCTURE REORGANIZATION

### THESIS.md Restructured
**Author:** CARL + Will
**Action:** Moved THESIS.md to thesis/ directory. Extracted Composition Shift narrative to this CHANGELOG. Convergence matrix marked as canonical (STATUS.md mirrors). PREDICTIONS.tsv moved from workbook/ to thesis/.

---

## 2026-03-31 — v2.1: JOLTS INVERSION + GAS $4 + TRIPLE NITROGEN SEIZURE

### THESIS Updated: v2.0 → v2.1
**Author:** CARL
**Action:** Minor version bump. Three vectors converging simultaneously confirmed.

**What changed:**
1. **JOLTS Feb: 0.91 (deepening).** Ratio dropped from 0.94 (Jan) to 0.91 in one month. Hires rate 3.1% = COVID-low. Quits rate 1.9% (8-month streak — workers trapped). Feb data PREDATES Iran — March will be worse.
2. **Gas $4.02 behavioral breakpoint FIRED.** Up $1.04 in 33 days (+35%). SPR 172M barrel release failing — gas rose through the entire release. CNN behavioral confirmation of fuel-vs-food tradeoffs.
3. **USDA wheat acreage: LOWEST SINCE 1919.** Corn -3.45M acres. Farmers fleeing N-intensive crops. Triple nitrogen seizure confirmed (Gulf + China + Russia). Food CPI loading for Q3-Q4.
4. **Convergence score upgraded:** UI exhaustion 4→5 (duration +2.0wk single month), gas confirmed at max. Total: 44→46/50.

**Old view (v2.0):** Multi-vector cost squeeze replacing employment detonator. Gas approaching $4, JOLTS newly inverted, food CPI possible but unconfirmed.
**New view (v2.1):** Three independent vectors SIMULTANEOUSLY confirmed/firing. Gas $4 breached. JOLTS deepening. USDA locks in food CPI. No longer prospective — executing. Q3 = consumption stress quarter.

### PREDICTIONS Added
- CRL-09: JOLTS Mar ratio <0.88 (75% conf)
- CRL-10: Food CPI YoY >4.0% (70% conf, Q4 2026)
- CRL-11: Hires rate ≤3.2% through Q2 (85% conf)

---

## 2026-03-27 — INSURANCE RELIEF COUNTER-SIGNAL

### THESIS Updated (minor, no version bump)
**Author:** CARL
**Action:** Added insurance relief as counter-evidence.

**What changed:**
- Auto insurance CPI collapsed from 20-30% to 5.9% YoY (BLS Feb 2026)
- Homeowners insurance decelerating: national +8.5%, FL +18%, down from 50% (Insurify 2025)
- Two cost-squeeze vectors easing

**Assessment:** Partially offsets thesis but outweighed by energy, food, and UI exhaustion vectors intensifying. No score change. Logged in counter-evidence section.

---

## 2026-03-10 — v2.0: MECHANISM SHIFT (MAJOR)

### THESIS Updated: v1.0 → v2.0
**Author:** CARL
**Action:** Major version bump. Thesis mechanism fundamentally changed.

**Old view (v1.0, Feb 2026):** Employment cracks → subprime auto/CC DQ spikes → bank NCOs → systemic repricing. Linear, fast, employment-first. Single-point-of-failure model.

**New view (v2.0, Mar 2026):** Multiple cost vectors (energy + food + insurance + HOA) simultaneously compress the bottom 60% while housing prices decline nationally. Employment is a slow grind, not a detonator. K-shape converging downward (top 40% now pulling back). Conversion through COST SQUEEZE + UI EXHAUSTION rather than mass layoffs.

**Why the mechanism changed:** v1.0 assumed employment breaks → credit collapses → banks eat losses. Reality is a multi-point-of-pressure system. We expected an earthquake; we got subsidence — the ground is sinking everywhere, slowly, from multiple causes. The destination (consumer credit crisis → bank losses) is the same; the path is different.

**Implications:**
- **Timing:** Slower than v1.0. Q2-Q3 stress, grinding not step-function.
- **Trades:** Longer duration needed. Roll timelines, don't trim positions.
- **Convergence score:** Established 10-vector matrix to track multi-source pressure.

### PREDICTIONS Established
- CRL-01 through CRL-08 created (initial prediction set)

---

## 2026-02-23 — v1.0: THESIS ESTABLISHED

### THESIS Created: v1.0
**Author:** CARL
**Action:** Initial thesis — "Beneath the Ice"

**Core claim:** 60% of American households are structurally fragile. Employment crack is the detonator. Subprime auto and CC delinquencies are the first visible signals. Bank NCOs follow.

**Initial predictions:** CRL-01 (gas peak stress), CRL-02 (subprime auto 60+ DQ >7.0%)

---

*This document is the audit trail for thesis evolution. Log every change with what/why/old→new. Read when assessing conviction or reviewing prediction calibration.*
