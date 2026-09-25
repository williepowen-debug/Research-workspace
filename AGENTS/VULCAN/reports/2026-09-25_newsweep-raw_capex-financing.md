# VULCAN news sweep: AI-capex demand and financing, 2026-09-13 to 2026-09-25

Compiled 2026-09-25, ~09:15 ET. Prices are yfinance closes pulled at compile time (`.venv`). They are labeled "yf" and should be re-pulled live before any band call.

## Most important for the AI-capex thesis (5 lines)
1. **The "pace the frontier" shock hit equities, not capex. No capex cut was found anywhere.** On 9/14 the SOX fell 5.9%, NVDA 3.4% and SoftBank 10.7%. I found no lab, hyperscaler or chip company that cut a capex budget, compute contract or data-center plan in response. Broadcom (AVGO) and Nvidia (NVDA) both said demand is unchanged.
2. **The S5 story of the window is Oracle's Project Jupiter force-majeure notice (reported 9/24).** Oracle is protecting itself against a power-driven delay on a Stargate site. About $18B of project debt is quoted at 89–91c. It was reported by Bloomberg; I have not verified it at the primary.
3. **Record AI financing is clearing, but at a price.** SoftBank sold $11.1B of junk bonds (priced 9/23), the largest high-yield sale on record, and it priced INSIDE talk. Coupons were still 8.625–9.75%, SoftBank's highest ever. CoreWeave (CRWV) placed a $4.2B convertible and set up a 35M-share at-the-market (ATM) share program.
4. **Rates are now a headwind to the financing.** The Fed hiked 25bp on 9/16 (primary). The 10Y closed at 5.11% on 9/23, the highest since 2007, and the 30Y hit its highest level since 2004 on 9/24. Reuters (9/22) reports AI issuers paying about 37bp over investment grade (IG).
5. **Demand-side watch item: OpenAI's largest training run has been on hold since August.** Altman now says he is "open to" slowing further, in step with other labs. A shrinking frontier-training appetite is the channel through which the safety turn could eventually reach S1/S3 compute demand. That is not yet visible in any filed number.

---

## 1. OpenAI / Anthropic statements (9/11–9/14) and what followed

| Item | Detail (exact wording where obtained) | Source, date | Confidence |
|---|---|---|---|
| Amodei essay | "We must slow the pace at which we improve the capabilities of AI models. Progress will still seem fast, and we must make wise use of the time we gain." Pacing does "not mean halting model training or technical progress." It floats limiting "training compute, the nature of training runs, or internal use of AI to improve AI." Three steps: embedded third-party evaluators, then coordination among democratic countries, then global coordination. | darioamodei.com "We Must Pace the Frontier", Sat **2026-09-12** | PRIMARY |
| Altman on the IPO | "I actually think that, given everything happening with safety, right now would be an ill-advised moment to go public, and we don't feel pressure on that." He also said "I would say not 2026". The target is now 2027. | Fortune interview, pub. **2026-09-12**; Fortune 9/14 | TIER-1 SECONDARY (Fortune is the interviewer) |
| Altman on pacing | "we need to pace the frontier" (X post, Sat 9/12). Earlier, at a 9/11 all-hands, he said OpenAI would consider slowing "preferably in step with other labs". | Yahoo Finance roundup; Reuters/Bloomberg relayed via resultsense, **9/11** | TIER-1 SECONDARY |
| Musk | "Dario is right" (X) | Yahoo Finance / Forbes 9/13 | TIER-1 SECONDARY |
| Nadella | Supports "deliberate pacing of AI to ensure alignment is right" (X, Sun 9/13) | Yahoo Finance roundup | TIER-1 SECONDARY |
| Zuckerberg | Backs third-party evaluators but not universal pacing | Yahoo Finance roundup | TIER-1 SECONDARY |
| Huang (Nvidia) | "We're not going to let that happen, sir" (to Trump on speakerphone, All-In Summit). Also "We should go as fast as we can, irrespective of anybody else" (CBS). | TechCrunch **9/14**; CNBC 9/15; Daily Caller 9/20 | TIER-1 SECONDARY |
| Hock Tan (Broadcom) | Slowdown talk "will not prompt the company to adjust its AI semiconductor revenue forecasts" | TradingKey, 9/14–15 | UNVERIFIED (aggregator; its dates are internally inconsistent) |
| SoftBank −10.7% | 9/14 Tokyo close, ¥6,540 → ¥5,839 (yf confirms −10.72%) | AP via ABC News **9/14** | TIER-1 SECONDARY + yf |

⚠️ **Number and mechanism are separate claims.** The −10.7% figure is confirmed. AP attributes the move to the slowdown/IPO statements. That attribution is plausible but confounded: the 10Y briefly crossed 5% the same day (Reuters 9/14).

**Follow-through (9/14–9/25):**

| Development | Detail | Source, date | Confidence |
|---|---|---|---|
| **Capex, contract or data-center change in response** | **NOT FOUND.** Searched: capex cut or pause after the essay; hyperscaler reactions; Stargate plan changes; lab compute contracts. Semafor (9/15) is analysis only: it says a 10% capex cut would turn a $66B shortfall of 6-quarter operating cash flow vs capex into a $74B surplus. It contains no company statement. | Semafor 9/15 | — |
| Retraction or clarification | **NOT FOUND.** No walk-back located. Fortune 9/15 reports Altman saying the IPO window moved to 2027 and that "markets aren't the culprit". | Fortune 9/15 (headline only) | TIER-1 SECONDARY |
| OpenAI private round | Talks on a VC round at a **$1.2T** valuation to make an IPO unnecessary. No size or investors given. | Fortune citing FT, **9/16** | TIER-1 SECONDARY |
| Cross-testing deal | OpenAI and Anthropic reached the contracting stage on mutual model safety tests, then the deal "quietly died" | Business Standard 9/22; 24/7 Wall St 9/24 (original outlet not named) | UNVERIFIED |
| Antitrust suit | *Buist v. Anthropic PBC*, N.D. Cal., filed **9/18**. Sherman Act §1 claim against Anthropic, OpenAI, Google and SpaceXAI. | CBS / The Hill / Business Standard 9/20 | TIER-1 SECONDARY |
| Background (pre-window) | OpenAI "slows model training"; the frontier model "Astra" is paused and its **largest planned training run remains on hold** after the Hugging Face breach | Reuters via Investing.com, **8/18**; OpenAI blog | TIER-1 SECONDARY |
| Anthropic IPO | Still planned. Marketing could start mid-October. | The National, 9/13 | TIER-1 SECONDARY |

## 2. Hyperscaler capex signals, 9/13–9/25

| Co. | Signal | Source, date | Confidence |
|---|---|---|---|
| ORCL | Q1 FY27 (9/10, just before the window): revenue $19.3B (+30%); OCI +121% to $7.4B; RPO $664B (+$209B YoY); Q1 capex $28.5B; **FCF −$5.0B**. A secondary reported −$5.4B, so there is a discrepancy; the primary figure is used. | Oracle 8-K Ex-99.1, 9/10 | PRIMARY |
| ORCL | FY27 capex guide of **$90–95B**, "not more than $70B net cash capex". Not found in the 8-K release; appears only in a secondary summary of the call. | financefeeds / Yahoo transcript | UNVERIFIED at primary |
| ORCL | **Project Jupiter (NM, Stargate) force-majeure notice** sent to Blue Owl's Stack Infrastructure over power delays. Aim: defer lease payments if the 2028 online date slips. About **$18B** of bank debt is quoted at **89–91c**. Oracle said force-majeure notices "do not, by themselves, establish a project delay… Project Jupiter remains on our planned schedule." The gas pipeline has been denied a state land crossing twice. | Bloomberg, relayed by Reuters/WMBD, GBAF, CNBC headline, **9/24** | TIER-1 SECONDARY (Bloomberg original unfetched) |
| ORCL | Ellison **cancelled a 10b5-1 plan** to sell up to 50M shares (~$7.5B). "No Oracle stock was sold under the plan." | Oracle 8-K Item 8.01, filed **9/14** (PR 9/12) | PRIMARY |
| MSFT / GOOGL / AMZN / META | **No guidance change, lease pause or cancellation, or new signing found in the window.** Searched: lease pause/cancel Sept 2026; new DC investment announcements; exec conference comments. Only reactions to the pacing debate (Nadella, Zuckerberg; see §1). | — | NOT FOUND |
| Consensus context | Jefferies' Chris Wood doubts the **$990B** 2027 hyperscaler capex consensus. BofA estimates **$795B** for 2026 and **$1.08T** for 2027. | inkl, medianama (Sept) | UNVERIFIED (aggregators) |

## 3. AI financing

| Deal | Talk → final | Source, date | Confidence |
|---|---|---|---|
| **SoftBank HY, $11.1B equiv.** (record; beats Numericable's $10.9B in 2014) | **Initial soundings (9/22):** 7.5y ~10%; EUR 6y mid-8%. **Guidance:** 3.5y 8.75–8.875%, 5.5y 9.375–9.5%, 7.5y 9.75–9.875%. **FINAL (9/23):** $1B 3.5y **8.625%** · $4.5B 5.5y **9.25%** · $4.5B 7.5y **9.75%** · €500M 4y **7.125%** · €500M 6y **8.00%**. **Priced INSIDE talk** on every USD tranche. Dollar orders >$30B, against >$20B early. Rated BB+. Proceeds go to the **$10B third/final tranche** of its $30B OpenAI follow-on (closing **10/1**), plus M&A. These are SoftBank's highest-ever USD yields. | Bloomberg via Yahoo 9/22; Seoul Economic Daily 9/23; Reuters via MarketScreener 9/23–24 | TIER-1 SECONDARY |
| **CoreWeave convertible** | Proposed $3.0B (9/17) → priced **$3.7B** (9/18) → **$4.2B issued** with the $500M greenshoe exercised in full (settled 9/22). **2.875%** coupon, due 4/1/2033. Conversion price ~$97.85 (22.5% premium to $79.88). Capped call cap $199.70; $498.8M spent on capped calls. Max 52,578,540 shares on conversion. Guaranteed by the same subsidiaries as the 9.25% 2030 notes. Cross-default at >$200M or 5% of LTM EBITDA. **Coupon/premium talk: NOT FOUND.** | CRWV 8-K 9/22 (Items 1.01, 3.02, 8.01, 9.01; **no Item 2.03**); CRWV IR release 9/18 | PRIMARY |
| **CoreWeave 424B5 (9/17)** | **ATM of up to 35,000,000 Class A shares** "at market prices prevailing at the time of sale". 11 sales agents; forward-sale structure (forward purchasers/sellers). Not contingent on the convertible. Use: general corporate purposes, incl. debt repayment and "improving credit profile toward investment grade." | CRWV 424B5, 9/17 | PRIMARY |
| IG market tone | AI-related issuers at **~115bp** vs broad IG **78bp**, a premium of about 37bp. Alphabet needed "large concessions" in August. Hyperscaler gross issuance is projected at **$420B in 2027** (+60%). | Reuters via BNN Bloomberg, **9/22** | TIER-1 SECONDARY |
| Pulled / postponed AI deals in window | **NOT FOUND.** Searched: pulled/postponed AI bond Sept 2026. The only hit was Prime Data Centers, delayed in July. | — | — |
| Meta SPV, xAI, DC ABS/CMBS | **No new priced deal found in the window.** Search hits were Hyperion (Oct 2025), SpaceX's $25B IG bond (June 2026) and xAI's $12B Colossus-2 debt (mid-2026). Bloomberg ran a 9/14 feature on DC CMBS risk, but it names no deal. | — | NOT FOUND |

## 4. Macro

| Item | Level / date | Source | Confidence |
|---|---|---|---|
| FOMC 9/16 | **+25bp to 3.75–4.00%**, vote 12-0. "Inflation remains elevated." First hike since 2023. | federalreserve.gov statement 9/16 | PRIMARY |
| 10Y | Briefly >5% on 9/14. **5.11% on 9/23** (+15bp; highest since 2007). yf ^TNX: 5.16 on 9/24, 5.18 on 9/25 (live). | CNN 9/23 (snippet), Reuters 9/14 | TIER-1 SECONDARY + yf |
| 30Y | **5.40% on 9/23** (highest close since 2004). Highest since 2004 again on 9/24, at 5.46% (Bloomberg) with an intraday high of 5.501%. | CNN 9/23, Bloomberg/Qz 9/24 | TIER-1 SECONDARY |
| Drivers | Strong September PMIs (fastest activity since Jul-2021), energy-driven input costs, Brent ~$105–107 | CNN, Reuters | TIER-1 SECONDARY |

**Share moves (closes, yf):**

| | 9/11 | 9/14 | 9/17 | 9/24 | Window 9/11→9/24 |
|---|---|---|---|---|---|
| NVDA | 218.29 | 210.96 (−3.4%) | 219.34 | 224.58 | **+2.9%** |
| ORCL | 150.28 | 144.79 (−3.7%) | 150.59 | 139.54 (−3.5% on 9/24) | **−7.1%** |
| CRWV | 88.99 | 82.98 (−6.8%) | 79.88 (−4.2%, convertible day) | 90.13 | **+1.3%** |
| SOX | 11,824 | 11,131 (−5.9%) | 11,599 | 12,493 | **+5.7%** |
| SoftBank (¥) | 6,540 | 5,839 (−10.7%) | 6,247 | 6,352 | 9/25 Tokyo: 6,150 (**−3.2%**, tied to the Oracle Jupiter news per Investing.com) |

Tokyo was closed 9/21–23. NVDA 9/24 is 224.58 on yf vs 223.95 in one aggregator; re-pull live before citing.

## 5. Nvidia

| Item | Detail | Source | Confidence |
|---|---|---|---|
| New deals / guarantees in window | **NOT FOUND.** The NVDA 8-K list shows nothing between 9/3 and 9/25. The last credit-support 8-K is 8/17 (items 1.01/2.03: the $105B-cap SB Energy/OpenAI Ohio guarantee). | SEC EDGAR 8-K index | PRIMARY (absence of filing) |
| Huang stance | Rejects any slowdown. Projects $3–4T of annual AI infrastructure spend by 2030. | CNBC 9/15, TradingKey | TIER-1 SECONDARY / UNVERIFIED for the $3–4T figure |
| China | Guidance assumes zero China DC sales. At the 9/24 US–China summit, USTR Greer said chip export controls were "not on the agenda". Asia Times reports an Entity-List loophole (Aivres, >$3B of Blackwell systems). | Motley Fool 9/21; Asia Times Sept | UNVERIFIED |

Sources: [Amodei essay](https://darioamodei.com/post/we-must-pace-the-frontier) · [Fortune 9/12](https://fortune.com/2026/09/12/sam-altman-openai-ipo-delay-ill-advised-moment-safety-concerns/) · [Fortune 9/16](https://fortune.com/2026/09/16/openai-ipo-sam-altman-vc-funding-valuation-1-2-trillion/) · [AP/ABC 9/14](https://abcnews.com/Business/wireStory/asian-shares-mixed-openai-investor-softbank-shares-plunge-136415006) · [Reuters 9/14](https://www.investing.com/news/economy-news/ai-warnings-knock-nasdaq-futures-pressure-tech-stocks-4898987) · [TechCrunch 9/14](https://techcrunch.com/2026/09/14/nvidia-ceo-jensen-huang-tells-trump-were-not-going-to-let-an-ai-slowdown-happen/) · [Reuters OpenAI training 8/18](https://www.investing.com/news/economy-news/openai-slows-model-training-to-bolster-security-after-hugging-face-hack-4865899) · [Oracle 8-K 9/10](https://www.sec.gov/Archives/edgar/data/0001341439/000119312526387905/orcl-ex99_1.htm) · [Oracle 8-K 9/14](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389753/d20034d8k.htm) · [GBAF Jupiter 9/24](https://www.globalbankingandfinance.com/oracle-cites-force-majeure-shield-itself-controversial-data/) · [SoftBank Reuters/MarketScreener](https://www.marketscreener.com/news/softbank-issues-11-1-billion-in-bonds-in-openai-financing-push-ce785adedb89f122) · [SoftBank soundings, Bloomberg/Yahoo](https://finance.yahoo.com/markets/stocks/articles/softbank-draws-over-20-billion-084641856.html) · [SoftBank guidance, Sedaily](https://en.sedaily.com/international/2026/09/23/softbank-junk-bond-draws-20-billion-in-demand-at-875) · [CRWV 8-K 9/22](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000432/crwv-20260917.htm) · [CRWV 424B5](https://www.sec.gov/Archives/edgar/data/1769628/000162828026062362/coreweave-424b5.htm) · [CRWV pricing PR](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-7-Billion-Convertible-Senior-Notes-Offering/default.aspx) · [Reuters AI debt 9/22](https://www.bnnbloomberg.ca/investing/2026/09/22/corporate-bond-buyers-get-picky-with-flood-of-ai-debt/) · [Fed 9/16](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm) · [Semafor 9/15](https://www.semafor.com/article/09/15/2026/slowing-ai-development-could-boost-hyperscaler-balance-sheets)
