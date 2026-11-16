# Who is paying to extend each stressed credit CREED follows — 2026-11-16

**Written:** 2026-11-16 (Mon) by CREED at PROME's 13:45 ET examination-list assignment, item 3 (prome-6f, on Will's word). **Logging only: this file moves no score, band, gate, trigger, prediction or case status.** It is a dated reading of evidence already on file, plus the October Trepp special-servicing report read today. It is not a forecast and not a trade input.

**Question asked of every credit:** who is funding the delay (sponsor equity, a lender modification or forbearance, an interest reserve or cash trap, rescue or preferred capital, a parent), and how long can that party keep paying, on the evidence held (a reserve balance, a maturity, a covenant date)? **UNKNOWN is an answer.** "NONE" means the delay is over: the loan has been foreclosed, sold, liquidated or put in a receiver's hands, or is in enforcement.

**Perimeter:** every row in `cases/CASES.tsv` whose `latest_status` is not a completed exit (SOLD, REO, FORECLOSED and NOTE_SALE are excluded) — 89 cases, including CASE-185 and CASE-186 added today — plus four lender- and fund-level credits CREED follows. A case's evidence lives in `cases/CASES.tsv`, `cases/CASE_EVENTS.tsv` and `cases/CASE_NOTES.md`; this file restates only what answers the question. ⚠️ The case ledger is a selection of named cases (`cases/README.md`, selection-bias limit). Counts here describe that ledger, not the market.

## Count (89 case rows)

| Answer | Cases |
|---|---:|
| A named party is paying to extend | 23 |
| NONE: delay over, enforcement or exit under way | 29 |
| UNKNOWN: evidence on file does not say | 35 |
| Not a distressed credit, or a duplicate row | 2 |

**So what:** where a payer is named, it is mostly the **lender** (modifications, forbearance, grace, or a trust carrying a delinquent loan), and in five cases the **sponsor** put in cash alongside (IMC paydown, RaDD $100M, The Jack $2.6M, S2 paydown, Sullivan recap). Dated runways are few: IMC to April 2027, Point at Rockridge to February 2027, Park West Village to August 2027, RaDD to December 2029, one S2 loan to July 2031, Blackjack about three months from October (SECONDARY). No interest-reserve **balance** is on file for any case, so no "months of reserve left" figure can be given. The 540 West Madison cash trap is the closest, and it reads "paid through 10/6/26" with no balance.

## Lender- and fund-level credits

| Credit | Who is paying to extend | How long, on the evidence held | Basis |
|---|---|---|---|
| ACRES Commercial Realty (ACR), Morgan Stanley repo facility | **The repo lender**: Morgan Stanley extended the facility to November 2027 and, on CREED's reading of a colour redline, cut the interest-coverage floor to 1.15x | Floor 1.15x for quarters ending 9/30/26 through 9/30/27, then 1.25x through 3/31/28, then 1.35x. ⚠️ The 1.15x comes from a heuristic parse; verify on the rendered Exhibit 99.1 before citing it outside the KB | `KB-CREED-117`, 8-K PRIMARY-READ |
| Arbor Realty Trust | **Shareholders**, in effect, by forgoing the dividend (suspended 10/30); who funds its delinquent borrowers is UNKNOWN | UNKNOWN | `KB-CREED-097` |
| Starwood Real Estate Income Trust (SREIT), redemption gate | **Redeeming investors** wait; the board stopped redemptions to avoid selling assets at depressed prices | No end date stated; in force since 2026-04-29 (last census 10/28) | `VX-CREED-5.03`, 8-K PRIMARY-READ |
| United Fidelity Bank, FSB | UNKNOWN. Parent support is constrained by a 2024 Federal Reserve agreement requiring prior approval for parent distributions and debt | At unchanged risk-weighted assets, reaching the 8% total-capital line needs $40.705M more capital; CET1 sits $13.239M above 4.5%. These are DEWEY's fixed-denominator figures, not a loss budget | `KB-CREED-120`, DEWEY 11/11 (Call Report read by DEWEY) |

## Case lines (one per live case)

| Case | Property | Status | Who is paying to extend | How long | Basis |
|---|---|---|---|---|---|
| `CASE-CREED-003` | 1740 Broadway | UNKNOWN | NONE: loan liquidated May 2024, loss realized | n/a | DBRS via Will workbook |
| `CASE-CREED-006` | Lafayette Centre | SPECIAL_SERVICING | UNKNOWN | UNKNOWN | only a 2024-06 SS transfer on file |
| `CASE-CREED-008` | AMA Plaza | FORECLOSURE | UNKNOWN | UNKNOWN | only a 2024-11 foreclosure complaint on file |
| `CASE-CREED-011` | Blackhawk Plaza | BANKRUPTCY | Chapter 11 stay (filed 2026-03-18) holds off the receivership; who funds operations UNKNOWN | UNKNOWN: no plan or sale date on file | research notes, SECONDARY |
| `CASE-CREED-012` | Gateway I and II | UNKNOWN | UNKNOWN | UNKNOWN: 2025 auction outcome not on file | search listing only |
| `CASE-CREED-013` | Alessandro Plaza | BANKRUPTCY | Chapter 11 stay (filed 2026-08-18); funding UNKNOWN; listed for sale | UNKNOWN | SECONDARY |
| `CASE-CREED-014` | Plaza Continental | BANKRUPTCY | Chapter 11 stay (filed 2026-03-30); operations run on the lenders' cash collateral (rents) under court order | UNKNOWN: final cash-collateral hearing 2026-11-17; plan and disclosure statement unread, so no end date | DEWEY 11/11-11/12, docket |
| `CASE-CREED-015` | Starwood Hotel Portfolio Whole Loan | SPECIAL_SERVICING | UNKNOWN (DSCR 0.64 mid-2025, so property cash did not cover debt service; who covered the gap is not on file) | UNKNOWN | SECONDARY |
| `CASE-CREED-017` | Chino Towne Center (Nano/WAL collateral parcel) | BANKRUPTCY | Chapter 11 stay; funding UNKNOWN | UNKNOWN | debtor filing via DEWEY |
| `CASE-CREED-018` | Cedar Group Apartments | UNKNOWN | UNKNOWN (no default event filed; MF, HOMER's lane) | UNKNOWN | Redfin record |
| `CASE-CREED-020` | Baltimore Peninsula land | DEFAULT | LENDER FORBEARANCE: Bank OZK carries the matured loan on nonaccrual ($40.0M carrying) while the borrower seeks buyers | UNKNOWN: no date stated; OZK says it takes title only if sales fail | OZK Q2-26 management comments, PRIMARY-CITED |
| `CASE-CREED-023` | Concord Tech Center | UNKNOWN | NONE: foreclosed (Feb 2026) | n/a | SECONDARY |
| `CASE-CREED-025` | The Jack | DEFAULT | SPONSOR EQUITY (a $2.6M paydown) plus LENDER (OZK nonaccrual) pending a recapitalization LOI | UNKNOWN: close was expected in Q3 2026, outcome not read | OZK Q2-26 MC, PRIMARY-CITED |
| `CASE-CREED-026` | Renaissance Milwaukee West (Wauwatosa hotel) | DEFAULT | LENDER (OZK nonaccrual) pending the sponsor's sale; earnest money non-refundable | UNKNOWN: close expected Q3 2026, outcome not read | OZK Q2-26 MC, PRIMARY-CITED |
| `CASE-CREED-027` | Sullivan Courthouse | MODIFIED | RESCUE CAPITAL: sponsor plus a new capital partner recapitalized it into a new pass-rated OZK loan; Brookfield took the deed 7/2 for $1 plus ~$232M assumed mortgage (SECONDARY) | UNKNOWN: new loan size and term undisclosed | OZK MC PRIMARY-CITED; deed SECONDARY |
| `CASE-CREED-031` | 1 South Wacker | DEFAULT | UNKNOWN (maturity default 2026-06-09; SS transfer unconfirmed) | UNKNOWN | SECONDARY |
| `CASE-CREED-032` | Aon Center | UNKNOWN | Nobody on the evidence held: owner reportedly DENIED a three-year extension (SECONDARY, unverified) | UNKNOWN | newsletter pasted by Will 10/01 |
| `CASE-CREED-033` | 75 West Apartments | DEFAULT | UNKNOWN (MF, HOMER's lane) | UNKNOWN | SECONDARY |
| `CASE-CREED-035` | Yorktown Center | SPECIAL_SERVICING | UNKNOWN (in SS after a maturity default) | UNKNOWN | TreppWire, SECONDARY |
| `CASE-CREED-036` | Sangertown Square | SPECIAL_SERVICING | Nobody now: the lender extended twice before; a DSCR hurdle blocked the third extension, so it went to SS | UNKNOWN | crenews, SECONDARY |
| `CASE-CREED-037` | Meadows Mall | SPECIAL_SERVICING | UNKNOWN (in SS at maturity) | UNKNOWN | crenews, SECONDARY |
| `CASE-CREED-038` | 6810 Mannheim Road (dual-brand O'Hare hotel) | DEFAULT | NONE: foreclosure litigation | n/a | headline only |
| `CASE-CREED-039` | Project James | SPECIAL_SERVICING | UNKNOWN (DSCR 1.30x, so property cash covers debt service while in SS; payoff failed at August maturity) | UNKNOWN | Trepp Aug SS, PRIMARY-READ |
| `CASE-CREED-040` | 111 Livingston St | SPECIAL_SERVICING | UNKNOWN | UNKNOWN | Trepp Aug SS names it only |
| `CASE-CREED-041` | 60 Madison Ave | SPECIAL_SERVICING | UNKNOWN | UNKNOWN | Trepp Aug SS names it only |
| `CASE-CREED-042` | BXHPP 2021-FILM (Hollywood studio-and-office loa | SPECIAL_SERVICING | LENDER MODIFICATION in progress: a 30-day documentation extension executed and a framework for a longer extension agreed; DSCR 1.45x, so property cash pays debt service | UNKNOWN: length of the longer extension not stated | Trepp Aug SS, PRIMARY-READ |
| `CASE-CREED-043` | Hyatt Regency New Orleans | SPECIAL_SERVICING | UNKNOWN | UNKNOWN | Trepp Aug SS names it only |
| `CASE-CREED-044` | Fresno Fashion Fair Mall | SPECIAL_SERVICING | UNKNOWN | UNKNOWN | Trepp Aug SS names it only |
| `CASE-CREED-045` | Harlem USA | SPECIAL_SERVICING | UNKNOWN | UNKNOWN | Trepp Aug SS names it only |
| `CASE-CREED-046` | 315 South Beverly Drive | UNKNOWN | NONE: disposed, loss 100% of balance | n/a | CREFC Aug, PRIMARY-READ |
| `CASE-CREED-047` | La Terraza | UNKNOWN | NONE: disposed, loss 31.4% of balance | n/a | CREFC Aug, PRIMARY-READ |
| `CASE-CREED-054` | Republic Plaza | RECEIVERSHIP | NONE: receiver (Trigild) appointed after Brookfield's default | n/a | SECONDARY |
| `CASE-CREED-061` | 475 17th St. | UNKNOWN | UNKNOWN (auction lead only) | UNKNOWN | LEAD |
| `CASE-CREED-078` | Centre Square | UNKNOWN | NONE: court-approved sale at $70M proposed; closing unconfirmed | n/a | PRIMARY-CITED via Will workbook |
| `CASE-CREED-081` | One Lincoln (prior benchmark) | FORECLOSURE | NONE: creditor auction completed March 2025 | n/a | SECONDARY |
| `CASE-CREED-083` | GSA Regional Office Building (301 7th St SW) | UNKNOWN | UNKNOWN (government disposition lead) | UNKNOWN | LEAD |
| `CASE-CREED-105` | Concourse office building (1 Copley Parkway) | FORECLOSURE | NONE: creditor bid reported (unverified) | n/a | LEAD |
| `CASE-CREED-106` | Meidinger Tower (462 S 4th St) | UNKNOWN | UNKNOWN (proposed sale failed) | UNKNOWN | LEAD |
| `CASE-CREED-107` | Corporate 500 (500-540 Lake Cook Road) | FORECLOSURE | NONE: foreclosure and marketing under way | n/a | LEAD |
| `CASE-CREED-109` | 50 Columbus Blvd. | UNKNOWN | UNKNOWN (listing only) | UNKNOWN | LEAD |
| `CASE-CREED-110` | Palisades Center (1000 Palisades Center Dr.) | FORECLOSURE | NONE: resolved with loss Oct 2025; creditor auction 2026-02-04 | n/a | SECONDARY |
| `CASE-CREED-112` | X Denver (3000 & 3100 Inca St.) | UNKNOWN | UNKNOWN (receivership requested Sep 2026; MF, HOMER's lane) | UNKNOWN | SECONDARY |
| `CASE-CREED-116` | Parkmerced — operating apartment collateral | FORECLOSURE | NONE: foreclosure being pursued (MF, HOMER's lane) | n/a | PRIMARY-CITED via Will workbook |
| `CASE-CREED-117` | Parkmerced — four redevelopment parcels | FORECLOSURE | NONE: creditor takeover July 2026 | n/a | SECONDARY |
| `CASE-CREED-118` | San Francisco Centre (865 Market St.) | UNKNOWN | NONE: lender-owned after the Nov 2025 auction; being sold | n/a | SECONDARY |
| `CASE-CREED-121` | 135 West 50th Street — leasehold | UNKNOWN | UNKNOWN (ground-lease termination disputed) | UNKNOWN | PRIMARY-CITED via Will workbook |
| `CASE-CREED-123` | Ashford Hospitality Trust — KEYS Pool A | UNKNOWN | NONE: receiver sold to a third party | n/a | PRIMARY-CITED via Will workbook |
| `CASE-CREED-124` | Ashford Hospitality Trust — KEYS Pool B | UNKNOWN | NONE: receiver in control; partial dispositions | n/a | PRIMARY-CITED via Will workbook |
| `CASE-CREED-125` | IMC / Andmore showroom portfolio | EXTENDED | SPONSOR PAYDOWN plus LENDER EXTENSION: returned to current after an extension and paydown | to April 2027 (the extended maturity) | Trepp Oct DQ, PRIMARY-READ |
| `CASE-CREED-126` | 650 Madison Avenue | UNKNOWN | UNKNOWN (brought current Dec 2025; who funded the cure not stated) | UNKNOWN | PRIMARY-CITED via Will workbook |
| `CASE-CREED-127` | Bank OZK life-science loan — property unnamed | UNKNOWN | NONE: paid off with a charge-off | n/a | PRIMARY-CITED via Will workbook |
| `CASE-CREED-128` | Bank OZK recapitalized credit — property unnamed | UNKNOWN | see CASE-CREED-027 (duplicate row) | see 027 | — |
| `CASE-CREED-130` | Park Greene Apartments | SPECIAL_SERVICING | UNKNOWN (transferred for imminent default; MF, HOMER's lane) | UNKNOWN | PRIMARY-CITED via Will workbook |
| `CASE-CREED-131` | Seventeen Hundred | UNKNOWN | UNKNOWN (lien dispute; mortgage default not established) | UNKNOWN | PRIMARY-CITED via Will workbook |
| `CASE-CREED-132` | Arbor Q2 2026 Texas bridge-loan resolution cohor | FORECLOSURE | NONE: foreclosed and resold, Arbor financing the buyers (lender funds the exit, not a delay) | n/a | PRIMARY-CITED via Will workbook |
| `CASE-CREED-133` | Sterling Apartments (2055 Center Avenue) | UNKNOWN | UNKNOWN (historical guaranty ruling) | UNKNOWN | PRIMARY-CITED via Will workbook |
| `CASE-CREED-135` | 2100 Ross | FORECLOSURE | UNKNOWN (auction was set for 2026-10-06; outcome not read) | UNKNOWN | SECONDARY |
| `CASE-CREED-136` | Michigan Plaza | DEFAULT | NONE: Barings is selling the nonperforming note | n/a | Trepp article, PRIMARY-READ |
| `CASE-CREED-137` | The Wade Hotel | UNKNOWN | n/a: an equity sale by Park Hotels, not a distressed loan | n/a | PRIMARY-READ |
| `CASE-CREED-144` | Wolfchase Galleria | SPECIAL_SERVICING | UNKNOWN | UNKNOWN | Trepp Sep SS names it only |
| `CASE-CREED-146` | Pembroke Lakes Mall | SPECIAL_SERVICING | UNKNOWN (maturity default March 2025, still in SS 20 months later; a foreclosure filing is unverified) | UNKNOWN | SECONDARY / LEAD |
| `CASE-CREED-147` | The Wymore 360 | SPECIAL_SERVICING | NONE: SS strategy is foreclosure; paid through 2026-07-06 | n/a | PRIMARY-CITED |
| `CASE-CREED-148` | St. Luke's Office | SPECIAL_SERVICING | UNKNOWN (paid through 2026-08-06; transferred for imminent default after Intel left) | UNKNOWN | PRIMARY-CITED |
| `CASE-CREED-149` | One SoHo Square | SPECIAL_SERVICING | BORROWER, by staying current: the loan pays while in SS for an imminent maturity default | UNKNOWN: Trepp prints a 2028-08-06 maturity in the same paragraph, unresolved | Trepp, PRIMARY-READ |
| `CASE-CREED-151` | 33 W Monroe | RECEIVERSHIP | NONE: court-appointed receiver | n/a | SECONDARY |
| `CASE-CREED-152` | 131 S Dearborn | UNKNOWN | UNKNOWN (equity-pledge enforcement by Decama Finance, not a lender foreclosure) | UNKNOWN | SECONDARY |
| `CASE-CREED-153` | Illinois Center (two towers) | FORECLOSURE | NONE: sheriff sale was set for 2026-11-12; special servicer LNR expected to bid; outcome unread 11/16 | n/a | SECONDARY |
| `CASE-CREED-154` | RaDD (Research and Development District) | EXTENDED | SPONSOR EQUITY ($100M fresh capital) plus LENDER EXTENSION (Bank OZK); OZK still holds $335.9M unfunded commitment | to December 2029 (extended maturity) | OZK 8-K 10/12, PRIMARY-CITED |
| `CASE-CREED-156` | Forge Atlanta (land) | MODIFIED | LENDER GRACE: the seller-lender (McCall Railroad) let the note pass its 2026-10-01 maturity with interest and fees unpaid | UNKNOWN: grace of undetermined duration | Webstar 10-K/A, PRIMARY-CITED |
| `CASE-CREED-157` | Westbrook Corporate Center | FORECLOSURE | NONE: in foreclosure | n/a | Trepp article, attributed |
| `CASE-CREED-158` | Continental Towers | DEFAULT | UNKNOWN (90+ days delinquent) | UNKNOWN | Trepp article, attributed |
| `CASE-CREED-160` | 320 West 31st Street (leasehold) | FORECLOSURE | NONE: foreclosure complaint by the loan's assignee | n/a | SECONDARY |
| `CASE-CREED-162` | Blackjack Portfolio (remaining 6 properties) | SPECIAL_SERVICING | LENDER (the BX 2021-21M trust): a three-month extension to sell the remaining properties (Morningstar via HOMER, SECONDARY, unverified) | about three months from the October transfer, roughly into January 2027 (exact date not read) | Trepp Oct SS PRIMARY-READ for the trust; extension SECONDARY |
| `CASE-CREED-163` | Point at Rockridge (seniors housing) | MODIFIED | LENDER MODIFICATION (agency K-deal): paying under modified terms | to February 2027 | Trepp study, attributed |
| `CASE-CREED-164` | Corinthians Retirement Community | DEFAULT | UNKNOWN (60 days delinquent) | UNKNOWN | Trepp study, attributed |
| `CASE-CREED-165` | Park West Village | MODIFIED | LENDER MODIFICATION by the special servicer (Nov 2025) | to August 2027 (modified maturity) | SECONDARY |
| `CASE-CREED-167` | NYAH Portfolio (JPMCC 2021-NYAH + mezz) -- 31 NY | SPECIAL_SERVICING | LENDER (the trust): delinquent since June 2025 and carried in SS; servicer lists a modification as the workout | UNKNOWN | Trepp, SECONDARY |
| `CASE-CREED-168` | Parkhill City (PKHL 2021-MF) | RECEIVERSHIP | NONE: receiver since July 2025; foreclosure ruling expected by end-2026 | n/a | SECONDARY |
| `CASE-CREED-169` | MFP Portfolio (JPMCC 2019-MFP) -- Chetrit 43-pro | SPECIAL_SERVICING | NONE: remaining six properties auctioned Aug 2026, subject to court approval | n/a | SECONDARY |
| `CASE-CREED-170` | S2 Capital sponsor cohort (TX/AZ multifamily): M | MODIFIED | LENDERS (modifications and refinancings on 26 properties, ~$1.2B) plus SPONSOR principal paydown; Capital One dismissed an $11.5M guaranty claim (SECONDARY) | one loan to July 2031 (North Dallas, 531 units); the rest UNKNOWN | S2 release, PRIMARY-READ |
| `CASE-CREED-171` | 540 West Madison | DEFAULT | CASH TRAP: debt service is paid from the property's cash-management account; pre-negotiation agreement signed, no resolution | paid through 2026-10-06; no reserve balance read, so the runway is UNKNOWN | GS3 10-D, PRIMARY-READ |
| `CASE-CREED-172` | Salesforce Tower (Indianapolis) | DEFAULT | Nobody yet: balloon unpaid at 2026-09-01; owner seeking a refinancing with JLL; not in SS | UNKNOWN | 10-D, PRIMARY-READ |
| `CASE-CREED-173` | Moxy Oakland Uptown (former; 172-room hotel) | RECEIVERSHIP | NONE: hotel closed, receiver, ACORE marketing the note | n/a | SECONDARY |
| `CASE-CREED-175` | Wilshire Courtyard | DEFAULT | UNKNOWN (matured July 2026; cured in September and delinquent again in October, CREED inference) | UNKNOWN | Trepp Oct DQ, PRIMARY-READ |
| `CASE-CREED-176` | Cove at Tiburon | DEFAULT | LENDER MODIFICATION (Nov 2025, term through Oct 2026); a six-month extension request is under review | to October 2026 done; about April 2027 if the request is granted | Trepp Oct DQ, PRIMARY-READ |
| `CASE-CREED-177` | Beaudry (downtown LA apartment tower) | UNKNOWN | NONE: Brookfield walked away; a loan sale is being sought | n/a | SECONDARY |
| `CASE-CREED-184` | 35 West Wacker (Leo Burnett Building) | FORECLOSURE | NONE: foreclosure filed 2026-11-03; payments stopped July | n/a | SECONDARY |
| `CASE-CREED-185` | 2400 Market | SPECIAL_SERVICING | UNKNOWN (new October SS transfer) | UNKNOWN | Trepp Oct SS, PRIMARY-READ |
| `CASE-CREED-186` | Project Prime (84-hotel portfolio) | SPECIAL_SERVICING | UNKNOWN (imminent monetary default; DSCR 1.25x, so property cash still covers debt service) | no extension on file; loan matures 2026-12-06 | Trepp Oct SS, PRIMARY-READ |
