# Is there a second bank shaped like United Fidelity? A 9/30/2026 Call Report screen of every insured bank
**Date:** 2026-11-27 (written 23:56 ET onward, from `date`) | **Mode:** Thesis | **Confidence:** High (filing cells, arithmetic) / Medium (criteria are fitted to one case) / UNKNOWN (enforcement at FDIC- and Fed-supervised banks)
**Commission:** PROME prome-80, plan leg 3 (`PROME/plans/2026-11-27_bank-failure-investigation-PLAN.md`, WQ-759 RULED A, class C9). Session dewey-2026-11-27-8654c74a. **Interpretation belongs to REGINALD**; this report finds and verifies.

## Key finding
**No lookalike.** On 9/30/2026 data, and on every quarter back to 9/30/2025, United Fidelity is the only insured bank that combined a multifamily-dominated loan book with a large real-estate venture book. Its venture holdings were 257% of total capital (146% at 6/30). The next-highest bank in the country is at 38%, and it is not a multifamily lender. Four small multifamily savings banks share two of its three structural features: a book over half multifamily at more than three times capital, and brokered funding above 15%. Those four are Piermont, DMB, Malaga and RiverHills. Only Piermont also shows fresh multifamily lateness (6.2% of its multifamily loans 30 to 89 days past due at 9/30, up from zero). **HOMER's five banks are not United Fidelity-shaped.** They are generalist commercial real estate lenders with multifamily at 7% to 18% of loans, no venture books and no capital stress. What they share is a jump in multifamily lateness this quarter.

**New fact, outside the screen but material to REGINALD's file:** the OCC's enforcement search, read 2026-11-27 at about 23:52 ET, now lists a **prompt corrective action directive against United Fidelity dated 09/17/2026 (AA-ENF-2026-42), amended 09/29/2026 (AA-ENF-2026-42A)**. Both were terminated on 11/27/2026. No document is posted. The OCC was therefore acting on the bank's capital before the 9/30 quarter closed. The 11/11 to 11/16 record carried "no directive under the prompt-corrective-action rules has ever been published"; that line is now overtaken.

## 1. The criteria, with United Fidelity's value on each, and the test on its own data

Source: FDIC BankFind financials API, the whole population at each date (4,284 rows at 9/30/2026, 4,314 at 6/30/2026; row count equals the API total, as the meta files record). Each FDIC field was mapped to its Call Report item and **verified cell for cell against United Fidelity's own 9/30 SDF filing**. The same check was run on 20 other banks' 9/30 SDF filings from DEWEY's 11/11 FFIEC archive: 21 banks and 16 cells each, with zero differences beyond $1K rounding on gross loans (`out/sdf-crosscheck.json`). Population: insured banks other than OI/NC classes, with loans at least 10% of assets (4,154 banks at 9/30).

| Feature (flag) | Threshold (DEWEY, set knowing UFB's values; looser than UFB) | UFB 6/30/2026 | UFB 9/30/2026 | Banks flagged 9/30 | Call Report item |
|---|---|---|---|---|---|
| A1 multifamily share of gross loans | ≥ 50% | 89.9% | 89.0% | 13 | RC-C 1.d / 2122 |
| A2 multifamily / total capital | ≥ 300% | 424% | 677% | 16 | 1460 / RC-R 3792 (CBLR banks: tier 1 + allowance) |
| B1 RE venture investments + unconsolidated subsidiaries / capital | ≥ 25% | 146% | 257% | 4 | RC 9 (3656) + RC 8 (2130) |
| B2 credit to insiders and their related interests / capital | ≥ 18.8% (population 90th percentile, 6/30 and 9/30) | 11.8% (80th pct) | 21.3% (92nd pct) | 419 | RC-M 1.a (6164) |
| C brokered deposits / deposits | ≥ 15% | 20.5% | 18.7% | 257 | RC-E M1.b (2365) |
| D smallest margin over a prompt-corrective-action "adequately capitalized" line (total 8, tier 1 6, CET1 4.5, leverage 4; CBLR banks leverage only) | < 2 points | +6.16 (leverage) | −0.74 (total) | 9 | RC-R 7205/7206/P793/7204 |
| E multifamily past due + nonaccrual / multifamily loans | ≥ 5%, or +2 points in one quarter (multifamily book ≥ $10M) | 0.00% | 78.75% | 121 | RC-N 1.d (3499/3500/3501) |
| F allowance / total nonaccrual | < 50%, with nonaccrual ≥ 1% of loans | 504% | 0.29% | 283 | 3123 / 1403 |
| G open enforcement order | short list only, read at the agencies' search pages | OCC consent order 2023-031 open | same, plus the PCA directive of 9/17, amended 9/29 | — | OCC EASearch |

**Not in the public file, and not proxied:** loans to affiliates (no Call Report item); loans to related sponsors that the bank does not report as insider credit (at UFB, the Pedcor and Birge & Held borrowers were about 46% of 2021 to 2025 origination dollars, PROME SYNTHESIS Addendum 2, yet reported insider credit was only $85.7M); related-party receivables (UFB's $146.7M fee receivable sits inside "other assets", RC-F, as free text); CD pricing (not on the form); underwriting, loan-to-value and collateral values. CRE loans not secured by real estate (RCx2746) and the CBLR election (RCOALE74) are not in the FDIC file. They were read from the SDF for the short list only: 2746 is at most $10.8M at any short-list bank, so the CRE ratios change very little.

**Test on United Fidelity's own history (FDIC five quarters; FFIEC bulk history in `PROME/reports/2026-11-11_united-fidelity-follow-up/F-quarterly-history.json` for 2021 to 2025):**

| Quarter | MF % loans | MF % capital | Ventures % capital | Brokered % deposits | MF past due + nonaccrual | Screen result |
|---|---|---|---|---|---|---|
| 12/31/2021 | 62.5 | 310 | 184 | 9.7 | $0 | A1 A2 B1 |
| 6/30/2022 | 80.7 | 488 | 119 | 25.1 | $0 | A1 A2 B1 C: all structural features, **17 quarters before closing** |
| 6/30/2024 | 87.3 | 486 | 134 | 42.2 | $0 | same |
| 9/30/2025 to 6/30/2026 | 89.4 to 89.9 | 424 to 442 | 140 to 146 | 31.7 to 20.5 | $121K to $298K | same; **rank 1 of the whole population at every date** |
| 9/30/2026 | 89.0 | 677 | 257 | 18.7 | $2,143.2M nonaccrual | all eight flags |

**What the test shows:** the screen finds United Fidelity on 6/30 data, and years earlier, but **only through its structure**. Its stress half (D, E, F) saw nothing until the quarter the loans went to nonaccrual. Multifamily lateness was at most $3.1M on a book of about $3B in every quarter from 2021 through 6/2026. A screen built to find trouble through delinquency could not have seen this bank coming. Feature B1, the venture book, is effectively United Fidelity's fingerprint: it is the only bank ever to combine B1 with A1 and A2 in the data read. A screen fitted to one case will always find that case, so it is no evidence that the screen has any power.
**Counter-test, the other 2026 failure in the data:** Nano Banc (cert 58590, failed 9/25/2026) shows the opposite pattern. At 12/31/2025, three quarters before closing, it already carried flags C, D, E and F: a 0.42-point capital margin, 24.3% of loans on nonaccrual and an allowance of 10% of nonaccrual. It had none of United Fidelity's structural features. The stress half of the screen catches a failure that is visible in its numbers; only the structure half catches one like United Fidelity, whose numbers stayed clean.

## 2. The short list (9/30/2026, ranked)

Eligibility: multifamily at least 100% of capital (194 banks), then ranked by flag count. Ranks 2 to 15 below. "Listed" means the bank or its parent is on the SEC's company ticker file (read 11/27); a ticker not in that file is not checked, so over-the-counter quotes are not covered.

| Rank 9/30 | Bank (cert) | Assets $B | Regulator | Listed | MF % loans | MF % capital | CRE % capital | RE ventures % capital | Insider % capital | Brokered % dep (q/q pts) | Capital margin, pts (line) | MF nonaccrual % | MF 30-89 % | MF stress q/q pts | Allowance % nonaccrual | Flags 9/30 | Flags 6/30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | United Fidelity Bank, fsb (Evansville, IN; cert 29566), reference | 5.92 | OCC | not in SEC ticker list | 89 | 677 | 687 | 257.2 | 21.3 | 18.7 (-1.8) | -0.74 total | 78.75 | 0.00 | 78.75 | 0 | A1 A2 B1 B2 C D E F | A1 A2 B1 C (rank 1) |
| 2 | Piermont Bank (New York, NY; cert 59154) | 0.51 | FDIC | not in SEC ticker list | 68 | 342 | 413 | 0.0 | 0.0 | 15.5 (2.6) | 6.31 cet1 | 0.00 | 6.19 | 6.19 | n/a | A1 A2 C E | A1 A2 (rank 15) |
| 3 | DMB Community Bank (Madison, WI; cert 14769) | 0.88 | FDIC | not in SEC ticker list | 69 | 483 | 565 | 0.0 | 0.7 | 19.9 (4.0) | 6.69 leverage | 0.00 | 0.00 | 0.00 | n/a | A1 A2 C | A1 A2 C (rank 5) |
| 4 | Malaga Bank F.S.B. (Palos Verdes Pen, CA; cert 32282) | 1.46 | OCC | not in SEC ticker list | 91 | 450 | 465 | 0.0 | 3.6 | 17.8 (0.2) | 12.85 leverage | 0.00 | 0.00 | 0.00 | n/a | A1 A2 C | A1 A2 C (rank 4) |
| 5 | RiverHills Bank (Milford, OH; cert 6662) | 0.33 | FDIC | not in SEC ticker list | 59 | 407 | 493 | 0.0 | 0.0 | 19.3 (-0.2) | 6.83 total | 0.00 | 0.00 | 0.00 | 866 | A1 A2 C | A1 A2 C (rank 6) |
| 6 | Universal Bank (West Covina, CA; cert 30722) | 0.39 | OCC | not in SEC ticker list | 60 | 218 | 326 | 0.0 | 2.0 | 17.4 (0.1) | 13.47 leverage (CBLR) | 0.00 | 0.00 | 0.01 | 30 | A1 C F | A1 C F (rank 8) |
| 7 | Modern Bank, National Association (New York, NY; cert 22398) | 0.65 | OCC | not in SEC ticker list | 24 | 163 | 241 | 0.0 | 0.0 | 15.3 (-11.3) | 5.58 leverage | 5.99 | 0.00 | 0.15 | 25 | C E F | C E F (rank 10) |
| 8 | OneUnited Bank (Boston, MA; cert 23966) | 0.66 | FDIC | not in SEC ticker list | 98 | 614 | 614 | 0.0 | 0.5 | 0.0 (-27.1) | 5.97 leverage (CBLR) | 0.06 | 0.00 | -0.32 | 512 | A1 A2 | A1 A2 C (rank 3) |
| 9 | Marquette Bank (Chicago, IL; cert 16250) | 2.03 | FED | not in SEC ticker list | 61 | 449 | 568 | 0.0 | 1.3 | 0.0 (0.0) | 4.58 leverage | 0.00 | 0.00 | 0.00 | 1,562 | A1 A2 | A1 A2 (rank 11) |
| 10 | First Federal Savings and Loan Association of San Rafael (San Rafael, CA; cert 31406) | 0.21 | OCC | not in SEC ticker list | 89 | 402 | 449 | 0.0 | 0.0 | 9.1 (-0.5) | 15.06 leverage | 0.00 | 0.00 | 0.00 | n/a | A1 A2 | A1 A2 (rank 12) |
| 11 | Genesis Bank (Newport Beach, CA; cert 59245) | 0.36 | FDIC | not in SEC ticker list | 63 | 374 | 438 | 0.0 | 0.0 | 0.3 (-3.4) | 7.68 leverage | 0.00 | 0.00 | 0.00 | 1,424 | A1 A2 | A1 A2 (rank 13) |
| 12 | Heritage Bank of Schaumburg (Schaumburg, IL; cert 21721) | 0.15 | FDIC | not in SEC ticker list | 73 | 355 | 365 | 0.0 | 11.6 | 0.0 (0.0) | 6.89 leverage | 0.00 | 0.00 | 0.00 | n/a | A1 A2 | A1 A2 (rank 14) |
| 13 | Community Federal Savings Bank (Woodhaven, NY; cert 57129) | 0.85 | OCC | not in SEC ticker list | 78 | 344 | 377 | 0.0 | 0.0 | 0.0 (0.0) | 6.87 leverage | 0.51 | 0.00 | -0.03 | 261 | A1 A2 | A1 A2 (rank 16) |
| 14 | Provident Savings Bank, F.S.B. (Riverside, CA; cert 30879) | 1.21 | OCC | PROV (parent Provident Financial Holdings) | 37 | 324 | 375 | 0.0 | 0.0 | 17.3 (-0.3) | 5.25 leverage | 0.12 | 0.00 | 0.01 | 1,260 | A2 C | A2 C (rank 17) |
| 15 | Prospect Bank (Paris, IL; cert 3722) | 0.78 | FDIC | not in SEC ticker list | 21 | 167 | 396 | 0.0 | 39.7 | 15.7 (-0.9) | 3.95 total | 0.00 | 0.06 | 0.06 | 98 | B2 C | B2 C (rank 19) |

**What each one does NOT share with United Fidelity.** No short-list bank has B1 (a real-estate venture book) or D (thin capital), and none has a multifamily nonaccrual jump.
- Piermont: no venture book, no insider concentration, capital margin 6.3 points, no nonaccrual. Its flag E is **30 to 89 day lateness of $13.6M (6.19% of multifamily)** that was zero at 6/30.
- DMB, Malaga, RiverHills: no venture book, no insider concentration, no lateness, wide capital margins (6.7, 12.9 and 6.8 points).
- Universal: multifamily is under 300% of capital; nonaccrual is 3.5% of loans (not multifamily) with an allowance of 30% of it.
- Modern Bank: multifamily only 24% of loans; its 6.0% multifamily nonaccrual is unchanged on the quarter (+0.15 points).
- OneUnited: brokered fell from 27.1% to 0.0% in one quarter. This could be a reporting change; the cause was not checked.
- Marquette, San Rafael, Genesis, Heritage, Community FSB: concentration only. No brokered funding above 15%, no lateness, no venture book.
- Provident (PROV): multifamily 37% of loans, at 324% of capital, with 17.3% brokered; no lateness, no venture book.
- Prospect: insider credit at 39.7% of capital and a capital margin of 3.95 points, but multifamily only 21% of loans.
- Just below the list (ranks 16 to 20): I3 Bank, Locus Bank, Bank of Brodhead, Flagstar Bank NA (FLG; multifamily 42% of loans, 265% of capital, multifamily nonaccrual 8.18%, 30 to 89 day multifamily up $158.3M in Q3, allowance 29% of nonaccrual, no venture book, margin 5.33 points) and Carver Federal (CARV).

**Enforcement status (G), read at the agencies' own pages, 2026-11-28 04:5x UTC:**

| Bank | Status | Source | State |
|---|---|---|---|
| United Fidelity (reference) | C&D 2023-031 (10/31/2023) open; **PCA directive AA-ENF-2026-42, 09/17/2026, amended AA-ENF-2026-42A 09/29/2026, both terminated 11/27/2026**; no directive document posted | OCC EASearch, query "United Fidelity" | VERIFIED (listing); text UNKNOWN |
| Community Federal Savings Bank (57129) | **C&D AA-ENF-2025-21, 04/24/2026, open; BSA/AML program, not credit** (order text read: "Bank Secrecy Act/Anti-Money Laundering ... compliance program"; zero mentions of multifamily, concentration or capital) | OCC EASearch + occ.gov order PDF | VERIFIED |
| Piermont (59154) | FDIC consent order 02/26/2024 (FDIC-23-0038b): oversight of fintech partners and anti-money-laundering controls; NY DFS order alongside it, which per DFS's own CRA evaluation "placed limits on asset growth and loan concentration"; current status not confirmed | Banking Dive, Orrick InfoBytes, NY DFS CRA evaluation (search summaries; FDIC database not reachable) | [NEWS], status UNKNOWN |
| Malaga, Provident | OCC: 0 records | OCC EASearch | VERIFIED (OCC only) |
| Universal, Modern Bank, San Rafael | OCC: only terminated orders (2010–2014; 2009–2013; none) | OCC EASearch | VERIFIED |
| Flagstar NA (context) | OCC civil money penalty $112,000, 10/23/2026 (AA-ENF-2026-45); no open C&D listed | OCC EASearch | VERIFIED |
| Carver (context) | OCC formal agreement AA-NE-2025-18, 05/14/2025, open; subject not read | OCC EASearch | VERIFIED (listing) |
| DMB, RiverHills, OneUnited, Genesis, Heritage, Prospect (FDIC); Marquette (Fed) | none found; OneUnited's 2008 FDIC C&D was terminated in 2015 | FDIC orders database **unreachable**: TLS certificate-chain error from this box, as on 11/11. This is not a bot block, and verification was not bypassed. The Fed's JSON list ends in 2018 and its "recent" feed is empty. Web search only. | SEARCH-NOT-FOUND |

## 3. HOMER's five banks (resolved to legal entities first)

Each name was matched in the FDIC financials file for 9/30 and 6/30. Matching was by name and size, because HOMER's group was banks under $10B. HOMER's 30 to 89 day rise reproduces exactly on these certificates: Preferred +$80.3M, BankPlus +$44.9M, American Momentum +$39.8M, MainStreet +$34.4M, CFG +$34.3M (HOMER `small_output.txt`).

- **Preferred Bank**, Los Angeles, cert 33539. Two other insured banks share the name: cert 10628 in Rothville MO ($0.13B) and cert 34900 in Casey IL, which is present at 6/30 and absent at 9/30. The $7.8B Los Angeles bank is the match.
- **BankPlus**, Belzoni MS, cert 5903 (parent BancPlus Corp).
- **American Momentum Bank**, College Station TX, cert 58309 (parent The Adam Corp Group).
- **MainStreet Bank**, Fairfax VA, cert 57742 (parent MainStreet Bancshares).
- **CFG Bank**, Lutherville MD, cert 34294 (parent Capital Funding Bancorp).

| Rank 9/30 | Bank (cert) | Assets $B | Regulator | Listed | MF % loans | MF % capital | CRE % capital | RE ventures % capital | Insider % capital | Brokered % dep (q/q pts) | Capital margin, pts (line) | MF nonaccrual % | MF 30-89 % | MF stress q/q pts | Allowance % nonaccrual | Flags 9/30 | Flags 6/30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 302 | Preferred Bank (Los Angeles, CA; cert 33539) | 7.82 | FDIC | PFBC (the bank itself) | 9 | 52 | 344 | 7.6 | 0.6 | 14.3 (0.2) | 5.26 tier1 | 14.80 | 26.47 | 25.89 | 49 | E F | E (rank 877) |
| 859 | BankPlus (Belzoni, MS; cert 5903) | 8.30 | FED | not in SEC ticker list | 7 | 45 | 215 | 0.0 | 1.2 | 0.1 (-0.9) | 6.94 leverage (CBLR) | 0.30 | 10.30 | 10.28 | 190 | E | none (rank 1501) |
| 293 | American Momentum Bank (College Station, TX; cert 58309) | 2.85 | FDIC | not in SEC ticker list | 18 | 65 | 172 | 0.0 | 2.7 | 0.0 (0.0) | 15.56 leverage | 11.35 | 11.03 | 9.29 | 34 | E F | E F (rank 303) |
| 201 | MainStreet Bank (Fairfax, VA; cert 57742) | 2.23 | FED | MNSB (parent MainStreet Bancshares) | 12 | 80 | 374 | 0.0 | 0.7 | 17.8 (-16.4) | 7.10 total | 2.92 | 16.13 | 14.22 | 22 | C E F | C F (rank 237) |
| 232 | CFG Bank (Lutherville, MD; cert 34294) | 6.30 | FDIC | not in SEC ticker list | 10 | 59 | 274 | 0.0 | 3.3 | 27.7 (-0.0) | 5.93 total | 10.23 | 8.00 | -9.98 | 55 | C E | C E (rank 240) |

Dollar moves in Q3, $K (FDIC, 9/30 less 6/30): multifamily nonaccrual Preferred +52,613 · BankPlus −12 · American Momentum 0 · MainStreet 0 · CFG −44,496. Multifamily 30 to 89 days is in the table above. Multifamily books: Preferred $540.6M, BankPlus $436.0M, American Momentum $360.3M, MainStreet $242.0M, CFG $428.5M.

**What the five have in common with each other:** all are under $10B. In all five, multifamily is a minority of loans (7% to 18%) and under 100% of capital (45% to 80%). All five are commercial real estate lenders more broadly (CRE 172% to 374% of capital). All five had a jump in multifamily 30 to 89 day lateness, which is how HOMER selected them. Three carry an allowance under 50% of their total nonaccrual (Preferred, American Momentum, MainStreet). None has a capital margin under 5 points, and none has a venture book of note (Preferred's 7.6% is the largest). They sit in five different states (CA, MS, TX, VA, MD).
**In common with United Fidelity:** none of the structural features (A1, A2, B1). MainStreet and CFG carry brokered funding above 15%. MainStreet's brokered share fell 16.4 points in Q3, from 34.2% to 17.8%. On these fields they look like ordinary CRE lenders with a lateness spike, not related-party multifamily specialists. **Enforcement:** none found (FDIC database unreachable; Fed list stale after 2018; web search only). SEARCH-NOT-FOUND.

## 4. Read

**A handful of partial matches, no lookalike.**
- Thirteen banks have multifamily above half of loans and 16 have it above 300% of capital; United Fidelity was one of them.
- Four of them pair that concentration with brokered funding: Piermont, DMB, Malaga, RiverHills, all under $1.5B.
- Only Piermont has a credit tell this quarter: 30 to 89 day lateness, not nonaccrual.
- No bank in the country pairs a multifamily book with a real-estate venture book. That venture book is the visible trace of the bank-as-developer model and its related-party book.

CATO's standing cautions apply.
- A screen match is not a forecast of failure.
- A concentration or low coverage has no demonstrated standalone predictive value. The four structural partial matches have reported near-zero multifamily problems for every quarter in the data.
- The thresholds were set by DEWEY knowing United Fidelity's values. The screen is fitted to one case and has not been tested out of sample.
- **What the screen cannot see:** related-party lending not reported as insider credit (United Fidelity's own reported insider figure was only 80th percentile at 6/30); affiliate lending (there is no line for it on the form); underwriting quality (for example, stacked first and second liens to one lender at 85% loan-to-value); collateral values; CD pricing; examination findings. The OCC's September directive shows a supervisor can act a full quarter before any of this appears in a Call Report.

## 5. Forward view (unscored; no row registered; DEWEY's reading of the data, interpretation REGINALD's)

- **What a second case would look like in the 12/31/2026 filings** (FFIEC CDR from about 1/30/2027; FDIC BankFind about late February; QBP about 2/25): a bank on the A list (multifamily at least 300% of capital) moving from near-zero multifamily nonaccrual to a large share in one quarter, with total capital falling toward 8%. If it follows United Fidelity's sequence, an OCC or FDIC PCA directive or consent order would appear on the agency lists first, possibly weeks before the Call Report. The structural pre-condition is already visible today, and only United Fidelity met it in full.
- **Expectation:** none of the 15 shows a United Fidelity-type nonaccrual jump at 12/31. Basis: no other bank has the venture or developer structure; the four brokered-funded multifamily banks have wide capital margins; ten of the 14 report zero multifamily nonaccrual. The meaningful alternative is Piermont. Its $13.6M of 30 to 89 day multifamily lateness either cures or migrates to nonaccrual, and the result will be visible at 12/31. On a capital base of about $64M (total capital, RC-R 3792, 9/30 SDF) that would be material to Piermont, but not a United Fidelity-scale event.
- **HOMER's five:** 30 to 89 day lateness either cures or rolls to nonaccrual by 12/31. Preferred already has 14.8% of its multifamily on nonaccrual and an allowance of 49% of total nonaccrual. It is listed (PFBC); its Q4 earnings release would normally come before the Call Report (timing INFERRED, not checked).
- **What would change this read:** any A-list bank reporting multifamily nonaccrual above 5% at 12/31; a PCA directive or consent order naming an A-list bank; Piermont's lateness rolling into nonaccrual together with a capital drop; a sponsor link from leg 2 (Pedcor or Birge & Held) to any bank on this list.

## Counter-evidence
- The screen found only United Fidelity on structure because its venture feature was chosen from United Fidelity's own balance sheet. A different kind of related-party lender, one that books its developer exposure as loans and not as ventures, would pass this screen clean. The insider-credit line does not catch it either: United Fidelity's own figure was unremarkable at 6/30.
- Brokered-funded multifamily savings banks with clean credit (DMB, Malaga, RiverHills) have operated that way for years. Concentration alone has not predicted failure in this data.
- The 2026 failure that the stress screen does catch (Nano Banc) was not multifamily-shaped. The second 2026 case does not look like the first.

## Source quality assessment
- Filing cells are primary: FDIC BankFind, cross-checked against FFIEC SDF filings at 9/30 for 21 banks.
- OCC enforcement listings are primary.
- FDIC and Fed enforcement status is unresolved (one secondary source, for Piermont).
- Ticker status rests on the SEC ticker file only.

## References (accessed 2026-11-27, about 23:40 to 23:58 ET)
- FDIC BankFind financials API, `https://api.fdic.gov/banks/financials`, REPDTE 20250930 to 20260930; queries and payload hashes in `research/2026-11-27_second-bank-screen/fdic/*-meta.json`. Field definitions: `https://api.fdic.gov/banks/docs/risview_properties.yaml`.
- FDIC institutions API (FED_RSSD, holding company, regulator): `research/2026-11-27_second-bank-screen/out/institutions-shortlist.json`.
- FFIEC CDR Public Web Service 9/30/2026 SDF filings, DEWEY archive `research/2026-11-11_003R-population/call-reports-sdf.tar.gz` (receipt `archive-receipt.json`).
- OCC Enforcement Action Search, `https://apps.occ.gov/EASearch/?q=<name>`; results `out/occ-easearch-results.json`. Community FSB order: `https://www.occ.gov/static/enforcement-actions/eaAA-ENF-2025-21.pdf`.
- Fed enforcement data: `https://www.federalreserve.gov/supervisionreg/ea-old.json` (ends 2018-12-26); `ea-cms-recent.json` (empty, updateDate 2026-02-25).
- Piermont: https://www.bankingdive.com/news/piermont-sutton-bank-fdic-consent-orders-baas-fintech/711815/ ; https://www.dfs.ny.gov/reports_and_publications/cra_exams/cr24piermont-bank ; Orrick InfoBytes 2024-04-02 PDF.
- SEC company ticker file `https://www.sec.gov/files/company_tickers.json` (declared-contact client string).
- United Fidelity history: `PROME/reports/2026-11-11_united-fidelity-follow-up/F-quarterly-history.json`; HOMER `AGENTS/HOMER/reports/2026-11-27_evidence/small_output.txt`.

**Reproduce:** from the repository root, run `python3 AGENTS/DEWEY/research/2026-11-27_second-bank-screen/pull_fdic.py <dir>`, then `screen.py <dir> <out>`, then `shortlist.py`. The committed `fdic/*.json.gz` copies re-create `out/screen-*.tsv.gz` byte for byte (checked for 6/30 and 9/30). `sdf_crosscheck.py` performs the SDF cross-check.

## Process report
**Searches run:** five FDIC population pulls; one institutions pull; 21 SDF extractions; nine OCC queries; Fed JSON (stale); four web searches for FDIC- and Fed-supervised banks.
**Data gaps:** FDIC enforcement database (TLS chain; also failed on 11/11); the Fed's post-2018 enforcement list; affiliate lending and related-party receivables are not on the form; OTC tickers.
**Source frustrations:** FDIC's orders site cannot be read from this box. The OCC listing gives the PCA directive's existence but no document.
**Confidence:** High on the cells and arithmetic. Medium on the criteria, which are fitted to one case. UNKNOWN on non-OCC enforcement.
**If I had more time/tools:** read the 12/31/2025 to 6/30/2026 SDF RC-F "other assets" text for the 15 banks, to look for related-party receivables; check the FDIC orders database from a machine with a complete certificate chain; check OCC and FDIC lists for any new PCA directive weekly until the 12/31 data.
**Suggestions:** promote `screen.py` only if REGINALD wants the screen re-run at 12/31 (BACKLOG candidate; not built as a standing tool).
