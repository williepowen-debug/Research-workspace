# Verify H2 — markets/data bookmark claims (read-only helper)

Run: 2026-10-29 ~15:24–15:45Z (11:24–11:45 ET), WALTER Rule 9 helper, Claude Opus 5.5. Every post's full text was read via api.fxtwitter.com (quotes and media URLs included). The images that carry the claims were viewed: TTF, CCC/HY ratio, buyback results, 3Fourteen hyperscaler chart, CCC yield chart. Not read: the macropaperr TIC image (a stock photo, no data), the Kobeissi chart, the BullTheory CCC chart and the TipsWatch article chart.

## TOP SUMMARY
1. **TTF €100 (HANS-T-07 L3).** The front month was November (TTFX26) on 10/28. It traded above €100 intraday: ICE c1 high 100.945 (Investing.com, not a settle). Whether it SETTLED at or above €100 is UNRESOLVED. The vendor NYMEX look-alike X26 daily bar shows 100.72 (377 lots). The ICE c1 table shows 98.50 for 10/28, and that page's own earlier vintage showed 99.25. No ICE Endex official settle was reached. X26 expires today, 10/29, and the generic ticker is already on December (Z26 96.90 intraday 10/29). The row's letter is "front-month daily settle, sustain 1, never grade across the roll", so the evidence does NOT yet establish the letter. HANS must get the official 10/28 X26 settle. +250% YTD: CONFIRMED (28.16 on 12/31/25 → 98.5–100.7, i.e. +250% to +258%).
2. **CCC credit.** The ICE CCC effective yield hit 18.17% on 10/23 (FRED BAMLH0A3HYCEY), the high of FRED's available window (data from 2023-10-30). It has since eased to 17.73% (10/28). "Highest since pandemic" cannot be tested on FRED (pre-2023 history is truncated). ICE CCC OAS was 13.56% on 10/23 and 13.07% on 10/28. Gina Martin Adams's 1,127 bp is the **Bloomberg** CCC OAS (BCAUOAS, data through 10/23), a different index from ICE's, not an error. The CCC/HY ratio is 3.34x, a record since 1996.
3. **Buybacks.** CONFIRMED. On 10/27, a $6.000B liquidity-support buyback in the 20–30Y segment (offered $10.746B, settled 10/28; Treasury results sheet in the post). The October total of $26.08B over 6 operations sums exactly. It is also the FY27-to-date total. All were liquidity support, with zero cash-management operations.
4. **World Bank CMO (Oct 28, 2026).** CONFIRMED at the primary: energy +32% in 2026, total commodities +23% in **2026** ("by 2026" is loose wording), Brent $91 avg 2026, commodities −7% in 2027.
5. **Trade.** CORRECTED-FRAMING. The September **advance goods** deficit (Census, 10/28) was $134.9B vs $132.1B in August. That is +$2.8B, a widest-since-March-2025 (18-month) high, but "surges" overstates a 2.1% move, and it is goods only, not the total trade balance.
6. **Not confirmed at a primary.** The "hyperscaler spreads above July wides" chart is driven by Oracle (+69bp vs 7/29); MSFT/GOOGL/AMZN are flat to tighter. The TIC "allies −60%" claim is not verified. Note that the post says "over 60%", not "6x" as in the WALTER item gist.

---

### 6. TTF €100 — @BullTheoryio 2115475956777578831 (2026-10-28T16:09Z)
- Full text read: yes, plus the image (TradingView TFM1! weekly, top of candle ~100.5, "+4.424 (+4.61%)").
- CLAIM: "European natural gas prices just crossed €100 for the first time since December 2022"; "more than 250% since start of year".
- PRIMARY: ICE Endex settlement **not reached**. Secondaries and vendor sources:
  - Investing.com ICE "TFMBMc1" historical table (fetched 10/29 ~15:35Z): 10/28 close 98.500, high 100.945, low 96.355, vol 125.75K. An earlier search snapshot of the same page showed 10/28 = 99.25 / high 99.57. The values are unstable, so this is not a settle.
  - Repo vendor (yfinance) NYMEX TTF look-alike TTFX26.NYM 10/28 daily bar: O 97.525, H 100.72, C 100.72, 377 lots. TTFZ26.NYM 10/28: C 100.341, 20 lots. The prior-day closes (10/20–10/27: 85.062, 87.426, 90.043, 93.853, 96.681, 96.061) match the ICE c1 table exactly, which suggests they are settlements. For 10/28 the two sources DISAGREE (100.72 vs 98.50).
  - TradingPedia 10/28 10:46 GMT: front month 97.35 intraday.
- HANS-T-07 letter (AGENTS/HANS/registry/THRESHOLDS.tsv): metric TTF-FRONT-MONTH-EUR-MWH; L3 >100; sustain 1; basis "TTF FRONT-MONTH daily settle, ICE/TradingEconomics"; "never grade a rung crossing across a roll"; the row flags X26→Z26 at 10/29.
- Evidence vs letter:
  - Intraday >100 on the front month (X26) on 10/28: supported by one secondary (ICE c1 high 100.945) and by the vendor bar.
  - Settle >100 on 10/28: CONFLICTING (NYMEX look-alike 100.72 vs ICE c1 table 98.50); unverified.
  - The 10/28 X26 settle is the last pre-roll front-month print. From 10/29 the front month is Z26 (vendor 96.90 intraday, 10/29 ~11:00 ET; ICE c1 97.53 last). Do not compare an X26 level with a Z26 level as a move.
  - I am not grading this as a fire; that is HANS's call.
- "First since Dec 2022": plausible. Not checked at a primary for the Dec 2022 date. The 2026 pre-October weekly highs on the chart are about 74, so nothing above 100 earlier in 2026.
- YTD: TTF=F 12/31/2025 close 28.161 (vendor) → 98.50 is +250%, 100.72 is +258%, today's 96.9 is +244%. CONFIRMED at the 10/28 print.
- VERDICT: CORRECTED-FRAMING. "Crossed €100" is true intraday; a settle above 100 is not established, and the move came on the expiring November contract.
- Gaps: official ICE Endex X26 and Z26 settles for 10/28.
- Owner: **HANS** (cc BRENT/HENRY/LIQUID per the row's chain).

### 7. CCC spreads 1,127 bp — @GinaMartinAdams 2115055227736936469 (2026-10-27T12:17Z)
- Full text read: yes, plus the image (HB Wealth "CCC-to-HY Spread Ratio", sources Bloomberg BCAUOAS / LF98OAS, data through Oct 23, 2026, as of 10/26; ratio 3.34x, a record since 1996; long-run average 1.90x).
- CLAIM: CCC spreads 1,127 bp, wider than 5 of 6 days since 1996 (83rd percentile); HY at its 16th percentile, BB at its 11th; CCC is 8% of the index.
- PRIMARY: The index identity comes from the chart's source line: **Bloomberg US Corporate HY CCC OAS (BCAUOAS)**, data through 10/23. The Bloomberg terminal itself was not reachable. Cross-check: 1,127 / 3.34 ≈ 337 bp HY, which matches ICE HY OAS of 3.38% on 10/23 (FRED BAMLH0A0HYM2).
- ICE comparison (FRED BAMLH0A3HYC): 13.56% on 10/23 (2026 high), 13.21% on 10/27, 13.07% on 10/28. ICE CCC & Lower runs about 230 bp wider than the Bloomberg CCC. That is an index-construction difference (ICE includes "& Lower" names), not an error.
- Percentile: on ICE (FRED window only, 2023-10-30 onward, n=786 obs), 11.27% would be the 97th percentile. That window is NOT the 1996 window, so the 83rd-percentile claim cannot be reproduced here.
- VERDICT: CONFIRMED (index = Bloomberg, date ≈ 10/23). The percentile is INDETERMINATE (no 1996+ data).
- Owner: **LIQUID**.

### 34 / 53. CCC yields 18.17% / "over 18%, highest since pandemic" — @great_martis 2114813667745390621 (10/26 20:17Z), @BullTheoryio 2115164953057558797 (10/27 19:33Z)
- Full text read: yes, both. great_martis's image is the TradingView chart of BAMLH0A3HYCEY at 18.17%.
- PRIMARY: FRED BAMLH0A3HYCEY (ICE BofA CCC & Lower US HY Effective Yield), pulled 10/29.
  - 10/20 18.01, 10/22 17.99, **10/23 18.17**, 10/26 18.08, 10/27 17.86, 10/28 17.73 (%).
  - 18.17 is the maximum of FRED's whole available window (2023-10-30 to now).
  - Six months ago (late April 2026) it was 12.92–13.08%. BullTheory's "around 13%" is CONFIRMED.
- BullTheory's other figures, checked on FRED:
  - "BBB ~1.1% over Treasuries": BAMLC0A4CBBB 1.09–1.13 (10/22–10/27). CONFIRMED.
  - "CCC >13% over": ICE CCC OAS 13.21–13.56. CONFIRMED.
  - The JPMorgan loan figures ($139.8B below 80c, $65B below 60c, tech 39%) and the CoreWeave figures were NOT verified; secondary only.
- "Highest since pandemic": cannot be tested on FRED (history truncated at 2023-10-30). The claim needs a pre-2023 series check against the 2022 high (ICE or Bloomberg).
- VERDICT: CONFIRMED for the level and date (18.17% = 10/23 close, not a fresh print on 10/26–10/27; the yield has eased since). INDETERMINATE for "highest since pandemic".
- Owner: **LIQUID**.

### 8 / 20. Treasury buyback $6B; month total $26.08B — @BullTheoryio 2115380835130146991 (10/28 09:51Z), @macropaperr 2115142741055484412 (10/27 18:05Z)
- Full text read: yes, both. The BullTheory image is the Treasury "Debt Buyback Operation Results" sheet dated 10/27/2026.
- PRIMARY (Treasury results sheet as imaged):
  - Operation 10/27/2026, settlement 10/28.
  - Maturity range 11/15/2046–08/15/2056 (20–30Y nominal).
  - Maximum $6,000,000,000; offered $10,746,000,000; accepted $6,000,000,000.
  - 35 issues eligible, 6 accepted. Largest: 912810SU3 (2.0% 2051) $1.333B at 52.423; 912810SD1 $1.693B.
- treasurydirect.gov and fiscaldata endpoints returned 404 from this box (paths not found). I did not resolve the correct URLs.
- Month total, via a secondary aggregator (tftc.io, mirrors Treasury data). October operations, all **liquidity support**, no cash-management operations:

  | Date | Segment | Accepted |
  |---|---|---|
  | 10/1 | 10–20Y | $6B |
  | 10/6 | 2–3Y | $1.33B |
  | 10/8 | 20–30Y | $6B |
  | 10/15 | 10–20Y | $6B |
  | 10/21 | TIPS 1–10Y | $0.75B |
  | 10/27 | 20–30Y | $6B |

  - Sum = $26.08B. CONFIRMED arithmetic; it equals FY27-to-date.
  - Tentative next operations: 11/4 (10–20Y), 11/5 (1M–2Y).
- VERDICT: CONFIRMED. Framing note: this is the routine liquidity-support program (a max-size take, offered/max = 1.79x on 10/27), not an emergency operation.
- Gaps: each operation's sheet was not read at treasurydirect.
- Owner: **BOND**.

### 11. World Bank energy +32% / commodities +23% — @TheObserverLens 2115465788677361939 (10/28 15:28Z)
- Full text read: yes.
- PRIMARY: World Bank press release "Commodity Prices Set to Increase by 23% in 2026 as Global Shocks Mount", Washington, Oct 28, 2026 (worldbank.org/en/news/press-release/2026/10/28/commodity-markets-outlook-october-2026).
  - "Energy prices are projected to rise 32% in 2026"; "set to push energy prices to a four-year high".
  - "Overall commodity prices are forecast to rise 23% this year before declining by 7% in 2027".
  - Brent $91 avg 2026 (2025: $69), $79 in 2027. Metals at a new high in 2026.
  - Revised up from the April 2026 CMO, which had energy +24% and commodities +16%.
- VERDICT: CONFIRMED. Minor framing: "+23% by 2026" means +23% in 2026 (y/y annual average), the same year as the energy figure.
- Owner: **CARL** (cc BRENT for Brent $91).

### 26. US HRC steel highest in 4+ yrs, +52% y/y — @unusual_whales 2115422579821351055 (10/28 12:37Z)
- Full text read: yes (no image).
- CLAIM: HRC $1,255/ton, +52% y/y, last seen May 2022; steel imports −14% in 9M 2026 (per Bloomberg).
- PRIMARY: not reached. Bloomberg is paywalled, and CRU, Fastmarkets and the CME HRC settle were not reached (cmegroup.com is blocked from this box).
- Secondary: GMK Center (10/20) attributes $1,255, +52% y/y and "last May 2022" to Fastmarkets, alongside the Nucor 10/19 letter (+$15/st, ending a 5-week hold), Kallanish $1,220–1,300/st (10/16) and CSI $1,320. That article's units conflict (per short ton vs per tonne).
- VERDICT: INDETERMINATE. Directionally corroborated by one secondary aggregator; the benchmark, unit and date are unverified; the Bloomberg attribution is unconfirmed.
- Gaps: CME HRC front-month settle or the CRU index; Census/AISI import data.
- Owner: **MIDAS**.

### 29. US trade deficit 18-month high — @Polymarket 2115425373693645091 (10/28 12:48Z)
- Full text read: yes (one line, no figure).
- PRIMARY: Census Monthly Advance Economic Indicators Report, Sept 2026, CB26-177, released 10/28/2026 08:30 ET (census.gov/econ/indicators/2026/advance_report2609.pdf).
  - Advance **goods** deficit $134.9B (Sept), vs $132.1B (Aug, revised from $132.6B advance): +$2.8B.
  - Exports $209.2B (+$5.3B); imports $344.1B (+$8.1B).
  - Highest since the March 2025 pre-tariff peak, per the Continuum preview (Mar 2025 ≈ $158.7B goods), so ~18 months is consistent.
  - FRED BOPGSTB (goods and services, BEA): Aug 2026 −$105.6B, the largest since Mar 2025 (−$133.0B).
- VERDICT: CORRECTED-FRAMING. The 18-month high is true, but it is the advance GOODS balance, not the total trade balance, and "surges" overstates a 2.1% widening. The September full goods-and-services report has not yet been published.
- Owner: **CARL**.

### 24. Allies cut net Treasury purchases — @macropaperr 2115400533104324705 (10/28 11:09Z)
- Full text read: yes; the image is a stock photo.
- Note: the post says "over **60%**" (to $174.3B in Jan–Aug 2026, the lowest since 2021), NOT "over 6x" as in the WALTER item gist.
- The post's country claims were not verified:
  - Japan net purchases −99%
  - Korea −$23.8B Jan–Aug, the largest since 1977
  - Taiwan a net seller
  - China reducing
- Other figures in the post:
  - 10Y "crossed 5%": FRED DGS10 = 5.00 on 10/23 and 10/26, 4.99 on 10/27. Roughly accurate.
  - Debt "$40.53T": not checked.
- PRIMARY: Treasury TIC August 2026 press release, 10/16/2026 (home.treasury.gov/news/press-releases/sb0662).
  - August foreign net purchases of long-term US securities $300.7B (private $257.8B, official $42.9B).
  - Treasury bonds and notes: private $90.9B, official $18.1B (≈$109.0B).
  - The release has no country cumulative figures and no "ally" classification.
- The "allies" grouping looks like a Bloomberg-style analysis that classifies countries by UN-voting alignment. The 2025 version appeared via Metalsmine: allies $463.9B in 2025. The 2026 article was not found.
- VERDICT: INDETERMINATE. The aggregate August TIC Treasury inflow was large, which is in tension with the post's tone; country figures need TIC S-form country tables.
- Owner: **BOND**.

### 19. BofA clients net sold $3.5B after $15B — @DeItaone 2115451337613688885 (10/28 14:31Z)
- Full text read: yes.
- CLAIM: net $3.5B sold last week after $15B the prior week; retail led; Communication Services had its largest weekly outflow since 2018; Industrials had a 13th straight week of outflows (Hill/Brown; the post's "Jill Carey Hall and Trey Brown").
- PRIMARY: BofA client-flow note, not public and not reached.
- VERDICT: INDETERMINATE. Secondary only (headline wire relay).
- Owner: **HENRY**.

### 22. 20-day corr 10Y yield vs NDX +0.51 — @KobeissiLetter 2115413042200535298 (10/28 11:59Z)
- Full text read: yes (chart not viewed).
- Plausibility check: correlation of daily ΔDGS10 against daily NASDAQ100 % change, both from FRED:
  - 20-day window ending 10/22: +0.53
  - ending 10/23: +0.54
  - ending 10/26: +0.54
  - ending 10/27: +0.62
  - ending 10/5: −0.67
- This is consistent with "+0.51" and with "−0.68 in late September" (exact method and dates differ). "Highest since March" was not checked.
- VERDICT: CONFIRMED-PLAUSIBLE (independent recompute, different basis). The interpretation is right: a positive yield–equity correlation means Treasuries are rallying when tech falls.
- Owner: **HENRY** (cc BOND).

### 17. 5Y TIPS matured 10/15 outperformed nominal — @TipsWatch 2115416796010578144 (10/28 12:14Z)
- Full text read: yes, plus the linked article (tipswatch.com, 2026-10-28).
- Facts:
  - CUSIP 91282CDC2, auctioned **Oct 21, 2021** ($19B), real yield −1.685% (a record low at auction), coupon 0.125%, breakeven 2.89%, matured 10/15/2026.
  - Annualized nominal return 2.375% vs the 5Y nominal yield of 1.20% in Oct 2021 (≈ +1.175 pp/yr); CPI averaged ~4.1%/yr.
- PRIMARY: TreasuryDirect auction record not checked, but the author is the primary analyst and the numbers are internally consistent.
- VERDICT: CONFIRMED (historical, low routing value).
- Owner: **CARL** (inflation) / BOND.

### 13 / 33. Hyperscaler spreads above July wides; AI-linked HY +100bp — @WarrenPies 2115081123030241647 (10/27 14:00Z), @junkbondinvest 2115052016225730579 (10/27 12:04Z)
- Full text read: yes, both. Pies's image is a 3Fourteen Research chart, "Long-Duration OAS and Semiconductor ETF Changes", daily 2026-04-01 to 2026-10-23, OAS change vs July 29:
  - Oracle 6.5% 2038: **+69.3 bp**
  - Meta 4.875% 2035: +17.8
  - Alphabet 4.8% 2036: −1.6
  - Amazon 4.875% 2036: −2.2
  - Microsoft 3.45% 2036: −19.4
  - SMH: +4.6%
- VERDICT (Pies): CORRECTED-FRAMING. Only Oracle (and Meta modestly) is above the July 29 levels; Alphabet and Amazon are about flat and Microsoft is tighter. "Hyperscaler spreads" is an Oracle-led move. Data through 10/23; single bonds per issuer.
- junkbondinvest: text only, no source or data. "AI-linked +100bp in a month", "CCC 4-year wides", "generic HY holding". Cross-check against ICE HY OAS: 3.40% (10/22) → 3.14% (10/28); headline HY is in fact tightening. "CCC 4-year wides" is consistent with ICE CCC OAS at its 2026 high of 13.56 on 10/23, but FRED can't test 4 years. The AI-linked basket is undefined. VERDICT: INDETERMINATE.
- Owner: **VULCAN** (AI credit), cc **LIQUID**.

## Unreached / not verified (unreached ≠ all-clear)
- ICE Endex official TTF settles (X26/Z26, 10/28).
- FRED pre-2023 ICE CCC history; Bloomberg BCAUOAS.
- treasurydirect.gov buyback pages (404 from this box).
- Bloomberg/Fastmarkets/CRU HRC; CME HRC (IP-blocked).
- TIC country tables and the "allies" analysis source.
- BofA flow note.
- JPMorgan loan-distress figures and CoreWeave figures in BullTheory #53.
