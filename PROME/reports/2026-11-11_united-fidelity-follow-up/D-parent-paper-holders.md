# UFB-D: Fidelity Federal Bancorp (FFED) and Pedcor parent paper: what was sold, on what terms, who holds it

Researcher: read-only public-source pass for PROME. Read date for every source below: 2026-11-11 (US Eastern evening; SEC server stamps show 2026-11-12 01:0x UTC). Raw downloads: `ufbD/raw/` (same scratchpad folder). Tokens: VERIFIED (read at source) · INFERRED · SEARCH-NOT-FOUND · UNKNOWN.

## 5-line answer

1. FFED (Nevada holding company, CIK 910492) has sold to outside investors $113.75M face of holding-company subordinated debt since 2018 ($30M + $23.5M + $35M + $25.25M). Known pieces: $30M 6.785% notes due Oct 2028 (2018), $23.5M 6.00% notes due Nov 2029 (2019), $35M 4.50% notes due Mar 2031 (2021) and $25.25M notes sold Dec 2022 (terms not found). Each known issue is fixed for 5 years and then floats. Before that: about $8.25M of 2004/2005 trust preferred securities, $8M of 8.25% subordinated debentures due 2028, and preferred Series A to D. VERIFIED from the 2021 offering circular (financials dated 2020-12-31) and the Form Ds.
2. CUSIP 315921AJ5 is VERIFIED as FFED's $23.5M note due 2029-11-01. Terms: 6.00% fixed until Nov 2024, then 3-month SOFR + 4.65% reset quarterly; ranked Tier 2 (subordinated); callable from Nov 2024 (not called as of the latest fund filing); no deferral feature is described. Fund filings show the floating coupon at 8.40% on 2026-08-31.
3. Registered-fund holders found for the 2026 periods are all small positions (under 1% of each fund):
   - Thompson Bond Fund: $7.0M of the 2029 note and $6.5M of the 2028 note (315921AG1).
   - Angel Oak Financial Strategies Income Term Trust (ticker FINS): $2.0M of the 2029 note and $1.0M of the 2031 note (315921AL0).
   - ArrowMark Financial Corp (ticker BANX): the former TARP preferred shares (Series A 2,789 and Series B 200), valued at 60% of liquidation value.
   Outside registered funds: a JP Morgan Securities triparty repo held $2.5M of the 2028 note as collateral (in Schwab's money fund filing). A private Angel Oak securitization (BFNS 2022-1) held $4M of the 2031 note in 2022.
4. Every fund filing up to the latest one (periods 2026-06-30 to 2026-08-31) marks the notes at 95 to 99.5% of par. Each reports "not in default" and "interest not in arrears". None of those periods includes the Q3 2026 loss, so none of the marks reflects it. ArrowMark's 60% mark on the preferred has not changed since at least June 2024.
5. We found no rating (KBRA or Egan-Jones) on FFED paper and no press or filing that reports an interest deferral. The 2024 Federal Reserve agreement, read on its text, requires prior Fed approval for "any interest payments due on subordinated debentures" and for capital distributions on preferred shares. It also asks for 30 days' notice before a "required notice of deferral". Pedcor Financial Bancorp has no EDGAR record of its own. Pedcor Financial LLC (CIK 1185822) has filed only Form 4s, the last in 2005.

## Table 1: offerings by FFED (EDGAR Form D, Regulation A, offering-circular disclosures)

| # | Date (first sale / issue) | Security | Offered | Sold | Investors | Placement agent | Use of proceeds | Source · status |
|---|---|---|---|---|---|---|---|---|
| D1 | 2018-02-07 (Form D filed 2018-02-09) | Equity, Rule 506(b). INFERRED to be the Series D 9% cumulative perpetual preferred: 4,300 shares at $1,000 = $4.3M, issued Feb 2018 "to the shareholders" (offering circular Note 22) | $4,300,000 | $2,000,000 at filing; circular says 4,300 shares were issued | 2 | none listed; $0 commission | not itemised; $0 to insiders | [Form D](https://www.sec.gov/Archives/edgar/data/910492/000091049218000003/primary_doc.xml) VERIFIED; link to Series D INFERRED (same $4.3M and month) |
| — | Oct 2018 (no Form D on EDGAR) | Subordinated notes due Oct 2028, $1 denominations; 6.785% fixed to Oct 2023, then 3-month LIBOR + 3.79% quarterly; Tier 2; no call before 5th anniversary. CUSIP 315921AG1 per fund filings | — | $30,000,000 | UNKNOWN | Sandler O'Neill | UNKNOWN | 2021 offering circular, Note 17(G), financials dated 2020-12-31 ([1-A POS doc](https://www.sec.gov/Archives/edgar/data/910492/000110465921134780/tm2121328d3_partiiandiii.htm)) VERIFIED; no Form D: SEARCH-NOT-FOUND in the CIK 910492 filing list |
| D2 | 2019-10-31 (Form D filed 2019-11-12) | Debt, Rule 506(b): subordinated notes due Nov 2029 (CUSIP 315921AJ5) | $23,500,000 | $23,500,000 | 8 | Sandler O'Neill & Partners (CRD 23328); commission $587,500 (2.5%) | not itemised; $0 to insiders | [Form D](https://www.sec.gov/Archives/edgar/data/910492/000091049219000001/primary_doc.xml) VERIFIED; minimum investment $500,000; solicited in CT, FL, GA, OH, WI |
| — | 2021-03-19 (no Form D on EDGAR) | Subordinated notes due 2031-03-30, $100 denominations; 4.50% fixed to Mar 2026, then 3-month SOFR + 3.84% quarterly; Tier 2; callable from Mar 2026. CUSIP 315921AL0 per fund filings | — | $35,000,000 | UNKNOWN | Sandler O'Neill | UNKNOWN | Offering circular Note 30 (subsequent events) VERIFIED. The 1-A POS cover lists it as $35M sold in the past year under 4(a)(2)/506(b) to accredited investors only. Issue date 3/19/2021 from the BFNS 2022-1 asset list. No Form D: SEARCH-NOT-FOUND |
| R1 | 1-A 2021-07-14; 1-A/A 2021-10-22; qualified 2021-10-28; 253G2 2021-11-04; 1-A POS 2021-11-05; qualified again 2021-11-16; 1-Z 2022-12-16 | Reg A Tier 1: FFED common stock issued in a share exchange for the merger of American Capital Bancorp into FFED. Not a cash raise | 48,867 shares at $78 | 29,776 shares, $2,322,528 | UNKNOWN (merger holders) | none; legal fees $60,000 + $15,000 | merger consideration | [1-Z](https://www.sec.gov/Archives/edgar/data/910492/000110465922127900/primary_doc.xml), [253G2](https://www.sec.gov/Archives/edgar/data/910492/000110465921134101/tm2131923d1_253g2.htm) VERIFIED. The 253G2 says FFED stopped trading on OTC Pink (symbol FDLB) on 2021-09-28 |
| D3 | 2022-12-29 (Form D 2023-01-12; D/A 2023-02-28; D/A 2023-04-11) | Debt, Rule 506(b). Coupon, maturity and CUSIP not stated in the Form D | $14.75M → $23.25M → $25.25M (raised by each amendment) | $25,250,000 by 2023-03-31 | 16 → 17 → 18 | Piper Sandler & Co. (CRD 665); commission $631,250 (2.5%) | not itemised; $0 to insiders | [D](https://www.sec.gov/Archives/edgar/data/910492/000110465923003468/primary_doc.xml), [D/A 1](https://www.sec.gov/Archives/edgar/data/910492/000110465923026244/primary_doc.xml), [D/A 2](https://www.sec.gov/Archives/edgar/data/910492/000110465923043894/primary_doc.xml) VERIFIED. Industry recoded to "Other Banking and Financial Services". The final amendment adds IN to the solicitation states |

### Older securities outstanding at 2020-12-31 (2021 offering circular Notes 17, 20–22; 1-A POS cover data), VERIFIED

| Security | Face / shares | Terms | Holder per document |
|---|---|---|---|
| Junior subordinated debentures due Dec 2034 (Fidelity Federal Bancorp Statutory Trust I-2004) | $3.093M ($3M of trust preferred) | 3-month LIBOR + 2.25%; **interest can be deferred for up to 20 consecutive quarters**; "No amounts have been deferred at December 31, 2020" | trust preferred holders not named |
| Junior subordinated debentures due Jun 2035 (Fidelity Federal Bancorp Trust II-2005) | $5.155M ($5M of trust preferred) | 3-month LIBOR + 1.90%; same 20-quarter deferral right | not named |
| Subordinated debentures due Jan 2028 | $8.0M | 8.25% fixed, quarterly; Tier 2; $100 denominations | Note 17(C): "StoneCastle Financial Corp issued … payable to Community Funding CLO, Ltd, as trustee". INFERRED: placed into a StoneCastle-arranged CLO |
| Promissory note due Jan 2027 | $5.0M | Prime + 0.50% | Bank of St. Croix, Inc. |
| Demand note (matured 2010) | $0.176M | 9.00% | principal owners of the Pedigo-Cordingley Group (insiders) |
| Series A preferred (ex-TARP) | 6,657 shares × $1,000 | cumulative; 9% after year 5 | US Treasury sold all of it to private investors in 2013 (Note 17(E)) |
| Series B preferred (ex-TARP warrant preferred) | 200 shares × $1,000 | cumulative 9% | same as Series A |
| Series C preferred | 4,000 shares × $1,000 | non-cumulative 6% | three members of the Pedigo-Cordingley Group (insiders) |
| Series D preferred | 4,300 shares × $1,000 | cumulative 9%; holders may elect 2 directors after 6 missed quarterly dividends | "the shareholders" (see D1) |
| Bank-level (UFB) junior subordinated debentures due Sep 2033 | $4.0M | 3-month LIBOR + 2.95%; Tier 2; US Bank trustee | not named |
| Bank-level (UFB) non-cumulative perpetual preferred | 25,000 sh at 8% (Mar 2021) + 20,000 sh at 7% (Sep 2021), $1,000 liquidation preference each = $45M | non-cumulative | "multiple third parties" (Note 30) |

The circular reports all of these figures as of 2020-12-31. Anything redeemed after that date is UNKNOWN to us.

## Table 2: terms of the November 2029 note (CUSIP 315921AJ5) and the sister issues

| Item | 315921AJ5 (2029) | 315921AG1 (2028) | 315921AL0 (2031) | Source |
|---|---|---|---|---|
| Issuer | Fidelity Federal Bancorp (holding company), LEI 5493004DRUFQ7MQTK142 | same | same; BFNS 2022-1 lists the obligor as "Pedcor Financial" | N-PORT filings; BFNS AUP report (2022-06-22) |
| Size | $23.5M | $30.0M | $35.0M | Offering circular Note 17 / Note 30 |
| Issue date | Oct 31, 2019 (Form D first sale); the circular says "October 2019" | Oct 2018 | Mar 19, 2021 | Form D; circular; BFNS |
| Maturity | 2029-11-01 | 2028-10-15 | 2031-03-30 | N-PORT `maturityDt` |
| Coupon | 6.00% fixed until Nov 2024, paid semiannually | 6.785% fixed until Oct 2023, paid semiannually | 4.50% fixed until Mar 2026, paid semiannually | circular |
| Floating reset | 3-month SOFR + 4.65%, paid quarterly | 3-month LIBOR + 3.79%, paid quarterly (the LIBOR successor rate is not stated) | 3-month SOFR + 3.84%, paid quarterly | circular; the BFNS list gives a 3.84% spread |
| Current coupon (fund filing) | 8.40092% at 2026-08-31 (Thompson) and 2026-07-31 (FINS) | 7.80453% at 2026-08-31 | 7.56543% at 2026-07-31 | N-PORT `annualizedRt` |
| Call | no redemption before the 5th anniversary "unless certain triggering events were to occur", so callable from about Nov 2024. Still outstanding at 2026-08-31 | no redemption before the 5th anniversary (Oct 2023). Still outstanding | callable from 3/30/2026 (BFNS list). Still outstanding at 2026-07-31 | circular; N-PORT |
| Ranking | unsecured subordinated; counted as Tier 2 capital; UMB Bank NA paying agent | same | same | circular |
| Deferral feature | none described in the circular. **This is a statement about the circular's summary; the note indenture itself was not found on EDGAR** | none described | none described | SEARCH-NOT-FOUND for the note documents |
| Default / arrears flags | `isDefault`=N, `areIntrstPmntsInArrs`=N, `isPaidKind`=N in every filing from 2024-07-31 to 2026-08-31 | same | same | N-PORT VERIFIED |

**What the Federal Reserve agreement says, read on its text** ([enf20240625a1.pdf](https://www.federalreserve.gov/newsevents/pressreleases/files/enf20240625a1.pdf), dated June 2024, VERIFIED). Paragraph 5(a) says the three companies (PFIN, PFB, FFED) "shall not, directly or indirectly, declare or pay dividends … or make any other capital distribution in respect of common shares, preferred shares, or other capital instruments, including, without limitation, any interest payments due on subordinated debentures, without the prior written approval of the Reserve Bank and the Director of Supervision and Regulation". Approval requests are due 30 days before "the earlier of the proposed declaration, payment, or distribution date, or required notice of deferral".

Reading: every coupon on FFED subordinated debt, and every preferred dividend, needs prior Fed approval. The notes describe no deferral right, so a coupon the Fed did not approve would be a missed payment. We INFER this from the absence of a deferral clause in the summary; we have not read the indenture. The trust preferred securities are different: they can defer for 20 quarters. No document we read shows a missed or deferred payment. The fund filings through 2026-08-31 report the notes as not in arrears.

## Table 3: holders, sorted by % of net assets (latest filing for each holder)

| Holder (fund) | Adviser | Listed? | Security | Latest period / filed | Principal | Value | Price (% of par) | Fund net assets | % of net assets | Current or historical |
|---|---|---|---|---|---|---|---|---|---|---|
| ArrowMark Financial Corp | ArrowMark Asset Management (INFERRED) | **LISTED**: ticker BANX on EDGAR; Nasdaq INFERRED | FFED Series A fixed-rate cumulative perpetual preferred | 2026-06-30 / 2026-08-21 | 2,789,000 units (NS). INFERRED: 2,789 shares × $1,000 = $2.789M liquidation value | $1,673,400 | 60.00 | $203.5M | 0.822% | current (2026) |
| Angel Oak Financial Strategies Income Term Trust | Angel Oak Capital Advisors (INFERRED for FINS; named as collateral manager in BFNS) | **LISTED**: ticker FINS; NYSE INFERRED | 315921AJ5 (2029) | 2026-07-31 / 2026-09-28 | $2,000,000 | $1,990,011 | 99.50 | $450.5M | 0.442% | current |
| Thompson Bond Fund (Thompson IM Funds Inc) | Thompson Investment Management (INFERRED) | **UNLISTED** open-end mutual fund (ticker THOPX INFERRED, not shown on EDGAR) | 315921AJ5 (2029) | 2026-08-31 / 2026-10-21 | $7,000,000 | $6,948,300 | 99.26 | $1,891.7M | 0.367% | current |
| Thompson Bond Fund | as above | UNLISTED | 315921AG1 (2028) | 2026-08-31 / 2026-10-21 | $6,500,000 | $6,189,855 | 95.23 | $1,891.7M | 0.327% | current |
| Angel Oak Financial Strategies Income Term Trust | as above | LISTED (FINS) | 315921AL0 (2031) | 2026-07-31 / 2026-09-28 | $1,000,000 | $984,075 | 98.41 | $450.5M | 0.218% | current |
| ArrowMark Financial Corp | as above | LISTED (BANX) | FFED Series B fixed-rate cumulative perpetual preferred | 2026-06-30 / 2026-08-21 | 200,000 units (NS) = all 200 shares, INFERRED $0.2M | $120,000 | 60.00 | $203.5M | 0.059% | current |
| Schwab Prime Advantage Money Fund (repo collateral, **not an owner**) | Charles Schwab Asset Management | UNLISTED | 315921AG1 posted as triparty collateral on a JP Morgan Securities repo | 2026-08-31 / 2026-09-08 (N-MFP3) | $2,500,000 | $2,406,148 | 96.25 | n/a | n/a | current. The owner of the bonds is a JPM repo counterparty and is UNKNOWN. Also listed in the N-MFP3s for 2026-04-30 and 2026-06-30 |
| BFNS 2022-1 (Cayman bank-sub-debt securitization; Angel Oak Capital Advisors collateral manager) | Angel Oak Capital Advisors | UNLISTED, private | "Pedcor Financial" 4.50% due 3/30/2031 (= 315921AL0 terms, INFERRED same note) | EY agreed-upon-procedures report dated 2022-06-22 (ABS-15G filed 2022-06-27) | $4,000,000 | n/a | n/a | n/a | n/a | **historical** (2022 initial portfolio); the current holding is UNKNOWN |
| Nuveen Tax-Advantaged Floating Rate Fund | Nuveen | was listed (JFP); not checked | "Pedcor Financial" and "Pedcor Bancorporation" non-cumulative preferred | sold in the period covered by the N-CSRS filed 2012-03-09 | n/a | n/a | n/a | n/a | n/a | **historical**, exited by about 2012 |

Sources (all VERIFIED at the primary_doc.xml, read 2026-11-11):
- Thompson: [0000894189-26-029528](https://www.sec.gov/Archives/edgar/data/795264/000089418926029528/primary_doc.xml)
- FINS: [0001193125-26-405268](https://www.sec.gov/Archives/edgar/data/1745059/000119312526405268/primary_doc.xml)
- BANX: [0000940400-26-033017](https://www.sec.gov/Archives/edgar/data/1578987/000094040026033017/primary_doc.xml)
- Schwab N-MFP3: [0001410368-26-091070](https://www.sec.gov/Archives/edgar/data/857156/000141036826091070/primary_doc.xml)
- BFNS: [exhibit99-1](https://www.sec.gov/Archives/edgar/data/1867816/000092963822001061/exhibit99-1.htm)
- Nuveen: [N-CSRS 2012](https://www.sec.gov/Archives/edgar/data/1313259/000110465912017141/a12-2815_33ncsrs.htm)

Known registered-fund holdings of the 2029 note: $9.0M of $23.5M (38%). Of the 2028 note: $6.5M of $30M, plus $2.5M seen as repo collateral. Of the 2031 note: $1.0M in a registered fund, plus $4M in BFNS as of 2022. Holders of the Dec 2022 $25.25M issue, the trust preferred and the $8M 8.25% debentures: SEARCH-NOT-FOUND.

### Price history (% of par = value / principal, from N-PORT `valUSD` / `balance`)

| Period end | Thompson AJ5 (2029) | FINS AJ5 (2029) | Thompson AG1 (2028) | FINS AL0 (2031) | BANX Series A / B |
|---|---|---|---|---|---|
| 2024-06/07/08 | 96.00 (8/31) | 97.00 (7/31) | 98.03 (8/31) | 86.76 (7/31) | 60.00 / 60.00 (6/28) |
| 2024-09/10/11 | 99.00 (11/30) | 99.50 (10/31) | 98.11 (11/30) | 88.58 (10/31) | 60.00 (9/30) |
| 2024-12 to 2025-02 | 99.03 (2/28) | 99.27 (1/31) | 99.00 (2/28) | 93.50 (1/31) | 60.00 (12/31) |
| 2025-03 to 2025-05 | 99.09 (5/31) | 99.31 (4/30) | 97.21 (5/31) | 94.23 (4/30) | 60.00 (3/31) |
| 2025-06 to 2025-08 | 99.13 (8/31) | 99.37 (7/31) | 98.07 (8/31) | 96.22 (7/31) | 60.00 (6/30) |
| 2025-09 to 2025-11 | 99.15 (11/30) | 99.39 (10/31) | 98.20 (11/30) | 98.16 (10/31) | 60.00 (9/30) |
| 2025-12 to 2026-02 | 99.16 (2/28) | 99.40 (1/31) | 98.33 (2/28) | 99.40 (1/31) | 60.00 (12/31) |
| 2026-03 to 2026-05 | 99.21 (5/31) | 99.45 (4/30) | **95.02** (5/31) | 98.34 (4/30) | 60.00 (3/31) |
| 2026-06 to 2026-08 | 99.26 (8/31) | 99.50 (7/31) | 95.23 (8/31) | 98.41 (7/31) | 60.00 (6/30) |

Observations, all VERIFIED as figures and INFERRED as to meaning:
- The 2029 note has drifted up toward par.
- The 2028 note dropped about 3.3 points between the 2026-02-28 and 2026-05-31 marks.
- The 2031 note rose from 86.8 to 99.4 as its first call date approached, then slipped to 98.3 to 98.4 after it was not called.
- All the notes are fair-value Level 2 (a model or matrix price, not a traded print). The preferred is Level 3, held flat at 60.
- FINS also held a reverse repo against the 2029 note (−$1.00M to −$1.09M, periods 2024-07-31 to 2025-04-30). This was borrowing against the bond, not a change in ownership.
- No filing in this table covers a period after 2026-08-31, so none of these marks reflects the Q3 2026 loss.

## Searched and found nothing (SEARCH-NOT-FOUND; each is a statement about the search, not proof of absence)

- EDGAR full-text search (endpoint `efts.sec.gov/LATEST/search-index`) for every CUSIP from 315921AA4 to 315921AS5 with computed check digits. Hits only for AG1, AJ5 and AL0, plus AA4, which appears once in an FFED 2001 filing (an old pre-2005 security; not followed up). Query 315921AR7 failed on the first try (the response had no hits object) and returned 0 hits on retry. **No CUSIP found for the Dec 2022 $25.25M issue.**
- Full text for "Fidelity Federal Bancorp", 2023-01-01 to 2026-11-11. Fund holders: only Thompson, FINS and BANX, plus FFED's own Form Ds and two bank S-1 mentions (NB Bancorp 2023, Security Midwest 2024) that were not followed up. The result list is capped at 100 rows, and the from=100 page returned nothing, so the list may be incomplete. A 2026-only NPORT-P query returned 14 hits from the same three filers.
- Full text for "Pedcor Financial Bancorp" (28 hits: Nuveen N-Q 2006–2011, FHLB Indianapolis 8-K 2017, FFED 1-A) and "Pedcor Financial" (87 hits). No current fund holder found.
- EDGAR company search for "pedcor": only PEDCOR INVESTMENTS LLC (CIK 925765, SC 13D/A filings to 2005) and PEDCOR FINANCIAL LLC (CIK 1185822, Form 4s to 2005). **Pedcor Financial Bancorp: no EDGAR record.**
- No Form D on EDGAR for the Oct 2018 $30M or Mar 2021 $35M note sales (checked the CIK 910492 filing list). The issuer may have relied on 4(a)(2) without filing.
- Web search for "Fidelity Federal Bancorp" with KBRA, Egan-Jones or rating: KBRA hits are all for **Fidelity Financial Corporation (Wichita KS), a different issuer**. Nothing found for FFED.
- Web search for deferral of interest by United Fidelity Bank or Fidelity Federal Bancorp in 2026: no press item.
- 13F does not apply: these are private debt and preferred, not 13F securities. No 13F search was run.

## Other outside paper (item 4)

- **Bank-level subordinated debt:** OCC Conditional Approval #1284 (dated 2022-03-14, published April 2022; [ca1284.pdf](https://www.occ.gov/topics/charters-and-licensing/interpretations-and-decisions/2022/ca1284.pdf), VERIFIED) approved United Fidelity Bank including **$50,000,000** of subordinated debt in Tier 2 capital. The debt was "to be issued in March 2022 and mature in 2032", fixed-to-floating, converting in 2027. The bank had to complete the sale within one year. Whether it was issued, and for how much, is UNKNOWN; the brief's figure of about $26.9M of Call Report subordinated notes is not reconciled. INFERRED: the $26.9M may be the $4M 2033 debentures plus a partial 2022 issue, or something else. Buyers: SEARCH-NOT-FOUND. A bank-level note sold under OCC Part 16 would not appear on EDGAR.
- **Bank-level perpetual preferred:** $45M of non-cumulative preferred (8% and 7%) was sold in 2021 to "multiple third parties". Holders are not named. VERIFIED that it was sold; holders UNKNOWN.
- **Trust preferred** ($3M from 2004 and $5M from 2005) and the **$8M 8.25% 2028 debentures** (Community Funding CLO via StoneCastle): no current holder documents found.
- **Former TARP preferred:** ArrowMark (BANX) holds 2,789 of the 6,657 Series A shares and all 200 Series B shares (INFERRED from the unit counts). Holders of the other ~3,868 Series A shares are UNKNOWN.

## Open unknowns

1. Terms, CUSIP and holders of the Dec 2022 $25.25M FFED debt (Piper Sandler, 18 investors).
2. Whether any FFED coupon or preferred dividend since June 2024 was paid with Fed approval or withheld. No document read shows either. The fund "not in arrears" flags run only to 2026-08-31.
3. The indenture text for the notes (deferral, events of default, acceleration). Not found on EDGAR.
4. Whether the 2004/2005 trust preferred, the $8M debentures, the $5M Bank of St. Croix note and the Series C/D preferred are still outstanding after 2020-12-31.
5. The UFB $50M 2032 subordinated note (OCC 2022): issued amount and holders; reconcile with the $26.9M Call Report figure.
6. Next fund filings that will cover the Q3 2026 period: BANX N-PORT for 2026-09-30 (due about late Nov 2026); Thompson for 2026-11-30 (about Jan 2027); FINS for 2026-10-31 (about late Dec 2026). These are the first marks that can reflect the Q3 loss.
7. Who owns the $2.5M of the 2028 note posted as JPM triparty collateral.
