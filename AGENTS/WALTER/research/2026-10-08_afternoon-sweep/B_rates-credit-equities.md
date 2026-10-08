# Afternoon sweep, domain B: US rates, Treasury, Fed, credit, equities and banks

**Window:** Thu 2026-10-08, 12:00 ET to ~16:23 ET. **Author:** WALTER read-only sweep subagent. Writes nothing outside this file.
**Dedup basis:** BOARD SIG-W-20261008-008, -013, -017, -020 and -030, read before the sweep. Only changes are reported.
**Grades:** VERIFIED-PRIMARY = Treasury or Fed source. SECONDARY = named press or data vendor. UNVERIFIED = a single unconfirmed report or an inference.

---

## 1. The 30-year bond auction, 13:00 ET (VERIFIED-PRIMARY)

**Source:** Treasury Fiscal Data `auctions_query`, pulled ~16:05 ET:
`https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query?filter=security_type:eq:Bond,auction_date:gte:2026-06-01`
The results PDF is `R_20261008_3.pdf`, published under treasurydirect.gov/instit/annceresult/press/preanre/2026/.

**Security:** "Bonds of August 2056", **CUSIP 912810UW6**, **term "29-Year 10-Month"** (Treasury's label), **reopening**, 5.125% coupon, issued 2026-10-15, maturing 2056-08-15.

Bidder shares are computed on **competitive accepted ($21,939.6M)**. That is the basis CNBC and investingLive use, and their figures tie to it.

| Metric | **10/08 (today)** | 09/10 (prior reopening, same CUSIP) | 08/13 (original issue, $25B) | Change vs 9/10 |
|---|---|---|---|---|
| Offering | $22.0B | $22.0B | $25.0B | — |
| **High yield** | **5.618%** | 5.308% | 5.216% | **+31.0bp** |
| Price at high | 92.889131 | 97.262274 | — | — |
| Allotted at high | 26.77% | 64.29% | — | — |
| Median / low yield | 5.567% / 5.000% | 5.250% / 4.000% | — | — |
| **Bid-to-cover** | **2.54** | 2.61 | 2.39 | −0.07 |
| **Indirect** | **72.32%** ($15,866.1M) | 79.48% | 66.85% | −7.2pp |
| **Direct** | **20.89%** ($4,583.0M) | 18.31% | 21.64% | +2.6pp |
| **Primary dealers** | **6.79%** ($1,490.5M) | 2.21% | 11.51% | +4.6pp |
| SOMA add-on | $522.5M (total accepted $22,522.5M) | $0 | — | — |
| **Tail vs 1pm WI** | **+0.1bp** (WI 5.617%). SECONDARY: investingLive, with a Newsquawk headline "Tail 0.1bps" | Not retrieved | 0.4bp tail, WI 5.212% (investingLive, earlier) | — |

**Context:**
- **Highest 30-year auction yield since at least 2001**, computed from the full Fiscal Data record of nominal 30-year bonds (287 rows back to 1979).
  - Every 30-year auction from 2001 onward cleared lower. The highest were 5.52% on 2001-08-09, 5.46% on 2001-02-08 and 5.08% on 2006-08-10.
  - The last higher print in that dataset is **6.144% on 1999-08-12**.
  - ⚠️ The dataset shows no 30-year auctions in 2000. I have not verified whether that is a gap in the data, so **"since 1999" is not established**. The defensible claim is "highest since at least 2001".
- **Bid-to-cover of 2.54 is above the 12-auction average of 2.418** (computed, 2025-10-09 to 2026-09-10) and equals the highest since Jan-2020 (2.54). It is still below September's 2.61.
- **The read is mixed.** The yield is a multi-decade high, foreign/indirect take-up fell 7pp from September, and dealers were left with 3× September's share. Against that, demand beat the 12-month norms and the tail was only 0.1bp.
  - Peter Boockvar via CNBC: *"decent but nowhere close to as good as the 10 yr auction yesterday."* investingLive graded it "B".
- **Cash 30Y around the auction:** the CBOE ^TYX index (yfinance 1-minute bars) read 5.615% at 13:00 ET and 5.618% at 13:02 ET, so the auction priced at the market. That is a cash proxy, not the WI.

**Desk: BOND (action).** Info: RED (the auction-demand side of any long-end row) and TERRY (TLT).

---

## 2. Treasury buyback, 13:40–14:00 ET (VERIFIED-PRIMARY)

**Source:** Treasury Fiscal Data `buybacks_operations` + `buybacks_security_details`, pulled ~16:10 ET:
`https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/buybacks_operations` (results file `BBR_20261008174000.pdf`).

**Bucket verified: Nominal Coupons, 20Y to 30Y. Operation type "Liquidity Support". Settles Fri 10/9.** This is a different operation from 10/6 (2Y–3Y).

| Metric | **10/08 (today)** | 09/24 (first $6B 20–30Y op) | $2B-cap era, 20–30Y (Jun-2025 to Aug-2026) |
|---|---|---|---|
| Max redeemed | $6.0B | $6.0B | $2.0B |
| **Par offered** | **$14.886B** | $10.468B | $17.9–36.5B |
| **Par accepted** | **$6.000B (100% of max)** | $4.078B (68%) | $2.0B, full in all but 2 ops (3/19 $0.205B; 11/20/25 $0.785B) |
| Offered ÷ max | 2.48× | 1.74× | ~9–18× |
| Issues accepted / eligible | 10 / 34 | 12 / 35 | 2–14 / ~35 |

**Where the $6B went:** all of it went to low-coupon 2049–2051 paper. Nothing maturing 2052–2056 was accepted.

| Issue | Accepted | Weighted average price |
|---|---|---|
| 2.25% Aug-2049 (912810SJ8) | **$2.623B** (43.7%) | 56.117 |
| 2.00% Aug-2051 (912810SZ2) | $1.851B | 51.055 |
| 2.375% May-2051 | $0.701B | 56.263 |
| 1.875% Feb-2051 | $0.501B | 49.850 |
| 3.00% Feb-2049 | $0.316B | 66.070 |
| Five other issues | $1–2M each | — |

Components sum to $6,000M (checked).

**What changed:** this is the **first time the raised $6B long-end cap filled completely**; 9/24 took only 68%. Dealers offered less than they did when the cap was $2B ($14.9B against $18–37B), so the cover ratio is far thinner even though the fill was complete.
- RED-FT-11's buyback-suppressor classifier watches this operation. **I have not graded RED's row, which is RED's job.**
- Related, outside the window: on 10/1, a **10Y–20Y** $6B operation was offered $46.391B and accepted $6.0B (2 of 41 issues).

**Verification of SIG-W-20261008-013 (the 10/6 operation).** The squawk figures now check against the primary:
- $14.763B offered ✓, $1.327B accepted ✓, 12 of 33 issues ✓.
- Treasury labels the bucket **"2Y to 3Y"** (consistent with -013's "2028–2029 coupons").
- Two facts -013 lacked: the **maximum was $4.0B**, so 10/6 filled **33% of its cap**, and the operation type was "Liquidity Support".
- No figure in -013 is wrong. This is an upgrade to VERIFIED-PRIMARY, not a correction.

**Desk: BOND (action).** Info: RED (FT-11).

---

## 3. Fed, and the rates driver in the window

| Item | Time (ET) | Source + URL | Grade | Why it matters | Desk |
|---|---|---|---|---|---|
| **St. Louis Fed President Musalem:** *"To bring inflation back to target… more monetary policy firming will be required."* He would not commit on the Oct 27–28 meeting ("open mind"); "rates ought to be going up… in the next 6 to 9 months" if "timely" means ~18 months; labor market "balanced and stable"; nominal yields up because real yields are up, partly on rate expectations; AI investment and deficits are also pushing yields up; "financial conditions have tightened modestly and orderly". The venue is a Bloomberg event in New York per Reuters, the Minneapolis Fed per FXStreet (conflict unresolved). | ~13:57 ET (FXStreet 17:57Z; Reuters/Derby 18:09Z; investingLive 18:12Z) | Reuters via AOL: https://www.aol.com/articles/feds-musalem-says-lowering-inflation-180921000.html · FXStreet: https://www.fxstreet.com/news/feds-musalem-signals-more-tightening-as-inflation-stays-elevated-202610081757 · investingLive: https://investinglive.com/central-banks/fed-s-musalem-says-more-monetary-policy-firming-will-be-required/ | SECONDARY ×3 independent. Not on federalreserve.gov, because Reserve Bank presidents are not on the Board feed; stlouisfed.org not checked. | A second official in one day after Waller (-030) pointing to more hikes, with a 6–9 month horizon. Not a 2026 voter. | HENRY (action); LIQUID info |
| **Trump on Truth Social:** "we will not be attacking Iran at any time prior to the Midterm Elections… November 3rd"; the blockade stays; "22 Million Barrels" through Hormuz "last night". | **12:17 ET** (decoded from the post ID 117406186276133332; CBS posted it 12:45 ET) | CBS live blog: https://www.cbsnews.com/live-updates/iran-war-nuclear-donald-trump-vance-rubio-strait-of-hormuz/ · post: https://truthsocial.com/@realDonaldTrump/posts/117406186276133332 | SECONDARY (CBS quoting the post; the post itself was not opened). The 22M-barrel figure is the administration's claim and is unverified. | **This is the afternoon rates driver.** Brent fell from $105.41 to $103.65 in the 12:10–12:15 ET bar (yfinance BZ=F), and the 30Y fell from 5.659% at 12:00 to 5.618% at 12:45 (^TYX). CNBC credits both the post and the auction for the yield reversal. Post-dates -020 (11:45 ET), so it is **not on the BOARD**. | Primary owner is Domain A (FALCON / BRENT); BOND and HENRY info for the rates channel |
| **Treasury OFAC:** "Operation Economic Outcast Neutralizes Iranian Regime's Remaining Shadow Fleet Network" (CBS: 17 vessels) | 13:00 ET | https://home.treasury.gov/news/press-releases/sb0653/ | VERIFIED-PRIMARY (title and time only; body not read) | Iran sanctions, not rates | Domain A (FALCON / BRENT) |
| federalreserve.gov feeds: **no** Board speech or press release in the window. The latest items are Waller at 04:30 ET today (already in -030) and the FOMC minutes on 10/7 at 14:00 ET. | Feeds pulled 16:19 ET | https://www.federalreserve.gov/feeds/speeches.xml · https://www.federalreserve.gov/feeds/press_all.xml | VERIFIED-PRIMARY (an absence, on Board feeds only) | — | — |

The H.4.1 release is due at 16:30 ET Thursday, after this sweep. It was not read.

---

## 4. Closes on 10/08

**Basis:** yfinance daily bars, pulled 16:20 ET.
- Equities and ETFs: the last 1-minute bar is 15:59 ET, so these are regular-session closes.
- ^TNX / ^TYX: CBOE yield indices, last bar 14:59 ET.
- ^VIX: last bar 16:04 ET, **before the 16:15 ET VIX close**, so this is not the official close.

| Item | Value | Change | Source / time | Grade | Why it matters | Desk |
|---|---|---|---|---|---|---|
| S&P 500 | **7,765.36** | −0.47% (prev 7,801.77) | yfinance ^GSPC, 15:59 ET bar | SECONDARY | Rates eased but stocks still fell | HENRY |
| Nasdaq-100 | **30,725.81** | **−1.39%** (prev 31,160.08) | yfinance ^NDX | SECONDARY | Tech led the decline. NDX opened down ~0.6% and lost about a further 0.8% after 12:00 (30,934 → 30,697 at 13:00) even as yields fell. **Afternoon cause not found** (see queries). The morning chip selloff after Samsung's results is a morning story, outside this window and not verified. | HENRY, VULCAN info |
| QQQ | **$747.58** | −1.34% | yfinance | SECONDARY | — | HENRY |
| **KRE (regional banks)** | **$69.59** | **+1.02%** (prev 68.89) | yfinance | SECONDARY | **Reversed:** −0.6% intraday at 11:57 (-030), 68.65 at 12:00, then +1.02% at the close. | REGINALD |
| VIX | **15.48** | +2.65% (VIXCLS 10/7 15.08) | yfinance, 16:04 ET print, not the 16:15 close | SECONDARY | Still low while the NDX fell 1.4% | HENRY |
| **10Y Treasury** | **5.231%** | −4.6bp (prev 5.277) | CBOE ^TNX, 14:59 ET. CNBC 16:06 ET: 5.229% | SECONDARY | Off the 24-year high. FRED DGS10 for 10/8 posts tomorrow (latest: 5.28% on 10/7). | BOND |
| **30Y Treasury** | **5.606%** | −5.5bp (prev 5.661) | CBOE ^TYX, 14:59 ET. CNBC 16:06 ET: 5.602%. Intraday high 5.698%, low 5.601% | SECONDARY | Closed **below the 5.618% auction stop**, so buyers marked to a small gain. FRED DGS30 for 10/7 is **5.67%**. ⚠️ -030 called the 10/5 30Y close of 5.66% the high, but 10/7's 5.67% is higher by 1bp (minor, flagged to BOND) | BOND |
| 5Y / 13-week | 4.991% (−3bp) / 4.043% (+0.6bp) | — | CBOE ^FVX / ^IRX | SECONDARY | The curve's long end rallied most | BOND |
| TLT | $77.87 | +0.93% | yfinance | SECONDARY | -030 cites TERRY's 82 strike | TERRY info |
| HYG / JNK | $77.14 / $92.73 | −0.05% / −0.03% | yfinance | SECONDARY | High-yield ETFs flat: no visible credit stress today. **HY OAS for 10/8 is not out** (FRED T+1). Latest is 309bp on 10/7 (CCC 1,229bp), already on -030. | LIQUID |
| Big banks | JPM 331.42 (+0.56%), BAC 53.61 (+0.17%), C 128.08 (+0.60%), **WFC 82.03 (+2.21%)**, GS 882.59 (−0.52%) | — | yfinance | SECONDARY | Bounce after -030's drawdown table. JPM reports Q3 Tue 10/13 before the open (calendar listing via search; not verified at JPM IR). | REGINALD |
| Regionals | WAL 75.50 (+1.55%), ZION 62.73 (+1.31%) | — | yfinance | SECONDARY | Moved with KRE | REGINALD |
| **OZK** | **$44.86** | **+2.98%** (prev 43.56), volume 2.37M | yfinance | SECONDARY | Rebounded but **closed below the 45 band for the 3rd straight session**. The band call belongs to the OZK desk; this is not a grade. Nothing new on the RaDD loan was found (row below). | OZK, TERRY info |
| BDC / alternative managers | OWL 9.27 (+1.76%), ARCC 18.74 (+1.57%), BIZD 12.17 (+1.16%), BX 112.68 (+0.76%), APO 115.30 (−0.22%), KKR 89.56 (−0.12%), ARES 116.26 (+0.44%) | — | yfinance | SECONDARY | No stress print in the listed names | BROCK |

### Bank OZK RaDD: anything new after -017?
| Item | Time | Source | Grade | Verdict |
|---|---|---|---|---|
| The Real Deal, "Loan modification again highlights Bank OZK exposure" | 14:53 ET (datePublished 18:53Z) | https://therealdeal.com/national/2026/10/08/loan-modification-again-highlights-bank-ozk-exposure/ | SECONDARY (re-reports Bisnow and Citi) | **NOT NEW.** It repeats the 10/9 maturity and Citi's "brief forbearance period" line. Its OZK spokesperson quote, via Bisnow, *"short-term extensions routinely occur as the parties finalize documentation for longer-term extensions"*, is the "issuer: routine" side already in -017. No sixth modification, extension, default, 8-K or statement found as of ~16:20 ET. **The 10/9 bridge maturity remains the open item.** |

---

## 5. US data and policy in the window
| Item | Result |
|---|---|
| Treasury debt management (refunding, buyback schedule change) | **Nothing in the window.** The Treasury press-release list's only 10/8 item is the 13:00 ET OFAC Iran release. |
| US data releases in the window | **None found.** Thursday's 08:30 data is outside the window. |
| Tariffs / shutdown | **Nothing in the window found.** Two searches (queries below) returned nothing dated 10/8. A low-quality site claims a stopgap funds the government to Dec 11 (UNVERIFIED, outside the window, not routed). |
| Credit events (fund gates, defaults) | **No named US HY default, bankruptcy or fund gate dated 10/8 in the window found.** Search turned up New World Development's (Hong Kong) ~$991M USD-note exchange offer, which expires 10/20. It is dated around 10/6–8 and is outside the US scope; flagged for possible ZHAO/LIQUID interest, UNVERIFIED. |

---

## NOTHING NEW FOUND (state the queries; one search is not proof of absence)
- **Other Fed speakers in the window besides Musalem:** checked the federalreserve.gov speeches and press RSS (Board only) and searched "Fed speaker October 8 2026 remarks rates" and "Fed president says October 8 2026 inflation rate hike Hammack OR Logan OR Musalem OR Goolsbee OR Kashkari OR Schmid OR Daly OR Barkin OR Bostic OR Williams". Only Musalem surfaced. Regional Fed sites other than St. Louis were not checked.
- **Cause of the NDX's afternoon leg:** searched "Nasdaq falls October 8 2026 stocks tech selloff" and found no 10/8 recap. **Cause unknown.**
- **KRE reversal driver:** searched "regional bank stocks rally October 8 2026 KRE" and found nothing. Lower yields after 12:17 is a plausible driver but an **inference, UNVERIFIED**.
- **OZK / RaDD:** searched "Bank OZK RaDD IQHQ loan October 2026". The only new-dated item is The Real Deal (not new). Not checked: SEC EDGAR 8-K for OZK, San Diego County recorder.
- **Credit events:** searched "private credit fund redemptions gate BDC October 8 2026" and "high yield bond default OR distressed exchange OR bankruptcy filing October 8 2026 company". Nothing dated 10/8 in the US.
- **Tariffs / shutdown / Treasury:** searched "Trump tariff announcement October 8 2026", "government shutdown news October 8 2026" and "tariff OR shutdown OR Treasury announcement October 8 2026 afternoon Bessent", and checked the home.treasury.gov press-release list.
- **30Y tail:** searched "30-year bond auction October 8 2026 tail when-issued" and "\"30-year\" bonds \"5.618%\" WI". The WI comes only from investingLive and Newsquawk headlines, so it is SECONDARY.

## Sources used
- Treasury Fiscal Data API: auctions_query, buybacks_operations, buybacks_security_details (primary)
- federalreserve.gov RSS: speeches.xml, press_all.xml (primary)
- home.treasury.gov/news/press-releases (primary)
- CNBC: https://www.cnbc.com/2026/10/08/us-treasury-yields-30-year-bond-auction.html (modified 20:06Z)
- investingLive: https://investinglive.com/news/us-treasury-sells-22-billion-of-30-year-bonds-at-a-high-yield-of-5-618/
- CBS live blog (Iran), The Real Deal (OZK), Reuters via AOL / FXStreet / investingLive (Musalem): URLs inline above
- yfinance via `FORGE/tools/market-data/fetch.py` and direct yfinance calls (closes, intraday). FRED via `fetch.py fred` (HY 309bp / CCC 1,229bp / DGS10 5.28% / DGS30 5.67%, all observations dated 10/7).
