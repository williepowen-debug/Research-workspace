# DRAFT — narrow public-records request to Florida DBPR (NOT SENT; for Will's review)

**Status:** DRAFT ONLY. Not submitted. No fee authorized. No contact made. Prepared 2026-09-28 late (CORAL) from the gaps in `dbpr_ucc_sample_test_2026-09-28.md`; **re-scoped the same night on CATO's review (Will-adopted): schema and a small named sample FIRST, statewide only as a later, separate step.**
**Addressee (if sent):** Florida Department of Business and Professional Regulation, Division of Florida Condominiums, Timeshares and Mobile Homes — Public Records Coordinator (Chapter 119, F.S.).
**Why this shape:** the public surfaces already give the spine (five county CSVs: PR#, MA#, name, address, units — ~28,000 rows). Not public are (i) the Building & Assessment Information submissions collected under s. 718.501(3)(c) and (ii) the SIRS Reporting Form's "Financial Information" page — which **does** collect a current reserve BALANCE and the planned special-assessment / loan / line-of-credit AMOUNT (DBPR instructions), though never a lender name, a funded loan balance, or a loss. A request that starts statewide buys volume before we know whether the fields are usable; this one buys the schema and nine rows first.

---

## Request text (draft) — STEP 1 only

> Under Chapter 119, Florida Statutes, I request the following public records held by the Division of Florida Condominiums, Timeshares and Mobile Homes, in electronic form (CSV or Excel):
>
> **A. Record layout / data dictionary** for (i) the **Building and Assessment Information** submissions made through the Division's online account under s. 718.501(3)(c), F.S., and (ii) the **Structural Integrity Reserve Study (SIRS) Reporting Form** submissions — including every field name, data type, and the meaning of each status code; and, for each dataset, the **metadata fields** the Division stores per submission: reporting period, date/time submitted, date/time last updated, whether the record was amended or superseded, and the submitting account's Managing Entity number (MA#) and Project number(s) (PR#).
>
> **B. The complete submissions (all years held), with the metadata in A,** for the following nine managing entities only: MA00007596 (Green Terrace Condominium Association), MA64878 (Ocean Five Condominium Association), MA00023691 (Sunset Palm Villas Condominium Association), MA00019742 (Dockside at Ventura Condominium Association), MA00016361 (Orlando International Resort Club Condominium Association), MA00024870 (Grande Isle Towers I & II Condominium Association), MA63899 (Windmill Lakes V Condominium Association), MA00015862 (The Gardens of Forest Lakes Condominium Association), and any managing-entity record for Palm Greens at Villa Del Ray Recreation Condominium Association, Inc. (Delray Beach) — for both datasets in A. If a submission for an entity does not exist, please say so explicitly for that entity and dataset.
>
> **C. Coverage statement:** the number of condominium associations that have submitted each form, by county, as of the extract date, and whether the Division maintains a statewide extract of either dataset (yes/no; if yes, its record count and the fee to produce it — **for information only; no statewide extract is requested at this time**).
>
> Please provide a cost estimate before incurring any charge above the statutory minimum; I do not authorize charges without prior written approval. If any field is exempt or confidential, please cite the exemption and provide the remainder.

**STEP 2 (not requested; decided only after Step 1 is read):** a statewide extract of one or both datasets, if the Step 1 schema shows usable fields, timestamps and amendment status.

---

## What this request CAN and CANNOT deliver (so the result is read correctly)

| Fact | Would Step 1 deliver it? |
|---|---|
| Which of the nine PLANNED to borrow (loan / LOC) to fund SIRS reserves, and how much | **Yes (SIRS form)** — planned, self-reported, no lender name |
| Current reserve balance | **Yes (SIRS form: "how much does the association currently have in reserves")** — self-reported, as of the submission date; the Building & Assessment form's "reserves collected" is an annual flow, not a balance |
| Special-assessment amounts and purposes | **Yes (Building & Assessment form)** — self-reported |
| Where associations keep deposit accounts | **Yes (Building & Assessment form)** — depository institutions, **not lenders** |
| Whether the record is current, amended or stale | **Yes, if the Division stores it (metadata in A)** — this is the point of asking for the schema first |
| Lender identity | **No** — not collected by DBPR (UCC / county records only) |
| Funded loan balance, committed vs drawn amount, default, maturity, loss | **No** — not collected by DBPR |

**Join path for any result:** DBPR MA# ↔ DBPR CSV spine (name, address, units) ↔ UCC debtor name via normalized-name match (CONDO→CONDOMINIUM, ASSN→ASSOCIATION, drop THE/punctuation) — 8/9 in the sample joined this way, 0/9 on a shared identifier. County official records (mortgages, assignments of assessments) are a third, county-by-county system and are NOT covered here.

*Approval to send, and any fee, is Will's. Sending this changes nothing about the association-bankruptcy count, which stays descriptive and ungraded, and it does not by itself establish or refute any bank exposure.*
