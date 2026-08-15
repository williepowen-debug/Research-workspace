# CARL — NY Fed Q2 2026 HHDC GRADING CARD
## ⚠️ FROZEN 2026-07-24, ~22 days before the data. Will-directed.

**Release:** Federal Reserve Bank of New York, *Quarterly Report on Household Debt and Credit, 2026:Q2* — expected **~2026-08-15** (Q1 2026 was released 2026-05-12; cadence is early-to-mid month following quarter-end). Data source: NY Fed Consumer Credit Panel / Equifax.

**Why this card exists.** On 7/24 the entire pre-registered Q2 consumer-credit cluster resolved against CARL's masking framework — 0 of 4 names, CRL-24 MISSED, COF *released* $662M of allowance. CARL's response was to discount those prints as issuer-level survivor bias and hold the convergence score. **That response is only legitimate if the un-masked measure is named in advance, with its consequences fixed before the data.** This card is that commitment. It is written 22 days early precisely so it cannot be tuned to the outcome.

**FREEZE RULE.** No edit to the thresholds, cells, or consequences below after this file is committed. If something genuinely needs changing, append a **dated addendum at the bottom** stating what changed and why, and the original stays visible. A silently edited grading card is worth less than no card.

---

## 0. ⚠️ INSTRUMENT CORRECTION — the V2 candidate I armed on 7/24 was specified against the wrong series

On 7/24 I wrote that a **"V2 (Subprime Auto 60+) 4→3 downgrade candidate"** was armed and "resolves on the ~8/15 NY Fed Q2 HHDC." **That is wrong, and building this card is what surfaced it.**

- **V2's own pre-registered downgrade trigger** (`thesis/THESIS.md`, matrix row 2) is: *"Fitch ATR drops below 6.5% for 2 consecutive months OR cure mechanism reverses across 3 trusts."* **Fitch Auto Loan ABS Index (ATR), monthly — not the HHDC.**
- **The HHDC does not publish a subprime auto series at all.** It reports auto loans **blended across the full credit spectrum**. A blended series cannot resolve a subprime-specific vector — that is the same composition error the masking framework itself is built on ([[finding_blended_index_masks_bifurcation]]).

This is the third instance in eight days of a threshold that fails on its **specification** rather than on the world (`finding_threshold_spec_fails_before_world`, promoted to auto-memory 7/24). I would have walked into it on 8/15 and either mis-graded or quietly re-specced after seeing the data. **Corrected here, before the print.**

**Restated correctly:**

| Vector | What actually resolves it | Can the 8/15 HHDC move it? |
|---|---|---|
| **V2 Subprime Auto 60+** (score 4) | **Fitch ATR <6.5% for 2 consecutive months**, or cure reversal across 3 trusts | **NO.** Needs the Fitch ATR monthly series. Track separately; the HHDC auto data is *corroborating context only*. |
| **V1 CC 90+ DQ → GFC** (score 4) | HHDC CC 90+ share — but the registered downgrade trigger is *"drops below 12.0% for 2 consecutive quarterly readings"* | **NOT ON ONE PRINT.** Q1 is 13.1%; <12.0% in Q2 would be a 1.1pp single-quarter collapse. A low Q2 **starts the 2-quarter clock**, it does not complete it. |

**Therefore, stated plainly and in advance: no convergence vector can be downgraded on the 8/15 HHDC alone under the triggers currently registered.** What this print *can* do is (a) resolve **CRL-05**, (b) deliver the un-masked discriminator between "the consumer is genuinely healing" and "issuer books are survivor-biased," and (c) start clocks. **If the print lands in the CONTAINMENT cell (§4) and I then want a same-print score move, that requires Will to authorize a new trigger — it is a thesis change, and inventing one after seeing the data is exactly the move this card exists to prevent.**

---

## 1. Q1 2026 BASELINES — locked (from `domain/sources/2026-05_NYFed_HHDC_2026Q1_condensed_brief.md`, primary-verified)

| Metric | Q1 2026 | Prior | Where in the report |
|---|---:|---:|---|
| **CC balances 90+ days delinquent (share)** | **13.1%** | 12.70% (Q4-25) | Report p. 12 / PDF p. 15 (product chart) |
| Student-loan balances 90+ DQ | **10.3%** | 9.6% | Summary, PDF p. 2 |
| Debt in **any** stage of delinquency | **4.8%** | ~unchanged | Summary, PDF p. 2 |
| CC **transition into early (30+)** DQ | **8.6%** | 8.7% (declining) | Report p. 13 / PDF p. 16 |
| CC **transition into serious (90+)** DQ | "mostly unchanged" | — | Report p. 14 / PDF p. 17 |
| Mortgage transition into serious (90+) DQ | **1.5%** | 1.4% (the only serious transition that rose) | Report p. 14 / PDF p. 17 |
| Auto transition into serious DQ | "mostly unchanged" | — | Report p. 14 / PDF p. 17 |
| Auto 90+ stock | **chart-only, NO exact figure in report text** | — | Report p. 12 / PDF p. 15 |
| Total household debt | $18.8T | +$18B QoQ | Summary, PDF p. 2 |
| CC balances | $1.25T | −$25B (seasonal) | Summary, PDF p. 2 |
| Third-party collections (share of consumers) | 5.0% | slight deterioration | Summary, PDF p. 2 |
| New foreclosure notations | 59,000 | slight increase | Summary, PDF p. 2 |
| New bankruptcy notations | 124,000 | unchanged | Summary, PDF p. 2 |
| CC limits / HELOC limits | +$60B (+1.1%) / +$14B (+1.4%) | expanding | Summary, PDF p. 2 |

**GFC reference peak for CC 90+: 13.74%.** Gap at Q1: **0.64pp.**

---

## 2. THE PRIMARY QUESTION — CRL-05

**CRL-05 (85% confidence, registered 2026-03-10): CC 90+ DQ breaches 13.74% (GFC peak). Timeframe Q2-Q3 2026.**

| Q2 print | Grade | Consequence |
|---|---|---|
| **≥13.74%** | ✅ **CONFIRMED** | Breach. Fire the cross-agent 🔴 to PROME per CLAUDE.md signal table. V1 stays 4 (the vector was already scored for a near-GFC level; a breach is confirmation, **not** an automatic promote to 5 — 5 is reserved for "fully fired, no further upside," and 13.74% is a reference point, not a ceiling). |
| **13.1% – 13.73%** | **OPEN, holds** | Still rising or flat into the breach window. Confidence stays 85% if rising, trims to ~75% if flat two quarters running. Q3 (~Nov) becomes the resolver; if it has not breached by the Q3 print, **CRL-05 resolves MISSED at that point** — the registered timeframe is Q2-Q3 2026 and I will not extend it a third time without a stated mechanism reason. |
| **12.0% – 13.09%** | ⚠️ **Materially adverse** | First decline off the 15-yr high. Cut CRL-05 85 → **≤55**. Starts the V1 two-quarter downgrade clock. Goes in the CONTAINMENT cell (§4). |
| **<12.0%** | ❌ **Near-fatal to CRL-05** | Cut to **≤25** and register V1 downgrade-clock quarter 1 of 2. A 1.1pp single-quarter drop would be the largest in the series' recent history and would mean the consumer-credit core of "Beneath the Ice" is wrong, not masked. |

---

## 3. THE DISCRIMINATOR — survivor-pool optics vs. genuine healing

This is the reason the print matters beyond CRL-05. The Q2 issuer prints (ALLY −40bps QoQ, COF −39bps + $662M release, SYF 5.43% under its ceiling, AXP flat) all improved. **The masking framework predicts the bureau-wide data will NOT improve in step, because issuers charge off, sell, or decline the worst borrowers and the bureau still sees them.**

**Pre-registered discriminator — I commit to reading it this way and no other:**

| Pattern in the Q2 HHDC | Reading | Pre-committed consequence |
|---|---|---|
| **A. Bureau DETERIORATES while issuers improved** — CC 90+ up, and/or aggregate DQ >4.8%, and/or CC serious-DQ transitions turn up | **SURVIVOR-POOL CONFIRMED.** The divergence is the mechanism, measured. | Masking framework **vindicated on its strongest available test.** CRL-20 back **45 → 65**. V1 holds 4. Route to REGINALD + RED as a resolved divergence. |
| **B. Bureau FLAT (±20bps on CC 90+) while issuers improved** | **Ambiguous — and I will call it ambiguous, not favourable.** | No confidence increase in either direction. CRL-20 holds 45. Explicitly NOT scored as support. Q3 becomes the tiebreak. |
| **C. Bureau IMPROVES roughly in step with issuers** (CC 90+ down ≥20bps AND aggregate DQ ≤4.7% AND CC transitions falling) | **CONTAINMENT gaining. The masking read is losing its central claim.** | CRL-20 **45 → ≤25**. CRL-05 per §2. Escalate to Will: V1 downgrade candidate with a *newly authorized* trigger, and **RED gets an explicit invitation to call the thesis on it.** |
| **D. Bureau improves MORE than issuers** | **Masking framework refuted on its own terms.** | CRL-20 → **≤15** and CRL-21 → resolve MISSED early rather than wait for October. Full thesis review, Path C provisional status revisited. |

**Cell C or D is a real possibility and I am recording that in advance.** Three consecutive quarters of bureau-wide improvement would mean the bottom-60% credit deterioration I have tracked since March is resolving, and "Beneath the Ice" would need to be rewritten, not defended.

---

## 4. WHAT DOES **NOT** COUNT — guards against my own known failure modes

Written now so they cannot be reached for later:

1. **A seasonal explanation does not rescue an adverse print.** Q2 CC balances/DQ have seasonal structure; if the print is adverse to me I may note seasonality *only* by comparing to the same quarter in prior years, not by asserting it. (`finding_threshold_spec_fails_before_world`, seasonal-artifact limb.)
2. **"Transitions vs stock" is not a free pass.** If the 90+ **stock** falls but **transitions into** 90+ rise, that is a genuine mixed read and gets logged as mixed — not as confirmation. The reverse also holds: I do not get to cite a falling transition rate as improvement if the stock is climbing. Q1 already had this shape (stock up, transition INTO 90+ down 16.2→10.9%) and I flagged it then; the Q2 print is what disambiguates.
3. **The VantageScore 4.0 caveat is settled and may not be re-raised.** It affects the credit-score-band charts (report pp. 6-9) only. The headline 90+ DQ rate is balance-based ($ delinquent ÷ $ total) and scoring-method-independent (Liberty Street + Wolf Street, May 12 2026). I resolved this on 2026-06-09; it is not available as an excuse.
4. **Revisions.** If Q1 is revised, grade against the **revised** Q1, and say so. Do not grade a Q2 print against a Q1 baseline the Fed has since restated.
5. **Chart-only figures are not exact figures.** The auto 90+ "~5.6% Q1 record" has been UNCONFIRMED since 7/12 — the Q1 report text contains no exact auto 90+ number. If Q2 is again chart-only, **it stays unconfirmed**; I do not get to eyeball a chart and call it a datum. (Open ROADMAP thread since 7/12.)
6. **Credit-supply expansion is a counter-signal and stays on the counter side.** CC limits +$60B / HELOC +$14B in Q1 means lenders were not tightening. If limits expand again in Q2, that is evidence *against* the stress thesis and goes to RED's containment list (KB-326), not into a footnote.
7. **One print is one print.** Whatever this shows, it is a single quarterly observation. It cannot by itself confirm the thesis either. The 2-quarter and 2-month structures in the registered triggers exist for a reason and I will not shortcut them in the direction I prefer.

---

## 5. SECONDARY READS — logged, not score-bearing

| Metric | Baseline | Why I care | Owner |
|---|---|---|---|
| Student-loan 90+ | 10.3% | CRL-04 already CONFIRMED; Q2 disambiguates the Q1 flag (stock rose 9.6→10.3% while the 4Q-sum transition INTO 90+ fell 16.2→10.9%) — on-ramp slack vs cohort exhaustion vs reacceleration | CARL/STUE |
| Mortgage serious-DQ transition | 1.5% (up from 1.4%) | Only serious transition that rose in Q1; pairs with **FHA total DQ 11.88%, highest since Q2-2021** (DEWEY 7/24) — the student-loan→FHA bridge | CARL/HOMER |
| New foreclosure notations | 59,000 | Consumers, not properties — the tempering context against ATTOM's +21% H1 filings | HOMER |
| Third-party collections | 5.0% | Medical/utility-heavy per the data dictionary — DOC's medical-debt channel in bureau primary | DOC |
| Auto 90+ / auto transitions | chart-only / "mostly unchanged" | **Corroborating context for V2 only.** Does NOT resolve V2 — see §0 | CARL |
| CC / HELOC limits | +1.1% / +1.4% | Credit-supply counter-signal (guard #6) | CARL → RED |

---

## 6. SEPARATE INSTRUMENT — the actual V2 resolver

**V2 (Subprime Auto 60+, score 4) resolves on the Fitch Auto Loan ABS Index (ATR), monthly.**

- Last CARL reading: **6.90% (Jan 2026)** — 32-year high, +34bps YoY, per Fitch via Auto Finance News (reframed May 2026). **That reading is now ~6 months stale and is the weakest link in the V2 score.**
- Registered downgrade trigger: **ATR <6.5% for 2 consecutive months**, or cure mechanism reverses across 3 trusts.
- **Owed action, independent of the HHDC: refresh the Fitch ATR series before 8/15** so the V2 discussion rests on current data rather than a January print. If ATR has been drifting down through H1 in step with the ALLY/COF improvement, **V2's own trigger may already be closer to firing than the HHDC would ever have shown** — and I would not have known, because I was pointing at the wrong instrument.

---

## 7. GRADING PROTOCOL

1. Pull the **primary PDF** from newyorkfed.org, not a press summary. (Press-cite half-life is real — the "FICO Spring 2026 ~9.8%" error came from a derivative cite; STUE caught it 6/9.)
2. Fill §1's table with Q2 actuals **before** writing any interpretation. Numbers first, reading second — SIGNAL separate from INTERPRETATION.
3. Grade §2 (CRL-05), then §3 (discriminator cell), then apply the §4 guards **as a checklist, out loud, in the write-up**.
4. Write the result into: `thesis/PREDICTIONS.tsv` (CRL-05, CRL-20) · `thesis/CHANGELOG.md` · `STATUS.md` · `workbook/KB.tsv` (one row) · this card as a dated §8 addendum.
5. Route: PROME (score/thesis consequence) · REGINALD (bank-side) · RED (**especially cells C/D — RED is invited to press it**).
6. If the print is adverse and I find myself writing more than a paragraph of explanation for why it does not count, **that is the tell that I am rationalizing.** Stop and route it to RED instead.

---

## 8. ADDENDA
*Original freeze 2026-07-24. Post-freeze changes go here, dated, with the original text above left intact.*

### 2026-07-24 — ⚠️ THE CELLS NOW CARRY POSITION CONSEQUENCES (Will ruling, relayed via NEXUS ~3:45 PM ET)

Will ruled on CRL-21's pre-registered position-action commitment: **it is DEFERRED to this print and DECIDED BY THIS CARD'S CELLS.**

| Cell (§3) | Position consequence |
|---|---|
| **D — masking refuted** | Execute the **FULL** commitment: trim short positions 25% **and** extend duration to Q2-2027+ |
| **C — masking losing** | The **duration-extension half only** |
| **A / B** | **Hold** — revisit at the ~Oct vintage leg |

Construction routes through **TERRY** when/if a cell fires; **Will approves**. Will's words: *"we can just revisit Aug 15th or later."* Timing alignment flagged by NEXUS: the **Aug-21 expiries (OZK ×5, KRE ×3, WAL ×1)** get handled in the same post-8/15 TERRY session with the cell verdict in hand.

**This is recorded as an addendum, not an edit, because it materially changes what the card does** — §3's cells were written to move confidence and score; they now also move capital. **The freeze rule is what forced this to be visible rather than absorbed into §3.**

### 2026-07-24 — RED has pre-registered a rationalization test against CARL on this print (ACCEPTED)

RED, verbatim: *"if the ~8/15 HHDC prints benign-or-better on the subprime/delinquency legs and V2 does not go 4→3, I file that as a scored rationalization finding against CARL."* Their framing, which I accept: **the test is not today's decision — it is whether the arming is a COMMITMENT or a QUEUE.** Rationalization would be nominating yet another instrument if 8/15 also comes in benign.

**⚠️ Instrument correction owed back to RED, because their grading condition inherits the defect I fixed this morning:** **V2 does not resolve on the HHDC** — it publishes no subprime auto series. The correct pairing is **Fitch ATR ~8/10 → V2** (its own v3 seasonality-matched trigger) and **CC 90+ on this print → CRL-05 / V1**. Grade against those two, not against a V2-on-HHDC condition that cannot fire.

### 2026-07-31 — DATE: the print window is **8/4–8/11, NOT ~8/15** (PROME 7/25, adopted; cells untouched)

The "~8/15" this card carries in prose was **unconfirmed and is a Saturday**. NY Fed cadence: Q1-2026 printed **Tue 5/12** (media advisory 5/5); Q2-2024 precedent **Tue 8/6**. **Working window: Tue 8/4 – Tue 8/11; pin the exact date when the media advisory posts (~1 week ahead — not out as of 7/31).** Nothing in the cells changes; **only when they grade** — plausibly ~a week earlier than planned. Consequences applied 7/31: Fitch ATR refresh re-dated **8/3** (before the window opens), CARL docket rows re-dated. Every "8/15" in the frozen text above should be read as "the Q2 HHDC release date."

### 2026-07-31 — Pre-registered INTERPRETIVE context for the grade session (flagged BEFORE the print; changes no cell, no threshold)

Recorded now so none of it can be reached for *after* seeing the data — in either direction:

1. **Cascade attribution is capped (STUE 7/25, DEWEY C2 accepted in full):** SL-delinquent borrowers hold **~2% of US CC balances (~$25B)**; the student-loan cascade closes **≤⅓ of the 0.62pp gap** to the GFC line, and **~62% of the Q1 share rise was denominator shrink**. **Expect the breach; don't attribute it to the cascade.** A CC 90+ breach graded in cell A/B on the *level* must not borrow causal support the arithmetic can't carry.
2. **The stock-vs-flow divergence is definitional, not hidden stress (DEWEY C2 via REGINALD 7/25):** the CCP/Equifax CC 90+ share (13.1%) is a **STOCK** measure including charged-off paper aging on reports for years; bank supervisory data (DRCCLACBS 2.92%, 5 straight quarters down; NCOs 3.84% vs 4.46% yr-ago) measures loss-bearing books and is **improving**. A breach on the stock measure while bank flow improves is **consistent with BOTH** "survivor-pool optics" (cell C/D direction) **and** "aged-paper composition" (benign). The §3 discriminator cells (early-DQ transitions, cohort splits) — not the headline level — carry the grade. This cuts BOTH ways and is logged to stop me over-reading a headline breach as masking-confirmed.
3. **Denominator guard:** any share-based cell input gets decomposed numerator-vs-denominator before grading (the Q1 precedent: 62% of the rise was denominator shrink).

---

### 2026-08-11 — ✅ **THE CARD IS GRADED. Print released Tue 8/11; graded same evening.**

**Primary:** `HHD_C_Report_2026Q2.pdf` + `HHD_C_Report_2026Q2.xlsx`, newyorkfed.org (§7.1 honored — primary, not a press summary; WebFetch returned 403, pulled via curl + browser-UA). Cover confirms **"2026:Q2 (RELEASED AUGUST 2026)"** — year-trap cleared. **Guard #4: Q1 was NOT revised** (13.1→13.12% is precision, not restatement; 4.76%, $18.784T, 59.16K, 10.34% all reconcile to §1's locked baselines) — graded against the original baseline.

**§1 actuals (Q1 → Q2):** CC 90+ **13.12 → 12.92%** · any-stage DQ **4.76 → 4.73%** · CC balances **$1.242 → $1.263T (+$21B)** · CC flow into 30+ **8.61 → 8.69%** · CC flow into 90+ **7.10 → 6.97%** · auto flow **7.72→7.87 / 2.97→3.00%** · mortgage flow **3.76→3.95 / 1.48→1.52%** · student 90+ stock **10.34 → 10.60%**, flow into 90+ **10.86 → 7.83%** · auto 90+ stock **5.60 → 5.49%** · foreclosures **59.2 → 55.2K** · bankruptcies **124.0 → 136.8K** · collections **4.98 → 4.88%** (avg amount **+2.4% to $1,577**) · CC limits **$5.474 → $5.559T** · total HH debt **$18.784 → $18.771T**.

**§2 → CRL-05 = ⚠️ MATERIALLY ADVERSE.** 12.92% lands in the **12.0–13.09%** band. Pre-committed consequence was *"cut 85 → ≤55"*; **taken to 20%**, below the ceiling, because the arithmetic is harsher than the band assumed: confirming by the registered Q3 endpoint needs **+82bps in one quarter** against a largest-recent-quarterly-rise of **+42bps**, straight after a −20bps print. **Stays OPEN; Q3 (~Nov) resolves; timeframe will NOT be extended a third time.**

**Addendum-3 denominator guard applied — and it does not rescue the prediction.** **100% of the 20bps decline is denominator growth: seriously-delinquent CC dollars ROSE $0.23B** ($162.95B → $163.18B) while balances grew 1.7%. The numerator did not improve. CRL-05 is written on the **share**, the share fell, the cut stands on its own letter. Logged as a structural read, not as relief.

**§3 → CELL B (AMBIGUOUS).** Called ambiguous, **not favourable**, per the cell's own wording. **A fails** (bureau did not deteriorate). **C fails on its third conjunct** — CC transitions are **mixed, not falling**: into-30+ **ROSE**, into-90+ fell; **auto and mortgage transitions rose on BOTH legs.** **D fails** (bureau +20bps vs issuers' 39-40bps). **→ CRL-20 HELD at 45, explicitly not scored as support in either direction. Q3 is the tiebreak.**

**⚠️ SEAM DEFECT IN THIS CARD, recorded rather than resolved silently.** Cells **B** (*"flat ±20bps"*) and **C** (*"down ≥20bps AND…"*) **both have their first condition satisfied at exactly −20bps** — the print landed on the seam between two of my own cells. C's conjunction is the disambiguator and it fails, so B governs. **4th instance of the threshold-spec class** ([[finding_threshold_spec_fails_before_world]]) and the first arising from two of *my own* pre-registered cells overlapping rather than from a misspecified instrument. **The freeze rule is what made this visible instead of absorbed.**

**⚠️ SECOND INTERNAL CONTRADICTION, same treatment.** §2's 12.0–13.09% band says the print *"Starts the V1 two-quarter downgrade clock"* — but **V1's registered trigger (`THESIS.md:290`) is "drops below 12.0% for 2 consecutive quarterly readings," and 12.92% is not below 12.0%.** §0 of this card exists precisely to make the registered trigger govern, so **the clock does NOT start.** Recording the coexistence rather than quietly picking, per the 8/3 card-vs-matrix precedent.

**Position consequence (7/24 Will addendum): CELL B → HOLD.** No trim, no duration extension. Revisit at the ~Oct vintage leg. **The Aug-21 expiries (OZK ×5, KRE ×3, WAL ×1) are therefore a standalone TERRY/Will decision, no longer card-driven.**

**Score: NO CHANGE, 53/70 holds** — exactly as §0 pre-committed. The adverse evidence landed in **confidence**, not in the score.

**§4 guards, run as a checklist:** ① seasonality — **not invoked**. ② stock-vs-flow — logged **MIXED**, not confirmation. ③ VantageScore — **not raised**. ④ Q1 unrevised ✓. ⑤ chart-only — **RESOLVED FROM A REAL DATUM:** the published *data file* gives auto 90+ numerically, **Q1 = 5.60% exactly**, confirming the relay figure unconfirmed since 7/12 and its **+39bps** Q4→Q1 acceleration; no chart was eyeballed. ⑥ **credit supply expanded again** (CC limits +$85B; HELOC balances 17th consecutive quarterly rise) → **RED containment list**. ⑦ one print is one print.

**§7.6 self-check — invoked, and obeyed.** Two structural counter-reads emerged that could each have been written up as "why the adverse print doesn't count": (a) **$40B drained out of 120+ late while $43.5B moved INTO severely derogatory** (1.754→1.987%) with bankruptcies **+10.3%** — the aggregate 3bps improvement is composition and the terminal bucket grew; (b) **mortgage carries a Fed-stated servicer-transfer reporting gap** this quarter, so mortgage *shares* are suspect while mortgage *transitions* (which rose on both legs) are not. **Both are routed to RED to press rather than banked as support, and neither was allowed to soften the CRL-05 cut.**

**🔴 ESCALATED TO WILL — outside this card's scope but discovered by grading it.** The registered **full-thesis kill rule** (`THESIS.md:398` — *"Claims <220K sustained 8+ weeks AND CC 90+ DQ declines 2 consecutive quarters"*) is **one print from firing**: claims **199K** (4-wk MA ~202,750) = leg 1 satisfied; **Q2 is decline #1 of 2**. Its v2.1-vs-v2.5.1 mismatch has been a ROADMAP open question since **2026-05-03**, three months pre-print, so raising it now is not post-hoc — **but rewriting a kill rule in the quarter it approaches firing is not CARL's call.** Will decides: leave as written and let Q3 grade it, or commission the re-spec **now**, pre-registered before the Q3 data.

**Source-text discrepancy flagged, not propagated:** the report's prose reads *"$85 billion (1.1%) uptick in the first quarter"* — inconsistent with its own data sheet (**$5.474T → $5.559T = +$85B = +1.6%, Q1→Q2**) and mislabeled as Q1 inside a Q2 report. Data sheet used.

**Written through to:** `thesis/PREDICTIONS.tsv` (CRL-05, CRL-20) · `thesis/CHANGELOG.md` · `STATUS.md` · `workbook/KB.tsv` (KB-CARL-382) · this addendum. **Routed:** PROME · REGINALD · RED · STUE · HOMER · DOC.

---

## §8 ADDENDUM — 2026-08-15 (Sat): **GUARD #4 WAS GRADED WRONG. Q1 *WAS* REVISED.** The grade survives; one headline figure becomes vintage-dependent.

**Appended under the freeze rule — the original §4 checklist verdict above stays visible and is NOT edited.**

**What the card said:** *"④ Q1 unrevised ✓"*, supported in CHANGELOG by *"13.1→13.12% is precision; 4.8→4.76%, $18.784T, 59.16K foreclosures, 10.34% student 90+ all reconcile to the locked baseline."*

**What is true:** the Q2 report carries its own footnote — ***"2026Q2 report includes a revision to 2026Q1 credit card balances outstanding"*** (`HHD_C_Report_2026Q2.xlsx`, Page 3 Data). Pulling the Q1 vintage directly (`HHD_C_Report_2026Q1.xlsx`, curl+UA, 2026-08-15):

| 2026Q1 figure | Q1 report | Q2 report | Revised? |
|---|---|---|---|
| CC 90+ **share** | 13.1200% | 13.1200% | **no** |
| CC **flow into 90+** | 7.1000% | 7.1000% | **no** |
| CC **balance** | **$1.2520T** | **$1.2420T** | **YES — −$10B** |
| Total debt | $18.7940T | $18.7840T | **YES — −$10B** |

**⚠️ HOW THE GUARD FAILED — the mechanism, because it is reusable.** Every figure in the supporting list was read **out of the Q2 report** and checked against a baseline that had **itself been sourced from the Q2 report.** A revision check that reads only the new vintage is **circular by construction** — it cannot detect a revision, and it returns ✓ with full confidence. **Detecting a revision requires opening the OLD report.** Guard #4's text (*"If Q1 is revised, grade against the revised Q1, and say so"*) never specified where the revision check gets its comparison, and that omission is the whole defect.

**CONSEQUENCE — bounded, and the grade stands:**
- ✅ **CRL-05's cut is unaffected.** It resolves on the 90+ **share**, and the share was **not** revised — the −20bps delta is exact.
- ✅ **The discriminator cell is unaffected.** Cell B rested on transitions, which were **not** revised.
- ✅ **The substantive half of guard #4 was in fact honored** — both quarters were pulled from the Q2 xlsx, so the grade *was* run against the revised Q1. What failed is the **reporting** half (*"and say so"*), which was answered with its opposite.
- ⚠️ **ONE HEADLINE FIGURE IS NOW VINTAGE-DEPENDENT AND MUST ALWAYS BE STATED WITH ITS BASIS.** The *"delinquent dollars ROSE $0.23B"* claim — the load-bearing sentence of the whole decomposition, the thing that let the card say *"the numerator did not improve"* — is derived (share × balance) and therefore inherits the balance revision:

| Basis | Q1 → Q2 delinquent CC dollars | Reads as |
|---|---|---|
| **Same-vintage** (both quarters from the Q2 report) — **CORRECT, and what the card used** | $162.95B → $163.18B | **+$0.23B, ROSE** |
| Cross-vintage (Q1 report's Q1 vs Q2 report's Q2) — naive | $164.26B → $163.18B | **−$1.08B, FELL** |

**The sign reverses.** The card's figure is the correct one, but anyone recomputing it from the Q1 report gets the opposite answer and would read the decomposition as *supporting* the benign case. The balance-growth claim also halves cross-vintage (+$21.0B/+1.69% → +$11.0B/+0.88%). **From here: cite the $0.23B only with "same-vintage (Q2 report)" attached.**

**Where this went:** it is the decisive evidence in `thesis/KILL_RULE_RESPEC_2026-08-15.md` §2(b) — a dollar-keyed kill leg would carry a $10B revision against a $0.23B signal (43×), which is why the re-spec keys leg 2 to the **flow** series (unrevised across this vintage pair) rather than to dollars. **The error and the fix are the same finding.**

*Discovered 2026-08-15 while drafting the row-44 re-spec, by pulling the Q1 xlsx to check whether the transition series was revision-stable. Not discovered by any check that was running.*
