# ECB/Fed Divergence + Funding — June 2026

> **HISTORICAL — June-2026 research, not maintained.** Policy rates and spreads here are June vintage; the ECB has since hiked to 2.50% (eff. 2026-09-16) and the Fed to 3.75-4.00% (2026-09-16). Live state → `STATUS.md`.
> *(HISTORICAL banner added 2026-09-18 at closeout. Found via `consumer_check --self`, which flagged statement-time values here as stale: they are correctly-dated HISTORY, and the defect was that nothing on the file SAID so. Data Hygiene requires a surface be FROZEN-with-a-banner or LIVE-with-an-alert, never the silent-rot middle — these were neither.)*
**Agent:** HANS  
**Created:** 2026-06-22 09:10 ET  
**Scope:** Phase 3 / Batch B1 only — ECB/Fed policy differential, U.S. transmission channels, and funding-stress watch. No TIC country holdings, energy/storage, bank/private-credit deep dive, or sovereign/LDI deep dive except one-line context.

---

## Bottom Line

The Jun11 ECB hike was **not explicitly a pre-committed hiking cycle**, but it was also **not safely dismissible as a one-off**. The ECB framed it as a data-dependent inflation-defense hike against Middle East/energy shock risk, with inflation projections revised higher and growth lower. Reuters snippets/polls around the meeting show investors/economists expected **additional tightening risk** rather than a clean one-and-done.

For U.S. markets, the important read is: **both central banks are hawkish, but the Fed still has the higher policy rate and the larger dollar-yield anchor.** ECB tightening can support EUR at the margin, but Fed dots and current rate differentials keep DXY/USD supported. Funding stress is **monitor-only**: no verified broad dollar-funding stress fired as of this pass. Fed central-bank liquidity swaps are tiny operational-size balances, and EUR/USD 3M basis current level remains unverified rather than breached.

---

## 1) Jun11 ECB Hike — One-Off or Renewed Tightening?

| Evidence | Read |
|---|---|
| ECB raised all three policy rates by **25bp** effective Jun17: deposit **2.25%**, MRO **2.40%**, MLF **2.65%**. | Real tightening, first hike in this revived baseline; not just rhetoric. |
| ECB projections: headline inflation **3.0% 2026**, **2.3% 2027**, **2.0% 2028**; core **2.5% 2026/2027**, **2.2% 2028**; growth **0.8% 2026**, **1.2% 2027**, **1.5% 2028**. | Stagflationary mix: higher inflation path + weaker growth. |
| ECB language: war/energy shock creates inflation pressures; risks are upside inflation / downside growth; decisions are **data-dependent and meeting-by-meeting**; **“not pre-committing to a particular rate path.”** | Official line = no promised cycle. Practically, the inflation shock keeps hike optionality alive. |
| Reuters search snippets: Jun11 hike was “long-telegraphed”; investors saw **two more hikes over the coming year**; Reuters poll before meeting said another hike was likely in September, with >90% expecting the June move. | Market/economist interpretation leaned renewed tightening risk, not one-off relief. |

**HANS classification:** **Conditional renewed tightening path.** The ECB is not locked into a cycle, but the June hike should be treated as the start of a renewed hiking *option set* unless energy/inflation pressure fades quickly or growth breaks hard.

---

## 2) Current Fed-vs-ECB Policy Differential

**Rate definitions matter:** compare the ECB **deposit facility rate** to the Fed **target range/midpoint**, not ECB MRO to Fed upper bound unless explicitly stated.

| Policy rate | Current | Source / note |
|---|---:|---|
| ECB deposit facility | **2.25%** | ECB Jun11 decision, effective Jun17. |
| ECB main refinancing operations | **2.40%** | ECB Jun11 decision, effective Jun17. |
| ECB marginal lending facility | **2.65%** | ECB Jun11 decision, effective Jun17. |
| Fed funds target range | **3.50%–3.75%** | FOMC Jun17 held unchanged. |
| Fed funds target midpoint | **3.625%** | Midpoint of 3.50–3.75. |
| Fed IORB | **3.65%** | Fed implementation note, effective Jun18. |
| Fed SOFR | **3.62%** | FRED latest fetched Jun22; observation Jun18. |

**Policy differential:** Fed midpoint **3.625%** minus ECB deposit **2.25%** = **+137.5bp USD-over-EUR**. Fed upper bound vs ECB deposit = **+150bp**.

**Likely direction:**
- **Fed:** Jun17 FOMC held, but SEP median fed funds rate is **3.8% for end-2026** vs current 3.625% midpoint, implying one hike is on the table; PCE median revised up to **3.6%** for 2026.
- **ECB:** data-dependent, but inflation revisions and Reuters polling/market snippets leave at least one more hike plausible if energy/inflation pass-through persists.
- **Net:** differential likely remains **USD-positive** unless ECB out-hikes the Fed or U.S. data rolls over. This is not yet Europe easing pressure on U.S. rates; it is a global inflation-rate-vol regime.

---

## 3) U.S. Transmission Channels

| Channel | Mechanism | Current HANS read |
|---|---|---|
| **EUR/USD** | ECB hikes support EUR via higher EUR yields; Fed hawkishness/risk-off supports USD. | EUR/USD ~**1.1446** via yfinance Jun22; EUR has eased from mid-June levels. Net signal: USD still supported despite ECB hike. |
| **DXY** | USD rate advantage + risk-off demand. | DXY ~**100.85** via yfinance Jun22; not a dollar-breakdown signal. |
| **UST demand / term premium** | If ECB hikes lift European yields, EUR-based investors have less need to reach for USTs; hedged UST attractiveness can fall when dollar hedging costs remain high. Risk-off can still send flight-to-quality into USTs. | Direction ambiguous: tightening abroad can pressure global duration/term premium, while stress can support USTs. Needs Batch B2 TIC/custody for flow answer. |
| **European bank dollar funding** | Higher USD rates + weaker EUR/risk shock can raise dollar funding cost for European banks/NDFIs; shows in EUR/USD basis, CP/CD markets, swap-line use, bank CDS. | Monitor-only. No verified broad stress from available checks. |
| **EUR/USD cross-currency basis** | More negative basis = premium to borrow dollars against euros. | Current live basis not verified; keep threshold **3M EUR/USD basis < -50bp** or fast move >20bp wider in 1 week. |
| **Fed/ECB swap lines** | Backstop for dollar shortage in foreign jurisdictions; activation/size change is a stress marker. | Standing lines exist. Fed SWPT was **$49mn on 2026-06-17** after $28mn Jun10 / $116mn Jun3 — tiny, consistent with testing/operational-size balances, not crisis usage. |
| **TPI / fragmentation** | ECB may use TPI if disorderly sovereign spread widening impairs monetary-policy transmission. TPI mention matters because hikes into weak growth can expose periphery/core fractures. | ECB says TPI remains available; no verified activation or disorderly spread threshold in this pass. Keep France-Germany >100bp / Italy-Germany >200bp as STATUS monitors, but Phase 7 owns clean live spreads. |

---

## 4) Verified Current Funding Stress?

**Answer: no verified current funding-stress threshold fired. Mark monitor-only.**

| Indicator | Current / evidence | Threshold | Status |
|---|---:|---:|---|
| Fed central-bank liquidity swaps (SWPT) | **$49mn** on 2026-06-17; prior **$28mn** Jun10, **$116mn** Jun3. | Sustained >$5bn = 🟠; >$25bn or rapid weekly surge = 🔴. | ✅ No stress. |
| EUR/USD 3M cross-currency basis | Live value **not verified**; CME page blocked automated fetch. | <**-50bp** or >20bp weekly widening = 🟠/🔴 depending speed. | ⚪ Data gap, not breach. |
| ECB emergency dollar operation / frequency change | Standing weekly USD ops exist; no current emergency frequency escalation found. | Daily USD ops or unusual take-up = 🔴. | ✅ No stress found. |
| EUR/USD / DXY | EUR/USD ~1.1446, DXY ~100.85. | EUR/USD fast break <1.10 with basis widening; DXY spike >105 with funding signals. | ✅ Not funding-stress alone. |
| ECB TPI / emergency action | TPI available, no activation found. | Activation / emergency meeting = 🔴. | ✅ No stress found. |

**Important caveat:** absence of a verified live EUR/USD basis quote is the main unresolved data gap. Do **not** assert “basis is calm” until a usable source is found; assert only that no threshold was verified as fired.

---

## 5) Handoff If Thresholds Fire Later

If any threshold fires, HANS should send compact outbox to **LIQUID/BOND/NEXUS** with:

| Trigger | Send to | Message payload |
|---|---|---|
| EUR/USD 3M basis < -50bp or widens >20bp in 1 week | LIQUID + NEXUS | Dollar funding stress is now visible in EUR funding markets; include basis level, weekly change, EUR/USD, DXY, and swap-line use. |
| Fed SWPT >$5bn sustained or >$25bn spike | LIQUID + BOND + NEXUS | Central-bank dollar-liquidity backstop is being used beyond operational test size; include latest H.4.1/SWPT series and direction. |
| ECB emergency dollar ops / daily frequency / unusual take-up | LIQUID + BOND + NEXUS | European bank dollar-funding demand moved from market-price stress to official-liquidity channel. |
| ECB TPI activation or disorderly spreads | BOND + LIQUID + NEXUS | Euro sovereign fragmentation risk has become a UST term-premium / flight-to-quality transmission event. |
| EUR/USD breaks <1.10 and DXY >105 alongside basis widening | LIQUID + NEXUS | FX move is no longer just rate differential; treat as dollar squeeze / global funding tightening candidate. |

No outbox written from this batch because no verified current threshold fired.

---

## Source Notes

- **ECB press release, 2026-06-11:** monetary policy decisions; 25bp hike; deposit/MRO/MLF to 2.25/2.40/2.65 effective Jun17; projections and TPI language. URL: https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html
- **Reuters search snippets, 2026-06-11 / 2026-06-03:** hike long-telegraphed; investors saw two more hikes over coming year; economists saw another likely in September. Direct Reuters fetch blocked by JS/401, so use snippets as secondary framing only.
- **Fed FOMC statement, 2026-06-17:** target range maintained at 3.50–3.75. URL: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm
- **Fed implementation note, 2026-06-17:** IORB 3.65%; ON RRP 3.50%; SRF 3.75%; reserve-management T-bill purchases if needed. URL: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a1.htm
- **Fed SEP, 2026-06-17:** median federal funds rate 3.8% end-2026; PCE 3.6%; core PCE 3.3%. URL: https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260617.htm
- **Fed central-bank liquidity swaps page / NY Fed operations page:** standing swap lines are a dollar-liquidity backstop; small value transactions may be operational-readiness tests; weekly publication when conducted. URLs: https://www.federalreserve.gov/monetarypolicy/central-bank-liquidity-swaps.htm and https://www.newyorkfed.org/markets/desk-operations/central-bank-liquidity-swap-operations
- **FRED fetched 2026-06-22:** DFEDTARU/L 3.75/3.50 through Jun22; SOFR 3.62 on Jun18; SWPT $49mn on Jun17.
- **yfinance fetched 2026-06-22 ~09:06 ET:** EURUSD=X 1.1446; DX-Y.NYB 100.85.
