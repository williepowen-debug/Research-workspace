# The 2026 LIBOR-OIS Equivalent: Counterparty Risk Dashboard

*As of March 30, 2026 — Quarter-End / Japan Fiscal Year-End*

***

## Executive Summary

LIBOR-OIS worked because LIBOR was unsecured interbank lending and OIS was risk-free overnight swap — the spread isolated pure counterparty credit risk. SOFR replaced LIBOR in 2023, but SOFR is *secured* (collateralized by Treasuries), so a direct SOFR-OIS equivalent fundamentally cannot capture the same signal. The modern counterparty risk toolkit is therefore necessarily multi-instrument. The best single replacement is the **SOFR-IORB spread** (secured overnight rate vs. the Fed's risk-free reserve rate), followed closely by **FRA-OIS** for forward-looking credit risk, and **USD/JPY cross-currency basis** for dollar-funding stress with a global dimension. Entering March 31 quarter-end — which is *simultaneously* Japan's fiscal year-end — all three deserve elevated monitoring. The SOFR-IORB spread already hit a 5-year wide of +32bps on October 31, 2025; the SRF used a record $74.6B on December 31, 2025; and USD/JPY has just broken the 160 intervention threshold with the strongest MoF rhetoric in years.

***

## 1. Why LIBOR-OIS Can't Be Directly Replicated

The power of LIBOR-OIS as a counterparty risk barometer rested on a structural asymmetry:[^1][^2]

- **LIBOR**: Unsecured interbank lending (3-month), carrying both credit risk and liquidity risk of the lending bank
- **OIS (Overnight Indexed Swap)**: Contractually linked to the overnight policy rate, minimal counterparty exposure, effectively risk-free

The spread therefore measured *how much extra banks charged each other for the unsecured credit risk of a 90-day interbank loan*. Before the 2007–08 crisis it sat at ~10bps. It spiked to ~50bps intraday on August 9, 2007 (BNP Paribas freezes funds), climbed to 108bps by December 2007 (UBS/Lehman write-downs), hit 83bps around Bear Stearns in March 2008, and reached 364–365bps in October 2008 after Lehman's collapse.[^2][^3][^4][^1]

SOFR, by design, is *secured* — it measures overnight repo backed by U.S. Treasuries. A spike in SOFR means collateral is abundant but *cash* is scarce or banks are unwilling to lend balance sheet. It cannot, by itself, distinguish a counterparty credit event from a pure liquidity/balance-sheet constraint event. The post-LIBOR environment therefore requires triangulating across several instruments to reconstruct what LIBOR-OIS once encoded in a single number.[^5][^6]

***

## 2. Ranked Replacements for LIBOR-OIS

### Tier 1: Best Direct Equivalents

#1 — SOFR vs. IORB Spread *(Primary Liquidity/Counterparty Stress Signal)*

The most actionable single indicator in the post-LIBOR world. IORB is the Fed's administered floor — the rate banks earn risk-free by simply parking reserves at the Fed. SOFR is the market rate for secured overnight borrowing. In a fully abundant-reserves regime, SOFR should trade *at or slightly below* IORB because no bank would pay more to borrow than they can earn by leaving cash at the Fed.[^7][^8][^9]

When SOFR rises above IORB, it reveals two things: (1) the reserve distribution has become unequal — cash is concentrated in a few G-SIBs who refuse to lend it out even when profitable, and (2) repo borrowers cannot access the banking system even with Treasuries as collateral, forcing them to pay above the Fed floor. The Fed's own research identifies this as the primary early warning of reserve scarcity.[^7]

On October 31, 2025, SOFR stood at 4.22% against an IORB of 3.90% — a +32bps spread, the widest since March 2020. The SRF was simultaneously tapped for $50.35 billion. As of March 27–30, 2026, SOFR (3.63%) is back slightly *below* IORB (3.65%) — system is currently within normal, but a quarter-end/FY-end surge tomorrow is the immediate watch point.[^10][^11][^12][^13][^14][^15][^16]

*Critical distinction*: When SOFR-IORB inverts positively (SOFR > IORB), it is the secured-market analog of the LIBOR-OIS spike — not a pure credit-risk signal, but a reserve-scarcity/intermediation-unwillingness signal that precedes and accompanies counterparty stress.

***

#2 — FRA-OIS Spread *(Forward-Looking Interbank Credit Risk)*

The FRA-OIS spread (3-month Forward Rate Agreement minus OIS rate) was explicitly described as "the modern proxy for risks in the banking sector" in academic literature. It differs from SOFR-IORB by being *forward-looking* — it embeds market expectations of what interbank credit risk will look like three months out, not just tonight. Like LIBOR-OIS, it compares an unsecured forward rate (the FRA) to a rate with minimal counterparty exposure (the OIS).[^17][^18]

Historically: near 0 in calm conditions, ~60bps during the 2011 European debt crisis, ~60–70bps in early COVID (March 2020), and approaching 170bps at the November 2008 post-Lehman peak. Currently, with 3-month SOFR OIS around 3.69–3.71% against EFFR of 3.64%, the implied FRA-OIS spread is in the 5–10bps range — normal. This is the indicator to watch for any *credit* component emerging, as distinct from the pure liquidity signal from SOFR-IORB.[^19][^20][^17]

***

#3 — Bank CDS Spreads *(Direct Counterparty Credit Pricing)*

CDS spreads on the major G-SIBs (JPMorgan, Citi, BAC, GS, Morgan Stanley, Wells Fargo) are analytically the cleanest equivalent to LIBOR-OIS because they *directly* price the probability of bank default. During the 2007–09 crisis, bank CDS spreads were co-plotted with LIBOR-OIS as the two key stress indicators and moved in near-lockstep. Yale's analysis of GFC phases uses exactly this pair as the stress dashboard.[^21]

The structural advantage of CDS over SOFR-based spreads: CDS will spike even if reserves are abundant, because they measure *credit* risk not *liquidity* risk. In a 2023-SVB-style scenario, you'd see CDS spreads blow out while SOFR-IORB remained calm. In a 2019-style repo crisis, SOFR-IORB would spike while CDS stayed flat. When *both* move together, you are in LIBOR-OIS territory — genuine systemic counterparty fear.

***

### Tier 2: Context-Specific Indicators

#4 — USD/JPY Cross-Currency Basis Swap *(Global Dollar Funding Stress)*

Cross-currency basis swaps measure the premium or discount at which non-dollar entities (Japanese banks, European banks) can swap their domestic currency for dollars in the FX swap market. A *more negative* basis means dollar funding is scarce globally — the foreign entity must pay an above-market rate to access dollars, an exact analog to LIBOR-OIS's bank-distrust signal but in the offshore dollar market.[^22][^23]

Japanese banks and life insurers are among the world's largest dollar borrowers, hedging massive USD-denominated asset portfolios. The 3-month USD/JPY basis hit -63.75bps in October 2022 (the widest since March 2020). With Japan's FY-end tomorrow (March 31, 2026), USD/JPY having broken 160, a $550B US-Japan investment deal expected to drive the 5–10y basis *wider* (more negative) throughout 2026, and the Bank of Japan likely hiking in April to 1.00%, the structural backdrop is the most JPY-basis-stressful since 2022.[^23][^24][^25][^26][^22]

**Critically**: MUFG's March 30, 2026 note characterizes the US-Japan swap spread rise as "more modest this time" versus prior episodes, suggesting the basis has not blown out yet — but tomorrow's quarter-end/FY-end is the highest-risk day of the calendar for this measure.[^24]

***

#5 — CP Spread vs. T-Bills *(Commercial Paper / Short-Term Credit Freeze Indicator)*

The 3-month AA Financial Commercial Paper rate minus the 3-month T-bill rate (or alternatively, CP minus EFFR, the CPFF series) is the old "TED-adjacent" measure that revealed when the commercial paper market was seizing. In 2008, the CP market froze entirely — Lehman's collapse made CP investors refuse to roll even high-grade paper, forcing the Fed's Commercial Paper Funding Facility. Currently, with 3-month nonfinancial CP at 3.68–3.75% and EFFR at 3.64%, the spread is ~4–10bps — benign. This is a *lagging* indicator in the LIBOR-OIS timeline; it blows out after the interbank market has already seized.[^27][^28][^20][^6]

***

#6 — SOFR vs. Fed Funds (EFFR) Spread *(Reserve Distribution Imbalance)*

SOFR is secured (Treasury-backed), EFFR is unsecured (pure interbank). In theory, SOFR should be *lower* than EFFR because it carries no credit risk. When SOFR trades *above* EFFR, it signals that collateral (Treasuries) is abundant but cash/balance-sheet capacity is the scarce factor — a reserve distribution problem. On October 27, 2025, SOFR was at 4.27% while EFFR was at 4.12% — SOFR above EFFR — signaling exactly this. As of late March 2026, SOFR (3.63%) and EFFR (3.64%) are nearly identical, back to normal. This spread is less precise than SOFR-IORB because the Fed Funds market itself has become thin (daily volume dwarfed by repo market).[^29][^12][^20][^30][^19]

***

## 3. The Stress Threshold Table

| Indicator | Current Level (Mar 30) | Watch Level | Alarm Level | 2007–08 Peak |
|-----------|----------------------|-------------|-------------|--------------|
| **SOFR-IORB spread** | -2bps (normal)[^12][^15] | +10bps | +25bps | N/A (metric didn't exist; IOER floor introduced Oct 2008) |
| **FRA-OIS (3M)** | ~5–10bps[^19][^20] | 25bps | 50bps | ~170bps (Nov 2008)[^17] |
| **Bank CDS (G-SIB avg)** | ~70–90bps (est., IG tight)[^31] | 150bps | 300bps | 400–500bps (Sep–Oct 2008)[^21] |
| **USD/JPY 3M basis** | Est. -10 to -20bps | -40bps | -60bps | -63.75bps (Oct 2022)[^22]; worse in 2008 |
| **CP-EFFR spread (3M AA Fin.)** | ~5–10bps[^20] | 40bps | 100bps | CP market froze; CPFF created |
| **SOFR-EFFR spread** | ~-1bps[^12][^20] | +10bps | +25bps | N/A |
| **SRF usage (quarter-end)** | $0 base; $74.6B Dec-31 record[^32][^33] | >$50B | >$100B or mid-month spike | N/A (facility created 2021) |
| **HY OAS** | 342bps[^34] | 450bps | 600bps | ~1,800bps (Dec 2008) |
| **VIX** | ~30+ (conflict)[^24] | 35 | 45 | 80+ (Nov 2008) |

*Note: "Alarm" levels are approximate thresholds where historical data shows market functioning became impaired. Bank CDS and FRA-OIS current levels are estimates based on IG credit tightness and money market rate data; exact real-time CDS quotes require Bloomberg/Markit.*

***

## 4. The BNP Paribas Moment in 2026: What's the Equivalent Trigger?

BNP Paribas on August 9, 2007 was significant because it was the first *named, credible institution* suspending normal operations due to an inability to value assets — it shattered the assumption that major banks always knew what their assets were worth. LIBOR-OIS jumped from 10bps to 50bps that day and never normalized because the *credibility* of the interbank market had broken.

The 2026 equivalent trigger is most likely one of the following scenarios:

**Most Probable: Private Credit Mark-Down Cascade**
Morgan Stanley's BDC (NHPIF) already hit its 5% redemption cap in early 2026. JPMorgan has begun marking down software loans used as collateral by private credit funds, reducing their borrowing capacity. Life/annuity insurers now hold an estimated $1.8 trillion in private credit — 46% of total debt holdings, a record. The NAIC is actively scrutinizing RBC treatment of private credit, CLOs, and structured products. The "BNP Paribas moment" here would be a major insurer or private credit BDC being forced to disclose it cannot mark assets at par, triggering forced redemptions, margin calls from bank lenders, and a sudden demand for short-term dollar liquidity — exactly the dynamic that would show up first in the SOFR-IORB spread and SRF usage.[^35][^36][^37][^38]

**High Risk (Tomorrow Specifically): SRF Spike + FX Intervention Failure**
March 31 is simultaneously U.S. quarter-end and Japan's fiscal year-end. Japanese banks and institutional investors face massive repatriation pressures to rebalance balance sheets. USD/JPY broke 160 on March 28/30, 2026, triggering the strongest MoF rhetoric in years — Vice Finance Minister Mimura stated "decisive action may soon be necessary". If SRF usage tomorrow materially exceeds the $74.6B December 31 record, and USD/JPY continues through 160 despite intervention threats, the cross-currency basis would be the first indicator to spike — effectively a 2026 "fire drill" LIBOR-OIS analog in the FX funding market.[^39][^25][^24]

**Medium-Term: Bank Reserve Scarcity Event (2019 Analog)**
Reserves have already hit $2.8 trillion — a 4-year low, concentrated in G-SIBs. The Fed's own research shows the system is close to the threshold where repo rates become acutely sensitive to balance-sheet demand. The FOMC's December 2025 minutes explicitly flagged repo rate volatility as a reserve-scarcity warning. The September 2019 repo crisis showed how quickly this can accelerate: SOFR spiked ~300bps in a single day in Sept 2019 when reserves hit a similar trough. A surprise large Treasury coupon settlement hitting simultaneously with quarter-end balance-sheet compression could recreate that dynamic.[^11][^16][^39][^7]

**Idiosyncratic / Black Swan: G-SIB-Specific CDS Event**
A single major bank announcing unexpected losses (real estate, private credit, leveraged finance) would show up first in that bank's CDS spread, then spread to peers, then to FRA-OIS, and finally to SOFR-IORB as counterparties pull overnight funding. This is the cleanest "counterparty risk" path — the one where bank CDS is the leading indicator, not SOFR-IORB.

***

## 5. Normal Plumbing vs. Counterparty Risk Being Priced

The critical distinction is whether stress is *anticipated and structured* (plumbing) or *unantic­ipated and spreading* (systemic):

**Normal Plumbing (quarter-end / year-end)**
- SRF usage spikes to $50–75B, then drops to zero in 1–2 days[^40][^32]
- SOFR spikes 15–25bps on quarter-end date, reverts immediately[^39]
- Cross-currency basis widens 10–20bps at Japan FY-end, normalizes post-April
- VIX elevated due to geopolitical risk (oil, Middle East) but stable or declining trend
- HY OAS widening is gradual and driven by macro, not abrupt credit event

**Counterparty Risk Being Priced**
- SOFR-IORB spread stays elevated for >3–5 days post quarter-end[^9][^7]
- SRF usage spikes mid-month (not just at period-end) — the October 2025 $15B mid-month draw was explicitly flagged as unusual[^41]
- FRA-OIS begins to move higher (forward credit premium being demanded)
- Bank CDS spreads widen *faster* than HY OAS (institution-specific fear vs. macro credit)
- USD/JPY basis swap stays wide even after FY-end rebalancing should have normalized
- Private credit: multiple BDCs hit redemption caps in same week, not isolated events
- HY OAS jumps 50+ bps in a single session (not a drift)

The line in 2026 is roughly: **SRF >$100B for multiple consecutive days** (not just quarter-end) + **SOFR-IORB persistently above +15bps** + **FRA-OIS through 25bps** = you are past plumbing and into priced counterparty risk. Any single indicator alone is noise; convergence across three or more indicators simultaneously is signal.

***

## 6. USD/JPY Cross-Currency Basis: The Early Warning Channel

Japanese banks and life insurance companies are structurally among the largest offshore USD borrowers in the world. Their funding model: borrow yen cheaply (BoJ policy rate 0.75%), swap into dollars via FX swaps, invest in U.S. fixed income. The cross-currency basis is the price of that dollar access. When it blows out, Japanese institutions face a funding squeeze in their highest-return asset.[^42][^26][^43]

March 31, 2026 concentrates multiple stressors simultaneously:
1. **Japan FY-end**: Institutional repatriation, balance-sheet squaring, USD demand surge[^39]
2. **BoJ April hike priced**: MUFG expects a 25bp BoJ hike to 1.00% in April, driving carry-trade unwind pressure[^24]
3. **USD/JPY at 160**: At or above the historic intervention threshold, MoF threatening "bold action"[^44][^25][^24]
4. **Japan $550B US investment deal**: Expected to structurally widen (make more negative) the 5–10y USD/JPY basis throughout 2026 as Japan state-backed institutions flow capital into the U.S.[^26]
5. **Incomplete fiscal year budget**: The Japanese government is operating on a provisional JPY 8.6 trillion stopgap budget until April 11, introducing political uncertainty into sovereign balance-sheet positioning[^24]

In prior stress episodes, the 3-month USD/JPY basis reached -63.75bps in October 2022 and went far wider in March 2020 before the Fed's emergency dollar swap lines calmed markets. MUFG's March 30 note characterizes the current US-Japan swap spread widening as "more modest" than prior episodes — meaning the system has not yet stressed, but is structurally primed.[^22][^23][^24]

A **USD/JPY basis move through -40bps on a sustained 2–3 day basis** around quarter-end, particularly if accompanied by SOFR jumping 20+ bps above its prior-day level, would be the earliest warning signal available before it appears in equity markets or mainstream financial news.

***

## 7. Indicators Already Showing Stress Most People Aren't Watching

**The Private Credit–Insurance Nexus (Most Under-Watched)**
Life and annuity insurers now hold an estimated $1.8 trillion in private credit, representing a record 46% of their total debt holdings. NAIC — the insurance regulatory body — is explicitly flagging this concentration as its top priority for 2026, with a "laser focused" mandate on RBC treatment of complex assets, CLO modeling, and third-party credit rating integrity. The new NAIC "discretion amendment" allowing the SVO to challenge credit ratings that are "materially higher" than SVO designations took effect January 1, 2026. If NAIC forces mark-downs via RBC reclassification, insurers face a forced selling event in illiquid private credit — precisely the asset-liability mismatch that cannot be resolved by Fed repo facilities.[^36][^37][^38][^45]

**Japan's Fiscal Situation (Understated)**
Japan is entering FY2026 without a passed initial budget — the government is operating on a provisional JPY 8.6 trillion stopgap that lasts until April 11. This is structurally unusual and adds political uncertainty to fiscal trajectory at precisely the moment when 30Y JGB yields hit 3.72% (up 19bps in a single session), the BoJ is debating intervention, and fiscal spending expectations are being revised higher due to energy price shocks. A disorderly JGB selloff (30Y above 4%) combined with USD/JPY above 160 would trigger a yen-carry unwind that directly hits U.S. Treasury markets — the Allianz Research paper from January 2026 identified UST 10Y at 5% as the breaking point for a JPY-led U.S. asset deleveraging scenario.[^44][^24]

**Reserve Concentration in G-SIBs**
Total bank reserves at $2.8T sounds like a lot, but the distribution matters as much as the level. G-SIBs are holding the bulk of these reserves as a regulatory buffer (G-SIB surcharge compliance, LCR requirements), making them effectively unavailable for redistribution to smaller banks and non-bank dealers who actually need them. The Fed's September 2025 Senior Financial Officer Survey found that nearly two-thirds of banks would reduce reserves if overnight rates moved 16bps above IORB — meaning the system is already near the sensitivity threshold where small funding demand shocks create large rate spikes. This is structurally different from 2019: then, reserves were scarce uniformly; now they are scarce *at the margin of intermediation* despite headline abundance.[^46][^16][^11]

**SRF as Indicator of Last Resort**
The SRF's purpose is explicitly to cap repo market rates at the upper bound of the Fed Funds target range (currently 3.75%). When the SRF is used outside of quarter-ends — as occurred on October 16, 2025 at $15B — it indicates that private funding markets are offering rates *above* the SRF's rate, meaning banks would rather borrow from the Fed than from each other. That is not counterparty credit risk (the collateral is Treasuries), but it is a direct signal of balance-sheet intermediation failure. The last time this happened at mid-month was COVID (March 2020) and the SVB regional bank stress (March 2023).[^47][^48][^41]

***

## 8. Ranked Summary: Best LIBOR-OIS Replacements

| Rank | Indicator | What It Measures | Current Status | Tomorrow's Risk |
|------|-----------|-----------------|----------------|-----------------|
| **1** | SOFR-IORB spread | Reserve scarcity / intermediation failure | Normal (-2bps)[^12][^15] | High — quarter-end |
| **2** | FRA-OIS (3M) | Forward interbank credit risk | Normal (~5–10bps)[^19] | Medium — rising if BoJ hike priced |
| **3** | G-SIB Bank CDS | Direct bank counterparty credit | Tight (est. IG regime)[^31] | Low-Medium |
| **4** | USD/JPY Basis Swap (3M) | Dollar offshore funding scarcity | Moderate; widening trend[^26] | **Very High** — Japan FY-end |
| **5** | SRF Usage | Funding market dysfunction | $0 current; $74.6B max[^32] | High — expect $30–75B+ |
| **6** | CP-EFFR Spread (3M AA Fin.) | Short-term credit market stress | Normal (~5–10bps)[^20] | Low |
| **7** | SOFR-EFFR Spread | Cash vs. collateral scarcity | Normal (~-1bps)[^12][^20] | Medium |

The most actionable single metric for real-time monitoring in 2026 is **SOFR-IORB**: it updates daily from FRED, its 2019 and 2020 analogs are well-documented, and it integrates both the reserve-scarcity and intermediation-unwillingness signals that are structurally most likely to be the precursor to a 2026 counterparty crisis. Cross-currency basis adds the global dollar-funding dimension that LIBOR-OIS also captured through Eurodollar market stress. Watching these two simultaneously, alongside SRF disclosures (published each morning by the NY Fed), gives the closest approximation to a 2026 LIBOR-OIS equivalent.

---

## References

1. [[PDF] The LIBOR-OIS Spread as a Summary Indicator](https://files.stlouisfed.org/files/htdocs/publications/mt/20081101/cover.pdf) - The spread reached its all-time high at 108 basis points on December 6,. 2007. Around the same time,...

2. [[PDF] The LIBOR-OIS Spread as a Summary Indicator](http://homepage.ntu.edu.tw/~nankuang/Money%20and%20Banking%20Supplement/6/LIBOR%20OIS%20spread.pdf) - In short, the LIBOR-OIS spread has been the summary indicator showing the “illiquidity waves” that s...

3. [[PDF] LIBOR: Origins, Economics, Crisis, Scandal, and Reform](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr667.pdf)

4. [[PDF] Policy Responses to the Global Crisis of 2007-09](https://www.frbsf.org/wp-content/uploads/Ito.pdf) - Both the Libor-OIS and the TED spreads stayed between 50 and 100 basis points from the beginning of ...

5. [Secured Overnight Financing Rate (Market Daily) - YCharts](https://ycharts.com/indicators/sofr) - Secured Overnight Financing Rate is at 3.63%, compared to 3.65% the previous market day and 4.36% la...

6. [TED spread - Wikipedia](https://en.wikipedia.org/wiki/TED_spread) - The TED spread is the difference between the interest rates on interbank loans and on short-term US ...

7. [[PDF] A User's Guide to Reducing the Federal Reserve's Balance Sheet](https://www.federalreserve.gov/econres/feds/files/2026019pap.pdf) - Now, we've returned to ample reserves, with EFFR trading just one basis point below IORB. Scarce res...

8. [The Overnight Money Warning - The B:Side Way with Chris Myers](https://www.thebsideway.com/p/the-overnight-money-warning) - SOFR is the Secured Overnight Financing Rate, the key rate for overnight borrowing backed by Treasur...

9. [Rates, Liquidity, and Tariffs: Three Questions to Answer in 2025](https://www.capitaladvisors.com/research/rates-liquidity-and-tariffs-three-questions-to-answer-in-2025/) - When reserves are abundant, SOFR tends to remain largely stable. As reserves decline, even a small c...

10. [Big cash crunch? Banks tap $26 billion Fed Repo lifeline](https://economictimes.com/news/international/us/big-cash-crunch-banks-tap-26-billion-fed-repo-lifeline-second-highest-since-2020-crash/articleshow/125743152.cms) - SRF use has surged through late 2025, including a $50.35 billion record on October 31, driven by mon...

11. [Federal Reserve Repo Operation: What Advisors Need to Know](https://get.ycharts.com/resources/blog/federal-reserve-repo-operation-2025/) - Standing Repo Facility Expansion: The Fed could increase the per-counterparty limit on repo operatio...

12. [Secured Overnight Financing Rate (SOFR) | FRED | St. Louis Fed](https://fred.stlouisfed.org/series/SOFR) - Graph and download economic data for Secured Overnight Financing Rate (SOFR) from 2018-04-03 to 2026...

13. [SOFR-IORB spread widens, signaling money market stress - LinkedIn](https://www.linkedin.com/posts/redmond-wong-584929232_the-spread-between-sofr-and-the-iorb-has-activity-7391384626902204416-Prcx) - The spread between SOFR and the IORB has widened, signaling emerging stress in money markets. On 31 ...

14. [Liquidity panic? SOFR-IORB spread hits highest level since 2020](https://economictimes.com/news/international/us/us-dollar-liquidity-crisis-sofr-iorb-spread-2025-hits-highest-level-since-2020-fed-warning-qe-next/articleshow/125092436.cms) - The SOFR-IORB spread, a crucial indicator of dollar liquidity, has spiked to 32 basis points, its hi...

15. [Interest Rate on Reserve Balances (IORB Rate) (IORB) - FRED](https://fred.stlouisfed.org/series/IORB) - Interest Rate on Reserve Balances (IORB Rate) (IORB) ; 2026-03-30: 3.65 ; 2026-03-29: 3.65 ; 2026-03...

16. [SOFR spiked 18 basis points on Friday. | Glenn Handley - LinkedIn](https://www.linkedin.com/posts/glennhandley_sofr-spiked-18-basis-points-on-friday-the-activity-7391776904820985856-nuaa) - SOFR spiked 18 basis points on Friday. The biggest one-day move since March 2020. Mark Cabana at Bof...

17. [Why It Matters That the FRA-OIS Spread Is Widening](https://www.bloomberg.com/news/articles/2020-03-09/why-it-matters-that-the-fra-ois-spread-is-widening-quicktake) - The spread has approached the levels in 2011 of close to 60, but is nowhere near the financial crisi...

18. [[PDF] Measuring Stress in Money Markets: The CDSS Index](https://www.ecb.europa.eu/events/pdf/conferences/exliqmmf/Session1_Demiralp_paper.pdf?b4a211a533a34820c3e6999ab8807421) - FRA-OIS spread: The spread between three-month forward rate agreements and the OIS rate reflects exp...

19. [USD SOFR OIS data: daily rates & forward curves | TraditionData](https://www.traditiondata.com/products/usd-sofr/) - What is the current SOFR rate? – Example SOFR swap data ; 24th Mar 2026 · 23rd Mar 2026 · 20th Mar 2...

20. [Federal Reserve Board - H.15 - Selected Interest Rates (Daily)](https://www.federalreserve.gov/releases/h15/) - The Federal Reserve Board of Governors in Washington DC.

21. [[PDF] CB2 15_Phases of the 2007–2009 Global Financial Crisis as ...](https://som.yale.edu/sites/default/files/2022-01/CB2%2015_Phases%20of%20the%202007%E2%80%932009%20Global%20Financial%20Crisis%20as%20Reflected%20in%20Bank%20Credit%20Default%20Swap%20Spreads%20and%20Libor-OIS%20Spread.pdf) - Two widely accepted indicators of financial sector stress are credit default swap (CDS) spreads, whi...

22. [MONEY MARKETS-Euro, yen FX swap rates hit more than ...](https://jp.reuters.com/article/usa-moneymarkets/money-markets-euro-yen-fx-swap-rates-hit-more-than-two-year-highs-flags-u-s-dollar-funding-stress-idUKL1N31126I/) - The cost of raising short-term U.S. dollar funds in Japanese and European currency swaps markets sur...

23. [MONEY MARKETS-Euro, yen FX swap rates hit more than two-year highs, flag U.S. dollar funding stress](https://jp.reuters.com/article/money-markets-euro-yen-fx-swap-rates-hit-more-than-two-year-highs-flag-us-do-idUSL1N3141V2/) - The cost of raising short-term U.S. dollar funds in Japanese and European currency swap markets surg...

24. [FX Weekly - MUFG Research](https://www.mufgresearch.com/fx/fx-weekly-30-march-2026/) - As we approach the fiscal year end in Japan we find ourselves in the unusual position of not having ...

25. [Japan's Latest Warnings on FX Intervention Help Buoy Yen](https://www.bloomberg.com/news/articles/2026-03-30/japan-s-fx-chief-warns-of-bold-action-after-yen-tops-160) - Japan's top currency official helped strengthen the yen by delivering his strongest warning yet to s...

26. [Japan's $550bn US trade deal set to drive cross-currency basis](https://www.globalcapital.com/article/2fy4f1pkz253xi11mtfy8/people-and-markets/leader/japans-550bn-us-trade-deal-set-to-drive-cross-currency-basis) - Japan's $550bn US trade deal set to drive cross-currency basis · Bye-bye euro curve steepeners, ther...

27. [3-Month Commercial Paper Minus Federal Funds Rate (CPFFM)](https://fred.stlouisfed.org/series/CPFFM) - Graph and download economic data for 3-Month Commercial Paper Minus Federal Funds Rate (CPFFM) from ...

28. [3-Month Commercial Paper Minus Federal Funds Rate (CPFF) - FRED](https://fred.stlouisfed.org/series/CPFF) - Series is calculated as the spread between 3-Month AA Financial Commercial Paper (RIFSPPFAAD90NB) an...

29. [Is a shift to TGCR good for US interest rate and credit markets?](https://sofracademy.com/is-a-shift-to-tgcr-good-for-us-interest-rate-and-credit-markets/) - SOFR, the Secured Overnight Financing Rate, is closely related to TGCR but incorporates additional s...

30. [Fed's T-bill pivot expected to ease supply, but rate futures flag tight ...](https://www.reuters.com/business/feds-t-bill-pivot-expected-ease-supply-rate-futures-flag-tight-funding-2025-10-31/) - SOFR seen rising sharply above fed funds rate in November, December; Fed did not do more to ease liq...

31. [2026 Investment Grade Credit Outlook: At a Turning Point?](https://www.pinebridge.com/en/insights/2026-investment-grade-credit-outlook) - Here we examine the forces shaping the 2026 investment grade credit markets and look at strategies t...

32. [Year end sees record borrowing from Fed's standing repo operation](https://www.reuters.com/business/finance/banks-tap-record-liquidity-new-york-feds-standing-repo-facility-2025-12-31/) - Financial firms borrowed $74.6 billion from standing repo operation on final trading day of 2025; Ye...

33. [Year End Sees Record Borrowing From Fed's Standing Repo Facility](https://money.usnews.com/investing/news/articles/2025-12-31/banks-tap-record-liquidity-from-new-york-feds-standing-repo-facility) - The firms borrowed $74.6 billion ​from the central bank, in loans collateralized with $31.5 billion ...

34. [ICE BofA US High Yield Index Option-Adjusted Spread - FRED](https://fred.stlouisfed.org/series/BAMLH0A0HYM2) - Observations. 2026-03-27: 3.42. Updated: Mar 30, 2026 9:03 AM CDT. Next Release Date: Mar 31, 2026. ...

35. [Private Credit Perspectives Q1 2026 - Long Angle](https://www.longangle.com/alts-education/private-credit-perspectives) - Long Angle's Private Credit Perspectives Q1 2026 examines the headlines surrounding private credit t...

36. [Life Insurers Hold More Private Credit Than Ever - WSJ](https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-03-05-2026/card/life-insurers-hold-more-private-credit-than-ever-4YmcDCl9craWUTGHB1Ut) - Life and annuity insurers held an estimated $1.8 trillion in private credit in 2025, a record 46% of...

37. [Continued Pressure: Why the Insurance Industry Will ... - Capstone DC](https://capstonedc.com/insights/insurance-2026-preview/) - Capstone expects NAIC scrutiny of insurer investment strategies to continue in 2026, with particular...

38. [The NAIC's Evolving Response to Private Equity in Insurance](https://www.cliffordchance.com/insights/resources/blogs/insurance-insights/2026/03/the-naics-evolving-response-to-private-equity-in-insurance.html) - This article describes recent and ongoing insurance regulatory initiatives in the U.S. examining the...

39. [Sharing insights elevates their impact](https://www.spglobal.com/marketintelligence/en/mi/research-analysis/sofr-quarter-end-spike.html) - The quarter end surge in SOFR was not as large as what we observed at year-end, but the rate did jum...

40. [Fed's Standing Repo Facility (SRF) Drops to Zero, from $75 billion ...](https://wolfstreet.com/2026/01/05/feds-standing-repo-facility-srf-drops-to-zero-from-75-billion-on-the-last-balance-sheet-as-yearend-liquidity-turmoil-dissolves/) - This spike in repo rates made it profitable for banks to borrow $75 billion at the SRF on December 3...

41. [US Fed's repo facility tapped for 15 billion, a sign of stress](https://www.linkedin.com/posts/laur%C3%A9line-renaud-chatelain-775a8643_us-repo-fed-activity-7384970076451520512-Q2fd) - The Federal Reserve's Standing Repo Facility lent a total of $50.35 billion on Friday, October 31st ...

42. [2026 Annual Foreign Exchange Outlook - MUFG Research](https://www.mufgresearch.com/fx/monthly-foreign-exchange-outlook-january-2026/) - USD DEPRECIATION TO EXTEND FURTHER. After surging by 7.0% in 2024, the US dollar depreciated by 9.4%...

43. [Japan: Staff Concluding Statement of the 2026 Article IV Mission](https://www.imf.org/en/news/articles/2026/02/13/imf-cs-02172026-japan-staff-concluding-statement-of-the-2026-article-iv-mission) - ... cross-currency funding exposures, and pockets of vulnerability in commercial real estate. ... Ma...

44. [[PDF] From Japan with love: New policy stance creates both market ...](https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/economic-research/publications/specials/en/2026/january/2026_01_29_Japan.pdf) - The trade-weighted JPY is still well below long-run averages and beyond defending specific levels fo...

45. [NAIC to be "laser focused" on insurer's changing appetites for ...](https://www.insuranceassetrisk.com/content/analysis/naic-to-be-laser-focused-on-insurers-changing-appetites-for-private-and-alternative-assets-in-2026.html) - NAIC to be "laser focused" on insurer's changing appetites for private and alternative assets. By Ro...

46. [The Fed - September 2025 Senior Financial Officer Survey Results](https://www.federalreserve.gov/data/sfos/september-2025-senior-financial-officer-survey.htm) - The two-year SOFR swap spread (U.S. Treasury yield - SOFR swap) is 16 basis points lower than curren...

47. [Standing Repo (SRP) Operations Rate (SRFTSYD) | FRED](https://fred.stlouisfed.org/series/SRFTSYD) - Standing Repo (SRP) Operations Rate (SRFTSYD) ; 2026-03-27: 3.75 ; 2026-03-26: 3.75 ; 2026-03-25: 3....

48. [Fed repo borrowing jumps as quarter-end pressure stirs money market](https://economictimes.com/markets/us-stocks/news/fed-repo-borrowing-jumps-as-quarter-end-pressure-stirs-money-market/articleshow/126244170.cms) - Fed repo usage jumps ahead of quarter-end, signalling tighter funding conditions. Synopsis. Usage of...

