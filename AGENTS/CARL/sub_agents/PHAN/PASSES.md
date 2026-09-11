# PHAN PASS LOG — dated ad-hoc pass narratives

> ⛔ **GREP THIS FILE, DO NOT READ IT WHOLE.** Split out of `DOSSIER.md` on **2026-09-11** under the read-cap remedy: the dossier had reached **41,078 B against the 32,550 B whole-read cap (126%)**, and the dated pass narratives were **14,827 B (36%) of it** — they grow by one section per pass while the durable assets (§1–§9) do not. On grep terms this file carries **no read-cap budget claim** (`READ_CAP.md` rule-8 mode ruling, same basis as CARL's `ROADMAP_THREADS.md` and `board_log.tsv`).
>
> **How to use it:** `DOSSIER.md` carries the CURRENT STATE block and the durable frameworks; come here only for the reasoning of a specific dated pass — `grep -A20 '2026-09-11 pass' AGENTS/CARL/sub_agents/PHAN/PASSES.md`.
>
> **Newest first.** Each section is the record of what that pass concluded **at that date** — including conclusions later superseded, which are tagged in place rather than deleted. A superseded call is evidence about the desk's calibration and is deliberately retained.

---

## 2026-09-11 pass (3rd ad-hoc, +1d) — the three SEARCH-NOT-FOUND gaps from 9/10, all closed

*Purpose of this pass: the 9/10 pass shipped with three named unreachable primaries. All three were fetch failures, not absences — retried 9/11 and all three resolved. **Two of the three moved a call, and one of those moves is against yesterday's own conclusion.** Predictions: one moved (P03), none resolved — CARL disposes (§8.4).*

### ① 🔴 FLOW-PHAN-06 RESTORED to ACTIVE — yesterday's downgrade was a period-basis error

The 9/10 pass could not reach Affirm's FQ4 earnings supplement (two timeouts; a third on 9/11) and fell back to the 10-K's fiscal-year aggregates, concluding **provision +29.2% < GMV +37% ⇒ trigger PARTIAL**. That arithmetic is right and the conclusion drawn from it is wrong: **FLOW-PHAN-06's trigger was authored on QUARTERLY provision growth** (the Apr-2026 sentence cites "Affirm +40% YoY provisions"), and the FY aggregate is dragged below the bar by a single flat quarter.

Rebuilt from SEC XBRL primaries — **the 10-Qs and the 10-K, differenced** (FY − 9-month = Q4), so no secondary is load-bearing:

| Qtr (FY26) | Provision | YoY | NCOs | YoY |
|---|---|---|---|---|
| Q1 | $162.8M | **+1.8%** | $127.5M | +12.6% |
| Q2 | $214.2M | **+40.0%** | $155.9M | +16.5% |
| Q3 | $196.5M | **+33.5%** | $158.0M | +22.2% |
| **Q4** | **$223.2M** | **+42.5%** | **$170.2M** | **+36.9%** |
| FY26 | $796.7M | +29.2% | $611.6M | +22.1% |

**Three consecutive quarters above the >30% bar, and Q4 provision +42.5% against Q4 GMV +36% — provision outpacing volume by 6.5pp on the most recent quarter.** ⭐ **The NCO column is the stronger evidence and it was not in the trigger:** net charge-offs are *realized* losses rather than a forward estimate, and their YoY growth accelerates monotonically every quarter — **+12.6% → +16.5% → +22.2% → +36.9%** — while headline 30+ DQ ex-Peloton *fell* to 2.5%. That is the composition-masking signature the pathway was written to detect, showing up in the one series management cannot re-estimate.

✅ **The +42% secondary read that 9/10 flagged as unverifiable is CONFIRMED at the primary (+42.5%), as is its NCO leg ($128M → $170M; actual $127.5M → $170.2M).** `[[finding_claim_outlives_its_discredited_instrument]]` — the supplement stayed unreachable, but the claim it carried was independently reconstructible from filings.

**Allowance leg re-tested for denominator-robustness** (9/10 quoted a single convention): rate rises on **all three** — 5.63→5.88% (incl. accrued interest + fees), 5.70→5.94% (excl. accrued interest), 5.65→5.89% (as recorded 9/10). **Delta +23 to +25bp; book +35.8% to +36.3%.** The leg does not depend on the convention chosen — quote it as a band, not as "+24bp".

⚠️ **The 3-leg BREAKPOINT is still NOT met, and that distinction is the whole discipline here.** §2c's breakpoint is *provision >30% YoY **AND** ABS WA FICO declining **AND** macro shock (gas >$4.50 / UI exhaustion)*. Leg 1 ✅ met. Leg 2 **UNTESTED — ABS WA FICO has not been refreshed since 672 at the Apr-2026 vintage; this is now the single largest open gap in the pathway.** Leg 3 ❌ not met (AAA $4.277 on 9/10, CRL-08's bar is $4.50). **ACTIVE describes the TRIGGER (provision-divergence-from-DQ), not the breakpoint.** Do not let "FLOW-PHAN-06 ACTIVE" travel as "breakpoint fired."

### ② BNPL-for-gasoline 38% — ATTRIBUTED, and it does NOT belong to the LendingTree series

9/10 declared this a miss rather than cite it. Primary located: **Protect Borrowers (Student Borrower Protection Center) + Data for Progress, *A Loan in Every Cart*, July 2026.** Full necessity set, denominator = **BNPL users**, "have taken out BNPL debt to finance X" (ever, not past-year): **groceries 46% · medical/dental 42% · paying down other debt 40% · utility bills 39% · gasoline 38% · restaurants/meal delivery 38% · rent/housing 33% · childcare 22%.**

⛔ **IT CANNOT BE QUOTED ALONGSIDE THE 47%/29%/13% LENDINGTREE FIGURES.** Different survey house, different instrument, different perimeter:

| | LendingTree BNPL Tracker | Protect Borrowers / Data for Progress |
|---|---|---|
| Population | U.S. consumers 18–80 | **likely U.S. voters** |
| n | 2,049 / 2,060 (QuestionPro) | 1,164 total; **BNPL-user subgroup n=438** |
| Fielded | Mar 3–6 and Mar 17–23, 2026 | **Jul 2–5, 2026** |
| Groceries | **29%** | **46%** |

**The same concept reads 29% and 46% across the two instruments — a 17pp gap on the one category both measure.** A likely-voter web panel is a political-polling frame, not a consumer-finance sample, and n=438 carries roughly ±4.7pp at 95%. `[[finding_cross_entity_comparison_needs_same_perimeter]]`. **Recommendation to CARL: carry the 38% as a DIRECTIONAL, weak-instrument datum for the pump→phantom-debt channel, explicitly on the PB perimeter — never merged into the LendingTree series, and never as the headline.** ✅ **Confirmed at the LendingTree primary 9/11: LendingTree publishes NO gasoline figure at all**, so any citation pairing "38% gasoline" with "47% late" is a cross-perimeter splice.

✅ **Collateral check — CARL's 🔴 red-band row survives it.** PB's own footnotes date the LendingTree tracker three different ways (Apr 13 / Jun 12 / Aug 19, 2026). Cause found at the primary: it is a **rolling-updated page ("Updated Aug 19, 2026")**, so the footnote dates are snapshots of one URL. **Our 8/19 stamp, the 34→41→47 series and the n=2,060 / Mar 17–23 field window are all correct as recorded.**

### ③ P03 / Rule 1033 — the conflict resolved AGAINST our own ledger

9/10 logged this conflict and declined to resolve it. Resolved at three independent law-firm secondaries (Mitchell Sandler · Cozen O'Connor · Holland & Knight, all read 9/11): **the tracker was right and our `REGULATORY.tsv` 2026-04-01 WITHDRAWAL row was wrong.** The CFPB **withdrew its request that the court vacate** Rule 1033 and **reopened the rulemaking** (ANPRM 2025-08-22, comments closed 2025-10-21; reconsideration covers the "representative" definition, **data-access fees**, and the security/privacy cost-benefit). The rule is **ENJOINED + UNDER RECONSIDERATION**; the Apr-2026 compliance date is **stayed**, not killed by the agency.

**P03 97% → 98%** — reopened rulemaking is *slower* than vacatur, so 2026 enforcement is impossible on either reading; the window verdict was never in doubt. **What was wrong was the story, not the score.** ⚠️ **And the correction cuts against the thesis:** "EFFECTIVELY DEAD" overstated it — **a rewritten, fee-permissive 1033 is a live 2027+ branch that the DEAD framing concealed**, and a fee-permissive rewrite would weaken phantom-debt visibility even after it takes effect. `[[finding_correction_to_the_sequence_survives_every_fact_check]]`: every fact in the 4/1 row was true; the order of vacatur-then-withdrawal inverted the reading. Row re-tagged `WITHDRAWN_SUPERSEDED_SEE_2026-09-11`; correction row appended. **§2b below carries the superseded "EFFECTIVELY DEAD" language VERBATIM by audit must-carry design — read it as an Apr-2026 artifact, not as status.**

### Nulls, unchanged rows, and what is still owed

- **No new state-AG EWA action since CO v. EarnIn (8/27)** — narrow count holds **NY+MN+DC+CO = 4 of 5**; **P07 unchanged at 88%**. (New detail only: ~57,000 CO consumers affected.)
- **P01 25% · P02 2% · P04 12% · P05 15% · P06 MIXED — all unchanged**, re-checked, no new information. **P02's MISS-at-FY-close recommendation from 9/10 is still owed a CARL disposition.**
- ⛔ **Still unreachable:** the Affirm FQ4 supplement (3rd timeout — now moot, reconstructed from filings) and `openbankingtracker.com` (2nd consecutive HTTP 429 — not used).
- 🔻 **Largest open gap in the domain: ABS WA FICO, unrefreshed since 672 (Apr-2026).** It is leg 2 of the FLOW-PHAN-06 breakpoint and nothing in this pass touched it. Next natural read: the ~11/05–11/20 gate.

---

## 2026-09-10 pass (2nd ad-hoc, +62d) — WQ-209, PROME-spawned under CARL's card
*Live-data pass. Every figure primary or named-secondary, each dated. **Predictions re-marked, NOT resolved — CARL disposes (§8.4).** `COCKROACH.tsv` + `REGULATORY.tsv` unfrozen per their own dated trigger (docket row 2026-09-08); DATA clock advanced 2026-07-10 → 2026-09-10. Full dispositions + gaps: `outbox/2026-09-10_PHAN-to-CARL_dossier-pass.md`.*

| Gate print | Volume | Headline credit | The leg that actually matters |
|---|---|---|---|
| **Affirm FQ4-26** — 10-K FYE 2026-06-30, filed 2026-08-27 (SEC XBRL, primary) | GMV **$50.2B FY26, +37% YoY**; Q4 $14.1B, +36% | 30+ DQ ex-Peloton **2.5% @ 6/30/26** — *down* from the 2.7–2.8% of the prior three quarters, *up* from **2.3%** a year earlier | **Allowance $563.3M = 5.89% of loans HFI vs 5.65% FY25 (+24bp)** while loans HFI grew +36.1% to $9.561B. Provision **$796.7M vs $616.7M = +29.2%**. NCOs **$611.6M vs $500.8M = +22.1%** |
| **Klarna Q2-26** — press release 2026-08-18 (primary) | GMV **$36.6B, +18% YoY** (U.S. +27%) | Provisions **0.52% of GMV** vs 0.56% Q2-25; U.S. Fair Financing 30+ DPD **−20bp QoQ** | Net income **+$9M** (vs −$53M Q2-25); FY26 GMV guide **CUT to $149–151B** from >$155B |

⛔ **SUPERSEDED 2026-09-11 — THIS DOWNGRADE WAS WRONG, AND IT WAS WRONG ON PERIOD BASIS, NOT ARITHMETIC. See the 2026-09-11 section above; FLOW-PHAN-06 is RESTORED to ACTIVE.** The FY figures below are all correct; the error was testing a trigger authored on QUARTERLY provision growth against a FISCAL-YEAR aggregate that a flat Q1 (+1.8%) dragged under the bar. Retained verbatim as the record of that pass. ~~Original call:~~ ⚠️ **FLOW-PHAN-06 DOWNGRADED — trigger ACTIVE → PARTIAL (1 of 2 legs).** The 7/10 trigger sentence (*"provisions +40% YoY vs DQ improvement"*) does not survive a named basis: FY26 provision **+29.2% is BELOW GMV +37% and below loans +36.1%**. What survives is the **allowance-RATE** leg (5.65% → 5.89%) — forward expected loss per dollar of book rose while the headline DQ fell. `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]` — never quote "provisions outpacing volume" without saying *vs GMV or vs loans, Q4 or FY*. Q4-only provision growth is reported at **+42%** but that is **SECONDARY** (analyst read of the supplement); ⛔ **SEARCH-NOT-FOUND — the primary `Affirm FY Q4 2026 Earnings Supplement, August 27 2026` (`investors.affirm.com/static-files/c160ce8f-a9b5-4896-b8ed-6544ac430809`) timed out on two fetch attempts; all FY figures above come from the 10-K XBRL instead.**

🔴 **The biggest item this pass is not a BNPL print — it is an instrument refutation sitting under CARL's own threshold.** NY Fed Liberty Street Economics, Aug-2026, *"How Distressed Are Consumers? Reconciling Diverging Credit Card Delinquency Measures"*: the credit-card 90+ **STOCK** delinquency rate (12.8%, vs 7.6% in Q3-2022) is driven by charged-off balances **staying on credit reports longer** — only ~**40%** of borrowers' charged-off debts were still being reported one year later in 2004–2012, **80% by 2024**. Exclude charged-off balances and the stock rate **"falls in line with both our flow delinquency rate and the Call Report delinquency rate"**; the flow rate is *"elevated but has been largely stable since 2024."* ⇒ **CRL-05 (CC 90+ DQ vs the 13.74% GFC peak) is instrumented on a series whose rise is substantially a reporting-DURATION artifact, not incidence.** This inverts PHAN's own framing in one direction and confirms it in the other: BNPL **under**-reports obligations, while the bureau stock series **over**-reports realized stress. **CARL must grade it; it belongs in RED's counter-log.** `[[finding_instrument_measures_a_superset_of_the_thesis_subject]]`

| Threshold (§3 row) | 7/10 vintage | **9/10 live** | Band |
|---|---|---|---|
| BNPL late-payment rate | 34–41% (ABA 2024) | **47%** — 34% ('24) → 41% ('25) → **47% ('26)** [LendingTree BNPL Tracker, n=2,060, fielded 3/17–23/26, pub 8/19/26] | 🟠 → 🔴 **FIRST RED BREACH (>45%)** |
| BNPL stacking, 2+ at once | 63% (CFPB Jan-25) | **63%** flat; **25% hold 3+** (was 23%) [LendingTree, n=2,049, fielded 3/3–6/26] | 🔴 held — **P01's >70% not reached** |
| Affirm 30+ DQ | 2.3% (Q4 FY25) | **2.5%** @ 6/30/26 | 🟢 under the >3% yellow |
| Klarna credit-loss provision | 0.65% (Q4-25) | **0.52% of GMV** (Q2-26) | 🟢 under the >0.60% yellow |
| Fintech failures (cumulative) | 3 | **3 — explicit DID_NOT_APPEAR null** (Parker Ch-7 5/7/26 = B2B, out of scope per 7/10; Solid Ch-11 = Apr-**2025**, pre-window; BlockFills = crypto) | 🟠 unchanged |
| Phantom-DTI gap | ~12pp | **not refreshed** — ⛔ SEARCH-NOT-FOUND: any *2026 FHA Mortgagee Letter or HUD final guidance on BNPL*. The 2025-06-24 RFI's comment period closed **2025-08-25**; nothing issued since | 🟠 carried, stale |

**Transmission into CARL's consumer thesis (the finding, not a restatement).** BNPL is now load-bearing for **necessities**: **54% of users agree they need these loans "to make ends meet"** (62% of parents with children <18, 59% of millennials), **29% have used BNPL for groceries** (25% in '25, **14% in '24**), 13% for rent [LendingTree, n=2,049, fielded 3/3–6/26]. That is the same bottom-cohort the **$4.146 pump** (CARL 9/5) and the food/tariff squeeze run through. ⭐ **The load-bearing point for the thesis: the late rate went 41% → 47% across a year in which payrolls were REVISED UP (July −23K → +21K, BLS 9/4) and LABOR's T-03 did not fire.** Shadow-layer deterioration is **not waiting on an employment break** — that is the rot-not-detonator reading of "Beneath the Ice," evidenced on a series CARL does not currently carry. It cuts the other way too: **V16's drop-back branch can resolve DOWN at the ~10/2 NFP and this series would still be deteriorating**, so the branch is not a referendum on the consumer leg.

**Also moved:** **P07 → 88% (trending HIT)** — **Colorado AG Weiser sued Activehours Inc. d/b/a EarnIn on 2026-08-27** (3.1M CO transactions Jan-2023→Jul-2025, ~$300M advanced, >$16M collected in tips + expedited-transfer fees, **average APR ~388%**); narrow state-AG count now **NY + MN + DC + CO = 4 of 5**, 3.7 months of window left. **P04 → 12% · P05 → 15% · P02 → 2% (recommend MISS at FY-close) · P03 → 97% · P01 → 25%.** **Furnishing moved:** Affirm now furnishes all pay-over-time products to **Experian and TransUnion** (loans issued from 4/1/25 and 5/1/25 respectively) — the §2a *"only Affirm reports, 2 of 3"* line is still directionally right but is no longer a static fact. **Klarna's U.S. pay-in-4 furnishing is CONTRADICTORY across secondary sources — UNKNOWN, do not cite either way.**

---


---

## 2026-07-10 passes — full change-history rows (moved from `DOSSIER.md` §9, 2026-09-11, read-cap reclaim)

*Four distinct 7/10 passes. Verbatim as they stood in §9; the dossier now carries a single compacted row pointing here.*

| Date | Pass | What changed |
|---|---|---|
| **2026-07-10** | **DOSSIER assembly** (MOLD / DAEDALUS editor) | Dossier assembled from PHAN's Apr-2026 frozen surfaces (transcription-with-provenance, no new analysis). Legacy CLAUDE.md/STATUS.md frozen same day; COCKROACH.tsv + REGULATORY.tsv kept live. |
| **2026-07-10** | **1st ad-hoc pass** (CARL-directed, ledger-hygiene only, no web data) | **(1)** 7 predictions dispositioned (§4 + `workbook/PREDICTIONS.tsv`): all 2026 windows still open → P02 **MIXED** (premise refuted, Klarna Q1 profitable), P03 re-marked 90%→96% (tracking-HIT, 1033 withdrawn), P04 60%→45%, P05 50%→40%, P06/P07 held, P01 held; calibration mode logged per row. **(2)** FLOW-numbering divergence (§2c) **reconciled — TSV numbering wins** (canonical crosswalk added; prose FLOW-PHAN-03→TSV-04, prose FLOW-PHAN-04→§2a framework/no TSV ID); TSV not renumbered. **(3)** Live ledgers COCKROACH.tsv + REGULATORY.tsv verified readable, headers clean, untouched. Header + §4 truth-stamped. |
| **2026-07-10** | **Staleness sweep** (CARL-directed, tag-don't-refresh, no web) | 6 rows STALE-tagged: 4 REGULATORY (1033 arc superseded by 4/1 WITHDRAWAL; HUD RFI ACTIVE vs parent STALLED) + 2 COCKROACH (both Klarna rows, deterioration REFUTED). §2a given `[as-of Apr-2026]` section tag. Retirement candidates listed (SCHEMA.tsv; CARL_HANDOFF — keep, load-bearing). |
| **2026-07-10** | **News sweep** (CARL-directed, web, last-30d) — SV-PHAN-2026-07-10-01 | **P06 CORRECTED** → MIXED: NY BNPL Act **SIGNED 2025-05-09** (predates the forecast → authored-blind-to-existing-fact); DFS rules proposed 2026-02-23 — REGULATORY.tsv +2 corrective rows, old 4/9 row STALE-tagged. **P07 → 80% trending HIT**: Minnesota AG v. Brigit 2026-06-10 (adds MN to NY/DC) — REGULATORY.tsv +1 row. **P02 → 6%**: Klarna Q1-2026 provision 0.55% GMV (May-18). **Affirm/Klarna Q1 actuals** (2.8% DQ/$512M; 0.55%) routed to CARL KB-228 (§6). **P04:** Parker/Hokodo 2026 failures found but B2B/out-of-consumer-scope → not counted, not appended. Furnishing≠visibility (Senate probe May-2026) reinforces P03/§2a. Affirm FQ4 earnings confirmed **2026-08-20** (§8). All figures year-verified 2026. |
