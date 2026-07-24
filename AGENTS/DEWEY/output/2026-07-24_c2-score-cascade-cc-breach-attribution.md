# Score-cascade attribution: does student-loan delinquency CAUSE the CC 90+ GFC breach? (CRL-05)
**Date:** 2026-07-24 | **Mode:** Thesis | **Confidence:** High (level/arithmetic, PRIMARY) / Medium (causal increment — literature is indirect)
**Flag:** CARL slate T1-1 / C2 (STUE-proposed, Will-gated) · **Deliver-by:** ~8/8 (before NY Fed Q2 HHDC ~Aug-15)

## Key Finding
The CC 90+ balance share (**13.12% Q1'26**) will **plausibly touch/breach the 13.74% GFC peak in the next 1–2 quarters on arithmetic momentum — but NOT because of the student-loan score cascade.** Three independent lines converge: (1) the SL cascade, sized bottom-up against the NY Fed's own cohort figure (~$25B of CC balances), closes only **~⅓ of the 0.62pp gap**; (2) ~**62% of the Q1 rise came from a shrinking denominator** (CC balances fell $25B), not surging delinquency — and that shrink is likely partly seasonal and may reverse Q2–Q3; (3) every *flow* and *bank-side* measure is flat-to-**improving** (CCP 30+ transition ticked down 8.7→8.6%, 90+ flow flat ~7.1%, bank call-report delinquency AND charge-offs falling). **Both adversarial verifiers REFUTED** the "cascade closes the gap alone" claim. The cascade is a **real but second-order, decelerating** contributor. **Decision read for CRL-05: expect the headline breach, but do not attribute it to the cascade — a breach here is a stock/measurement event, not fresh systemic consumer stress.** The NY Fed itself judges spillover "likely to be limited."

## Sub-answer 1 — The attribution coefficient (score band → CC delinquency)
Serious (90+) delinquency is **more** score-sensitive than early (30+):

| Metric | Subprime | Near-prime | Prime | Differential |
|---|---|---|---|---|
| CC **30+** DPD, bal-share, 2023Q3 [PRIMARY: Fed FEDS Note, Driscoll et al, 2024-01-12] | 15.68% (<620) | 5.34% (620–719) | 1.05% (>719) | near-prime→subprime **+10.34pp** |
| CC **90+** account-incidence, yr-after-scoring, FICO bands [PRIMARY: FICO Credit Insights Report 2025] | 55.9% (300–549) / 25.4% (550–599) | 12.0% (600–649) / 5.3% (650–699) | 1.8% (700–749) / 0.2% (750–850) | each ~50pt band drop ≈ **doubles** the 90+ rate |

- The −69pt cohort anchor is FICO's own: SL-delinquent borrowers averaged **617 (Jan'25) → 548 (Apr'25)**. On the 90+ table that is +13pp (one band) to +44pp (two bands) — **larger in pp than the +10.34pp 30+ differential**, confirming 90+ is where the score channel bites hardest [PRIMARY: FICO Credit Insights Report 2025, fico.com/en/resource-access/download/55026].
- ⚠️ Two load-bearing caveats. **(a)** The exact 55.9/25.4 bars were reconstructed from a FICO chart (only the 600–649 = 12.0% point is text-confirmed); treat "each ~50pt drop roughly doubles the 90+ rate" as the durable claim, not the exact bars. **(b)** The FEDS Note's own thesis is that much of the band-level rise is a **composition effect** from pandemic-era upward score migration, *not* deterioration at a given score — so band rates conflate score-mechanism with who is in the band. This is the confound sub-answer 4 must resolve.
- **Balances cut the other way (load-bearing for the arithmetic):** subprime carry far smaller limits — avg credit line $2.2K deep-subprime / $3.3K subprime vs $8.4K prime / $13.2K superprime [PRIMARY: CFPB Consumer Credit Card Market Report 2025]. Subprime defaults are **higher-probability but fewer-dollars-per-account.**

## Sub-answer 2 — Lag structure + issuer mediation
The score-drop→card-delinquency channel is **not mechanical**; it runs through issuer line management and utilization:
- Issuers subscribe to bureau "account-management triggers" (Equifax/TransUnion) that flag score drops, cross-lender delinquencies (incl. a new **student-loan** delinquency), and rising utilization on a daily/weekly/monthly cadence [INSTITUTIONAL: Equifax Business Insights 2025; PRIMARY: CFPB *Credit Card Line Decreases*, 2022-06-29].
- A credit-line decrease (CLD) cuts a **median ~75% of the open line**, spiking utilization to **89–94% ("maxed out")**, which drives a **further** score decline (utilization ≈ 30% of FICO) [PRIMARY: CFPB CLD report 2022, Figs 2–6]. This is the transmission: score drop → line cut → utilization spike → more score damage → higher price/denial of credit.
- SL delinquencies feed it directly — federal SL delinquencies reappeared on reports **Jan 2025** after a 43-month pause; payment history is 35% of FICO; **5.6M** borrowers went newly delinquent Q1'25 with score drops of −74pt (subprime) to −177pt (prime) [PRIMARY: NY Fed Liberty Street, 2025-05].
- **The lag is loose and the link is partial.** No published clean quantitative lag for score-drop→card-delinquency exists. Population-level: SL delinquency onset Jan'25 → card-delinquency overlap visible by Q1'26 ≈ **~12 months**, but that is co-incidence of fragility, not an identified causal lag. And **67% of CLDs had no cardholder delinquency** — issuer line-cutting is substantially internal risk management, so the score→line-cut→delinquency path is real but only a **partial** mediator [PRIMARY: CFPB CLD report 2022, Table 1].

## Sub-answer 3 — The arithmetic (does the cascade close the 0.62pp gap?)
**Gap to breach:** 13.74 − 13.12 = **0.62pp** of $1.25T = **~$7.75B** additional 90+ CC balances.

**Cohort denominator (the key upgrade this run):** delinquent/defaulted SL borrowers collectively hold **~2% of all US CC balances = ~$25B** [PRIMARY: NY Fed Liberty Street, 2026-05]. Within-cohort card stress is severe and rising: 56% of newly-defaulted SL borrowers who hold a card are already past due on it; serious (90+) CC delinquency in the seriously-delinquent-SL cohort rose **1.03% → 5.96%** (Dec'24→Jun'25) [INSTITUTIONAL: TransUnion 2025-07].

**Bottom-up cascade contribution:**
- Incremental 90+ dollars ≈ cohort CC balances ($25B) × incremental 90+ rate attributable to the cascade. At the observed cohort 90+ rate (~6%) applied as *incremental*: ~$1.5B ≈ **0.12pp**. Even a generous read tops out near **~0.19pp (~$2.4B) ≈ ⅓ of the gap.**
- To close the full $7.75B from the cohort alone, **~28% of the entire cohort's card balances would have to roll 90+ as a purely incremental effect** — implausible.
- ⇒ **The cascade does NOT close the gap alone.** A breach requires the stock mechanic and/or non-SL deterioration.

**Where the Q1 move actually came from (decomposition):** CC balances fell **$25B → $1.25T** in Q1'26; implied 90+ dollars rose only ~$2.1B (~$162B→$164B), yet the share jumped +0.42pp. **~62% (~0.26pp) of the rise was the shrinking denominator; only ~38% (~0.16pp) was numerator growth** [PRIMARY: NY Fed HHDC Q1'26]. **DEWEY analytic addition:** the Q1 balance-shrink is likely **partly seasonal** (card balances typically fall in Q1 on tax-refund paydown and rebuild Q2–Q4). If so, the denominator tailwind **reverses** into Q2–Q3, pushing the share *down* all else equal — so a clean Q3 breach is **less assured** than the +0.42pp/qtr trend implies. *(Caveat: I did not confirm the series' seasonal-adjustment status; treat as a directional flag, not a settled figure.)*

## Sub-answer 4 — Adversarial confound (score-mechanism vs shared income shock)
The causal literature supports a **split, not either/or**:
- A credit score is mechanically a **lagging summary of realized delinquency**, so a score decline is **predominantly a co-symptom** of the same shock that produces the CC delinquency. A naive "score cascade" added *on top of* the shock **double-counts** for the bulk of the effect. NY Fed: 56% of defaulted SL borrowers **already** had a card past due, attributed partly to **pre-existing fragility** [PRIMARY: NY Fed 2026-05].
- **But a real, second-order causal increment exists** — the score is itself a lender *input*, so moving it (income held constant) changes credit access and downstream default. Clean natural experiments: Dobbie et al. (2020, JF) bankruptcy-flag removal raises limits/borrowing with a "precise zero" on earnings; Musto (2004); Liberman-Chile (2018, 2.8M deletions); Agarwal et al. (2018) — MPC-to-borrow ~59% for FICO<660, ~0 for high scores, so a score-driven **limit cut removes liquidity** that constrained borrowers would have drawn [ACADEMIC/PRIMARY, various]. A pure-information score change raised CC delinquency ~**+6.4pp** over 3 years in a Dobbie follow-on *(MEDIUM — not PDF-verified, 403; do not make load-bearing)*.
- **US-specific damper:** the cleanest contractual score→cross-default channel ("universal default" APR hikes) was **disabled by the CARD Act of 2009** — issuers can't raise the rate on existing balances unless 60+ DPD. So any present-day cascade must run through the weaker limit-cut / refi-denial path, concentrated in already-constrained low-score borrowers.
- **Reverse natural experiment (Sweet cohort):** Sweet v. Cardona discharges + **deletes tradelines** for **271K+** borrowers (final approval Nov 2022) — a score-up-with-income-constant shock. **Gap:** no published study measures the Sweet cohort's own post-deletion scores/performance. The cleaner **analogs** both show the mechanism AND its limits: CFPB **Fresh Start** (1.9M borrowers, defaults→current, median **+54pt**, ~48% up a tier) found the delinquency drop **"does not appear to have spilled over"** to other loans; CARES forbearance (~37M, +9pt avg) similar [PRIMARY: CFPB 2023; NY Fed 2020-11].
- **Net:** mostly marker, with a **small legitimate mechanism increment.** The honest causal number is "a modest positive increment," not the full cascade.

## Counter-Evidence (the NULL is strongly supported)
- **Bank supervisory data prints the opposite sign.** Call-report CC delinquency (DRCCLACBS) **fell to 2.92%** — 5 straight quarters down; small banks 6.43% (from 7.86%); top-100 2.80%. Bank net **charge-offs also falling** (CORCCACBS 3.84% vs 4.46% yr-ago) [PRIMARY: FRED, Q1'26]. Rising realized losses are the true bank stress tell — and they're declining.
- **13.12% is not novel** — the identical 13.12% printed in **2011Q1**, a no-crisis recovery quarter. Underlying flows run **~4pp below** GFC levels (90+ flow 7.1% now vs 10.64% in 2010Q2).
- **The impulse is decelerating** — SL transition into serious delinquency fell 16.2%→10.9%; the 2025 surge was a one-time reporting-cliff (on-ramp expiry Oct'24), now cresting.
- **The 90+ measure accumulates charged-off paper** (severely-derogatory lingers for years on Equifax), so the numerator ages rather than clears — mechanically lifting the share independent of fresh stress.
- **Counter to the counter (steelman of the thesis):** the 90+ bucket has accumulation momentum — balances stay 90+ until ~180-day charge-off, so even flat inflow keeps filling the deep bucket faster than it clears; a near-breach on lag alone is plausible; and the SL cohort was a genuine part of the 2025 wave now aging in.

## Source Quality Assessment
Spine is **PRIMARY and strong** (NY Fed CCP/Equifax workbook, Fed FEDS Note, CFPB reports, FRED, FICO). The two soft spots, both flagged inline: the FICO 90+ **exact bars** (chart-reconstructed; the *doubling* pattern is robust) and the **causal increment magnitude** (literature is indirect — natural experiments shock the score *up*/information set, not a forced downward default; the ~6.4pp figure is unverified). The cohort denominator (~$25B) is a clean primary anchor that sidesteps the unreconciled "7–9M" borrower count (point-in-time ~5.4–5.8M vs cumulative-ever ~6.8M).

## References
- NY Fed HHDC Q1 2026 (PDF + xlsx): newyorkfed.org/medialibrary/interactives/householdcredit/data/{pdf/HHDC_2026Q1, xls/HHD_C_Report_2026Q1.xlsx} — CC 90+ share 13.12% (Page 12), flows (Pages 13–14), by-age (Page 27)
- NY Fed Liberty Street: "Federal Student Loan Defaults Return…" (2026-05); "Student Loan Delinquencies Are Back…" (2025-05); "Following Borrowers Through Forbearance" (2020-11)
- Fed FEDS Note, Driscoll/Flagg/Katcher/Sommer (2024-01-12): federalreserve.gov/econres/notes/feds-notes/…-20240112.html
- FICO Score Credit Insights Report 2025: fico.com/en/resource-access/download/55026
- CFPB: *Credit Card Line Decreases* (2022-06-29); *Consumer Credit Card Market Report 2025*; *Fresh Start* blog (2023); SL Borrower Survey (2023–24)
- Academic: Dobbie et al. (2020, JF); Musto (2004, JB); Liberman et al. (2018); Agarwal et al. (2018, QJE); Fulford (2015)
- FRED (via scripts/fred_pull.py): DRCCLACBS / DRCCLT100S / DRCCLOBS (delinquency); CORCCACBS / CORCCOBS (charge-offs)
- TransUnion student-loan collections updates (2025-05/07); CARD Act of 2009 (PL 111-24)

## Process Report
**Engines:** DEWEY primary-pull spine (NY Fed HHDC xlsx/PDF direct + FRED consumer-credit) + fan-out (8 agents / ~486K tokens / 0 err / ~9.5 min): 6 finder legs + 2 adversarial verifiers.
**What worked:** the primary-pull carried the verdict as designed — the NY Fed xlsx gave the exact CC 90+ series (13.12% + 13.74% GFC peak from one file), and the fan-out's NY Fed CCP ~$25B cohort figure + denominator decomposition were decisive. Both verifiers independently REFUTED the strong-form claim, converging with the arithmetic.
**Data gaps:** no primary co-hold share or avg CC balance for the SL-delinquent cohort (only the ~$25B aggregate); no clean quantified score→card-delinquency *lag*; no study of the Sweet cohort's own post-deletion performance; no published current→90+ transition matrix by score band (FICO's forward-hazard is the closest analog).
**Source frustrations:** FICO 90+ table is chart-locked (a small-model first-read mis-assigned the bars — caught and corrected via text anchors); federalreserve.gov "Predicting CC Delinquency" + Philly Fed EI PDFs returned 403 (→ BACKLOG, recurring Fed-PDF 403 class); Dobbie follow-on 6.4pp unverifiable (403).
**Confidence:** High on level/arithmetic/counter-evidence; Medium on the causal increment (indirect literature).
**If I had more time/tools:** issuer master-trust monthly data (COF/SYF/DFS/Citi/JPM) — the single-name secondary series the fan-out can't reach — would test whether subprime-tilted issuers diverge from the falling aggregate; a NY Fed CCP cohort-match (SL-delinquent vs matched control) is the one clean test that would settle the confound. **Both are readable in the mid-July large-issuer Q2 earnings BEFORE the Aug-15 NY Fed Q2 HHDC** — the pre-position window CRL-05 cares about.
