# DRAFT — narrow public-records request to Florida DBPR (NOT SENT; for Will's review)

**Status:** DRAFT ONLY. Not submitted. No fee authorized. No contact made. Prepared 2026-09-28 late (CORAL) from the gaps found in `dbpr_ucc_sample_test_2026-09-28.md`.
**Addressee (if sent):** Florida Department of Business and Professional Regulation, Division of Florida Condominiums, Timeshares and Mobile Homes — Public Records Coordinator (Chapter 119, F.S.).
**Why narrow:** the public surfaces already give the spine (five county CSVs: project PR#, managing-entity MA#, name, address, units — ~28,000 rows). What is NOT public is (i) the Building & Assessment Information submissions collected under s. 718.501(3)(c) and (ii) the SIRS Reporting Form's "Financial Information" page (planned special assessment / loan / line of credit and amount). Neither names a lender; the request therefore asks for exactly those two datasets, keyed to MA#, and nothing else. Nothing in DBPR's collection can supply loan balances, funding, default or maturity — do not ask for what the Division does not hold.

---

## Request text (draft)

> Under Chapter 119, Florida Statutes, I request the following public records held by the Division of Florida Condominiums, Timeshares and Mobile Homes, in electronic form (CSV or Excel), keyed by Managing Entity number (MA#) and Project number (PR#) where available:
>
> **1. Building and Assessment Information submissions** made by condominium associations through the Division's online account under s. 718.501(3)(c), F.S., for reporting years 2024, 2025 and 2026 — specifically the fields: amount of assessment or special assessment by unit type (including reserves); purpose of the assessment or special assessment; total annual amount collected from unit owners; total amount of reserves collected; number and amount of special assessments issued (current year and next year anticipated); and the names of the financial institutions with which the association maintains accounts.
>
> **2. Structural Integrity Reserve Study (SIRS) Reporting Form submissions** — the "Financial Information" page fields only: cost of the SIRS to the association; amount currently held in reserves; whether the reserve schedule results in a special assessment, loan, or line of credit (or reserves are sufficient); and the amount of any such special assessment, loan, or line of credit — for all submissions received to date, in the same layout the Division uses for its public SIRS Reporting Database.
>
> **3. Record layout / data dictionary** for items 1 and 2, and a statement of coverage (number of associations that have submitted each form, by county, as of the extract date).
>
> **Scope option (smaller):** if a statewide extract is burdensome, please provide items 1 and 2 for the following nine managing entities only: MA00007596 (Green Terrace), MA64878 (Ocean Five), MA00023691 (Sunset Palm Villas), MA00019742 (Dockside at Ventura), MA00016361 (Orlando International Resort Club), MA00024870 (Grande Isle Towers I & II), MA63899 (Windmill Lakes V), MA00015862 (The Gardens of Forest Lakes), and any managing-entity record for Palm Greens at Villa Del Ray Recreation Condominium Association, Inc. (Delray Beach).
>
> Please provide a cost estimate before incurring any charge above the statutory minimum; I do not authorize charges without prior written approval. If any field is exempt or confidential, please cite the exemption and provide the remainder.

---

## What this request CAN and CANNOT deliver (so the result is read correctly)

| Fact | Would this request deliver it? |
|---|---|
| Which associations have PLANNED to borrow (loan / LOC) to fund SIRS reserves, and how much | **Yes (item 2)** — planned, self-reported, no lender name |
| Special-assessment amounts and purposes by association | **Yes (item 1)** — self-reported |
| Where associations keep deposit accounts | **Yes (item 1)** — depository institutions, **not lenders** |
| Lender identity | **No** — not collected by DBPR (UCC / county records only) |
| Committed amount, funded amount, balance, default, maturity | **No** — not collected by DBPR |
| Reserve balance | **Partial** — the SIRS form asks "how much does the association currently have in reserves"; the Building & Assessment form's "reserves collected" is an annual flow |

**Join path for any result:** DBPR MA# ↔ DBPR CSV spine (name, address, units) ↔ UCC debtor name via normalized-name match (CONDO→CONDOMINIUM, ASSN→ASSOCIATION, drop THE/punctuation) — 8/9 in the sample joined this way, 0/9 on a shared identifier. County official records (mortgages, assignments of assessments) are a third, county-by-county system and are NOT covered here.

*Approval to send, and any fee, is Will's. Sending this changes nothing about the association-bankruptcy count, which stays descriptive and ungraded.*
