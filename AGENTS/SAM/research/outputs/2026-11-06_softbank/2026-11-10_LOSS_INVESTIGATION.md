# SoftBank Q2 FY2026 loss: SAM leg of PROME's investigation (Will's word, 17:18 ET 11/10)

**Read:** 2026-11-10 17:18–17:25 ET (clock). **Owner:** SAM (lead on SoftBank's own documents). Spending: $0. No threshold, gate, band, card or prediction moved.

**Other legs, not duplicated here:**
- VULCAN: the Pike County project; who got the advance payments; the OpenAI, Oracle and Stargate chain.
- LIQUID: SoftBank credit (CDS, bonds, yen retail).

**Sources (primary, SoftBank IR, re-fetched about 17:18 ET; SHA-256 prefixes):**
- financial report `financial-report_q2fy2026_01_en.pdf` (c3fa95f8)
- data sheet `earnings-datasheet_q2fy2026_02.pdf` (87990f8b)
- earnings deck `earnings-presentation_q2fy2026_01_en.pdf` (1e69c9ec)
- accounting deck `investor-accounting_q2fy2026_01_en.pdf` (2945557a)

**Page convention:**
- Financial report pages are given as PDF / printed (e.g. "fr 7/5").
- Deck and data-sheet pages are given as printed.
- The call transcript PDF still returns 404.

**Pass 1** (card 010, the line 55 correction): `2026-11-10_RESULTS_GRADE.md` § Correction, commit c3e000bc76.

## (1) Q2 loss bridge (Q2 alone, ¥B; data sheet p.2 consolidated; segment rows p.3 holding companies, p.16 Other)

| Line | Q2 | Segment / entity | Cash or not | Source |
|---|---|---|---|---|
| Gross profit | +1,143.4 | group | operating | ds p.2 |
| SG&A | −1,081.9 | group; H1 driver Arm share-based pay and Ampere (AI Computing +¥335.2B H1); Energy Global share-based pay ¥136.0B H1 | mixed; share-based pay is non-cash | ds p.2; acct p.7, p.10 |
| Gain on investments, net | −133.6 | holding cos **−303.9** (Intel shares **−270.1** in Q2); SVF **+245.6**; Other −75.3 | non-cash marks | ds p.2–3; deck p.14 |
| Finance cost | **−461.9** | holding cos −387.5. H1 SBG interest ¥676.4B, +¥407.2B YoY, incl. "full recognition of unamortized financing costs upon early repayment of the bridge loans" | mostly cash; the fee write-off is non-cash (amount not stated) | ds p.2–3; acct p.7 |
| FX gain | +220.3 | group | non-cash | ds p.2 |
| Derivative (excl. investments), net | −41.7 | holding cos **−314.1**, which contains the **Intel collar −321.9** (T-Mobile collar +¥49.3B H1); Other **+274.7**, consistent with the Energy Global warrant liability falling on the August partial forfeiture (SAM inference; H1 warrant loss ¥203.8B) | non-cash | ds p.2–3, p.16; fr 9/7; fr 71/69 |
| Change in SVF third-party interests | −2.6 | SVF | non-cash | ds p.2 |
| Other gain (loss) | **−669.9** | Other segment −676.0: **power equipment −597.2** (SB7) + **Lordstown, Ohio factory impairment −72.5** | ¥457.0B write-off of cash already paid; **¥140.2B cash from Q3**; impairment non-cash | ds p.2, p.16; fr 75/73 notes 1–2 |
| **Pre-tax** | **−1,027.9** | | | ds p.2 |
| Net income | −1,060.6 | | | ds p.2 |
| **Attributable to owners** | **−1,115.3** (Q1 +347.3; H1 −768.0) | | | ds p.2 |

The rows sum to the pre-tax line (SAM check: 1,143.4 − 1,081.9 − 133.6 − 461.9 + 220.3 − 41.7 − 2.6 − 669.9 = −1,027.9 ✓).

**Plain words:**
- About ¥1.25T of Q2's loss is **non-cash marks**: Intel shares, the Intel collar and the power write-off of money already spent.
- About ¥0.46T is **finance cost**, mostly cash interest.
- The only **new cash** that the write-off obliges is the ¥140.2B settlement.

## (2) The ¥597.2B power-equipment loss

| Question | Answer | Source |
|---|---|---|
| Entity | **Silver Bands 7 LLC (SB7)**, "a subsidiary in which SBG and SVF2 have invested, and a separate entity from SB Energy" | deck p.16, p.18; fr 7/5 |
| What for | "manufacturing capacity reservation agreements, equipment purchase contracts, and other arrangements for power generation-related equipment ... for AI data center projects in the U.S., including the PORTS-Pike Technology Campus". Bought "in anticipation of shortages"; "expect to recoup the investment through project financing" | fr 7/5; deck p.16 |
| To whom | **Not named.** No supplier name, and no "turbine", GE Vernova, Siemens, Mitsubishi Heavy or Bloom anywhere in the four documents (SAM grep) | — |
| Paid in total | FY2025 through 9/30: **¥1,500.9B ($9.48B)**; $3.9B in FY2025 and $5.6B in H1 FY2026 | fr 7/5; deck p.16 |
| Loss split | $2.9B (¥457.0B) of non-refundable advances, for equipment "no longer in the revised procurement plans"; $0.9B (¥140.2B) "contract modifications and settlements", with cash "expected from Q3 onward" | acct p.8; fr 75/73 |
| Ohio | **"The loss of $3.7B is completely unrelated to PORTS-Pike"** | acct p.8 |
| Still on the balance sheet | **$6.6B** of advances allocated to PORTS-Pike and others (deck p.18). The balance-sheet line "advance payments related to the acquisition of assets for power generation and AI data centers in the U.S." is **¥1,065.1B**, +¥386.4B in H1 | deck p.18; fr 29 |
| Rebates | Up to **$2.1B over 10 years** on future purchases, conditional; **not recognised** | fr 7/5 |
| Further commitments | Not quantified in what I read. No purchase-obligation table found for SB7 (SAM grep: "commitment", "purchase obligation"). How much more the $6.6B plan needs before project financing is a known-unknown | — |
| Guarantees | **No SBG guarantee of SB7 or of SB Energy found.** The financial report's guarantees are the SVF2 OpenAI-shares loan (¥1,543.7B) and Son-related receivables. Debt at wholly owned financing subsidiaries and SB Northstar is "non-recourse to SBG" | fr 14/12, fr 83 |
| SB Energy side | Not in the loss. Linked items in the same Other segment, at **Energy Global, LP**, the solar and data-center developer (SAM reading: consistent with SB Energy's parent; not stated as such in what I read): <br>• warrants to OpenAI, a **¥541.8B liability** at 9/30, partly forfeited in August with the PORTS-Pike lease <br>• **$1.5B** of advances received under a share-issuance agreement <br>• **¥552.9B** paid in H1 for US power and data-center assets <br>The PORTS-Pike credit support is NVIDIA's (deck p.45, citing SB Energy's 8/17 release) | fr 37, fr 71/69, fr 39; acct p.10 |
| More loss flagged? | **None flagged.** The deck calls it a realignment "following a review of the project portfolio". No impairment trigger is named for the remaining $6.6B | deck p.17 |

## (3) The ¥321.9B Intel collar

| Question | Answer | Source |
|---|---|---|
| Structure | Prepaid forward **collar** contracts by **a wholly owned financing subsidiary**, August 2026, backed by **all 87.0M Intel shares** held. Shares to deliver at settlement are set by Intel's price at valuation dates, within a **cap and floor** on the per-share settlement price | fr 6/4, fr 71/69 note 2; acct p.9 |
| Raised | **$7.35B** (deck: $7.4B; "monetized at 3.7x the acquisition cost", against $2B cost at $23 in August 2025) | fr 9/7; deck p.70 |
| Liabilities at 9/30 | Prepaid-forward financial liability **¥1,139.6B**; derivative liability **¥337.9B** ($2.147B) | fr 14/12, fr 71/69; acct p.9 |
| Why the loss | Intel rose between the August execution and 9/30, so the collar's liability rose. Intel's fair value at 9/30 was $10,455M ($120.23 a share; June 30: $139.63, $12,142M) | fr 9/7; acct p.9 |
| Recourse | Financing-subsidiary debt is **"non-recourse to SBG"** | fr 14/12 |
| Counterparty, cap and floor levels, settlement dates, margin terms | **Not disclosed** in the four documents | — |
| Remaining exposure | Above the cap, gains go to the counterparty. Below the floor, SoftBank is protected. Between the two, SoftBank keeps the price risk on the shares to be delivered. In the leverage ratio Intel counts **net of the settlement amount** | deck p.82 item a |
| Zero Hedge's "rights of use" on ¥1.1T of ¥1.65T of shares | Not found in these documents. Intel's carrying amount is ¥1,645.1B (fr 29), which is consistent with the ¥1.65T figure | fr 29 |

## (4) Leverage, cash and ceiling language

- **15.9% at 9/30** (net debt ¥11.30T ÷ holdings ¥71.14T; ds p.17). Both losses are inside it.
- **Intel:** holdings value is net of the settlement amount (deck p.82 item a). The collar liability is deducted from net debt (item i). So the derivative loss has **no separate LTV effect**.
- **Power:**
  - The cash went out before 9/30. SBG's stand-alone Q2 cash bridge carries "Data center and power generation-related expenditures **−¥0.4T**" (deck p.79).
  - The **¥140.2B** settlement still to pay is about **+0.2 point** if SBG funds it.
  - Whether SB7's equity sits in "Others (b)" unlisted holdings is not stated.
- **Roll to Arm $181.49** (vendor, 11/10 regular-session close; USD/JPY 158.69 live 17:23 ET), on SoftBank's basis: **22.7%**. With the settlement: **22.9%**. 25% is reached at Arm about **$145** (about **$149** with the settlement); 35% at about $45 (`ltv_lookup.py`, SAM arithmetic).
  - Not in any figure: the ABB $5.4B (about +1.2 points if debt-funded) and the October $10B OpenAI tranche (included in the roll, per the grade file).
- **Cash:**
  - **¥5.0T ($32B)** against **¥1.6T ($10B)** of bond redemptions over two years (deck p.23).
  - The cash figure includes ¥511.4B of undrawn lines and excludes ¥934.3B of SB Northstar PB borrowing.
  - Q2: record financing of **$56.5B**; the **$40B bridge was fully repaid** early (deck p.66).
- **Ceiling language, unchanged:**
  - "Maintain LTV below 25% in normal circumstances (upper threshold of 35% even in extraordinary circumstances)".
  - "Maintain at least 2 years' worth of bond redemptions in cash position" (deck p.65).
- **Covenants:** **none disclosed.** No "covenant" hit in the four documents (SAM grep).
- **Ratings as of 11/10** (deck p.71):
  - **JCR A, outlook Negative**
  - **S&P BB+**, outlook revised Negative → **Stable on 7/16**
  - **Fitch BB+ Stable**, newly assigned 9/11
  - No post-results rating action in these documents. Agency actions are LIQUID's leg.

## (5) Musk's turbine claim

- **The claim:** X, 11/6: "SoftBank is defaulting on its turbine orders." It named no supplier, order, amount or project (card 20261109-005).
- **What the documents say:**
  - **Corroborated in part:** SB7 did cut equipment orders. It realigned its procurement, wrote off $2.9B of advances for equipment no longer in the plan, and took $0.9B for "contract modifications and settlements" tied to "SB7's obligations to its suppliers".
  - **Contradicted on "default":** SoftBank describes negotiated modifications and settlements, with cash to be paid and rebates won. That is not a failure to pay.
  - **Narrowed on Ohio:** "completely unrelated to PORTS-Pike".
  - **Not established:** that the equipment was turbines. The documents say only "power generation-related equipment".
- **Who it was:** the counterparty is unnamed.

## (6) Why 9984.T rose 13.88% on 11/10

| Fact | Basis |
|---|---|
| 9984.T closed ¥3,872 (+13.88%) on 11/10, after **¥4,765 on 10/29 → ¥3,400 on 11/9 (−28.6% in eight sessions)**. Still −18.7% from 10/29 | vendor daily closes (yfinance), completed sessions |
| SoftBank released at **15:30 JST, the Tokyo close** (01:30 ET; card 005; my grade file) | so the 11/10 Tokyo session **did not trade on the loss** |
| US ADR **SFTBY $11.27, −4.00%** on the 11/10 US session, the first full session after the release | vendor, completed US session |
| First Tokyo session on the results: **11/11, opens 09:00 JST = 19:00 ET tonight** | — |

- **Plain words:** the +13.88% is not the market shrugging off the loss. It traded before the loss was public, as a rebound after an eight-session slide. The first reaction to the loss is the ADR's −4.0%, with Tokyo's reaction still to come.
- **Unknown:** what drove the 11/10 in-session rally. Two searches found no dated report of it (secondary search, about 17:24 ET).
- **Offsetting messages in the release itself** (deck):
  - record quarterly financing and the bridge repaid early;
  - cash at more than two years of redemptions;
  - pro forma NAV ¥44.7T;
  - Gotō (⚠️ secondary AI transcript): "well under 25%", OpenAI round uplift "likely in the third quarter".

## (7) Corrections in SAM's records

| Surface | Was | Now |
|---|---|---|
| Grade line 55 | "no route to SoftBank's leverage" | **Corrected** in pass 1: there is a route through the SB7 write-off, already inside 15.9%, about +0.2 point pending |
| Grade row 9, the SB Energy guarantee | none found | **Stands, narrowed**: SB7 is a different entity; no SB7 guarantee found either |
| Grade "Other figures" | six-month −¥768.0B only | Q2 alone **−¥1,115.3B** added (pass 1 § Correction) |
| STATUS line 7 | "Musk's turbine claim has no route" | **Corrected** 17:20 ET (c3e000bc76) |
| Arm margin loan maturity | the "9/2027" relay | Already superseded in the grade (2 years + 1 from Sep 2026). Zero Hedge's "to 2028" relay fits, but is not primary |
| Kill-on-sight lines | — | **Unchanged.** Still never "SoftBank reported 22%" and never the 9/30 figure as today's leverage. **Added:** do not call the power loss a "default" or an "Ohio write-off" |
| Grade letter | CONFIRMED | **Not touched** |

## Known-unknowns (each named)

1. SB7's suppliers and whether the equipment was turbines. SoftBank names neither; VULCAN's leg may.
2. SB7's remaining purchase obligations beyond the $6.6B of advances, and the size and timing of project financing.
3. Whether SBG stand-alone or SB7 or SVF2 pays the ¥140.2B settlement. The +0.2 point assumes SBG.
4. Whether SB7's equity is valued in "Others (b)" in the LTV.
5. The Intel collar's counterparty, cap and floor, settlement dates and any margining. Zero Hedge's "rights of use" claim is unverified.
6. The non-cash share of Q2 finance cost (the unamortised bridge fees).
7. Energy Global's identity relative to SB Energy (SAM reading only).
8. The driver of the 11/10 Tokyo rally, and the 11/11 Tokyo reaction (opens 19:00 ET).
9. Gotō's words at the primary (SoftBank's transcript is still 404).
10. Rating-agency reaction after the results (LIQUID's leg).
