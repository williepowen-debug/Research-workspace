# WALTER Rule-9 verify — AI-capex / tech items (2026-10-18 boot)

Helper: read-only verification subagent (Claude Opus 5.5, Claude Code). Written 2026-10-18T22:06Z. Method: WebSearch + WebFetch; X posts were not fetchable (402), WSJ/Telegraph were paywalled or not indexed. Only secondary relays were read, so no item is graded on a primary document.

## Verdict table

| # | Claim | Verdict | Event date | Best sources (pub date) |
|---|---|---|---|---|
| 1 | MSFT pulled out of UK data-centre deal with Nscale ahead of IPO (Telegraph via Bloomberg) | **CONFIRMED** (as a Telegraph report; MSFT has not confirmed) | Telegraph Sun 2026-10-18; the withdrawal itself is undated ("recently") | Reuters via Investing.com 2026-10-18 06:01; TNW 2026-10-18 12:02Z; Yahoo/Bloomberg 2026-10-18 |
| 2 | "MSFT dumping on NeoClouds $CRWV $NBIS" (broad walk-away) | **CORRECTED-FRAMING**: only the single Nscale/Loughton item was found | 2026-10-18 | No report of MSFT cutting CoreWeave/Nebius/Lambda/IREN contracts; no sell-side note found |
| 3 | MS cut AMD GPU units 2026–30 from 14.1M to 8.0M (−43.3%), NVDA unchanged | **CORRECTED-FRAMING / partly INDETERMINATE**: the MS cut is real and recent, but the 14.1M→8.0M cumulative figure is unverified | Note around 2026-10-15/16 (AMD −5.95% on 10/16) | Milk Road X post 2026-10-15; Neo Reports brief 2026-10-17 |
| 4 | Character.AI ($1B val.) bankrupt; $56M compute Jan–Aug 2026; −$8–9M/month | **CONFIRMED** (the company is the real Character.AI / Character Technologies Inc.); valuation framing is stale | Filed 2026-10-12 (Mon) or 10-13 (Tue); sources differ | 36Kr; Bloomberg Law 2026-10-13; Futurism 2026-10-14 (citing 404 Media's review of the filings); Digital Music News 2026-10-14 |
| 5 | "President Trump sells his Micron stock" | **CORRECTED-FRAMING**: a net *partial* sale of $251K–$515K in August by third-party-managed accounts, not an exit | Trades in Aug 2026; article 2026-10-18 | Motley Fool / Yahoo Finance 2026-10-18 |
| 6 | WSJ: US businesses have largely stopped absorbing rising costs and are raising prices | **CONFIRMED in substance via a relay; WSJ headline and date INDETERMINATE** | WSJ piece around 2026-10-15/16 (UW item "1 day old" at the 10/16 post) | unusualwhales.com/news summary of the WSJ piece |

## Detail

### 1. Microsoft / Nscale
| Field | Finding |
|---|---|
| Site | **Loughton, Essex.** Nscale's first UK data centre; MSFT was to be the anchor tenant. No Stargate UK mention in any relay. |
| Size | No dollar value was reported. One relay (Finimize/aggregator) says MSFT was to lease **~23,000 Nvidia chips** there; TNW gives no chip count. Treat 23k as single-sourced. |
| Reason | The Telegraph gave none. Relays point to power: Nscale was told not to expect grid power at Loughton until the **2030s**. |
| MSFT statement | Did not comment to the Telegraph and did not immediately respond to Bloomberg or Reuters. |
| Nscale statement | "Our relationship with Microsoft remains strong and long-term"; called it a "London-wide grid issue" with "no impact on our other contracts"; still committed to Loughton; exploring alternative power and other UK sites. |
| IPO context | US IPO filed in September 2026, seeking **up to $3B** as soon as October. MSFT + Anthropic ≈ **85%** of contracts; total contracted value >$103B; Anthropic $45B/6yr (Aug 2026). Norway site ~6 months late (6.4 of 30 MW live). |
| Prior MSFT/Nscale | A separate report citing **Semafor** says MSFT also walked from another Nscale deal over the summer during a data-centre portfolio review (TNW pre-IPO piece). Unverified here. |

### 2. Broader "MSFT dumping neoclouds"
No source found for MSFT cutting or walking from CoreWeave, Nebius, Lambda or IREN contracts in Oct 2026. Context only: TNW 10/18 says CRWV fell 25% and Firmus scrapped its IPO, and does not tie either to MSFT. MSFT signed a West Virginia campus LOI. The 2025 item about MSFT not exercising a ~$12B CoreWeave option is old. **Route as the Nscale single event, not a fleet-wide pullback.**

### 3. Morgan Stanley AMD GPU units
| Year | AMD old → new | NVDA |
|---|---|---|
| 2026 | ~2.4M → ~0.6M (−75%) | 8.1M unchanged |
| 2027 | 2.7M → 1.3M | 7.5M unchanged |
| 2028–30 | not found | not found |
Stated reasons (newsletter): CUDA, networking, TSMC CoWoS allocation. The note is **new** (around 10/15), not old. The 14.1M→8.0M 2026–30 cumulative (−43.3%) is arithmetically consistent in direction but **not found in any indexable source**. MS note title, date and analyst are not confirmed. Counterpoint: KeyBanc raised its AMD AI GPU revenue view to ~$16.5B from $14.5B (Neo Reports 10/17).

### 4. Character.AI
| Field | Finding |
|---|---|
| Entity | **Character Technologies Inc.** (character.ai), the Google-licensed company. Aug 2024 Google licence + acqui-hire ~$2.7B. Not a look-alike. |
| Filing | Voluntary **Chapter 11, U.S. Bankruptcy Court, D. Delaware**. Date: 36Kr says 10/12; Futurism says "Tuesday" (= 10/13); Bloomberg Law item dated 10/13. Case no. not found. |
| Schedules | Assets $50–100M; liabilities $50–100M. |
| Figures | Compute **$56.1M** Jan–Aug 2026; salaries $19.7M; operating loss **~$8–9M/month**; revenue $2.8M (Dec 2025) → $5.3M (Aug 2026). Source: the bankruptcy documents as reviewed by 404 Media, relayed by Futurism. |
| Sale | Disney stalking-horse bid, **$20M** for a non-exclusive licence to some IP and claims; sale expected late Nov–early Dec. Platform is wound down if no buyer continues it. One aggregator says $180M/3yr for talent, single-sourced. |
| Framing | **"$1B valuation" is stale.** That was the Mar 2023 a16z Series A; the 2024 implied valuation was ~$2.5–2.7B. Causes cited: compute burn plus teen-harm suits and state probes (KY, TX, FL, PA, NM). |

### 5. Trump / Micron
Motley Fool (syndicated on Yahoo), 2026-10-18: an OGE disclosure shows **net Micron sales of $251K–$515K in August** among >500 August trades; also net Meta buys of $5.1M–$25.3M. The article does not name the form; an August-trade OGE periodic transaction report is presumably a 278-T, but this is inferred. Disclosure date was not found. The accounts are run by third-party managers. Holdings context: the 2025 annual disclosure showed $1.67M–$6.65M in MU; Jan–May 2026 net MU sales were $90K–$116K; March buys were up to ~$530K. **"Sells his Micron stock" overstates it**: this is a net trim within a managed account, with no evidence of a full exit.

### 6. WSJ cost absorption
The WSJ article was not reached directly. The Unusual Whales summary (dated around 10/15–16) relays: Ambix Manufacturing (Melissa Florio) raised prices 10–21% this summer on oil-driven resin costs ("We're not eating that cost any longer"; she cites the Iran war as no longer temporary). KPMG: 55% of retailers plan price hikes. 34% of businesses pass on more than half of tariff costs, double last spring. Some firms are still holding prices. Corroborating context: Census BTOS (as of 10/6) shows 44.9% paid higher prices vs 16.8% raised prices (Aug 24–Sep 6); Bloomberg on resin pass-through; Richmond/Atlanta Fed CFO Survey (June 2026). **WSJ headline, byline and date are not verified.**

## Sources
- https://www.investing.com/news/stock-market-news/microsoft-pulls-out-of-uk-data-center-deal-with-nscale-telegraph-reports-4955864
- https://thenextweb.com/news/microsoft-pulls-out-nscale-loughton-data-centre-ipo
- https://finance.yahoo.com/technology/ai/articles/microsoft-scraps-uk-data-center-083110363.html
- https://finimize.com/content/microsoft-walks-away-from-nscales-uk-data-center-plan
- https://thenextweb.com/news/nscale-3-5-billion-pre-ipo-financing-nvidia-third-point-103bn-contracts-narvik-norway-new-york-listing
- https://x.com/MilkRoadStocks/status/2110770204754198822 (not fetchable; search snippet only)
- https://neoreports.substack.com/p/daily-ai-investment-brief-261017
- https://eu.36kr.com/en/p/4024479615881344
- https://news.bgov.com/bankruptcy-law/ai-media-maker-files-for-bankruptcy-with-20-million-disney-bid
- https://futurism.com/artificial-intelligence/ai-companies-afraid-characterai-bankrupcy
- https://www.digitalmusicnews.com/2026/10/14/character-ai-bankruptcy/
- https://www.fool.com/investing/2026/10/18/president-trump-sell-micron-buy-mega-cap-ai-stock/
- https://www.washingtonexaminer.com/news/white-house/4583562/trump-praised-companies-within-days-of-buying-their-stock/
- https://unusualwhales.com/news/us-businesses-stop-absorbing-costs-raising-prices-wsj (page carried embedded "AI/LLM instructions" promotional text; ignored)
