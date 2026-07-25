# AXIS B — Is the 11.47% MMI capital ratio deferral-flattered?

**Study:** DEEP-RESEARCH-PROMPT-19, Axis B · **Date:** 2026-07-24 · **Ledger:** REQ-DEWEY-20260724-019
**Parent:** `AGENTS/DEWEY/output/2026-07-24_fha-va-loss-waterfall.md`

**VERDICT: PARTIALLY — with a material framing correction, but the parent's "federally absorbed" KILL survives on magnitude.**
**Confidence: HIGH on the numbers** (all from audited/primary HUD sources, reconciled two independent ways). **MEDIUM-HIGH on attribution** (HUD does not break out partial-claims-only within the line that carries them).

The hypothesis is directionally correct and was under-explored. The deferral is real, large, and growing fast. It is also *marked*, and too small to threaten the ratio.

---

## 0. Correction to the prompt's premise (date-checked)

**ML 2025-06 is not the operative waterfall.** ML 2025-06 (Jan 16 2025) was **superseded by ML 2025-12**, *"Tightening and Expediting Implementation of the New Permanent Loss Mitigation Options"* (Apr 15 2025), effective **Oct 1 2025**. All findings below are against ML 2025-12. The Oct 1 2025 mandatory date is correct; the ML number is not.

---

## 1. Accounting mechanics

From the **HUD FY2025 Agency Financial Report** (audited, Dec 18 2025), Note 1.K and Note 7:

- Partial claims are **"second mortgages on HUD insured properties and are classified as defaulted guaranteed loans"** — an **asset**, not a realized loss. The note "is not due until an FHA-insured borrower's first lien has been paid in full."
- **They ARE marked.** Post-Credit-Reform receivables are valued at **"the net present value of expected cash flows"**; the gap between cost and NPV is the **Allowance for Subsidy**. This is the most important fact against the strong form of the hypothesis — not carried at face.
- Most partial-claim notes sit in **Note 7 (Loans Receivable, Net)**. A small residue — partial claims where FHA paid but has not received the note — sits in Note 6: **$460M gross, $240M allowance, $220M net**.
- **Confirmed in the MMI report itself:** *"HUD-held notes have become a larger component of capital resources in recent years, **due to an increase in partial claims volume**"* (FY2025 Annual Report, Ch. II). The receivable is **inside the capital ratio numerator**.

### Payment Supplement is carried identically — it IS a partial claim
ML 2025-12: *"The Payment Supplement is a loss mitigation option that **utilizes Partial Claim funds** … evidenced by a **non-interest bearing Note, Subordinate Mortgage**… given in favor of the Secretary, representing the total of all funds paid from the **Mutual Mortgage Insurance Fund**."* Filed as **Claim Type 33** — the partial-claim claim type — with a 36-month Monthly Principal Reduction period. **No separate accounting object**; it flows into the same receivable line.

---

## 2. Volume and trend

**MMI/CMHI Single-Family, defaulted guaranteed loans from post-1991 guarantees** (Note 7I — the line carrying partial-claim notes), from five separate audited AFRs:

| FY | Gross ($M) | Allowance for Subsidy ($M) | Net ($M) | Allowance % |
|----|-----------|---------------------------|---------|------------|
| 2020 | 13,780 | (4,562) | 9,807 | 33.1% |
| 2021 | 16,870 | (5,751) | 11,410 | 34.1% |
| 2022 | 25,542 | (6,310) | 19,475 | 24.7% |
| 2023 | 29,500 | (6,845) | 23,063 | 23.2% |
| 2024 | 34,265 | (9,327) | 25,370 | 27.2% |
| **2025** | **39,800** | **(12,496)** | **27,858** | **31.4%** |

- **Gross grew 189% (2.9x) FY2020 → FY2025.**
- **The allowance ratio is RISING** (23.2% → 31.4% since FY2023). HUD is marking these down *harder*, not hiding them.

### It is essentially the entire non-cash component of forward capital resources
Reconciled two ways, agreeing exactly:
- Forward stand-alone capital resources FY2025 = **$130,533M** (Exhibit II-6)
- Total capital resources $139,665M − HECM $9,131M = $130,534M ✓
- HUD states **">$100 billion is cash and cash equivalents"**
- $100B cash + $27.86B receivable ≈ **$127.9B of $130.5B**

**→ The partial-claim receivable is ~21.3% of forward capital resources and effectively the whole non-cash residual.**

---

## 3. THE RE-DEFAULT RATE — HUD does publish it, and it is bad

FY2025 Annual Report Exhibits O-9/O-10, data tables A-9/A-10. Definition: *delinquent within one year of receiving a partial claim, loan modification, combination, or payment supplement.*

**Table A-9 — one-year redefault by quarter of option received:**

| Cohort | 90+ day | **Total** |
|--------|---------|-----------|
| 2020 & 2021Q1 | 6% | **11%** |
| 2022Q4 | 17% | **40%** |
| 2023Q4 | 25% | **53%** |
| 2024Q2 | 27% | **51%** |
| 2024Q3 | 30% | **56%** |
| **2024Q4** | **31%** | **58%** |

**Table A-10 — by fiscal year:** FY2022 31% → FY2023 48% → **FY2024 55%**, against a **2009–2019 average of 46%**. Recent cohorts run *above* the post-GFC crisis-era average.

**Compounding (Exhibit O-12):** by Sept 2025, **66%** of borrowers receiving a home-retention option had ≥1 prior option in five years and **~40% were receiving their third option in five years** (vs ~2% with 2+ in Jan 2018).

HUD's own words: *"repeated loss mitigation costs negatively impact MMI Fund performance"*; the new waterfall was implemented *"to address a cycle of surging redefault rates and unsuccessful loss mitigation interventions."*

**The deferral is NOT benign.** At 58% one-year redefault (31% to 90+), a large share of these receivables sit behind borrowers already failing again.

---

## 4. Assumed recovery vs realized — and what the actuary declined to do

- **Assumed:** only disclosed recovery assumption is the implied **68.6 cents on the dollar** (100% − 31.4%) embedded in the Note 7I NPV mark.
- **Realized:** **HUD does not publish a realized collection rate on partial-claim notes.**
- **The FY2025 independent actuarial review (ITDC) barely engages this.** In 381,721 characters, **"redefault" appears exactly ONCE**.
- **The review assumes reversion.** It sets the COVID loss-mitigation indicator to **0** and assigns `fy_2012_2021Q2 = 1`: *"we cautiously assume that the loss mitigation expense level under the new waterfall can be similar to the levels observed in the data period before the COVID-19 pandemics."* **The ratio embeds assumed reversion to pre-COVID loss-mit costs while realized redefault is at 58% and rising.**
- **The actuary explicitly declines the question:** *"Whether the benefits of delaying or avoiding a claim outweigh the underlying cost of loss mitigation tools **is not addressed in sensitivity tests**."*
- **The ratio books a policy benefit with zero operating history:** the one-option-per-24-months limit is *"projected to save approximately $1 billion… doubling the savings from the loss mitigation reforms to **$2.07 billion** on the existing book"* — from a waterfall effective **the day after** the Sept 30 2025 measurement date. That is **0.126pp** of the ratio.

---

## 5. Oversight: HUD OIG flags collectability; GAO does not

- **HUD OIG 2018-LA-0005** (Sept 21 2018) — *primary, read in full*: NSC lacked controls to track partial claim notes for collection; **$6M at risk** across 695 sampled loans; OIG warned HUD *"could be overstating"* partial claim note balances.
- **HUD OIG, 2026 — "Review of Single-Family Partial Claims Collection Process"** *(⚠️ SECONDARY — primary unreachable)*: audit ran **April 2025–March 2026**; statistical sample of **81** terminated FHA loans (FY2021–24), **74 had servicing or collection problems**; 37 lien-release recordation delays, 14 slow payoff-check deposits, 9 demand letters delayed/never sent. Causes: **a surge in partial claim volume**, weak contractor oversight, manual processes. Consequence: *"increased risk that FHA will not collect the debts, ultimately impacting the FHA insurance fund."*
- FY2025 HUD financial statement audit: **no material weakness** from external auditors on this; internal-control deficiencies over FHA loans receivable noted at the lesser **significant deficiency** level.
- **GAO: nothing found.** No GAO product addresses partial-claim receivable valuation or deferral.

---

## 6. MATERIALITY — the decisive test

| Test | Result |
|------|--------|
| Net receivable / IIF ($1,647,236M) | **1.69pp** |
| Gross receivable / IIF | 2.42pp |
| **Ratio if the entire NET receivable → zero** | **11.47% → 9.78%** |
| That vs. the 2% statutory minimum | **still 4.9x** |
| Capital needed to breach 2% floor | $155.9B of destruction; entire gross receivable is $39.8B — **cannot get there** |
| Actuarial sensitivity: +10% loss-mit rates | −3.3% NPV ≈ −$1.2B ≈ **−0.07pp** |

**Even assuming 100% loss on every single-family partial-claim dollar HUD carries — zero recovery, beyond marks already taken — the ratio lands near 9.8% and remains ~5x the statutory minimum.**

---

## 7. NEGATIVES / COULD NOT FIND

1. **HUD does not disclose a partial-claim-only balance.** The $39.8B is MMI/CMHI **Single-Family defaulted guaranteed loans**, the line partial claims are classified into; it may also contain SF Mortgage Notes Assigned and PMM notes. HUD breaks out HECM separately but **not partial-claims-within-single-family**. This is the disclosure that would size the deferral exactly, and it does not exist publicly. Attribution rests on: (a) HUD's statement that HUD-held-note growth is driven by partial claim volume; (b) partial claims explicitly classified as defaulted guaranteed loans; (c) the clean reconciliation to the non-cash residual of forward capital resources.
2. **No COUNT of outstanding partial claims is published** in the Annual Report, actuarial review, or AFR. Searched loss-mitigation exhibits and appendix tables A-9 through A-18 — HUD publishes *rates*, never *counts or balances*.
3. **No realized collection/recovery rate on partial-claim notes is published.** The 31.4% allowance is an assumption; no realized collection experience is disclosed against it.
4. **Could not reach the 2026 HUD OIG partial-claims report at primary.** hudoig.gov is Cloudflare-protected — WebFetch 403, direct PDF fetches 410, oversight.gov search 404. Probed six plausible report numbers, all failed. The 74-of-81 finding is secondary-sourced and labeled as such. The 2018 predecessor was read in full.
5. **No GAO treatment exists** of partial-claim receivable valuation.
6. **Payment Supplement is not separately identified** anywhere in the FY2025 audited statements.
7. **No FHA MIP cut is proposed, pending, or enacted for FY2026-27** as of 2026-07-24 (Feb 2023 30bp cut remains operative). **The FY2026 actuarial review has not been released** (axis C's premise holds).

---

## 8. What this does to the parent's verdict

**The KILL survives, with one framing correction that should be recorded.**

- **Survives:** the fund's absorption capacity is not an accounting illusion. The receivable is marked, marked increasingly hard, and too small by an order of magnitude to threaten the 2% floor.
- **Correction:** *"record 11.47%"* should not be cited as a clean cash cushion. **~1.7pp of it — ~21% of forward capital resources, and effectively the entire non-cash component — is a zero-interest subordinate-lien receivable from borrowers re-defaulting at 58% within one year**, repayable only on sale/refi/payoff, on which HUD publishes no realized collection experience, and whose collection process HUD's own OIG found defective in 74 of 81 sampled loans.
- **"Absorbed" and "not yet recognized" are indeed partly conflated in the headline ratio — but the conflated amount is ~1.7pp, not ~9pp.**

**Recommended confidence markdown:** none to the *absorption* conclusion. But the claim that FHA is "nowhere near escaping the federal wrap" should carry the caveat that **the buffer's growth since FY2020 is disproportionately receivable accretion (2.9x) rather than cash**, and that the FY2025 ratio embeds two forward assumptions with zero operating history — reversion to pre-COVID loss-mit expense, and $2.07B of savings from a waterfall effective the day after the measurement date. Both are axis-C exposures; axis B independently confirms axis C's concern.

---

## Sources

- [HUD FY2025 Annual Report to Congress, MMI Fund](https://www.hud.gov/sites/dfiles/Housing/documents/2025FHAAnnualReportMMIFund.pdf) — primary, extracted in full
- [HUD FY2025 Agency Financial Report](https://www.hud.gov/sites/dfiles/CFO/documents/afr2025.pdf) — primary, audited; Notes 1.H, 1.K, 6, 7I
- [FY2025 Annual Actuarial Review, SF Forward (ITDC)](https://www.hud.gov/sites/default/files/SFH/documents/ITDC-FY2025-Actuarial-Review-SF-Forward-Final-Report-Appendix-F-Included.pdf) — primary, extracted in full
- [HUD Mortgagee Letter 2025-12](https://www.hud.gov/sites/dfiles/OCHCO/documents/2025-12hsgml.pdf) — primary
- HUD AFRs [FY2024](https://archives.hud.gov/reports/afr/afr2024.pdf), [FY2023](https://archives.hud.gov/reports/afr/afr2023.pdf), [FY2021](https://archives.hud.gov/reports/afr/afr2021.pdf) — primary, for trend
- [HUD OIG 2018-LA-0005](https://www.hudoig.gov/sites/default/files/documents/2018-LA-0005.pdf) — primary
- [National Mortgage News — HUD watchdog alleges mishandling of partial claims](https://www.nationalmortgagenews.com/news/hud-watchdog-alleges-mishandling-of-partial-claims) — ⚠️ secondary
- [Fullerton Observer, 2026-07-03](https://fullertonobserver.com/2026/07/03/hud-fails-to-service-majority-of-federally-backed-loans-audit-reveals/) — ⚠️ secondary
