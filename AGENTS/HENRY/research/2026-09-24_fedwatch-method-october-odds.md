# October FOMC hike odds — FedWatch method, HENRY computation (Will-directed, 2026-09-24 ~23:4x ET)

**Why:** every desk (HENRY, BOND, LIQUID, VIOLET) quoted October-hike odds from press/TE secondaries (64–77.5%); none read the priced figure. Shared blind spot named in the 9/24 peer read.

**Access:** CME settlements endpoint and FedWatch page — **HTTP 403, CME blocks automated access (Data Terms of Use).** Not circumvented. ⇒ computed the FedWatch inputs directly.

**Method (CME FedWatch's own):** 2026 FOMC = 10/27–28 then 12/8–9 [federalreserve.gov, fetched 9/24] ⇒ **no November meeting** ⇒ Nov 30-day fed funds future (ZQX26) prices the full post-October month. P(+25) = (100 − ZQX26 − EFFR) / 0.25. EFFR **3.88 [FRED 9/23]** (target 3.75–4.00, IORB 3.90).

**Prices:** yfinance 30-min bars, last trade at/before **15:00 ET** each regular session (≈ ZQ settlement window; **NOT the CME settlement**). ⚠️ The yfinance daily row labelled "9/24" pulled after 18:00 ET is the **9/25 evening session** (vol ~2.5K vs 183K in the 9/24 regular session) — not used.

| Session | ZQX26 | Implied Nov EFFR | P(Oct +25) |
|---|---:|---:|---:|
| 9/21 | 95.975 | 4.025 | 58% |
| 9/22 | 95.980 | 4.020 | 56% |
| 9/23 | 95.950 | 4.050 | 68% |
| **9/24** | **95.940** | **4.060** | **72%** |

**Year-end:** ZQZ26 95.800 ⇒ Dec avg 4.200; with days 1–9 at the post-Oct 4.060 ⇒ post-Dec EFFR ≈ 4.257 ⇒ **+37.7bp ≈ 1.5 hikes priced by year-end.** ZQF27 95.725 ⇒ 4.275 (consistent).
**Oct contract (ZQV26) NOT used:** only 3 post-meeting days ⇒ one 0.005 tick ≈ 21pp; 96.100 ⇒ "83%" is noise.

**Caveats (travel with the figure):** ① vendor last-trade, not settlement ② precision ±2pp (0.005 quote) ③ binary 25bp/hold assumption (no 50bp or cut tail) ④ assumes EFFR stays 3.88 in-range; a quarter-end/month-end EFFR drift moves the implied P ⑤ not CME's published number — CME's may differ by a few pp on its own EFFR/settlement inputs.
**Cross-check (secondary, 9/24):** 69.7% (KuCoin flash), 73.5%, 77.5% (CNBC, "up from ~53% Wednesday") — consistent with 72% ±; the 53% "Wednesday" vs my 68% [9/23 15:00] is likely an intraday-timing difference (flash PMI 9/23 09:45 ET), unverified.

**So what:** the post-FOMC hike path is still being priced UP (56→72% in two sessions, alongside 10Y real +22bp) — supports BOND's ACM reading (path, not term premium) as at least part of the move. Not a HENRY threshold; no row registered.
