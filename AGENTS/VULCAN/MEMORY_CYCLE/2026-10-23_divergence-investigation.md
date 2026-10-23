# Idea #1 — "Where the puck is going": memory equities vs contract prices

**Desk:** VULCAN (S2 memory channel) · **Written:** 2026-10-23 16:07 EDT (from `date`) · **Type:** research only. No trade, size or order is proposed here; TERRY builds cards, Will approves (root rule #5).
**Tiers:** T1 = primary (company release/filing, SEC XBRL, own fetch) · T2 = named outlet read directly · T3 = search summary/relay. UNVERIFIED = not confirmed at any tier.

---

## Bottom line

1. **The divergence is real and wider than on 10/16, but the contract side has not moved.** Memory equities are 28–56% below their June 2026 peaks (own fetch, 10/23 close), while TrendForce's public 4Q26 forecast (conventional DRAM +10–15% QoQ, NAND +15–20%, 9/30) is unrevised. The only "new" number, ~20% QoQ (StockHub/Commercial Times relay, 10/20), is a relay, not a TrendForce revision (KB-253). DDR5 spot is up +1.1% week over week and DDR4 is flat. This week's spot data shows no sign of a roll.
2. **Half of the desk's "−17.9% memory basket" is hard-disk makers.** `semi_watch.py` averages MU/SNDK/WDC/STX equally. WDC and STX make HDDs, which carry their own supply shock (Toshiba doubling capacity, 10/02, KB-192). The pure-semiconductor half (MU, SNDK) was −14.8% on the 10/16 row. The divergence is still real but smaller than the headline.
3. **History says equity leads contract by about 4–5 months, and the stocks bottom around when the contract forecast turns, not before.** In 2018 MU fell 28% from its peak while contract prices rose 0–2%. Contracts rolled in October, and the stock fell to −54% at the trough two months later. In 2021 MU fell 31% before TrendForce cut its Q4 outlook (9/22). The stock bottomed three weeks after the cut (10/13). MU peaked 6/25/2026, four months ago, so the 2026 timing matches both analogs.
4. **Valuation already discounts the earnings.** MU trades at ~5.0x consensus FY27 EPS but 7.2x book. 2019 and 2022 troughs were ~1.0–1.3x book. On book value the stock is far from a trough multiple. The market is pricing peak earnings, not a cheap asset.
5. **The 10/28–29 prints decide it.** If SK hynix or Samsung cite customer order cuts or inventory digestion, the 2018/2021 analog says the stocks still have one leg down. If both confirm 2027 supply is contracted and say nothing of cuts, the equity drawdown is a thermometer reading and the gap should close upward.

---

## 1. Contract and spot evidence after 9/30

| Item | Value | Date | Tier / source |
|---|---|---|---|
| TrendForce 4Q26 conventional DRAM contract | **+10–15% QoQ** (unrevised) | pub. 9/30; restated in 10/21 spot note context and NextMSC tracker 10/9 | T1-ish public PR (KB-187); restated T3 [TrendForce spot 10/21](https://www.trendforce.com/news/2026/10/21/insights-memory-spot-price-update-ddr5-supply-tight-ddr4-trading-subdued-despite-0-84-gain-in-mainstream-prices/) |
| TrendForce 4Q26 NAND contract | **+15–20% QoQ** (unrevised) | 9/30 | same |
| "~20% QoQ 4Q26 DRAM" | relay of Commercial Times; StockHub AI summary attributes it to TrendForce. Prior quarters ~+80% (2Q) and ~+40% (3Q). Drivers: "high base, weakening purchasing power, gradual application of LTA price caps" | 10/20 | T3 [StockHub](https://www.stockhub.kr/en/news/news_b7244c205001); KB-253. **Not a research revision.** Perimeter probably includes HBM, since 9/30's all-in was 15–20% |
| TrendForce 1Q27 contract forecast | **Not published.** None found; a 1Q27 outlook usually appears late Dec | — | T3 search, 10/23 |
| DDR5 16Gb spot session avg | **$61.267 (+0.27% d/d)** vs $60.60 on 10/16 ⇒ **+1.1% w/w** | 10/23 18:10 GMT+8 | T2 [TrendForce spot table](https://www.trendforce.com/price/dram/dram_spot), read directly; 10/16 from S2_SERIES |
| DDR4 16Gb spot | $82.87 (−0.30% d/d) vs $83.66 on 10/16 ⇒ −0.9% w/w | 10/23 | same |
| DDR4 8Gb (1Gx8 3200) spot | $47.107 (+0.23% d/d); weekly avg +0.84% to $46.357 (wk of 10/20) | 10/23; 10/21 | T2 TrendForce |
| DDR5 spot commentary | "supply remains tight and suppliers are clearly reluctant to sell"; buyers raising targets "still cannot secure allocation" | 10/21 | T2 TrendForce |
| DDR4 commentary | module houses "strictly controlling capital and inventory… trading sentiment subdued" | 10/21 | T2 TrendForce |
| NAND 512Gb TLC wafer spot | **$18.592, −1.28% w/w**; "narrow trading range" | wk of 10/19 | T2 TrendForce |

**Verdict Q1:** Nothing changed on the contract side. DRAM spot is flat to slightly up. NAND wafer spot slipped −1.3%, the only soft print, and wafer spot is a small, noisy market. **The pre-registered "TrendForce cuts a contract forecast" leg has NOT fired.**

## 2. Samsung, SK hynix and HBM

| Item | Value | Tier / source |
|---|---|---|
| Samsung Q3 prelim (10/08) | Sales ~KRW195T, OP ~KRW107.40T (+20.0% QoQ, ×8.8 YoY); OP margin ~55.1%. No division split | T1 (KB-196) |
| Samsung pre-prelim DS (memory) estimate | ~KRW110T (down from >113T); MX reportedly ~KRW1.5T operating loss on memory costs | T3 [search summary of FnGuide/press](https://www.sammyfans.com/2026/10/07/samsung-q3-2026-profit-ai-chip-demand/amp/). UNVERIFIED at primary |
| Samsung full Q3 | 10/29 | desk KB-226 |
| SK hynix Q3 release | **before 09:00 KST 10/28**, call 09:00 KST (company notice; 6-K 10/14) | T1 [SEC 6-K](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526420934/d413172d6k.htm) via search; MoneyToday's "29th" and AJ Bell's 10/29 call date conflict with the company notice |
| SK hynix Q3 OP consensus | **KRW76.96T**, OPM ~78.4% (FnGuide, 10/19); down from ~78.8T (9/15) on won strength. Hana 77.9T (+29% QoQ); DS 70T | T2 [MoneyToday 10/19](https://www.mt.co.kr/en/industry/2026/10/19/2026101913371799572); others T3 |
| SK hynix Q2 actual (base) | Rev KRW79.32T, OP 60.54T (76% OPM); 2026 capex raised to "high-40 trillion won" | T3 [Tom's Hardware via search](https://www.tomshardware.com/tech-industry/sk-hynix-operating-profit-rises-557-percent); capex wording UNVERIFIED at transcript |
| SK hynix Q4 OP consensus | KRW87.27T (FnGuide) | T2 MoneyToday |
| HBM 2027 allocation | **Mostly contracted, price unsettled at Samsung.** MU: "vast majority" of CY27 HBM bits contracted at "significant price increases" (T1, KB-188). Samsung: final-stage price talks with Nvidia/Broadcom, "large share" of 2027 orders secured (Chosun Biz via SammyFans 10/06, T3). DigiTimes: all three makers allocated 2027 DRAM+HBM, buyers getting 60–70% of requests (T3). TrendForce 8/17 bulletin: 2027 HBM talks "stuck" since 2Q26 (T3). SK hynix 2027 HBM4 close: **not found** | mixed |
| HBM 2027 price | TrendForce blended HBM ASP **+121% YoY** (KB-179) | T2 |

**Management language to watch on 10/28–29:**

| Confirms the bear (stocks right) | Falsifies the bear (contract right) |
|---|---|
| "customers adjusting/digesting inventory", "order adjustments", "pull-in normalization", any named customer cut | "2027 supply sold out / fully allocated" for DRAM and HBM, said on the call |
| 4Q bit-shipment guide down QoQ, *or* ASP guide below TrendForce's +10–15% | 4Q DRAM ASP guided up ≥ high-single/low-double digits |
| Mobile/PC "demand destruction" extending to *server* | Mobile weakness confined to consumer, server "undersupplied" |
| Capex *raised* again for 2027 conventional DRAM/NAND (supply response) | Capex steered to HBM/packaging only; conventional wafer adds flat |
| HBM4 2027 price "not finalized" plus volume reallocation | HBM4 2027 price and volume "finalized" |

## 3. Equity drawdowns (own fetch)

Quotes from `fetch.py price`, fetched 2026-10-23T20:04:21Z–20:04:28Z, as-of 2026-10-23 (US = regular-session close; Korea = 10/23 KRX close). Peaks and history from yfinance (`.venv`, 1y daily closes, unadjusted), pulled 10/23 ~20:05Z. **T1 own fetch.**

| Ticker | 10/23 close (day) | 52-wk peak (date) | Peak→now | Post-8/1 high (date) | From post-8/1 high | ~1 mo (9/23→10/23) |
|---|---|---|---|---|---|---|
| MU | **$877.55** (+2.46%) | $1,213.56 (6/25) | **−27.7%** | $1,097.39 (10/01) | −20.0% | −18.1% |
| SNDK | **$1,238.03** (−1.82%) | $2,335.00 (6/25) | **−47.0%** | $1,887.04 (9/22) | −34.4% | −31.9% |
| WDC (HDD) | **$343.67** (−2.97%) | $746.23 (6/18) | **−53.9%** | $548.56 (8/04) | −37.4% | −27.4% |
| STX (HDD) | $630.49 | $1,094.04 (6/22) | −42.4% | — | — | −31.8% |
| 000660.KS SK hynix | **₩1,277,000** (+4.42%) | ₩2,919,000 (6/22) | **−56.3%** | ₩1,868,000 (9/21) | −31.6% | −31.4% |
| 005930.KS Samsung | **₩215,500** (+0.47%) | ₩362,500 (6/18) | **−40.6%** | ₩285,500 (9/23) | −24.5% | −24.5% |

Notes: (a) Korean names show ±25–30% single-day moves (7/31: hynix +30.0%, Samsung +26.8%). These are confirmed real by T3 press ("rebound near 30%"), not split artefacts. (b) Equal-weight MU/SNDK/WDC/STX over 9/23→10/23 = **−27.3%**. This is my window, **not** a cadence row; tonight's registered S2 row will differ. (c) **Basket composition caveat:** on the 10/16 cadence row, MU+SNDK alone were −14.8% vs the −17.9% four-name mean. HDD drawdowns carry a separate supply root (Toshiba capacity, KB-192).

## 4. Valuation context

| Metric | Now | Prior troughs/peaks | Source / tier |
|---|---|---|---|
| MU market cap | $992.9B (877.55 × 1,131.4M sh) | — | shares: 10-K cover 10/02 (SEC XBRL, T1) |
| MU P/B | **7.2x** (equity $138.4B at 9/03/26; BVPS $122.30) | **0.97x** May-2019 · **1.22x** Aug-2022 · 1.32x Feb-2023 · 10-yr median 1.98x, max 15.1x | equity T1 SEC 10-K; history T3 [Macrotrends](https://www.macrotrends.net/stocks/charts/MU/micron-technology/price-book), [GuruFocus](https://www.gurufocus.com/term/pb-ratio/MU) |
| MU trailing GAAP P/E | **11.7x** (FY26 NI $84.97B) | ~4x TTM in Sep-2018 (near the cycle's EPS peak) | T1 own calc; 2018 T3 [Motley Fool 9/12/2018](https://www.fool.com/investing/2018/09/12/microns-rock-bottom-pe-ratio-doesnt-tell-the-whole.aspx) |
| MU forward P/E | **~5.0x** FY27 consensus EPS $174.31; ~5.75x on FQ1 guide $38.15 × 4 | Benzinga 10/12: 5.6x at a higher price | consensus T2/T3 [Benzinga via Webull 10/12](https://www.webull.com/news/15737045709186048) |
| SNDK / SK hynix forward P/E | 6.9x / 4.1x (10/12 prices; lower now for hynix) | — | same, T3 |

**Read:** A ~5x forward multiple is what a *peak* cycle looked like in 2018 (~4x TTM). On book value, MU is ~6x above prior trough multiples. "Cheap on P/E" is the classic peak-cycle trap. The investment question is whether FY27 EPS of $174 holds. The P/E does not answer it.

## 5. Historical analogs: equity fell >15% while contract still rose

All prices are own yfinance fetch (T1, unadjusted closes). Contract facts are TrendForce/DRAMeXchange releases.

| Episode | Equity peak | Equity drawdown while contract still up | Contract turn (source) | What came next |
|---|---|---|---|---|
| **2018** | MU $62.62 (5/29/18) | **−27.8%** to $45.23 (9/30/18) while 3Q18 PC/server/mobile contract **+0–2% QoQ** ([DRAMeXchange 11/15/18](https://dramexchange.com/WeeklyResearch/Post/2/5145.html), T2) | Contract "started to slide in October"; 4Q18 ASP ~−8% ([TrendForce 12/4/18](https://www.trendforce.com/presscenter/news/20181204-10078.html)); 1Q19 forecast raised to **~−20%** ([1/15/19](https://www.trendforce.com/presscenter/news/20190115-10093.html)) (T3 summaries of these) | MU fell further to **$29.02 (12/24/18), −53.7%** from peak, ~2 months after the turn and ~7 months after the equity peak; recovered to $53.78 by 12/31/19 |
| **2021** | MU $95.59 (4/12/21) | **−30.6%** to $66.38 (10/13/21); contract rose through 3Q21 | TrendForce 9/22/21: 4Q21 DRAM ASP **−3–8%**, PC DRAM −5–10% ([PR](https://www.trendforce.com/presscenter/news/20210922-10947.html), T3 summary) | Stock **bottomed 3 weeks after the cut** and returned to $93.15 by 12/31/21. The real down-cycle came in 2022 (MU $48.88, 9/26/22) |
| **2026 (now)** | MU $1,213.56 (6/25/26) | −27.7% to $877.55 (10/23); 4Q26 contract forecast +10–15% | **No turn yet** | ? |

**Pattern (n=2, small):** both times equity led the contract turn by **~4–5 months**. 2026 is at month 4. In 2018 the contract turn brought a *second leg* (−28% → −54%). In 2021 it marked the *low*. What separated them was whether the turn was steep (2018: −8% then −20%) or shallow (2021: −3–8%). So the variable to forecast is the **size** of any 1Q27 decel, not its sign. One structural difference also matters: in 2026, >35% of MU revenue is in multi-year SCAs with floor/ceiling bands (T1, KB-188). Neither 2018 nor 2021 had this, so contracts may be slower to fall and slower to rise.

## 6. Bear case: evidence now

| Bear claim | Evidence | Strength |
|---|---|---|
| OEM demand destruction | IDC Q3 phones **−22.0% YoY** (255.3M; IDC blames memory cost) [KB-230, T2]; Apple ≥15% iPhone 18 Pro Oct component cut (relay, KB-205); Samsung MX Q4 component cut 20–30% (relay, KB-221); Jefferies weak iPhone 18 Pro lead times (relay, KB-254); Samsung MX ~₩1.5T loss (T3) | **Strong on units, unconfirmed by any OEM** (upgrade leg not fired) |
| Customer inventory build / double-ordering | Hyperscalers placed "open-ended orders" (NAND Research, T3); TrendForce 3Q: server DRAM undersupplied, buyers building inventory (via TechTimes, T3); module houses "strictly controlling… inventory" (TrendForce 10/21, T2). **No report of cancellations or digestion found** | Plausible mechanism, **no direct evidence** |
| Price elasticity / LTA caps | TrendForce: 4Q gains narrowing on "weakening purchasing power" and "LTA price caps" (relay 10/20); 9/30: some suppliers to lag the average on LTA terms (KB-187); Kioxia CEO resisting hikes (KB-161) | Real, but caps the *upside*; does not signal a fall |
| China supply | CXMT: ~320k wpm → ~420k by 2027 (Commercial Times via TrendForce, T3); 4F2 cell + DDR5 RDIMM by end-2026 claimed, full 4F2 commercialization after 2028 (KB-222; StockHub 10/20); 2Q26 share 9.5%. YMTC: third Wuhan fab end-2026, ~50k wpm from 2027, half reportedly DRAM (heise/TrendForce, T3). TrendForce: no meaningful global impact "until 2027 or later" | **2027–28 risk, not 4Q26**; the 10/10–15 KOSPI rout was triggered by CXMT headlines (KB-215) |
| Incumbent supply response | MU FQ1 capex ~$11.5B, 1H FY27 ~$25B, higher in 2H (T1, KB-186); SK hynix 2026 capex "high-40T won" vs 30.2T in 2025 (T3); Lam CY27 WFE outlook >$200B vs 2026 $140B+ (call relay, KB-272) | **The strongest bear leg.** WFE +40%+ implies a 2027–28 bit-supply wave; this is the 2018 mechanism |
| Rate/credit backdrop | US 10Y 5.10% (10/16); HY selloff (STATUS 10/23) | Multiple compression independent of memory |

## 7. Supply side and Solidigm

| Maker | 2026–27 capex signal | Source |
|---|---|---|
| Micron | FQ1 FY27 ~$11.5B; 1H FY27 ~$25B, 2H higher (≈$50B+ run-rate, extrapolation); Idaho/NY fabs, ID1 not before 2027 | T1 8-K (KB-186); T3 timeline |
| SK hynix | 2026 high-40T won (from 30.2T in 2025); M15X accelerated, Yongin Ph1 cleanroom early 2027, M17 NAND; $26.5B ADR raise | T3 (Tom's Hardware, Futurum) |
| Samsung | HBM ~20% → ~30% of DRAM wafer capacity in 2027 (KB-179, T2); Pyeongtaek P4/P5 accelerated; first Yongin fab pulled to 2029 | T2/T3 |
| WFE | Lam initial CY27 WFE >$200B vs 2026 $140B+ | call relay (KB-272) |

**Solidigm halt (10/23, T1 SK hynix newsroom/6-K, KB-271):** the review of pre-IPO/IPO options is halted. SK hynix says US capacity investment needs are "unchanged" and will weigh **direct investment and other external financing**. **Effect on NAND supply: marginal and slow.** No US NAND fab was committed. Reuters had reported a plant "under consideration" (upstate NY a candidate, T3). Any such fab would deliver bits in 2028+ at the earliest. The halt removes an *equity* funding route, not capacity, and the parent says it will fund the need another way. Reading it as "supply discipline" overstates it. At most it is a slightly lower probability of a 2028+ US NAND add. Its clearest content is a **capital-markets signal**: the share-price correction made the IPO unattractive.

---

## Bull vs bear

| Bull: contract decides, equities overshot | Bear: equities see the 1Q27 turn first |
|---|---|
| 4Q26 contract +10–15%/+15–20% unrevised; DDR5 spot +1.1% w/w with sellers withholding | Rate of increase falling fast: ~+80% (2Q) → ~+40% (3Q) → +10–20% (4Q). The second derivative turned in 2Q |
| MU guides "sequential revenue growth each quarter" FY27 and FQ1 as the GM "floor" (T1) | MU's own words: "more moderate rate of price increases"; server content growth "modestly lower than prior expectations" |
| 2027 HBM/DRAM largely allocated; HBM ASP +121% fcst | Allocation at 60–70% of requests invites over-ordering; history (KB-139) shows backlog/allocation data runs 9–27 months *late* |
| SCAs (>35% of MU rev) floor prices | SCA ceilings also cap upside; equity was priced for uncapped spot |
| 2018/2021: equity bottomed within weeks of the contract turn; a shallow turn (2021) marked the low | 2018: a steep turn produced a second leg to −54%. WFE +40% in 2027 is a 2018-style supply wave |
| Fwd P/E ~5x | P/B 7.2x vs ~1x troughs; single-digit P/E is the peak-cycle signature |

---

## Pre-registerable test for 10/28 (SK hynix) and 10/29 (Samsung)

*Drafted 2026-10-23 16:07 EDT, before both prints. First public: none. Neither company has reported Q3 detail.* This proposes wording for VULCAN to register. It does not replace the S2 upgrade legs pre-stated 10/15 in STATUS, which stay governing.

**Definitions.** "Order-cut language" = management or official release text citing customer order reductions, inventory adjustment/digestion, or order cancellation for DRAM or NAND in any end market. "Server-scoped" = applied to server/datacenter/AI. "Supply-sold-out language" = 2027 DRAM or HBM supply described as fully allocated, sold out, or contracted.

| Outcome | Condition (all from the companies' own release/call, 10/28–10/29 KST) | Reading for idea #1 |
|---|---|---|
| **CONFIRMS divergence-as-overshoot (bull)** | **No** order-cut language from either company, **AND** at least one gives supply-sold-out language for 2027, **AND** neither guides 4Q DRAM ASP down QoQ | Equity drawdown was a thermometer; expect contract to stay up through 4Q26; S2 held at 2 |
| **FALSIFIES (bear, stocks were right)** | Order-cut language from **either** company that is **server-scoped**, **OR** either guides 4Q DRAM bit shipments **and** ASP both down QoQ | Contract turn likely in 1Q27; S2 upgrade leg fires (→3 per STATUS 10/15); 2018 analog in play |
| **AMBIGUOUS** | Order-cut language confined to mobile/PC/consumer; or ASP guide positive but below +10%; or capex raised for conventional DRAM/NAND | Not graded either way. Re-test on TrendForce's next contract release (Oct/Nov contract or 1Q27 outlook) |

**Secondary market test (thermometer only, never decisive per VULCAN-11):** by 10/30 close, did MU+SNDK (equal weight) outperform SOXX from the 10/27 close? Record it. Do not use it to grade.

**Kill for the idea itself:** a TrendForce research revision cutting 4Q26 or forecasting 1Q27 conventional DRAM contract **≤0% QoQ** settles the question in the bear's favour, whatever the prints say.

---

## Open questions / what we could not reach

| Gap | Status |
|---|---|
| TrendForce 4Q26 contract research after 9/30 (paywalled monthly contract reports) | Not reached; only public PR and spot notes read |
| October DRAM/NAND *actual* contract settlements (month-end) | Not yet published as of 10/23 |
| SK hynix Q3 revenue consensus; Samsung DS consensus post-prelim | Only OP consensus (T2); DS ~110T is pre-prelim T3 |
| SK hynix 2027 HBM4 contract close | Not found; treat as UNVERIFIED |
| Samsung 2026/27 capex guide | Not found in this pass |
| MU forward P/E at 2018 peak (true forward basis) | Not found; only ~4x TTM (T3) |
| Actual 1Q19 and 4Q21 contract outcomes (vs forecasts) | Forecasts only (T3 summaries of TrendForce PRs) |
| Apple/Samsung MX build cuts company-confirmed | No; relays only (upgrade leg not fired) |
| Cancellations/double-order unwind | No direct evidence found either way |
| 10/23 post-close S2 cadence row | Separate desk instrument, not run here; my 1-month figures use a 9/23→10/23 window |
