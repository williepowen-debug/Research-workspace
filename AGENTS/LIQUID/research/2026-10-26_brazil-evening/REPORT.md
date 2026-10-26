# Brazil evening follow-up — 2026-10-26T17:40:46-04:00

**Assignment:** Will asked whether LIQUID could act now on the closing comparison, participant/cash-demand search, published funding/credit read and Brazilian auction verification. Existing channels only; no new standing collector, trade or gate. Prior daytime assessment remains dated at `../2026-10-26_brazil-transmission/REPORT.md`.

## Result

**The closing comparison strengthens the case for a concentrated Brazilian price shock rather than a demonstrated broad US liquidation. A named pre-event fund/dealer exposure is now documented, but the cash-demand and forced-sale bridge remains missing.** Official Brazilian auction-result access was blocked; reporter-origin evidence advances buybacks from announced offers to reported allotments, not independently verified settlement. October 26 SOFR/ICE have not appeared in the retrieved official/FRED series yet.

| Work possible now | Completed result | Remaining limitation |
|---|---|---|
| Closing comparison | 14 instrument pulls, raw daily US closes plus matched Friday/Monday 5pm NY FX minute proxies, saved | Vendor mirror data; no official FX fix or funding basis; Brazilian index close has conflicting public reports |
| Participant/cash-demand check | Original Brazil Journal reporting independently read; named UBR swap exposure recovered from issuer | Anonymous stops still unnamed; no observed current margin/refusal/liquidation at UBR or any named fund |
| Funding/credit publication check | First-published seven-series pull and NY Fed repo/SOFR saved at 17:35 ET | Last credit/SOFR observation remains October 23; October 27 IORB reference is not a matching new funding observation |
| Brazilian auction check | Latest Reuters reporting and retained LFT scope located; official page/API attempted | HTTP 429/503; no verified allotment/settlement, tomorrow's retained sale has not occurred |

## 1. Closing baseline — October 26 versus October 23

Source: direct yfinance query at roughly **17:35 ET**, `close-comparison.json`; calculations `derived-returns.json`. US securities/index rows are **raw unadjusted daily vendor bars**, not exchange-certified official closes or executable prices. All returned October 26 rows were checked. Price returns exclude distributions and are not portfolio flows or credit-spread changes.

| Object | October 23 raw close | October 26 raw close | Change |
|---|---:|---:|---:|
| Brazil ETF EWZ, USD | $42.59 | $34.15 | −19.82% |
| US high-yield ETF HYG, USD | $77.05 | $77.20 | +0.19% |
| US investment-grade ETF LQD, USD | $103.85 | $104.02 | +0.16% |
| Dollar EM sovereign ETF EMB, USD | $91.65 | $91.50 | −0.16% |
| Senior-loan ETF BKLN, USD | $20.26 | $20.30 | +0.20% |
| US regional-bank ETF KRE, USD | $72.46 | $72.73 | +0.37% |
| S&P 500 | 7,623.68 | 7,676.77 | +0.70% |
| VIX | 19.45 | 18.39 | −5.45% |

**Inference:** the daytime separation survived the retrieved US close. This weighs against a same-day generalized sale of the sampled US assets to meet Brazilian losses. It cannot clear private dollar funding, explain investor motives or establish corporate OAS tightening. EMB contains Brazil and is not an ex-Brazil control. EWZ differs from Ibovespa in composition, currency, trading hours and tracking; it is not simply the local-index loss plus an independently measured FX move.

**Brazilian local-index qualification:** vendor ^BVSP returned 176,608.23 / −13.88%, with zero daily volume. Band's [18:01 Brazil-time closing report](https://www.band.com.br/economia/macroeconomia/dolar-fecha-a-r-540-e-registra-maior-alta-diaria-desde-1999) agrees at 176,608 / −13.88%; other publications report 177,540 / −13.43%. [UOL's earlier 17:14 local article](https://economia.uol.com.br/cotacoes/noticias/redacao/2026/10/26/com-eleicao-de-lula-dolar-fecha-acima-de-r-540-e-ibovespa-despenca-14.amp.htm) explicitly described the index as not final. No official B3 close was independently recovered; **no official Ibovespa closing grade**. Use EWZ for the clean US-session comparison, and preserve the conflicting local observations. The difference does not establish cross-market transmission.

## 2. Same-clock FX test

For **both October 23 and October 26**, exact one-minute bars opening **20:59 UTC** were present. Their closes approximate **17:00 New York**. Five pairs were checked for the exact target timestamp; no prior-bar substitution. These are matched **vendor minute proxies**, not certified fixes, SAM's canonical session grade or measured funding rates. This avoids mixing each feed's differently timed daily bars; it does not resolve the broader source limitations.

| Object | October 23 | October 26 | Quote change |
|---|---:|---:|---:|
| USD/BRL, reais per USD | 4.97710 | 5.40510 | +8.60%, real weaker |
| USD/JPY, yen per USD | 156.81400 | 157.48100 | +0.43%, yen weaker |
| USD/MXN, pesos per USD | 18.66250 | 18.56400 | −0.53%, peso stronger |
| USD/ZAR, rand per USD | 16.59500 | 16.63812 | +0.26%, rand weaker |
| EUR/USD, USD per euro | 1.12045 | 1.11769 | −0.25%, euro weaker |

Same-time USD legs imply **BRL/JPY −7.53%, MXN/JPY +0.96%, ZAR/JPY +0.17%**. Derived indicative crosses, not traded crosses or financing returns. The real's fall against yen coexists with yen weakness against USD and resilience in the other two sampled yen crosses. This weakens a universal high-yield-currency carry unwind interpretation; it does not exclude a specific Brazil carry exit. USD/BRL up 8.60% is not an 8.60% drop in the reciprocal real-dollar value. No participant's financing currency, interest earned or realized trading return is identified. No new SAM probability or trigger grade.

## 3. Participant search — a named exposure, still no demonstrated forced cash chain

**Anonymous stop report independently recovered:** [Brazil Journal original](https://braziljournal.com/bloody-monday-b3-e-csn-desabam-40-btg-e-bb-mergulham-30), Giuliana Napolitano, October 26, direct HTTP200 body saved in `brazil-journal-stop.txt`; retrieval metadata/excerpts in source-access.json. It attributes amplification to an **unnamed** equity manager describing stop losses. This confirms the report WALTER found, not the truth of every execution or an independent second manager. No fund, lender, limit, position size, unpaid call or unrelated asset sale is identified. The author's separate [pre-opening manager preview](https://braziljournal.com/acoes-domesticas-boas-devem-cair-20-30-gestores-preveem-segunda-caotica) also uses unnamed managers and forecasts; it is not actual liquidation evidence. Full text independently read; no named identity recovered.

**Concrete pre-event exposure candidate:** [ProShares issuer-primary UBR page](https://www.proshares.com/our-etfs/leveraged-and-inverse/ubr), holdings **as of October 23**, saved `ubr-page.html` and `ubr-holdings-extract.json`. UBR seeks twice daily Brazil index performance. Disclosed swap counterparties: **Goldman Sachs International, UBS AG, Citibank NA, Bank of America NA and Société Générale**; combined displayed exposure value **$7,764,917**. Page net assets **$3,889,167**; the holdings net-other-assets line is **$3,889,180.76**, a separately displayed object, not a replacement NAV reconciliation. Scale is millions. This identifies a small leveraged fund and named contract counterparties **before** the shock. It does **not** establish October 26 portfolio reductions, dealer hedge sales, a margin call, payment, bank loss, fund failure or contagion. Notional is not cash lent or loss. No observed post-event position/collateral file or executed hedge was recovered. It cannot support a systemwide amplification estimate.

[Direxion BRZU primary product page](https://www.direxion.com/product/daily-msci-brazil-bull-2x-etf) confirms another 2× daily product, but displayed pricing remains October 23; clicking the daily-holdings link returned the product page, not a dated holdings file. No BRZU counterparty or October 26 flow inferred. No further vehicle census or standing monitor commissioned.

**Bounded negative:** English/Portuguese searches covered October 26 named funds, stop-loss/stop loss, zeragem, forced liquidation, calls/chamadas de margem, redemptions/resgates and B3 collateral/default notices. Recovered results included pre-event data, generic education, unrelated maturities and anonymous/social claims. No named unmet collateral call, verified forced sale of unrelated assets or failed institution was recovered. No complete CVM census, broker-book access or named-counterparty collateral agreement was examined. WALTER's earlier same-day search is a source pointer, not independent proof of absence. Private information may remain unpublished.

## 4. Brazilian financing — more execution reporting, primary wall remains

[Reuters byline via UOL, October 26 12:44 Brazil time](https://economia.uol.com.br/noticias/reuters/2026/10/26/tesouro-recompra-r71-bilhoes-em-ntn-fs-em-meio-a-disparada-das-taxas.htm) reports **R$7.1B** of fixed-rate NTN-F repurchases, including 5M/2.4M/1M securities across the stated tenors. [Reuters closing rates report, 17:15 Brazil time](https://economia.uol.com.br/noticias/reuters/2026/10/26/taxas-dos-dis-disparam-mais-de-250-pontos-base-apos-lula-superar-flavio-na-eleicao.htm) reports a further **R$7.7B** of inflation-linked repurchases in the afternoon: about **R$14.8B combined**, a sum of rounded reported amounts, not an independently reconciled primary cash total. Full page opens failed; indexed Reuters body supplied the claims. Earlier notices put settlement on October 27; **accepted/report-repurchased is not independently verified paid cash**. These are domestic bond-market absorption measures, not dollars delivered or evidence all financing reopened.

The retained **October 27 floating-rate LFT sale** remains reported, alongside cancellation of inflation-linked/fixed-rate sales. Tomorrow's actual placement is still future at this report's cutoff, not a task that can be finished today. No amount/yield/cover is invented.

**Primary attempt:** Treasury CKAN auction-result API, dataset 402f46f7-51a2-474f-be54-ec0f258c83f6, returned **HTTP 503**; direct official dataset and theme landing page returned **HTTP 429**. Access evidence in source-access.json plus tool receipts; stop retrying the rate-limited source in this pass. No bypass, official-results reconstruction from snippets or use of old Treasury CSV as current. Primary allotment, settlement cash, revised official auction circular and cash-buffer sufficiency remain unresolved.

## 5. Published funding and credit frontier — checked, not postponed without looking

`funding-credit-frontier.json`, retrieval **October 26 17:35 ET**: seven first-published FRED series returned no error/short flag; latest ICE HY/IG/BB/B/CCC and SOFR99 observation is still **October 23**. Latest HY remains **338bp**, existing strict >320 run **eight**, last reset 316 October 13. No new observation means no ninth cell or new fire. Same-date first-published SOFR99 **4.00%** minus IORB **3.90%** is **+10bp**, 079 NOT ARMED. IORB now displays **October 27 3.90%** as a reference; do not pair it with October 23 rates. Credit first-release metadata does not establish wall-clock publication time.

NY Fed direct repo/SOFR responses saved in the same file: October 26 repo remains morning $0 / afternoon $5M; no borrower/motive/Brazil attribution. Latest SOFR remains October 23. Existing 079 FIRE legs UNGRADEABLE; month-end publication exclusions October 28–November 3, no bridging. X1 CLOSED / DON'T-SIZE. Same-source refresh does not measure offshore FX funding bases, haircuts or private borrowing constraints.

## What can change the conclusion next

- **October 27 publications:** actual October 26 SOFR distribution and ICE quality tiers, when published. Broader BB/B/IG widening together, financing refusal or persistent funding stress strengthens transmission; continued resilience/quiet rates weakens the respective measured channels, not every private channel.
- **October 27 retained LFT auction:** official placement and terms versus postponement/failure; confirm local access and source vintage. It is a Brazilian funding test, not a US dollar-funding trigger.
- **Participant bridge:** a current named fund/issuer/clearing/broker statement or dated holdings/collateral record connecting the loss to an actual cash obligation and sale. UBR supplies a pre-event contract candidate; no actual obligation or execution yet. Do not assume every leveraged investor received a lender margin call.

No unattended monitoring, alerts, new scheduling, peer launch or trade follows. Save this baseline and use existing owed duties. Startup/repair work is not repeated. Remaining unavailable evidence is stated rather than supplied from inference.
