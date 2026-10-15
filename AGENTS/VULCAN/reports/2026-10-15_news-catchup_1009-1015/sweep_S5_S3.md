# VULCAN news sweep: S5 (AI-infra financing) + S3 (AI power demand), 2026-10-09 → 2026-10-15

Swept 2026-10-15 ~12:15 ET (`date`: Thu Oct 15 12:11:44 EDT 2026). Research assistant output. **Not a repo file and not graded.**
Labels: **P** = primary (issuer filing or press release, regulator, grid operator). **R** = relay (press citing others). **R-gated** = the original is paywalled and only the relay was read. **COMPUTED** = arithmetic done here. **UNVERIFIED** = could not be confirmed.
Class: **PRICE** = market move. **STRUCT** = contractual, financing-structure or regulatory event.

---

## 0. HEADLINE FOR GRADING: Volta ~$5B GPU loan (coordinator's priority item)

| Field | Figure | Source URL | Source date | P/R |
|---|---|---|---|---|
| Borrower / arrangers | Volta Tydal Holdings S.à r.l. (Lux). JPM + GS are joint lead arrangers | https://ca.finance.yahoo.com/news/volta-launches-5b-leveraged-loan-142910544.html (PitchBook News) | 2026-10-09 10:29 ET | R (trade press, loan-desk level) |
| Structure | $5.012B total = **$1.3B 1L TLC** + **$3.712B GPU TL**. 6-yr, **WAL 3.1y**, sculpted to fully repay by 5.5y. NC2, then 102 in yr 3, par in yr 4. Ticking fee 45% of drawn spread (60-day holiday). **Unrated** | same | 2026-10-09 | R |
| **FORMAL LAUNCH TALK (both tranches)** | **S+625–650, 0% floor, OID 97–98, YTM 11.21–11.75%**. Commitments due **5pm ET Wed 10/14**. Step-downs "yet to be announced" | same | 2026-10-09 | R |
| Same talk reported earlier | "6.25–6.50pp over benchmark", 97–98, ~11%, lender call on a Monday | https://www.briefs.co/news/jpmorgan-pitches-5-billion-ai-loan-for-volta-at-roughly-11-y/ (cites Bloomberg 2026-10-05 "JPMorgan dangles 11% yield…") | 2026-10-05 | R-gated |
| **PRE-LAUNCH SOUNDING (Aug–Sep)** | **S+500, OID 98–98.5**, "sounding out investors" for feedback before Labor Day. "Early stages", pricing subject to feedback. 75% loan-to-cost (~105% debt/GPU cost). **No corporate guarantee** | https://octus.com/resources/articles/volta-jpm-sound-out-investors/ | 2026-09-01 (Bloomberg first reported 8/27) | R (trade press) |
| What happened between | The S+500 attempt "failed to clear". Buyers asked for **~125–150bp more spread, plus the discount** | https://aiweekly.co/alerts/jpmorgan-goldman-underwrite-only-13b-of-voltas-5b-ai-loan (cites Bloomberg/Claire Ruckin 10/12); https://cryptobriefing.com/jpmorgan-goldman-volta-5b-ai-loan/ | 2026-10-12 | R-gated |
| Underwriting curbed (STRUCT) | Banks **underwrote only the $1.3B TLC**. The **$3.712B GPU TL has no bank backstop** (best efforts). Bloomberg calls it "a rare move to limit exposure" | https://www.bloomberg.com/news/articles/2026-10-12/jpmorgan-goldman-curb-exposure-on-5-billion-volta-ai-loan-sale (403, not read); relays aiweekly, qz.com | 2026-10-12 | R-gated |
| Semafor | Expected to price "later this week" at **≥11%**. **Apollo $1.5B order**. Rate steps down if Anthropic gets an IG rating. Allocations "still under discussion" | https://semafor.com/article/10/13/2026/voltas-5-billion-debt-deal-is-a-pulse-check-on-the-ai-financing-boom | 2026-10-13 16:32 ET | R (exclusive) |
| **Final pricing / pulled / downsized** | **NOT FOUND.** No report after the 10/14 5pm deadline as of 12:15 ET 10/15 | Searches: "Volta loan priced/allocates/finalizes", "Volta … flex price talk octus/9fin/LevFin". Bitdeer 6-Ks 10/2 and 10/8 checked on EDGAR: director resignation and a $100M buyback, nothing on Volta | — | UNVERIFIED |

**Grading arithmetic (COMPUTED, rough).** A 1pt OID is spread over a 3.1y WAL, so it adds ~32bp/yr. No compounding.

| Basis | Soft (pre-launch) talk | Launch talk | Δ yield-equiv |
|---|---|---|---|
| Tight vs tight | S+500 @98.5 → ~548bp | S+625 @98 → ~690bp | **~+142bp** |
| Mid vs mid | S+500 @98.25 → ~556bp | S+637.5 @97.5 → ~718bp | **~+162bp** |
| Wide vs wide | S+500 @98 → ~565bp | S+650 @97 → ~747bp | **~+182bp** |

**Read for the desk:**
1. The load-bearing number, **cleared pricing against FORMAL LAUNCH talk (S+625–650 / 97–98), CANNOT BE GRADED: no final pricing was found.** Measured against the launch talk, nothing is known yet to be flexed or pulled.
2. The S+500 figure was a **pre-launch sounding**, per Octus's own words ("sounding out", "early stages", "subject to feedback"). It was not a formal launch talk. Measured against it, the move is talk-to-talk, not cleared. It is **+125–150bp on spread alone** and **~+142 to +182bp yield-equivalent**, which **straddles the +150bp red line**. Whether a pre-launch sounding counts as "talk" under the S5 rule is a **rule-reading question for the desk / Will**. I have not settled it.
3. STRUCT signal, independent of the grade: the banks would not underwrite **74%** of the package ($3.712B / $5.012B, COMPUTED).

---

## 1. S5: AI-infra deals pulled, postponed, flexed or priced since 10/9

| Claim | Figure | Source URL | Source date | P/R | Class |
|---|---|---|---|---|---|
| **AirTrunk (Blackstone) Singapore data-centre REIT IPO POSTPONED** | ~US$1.5B raise, ~US$15B valuation. Was slated for Sep/Oct; "early 2027" possible. Cause: AI-stock selloff and rate uncertainty | https://www.tradingview.com/news/reuters.com,2026:newsml_L4N45Z0H4:0-blackstone-backed-airtrunk-delays-singapore-reit-ipo-amid-ai-stock-selloff-sources-say/ ; https://w.media/airtrunk-postpones-singapore-us1-5-billion-reit-ipo-amid-ai-stock-selloff-report/ | WSJ 2026-10-13; Reuters confirmed (2 sources) | R | STRUCT. **POSTPONED, not withdrawn ⇒ AMBIGUOUS under the 10/09 ruling, not scored.** Composition caveat: a REIT of operating data centres (colo, not a neocloud) |
| **Cipher Digital $850M 0% converts due 2032 PRICED AT LAUNCH SIZE** | Launched 10/13 at $850M (+$150M greenshoe). **Priced 10/14 at $850M**, 0.00% coupon, conv. price $15.31 = **35.0% premium** to $11.34 (10/13 close). Net ~$835.1M. Settles 10/16. Also exchanging ~$165.9M of 1.75% 2030 converts for ~40.7M shares | https://www.sec.gov/Archives/edgar/data/1819989/000119312526419743/d134900d8k.htm (launch) ; https://www.sec.gov/Archives/edgar/data/1819989/000119312526421035/d77312dex991.htm (pricing) | 2026-10-13 / 2026-10-14 | **P** (8-K) | STRUCT. **Counter-evidence: an AI-infra issue cleared at size during the selloff.** Launch talk for coupon and premium was not in the 8-K, so terms against talk are UNVERIFIED. CIFR fell ~5% on pricing day (247wallst relay) |
| Firmus ASX IPO withdrawal (already FIRED by the desk 10/09, KB-209) | A$7.1B (~US$4.94B), ~US$30.6B valuation. Bankers had weighed cutting to US$20–25B and the price from A$11 to A$8.25. Revenue ~$51M/yr | https://finance.yahoo.com/markets/stocks/articles/firmus-explores-3-billion-private-120453436.html (Bloomberg via Quartz); https://www.abc.net.au/news/2026-10-09/firmus-float-gets-pulled-following-lacklustre-investor-demand/107246230 | 2026-10-09 | R | STRUCT (already scored) |
| **Firmus after withdrawal: private round** | Exploring **$2–3B** private round with existing investors. **Equity/debt mix undetermined.** Nvidia participation unclear. Existing holders had planned to take ~half the IPO. Also "exploring a longer-term US listing". **No valuation reported; nothing closed** | https://finance.yahoo.com/markets/stocks/articles/firmus-explores-3-billion-private-120453436.html | 2026-10-09 08:04 ET | R-gated (Bloomberg) | STRUCT, in progress |
| SB Energy IPO (Nasdaq: SBE) | **Still delayed. No launch found.** IFR: launch held because of a valuation gap vs a US$50B target / US$5B raise; roadshow had been planned for the week of 9/21. Nvidia: $1.5B prepaid at a 10% discount + $1.5B concurrent placement. SoftBank discussing a margin loan on part of its SB Energy stake | https://www.ifre.com/equities/2490131/sb-energy-delays-ipo-launch-amid-data-centre-backlash | IFR issue 2652 (9/26–10/2) | R | STRUCT. **No withdrawal found ⇒ not scored.** The "mid-to-late October" window rests on an Investing.com assumption, not a reported plan |
| Lambda IPO | No S-1, launch or pricing found for 10/9–10/15 | searched "Lambda IPO October 2026" | — | UNVERIFIED (absence) | — |
| Crusoe | No new financing found in window | searched | — | UNVERIFIED (absence) | — |
| Nebius / IREN / Applied Digital / TeraWulf | **No 8-K or 6-K financing in window.** EDGAR swept 10/8–10/15: IREN filed only DEF 14A/ARS (10/13); APLD, WULF, NBIS, HUT, CORZ, GLXY, DOCN had nothing non-insider. IREN +4% on 10/12 on an **unconfirmed** report of an Anthropic cloud deal | EDGAR submissions API; https://247wallst.com/investing/2026/10/12/iren-climbs-4-on-report-of-unconfirmed-anthropic-cloud-deal-terawulf-and-applied-digital-hold-flat/ | 2026-10-15 sweep | P (absence) / R | — |
| Gartner, via Reuters | ~80% of neoclouds could shut by 2030. >$3.5T of AI infra spend at impairment risk | BNN/Reuters link in §2 | 2026-10-15 | R | narrative |
| Morgan Stanley, via Semafor | September was the 2nd-lowest AI-financing issuance month of 2026. Expects Q4 slower. >$450B AI-related debt YTD | Semafor link above | 2026-10-13 | R | flow |

---

## 2. S5: CoreWeave (CRWV)

### 2a. PRICE (closes from yfinance, pulled 2026-10-15 12:11 ET; 10/15 is INTRADAY)

| Date | CRWV close | Δ |
|---|---|---|
| 09-30 | 87.12 | |
| 10-06 | 91.72 (10-session high) | |
| 10-08 | 81.58 | −7.8% d/d (OpenAI revenue report) |
| 10-13 | 77.81 | |
| **10-14** | **65.78** | **−15.46% d/d (COMPUTED; matches Reuters ">15%" and SiliconANGLE "15.5%")** |
| 10-15 (intraday) | 64.14 | −2.5% |

10 sessions (9/30 → 10/14): **−24.5%** (COMPUTED). Peak 10/6 → 10/14: **−28.3%**. Peak → 10/15 intraday: **−30.1%**. The desk's "~−29% over 10 sessions" matches the **peak-to-trough** basis, not a strict 10-session window. **Name the basis when citing it.**
Peers, 10/13 → 10/14 close (COMPUTED): ORCL −8.83% (143.20→130.55) · NBIS −10.1% · IREN −12.2% · APLD −9.4% · CIFR −12.3% · WULF −12.6% · BE −9.2% · SOXX −4.5%.

### 2b. What drove 10/13–10/14

| Claim | Figure | Source URL | Source date | P/R | Class |
|---|---|---|---|---|---|
| Trigger 1: OpenAI revenue disclosure | OpenAI told investors annualized revenue was **~$50B at end-Sept**, vs a ~$68–70B figure circulated in late Sept. The gap is partly a revenue-counting basis difference. CRWV −7.8% on 10/8, ORCL −5% | https://finance.yahoo.com/markets/stocks/articles/coreweave-stock-fell-nearly-8-165813372.html ; https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html (403) | 2026-10-08 | R | PRICE (S1 root: count once) |
| Trigger 2: bond chart went viral | Chamath Palihapitiya (Tue 10/13) posted a chart of a **$1.25B CRWV bond** yield briefly passing **15%**. Musk replied "Yikes". Heavy put buying | https://siliconangle.com/2026/10/14/shares-of-oracle-neoclouds-drop-on-coreweave-debt-concerns/ | 2026-10-14 18:20 ET | R | PRICE |
| Bonds | **April-issued 2031 notes yield >16%** (Reuters/BNN). The other Reuters piece says **2032 notes ~78c, yield just over 16%** (Tradeweb). **The two maturities conflict; reconcile before citing** | https://www.bnnbloomberg.ca/investing/2026/10/15/coreweave-shares-bonds-slide-further-as-ai-debt-fears-mount/ ; https://www.933thedrive.com/2026/10/15/ai-credit-default-swap-spreads-widen-sharply/ (Reuters, Westbrook/Cooper) | 2026-10-15 | R | PRICE (credit) |
| **CDS** | **~1,000bp 5y**. Reuters' own calc: ~63% implied 5y default probability vs ~30% a year earlier. Exact figure not given | same two Reuters links (S&P GMI / LSEG data) | 2026-10-15 | R | PRICE (credit) |
| CEO memo (internal, seen by Reuters) | Intrator: "We are confident in our backlog which more than supports all of our debt obligations." Says markets "can sometimes misread" | BNN/Reuters ; SiliconANGLE | 2026-10-14 memo | R | narrative. **Not filed** (no 8-K) |
| Debt / backlog context | "~$50B debt" (LSEG; likely includes leases). Another relay puts Q2 total debt at ~$35B. **Basis conflict.** Backlog $104B at 6/30, plus >$25B signed early Q3 (MSFT, META, OpenAI). 2026 capex guide $35–39B (raised +$4B in Aug). McBee to FT: wants an IG rating | BNN/Reuters ; SiliconANGLE ; https://pulse2.com/coreweave-revenue-backlog-reaches-104-billion-before-another-25-billion-of-new-commitments/ | various | R | context |
| **New financing / covenant / customer contract** | **NONE FOUND in window.** EDGAR 10/1–10/15: only Forms 4 and 144 (insider sales filed 10/6, 10/13 ×3, 10/14 ×2). **No 8-K** | EDGAR CIK 0001769628 submissions API | 2026-10-15 | **P (absence)** | — |
| Benzinga: "240 MW India entry" in the same week | Headline only. Article 403; partner and financing not read | https://www.benzinga.com/trading-ideas/movers/26/10/62270172/... | ~2026-10-09 | UNVERIFIED | STRUCT? |
| **Q3 2026 earnings date** | **NOT ANNOUNCED.** IR news page renders "Loading…"; no Business Wire date release found. Precedent: Q3-25 date announced 10/27 for 11/10; Q2-26 announced 7/27 for 8/11. Third-party estimates: 11/10 or 11/16 (unconfirmed). Expect a release around **~10/26–10/28** | https://investors.coreweave.com/news/default.aspx ; https://www.businesswire.com/news/home/20251027854203/en | — | UNVERIFIED | calendar |

---

## 3. S5: Oracle (ORCL)

| Claim | Figure | Source URL | Source date | P/R | Class |
|---|---|---|---|---|---|
| **No ORCL 8-K in window** | EDGAR 10/1–10/15: one Form 4 (10/1) only | EDGAR CIK 0001341439 | 2026-10-15 | **P (absence)** | — |
| **Chip-lease SPV talks with Apollo + Goldman** | WSJ: talks to fund chips for a **1 GW** data center via a separate entity that buys the chips and leases them to ORCL (off balance sheet). Aim to close in 2026. **No amount given** ("tens of billions" for a 1 GW Nvidia build). Other partners in talks | https://investinglive.com/stocks/wsj-broadcom-seeks-over-50-billion-for-openai-chips-as-oracle-spacex-chase-ai-debt-deals/ | WSJ 2026-10-07 | R-gated | STRUCT (talks, not signed) |
| **5y CDS record** | **288bp**, unchanged d/d on 10/15. Was **260bp a week earlier**; +26bp overnight into 10/14 (S&P GMI). ~203bp around 10/10 (FT relay). **Morgan Stanley note 10/7: 260** | https://www.933thedrive.com/2026/10/15/ai-credit-default-swap-spreads-widen-sharply/ ; https://startupfortune.com/bond-investors-are-starting-to-say-no-to-the-ai-debt-binge/ | 2026-10-15 / 2026-10-10 | R | PRICE (credit) |
| Bonds | 2036 and 2056 spreads "widened further" (FT relay, 10/10). The 6.7% 2056s went **>8%** in late Sept on the Jupiter force majeure. **No October level found for the 2056s** | startupfortune ; https://www.tipranks.com/news/oracle-credit-default-swaps-hit-record-high-as-2056-bond-yield-tops-8 | 2026-10-10 | R | PRICE |
| Equity | −8.83% on 10/14 (COMPUTED). −5% on 10/8 (OpenAI revenue + WSJ chip-financing report). −5.5% on the trucked-gas report (10/8) | yfinance ; relays | — | P (price data) / R | PRICE |
| Rating level (background, NOT new) | S&P BBB- (from BBB) on **2026-07-09**, stable outlook, A-3 short-term. Desk should already hold this | https://ppc.land/s-p-cuts-oracle-to-bbb-as-ai-buildout-widens-cash-deficit-to-42bn/ | 2026-07-09 | R | STRUCT (old) |
| Project Jupiter force majeure (background, NOT in window) | Notice to the Blue Owl/STACK developer on **2026-09-24**, to allow payment delay if the 2028 start slips. Gas pipeline slipped to 2027. NM air permit due by 11/23. Site flooded 9/30 (no critical damage) | https://techcrunch.com/2026/09/24/oracle-sends-force-majeure-notice-on-its-new-mexico-stargate-data-center/ ; https://capacityglobal.com/news/165bn-project-jupiter-what-oracles-force-majeure-notice-means-for-ai-data-centre-risk/ | 2026-09-24 | R | STRUCT (old) |
| $38B Vantage TX/WI construction loan (JPM/MUFG) | >6 months in syndication. Some lenders selling slices to non-banks **at a discount**. No price given | https://startupfortune.com/banks-are-now-trying-to-offload-the-ai-data-center-debt-they-just-underwrote/ (Bloomberg relay) | ~2026-10 (date not pinned) | R | STRUCT/PRICE |
| Tencent ~$7B, ~100k-chip lease (5y, ~30% upfront) | Single low-quality source. **UNVERIFIED** | https://timothysykes.com/news/oracle-corporation-orcl-news-2026_10_13 | 2026-10-13 | R (weak) | STRUCT? |
| **$3.3B lessor guarantee (Sept-2026 maturity)** | **Nothing found in window.** No 8-K. Searched under the Oracle financing queries | — | — | UNVERIFIED | — |
| Calendar | ORCL analyst day **2026-10-28** (per sentisense relay) | https://app.sentisense.ai/stories/oracle-shares-slip-over-4-percent-after-multiple-analyst-target-cuts-analyst-day-09022026 | 2026-09-02 | R | calendar |

---

## 4. S5: other chip, hyperscaler and private-credit financing

| Claim | Figure | Source URL | Source date | P/R | Class |
|---|---|---|---|---|---|
| Broadcom arranging financing for OpenAI custom chips | **>$50B**. Lenders approached: **Apollo, Blackstone**. Early stage; size could change. Close targeted before YE. Covers several GW ("Nexus"/Jalapeño/Serrano) | investinglive (WSJ relay) | 2026-10-07 | R-gated | STRUCT (talks) |
| SpaceX chip financing (Nvidia, for xAI Colossus 2) | **$40B**: ~$10B bank loans + ~$30B **IG** debt. **Apollo to lead**; PIMCO in talks. Close expected **2027** (FT) | https://www.bnnbloomberg.ca/business/company-news/2026/10/07/spacex-seeks-us40-billion-financing-to-buy-nvidia-chips-sources-say/ | 2026-10-07 | R (Reuters/FT) | STRUCT (talks). Just before the window |
| SpaceX bonds | "SpaceX joins Oracle above 7.5%" yield, hyperscaler bond screen (headline only) | https://www.tradingview.com/news/benzinga:7522ce132094b:0-highest-yielding-hyperscaler-bonds-in-october-2026-spacex-joins-oracle-above-7-5/ | 2026-10 | R | PRICE. UNVERIFIED detail |
| SoftBank 5y CDS | **424bp**, +24bp | 933thedrive/Reuters | 2026-10-15 | R | PRICE |
| Meta "Beignet" (Hyperion) 6.581% 2049 secured, $27.3B | **~91–91.6c on 10/7** (record low). Yield up to **7.55%**, ~**230bp** over UST. Was 94.4 ~3 weeks earlier; >110 just after issue. **No 10/9–10/15 print found** | https://www.tokenpost.com/news/technology/27470 ; https://protos.com/metas-ai-bond-just-hit-a-record-low-as-its-stock-soared/ | 2026-10-07 | R | PRICE |
| Meta new $25B bond demand | $96B peak orders vs $125B for a $30B deal a year earlier. **El Paso 1 GW "Project Sopaipilla"**: BlackRock raising >$12B of bonds | startupfortune (FT relay) | 2026-10-10 | R | STRUCT/flow |
| Hyperscaler CDS | AMZN, GOOGL, META, NVDA at **record** wides, but far smaller than ORCL/CRWV. No levels given | 933thedrive/Reuters | 2026-10-15 | R | PRICE |
| Amazon GPU sale-leaseback SPV | ~$8B of GB-series chips into an SPV: debt plus up to 10% outside equity, leased back. **Talks only; no update in window** | https://siliconangle.com/2026/10/02/report-amazon-to-offload-8b-worth-of-ai-chips-lease-them-back/ | FT 2026-10-02 | R | STRUCT (talks, pre-window) |
| BDC / private-credit stress tied to data centers | **No data-center-specific mark or nonaccrual found.** General backdrop: BDC distressed debt $6.8B (5.2% of assets, +64% YoY, PitchBook via Forbes 10/3). Non-traded BDC redemption requests 10.3% (Q2, Fitch) | https://www.forbes.com/sites/mayrarodriguezvalladares/2026/10/03/private-credit-and-equity-face-warnings-on-ai-lending-concentration/ | 2026-10-03 | R | context. UNVERIFIED for DC-specific |
| Anthropic Q3 revenue (pre-IPO meeting) | $16.8B, +45% q/q. Targeting a $2T valuation | 933thedrive/Reuters | 2026-10-15 | R (single investor) | context (Volta step-down hinges on an Anthropic IG rating) |

---

## 5. S3: AI power demand

| Claim | Figure | Source URL | Source date | P/R | Class |
|---|---|---|---|---|---|
| **DOE 202(c) Order No. 202-26-50 (PJM)** | Issued **10/12**, effective **10/13–10/16**. PJM applied 10/11. Forecast **"at or around 111,500 MW (or higher)"** on 10/13. **"Within 900 MW of its reserve margin on October 14"**. Generation outages **61,591 MW**. Most acute zones: **BGE, PEPCO, Dominion**. Authorizes backup generation at **large loads / data centers** "as a last resort before or during" an EEA 3 | https://www.energy.gov/documents/doe-order-no-202-26-50 (PDF text extracted here) | 2026-10-12 | **P** | STRUCT (regulatory) |
| PJM operations | Max Gen Alert + Load Management Alert, 10/13 extended to 10/14. **Pre-Emergency Load Management (DR) called 10/13 AND 10/14** for the evening net-load peak. Non-firm exports recalled. **All maintenance outages recalled from noon 10/14.** Forecast peaks: **112,447 MW (10/13), 113,312 MW (10/14)**. **"PJM has not yet had to use" the data-center backup authority.** **No EEA declared** in the posts read | https://insidelines.pjm.com/operations-update-extends-maximum-generation-alert-calls-on-demand-response/ | 2026-10-13, updated 10/14 15:00 | **P** | STRUCT. **No data-center curtailment occurred as of 10/14 15:00.** 10/15–16 not checked |
| Prior PJM 202(c) | An earlier order covered 9/17–18; Eddystone 202-26-40 runs to 11/20 | IBTimes relay ; energy.gov | — | R/P | context |
| **FERC rejects most of PJM's large-load plan** | **10/9 order** (eLibrary 20261009-3055). REJECTED: **IRAS** (connect without matching capacity in exchange for pre-emergency curtailment), **BYONC**, curtailment provisions ("appear to dictate which retail customers… will be curtailed"), and the compensation framework. KEPT: the large-load definition (50 MW, per mgrid relay) + the registry. Rosner: region could shed "thousands of megawatts… on an involuntary basis"; says the states must set curtailment priority | https://www.utilitydive.com/news/ferc-pjm-large-load-interconnection-iras-byonc/832716/ ; https://mgrid.org/2026/10/10/ferc-rejects-pjms-curtail-first-plan-for-new-large-loads-and-keeps-only-the-50-mw-definition-and-a-registry/ | 2026-10-09 (UD 10/12) | R (order cited by accession number; FERC order not read) | STRUCT. **Removes the federal "curtail-first" mechanism, so curtailment priority goes to the states.** 30-day compliance filing (mgrid; UNVERIFIED) |
| PJM emergency procurement | Window 9/30–10/21, results in December. Board letter 7/27 cites ~60 GW shortfall over a decade | IBTimes / Reuters relay | — | R | calendar |
| Utility refusing a contracted data-center load | **None found in window.** Closest: Texas Gov. Abbott's **8/3** audit directive pausing ERCOT large-load studies (~474 GW queue; ERCOT targets December for the audit). **Old, not in window** | https://www.utilitydive.com/news/texas-hits-pause-data-center-interconnections/827046/ ; https://www.utilitydive.com/news/ercot-texas-puc-data-center-audit/828472/ | 2026-08-05 | R | STRUCT (old) |
| Xcel/SPS large-load tariff (PUCT **Docket 60332**) | Filed late Sept. **>75 MW**; large loads pay transmission, substation, interconnection and new generation; commercial + credit requirements; third-party-gen option. **No PUCT order or schedule found.** NM filing to follow | https://texaspolitics.com/2026/09/29/xcel-proposes-texas-tariff-to-make-data-centers-pay-grid-costs/ | 2026-09-29 | R | STRUCT (pending). Check the PUCT Interchange directly |
| Wisconsin PSC | **No October decision found.** Latest: We Energies VLC tariff (4/24: ≥100 MW mandatory, 15-yr minimum, capacity-only option removed); Alliant–Meta Beaver Dam 220 MW (5/7) with a standalone large-load tariff ordered | https://www.datacenterknowledge.com/regulations/psc-tightens-data-center-tariff-rules-in-wisconsin | spring 2026 | R | STRUCT (old). UNVERIFIED for any pending Alliant tariff docket |
| **Oracle trucking CNG to data centers** | Bloomberg 10/8: trucked CNG at **Shackelford Co. TX** (OpenAI campus, early construction; **VoltaGrid**). Part of **Abilene** reportedly on trucked gas + mobile generators pending substation/pipeline. Utah site >1 yr (Certarus). Weighing it for Jupiter. ~**4× hub** cost. ORCL −5.5%, BE −8% | https://datacenterdynamics.com/en/news/oracle-trucks-in-gas-to-support-operations-at-utah-and-texas-data-centers-report ; https://investinglive.com/news/oracle-trucks-in-natural-gas-to-keep-ai-data-centres-on-schedule-as-pipelines-lag/ | 2026-10-08 | R-gated | STRUCT (power-supply bottleneck). **Abilene detail rests on one relay: UNVERIFIED** |
| Bloom fuel cells | Belong to **Project Jupiter (NM)**, up to 2.45 GW (April swap from turbines). **No Bloom link to Abilene or Shackelford found** | TechCrunch 9/24 | — | R | correction to the prompt's framing |
| **Lordstown OH data-center ban** | **No October 2026 news found.** History: ban passed 6–0 (Nov 2025), repealed (Dec 2025), 180-day moratorium (Jan 2026, likely expired ~Jul, inference). Developer Bristolville 25 took it to the Ohio Supreme Court (date/outcome not found) | https://www.datacenterdynamics.com/en/news/data-centers-now-banned-in-lordstown-ohio/ ; https://www.wfmj.com/story/53248144/developer-takes-fight-over-lordstown-data-center-to-ohio-supreme-court | 2025-11 → 2026-01 | R | UNVERIFIED for the current status |

---

## 6. Not found / tried (gaps)

- **Volta final pricing or allocation** (the deadline was 10/14 17:00 ET). Bloomberg 10/12 original returned 403.
- CRWV Q3 date; CRWV exact CDS figure; which CRWV note (2031 or 2032) is at 16%.
- ORCL $3.3B lessor guarantee; ORCL 2056 October level; confirmation of the Tencent lease.
- Meta Beignet print after 10/7; Amazon SPV status.
- Data-center-specific BDC marks.
- PJM 10/15–16 operations and whether any data-center backup generation was dispatched.
- PUCT 60332 procedural schedule; Lordstown current status.
- Blocked: cnbc.com, benzinga.com, bloomberg.com (403); CoreWeave IR (JavaScript render).
