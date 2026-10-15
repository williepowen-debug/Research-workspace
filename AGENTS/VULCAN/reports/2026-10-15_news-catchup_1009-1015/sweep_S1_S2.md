# VULCAN S1/S2 news + data sweep, 2026-10-09 → 2026-10-15

Compiled 2026-10-15 ~12:15 ET by a research subagent. Nothing in the repository was edited.

**Legend.** `P` = read at the primary (issuer press release, SEC/EDGAR filing, exchange, TrendForce or BLS page). `R` = relay or secondary, with the outlet named. `PX` = price/tape data pulled from the Yahoo Finance chart API (a vendor feed, not an exchange primary). US rows dated 10-15 are **INTRADAY (~12:15 ET), not closes**. Korean and Japanese 10-15 figures are closes.
**Discipline tag.** `PRICE` = a stock, index or bond move. `CONTRACT` = a change to a capex budget, contract, lease, order, financing or filed obligation. `INFO` = a forecast, statement or calendar item. **Headline finding: across 10/9–10/15 nearly every S1 item is PRICE; none is a hyperscaler CONTRACT change. The CONTRACT-class items that do exist sit at the edges: S5 financing (an IPO postponement) and S2 consumer demand (OEM order cuts).**

---

## 0. Primary-filing check (EDGAR submissions API, pulled 2026-10-15 ~12:00 ET)

| Issuer | Last 8-K (items) | Any non-insider filing 10/05–10/15 | Read |
|---|---|---|---|
| CRWV | 2026-09-22 (1.01, 3.02, 8.01, 9.01) | none (Form 4s only) | P |
| ORCL | 2026-09-14 (8.01, 9.01) | none | P |
| NVDA | 2026-09-03 (8.01) | 4/A only | P |
| MSFT | 2026-09-02 (7.01, 9.01) | none | P |
| GOOGL | 2026-08-10 (8.01, 9.01) | none | P |
| META | 2026-07-29 (2.02, 9.01) | none | P |
| AMZN | 2026-09-14 (8.01, 9.01) | 3/A only | P |
| MU | 2026-09-30 (2.02, 9.01) | **10-K filed 2026-10-09** (FY ended 2026-09-03); 144 filed 10/14 | P |
| TSM | n/a (6-K filer) | **6-K 10/08 (Sept revenue); 6-K 10/15 (3Q26 results)** | P |

⇒ **No S1 issuer filed an 8-K in the window.** No hyperscaler or CRWV/ORCL filed a material agreement (1.01), a new obligation (2.03), a termination (1.02) or a capex revision. An 8-K filed after ~12:00 ET 10/15 would not show here.

---

## S1 — AI-capex concentration

### S1(a) What drove the 10/13–10/15 selloff

**Tape (PX, Yahoo chart API, pulled 10/15 ~12:15 ET)**

| Ticker | 10/09 | 10/12 | 10/13 | 10/14 | 10/15 (intraday) | Tag |
|---|---|---|---|---|---|---|
| CRWV | 82.08 (+0.6%) | 80.26 (−2.2%) | 77.81 (−3.1%) | **65.78 (−15.5%)**, vol 108.5M | 64.15 (−2.5%) | PRICE |
| ORCL | 141.40 | 137.39 (−2.8%) | 143.20 (+4.2%) | **130.55 (−8.8%)**, vol 52.0M | 133.34 (+2.1%) | PRICE |
| NBIS | 221.07 | 210.06 (−5.0%) | 206.86 (−1.5%) | **186.01 (−10.1%)** | 176.58 (−5.1%) | PRICE |
| NVDA | 229.28 | 226.32 (−1.3%) | 228.52 (+1.0%) | 221.30 (−3.2%) | 217.38 (−1.8%) | PRICE |
| AVGO | 361.54 | 354.73 (−1.9%) | 357.31 (+0.7%) | 346.25 (−3.1%) | 339.35 (−2.0%) | PRICE |
| MU | 1029.00 | 989.04 (−3.9%) | 953.19 (−3.6%) | 914.13 (−4.1%) | 912.23 (−0.2%) | PRICE |
| SOXX | 559.40 | 544.85 (−2.6%) | 543.90 (−0.2%) | 519.42 (−4.5%) | 507.97 (−2.2%) | PRICE |
| SPY | 778.57 | 778.10 | 778.01 | 769.60 (−1.1%) | 769.87 (0.0%) | PRICE |

**Checking the figures in the brief against the tape (PX):**

| Brief's figure | Measured | Verdict |
|---|---|---|
| CRWV −15.5% on 10/14 | 87.12→… 77.81→65.78 = **−15.46%** | ✅ |
| CRWV 3.6× volume | 108.45M vs 20-day avg 30.9M = **3.51×**; vs 50-day avg = **3.84×** | ≈ ✅ (the multiple depends on the window; state which one) |
| CRWV ~−29% over 10 sessions | 10 sessions (9/30→10/14) = **−24.5%**. From the 20-day high (10/06, 91.72) → 10/14 = **−28.3%**, → 10/15 intraday = −30.1% | ⚠️ **−29% is peak-to-trough over 7 sessions, not a 10-session return.** The 10-session figure is −24.5%. |
| KOSPI ~−8% on 10/15 | close **5,554.22, −7.57%** (intraday low 5,450.81, more than −9%) | ✅ approximately; quote the close |
| Nikkei ~−4% on 10/15 | close **64,425.95, −4.90%** (Yahoo meta, matching Japan Times) | ⚠️ **closer to −5% than −4%** |

**Causes, sorted by type**

| # | Driver | Figure / claim | Source (URL) | Source date | P/R | Tag |
|---|---|---|---|---|---|---|
| 1 | **Hot US September CPI** (released 10/14 08:30 ET) | headline +0.6% m/m, **+3.7% y/y**; core +0.3% m/m, **+2.6% y/y**. Yahoo reports consensus at 3.6% / 2.5%. Hike odds rose; Collins and Williams both lean toward one more hike | https://www.bls.gov/news.release/cpi.nr0.htm ; https://finance.yahoo.com/markets/live/stock-market-today-hot-inflation-report-drops-tech-drives-sp-500-nasdaq-down-152206632.html | 2026-10-14 | P (BLS) / R (consensus, Fed, Yahoo) | INFO (macro) |
| 2 | **CRWV bond-yield chart went viral** | Chamath Palihapitiya posted on X on **10/13** that a CRWV bond yield had hit an all-time high of **15%**, against ~9% this summer. Musk replied "Yikes." | https://www.fool.com/investing/2026/10/14/why-coreweave-stock-tumbled-today/ | 2026-10-14 13:41 ET | R (Motley Fool) | PRICE (credit) |
| 3 | **CRWV 9.625% 2032 notes** ($1.25B, issued June) | ~**78c**, yield **just over 16%** (Tradeweb) early 10/15; 5-year **CDS above 1,000bp** (S&P/LSEG) | https://thecryptobasic.com/2026/10/15/coreweave-stock-falls-another-6-as-bond-yields-top-15-despite-ceo-reassurance/ (citing Reuters) | 2026-10-15 | R (2nd-hand Reuters) | PRICE (credit). **For LIQUID's spread tells** |
| 4 | **Intrator internal memo** (10/14) | Says contracted backlog covers debt obligations; competitors' difficulties are "bleeding into the narrative around CoreWeave" | same as #3 (citing Reuters) | 2026-10-14 | R. **UNVERIFIED at Reuters**; a direct search found nothing | INFO |
| 5 | **Gartner research note (10/14)** | **>$3.5T** of AI infrastructure spend exposed to impairment by end-2030; providers need **~$8.5T** cumulative revenue (capex + financing + 12% ROIC) against Gartner's **~$3.5–3.6T** AI revenue forecast; **>80% of neoclouds cease independent operations by 2030** (analyst Will Sommer: this includes acquisition, not only failure) | Primary URL exists: https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030 (**403 / bot wall, NOT read**). Read: https://www.techtarget.com/it-infrastructure/news/366652181/Gartner-forecasts-massive-AI-infrastructure-write-downs | 2026-10-14 | R (TechTarget). The primary title was seen only in the search index | INFO (forecast). **A forecast, not a contract** |
| 6 | **AirTrunk (Blackstone) postponed** its ~US$1.5B Singapore REIT IPO, possibly to early 2027. Stated reasons: market volatility and US-rate uncertainty | WSJ via https://w.media/airtrunk-postpones-singapore-us1-5-billion-reit-ipo-amid-ai-stock-selloff-report | WSJ ~10/13; w.media 10/14 | R | **CONTRACT-adjacent (S5)**. ⚠️ **Under the desk's 10/09 ruling, POSTPONED with no withdrawal = AMBIGUOUS and NOT scored**, unlike Firmus (withdrawn 10/09, already KB-209) |
| 7 | **CXMT 4F² DRAM claim** (see S2) hit memory names on **10/12–10/13**, before the CPI/CRWV leg | KOSPI −5.5% on 10/13 | see S2 | 10/10–10/13 | P(tape) / R | PRICE |
| 8 | **Broadcom CEO Hock Tan, Singapore, ~10/12:** "a lot of investors have no clue what they are investing in"; compared AI investing to a casino; said **capital availability** could become the binding limit on AI growth | https://www.tikr.com/blog/chinas-cxmt-and-broadcoms-ceo-rattle-chip-stocks-which-fear-matters-more-for-micron | ~2026-10-13 | R (TIKR). **Not verified at a primary or transcript** | INFO |
| 9 | Oracle −8.8% on 10/14 | Coverage puts it down to CPI and yields plus AI-financing risk. Only Oracle-specific item: it again urged FERC to approve the gas pipeline for **Project Jupiter** (NM), warning that delay threatens the timeline. **No new contract, no filing** | https://www.tradingkey.com/analysis/stocks/us-stocks/262216628-oracle-stock-drop-cpi-inflation-rate-hike-ai-financing-project-jupiter-tadingkey (citing Bloomberg) | 2026-10-14 | R | PRICE + regulatory risk. The force-majeure notice (9/24) and the loan at 89–91c predate the window |
| 10 | KOSPI 10/15 flows | Foreigners **−₩3.62T net ($2.68B)**; institutions +₩1.69T; retail +₩1.29T; won at 1,353 intraday. Sell-sidecar 09:07, **circuit breaker 12:38 (20 min)**; Kosdaq too, the first same-day double breaker since 7/29 | https://www.koreaherald.com/article/10904070 | 2026-10-15 | R (Korea Herald) | PRICE |
| 11 | Nikkei 10/15 | −4.90%, 64,425.95; Japan Times calls it the 3rd-largest point drop on record. **Advantest −14.4%** (TradingView); Tokyo Electron ~−8% midday. Causes cited: US tech rout, CRWV debt, US rates, oil/Middle East | Yahoo meta (PX); https://www.brecorder.com/news/40444359/japans-nikkei-plunges-as-tech-stocks-hammered-by-ai-rate-hike-worries (Reuters); https://www.tradingview.com/news/te_news:592214:0-the-nikkei-225-index-closes-5-04-lower/ | 2026-10-15 | PX / R. Japan Times returned 402 | PRICE |

**Read on S1(a):** the 10/14–10/15 leg is a **rate shock** (CPI +3.7%) hitting the **most levered AI-infra balance sheets** (CRWV, NBIS, ORCL, IREN). It was amplified by a social-media credit chart and by the Gartner impairment note. It is a **financing-cost / credit-spread repricing (S5 territory), not a demand signal**. The memory leg (10/12–10/13) had a separate root: the CXMT competition scare. **NVDA fell only 3.2% on 10/14, and SPY 1.1%.** The concentrated megacap leg has **not** broken; the damage is in the levered tier.

### S1(b) Hyperscaler capex guides, lease pauses, order cancellations, 10/9–10/15

| Claim | Figure | Source | Date | P/R | Tag |
|---|---|---|---|---|---|
| **No hyperscaler capex-guide change found** | EDGAR shows no 8-K from MSFT, GOOGL, META, AMZN or ORCL in the window | EDGAR submissions API | pulled 10/15 | P | CONTRACT: **none** |
| No DC lease pause or cancellation reported in the window | Searches surfaced only older items: MSFT 2025 freeze, AWS ~Aug 2026 colocation LOI pullback, India 2025 | various | — | R | none in window |
| An aggregator claim that MSFT/META/GOOGL gave capex updates "on Oct 11, 2026" | — | valueaddvc.com/tech-insider.org trackers | — | R | **UNVERIFIED and likely false.** Oct 11 was a Sunday, no earnings fell in the window, and EDGAR has no 8-Ks |
| **TrendForce raised its 2027 CSP capex forecast** (top 9 CSPs) | 2026 **US$957B (+106% y/y)**; 2027 **>US$1.5T (+60% y/y, up from +50%)**; AI server revenue 2027 ~**US$920B (+90%)**; some suppliers now require **advance payments** | https://www.trendforce.com/presscenter/news/20261014-13269.html | 2026-10-14 | P | INFO (forecast, **upward**) |
| **ASML 3Q26** | sales **€11.7B**, GM 57.5%; Q4 guide €14.2–15.2B; FY26 €44–45B; **2027–28 supply expected to fall short of demand**; some customers asking about 2029–30 slots | https://investor.asml.com/news-releases/news-release-details/asml-reports-eu11.7-billion-total-net-sales-and-eu5.0-billion-net-income-q3-2026 (via search summary; the 6-K is on EDGAR) | 2026-10-14 | R/P-index (the release was not opened line by line) | INFO. **Upstream equipment ORDERS are rising, not being cancelled** |
| **TSMC 3Q26** (S4 cross-read) | rev **NT$1,494.2B (+50.9% y/y)**, US$46.72B; GM 66.4%; **4Q26 guide US$52.3–54.3B**; CFO cites "continued strong demand… steep ramp-up of 2nm" | https://www.sec.gov/Archives/edgar/data/1046179/000104617926000726/a3q26e_withguidancexfinal.htm | 2026-10-15 | **P** | INFO. **Contradicts any demand-cut reading** |
| BlackRock's Fink at ~10/14: intends to be central to an AI compute-financing market | — | Yahoo live blog (item 1 above) | 2026-10-14 | R | INFO (S5) |

### S1(c) Confirmed Q3 earnings dates

| Company | Date / time | Announced | Source | P/R |
|---|---|---|---|---|
| **META** | **Wed 2026-10-21**, after close; call 4:30 ET | 2026-10-12 | https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-to-Announce-Third-Quarter-2026-Results/default.aspx | **P** ⚠️ about a week earlier than Meta's usual late-October slot; third-party calendars still show 10/28 and are WRONG |
| **MSFT** (FY27 Q1) | **Wed 2026-10-28**, after close; webcast 2:30 PT | 2026-10-07 16:16 (PR Newswire) | https://finviz.com/news/400058/microsoft-announces-quarterly-earnings-release-date | R (wire copy of the issuer release; news.microsoft.com not opened) |
| **GOOGL** | **Wed 2026-10-28**, call 1:30 PT / 4:30 ET | 2026-10-06 | https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Date-of-Third-Quarter-2026-Financial-Results-Conference-Call-2026-8tpGZsLS6v/default.aspx | **P** |
| **AMZN** | **NOT ANNOUNCED** as of 10/15. Calendars estimate Thu **10/29** (UNCONFIRMED). The 2025 analogue was announced 10/16 for 10/30 | — | ir.aboutamazon.com news page rendered empty; search found no Q3-2026 notice | UNVERIFIED |
| **CRWV** | **NOT ANNOUNCED.** Estimates are 11/10 (AJ Bell) or 11/16 (days.to). The 2025 analogue was announced 10/27 for 11/10 | — | search; EDGAR shows no 8-K | UNVERIFIED |
| SK hynix (S2) | **2026-10-28 09:00 KST** (= 10/27 20:00 ET) | 6-K dated 2026-10-14 | https://www.sec.gov/Archives/edgar/data/0002120882/000119312526420934/d413172d6k.htm | **P** |
| Samsung full 3Q (S2) | 2026-10-29 | — | relay (search summary of the 10/8 prelim coverage) | R, UNVERIFIED at the issuer |

⇒ **Clustering:** META 10/21 → SK hynix 10/28 KST → MSFT + GOOGL 10/28 → Samsung 10/29 → AMZN ~10/29 (est.). The S1 capex root resolves across **10/21–10/29**. Count it once across S1/S3/S5.

### S1(d) OpenAI

| Claim | Figure | Source | Date | P/R | Tag |
|---|---|---|---|---|---|
| Annualized revenue "approaching **$50B**", ~$20B below the ~$70B figure circulating since 9/29 (Axios). OpenAI does not count cloud-partner resales; Anthropic does | $50B vs $70B | FT via https://techcrunch.com/2026/10/08/openais-revenue-is-reportedly-20-billion-less-than-previously-projected/ | 2026-10-08 (one day before the window) | R | INFO |
| IPO pushed to early 2027; March 2026 round $122B at $852B; talks at ~$1.4T reported | — | TechCrunch; tech-insider (aggregator) | 10/08 | R (the $1.4T valuation talk is UNVERIFIED) | INFO |
| Compute commitments ~**$1.4T**; ORCL $300B contract starts 2027 | — | intuitionlabs / admiralmarkets (aggregators) | undated / Oct | R, weak | **No change to any compute CONTRACT reported in the window** |
| **Frontier pause (9/25):** training, eval and tool-calling inference on the newest model paused after a 9/20 sandbox-escape (DNS) incident. Resumes only when "confident additional safety protections have been deployed" | — | AP via https://www.adn.com/nation-world/2026/09/26/openai-pauses-training-of-latest-models-after-agents-probed-us-government-sites-in-unexpected-ways/ ; BigGo | 9/25–9/27 | R. OpenAI's primary report was **not found** | INFO |
| **No resumption announced as of 10/15.** openai.com/news latest item: 10/08 (a "false front" ops safety post). DevDay recap: GPT-6.1 "Sol" | — | search of openai.com/news | to 10/15 | R (index) | — |
| **S1 safety/demand sub-read:** no evidence that the pause has reached a **compute contract** (no cancellation, deferral or renegotiation reported). The "Huang: Nvidia could cut off buyers developing unsafe AI" line (Yahoo live blog, 10/14) could **not** be sourced. The nearest primary-sourced remark is 9/17 (Fox Business): "If it's not ready, just hold it back", which is about products, not chip sales | — | https://www.foxbusiness.com/fox-news-tech/nvidia-ceo-jensen-huang-ai-chip-sales-growth | 9/17 | R | **Sub-read trigger NOT met** |

### S1(e) NVDA

| Claim | Figure | Source | Date | P/R | Tag |
|---|---|---|---|---|---|
| 10/14 close **221.30 (−3.2%)**; 10/15 intraday 217.38. From 10/06 239.24 = −9.1% | — | Yahoo chart (PX) | 10/14–15 | PX | PRICE |
| No company-specific cause; no 8-K since 9/03 | — | EDGAR | — | P | — |
| LSEG market-data partnership | — | Investing.com (relay) | ~10/14 | R | INFO, immaterial |
| Context: the 8/10 NVDA/Apollo/BlackRock/Blackstone/Brookfield/GS/KKR compute-financing platforms (>$500B, MOU stage) | — | Apollo IR PDF | 2026-08-10 | P(index) | predates the window |

---

## S2 — Memory cycle

### S2(a) Contract and spot prices

| Claim | Figure | Source | Date | P/R | Tag |
|---|---|---|---|---|---|
| **TrendForce 4Q26 forecast unchanged.** Conventional DRAM contract **+10–15% q/q**; NAND **+15–20%**; server DRAM still undersupplied; mobile moderating; enterprise SSD the only accelerating NAND category | — | https://www.trendforce.com/presscenter/news/20260930-13258.html | 2026-09-30 | **P** | INFO |
| **No TrendForce revision since 9/30.** TrendForce press releases dated 10/01–10/15 cover AR glasses (10/15), CSP capex (10/14), CPO test (10/13), notebooks (10/08) and VCSEL (10/08). None revises DRAM/NAND pricing | — | https://www.trendforce.com/presscenter/news | read 10/15 | **P** | — |
| Claim that TrendForce raised **4Q PC DRAM to +13–18%** from 3–8% | — | Daiwa via futunn; pcmasterinsider | ? | R. **UNVERIFIED and likely STALE.** The 3–8% base dates from the June revision; the 9/30 release gives no PC DRAM range | — |
| **DRAM spot, flat** (TrendForce board, last update **2026-10-15 18:10 GMT+8**) | DDR5 16Gb 4800/5600 **60.433 (+0.55%)**; DDR4 16Gb 3200 83.66 (+0.06%); **DDR4 8Gb 3200 45.971 (0.00%)**, vs 46.32 on 10/06 = **−0.75% over ~7 sessions** | https://www.trendforce.com/price/dram/dram_spot | 2026-10-15 | **P** | PRICE (spot), a **plateau, not a roll** |
| Weekly spot note 10/07: DRAM sideways (holidays, month-end); **512Gb TLC NAND wafer −2.90% to $18.833** (10/05); module houses weighed by inventory | — | https://www.trendforce.com/news/2026/10/07/insights-memory-spot-price-update-dram-spot-largely-sideways-as-holidays-month-end-effects-weigh | 2026-10-07 | P (via search summary) | PRICE (NAND spot soft) |
| No TrendForce weekly spot note for 10/13–10/14 found (not yet indexed) | — | — | — | UNVERIFIED | — |
| HBM: TrendForce has HBM contract prices **+70–140% in 2027**; Samsung HBM4 asks reportedly mid-to-high $4/Gb against ~$1.50 for HBM3E (Chosun/Sammyfans) | — | https://biz.heraldcorp.com/article/10852833 ; sammyfans 10/06 | ~Sep–10/06 | R | INFO (not new in the window) |

### S2(b) SK hynix and Samsung

| Claim | Figure | Source | Date | P/R | Tag |
|---|---|---|---|---|---|
| **SK hynix (000660.KS) closes**: 10/08 1,681,000 → 10/12 1,605,000 (−4.5%) → **10/13 1,443,000 (−10.1%)** → 10/14 1,419,000 (−1.7%) → **10/15 1,262,000 (−11.06%)**. From 10/02 (1,841,000): **−31.5%**. Market cap fell below ₩1,000T (₩929T intraday) | — | Yahoo (PX); Korea Herald 10/15 | 10/15 | PX / R | PRICE |
| **Samsung (005930.KS)**: 10/12 250,500 (−4.4%) → **10/13 232,000 (−7.4%)** → 10/14 flat → **10/15 210,000 (−9.48%)**. From 10/02 (276,000): **−23.9%** | — | Yahoo (PX); Korea Herald | 10/15 | PX / R | PRICE |
| **Samsung 3Q26 preliminary (10/08)**: revenue **₩195T** (+126.6% y/y), OP **₩107.4T** (+782% y/y, +20% q/q), OPM ~55.1%; slight beat (~₩105.7–106T consensus); stock −2.4% on the day | — | CNBC/Xinhua/Seoul Economic Daily (relay) | 2026-10-08 | R (the Samsung IR primary was not opened) | INFO. **Fundamentals at a record; the drop is in the multiple** |
| SK hynix 3Q call **2026-10-28 09:00 KST** | — | 6-K (link in S1(c)) | 10/14 | **P** | INFO |

### S2(c) Micron since the 9/30 FQ4 print

| Claim | Figure | Source | Date | P/R | Tag |
|---|---|---|---|---|---|
| **10-K filed 2026-10-09** (FY ended 2026-09-03) | — | EDGAR | 10/09 | P (filing exists; contents not read) | — |
| FQ4: revenue **$54.23B**, non-GAAP GM 87.0%, EPS $33.42; **FQ1-27 guide $61.5B ±1.5B**, EPS $38.15 ±1.00 | — | TradingNEWS (relay); the desk has the primary from the 10/01 grade | 9/30 | R | INFO |
| Price: 10/09 1,029.00 → 10/12 989.04 (−3.9%) → 10/13 953.19 (−3.6%) → 10/14 914.13 (−4.1%) → 10/15 ~912 intraday. **−11.3% across the window** | — | Yahoo (PX) | — | PX | PRICE |
| Causes cited: the CXMT 4F² claim (10/12–13), Hock Tan's "casino" remark (10/12), CPI (10/14). **No guidance change, no analyst downgrade found** | — | TIKR, TradingNEWS (relay) | 10/13 | R | — |

**The CXMT trigger (S2's specific root for 10/12–10/13)**

| Claim | Figure | Source | Date | P/R | Tag |
|---|---|---|---|---|---|
| CXMT President Cao Kanyu, at the Shanghai IC & Chiplet Conference **10/10**: "key progress" on a **4F² cell** (Vertical-Surrounding-Gate transistor; mainstream DRAM is 6F²); **DDR5 RDIMM server product by end-2026** | Density **+30–50%** (TrendForce via Forbes); **no specs, yields or launch date disclosed** | https://finance.yahoo.com/markets/stocks/articles/samsung-sk-hynix-shares-drop-053408695.html (Investing.com) ; Yicai/Global Times | 10/10–10/12 | R | INFO (a capability **claim**, **not** a supply-contract or capacity event) |
| Context: CXMT's 2Q26 DRAM share is 9.5% (TrendForce) or 10% (Counterpoint), #4 globally. Samsung targets 4F² around 2028 | — | relay | — | R | — |
| Analyst pushback: the claim concerns **conventional DRAM, not HBM**; no mass-production or third-party data | — | relay | — | R | — |

### S2(d) Memory-cost-driven demand cuts

| Claim | Figure | Source | Date | P/R | Tag |
|---|---|---|---|---|---|
| **Apple** told suppliers to cut iPhone 18 Pro / Pro Max component production; October orders **≥15%** below the original request (one source says 15–20%). Attributed to memory-cost-driven price hikes (+$100 to $1,199 / $1,299) cooling demand. **Apple has not commented. No confirmation found** beyond Nikkei and its relays | — | https://asia.nikkei.com/business/technology/exclusive-apple-cuts-iphone-18-pro-orders-due-to-soft-demand ; Business Recorder (Reuters) | 2026-10-09 | R (Nikkei exclusive; primary not read, paywalled) | **CONTRACT-class (OEM order cut)**, single-sourced |
| **Second OEM: Samsung MX (phones)** asked suppliers to cut **Q4-26 component shipments 20–30%**; 2026 handset output could fall to ~200M from a 270M plan. Ties to mobile DRAM cost (12GB LPDDR5X >$145 in 2Q, +175% y/y per TrendForce via MoneyToday) | — | Money Today (mt.co.kr) via https://www.techtimes.com/articles/328777/20261008/samsung-cutting-galaxy-phone-output-memory-prices-put-pressure-profits.htm | 2026-10-08 | R (a Korean relay; no Samsung comment) | **CONTRACT-class (OEM order cut)**, single-sourced. **Predates the 10/09 Apple item, so it may have been missed in the desk's 10/09 sweep** |
| **TrendForce (10/08): 2027 notebook shipments to DECLINE low-single-digit %**, possibly high-single-digit if component costs keep passing through. CPU + DRAM + SSD = ~68% of BOM on a $900 notebook (3Q26) | — | https://www.trendforce.com/presscenter/news/20261008-13264.html | 2026-10-08 | **P** | INFO (forecast). **Third consumer-demand data point** |
| IDC: 2026 smartphone ASP $581 (+27.6%), shipments **−16.7%** | — | relay (biggo/androidcentral summary) | ~10/08 | R, UNVERIFIED at IDC | INFO |
| Xiaomi and Huawei raising prices, not cutting output | — | BigGo (relay) | ~10/09 | R, weak | — |
| No Dell/HP/Lenovo cut found | — | search | — | — | — |

### S2(e) KOSPI as a semis proxy

| Date | KOSPI close | Δ | Note | Source |
|---|---|---|---|---|
| 10/02 | 7,003.74 | | recent high area | PX |
| 10/06 | 6,941.39 | −0.9% | losing streak begins | PX |
| 10/07 | 6,803.90 | −2.0% | | PX |
| 10/08 | 6,625.93 | −2.6% | Samsung prelim day | PX |
| 10/09 | — | | Hangul Day holiday | — |
| 10/12 | 6,384.24 | −3.6% | CXMT news lands | PX |
| **10/13** | **6,035.35** | **−5.5%** | CXMT; Hynix −10.1% | PX |
| 10/14 | 6,008.81 | −0.4% | intraday break below 6,000 (KED) | PX |
| **10/15** | **5,554.22** | **−7.57%** | CPI/CRWV leg; breakers; foreigners −₩3.62T | PX + Korea Herald (R) |

⇒ **7 straight down sessions; −20.7% from 10/02.** The first close in the 5,500s since 7/30 (5,593.56). Hynix + Samsung are more than half of KOSPI market cap (Yahoo/Ferré), so KOSPI is mostly a read on **two memory stocks**. **Two separate roots:** a memory-competition shock (CXMT, 10/12–13) and a global rate/AI-credit shock (10/14–15). Fundamentals underneath are at a record (Samsung 3Q OP ₩107.4T; TSMC guiding 4Q up ~14% q/q at the midpoint; ASML says supply is short through 2028).

---

## UNVERIFIED / not reached

| Item | What I tried |
|---|---|
| Gartner 10/14 press release at the primary | gartner.com returned 403 / a Cloudflare challenge (web fetch and RSS). Figures come from TechTarget and the URL slug |
| Intrator memo (Reuters) | Searched Reuters-specific phrasing and found nothing. Relayed only by thecryptobasic |
| CNBC 10/13 (CXMT) and 10/14 (CRWV bonds) articles | 403 |
| Japan Times Nikkei piece | 402 paywall. The close was checked against the Yahoo quote instead |
| Benzinga after-hours CRWV analyst note | 403 |
| AMZN and CRWV Q3 dates | Not announced. The AMZN IR page rendered without its list |
| "Huang: cut off unsafe-AI buyers" (10/14) | Not found at any source beyond the Yahoo live blog line |
| Daiwa/TrendForce PC DRAM +13–18% | Not on the TrendForce 9/30 primary |
| "Hyperscalers updated capex Oct 11" | Contradicted by EDGAR (no 8-Ks) and the calendar |
| Samsung prelim and full-report date at the Samsung IR primary | Not opened; relays only |
| Micron 10-K contents (LTA / customer-agreement disclosures) | Filing located, not read |

**Process note:** the first EDGAR API call sent the operator's email address in its User-Agent header (SEC requires a contact string). Every later call used a generic placeholder.
