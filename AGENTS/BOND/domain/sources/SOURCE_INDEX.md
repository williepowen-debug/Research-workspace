# BOND Source Index

**Purpose:** Map each BOND metric to a source, update cadence, and owner boundary.

| Metric | Primary source | Backup/source note | Cadence | Owner boundary |
|---|---|---|---|---|
| HY OAS | FRED `BAMLH0A0HYM2` | Market-data dashboard | Daily / 1-day lag | LIQUID owns dashboard threshold; BOND owns issuance/credit-market-function implication. |
| CCC OAS | FRED `BAMLH0A3HYC` | Market-data dashboard | Daily / 1-day lag | LIQUID owns systemic credit stress; BOND uses as lower-quality credit function. |
| IG OAS | FRED `BAMLC0A0CM` | FRED | Daily / 1-day lag | BOND owns IG primary-market function implication. |
| 2Y / 10Y / 30Y yields | FRED `DGS2`, `DGS10`, `DGS30` | yfinance Treasury proxies | Daily | HENRY/LIQUID use macro/plumbing; BOND owns term-premium/auction-function interpretation. |
| Treasury auction BTC/tail/takedown | Treasury auction results / FiscalData | TreasuryDirect announcements | Every auction | BOND owns. Signal LIQUID/ZHAO on weak demand. |
| Dealer Treasury positions | NY Fed Primary Dealer Statistics / FR2004 | FT/BBG summaries when primary delayed | Weekly | BOND owns dealer absorption; LIQUID owns repo funding consequence. |
| Corporate issuance | SIFMA monthly; IFR/Reuters/FT for weekly color | High-quality market news | Weekly/monthly | BOND owns market-access / issuance-freeze state. |
| Pulled deals / concessions | Reuters/FT/BBG/WSJ | News sweep | Event-driven | BOND owns signal; REGINALD consumes if bank funding burden rises. |
| CDX.HY / CDX.IG | ICE/CME/market-data/news sources | ETF/proxy only if no direct source | Weekly/event | BOND owns CDX-cash divergence. |
| HYG/LQD/TLT prices | yfinance via market-data tool | Brokerage screen if needed | Daily | BOND uses for position support; not primary evidence alone. |
| VIX/SPX | HENRY/VIOLET | market-data dashboard | Daily | Consume only for credit-equity lead timing. |
| TIC / foreign flows | ZHAO | Treasury TIC | Monthly | Consume, do not own. |
| SOFR/RRP/SRF | LIQUID | market-data dashboard / NY Fed | Daily | Consume, do not own. |
