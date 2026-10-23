# Reader I: The Paramount Skydance / Warner Bros. Discovery merger pause (7/24 to 10/6) and what is left after closing

**Prepared:** 2026-10-22 20:53 ET (per `date`). Read-only reader I for PROME. 16 of 25 WebSearch calls used; SEC EDGAR pulled directly (curl, data.sec.gov and Archives); CourtListener RECAP API for the dockets; `FORGE/tools/market-data/fetch.py` plus the Yahoo chart endpoint for prices.
**Tokens:** VERIFIED = read at the primary (SEC filing, court docket/order). INFERRED = supported, not directly established. SEARCH-NOT-FOUND = query returned nothing. UNKNOWN. SECONDARY = press or aggregator, not checked at a primary. No trade recommendation.

## 0. The premise is void: the deal closed 2026-10-06

PROME's brief (and my search results from August) describe a live pause. It ended. Corrections, all VERIFIED unless marked:

| Brief said | Primary says | Source |
|---|---|---|
| Deal paused until a merits ruling or 2027-06-01 | Pause (stipulation 2026-07-24) ended by a consent decree: signed 2026-09-21, entered and the no-close order dissolved by Judge Martínez-Olguín on **2026-09-30** (Dkt 266 in 4:26-cv-07116-AMO) | 8-K filed 2026-09-30, acc. 0001104659-26-112347; CourtListener docket 73606877 entry 266 |
| Merger closed? | **Closed 2026-10-06**; WBD is a wholly owned subsidiary; company renamed Skydance Corp, NYSE SKYD | 8-K filed 2026-10-06, acc. 0001104659-26-113913; 13D/A filed 2026-10-08 ("On October 6, 2026 ... consummated") |
| Ticking fee accrues monthly | Paid for **6 days only** (Oct 1 to Oct 6): **$41,886,975.78** total | 8-K 0001104659-26-113913, Item 2.01 |
| ~$52B debt "in limbo" | Priced 2026-09-28 to 09-30, issued **2026-10-05**, one day before closing; $49B bridge **reduced to $0, no draw** | 8-K Items 1.01/1.02; Ex. 99.2 note |
| Trial 2027-03-02 | Never held. Both the 12-state case and the WGA case show **terminated 2026-10-01** | CourtListener (docket 73606877; docket 73614167) |

The 10-Q (filed 2026-08-04, https://www.sec.gov/Archives/edgar/data/0002041610/000204161026000054/psky-20260630.htm) is the last pre-resolution primary: it confirms the stipulation text ("will not close ... until the earlier of (1) five days after a merits determination ... or (2) June 1, 2027"), the 2026-08-04 order setting a 12-day trial 2027-03-02 to 2027-03-19, and the merger-agreement terms below. VERIFIED.

## 1. How the pause ended (litigation)

### 1a. Timeline (filed or docketed)

| Date | Event | Source | Token |
|---|---|---|---|
| 2026-04-30 | Faust et al. (consumers) file Clayton Act s.7 suit, 4:26-cv-03790-AMO | 10-Q; order of 2026-10-21 | VERIFIED |
| 2026-07-13 | 12 states file 4:26-cv-07116-AMO; TRO motion | 10-Q | VERIFIED |
| 2026-07-14 | WGA West/East file 4:26-cv-07212-AMO | 8-K 2026-09-30 | VERIFIED |
| 2026-07-20 | TRO granted | 10-Q | VERIFIED |
| 2026-07-24 | Stipulation: no close, no integration until earlier of 5 days after merits determination or 2027-06-01. Court granted same day | 10-Q | VERIFIED |
| 2026-08-04 | Order: single 12-day trial 2027-03-02 to 2027-03-19 (states + WGA) | 10-Q | VERIFIED |
| 2026-08-05 | Faust original complaint dismissed for lack of Article III and antitrust standing (leave to amend) | Order of 2026-10-21 (Dkt 102, background section) | VERIFIED |
| 2026-09-17 | FCC grants waiver of the 25% foreign-ownership benchmark so Saudi (PIF), Abu Dhabi (L'imad), Qatar (QIA) funds can hold non-voting equity; Commissioner Gomez dissents | cordcuttersnews.com 2026-09-18 (https://cordcuttersnews.com/fcc-waiver-lets-saudi-qatari-and-abu-dhabi-funds-back-paramounts-purchase-of-warner-bros-discovery/) | SECONDARY (FCC order not retrieved; the FCC link I found, DA-26-411, was a binary I could not read) |
| 2026-09-21 | Consent decree with the 12 states and WGA settlement signed; joint motion to modify the no-close order | 8-K 2026-09-30 | VERIFIED |
| 2026-09-24 | Virtual hearing; judge: "not a rubber stamp"; Sen. Booker letter asked for independent public-interest review (no competitive impact statement, no comment period); Block the Merger coalition moved to oppose; amicus briefs allowed | Variety AU 2026-09-25 (https://au.variety.com/2026/film/news/judge-paramount-state-ags-settlement-hearing-40682/); docket entry 271 (transcript of 9/24 proceedings) | SECONDARY for the narrative; hearing itself VERIFIED by docket |
| 2026-09-30 | Order entering the decree: "fair, reasonable, and good faith approach to address the competitive harms" (AP quote). Settlement conference of 10/14-15 vacated (Dkt 268) | Dkt 266; AP via mynews13.com 2026-09-30 | VERIFIED (docket text); quote SECONDARY |
| 2026-10-01 | States and WGA civil cases terminated. Faust plaintiffs file a Ninth Circuit mandamus petition (26-6423) | CourtListener | VERIFIED |
| 2026-10-02 | **Ninth Circuit denies mandamus** (Fletcher, Desai, de Alba): "Petitioners have not demonstrated a clear and indisputable right to the extraordinary remedy of mandamus"; all other motions moot | CourtListener docket 74923504 entry 11 | VERIFIED (docket text) |
| 2026-10-06 | Closing | 8-K | VERIFIED |
| 2026-10-15 | Handwritten letter from a member of the public filed in the closed states case (Dkt 273) | CourtListener | VERIFIED; no legal effect |
| **2026-10-21** | **Faust First Amended Complaint dismissed, leave to amend; amended complaint due within 21 days (about 2026-11-11), no new claims or parties without leave** | Order Dkt 102, https://storage.courtlistener.com/recap/gov.uscourts.cand.469028/gov.uscourts.cand.469028.102.0.pdf | VERIFIED (read the order) |

### 1b. The 12 states (VERIFIED, 8-K 2026-09-30)
California, Arizona, Colorado, Connecticut, Massachusetts, Minnesota, Nevada, New Jersey, New Mexico, New York, Oregon, Washington. California AG Bonta led. Bonta's stated reason for settling: prefer to resolve it "in the boardroom instead of the courtroom" (newschannel9.com 2026-09-21, SECONDARY). Variety notes the decree has no structural remedy that Bonta had earlier said was needed.

### 1c. What the states got (the decree, 5-year commitment period; VERIFIED, 8-K 2026-09-30)
- Film output: 30 films/yr (years 1-2), 32/yr (years 3-5); 20 wide releases (21 later), 4 independent films/yr; 45-day theatrical window; shortfall costs $30M per film into industry funds, and after a 6-month cure period a missed annual commitment forces divestiture of Miramax Studios.
- Basic cable: separate affiliation negotiations for the two portfolios; uncured material breach forces divestiture of BET, VH1, Comedy Central, Smithsonian, Destination America, Science.
- $300M/yr more US production than combined 2025 levels ($1.5B over 5 years); no sale or closure of the Paramount or Warner Bros. lots; honour collective bargaining agreements; $9.5M/yr training; $5M/yr independent film fund.
- Within 180 days of closing (so by about 2027-04-04): five-member News Editorial Independence Board for CBS News and CNN. Pluto TV kept free. Compliance Monitor, independent Monitoring Trustee, semiannual reports. States' fees reimbursed up to $40M.
- WGA settlement: $17.5M one-time to the Writers' Guild-Industry Health Fund within 7 days of closing; WGA legal fees up to $6.0M; CBS News Broadcast WGA headcount floor.
- Company's stated view: no material impact on synergy and leverage targets (company claim, forward-looking).

### 1d. DOJ, FCC, other suits
| Item | Finding | Token |
|---|---|---|
| DOJ | No DOJ complaint or consent decree in the filings I read. Reader C and press report DOJ cleared in June 2026 with no conditions (CNN/KRDO 2026-06-12). I did not retrieve the DOJ closing statement or HSR timing | SECONDARY / not checked at primary |
| FCC | WBD holds no broadcast licences, so no CBS-station transfer was needed for the WBD merger (INFERRED; 10-Q lists FCC licences only as Paramount's own intangibles of $2,558M). The FCC action that mattered was the foreign-ownership waiver for the Gulf funds (above) | INFERRED; waiver SECONDARY |
| Faust consumers | Open: dismissed again 2026-10-21 with leave to amend; Ninth Circuit mandamus already denied. Remaining threat is small: the court has twice found no standing | VERIFIED |
| Block the Merger coalition (Committee for the First Amendment, Free Press, Freedom of the Press Foundation, Future Film Coalition, International Documentary Association) | Opposed the decree as amici/movants (PYMNTS, citing Deadline). **No notice of appeal found** on the states docket through 2026-10-22 (the docket shows the case terminated 10/1; I could not read every entry) | SEARCH-NOT-FOUND for an appeal; a CourtListener-only check |
| Shareholder suits | The 2026-09-30 8-K risk text mentions possible stockholder litigation generically; no specific suit found | SEARCH-NOT-FOUND |
| Settlement or compromise talks (the original ask) | Moot: they succeeded 9/21. The August press said "no indications the parties are currently discussing" a settlement (CP24/CNN 2026-08-04, SECONDARY) and the 10-Q (7/23) already noted the states deferred their PI filing pending "further discussions" | VERIFIED (10-Q) |

## 2. The carry of the pause (7/24 to 10/6 = 74 days)

### 2a. Ticking fee: actual vs what the longer delay would have cost
Formula: $0.00277778 per WBD share per calendar day after 2026-09-30, cap $0.25 per 90-day period (10-Q; the cap equals 90 x the daily rate, so it does not bind below 90 days of accrual). Not payable if the agreement terminates.

| Item | Value | Basis | Token |
|---|---|---|---|
| Actual ticking paid | **$41,886,975.78** = 6 days x $0.00277778 x ~2.513B shares | 8-K Item 2.01; shares derived by me (41,886,975.78 / 0.01666668) | VERIFIED amount; share count INFERRED arithmetic |
| Per day | ~$6.98M | 2.513B x $0.00277778 | INFERRED (press: "about $7 million per day") |
| Per month (30.4 days) | ~$212M | same | INFERRED |
| Per 90 days | ~$628M | 2.513B x $0.25 | INFERRED |
| Cost had the 2027-03-02 trial gone ahead (close on 2027-03-19 as a floor) | 170 days = $0.472/share = **~$1.19B** | arithmetic | INFERRED counterfactual |
| Close at the 2027-06-01 stipulation outside date | 244 days = $0.678/share = ~$1.70B | arithmetic | INFERRED counterfactual |
| Who pays | Paramount (now Skydance Corp) pays WBD holders in cash at closing; under the subscription agreements the Trust's commitment is "plus any Ticking Consideration", so the equity syndicate funds it (8-K filed 2026-03-02) | | VERIFIED text; allocation of this $41.9M inside the $47.0B PIPE UNKNOWN |

### 2b. Debt carry and fees
| Item | Finding | Source | Token |
|---|---|---|---|
| Acquisition notes during the pause | **No interest was paid on acquisition debt during the pause.** Notes were launched 9/28, priced 9/30 and issued 10/5, one day before closing. Two features are consistent with timing the deal to the resolution: (a) the 9/28 launch followed the 9/21 settlement and the 9/30 court order the same day as pricing; (b) the first-lien indenture, section 3.10, carries a **Special Mandatory Redemption at 101.0% of issue price plus accrued interest** if the acquisition has not closed by 2027-06-11, the issuer says it will not pursue it, or the agreement terminates. I found no escrow account language in the closing 8-K or the first-lien indenture (the three "escrow" hits are lien carve-outs) | 8-K 0001104659-26-113913; Ex. 4.2 s. 3.10 (https://www.sec.gov/Archives/edgar/data/2041610/000110465926113913/tm2626659d7_ex4-2.htm) | VERIFIED |
| Bridge | $54.0B commitments (Dec 2025/Feb 2026), cut to $49.0B on 2026-04-09 when the Term A loans and $5.0B revolver were arranged, then **reduced to $0 and terminated at closing; never drawn.** 364-day tenor (so expiry would have been about 12 months after funding, not a pause-period issue) | 8-K 2026-04-09 (k0409); 8-K 2026-10-06 Item 1.01/1.02; Ex. 99.2 | VERIFIED |
| Bridge commitment-fee drag | **$384M** cash paid for bridge commitment fees, written off (pro forma adjustment 5e). This covers the whole commitment life since Dec 2025, not only the pause. It is the cleanest filed number for the cost of holding the bridge | Ex. 99.2 balance sheet and note 5e | VERIFIED (pro forma, preliminary) |
| Other pause costs | Netflix break fee $2.8B paid in Q1 2026 (cash plus $2.15B revolver draw, interest on that draw ran during the pause; the equity syndicate reimburses via the PIPE); $9M bondholder/third-party costs in pro forma. A buy-side holder (Impax) told Bloomberg the delay "cost the company hundreds of millions of dollars" (quote, SECONDARY, unsized) | 10-Q; Ex. 99.2; briefs.co 2026-10-01 | VERIFIED / SECONDARY |
| Run-rate interest after closing (the real carry now) | Pro forma net interest: $3,090M for six months to 6/30/26 (~$515M per month); $6,435M full-year 2025 basis (~$536M per month); of which interest on the new financing alone is $4,199M per year (~$350M per month) | Ex. 99.2 | VERIFIED (pro forma) |

### 2c. Financing as filed (reconciles reader C)
Issued 2026-10-05: $30.0B first-lien notes (coupons 6.300% to 8.900%, 2028 to 2066), $11.4B second-lien USD (8.250% 2031 $6.0B; 8.875% 2034 $4.0B; 9.125% 2036 $1.4B) plus EUR 885M 7.000% 2031; Term B $8.5B + EUR 850M; Term A $2.5B + $2.5B; PIPE 3,917,657,246 Class B at $12.00 (= $47.01B) on 2026-10-06; WBD exchange-offer notes 99.15% tendered into $11.98B + EUR 547M second-lien notes on 2026-10-09 (8-K filed 2026-10-13). VERIFIED.

## 3. Termination economics (now moot; recorded for the counterfactual)

| Term | Value | Source | Token |
|---|---|---|---|
| Regulatory Termination Fee, Paramount to WBD | **$7.0B** if the deal dies on antitrust/regulatory failure or a court order on antitrust grounds | 10-Q | VERIFIED |
| Who funds it | The Ellison Parties via PIPE shares at **$16.02/share** (about 437M shares for $7.0B); same mechanism for the $2.8B Netflix fee (about 175M shares). Note the actual closing PIPE price was **$12.00**, so the $16.02 reference no longer matches the market | 10-Q; 8-K 2026-10-06 Item 3.02 | VERIFIED |
| WBD fee to Paramount | $3.0B in certain cases, including WBD taking a competing bid; plus reimbursement of the Netflix fee and any amended-notes amount for certain WBD breaches | 10-Q; 8-K filed 2026-03-02 | VERIFIED |
| Termination date | 2027-03-04, one automatic extension to 2027-06-04 | 10-Q | VERIFIED |
| Ticking fee if terminated | Not payable | 10-Q | VERIFIED |
| Notes if terminated | Special Mandatory Redemption at 101% (above): the bond buyers were protected, the equity was not | Ex. 4.2 | VERIFIED |
| WBD separation (Discovery Global spin) | The Netflix-era plan split WBD; under the Paramount deal WBD is acquired whole. CNN stays in the combined company (a stated settlement point; stockanalysis.com 2026-09-21). One search found nothing on any formal cancellation; moot after closing | stockanalysis.com | SECONDARY / SEARCH-NOT-FOUND |
| WBD legacy debt | 3/31/26: $17.7B senior notes + $15.0B bridge; bridge refinanced 6/4/26 with $13.0B + EUR 1.7B 7-year term loans, repaid at closing. $2.4B tender offers; exchange offers per 2c | 10-Q | VERIFIED |
| How WBD bonds traded against the deal during the pause | Not retrieved. Fitch (at closing) rates WBD legacy senior unsecured B+/RR6 (reader C, TheWrap, SECONDARY) | | UNKNOWN |

## 4. Ellison guarantee and Oracle collateral

### 4a. Does the guarantee survive closing?
| Question | Answer | Token |
|---|---|---|
| Filed terms | Trust and Larry Ellison personally, jointly and severally, guaranteed to WBD: the Netflix fee, the amended-notes payment, **$45.72B of the Merger Consideration** (+ contingent equity), damages for breach or fraud, the **$7.0B Regulatory Termination Fee**, certain costs. Covenants: reasonable best efforts on approvals, litigate on the merits including appeal, no impairing actions; **Oracle and the Ellison Institute are excluded from "controlled affiliates"**. No term, step-down or Oracle pledge appears in the 8-K description | 8-K filed 2026-03-02 | VERIFIED |
| Status after closing | The guarantee runs **to WBD for the payment of merger consideration and termination-related fees**. Consideration was paid on 2026-10-06 ($77,990M to WBD holders per reader C). So the guaranteed payment obligations appear **discharged**; I found no post-closing continuing obligation, and no 8-K after 10/6 mentions it | INFERRED; guarantee exhibit (Ex. 10.1 of the 3/2 8-K) text not read |
| "$40.4B" figure | December 2025 version of the tender-offer guarantee (TheWrap/CNN/IBC, 2025-12-22/23, SECONDARY). The filed February 2026 guarantee is $45.72B of consideration. Use the filed number | | VERIFIED / SECONDARY |
| Deleveraging support cited by rating agencies / press | Puck (2026-10, paywalled, 403) reportedly says lenders and markets expect Larry Ellison to cover deleveraging shortfalls or add equity before 2029 to reach 3x, with an insider saying no new equity is needed. I could not read it. Nothing in the filings I read creates an Ellison deleveraging covenant; S&P's action (BB, 2026-09-24) is reported with no detail on Ellison support (IBTimes) | | UNKNOWN / SECONDARY. This is a gap: the "Ellison deleveraging pledge S&P cites" in PROME's task was **not found** at a primary |

### 4b. Pledge terms and filings
| Item | Finding | Token |
|---|---|---|
| Pledge terms (margin call, LTV) | **SEARCH-NOT-FOUND** in any deal-linked filing: not in the 8-K of 2026-03-02, 2026-09-30, 2026-10-06, the 10-Q, or the first-lien indenture. The 10-06 lock-up expressly permits PIPE investors to pledge new shares (reader C) | SEARCH-NOT-FOUND (owner-declared path = the deal 8-Ks) |
| Form 4 by Larry Ellison since 7/24 | Only one, filed 2026-10-19 (acc. 0001341439-26-000103): a **restricted stock unit grant** of 223,099 Oracle RSUs on 2026-10-15, vesting 40/30/20/5/5% from 2027. Not a pledge change | VERIFIED (read the XML) |
| Section 16 / 13D by the Trust on Skydance Class B | **None found** through 2026-10-22 in Skydance's EDGAR filing list (Forms 3/4 filed 10/7, 10/8, 10/19, 10/20 are officers/directors) or via EDGAR full-text search for filings by Larry Ellison. A 10% holder of Class B (about 500M shares of ~5.0B INFERRED) would owe a Form 3 within 10 days and a 13D. Either the Trust's retained Class B stake is under those thresholds, or the filings are late or under another filer ID. This bears directly on how much equity the Ellison family kept | SEARCH-NOT-FOUND; interpretation INFERRED |
| RedBird | Cardinale Form 4 filed 2026-10-08: 175,000,000 + 158,333,333 Class B acquired at $12.00 on 2026-10-06 = **$4.0B** through RedBird entities, on top of earlier RedBird holdings | VERIFIED (read the XML) |
| Gulf funds | Reported plans: PIF $10B, L'imad $7B, QIA $7B = $24B of the $47B (cordcuttersnews, 2026-09-18; the FCC petition, as reported, put Middle East investors at 38.5% of equity: PIF 15.1%, UAE 12.8%, QIA 10.6%, webpronews/Schiff letter) | SECONDARY; the 8-Ks name the parties but give no per-party dollar split |

### 4c. Oracle price path (context for collateral; reader D covers the proxy)
Yahoo daily closes via the chart endpoint, fetched 2026-10-22:

| Date | ORCL close | Note |
|---|---|---|
| 2026-06-01 | $248.15 | 52-week high in the 6-month window |
| 2026-06-03 | $230.33 | |
| 2026-07-23 | $120.04 | |
| **2026-07-24** | **$114.99** | window low (day the pause was agreed) |
| 2026-08-12 | ~$153 | rebound high of the period |
| 2026-09-30 | $137.30 | |
| 2026-10-06 | $144.77 | closing day |
| 2026-10-14 | $130.55 | |
| 2026-10-22 | **$125.54** (-2.78% on the day) | fetch.py |

ORCL is down 49% from 6/1 and up 9% from the 7/24 low. If the Trust holds about 1.16B Oracle shares (Paramount statement of Dec 2025, SECONDARY, reader C), that is about $146B at $125.54 vs $288B at the 6/1 high (INFERRED arithmetic). The slide happened mostly before the pause; the pause window itself (7/24 to 10/6) saw Oracle rise from its low. I have no filed LTV, so coverage ratios cannot be computed (UNKNOWN). Pledged-share counts are reader D's lane (proxy).

## 5. Market read

### 5a. Skydance equity
| Date | SKYD/PSKY close | Event |
|---|---|---|
| 2026-07-23 | $8.49 | day before the pause |
| 2026-07-24 | $8.21 | record low then (Bloomberg Law); pause announced |
| 2026-07-31 | $7.96 | |
| 2026-09-01 | $10.55 | |
| 2026-09-21 | $9.91 | decree day; closed down about 3% after a morning gain (stockanalysis, SECONDARY) |
| 2026-09-30 | $10.33 | |
| 2026-10-01 | $9.34 | bond sale selloff, intraday -7.5% (briefs.co) |
| 2026-10-06 | $9.53 | closing day |
| 2026-10-13 | $9.27 | last cum-warrant close |
| 2026-10-14 | $7.06 | ex-warrant (-23.84%); NYSE adjusted reference price from $9.27 to $9.07 (IBTimes) |
| 2026-10-19 | $6.80 | window low |
| **2026-10-22** | **$7.79** (-1.02%) | fetch.py |

- The 10/14 "plunge" is mostly mechanical. About 471M warrants (strike $12.00, 10-year) were distributed to public holders 10/13; the warrant closed at **$2.20** on 10/13 (rallies.ai, SECONDARY), and $9.27 - $2.20 = $7.07, which matches the $7.06 ex-date close (my arithmetic, INFERRED). A holder who kept the warrant lost almost nothing that day. Director Cardinale bought 4.9M warrants at **$2.80** on 2026-10-16 (Form 4, VERIFIED).
- Equity vs the PIPE: $7.79 is **35.1% below $12.00**; the PIPE group's mark is -$16.5B on $47.0B (arithmetic). On closing day ($9.53) it was already -20.6%. PIPE investors bought after the court cleared the deal and were underwater from day one; the warrant dividend went to existing public holders, not to Ellison, RedBird or (INFERRED) the PIPE assignees who did not hold shares on the 10/5 record date.
- Price check on the 7/24 level: the Bloomberg Law figure ($8.21) matches the Yahoo series, so the series is trustworthy for this stock.

### 5b. Bonds and CDS (the user-requested "did public markets balk after buying")
| Metric | Level | Date | Source | Token |
|---|---|---|---|---|
| 8-year junk-rated note (priced at par) | ~95 | 2026-10-01 | Bloomberg via briefs.co | SECONDARY |
| 10-year $5.25B investment-grade note | quoted ~+278 bp vs Treasuries; issued at +262.5 | 2026-10-01 (Trace) | briefs.co | SECONDARY |
| IG book | ~$80B final vs $109B peak orders; long-end demand down by more than half; Bloomberg: >$200M unrealized losses on IG paper | 9/28 to 10/1 | briefs.co | SECONDARY |
| New-issue IG vs JPM IG index | -27 bp over 10 days to 10/8, weakest since April 2020 (ex-Skydance +4 bp) | 2026-10-08 | IBTimes | SECONDARY |
| 9.125% 2L due 2036 | **~91** (par at issue 9/30) | 2026-10-13 | Debtwire via IBTimes (https://www.ibtimes.co.uk/skydance-shares-fall-merger-debt-credit-risks-1825942) | SECONDARY |
| 5Y CDS (Debtwire label "Paramount Global") | **577 bp** from 268 bp on 9/17 | 2026-10-13 | same | SECONDARY; the single-name reference after the exchange is UNKNOWN |
| 5Y CDS, second print | 576 bp "record", ~39.5% implied default probability (LSEG) | 2026-10-14 | rallies.ai headline; page could not be read | UNVERIFIED |
| Another summary | bonds down about 3 points since 10/2; CDS at a 17-year high | ~10/14 | search digest of rallies.ai | UNVERIFIED |
| First-lien trading level, latest of any tranche after 10/15 | not found | | | SEARCH-NOT-FOUND |
| Ratings | Fitch BB from BB+ (issuer; 1L BBB-); S&P BB from BB+ on 2026-09-24; Moody's issuer not found, new notes speculative grade per press | | IBTimes; reader C | SECONDARY |

Reading: the market priced the debt as a leveraged, junk-issuer credit (Debtwire net debt $84.3B at close; its base-case savings leave leverage above the 3x target even in the optimistic case at about 3.1x in 2029, IBTimes) rather than as a deal-completion risk. The CDS widening (268 to 577 bp in 26 days) began after the decree and straddles the closing, so it measures the cost of the leverage, not the lawsuit. No later quotes than 10/15 were reached.

### 5c. WBD and the merger-arb spread during the pause (the original ask)
| Date | WBD price | Spread to $31.00 | Source | Token |
|---|---|---|---|---|
| 2026-07-24 | not verified (one page cited $25.77, unsourced) | n/a | search result | UNVERIFIED |
| 2026-08-18 | **$28.48** (+1.97% that day) | **$2.52 = 8.8% gross**; shareholders already approved; litigation named the key driver | parameter.io 2026-08-19 (https://parameter.io/warner-bros-discovery-wbd-stock-rises-2-as-paramount-merger-spread-holds-at-8-8/) | SECONDARY |
| 2026-09-21 | +10% to +11% on the settlement; ~$31 reported by 9/22 | near zero | stockanalysis; TIKR | SECONDARY |
| **2026-10-05** | **$30.95** | $0.067 below $31.01666668 = **0.22%** | Yahoo chart meta (the last print before the merged shares were delisted) | VERIFIED as fetched |

Implied probability of closing on 2026-08-18, from the 8.8% spread (my arithmetic, INFERRED; no filed break price exists). p = (price - break) / (31.00 - break), ignoring ticking and time value:

| Assumed break price | Implied p |
|---|---|
| $18 (the 52-week low in Yahoo meta, $17.995) | 81% |
| $20 | 77% |
| $22 | 72% |

Cross-check: an 8.8% gross spread to a March 2027 trial date is about 15% annualized over about 0.58 year, which the market charged mainly as a litigation premium. The ticking fee would have added about $0.47 per share by 3/19 (1.7% of the price), so the true unlevered spread was a little wider than quoted. The spread then collapsed on the settlement, from 8.8% to about 0.2% at closing. The market's August probability estimate of roughly 70 to 80% was too low for the way it resolved, but the resolution came from a negotiated decree, not a ruling.

## 6. Load-bearing uncertainties and what I could not reach
1. **How much equity the Ellison family kept.** Press says PIF/L'imad/QIA were slated for about $24B of the $47.0B PIPE, RedBird took $4.0B (verified), LionTree is also an assignee, and there is no Form 3, Form 4 or 13D by Larry Ellison or the Trust for Skydance through 10/22. The Trust's real exposure, and whether anything of its guarantee still binds, rests on that number. UNKNOWN.
2. **Guarantee discharge.** I read the 8-K summary, not the guarantee exhibit; "discharged at closing" is INFERRED from its payment-only structure.
3. **Pledge terms for Oracle collateral.** No deal-linked filing mentions a pledge, margin trigger or LTV. SEARCH-NOT-FOUND. The "Ellison deleveraging pledge" in the task prompt was not located at any primary.
4. Not reached: the FCC order itself (DA number not confirmed), DOJ closing statement, the Fitch/S&P/Moody's releases (paywalled), Bloomberg/Deadline/CNBC pages (403/paywall), any CDS screen after 10/15, first-lien bond prices after 10/1, WBD bond trading during the pause, Puck's Ellison piece (403), Form 4/13D beyond what EDGAR lists, a Ninth Circuit or notice-of-appeal check beyond CourtListener, and whether the Block the Merger coalition filed anything on 10/1.

## SUMMARY FOR PROME
1. **The delayed-merger premise is void.** The July 24 stipulation (no close until 5 days after a merits ruling or 2027-06-01) was dissolved on 2026-09-30 when Judge Martínez-Olguín entered the consent decree signed 9/21 with the 12 states (CA, AZ, CO, CT, MA, MN, NV, NJ, NM, NY, OR, WA); the WGA suit settled 9/21; both cases terminated 10/1; deal closed 10/6 (8-K 0001104659-26-113913). No trial, no ruling, no DOJ action. The decree is behavioral (30-32 films a year, Miramax and basic-cable divestiture triggers, news editorial board by about 4/4/2027, $1.5B extra US production, $40M states' fees, monitor).
2. **Cost of the pause, filed:** ticking fee was **$41.9M** (6 days, ~$6.98M a day, ~$212M a month, ~2.51B shares); bridge commitment fees **$384M** cumulative (never drawn, cut to $0); acquisition notes issued 10/5, one day pre-close, so **zero** pause-period interest. Who paid: Paramount/Skydance, funded by the equity syndicate. Counterfactual: a March 19, 2027 close would have cost ~$1.19B in ticking fees; June 1, 2027 about $1.70B.
3. **Failure scenario in dollars (now moot):** $7.0B Regulatory Termination Fee to WBD (Ellison-guaranteed, funded by Ellison PIPE shares at $16.02); $2.8B Netflix fee already sunk; $3.0B reverse fee only if WBD walks; notes would have been redeemed at 101 under Special Mandatory Redemption.
4. **What is left:** Faust consumer suit dismissed again 10/21 (amended complaint due about 11/11/2026; Ninth Circuit mandamus denied 10/2). No appeal of the decree found. The live exposure is the leveraged balance sheet: pro forma net interest ~$515M-$536M a month; Debtwire net debt $84.3B.
5. **Merger-arb read:** WBD $28.48 on 8/18 (8.8% gross spread; implied closing odds ~72-81% depending on an assumed $18-$22 break price, INFERRED); $30.95 on 10/5 (0.22% below the final $31.0167).
6. **Post-close market:** SKYD $7.79 on 10/22, **35% below the $12.00 PIPE price** (-$16.5B mark on $47.0B); most of the 10/14 drop is the warrant dividend ($9.27 less $2.20 warrant = $7.07). 5Y CDS 577 bp on 10/13 vs 268 on 9/17; 9.125% 2036 second-lien ~91 vs par; 8-year note ~95 the day after pricing. All SECONDARY. Public buyers did balk after buying, and the move is about leverage, not litigation.
7. **Oracle:** ORCL $125.54 on 10/22, -49% from $248.15 on 6/1, +9% from the $114.99 low on 7/24. Larry Ellison's only Skydance-period Oracle filing is an RSU grant (Form 4, 10/19). No deal-linked filing shows pledge terms, LTV or a pledge change.
8. **Load-bearing uncertainties:** (a) the Ellison family's retained Skydance equity: no Form 3/4/13D from Larry Ellison or the Trust through 10/22; (b) whether the $45.72B guarantee has any post-closing life (INFERRED discharged; exhibit not read).
9. **Could not reach:** rating releases, post-10/15 bond and CDS levels, first-lien trading prices, the FCC order text, DOJ's closing statement, Puck/Bloomberg paywalled pieces, WBD bond prices during the pause. The "S&P-cited Ellison deleveraging pledge" was not found at a primary.
