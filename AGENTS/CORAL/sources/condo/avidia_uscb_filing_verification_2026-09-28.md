# Avidia Bancorp + USCB Financial Holdings — filing verification of the outside reviewer's association-lending figures

**Run:** 2026-09-28 ~20:1x ET (CORAL, Will's follow-up ③). **Method:** primary documents pulled from SEC EDGAR (`data.sec.gov` submissions index → filing primary document), tables parsed from the filing HTML; no aggregator. Reviewer's figures (relayed via Will at the 9/28 closeout) treated as LEADS and read at the source.

---

## 1. Avidia Bancorp, Inc. (NASDAQ: AVBC; CIK 0002058758; Avidia Bank, Hudson, Massachusetts)

**Filing:** Form 10-Q for the quarter ended **2026-06-30**, filed **2026-08-13**, accession `0001193125-26-349298`, primary document `avbc-20260630.htm`. Companion: Form 10-K for FY **2025-12-31**, filed 2026-03-27, accession `0001193125-26-129221`.

### 1a. Reviewer's claim → what the filing says

| Reviewer (lead) | Filing (verified) | Verdict |
|---|---|---|
| "$494.331M of association loans" at 6/30/2026 | Loan composition table (Note — Loans): **Condominium associations $494,331K at June 30, 2026** vs $506,683K at Dec 31, 2025 (−$12,352K, −2.4%). Segment = **21.9%** of total loans $2,257,379K | ✅ exact |
| "entirely current" | Aging analysis, June 30, 2026: Condominium associations — amortized cost $494,331K · **Current $494,331K · 30–89 days $0 · 90+ days $0 · total past due $0** | ✅ |
| "pass-rated" | Risk-rating-by-origination-year table, June 30, 2026: Condominium associations — **Pass (Rated 1–5, M, P) $494,331K = 100%**; no Special Mention, Substandard or Doubtful rows; **current-period gross charge-offs —** | ✅ |
| (not claimed) nonaccrual | Segment description (10-Q Note, verbatim): *"This portfolio has experienced almost no delinquency, with no nonaccruals or charge-offs since the Company has entered this niche."* | ✅ 0 nonaccrual |
| (not claimed) reserve | ACL on the segment **$2,809K at 6/30/2026 (0.57% of segment)**, down from $2,967K at 12/31/2025 via reversals (−$46K in Q2, −$158K YTD) | reserve RELEASING |

### 1b. Scope — the whole portfolio, NOT Florida-only

- **Loan category (10-Q, verbatim):** *"Condominium Associations: Loans in this segment are secured by the assignment of association fees and dues paid by the individual condominium unit owners. The funds are typically used for major improvements and repairs to the structures, landscape and parking lots or garages, and are repaid over 5 to 30 years."* ⇒ this IS the repair-loan category the CORAL bridge cares about (association borrowing for structural/common-area repairs).
- **Geography (10-K FY2025, Item 1, verbatim):** *"While our condominium association loans are primarily made to condominium complexes located in our primary market area and surrounding area, we have made loans to condominium complexes outside of our market area. At December 31, 2025, the three states in which we had the largest concentration of condominium association loans were **Massachusetts ($247.9 million), Florida ($78.4 million) and New York ($47.4 million)**. At December 31, 2025, the largest condominium association loan had an outstanding balance of **$22.8 million and it was performing according to its original terms. The condominium complex is located in Miami Beach, Florida.**"*
- ⇒ **Florida slice = $78.4M of $506.7M (15.5%) at 12/31/2025.** The 10-Q gives **no state breakdown**, so the 6/30/2026 Florida balance is UNKNOWN. What CAN be said: because the ENTIRE segment is 100% current and 100% pass at 6/30/2026, every subset of it — including whatever the Florida slice now is — is also current and pass. That is arithmetic, not a Florida disclosure.
- **Collateral (10-K):** assignment of unit-owner dues cash flows, assignment of the association's priority lien, assignment of rental income on rented units. Terms up to 30 years, fully amortizing. Lending since **2014**.
- **Vintage (10-Q, 6/30/2026 amortized cost by origination year):** 2026 $11,452K · 2025 $19,310K · 2024 $8,723K · 2023 $37,382K · **2022 $230,674K (46.7%)** · prior $186,790K. Descriptive; the 2022 concentration is noted, not interpreted.
- **Risk language (10-Q):** *"Credit quality would be affected if there is a significant population decline locally or regionally."*

### 1c. What this establishes for the CORAL bridge
A **baseline**: one SEC-registered bank with a large, disclosed, national condo-association REPAIR-loan book that includes a Florida concentration (~$78M at YE2025, largest loan Miami Beach) shows **zero past-due, zero nonaccrual, zero charge-off, 100% pass, reserve releasing** at 6/30/2026. **Counterevidence to bank-loss transmission as of mid-2026; not evidence about Florida associations in general** (the book is 84.5% non-Florida at YE2025 and underwritten by one lender). Next observable: 10-Q for 9/30/2026 (~mid-Nov 2026); 10-K FY2026 (~late Mar 2027) for the state breakdown.

---

## 2. USCB Financial Holdings, Inc. (NASDAQ: USCB; CIK 0001901637; U.S. Century Bank, Miami, Florida)

**Filing:** Form 10-Q for the quarter ended **2026-06-30**, filed **2026-08-07**, accession `0001562762-26-000090`, primary document `uscb-20260630.htm`. Companion: Form 10-K FY2025, filed 2026-03-13, accession `0001562762-26-000027`.

### 2a. Reviewer's claim → what the filing says

| Reviewer (lead) | Filing (verified) | Verdict |
|---|---|---|
| "only $2.148M of nonaccrual loans across the entire $2.317B loan portfolio" (June 2026 10-Q) | Aging table as of **June 30, 2026**: total loans **$2,316,695K** (accruing $2,314,547K + non-accrual **$2,148K**); 30–89 days past due $1,228K; 90+ & accruing $0. Non-accrual table: residential real estate $1,508K (1-4 family $1,284K; **condo residential $224K**) + C&I secured $640K = $2,148K. NPL/total loans **0.09%** (vs 0.14% at 12/31/2025, when non-accrual was $3,138K). ACL/total loans 1.15%. OREO $0 | ✅ exact |
| "its $68.7M 'condo commercial' category had no delinquency/nonaccrual" | Commercial real estate → **Condo commercial $68,666K: current $68,666K, 30–89 $0, 90+ $0, non-accrual $0** (12/31/2025: $61,525K, also clean). = 2.96% of loans | ✅ exact |
| (implied) that "condo commercial" = condo-ASSOCIATION lending | ⛔ **NOT SUPPORTED BY EITHER FILING.** Neither the 10-Q nor the 10-K defines "Condo commercial"; no loan-table category is labelled association/HOA. The 10-K DOES confirm USCB **originates loans to "condominium or homeowners' associations ('Associations')"** (Item 1A risk factor, verbatim: *"these loans are primarily secured by and rely upon the cash flow received by the Associations from payments received from their property owners, as well as cash on hand… our ability to recover amounts on non-performing loans made to Associations is dependent upon the Association having sufficient cash on hand… and/or having the ability to impose assessments on its property owners, some of whom may not have the ability to pay such assessments"*) and describes an HOA business line since **2016** ("deposit collection, lockbox services, payment services, and lending products"). **But the SIZE of the Association loan book and WHICH table category holds it are undisclosed.** "Condo commercial" may be commercial condominium units, association loans, or both — UNKNOWN. | ⚠️ scope UNKNOWN |

### 2b. What this establishes
- The two USCB numbers are exact and correctly dated (**June 30, 2026, 10-Q filed 2026-08-07**).
- **USCB's condo-association credit is structurally unobservable in its SEC filings** — the same conclusion CORAL reached from the Q2 releases (STATUS § FL BANK EXPOSURE). The "condo commercial" line is a clean CRE sub-category, **not a verified proxy for association lending**; do not cite it as one. USCB stays a canary only via an explicit disclosure of Association-loan deterioration, which none of its filings currently contains.
- Whole-bank asset quality is benign on every printed metric; that is the bank-rail read already on record (Q2 0-of-4), now re-dated to the filing.

---

## 3. Source-access log
| Source | Result |
|---|---|
| `data.sec.gov/submissions/CIK0002058758.json` (Avidia) | 200 — filer resolved, 10-Q/10-K accessions listed |
| `sec.gov/Archives/edgar/data/2058758/000119312526349298/avbc-20260630.htm` | 200 — 7.1 MB, 77 HTML tables parsed |
| `sec.gov/Archives/edgar/data/2058758/000119312526129221/avbc-20251231.htm` | 200 — state concentration passage read |
| `data.sec.gov/submissions/CIK0001901637.json` (USCB) | 200 |
| `sec.gov/Archives/edgar/data/1901637/000156276226000090/uscb-20260630.htm` | 200 — 3.8 MB; tables are div-laid-out (HTML `<table>` parser found 0), read from text |
| `sec.gov/Archives/edgar/data/1901637/000156276226000027/uscb-20251231.htm` | 200 — HOA business + Association risk factor read; no category definition found |

*Figures in thousands of dollars as printed unless stated. Nothing here changes a colour, a scenario weight, or the bank-transmission rail (NOT met, NOT armed).*
