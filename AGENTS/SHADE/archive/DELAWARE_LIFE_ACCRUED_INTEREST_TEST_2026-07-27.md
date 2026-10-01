# SHADE — Delaware Life: the accrued-interest anomaly, tested

**Date:** 2026-07-27 ET
**Question:** is Delaware Life's $16.37B affiliate-contingent book **impaired** or merely **mis-labelled**? The accrued-interest anomaly flagged 7/27 was the sharpest available proxy.
**Source:** Delaware Life Insurance Company statutory financial statements, **Form N-VPFS filed 2026-06-29, accession `0001193125-26-286687`** (CIK 704843, Delaware Life Variable Account C), KPMG-audited, Delaware DOI basis. **All figures read directly from the filing. $000s.**

---

## VERDICT

**The anomaly is REAL and now has four controls — but it is EXPLAINED by a disclosed contractual feature, and it is NOT evidence of impairment.**

**The anomaly does not survive as a PIK/impairment finding, and I am retiring it as one.** What replaces it is better: the filing **names** the mechanism (**trust notes that allow for deferred interest**), **quantifies the income** ($159.6M in 2025), and then **withholds the population that generates it** — so the one ratio that would answer "how much of this book doesn't pay cash?" **cannot be computed from the filing.**

**Net effect on the firing vector: no change to the call, one dampener strengthened, one new measurement gap opened.**

---

## 1. THE ANOMALY, WITH ALL CONTROLS

Every affiliate securities transaction disclosed in the filing, 2023–2025:

| Year | Counterparty | Direction | Book value | Accrued interest | **Accrued / Book** | Cash | FV / Book |
|---|---|---|---:|---:|---:|---:|---:|
| 2023 | CSLAC | purchase | 313,574 | 2,751 | **0.88%** | 315,884 | 99.86% |
| 2024 | CSLAC | purchase | 232,753 | 2,390 | **1.03%** | 235,143 | 100.00% |
| 2024 | **Barbco** | purchase | 176,273 | 749 | **0.43%** | 177,022 | 100.00% |
| 2025 | **GLIC** | **sale** | 319,579 | 3,022 | **0.95%** | 324,212 | — |
| 2025 | GLIC | purchase | 3,665 | 68 | **1.86%** | 3,712 | — |
| **2025** | **CSLAC** | **purchase** | **343,412** | **33,559** | **🔴 9.77%** | **374,750** | **99.35%** |

**Four independent controls, and the anomaly survives all of them:**
- **Same counterparty, prior years:** CSLAC ran **0.88%** and **1.03%**. The 2025 print is **9.5× its own two-year history.**
- **Same year, different affiliate:** the GLIC sale — **nearly the same size** ($319.6M vs $343.4M) and in the **same 2025** — ran **0.95%**. So this is **not** a 2025 rate-environment effect, **not** a company-wide accounting change, and **not** a year-end timing artifact.
- **Different affiliate, different year:** Barbco **0.43%**.
- **Direction-independent:** it appears on a purchase, and the same-year sale is normal.

**Range of all five non-anomalous transactions: 0.43%–1.86%. The 2025 CSLAC purchase: 9.77%.**

**Why the ratio matters mechanically:** accrued/book ≈ coupon × time-since-last-payment. A semi-annual payer maxes out near **0.5 yr** — needing a **~19.5% coupon** to reach 9.77%. A quarterly payer would need **~39%**. **9.77% is only reachable if interest has been accumulating for roughly a year or more without being paid.**

⚠️ **DLIC paid the accrued interest in cash.** Cash of **$374,750** = fair value **$341,191** + accrued **$33,559**. So **$33.6M of cash moved from the $64.7B regulated insurer to its subpoenaed affiliate, in exchange for interest the underlying obligors had not paid.** That is a Key-Ratio-#3 (capital leakage) shaped fact, and it is the reason the anomaly was worth testing.

---

## 2. THE MECHANISM — the filing names it

> *"The Company holds investments in **trust notes that allow for deferred interest**. The Company recorded **deferred interest of $159,580 and $114,223** during 2025 and 2024, respectively."*

> *"…the Company holds investments in **trust notes** in which the proceeds from such investments were used to purchase **general account funding agreements and a pool of private-credit assets**, which are **predominantly contingent on the performance of affiliates.** As of December 31, 2025 and 2024, the carrying value of these investments was **$326,225 and $289,475 (restated)**."*

**Deferred interest is a contractual feature of the instruments, disclosed in the open.** That mechanically produces exactly the profile observed: interest accumulating over more than one period, so accrued-to-book far above a normal coupon fraction. **The anomaly is explained.**

**So: NOT a PIK finding.** PIK is separately disclosed and **fell sharply** — cumulative paid-in-kind interest in principal balances went **$81,975 (2024) → $36,172 (2025), −55.9%.**

---

## 3. ⚠️ THE ARITHMETIC THAT DOESN'T WORK — and this is the new finding

| | 2025 | 2024 |
|---|---:|---:|
| Deferred interest **recorded during** the year | 159,580 | 114,223 |
| Trust notes **carrying value** (the named population) | 326,225 | 289,475 |
| **Deferred interest ÷ trust-note carrying value** | **48.9%** | **39.5%** |

**No instrument yields 49% a year.** So the two disclosures **cannot refer to the same population** — the $326M is the *related-party* trust-note subset, while the $159.6M of deferred interest presumably arises from a **broader, undisclosed** trust-note book.

**That is the finding: the filing names the practice, quantifies the income, and never discloses the denominator.** The single ratio that would answer *"what share of this book does not pay cash?"* **is not computable from the filing.** Same class as the SSAP-25 self-set threshold — the number exists, the population it applies to is the filer's to define.

**And the composition disclosure has the same shape.** The $16.37B breaks down as:

| Component | 2025 | 2024 (restated) | Δ |
|---|---:|---:|---:|
| Short-term investments | 3,242,905 | 2,146,225 | +51.1% |
| **Bonds** | **12,619,338** | **6,804,448** | **+85.5%** |
| Other invested assets | 509,702 | 575,852 | −11.5% |
| **Total** | **16,371,945** | **9,526,525** | **+71.9%** |

**Named sub-structures:** SAFAs **$308,269** (+62.4% YoY) and trust notes **$326,225** (+12.7%) = **$634,494 combined — just 3.9% of the $16.37B.**

**⚠️ So ~96% of the affiliate-contingent book is described only as *"private credit investments with certain counterparties."* $15.7B carries no structural description at all.**

---

## 4. IMPAIRED OR MIS-LABELLED? — the evidence, both ways

**AGAINST impairment (and this is the stronger side):**
- **Non-admitted accrued investment income is $225 (2025) and $46 (2024).** Policy: exclude income *"over 90 days past due or where the collection of interest is uncertain."* On a **$45.9B** general account generating **$2.45B** of net investment income, **$225K is essentially zero** — management asserts substantially all accrued interest is collectible.
- **The CSLAC securities priced at 99.35% of book** — near par, not distressed.
- **PIK fell 55.9%.**
- **Deferred interest is roughly stable as a share of income:** 114,223/1,806,782 = **6.32%** (2024) → 159,580/2,446,596 = **6.52%** (2025), while net investment income itself grew **+35.4%**.
- Statutory audit opinion **UNMODIFIED**.

**⚠️ BUT — the strongest dampener is measuring the wrong thing.** The $225K non-admission test catches interest **"over 90 days past due."** **Contractually deferred interest is never past due — deferral is the contract.** So the non-admission test **cannot, by construction, flag a deferred-interest trust note**, no matter how doubtful the ultimate collection. **The reassurance is real but much narrower than it looks, and it should never be cited as evidence that the affiliate book is performing.**

**Keeping the question open:**
- The 2025 CSLAC ratio is **~10× all five other affiliate transactions**.
- Deferred interest grew **+39.7%**, faster than NII's +35.4%.
- **$33.6M of cash** left the insurer for uncollected interest, to the co-subpoenaed affiliate.
- The deferred-interest **denominator is undisclosed**; the book's composition is **96% undescribed**.

**VERDICT: not impaired on any evidence in this filing — and not demonstrably sound either.** The honest statement is that **~6.5% of Delaware Life's investment income is non-cash by contract, arising from instruments that are "predominantly contingent on the performance of affiliates," and the filing does not disclose how large that population is.**

---

## 5. WHAT CHANGED, AND WHAT DID NOT

**Retired:** the accrued-interest anomaly as a possible **PIK / impairment** finding. It has a disclosed, contractual explanation, and PIK moved the other way. *(Recording this plainly: my own 7/27 flag does not survive its own test.)*

**Retained and sharpened:** the 2025 CSLAC transaction remains a genuine outlier against four controls, and the **$33.6M cash-for-accrued-interest transfer to the co-subpoenaed affiliate** stands on its own as a capital-leakage observation.

**New:** the **deferred-interest denominator gap** and the **96%-undescribed composition** — two more instances of the day's through-line, *the filer defines the population.*

**Unchanged:** vector #1 stays **FIRING** on the restatement itself. No threshold moves. Still **no charges filed**. Still a **disclosure** event with **no write-down and no surplus restatement**.

---

## 6. NEXT TESTS

| # | Test | Where | Kills / confirms |
|---|---|---|---|
| 1 | **What is the total trust-note book** (not just the related-party subset)? | Annual statement Schedule D / NAIC InsData — **not** in the N-VPFS | Would make the deferred-interest share computable for the first time |
| 2 | **Does the FY2026 filing show deferred interest growing faster than NII?** | Next N-VPFS (~mid-2027) | 6.5% → materially higher = deterioration; flat = contractual, not credit |
| 3 | **Does non-admitted accrued income rise off $225K?** | Same | ⚠️ Weak test by construction (§4) — deferral is never "past due." Use only as a floor |
| 4 | **What did DLIC actually buy from CSLAC in 2025?** | CUSIP-level Schedule D — **not obtainable** (CSLAC has no EDGAR route; see the 7/27 addendum) | Would resolve impaired-vs-deferred directly |

⚠️ **Do not re-run the N-VPFS crawl for Athene** — the route does not reach it (tested and refuted 7/27).

---

## 7. NUMBERS DISCIPLINE

- ✅ **Primary, read directly:** all six affiliate transactions in §1; deferred interest **$159,580 / $114,223**; trust notes **$326,225 / $289,475**; SAFAs **$308,269 / $189,869**; PIK **$36,172 / $81,975**; non-admitted accrued income **$225 / $46**; NII **$2,446,596 / $1,806,782 / $1,243,551**; the $16.37B composition table.
- ⚠️ **DO NOT call the 9.77% a PIK finding** — PIK is separately disclosed and fell 55.9%.
- ⚠️ **DO NOT cite the $225K non-admitted figure as evidence the affiliate book performs** — deferred interest is never "past due" by construction.
- ⚠️ **DO NOT divide $159,580 by $326,225** and report 49% as a yield — the populations differ; the denominator is undisclosed.
- ⚠️ **NO write-down was taken; surplus was not restated; no charges have been filed.**
- ⚠️ **Mark Walter is a person** — never bare "WALTER."
