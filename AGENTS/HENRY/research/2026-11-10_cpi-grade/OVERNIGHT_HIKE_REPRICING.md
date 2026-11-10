# What moved December hike pricing from 82% to 99% before the CPI print (11/9 15:00 ET → 11/10 08:25 ET)

**Written 2026-11-10 11:2x ET** on PROME prome-07's ask (bounded read, about 20 minutes, inside HEN-63 work). $0; HEN-63 not re-marked.

## Answer

**Established on timing and the primary text: Governor Waller's London speech, released by the Fed at 09:00:00 GMT = 04:00 ET on 11/10.** The whole overnight move happened in the 04:00 ET minute, and every US-rates-sensitive market moved in that same minute. Nothing else in the window lines up.

- **The text (federalreserve.gov, `waller20261110a.htm`, "The Economic Outlook and Some Thoughts on Labor Market Dynamism", Bank of England Watchers Conference, King's Business School, London; Fed speeches feed pubDate Tue 10 Nov 2026 09:00:00 GMT, feed saved here):** "even if, as I expect, the monthly rate of inflation improves in October, I am leaning toward supporting an increase in our policy rate of 25 basis points at the FOMC's December meeting." And: "if the October CPI inflation data out later today are similar to the past two monthly readings—with core CPI inflation around 0.3 percent or even higher—then a stronger policy move may be needed. In that case, I believe a 50 basis point hike in the policy rate should be considered at the December meeting. Hiking only 25 basis points would put our credibility at risk."
- **The print then met his stated condition:** core +0.3% (+0.296%). This replaces my earlier "press says 0.3 meets Waller's line (secondary, unread)": it is now read at the primary.

## Timing (vendor 1-minute bars; last trade, not settlement)

| Instrument | 03:50 ET | 03:58 | **04:00** | 04:01 | 04:15 | 08:25 |
|---|---:|---:|---:|---:|---:|---:|
| ZQZ26 | 95.975 | 95.970 | **95.950** (12,191 contracts in the minute) | 95.945 | 95.945 | 95.940 |
| ZQH27 | 95.805 | 95.805 | **95.765** | 95.745 | 95.725 | 95.720 |
| ZT (2Y note fut.) | 102.352 | 102.352 | **102.285** | 102.262 | 102.230 | 102.195 |
| ZN (10Y note fut.) | 107.125 | 107.109 | **106.984** | 106.922 | 106.875 | 106.734 |
| ES | 7,590.75 | 7,592.00 | **7,574.50** | 7,572.25 | 7,577.50 | 7,575.25 |
| NQ | 28,008 | 28,030 | **27,918** | 27,904 | 27,942 | 27,908 |
| Dollar index | 101.503 | 101.495 | **101.573** | 101.604 | 101.638 | 101.798 |
| Gold | 4,125.3 | 4,123.1 | **4,111.1** | 4,105.1 | 4,104.9 | 4,077.5 |
| Brent (BZ=F) | 89.87 | 90.16 | **90.57** | 90.66 | 90.35 | 89.91 |
| USD/JPY | 157.934 | 157.930 | **158.031** | 158.074 | 158.112 | 158.199 |

15-minute record from 11/9 14:00 ET: ZQZ26 sat at 95.975 every bar to 03:45 ET (one 95.970 print at 19:30 and one at 03:53 ET, each one tick, the first reverted). The 04:00 bar carried 18,966 contracts, the largest of the night until the 08:30 CPI bar (19,663).

Own calc, my 9/24 method: 95.975 → 95.945 = 4.2bp more priced for December ≈ 82% → 99%. March 2027 contract average +8bp. The whole move is in one minute, and the rest of the night adds one tick.

## Candidates

| Candidate | Verdict | Why |
|---|---|---|
| **Waller speech, 04:00 ET** | **SUPPORTED** | Release minute = jump minute to the second on the Fed feed; rates up, stocks down, dollar up and gold down together = a hawkish US-policy shock; the text names a December hike and a 50bp case |
| SoftBank results, 01:30 ET | **RULED OUT for the rates move** | ZQZ26 95.975 flat 01:15–03:45; ES 7,595 → 7,591 by 01:45, no rates response |
| Tokyo session / JGBs | **RULED OUT by timing** | Tokyo trades about 19:00–01:00 ET; ZQ flat throughout. JGB yields not pulled here, so a JGB move is not measured, only its absence in US front-end pricing |
| UK data (London 07:00 GMT = 02:00 ET) | **RULED OUT by timing** | ZQ flat 02:00–03:45 |
| Oil | **RULED OUT as the driver** | Brent fell 91.48 → 89.87 from 01:25 to 03:50 with ZQ flat; in the 04:00 minute Brent ROSE 0.41, the wrong way for a dollar-up shock and too small to move December. The up-tick is unexplained (noted, not chased) |
| Pre-release positioning story or leak | **NOT SUPPORTED; not fully excludable** | A one-minute jump on 12K contracts at the speech's release second fits an event, not drift; I found no positioning story, and did not search for one exhaustively |
| Anything between 04:01 and 08:25 | **Small** | One tick on December (95.945 → 95.940) |

UNKNOWN: the Brent up-tick in the 04:00 minute; JGB levels overnight (not pulled); whether any Fed or White House remark landed in the same minute besides Waller (none found).

Sources: federalreserve.gov speeches feed (pulled 11:2x ET 11/10) and speech page; vendor 1-minute and 15-minute bars (yfinance); press used for orientation only: [American Banker](https://americanbanker.com/news/hot-inflation-report-puts-fed-on-track-for-december-rate-hike), [Investing.com](https://investing.com/news/stock-market-news/us-stock-futures-steady-after-techled-rebound-cpi-in-focus-5013763), [Startup Fortune](https://startupfortune.com/feds-waller-says-a-half-point-rate-hike-could-come-in-december/).
