# HENRY — dealer map on the 11/20 chain, monthly-expiry Friday (2026-11-20, reads 11:34–11:39 ET)

**Session:** PROME launch letter prome-77 (11:33 ET), task (3). Claude Code, Opus 5.5, laptop. Stamps from `date`.

## 1. Source: Cboe blocked today, vendor chain used, NOTHING PUBLISHED

- `gamma_flip.py` reached Cboe's delayed-quote feed and got HTTP 403. One diagnostic request at 11:34:54 ET: `cdn.cboe.com/api/global/delayed_quotes/options/_SPX.json` now answers **307 → `cdn-api.cboe.com`**, and that host returns a **Cloudflare 403 block page** (4,541 bytes of HTML). Under the root Blocked-sites rule this source is unusable by automation: no retry with a different identity, no proxy. **Will is told.** The same block takes away the Cboe `_VIX` `last_trade_time` proof my VIX-settle rule uses; FRED VIXCLS (T+1) is the fallback.
- The script fell back to the vendor (yfinance) chain and, by its own rule, labels the read **NOT THE CANONICAL CHAIN, publish nothing**. `PUBLISHED.tsv` not written. Sign and flip are still the robust part; $B and walls less so on this source.
- **Today's 11/20 expiry is not in this map.** The script drops contracts with zero days left (T = 0), so the AM-settled monthlies (settled at this morning's open) and the PM-settled 11/20 weeklies (live until 16:00) are both excluded. This is the post-expiry book I said yesterday to compare by flip, not by $B.

## 2. The map (vendor chain, open interest through 11/19, IV live)

| Horizon | Spot | Flip | Net gamma at spot ($B per 1%) | Call wall | Put wall |
|---|---|---|---|---|---|
| 14d | 7,080.54 | ~7,440 | **NEGATIVE −30.1** | 7,000 (clean) | 7,000 = call wall: put side UNRESOLVED |
| 35d | 7,080.54 | ~7,422 | **NEGATIVE −56.4** | 7,400 (+15% over #2) | 7,000 (+87% over #2) |
| `--both` verdict | | **flip band 7,422–7,440, both NEGATIVE** | | WITHHOLD (14d 7,000 vs 35d 7,400) | WITHHOLD (put = call at 14d) |

**Profile (35d, own calc, `profile.py`, pull at spot 7,082.55, 5,533 contracts):** −59.7 at 6,900 · −60.5 at 7,000 · −58.7 at 7,100 · −51.0 at 7,200 · −35.2 at 7,300 · −12.9 at 7,400 · −0.6 at 7,450 · +11.8 at 7,500. **Flat from 6,900 to 7,100: no trough under spot.** Yesterday's Cboe profile had a trough at 7,150; today there is no level below spot where dealer selling-into-weakness tapers.

**QQQ (35d, own calc):** spot 624.21, net about −2.3, flip about 655 (crosses between 650 and 660); flat about −2.5 from 605 to 620. Walls not run through `--both`; none quoted.

**Compared with yesterday (flips only, across the expiry):** 11/19 12:17 ET Cboe flip 7,498 / 7,517 with the 11/20 expiry still in the book; my estimate then for after the expiry, about 7,525–7,530. Today's vendor flip 7,422–7,440 is about 90 points lower. Three things moved at once and I cannot separate them: IV is higher (VIX 30 vs 26–28), one more day of open interest, and a different source. The sign did not change.

## 3. What it means

**Dealers are short gamma at about the same rate from 6,900 up to 7,100, so there is no mechanical cushion under the S&P down to at least 6,900; their hedging adds to moves both ways.** The amplification only halves above about 7,300 and ends near 7,420–7,450. The 7,000 strike holds the largest put gamma on the 35-day book; under this estimator's convention (dealers short puts) that is where they are most short gamma, so 7,000 is a place moves accelerate through, not a floor. ⚠️ Free-tier proxy; the convention is an assumption.

**What would turn it:** a reclaim of about 7,420–7,450 (about +5% from 7,054). Nothing nearer flips the sign. Partial relief comes over 7,200–7,300, where the per-point push drops by a third to a half. Below, the next mechanical change is time: the December monthly (12/18) is the large book left.

## 4. Tape at 11:39 ET (vendor, intraday, not closes)

S&P 7,053.91 (−1.72%; 11/19 close 7,175.83 vendor, FRED SP500 11/19 not posted), **16.87 points over the red line 7,037.04 (−9.79% from the 7,818.93 peak)**; session low 7,056.05 on the 11:35 bar at the time of the bar pull. QQQ 624.07 (−3.02%), SMH −6.72%, NVDA −6.54%; RSP −0.23% (narrow: equal-weight barely down); IWM −1.22%; KRE +0.12%; HYG −0.14%; 10Y 4.95% (about −10bp); USD/JPY 158.73 (−0.63%, not near SAM's 2% velocity line). VIX 29.95, VIX9D 30.16, VIX3M 27.93: **inverted** (VIX3M/VIX 0.933, deepest of the week). 11/19 VIX settle 28.44 (FRED VIXCLS 11/19).

**Credit:** FRED HY 352 [11/19] (347 [11/18]), BB 210, CCC 1,361, CCC−BB 1,151. First close over 350; REGINALD's REG-T-04 day 1 of 3 (REGINALD grades). HYG barely moves while the index falls. Under H4 as amended today, a quiet credit tape is no all-clear for an equity break.

**D:L823 (10/22 KRE/QQQ alarm), state only:** from 11/4, KRE −6.4%, QQQ −9.8% (intraday). A hit needs both down 10%; KRE is 3.6 points short and rose today. Still UNRESOLVED until 2027-01-20 to 02-18.

## 5. PROJECTION (moves nothing by itself; separate events, separate clocks)

- **HEN-64 (registered 0.40 on 11/19): a close under 7,100 on any session 11/19–11/25.** 11/19 closed 7,175.83 (vendor), so not yet. Today, 46 points under the line with about 4h20m left and VIX near 30 (one-sigma move in the remaining session about 110 points): **about 65% that today's close is under 7,100.** Not a re-mark of the row; the row keeps 0.40 as registered.
- **S&P close under the red line 7,037.04 today: about 45%.** On any session through Wed 11/25: about 60%. **Not registered** (unscored): HEN-64 already grades the near line, and a second row on the same path would double-count one event.
- **Base case (about 55%, through 11/25):** two-way trade between about 6,900 and 7,200 with closes near the red line, chips leading, equal-weight and banks holding, credit lagging. **Alternative (about 25%):** a reflex over 7,200 by Wednesday on short covering and today's expiry clearing, with VIX back under 25. **Tail (about 20%):** closes under 6,900 with VIX settling over 33 and HY over 375 on the 11/20–11/24 prints, i.e. credit joining. These three are one distribution over the 11/25 close path.
- **What would change my mind:** HY widening by 15bp or more in a print while HYG breaks lower (credit joining); KRE turning down with QQQ (the D:L823 joint leg); or a reclaim of 7,300 (the map's amplification halving).

## 6. Not done

- Map not published (non-canonical chain). Walls withheld in any case.
- Today's 0DTE gamma excluded by construction; it is large near spot into the 16:00 close.
- 11/19 close read: S&P 7,175.83 and VIX 28.44 are the vendor close and FRED VIXCLS; FRED SP500 11/19 not posted at 11:35 ET. Cboe settle proof unavailable (blocked).
