# ARCC vs MFIC shared-borrower marks, 6/30/2026 (tests ARCC's "eye to eye on the marks")

BROCK, 2026-10-29 ~00:01–00:05 ET, at Will's request. Primary XBRL + HTML from both Q2 10-Qs.

## Sources
| Filer | 10-Q accession | sha256 of the XBRL instance |
|---|---|---|
| ARCC | 0001628280-26-050307 | 15b49d7baf95233d6dffdac01aee7560e8232a0f2bf55f5f424265ffb8d92cec |
| MFIC | 0001193125-26-335848 | 68e480f58de9f27547adc6b3c1a8f7a5f098c38635ded6e320ec7a7b9c250e75 |

## Method
`extract.py` (positions per InvestmentIdentifierAxis context) → `compare.py` (first-SOI perimeter by HTML row order: ARCC row 1932, MFIC row 932; **ties exactly**: ARCC $29,349.3M, MFIC $2,770.3M) → `PAIRS.tsv` (curated) → `compare_pairs.py`. `mfic_tail.py` ranks MFIC markdowns by entity string.
Matching: an exact-name pass found 5; a two-token pass and a distinctive-word sweep (75 candidates, read by hand) brought it to **13 true pairs**. The rest were word collisions (Patriot, Safety, Funding...). DRS (Dr. Scholl's): MFIC holds no debt line, so n=12 compare. **A shared borrower is not proof of the same tranche or terms.** Debt = positions with cost>0 and FV>0 whose identifier names a debt instrument.

## Results
| Borrower | ARCC FV/cost | MFIC FV/cost | MFIC − ARCC (pp) | MFIC debt cost $M |
|---|---|---|---|---|
| ACP Avenu | 1.011 | 0.956 | −5.5 | 9.2 |
| Alcresta Therapeutics | 1.000 | 0.999 | −0.1 | 9.3 |
| Berner Food & Beverage | 1.000 | 0.995 | −0.5 | 35.7 |
| Cards-Live Oak | 1.000 | 0.995 | −0.5 | 4.3 |
| GS SEER | 0.898 | 0.940 | +4.1 | 4.5 |
| High Street | 1.000 | 1.002 | +0.2 | 28.7 |
| NCP-MSI | 1.000 | 0.979 | −2.1 | 9.1 |
| Shout! Factory | 0.984 | 0.996 | +1.2 | 13.3 |
| Silk (Suave) | 0.990 | 1.014 | +2.5 | 24.5 |
| Truck-Lite | 1.000 | 0.999 | −0.1 | 3.6 |
| Generator / Total Power | 1.000 | 0.977 | −2.3 | 14.3 |
| Zendesk | 0.970 | 0.929 | −4.1 | 8.3 |
**MFIC − ARCC: median −0.14 pp, MFIC-cost-weighted −0.36 pp, range −5.5 to +4.1.** MFIC marks the shared names slightly *below* ARCC, so it is not more generous on the same credits.

**Coverage limit (the main result):** the shared debt is $164.8M = **5.4% of MFIC's cost**, marked 0.990 against 0.912 for MFIC's whole book. The overlap is the healthy part, and the discount lives in the ~95% ARCC doesn't hold. ⇒ "Eye to eye" is **consistent where testable, but untestable where it matters.**

## Where MFIC's markdown sits (6/30 first SOI: cost $3,038.3M, FV $2,770.3M, net −$267.9M)
Top 10 entities = 63% of net markdown on 9.8% of cost; top 20 = 83% on 16.4% (≈$498M cost, ≈$275M FV). The worst: Carbonfree Chemicals SPE 0.26 · K&N 0.02 · ChyronHego 0.69 · LendingPoint 0.54 · Renew Financial 0.01 · US Auto pool 0.40 · Kauffman 0.40 · New Era Technology 0.06 · Banner 0.40 · Bird/Blue Jay 0.78. Entity strings split some company groups, so the ranking is approximate.

## Reading [DERIVED, illustrative]
ARCC's ~$263M equity haircut (KB-BRK-403) sits **on top of** MFIC's own −$267.9M of marks, because NAV already embeds them. Putting it all on the visible top-20 tail (~$275M FV) would value that tail near zero, which is implausible. So the price must also carry some mix of: weakness beyond the visibly marked tail; Q3 deterioration (NAV −3.8% to 9/30, partly inside $12.86 already); deal costs; and leverage over a stock trading at 65% of NAV. This method cannot apportion between them. The N-14 background, MFIC's Q3 SOI and ARCC's post-close purchase allocation can.
