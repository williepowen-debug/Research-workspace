# B. COREWEAVE (CRWV) CREDIT AND WHY IT FELL 10% TODAY

**Reader B, read-only. Written 2026-10-22 20:42 ET. 13 of 25 web searches used. Tags: VERIFIED (read at the primary document) / INFERRED / SEARCH-NOT-FOUND / UNKNOWN. "Filed" = SEC document; "reported" = press.**
Primary sources pulled this session from SEC EDGAR (fetched ~20:35 ET): CRWV 10-Q for Q2 2026 (filed 2026-08-12, acc. 0001769628-26-000366), 10-Q Q1 (2026-05-08), 10-K FY2025 (2026-03-02), 8-Ks of 2026-08-10 (DDTL 5.5), 2026-09-17 and 2026-09-22 (convertible, ATM), 424B5 2026-09-17, Form 4 filings since 2026-09-01, plus the DTCC public SBS tape files in PROME scratchpad (10/20, 10/21, 10/22). Press releases and press stories are labelled SECONDARY.

---

## 0. Headline in five lines

| # | Finding | Tag |
|---|---|---|
| 1 | No company filing explains 10/22. EDGAR's CRWV filing list shows nothing after 2026-10-14 (Forms 4/144 only) and no 8-K after 2026-09-22. | VERIFIED (EDGAR submissions JSON pulled 20:34 ET 10/22) |
| 2 | 10/22 was an equity-led move: DTCC CDS prints on 10/22 were NOT wider than 10/20 (Dec-2031 18.3 pts upfront on 10/22 vs 19.1-19.6 pts on 10/20). | VERIFIED on the tape; causal read INFERRED |
| 3 | Oracle is named in CRWV's filings only as a COMPETITOR. It is not a named customer or counterparty. The link to Oracle is shared OpenAI-demand dependence, shared sector financing and rates beta, shared GPU supplier (Nvidia). No contractual tie found. | VERIFIED (competitor text) / INFERRED (link mechanisms) |
| 4 | Debt principal at 6/30/26 is $35.55B (plus $16.5B lease liabilities = $51.6B), and since then +$4.2B convertible (9/22), a $2.6B DDTL 5.5 (8/7) and a 35M-share ATM / collared-forward programme (9/17). | VERIFIED |
| 5 | The market's worry is the funding loop, not near-term default: CDS curve is steeply upward (1-yr near par, 5-yr about 18 pts upfront), and CRWV needs the debt market to keep building (analyst est. about $30B raise in 2027, Baird, SECONDARY). | VERIFIED curve / SECONDARY estimate |

---

## 1. Debt stack at the latest 10-Q (June 30, 2026) -- VERIFIED (10-Q Note 10, p. 27-30)

| Facility | Maturity | Eff. rate | 6/30/26 $M | 12/31/25 $M | Notes |
|---|---|---|---|---|---|
| DDTL 1.0 | Mar 2028 | 15% | 1,300 | 1,553 | recourse |
| DDTL 2.0 | Aug 2030 | 11% | 3,190 | 5,037 | recourse |
| DDTL 2.1 | Mar 2031 | 9% | 3,000 | 2,741 | recourse |
| DDTL 3.0 | Aug 2030 | 9% | 2,215 | 340 | recourse |
| DDTL 5.0 ($3.1B, Morgan Stanley agent, SOFR+4.50%) | Nov 2031 | 9% | 1,101 | -- | recourse; commitment ends 9/30/26; guaranteed by parent |
| 2030 Senior Notes (9.25% per 9/22 8-K) | Jun 2030 | 10% | 2,000 | 2,000 | |
| 2031 9.00% Senior Notes | Feb 2031 | 10% | 1,750 | 1,750 | |
| 2031 9.75% Senior Notes | Oct 2031 | 10% | 2,750 | -- | issued Apr 2026 |
| 2032 9.625% Senior Notes | Jul 2032 | 10% | 1,250 | -- | issued Jun 2026 |
| 2032 EUR 8.50% Senior Notes (EUR 2.0B) | Jul 2032 | 9% | 2,279 | -- | issued Jun 2026; swapped to USD fair-value hedge |
| 2031 1.75% Convertible | Dec 2031 | 2% | 2,588 | 2,588 | |
| 2032 1.75% Convertible | Oct 2032 | 2% | 4,000 | -- | issued Apr 2026 |
| OEM / software-licence financing (recourse) | Dec 2026-Jul 2030 | 11% | 4,220 | 3,518 | |
| Magnetar loan | Jan 2029 | 12% | 189 | 273 | |
| Revolver ($2.0B remaining capacity; LCs $533M) | Nov 2029 | -- | 0 | 1,000 | repaid Apr 2026 |
| **Recourse principal** | | | **31,832** (calc.) | | carrying value net of discount $31,405M |
| DDTL 4.0 ($8.5B facility, MUFG agent, non-recourse SPV CCAC VIII) | Mar 2032 | 7% | 2,837 | -- | $1.4B floating SOFR+2.25%, $1.5B fixed UST+2.00%; commitment to 6/30/27 |
| OEM financing (non-recourse) | Aug 2026-Aug 2028 | 9% | 882 | 647 | |
| **Total principal** | | | **35,551** | | 10-Q maturity table total |

Maturity wall (10-Q): rest of 2026 $4,413M; 2027 $6,184M; 2028 $4,416M; 2029 $2,421M; 2030 $3,221M; thereafter $14,896M. Current debt $7.5B (recourse $6.2B + non-recourse $1.3B).
Balance sheet 6/30: cash $5,524M; availability under facilities $10,014M; total liquidity $15,553M (10-Q p. 46). Lease liabilities (operating+finance, current+non-current) $16.5B (calc. from balance sheet); leases signed but not commenced $35.5B (2026-2029 starts, 7-16 yr terms). Total liabilities $72.0B vs equity $5.0B, total assets $77.1B.

**Post-quarter additions (all VERIFIED, 8-K):**

| Date | Item | Terms |
|---|---|---|
| 2026-08-07 | DDTL 5.5, $2.6B, JPMorgan agent, MUFG co-arranger | SOFR+5.50%; matures 9/1/2031; draws to Dec 2026; parent guarantee; DSCR >= 1.35x from first full month after commitments reduce to zero or 12/31/26; event of default on "adverse events with respect to certain material contracts" |
| 2026-09-17 | 35,000,000-share ATM (Equity Distribution Agreement, 11 sales agents; incl. collared forward-sale agreements with DB, GS, MS, Citi) | No sales until at least 30 days after the convert purchase agreement date, i.e. window opened about 10/17-10/18. Whether any sale has occurred: UNKNOWN (no 8-K/424B after 9/22) |
| 2026-09-22 | $4.2B 2.875% Convertible Senior Notes due 4/1/2033 (incl. $500M option), unsecured, guaranteed by subs | Conversion price about $97.85 (22.5% premium to 9/17 close, implying 9/17 close about $79.88); max 52.6M shares; cross-default trigger on subsidiary debt > greater of $200M or 5% of LTM EBITDA; capped calls bought |

**Covenants reported.** 10-Q: "in compliance with all covenants under its delayed draw term loan facility agreements" at 6/30 (VERIFIED). DDTL 4.0 sizing/maintenance mechanics (DSCR 1.20x sizing, 1.15x maintenance, cash trap on parent bankruptcy, power-cost hedge) are in DEWEY's 2026-08-02 read of the filed agreement (`AGENTS/DEWEY/output/2026-08-02_ai-credit-guarantee-web.md` section 4); not re-read here. 10-Q language on DDTL 4.0: sizing "based upon the depreciable cost of computing equipment, projected debt service coverage and project-level conditions" -- consistent with DEWEY's correction that it is a cost-at-funding and DSCR test, not a mark-to-market borrowing base.

**Interest versus cash flow (10-Q):**

| Metric | Q2 2026 | 6M 2026 | Source |
|---|---|---|---|
| Revenue | $2,575M | $4,653M | VERIFIED |
| Operating income (GAAP) | -$49M | -$193M | VERIFIED |
| Adj. EBITDA / adj. operating income | $1,510M / $128M | -- | VERIFIED (8/11 press release) |
| Interest expense, net | $640M (contractual $592M, less $79M capitalised, plus $45M amortisation = $558M in debt note; $640M on P&L includes lease/financing-component interest) | $1,176M | VERIFIED |
| Operating cash flow | $679M (calc.: $3,663M less Q1 $2,984M) | $3,663M | VERIFIED (calc.) |
| Cash paid for PP&E | about $6.4B (calc. and SECONDARY 247wallst: capex $6.42B, FCF -$5.74B) | $14.1B | 6M VERIFIED |
| Q3 guide (SECONDARY: Zacks, TIKR) | revenue $3.45-3.60B; adj. op. income $200-260M; interest expense $860-940M | | SECONDARY, not seen in a filing (guidance was given on the call) |

Run-rate: Q3 guided interest $860-940M a quarter is about $3.4-3.8B annualised against Q2 operating cash flow of $0.68B (a quarter) and H1 $3.7B (H1 inflated by customer prepayments: deferred revenue $9.7B vs $8.2B at YE). Net: interest is covered by GAAP operating income about 0x (negative), by adj. EBITDA about 2.4x in Q2 ($1,510M / $640M). INFERRED from the figures above.

---

## 2. Customer concentration and the Oracle question

**Filed concentration:**

| Item | Figure | Source |
|---|---|---|
| FY2025 revenue from top customer = Microsoft | 67% | VERIFIED, 10-K |
| Q2 2026 revenue: Customer A / B / C | 36% / 26% / 10% (names not given; 6M: 40% / 23% / <10%) | VERIFIED, 10-Q note 2 |
| Accounts receivable 6/30: Customer A / B | 32% / 32% (A was 68% at YE25) | VERIFIED |
| Customer A = Microsoft | likely (was 71% of Q2-25 revenue; 10-K names Microsoft top) | INFERRED |
| RPO 6/30/26 | $103.7B; 41% in 24 months, 39% in months 25-48, 20% months 49-78 | VERIFIED |
| Revenue backlog | about $104B at 6/30, excludes more than $25B net new commitments added early Q3 (8/11 release) | VERIFIED (release) |
| Share of backlog by customer | not disclosed in any filing found | SEARCH-NOT-FOUND |
| Backlog quality | "about two-thirds with investment-grade counterparties incl. Microsoft, Meta, IBM, Caterpillar" (Deutsche Bank, via CNBC 10/15) | SECONDARY |

**Named contracts (filed):**

| Customer | Commitment | Source |
|---|---|---|
| OpenAI | Mar 2025 MSA up to $11.9B through Oct 2030 (10-K); Sept 2025 order form up to $6.5B through 5/31/2031 (10-K, 10-Q). May 2025 add-on $4B and total $22.4B are reported, not seen in the filings I read. | VERIFIED ($11.9B, $6.5B); SECONDARY ($4B, $22.4B: BNN/Reuters 9/25/25) |
| Meta | Sept 2025 order form up to $14.2B through Dec 2031 (10-K); Mar 2026 order form up to $21.0B through Dec 2032 incl. option (10-Q) | VERIFIED |
| Microsoft | MSA dated 2/22/2023 (exhibit); contract value not disclosed in filings read | VERIFIED existence / amount UNKNOWN |
| Jane Street | about $6.0B commitment announced Apr 2026 (10-Q risk factor); $1.0B equity at $109 in April | VERIFIED |
| Google | Not named as a customer in any CRWV filing text read. Appears as a competitor (10-K, 10-Q) and as the first "CoreWeave Interconnect" cloud partner (8/11 release). A 2025 report said CRWV would supply capacity for Google's OpenAI deal. | VERIFIED (competitor/partner); customer status UNKNOWN (reported only, not re-verified) |
| Nvidia | Not a customer in filings read. Sole GPU supplier ("all of the GPUs used in our infrastructure today are NVIDIA GPUs"; customers contractually specify Nvidia). Equity investor: 23M shares at $87.20 for $2.0B (Jan 2026); about 9% (FactSet via CNBC) / 10% (TIKR) holder. Jan 2026 collaboration framework. | VERIFIED (10-Q); holder % SECONDARY |

**Is Oracle a CoreWeave customer, counterparty or competitor?** The only occurrence of "Oracle" in the 10-K, Q1 10-Q and Q2 10-Q is the competitor list: "Key competitors that offer general purpose cloud computing services ... include Amazon (AWS), Google (Google Cloud Platform), Microsoft (Azure), and Oracle, a number of which are also our current customers." (10-Q risk factors, p. 58-ish). The "a number of which" clause does not say which. Oracle is not named as customer, lender, guarantor or landlord anywhere in the three filings. VERIFIED (text search, counts: 1 occurrence per filing). SEARCH-NOT-FOUND: any press report of an Oracle-CoreWeave contract.

**What the Oracle-CoreWeave CDS link is, by candidate mechanism:**

| Candidate link | Evidence | Verdict |
|---|---|---|
| Shared customer (OpenAI) | CRWV: OpenAI up to about $22.4B contracts (secondary) of about $104B backlog (about 20%, INFERRED arithmetic, note some contracts "up to"). Oracle: about $300B OpenAI deal (CNBC 10/19). On 10/8 an OpenAI-revenue report (annualised revenue "near $50B" vs "near $70B" a week earlier; part accounting, net basis) hit CRWV -7.77% to $81.58, and Oracle and Nvidia also fell (TIKR 10/9, SECONDARY). | Real, and the only one with a dated same-day co-move. OpenAI's ability to pay is a common tail risk. VERIFIED that both are OpenAI suppliers; magnitude of co-move on 10/8 for Oracle UNKNOWN |
| Shared lender base | CRWV agents: MUFG (DDTL 4.0, 5.5), JPMorgan (5.5), Morgan Stanley (5.0); ATM agents incl. DB, GS, JPM, MS, MUFG, Citi, TD, Wells. Oracle-side bank syndicates not examined here (DEWEY file covers a $3.3B lessor guarantee maturing Sept 2026). | Plausible overlap among the same large banks; not shown. INFERRED / UNKNOWN |
| Shared GPU vendor | Nvidia: sole CRWV supplier and 9-10% holder; Oracle buys Nvidia GPUs for OCI (not re-verified here). Nvidia CDS also rose sharply 10/15 (Reuters). | Real but generic; it is a supply chain, not a cross-default |
| Pure sector / rates beta | Reuters 10/15-16: hot US CPI (TIKR: Sept CPI 3.7% printed 10/14), higher-rate expectations; CDS records for Amazon, Alphabet, Meta, Nvidia too. CNBC 10/19: Oracle CDS 315 bp, "bridge between junk-rated neoclouds and investment-grade hyperscalers" (Rosenberg). | Dominant. Oracle CDS moved 260 (about 10/8) to 282-288 (10/15) to 295-315 (10/19-20) while CRWV went from 452 (June) to 1,038-1,194 |
| Direct contractual / cross-default | none found | SEARCH-NOT-FOUND |

**Verdict:** shared OpenAI-demand exposure plus sector financing/rates beta (both are "debt-funded AI capex with negative or thin FCF"); Nvidia as common vendor. Oracle sits in CRWV's filings as a competitor. The link is correlation through the AI-capex-funding trade, not a legal chain.

---

## 3. 2026 events (all VERIFIED from 8-K/10-Q unless marked)

| Date | Event |
|---|---|
| 2026-01 | Nvidia $2.0B private placement, 23M shares at $87.20; collaboration framework |
| 2026-03-30/31 | DDTL 4.0, $8.5B (MUFG) |
| 2026-04 | $2.75B 9.75% 2031 notes; $4.0B 1.75% 2032 convert; $1.0B equity at $109 (Jane Street, about 9M shares); Jane Street about $6.0B compute commitment |
| 2026-05 | DDTL 5.0, $3.1B (Morgan Stanley); S&P rating reported B+ / positive outlook (SECONDARY snippet, conflicting sources; Moody's UNKNOWN) |
| 2026-06 | $1.25B 9.625% 2032 notes and EUR 2.0B 8.5% 2032 notes; S-3ASR shelf filed 6/5; Nasdaq-100 inclusion |
| 2026-08-07 | DDTL 5.5, $2.6B |
| 2026-08-11 | Q2: backlog about $104B (plus more than $25B early Q3); 2026 capex guide raised to $35-39B from $31-35B; revenue guide $12.4-13.2B; adj. op. income $960M-1.15B; year-end run-rate $18.5-19.5B; active power 1.5 GW, contracted 3.7 GW (SECONDARY for guidance: Quartr public page, Channelchek; release itself defers guidance to the call). Stock +14% on the print (SECONDARY). |
| 2026-09-17/22 | $4.2B 2.875% 2033 convert; 35M-share ATM / collared forwards |
| 2026-10-08 | OpenAI revenue report; CRWV -7.77% to $81.58 (SECONDARY) |
| Core Scientific | Deal terminated: Core Scientific holders voted it down 10/30/2025 (all-stock, about $9B, $20.40/sh); CRWV remains its tenant. No Core Scientific text in the Q2 10-Q. VERIFIED (CRWV press release, secondary confirmations) |
| Downgrades / covenant news | None found in 2026 (SEARCH-NOT-FOUND for agency downgrade; Goldman UPGRADED to Buy and JPMorgan, Barclays, Deutsche Bank bullish this week per CNBC 10/22). No covenant breach reported; 10-Q compliance statement at 6/30. |
| Capital need | Q3 FCF consensus about -$10.1B (FactSet via CNBC); Baird estimates about $30B raise in 2027 (SECONDARY). 2026 capex $35-39B vs H1 capex $14.1B implies H2 capex $21-25B. |

**Insider selling (Form 4, VERIFIED, my sum of non-derivative code S rows with Form 4 filing date 9/1-10/14, shares x price):** about $191M across 9 officers, of which Intrator about $141M (1.62M shares), McVeety $22M, Agrawal $12M. Weekly sale-date totals: week of 9/1 $38M, 9/8 $42M, 9/15 $25M (incl. 9/14), 9/22 $32M, 9/29 $27M+$18M, 10/6 about $0, 10/12-13 $5M. So selling visibly STOPPED after 10/1. Press total: three co-founders (Intrator, Venturo, McBee) sold $3.3B since the March 2025 IPO, $2.4B in 2026 (Bloomberg, relayed by aiweekly 2026-10-16 and beinsure 10/17, SECONDARY); company: "All sales are pre-scheduled, fully disclosed" (10b5-1). Form 144s filed 9/29, 9/30 (7), 10/6, 10/13 (3) -- notices of proposed sales, amounts not parsed (UNKNOWN).

---

## 4. What drove the moves (dated closes; share-price closes are SECONDARY unless computed)

| Date | CRWV move | Catalyst, with source | Tag |
|---|---|---|---|
| 10/8 | -7.77% to $81.58 | OpenAI reported annualised revenue about $50B vs about $70B (TIKR 10/9). Oracle, Nvidia also fell. Also Benzinga 10/7 on the $2.6B DDTL 5.5 cash-trap structure. | SECONDARY |
| 10/14 (Wed) | -15.5% to $65.78 | Bloomberg report that CRWV unsecured bonds fell to distress levels (9.625% 2032 about 79.5, yield about 15%); hot Sept CPI 3.7% / rate-hike fear; Intrator memo "market misunderstands and acts irrationally ... backlog more than supports all of our debt obligations" | SECONDARY (Reuters, CNBC, TIKR, Admiral) |
| 10/15 (Thu) | +5.94% to $69.69 (intraday low $59.51) | Dip-buying; CDS record about 1,140 bp intraday, 1,038 last; Oracle CDS 282 | SECONDARY (CNBC) |
| 10/16 (Fri) | -11.91% (about $61.4 computed) | Bloomberg 10/16 piece: co-founders sold $3.3B since IPO, $2.4B in 2026; stock "down more than 60% from its June 2025 peak"; 9.625% 2032 near 78 cents. Same day: Deutsche/others bullish notes. | SECONDARY; causality INFERRED |
| 10/19-10/21 | flat to -1% (10/20 $62.13; 10/21 $61.82 per fleet anchors) | 9.625% 2032 YTM 14.9%; CDS about 1,082 bp (10/19) | SECONDARY (CNBC) |
| 10/22 (Thu) | -10.06% to $55.60 (fleet anchor; CNBC: "plunging 10% on Thursday") | CNBC (updated 10/22): "interest rates spiking and AI build-out concerns mounting"; stock -36% in October; CDS 1,145 bp (+39% in Oct); NextDC -40% after cutting earnings guide (Wed); Firmus IPO scrapped; Nscale IPO watch; credit desks say HY market "effectively on hold" until after midterms in two weeks; Intrator memo to staff Thursday ("range of funding options ... additional flexibility to raise equity over time"); market cap about $31B. Co-founder sale story still in circulation. | SECONDARY; no single trigger found. UNKNOWN whether the "additional flexibility to raise equity" line (ATM now eligible) was read as imminent dilution -- INFERRED only |

Not catalysts (checked): no CRWV 8-K, 424B or 10-Q since 9/22; no rating action found; no lockup expiry (IPO lock-up and Put Right ended in 2025: the Put Right terminated Sept 2025 per 10-Q). Peer co-moves: Nebius -33% and IREN -38% in October (CNBC).

---

## 5. CDS

**Reference entity and instruments (DTCC public SBS tape, 10/19-10/22 files; VERIFIED on the tape, interpretations INFERRED):**
- Entity: CoreWeave, Inc.; RED ID 239FAVSN1 (also 239FAV prefix). Prints also reference ISIN US21873SAC26 ("SR NT 144A", reference obligation, probably the 144A senior unsecured notes -- exact tranche not verified) and the generic "standard reference obligation" ID XSSNRREFOBL0.
- Standard 5.00% coupon contracts, upfront paid; clearing flags mixed ("I" = intermediated, "N" = not cleared).
- Tenors seen: Jun-2027, Dec-2027, Jun-2028, Dec-2028, Dec-2029, Dec-2030, Jun-2031, Dec-2031.

**Prints with a true notional (non-capped), upfront / notional, per 100:**

| Print (UTC) | Maturity | Notional | Upfront (pts) |
|---|---|---|---|
| 10/19 20:09 | Dec-2031 | $3M | 18.60 |
| 10/20 14:14 / 14:23 / 14:37 | Dec-2031 | $2M / $1M / $2M | 19.08 / 19.08 / 19.58 |
| 10/20 15:24 | Dec-2030 | $2M | 15.08 |
| 10/20 18:36 | Dec-2030 | $2M | 15.83 |
| 10/20 20:20 | Dec-2028 | $2M | 7.58 |
| 10/21 19:33-20:00 | Dec-2030 | $1M x3 | 14.94 / 14.69 / 14.63 |
| 10/21 20:55 | Jun-2027 / Jun-2028 | $2M | 0.32 / 4.07 |
| 10/22 14:05 | Dec-2031 | $3M | 18.31 |
| 10/22 18:30 | Dec-2027 | $2M | 3.56 |
| 10/22 19:33 | Jun-2027 | $0.5M | 1.31 |
| 10/22 20:29 | Jun-2031 | $2M | 18.06 |

Other prints are disseminated as "5,000,000+" (cap), so upfront per notional cannot be computed from them (e.g., 10/22 18:03 Dec-2031 $977,778 on an undisclosed notional of at least $5M).
Reading: curve is steep (about 0.3 pts at Jun-27 to about 18-19.6 pts at 5 years); the 10/22 5-yr prints (18.06-18.31) are at or inside the 10/20 prints (19.08-19.58). The 18.08 fleet anchor reproduces closely with the 10/22 Jun-2031 and Dec-2031 prints. Spread conversion is model-dependent and belongs to LIQUID.

**Level history (SECONDARY except tape):**

| Date | 5Y CDS | Source |
|---|---|---|
| June 2026 | about 452 bp | TIKR 10/19 |
| 10/15 | >1,100 bp (S&P Global MI); intraday >1,140; last 1,038; "record 1,194.5" (TIKR, vendor and date unstated) | Reuters, CNBC, TIKR |
| 10/19 | about 1,082 bp (about 2% lower than Friday) | CNBC |
| 10/22 | 1,145 bp (+39% MTD, +179% y/y) | CNBC |
Implied 5-yr default probability about 63-64% at 1,000 bp (Reuters/TokenPost; recovery-assumption dependent, SECONDARY). Oracle 5Y: 260 (a week before 10/15), 282-288 (10/15), 295-300 (10/16), 315 (10/19) (CNBC, Reuters, Securitas; sources differ).

**Liquidity.** Public tape count of CRWV new-trade prints: 14 across 10/19-10/20 (3 + 11), 7 on 10/21, 8 on 10/22 through 20:29 UTC; Oracle prints keyed by underlier name: 10 (10/20), 12 (10/21), 7 (10/22). So print counts are comparable to Oracle's, but many CRWV prints are small ($0.5-3M) or capped; an end-of-day 10/22 DTCC file has 12 "EROR" (error-correction) records on CRWV at 13:44 UTC touching every tenor -- a reporting correction, content UNKNOWN. S&P Global MI's Nolan called Oracle CDS "supported by high liquidity" (CNBC 10/19) and made no equivalent statement for CRWV. CRWV was NOT in the seven-name DTCC weekly-volume tally ($9B+/week for Oracle, SpaceX, Alphabet, Amazon, Meta, Broadcom, Nvidia in September; TokenPost). Net: tradable but thinner than the hyperscaler names; single-name volumes and open interest beyond the public tape UNKNOWN. Nebius has no tradable CDS (Reuters).

---

## 6. Equity

| Item | Value | Source / tag |
|---|---|---|
| Close 10/22 | $55.60, -10.06%; 10/21 $61.82 | fleet anchor |
| October 2026 path | 10/6 $91.72 -> 10/9 about $82 -> 10/14 $65.78 -> 10/15 $69.69 -> 10/16 about $61 -> 10/22 $55.60; -36% MTD, about -37% since 9/30 ($87) | SECONDARY (TIKR, CNBC, StocksToTrade), computed |
| From peak | market cap peak about $90B (June 2025) vs about $31B now (CNBC); stock "down more than 60%" from June 2025 peak (Bloomberg); YTD roughly flat to -10% at $65-70 (Reuters 10/16) and about -20% at $55.6 (INFERRED, YE25 price not pulled) | SECONDARY / INFERRED |
| Shares | Class A 458.9M + Class B 92.7M (7/31/26) = 551.5M; market cap at $55.60 about $30.7B (calc.) | VERIFIED (10-Q cover) |
| Dilution stack | options 23.6M, RSUs 29.3M, warrants 11.9M; converts max 52.6M (new) plus older converts; ATM 35M shares (about $1.9B at $55.60, calc.) | VERIFIED (424B5), calc. |
| Short interest | no October 2026 figure found. Stale: about 10.4% of float (Nov 2025), undated Fintel 20.5%. | SEARCH-NOT-FOUND (current); do not cite the stale figures |
| Lockups | none live (IPO lock-up ended 2025). Insider supply = 10b5-1 plans; ATM/collared forwards now eligible (30-day standstill passed about 10/17-18) | VERIFIED / INFERRED |
| Analysts | TIKR 10/19: 22 buy, 8 outperform, 8 hold, 1 underperform, 2 sell; avg target $140.58 (range $39-$278) | SECONDARY |
| Held by | Nvidia about 9% (FactSet); founders about 20% combined, "top six shareholders" (company, via Bloomberg) | SECONDARY |

---

## 7. Cross-checks against fleet anchors

- HYG file prices (2030 notes 85.76/14.44%; Feb-2031 81.75/14.91%; Oct-2031 81.74/15.12%) not re-verifiable here. Press yields are consistent in level: 9.625% 2032 YTM 14.9% (CNBC 10/19), 9.75% 2031 15.78% (CNBC 10/15), "about 15%" unsecured (CNBC 10/22).
- 10/16 -11.9% and 10/22 -10% confirmed by press (aiweekly/beinsure for 10/16; CNBC for 10/22). Fleet's "10/20 close $62.13 window high" not checked.
- CDS 18.08 pts upfront: reproduced within 0.2-0.3 pts by 10/22 Jun/Dec-2031 prints (18.06, 18.31).

## SUMMARY FOR PROME

1. 10/22 (-10.06% to $55.60) has no company-filing trigger: EDGAR shows no CRWV 8-K after 9/22 and no filing of any kind after 10/14 (VERIFIED 20:34 ET). CNBC (updated 10/22) cites spiking rates, AI-build-out worry, failed/weak neocloud capital events (NextDC -40%, Firmus IPO pulled, Nscale IPO pending), HY market "on hold" until after the midterms, and an Intrator staff memo saying it has "additional flexibility to raise equity" (SECONDARY). The ATM (35M shares, about $1.9B) became eligible about 10/17-18 (INFERRED relevance).
2. CDS did not lead: DTCC 10/22 5-yr prints (18.06-18.31 pts upfront) are at or inside 10/20 prints (19.1-19.6). Curve is steep (Jun-27 about 0.3 pts, Dec-28 7.6, Dec-30 about 15, Dec-31 about 18.5) = market prices late-dated refinancing risk, not an imminent miss.
3. 10/16 -11.9%: Bloomberg report that co-founders sold $3.3B since IPO ($2.4B in 2026) plus bond stress (SECONDARY; causality INFERRED). Form 4s show about $191M open-market sales 9/1-10/14, mostly Intrator, and virtually none after 10/2. 10/14 -15.5%: Bloomberg bond-distress story + hot CPI; 10/8 -7.8%: OpenAI revenue report.
4. Debt: $35.55B principal at 6/30 (recourse $31.8B, non-recourse $3.7B) + $16.5B leases; since then +$4.2B 2.875% 2033 converts (9/22), $2.6B DDTL 5.5, 35M-share ATM. Maturities $4.4B rest-2026, $6.2B 2027, $4.4B 2028. Cash $5.5B, liquidity $15.6B. Q2 net interest $640M vs GAAP operating loss $49M, operating cash flow $679M (calc.); Q3 interest guided $860-940M (SECONDARY). Capex guide $35-39B; FY26 H2 needs about $21-25B. Covenant compliance stated at 6/30; DDTL 5.5 DSCR 1.35x.
5. Concentration: Microsoft 67% of FY25 revenue; Q2-26 top three customers 36/26/10% (unnamed). Backlog $103.7B RPO, $104B revenue backlog, +$25B early Q3. OpenAI $11.9B + $6.5B filed (about $22.4B reported); Meta $14.2B + $21.0B filed; Jane Street about $6B. No per-customer backlog split filed.
6. ORACLE-CRWV LINK VERDICT: Oracle appears in CRWV's 10-K/10-Qs once, as a competitor; not a named customer, lender or counterparty. The link is (a) shared OpenAI dependence (Oracle about $300B; CRWV about $22B; both fell on the 10/8 OpenAI revenue report), (b) shared debt-funded-AI-capex and rates beta (CPI 3.7%), (c) Nvidia as common vendor. Shared-lender overlap among large banks is plausible (MUFG, JPM, MS on CRWV) but unproven. No contractual or cross-default tie found.
7. Load-bearing uncertainties: (i) whether any ATM / collared-forward sales have occurred since about 10/17 (no filing yet; 10-Q or 8-K will show); (ii) the 10/22 trigger is press-inferred only, and who owns the unnamed Customer A/B concentration and the DDTL 5.5 / 4.0 anchor contract (redacted).
8. Could not reach: Moody's/S&P/Fitch actions (one secondary snippet: S&P B+ positive, May 2026), current short interest, Benzinga/CNBC primary pages beyond what was fetched, Quartr transcripts (subscription required), HYG holdings file, Oracle-side lender list, volumes/open interest on CRWV CDS beyond the public tape.
