# Europe UST Holdings / TIC Custody Refresh — April 2026

> **HISTORICAL — April-2026 TIC data, not maintained.** Superseded by later TIC releases; `VX-HANS-1.0x` carries the tracked rows. Live state → `STATUS.md`.
> *(HISTORICAL banner added 2026-09-18 at closeout. Found via `consumer_check --self`, which flagged statement-time values here as stale: they are correctly-dated HISTORY, and the defect was that nothing on the file SAID so. Data Hygiene requires a surface be FROZEN-with-a-banner or LIVE-with-an-alert, never the silent-rot middle — these were neither.)*
**Agent:** HANS  
**Created:** 2026-06-22 09:25 ET  
**Scope:** Phase 4 / Batch B2 only — Europe UST custody holdings and TIC flow interpretation. No PMI actuals, energy/storage, bank/private-credit, sovereign/LDI deep dive, workbook edit, outbox, or trade recommendation.

---

## Bottom Line

Europe is **neutral/noisy, not a confirmed demand-hole contributor** in the April 2026 TIC data. Aggregate TIC flows were supportive for long-duration U.S. securities, but Europe-specific custody-country data are mixed: **UK bought**, **Lux/France/Switzerland were small buyers/near-flat**, while **Belgium/Ireland/Germany sold on net**. The target Europe custody cluster is basically flat for April (**~-$0.7B net U.S. sales to the seven-country watchlist**) and therefore does **not** clear a LIQUID/ZHAO/SAM outbox threshold.

The important caveat: TIC country data are **custodial attribution**, not true beneficial ownership. Ireland/Luxembourg/Belgium can reflect fund domiciles, custodians, clearing systems, and third-country official/private portfolios rather than domestic European investor conviction. Belgium/Euroclear is the most important watch item because a Belgium drawdown can be custody migration/official proxy behavior, not “Belgium selling.”

---

## 1) Correct April 2026 Major Foreign Holders / Country Data

**Primary source retrieved:** Treasury TIC **Table 5: Major Foreign Holders of Treasury Securities**, current as of **2026-04**, plus TIC **Table 3** all-country detail for Germany and bill/coupon splits.  
**Units:** billions of dollars. Table 3 source is in millions; values below converted to billions.

| Country / node | Apr 2026 holdings | Mar 2026 holdings | MoM holdings change | Apr 2026 net U.S. sales to foreigners | LT Treasuries holdings | LT net sales | ST/bills holdings | ST net sales | Apr 2025 holdings | YoY holdings change | Read |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **United Kingdom** | **937.5** | 926.9 | **+10.6** | **+17.1** | 844.1 | **+26.0** | 93.4 | **-8.9** | 807.7 | **+129.8** | Supportive, coupon-led; UK remains the largest Europe custody node. |
| **Belgium / Euroclear proxy** | **459.9** | 454.0 | **+5.9** | **-8.7** | 382.6 | **-12.0** | 77.3 | **+3.3** | 411.1 | **+48.8** | No holdings collapse, but Apr flow is LT-selling/bill-buying; watch Euroclear/official-proxy signal. |
| **Luxembourg** | **431.1** | 432.0 | **-0.9** | **+0.3** | 336.8 | **+8.9** | 94.3 | **-8.6** | 410.9 | **+20.2** | Neutral/slightly supportive; rotation from bills to coupons. |
| **France** | **393.3** | 393.0 | **+0.3** | **+1.8** | 372.0 | **+1.4** | 21.3 | **+0.5** | 360.6 | **+32.7** | Stable/supportive. |
| **Ireland** | **345.3** | 355.2 | **-9.9** | **-9.3** | 237.5 | **-4.2** | 107.8 | **-5.1** | 339.9 | **+5.4** | April seller; fund-domicile/custody caveat matters. |
| **Switzerland** | **288.6** | 286.4 | **+2.3** | **+2.5** | 231.2 | **+1.0** | 57.4 | **+1.5** | 310.9 | **-22.2** | Small Apr buyer, but YoY lower. |
| **Germany** | **107.7** | 112.5 | **-4.9** | **-4.4** | 78.1 | **-4.7** | 29.6 | **+0.3** | 110.6 | **-2.9** | Small seller; not systemically important vs custody hubs. |

**Seven-country watchlist total (UK, Ireland, Luxembourg, Belgium, France, Switzerland, Germany):**
- Apr 2026 holdings: **$2.963T**.
- Apr 2026 net U.S. sales: **~-$0.7B** (essentially flat/noisy).
- Long-term/coupon net sales: **~+$17.4B**.
- Short-term/bill net sales: **~-$17.0B**.

**Euro Area availability:** Treasury Table 5 does **not** publish a separate “Euro Area” aggregate. Table 3 has country detail, but some euro-area micro countries are absent or partially suppressed. A rough named euro-area subtotal for available reporters (Austria, Belgium, Cyprus, Finland, France, Germany, Greece LT-only, Ireland, Italy, Luxembourg, Netherlands, Portugal, Spain) gives approximately **$1.965T holdings** and **-$4.8B Apr net sales**; treat this as an **incomplete constructed subtotal**, not an official Euro Area series.

---

## 2) Aggregate April TIC Flows vs Country/Custody Holdings

**Do not mix these two readings:**

| Dataset | What it says | April 2026 read | HANS use |
|---|---|---|---|
| **Aggregate TIC flows** | Cross-border net acquisitions of U.S./foreign securities, short-term instruments, and banking flows. | Total net TIC inflow **+$26.1B**; foreign purchases of LT U.S. securities **+$206.0B**; private LT purchases **+$164.4B**, official **+$41.6B**; T-bills **-$13.6B**; banks' dollar liabilities **-$79.6B**. | Macro flow pressure: Apr was not an obvious global buyer strike, but bank-liability outflow and bill selling keep the mix noisy. |
| **Country/custody holdings** | End-period Treasury holdings attributed to the country/custodian where securities are held/reported. | UK **$937.5B**, Belgium **$459.9B**, Lux **$431.1B**, France **$393.3B**, Ireland **$345.3B**, Switzerland **$288.6B**, Germany **$107.7B**. | Custody-node signal: identify whether Europe hubs are absorbing, rotating bill/coupon, or transmitting third-country selling. |

**Why custody attribution matters:** Treasury explicitly says country-holder data are collected primarily from U.S.-based custodians/broker-dealers and may not identify the true owner when securities are held in a third-country custody account or managed by foreign portfolio managers for clients elsewhere. That is exactly why **Ireland/Lux/Belgium** can move for reasons unrelated to domestic Irish/Lux/Belgian demand:

- **Ireland / Luxembourg:** fund domiciles, UCITS/ETF platforms, asset managers, and treasury centers can show changes in custody positions that belong economically to global investors.
- **Belgium:** Euroclear/custody infrastructure can proxy for official or third-country accounts; Belgium selling can be a China/official/custody-routing signal, or just settlement/custody noise.
- **UK:** global dealer/asset-management custody node; large moves often matter, but are not a clean read on domestic UK household/institution demand.

---

## 3) Demand Classification

**HANS classification for April 2026:** **Neutral/noisy with coupon support; not demand-hole confirmation.**

Evidence:
1. **Aggregate Apr TIC was supportive for long-term U.S. securities**: foreign residents bought **+$206.0B** LT U.S. securities; private + official buyers both positive.
2. **Europe custody cluster was flat overall**: seven-country watchlist net U.S. sales were only **~-$0.7B**.
3. **Composition matters:** the cluster showed **coupon/long-term buying (~+$17.4B)** offset by **bill selling (~-$17.0B)**. That is not the same as broad UST abandonment.
4. **Local stress signal absent:** no single Europe custody node shows a threshold-grade drawdown. Belgium/Ireland/Germany sold, but UK/Lux/France/Switzerland absorbed enough to neutralize the watchlist.
5. **Banking-flow drag is separate:** aggregate banks' own net dollar liabilities fell **-$79.6B**, which matters for LIQUID/funding, but should not be misread as country UST selling.

---

## 4) What Matters for LIQUID / ZHAO / SAM

| Watch item | Why it matters | Current Apr 2026 read |
|---|---|---|
| **Belgium / Euroclear shifts** | Possible custody proxy for official/China-linked flows or Euroclear settlement/custody rerouting. | Belgium Apr net sales **-$8.7B**, LT **-$12.0B**, bills **+$3.3B**; holdings still **+$5.9B MoM** and **+$48.8B YoY**. Monitor, not alarm. |
| **UK/Ireland/Lux selling cluster** | UK is largest Europe custody node; Ireland/Lux are fund domiciles. Simultaneous selling would imply wider private/custody demand weakness. | Not simultaneous: UK **+$17.1B**, Lux **+$0.3B**, Ireland **-$9.3B**. No cluster breach. |
| **Official vs private flow changes** | Official selling/support affects term premium and reserve behavior; private buying may be hedge/carry/basis driven. | Aggregate Apr official inflow **+$49.2B** and official LT purchases **+$41.6B**; Table 5 official holdings only **+$4.3B MoM**, with bills up and bonds/notes down. Mixed but not official buyer strike. |
| **Bill vs coupon divergence** | Bill selling with coupon buying can mean duration demand remains intact while cash/collateral preference changes; coupon selling + bill buying can signal duration aversion. | Seven-country watchlist: **LT +$17.4B**, **ST -$17.0B** = coupon support despite bill runoff. Belgium alone is opposite: LT selling/bill buying. |
| **Japan/China offset question** | Europe can offset SAM/ZHAO selling or amplify a demand hole. | Europe did not obviously offset all Asia risk, but also did not join a demand hole. China was roughly flat/slightly selling in Table 5 (**$651.1B Apr vs $652.3B Mar**); Japan rose (**$1.210T vs $1.192T**). |

---

## 5) Thresholds / Monitor Rules for Future Outbox Signals

Write HANS outbox to **LIQUID/ZHAO/SAM/NEXUS** only when a verified threshold fires.

| Trigger | Priority | Send to | Payload |
|---|---|---|---|
| **Belgium holdings drop >$30B MoM** or **>$75B over 3 months**, especially with China/Japan selling | 🟠 / 🔴 if rapid | LIQUID + ZHAO + NEXUS | Belgium/Euroclear custody drawdown; include LT vs bill split and China/Japan context. |
| **UK + Ireland + Luxembourg combined net sales < -$50B in a month** or **< -$100B over 3 months** | 🟠 | LIQUID + NEXUS | Europe private/custody cluster joining demand-hole complex. |
| **Seven-country Europe custody watchlist net sales < -$75B in a month** | 🟠 / 🔴 if official selling also visible | LIQUID + NEXUS + SAM/ZHAO if Asia also selling | Broad Europe custody selling; include aggregate TIC LT flow and bill/coupon split. |
| **Coupon/long-term net sales < -$50B while bills rise** in the watchlist | 🟠 | LIQUID + BOND + NEXUS | Duration aversion rather than simple cash/collateral shift. |
| **Foreign official Treasury holdings drop >$50B MoM** or **official LT net sales < -$50B** | 🟠 / 🔴 if persistent | LIQUID + ZHAO + SAM + BOND | Reserve/official buyer strike risk. |
| **Aggregate TIC: LT U.S. securities purchases turn negative while banks' dollar liabilities fall >$75B** | 🔴 if same month and Europe cluster sells | LIQUID + BOND + NEXUS | Demand weakness plus dollar-liability contraction/funding stress. |

**No outbox written from Batch B2:** no verified current Europe custody threshold fired.

---

## Recommended Workbook Updates — Do Not Edit Yet

Batch B2 instruction was **do not edit workbook unless explicitly necessary**. Recommended Phase 8 updates:

1. Mark old UST/custody rows in `AGENTS/HANS/workbook/VX.tsv` / `FLOW.tsv` as stale if they cite pre-2026 or Apr/Mar war-regime assumptions.
2. Add/refresh a Europe UST custody row with:
   - Current: seven-country watchlist Apr 2026 holdings **$2.963T**, net sales **~-$0.7B**, LT **+$17.4B**, ST **-$17.0B**.
   - Status: **NEUTRAL/NOISY; coupon support; no demand-hole threshold**.
   - Thresholds: Belgium >$30B MoM drawdown; UK+IE+LU < -$50B monthly; watchlist < -$75B monthly; official LT < -$50B.
3. Add source URLs:
   - `https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.txt`
   - `https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table3.txt`
   - `https://home.treasury.gov/news/press-releases/sb0536`

---

## Source Quality / Retrieval Notes

| Source | Result | Quality |
|---|---|---|
| Treasury TIC press release for April 2026 (`sb0536`) | Retrieved successfully; aggregate flows and TIC caveats verified. | **Primary / high**. |
| Treasury TIC Table 5 current (`slt_table5.txt/html`) | Retrieved successfully with **2026-04** country holdings for major foreign holders. | **Primary / high** for top holders. |
| Treasury TIC Table 3 all-country detail (`slt_table3.txt`) | Retrieved successfully; used for Germany and bill/coupon/net-sales split for all target countries. | **Primary / high**, but some small-country cells suppressed as `n.a.`. |
| Legacy `Publish/mfh.txt` | Retrieved but stale Jan 2023 table; **not used**. | Low/currently broken endpoint. |
| Legacy `Publish/mfhhis01.txt` | Retrieved through Dec 2025; not current enough for Apr 2026. | Useful historical backup, not current. |

---

## Unresolved / Caveats

- No official “Euro Area” aggregate found in Table 5; constructed euro-area subtotal is incomplete and should not be treated as a Treasury series.
- Country attribution remains custody-based; Belgium/Ireland/Lux moves require interpretation with China/Japan/official/private context.
- This pass does not verify hedged-return math, cross-currency basis, or European bank funding beyond the TIC/bill/coupon split; Batch B1 owns funding thresholds.
