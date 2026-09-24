# CARL data catch-up — 2026-09-24 (7-day gap since 9/17)

**What this file is:** the source record behind the 2026-09-24 STATUS refresh. Sections A–C were gathered by three read-only research sub-agents (Opus) and are reproduced verbatim, including their own P/S (primary/secondary) labels and stale-year rejections. CARL did sections D–E directly. CARL did not re-verify every agent figure; STATUS cites only the figures marked primary, or labels them secondary.

## D. CARL-direct: FSA portfolio file (docket row 9/18, run 9/24)
- HEAD 2026-09-24T16:58Z: `Last-Modified: Fri, 18 Sep 2026 21:16:38 GMT`, 134,144 B, ETag `d443da744eb7102b6b5f366e39a8e1a0:1790013773.280008`. Baseline was Thu 18 Jun 2026 21:05 GMT, 133,120 B. **CHANGED.** HTTP/2 failed once (curl err 92); `--http1.1` worked.
- Copy: `domain/sources/2026-09-24_FSA_PortfoliobyLoanStatus_LM-2026-09-18.xls` (MD5 d443da74…, equals the ETag prefix).
- Federally Managed sheet, $B / recipients M, FY2026 Q2 (3/31) → Q3 (6/30): Repayment 632.8/17.2 → 658.5/17.4 · Deferment 156.5/3.6 → 149.7/3.3 · Forbearance 484.6/8.4 → 459.2/8.0 · **Cumulative in default 220.3/9.0 → 234.1/9.3** · Other 8.5/0.2 → 8.9/0.2. Q1 → Q2 default change was +39.8/+1.3.
- Direct Loan sheet Q3: default 187.8 / 7.55; forbearance 449.7 / 7.98. FFEL (all holders) Q3: default 69.3 / 3.19.

## E. CARL-direct: V2 August broad tier (OTTO `panel_10d.py --history 2 --dry-run`, 2026-09-24T13:02, positive control PASS; nothing written to OTTO's ledger)
| Deal | Aug-26 60+ | Aug-25 60+ (OTTO PANEL_10D.tsv) | YoY Aug | Jul-26 | Jul-25 | YoY Jul |
|---|---|---|---|---|---|---|
| SDART 2022-6 | 11.01 | 9.98 | +1.03 | 10.79 | 9.99 | +0.80 |
| SDART 2023-1 | 10.09 | 9.37 | +0.72 | 10.23 | 9.49 | +0.74 |
| SDART 2024-1 | 9.90 | 8.39 | +1.51 | 9.70 | 8.25 | +1.45 |
Broad mean +1.09pp (July +1.00pp). 0 of 3 improving. Level-vs-base split of the Jul→Aug change in the YoY gap: 2022-6 level +0.22 / base −0.01; 2023-1 level −0.14 / base −0.12; 2024-1 level +0.20 / base +0.14. Deep tier (EART) August not yet filed. Carvana tier (BLAST, not in L3) 60+: 2024-1 15.30→16.48, 2023-1 14.80→15.82 MoM. Double-matched control: NOT computed this pass.

## F. CARL-direct: HY spreads (FRED, same-date)
9/23: HY 2.73 / CCC 10.93 / BB 1.59 → CCC−BB 934bp, the maximum of the series since 2025-01-01 (computed over FRED CSV from 2025-01-01). Prior days: 9/18 928, 9/21 924, 9/22 919.

## G. Boot instrument defect found and fixed
`boot.py` collapsed view printed Ally's 4 new 10-Ds (9/23) under the Exeter V2-panel header: the Exeter header survived only because "REGISTERED" contains the marker "RED". Raw `abs_monitor.py` output was correct. Fixed in `collapse_output()`: section headers print only above a surviving line in their own section.

---
## A. Energy / Fed / claims sweep (agent)
# Energy / Fed / Claims sweep — pulled 2026-09-24 (~12:45–13:10 ET)

Every value below was checked against the year 2026 at the source. "PRIMARY" means I read it on the issuer's page or file myself (the raw CSV, PDF or HTML, not only the WebFetch summary, wherever noted).

## 1. Retail gasoline

### AAA national average, regular (gasprices.aaa.com, PRIMARY)
| Date (2026) | Regular | Basis / source |
|---|---|---|
| Thu 9/24 | **$4.4825** | AAA national page "Price as of 9/24/26" — https://gasprices.aaa.com/ ; also AAA 9/24 post |
| Wed 9/23 | $4.4744 | AAA national page, "Yesterday Avg" |
| Thu 9/17 | $4.4386 | AAA national page "Week Ago" + AAA 9/17 post |
| Thu 9/10 | $4.2770 | AAA 9/17 post "One Week Ago" + 9/10 post |
| Thu 9/3 | $4.1436 | AAA 9/3 post |
| 8/24 (month ago) | $4.0991 | AAA national page |
| 9/24/2025 (year ago) | $3.1634 | AAA national page |
| 9/18–9/22 daily | NOT OBTAINED | AAA publishes only current, yesterday, week-ago, month-ago and year-ago values. It has no public daily history, and its weekly posts are Thursdays only. |

**Key question: did AAA regular reach $4.50 in September 2026? No such day is documented.** The highest AAA daily national figure I can document for September is **$4.4825 on 9/24**, which is today and is also the latest print. The documented points rise every time: 4.1436 → 4.2770 → 4.4386 → 4.4744 → 4.4825. A move above $4.50 and back within 9/18–9/22 cannot be ruled out without daily data, but it is implausible because the gaps between the documented points are only about 1¢ a day.
- AAA 9/24 post, verbatim: "At $4.48 per gallon, this is the highest the national average has ever been **for this time of year**." Also: "So far, the average for this month is $4.30, higher than the previous September record of $3.83 set in 2023." — https://gasprices.aaa.com/national-average-climbs-nearly-5-cents-since-last-week/
- AAA 9/17 post, verbatim: "the national average is inching closer to **this year's record high of $4.56 set on May 21**. The all-time high for the national average is $5.01 set on June 14, 2022." — https://gasprices.aaa.com/pump-prices-keep-climbing-as-crude-oil-remains-high-2/ → **AAA was above $4.50 earlier in 2026 (May 21: $4.56), but not in September.**
- AAA national all-time highs (national page): Regular $5.0165 on 6/14/22; **Diesel $6.5276 on 9/22/26 (a new all-time record set this week)**.

### AAA other grades today (9/24/26, PRIMARY)
| Series | Today | Yesterday | Week ago | Month ago | Year ago |
|---|---|---|---|---|---|
| National diesel | **$6.5141** | $6.5217 | $6.3956 | $5.6134 | $3.6930 |
| Florida regular | **$4.3820** | $4.2941 | $4.2986 | $3.8467 | $3.0339 |
| Florida diesel | $6.1943 | $6.2264 | $6.3480 | $5.4724 | $3.5581 |

The Florida figures come from https://gasprices.aaa.com/?state=FL . FL regular rose **8.8¢ in one day** (4.2941 → 4.3820). The FL diesel record is $6.3492 on 9/18/26, and FL diesel is now easing. The FL regular record is still $4.8907 (6/13/22).

### EIA weekly retail (FRED, PRIMARY — raw CSV read)
| Week (Mon) | GASREGW regular | GASDESW diesel |
|---|---|---|
| **2026-09-21** | **$4.478** ✅ confirms our pull | **$6.529** |
| 2026-09-14 | $4.319 | $6.285 |
| 2026-09-07 | $4.157 | $5.967 |
| 2026-08-31 | $4.071 | $5.599 |

Source: https://fred.stlouisfed.org/graph/fredgraph.csv?id=GASREGW,GASDESW . Week over week: regular +15.9¢, diesel +24.4¢. Caveat: FRED's GASREGW column is blank for 6/22 and 6/29/2026 (a gap in the series; this does not affect the latest values).

## 2. EIA on-highway diesel
GASDESW = **$6.529, week of 2026-09-21** (prior week $6.285). PRIMARY (FRED raw CSV).

## 3. Brent — two DIFFERENT instruments, do not splice
| Date | Brent SPOT (FRED DCOILBRENTEU, EIA/Europe Brent spot FOB) | Brent FUTURES front-month (BZ=F, Yahoo; NYMEX Brent Last Day Financial, tracks ICE) | Spot minus futures |
|---|---|---|---|
| 9/15 | **$130.80** ✅ | $108.75 | +$22.05 |
| 9/16 | $127.84 | $105.83 | |
| 9/17 | $121.18 | $104.82 | |
| 9/18 | $119.66 | $103.87 | |
| 9/21 | $116.15 | $100.34 | |
| 9/22 | **$114.89** ✅ (latest spot on FRED) | **$99.25** (Reuters settle, confirmed) | +$15.64 |
| 9/23 | not yet on FRED | $103.08 (Yahoo daily close) | |
| 9/24 | — | $105.07 **intraday, 12:50 ET, NOT a settle** | |

- The spot series is PRIMARY (FRED raw CSV, read myself). The futures series is SECONDARY: Yahoo chart API, https://query1.finance.yahoo.com/v8/finance/chart/BZ=F . Reuters, via Yahoo Finance on 9/22, gives the 9/22 settle as "$99.25, down $1.09".
- **Change 9/15→9/22:** spot −$15.91; futures −$9.50. The spot premium over futures narrowed from $22 to $16, so physical crude was tighter than futures and has been easing faster.
- **Drivers reported by the wires (SECONDARY):**
  - Reuters, 9/22: Saudi crude moving through Hormuz averaged "about 2.9 million barrels a day over the last six days, up from roughly 700,000 barrels a day in August"; the Saudi East-West pipeline restarted after the drone disruption of 9/13; Yanbu port was due to resume exports; an Iranian official said Iran could reopen the Strait within a week if the U.S. eased military pressure and lifted its port blockade. https://finance.yahoo.com/energy/articles/oil-rises-slightly-ahead-potential-003404571.html
  - Bloomberg via World Oil, 9/21: Brent "declined for a fourth session, settling 3.4% lower" to about $100; Saudi exports via Hormuz rising; hopes of U.S.–Iran diplomacy at the UN General Assembly. https://www.worldoil.com/news/2026/9/21/brent-falls-to-100-as-strait-of-hormuz-oil-flows-increase/
  - CNBC, 9/17 (headline only; the page returned 403): "Oil prices fall as Saudi Arabia reportedly offers more crude via Hormuz after pipeline attack."
- The cause of the 9/23 rebound to $103 is NOT OBTAINED. AAA's 9/24 post has WTI settling 9/23 at $92.16, up $1.64.

## 4. FOMC, 9/15–16/2026 (all PRIMARY, federalreserve.gov)
- **Statement** (https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm): "approved … by a 12 – 0 vote: The Committee decided to raise the target range … by 1/4 percentage point to 3-3/4 to 4 percent … Inflation remains elevated. Today's policy action will support a timelier return to the Committee's 2 percent goal. The Committee will deliver price stability." The statement contains **no easing language and no explicit guidance toward further hikes.**
- **Transcript:** https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20260916.pdf (Chairman **Warsh**, 15 pp., marked FINAL)

**(a) Easing, or the cycle being done: none.** The Chair never signals a cut or an end to hikes. He repeatedly refuses forward guidance:
- p.4–5: "I'm not in the forward guidance business … I'm not going to prejudge any future decisions we make."
- p.13: "My business is to not give forward guidance … Today's action **starts to show** we're serious about this … when we continue our discussions over the course of the next several weeks and months, we'll have more to say about it. But I'm ill-prepared to prejudge those future actions."

**(b) Further hikes, signalled only implicitly:**
- p.1: "I would be hard pressed to describe broad financial conditions as restrictive … So we removed a dose of accommodation."
- p.7: "my colleagues were hard pressed to describe it that way, too … we'll continue to evaluate that prospectively."
- p.3: "The median participant judges that the appropriate federal funds rate to be 4.1 percent at the end of this year and to remain there next year. Inflation risks are to the upside while labor risks are roughly balanced."
- p.14: "the job we'll continue to do, is to ensure price stability."

**(c) Consumers, households, energy and labor:**
- Labor, p.2: "The jobless … rate remains low at around 4.1 percent … Unemployment claims, on a four-week moving average, are running at levels consistent with full employment. So the labor side … is in good shape."
- Inflation, p.2: "total PCE prices likely was around 3.6 percent in August. Core PCE and CPI prices are running at about 3.2 and 2.4 percent."
- Energy, p.4 (CBS asked about Hormuz): "We cannot affect any individual price, whether it be oil prices, whether it be foodstuffs … what we can do, and will do, is ensure that any change in relative prices don't broaden out."
- Energy, p.12: "It's not simply spot prices of energy … but it's the difference between those spot prices and so-called crack spreads—what that means for products that find their way into stores."
- Households, p.9 (NBC asked who is "least well off" and pinched by gas, groceries and mortgages): "people that don't own financial assets—call that a bit less than 50 percent of the country. They don't have equity in their home … So they're living off their paycheck that comes every couple of weeks … in aggregate, we're running more or less at full employment … stable prices … offers good news."
- Labor, p.14: "I don't believe that we need to do harm to the labor markets to achieve our objective."
- p.6 (retail sales question): "I'm not a data-point-dependent guy."

**SEP median (PRIMARY, https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm):**
| | 2026 | 2027 | 2028 | 2029 | Longer run | June 2026 medians (2026/27/28/29) |
|---|---|---|---|---|---|---|
| Fed funds | **4.1** | **4.1** | 3.9 | 3.6 | 3.2 | 3.8 / 3.6 / 3.4 / 3.1 |
| PCE | 3.7 | 2.3 | 2.1 | 2.0 | 2.0 | 3.6 / 2.3 / 2.0 / 2.0 |
| Core PCE | 3.4 | 2.5 | 2.2 | 2.0 | — | 3.3 / 2.5 / 2.1 |
| Unemployment | 4.1 | 4.1 | 4.1 | 4.1 | 4.2 | 4.3 / 4.3 / 4.2 / 4.2 |
| Real GDP | 2.3 | 2.4 | 2.2 | 2.1 | 2.0 | 2.2 / 2.3 / 2.2 / 2.0 |

**Dot counts (Figure 2, parsed from the HTML table):**
- **2026:** 4 at 4.375, **12 at 4.125**, 2 at 3.875. Against today's 3.875 midpoint, **16 of 18 see at least one more 25bp hike in 2026** (4 see two) and 2 see none.
- **2027:** 8 at 4.375, 6 at 4.125, 3 at 3.625, 1 at 3.125. The median is flat at 4.125, and 4 of 18 have cuts back below today's level.
- **Cuts start in 2028**, with the median at 3.9.

**Fed speeches 9/17–9/24** (the federalreserve.gov speeches RSS lists four):
- **Barr, 9/23, "A Long-Term View on the Costs of Shelter"** — https://www.federalreserve.gov/newsevents/speech/barr20260923a.htm . Verbatim: "inflation is above our 2 percent target and not clearly trending toward target in a timely way. Moreover, risks to achieving our inflation target have increased, while risks to the labor market have receded. The FOMC took important action to that end last week by increasing the policy rate, which I supported. **In my base case, further policy adjustments are likely to be needed** to ensure inflation comes down to target in a timely fashion." → **hawkish, signals further hikes.**
- Jefferson, 9/22 (discount window / Treasury market), Bowman, 9/18 (stress testing), and Bowman, 9/18 (SVB review): **no forward-guidance content** found in keyword scans (policy rate / inflation / easing).
- Regional Fed presidents' remarks (not on the Board RSS) were NOT searched.

## 5. Weekly jobless claims (DOL)
| Release | Week ending | Initial claims SA | 4-wk MA | Continuing claims SA (week ending) | Source |
|---|---|---|---|---|---|
| **Thu 9/24/26** | **Sep 19** | **197,000** (−1,000) | **202,250** (−1,750) | **1,719,000** (w/e **Sep 12**; +2,000); 4-wk avg 1,744,000; IUR 1.1% | PRIMARY — https://www.dol.gov/ui/data.pdf (PDF text read) |
| Thu 9/17/26, as first published | Sep 12 | 196,000 | 203,250 | 1,730,000 (w/e Sep 5); a Reuters note gave a 39K drop, "lowest since Jan 2024" | Published values confirmed from the 9/24 PDF's revision lines. The 9/17 release itself was not retrieved (dol.gov returned 403 to curl; Detroit News returned 402). |
| 9/12 week, as revised on 9/24 | Sep 12 | **198,000** (up 2K) | **204,000** (up 750) | 1,717,000 (w/e Sep 5, down 13K) | PRIMARY (9/24 PDF) |

- The 197K figure is the w/e Sep 19 advance print and matches FRED ICSA and IC4WSA (202,250).
- NSA initial claims for w/e 9/19 were 163,811, against 180,992 in the same week of 2025.
- Reuters had expected 208K for the 9/17 release; the 9/17 dip was flagged as possibly Labor Day seasonal noise (secondary, search snippet).

## Source weaknesses
1. AAA has no daily history, so the 9/18–9/22 dailies are missing. The "never hit $4.50 in September" conclusion rests on documented points that rise every time, not on a complete daily series.
2. The Brent futures series is secondary (Yahoo). Only the 9/22 settle is cross-confirmed (Reuters). The 9/24 value is intraday.
3. The 9/17 DOL release PDF was not directly retrieved; its as-published values are taken from the 9/24 primary PDF's revision lines.
4. Brent spot on FRED lags; the last value is 9/22.

---
## B. Credit / housing sweep (agent)
# CARL sweep — consumer credit & housing (gathered 2026-09-24, Thu)

P = primary (issuer page/PDF fetched); S = secondary (trade press / search snippet); every year was checked as 2026 at the fetched page unless marked.

## 1. ICE First Look — AUGUST 2026: **NOT OBTAINED**
Tried: `mortgagetech.ice.com/.../first-look-at-august-2026-mortgage-data` (404), the ICE data-reports index (latest listed = July First Look), ir.theice.com press list (no list rendered), 4 web searches. Release cadence: June data came out 7/24 and July data on 8/25, so August is probably due around 9/24–9/25. **Re-check tomorrow.** The latest available data is July:

| Metric (July 2026) | Value | MoM | YoY | Source |
|---|---|---|---|---|
| National DQ (30+, excluding foreclosure) | **3.39%** | −16 bp (−4.56%) | +12 bp (+3.69%) | P ICE [First Look Jul-26](https://mortgagetech.ice.com/resources/data-reports/first-look-at-july-2026-mortgage-data), rel. 8/25/26; table via S [INN repost](https://investingnews.com/ice-first-look-at-mortgage-performance-mortgage-delinquencies-ease-in-july-as-both-new-defaults-and-cure-activity-improve/) |
| vs July 2019 pre-pandemic | −41 bp (Mortgage Monitor) / −46 bp (First Look page) | | | ⚠️ ICE's two surfaces disagree |
| 30+ DQ count | 1,875,000 | −86k | +81k | INN repost of the ICE table |
| 90+ DQ count | 563,000 | −7k | +97k | same |
| FC pre-sale inventory | 296,000 (0.54%) | +4k | +89k (+42%) | same |
| FC starts | 40,000 table / **38,600** ICE page text | −8.3% | +22.8% / +23% | ⚠️ inconsistent across ICE surfaces |
| FC sales | 7,900 | +8.4% | +14.2% | same |
| New 90+ rolls | 102,000 | | −4% YoY; FHA −13% YoY | P ICE page |
| Top non-current states | LA 8.20, MS 8.13, AL 5.99, IN 5.99, AR 5.57 | | | FL not in top/bottom 5 |
| Prior month (June) | 3.55%; FC starts 43,200 (6-yr high) | | | S HousingWire/BusinessWire, rel. 7/24 |

ICE's September Mortgage Monitor (rel. 9/11/26, S [CalculatedRisk](https://calculatedrisk.substack.com/p/september-ice-mortgage-monitor-annual)): ICE HPI August **+1.5% YoY** (6th straight month of acceleration, but momentum cooling). FL: **Cape Coral −2.3% YoY**; Miami +1.6% YoY (ranked 49th, up from 94th). FHA/VA split: not given in the public text.

## 2. Auto ABS indices
| Series | Value | Period | Release | Source |
|---|---|---|---|---|
| Fitch subprime 60+ DQ, **AUGUST** | **NOT OBTAINED** | Aug-26 | — | 5 searches; no Fitch page and no trade-press article found |
| Fitch subprime 60+ DQ | **6.13%** (+33 bp MoM) | Jul-26 | article dated 9/21/26 | S [CUCollector blog](https://blog.cucollector.com/the-seasonal-loan-delinquency-reprieve-may-be-ending/) (not Fitch primary) |
| Fitch subprime 60+ DQ | 5.80% | Jun-26 | — | same S. ⚠️ Another snippet gives "5.67% Jun-26 vs 6.31% Jun-25" — conflicting and unverified |
| Fitch subprime 60+ DQ record | 6.90% | Jan-26 index (Dec-25 collection period) | — | S [Auto Remarketing](https://www.autoremarketing.com/subprime/fitch-stress-in-subprime-surfaces-through-auto-abs-trends/) |
| Fitch subprime annualized net loss (ANL) | 9.81% (Jan-26); TTM 9.00% | Jan-26 | — | same S. **No Aug/Jul ANL figure found** |
| Subprime recovery rate | 39.5% Jun → 38.0% Jul | Jul-26 | 9/21 | S CUCollector (index source unstated) |
| Fitch prime 60+ | NOT OBTAINED for 2026 | | | |
| **KBRA auto ABS, August 2026** | Prime: ANL and both DQ measures moved ≤4 bp MoM and YoY. **Non-prime: ANL +67 bp MoM (+34 bp YoY); early-stage DQ +5 bp MoM (+26 bp YoY); late-stage DQ −9 bp MoM (−5 bp YoY)** | Aug-26 | **9/16/26** | P [KBRA](https://indices.kbra.com/publications/nGfSyykg/u-s-auto-loan-abs-indices-august-2026?format=web). Levels are paywalled; only the changes are public |
| S&P auto ABS tracker | NOT OBTAINED (search returned only 2023–24 pages) | | | |

⛔ **Stale-year trap caught:** search snippets gave "subprime ANL 8.9% in August, up 27%, 60+ at 4.9%; prime 0.4%/0.6%". Those figures come from a **~2015** Auto Finance News article (it cites 2013–15 vintages). Also rejected: Auto Remarketing "softens in September" = **Sept 2014** data (4.34%/7.08%). **Do not use either.**

## 3. Credit bureaus / VantageScore
| Metric | Aug-26 | Aug-25 | Source |
|---|---|---|---|
| VantageScore 30–59 DPD | 1.02% | 1.02% (unchanged) | P-ish: [BusinessWire via FinancialContent](https://www.financialcontent.com/article/bizwire-2026-9-24-vantagescore-creditgauge-august-2026-new-consumer-credit-card-accounts-grow-as-lenders-tap-credit-demand), rel. **9/24/26** |
| 60–89 DPD | 0.38% | 0.40% | same |
| 90–119 DPD | 0.22% | 0.22% | same |
| Average VantageScore 4.0 | 701 | — | same |
| Average balance | $107.5K (+$1,176, +1.1% YoY) | | same |
| Utilization | 49.60% | 50.80% | same |
| Card originations | 3.77% | 3.70% | +0.11 pt MoM |
| **By score tier / income** | **NOT in the public release.** No K-shape split was available; the CreditGauge Live dashboard was not queried | | |
| Equifax Market Pulse (Aug-26 webinar) | Qualitative only: revolving DQ still falling YoY; installment mixed, with **first mortgage the exception (DQ up YoY)**; growth in HELOC use | | S [Equifax blog](https://www.equifax.com/business/blog/-/insight/article/august-2026-consumer-pulse-the-latest-consumer-credit-trends/); no figures captured |
| TransUnion monthly, 9/15–9/24 | NOT FOUND. Latest is the Q2-26 CIIR ("More Americans have access to credit…") | | [TU newsroom](https://newsroom.transunion.com/Q2-2026-CIIR/) |

## 4. Cox Automotive
| Metric | Value | Release | Source |
|---|---|---|---|
| Manheim UVVI, mid-Sept (first 15 days) | **206.2**; −1.0% MoM (seasonally adj.), −1.1% unadjusted | **9/18/26** | P [Cox](https://www.coxautoinc.com/insights/manheim-used-vehicle-value-index-mid-september-2026-trends/) |
| YoY | **−0.4% SA (first negative YoY of 2026)**; −1.1% NSA | | same |
| Segments | Only compacts and EVs (+2.3%) above year-ago; non-EV −1.3%; midsize, pickups, SUVs negative | | same (Cox cites higher gas prices / Middle East) |
| Wholesale days' supply | 27.8 days (+2.4 YoY); sales conversion 55.8% (−1.4 pt) | | same |
| Dealertrack Credit Availability Index, Aug | **105.3** (+0.4% MoM, +7.7% YoY; highest since Nov-2015) | **9/10/26** | P [Cox CAI](https://www.coxautoinc.com/insights/aug-2026-cai/) |
| Subprime share of originations | **16.6%** (+20 bp MoM; +300 bp YoY from 13.6%) | | same |
| Approval rate | 73.9% (+20 bp MoM; −50 bp YoY) | | same |
| Negative equity / >72-month loans / down payment | 57.4% / **31.3% (record)** / 13% (matches Oct-22 low) | | same |
| Average contract rate / yield spread / 5-yr UST | 10.99% / 6.61% (+4 bp) / 4.38% (highest since Jan-25) | | same |
| Cox repossession note | NOT FOUND | | |

## 5. Housing sales
| Metric | Value | Release | Source |
|---|---|---|---|
| **Existing home sales, Aug-26** | **3.98M SAAR**, −2.0% MoM, −1.2% YoY | **9/10/26**, earlier than the ~9/22 you expected | P [NAR](https://www.nar.realtor/newsroom/nar-existing-home-sales-report-shows-2-0-decrease-in-august) |
| Median price | $429,100, +1.6% YoY (38th straight YoY gain); SF $434,800 (+1.7%); condo $371,600 (+1.5%) | | same |
| Inventory / months' supply | 1.62M / 4.9 months | | same |
| First-time buyers / all-cash / distressed / days on market | 30% / 27% / 2% / 31 days | | same |
| South | 1.84M (−1.6% MoM, flat YoY); median $366,500 (+0.7%) | | same |
| ⛔ Rejected | One search snippet said "3.62M". That is not the NAR figure. | | |
| **New home sales, Aug-26** | **684k SAAR**, +6.4% MoM (±19.5%, not statistically significant); −2.0% YoY (±15.7%) | **9/24/26** (CB26-155) | P [Census PDF](https://www.census.gov/construction/nrs/pdf/newressales.pdf) |
| Median / average price | **$393,700 (−5.8% YoY**, ±8.2%, not significant); average $478,700 (−8.8% YoY, ±7.7%, **significant**) | | same |
| For-sale inventory / months' supply | 483k (−2.0% YoY) / **8.5 months** (9.0 in July) | | same. Next release 10/27/26 |

## 6. ATTOM August 2026 foreclosure report (rel. **9/17/26**, P [ATTOM](https://www.attomdata.com/news/market-trends/foreclosures/august-2026-foreclosure-market-report/))
| Metric | Value | MoM | YoY |
|---|---|---|---|
| Properties with a filing | 40,277 | +1% | **+13%** |
| Starts | 25,894 | −3% | +7% |
| REOs (completed foreclosures) | 5,794 | +22% | **+42%** |
| National rate | 1 per 3,569 units | | |
| Top states by rate | SC 1/1,547 · NV 1/1,920 · **FL 1/2,397 (#3)** · TX 1/2,445 · MD 1/2,530 | | |
| **Florida** | **#1 in starts (3,189)**, ahead of TX 3,126 and CA 2,565; FL REO count not itemized | | |
| Metros by rate (>200k population) | Columbia SC 1/1,232 · **Punta Gorda FL 1/1,249 (#2)** · Spartanburg SC · Fayetteville NC · Charleston SC | | |
| REO leaders | TX 1,835 (Houston 448, Dallas 402, San Antonio 256) | | |

## 7. Consumer-credit / BNPL / fintech news, 9/17–9/24
| Date | Item | Source |
|---|---|---|
| 9/16 (reported 9/22) | House Financial Services Committee passed **H.R. 10184** 28–21 on party lines: CFPB moved to appropriations, a small-dollar-credit safe harbor (≤$3,500), a $30B supervision threshold. Author rates enactment this year "very unlikely." | S [Ballard Spahr CFM](https://www.consumerfinancemonitor.com/2026/09/22/house-financial-services-committee-approves-legislation-to-place-cfpb-under-congressional-appropriations-process/) |
| 9/17 or 9/18 (sources conflict) | Senate Banking Committee advanced **Brian Johnson** as CFPB Director, 13–11. Mark Paoletta has been Acting Director since 8/1. | S Ballard / Paul Hastings |
| 9/16 | Same committee passed H.R. 7866, the American Lending Fairness Act | S search snippet only |
| — | CFPB newsroom: **no September 2026 items** (latest Aug-2026) | P [CFPB newsroom](https://www.consumerfinance.gov/about-us/newsroom/) |
| — | BNPL credit disclosure / subprime-lender failure / sponsor-bank order in the window: **none found** | 3 searches |
| ⚠️ context | A secondary source (CUCollector, 9/21) says the **Fed raised rates on 9/16 to 3.75–4.00%**. Cox's mid-Sept note also mentions "Federal Reserve rate increases." **Not verified here and outside this task. Confirm with the macro owner before anyone cites it.** | S |

## 8. Student loans
| Item | Value | Date | Source |
|---|---|---|---|
| **FSA Q3 FY2026 portfolio (as of 6/30/26) — POSTED** | Announcement GENERAL-26-57 | **9/22/26** | P [FSA Partner Connect](https://fsapartners.ed.gov/knowledge-center/library/electronic-announcements/2026-09-22/federal-student-aid-posts-updated-reports-fsa-data-center) |
| Defaulted | **>9.3M recipients (+~400k QoQ), $234B**, ≈14% of the $1.64T ED-managed book. +~1.6M borrowers / +$54B since Dec-25 (S) | 6/30/26 | P (the H1 delta is S: College Investor/search) |
| Delinquent 30+ | **~3.5M (~20% of recipients in repayment)**; ~1.5M in late-stage DQ, at risk of default within 6 months (S). **31+ DQ rate = 15.7% of $ in active repayment** | 6/30/26 | P |
| Repayment / forbearance | 17.4M (43%) with $658B; forbearance 8.0M with $459B | | P |
| IDR | ~13M borrowers, $792B (vs $740B YoY) | | P |
| Total portfolio | 42.3M recipients, >$1.7T | | P |
| SAVE → RAP | RAP (Repayment Assistance Plan) went live 7/1/26. Servicers sent 90-day notices from 7/1; **first switch deadlines 9/29/26**; non-responders go to Standard (higher payments). ~7.5M in SAVE. | 9/22 | S Forbes (403, snippet only), NerdWallet |
| Involuntary collections | Paused since the **1/16/26** ED announcement (Treasury offset, wage garnishment, benefit offset). **No restart date found**; secondary sources say the pause held as of Aug-26. Treasury took over collection of defaulted loans (announced 3/20/26). **No new announcement found for 9/17–9/24.** | | S CNBC/NASFAA; the ed.gov primary was not re-fetched |

## Source weaknesses (summary)
- **ICE Aug First Look and Fitch Aug index were not obtained.** Fitch July (6.13%) is secondary only, and a conflicting June figure (5.80 vs 5.67) is unresolved.
- KBRA gives only changes; its levels are paywalled.
- VantageScore has no score-tier split in the public release, so there is no K-shape read.
- ICE July: foreclosure starts 38,600 vs 40,000 and "vs 2019" −41 vs −46 bp disagree across ICE's own surfaces.
- The Fed-hike claim (9/16, 3.75–4.00%) is unverified secondary context. Route it to the macro owner and don't cite it.

---
## C. Macro / consumer sweep (agent)
# Macro/Consumer Sweep, gathered Thu 2026-09-24 (ET)

Key: P = primary source read directly; S = secondary source (primary not reached, or primary page did not render). Every figure below was checked as a 2026 figure at the page it came from, unless marked otherwise.

## 1. BEA: GDP, PIO, and UMich schedule

| Item | Value | Ref period | Released | Source | P/S |
|---|---|---|---|---|---|
| **Q2 GDP third estimate** | **NOT RELEASED.** Scheduled for **Wed 2026-09-30, 8:30 ET** (combined with Industries, Corporate Profits, State GDP and State Personal Income) | Q2 2026 | — | [BEA schedule](https://www.bea.gov/news/schedule) | P |
| **Aug Personal Income & Outlays** | **NOT on Fri 9/25.** Scheduled for **Wed 2026-09-30, 8:30 ET**, the same morning as the GDP third estimate | Aug 2026 | — | [BEA schedule](https://www.bea.gov/news/schedule) | P |
| Q2 real GDP (2nd est., the current vintage) | +1.5% SAAR, unrevised from the advance estimate | Q2 2026 | 2026-08-26 | [BEA](https://www.bea.gov/news/2026/gdp-second-estimate-and-corporate-profits-2nd-quarter-2026) | P |
| Q2 consumer spending (2nd est.) | Revised up; BEA's summary gives no standalone real PCE %. An import revision offset it | Q2 2026 | 2026-08-26 | same | P (the % was not captured) |
| Q2 PCE price index / core | **+5.3% / +3.6% SAAR**, each revised up 0.2 pp | Q2 2026 | 2026-08-26 | same | P |
| Q2 corporate profits | +$400.9B (Q1: +$74.4B) | Q2 2026 | 2026-08-26 | same | P |
| Personal saving rate | Not in the GDP 2nd-estimate text. It is due in the 9/30 PIO (and annual-update revisions, if any, come with the 3rd estimate) | — | — | — | NOT OBTAINED |
| **UMich Sept final** | Scheduled **Fri 2026-09-25, 10:00 ET** | Sep 2026 | — | [UMich SCA](https://www.sca.isr.umich.edu/) | P |
| UMich Sept preliminary | Sentiment **47.8** (Aug 51.7, −3.9 pts); current conditions 50.9; expectations 45.8; **1-yr inflation 4.6%** (highest since June); **5-10yr 3.4%** | Sep 2026 prelim | 2026-09-11 | [UMich SCA](https://www.sca.isr.umich.edu/) | P |

## 2. Conference Board

| Item | Value | Ref | Released | Source | P/S |
|---|---|---|---|---|---|
| Consumer Confidence, Sept | **NOT RELEASED.** Due **Tue 2026-09-29, 10:00 ET** | Sep 2026 | — | [investing.com calendar](https://www.investing.com/economic-calendar/cb-consumer-confidence-48) / search | S (date only) |
| Consumer Confidence, Aug (prior) | 89.4 (−0.8); Present Situation 121.2 (+6.8); **Expectations 68.2** (−5.8; below the 80 recession signal since Feb 2025) | Aug 2026 | 2026-08-25/26 | [Advisor Perspectives](https://www.advisorperspectives.com/dshort/updates/2026/08/26/consumer-confidence-conference-board-ajugust-2026) | S |
| LEI, Aug | **−0.1% to 99.5** (2016=100), after +0.2% in Jul; first decline since March; 6-month growth −0.1% (Feb→Aug). CEI +0.1% to 114.9; LAG +0.2% to 120.6. CB forecasts 2026 GDP at 1.9% and cut 2027 to 1.8% from 1.9% | Aug 2026 | ~2026-09-18 | [PR Newswire / CB](https://www.prnewswire.com/news-releases/the-conference-board-leading-economic-index-lei-for-the-us-edged-down-in-august-302883352.html) | P (CB wire release, via search summary; body not fetched) |

## 3. Regional Fed and national activity reads (9/17–9/24)

| Survey | Headline | Prices | Released | Source | P/S |
|---|---|---|---|---|---|
| Philly Fed Mfg, Sep | **37.8** (Aug 47.4; consensus 30.5); new orders 29.2; employment 11.8 (−16); future activity 52.9 | **Prices paid 48.6 (rose)**; prices received 31.3 | 2026-09-17 | [FXStreet](https://www.fxstreet.com/news/united-states-philadelphia-fed-manufacturing-survey-came-in-at-378-above-forecasts-305-in-september-202609171230), [Academic Capital](https://www.academic-capital.com/2026/09/philadelphia-fed-manufacturing-survey.html) | S (the philadelphiafed.org page did not render the data) |
| Richmond Fed Mfg, Sep | **−2** (Aug +4); shipments −5; new orders −6; employment +7. Services revenues 0 (from −8) | Mfg prices-paid growth "increased notably", prices received up only slightly (margin squeeze); services prices paid eased | 2026-09-22 | [FXStreet](https://www.fxstreet.com/news/united-states-richmond-fed-manufacturing-index-below-expectations-5-in-september-actual-2-202609221400), [FX.co services](https://www.fx.co/en/forex-news/3179615) | S |
| KC Fed Mfg, Sep | **Composite 20** (Aug 17) | NOT OBTAINED | 2026-09-24 (primary schedule confirms Thu 9/24) | [FX.co](https://www.fx.co/en/forex-news/3185937); [KC Fed release dates](https://www.kansascityfed.org/surveys/manufacturing-survey/manufacturing-survey-release-dates/) | S. ⚠️ The KC Fed page titled "Edged Higher in September" is the **2025** release (composite 4). Do not cite it |
| CFNAI, Aug | **−0.04** (Jul rev. +0.08); MA3 +0.01 (from −0.01); personal consumption & housing +0.01 (from −0.06) | n/a | 2026-09-21 | [FRED CFNAI](https://fred.stlouisfed.org/series/CFNAI) (P for the value); [TradingView/TE](https://www.tradingview.com/news/te_news:585328:0-chicago-fed-activity-index-down-in-august/) for components (S) | P/S |

## 4. Consumer spending trackers

| Tracker | Value | Ref | Released | Source | P/S |
|---|---|---|---|---|---|
| **BofA Consumer Checkpoint ("Still sizzling")** | Card spending per household **+0.9% MoM SA** (Jul −0.2%); **+4.5% YoY**; **ex-gasoline +3.7% YoY** | Aug 2026 | **2026-09-14** | [BofA Institute PDF](https://institute.bankofamerica.com/content/dam/economic-insights/consumer-checkpoint-september-2026.pdf) | P |
| BofA, discretionary spending by income (3mma YoY SA) | **Higher +5.9% / Lower +5.7% / Middle +5.1%**. BofA: the higher-to-lower gap is "the smallest since January 2024" and the "K" in card spending is "effectively" closed | Aug 2026 | 2026-09-14 | same | P |
| BofA, wages and credit by income | Lower-income after-tax wage growth outpaced the other cohorts for the 2nd straight month (chart only, no %); revolver CC utilization near pre-pandemic and down YoY; lower- and middle-income deposits above 2019 | Aug 2026 | 2026-09-14 | same | P |
| BofA caveats (their own) | The K "likely persists" in big-ticket items (vehicles, moving); part of the wage gain may be **temporary (lower tax withholdings)**; durables and airline *transactions* are down YoY (price-driven spending); general merchandise spending +5.6% YoY (value-seeking) | Aug 2026 | 2026-09-14 | same | P |
| Chicago Fed CARTS, Sep | **NOT OUT.** Latest is the Aug preliminary, **+0.5% MoM** ex-auto (Jul +0.1%), updated 2026-09-09. Next release 2026-10-08 | Aug 2026 | 2026-09-09 | [FRED CARTSPRELIM](https://fred.stlouisfed.org/series/CARTSPRELIM) | P |
| ⚠️ CARTS "+0.5% Sep / +0.2% real" | This search hit is the **2025** figure (X post dated Oct 2025). Do not cite it | — | — | — | rejected |
| Visa SMI / Mastercard SpendingPulse | NOT OBTAINED. Searches returned only 2021–22 and product pages; no Aug/Sep 2026 print found | — | — | — | — |

## 5. Carnival (CCL)

| Item | Value | Source | P/S |
|---|---|---|---|
| Q3 FY26 results date | **Confirmed: Tue 2026-09-29.** Release before the open; call at 10:00 ET (announced 2026-09-15) | [Cruise Industry News](https://cruiseindustrynews.com/cruise-news/2026/09/carnival-to-hold-conference-call-on-third-quarter-earnings/) | S (relays the company notice) |
| Pre-announcement | **None found.** Sell-side trims instead: Jefferies cut 2026/27 EPS by 3% (fuel; Brent +~33% since the 6/23 Q2 print; CCL is unhedged); TD Cowen cut its price target from $34 to $32 on 2026-09-22. Consensus EPS ~$1.35, revenue ~$8.4B | [Proactive](https://www.proactiveinvestors.com/companies/news/1099005/carnival-faces-fuel-pricing-headwinds-ahead-of-third-quarter-results-1099005.html), [ScanX](https://scanx.trade/stock-market-news/companies/carnival-q3fy26-results-eps-expected-1-35-revenue-8-4-billion/51531006) | S |

## 6. Tariffs and trade (9/17–9/24)

| Date | Item | Source | P/S |
|---|---|---|---|
| 2026-09-18 | USTR's Section 301 "structural excess capacity" report and remedies were **delayed until after the 9/24 Trump–Xi summit**. The earlier plan was to recommend a **7.5% tariff on Chinese goods**. The probe covers 16 economies | [Korea Times / Bloomberg](https://www.koreatimes.co.kr/foreignaffairs/20260918/us-expected-to-delay-new-excess-capacity-tariff-announcement-until-after-trump-xi-summit-report); [InsideTrade](https://insidetrade.com/daily-news/sources-section-301-overcapacity-report-punted-after-trump-xi-summit) | S |
| 2026-09-23 | Bessent: the US–China tariff truce is **extended to 2027-01-10** (was set to expire ~2026-11-10) | [CNBC](https://www.cnbc.com/2026/09/24/us-china-trade-truce-bessent-trump-xi.html) (403 when fetched); [CBS live](https://www.cbsnews.com/live-updates/trump-china-xi-jinping-state-visit-dinner-tariffs-ai/), [Al Jazeera](https://www.aljazeera.com/news/2026/9/24/trump-xi-summit-whats-on-the-agenda-why-it-matters) | S |
| 2026-09-24 | **Summit outcome: nothing on tariffs announced as of CBS live update 12:59 PM ET.** A bilateral meeting is under way and the state dinner is tonight. A "Board of Trade" announcement is expected (USTR Greer). **Re-check tomorrow morning** | [CBS live](https://www.cbsnews.com/live-updates/trump-china-xi-jinping-state-visit-dinner-tariffs-ai/) | S |
| Context, not new this week | China-specific stack per Al Jazeera: 10% fentanyl duty, plus the Section 301 forced-labor tariff (12.5% for non-adopters, effective 2026-07-24). One outlet's "30% on Chinese goods" figure is UNVERIFIED | [USTR fact sheet](https://ustr.gov/about/policy-offices/press-office/fact-sheets/2026/july/fact-sheet-ustr-section-301-action-response-failure-60-economies-ban-imports-produced-forced-labor), [Al Jazeera](https://www.aljazeera.com/news/2026/9/24/trump-xi-summit-whats-on-the-agenda-why-it-matters) | P (USTR) / S |
| Section 122 | **No new court development found for 9/17–9/24.** Status: CIT struck the tariff down on 2026-05-07; the Federal Circuit stayed that ruling pending appeal on 2026-06-11; the tariff expired on 2026-07-24 at its 150-day limit; the appeal (and so refunds) is still pending | [Skadden](https://www.skadden.com/insights/publications/2026/05/us-trade-court-strikes-down-section-122-tariffs), [Fed Cir stay order](https://reason.com/wp-content/uploads/2026/06/Federal-Circuit-Section-122-Stay-Order-1.pdf) | S |

## 7. Florida (9/17–9/24)

| Item | Value | Date | Source | P/S |
|---|---|---|---|---|
| Minimum wage | **$14 → $15/hr on 2026-09-30**, the final Amendment 2 step. Tipped minimum rises to $11.98. From 2027, annual increases are indexed to CPI-W (12 months through Aug 31) | effective 9/30 | [Lowndes](https://www.lowndes-law.com/newsroom/insights/floridas-minimum-wage-reaches-15-00-on-september-30-2026), [Fisher Phillips](https://www.fisherphillips.com/en/insights/insights/floridas-minimum-wage-is-rising-sept-30) | S (law-firm alerts; constitutional schedule) |
| FL unemployment, Aug | **4.5%** (Jul 4.6%; Aug-2025 4.0%, **+0.5 pp YoY**); US 4.1%. One of 9 states with a significant MoM decline. News reports: 502k unemployed of an 11.1M labor force; +21.8k jobs | Aug 2026, released 2026-09-18 | [BLS LAUS](https://www.bls.gov/news.release/laus.nr0.htm) (P); [WUSF](https://www.wusf.org/economy-business/2026-09-19/florida-jobless-rate-falls-for-third-straight-month) (S, for the counts) | P/S |
| Citizens Property Insurance | **~255,000 policies as of 2026-09-18** (266,231 at 8/31; 1.4M at the Sep-2023 peak); **projected ~248k at year-end** with ~$77B exposure; 1.8% market share. OIR approved 4 more homeowners rate cuts (avg −7%, 62k policies) on 9/23 | 2026-09-18/23/24 | [Tallahassee Reports](https://tallahasseereports.com/2026/09/24/citizens-property-insurance-president-market-is-working/), [Insurance Journal](https://www.insurancejournal.com/news/southeast/2026/09/23/886558.htm) | S (citizensfla.com not reached) |
| FL foreclosures, Aug (ATTOM) | **FL led the nation in starts: 3,189**; filing rate 1 per 2,397 units (**3rd highest** state); **Punta Gorda 1 per 1,249 (#2 metro)**. US: 40,277 filings (+1% MoM, **+13% YoY**); starts 25,894 (+7% YoY); **REO 5,794 (+42% YoY)**. FL YoY change: NOT OBTAINED (my extractor garbled it; do not use "+7%" as a FL number) | Aug 2026, released 2026-09-17 | [ATTOM via PR Newswire](https://www.prnewswire.com/news-releases/foreclosure-activity-remains-above-year-ago-levels-in-august-2026-302881135.html) | P (ATTOM wire) |

## Source weaknesses (read before citing)
1. **The 9/30 double release**: GDP 3rd estimate plus Aug PIO on the same morning. Any docket row expecting PIO on 9/25 is wrong.
2. Philly, Richmond and KC Fed figures are from secondary sources. The Fed pages did not render their data tables. KC Fed has no prices data, and the only primary-titled page found was the 2025 release.
3. Two stale-year traps were caught: the KC Fed "Edged Higher in September" page (2025) and the CARTS "+0.5% Sep" figure (Oct-2025 X post).
4. The BofA income-cohort figures are primary but come from BofA's internal data (their own selection-bias disclaimer). BofA says the K is "effectively closed" in card spending. That runs counter to the CARL K-shape thesis. BofA's own caveats (big-ticket K persists; temporary withholding boost) should travel with the figure.
5. The trade summit is **still in progress**. The outcome needs a re-check on 9/25.
