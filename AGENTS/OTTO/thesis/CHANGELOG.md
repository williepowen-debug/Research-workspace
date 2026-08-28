# OTTO Thesis CHANGELOG

Audit trail of **thesis/POV pivots** — every material change in OTTO's view, logged
old → new with a date and trigger. This is the trajectory record that STATUS-narrative
pruning would otherwise destroy (per auto-memory `[[finding_pov_changelog_pattern]]`).

**Scope:** analytical/thesis changes only — conviction shifts, mechanism reframes,
prediction-confidence moves of note, new transmission rows, case-status escalations.
NOT routine dashboard refreshes (those live in STATUS) and NOT structural doc/folder
changes (those live in `MAINTENANCE.md`).

**Versioning:** OTTO's canonical thesis is `thesis/THESIS.md` (**v1.4 as of 2026-08-27** — the s019 bump: **First Brands plan confirmation DENIED and every debtor ordered into Ch.7 (Aug 24)**, moving the fraud-recovery-magnitude leg from forecast to court order while **neither systemic leg moves**; OTTO-32 85→97% resolving on ENTRY of the conversion order. *Prior: v1.3 2026-08-14* — the s018 bump: the **bank-contagion transmission leg joins the funding leg as DISCONFIRMED** (OTTO-30 falsified), Secondary-thesis falsifier #2 **ran, did not fire, and was re-specified as unsound** (a one-sided instrument), plus three factual corrections carried since v1.2 — the vacated Oct-19-2026 Tricolor trial date, the First Brands trial's true four-day/under-advisement posture, and the wrong "all 7 panel deals rising" claim — and a rebuilt calibration scoreboard naming **measure-design as the dominant failure family**. *Prior: v1.2 2026-07-25 absorbed the four s016 moves; v1.1 2026-07-04; v1.0 2026-06-09.*);
`STATUS.md` § THESIS is a live-state mirror. Entries here are dated and may cite the
thesis version they moved. *(Preamble corrected 2026-07-25 — it had described the
pre-Jun-9 layout, in which neither `thesis/THESIS.md` nor `MAINTENANCE.md` existed.)*

**Format:** reverse-chronological. Each entry: `### YYYY-MM-DD — headline`, then **Was → Is**, **Trigger**, **Touches**, and any calibration note. *(Un-fused from the first entry heading 2026-08-14 — the sentence had been concatenated onto an entry title since the v1.2 pass, so the newest entry always inherited the words "Format: reverse-chronological. Each entry:" as part of its heading.)*

### 2026-08-27 — First Brands: the recovery-magnitude leg goes from forecast to court order (confirmation DENIED, all debtors ordered into Ch.7)

**Was →** *"First Brands plan confirmation is under advisement since Aug 7; the plan routes 111 of 112 debtors to Ch.7 and both live outcomes deliver majority-Ch.7; a written ruling is OTTO-32's resolver, modeled ~Sep 15. OTTO-32 85%."* Admin-insolvency (recoveries grind toward zero because administrative expenses exceed estate value) was carried as a **forecast mechanism**.

**Is →** **Judge Lopez DENIED confirmation on 2026-08-24 and ordered EVERY debtor's case converted to Chapter 7.** `[CONF Dkt 3710, Order Denying Plan Confirmation, signed + entered 8/24/2026; Dkt 3701 Courtroom Minutes]`. Scope per the debtors' own filing `[CONF Dkt 3722, 8/26]`: the Court *"ordered that **each** of the Debtors' Chapter 11 Cases be converted to cases under chapter 7."* The admin-insolvency mechanic is now **operative fact, not forecast** — conversion removes the reorganisation path that was the only route above the admin-expense floor, on a $12B book already recovering <2%. **OTTO-32 85% → 97%, still OPEN**, resolver re-keyed to **entry** of the conversion order (which converts *"effective upon entry"* and is not yet entered).

**Scope discipline — what did NOT move.** This is a **recovery** event, not a fraud-discovery event: the confirmed-case count stands at **4**. **Neither systemic-transmission leg moves** — funding (OTTO-05, spreads tightened) and bank-contagion (OTTO-30, zero new US bank names) remain **DISCONFIRMED**. So the s018 asymmetry — *pattern and recovery-magnitude stand, both systemic legs are down* — **widens rather than reverses.** The Secondary thesis is untouched by this entry.

**Trigger:** the standing every-session poll of `docket_id:71483359` at s019 boot, after 13 days dark. **Not** the prediction scanner — see the calibration note.

**Touches:** `STATUS.md` (signal line, THESIS case table, First Brands vector rewritten, CRITICAL TIMELINE +2 rows / 1 retired / 2 swept-unswept, predictions mirror, signal-trigger row, footer, BOTTOM LINE) · `thesis/PREDICTIONS.tsv` (OTTO-32 85→97%) · `docket/CATALYSTS.tsv` (+2 rows, 1 retired, 2 swept) · `workbook/ML.tsv` (ML-OTTO-233→237) · `workbook/STATUS_archive_20260827.md` (new) · `NEXUS_BRIEF.md`.

**⚠️ Calibration note — the branch was right and the date was wrong, for the second consecutive session.** OTTO-32 **held at 85% since May** through a denied disclosure statement, a four-day trial and 17 days of advisement, with no trim when the timeline got uncomfortable. But the ruling arrived on **day 17** against a published **~Sep 15 midpoint** of a 2-8 week (14-56 day) band — *inside* the band. On 8/14 the NY Fed release had the identical shape (window right, midpoint 5 days early). **Two instances, same direction, same cause: a band is published as its midpoint, the midpoint is then read as the expected date, and the row goes unpolled until near it.** **Rule promoted: a `modeled` row is a WINDOW — stop publishing its midpoint as the date, and key poll cadence to the window's OPEN, not its centre.**

**⚠️ Second calibration note — the instrument built to flag this could not see it.** `predictions_due.py` reported *"0 overdue, 0 due soon"* on the morning OTTO-32 became decidable, because it keys **only on `Resolve_Date`** (9/30). **A prediction whose resolving event has already happened is structurally invisible to a date-keyed scanner.** It was the standing docket-poll rule that caught this, not the boot kit. **Sixth measure-design defect** (ML-OTTO-235); fix scoped, not built.

### 2026-08-14 — The Invisible Exit is disconfirmed as a GENERAL phenomenon; it survives only as a lender-concentration claim

**Was → Is.** *Was:* the Secondary thesis asserted that skip-default is a material, industry-wide driver of subprime auto loss — "a material fraction of subprime auto loans... exits through skip-default rather than 30/60/90-day delinquency," with conviction **HIGH on mechanism** since the Jun-24 indictment. *Is:* **the mechanism is confirmed at Tricolor and DISCONFIRMED as a general deep-subprime phenomenon**, on the first reading of a purpose-built test. Conviction splits: **(a) mechanism at Tricolor HIGH, unchanged** (criminally charged, 30K missing vehicles); **(b) mechanism as a general deep-subprime effect MEDIUM → LOW.**

**Trigger.** The **Severity-Divergence Test**, built this session to replace the retired one-sided NY Fed falsifier, returned **REFUTE** on its first run. `[CONF SEC 10-D, Exeter EART ×4, 13 monthly filings 2025-07-25 → 2026-07-30; Manheim UVVI YoY +1.3%, inside the ±3% common-mode band]` **Panel-mean ΔSeverity +0.06pp against ΔFrequency +1.85pp** — over twelve months deep-subprime delinquency rose ~1.9pp while loss severity did not move at all. Three of four deals show the ordinary-credit signature individually and **two show severity falling**.

**Why that is evidence and not noise.** The test's discriminator is an asymmetry, not a correlation: ordinary credit deterioration raises **frequency** at flat **severity** (more bad borrowers, same collateral); skip-default raises **severity** at flat **frequency** (the vehicle is gone, and the loan never enters the 30→60→90 roll). **Ordinary deterioration cannot produce the skip shape.** Thresholds were base-rated *before* they were set — pooled monthly recovery SD 2.12pp ⇒ minimum detectable skip-share change **4.5% at n=12** — so the null here is a measured null, not an absence of looking.

**Touches.** `thesis/THESIS.md` (conviction decomposition split (a)/(b); the whole § "What would falsify the Secondary Thesis" rewritten around the armed SDT + first reading), `thesis/PREDICTIONS.tsv` (**OTTO-35** created at 15%), `docket/CATALYSTS.tsv` (quarterly re-run docketed ~2026-11-15 with its decision rule pre-set), `STATUS.md` (dashboard row + predictions mirror + boot pointer), `scripts/severity_divergence.py` (new), `scripts/panel_10d.py` (upsert fix), `workbook/ML.tsv` ML-OTTO-229→232.

**⚠ The uncomfortable part, recorded rather than smoothed.** The thesis survived by narrowing — from "industry-wide" to "operates where the cohort is deliberately concentrated." That narrowing is defensible on the evidence (Tricolor really was 75% undocumented / 68% no credit score), **but the concentrated pools are 144A with no public performance reporting, so the narrowed claim is largely unfalsifiable from public sources.** A thesis that retreats to where it cannot be measured is weaker than it looks, and this one just did that once. **Decision rule pre-set so it is not re-litigated later: if the SDT returns REFUTE on the next two quarterly runs, cut the Secondary thesis's load-bearing role in the Primary thesis — do NOT narrow the claim a second time.**

**🟡 Lead, explicitly not a finding.** EART 2023-1 is the sole divergent deal (**severity +5.52pp**) and is also the deal whose 60+ DQ **fell** −0.16pp on the 7/30 filing. n=1 of 4; a servicing transfer or pool-specific event would look identical. Watch it; do not build on it.

---

### 2026-08-14 — THESIS bumped v1.2 → v1.3 (version-bump record)

**Was → Is.** *Was:* canonical `thesis/THESIS.md` at **v1.2 (2026-07-25)**, two sessions behind — it carried neither the s017 First-Brands-cramdown material nor any of s018, and contained three statements that had become **factually wrong**. *Is:* **v1.3**, current as of 2026-08-14.

**Trigger.** The v1.2 doc was flagged as owed in two consecutive closeouts (s017, s018) and the drift had passed from *incomplete* to *wrong* — the failure mode where a canonical doc keeps being cited because nobody re-reads what it actually says.

**What changed — four things, in order of consequence.**
1. **The BANK-CONTAGION transmission leg is added to the conviction decomposition as DISCONFIRMED.** With the funding leg already dead (Jul 4), **both** systemic-transmission channels are now measured and closed, while pattern + fraud-recovery magnitude are untouched. A consequence line was added telling readers plainly: *stop citing OTTO for "auto fraud transmits to banks."*
2. **Secondary-thesis falsifier #2 retired as tested-and-not-fired — and re-specified as unsound.** The NY Fed Q2 print (8/11) did not fire it, but the deeper finding is that **it never could have confirmed the thesis**: a skip cohort cannot move a $1.713T aggregate, so the instrument was one-sided. A properly-scoped cohort-level replacement is now explicitly **owed**, and the doc says so rather than quietly claiming falsifiability it does not have.
3. **Three factual corrections.** The Tricolor trial is **Jan 25 2027** (v1.2 carried the vacated Oct 19 2026 date, in two places); the First Brands confirmation trial ran **four days and has been UNDER ADVISEMENT since Aug 7**; and v1.2's **"all 7 panel deals have risen every month"** is wrong — **3 of 4 DEEP**, EART 2023-1 fell 0.16pp.
4. **Calibration scoreboard rebuilt** (9 resolved, 4/9 confirmed) with the clustering stated plainly — **every falsification sits on a transmission or measurement claim, none on the fraud-pattern claim** — plus **measure-design named as the dominant failure family (5 instances, 2 built after naming the pattern)** and a **break-condition scope amendment**: the break condition is written entirely on the fraud leg and therefore could not register either transmission disconfirmation. Rather than patch a clause in, the doc now declares two separable claims with two scoreboards, and marks the transmission claim **retired, not weakened**.

**Touches.** `thesis/THESIS.md` (header, conviction decomposition, ONE-LINER, case table, Secondary falsifiers + tier qualification, transmission chain stages 4-5 + critical observation, why-now driver 1, risk matrix, break condition, calibration scoreboard, failure-pattern synthesis, cross-agent links, footer stamp — **the v1.1 footer stamp that had been contradicting the v1.2 header is also fixed**), `STATUS.md` § THESIS mirror (v1.2 → v1.3, both "owed" flags cleared), this file's versioning preamble.

**Lesson worth keeping.** The doc did not drift because anyone disagreed with it — it drifted because **it is read as a pointer and edited as a record.** The three factual errors all had correct values sitting in STATUS on the same day. `[[finding_doc_mirror_consistency_check]]` catches *set* mismatches between canonical and mirror; it does not catch a canonical doc that is merely **old**. A version stamp two sessions behind is itself the tripwire — treat it as one.

---

### 2026-08-14 — OTTO-30 falsified: the "cockroach spreads to a 6th bank" transmission claim is DEAD, and it died on a pre-registered test

**Was → Is.** *Was* (since 2026-04-15): the Tricolor fraud would surface a **new** US bank counterparty by Q2-2026 earnings — the Cockroach thesis's bank-transmission leg, held at 45% until Jul 25 and 12% thereafter. *Is:* **FALSIFIED.** A complete EDGAR full-text scan of the entire window (2026-04-15 → 08-14) returns **zero new US bank names**. The named-bank list closes at **7** (JPM, Fifth Third, Regions, MTB, OBK, TFIN + Barclays-UK), every one of which disclosed *before* the window opened.

**Trigger.** The pre-registered falsification check written into the row on 2026-07-25, run 2026-08-14 once its gate (small-bank Q2 10-Q deadline ~08-14) closed. `[CONF SEC EDGAR FTS q="Tricolor", run-stamped 2026-08-14, 31 hits, complete scan]`

**Touches.** `thesis/PREDICTIONS.tsv` (OTTO-30 → FALSIFIED), STATUS § SIGNAL DASHBOARD (named-banks row → 🟢 closed) + § PREDICTIONS, `docket/CATALYSTS.tsv` (Aug-31 resolve row closed early), `workbook/ML.tsv` ML-OTTO-223.

**What this does and does NOT mean.** It kills the *bank-count* transmission channel, **not** the fraud thesis: Tricolor's mechanism is criminally charged, recovery is ~3%, and the $113M gridlock is unresolved. **The Cockroach thesis has now been disconfirmed on BOTH of its systemic-transmission legs** — funding (OTTO-05, spreads tightened) and bank-contagion (OTTO-30, no new names) — while remaining intact on **pattern and fraud-recovery magnitude**. That asymmetry is the honest 2026 shape of this thesis. **✅ Paid same session: `thesis/THESIS.md` bumped to v1.3 — see the version-bump entry above.**

**Calibration.** The 45→12% cut on 7/25 was made by **measuring** the instrument, and it pointed the right way three weeks before resolution — the process worked. The counter-lesson is the **known-unknown trap**, which fired **twice inside this single prediction** (OBK, then TFIN): both were names new to OTTO whose *first* disclosure predated the window. **A forward-discovery claim must be graded on a counterparty's FIRST disclosure date, never on the date of the filing that surfaced it.**

---

### 2026-08-14 — The consumer aggregate is demoted from evidence to a non-contradiction check

**Was → Is.** *Was:* NY Fed HHDC auto figures were carried in the SIGNAL DASHBOARD alongside the ABS panel and read as part of the Invisible-Exit evidence base. *Is:* **the consumer aggregate can never CONFIRM the Secondary thesis** — the skip cohort is far too small to move a $1.713T stock — so it is a **non-contradiction check only**, and OTTO stops citing it as confirming evidence.

**Trigger.** Q2-2026 HHDC (published 2026-08-11): auto transition into 90+ moved **+3.3bp QoQ to 3.0028%** (a first 3.00%+ print) while OTTO's deep-subprime 10-D panel sits at **10.8-14.8% 60+ DQ** and DEEP annualized net loss runs **18.85% vs BROAD 6.41%**. The divergence held and widened — which is what the thesis predicts, and precisely why the aggregate cannot be the instrument.

**Touches.** STATUS § SIGNAL DASHBOARD (three NY-Fed rows + an explicit RULING row), `docket/CATALYSTS.tsv` (2026-08-11 row), `workbook/ML.tsv` ML-OTTO-224. Applies auto-memory `[[finding_cohort_too_small_to_move_the_index]]`.

**Second-order note, recorded as hypothesis not conclusion.** Pct-of-balance 90+ **fell** to 5.49% while the transition rate **rose** — mechanically, balances are leaving the bucket faster than they enter, i.e. faster charge-off, which is what skip-defaults imply. **[EST] — not separable from ordinary seasonal charge-off timing with this data.** Same refusal-to-join discipline as the Carvana finance-GPU read.

---

### 2026-08-14 — Carvana: the tape rejected the read, and the read did not change

**Was → Is.** *Was* (s017): "the guide-down was absorbed in three sessions" — CVNA −3.6% vs the pre-print close. *Is:* CVNA **$75.92**, **+14.5% ABOVE the pre-print close**, +18.7% off the level STATUS carried, and only −7.4% from Gotham's split-adjusted $82.01. **The s017 framing was understated to the point of being wrong in spirit.**

**Trigger.** Live quote 2026-08-14 against the s017 dashboard value.

**Touches.** STATUS § SIGNAL DASHBOARD (CVNA price row), § THESIS case table, § Carvana vector; s017 Carvana block archived to `workbook/STATUS_archive_20260814.md`.

**The distinction being defended.** **Nothing has contradicted the finance-GPU series** (Other GPU/unit $2,869 → $2,807 → $2,666, accelerating) — **it has been ignored.** Those are different things, and a rising tape does not retire an instrument. What the price *does* refute is any near-term **timing** claim, and OTTO holds none on Carvana. Conviction on collateral quality is unchanged; conviction on the related-party allegation is unchanged; **the systemic/timing leg keeps disconfirming on schedule.**

---

### 2026-08-14 — OTTO-10 cut 65% → 20%, and the row finally names its instrument

**Was → Is.** *Was:* subprime origination share falls below 13% by Sep 30 2026, 65%, against a baseline of "14.7% (2025 est)" and **no named instrument**. *Is:* **20%**, with the instrument written in — **Equifax subprime UNIT share** (ML-OTTO-027 / VX-OTTO-055: 16.5% → 15.2% → 14.7%).

**Trigger.** The row's own series is **decelerating** (−1.3pp, then −0.5pp), extrapolating to ~14.2% for 2026 against a <13% line. Cut on arithmetic — the same discipline applied to OTTO-34 on 2026-08-03.

**Touches.** `thesis/PREDICTIONS.tsv` (OTTO-10 confidence + instrument line), STATUS § PREDICTIONS, `workbook/ML.tsv` ML-OTTO-228.

**The near-miss that is the real entry.** The NY Fed **<620 DOLLAR share is 16.13% and rising**, which read carelessly satisfies OTTO-10's invalidation ("stays >14%") on the spot. **It was not used.** Units ≠ dollars and Equifax ≠ NY Fed CCP — and the divergence is **mechanically real**: average subprime balance rose $22,800 → $24,575, so **dollar share can rise while unit share falls and both series are correct simultaneously.** The defect the near-miss exposed is that **the row named no instrument at all**, which is exactly what made grading it off the wrong series available. Applies `[[finding_cross_entity_comparison_needs_same_perimeter]]` and `[[finding_hypothesis_needs_an_instrument_for_its_defining_mechanism]]`.

---

### 2026-08-03 — First Brands: the vote says CRAMDOWN, which is the branch consensus was writing off

**Was → Is.** *Was* (s016 + fleet-wide, 7/25-7/31): the plan is "creditor-backed going in," so an outright class rejection and a cramdown fight looked like the weaker branch; ballot tallies were believed non-public until a 7/27 certification. *Is:* the tabulation was filed **2026-07-24** (Dkt 3351) and says the **secured classes accepted 100% by number AND amount at every debtor** while **Class 7 general unsecured rejected at 83 of 92 subclasses** — **confirmation requires §1129(b) cramdown at 83 debtors.** "Creditor-backed" was true of the *secured stack only*.

**Trigger.** Docket-primary pull of the Kroll/Orchowski tabulation declaration and Exhibit A "Comprehensive Final Tabulation" via the CourtListener RECAP mirror of PACER 25-90399, after the Kroll web docket returned 403.

**Qualification that matters more than the headline.** The 90.2% rejection rate fails through **two different prongs that mean opposite things**: on large debtors it is genuine economic opposition failing the two-thirds *amount* test (Brake Parts Inc LLC: 79.45% accepting by number, 19.97% by amount, $2.30B rejecting); on small debtors it is a **tabulation artifact** failing *numerosity* — 1 of 3 ballots accepting despite **99.99997% of amount**, because two ballots carrying **$1.00 voting amounts** voted no. OTTO does not read the 90.2% as a creditor revolt and neither should any consumer of this row.

**Net effect on OTTO-32: none — held 85%.** The plan still routes 111/112 debtors → Ch.7, so both live branches (cramdown-confirm, or confirmation fails and cases convert) deliver majority-Ch.7. What changed is *timeline* risk, not *branch* risk: three trial days produced **no ruling**, and Sep 30 is the resolve date.

**Touches.** `STATUS.md` (First Brands vector rewritten, timeline rows Jul 20/24/27/28-30 swept, BOTTOM LINE), `thesis/PREDICTIONS.tsv` (OTTO-32 note), `docket/CATALYSTS.tsv`, `workbook/ML.tsv` (ML-OTTO-210/211/212/213).

---

### 2026-08-03 — Carvana: the compressing line is the FINANCE line, and OTTO cannot yet say why

**Was → Is.** *Was:* the Carvana sub-thesis held primary evidence that the **collateral** is worse than deep subprime (BLAST CNL 24.67% vs Exeter 16.70%, seasoning-controlled), with no read on whether that reaches the P&L. *Is:* Q2 shows the **finance line specifically** compressing — **Other GPU per retail unit $2,869 → $2,807 → $2,666** across three quarters, accelerating, while Adj EBITDA margin fell **12.4% → 10.4%** on a record quarter. The collateral read and the earnings read now point at the same line.

**Trigger.** SEC 8-K Ex-99.1 filed 2026-07-29, decomposed per-unit rather than taken at the headline.

**What OTTO explicitly does NOT conclude.** Carvana attributes the decline wholly to benchmark rates. **A 10-D reports pool performance, not the economics of the sale** — nothing in OTTO's instrument set separates rate-driven from credit-driven compression. Anyone joining "collateral worse + finance GPU down" into causation is inferring. **Conviction up on the two facts; unchanged on the mechanism linking them.**

**Counter-evidence, recorded.** Retained **beneficial interests in securitizations grew 3.3%** (to $502M) against **38% unit growth** — Carvana is not warehousing a growing residual. And the **market absorbed the guide-down in three sessions** (realized −7.4%, back to −3.6% vs pre-print by 8/3), which is the systemic/repricing leg disconfirming on schedule, consistent with the standing two-leg split.

**Touches.** `STATUS.md` (new Carvana POST-PRINT vector, 2 dashboard rows), `workbook/ML.tsv` (ML-OTTO-216/217/218). No prediction moved — the CARL joint discriminator is owed before any claim is written.

---

### 2026-08-03 — Tricolor: cooperator map goes 1 → 3, and the allocutions are being unsealed

**Was → Is.** *Was:* one named cooperator (ex-COO Goodgame), with OTTO-33's best channel (the TBK syndicate roster) closed as unobtainable. *Is:* **two further cooperators named — Jerome Kollar (25-cr-584) and Ameryn Seibold (25-cr-585)**, both 7-count Informations with indictment waived (Dec 2025), and **Castel ordered their guilty-plea transcripts unsealed on 7/30.**

**Trigger.** SDNY docket sweep of 1:25-cr-00579 (Dkt 115 letter, Dkt 116 memo endorsement) plus the two cooperator dockets.

**Why it moves OTTO-33 60 → 68% and why only that far.** A plea **allocution names counterparties on the record**, and unlike the dead syndicate route it needs no cert-blocked docket and no press — so the *instrument* improved materially. But **neither Kollar nor Seibold scores the claim**: they are individuals, not corporate counterparties, and were first disclosed in **Dec 2025, before the 2026-07-25 window** — known-unknowns newly surfaced to OTTO, the third occurrence of the OBK/TFIN trap. Confidence rises on measurement power, not on evidence.

**Touches.** `STATUS.md` (Tricolor Criminal Track vector), `thesis/PREDICTIONS.tsv` (OTTO-33 60→68%, instrument extended), `docket/CATALYSTS.tsv` (+3 rows), `workbook/ML.tsv` (ML-OTTO-214/215).

---

### 2026-08-03 — OTTO-34 cut 60 → 50% on its first post-creation measurement (arithmetic, not sentiment)

**Was → Is.** Baseline 27.58% → **27.86%** on the 10-D filed 2026-07-30; delta **+0.28pp**, extending the decelerating series .35/.33/.30/.28. Extrapolated over the five remaining filings to December this lands **≈28.96%** — fractionally **under** the 29.0% line.

**Trigger.** Scheduled monthly re-run of `scripts/panel_10d.py`.

**Note.** This is the row working as designed: it was written to straddle 29.0% so it would carry calibration information, and the straddle resolved marginally unfavourable. One 0.35pp month reverses it. **Touches.** `thesis/PREDICTIONS.tsv`, `STATUS.md` (dashboard + predictions block).

---

### YYYY-MM-DD — headline`, then
**Was → Is**, then **Trigger** (what evidence forced it), then **Touches** (which
docs/predictions moved).

---

### 2026-07-25 (session 016, Will-directed) — Carvana sub-thesis gets its first primary-source evidence, two days before earnings — and one piece of it cuts against OTTO

**Was → Is:** the Carvana sub-thesis has been **allegation-only** since it was carved out on Jun 9 — Gotham's Jan 28 report, GT retained, no DOJ action, and **no OTTO primary evidence of its own**. Carried at LOWER conviction for exactly that reason. **Is:** Bridgecrest — Carvana/DriveTime's securitization shelf — is now in the 10-D panel, so OTTO can read Carvana-originated collateral performance directly from trustee reports.

**The finding, seasoning-controlled in both directions:**

| Same vintage | pool factor | 60+ DQ | CNL | ANL |
|---|---|---|---|---|
| EART 2024-1 *(deep subprime)* | 41.80% | 10.26% | 16.70% | 15.92% |
| **BLAST 2024-1 *(Carvana)*** | 37.36% | **15.57%** | **24.67%** | **17.35%** |
| EART 2023-1 *(deep subprime)* | 24.80% | 11.97% | 22.05% | 18.53% |
| **BLAST 2023-1 *(Carvana)*** | 33.51% | **15.20%** | **25.12%** | **19.30%** |

**Carvana's collateral is performing worse than Exeter's deep subprime, same vintage.** 2024: CNL **1.48×** on a pool factor only 4.4pp lower — seasoning cannot produce an 8pp cumulative-loss gap. 2023: Carvana is **less** seasoned and still loses more, so the control works *against* the comparison and strengthens it.

**And Bridgecrest shows the sharpest recent break in the entire panel** — 60+ DQ flat through spring (13.85 → 13.85 → 13.77) then **15.57%, +1.80pp in a single month**; BLAST 2023-1 the same at +1.85pp. Elsewhere single-month moves run +0.4 to +0.9pp.

**⚠ The counter-evidence, recorded because it cuts against OTTO's own thesis.** Bridgecrest **extension rates are LOWER than Exeter's** (3.3-3.9% vs 4.1-5.7%). If the related-party allegation implies Carvana masks delinquency by extending loans — the mechanism the Tricolor indictment describes — **the primary data does not support it.** Carvana extends *less* than a comparable deep-subprime servicer.

**So what moved, precisely:** conviction rises on **collateral quality** — Carvana's book is worse than the market has been told to expect. Conviction does **not** rise on the related-party/reporting-manipulation claim; on the extension channel it arguably falls. **Worse underwriting or borrower mix is not reporting fraud, and OTTO should not let a real finding on the first question be read as support for the second.**

**Timing:** CVNA reports Q2 **Wed Jul 29 after close**, with the stock −14.4% off its Jul 16 high and Gotham's precedent of dropping reports on earnings day. TRADE.md remains FROZEN — this is a watch, not a position.

**Touches:** `scripts/panel_10d.py` (3rd issuer spec — Bridgecrest uses paren footnotes, dollar-only DQ buckets, a stated 60+ figure at line 55, CNL derived off line 14), `workbook/PANEL_10D.tsv` (64 rows), STATUS (new Carvana vector, timeline archive pass), `workbook/ML.tsv` ML-205/-206/-207.

---

### 2026-07-25 (session 016, Will-directed) — Summer re-deterioration CONFIRMED on an instrument OTTO built itself; the "deep bleeds, broad is fine" framing weakens

**Was → Is:** the summer re-deterioration in subprime auto credit was OTTO's **expectation, untested**. Fitch's obtainable data stopped at **March 2026** (a seasonal tax-refund low), so every read since has been "unobserved, not disconfirmed" — a phrase this session used repeatedly and correctly. **Is: observed and confirmed.**

**Trigger:** Will asked whether the Fitch gap could be fixed. S&P and KBRA were tested and found closed (403 / paid). So OTTO built a **fixed panel of 7 named deals** parsed from SEC 10-D Exhibit 99.1 — the same primary documents the rating agencies aggregate.

**The result, from the first real run:**

| | trough → latest 60+ DQ | off trough |
|---|---|---|
| EART 2022-2 (DEEP) | 13.23 → **14.79%** | +1.56pp |
| EART 2022-3 (DEEP) | 12.27 → **13.59%** | +1.32pp |
| EART 2023-1 (DEEP) | 10.71 → **11.97%** | +1.26pp |
| EART 2024-1 (DEEP) | 9.37 → **10.26%** | +0.89pp |
| SDART 2022-6 (BROAD) | 8.88 → **10.45%** | +1.57pp |
| SDART 2023-1 (BROAD) | 8.62 → **9.96%** | +1.34pp |
| SDART 2024-1 (BROAD) | 7.78 → **9.19%** | +1.41pp |

**7 of 7 deals, both tiers, four vintages — troughed in spring, risen every month since, all now above their first observation.**

**The thesis-level wrinkle, and it cuts against OTTO.** Since s015 OTTO has framed the subprime picture as *deep-subprime bleeds while broad subprime holds up* — supported by Ally's five straight improving quarters and the 2.3× CNL tier split. The panel confirms the **level** gap (ANL 18.85% DEEP vs 6.41% BROAD, ~2.9×) but shows **broad subprime is not insulated**: off-trough it has risen slightly *faster* than deep (mean +1.44 vs +1.26pp; BROAD's slowest deal, +1.34pp, still beats DEEP's mean), while in the latest month deep is marginally faster (+0.61 vs +0.46pp). **Level bifurcation is intact; rate-of-change bifurcation is not — the tiers are deteriorating at comparable speed.** *(Refined 2026-07-25 after deduping the ledger; the first pass read off-trough only and stated the case one-sidedly.)* That is a genuine qualification of OTTO's own framing and should temper any "it's contained to deep subprime" read.

**Second-order:** the DQ gap between tiers (1.3×) is far narrower than the loss gap (2.9×) — deep subprime converts delinquency into loss much faster, consistent with recoveries of 21.8-30.9% and falling on the 2022 vintages (EART 2022-3: 28.89 → 21.83% across Mar-Jun filings).

**Method note worth keeping:** the missing instrument turned out to be one parser away, inside documents OTTO was already reading for OTTO-04. The lesson generalises past this metric — **before accepting a data wall, check whether the primary documents already in hand contain the field.**

**Touches:** `scripts/panel_10d.py` + `workbook/PANEL_10D.tsv` (new), STATUS (3 new dashboard rows, boot-pointer, BOTTOM LINE), `workbook/ML.tsv` ML-201/-202/-203/-204, MAINTENANCE (instrument build + 4 parser defects).

---

### 2026-07-25 (session 016, Will-directed) — OTTO-04 metric re-based to the deep-subprime 10-D tranche; the prediction was RETIRED rather than re-scored

**Was → Is:** OTTO-04 ("2022 vintage CNL >25% by Sep 30") resolved on the **Fitch blended subprime index** — a convention Will ratified 2026-07-04 when the only known problem was composition bias. **Is:** the canonical 2022-vintage measure is now the **deep-subprime 10-D tranche** — `Cumulative net loss ratio` for **EART 2022-2 / 2022-3**, pulled directly from SEC EDGAR.

**Trigger:** new information since the July ratification — the blended index is not merely biased, it is **unobtainable**. OTTO has no Fitch-direct access; the Auto Remarketing/AFN free mirror has decayed to where its newest indexed piece still covers the *January* index. Latest usable data: **March 2026**. Two consecutive WINTERKORN runs failed to verify a release.

**The metric change is right, and it is not the interesting part.** The deep-subprime tranche is what the thesis actually cares about, it is primary-source, and it is retrievable on demand. Full series now on file `[CONF SEC 10-D]`: **EART 2022-3** 25.21 → 25.53 → 25.90 → 26.27 → 26.60 → 26.95 → 27.28 → **27.58%** across the Dec-2025 → Jun-2026 filings, monthly deltas **decelerating .37 → .30pp**; **EART 2022-2** 24.23 → **26.34%**, .33 → .26pp.

**The interesting part: the prediction could not follow the metric.** OTTO-04 was made **2026-02-23**. On the re-based measure, **EART 2022-3 was already at 25.90%** (10-D filed 2026-01-28) and 2022-2 crossed 25% within days (25.22%, filed 2026-03-03). **The re-based claim was true-at-creation — zero forecasting content.** Scoring it CONFIRMED would have converted a likely-miss into a hit; it is the OTTO-30 known-unknown trap running in reverse.

**Disposition:** OTTO-04 **RESOLVED EARLY (2026-07-25)** as **FALSIFIED-on-metric / CONFIRMED-on-substance** (the OTTO-29 convention Will ratified Jul 4), with **no calibration credit taken**. Resolving early is correct because both metrics now have determinate answers — nothing is learned by holding it to Sep 30. Forward replacement opened: **OTTO-34** — *EART 2022-3 CNL ≥29.0% on the 10-D filed December 2026*, 60%, deliberately near-coin-flip, instrument and parse-recipe named in-row.

**The rule this establishes, which generalises past OTTO:** *when you re-base an open prediction's metric, test whether the new metric was already satisfied at the original Made_Date. If it was, the prediction is not re-based — it is retired, and a fresh forward claim replaces it.* Recorded in `PREDICTIONS_ARCHIVE.md` § credit note.

**What is genuinely still open:** OTTO-04's substance was never in doubt after s015. What has never been tested is **where deep-subprime 2022 terminates** — a ~29-30% grind versus a ~28.5% plateau. That is what OTTO-34 measures, and the observed deceleration (.37 → .30pp/mo) is what makes it a real question.

**Touches:** `thesis/PREDICTIONS.tsv` (OTTO-04 resolved + OTTO-34 created), `thesis/PREDICTIONS_ARCHIVE.md` (scoreboard 5/7 → 6/8 + credit note + the transferable rule), STATUS (§ PREDICTIONS, dashboard CNL row re-based, timeline), `docket/CATALYSTS.tsv` (2026-09-01 decision row closed ~5 weeks early).

---

### 2026-07-25 (session 016, RP-OTT-1.6) — "The books looked clean" stops being an inference and becomes a documented mechanism

**Was → Is:** The Invisible Exit's central claim is that a fraud lender's book *looks clean until the moment it collapses*. Until now OTTO supported that with outcome evidence — 30K missing vehicles, ~3% recovery, a Vervent mod program — i.e. **inference from how it ended**. **Is:** the mechanism is now documented at the point of control. All **eleven** Tricolor securitizations (2018-2025) carry a third-party agreed-upon-procedures report, and those procedures compare the securitization data tape **to Tricolor's own servicing and origination systems** — the systems the superseding indictment alleges were falsified. *"We compared Characteristics 8. through 12. to … the Servicing System Screen Shots"* (Deloitte). **A tape derived from a doctored source agrees with it by construction.**

**Trigger:** `[CONF SEC EDGAR]` — all 11 Form ABS-15G filings + 12 Exhibit 99.x AUP reports, depositor CIK 0001757871. Commissioned by Will as Tier 1 of the 2018-2021 vintage thread.

**Why it's thesis-level:** it converts the Secondary thesis's weakest link — *why did nobody notice for seven years?* — from a plausibility argument into a structural one. An AUP is a **reconciliation, not an audit**; it is not designed to test whether the originator's records are true. Three major firms (Crowe → Deloitte → Grant Thornton) each produced accurate reports that were, against this fraud, uninformative. Double-pledging is likewise outside scope: lien documents are checked, but on **150 of ~10,000 loans (1.5%)**, and confirming Tricolor's own lien is not a search for competing pledges. **No procedure inspects a vehicle.**

**Also retires a lead — my own, from earlier the same session.** I had headlined "2018-2021 vintages implicated." Tricolor securitized **two** deals in that window (TAST 2018-2, 2021-1) with a **32-month gap**; **nine of eleven** are 2022-2025. The 2022-centric frame was right. Corrected in STATUS, CHANGELOG, and NEXUS_BRIEF — the last of which had already gone out with the wrong gloss.

**Reusable output:** a 144A subprime shelf's ABS-15G/Exhibit 99.1 is its one public trace. Four cheap diagnostics now defined — *what is the tape compared against; who chose the sample; how large relative to the pool; has the provider rotated* — applicable to CPS, Flagship, Lendbuzz, SAFCO, GCAR.

**Touches:** `research/outputs/RP-OTT-1.6_Tricolor_ABS15G_Diligence_Forensics.md` (new), `workbook/ML.tsv` ML-195/-196/-197/-198, STATUS (BOTTOM LINE + criminal-track vector + 2018-2021 correction), NEXUS_BRIEF (retraction + new mechanism line), RESEARCH_STATUS index. No prediction moved.

---

### 2026-07-25 (session 016) — 🔴 DOJ has criminally charged BOTH of OTTO's thesis mechanisms; Invisible Exit escalates from inference to indictment

**Was → Is:** The Primary (Cockroach/double-pledging) thesis rested on bankruptcy-estate evidence and the Dec-2025 indictment's *bank-fraud* framing. The Secondary (Invisible Exit) thesis — that the immigrant subprime cohort skip-defaults in a way that **bypasses the 30→60→90 DQ chain**, which is why fraud-lender books look clean until collapse — was OTTO's own **inference from data**, explicitly the weaker leg (MEDIUM-HIGH, "structurally validated" only by the Tricolor 30K-missing-vehicles / Vervent Fresh Start evidence).

**Is:** a **superseding 8-count indictment** unsealed **2026-06-24** against founder Daniel Chu charges, as criminal conduct, that Tricolor executives *"manipulated delinquent loan data to make non-performing loans appear current"* **and** *"pledged the same collateral to multiple lenders simultaneously"*, plus fictitious payment records and falsified borrowing-base reports. **Both legs of OTTO's thesis are now federal criminal allegations, not OTTO inferences.**

**Trigger:** `[CONF DOJ/SDNY via Reuters, Bloomberg, NatLawReview, Barnes & Thornburg]` — surfaced 2026-07-25 during the 21-day catch-up sweep. **It happened Jun 24, ten days before OTTO's Jul 4 session, and was missed then too.**

**Three escalations, in order of importance:**
1. **The Invisible Exit mechanism is charged.** "Making non-performing loans appear current" is precisely the DQ-chain bypass OTTO modelled. This is the strongest available validation short of conviction, and it should move the Secondary thesis's conviction up — it is no longer OTTO's private read of anomalous data.
2. **"Continuing financial crimes enterprise from at least 2018."** The alleged fraud ran **seven years** before collapse, so **originations** were tainted from 2018. ~~The indictment implicates 2018-2021 vintages, widening the impaired-collateral window materially.~~ **⚠ CORRECTED same day by RP-OTT-1.6:** that was overstated. Tricolor securitized only **two** deals in 2018-2021 (TAST 2018-2, 2021-1, with a 32-month gap); **nine of eleven** deals are 2022-2025. The securitized-collateral window did **not** widen materially, and the phrasing could have been read as *industry-wide* 2018-2021 vintage impairment, which does not follow from the indictment at all. **Lead retired; the wording was the error, not the indictment.**
3. **The statute is the tell on DOJ's own conviction.** DOJ invoked **18 U.S.C. § 225 (CFCE, the "financial kingpin" statute)** — mandatory minimum **10 years to life**, used a handful of times since the S&L crisis and not at all in over a decade. Prosecutors do not revive a dormant mandatory-minimum statute for a marginal case. Charges roughly doubled vs. the December original. Chu pleaded **not guilty 2026-06-30**.

**Fourth, separately dated:** former COO **David Goodgame pleaded GUILTY 2026-06-24** to six counts (bank/wire/securities fraud, conspiracy, false statements) and is **cooperating** against Chu — a flip from his Jan-2026 not-guilty plea. **This fires OTTO's standing outbound trigger** ("cooperating witness reveals new fraud/participants" → CARL, REGINALD, 🟠 ELEVATED). A cooperating COO is the highest-value fraud-surface-expansion vector available; expect new counterparties to surface through his proffer.

**Calibration note — this is a coverage failure, not a lucky find.** Four Tricolor criminal-track developments (Jun 24 superseding indictment, Jun 24 Goodgame plea, Jun 30 arraignment, Jul 7 trial re-date) all landed in a window OTTO was nominally awake for on Jul 4, and none were caught. The Jul 4 session swept *bankruptcy* dockets and *ABS* data but did not sweep the **criminal** track — which WINTERKORN's spec explicitly scopes as "selective: trial date + cooperator motions only." That scoping was too narrow: it treated the criminal case as a date-keeping problem when it is a *fraud-surface-discovery* channel.

**Touches:** STATUS (THESIS mirror, dashboard, ACTIVE VECTORS, CRITICAL TIMELINE), `workbook/ML.tsv` ML-191/-192/-193/-194, `thesis/THESIS.md` (conviction on Secondary — **owed, see LAST_COMPLETION gaps**), WINTERKORN spec scope (**owed**), cross-agent trigger to CARL/REGINALD.

---

### 2026-07-25 (session 016) — Double-pledge mechanic confirmed in a THIRD collateral class (floorplan/inventory)

**Was → Is:** OTTO tracked Tricolor's double-pledging across two collateral layers — the ABS warehouse (29,000 double-pledged loans) and the receivables layer ($113M disputed-ownership escrow). **Is:** a third layer is now primary-sourced — **floorplan/vehicle inventory**. TBK Bank (Triumph Financial) is agent on a $60.5M Tricolor floorplan facility holding ~$22.5M on a claimed *first-priority* interest in vehicle inventory, while its own 10-Q concedes "other creditors have asserted that they have interests in some of the collateral."

**Trigger:** `[CONF SEC 10-Q, TFIN CIK 0001539638, filed 2026-07-21]`, found via complete EDGAR full-text scan.

**Why it's thesis-level, not a dashboard row:** the Cockroach thesis claims fraud, once found, is broader than first disclosed. Each additional *collateral class* touched by the same mechanic is independent confirmation that Tricolor's double-pledging was systemic to the business model rather than confined to the securitization channel. It also opens a new discovery surface: **~$38M of the syndicate is held by unnamed participants.**

**Second-order:** TBK carries the $22.5M **unreserved** 9.5 months post-Ch.7 on an "adequately secures" assertion, against inventory where OTTO's own data shows ~30,000 vehicles missing and ~3% realized recovery. Loss-recognition lag is itself now a tracked mechanic (same shape as the $113M escrow: *banks cannot book losses cleanly even when substance is clear*).

**Touches:** STATUS (new ACTIVE VECTOR + 3 dashboard rows + timeline), `workbook/ML.tsv` ML-184, NEXUS_BRIEF (new REGINALD send-row), WALTER signal `SIG-OTTO-WALTER-20260725-tricolor-floorplan-tfin`. No prediction moved — this is new surface, not a resolution.

---

### 2026-07-25 (session 016) — Two predictions downgraded hard on primary evidence; the failure mode is measure-design, not luck

**Was → Is:** OTTO-30 **45% → 12%**; OTTO-31 **30% → 12%**.

**Trigger — OTTO-30:** a *complete* EDGAR full-text scan (all operating-company forms mentioning "Tricolor", 2026-04-15 → 07-25) returned **zero new US bank names**. Every in-window filer disclosed before the window opened. **Trigger — OTTO-31:** MTB Q2 (Jul 15) posted record EPS $5.32 vs $4.66 est with no wind-down language and active promotion of Wilmington's custody franchise — a second corporate-side disconfirmation.

**The pattern worth naming.** With OTTO-26 (right direction, wrong date), OTTO-29 (confirmed-on-substance, falsified-on-window), OTTO-04 (deep-subprime substance confirmed, blended-index metric may miss) and now OTTO-30, **four of OTTO's claims have failed or are failing on how the claim was *measured* rather than on whether the world moved as expected.** OTTO-30 is the cleanest case: it asked "does a 6th bank *disclose*" — but a bank that disclosed in Sept 2025 and was never *found* is indistinguishable, from OTTO's side, from one that never disclosed. The prediction measured OTTO's own discovery latency, not the world. **Both times OTTO's named-bank list was found incomplete (OBK, now TFIN), the cause was press-sampling rather than complete scan.**

**Corrective adopted:** discovery-type claims must specify the *instrument* (complete EDGAR FTS, not press monitoring) and a pre-registered re-check. OTTO-30 now carries one: re-run the identical query 2026-08-15; still zero → FALSIFIED.

**Touches:** `thesis/PREDICTIONS.tsv` (OTTO-30/-31 confidence + notes), STATUS § PREDICTIONS, MEMORY (finding), auto-memory candidate.

---

### 2026-07-25 (session 016) — OTTO-32 resolution mechanics reframed (confidence held at 85%)

**Was → Is:** Jul 28 was carried as a same-day resolver ("plan confirmed = OTTO-32 CONFIRMED early"). **Is:** Jul 28 is the **opening of a multiday contested confirmation trial** — creditors sought further production on the litigation claims at the plan's core, the court is weighing privilege issues pre-trial, and every plan revision has drawn "a wall of objections" including the UST `[PRESS Law360/Octus/TT]`.

**Trigger:** T-3 pre-hearing verification pass.

**Why it matters even though confidence didn't move:** the *substance* (111/112 debtors → Ch.7) is unchanged and the Sep 30 window stays comfortable — but anything scoring OTTO-32 off a Jul 28 headline would misread a process readout as a verdict. **Catalyst-date ≠ resolution-date** (auto-memory `[[finding_catalyst_vs_consequence_conflation]]`).

**Also newly surfaced:** debtor suits vs Patrick James + Onset Financial seek **>$2.7B** and are **stayed** pending the criminal case; Lopez ordered a criminal-proceedings status update by **Jul 13** — a dated node that was never on OTTO's docket.

**Touches:** `thesis/PREDICTIONS.tsv` OTTO-32 notes, STATUS (§ PREDICTIONS, CRITICAL TIMELINE, BOTTOM LINE), `docket/CATALYSTS.tsv`.

---

### 2026-07-04 (session 015) — 2022-vintage CNL is bifurcated by tier; OTTO-04's blended-index metric decoupled from the substance
- **Was:** OTTO-04 ("2022 vintage CNL >25% by Sep 30") tracked as a single blended Fitch subprime-index number (22.42%@31mo) "in striking distance" of 25% (68% after the spring seasonal nudge). The 2022-vintage *magnitude* question and the *index-metric* question were treated as one.
- **Is:** Primary-source 10-D pull `[CONF SEC 10-D]` shows the "2022 vintage" is bifurcated **~2.3x by credit tier** at identical ~44-48mo seasoning — DEEP subprime (Exeter EART 2022-3 **27.58%** / 2022-2 26.34%) is already well past 25% and grinding to ~28-29% terminal, while BROAD subprime (Santander SDART 2022-6 **12.08%**) is nowhere near. The Fitch blended index is a composition-weighted average between, anchored DOWN by Santander's dominant $2B+ low-CNL deals. **So the thesis-relevant SUBSTANCE (deep-subprime 2022 impairment) is CONFIRMED >25% by primary source, but the blended-index METRIC OTTO-04 resolves on may NOT cross 25%** — a metric-falsification would not be a substance-falsification (same shape as OTTO-29/-26 falsified-on-window / confirmed-on-substance). Both tiers are DECELERATING into summer with no post-tax-season re-acceleration in the May-collection prints; the Fitch "May print" carries only March data (2mo lag), so the index hasn't turned either. OTTO-04 nudged **68→62%** on the composition drag.
- **Trigger:** session-015 primary-source EDGAR 10-D pull (EART 2022-2/-3, SDART 2022-6, May-2026 collection filed Jun-2026) + Fitch print sourcing (AutoRemarketing May 21 2026 = March data). Closed the standing "EDGAR 10-D blocked" tooling gap (403 = missing User-Agent header).
- **Touches:** OTTO-04 68→62% (PREDICTIONS.tsv + STATUS dashboard & predictions rows); STATUS 2022-CNL row rebuilt by-tier + Fitch DQ/ANL/recovery rows re-stamped with data-month; ML-182/-183. Applies auto-memory `[[finding_blended_index_masks_bifurcation]]` + `[[finding_decouple_idiosyncratic_from_systemic_leg]]` + `[[finding_measure_actionable_not_gross_rate]]`. **Resolved (Will-ratified Jul 4):** OTTO-04's canonical measure STAYS the blended index; a Sep-30 miss resolves falsified-on-window / confirmed-on-substance (deep-subprime tranche already >25% — OTTO-29 convention). Convention recorded in PREDICTIONS.tsv OTTO-04 Notes.

### 2026-07-04 — Systemic subprime-ABS funding-freeze sub-thread DISCONFIRMED (OTTO-05 falsified)
- **Was:** OTTO carried a systemic funding-stress leg alongside the fraud-pattern leg — the expectation that subprime auto ABS spreads keep widening (OTTO-05: BBB >250bps by Jun 30), with dealer reluctance to print below-IG framed as a market-freezing signal. Composite severity ran 🔴🔴.
- **Is:** The funding-freeze sub-thread is **disconfirmed.** Subprime BBB ABS spreads **TIGHTENED to +140bps** (EART 2026-3, settled ~Jun 24) from +190 in Mar; the deal **upsized to $1.2bn** and Exeter earned its **first-ever AAA** — a market that is open, deep, and repricing tighter, not freezing. Ally (near-prime) credit is *improving* (NCO/DQ down YoY, 4 straight quarters). **The fraud-pattern leg (Tricolor recovery ~3%, First Brands → majority Ch.7) is intact and idiosyncratic; it is NOT transmitting into a broad subprime-ABS repricing.** Composite downgraded 🔴🔴 → 🔴 fraud-leg / 🟠 systemic-funding-leg. The two legs must be kept distinct: cockroach fraud-discovery ≠ systemic funding stress.
- **Trigger:** Jul 4 catch-up sweep of the Jun 30 prediction resolve — EART 2026-3 direct primary print (+140bps BBB) `[CONF SEC FWP/IFR]`; Ally Q1 credit metrics + Jul 21 earnings timing.
- **Touches:** OTTO-05 FALSIFIED; OTTO-28 FALSIFIED-on-window; OTTO-04 nudged 75→68% (seasonal); STATUS signal-status 🔴🔴→🔴/🟠 + dashboard ABS rows; ML-177/-179. **Follow-up ✅ DONE (Jul 4, THESIS v1.1):** updated `thesis/THESIS.md` — conviction-decomposition (Magnitude leg split into idiosyncratic-fraud-recovery HIGH vs systemic-funding LOW) + transmission chain (stage 3/7 + critical observation) + why-now driver 2 (reversed) + risk matrix + break condition + calibration scoreboard. Fraud-pattern predictions (OTTO-01/-29/-32) unchanged in substance.

### 2026-06-09 — Carvana carved out as separate-conviction sub-thesis (v1.0 THESIS introduction)
- **Was:** Carvana bundled in the Primary Cockroach case table at equal weight to the 4 confirmed cases (Tricolor / First Brands / MFS / PrimaLend). STATUS § THESIS showed all 5 rows in one table; conviction implied uniform on the pattern.
- **Is:** Carvana is a **separate sub-thesis with explicit LOWER conviction.** Reasons: (a) allegation-only — no DOJ indictment, no SEC action, no auditor resignation; (b) GT ratified May 5 (disconfirms the "GT resigns" red-line trigger); (c) governance vote 96% against separation = thesis-confirming on related-party concern but not the Cockroach archetype; (d) insider signal mixed (CFO selling vs RSU withholding); (e) William Blair June conviction list = bull offset; (f) no short-seller activity Mar 15–Jun 8 (Gotham/Hindenburg/MW silent — mild evidence the thesis isn't ripening). **Cockroach case count is now 4 confirmed, not 5.** Carvana re-enters the Primary table only if Jun 12+ discovery surfaces specific manipulation evidence.
- **Trigger:** thesis/THESIS.md v1.0 introduction (Jun 9) forced the bundling question. Carving out is the substantive change; the folder consolidation is the structural one.
- **Touches:** thesis/THESIS.md v1.0 dedicated CARVANA SUB-THESIS section + decomposed-conviction footer ("Carvana sub-thesis: LOWER"); STATUS § THESIS reframed (4 confirmed + 1 alleged carve-out). No prediction-confidence move on the existing OTTO-NN rows.

### 2026-06-09 — Tricolor §341 resolution-slip past Sep 30: modeled-likely → concrete
- **Was:** OTTO-29 Tricolor distribution-plan resolution-slip past Sep 30 was *modeled likely-slip* (no plan filed May–Jun per STATUS).
- **Is:** **Concrete.** WINTERKORN inaugural pre-fire verification (Jun 9) caught a Verita-noticed §341 continuance to **Nov 11 2026**. The Jun 17 §341 meeting itself happens but is already noticed-continued; distribution-plan filing slips past the Sep 30 OTTO-29 resolve by docket-confirmed action, not projection. Substance call unchanged (Tricolor recovery near-zero); only the resolution-window assertion firmed.
- **Trigger:** WINTERKORN sub-agent inaugural run (Jun 9, T-3 pre-hearing verification) caught it. The catch is exactly the value-prop the sub-agent was built to deliver (the canonical Jun 17→Jun 12 failure mode, made cadence-driven).
- **Touches:** STATUS CRITICAL TIMELINE (Jun 17 row reframed; new Nov 11 row added); CATALYSTS.tsv (Jun 17 Tricolor row date_class modeled→confirmed + Nov 11 row added); OTTO-29 substance sharpened (Notes-column refresh pending — date stays Sep 30).

### 2026-06-08 — ABS structural claim falsified + OTTO-05 recalibrated (data refresh)
- **Was:** Subprime ABS market "IG-only — BB/single-B tranches not clearing" (structural 🟠); BBB spread extrapolated ~200-235bps; OTTO-05 (BBB >250 by Jun 30) at 62%.
- **Is:** **Below-IG IS clearing** — Exeter EART 2026-2 placed BB- (+380) and single-B (+320) tranches publicly (Mar 20, SEC FWP). Direct BBB print **+190bps** (EART Class D) sits *below* the extrapolation. OTTO-05 dropped 62 → 48% (needs +60bps in 3wk absent a fresh catalyst). "IG-only" claim retired.
- **Trigger:** Jun 8 dashboard data-refresh sweep — primary-source SEC FWP for EART 2026-2 superseded OTTO's hand-extrapolated spread levels.
- **Touches:** OTTO-05 (62→48%); STATUS SIGNAL DASHBOARD (3 spread rows); issuance row 🟠→🟢-reframed. Calibration note: OTTO had been over-extrapolating BBB off A-rated + a too-wide BBB-over-A premium.

### 2026-06-08 — First Brands OTTO-32 resolver: Jun 17 → Jun 12
- **Was:** OTTO-32 (First Brands majority Ch.7) resolver = Jun 17 plan-confirmation hearing.
- **Is:** Operative resolver is the **Jun 12 UST convert-or-dismiss hearing** (10am CT, §1112(b)). May 20 DS denied (entanglement + <14d creditor review + admin-insolvency); Jun 17 confirmation is now *contingent on surviving Jun 12*. Conviction unchanged (85%) — only the resolver date/mechanism moved earlier.
- **Trigger:** Jun 8 catalyst-prep sweep (Law360 #2482099 / Octus) — surfaced the §1112(b) hearing OTTO's timeline had folded into "Jun 17."
- **Touches:** OTTO-32 Notes; STATUS CRITICAL TIMELINE + signal-trigger; CATALYSTS.tsv (new Jun 12 row, Jun 17 re-characterized).

### 2026-06-02 — First Brands Ch.7: IN MOTION → ADVANCING
- **Was:** Ch.7 conversion "in motion" (US-Trustee dismiss-or-convert motion filed May 13).
- **Is:** Mechanism **advancing** — 4 Evolution SPV debtors already converted (Apr 9 Lopez order); PMG plan routes all other 111 debtors to Ch.7; May 20 conditional-DS approval DENIED on admin-insolvency grounds (the denial basis = UST's outright-conversion argument, so it cuts *toward* thesis). Confirmation re-targeted Jun 17.
- **Trigger:** First Brands docket sweep (Jun 2) — Law360 / CreditSights cleared the auth-gated Kroll docket.
- **Touches:** OTTO-32 held 85%; STATUS CRITICAL TIMELINE; ML-OTTO-171.

### 2026-05-22 — Wilmington Trust: franchise-exit thesis collapses to narrow Tricolor resignation
- **Was:** 🔴🔴 "Wilmington exiting its entire non-mortgage ABS custodial business" (billions in ABS); OTTO-31 opened 60%.
- **Is:** 🟠 narrow — only the **Tricolor-specific** indenture-trustee resignation (Sep 20 2025) is corporate-confirmed. Full-exit allegation **denied corporate-side** (American Banker, M&T anon source: unit "is accepting new clients") + active-business evidence (#2 US ABS/MBS trustee 1H 2025). OTTO-31 dropped 60 → 30%.
- **Trigger:** May 22 PM corporate-side sweep. Plaintiff allegation = litigation rhetoric, not franchise exit.
- **Touches:** OTTO-31 (60→30%); STATUS active vectors (split into Wilmington-narrow + successor-vacuum rows); auto-memory `[[finding_refresh_not_retire_perentity_profiles]]`-adjacent calibration lesson (weight `[ALLEG]` ≤40%).

### 2026-05-21 — Tricolor recovery: deadline + magnitude corrected
- **Was:** Vehicle-sale deadline Apr 30 (per Apr 15 recalibration); recovery outcome open.
- **Is:** Operative deadline was **Mar 31** (no extension); auctions ran; ~3% recovery projected (5,857 vehicles / $39.5M net); **~30K vehicles missing, up to $1.1B** (Invisible Exit at industrial scale); $113M distribution gridlock = new transmission mechanic.
- **Trigger:** May 21 sourced docket + AFN auction-proceeds reporting superseded the Apr 15 recalibration.
- **Touches:** OTTO-29 raised to 80% (substance) but flagged resolution-at-risk; STATUS dashboard + thesis blocks; ML-OTTO-145 supersedes ML-OTTO-140.

### 2026-04-15 — Recovery-signal metric reframed: vehicle proceeds → ABS note price
- **Was:** "Recovery outcome" framed around vehicle auction proceeds ($125M cost-basis ceiling).
- **Is:** The signal-rich metric is **ABS note market price** (already <10¢ on the dollar = >90% implied noteholder loss), not vehicle proceeds. The question was mis-framed.
- **Trigger:** Apr 15 Tricolor recovery deep-dive; Will wanted the reframe said plainly before the data.
- **Touches:** Cockroach magnitude strengthened; Invisible Exit structurally validated.

---

*Seeded 2026-06-08 from STATUS/MEMORY trajectory at CHANGELOG introduction. Pre-2026-04 pivots not backfilled — reference STATUS archive + ML.tsv if needed.*

## 2026-08-27 (s020) — Carvana sub-thesis: the headline mechanism number was over-scoped by OTTO and is retired

**Was:** *"Bridgecrest services $26B at 0.117% fee (below market). Low fee enables inflated loan sale prices."* — carried as **fact**, with no `[EST]` tag and no attribution, in `CLAUDE.md` § Fraud Mechanisms, `THESIS.md` § Carvana Claim, `VX-OTTO-008`, `RP-OTT-3.1`, `RP-OTT-4.1` and `RESEARCH_STATUS`.

**Is:** the claim is re-scoped to Gotham's own perimeter and OTTO's restatement is **refuted**. Gotham wrote *"we **estimate** Bridgecrest earns a very low servicing fee of 0.117% per year **on loans sold by CVNA to 'Third parties'**"* — an `[EST]` on **third-party whole-loan sales**. OTTO widened it to the entire **$26B managed portfolio**, which contains the ABS trusts. `[CONF SEC 424B5]` **BLAST 2024-1's disclosed base servicing fee is 3.50%/yr** — vs **SDART 2024-1 3.00%** and **Drive 2019-3 4.00%**. **At the ABS level Bridgecrest is at market**, sitting between Santander's broad and deep shelves exactly where its collateral quality sits.

**Trigger:** Will supplied a popular-media video (*The Infographics Show*, "The Next Great Recession Isn't Housing") whose Santander/Drive 2019-3 section prompted a servicing-fee pull. **The video's own systemic claims are largely wrong** — its "30%+ of subprime auto loans defaulting" is refuted by OTTO's panel (broad ANL 5.69-6.15%, deep 14.97-20.86%) and it attributes Tricolor's fraud collapse to the truck cycle. **The lead was still worth running: a bad artifact pointed at a real document.**

**Conviction effect: NO fall on related-party manipulation.** The claim was never load-bearing on the ABS perimeter, so refuting OTTO's over-scoped restatement removes a *bad argument for* the thesis, not evidence for it. What it removes is OTTO's ability to assert a below-market fee from anything filed. **Symmetrically:** if Gotham's estimate holds on its own perimeter, it is **26-34× below what the same servicer charges for identical work on its own trusts** — a sharper benchmark than any external peer set, and undecidable without private whole-loan agreements.

**🔴 The larger find, same pull — and it cuts against OTTO.** *"Supplemental Servicing Fees"* is defined **identically in all three shelves** as *"(i) late fees, **(ii) extension fees**, (iii) non-sufficient funds charges and (iv) any and all other administrative fees,"* **all retained by the servicer.** So the party granting an extension is **paid** to grant it — extensions are a revenue line, not only a masking lever. **But the clause is industry-standard boilerplate present in Santander's shelves too, so a high extension rate is not evidence of intent by itself.** This weakens any inference OTTO might have drawn from extension levels alone, and it is recorded because it points away from the thesis.

**Touches:** `CLAUDE.md` § Fraud Mechanisms · `thesis/THESIS.md` (v1.4 → **v1.5**, Claim + What-would-resolve) · `STATUS.md` (2 dashboard rows + thesis pointer) · `RESEARCH_STATUS.md` (HIGH item closed, ~6 months open) · `workbook/ML.tsv`. **NOT touched:** `workbook/VX.tsv` — FROZEN 2026-07-04, correcting one row inside a frozen ledger would imply the other 87 are maintained.

