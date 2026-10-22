# GENIUS Act stablecoin rewards and regional-bank deposit flight
**Date:** 2026-10-22 | **Mode:** Thesis | **Confidence:** Rule text High · Who may pay rewards (exchanges/affiliates) Medium (unsettled across regulators) · Outflow size Low · Bank deposit-mix data High (mixed vintages) / link from deposit mix to stablecoin exposure Low · Reserve location Medium · AI-agent link Low · Dashboard series High | **Request:** REQ-DEWEY-20261022-002 (WALTER) | **Recipients:** REGINALD, LIQUID (action); GIBBS, BOND, CARL, RED, PROME, TERRY (info)

## Key Finding
From 2027-01-18 a payment-stablecoin issuer may not pay holders "any form of interest or yield ... solely in connection with the holding, use, or retention" of the coin. The OCC's final rule (2026-10-21) keeps that ban word for word and adds an anti-evasion clause. What it dropped is only the proposal's rebuttable presumption against issuer-to-affiliate/third-party yield chains. The rule binds **issuers only** and creates **no OCC approval process for exchange rewards programs**, so exchange and affiliate rewards are neither blessed nor presumed illegal: they will be judged case by case, with no safe harbor. The FDIC, NCUA and Fed proposals, none of them final, still contain the presumption, so the rewards outcome is not settled across regulators. The largest published deposit figures ($6–6.6T) are **at-risk pools that assume interest-bearing stablecoins**, not forecasts, and every empirical study predates GENIUS taking effect. Observed data since signing show commercial-bank deposits +$1,505.6B (+8.2%) against stablecoin supply +$46.1B, with supply flat year on year (−0.7%). No post-GENIUS deposit data exist yet.

## Premise check
**The relayed claim that stablecoin rewards restrictions were "DROPPED" is wrong as to the legal text.** WALTER logged the correction on 2026-10-22 as SIG-W-20261022-014 (correcting SIG-W-20261021-025), from DEWEY's intake notes and REGINALD's own read of the rule. This report is the durable source for the "DEWEY notes" cited there.

| Claim as relayed | What the OCC primary text says | Verdict |
|---|---|---|
| Rewards/yield restrictions "DROPPED" | Final 12 CFR 15.10(c)(4) keeps the statutory yield ban verbatim: an issuer must not "Pay a payment stablecoin holder any form of interest or yield (whether in cash, tokens, or other consideration) solely in connection with the holding, use, or retention of such payment stablecoin." 15.10(c)(6) bars any activity the OCC "determines is an evasion of the requirements of section 4" [PRIMARY: OCC final rule PDF pp. 656–657, 2026-10-21] | **Wrong.** The ban stands and takes effect 2027-01-18 |
| (implied) Affiliate/third-party restrictions removed | The proposal's rebuttable presumption ((c)(4)(i)–(iii)) was deleted: "the OCC does not believe that it is appropriate to impose a rebuttable presumption with respect to the yield prohibition at this time" (pp. 113–114). In the same document: "the OCC retains its authority to address evasion of section 4 of the Act (12 U.S.C. 5903), including the yield prohibition" (p. 101) [PRIMARY] | **Partly right.** The burden-shifting device is gone. The anti-evasion power remains |
| (implied) Existing exchange programs are grandfathered | "The OCC declines to presume that rewards programs that predated the GENIUS Act comply with the GENIUS Act ... Congress could have provided a safe harbor for such programs but did not do so" (pp. 104–106) [PRIMARY] | **Wrong.** No grandfathering and no safe harbor |
| (secondary headlines) Exchanges "need OCC sign-off" / the rule "requires case-by-case approval" | The text contains no approval or pre-clearance process for third-party programs. The OCC will "monitor arrangements with permitted payment stablecoin issuers ... as part of its review of issuers' applications and ongoing supervision" (p. 114) [PRIMARY] | **Overstated** by CoinDesk, Roll Call and cryptotimes [NEWS] |
| (implied) Settled across the sector | FDIC (91 FR 18538–39), NCUA (91 FR 28969–70) and Fed (91 FR 61591; comments close 2026-11-30) proposals all still contain the presumption. None is final [PRIMARY: Federal Register] | **Not settled** |

The original "DROPPED" post (attributed to Eleanor Terrett) was not located: X is not fetchable. The verdict above rests on the OCC text, not on the post. Some secondaries also overstate in the other direction: Coinpedia's headline "OCC Final Rule Drops Stablecoin Yield Curbs" [NEWS] is as wrong as the claim that exchanges need OCC sign-off.

## Evidence

### What the rule permits and what it leaves open
Three channels exist for paying a stablecoin holder something that looks like a deposit rate.

**(a) The issuer pays directly.** Barred from 2027-01-18 under both the statute and the OCC rule. The OCC also closed off relabeling: "Interest does not stop being interest merely because it is given a different name" [PRIMARY: OCC final rule p. 106].

**(b) An exchange, wallet or affiliate pays.** The statute names only the issuer as payor. It also lacks the "either directly or indirectly" wording used in the neighboring rehypothecation clause (§4(a)(2)), and that textual gap is the industry's core argument [PRIMARY: Pub. L. 119-27]. The OCC answered with agency and evasion theory rather than a per se rule. An agent paying "on the issuer's behalf" is covered, and "it would clearly evade the statutory prohibition on yield for an issuer to merely pay another entity to make an interest or yield payment that the issuer could not make directly" (p. 102). Beyond that, "the OCC will apply the language of the statute to the facts and circumstances of any particular arrangement" (pp. 103–104).

**(c) Payments "not solely" for holding.** The OCC reads "solely" by its plain terms, so "payments made for other purposes are not barred". It keeps a look-through for payments made "only nominally for another purpose in an attempt to evade the statute" (p. 110). Payments for bona fide services "generally would not be prohibited" (pp. 104–106). This is a concrete opening for activity-linked rewards.

The Senate market-structure text described in secondaries would ban yield on idle balances while allowing activity-based rewards, and would add a community-bank "circuit-breaker". That bill is stalled: cloture failed 49–50 on 2026-09-15 [NEWS: CNBC; INSTITUTIONAL: DLA Piper, Latham & Watkins]. The OCC: "Unless and until such legislation passes, the OCC must implement the GENIUS Act's yield prohibition, as enacted" (pp. 97–98).

There is economic room for a rewards program that competes with bank rates. In Q2 2026 Circle earned an average 3.57% on the Circle Reserve Fund and 2.98% on reserve cash [PRIMARY: Circle 10-Q, period ended 2026-06-30]. For comparison, the 22 regionals in Table 3 paid 1.18–2.81% on total deposits in Q2–Q3 2026, and Apollo cites a 0.1% average checking rate [INSTITUTIONAL: Apollo, 2026-09-27]. *DEWEY arithmetic, not a sourced claim:* passing even part of a ~3.5% reserve yield to holders would beat noninterest-bearing and average checking balances. Whether such a pass-through survives the (c)(6) anti-evasion test is exactly the open question.

#### Table 1 — Rule text: rewards, reserves, effective dates

| # | Provision | Exact text / content | Status, date | Source |
|---|---|---|---|---|
| 1a | Statutory yield ban, GENIUS §4(a)(11), 12 U.S.C. 5903(a)(11) | "No permitted payment stablecoin issuer or foreign payment stablecoin issuer shall pay the holder of any payment stablecoin any form of interest or yield (whether in cash, tokens, or other consideration) solely in connection with the holding, use, or retention of such payment stablecoin." | Enacted 2025-07-18; effective 2027-01-18 | [PRIMARY] Pub. L. 119-27 |
| 1b | OCC final 12 CFR 15.10(c)(4) | "Pay a payment stablecoin holder any form of interest or yield (whether in cash, tokens, or other consideration) solely in connection with the holding, use, or retention of such payment stablecoin." "Payment stablecoin holder" is newly defined as "the beneficial owner of a payment stablecoin" (§15.2) | Final 2026-10-21; effective 2027-01-18 | [PRIMARY] OCC final rule pp. 650, 656–657 |
| 1c | Foreign issuers, §15.31(c) | Same ban for foreign issuers registered with the OCC | Final, same dates | [PRIMARY] p. 700 |
| 1d | Anti-evasion, §15.10(c)(6) | "Engage in any activity that the OCC determines is an evasion of the requirements of section 4 of the GENIUS Act (12 U.S.C. 5903) or this part." | Adopted as proposed | [PRIMARY] p. 657 |
| 1e | Presumption dropped | "the OCC does not believe that it is appropriate to impose a rebuttable presumption with respect to the yield prohibition at this time." Rationale: it "could have been both overinclusive and underinclusive" | Deleted from final | [PRIMARY] pp. 113–114 |
| 1f | Anti-evasion retained | "the OCC retains its authority to address evasion of section 4 of the Act (12 U.S.C. 5903), including the yield prohibition" | — | [PRIMARY] p. 101 |
| 1g | Legacy rewards programs | "The OCC declines to presume that rewards programs that predated the GENIUS Act comply with the GENIUS Act." "Congress could have provided a safe harbor for such programs but did not do so." | No grandfathering | [PRIMARY] pp. 104–106 |
| 1h | Other safe harbors refused | No safe harbor for de minimis payments, white-label partners, securities or DeFi, and no general safe harbor | — | [PRIMARY] pp. 104–106 |
| 1i | Labels vs substance | "Interest does not stop being interest merely because it is given a different name." "Interest", "yield", "pay", "holding", "use" and "retention" are deliberately left undefined | — | [PRIMARY] pp. 106–110 |
| 1j | "Solely" | "payments made for other purposes are not barred by the GENIUS Act". The OCC will look through payments made "only nominally for another purpose" | Industry-favorable reading with a look-through | [PRIMARY] p. 110 |
| 1k | Indirect/agent payments | An agent paying "on the issuer's behalf ... would be within the scope"; intermediary cases "may present closer questions" | Case by case | [PRIMARY] pp. 102–103 |
| 1l | Oversight mechanism | OCC "will initially monitor arrangements ... as part of its review of issuers' applications and ongoing supervision." **No approval process for exchange programs** | — | [PRIMARY] p. 114 |
| 1m | Deposits carved out | "the prohibition does not extend to paying interest on deposits, including deposits in tokenized form" | — | [PRIMARY] p. 98 |
| 1n | Pending legislation | "Unless and until such legislation passes, the OCC must implement the GENIUS Act's yield prohibition, as enacted." | CLARITY (H.R. 3633) stalled; Senate cloture failed 49–50 on 2026-09-15 | [PRIMARY] pp. 97–98; [NEWS] CNBC 2026-09-15 |
| 1o | Other regulators | FDIC (91 FR 18534), NCUA (91 FR 28956) and Fed (91 FR 61580) proposals **retain the affiliate/related-third-party presumption** | All proposed; Fed comments close 2026-11-30 | [PRIMARY] Federal Register API, queried 2026-10-22 |
| 1p | Reserve assets, statute §4(a)(1)(A) / final §15.11(b) | 1:1 reserves in: coins and currency or Fed balances; demand deposits at insured depository institutions; T-bills/notes/bonds of ≤93 days remaining; overnight repo and reverse repo on short Treasuries; government MMFs investing in those assets; other approved federal assets; tokenized forms | Final | [PRIMARY] Pub. L. 119-27; OCC pp. 657–662 |
| 1q | Liquidity floor and concentration, §15.11(c)(2) | "Maintain at least 5 percent of its reserve assets as demand deposits ... or money standing to the credit of an account with a Federal Reserve Bank"; cap any one counterparty at "no more than 40 percent of its reserve assets". U.S. government exposures, appropriate custodians and centrally cleared repo are excluded from the cap | Final | [PRIMARY] OCC final rule |
| 1r | Effective date, §20 | Earlier of 18 months after enactment (**2027-01-18**) or 120 days after final rules (2027-02-18). The first prong governs | 2027-01-18 | [PRIMARY] Pub. L. 119-27; OCC p. 1 |
| 1s | Offer ban for unpermitted coins, §3(b)(1) | Digital asset service providers may not offer non-permitted payment stablecoins to U.S. persons beginning 3 years after enactment | 2028-07-18 | [PRIMARY] Pub. L. 119-27 |
| 1t | State option, §4(c)(1) | State-qualified issuers with ≤$10B outstanding may use a "substantially similar" state regime. Treasury's principles rule is still proposed (91 FR 16844) | Open | [PRIMARY] |

Reactions follow each side's interest [INSTITUTIONAL]. ABA (Nichols, 2026-10-21): the rule "will preserve the status quo for crypto platforms". BPI (Paridon): omitting the presumption "replaces clarity with ambiguity". ICBA restated its "$850 billion" lending-decline advocacy estimate. Blockchain Association (Fraser): "We are especially grateful that the OCC listened to the industry" [NEWS: Roll Call 2026-10-22]. The bank groups' complaint is that issuers "can provide economically equivalent yield while technically avoiding the statutory prohibition" [INSTITUTIONAL: ABA Banking Journal paraphrase]. That complaint concedes the ban stands.

### How large is the plausible migration?
The published range runs from about $0 to $6.6T, and three assumptions explain nearly all of the spread. The first is whether yield reaches holders. The second is how much of issuer reserves recycle back into bank deposits. The third is whether the figure is a gross at-risk pool or a net flow. **Caveat (must survive):** TBAC's ~$6.6T and Moynihan's "as much as $6T" are at-risk pools that assume interest-bearing stablecoins, not forecasts. TBAC's own footnote 4 calls interest-bearing stablecoins "a hypothetical design feature that is not currently contemplated by the GENIUS Act" [PRIMARY: TBAC deck, 2025-04-30]. **Caveat (must survive):** every empirical study listed covers data before GENIUS took effect (most end mid-2025). There is no post-GENIUS deposit data.

#### Table 2 — Outflow estimates (groups kept separate; never averaged)

**2A. Official and official-advisory**

| Source | Date | Figure | What kind of number | Key assumptions | Source's interest / tag |
|---|---|---|---|---|---|
| TBAC "Digital Money" (Q2-2025 refunding) | 2025-04-30 | ~$6.6T "at risk" ($5.7T demand deposits + $0.9T non-demand transactional), out of $17.8T total deposits at 4Q24 | **Pool, not a forecast** | Rotation tied to *interest-bearing* stablecoins (fn. 4: "not currently contemplated by the GENIUS Act"); fn. 3 assumes "limited movement in deposit rates". Market takeaway "~$2tn by 2030" | Treasury advisory committee of dealer and bank members [PRIMARY] |
| Fed Board FEDS Note (J. Wang) | 2025-12-17 | Lending, not deposits: each $100B of non-recycled drain → $60–126B less lending. Scenarios: low $65–141B; moderate $190–408B; high, with issuer master accounts, $600B–$1.26T | Scenario lending effect | Net drain = (1 − share of reserves held at banks) × stablecoin growth, less a foreign offset; reserve deposit share: Circle ~13%, Tether ~0 | Fed staff, "not official policy" [PRIMARY/ACADEMIC] |
| White House CEA | 2026-04 | A yield **ban** adds only +$2.1B of lending (+0.02%); worst case +$531B (4.4% of 2025Q4 loans) | General-equilibrium model | Ample reserves; T-bill reserves recycle to dealers' deposits; assumes community-bank deposit share constant | Administration opposes the ban [PRIMARY]; Nigrinis rebuts its "favorable assumptions" [INSTITUTIONAL] |
| Gov. Miran speech | 2025-11-07 | No outflow figure; staff-compiled private forecasts put stablecoins at $1–3T by end of decade; "little prospect of funds broadly fleeing the domestic banking system" | Opinion plus market range | No yield, no insurance → mostly foreign demand | FOMC member [PRIMARY] |
| KC Fed (Jacewitz) | 2025-08 | $1 deposit → stablecoin cuts lending ~50¢; −$325B lending if the market reaches $900B | Scenario | Current issuer asset mix | Regional Fed [UNVERIFIED: secondary only] |

**2B. Bank industry and bank-aligned (high end; interest: close the rewards channel)**

| Source | Date | Figure | What kind of number | Key assumptions | Source's interest / tag |
|---|---|---|---|---|---|
| Brian Moynihan (BofA), Q4-25 call | 2026-01-14 | "As much as $6T", 30–35% of deposits | **Pool**, conditional on stablecoins paying interest; attributed to "Treasury studies" (likely TBAC) | Interest-bearing | Large-bank CEO [NEWS: The Block] |
| ICBA | 2025-12-15 | −$1.3T community-bank deposits → −$850B community-bank lending | Advocacy projection "by end of decade" | Intermediaries keep paying yield; underlying study unnamed | Community-bank lobby [INSTITUTIONAL] |
| Nigrinis, promoted by Consumer Bankers Association | 2025-10-16 | No-yield case: ~6% deposit drop, ~$250B less lending. Yield at fed funds rate: ≥25% deposit drop, ~$1.5T less lending | Scenario | CEA says it imports a CBDC substitution rate | Bank trade group [INSTITUTIONAL] |
| ABA / state bankers' op-eds | 2025–26 | Repeat "Treasury: up to $6.6T at risk" | Citation of the TBAC pool as a Treasury estimate | Drops the TBAC conditionality | Lobby [NEWS] |

**2C. Sell-side and ratings (sell-side figures were not read in primary form)**

| Source | Date | Figure | Kind | Assumptions | Tag |
|---|---|---|---|---|---|
| Standard Chartered (Kendrick) | 2026-01-27 | ~$500B out of US/developed-market deposits by end-2028; ~$1T out of EM deposits | Forecast | $2T market by 2028; little re-depositing | Crypto-bullish sell-side [NEWS] |
| Citi GPS | 2025 (rev. Oct 2025) | Market $1.9T base / $4T bull / $0.9T bear by 2030 | Market size | — | [NEWS]; a $182–908B deposit range is [UNVERIFIED] |
| JPMorgan research | 2025 | Market only $500–600B by 2028 | Market size | Faster velocity means smaller balances | [NEWS] |
| S&P Global Ratings | ~2026-06 | No dollar figure; threat "limited" but "conditional"; not factored into bank ratings | Qualitative | Demand mostly ex-US | [NEWS: secondary] |
| Moody's / Fitch | 2026 | No outflow figure found | — | — | [UNVERIFIED] / gap |

**2D. Crypto industry (low end; interest: preserve rewards)**

| Source | Date | Figure | Kind | Assumptions | Tag |
|---|---|---|---|---|---|
| Charles River Associates, **commissioned by Coinbase** | 2025-07 | No statistically significant effect of USDC growth on community-bank deposits (2019–2025). Extreme 1:1 case = 6.8% of community-bank deposits; "plausible" <1% | Empirical plus scenario | Full PDF not retrieved | Sponsored [INSTITUTIONAL] |
| Coinbase (Shirzad) | 2025–26 | USDC and deposits "growing together" | Assertion | Cites CRA and CEA | [NEWS] |

**2E. Observed since GENIUS signing (DEWEY pulls, 2026-10-22)**

| Measure | Basis | Then | Latest | Change |
|---|---|---|---|---|
| Deposits, all commercial banks | FRED DPSACBW027SBOG, SA, weekly | $18,265.9B (wk 2025-07-16) | $19,771.5B (wk 2026-10-07) | **+$1,505.6B (+8.2%)** |
| Deposits, large domestically chartered | FRED DPSLCBW027SBOG, SA | $11,458.4B (wk 2025-07-16); $11,585.2B (wk 2025-10-08) | $12,441.0B (wk 2026-10-07) | **+8.6%** since signing; **+7.4% YoY** |
| Deposits, small domestically chartered | FRED DPSSCBW027SBOG, SA | $5,401.9B (wk 2025-07-16); $5,457.3B (wk 2025-10-08) | $5,688.3B (wk 2026-10-07) | **+5.3%** since signing; **+4.2% YoY** |
| USD-pegged stablecoin supply | DefiLlama stablecoincharts/all, global | $257.71B (2025-07-18); $305.81B (2025-10-22) | $303.76B (2026-10-22); peak $315.54B (2026-05-17) | +$46.1B since signing; **−0.7% YoY** |

**H.8 caveat (must survive):** the H.8 "large" panel is the top 25 domestically chartered banks by assets. Most KRE names sit in "small", but a few large regionals (for example HBAN) may sit in "large". The large/small growth gap is therefore not a clean regional-versus-money-center split, and **nothing in the data ties the gap to stablecoins**. The stablecoin total includes some synthetic and tokenized-fund products (for example BUIDL, $2.17B; USDe, $4.65B), so a strict payment-stablecoin total is smaller.

How to read Table 2: the defensible central range is set by assumptions, not by consensus. If yield reaches holders at scale through intermediaries, the bank-aligned scenarios (Nigrinis ≥25%; ICBA $1.3T for community banks) describe that world. If the ban holds as written and demand stays payments-driven and mostly offshore, the official and crypto-side figures (CEA; Miran; CRA "<1%") describe it. Standard Chartered's ~$500B by 2028 (≈2.5% of current deposits, *DEWEY arithmetic*) assumes a $2T market, which the flat ~$300B supply path is not tracking. This report does not pick between these worlds. The regulatory variable that separates them is Table 1 rows 1j–1o.

### Which banks are most exposed?
The sources disagree on which bank tier is most exposed, and no source tests exposure at the bank level:

- **Fed staff:** "Mid-sized regional banks ... may face the greatest vulnerabilities", lacking "both the scale advantages of large institutions and the relationship depth of community banks". For community banks "the picture is likely to be more mixed" [PRIMARY: FEDS Note, 2025-12-17].
- **Standard Chartered:** ranks US regionals most exposed, measured by net interest margin's share of revenue; secondaries name HBAN, MTB, TFC and CFG [NEWS].
- **ICBA:** argues community banks are most exposed [INSTITUTIONAL].
- **CEA:** its model holds the community-bank deposit share constant, which assumes away any differential exposure [PRIMARY].

On deposit type, TBAC names noninterest-bearing transactional deposits as the at-risk class because they are "already non-interest bearing" and "easily transferred" [PRIMARY]. Current crypto users skew young, low-income and unbanked. About 2% of U.S. adults used crypto for payments in 2025 [NEWS on Fed SHED data], and crypto payment use is under 2% in 2023–24 [PRIMARY: KC Fed, 2025-09-24]. Only 1% of corporate treasurers use or pilot stablecoins [NEWS: AFP 2026 survey]. **Gap:** no U.S. study links stablecoin flows to bank-level deposit loss by noninterest-bearing (NIB) share. Table 3 is therefore an exposure *input*, not an exposure measure.

#### Table 3 — Deposit mix, 22 banks (sorted by reported NIB share; descriptive only, not an exposure or trade ranking)
Key:
- **Unins gross** is Q2 2026 (6/30/26) FDIC Call Report RC-O M2 at bank level. It includes collateralized public funds and intercompany balances.
- **Unins company** is the bank's own figure, and its basis is stated in every row.
- **Do not rank across the two uninsured columns, or across different bases within the company column.**
- Cost figures marked (d) are DEWEY derivations from average-balance tables. They cover interest only.
- E = `https://www.sec.gov/Archives/edgar/data/`.

| Ticker | Period end (all cols unless noted) | Total dep $B | NIB $B | NIB % | Unins gross (FDIC, 6/30/26) | Unins company (basis, period) | Brokered $B (basis) | Cost total / IB % | Mix notes | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| ZION | 9/30/26 | 77.948 | 26.371 | 33.8% | 46.2% | 45% ($34.4B; company, includes collateralized $2.7B; 6/30/26) | 3.487 (excl. reciprocal; 9/30/26) | 1.59 / 2.40 | reciprocal ≈$6.6B | [8-K Ex-99.1, filed 2026-10-19](https://www.sec.gov/Archives/edgar/data/109380/000010938026000125/exh991earningsrelease20260.htm) [PRIMARY] |
| COLB | **6/30/26 (Q2)** | 52.056 | 17.218 | 33.1% | 39.5% | 40% ($20.59B; Call Report method; 6/30/26) | 0.978 | ≈1.32 (d, period-end NIB proxy) / 1.96 | customer 93%, public/admin 5%, brokered 2% | [10-Q, filed 2026-08-04](https://www.sec.gov/Archives/edgar/data/887343/000088734326000170/colb-20260630.htm) [PRIMARY] |
| FBP | 9/30/26 | 16.919 | 5.466 | 32.3% | 47.4% | 29.59% (excl. fully collateralized government; 9/30/26) | 0.600 (brokered CDs) | 1.43 (d) / 2.11 (d) | **government deposits $3.0B (17.7%; PR/USVI/FL, collateralized)** | [8-K Ex-99.1, filed 2026-10-22](https://www.sec.gov/Archives/edgar/data/1057706/000105770626000028/exhibit991.htm) [PRIMARY] |
| FHB | **6/30/26 (Q2)** | 20.154 | 6.448 | 32.0% | 48.4% | 45% (excl. public deposits; 6/30/26) | 0 (Call Report BRO) | ≈1.20 (d, proxy) / 1.75 | NIB includes ≈$0.8B Guam/CNMI | [10-Q, filed 2026-08-03](https://www.sec.gov/Archives/edgar/data/36377/000110465926089785/fhb-20260630x10q.htm) [PRIMARY] |
| WAL | 9/30/26 | 81.755 | 25.752 | 31.5% | 38.1% | none disclosed | 5.3 wholesale (excl. reciprocal $15.2B; 6/30/26) | 1.83 (d, interest only; **excludes ECR costs, $158.4M in Q3**) / 2.76 | Commercial 34%, Mortgage 21%, Escrow 16%, HOA 14%, Consumer Digital 7%, Other 8%; ~39% of NIB carries no ECR | [8-K Ex-99.1, filed 2026-10-19](https://www.sec.gov/Archives/edgar/data/1212545/000162828026066286/pressrelease-9302026.htm) [PRIMARY] |
| GBCI | **6/30/26 (Q2)** | 24.654 | 7.423 | 30.1% | 34.0% | none disclosed | 0.003 (wholesale) | 1.18 (core, incl. NIB) / n.a. | core $24.651B | [10-Q, filed 2026-08-04](https://www.sec.gov/Archives/edgar/data/868671/000086867126000069/gbci-20260630.htm) [PRIMARY] |
| UCB | 9/30/26 | 24.888 | 6.751 | 27.1% | 39.4% | ≈28.2% (derived, excl. collateralized $2.79B; 6/30/26) | 0.171 | 1.69 / 2.31 | public funds $2.9B | [8-K Ex-99.1, filed 2026-10-20](https://www.sec.gov/Archives/edgar/data/857855/000110465926117113/tm2627820d1_ex99-1.htm) [PRIMARY] |
| EWBC | 9/30/26 | 71.493 | 18.539 | 25.9% | 51.5% of DEP | 48% of *domestic* deposits (excl. collateralized and affiliate; 6/30/26) | 2.64 (Call Report BRO, 6/30/26) | 2.08 / 2.81 | Consumer & Business 52%, Commercial 36%, International 6%, Treasury/Other 6% | [8-K Ex-99.1, filed 2026-10-20](https://www.sec.gov/Archives/edgar/data/1069157/000106915726000048/ewbc9918k9302026.htm) [PRIMARY] |
| FNB | 9/30/26 | 39.550 | 10.134 | 25.6% | 40.2% | none (coverage ratio 140.1% only) | 1.42 (BRO, 6/30/26) | 1.76 (d) / 2.37 | n.a. | [8-K Ex-99.1, filed 2026-10-20](https://www.sec.gov/Archives/edgar/data/37808/000003780826000027/fnbex991earningsreleaseq32.htm) [PRIMARY] |
| EBC | **6/30/26 (Q2)** | 25.919 | 6.541 | 25.2% | 41.6% | 31% (excl. internal and collateralized; 6/30/26) | 0.113 | 1.47 (d) / 1.96 | municipal deposits seasonal; reciprocal $2.30B | [10-Q, filed 2026-08-07](https://www.sec.gov/Archives/edgar/data/1810546/000162828026054656/ebc-20260630.htm) [PRIMARY] |
| UBSI | 9/30/26 | 27.711 | 6.825 | 24.6% | 38.3% | 32% (excl. affiliate and collateralized; 9/30/26) | 0.34 (BRO, 6/30/26) | 1.88 (d) / 2.51 | n.a. | [8-K Ex-99.1, filed 2026-10-22](https://www.sec.gov/Archives/edgar/data/729986/000119312526428347/d41860dex991.htm) [PRIMARY] |
| SSB | 9/30/26 | 57.638 | 13.446 | 23.3% | 37.8% | 29.2% (uninsured and uncollateralized; 6/30/26) | 4.9 (6/30/26) | 1.80 / 2.37 (d) | 64% commercial / 36% consumer | [8-K Ex-99.1, filed 2026-10-21](https://www.sec.gov/Archives/edgar/data/764038/000119312526427824/ssb-ex99_1.htm) [PRIMARY] |
| VLY | 9/30/26 | 55.229 | 12.447 | 22.5% | 39.8% | 28% (excl. collateralized government and intercompany; 9/30/26) | 5.3 ("indirect customer") | 2.33 / n.a. | branch 65%, specialized 25%, indirect 10% | [8-K Ex-99.1, filed 2026-10-22](https://www.sec.gov/Archives/edgar/data/714310/000071431026000045/exhibit991earningsrelease1.htm) [PRIMARY] |
| HOMB | 9/30/26 | 18.756 | 4.209 | 22.4% | 46.7% | 25.7% (net of intercompany $1.26B and collateralized $3.11B; 6/30/26) | 0.587 (6/30/26) | 1.83 (d) / 2.37 | public funds $3.23B (6/30/26); NIB line is "Demand and non-interest-bearing" | [8-K Ex-99, filed 2026-10-14](https://www.sec.gov/Archives/edgar/data/1331520/000133152026000117/homb093026earningsrelease.htm) [PRIMARY] |
| BPOP | 9/30/26 | 68.705 | 15.011 | 21.8% | 54.5% (two charters) | ≈20.4% (derived: balances >$250K plus uninsured foreign; 6/30/26) | 0.969 | 1.64; **1.13 excl. PR public** / n.a. | **PR public deposits $21.47B = 31%** (collateralized; seasonal outflows) | [8-K Ex-99.1, filed 2026-10-22](https://www.sec.gov/Archives/edgar/data/763901/000076390126000022/ex9918kpressreleaseq32026.htm) [PRIMARY] |
| AUB | 9/30/26 | 30.966 | 6.762 | 21.8% | 36.4% | 31.6% (uninsured and uncollateralized; 9/30/26; % derived) | 1.086 | 2.00 / 2.55 | NIB 22%, interest checking 25%, MM 21%, savings 9%, retail time 13%, jumbo 6%, brokered 4% | [8-K Ex-99.1, filed 2026-10-20](https://www.sec.gov/Archives/edgar/data/883948/000088394826000077/aub-ex99d1.htm) [PRIMARY] |
| PNFP | 9/30/26 | 103.036 | 20.912 | 20.3% | 49.5% | 41% (uninsured excl. collateralized; 9/30/26) | ≈9.40 (derived) | 2.18 (d) / 2.74 | post-Synovus combination; not like-for-like YoY | [8-K Ex-99.1, filed 2026-10-21](https://www.sec.gov/Archives/edgar/data/2082866/000208286626000087/pnfp_09302026xex991xfiling.htm) [PRIMARY] |
| EGBN | 9/30/26 | 8.034 | 1.553 | 19.3% | 27.7% | 30.1% ($2.415B; company; 9/30/26) | ≈2.25 (28% of deposits) | 2.69 / 3.36 | C&I-related 23%, CRE-related ≈14% | [8-K Ex-99, filed 2026-10-21](https://www.sec.gov/Archives/edgar/data/1050441/000105044126000110/finalegbnerq3-2026xearni.htm) [PRIMARY] |
| WTFC | 9/30/26 | 62.435 | 11.585 | 18.6% | 36.2% (16 charters, includes intercompany) | none disclosed | 4.773 (6/30/26) | n.a. / 2.73 | NIB 19%, NOW 11%, wealth 3%, MMDA 39%, savings 10%, CDs 18% | [8-K Ex-99.1, filed 2026-10-19](https://www.sec.gov/Archives/edgar/data/1015328/000101532826000026/exhibit9912026-q3.htm) [PRIMARY] |
| HBAN | 9/30/26 | 224.678 | 41.317 | 18.4% | 32.5% | 31% (consolidated, net of $4.6B intercompany; 6/30/26) | 5.8 (6/30/26) | 1.90 / 2.31 | Consumer & Regional 66%, Commercial 30%, Treasury/Other 4%; includes Cadence/Veritex | [8-K Ex-99.2, filed 2026-10-22](https://www.sec.gov/Archives/edgar/data/49196/000004919626000084/hban20260930_8kex992.htm) [PRIMARY] |
| FLG | **6/30/26 (Q2)** | 67.521 | 11.731 | 17.4% | 28.9% | 21% ("uninsured or not collateralized"; 6/30/26) | 2.148 (excl. reciprocal); BRO 6.53 | 2.53 (d) / 3.08 | includes $2.6B non-servicing custodial | [10-Q, filed 2026-08-06](https://www.sec.gov/Archives/edgar/data/910073/000091007326000068/fbc-20260630.htm) [PRIMARY] |
| OZK | **Total 9/30/26 (secondary); all other cols 6/30/26** | 34.83 (Q3, secondary); 34.00 (FDIC Q2) | 3.95 (Q2) | 11.6% (Q2) | 32.5% | none obtained | 2.52 (BRO, 6/30/26) | ≈2.81 / ≈3.17 (Q2, d, approximate) | not obtained | Q3 total: [Bank OZK IR](https://ir.ozk.com/news-releases/news-release-details/bank-ozk-announces-third-quarter-2026-earnings) (403; via search) and [NWA Democrat-Gazette 2026-10-20](https://www.nwaonline.com/news/2026/oct/20/bank-ozk-releases-third-quarter-earnings-beats/) [NEWS]; Q2: FDIC CERT 110 [PRIMARY] |

FDIC cross-check source for every bank: [FDIC BankFind financials API](https://api.fdic.gov/banks/financials?filters=CERT:57512%20AND%20REPDTE:20260630&fields=DEP,DEPNIDOM,DEPUNA,BRO), fields DEP/DEPNIDOM/DEPUNA/BRO, REPDTE 2026-06-30, with the CERT changed per bank [PRIMARY]. Where both a company figure and a Call Report figure exist, they agree (ZION 45% vs 46.2%; COLB, AUB and EGBN dollar figures identical).

**Table 3 caveats (must survive):**
- **Mixed vintages.** Five rows (FLG, EBC, FHB, COLB, GBCI) are Q2 2026 because no Q3 8-K was on EDGAR as of 2026-10-22. OZK's Q3 total comes from secondary copies of its release; Bank OZK is not an SEC filer.
- **Mixed uninsured bases.** Uninsured shares come on different bases: gross Call Report, consolidated net of intercompany, or uninsured-and-uncollateralized. The gap between gross and adjusted figures runs from 4 to 23 points (for example HOMB 46.7–48.6% gross vs 25.7% adjusted).
- **Puerto Rico public deposits.** BPOP (31% of deposits) and FBP (17.7%, government) carry large collateralized, policy-driven government deposits. These behave differently from retail or commercial balances and distort both uninsured shares and deposit costs.
- **WAL's NIB** includes earnings-credit balances whose cost sits outside interest expense, so a high NIB share there does not mean cheap funding.
- **Call Report brokered (BRO)** includes reciprocal deposits above the statutory cap.

### Where a migrating dollar lands
**Caveat (must survive):** for USDC plus USDT, bank deposits are a small share of reserves. Most reserve dollars sit in dealer repo and T-bills.

#### Table 4 — Reserve recycling (USDT, USDC, USD1, plus USAT for context)

| Coin (outstanding 2026-10-22, DefiLlama) | Reserve as-of | Bank deposits | T-bills | Repo / reverse repo | MMF | Other | Where the bank-deposit leg sits | Source / tag |
|---|---|---|---|---|---|---|---|---|
| USDT ($182.74B) | 2026-06-30 (Q2 attestation, BDO; assets $187.75B) | ≈$34M "cash and bank deposits" at **YE2025** [UNVERIFIED]; Q2 2026 cash/MMF/other ≈$9.1B (≈4.8%) not itemized | $114.96B (≈61%) | $25.62B (overnight $18.63B + term $6.99B) | in the unitemized ≈$9.1B | gold $18.84B, BTC $5.80B, secured loans $13.45B | Offshore issuer; T-bills reportedly custodied at Cantor Fitzgerald | [NEWS] Forklog 2026-08-01, KuCoin; Cantor per [NEWS] Bloomberg 2026-01-27. BDO PDF not opened; Q3 attestation not yet out |
| USDC ($72.50B) | 2026-06-30 (10-Q) | **$11.428B cash (15.6%)**, "primarily" at G-SIBs; banks not named; FDIC-insured portion $1.8M across 7 banks | inside Circle Reserve Fund (CRF) | inside CRF | **CRF $61.917B (84.4%)**, BlackRock-managed, BNY custody | — | G-SIB wholesale deposits (uninsured) | [PRIMARY] Circle 10-Q Q2 2026; 10-K FY2025 |
| ↳ CRF look-through | 2026-09-30 (N-MFP3) | — | $25.36B (40.9%) | $36.65B (59.1%) Treasury repo; counterparties: Wells Fargo Bank 6.96, Goldman 6.19, Barclays 6.10, BNP 4.50, Citi 3.83, Mizuho 3.82, JPM 2.98 ($B) | net assets $62.47B | — | Dealer repo with G-SIB broker-dealers; repo share swings with the calendar (88.0% at 2026-07-31) | [PRIMARY] SEC N-MFP3, BlackRock Funds CIK 844779, Jul/Aug/Sep 2026 |
| USD1 ($4.00B) | 2026-08-31 (KPMG-examined) | **$1.129B (26.9%)** demand deposits at unnamed "U.S. commercial banks, regulated by the Federal Reserve" | — | — | $3.066B (73.1%) government MMF (CUSIP 31607A703; fund not verified) | — | Unnamed Fed-regulated banks | [PRIMARY] BitGo USD1 Reserve Report Aug-2026 |
| USAT ($0.18B, context) | 2026-06-30 | $17.7M (10%) | — | $159.7M (90%) reverse repo | — | — | Anchorage issuer; Cantor custodian | [UNVERIFIED] DIA aggregator |

Sum for the two majors (*DEWEY arithmetic on mixed vintages*: USDC 2026-06-30, USDT deposits YE2025, USDT assets 2026-06-30): about **$11.5B of about $261B of reserves, ≈4.4%**, sits directly in bank deposits, and that slice is concentrated at G-SIBs rather than regionals. The unitemized ≈$9.1B of Tether assets could hold some deposits, so this is a floor for USDT.

**DEWEY / standard-money-mechanics inference (not a sourced finding):** a dollar that leaves a regional bank for USDC or USDT mostly funds T-bill purchases or dealer repo. The deposit then moves to the seller's or dealer's bank. It leaves the banking system only if it ends up at the Fed (ON RRP, or a Treasury General Account build). The CRF July book showed no Fed RRP counterparty. If that holds, migration would show up as **small-bank deposits shifting toward large and foreign-related banks rather than as a fall in the all-bank total**. Fed staff make a related, sourced point: reserves recycle as concentrated, uninsured wholesale deposits at a few custodial banks, which is a *composition* risk for the receiving banks [PRIMARY: FEDS Note 2025-12-17]. The CEA model rests on the same recycling logic [PRIMARY].

### The AI-agent link
The joint hypothesis has three links: cheap sticky deposits, yield-paying stablecoins, and AI agents that move money with little effort. The evidence supports the first and third links separately. It does **not** yet connect agents to stablecoins. **Caveat (must survive):** the deposit-flight motive behind the October 2026 big-bank restrictions on AI agents comes from anonymous and FT-sourced reporting. On the record, the banks cite security and liability. The agent cash-sweep commentary (Apollo/Slok) points at high-yield savings, not stablecoins.

#### Table 5 — AI agents, bank restrictions and stablecoin rails

| Item | Date | Fact | Stated reason / relevance | Tag |
|---|---|---|---|---|
| Apollo, Torsten Slok, "Is an agentic bank run coming?" | 2026-09-27 | AI assistants ("Muse and similar") could sweep household cash from ~0.1% checking into accounts paying 3.3–5.0% (SoFi, Wealthfront, Varo and others) | Scenario, not an observed flow. **No mention of stablecoins** | [INSTITUTIONAL] Apollo |
| Plaid–Muse integration | 2026-10 | One analysis says the integration does not explicitly enable sweeping | Limits the scenario's immediacy | [NEWS] investingLive |
| Citi | 2026-10 | Bars third-party AI agents from logging in or transacting; read-only open-banking access remains | Protecting accounts and information | [NEWS] The Paypers 2026-10-19, citing the FT |
| Bank of America | 2026-10-14 | Limits agent access to consumer deposits while it builds liability protocols; Moynihan wants a human to approve money leaving an account | Liability and control | [NEWS] The Paypers; Retail Banker International |
| JPMorgan | mid-Oct 2026 (Q3 call) | Will block outside agents until its own protections are ready | "Rogue agents" | [NEWS] The Paypers |
| Morgan Stanley; Schwab | 2026-10-22; Oct 2026 | Reported to be blocking third-party agents | — | [UNVERIFIED] Axios (403, snippet only); [NEWS] Coin Insider |
| Deposit-flight motive | Oct 2026 | Executives reportedly contacted the Fed about consumer agent use (per "a person familiar"; the Fed declined comment). A "$1.6T of non-interest-bearing deposits at JPM/BAC/WFC" figure appears **with no named source** | Attribution only; no bank says this on the record | [NEWS]/[UNVERIFIED] The Paypers; Futu |
| Agent payment rails | 2025-10 to 2026 | Coinbase x402 (USDC pay-per-request; reported 160–188M transactions, unverified); Stripe/Tempo Machine Payments Protocol (~Mar 2026); Visa Trusted Agent Protocol and Mastercard Agent Pay (Oct 2025); Google AP2 | These are **payment** rails, not yield products | [NEWS]/vendor: Cointelegraph; CoinDesk 2026-08-23 |
| GENIUS effect on agent float | from 2027-01-18 | An agent's idle payment-stablecoin balance earns nothing from the issuer. It could earn only through an intermediary reward that survives Table 1 rows 1d–1k | Ties the AI-agent story back to the rewards question, not to GENIUS per se | DEWEY reading of [PRIMARY] text |

*Inference:* the agent risk banks are acting on is deposit-rate arbitrage toward high-yield savings and money funds. That risk exists with or without stablecoins. A sweep into a high-yield account at another insured bank reshuffles deposits inside the system; it hits the low-cost-deposit franchise rather than aggregate deposits. Stablecoins enter this channel only if intermediary rewards make them a competitive yield option.

### What early data would show it happening

#### Table 6 — Early-warning dashboard (latest values as pulled 2026-10-22)

| Series | ID / publisher | Cadence, lag | Latest value (date) | Pattern consistent with migration (*inference*) |
|---|---|---|---|---|
| USD stablecoin supply | DefiLlama stablecoincharts/all | daily, ~0 d | $303.76B (2026-10-22); USDT $182.74B, USDC $72.50B | Sustained rise, especially in US-regulated coins after 2027-01-18 |
| Deposits, small domestically chartered (SA) | FRED DPSSCBW027SBOG (H.8) | weekly (week ending Wed), ~9 d; next release 2026-10-23 for wk 10-14 | $5,688.3B (wk 2026-10-07); +4.2% YoY | Declines while large and foreign-related deposits hold or rise |
| Deposits, large domestically chartered (SA) | FRED DPSLCBW027SBOG | weekly, ~9 d | $12,441.0B (wk 2026-10-07); +7.4% YoY | Flat or rising (receives recycled reserve deposits) |
| Deposits, all commercial banks (SA) | FRED DPSACBW027SBOG | weekly, ~9 d | $19,771.5B (wk 2026-10-07); +7.2% YoY | Little change (recycling), unless reserves move to the Fed |
| Deposits, foreign-related institutions (SA) | FRED DPSFRIW027SBOG | weekly, ~9 d | $1,642.2B (wk 2026-10-07) | Rise (foreign G-SIB repo dealers) |
| Large time deposits, all commercial banks | FRED LTDACBW027SBOG | weekly, ~9 d | $2,605.7B (wk 2026-10-07) | Banks bidding term funding to replace core deposits |
| Money market fund assets | ICI weekly | weekly (Thu), ~1 d | $7,923.08B (wk 2026-10-14); government $6,519.99B (institutional $4,537.76B) | Rise in government institutional funds (USDXX is a 2a-7 government fund; whether ICI counts it is unconfirmed) |
| Retail MMF | FRED WRMFNS (H.6) | weekly, published monthly, ~3–4 wk | $3,034B (2026-08-31) | Separates the high-yield-savings/MMF sweep from the stablecoin channel |
| Circle Reserve Fund (USDXX) size | BlackRock product page | daily, ~1 d | $60.77B (2026-10-21) | Growth = new USDC reserve dollars |
| CRF holdings look-through | SEC N-MFP3, CIK 844779, series S000077205 | monthly, ~5–7 business days | $62.47B; 59.1% repo / 40.9% T-bills (2026-09-30) | Shows which dealers receive the money |
| Circle reserve table (cash vs CRF) | SEC 10-Q, CIK 1876042 | quarterly, ~5 wk; Q3 10-Q expected early-to-mid Nov | cash $11.43B / CRF $61.92B (2026-06-30) | Cash leg = direct G-SIB deposits |
| Tether attestation (BDO) | tether.to transparency | quarterly, ~4–5 wk; Q3 not yet out | Q2: assets $187.75B (2026-06-30); live JSON assets $188.30B / liabilities $182.83B (fetched 2026-10-22, undated) | Offshore demand indicator |
| USD1 reserve report (KPMG) | BitGo attestations | monthly, ~3–4 wk | $4.196B; 26.9% bank demand deposits (2026-08-31) | — |
| Bank deposit costs and NIB mix | company 8-K/10-Q (Table 3 banks) | quarterly; Q3 season runs to ~2026-10-30 | Table 3 | NIB share falling faster than peers; IB cost rising (deposit beta) |
| Call Reports (FFIEC 031/041) | FFIEC CDR / FDIC BankFind | quarterly; Q3 due ~2026-10-30 [UNSOURCED: standard FFIEC schedule] | Q2 2026 pulled for Table 3 | Bank-level NIB and uninsured shifts |
| FDIC Quarterly Banking Profile | FDIC | quarterly, ~8 wk | Q2 2026: domestic deposits +$142.7B (+0.8% q/q); uninsured +$317.4B [NEWS: ABA Banking Journal] | By-size-tier deposit change. Note: a Crane Data quote ("insured deposits decreased slightly") does not reconcile with these figures; check the FDIC primary |
| Policy dates | Federal Register | event | Fed GENIUS comments close 2026-11-30; OCC rule effective 2027-01-18; DASP offer ban 2028-07-18 | FDIC/NCUA/Fed finals keeping or dropping the presumption; any CLARITY "skinny" lame-duck vote [NEWS: Roll Call] |

No Treasury TIC or Fed Z.1 stablecoin-issuer series was found (searched; not proven absent). The H.8 large and small panels are re-benchmarked periodically, so step changes at reclassification dates are not flows (general knowledge, not verified this session).

## Counter-Evidence
Evidence against the migration hypothesis (strongest first):
- **No aggregate drain so far.** Since signing, deposits rose +$1,505.6B (+8.2%) while stablecoins rose +$46.1B. Supply is −0.7% YoY, and USDC is −4.8% YoY from a $79.63B peak on 2026-03-18 [PRIMARY: FRED; DefiLlama]. Even if every stablecoin dollar added since signing were US deposit substitution, it would be ≈0.25% of deposits (*DEWEY arithmetic*).
- **Demand is mostly offshore.** Miran expects demand mostly "from locales unable to access dollar-denominated saving instruments" [PRIMARY]. Standard Chartered puts ~2/3 of demand in emerging markets [NEWS]. S&P says demand is mostly ex-US [NEWS]. Fed staff note that foreign demand can *add* to US deposits when reserves are held domestically [PRIMARY: FEDS Note].
- **Reserves recycle.** T-bill and repo reserves return to dealers' deposits. The net drain depends on how reserves are held and on master-account access [PRIMARY: FEDS Note; CEA].
- **Banks can defend with price.** BIS WP 1382 (2026-10-13) finds "deposit rate increases predict slower stablecoin growth", with IV estimates ~3× OLS and stronger effects for USDC [ACADEMIC]. That makes stablecoins a rate-sensitive substitute: the cost shows up in margins, not necessarily in lost funding.
- **No causal deposit effect found.** Ribba (2026, structural VAR) finds no crowd-out [ACADEMIC; read secondhand]. CRA, commissioned by Coinbase, finds no significant USDC effect on community-bank deposits [sponsored].
- **Users are not core depositors.** Crypto payment users skew young, low-income and unbanked [PRIMARY: KC Fed]. Corporate use is 1% [NEWS: AFP].
- **Supply forecasts are being missed.** The $2T-by-2028 forecasts are not tracking supply; JPMorgan sees only $500–600B by 2028 [NEWS].

Evidence that weakens the counter-case:
- The counter-evidence is strongest for *aggregate levels*. It is weaker for **composition**: uninsured issuer deposits concentrated at a few custodial banks, which Fed staff liken to SVB-style concentration [PRIMARY].
- It is also weaker for **franchise value**: repricing of cheap deposits.
- All of it predates the 2027-01-18 effective date and any scaled intermediary-yield regime.
- Most of it comes from sources with a stake in the outcome: the CEA opposes a yield ban, CRA was funded by Coinbase, and the bank groups lobby for closing the rewards channel.

## Unknowns
1. Whether the FDIC, NCUA and Fed finalize with or without the presumption, and whether state "substantially similar" regimes import it. The next dated point is Fed comments closing 2026-11-30.
2. How the OCC will treat specific exchange or affiliate revenue-share rewards programs after 2027-01-18. No guidance or enforcement action exists yet.
3. Whether CLARITY, or a "skinny" version, passes in the lame duck, and its final rewards text (secondary-sourced only; Senate text not pulled from congress.gov).
4. The share of stablecoin demand held by US residents: no estimate found.
5. Current exchange reward rates on USDC and other coins: not pulled.
6. The names of the G-SIBs holding Circle's ≈$11.4B of cash, and of the banks holding USD1's $1.13B.
7. Tether's Q2 2026 itemized cash, bank-deposit and MMF lines, and its Q3 2026 attestation (not yet published).
8. Q3 2026 deposit figures for FLG, EBC, FHB, COLB and GBCI; OZK's Q3 detail from a primary source; adjusted uninsured figures for WAL, WTFC, FNB, GBCI and OZK.
9. Which of the 22 banks sit in the H.8 "large" panel versus "small".
10. Any bank-level evidence linking NIB share to stablecoin outflows: none exists.
11. Actual AI-agent-driven cash movements: no data found. Whether any bank ties its agent restrictions to stablecoins on the record: none found.
12. Post-GENIUS deposit sensitivity: no study yet.

## Source Quality Assessment
- **Rule text: strong.** It comes from the OCC final-rule PDF (Federal Register version pending, so page cites are the PDF's own numbers), the GPO statute, and Federal Register proposals. Coordinator-verified quotes are used verbatim.
- **Deposit-mix table: primary but uneven.** It rests on EDGAR 8-K/10-Q filings and the FDIC Call Report API. Vintages and definitions are mixed and labeled per row. OZK's Q3 total is secondary.
- **Reserve data: mixed.** USDC is strong (10-Q, N-MFP3). USD1 is primary (KPMG-examined report). USDT rests on news secondaries of the BDO attestation, which have an unexplained issued-vs-liabilities gap. USAT is from an aggregator only.
- **Outflow estimates: weak as forecasts.** Almost every figure comes from a party with an interest: bank lobbies, crypto sponsors, a pro-crypto administration, or crypto-bullish sell-side. Official figures are pools or scenarios. Several sell-side and ratings figures are secondhand.
- **AI-agent evidence: weakest.** It is news-level, the key motive is anonymously sourced, and the FT and Axios originals were not read.
- **H.8 and DefiLlama: primary data.** The interpretive caveats above apply.

## References
All accessed 2026-10-22.

**Statute, rules and official sources**
- OCC News Release 2026-92 (2026-10-21): https://www.occ.gov/news-issuances/news-releases/2026/nr-occ-2026-92.html
- OCC final rule PDF, Docket OCC-2025-0372: https://www.occ.gov/news-issuances/news-releases/2026/nr-occ-2026-92a.pdf
- GENIUS Act, Pub. L. 119-27: https://www.govinfo.gov/content/pkg/PLAW-119publ27/html/PLAW-119publ27.htm
- OCC proposal, 91 FR 10202: https://www.federalregister.gov/documents/full_text/text/2026/03/02/2026-04089.txt
- FDIC proposal, 91 FR 18534: https://www.federalregister.gov/documents/full_text/text/2026/04/10/2026-06974.txt
- NCUA proposal, 91 FR 28956: https://www.federalregister.gov/documents/full_text/text/2026/05/18/2026-09915.txt
- Fed proposal, 91 FR 61580: https://www.federalregister.gov/documents/full_text/text/2026/09/29/2026-19860.txt
- Federal Register API: https://www.federalregister.gov/api/v1/documents.json
- TBAC Q2-2025 charge: https://home.treasury.gov/system/files/221/TBACCharge2Q22025.pdf
- FEDS Note (Wang, 2025-12-17): https://www.federalreserve.gov/econres/notes/feds-notes/banks-in-the-age-of-stablecoins-implications-for-deposits-credit-and-financial-intermediation-20251217.html
- Miran speech (2025-11-07): https://www.federalreserve.gov/newsevents/speech/miran20251107a.htm
- CEA (2026-04): https://www.whitehouse.gov/wp-content/uploads/2026/04/Effects-of-Stablecoin-Yield-Prohibition-on-Bank-Lending.pdf
- KC Fed (Hayashi & Routh, 2025-09-24): https://www.kansascityfed.org/research/payments-system-research-briefings/us-consumers-use-of-cryptocurrency-for-payments/
- BIS WP 1382: https://www.bis.org/publications/working-paper-1382-are-stablecoins-and-bank-deposits-substitutes

**Market and filing data**
- FRED series: https://fred.stlouisfed.org/series/DPSACBW027SBOG ; https://fred.stlouisfed.org/series/DPSLCBW027SBOG ; https://fred.stlouisfed.org/series/DPSSCBW027SBOG ; https://fred.stlouisfed.org/series/DPSFRIW027SBOG ; https://fred.stlouisfed.org/series/MMMFFAQ027S
- DefiLlama: https://stablecoins.llama.fi/stablecoincharts/all ; https://stablecoins.llama.fi/stablecoins?includePrices=true ; https://stablecoins.llama.fi/stablecoin/1 ; https://stablecoins.llama.fi/stablecoin/2
- Circle 10-Q Q2 2026: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000248/crcl-20260630.htm
- Circle 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000062/crcl-20251231.htm
- Circle Transparency: https://www.circle.com/transparency
- BlackRock Circle Reserve Fund: https://www.blackrock.com/cash/en-us/products/329365/circle-reserve-fund
- N-MFP3 filings, Jul / Aug / Sep 2026: https://www.sec.gov/Archives/edgar/data/844779/000119312526337709/primary_doc.xml ; https://www.sec.gov/Archives/edgar/data/844779/000119312526384920/primary_doc.xml ; https://www.sec.gov/Archives/edgar/data/844779/000119312526416631/primary_doc.xml
- Tether transparency JSON: https://app.tether.to/transparency.json
- BitGo USD1 Aug-2026 report: https://landing.bitgo.com/rs/552-OGK-141/images/USD1_Reserve_Attestation_Report_August_2026.pdf?version=0
- ICI MMF: https://www.ici.org/research/stats/mmf
- FDIC BankFind API: https://api.fdic.gov/banks/financials
- Bank 8-K/10-Q URLs: inline in Table 3.

**Institutional and advocacy**
- ICBA (2025-12-15): https://www.icba.org/w/icba-analysis-permitting-interest-on-stablecoins
- ICBA (2026-10-21): https://www.icba.org/w/icba-continues-call-for-occ-to-ensure-stablecoin-rules-limit-harm-to-local-lending
- ABA Banking Journal: https://bankingjournal.aba.com/2026/10/occ-finalizes-stablecoin-rule-with-narrow-payment-of-interest-prohibition/
- BPI: https://bpi.com/occ-genius-act-rule-leaves-room-for-ambiguity-on-yield/
- CBA/Nigrinis: https://consumerbankers.com/press-release/icymi-new-research-examines-impact-of-interest-bearing-stablecoins-on-banks-ability-to-lend/
- Open Banker: https://openbanker.beehiiv.com/p/moneyinlendingout
- CRA: https://www.crai.com/insights-events/publications/stablecoins-impact-community-bank-deposits/
- Apollo: https://www.apollo.com/institutional/insights-news/insights/daily-spark/is-an-agentic-bank-run-coming
- Latham & Watkins tracker: https://www.lw.com/en/us-crypto-policy-tracker/legislative-developments
- DLA Piper: https://www.dlapiper.com/en/insights/publications/2026/09/senate-fails-to-advance-the-clarity-act

**News**
- CNBC (2026-09-15): https://www.cnbc.com/2026/09/15/senate-cloture-vote-on-clarity-act-fails-dealing-regulatory-setback-to-crypto-industry.html
- Roll Call (2026-10-22): https://rollcall.com/2026/10/22/stablecoin-yield-rule-revives-crypto-vs-banking-industry-fight/
- CoinDesk (2026-10-21): https://www.coindesk.com/policy/2026/10/21/occ-s-final-rule-to-start-fresh-in-weighing-stablecoin-rewards-against-genius-act-ban
- Coinpedia: https://coinpedia.org/crypto-live-news/genius-act-news-occ-final-rule-drops-stablecoin-yield-curbs-banks-push-back/
- The Block (Moynihan): https://www.theblock.co/post/385724/bank-of-america-ceo-stablecoin-yields
- The Block (Standard Chartered): https://www.theblock.co/post/387211/standard-chartered-warns-stablecoins-could-drain-500-billion-from-u-s-bank-deposits-by-2028
- The Block (JPMorgan): https://www.theblock.co/post/383236/jpmorgan-stablecoin-market-projections
- Citi (Yahoo): https://finance.yahoo.com/news/citi-projects-19-trillion-stablecoin-boom-by-2030-152224619.html
- S&P (CryptoBreaking): https://www.cryptobreaking.com/sp-stablecoins-us-banks-impact/
- KC Fed Jacewitz (Payment Expert): https://paymentexpert.com/2025/08/12/fed-warns-stablecoins-may-squeeze-bank-credit/
- The Paypers (2026-10-19): https://thepaypers.com/fintech/news/citi-and-bank-of-america-restrict-ai-agents-from-accessing-accounts
- Retail Banker International: https://www.retailbankerinternational.com/news/us-banks-limit-ai-agents-access/
- investingLive: https://investinglive.com/stocks/apollo-s-slok-warns-ai-agents-could-trigger-a-bank-run-agentic-bank-run-is-still-a-run/
- Axios (2026-10-22, not read): https://www.axios.com/2026/10/22/ai-agents-banks-unauthorized-accounts-access
- CoinDesk (2026-08-23): https://www.coindesk.com/business/2026/08/23/crypto-s-next-billion-users-might-be-ai-agents-and-they-re-paying-with-stablecoins
- Forklog (Tether Q2): https://forklog.com/en/tethers-excess-reserves-halve-in-q2/
- Bloomberg (USAT/Cantor): https://www.bloomberg.com/news/articles/2026-01-27/tether-anchorage-digital-launch-us-focused-stablecoin-usat
- Fed SHED summary: https://coinmarketcap.com/academy/article/fed-report-americans-crypto-usage-2025
- NWA Democrat-Gazette (OZK): https://www.nwaonline.com/news/2026/oct/20/bank-ozk-releases-third-quarter-earnings-beats/
- Decrypt (proposal and Coinbase): https://decrypt.co/359506/banking-occ-new-stablecoin-yield-rules-coinbase

## Process Report
- **Searches run:** Four research legs: (1) rule text; (2) outflow estimates, exposure, AI agents and counter-evidence (~30 tool calls reported); (3) reserves and dashboard; (4) deposit mix for 22 banks. Tool-call counts for legs 1, 3 and 4 were not recorded. Primary pulls included the OCC final-rule PDF, the GPO statute, the Federal Register API, EDGAR 8-K/10-Q filings, three N-MFP3 filings, the FDIC BankFind API (22 banks, 37 charters), FRED H.8 and DefiLlama. DEWEY independently re-verified the OCC quotes (against the final-rule text), the H.8 figures (FRED pull) and the DefiLlama figures (API pull). DEWEY also spot-checked two Table 3 rows against the 8-K exhibits: ZION total deposits $77,948M and NIB $26,371M, and HBAN $224,678M and $41,317M. Both match exactly. Sub-agents ran in data-return mode. A report-writer sub-agent drafted this report and DEWEY reviewed it before filing.
- **Data gaps:**
  - No post-GENIUS deposit data or study.
  - No US-resident share of stablecoin demand.
  - The banks holding Circle's and USD1's cash are not named.
  - Tether's Q2 itemization (cash, bank deposits, MMF) was not obtained; the Q3 attestation is not yet out.
  - Q3 figures are missing for FLG, EBC, FHB, COLB and GBCI; OZK's Q3 detail is not from a primary source.
  - Fitch: no estimate. Moody's and S&P: primaries not read. Citi deposit range and KC Fed (Jacewitz): primaries not read.
  - Senate CLARITY rewards text: not pulled from congress.gov.
  - Exchange reward rates: not pulled.
  - H.8 panel membership: not checked.
- **Source frustrations:**
  - ir.ozk.com, Axios and the FT returned 403 or a paywall.
  - The CRA PDF and BitGo's September report URL served HTML instead of a PDF.
  - The Paxos transparency page rendered no figures.
  - The OCC final rule is not yet in the Federal Register (PDF page cites used).
  - Bank OZK is not an SEC filer.
  - Several Q3 releases are not yet on EDGAR.
  - X (the "DROPPED" post) is not fetchable.
- **Confidence in findings:**
  - High for rule text and data series.
  - Medium on how the rewards question resolves for exchanges and affiliates (case-by-case, other regulators pending).
  - Low on migration size: every estimate is assumption-driven and pre-GENIUS.
  - Low on the AI-agent→stablecoin link, which no source makes.
- **If I had more time/tools:**
  - Re-pull Q3 deposit figures for the five Q2-vintage banks and OZK after ~2026-10-30, along with Q3 Call Reports.
  - Open the Tether BDO PDF and Circle's August attestation.
  - Map H.8 panel membership for the 22 banks.
  - Pull the Senate CLARITY text from congress.gov.
  - Pull FDIC QBP deposits by size tier.
  - Read the FT and Axios originals.
- **Suggestions (for scripts/BACKLOG.md, DEWEY to decide):**
  - An FDIC BankFind deposit-mix puller (DEP, DEPNIDOM, DEPUNA, BRO by CERT list, with multi-charter summing).
  - An N-MFP3 parser for the Circle Reserve Fund repo and counterparty look-through.
  - A weekly H.8 large/small/foreign-related plus DefiLlama plus ICI snapshot script to drive Table 6.
  - Recurring blockers to log: ir.ozk.com 403, and PDF-served-as-HTML (CRA, BitGo).
