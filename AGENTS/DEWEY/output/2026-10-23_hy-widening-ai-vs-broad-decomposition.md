# Is October's junk-bond widening AI-concentrated or broad?
**Date:** 2026-10-23 (research 11:35–11:56 ET) | **Mode:** Thesis | **Request:** REQ-DEWEY-20261023-002 (WALTER, Will-directed 2026-10-23 11:12 ET) | **Confidence:** High on index, tier and timing facts (FRED, ICE-via-Fidelity); Medium on the October AI vs non-AI split (fund holdings and exchange quotes, not TRACE or ICE sector data); Low on the exact AI share of the index

## Key Finding

**Mostly broad, with a sharp AI hot spot that is too small to drive the index.**
- **Timing.** About 65% of the +80bp HY widening (260 [8/28] → 340 [10/22], FRED) came in **September** (→312 [9/30]). That month was a broad selloff driven by rates, the Middle East war and supply. ICE Technology moved **in line** with the index from 5/31 to 9/30 (+38bp each). Telecom (+103) and Cable TV (+311) led.
- **October.** In October, AI-infrastructure bonds diverged hard:
  - CoreWeave notes widened by about +230bp in G-spread from 9/30 to 10/22. SoftBank's newer notes widened by about +100, and Oracle's long bonds by about +70.
  - At ~3% of the high-yield fund, that slice explains roughly **3bp of the ~+24bp** widening from 10/13 to 10/22. The rest of the fund widened about +25bp.
  - On **10/22 itself**, the rest of the fund widened about +15bp. Every rating tier moved (BB +12, B +14, CCC +33).
- **Rough share (DEWEY estimate, method in §2).** The AI-infrastructure slice is about **10–15% of October's widening** and **under ~10% of the 8/28 → 10/22 move**.
- **The unexplained part.** CCC's +161bp in October (1,179 → 1,340, the widest since July 2020) is where the AI share is **unknown**: the composition of the CCC tier is not public.

## Intake checks

| Check | Result | Source |
|---|---|---|
| (a) LIQUID, BROCK or VULCAN October sector or AI-vs-non-AI decomposition | **Not fired.** None exists. LIQUID STATUS: "HY breadth is terminal-gated". LIQUID's 10/15 HYG analysis is a one-day ≥12%-yield sleeve study (CoreWeave 28% of the sleeve's loss), not an October AI split | `AGENTS/LIQUID/STATUS.md` line 78; `AGENTS/LIQUID/research/2026-10-15_L708-ccc-gap/hyg_decomp_output.txt` |
| (b) Date window | Inside the high-value window (before the 10/27 close) | — |
| (c) Latest FRED HY first print | **3.40% (340bp) on 10/22** (≥320), so full scope applies. CCC 13.40% | FRED `BAMLH0A0HYM2`, `BAMLH0A3HYC`, pulled 11:40 ET 10/23 |

## (1) Sector cross-section, ICE BofA US High Yield Constrained (republished by Fidelity)

| Sector | %MV 5/31 | OAS 5/31 | %MV 9/30 | OAS 9/30 | Δ OAS | Sept total return |
|---|---|---|---|---|---|---|
| **Index** | 100 | **274** | 100 | **312** | **+38** | −2.49% |
| Energy | 10.7 | 164 | 11.1 | 181 | +17 | −2.04% |
| Healthcare | 8.9 | 247 | 9.0 | 234 | −13 | −1.73% |
| **Technology** | 7.6 | 304 | **6.7** | 342 | **+38** | **−1.93%** |
| Telecom | 7.0 | 331 | 8.5 | 434 | +103 | −2.74% |
| Cable TV | 3.6 | 668 | 2.7 | 979 | +311 | −4.78% |
| Gaming | 3.5 | 250 | 3.6 | 288 | +38 | −2.58% |
| E. Utilities | 3.3 | 164 | 3.3 | 193 | +29 | −2.58% |
| Chemical | 3.3 | 248 | 3.1 | 274 | +26 | −2.62% |
| Autos | 3.0 | 266 | 2.9 | 321 | +55 | −2.72% |

[PRIMARY-relay: ICE BofA via Fidelity Institutional "U.S. Fixed Income" monthly PDF. As of 9/30: https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F931730.PDF, pulled 10/23 11:42 ET. As of 5/31: Wayback snapshot 20260613001911 of the same URL.] Rows were read with `pdftotext -layout` to fix column alignment.
- Fidelity's own September attribution: "an escalating conflict in the Middle East and hawkish Fed rhetoric producing sharply higher rates"; HY fund outflows −$4.7B; issuance $51.7B; two defaults; ICE default rate 1.75%.
- **No 8/31 vintage** is archived, so the 5/31 → 9/30 change includes June–August, when the index went 274 → ~263.
- **The 10/31 table** (the decisive October primary) should publish ~mid-to-late November (the 9/30 vintage was live by 10/23, a ~3-week lag).

**Rating tiers (FRED, bp):**

| Date | HY | BB | B | CCC | BB/B blend* |
|---|---|---|---|---|---|
| 8/28 | 260 | 150 | 272 | 1,026 | 192 |
| 9/30 | 312 | 194 | 316 | 1,179 | 236 |
| 10/13 | 316 | 191 | 317 | 1,267 | 234 |
| 10/21 | 327 | 198 | 332 | 1,307 | 244 |
| 10/22 | 340 | 210 | 346 | 1,340 | 256 |

\*Blend weighted at the 9/30 ICE tier weights, BB 60.6 / B 31.4 (Fidelity). The blend is DEWEY arithmetic. [PRIMARY: FRED `BAMLH0A0HYM2`, `BAMLH0A1HYBB`, `BAMLH0A2HYB`, `BAMLH0A3HYC`, pulled 10/23]

## (2) AI-infrastructure bond basket vs the rest of the market

**(a) HYG holdings, evaluated by its pricing vendor (same-day).** The basket is 17 HYG bonds:
- CoreWeave ×4
- SoftBank ×3
- APLD ComputeCo ×3
- WULF Compute, Cipher Compute, Core Scientific, Galaxy Helios, Flash Compute, Edged Compute, Black Pearl Compute

That is **3.05% of HYG** (as of 10/22).

| Window (HYG file dates) | Fund Δ yield-to-worst | AI basket Δ YTW | Rest of fund Δ YTW | AI contribution to fund | Treasury move (FRED: HY eff. yield − OAS) | ≈ AI spread Δ | ≈ ex-AI spread Δ |
|---|---|---|---|---|---|---|---|
| 10/13 → 10/22 | +4.6bp | **+78.9bp** | +2.2bp | +2.4bp | ≈ −23bp | **≈ +100** | **≈ +25** |
| 10/21 → 10/22 | −0.4bp | +19.6bp | −1.0bp | +0.6bp | ≈ −16bp | ≈ +36 | ≈ +15 |
| 10/16 → 10/21 | +0.8bp | −8.6bp | +1.1bp | −0.3bp | — | — | — |

[PRIMARY-derived: iShares HYG holdings CSV/XLS. The 10/22 file was pulled by DEWEY 11:44 ET from `…/239565/…/latest-holdings.csv`. The 10/13, 10/14, 10/16 and 10/21 files are LIQUID's committed downloads under `AGENTS/LIQUID/research/2026-10-1{4,5,9}*` and `2026-10-22_after-close/`.]
- **Vendor prices, not trades.** iShares says the vendor price "may not necessarily be as of the date shown". Fund-level yield changes track FRED HY effective-yield changes day by day (e.g. 10/22: HYG −0.4bp vs FRED −3bp), so the files behave as same-day.
- **The spread columns are approximate.** They subtract the index's own Treasury component from the yield change, which ignores tenor and duration differences.
- **Sector moves, 10/13 → 10/22, in yield:** Transportation +103bp (airlines), "Other" +32, Communications +20 (includes SoftBank), Consumer Cyclical +6, Energy −15, Capital Goods −10.

**(b) Exchange quotes, daily (G-spread over the Treasury par curve; not OAS, not TRACE).** Average change per issuer group:

| Window | HY OAS (FRED) | CoreWeave (3 notes) | SoftBank (4 older notes) | SoftBank (2 Sept-2026 notes) | Oracle (7 long bonds, BBB−) |
|---|---|---|---|---|---|
| 9/1 → 10/21 | +62 | **+238** | +53 | n/a | +77 |
| 9/30 → 10/22 | +28 | **+227** | +95 | +110 | +70 |
| 10/13 → 10/22 | +24 | +137 | +88 | +104 | +46 |

[INSTITUTIONAL: German exchange quotes (Frankfurt, Düsseldorf, Stuttgart, Baader) via the onvista public API, pulled 10/23 11:30–11:40 ET; DEWEY spot-checked CoreWeave 9.75% 2031 at a 10/22 last of 79.815 (Frankfurt, stamped 15:20 UTC)]

| Bond | ISIN | 8/28 price / yield / G-spread | 10/22 price / yield / G-spread |
|---|---|---|---|
| CoreWeave 9.00% 2/1/2031 | USU2069EAB66 | 89.83 / 12.02% / 756 | 80.75 / 15.29% / 1,053 |
| CoreWeave 9.75% 10/1/2031 | USU2069EAC40 | 89.86 / 12.49% / 801 | 79.81 / 15.78% / 1,100 |
| CoreWeave 9.625% 7/15/2032 | USU2069EAE06 | 89.18 / 12.26% / 773 | 80.95 / 14.64% / 983 |
| SoftBank 9.25% 4/1/2032 (issued Sept) | USJ7600PAB97 | 100.70 / 9.09% / 397 (9/30) | 97.23 / 9.92% / 512 |
| Oracle 5.25% 2/3/2032 | US68389XCZ69 | 95.87 / 6.15% / 165 | 90.63 / 7.42% / 263 |
| Oracle 6.85% 2/4/2066 | US68389XEC56 | 88.02 / 7.84% / 262 | 78.94 / 8.76% / 347 |

**Cross-check between independent sources:** CoreWeave 9.75% 2031 was 80.08 in HYG's vendor price and 79.81 on Frankfurt on 10/22. News reports for 10/14–10/15 match within a point (Forbes via TIKR; Yahoo via Admiral Markets).

**Limits of these quotes:**
- Bid/ask gaps run 2–3 points on CoreWeave, so levels are good to ±1–2 points.
- No price was found for the straight secured notes of APLD, WULF, Cipher, IREN, Crusoe or Lambda.
- The CoreWeave 9.25% 2030 is not exchange-listed.

## (3) Strategist attribution; the Connect CRE claim

| Claim | Index | Date | Source |
|---|---|---|---|
| "Spreads on AI-related high-yield debt recently widened to over 350 basis points, while spreads on debt used specifically for data centers widened to over 400 basis points, according to Goldman Sachs. That compares to the spread for non-AI BB/B debt, which has held steady at around 250 basis points." | Goldman AI HY basket vs non-AI BB/B | "recently"; published 10/16 | [INSTITUTIONAL via NEWS: Business Insider (J. Sor) via AOL](https://www.aol.com/articles/ai-debt-fears-suddenly-rippling-165706000.html), quote verified by DEWEY 11:53 ET |
| Goldman (Amanda Lynam): neoclouds and frontier-lab-exposed firms "largely at the epicenter"; AI-adjacent energy and utilities "more resilient". No bp figures | Goldman AI HY | wk ~10/12; published 10/19 | [INSTITUTIONAL via NEWS: CNBC](https://www.cnbc.com/2026/10/19/coreweave-oracle-ai-credit-stress.html) |
| Goldman (Lynam), late Sept: HY supply "overwhelming investors"; junk +12bp to 294, the widest since April. **Supply-driven and broad** | — | ~9/25; published 9/28 | [NEWS: Bloomberg, headline/summary only (403)](https://www.bloomberg.com/news/articles/2026-09-28/goldman-says-high-yield-debt-deluge-is-overwhelming-investors) |
| HY data-center bonds ~220bp over HY at the Dec-2025 peak; the premium "largely disappeared" in 1H26 and "started to widen again" from late July | Bloomberg-sourced composite | published 8/6 | [INSTITUTIONAL: Penn Mutual AM](https://www.pennmutualam.com/market-insights/blogs/chart-of-the-week/2026-08-06-ai-infrastructure-bonds-a-full-picture-of-spreads) |

**Reconciling Goldman with FRED.** "Non-AI BB/B … held steady at around 250" matches FRED **for October only**: the BB/B blend stayed in a 235–256bp band from 10/1 to 10/22. Since 8/28, though, it rose 192 → 256. Goldman's line describes the October split. It does not describe the whole move.

**Connect CRE claim.** The article is Joe Palmisano, "Bond Market's AI Warning Is About Growth, Not Prices", 2026-10-21 (https://www.connectcre.com/stories/bond-markets-ai-warning-is-about-growth-not-prices/). It says: "Dollar high-yield AI-related spreads widened 25 basis points in one day to a record 360 basis points over Treasurys, while non-AI spreads moved just two basis points and remained below their March peak."
- **It names no source, index or date.**
- **Verdict: UNVERIFIED, not killed.** The level is consistent with Goldman's ">350" (10/16). The "one day" cannot be 10/22, because the article predates it. Leg arithmetic fits **10/20** best.
- **Do not relay it as a named bank's figure, and do not relay it as the 10/22 move.**

No numbered AI vs non-AI HY split was found from JPM, Barclays, MS, Citi, UBS, DB, Nuveen, PGIM, PIMCO or Apollo.

## (4) How big the AI/tech slice of high yield is

| Measure | Value | As of | Source |
|---|---|---|---|
| ICE Technology sector | **6.7%** of market value (7.6% on 5/31) | 9/30/2026 | ICE BofA via Fidelity (above) [PRIMARY-relay] |
| AI-infrastructure bonds in HYG (17 bonds, DEWEY basket) | **3.05%** | 10/22/2026 | HYG holdings [PRIMARY-derived] |
| AI-related share of US HY | ~2.6% | published 5/7/2026; provider unnamed | [INSTITUTIONAL: M&G Bond Vigilantes](https://bondvigilantes.com/blog/2026/05/a-braive-new-world-for-high-yield/) |
| Tech share of "the overall high yield index" | 8.6% (index unnamed) | published 7/28/2026 | [INSTITUTIONAL: J.P. Morgan AM](https://am.jpmorgan.com/sg/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/ai-the-new-bond-giant/) |

**Caveat on the Technology sector.** ICE's "Technology" sector is not the same as AI. Data-center and compute-SPV issuers sit in other sectors: in HYG they are classed "Other", and SoftBank as "Communications". The July "8.3%" figure remains unsourced.

## (5) CCC long-run history (scope item 5)

The CCC & lower OAS was **1,340bp on 10/22/2026**:
- The widest since **15 July 2020**.
- 80th percentile of all days since 12/31/1996, and 93rd percentile since 2010.
- Above the 2022 peak (1,289) and the 2023 peak (1,186).

Earlier periods at or above 1,340: 1998–2003, 2008–09, 2011, 2015–16, 2020. Peaks: 2008 4,429; 2016 2,066; 2020 1,962.

[PRIMARY: FRED `BAMLH0A3HYC`, full history via `scripts/fred_pull.py BAMLH0A3HYC --splice` (Wayback archive spliced to live; 152-observation overlap, all match), 7,785 observations]

## (6) Counter-evidence (against "broad")

- **The AI slice did lead in October.** Goldman's AI basket rose to >350 while non-AI BB/B held ~250. CoreWeave's 5-year CDS hit a record ~1,194bp on 10/15 [NEWS: Investing.com via relays]. The CoreWeave break came on 10/13–10/14, before 10/22.
- **The 10/22 trigger was AI news:** Meta −7% on capex guidance, Lam −12%, SOX −6.7%, CoreWeave −10% [NEWS/UNVERIFIED: Yahoo live blog, Mitrade]. Nvidia's Jensen Huang spoke of a "scarcity of capital" for neoclouds [NEWS: CNBC 10/22].
- **CCC carried October:** +161bp, versus BB +16 and B +30 from 9/30 to 10/22. If AI issuers make up a meaningful part of CCC, the AI share of October is higher than the HYG-weight estimate. **The composition of CCC is UNKNOWN.**
- **A second "AI" channel sits in loans.** Tech is 39% ($54.4B) of leveraged loans priced below 80 cents, driven by software and AI-disruption fears, not capex borrowers [INSTITUTIONAL via NEWS: Bloomberg, JPM's Jantzen, via Yahoo 10/6](https://finance.yahoo.com/markets/stocks/articles/deeply-distressed-us-loans-rise-181049683.html).

**Against "AI-concentrated" (supporting broad):**
- **September was 65% of the move**, and tech moved only in line with the index.
- **Every tier widened.**
- **Outside AI on 10/13 → 10/22:** HYG ex-AI ≈ +25bp in spread terms, airlines +103bp in yield.
- **Fund flows:** US bond funds −$969M in the week to 10/21, "ending a 26-week streak" [NEWS: Reuters/LSEG Lipper, 10/23 relay](https://1027wbow.com/2026/10/23/us-equity-funds-post-inflows-for-a-second-straight-week/).
- **CNBC (10/22):** investors "demanding more compensation for credit risk beyond AI-linked borrowers" [NEWS](https://www.cnbc.com/2026/10/22/ai-debt-and-french-bonds-stress-test.html).
- **Macro backdrop:** the Iran war and oil (Brent >$110), Fed hawkishness and a 10-year at a 24-year high in early October.

## (7) UNKNOWNs

1. ICE sector OAS for October (the 10/31 table; ~mid-to-late November).
2. Composition of the CCC tier: how much is AI-infrastructure?
3. Goldman's AI basket membership, exact dates and primary note.
4. The source and date of the Connect CRE figure.
5. TRACE trade prints for the basket (no free source; `trace_bond.py` price wall).
6. Prices for the straight secured notes of APLD, WULF, Cipher, IREN and Crusoe.
7. How the October issuance collapse (~$7B vs $51.7B in September) splits between AI and non-AI: the October figure is a Bloomberg relay, unopened (403). Fidelity confirms September only.
8. Agency default rates for September/October (none found; ICE default rate 1.75% at 9/30).

## (8) Verdict

**Mixed, mostly broad.**
- The August–October widening is predominantly a broad credit repricing: September's rates, war and supply selloff took the index 260 → 312, with tech moving only in line.
- An AI-specific leg was layered on in October: CoreWeave about +230bp, SoftBank about +100, Oracle about +70.
- Because AI-infrastructure bonds are only **~3% of the high-yield market**, that leg accounts for roughly **10–15% of October's index widening and under ~10% of the full +80bp** (DEWEY estimate from HYG weights and yield changes; not an ICE attribution).
- The 10/22 +13bp was **AI-triggered but broad in effect**: BB +12, B +14, and the rest of HYG about +15bp in spread terms.
- **The one place the answer could flip is CCC** (+161bp in October), whose composition is not public.

REG-T-04 is not graded here; that call belongs to its owners.

## Source Quality Assessment

- **Strong:** FRED tiers, timing and CCC history are primary. The ICE sector tables are a primary relayed by one republisher (Fidelity).
- **Medium:** the AI basket rests on two independent public price sources that agree within ~0.3 points (iShares vendor evaluation; German exchange quotes). Neither is a trade print.
- **Weak:** the strategist split is one bank (Goldman), relayed by news. The Connect CRE claim is unsourced.

## References
(accessed 2026-10-23 unless stated)
- FRED: BAMLH0A0HYM2, BAMLH0A0HYM2EY, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC, BAMLC0A0CM, DGS5: https://fred.stlouisfed.org/series/<ID>
- Fidelity Institutional US Fixed Income (ICE BofA sector table), 9/30 vintage: https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F931730.PDF; 5/31 vintage: https://web.archive.org/web/20260613001911id_/https://institutional.fidelity.com/app/proxy/content?literatureURL=/931730.PDF
- iShares HYG holdings (10/22): https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf/latest-holdings.csv; earlier files: LIQUID's committed downloads (paths in §2)
- onvista public API (exchange quotes): `https://api.onvista.de/api/v1/bonds/ISIN:<isin>/snapshot` and `/api/v1/instruments/BOND/<entityValue>/eod_history?idNotation=<id>&range=M3&startDate=2026-08-25`
- Treasury par yield curve (G-spread base): https://home.treasury.gov (daily par yield curve rates, 2026)
- Business Insider/AOL 10/16; CNBC 10/9, 10/19, 10/22; Penn Mutual 8/6; M&G 5/7; JPMAM 7/28; Connect CRE 10/21; Bloomberg via Yahoo 10/6; Reuters/LSEG relay 10/23: URLs inline above
- Reproduce: (1) `python3 AGENTS/DEWEY/scripts/fred_pull.py <ID> --start 2026-08-25 --csv`. (2) `pdftotext -layout` on the Fidelity PDF; read the "ICE BofA HIGH-YIELD CORPORATE SECTORS" block. (3) Match HYG holdings files on (name, coupon, maturity). Basket regex: `^(COREWEAVE|SOFTBANK|WULF COMPUTE|GALAXY HELIOS|FLASH COMPUTE|EDGED COMPUTE|CORE SCIENTIFIC|CIPHER COMPUTE|BLACK PEARL COMPUTE|APLD COMPUTECO)`. Compute the weight-averaged Δ YTW. The 10/21 XLS needs bare `&` escaped before XML parsing. (4) G-spread = yield to maturity (30/360, semiannual, from clean price + accrued) minus the linearly interpolated Treasury par curve.

## Process Report
**Searches run:**
- DEWEY primary pulls: FRED ×8 series; Fidelity PDF ×2 vintages (live + Wayback); HYG holdings, plus re-parsing LIQUID's four committed files; one onvista spot-check; one Goldman quote verification.
- Two Opus legs: the exchange-quote basket (30 tool calls) and attribution/breadth (57).
- The full `/deep-research` harness was not used.

**Data gaps:** §7.

**Source frustrations:**
- iShares' `asOfDate` parameter is ignored on `latest-holdings.csv`, so only today's file is available. History exists only where a desk saved it: **LIQUID's saved files made the October split possible.**
- The Fidelity PDF has no August vintage on Wayback.
- Bloomberg returns 403.
- The 10/21 HYG XLS contains bare `&` characters that break XML parsing.

**Confidence in findings:** High on timing and tiers; Medium on the October split; Low on the CCC composition and the exact AI share.

**If I had more time/tools:**
- Save HYG and JNK holdings daily (a collector is out of scope, so a WALTER/LIQUID call).
- Re-run when the 10/31 Fidelity table lands.
- Get TRACE through an authenticated FINRA account (needs Will's word).

**Suggestions:**
- **BACKLOG:** add onvista as the `trace_bond.py` price fallback for RegS/144A bonds. Caveats: these are exchange quotes, not trades; Frankfurt/Düsseldorf "last" stamps can be morning prints.
- **BACKLOG:** an `ishares_holdings.py` helper with `&`-sanitising and file-pair comparison.
