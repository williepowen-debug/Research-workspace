# Triggered-unwind search — October 26, 2026

Will requested: “I would like to look for triggered unwinds.” This is a completed bounded investigation, not a recurring monitor, a trade recommendation or a claim to have searched private prime-broker books. Prices were pulled at approximately 13:44 ET; primary funding result refreshed 13:47 ET. No other desk's files were edited.

## Result and evidence ladder

**A local stop-loss amplification report was found. A named fund liquidation, unmet margin call, clearing-member failure, forced yen-funded close or Brazil-driven sale of unrelated US assets was not verified.** The sampled cross-market pattern weighs against a broad ongoing carry liquidation at the observation time. This is not evidence that no particular investor is unwinding.

| Candidate | Observation | Evidence state and limit |
|---|---|---|
| Local Brazilian equity stop losses | Brazil Journal, Giuliana Napolitano, October26, quotes one unnamed equity manager attributing some outsized falls to stop-loss orders | **Reported mechanism**, direct publication body recovered HTTP200 and read. No fund name, threshold, execution tape, size or corroborating named manager. Stops may be voluntary risk controls; they are not automatically lender-enforced margin liquidations. |
| Yen-funded Brazil carry | An Aephel morning brief asserts that the long-real/short-yen trade is being forced closed | **Unsupported as a measured event** in this investigation. Indexed body read; original page403. No named position, lender, collateral demand or underlying execution data supplied. Not disproved by missing support. |
| Broader carry basket | Yen weaker versus USD, Australian dollar and euro; peso stronger, rand weaker; derived MXN/JPY up while BRL/JPY down | **Mixed market proxies**, not a shared broad unwind signature. Cannot identify investor motives or establish causality. |
| Unrelated US risk selling | US equities, regional-bank ETF and corporate-credit ETFs positive at13:44ET | Counterevidence to a simultaneous broad cash-raising sale in this sample; duration/distributions/basis affect ETFs. Does not prove credit spreads tightened or private financing stayed available. |
| Exchange/retail controls | B3 widened lower futures price bands; retail Treasury trading delayed for rate volatility | **Primary confirmed controls**, not confirmed margin hikes, a clearing failure or a liquidation instruction. |
| Dollar funding | NYFed afternoon repo accepted$5M after morning$0; latest SOFR observation remainsOctober23 | **Same-day public facility result**, not participant identity or Brazil attribution. Small positive take-up alone does not establish seizure. Pre-event SOFR cannot clear Monday funding. |

## Fresh cross-market observations

One-off direct yfinance retrieval; raw unadjusted prior daily closes compared with current minute-bar closes. Full bars and exact timestamps in prices.json. All observations below13:44ET except VIX13:29ET and EZA13:37ET. FX vendor prior closes are not independently certified17:00NY or official Brazilian closes. Prices are vendor mirrors, not exchange-certified closes or executable quotes.

| Object | Intraday change from vendor October23 daily close |
|---|---:|
| Brazil dollar equity ETF EWZ | −21.37% |
| USD/BRL (reais per dollar) | +7.61%, real weaker |
| USD/JPY (yen per dollar) | +0.59%, yen weaker |
| USD/MXN (pesos per dollar) | −0.81%, peso stronger |
| USD/ZAR (rand per dollar) | +0.94%, rand weaker |
| AUD/JPY | +0.66% |
| EUR/JPY | +0.34% |
| Mexico equity ETF EWW | +0.57% |
| South Africa equity ETF EZA | +0.71%, last13:37ET |
| Dollar EM sovereign ETF EMB | −0.15% |
| US high-yield ETF HYG | +0.18% |
| US investment-grade ETF LQD | +0.21% |
| Senior-loan ETF BKLN | +0.05% |
| S&P500 | +0.65% |
| Nasdaq100 ETF QQQ | +1.12% |
| US regional-bank ETF KRE | +0.48% |
| VIX |18.25, −6.17%, last13:29ET |
| Gold ETF GLD | +0.48% |
| Bitcoin USD feed | +0.09% versus vendor prior daily close, not a24h return |

**Cross-check on the carry inference:** same-time USD legs produce BRL/JPY−6.53%, MXN/JPY+1.41%, ZAR/JPY−0.34% (crosses-derived.json). A falling BRL/JPY pair alone cannot establish yen funding being repaid: the same snapshot has a weakening yen against USD. This does not exclude specific yen-funded Brazilian exits. No statistical event study or causal attribution from these returns.

Selected hourly checkpoints in the saved minute bars show EWZ31.6171 at09:30ET and33.49 at13:44ET; USD/BRL5.5959 at09:30ET and5.4344 at13:44ET. The sampled endpoints show partial recovery from the opening stress, not a continuously intensifying decline. This is not a monotonic-path claim, session-high/low certification or a declaration that the seller is exhausted. Brazil pressure persisted: EWZ remained sharply below Friday.

## What the primary notices establish

B3 notice666/2026-SSN,09:07:56local publication, says that from09:30local solely for October26 regular trading, IND/WIN lower daily price limits widen from−15% to−20% across maturities. Direct HTTP200 body read and saved in primary-retrievals.json. **A wider allowed price move is not a higher collateral requirement.** No dated primary notice of a margin increase, member default or failed settlement was recovered by the bounded queries. That is searched-but-unverified, not proof none exists.

Tesouro Direto official October26 10:00 notice states trading is closed because of high rate volatility and expects normalization during the day; Tesouro Reserva remains operating. Direct HTTP200 body recovered. This notice establishes a trading interruption, not an actual redemption gate imposed by a named investment fund or a failed government payment. Current reopening was not verified.

NYFed raw results at13:47:06ET include RP10262625 (08:30 close) submitted/accepted$0, and RP10262627 (13:45 close; lastUpdated13:45:51) submitted/accepted$5,000,000: Treasury$2M, agency$1M, MBS$2M. These are dollars, not billions. Total for the two returned operations$5M. The13:45:44 retrieval still returned morning-only data; absence of the afternoon row then was not a zero. Retain both captures rather than overwrite history. Offered facilities/announcements are not funds taken up. No borrowing institution or reason is disclosed here. LIQUID owns gate interpretation; no threshold grade changed.

## Search scope and unresolved leads

English and Portuguese queries covered October26 Brazil margin calls/chamadas de margem, forced liquidation/zeragem compulsória, fund redemptions/resgates, stop losses, B3 price limits/margins/defaults, and Brazil-yen/MXN/ZAR transmission. A reporting lead through SpaceMoney was traced to the original Brazil Journal body; they are one underlying report, not two independent confirmations. Generic educational pages, old reports, future maturities and pre-event fund NAV tables are not event evidence. No named failed fund, missed margin payment or publicly documented portfolio liquidation was found in this bounded search. No complete CVM filings census, paid dealer/prime-broker note set or clearing position records were accessible/assessed.

LIQUID's contemporaneous report at13:38ET independently reached a mixed-proxy/no-demonstrated-funding-transmission conclusion. Its source-qualified paragraph distinguishes direction checks from a causal event study. WALTER read that file and did not edit it. The newer repo result is a delta to its pending-afternoon cell; no automatic gate clearance follows. SAM's latest consulted STATUS is datedOctober20, not a fresh owner endorsement.

## Next discriminators within this question

1. Find a **named** manager/broker statement or filing that connects an actual position reduction to a stop, loss limit, collateral call or credit-line restriction, including time/size/funding currency. This would move beyond today's anonymous local amplification report.
2. Separate an actual change in margin requirements from price-band changes; obtain the effective date, instruments and cash required if a notice appears. Price drops and normal daily variation margin do not by themselves demonstrate an unpaid call.
3. Look for broadening into multiple non-Brazil carry pairs plus unrelated liquid assets, and a documented common investor/financing link. Asset prices alone nominate a candidate; they cannot identify the forced seller.
4. Examine confirmed redemption/execution/settlement or financing events as they become public. Daily or delayed fund reports may lag the price event; do not label unavailable same-day disclosures as a clean result.

These are ranked follow-ups, not scheduled polling. Existing SAM/LIQUID/HENRY ownership applies; no new desk launched. No basis yet to recommend a Brazil-triggered US short or a rebound trade.

## Sources and access

- Original stop report, direct HTTP200: https://braziljournal.com/bloody-monday-b3-e-csn-desabam-40-btg-e-bb-mergulham-30 ; body hash/access metadata and short excerpt in article-access.json. Anonymous manager claim is not independently audited execution evidence.
- Unsupported carry claim lead, indexed body only/original403: https://www.aephel.com/research/daily-brief/2026-10-26-morning-brief-monday-october-26-2026 . Not adopted as fact.
- B3 primary notice: https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/Detail?agencia=17&dataNoticia=2026-10-26+09%3A07%3A56&idNoticia=3527929
- Retail Treasury primary: https://www.tesourodireto.com.br/ja/w/atraso-na-abertura-do-mercado
- NYFed primary: https://markets.newyorkfed.org/api/rp/repo/all/results/latest.json ; timestamped snapshots preserved.
- Funding observation dates: https://markets.newyorkfed.org/api/rates/secured/sofr/last/5.json
- Vendor method/values: collect.py, prices.json, crosses-derived.json; no continuous oil contracts used.
- Owner source: AGENTS/LIQUID/research/2026-10-26_brazil-transmission/REPORT.md (working file; preserve selected source/version separately before transfer).
