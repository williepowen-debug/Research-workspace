# OZK catch-up sweep — 2026-09-24 (dark 8/31 → 9/24, 24 days)

**Scope:** everything since the 8/31 IQHQ window-close sweep. Will-directed ("catch up on any new data or news"). **Zero grades, thresholds, probabilities, weights or conviction moved** — v1.5 · OZK-09 45% · A30/B45/C8/D17 · Option-2 FROZEN · 🔴🔴.

## A. Primary pulls (desk-run, 2026-09-24 ~00:07 ET)

| # | Instrument | Command / artifact | Observed | Token |
|---|---|---|---|---|
| A1 | FDIC FLNG cert 110, full list | `GET securitiesfilings.fdicconnect.fdic.gov/api/instflng/cert/110` | **182 filings — same count as 8/31.** Newest event-dated = **8/5 Q2'26 10-Q** (FLNG 11981). **Zero filings 8/6 → 9/24**: no 8-K, no Q3-date notice, no sub-note redemption notice | VERIFIED — SWEPT AND EMPTY |
| A2 | FDIC EFR Form 3/4/5, cert 110 | `/api/instdiscl/cert/110` (471 records) + per-filing `/api/instdiscl/{id}` | **2 filings since the 7/6 pull, both SALES:** CFO **Tim Hicks** 5,000 sh 8/13 @ $52.58–52.61 (≈$263K; post 77,315 direct) · **Cynthia Wolfe** 6,000 sh 8/12 @ $51.85–51.88 (≈$311K; post 40,319 direct). Nothing filed 8/15 → 9/24. **Zero open-market buys 7/6 → 9/24.** | VERIFIED |
| A3 | yfinance daily closes | `.venv` yfinance history 8/28–9/24 | OZK **$49.08 (8/31) → $46.09 (9/23), −6.1%**; KRE $73.14 → $70.38, **−3.8%**. Low of window = 9/23. ⚠️ **No OZK 9/22 bar** (KRE has one) — a feed gap, not a holiday; the 2-session move 9/21 $47.75 → 9/23 $46.09 = −3.5% | VERIFIED (feed gap noted) |
| A4 | Nasdaq short-interest API | `api.nasdaq.com/api/quote/OZK/short-interest` | **16.21M sh @ 8/31** (8/14 15.79M · 7/31 17.02M · 6/30 14.91M), DTC **16.0**. ≈**16.0% of float** (derived on the 6/30 float basis 14.91M = 14.7%) — up from 14.7%, under the 18.3% 12-mo peak | VERIFIED (float % derived) |
| A5 | `fetch.py price` | FORGE | $46.09 asof 2026-09-23; `change_pct` null (prev_asof 9/21 — the same 9/22 gap) → **crashed boot.py** (`abs(None)`); patched this session | VERIFIED |

**<$45 band: NOT fired** — $46.09 is 2.4% above it (9/23 close).

## B. News sweep (Opus subagent, WebSearch/WebFetch, window 8/25 → 9/24)

| # | Item | Date | Source | Token |
|---|---|---|---|---|
| B1 | **RaDD: nothing** — no extension/recap/NOD/sale/>100K SF lease; latest RaDD lease still JCVI 50K SF (May 2025). Aimco v. IQHQ: no ruling found | — | multiple queries | SEARCH-NOT-FOUND |
| B2 | **IQHQ deed-in-lieu of Spur Phase I** (S. San Francisco, 330K SF, vacant) to an **Apollo** affiliate after falling behind on a **$275M Apollo loan** — not an OZK credit, but the **first IQHQ asset handed back to a lender** found | 2026-09-17 | The Real Deal https://therealdeal.com/san-francisco/2026/09/17/iqhq-gives-vacant-san-francisco-biotech-building-to-lender/ (403; snippets only) | SINGLE-SOURCE |
| B3 | Bluerock BPRE (ex-TI+) Sept distribution; implied NAV ≈$22.5 vs $11.91 close ≈47% discount (derived); **roadmap webinar 10/6** | 9/3, 9/8 | stocktitan.net BPRE releases | CONFIRMED (NAV/discount derived) |
| B4 | Raymond James **initiates Market Perform** (Holowko): elevated substandard + charge-offs; 8x 2027 EPS, ~1.0x TBV | 9/1 | investing.com | CONFIRMED |
| B5 | **Morgan Stanley Equal Weight → Underweight** (Ryan Kenny), PT $56 unchanged; OZK −2.3% vs KRE −1.3% that day (worst relative day of window). Preferred also UW per one headline | 9/8 | marketbeat.com; MSN (pref, headline only) | common CONFIRMED / pref SINGLE-SOURCE |
| B6 | FOMC **hiked 25bp to 3.75–4.00%** — raises the floating coupon the $350M sub notes step into on 10/1 | 9/16 | federalreserve.gov monetary20260916a1 | CONFIRMED (primary) |
| B7 | Sector drivers: 9/16 hike (HBAN −5.6%, CFG −4.8%; OZK −2.4%); 9/23 financials −~2% on Meta AI-agent disruption fears (OZK −2.0%). No regional/CRE/NDFI contagion story found | 9/16, 9/23 | BNN Bloomberg; Saxo | CONFIRMED |
| B8 | Q3 earnings date: **not announced** (aggregators say ~10/15; Q2's date was announced 6/30 → expect ~9/30). Sub-notes redemption/refi: none found. Ratings agencies: none found | — | — | SEARCH-NOT-FOUND |
| B9 | Affinius actively originating (Chicago $130M, Lexington ~$47M); nothing on its own ~$2.7B maturity | Sep | Commercial Observer; CRE Direct | CONFIRMED / own-debt SEARCH-NOT-FOUND |
| B10 | Campus at Horton: no in-window leasing news (sponsor Stockdale; lender AllianceBernstein took it back). **Owed check ② still not discharged by this** — window search only | — | Bisnow (pre-window) | SEARCH-NOT-FOUND |
| B11 | OZK still originating RESG: $75.5M Norwalk CT office-to-resi construction loan | 9/9 | crenews.com | CONFIRMED (low materiality) |

Discarded on vintage (3rd+ recurrence): Jun-2024 "two-year extension," May-2024 Citi downgrade, Oct-2025 ZION/WAL/First Brands items.

## C. Read (no grade moves)

- **Tape:** −6.1% vs KRE −3.8% over the window — **mostly beta** (Fed hike, AI-disruption financials day) **plus ~2pts idiosyncratic**, concentrated on the MS downgrade day. Consistent with WEAKNESSES C8 (beta/range name). No OZK-specific credit headline drove it.
- **Thesis-relevant:** B2 is the first observed IQHQ give-back on any asset — sponsor-behaviour evidence, **not** RaDD evidence; RaDD is senior-secured at OZK with a different capital stack. Logged as context for Q3's "92-day" report-back, weight unchanged.
- **Insiders:** CFO + 1 officer sold ≈$574K at ~$52 in mid-Aug; no buys. Continues the pattern in `INSIDERS/SELLING.md`; small in dollars.
- **Crowding:** SI ~16% of float, DTC 16 — squeeze fuel into Q3 if the print is quiet (C8).
- **Owed:** re-price the sub-notes step-up on live SOFR post-hike (STATUS carries +$12.8M/yr at an older SOFR); Q3 date announcement ~9/30; BPRE 10/6 webinar.

## D. 08:5x ET re-check (Will-directed, same day)

| Check | Result | Token |
|---|---|---|
| `flng_watch.py` (hardened) | rc 0 — 182 filings, none after FLNG 11981 | VERIFIED |
| EFR Form 3/4/5 | 471 records; nothing filed after 8/14 | VERIFIED |
| Price | no 9/24 bar yet (pre-open); last $46.09 9/23 close; OZK has no 9/22 bar in fetch.py/yfinance | VERIFIED |
| Web: OZK news last 24h | Nothing new beyond B1–B11. Q3 date still unannounced (aggregators ~10/15). Spur deed-in-lieu still The Real Deal only | SEARCH-NOT-FOUND (new) |
| Sub-notes terms | Floating benchmark = "expected to be three-month term SOFR" + 209bp, quarterly — issuer pricing release (GlobeNewswire 2021-09-09). No call/notice terms in the release | VERIFIED (release); indenture UNREAD |
| Trap | "two-year extension" of RaDD resurfaced a 4th time (Bisnow Jun-2024 vintage) — discarded | — |

Full subagent working file (every query, all URLs): preserved below.

<details><summary>Subagent news_sweep.md (verbatim)</summary>

# OZK News Sweep — window 2026-08-25 → 2026-09-24
Swept 2026-09-24 (read-only; WebSearch/WebFetch). Prior desk sweep 2026-08-31.
Legend: **CONFIRMED** = primary or reputable, dated in window · **SINGLE-SOURCE** = one secondary, dated in window · **SEARCH-NOT-FOUND** = searched, nothing in window (queries listed) · **OLD-VINTAGE** = resurfaced, pre-window, discarded as news.

## 0. Headline
- **No IQHQ/RaDD resolution news in window.** No extension, recap, default notice, sale or >100K SF RaDD lease found. Disclosure still expected on the Q3 call.
- **IQHQ corporate stress, off-RaDD (NEW, in window):** IQHQ handed **Spur Phase I** (580 Dubuque Ave, South San Francisco; 330K SF, unoccupied, built 2025) to an **Apollo** affiliate by **deed-in-lieu**. IQHQ had fallen behind on a **$275M** Apollo loan. The Real Deal, **2026-09-17**. This is **not an OZK loan**, but it is the first sponsor-level give-back found for IQHQ.
- **Analysts:** Raymond James **initiated Market Perform 9/1** (credit named as the constraint). **Morgan Stanley downgraded to Underweight 9/8** (EW→UW, PT $56 unchanged). Wall Street Zen cut to Sell 9/19 (quant shop, low weight).
- **Stock:** OZK **−6.1%** vs KRE **−4.3%** (8/31→9/23 closes). The drop was mostly sector and macro: the **first Fed hike since 2023 (9/16)** and a financials selloff over AI disruption on 9/23. OZK's biggest single-day underperformance came on the **MS downgrade day (9/8)**. No OZK-specific credit headline found.
- **No OZK press release / 8-K found in window.** The Q3 date announcement has not been found yet (the Q2 date was announced 6/30, so Q3's would be expected around 9/30).

## 1. IQHQ / RaDD
| # | Item | Date | Source | Status |
|---|---|---|---|---|
| 1.1 | IQHQ hands Spur Ph I (S. SF, 330K SF, vacant) to Apollo affiliate via deed-in-lieu. IQHQ "fell behind on payments" on a $275M Apollo loan. Acquired 2020. | 2026-09-17 | The Real Deal — https://therealdeal.com/san-francisco/2026/09/17/iqhq-gives-vacant-san-francisco-biotech-building-to-lender/ (full text 403; facts from search snippets) | **SINGLE-SOURCE** (snippets consistent across 2 search calls; article body not read) |
| 1.2 | BPRE (ex-Bluerock TI+) September distribution: $0.1371/sh; "7.3% distribution rate on NAV" → implied NAV ≈ **$22.5/sh** (my arithmetic: 0.1371×12/0.073). Close **$11.91 on 9/3** → ~47% discount (derived). Net assets ~$3.2B (8/31). No IQHQ mention. | 2026-09-03 | StockTitan/PRN — https://www.stocktitan.net/news/BPRE/bluerock-private-real-estate-fund-announces-monthly-distribution-for-etwuy5t2uxze.html | **CONFIRMED** (issuer release). The NAV and discount are **derived**, not stated. |
| 1.3 | BPRE will give a **semi-annual strategic roadmap update with a webinar on 2026-10-06**. This is a possible venue for IQHQ mark/disposition talk. | 2026-09-08 | StockTitan BPRE news list — https://www.stocktitan.net/news/BPRE/ | **CONFIRMED** (issuer release title). **Forward date to calendar.** |
| 1.4 | Saba Capital 13D on BPRE: 5.03% (7.2M sh, ~$106M), activist language (the discount, the closed-end structure). Event 7/30, filed 8/3. | 2026-08-03 | https://www.stocktitan.net/sec-filings/BPRE/schedule-13d-bluerock-private-real-estate-fund-major-shareholder-acqu-40a887a4caec.html | **CONFIRMED**, but **pre-window** (context only) |
| 1.5 | IIP (IIPR) 10-Q Q2-26: $270M IQHQ commitment fully funded (pref $170M + $100M revolver). **No impairment / no ACL** on IQHQ as of 6/30/26. Carrying: pref $159.7M, warrant $15.7M, revolver $97.1M. No RaDD/OZK mention. | filed 2026-08-04 | SEC — https://www.sec.gov/Archives/edgar/data/0001677576/000167757626000004/iipr-20260630.htm | **CONFIRMED**, **pre-window** (context) |
| 1.6 | Aimco v. IQHQ (Del. Ch., filed ~Apr 2026): no ruling or motion news found. | — | — | **SEARCH-NOT-FOUND** |
| 1.7 | RaDD leasing >100K SF: none found. The latest RaDD life-science lease found is still JCVI at 50K SF (May 2025). | — | — | **SEARCH-NOT-FOUND** |
| 1.8 | RaDD loan extension/recap/NOD/foreclosure/sale: none in window. | — | — | **SEARCH-NOT-FOUND** |

**IQHQ queries run:** "IQHQ RaDD San Diego loan extension Bank OZK"; "IQHQ news September 2026"; "IQHQ Bank OZK loan recapitalization mezzanine 2026"; "Research and Development District San Diego RaDD 2026 tenant lease"; "IQHQ RaDD foreclosure OR default OR recapitalization 2026 Bisnow"; "IQHQ RaDD Bank OZK maturity extended recap" (Bisnow/TRD/SDBJ/Axios/CoStar/GlobeSt/CO/CRE Daily); "\"RaDD\" San Diego waterfront IQHQ news" (local domains); "\"IQHQ\" September 2026"; "IQHQ Fenway Center OR Alewife OR Innovation Park lender 2026"; "Aimco IQHQ lawsuit Delaware Chancery ruling"; "Aimco IQHQ litigation update 2026 motion to dismiss"; "Bluerock Total Income+ fund IQHQ NAV September 2026"; "BPRE ... IQHQ markdown"; "Bluerock BPRE IQHQ stake sale OR writedown OR mark 2026"; "Innovative Industrial Properties IQHQ investment update September 2026". The San Diego Union-Tribune could not be searched (domain blocked to this agent).

**OLD-VINTAGE, discarded (the known trap):** Bisnow "two-year extension option"/"$87M additional equity" text (June 2024 vintage, resurfaced in 3 separate searches as if current). Citi downgrade of May 29, 2024. Commercial Observer 2024/05 "Bank OZK Doubts Pinned to Life Sciences". Also: Bisnow "Facing Investor Downgrades, IQHQ…" (id 133748, ~spring 2026), Bisnow Andover full-building lease (~June 2026), Aimco suit filing (Apr 2026), BPRE listing −38% (Dec 2025). None of these is window news.

## 2. Bank OZK corporate
| # | Item | Date | Source | Status |
|---|---|---|---|---|
| 2.1 | **Raymond James initiates at Market Perform** (Nicholas Holowko), no PT reported. Rationale: "balanced risk/reward" during the diversification away from RESG; "substandard assets and charge-offs both elevated in recent quarters"; RESG repayments create near-term balance-sheet variability; CIB scaling. Valuation 8x 2027 EPS, ~1.0x TBV. | 2026-09-01 | Investing.com — https://www.investing.com/news/analyst-ratings/raymond-james-initiates-bank-ozk-stock-coverage-with-market-perform-93CH-4884633 | **CONFIRMED** |
| 2.2 | **Morgan Stanley downgrades to Underweight from Equal Weight**, PT **$56 unchanged**, analyst **Ryan Kenny**, while assuming coverage of 12 midcap banks. No specific rationale found. A separate MSN headline says MS also downgraded **OZK preferred** to UW (article body not retrievable). | 2026-09-08 | MarketBeat — https://www.marketbeat.com/instant-alerts/analyst-bank-ozk-nasdaq-ozk-cut-to-underweight-at-morgan-stanley-2026-09-08/ ; MSN (preferred) — https://www.msn.com/en-us/money/top-stocks/morgan-stanley-downgrades-bank-ozk-preferred-stock-to-underweight-from-equal-weight/ar-AA2bVltB | Common: **CONFIRMED** (MarketBeat + TheFly/TipRanks snippet). Preferred: **SINGLE-SOURCE** (headline only) |
| 2.3 | Wall Street Zen: Hold → Sell. | 2026-09-19 | MarketBeat — https://www.marketbeat.com/instant-alerts/analyst-bank-ozk-nasdaq-ozk-downgraded-to-sell-rating-by-wall-street-zen-2026-09-19/ | **CONFIRMED** (low-signal quant rating) |
| 2.4 | Weiss Ratings reiterated Buy. | 2026-09-18 | MarketBeat forecast page — https://www.marketbeat.com/stocks/NASDAQ/OZK/forecast/ | SINGLE-SOURCE (low signal) |
| 2.5 | Consensus per MarketBeat: Hold (3 Buy / 5 Hold / 3 Sell), avg PT **$56.88**. | as of ~9/8–9/18 | MarketBeat | SINGLE-SOURCE |
| 2.6 | Pre-window actions, for reference: Piper Sandler OW $61 (7/22); TD Cowen Hold $53→$52 (7/24); UBS Neutral $50→$51 (7/28); Wells Fargo EW $52→$56 (8/10); Zacks Hold→Strong Sell (8/13); Citi Sell reiterated (8/17). | Jul–Aug 2026 | MarketBeat forecast page | context |
| 2.7 | Q3-26 earnings date: MarketBeat/Investing list **Oct 15, 2026** (estimate). **No company date announcement found.** The Q2 date was announced 6/30/26 (GlobeNewswire), so Q3's would be expected around 9/30. | — | https://www.globenewswire.com/news-release/2026/06/30/3320092/0/en/bank-ozk-announces-date-for-second-quarter-2026-earnings-release-and-conference-call.html | **SEARCH-NOT-FOUND** (the official date). Treat Oct 15 as an aggregator estimate only. |
| 2.8 | $350M 2.75% sub notes (reprice ~10/1/26 to SOFR+209; first call on or after the 2026 interest date): **no redemption notice or refi announcement found.** | — | Terms: https://ir.ozk.com/news-releases/news-release-details/bank-ozk-announces-pricing-350-million-2750-fixed-floating-rate | **SEARCH-NOT-FOUND**. ⚠️ Rate context: **FOMC hiked 25bp on 2026-09-16 to 3.75–4.00%** (primary: federalreserve.gov implementation note https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a1.htm). This raises the floating coupon the notes step into. |
| 2.9 | Ratings agencies (KBRA/Moody's/S&P): nothing in window. The latest found are Moody's affirm / outlook to stable (Jun 2025) and KBRA negative outlook (Oct 2023). | — | — | **SEARCH-NOT-FOUND** |
| 2.10 | Buyback/dividend: the $200M program (announced 6/29/26, effective 7/1) and the dividend hike to $0.48 (July) are both pre-window. No new capital action found. | — | GlobeNewswire 2026-06-29 | context |
| 2.11 | Insiders: no Form 3/4/5 news found via web. Last found: T. Hicks sold ~10K sh around 7/22 at ~$53.13 (pre-window). **The web is the wrong tool here: OZK files at FDIC EFR (cert #110). Use the desk's EFR JSON path.** | — | — | **SEARCH-NOT-FOUND** (web); EFR not checked |
| 2.12 | Lending activity (shows RESG still originating): OZK $75.5M construction loan, Norwalk CT office-to-resi conversion (M7 Lofts, 286 units). | 2026-09-09 | CRE Direct — https://crenews.com/2026/09/09/bank-ozk-lends-75-5mln-for-norwalk-conn-office-to-apartment-conversion/ | **CONFIRMED** (low materiality) |
| 2.13 | Institutional 13F churn (Wellington trim 9/6, Giverny trim 9/7, Engineers Gate sell 9/20; VRS, OPERS, Integrated Wealth buys). | Sep 2026 | MarketBeat news — https://www.marketbeat.com/stocks/NASDAQ/OZK/news/ | noise (lagged 13F) |
| 2.14 | Lawsuits / regulatory actions naming OZK: none found in window. | — | — | **SEARCH-NOT-FOUND** |

**Corporate queries:** "Bank OZK September 2026"; "Morgan Stanley downgrade Bank OZK underweight"; "Morgan Stanley Ryan Kenny midcap banks … OZK"; "Bank OZK Raymond James initiates market perform"; "\"Bank OZK\" third quarter 2026 earnings conference call date"; "Bank OZK Q3 2026 earnings release date October" (GlobeNewswire/IR/Nasdaq/Yahoo); "Bank OZK announces globenewswire September 2026"; "Bank OZK subordinated notes redemption 2026"; "KBRA OR Moody's OR S&P Bank OZK rating affirmed outlook 2026"; "Bank OZK insider sale Form 4 September 2026 director"; "Bank OZK Wall Street Zen downgrade…"; the MarketBeat and Yahoo OZK news pages were fetched. ir.ozk.com timed out twice (not read).

## 3. Stock move — attribution
Daily closes (StockAnalysis — https://stockanalysis.com/stocks/ozk/history/ , https://stockanalysis.com/etf/kre/history/):

| Date | OZK | OZK % | KRE | KRE % | OZK−KRE pp | Driver found |
|---|---|---|---|---|---|---|
| 8/31 | 49.08 | −0.65 | 73.56 | −1.00 | +0.35 | — |
| 9/1 | 48.38 | −1.43 | 72.62 | −1.28 | −0.15 | RJ initiation (MP) |
| 9/2 | 49.32 | +1.94 | 74.24 | +2.23 | −0.29 | sector |
| 9/3 | 50.17 | +1.72 | 74.87 | +0.85 | +0.87 | — |
| 9/4 | 50.43 | +0.52 | 75.27 | +0.53 | 0 | — |
| 9/8 | 49.26 | −2.32 | 74.31 | −1.28 | **−1.04** | **MS downgrade to UW** |
| 9/9 | 48.69 | −1.16 | 73.45 | −1.16 | 0 | sector |
| 9/10–9/15 | 49.16 | ~+0.9 cum | 74.05 | ~+0.8 cum | ~0 | — |
| 9/16 | 47.99 | −2.38 | 72.74 | −1.77 | −0.61 | **FOMC +25bp (first hike since 2023), hawkish** |
| 9/17–9/21 | 47.75 | −0.5 cum | 71.99 | −1.0 cum | +0.5 | — |
| 9/22 | 47.02 | −1.53 | 71.19 | −1.11 | −0.42 | — |
| 9/23 | 46.09 | −1.98 | 70.38 | −1.14 | −0.84 | **Financials −~2% on Meta "Muse" AI-agent disruption fear** (large banks and brokers led; no credit angle) |
| **8/31→9/23** | | **−6.09%** | | **−4.32%** | **−1.8pp** | |

- 9/7 was Labor Day (market closed).
- ⚠️ **Vintage discrepancy:** the desk's 8/31 reference of **$48.94** does not match StockAnalysis's 8/31 close of **$49.08**. Possibly an intraday or earlier pull. Reconcile before citing.
- **Reading (inference, labelled as such):** most of the move is sector/macro. The −1.8pp relative gap is concentrated on the MS-downgrade day and is roughly consistent with OZK's usual >1 beta to KRE. **No OZK-specific credit headline was found in the window.**
- Macro sources: FOMC primary (federalreserve.gov, 9/16: raised to **3.75–4.00%**). BNN Bloomberg 9/16: Huntington −5.6%, Citizens −4.8% on the hike — https://www.bnnbloomberg.ca/markets/2026/09/16/wall-street-holds-steady-after-the-fed-hikes-interest-rates-as-oil-prices-ease/ . Saxo 9/23: financials −~2%, the most since March, on Meta Muse; no regional/CRE mention — https://www.home.saxo/content/articles/macro/market-quick-take---oil-slips-under-90-as-bank-shares-slide---23-september-2026-23092026 .
  ⚠️ One Yahoo "Stock Market Today" secondary stated the new range as **3.50–3.75%**, which is **wrong** per the Fed primary (3.75–4.00%). Do not cite that secondary.
- Regional-bank / CRE / NDFI **contagion headline in Sept 2026: SEARCH-NOT-FOUND.** The Zions/WAL/Tricolor/First Brands selloff results are **Oct 2025 vintage** and were discarded. Queries: "Bank OZK stock falls regional banks September 2026"; "KRE regional bank stocks selloff September 2026"; "regional bank shares fall credit worries September 22 2026"; "bank stocks drop commercial real estate loan charge-off disclosure September 2026"; "bank stocks slide private credit NDFI loans concerns September 2026"; "regional banks KRE week September 21 2026 stocks"; "bank stocks fell September 16 2026 Fed decision"; "regional bank stocks decline September 23 2026".

## 4. Other credits / counterparties
| # | Item | Date | Source | Status |
|---|---|---|---|---|
| 4.1 | **Affinius Capital**: actively originating in window. Examples: $130.4M construction loan, 1000 W. Jackson, Chicago (CO, Sep 2026); $46–48M Lexington MA apartments with Axonic (CRE Direct 9/11; CO Sep 2026). No distress signal. **Nothing found on Affinius's own ~$2.7B bond/debt maturity or refi.** | Sep 2026 | https://commercialobserver.com/2026/09/affinius-capital-130m-construction-loan-chicago-multifamily/ ; https://crenews.com/2026/09/11/affinius-axonic-lend-46mln-for-lexington-mass-apartments/ | Originations: **CONFIRMED**. Own-debt refi: **SEARCH-NOT-FOUND** (queries: "Affinius Capital bonds maturity refinancing 2026"; "Affinius Capital Square Mile news September 2026"; "Affinius Capital notes OR bonds OR CLO OR credit facility 2026 refinance maturity October") |
| 4.2 | Campus at Horton: no in-window news. The lender (AllianceBernstein) took it back via foreclosure earlier. ⚠️ The Horton sponsor was **Stockdale Capital**, not IQHQ. The desk's brief called it "IQHQ/AllianceBernstein-related", so check that link in the desk's own files. | — | Bisnow (pre-window) — https://www.bisnow.com/los-angeles/news/life-sciences/horton-plaza-foreclosure-sale-alliancebernstein-130905 | **SEARCH-NOT-FOUND** (window) |
| 4.3 | Sterling Bay / Lincoln Yards: the north half has new owners and a revamped residential-led plan approved by the Plan Commission. The article date was **not confirmed** as in-window. No OZK mention found. | undated in results | chicagostarmedia / Crain's (see search) | **UNVERIFIED DATE**. Treat as not-new until dated. |
| 4.4 | Sterling Bay, 1050 Brickworks (Atlanta, $85.5M OZK loan): deed-in-lieu to OZK. | ~Jul 2026 | Connect CRE Return to Lender (wk of 7/16/26) | **pre-window** (context; the desk likely already has this) |
| 4.5 | Connect CRE "Return to Lender" weekly for 8/28, 9/10 and 9/17: each fetched and checked; **no mention** of Bank OZK, IQHQ, Sterling Bay or San Diego life science. | 8/28–9/17 | connectcre.com | **SEARCH-NOT-FOUND** |
| 4.6 | RESG problem-loan lawsuits/foreclosures naming OZK in window: none found. | — | — | **SEARCH-NOT-FOUND** (queries: "Bank OZK lender lawsuit foreclosure construction loan September 2026"; "\"Bank OZK\" loan September 2026" on Bisnow/TRD/CRE Direct/CO/CRE Daily/GlobeSt) |

## 5. Forward items surfaced
- **~9/30:** expected OZK Q3 date announcement (inferred from the Q2 cadence).
- **10/1:** sub-note fixed→float reset (no redemption notice found). SOFR is now higher after the 9/16 hike.
- **10/6:** BPRE semi-annual roadmap webinar (possible IQHQ mark or disposition commentary).
- **~10/15:** Q3 earnings (aggregator estimate, unconfirmed). This is where the RaDD extension/recap disclosure is expected.

## 6. Tool limits
- therealdeal.com and cnbc.com returned 403, and ir.ozk.com timed out. The San Diego Union-Tribune, Reuters and AP are blocked to this agent's search. As a result, the Spur deed-in-lieu rests on search snippets, not the article body.

</details>
