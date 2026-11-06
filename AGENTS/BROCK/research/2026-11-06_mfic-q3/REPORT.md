# MFIC Q3-2026 read and ARCC shared-borrower re-run, 9/30/2026

BROCK, 2026-11-06, on Will's word ("can you handle these gaps now?"). Resolves the 11/06 CATALYSTS row. No score, level, gate or trade changed.

## Sources
| Doc | Accession | Instrument sha256 |
|---|---|---|
| MFIC Q3 10-Q (filing date 11/05) | 0001193125-26-447829 | 72d50e14b685cc752fc38eca7f0c5dd4821c2e37862d4d0d8d5049f829066d9c |
| MFIC 8-K 2.02 + Ex 99.1, 11/05 | 0001193125-26-448373 | n/a |
| MFIC Q2 10-Q (control: sha matches the 10/29 study) | 0001193125-26-335848 | 68e480f58de9f27547adc6b3c1a8f7a5f098c38635ded6e320ec7a7b9c250e75 |
| ARCC Q3 10-Q, 10/27 | 0001628280-26-067383 | a79405ddd37740cab50e3902422cc32a35073306d3ddf4e7cdd985baf388d432 |

Call not read. Apollo's or Ares's view of any name below is unknown.

## 1. NAV, income, dividend (separate passes)
| Item | 9/30/26 | 6/30/26 | Basis, source |
|---|---|---|---|
| NAV per share | $12.86 | $13.37 | −3.81%, Ex 99.1. Final equals the ~$12.86 preliminary to the cent |
| NII per share | $0.34 | $0.40 | Ex 99.1 |
| Dividend declared 11/04 | $0.31 | $0.31 | 1.10x on $0.34 [DERIVED]; held. Cut from $0.38 on 5/5 (KB-BRK-143) |
| Total investment income, quarter | $62.0M | | $82.6M a year earlier, −24.9% [DERIVED] |
| Net realized / unrealized, quarter | −$29.1M / −$14.9M | | 10-Q MD&A |
| Portfolio FV | $2,545.1M | $2,770.3M | balance sheet |
| Portfolio cost | $2,852.0M | $3,061.8M | balance sheet |
| FV/cost | 0.892 | 0.905 | balance-sheet basis. 0.900 / 0.912 if rows with no FV fact are dropped, the 10/29 study's basis |
| Debt/equity · net leverage | 1.49x · 1.43x | 1.58x · 1.54x | Ex 99.1. Falling because repayments exceed new loans: $189M net repaid, $0.9M new commitments |
| Asset coverage | ~166.9% | | (net assets $1,059.3M + debt $1,583.0M) / debt [DERIVED], not an issuer-stated figure. BRK-11 line is 150% |

## 2. Non-accruals (own pass, not from the summary)
Issuer: **7.9% of the "total debt portfolio at amortized cost"**, from 4.4% a year earlier (10-Q MD&A).

| Basis | 9/30/26 | 6/30/26 |
|---|---|---|
| Cost, SOI footnote 14 | $226.2M = 7.9% of total investments | $141.4M = 4.6% (ties to issuer, KB-BRK-283) |
| Fair value, SOI footnote 14 | $144.8M = 5.7% of total investments | $80.2M = 2.9% (issuer 2.8%, KB-BRK-283) |

⚠️ The issuer's sentence says debt portfolio; the SOI sum only reproduces 7.9% against TOTAL investments. Quote the denominator with the number. The percentages above are DERIVED from the SOI; the cost share ties to the issuer at both dates, which is the parser check.

| New on non-accrual in Q3 | Cost $M | FV $M | FV/cost |
|---|---|---|---|
| LendingPoint LLC | 39.0 | 16.4 | 0.42 |
| Thomas Scientific | 35.0 | 26.8 | 0.77 |
| Heniff Holdco | 32.7 | 28.6 | 0.87 |
| Magnate Holding | 21.4 | 17.2 | 0.80 |
| Kauffman Engineering, restructured successor | 3.2 | 3.2 | 1.00 |
| CSC Holdings | 1.6 | 1.0 | 0.59 |
| **Total new** | **132.9** | **93.2** | **0.70** |

Off the list: Kauffman Intermediate ($18.2M cost, restructured), Aventiv/Securus ($7.7M, restructured). Banner fell from $15.4M to $2.1M, also on restructuring (MD&A names Kauffman, Banner, Securus). Midwest Vision: non-accrual cost fell $23.3M to $12.1M and that remainder is at FV zero.

**Inference, not a filed fact:** Thomas, Heniff and Magnate carry 0.81 of cost combined ($72.6M on $89.1M) while on non-accrual, so they are where further MFIC markdown would most plausibly come from. A mark can be right on a non-accrual loan; I have not read these credits.

## 3. Tail marks, 9/30 vs 6/30
| Name | FV/cost 6/30 | FV/cost 9/30 | Q3 unrealized (MD&A) |
|---|---|---|---|
| ChyronHego | 0.69 | 0.46 | −$15.6M, largest in the quarter |
| LendingPoint LLC only (label corrected 11/06 on OTTO, card 039; whole relationship 0.64 to 0.54, and the −$5.9M is whole-relationship) | 0.54 | 0.40 | −$5.9M |
| US Auto pool | 0.40 | 0.11 | −$5.1M |
| Tasty Chick'n | 0.62 | 0.32 | −$3.9M |
| Thomas Scientific | 0.89 | 0.77 | −$4.2M |
| Carbonfree SPE | 0.26 | 0.24 | not listed |
| K&N · Renew | 0.02 · 0.01 | 0.02 · 0.01 | already near zero |

The reading guide said lower tail marks or NAV under $12.86 mean haircut migration. **NAV leg: no. Tail leg: marks are lower than 6/30, but they are inside the $12.86 Ares and the market already had, so this is not migration past the deal price.** The new public fact since the deal is the non-accrual list, not the NAV. Whether Ares had that list in diligence is unknown.

## 4. ARCC shared-borrower re-run
Method and PAIRS.tsv unchanged. Ties: MFIC FV $2,545.2M vs $2,545.1M, ARCC FV $29,229.7M vs $29,212.6M (0.06% over). Output: `rerun_output.txt`.

| | 6/30 | 9/30 |
|---|---|---|
| n | 12 | 12 |
| MFIC − ARCC, median | −0.14pp | −0.02pp |
| MFIC − ARCC, MFIC-cost weighted | −0.36pp | −0.31pp |
| Range | −5.5 to +4.1pp | −6.3 to +4.2pp |
| Shared MFIC debt cost | $164.8M, 5.4% | $165.4M, 5.8% |
| Shared FV/cost vs whole book | 0.990 vs 0.912 | 0.992 vs 0.900 (no-FV rows dropped, same basis) |

Same answer as 10/29: "eye to eye" holds where it can be tested and cannot be tested where it matters. **A name search of ARCC's 9/30 schedule finds none of LendingPoint, Thomas Scientific, Heniff, Magnate, Bird/Blue Jay, Tasty Chick'n, Munson, Simeio, Midwest Vision or Naviga**, so no name in the problem list has an Ares cross-mark. A name search can miss a differently named borrower. A shared borrower is not proof of the same tranche.

## 5. Ladder and grading
- Ladder row 6 (>5%): **NOT FIRED**, −3.81%.
- 🔧 **Correction:** KB-BRK-451 and the ladder called GSBD −2.99% the "worst filed" and I told Will the same. MFIC's −3.8% was already in KB-BRK-403 on 10/29. Worst among names read is MFIC −3.81%; the other listed BDCs were not all read. Row 6's Q2 note "max FSK −2.81%" sits beside MFIC −3.20% in KB-BRK-210; neither reaches 5%.
- BRK-11: MFIC ~166.9%, not a breach. Convergence unchanged, 58/70.
