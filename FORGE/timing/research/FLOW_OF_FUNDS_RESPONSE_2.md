# The 2007 Selling Sequence: Z.1 Flow of Funds Data, Institutional Lags, and the 2026 Private Credit Mapping
## Executive Summary
Your hypothesis about the 2007 selling sequence was directionally right on insurance and pensions but materially wrong on mutual funds and banks. The Z.1 data reveals that **broker-dealers and money market funds, not mutual funds, were the first major institutional sellers of corporate bonds** — broker-dealers turned net sellers in Q4 2007 at -$115.4B SAAR, while money market funds turned net sellers one quarter earlier in Q3 2007. Critically, **banks were the last large-institutional actor to sell, not arriving until Q2 2008**, a full five quarters after the crisis began. Mutual funds produced their peak selling not in Q3 2007 but in Q4 2008 (-$353.9B SAAR). In 2026, the private credit market appears to be in a simultaneous Stage 1/Stage 2 transition: retail credit vehicle gates and partial fulfillments have already begun, suggesting the system is two to three stages from the bank/pension selling phase that would constitute a systemic event.

***
## Section 1: The Z.1 F.212 Quarterly Flow Table
The Federal Reserve's Z.1 Financial Accounts of the United States, Table F.212, tracks net purchases (positive) and net sales (negative) of corporate and foreign bonds by sector, expressed as seasonally adjusted annual rates (SAAR). The data below is drawn directly from FRED BOGZ1 series for flow data (FA prefix) and approximated from level changes (LM prefix, marked with asterisk) where flow series are not directly accessible.
### Net Purchases of Corporate & Foreign Bonds by Sector ($B SAAR)
| Sector | 2007 Q1 | 2007 Q2 | 2007 Q3 | 2007 Q4 | 2008 Q1 | 2008 Q2 | 2008 Q3 | 2008 Q4 |
|---|---|---|---|---|---|---|---|---|
| **Broker-Dealers** (FA663063005) | +162.4 | +47.4 | +37.4 | **-115.4** | -66.3 | **-334.1** | -114.0 | -255.5 |
| **Money Mkt Funds** (FA633063005) | +103.1 | +165.4 | **-50.7** | -154.6 | +87.5 | -66.8 | **-389.0** | -236.9 |
| **P&C Insurance** (FA513063005) | +15.2 | +32.6 | +14.5 | **-35.6** | -19.6 | -12.2 | +10.1 | -34.8 |
| **Life Insurance** (FA543063005) | +66.8 | +56.5 | +61.3 | **-18.3** | +14.9 | +44.1 | -31.3 | -37.1 |
| **Banks (Com.)** (FA763063005) | +85.4 | +110.1 | **+310.6** | +100.0 | +5.9 | **-23.6** | -127.8 | -107.3 |
| **Mutual Funds** (FA653063005) | +83.6 | +100.0 | +169.1 | -2.0 | +2.9 | +256.9 | -93.1 | **-353.9** |
| **Private Pension** (FA593063005) | +115.0 | +172.8 | +23.9 | +250.4 | **-33.3** | +42.9 | -68.6 | -208.0 |
| **ETFs/Closed-End** (FA583063005) | +197.0 | +261.9 | +99.7 | +196.5 | **-37.9** | +74.9 | -89.9 | -279.9 |
| **Households\*** (LM153063005) | +39.5 | -77.3 | +259.3 | +30.0 | +26.9 | -28.0 | +71.9 | +26.0 |
| **S&L Pension\*** (LM213063003) | +11.1 | -10.3 | +16.7 | +3.2 | -2.5 | -6.8 | -5.3 | -7.5 |
| **Rest of World\*** (LM263063005) | +183.8 | +131.0 | +33.9 | +73.0 | +4.0 | **-27.1** | -308.4 | -59.7 |

*\* Approximate flow derived from QoQ change in levels outstanding. Household series is a Z.1 residual and less behaviorally reliable.*

Key notes on series coverage: The Z.1 does not have a discrete "hedge fund" or "SIV" category. SIV/conduit behavior is captured indirectly through ABS issuers (liability contraction beginning Q1 2008), broker-dealer inventory absorption, and money market fund ABCP run dynamics. Private pension (FA593063005) covers defined benefit and defined contribution plans combined.[^1][^2]

***
## Section 2: The Actual Selling Sequence — Who Sold First and the Lags
### The First-Sell Timeline
| Rank | Sector | First Net-Sell Quarter | Amount (SAAR $B) | Lag from Crisis Origin |
|---|---|---|---|---|
| 1 | Money Market Funds | 2007 Q3 | -$50.7B | 0 (trigger quarter) |
| 2 | Broker-Dealers | 2007 Q4 | -$115.4B | +1 quarter |
| 3 | P&C Insurance | 2007 Q4 | -$35.6B | +1 quarter |
| 4 | Life Insurance | 2007 Q4 | -$18.3B | +1 quarter |
| 5 | ETFs / Closed-End Funds | 2008 Q1 | -$37.9B | +2 quarters |
| 6 | Private Pension | 2008 Q1 | -$33.3B | +2 quarters |
| 7 | Banks (Commercial) | 2008 Q2 | -$23.6B | +3 quarters |
| 8 | Rest of World | 2008 Q2 | -$27.1B | +3 quarters |
| 9 | Mutual Funds (peak) | 2008 Q4 | -$353.9B | +5 quarters |
| 10 | Private Pension (peak) | 2008 Q4 | -$208.0B | +5 quarters |

The zero point is Q3 2007 because that is when money market funds turned net sellers, corresponding to the August 2007 ABCP market seizure. Cheyne Finance, the first SIV forced into wind-down, collapsed in August 2007 when its commercial paper funding dried up and it breached its major capital loss trigger. This caused MMFs holding ABCP to refuse rollovers, forcing them to liquidate corporate bond holdings — precisely the mechanism that shows up in the Z.1 data.[^3][^4]
### The Q3 2007 Anomaly: Banks Were Massive Buyers
The most surprising finding is the bank line: **commercial banks purchased a net +$310.6B SAAR in corporate bonds in Q3 2007** — the same quarter the crisis began. This reflects two dynamics. First, banks were absorbing off-balance-sheet SIV assets that they had provided liquidity backstops to, taking SIV portfolios back onto their balance sheets to avoid reputational damage (Citi took on $49B across five vehicles; HSBC and Standard Chartered followed). Second, broker-dealer subsidiaries of banks were actively market-making and absorbing client sells. Banks did not flip to net sellers until Q2 2008, and this lag is structural, not behavioral: they were the buyer of last resort, funding via repo until repo markets themselves froze after Bear Stearns (March 2008) and then Lehman (September 2008).[^5][^6]
### The Mutual Fund Paradox
Mutual funds produced a net +$169.1B in Q3 2007 — the same quarter the academic literature identifies as the onset of mutual fund corporate bond selling. This apparent contradiction is resolved by cross-sectional heterogeneity documented by Manconi, Massa, and Yasuda (2012): funds with heavy securitized bond exposure sold corporate bonds aggressively while unexposed funds were net buyers. The Z.1 aggregate masked this divergence. The Z.1 aggregate turned net seller only marginally in Q4 2007 (-$2.0B), then swung positive again in Q2 2008 (+$256.9B) before the catastrophic Q4 2008 sell (-$353.9B). The Q2 2008 buying surge reflects funds that were buying distressed corporate paper opportunistically — and got badly wrong.[^7][^8][^9]

***
## Section 3: Gradual vs. Cliff-Like Selling Within Each Sector
### Pattern Classification
**Cliff-like (sudden, one-quarter reversal of large magnitude):**
- **Money Market Funds**: Flipped from +$165.4B to -$50.7B in a single quarter (Q2→Q3 2007), then went -$154.6B the next quarter. The ABCP market freeze was an immediate shock — not gradual.[^10]
- **Broker-Dealers**: Flipped from +$37.4B to -$115.4B in Q3→Q4 2007. Margin constraint tightening was documented as early as July 2007, but the full reversal required the Citi writedown and credit ratings cycle in Q4.[^11][^12]
- **Mutual Funds Q4 2008**: Turned from +$256.9B to -$93.1B to -$353.9B. Post-Lehman cliff.

**Gradual (multi-quarter deterioration):**
- **Insurance (both P&C and Life)**: P&C first turned negative Q4 2007 but oscillated — only consistent selling from Q3 2008 onward. Life Insurance retained corporate bonds through Q1-Q2 2008, selling modestly. The IMF (2009) documented that insurers sold little as long as they remained above minimum capital ratio thresholds. The gradual pattern reflects this: they sold only when capital erosion from equities forced them to.[^13]
- **Banks**: Six-quarter gradual transition from large buyer (+$310.6B Q3 2007) to seller (-$107.3B Q4 2008). Never produced a cliff-like reversal — selling accelerated proportionally with repo market deterioration.
- **Private Pension**: Sold in Q1 2008, bought again in Q2 2008, then heavy selling Q3-Q4 2008. Episodic, not cliff-like, reflecting asset-liability management rebalancing rather than a single trigger.

***
## Section 4: Revisions to the User's 2007 Hypothesis
Your original sequence, with corrections from the Z.1 data:

| Stage | Your Hypothesis | Actual Data | Verdict |
|---|---|---|---|
| **Stage 1** | Hedge funds/SIVs (Q2 2007) | SIVs began asset sales June 2007 ($55.6B by Nov 2007[^14]). Shows in Z.1 as MMF ABCP run and broker-dealer absorption. | ✓ Directionally correct. The timing is Q2-Q3 2007, not Z.1 captured directly. |
| **Stage 2** | Mutual funds (Q3 2007) | Mutual funds were NET BUYERS +$169.1B in Q3 2007 in aggregate. Funds with securitized exposure sold, but offset by others. | ✗ Aggregate Z.1 contradicts this. Academic microdata supports it as a cross-sectional story, not aggregate. Mutual funds peaked in selling Q4 2008. |
| **Stage 3** | Insurance (Q3-Q4 2007) | P&C turned Q4 2007 (-$35.6B). Life held until Q4 2007 (-$18.3B). Sold gradually. | ✓ Correct on timing. Selling was smaller and more gradual than you may have assumed. |
| **Stage 4** | Banks recognized losses/wrote down (Q4 2007) | Banks were BUYERS +$100B in Q4 2007. They absorbed SIV assets. Net selling didn't begin until Q2 2008. | ✗ Wrong by two full quarters. Writedowns (Citigroup) ≠ corporate bond selling. Banks absorbed, not sold, in Q4 2007. |
| **Stage 5** | Pension funds (2008) | Private pension first net sell Q1 2008, heavy Q3-Q4 2008. State/local pensions small sellers from Q2 2007. | ✓ Mostly correct. |

The missing stage in your hypothesis is **broker-dealers** as the first large institutional net seller (Q4 2007, -$115.4B), driven by proprietary book deleveraging and margin constraint tightening in July 2007. Broker-dealers preceded mutual funds by five full quarters in peak selling.[^11]

***
## Section 5: The 2026 Mapping — What You Got Right and What Needs Updating
### Your Proposed Analog Map
| 2007 Actor | Mechanism | 2026 Analog | Assessment |
|---|---|---|---|
| Hedge funds/SIVs | Structured vehicle liquidity loss, ABCP run | Private credit funds (BDCs, evergreen vehicles) | ✓ Correct and already underway |
| Mutual funds | Retail redemptions triggering forced corporate bond sales | Retail credit ETFs (HYG, JNK) + BDC retail | ✓ Partially. Retail BDC redemptions are the cleaner analog; HYG/JNK are public and mark daily (no gate mechanism) |
| Insurance | Regulatory capital and portfolio allocation constraints | PE-controlled insurers (Athene/Apollo, Global Atlantic/KKR, Everlake/Blackstone) | ✓ Correct and the most structurally dangerous — these insurers hold 40% of financial and ABS private placements despite controlling only 14% of general account assets[^15] |
| Banks | Writedowns, capital adequacy constraints | Banks with ~$95B PC commitments | ✓ Correct framing. Fed data confirms $95B in bank exposure to BDCs/PC vehicles at end-2024[^16]. OFR estimates total bank+nonbank exposure to private credit at $410–540B[^17] |
| Pension funds | Late-cycle forced selling, asset-liability management | Not yet identified as a 2026 concern | Still early stage — pensions have de-risked significantly since 2007 |
### What Your 2026 Map Is Missing
**1. The Non-Traded BDC Gate Mechanism is the 2007 SIV analog, not the mutual fund analog.** The structural match is: SIVs/ABCP conduits in 2007 (issued short-term paper to fund long-term assets, broke when ABCP refused) ≈ non-traded BDC evergreen funds in 2026 (offered quarterly liquidity to retail investors who believed they owned an illiquid asset class). Both featured an asset-liability mismatch embedded in a vehicle most investors didn't understand. The gates now being applied (5% quarterly limits) are the exact analog of SIVs accessing bank liquidity backstops — temporary containment that buys time but does not eliminate the underlying mismatch.

**2. Software sector concentration has no 2007 analog at this scale.** Software represents ~26% of BDC portfolios and ~19% of private credit CLOs. The 2007 crisis had concentrated exposure in residential subprime; 2026 has concentrated exposure in leveraged software loans facing AI-driven revenue disruption. This is a credit quality shock layered on top of a structural liquidity mismatch.[^18]

**3. PE-insurance interlocking creates a new contagion channel.** In 2007, insurance companies sold corporate bonds primarily because of equity losses (they held very different assets from the subprime pools). In 2026, PE-owned insurers like Athene, Global Atlantic, and Everlake have *already allocated* aggressively into the private credit they also manage, creating circularity. If private credit defaults rise, the insurer's general account deteriorates, triggering regulatory scrutiny — the Treasury meeting with insurance regulators on March 30, 2026 is the first official acknowledgment of this channel. The Treasury is focused on four specific issues: fund-level leverage, private credit ratings consistency, offshore reinsurance, and investment liquidity.[^19][^20]

**4. Bank credit lines to PC funds are a 2007 liquidity-backstop analog.** Just as banks provided liquidity lines to SIVs in 2007 and ended up absorbing those portfolios, banks have provided $123B in committed exposures to private credit obligors (Y-14 data) plus subscription credit lines and NAV facilities. If PC funds continue gating, banks face drawdown risk on these committed lines.[^17]

***
## Section 6: Where 2026 Is in the 2007 Sequence
### Stage-by-Stage Assessment (March 2026)
**Stage 1 — Structured Vehicle Distress: IN PROGRESS**

The BDC/evergreen fund gate cascade is accelerating. Blue Owl permanently halted redemptions at one retail fund in February 2026. Apollo gated at 5% against 11.2% redemption requests (>$1.5B) in Q1 2026. Ares received 11.6% redemption requests, also at the 5% gate. Blackstone, Morgan Stanley, and BlackRock all saw record redemption requests. Goldman Sachs projects $50–70B in net retail outflows from private credit evergreen vehicles in 2026, likely extending into 2027. New commitments to non-traded BDCs declined 40% month-on-month in January 2026.[^21][^22][^23][^24][^25][^26]

The Moody's downgrade of FS KKR Capital Corp (BDC) to junk on March 24, 2026 is significant: it is the first major BDC rating agency downgrade of the cycle, analogous to the first CDO tranche downgrades in summer 2007 that broke the AAA rating fiction.[^27]

Barclays' withdrawal from asset-based lending to smaller borrowers (March 25, 2026) following losses from Market Financial Solutions and Tricolor Holdings confirms that the contagion has moved from private credit fund NAV erosion into bank credit provider behavior — exactly the mechanism by which Q3 2007's ABCP freeze turned into Q4 2007 broker-dealer deleveraging.[^28][^29]

**Stage 2 — Retail Credit Vehicle Redemptions: IN PROGRESS (Early)**

The retail BDC redemption cascade is structurally the mutual fund / ETF analog. However, the Z.1 data from 2007 shows that mutual fund aggregate corporate bond buying *increased* in Q3 2007 (+$169B) even as a subset of funds with securitized exposure was selling. The 2026 equivalent: while gating vehicles are seeing outflows, institutions and qualified buyers may be purchasing the most liquid PC assets at widened spreads. The aggregate Z.1 net purchase figure for corporate bonds may not turn negative even as the private credit subset deteriorates. The signal to watch is not HYG/JNK flows (those are publicly marked and will reprice immediately) but BDC NAV erosion and non-traded fund redemption fulfillment rates.

**Stage 3 — Insurance Sector: EARLY TRANSITION**

The Treasury convening meeting with insurance regulators (announced March 30, 2026) is the regulatory equivalent of the moment in 2007 when the OTS and OCC began questioning bank SIV exposure. PE-linked insurers committed $90B to PC funds and hold substantial related-party exposures: Blackstone's Everlake at 35% related-party assets, Brookfield's American National at 30%, KKR's Global Atlantic at 22%, Apollo's Athene at 12–18%. These are not selling yet, but the regulatory pressure is mounting. The critical threshold is minimum statutory capital ratios — insurers historically do not sell until that floor is approached.[^7][^13][^30][^20][^31]

**Stage 4 — Bank Recognizing Losses: VERY EARLY**

JPMorgan remarking loans to PC funds downward (March 2026) is the first visible bank-level credit action. Barclays pulling back from deals and raising pricing is a credit tightening, not yet forced selling. The 2007 analog is mid-Q3 2007: banks are absorbing stress, not yet sellers. The Z.1 2007 data showed banks as *buyers* for five more quarters after the crisis started. This is the most important stage to watch: bank net selling of corporate credit would be the clearest systemic signal.[^32]

**Stage 5 — Pension Funds: NOT YET**

No evidence of pension reallocation from private credit. Pension funds typically follow the full cycle.
### The 2026 Selling Sequence (Current Estimate)
| Stage | 2007 Analog | 2026 Actor | Status | Z.1 Signal Timing |
|---|---|---|---|---|
| 1 | SIV/conduit breakdown | BDC gates, PIK loans, Tricolor/First Brands defaults | **Active** | Now (Q1 2026) |
| 2 | MMF ABCP run | Retail BDC/evergreen redemption cascade | **Active (early)** | Q1–Q2 2026 |
| 3 | Broker-dealer deleveraging | Bank credit tightening (JPM, Barclays) | **Early** | Q2–Q3 2026 |
| 4 | Insurance capital constraints | PE-insurance review, Treasury meetings | **Very early** | Q3–Q4 2026 |
| 5 | Bank loss recognition | Banks remarking PC loan portfolios | **Very early** | Q3 2026 onward |
| 6 | Pension selling | Not visible | **Not yet** | 2027+ |

The 2007 data suggests a **5-quarter transmission timeline** from the first MMF/structured vehicle selling to peak pension selling. If Q1 2026 is approximately equivalent to Q3 2007, peak institutional selling (the pension + bank mutual selling that characterized Q4 2008) would be estimated for late 2027 — assuming the rate of progression is similar.

***
## Section 7: The 2026 "Meredith Whitney" — Who Has Made the Systemic Call?
Meredith Whitney's October 31, 2007 Citi downgrade was a single precise quantitative call that broke institutional consensus and triggered cascading institutional selling. Her memo had four characteristics: (1) a specific capital shortfall estimate ($30B), (2) a specific required action (dividend cut or asset sale), (3) a specific stock downgrade, and (4) timing that preceded wider institutional recognition.[^33][^34][^35]

The 2026 environment has multiple analysts making bearish private credit calls, but none has produced a single moment equivalent to Whitney's Citi downgrade — partly because there is no single public company equivalent (private credit funds don't mark to market daily) and partly because the stress is distributed across hundreds of funds.

**Most Whitney-Equivalent Call: Jeffrey Gundlach (DoubleLine Capital)**

Gundlach first made the systemic call in November 2025, warning that private credit "has the same trappings as subprime mortgage repackaging had back in 2006" and introducing the "100 or zero" pricing thesis — that private credit assets have only two realistic valuations rather than continuous market pricing. He repeated the warning in March 2026. Structurally, Gundlach's call parallels Whitney's: he is making a specific valuation and transparency argument (marks are meaningless), a specific behavioral prediction (when investors try to exit simultaneously, there is no orderly market), and he has broken from Wall Street consensus. Unlike Whitney, his call names a sector rather than a single company.[^36][^37][^38]

**The Quantitative Call: Morgan Stanley, Joyce Jiang (March 16, 2026)**

Jiang's team published the most specific quantitative note: direct lending default rates will reach 8%, driven by AI disruption to the software sector (26% of BDC portfolios). This is a concrete estimate with a mechanism. Morgan Stanley's note is the 2026 analog to the October 2007 consensus-shifting reports that followed Whitney — it is not the first bearish call, but it carries institutional imprimatur and specific estimates. The significant caveat: Jiang explicitly argues the risk is "significant but not systemic."[^39][^40][^41]

**The Structural Warning: OFR Brief 26-02 (March 12, 2026)**

The Office of Financial Research's brief quantifying $410–540B in total counterparty exposures between banks and private credit entities represents the equivalent of the 2007 Fed/OCC examinations of SIV exposure. It is regulatory, not market-facing, but it establishes the size of the channel. An OFR warning that explicitly uses the word "systemic" would be the bureaucratic-sector equivalent of Whitney's downgrade.[^17][^42]

**UBS (February 2026) and Whalen Global Advisors (March 2026)**

UBS's 15% default scenario under aggressive AI disruption and Christopher Whalen's bank-exposure report (with the quantitative claim that UBS's figure is "roughly three times the peak delinquency rates of bank loans during the 2008 financial crisis") are the dissenters who lack the market platform to trigger a cascade.[^27][^43]
### What Would Trigger a Whitney Moment in 2026
The structural requirement is a public, specific, quantifiable failure at a single identifiable node that forces other institutions to recognize similar exposures. In 2007, Citi's capital shortfall was that node. In 2026, the candidates are:

1. **A major BDC NAV mark that exposes widespread valuation fiction** — e.g., FS KKR (already Moody's-downgraded to junk) reporting a large asset write-off that implies peer portfolios are similarly mispriced.
2. **A PE-insurance general account impairment** — e.g., Athene, Global Atlantic, or Everlake disclosing that their related-party private credit holdings are impaired, forcing NAIC intervention.
3. **A bank announcing material losses on its PC fund credit lines** — which would immediately cause all banks to reprice and pull subscription lines, triggering a broad gating cascade.
4. **A public PC CLO downgrade cascade** — similar to the CDO downgrade cascade of summer 2007. Private credit CLOs have 19% software exposure; a wave of software defaults would be publicly visible through CLO note downgrades.[^18]

***
## Methodological Note on the Z.1 Data
Several caveats apply to interpreting this table. First, the household sector in Z.1 is a **residual** — computed as the difference between total net issuance and all measurable sector purchases. Negative household flows partly reflect measurement error and reclassification, not necessarily behavioral selling. Second, the flow series (FA prefix) represent SAAR-annualized rates; a single quarter print of -$150B means -$37.5B in the actual quarter. Third, hedge funds and SIVs have **no direct Z.1 sector** — their behavior is distributed across broker-dealers (who absorbed and then sold their assets), ABS issuers (whose liability contraction from 2008 Q1 onward reflects CDO/CLO unwind), and the "funding corporations" category. Fourth, the state and local government pension series derived from level changes is approximated and small in magnitude; do not over-interpret it. Fifth, the "mutual funds" series in Z.1 captures open-end bond funds but does not separately identify high-yield vs. investment-grade allocations; the aggregate obscures the heterogeneous behavior documented in the Manconi/Massa/Yasuda (2012) academic study.[^9]

---

## References

1. [[PDF] Flow of Funds Accounts of the United States - Federal Reserve Board](https://www.federalreserve.gov/releases/z1/20081211/z1.pdf) - Nonfinancial business debt rose at an annual rate of 3 percent in the third quarter, 2¾ percentage p...

2. [[PDF] Flow of Funds Accounts of the United States - Federal Reserve](https://www.federalreserve.gov/releases/z1/20090312/z1r-1.pdf) - In 2008, federal government debt rose more than 24 percent, after a 5 percent increase in 2007. At t...

3. [End of an era as Cheyne SIV finally liquidated - GlobalCapital](https://www.globalcapital.com/securitization/article/28mts1wjsrfaw4n5ov9xc/clos-cdos/end-of-an-era-as-cheyne-siv-finally-liquidated) - Cheyne Capital’s structured investment vehicle (SIV) has finally been liquidated, marking another po...

4. [[PDF] SUMMER 2007: DISRUPTIONS IN FUNDING](https://fcic-static.law.stanford.edu/cdn_media/fcic-reports/fcic_final_report_chapter13.pdf)

5. [Almost all SIV assets now sold off, Fitch says - Risk.net](https://www.risk.net/derivatives/structured-products/1517514/almost-all-siv-assets-now-sold-fitch-says) - The structured investment vehicles (SIVs) at the heart of the credit crisis have now disposed of 95%...

6. [The Fed - Primary Dealers' Behavior during the 2007-08 Crisis](https://www.federalreserve.gov/econres/notes/feds-notes/primary-dealers-behavior-during-the-2007-08-crisis-part-I-repo-runs-20170622.html) - The Federal Reserve Board of Governors in Washington DC.

7. [The Role of Institutional Investors in Propagating the Crisis of 2007-2008](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1454831) - Using a novel data set of institutional investors’ bond holdings, we study a transmission mechanism ...

8. [The Behavior of Intoxicated Investors: The role of institutional investors in propagating the crisis of 2007-2008](https://www.nber.org/papers/w16191) - Founded in 1920, the NBER is a private, non-profit, non-partisan organization dedicated to conductin...

9. [The role of institutional investors in propagating the crisis of 2007–2008](https://econpapers.repec.org/article/eeejfinec/v_3a104_3ay_3a2012_3ai_3a3_3ap_3a491-518.htm) - By Alberto Manconi, Massimo Massa and Ayako Yasuda; Abstract: Using novel data on investors' bond po...

10. [[PDF] Maintaining Stability in a Changing Financial System](https://www.kansascityfed.org/Jackson%20Hole/documents/3164/2008-Gorton031209.pdf) - the unique design of subprime mortgages resulted in unique structures for their securitization, re- ...

11. [Market Making and Proprietary Trading in the US Corporate Bond ...](https://publications.banque-france.fr/en/market-making-and-proprietary-trading-us-corporate-bond-market) - I study broker-dealers' trading activity in the US corporate bond market. I find evidence of broker-...

12. [Market Making and Proprietary Trading in the US Corporate Bond Market](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3390044) - I study dealers' trading activity in the US corporate bond market.Dealers are market makers half of ...

13. [[PDF] How the Financial Crisis Affects Pensions and Insurance and Why ...](https://www.imf.org/external/pubs/ft/wp/2009/wp09151.pdf) - Abstract. This paper discusses the key sources of vulnerabilities for pension plans and insurance co...

14. [[PDF] Moody's Update on Structured Investment Vehicles](https://fcic-static.law.stanford.edu/cdn_media/fcic-docs/2008-01-16%20Moody's%20Update%20on%20Structured%20Investment%20Vehicles%20(Moody's%20Special%20Report).pdf)

15. [Insurers Boost Private Credit Allocations - Debexpert](https://www.debexpert.com/blog/insurers-boost-private-credit-allocations) - Insurance companies are increasingly investing in private credit to achieve higher yields and better...

16. [US banks support rivals' boom with $95 billion in private debt](https://www.linkedin.com/posts/hugh-suhr_bank-lending-to-private-credit-funds-swells-activity-7333910099087785984-nQiM) - US banks, typically in fierce competition with private credit firms, are enabling their rivals' boom...

17. [[PDF] OFR Brief: Measuring Counterparty Exposures to Private Credit](https://www.financialresearch.gov/briefs/files/OFRBrief-26-02-measuring-counterparty-exposures-private-credit.pdf) - We estimate that total bank and nonbank lending to private credit entities, including. BDCs, ranges ...

18. [Private credit default rates to reach 8%, says Morgan Stanley](https://www.cnbctv18.com/market/private-credit-default-rates-to-reach-8-says-morgan-stanley-ws-l-19869769.htm) - Morgan Stanley predicts default rates in direct lending will rise to 8% due to AI disruption in soft...

19. [US Treasury Reportedly to Meet with Insurance Regulators to ...](http://www.aastocks.com/en/stocks/news/aafn-con/NOW.1514036/latest-news/AAFN) - The first meeting could be announced as early as Wednesday (1st). The report states that the parties...

20. [Exclusive: US Treasury to consult with insurance regulators on ...](https://www.reuters.com/business/finance/us-treasury-consult-with-insurance-regulators-private-credit-lenders-sources-say-2026-03-30/) - US Treasury plans meetings with insurance regulators, seeks details on leverage, liquidity · Consult...

21. [Private Credit Concerns in Context](https://www.youtube.com/watch?v=pU3jPw2CyWo) - Goldman Sachs’ Alex Blostein and Vivek Bantwal discuss the market sentiment, fundamentals, and the o...

22. [Retail Outflows in Private Credit Funds to Continue - Markets Media](https://www.marketsmedia.com/retail-outflows-in-private-credit-funds-to-last-until-2027/) - Goldman Sachs expects funds in to see net outflows through 2026 and likely 2027.

23. [Apollo Is Latest Private Credit Firm to Limit Redemptions](https://www.businessinsider.com/apollo-private-credit-firm-gate-redemptions-2026-3) - Apollo's private credit fund saw investors request to redeem 11.2% of outstanding shares. The firm g...

24. [Private credit funds recalibrate retail channel after Blue Owl gating](https://pe-insights.com/private-credit-funds-recalibrate-retail-channel-after-blue-owl-gating/) - The fund reported $2.1bn in redemptions in the fourth quarter. Apollo Global Management's $25.1bn Ap...

25. [Private credit stocks slide after Blue Owl halts redemptions at fund](https://x.com/_soniashenoy/status/2024695696264229096) - Financial times reports that US based asset manager Blue Owl has permanently restricted investor red...

26. [Ares Q1 2026 Redemptions Alarm Investors | Mark J. Higgins, CFA ...](https://www.linkedin.com/posts/markhiggins_semiliquid-privatemarkets-privatecredit-activity-7442225073865842689-HPbt) - “In mid-to-late February 2026, Saba—working alongside Cox Capital Partners—moved to launch tender of...

27. [Private Credit Warning Signs: a Timeline of What's Spooked Markets](https://www.businessinsider.com/blackstone-private-credit-warning-signs-financial-crisis-risks-2026-3) - The private credit sector has drawn more scrutiny from markets in recent months as firms get hit wit...

28. [Barclays pulls back on asset-based lending after MFS, Tricolor](https://www.businesstimes.com.sg/companies-markets/banking-finance/barclays-pulls-back-asset-based-lending-after-mfs-tricolor) - [LONDON] Barclays is scaling back its asset-based lending to smaller borrowers, according to people ...

29. [Barclays Pulls Back on Asset-Based Loans After MFS, Tricolor](https://www.bloomberg.com/news/articles/2026-03-25/barclays-pulls-back-on-asset-based-lending-after-mfs-tricolor) - Barclays Plc is scaling back its asset-based lending to smaller borrowers after facing losses from t...

30. [Insurers Have Promised Private Credit Funds $90B](https://www.thinkadvisor.com/2026/03/18/insurers-have-promised-private-credit-funds-90b/) - Treasury research office analysts wonder what the promises would mean in a long market downturn.

31. [Apollo's Athene targets rivals in insurer asset debate](https://www.insurancebusinessmag.com/us/news/breaking-news/apollos-athene-targets-rivals-in-insurer-asset-debate-546541.aspx) - The filing coincided with the conclusion of NAIC summer meeting, where state regulators scrutinized ...

32. [Private credit strains ripple through Wall Street as investors grow wary](https://www.reuters.com/business/finance/private-credit-strains-ripple-through-wall-street-investors-grow-wary-2026-03-24/) - Investors have pulled billions of dollars from some of the biggest private-credit funds in the first...

33. [Fierce Female Analyst Takes on Citi - The Glass Hammer](https://theglasshammer.com/2007/11/fierce-female-analyst-takes-on-citi/) - Whitney downgraded Citi's stock to “market underperform” status, equivalent to a recommendation to s...

34. [The Analyst Who Rocked Citi - Bloomberg](https://www.bloomberg.com/news/articles/2007-11-26/the-analyst-who-rocked-citibusinessweek-business-news-stock-market-and-financial-advice) - Whitney began work on the report in early October, after Citi reported a dramatic decline in earning...

35. [[PDF] Citigroup - ny times](https://graphics7.nytimes.com/images/blogs/dealbook/Citi_report_CIBC.pdf) - Meredith.Whitney@us.cibc.com. Carla Krawiec, CFA. 1 (212) 667-4527 ... Downgrading Stock Due to Capi...

36. ['Bond King' Jeffrey Gundlach warns of the next financial crisis - Fortune](https://fortune.com/2025/11/18/jeffrey-gundlach-bond-king-next-financial-crisis-private-credit-subprime-mortgage/) - Gundlach illustrated the fragility of this pricing system by noting that private assets essentially ...

37. [Jeffrey Gundlach says it's a 'going nowhere' market, warns of private ...](https://www.cnbc.com/2026/03/23/jeffrey-gundlach-says-its-a-going-nowhere-market-warns-of-private-credit-strains.html) - Jeffrey Gundlach says it's a 'going nowhere' market, warns of private credit strains. Published Mon,...

38. [Jeffrey Gundlach: Private Credit Is An Unmitigated Disaster, And It's ...](https://www.youtube.com/watch?v=d8sPQom4cnc) - ... 2026. Gundlach makes the case that we are living through a ... 100% of their equity exposure out...

39. [Private Credit Default Rates to Reach 8%, Morgan Stanley Says](https://www.bloomberg.com/news/articles/2026-03-16/private-credit-default-rates-to-reach-8-morgan-stanley-says) - Default rates in direct lending will climb to 8% as advances in artificial intelligence disrupt the ...

40. [Morgan Stanley Sees Private Credit Default Rates Reaching 8% (2)](https://news.bloomberglaw.com/banking-law/morgan-stanley-sees-private-credit-default-rates-reaching-8-2) - Default rates in direct lending will climb to 8% as advances in artificial intelligence continually ...

41. [Private credit default rates will climb, Morgan Stanley warns](https://www.cfobrew.com/stories/2026/03/18/private-credit-default-rates-will-climb-morgan-stanley-warns) - “Overall, we expect the direct lending default rates to reach 8%, approaching Covid peak levels.” Th...

42. [OFR Brief: Private Credit Exposures to Banks | Banking &a...](https://changeflow.com/govping/banking-finance/us-fed-2026-03-13-113) - The Office of Financial Research (OFR) published a brief on March 12, 2026, analyzing counterparty e...

43. [Banks Quietly Loaded Up on Private Credit Risk. The Cycle Is Now ...](https://www.prnewswire.com/news-releases/banks-quietly-loaded-up-on-private-credit-risk-the-cycle-is-now-turning-302711947.html) - UBS believes defaults in private credit could reach 15% roughly three times the peak delinquency rat...

