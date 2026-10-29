# H3: Eagle Bancorp (EGBN) and Valley National (VLY), Q3 2026: CRE, office and multifamily (for CREED)

Pulled 2026-10-28. Read-only; no repo files edited. Tiers: **PRIMARY-READ** means I read it in the filing or the FDIC API myself. **FLEET-PRIMARY** means REGINALD's reader extracted it from the primary and I did not re-read it. **SECONDARY** means anything else. **DERIVED** means my own arithmetic on printed figures, not a company disclosure.

## 0. What the fleet already holds (do not duplicate)

| Surface | Contents |
|---|---|
| `AGENTS/REGINALD/research/EGBN/sources/2026-10-22_Q3_8K/egbn_q3_extract.md` | Full EGBN Q3 8-K extract (release and all 31 deck slides): asset quality, office, multifamily, HFS, funding, named loans. **Covers almost everything CREED asked about EGBN.** |
| `AGENTS/REGINALD/research/EGBN/data/EGBN_asset_quality_quarterly.tsv` | EGBN Q3-25 / Q2-26 / Q3-26 series |
| `AGENTS/REGINALD/domain/sources/2026-10-22_catchup/vly_q3_extract.md` | Full VLY Q3 8-K extract (release and 38 slides): past dues, nonaccrual, ACL by segment, charge-offs, maturity outcomes, multifamily and office detail |
| `AGENTS/REGINALD/reports/2026-10-22_catchup/REPORT.md` §3–4 | REGINALD's verdicts. VLY: "Q2 early flag STRENGTHENS (bank-specific)" (CRE problem loans up while quantitative CRE reserves were released for a second quarter). EGBN: Prince George's $56.0M multifamily loan went to nonaccrual and was extended to 12/21/26; Q4 multifamily wall $265.7M. |
| `AGENTS/REGINALD/reports/2026-09-27_VLY_CRE_transmission.md` row 101 | The source of the $9.4M → $101.5M figure: **Call Report**, not the 10-Q |
| REGINALD predictions REG-28/29/30 | EGBN "extend, not exit" 65%; cohort Q4 net charge-off rise 45%; VLY nonaccrual ≥ $511.4M at 12/31 60% |
| REGINALD STATUS evidence limits | "VLY modifications and MF buckets await the 10-Q (~11/10)" |
| BOARD SIG-W-20261022-011 | WALTER's sweep of the VLY headline figures |

What REGINALD did **not** have, and this file adds: the Call Report decomposition below. It identifies the Q2 VLY commercial real estate 30–59 day bucket as almost entirely multifamily, which converts the Q3 release's "three CRE loans" into a multifamily read.

## 1. VLY, WQ-311: the multifamily 30–89 day past-due cohort

### 1a. The baseline is Call Report data (PRIMARY-READ, FDIC BankFind API, Valley National Bank cert 9396, $K)

| Field | 9/30/25 | 12/31/25 | 3/31/26 | **6/30/26** |
|---|---|---|---|---|
| Multifamily 30–89 days past due (P3REMULT) | 9,543 | 1,608 | 9,362 | **101,497** |
| Multifamily 90+ days, still accruing (P9REMULT) | 0 | 0 | 0 | **5,454** |
| Multifamily nonaccrual (NAREMULT) | 70,237 | 76,250 | 62,574 | 61,550 |
| Multifamily net charge-offs, year to date (NTREMULT) | – | 7,934 (full year 2025) | 4,335 | 9,397 (so Q2 alone ≈ 5,062, DERIVED) |
| Non-owner-occupied CRE 30–89 days (P3RENROT) | 21,186 | 70,229 | 40,849 | **0** |
| Owner-occupied CRE 30–89 days (P3RENROW) | – | – | – | 4,537 |
| Multifamily loans (LNREMULT) | – | 8,571,713 | 8,588,462 | 9,034,186 |

The FDIC index is dated 2026-08-19, so it holds no Q3 Call Report yet. Q3 Call Reports are due 10/30; the FDIC API refreshes later than that.

### 1b. Reconciliation to the Q2 10-Q (PRIMARY-READ: 10-Q acc 0000714310-26-000041, past-due table and MD&A)

The 10-Q prints "Commercial real estate" 30–59 days at **$106,034K** and 60–89 days at **nil**, at 6/30/26.

Call Report: multifamily 101,497 + owner-occupied 4,537 + non-owner-occupied 0 = **106,034**. That is an exact match (DERIVED). **So the 10-Q's Q2 CRE 30–59 bucket was 95.7% multifamily.** The rest was owner-occupied.

The 10-Q's CRE 90+ figure of $5,454K is the same number as the Call Report's multifamily 90+ figure. So the Q2 10-Q sentence *"migration of a $5.5 million commercial real estate loan previously reported in the 30 to 59 days past due delinquency category at March 31, 2026"* describes a **multifamily** loan.

The 10-Q itself calls the Q2 jump *"mainly due to certain larger commercial real estate loans"* (MD&A) and, in the highlights, *"a few larger CRE loans within the 30 to 59 days past due delinquency category."* The 10-Q never uses the word multifamily for these loans. Its loan table footnote says only: *"Includes loans collateralized by properties that are greater than 50 percent rent regulated totaling approximately $559 million"* at 6/30/26.

### 1c. What happened in Q3 (PRIMARY-READ: VLY Q3 8-K acc 0000714310-26-000045, EX-99.1, read 10/28)

Verbatim:
- *"Loans 30 to 59 days past due decreased $41.7 million to $109.3 million at September 30, 2026 as compared to June 30, 2026 primarily due to the migration of three CRE loans totaling $24.7 million, net of partial charge-offs of $9.1 million during the third quarter 2026, to non-accrual loans at September 30, 2026, as well as lower residential mortgage loan delinquencies."*
- *"Loans 90 days or more past due and still accruing interest increased $1.3 million to $17.3 million ... largely due to the third quarter 2026 migration of a $4.0 million CRE loan previously reported in the 30 to 59 days past due delinquency category at June 30, 2026"*
- *"Loans 60 to 89 days past due increased $14.8 million to $27.9 million ... mainly due to one CRE loan relationship totaling $10.9 million and higher residential mortgage loans delinquencies."*
- *"Non-accrual CRE loans decreased $3.0 million to $253.1 million ... primarily reflecting repayments and partial charge-offs, partially offset by the migration of three CRE loans previously reported as loans 30 to 59 days past due at June 30, 2026 to non-accrual status"*
- *"(ii) partial charge-offs totaling $9.1 million related to the aforementioned three non-accrual CRE loans totaling $24.7 million, net of the charge-offs, with no related allocated reserves within our allowance for credit losses"*

The release's asset-quality table for CRE (excluding construction), $K:

| Bucket | 6/30/26 | 9/30/26 |
|---|---|---|
| 30–59 days | 106,034 | 72,568 |
| 60–89 days | — (nil) | 10,869 |
| 90+ days, accruing | 5,454 | 10,295 |

### 1d. Answer to WQ-311: the cohort partly rolled to nonaccrual, and part of it persists or is unplaced

**Rolled to nonaccrual: at least about $29.3M of the multifamily cohort** (DERIVED bound). The three loans came out of the 6/30 CRE 30–59 bucket at $33.8M gross ($24.7M net plus $9.1M partial charge-offs). That bucket held only $4.5M that was not multifamily, so at least $29.3M of the $33.8M must have been multifamily. The company does not state the property type of the three loans.
- They took about **27% partial charge-offs** ($9.1M on $33.8M, DERIVED) and carried **no allocated reserves**.
- Most of VLY's Q3 CRE gross charge-offs of $19.1M is these three loans.

**Moved to 90+ accruing: $4.0M.** It is multifamily or owner-occupied; which one is not determinable.

**Remainder: about $64–68M (DERIVED) is unplaced.** It may have cured, paid off, or still be past due. 9/30 CRE 30–59 is $72.6M and 60–89 is $10.9M (one relationship), but **the 9/30 property mix is not disclosed.** The Q3 Call Report (multifamily 30–89, 90+ and nonaccrual at 9/30) is the instrument that settles it. It is due 10/30, and the 10-Q is due around 11/10.

**The $5.454M Q2 multifamily 90+ loan:** its Q3 status is not stated. 9/30 CRE 90+ is $10.3M; $4.0M of that is the new loan and the other $6.3M is not explained.

**Location (NYC rent-regulated, New Jersey, Florida, etc.): NOT DISCLOSED** for any of these loans in the release, the deck or the Q2 10-Q.
- Context, Q3 deck slide 31 (PRIMARY-READ): non-co-op multifamily $7.3bn = NY outside Manhattan $2.2bn (LTV 66%, DSCR 1.29x) · Other $1.5bn · NJ $1.5bn · FL & AL $1.2bn (60% / 1.45x) · Manhattan $0.8bn (62% / 1.28x). Co-ops $1.8bn. NYC multifamily $3.1bn by share of rent-regulated units: 0% of units 46% · 1–20% 7% · 21–50% 30% · 51–99% 6% · 100% 11%.
- **Inference, not disclosure:** the weakest coverage sits in NY outside Manhattan and in Manhattan (DSCR 1.28–1.29x), so that is the likely home. Do not cite it as fact.

**Net read for CREED (ANALYTICAL):** the Q2 "one unplaced signal" was real multifamily stress, and about a third of it reached nonaccrual within one quarter, at roughly a 27% partial loss severity. It looks concentrated: three loans averaging about $11M gross, against a non-co-op average loan size of $6.6M. That points toward idiosyncratic or bank-specific. It does not show broad spread. **Location remains unknown, so the NYC rent-regulated vs national-multifamily tie-break is still open.**

### 1e. Other VLY Q3 CRE items (FLEET-PRIMARY, from REGINALD's extract; spot-checked against the release text)

| Item | Figure |
|---|---|
| Nonaccrual: total / CRE / construction | $511.4M (0.96% of loans) / $253.1M / $39.3M. Construction includes a $30.1M loan, "well-secured", no specific reserve. |
| Net charge-offs | $37.1M (0.28% annualized). CRE net charge-offs about $18.4M (DERIVED). Largest single item: an $11.6M C&I partial charge-off. |
| Provision | $30.7M |
| ACL / loans | 1.13% (Q2 1.16%) |
| CRE allowance (ex-construction) | 0.90% (Q2 0.96%) |
| CRE including construction allowance | $299.4M, down $19.7M. The release cites *"a decline in quantitative reserves largely within certain CRE loan categories, including construction loans"*. |
| ALL / nonaccrual | 113.6% (Q2 127.7%) |
| Criticized and classified | $3.8bn, 7.1% of loans (CRE $3.0bn). No special-mention vs substandard split. |
| Office | $3.0bn (LTV 63%, DSCR 1.79x). FL & AL $1.1bn (58% / 1.88x); Manhattan $0.2bn. **Office nonaccrual and past dues are not disclosed.** |
| Q3 CRE maturities | $1,408M maturing: $1,242M retained, $162M paid off and left, $4M modified. 4Q26 maturities $1,857M. |
| OREO | $1.7M |
| Loan or note sales | None disclosed |
| Modifications to borrowers in financial difficulty, and re-defaults of the Q2 payment-delay modifications ($108M) | **Not disclosed** until the 10-Q |

### 1f. VLY Florida (PRIMARY-READ, Q3 deck slide 30 and release, for CORAL)

| Item | Figure |
|---|---|
| CRE by geography | Florida is **28%** of the $28.0bn CRE book (pie chart). Table row "Florida / Alabama" **$7.7bn**, LTV 60%, DSCR 1.80x, the strongest DSCR of any region. |
| Multifamily FL & AL | $1.2bn (slide 31): 16% of non-co-op multifamily, average loan $4.0mm, 60% / 1.45x |
| Office FL & AL | $1.1bn, 58% / 1.88x (slide 32, via REGINALD) |
| Release text | Q3 CRE growth was driven by *"new owner occupied CRE loan originations from our healthcare vertical and the Florida market, as well as an uptick in construction loan advances primarily in New York and Florida."* |

**No Florida-specific delinquency, nonaccrual or charge-off is disclosed.** The location of the $30.1M construction nonaccrual is not stated. Q3 construction advances were "primarily New York and Florida", but that does not place the loan.

## 2. EGBN Q3 (FLEET-PRIMARY: REGINALD's extract of 8-K acc 0001050441-26-000110; I did not re-read the release)

| Item | Figure |
|---|---|
| Nonperforming loans | $166.0M (Q2 $111.1M). NPAs 1.75% of assets. **OREO $0.** |
| Nonaccrual inflow | $73.7M, of which 76.0% came from one multifamily loan. That loan = Prince George's apartments **$56.0M**: LTV 88%, DSCR 0.74, maturity extended to 12/21/26. Its reserve is not disclosed. |
| Net charge-offs | $4.2M (0.25%), down from Q2 $47.9M |
| Provision | $2.8M |
| ACL | $120.8M, 1.84% of loans. **ACL / nonperforming loans 72.75% (Q2 109%).** |
| Office overlay | Released. Performing-office coverage 4.86% (Q2 7.22%). Reserves on income-producing office $23.8M. |
| Office book | Total CRE office $659.3M. Income-producing office $523.5M, of which $47.3M is criticized (all substandard). |
| Office nonaccrual > $5M | Fairfax $18.5M (matured 2/28/26, DSCR −0.56) · DC $15.5M · Fairfax $5.9M |
| Office maturities | 2026: $69.2M |
| Income-producing multifamily | $574.8M (Q2 $691.9M): 43.1% criticized, 11% nonaccrual. **$265.7M matures 4Q26.** Geography: DC 45% / VA 28% / MD 20%. |
| Large criticized apartment loan | DC $20.5M at **LTV 152%, DSCR 0.24**, matures 12/30/26 |
| Criticized and classified (incl. HFS) | $648.4M (Q2 $759.6M). Criticized/classified / Tier 1 = 53.5%. Only 73.9% of criticized loans are performing. |
| 30–89 days past due | **$357K** (Q2 $44.1M) |
| Held for sale | $13.5M (Q2 $49.7M). Q3 sales $34.6M with no gain or loss. Valuation allowance $1.5M. **No new HFS transfers.** |
| Capital | CET1 14.99%. CRE concentration 245.8%. |

**One small addition (PRIMARY-READ, Call Report, EagleBank cert 34742, $K, 6/30/26):**

| Field | Figure |
|---|---|
| Non-owner-occupied CRE 30–89 days | **42,704** |
| Multifamily 30–89 days | 0 |
| Multifamily nonaccrual | 35,891 |
| Non-owner-occupied nonaccrual | 42,136 |
| Multifamily net charge-offs, H1 | 20,282 |
| Non-owner-occupied net charge-offs, H1 | 24,261 |

So EGBN's Q2 $44.1M past-due figure was almost entirely non-owner-occupied CRE, not multifamily. That bucket fell to $357K by 9/30, but where it went (cured, paid off, or into the $73.7M nonaccrual inflow) is **not disclosed**. If it went to nonaccrual, it would sit inside the roughly $17.7M of inflow not explained by the Prince George's loan (DERIVED). **EGBN's 10/22 call has not been heard. EGBN's 10-Q has not been filed** (EDGAR checked 10/28; Q2 10-Q was filed 8/6).

## 3. Open gaps and where they resolve

| Gap | Resolves in |
|---|---|
| 9/30 multifamily 30–89 / 90+ / nonaccrual at VLY and EGBN, which settles the cure vs persist question numerically | **Q3 Call Report (RC-N), due 10/30.** Then the FDIC API, or FFIEC CDR for an earlier read. |
| VLY property type and location of the three loans and the $10.9M relationship; modification table; re-defaults of payment-delay modifications | VLY 10-Q, around 11/6–11/10 (the Q2 10-Q was filed 8/6) |
| VLY 10/22 call transcript | Not obtained. Gurufocus returned 403; no free transcript found (SECONDARY sources only). |
| EGBN 10/22 call transcript | Not read by anyone in the fleet |
