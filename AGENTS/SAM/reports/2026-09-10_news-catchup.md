# SAM news and data catch-up — September 10, 2026 (JST) / September 9 (ET)

**Written 2026-09-10 ~02:0x UTC (Sep-9 ~22:0x ET / Sep-10 ~11:0x JST), Will-directed ("get SAM's files caught up to current with any news or new data/intel from live searches").** Boot sweep 13/13 scripts OK (`reports/boot-runs/20260910T015008Z_3db90c36.jsonl`). No pull performed: local was 12 commits ahead of origin and 0 behind, and BOND had an uncommitted working set (pull protocol rule 2). Every figure below carries its own source clock; nothing here grades a prediction, changes thesis version, or moves the FLAT book.

## 1. Live levels (vendor unless stated)

| Instrument | Level | Clock / source | Note |
|---|---|---|---|
| USD/JPY | **153.69** | vendor 2026-09-10 01:50 UTC | BOJ reference Sep-9: 9:00 JST 153.45–47; **17:00 JST 153.11–13**; range **152.95–153.93**; central 153.72 (`fx260909.pdf`). Sep-8 17:00 was 153.80–82 ⇒ yen +0.45% d/d on the official reference |
| EUR/JPY · GBP/JPY · AUD/JPY | 178.81 · 208.26 · 110.86 | vendor 01:50 UTC | BOJ Sep-9 17:00 EUR/JPY 178.26–30 |
| FXY | $59.70 (+0.24%) | Sep-9 close | not a certified mark |
| DXY / VIX / S&P 500 | 98.80 (−0.04%) / **16.46 (+4.71%)** / 7,636.36 (−0.48%) | Sep-9 close, vendor | modest risk-off day; gold 4,451.70 (+1.32%) |
| US 3M / 5Y / 10Y / 30Y | 3.80 / 4.61 / 4.84 / **5.29%** | Sep-9 close, vendor | 30Y back near the Aug-18 19-yr high (CNBC 8/18: 5.33%) |
| Brent (BZ=F continuous) / WTI | **$101.68** / $96.79 (+4.04%) | 01:39 UTC Sep-10 / Sep-9 close | continuous front-month vendor marks, NOT the named November contract used in the Sep-4/8 matched read |
| Nikkei 225 | 64,314 (−1.27%) intraday | Sep-10 ~10:5x JST vendor | Sep-9 close 65,143 (−126.55); Sep-8 close 65,269 (−1,130.51, −1.70%) per News On Japan |
| MOF JGB curve Sep-9 | **2Y 1.833 / 5Y 2.243 / 10Y 2.891 / 20Y 3.713 / 30Y 3.956 / 40Y 3.960%** | MOF `jgbcme.csv`, pub Sep-9 | 5-day: 10Y −11.5bp, 30Y −16.6bp, 40Y −17.4bp from Sep-2 |
| US–JP differential Sep-9 | 5Y **2.367pp** / 10Y **1.939pp** | `rate_differential.py` | +11.7bp / +13.9bp above the SAM-41 bars; runs 0/5; widening on the US leg |
| JPY xccy PROXY Sep-9 | residual **−11.5bp**, Δ −0.9bp | `xccy_basis.py` | vendor revision of the −11.78/−1.15 recorded Sep-9; pair expires Sep-14 |
| BOJ Sep meeting OIS (Totan) | **98% incremental 25bp equiv; 1.2213%** | image Sep-9 15:15 JST (assumed) | unchanged this boot; next chart expected Sep-10 15:15 JST — review before citing |
| Fed Sep-16 pricing | **54% +25bp / 46% hold** | Polymarket, Sep-10 01:45 UTC, $109.2M volume | prediction market, not CME; CME FedWatch "~56%" circulates in secondary press with no pinned date |

## 2. BOJ Sep-9 FINAL settlement — the Sep-9 leg closes as anticipated fiscal

Primary: `https://www.boj.or.jp/en/statistics/boj/fm/juq/d_release/jd/2026/jd20260909.xlsx` (the `jd/<YYYY>/` layout; the flat `jd/jd20260909.xlsx` path 404s). Units ¥100M.

| Item | Projection | Provisional | **Final** |
|---|---:|---:|---:|
| Banknotes | +600 | +600 | +600 |
| Treasury funds and others | −33,600 | −35,900 | **−35,900** |
| Surplus/shortage | −33,000 | −35,300 | −35,300 |
| Market operations (ex-LSP) | +500 | +100 | +100 |
| Net change in current accounts | −32,500 | −35,200 | **−35,200** |
| Balance | 4,119,300 | 4,116,600 | **4,116,600** |

Final fiscal **−¥3,590B = provisional**. Versus Ueda Yagi's Sep-3 forecast (−¥3,600B): **+¥10B**. Versus BOJ's own Sep-8 projection (−¥3,360B): −¥230B. **Inference unchanged from Sep-9: the Sep-9 gross drain was ordinary anticipated funding; it supplies no incremental intervention evidence.** Sep-8 (final −¥1,100B vs Ueda +¥100B) remains the unexplained residual. Sep-10 provisional (`jx20260910.xlsx`) and the Sep-11 projection were both 404 at 01:52 UTC — expected ~18:00 JST and ~10:00 JST respectively. Attribution for Sep-7/8 stays **OPEN**; Japan's settlement series cannot see a US-only leg.

## 3. BOJ Sep-9 market operations vs the Aug-31 schedule (SAM-33 absence check, primary)

`ope/d_release/ope/2026/ope20260909.xlsx` vs `mpr260831a.pdf` (Quarterly Schedule Jul–Sep 2026, schedule update):

| Bucket | Offered Sep-9 | Scheduled size | Scheduled date? | Bids / accepted | BTC | Avg spread |
|---|---:|---:|---|---:|---:|---:|
| 1–3Y | ¥355.0B | 3,550 | yes (9/9, 9/28) | 11,080 / 3,553 | 3.12× | +0.001 |
| 5–10Y | ¥335.0B | 3,350 | yes (9/9, 9/16) | 7,862 / 3,354 | 2.34× | −0.005 |
| **25Y+** | **¥75.0B** | **750** | **yes (9/9, 9/16)** | 1,884 / 752 | **2.51×** | +0.021 |

Plus routine securities-lending (¥45.4B AM, ¥1.0B PM). **Every Sep-9 purchase was a scheduled-date, scheduled-size competitive auction. No fixed-rate operation, no additional date, no size increase.** Monthly plan ¥2,500B (計 25,000); Oct–Dec schedule due **Sep-30 17:00 JST**. ⇒ **SAM-33's falsifier has NOT fired through Sep-9** (verified at the operation record, not inferred from silence). Masu's Sep-10 restatement that the Bank "decided at the June 2026 MPM to halt the reduction … from fiscal 2027 … about 2 trillion yen per month" is the scheduled taper-plan endpoint, which the prediction's own terms exclude from the falsifier.

## 4. MOF weekly flows, week Aug-30 → Sep-5 (MOF ITS, via `mof_flows.py`)

| Leg | Net |
|---|---:|
| Residents' foreign equity | −¥481.6B |
| Residents' foreign LT debt | **+¥111.9B** |
| Residents' foreign ST debt | +¥103.8B |
| Non-residents' Japanese equity | +¥690.0B |
| Non-residents' JGBs (LT) | **+¥449.6B** |

Weekly LT inside the ¥1.5T bar (🟢 not applicable). **4-week rolling LT −¥1.55T = 🟡 ELEVATED vs the ¥1.4T base-case upper** (script alert), driven by the −¥1.98T [8/16–22] and −¥824.0B [8/23–29] weeks; 12-week rolling −¥266.6B. Third consecutive week of foreign inflows into JGBs. Sector-neutral: says nothing about USTs or named institutions.

## 5. BOJ September: pricing, the pre-MPM speech cluster, and the Bessent campaign

- **Masu Kazuyuki, Fukui, Sep-10 (BOJ primary `ko260910a1.pdf`, 40,083 chars extracted).** Neutral rate: natural rate range −0.9% to +0.5% ⇒ nominal **"1.1 to 2.5 percent"**, "simply a reference"; **"Japan alone has a policy rate that is below the estimated range"**; "To complete the normalization … I am convinced that the Bank needs to raise the policy interest rate further, so that it falls solidly within the estimated range … ensuring the flexibility needed to swiftly adjust the policy rate in either direction." Underlying inflation "very close to 2 percent"; "the Bank will continue to raise the policy interest rate … It will consider the timing and pace of adjustment, while examining the likelihood of realizing the baseline scenario and the risks … from crude oil prices, AI-related demand, and developments in foreign exchange rates." FX: "the Bank does not set its policy interest rate to respond directly to changes in foreign exchange rates. That said, the impact of the yen's depreciation on prices has become more pronounced than in the past." Balance sheet: halt-the-reduction from FY2027, ~¥2T/month (~¥24T/yr); holdings peaked ~¥590T (~50% of outstanding); "What JGB maturities the Bank should hold … is likely to become a topic of growing importance." No explicit September call in the text.
- **Ueda, Sep-2** (Bloomberg/Japan Times 9/2; Nikkei 9/2 "rate hikes on table at every meeting, including this month's"): policy decided "with upside price risks in mind"; three upside forces — Middle East conflict, AI investment demand, yen depreciation. **Takata, Sapporo, Sep-2** (Bloomberg 9/2): "nimble" hikes to prevent upside deviation. **Himino, Saitama, Aug-26** (Japan Times 8/27): no pushback against September pricing. **Reuters Aug-14 sources**: September hike "in sight", faster pace than ~2/yr under consideration.
- **Aida Takuji (Takaichi economic adviser; Crédit Agricole), Reuters Sep-7** (investing.com mirror): pulls his forecast forward to a **September hike to 1.25%**, **another in January 2027**, then "around once every six months"; reason — "a narrow window of opportunity … before an extraordinary session of parliament convenes in early October" (food-levy suspension bill); warns the pace "would weigh on the economy". Reflationist camp now forecasting, not opposing.
- **Bessent, Aug-31 CNBC at the G20 Asheville** (nippon.com/Jiji Sep-1 10:18 JST): "It's my belief that the Japanese government and that the BOJ will do the things that will lead to a stronger yen"; "I have information that the market doesn't have." Already carried in the archived 9/1 block ("Bessent told Ueda (8/30) and Katayama (8/31)"). **New Sep-9:** TradeTheNews/FXStreet 05:53 GMT quotes Bessent: "When we intervene on yen, I have good insight … what BOJ … will do" (secondary, partial). Bloomberg Sep-9 headline: "BOJ faces pressure from Bessent's push for yen, risking market disruption" should the BOJ under-deliver (body 403 — headline only).
- **Katayama, Sep-8** (Bloomberg 9/8 headline via search): stance "hasn't shifted" since the joint intervention; will "maintain orderly markets"; close contact with Bessent.
- **HSBC, Sep-7** (FXStreet): ~75bp cumulative priced by April 2027; Sep-18 "a critical test"; base case range-bound USD/JPY.
- **Market narrative on the yen (Business Insider Sep-9; Nikkei Sep-8 10:29 JST "touching the 152 level"):** carry unwind + repatriation expectations + BOJ pricing + US pressure; MUFG's Wan: "driven mainly by domestic Japanese factors"; LPL: a break below 152 could "reignite" the carry-unwind risk. **None of this is transaction evidence** — CFTC is still Sep-1 (pre-rally); Sep-11 gives Sep-8 positions.

**Read:** the September hike is now consensus across the board's hawks, the PM's own adviser, and the US Treasury, and priced at 98% (Totan). The asymmetry noted Sep-1 (a surprise HOLD is the larger yen move, and it is yen-negative) is unchanged. **No re-pencil; no route re-arms.**

## 6. Fed side

- **Waller, Sep-3** (Fed primary): inclined to HOLD if disinflation signs continue over "the next two weeks"; a hike "may be appropriate" Sep 15–16 if August data show the improvement was fleeting; policy "only slightly" restrictive. Press: hike odds ~65% → ~50-50 after the speech.
- **Pricing Sep-10 01:45 UTC:** Polymarket 54% hike / 46% hold. CNBC Aug-28 "coin flip"; Forbes Aug-31 CME 66%. **No CME primary read this session.**
- **US CPI (Aug) Sep-11 08:30 ET** consensus (Kiplinger): headline +0.4% m/m / 3.4% y/y; core +0.4% / 2.4%. The registered Fed-side tripwire remains the actual dot walk-back at the Sep-16 SEP, not CPI.
- US 10Y 4.84 / 30Y 5.29% (Sep-9 vendor); the US leg is what widened the SAM-41 gaps this week (JP 5Y −8.9bp vs US 5Y +7bp over 5 days).

## 7. Fiscal / politics (Takaichi)

- **FY2027 budget requests ¥143.1T (MOF, Fri Sep-4; Japan Today/Reuters, Xinhua 9/4):** record for a 4th straight year; includes ¥12T under a new uncapped "special investment" category; **debt-servicing request ¥36.64T (+¥5.36T y/y)** on an **assumed interest rate raised to 3.8% from 3.0%** after the 10Y hit 3% (first since 1996); defense ¥8.84T. Takaichi (Japan Times 9/5): the new process improves "transparency" and ends reliance on extra budgets.
- **No second FY2026 supplementary budget** (Japan Times/Jiji Sep-3): Kumamoto earthquake and rain-disaster responses to be funded from reserves in the initial + first extra budget; **extraordinary Diet session under consideration for early October**; Kihara: "only for measures that are truly urgent and imperative."
- **Food consumption-tax (8%) suspension for two years** to be debated in the October session (per Aida/Reuters 9/7) — the fiscal item Aida frames the BOJ's September "window" around.
- Nikkei "readies record budget, alarming market" is the **Dec-19-2025** FY2026 piece, not September news — do not cite it as current.

## 8. GPIF

- **Aug-21 management-committee meeting** (Bloomberg 9/3; agenda posted 8/31, already in the 9/8 assessment §GPIF): first publicly announced August meeting in seven years; basic-portfolio review project-team report on the agenda; **no allocation decision announced**.
- **Ueno Kenichiro (health minister), Sep-8** (Japan Times via mirror): the fund "decided in March that there wasn't a need for [a review], but my understanding is that it's continuing to consider the matter in an appropriate way"; "the investment environment hasn't diverged too much from the GPIF's assumptions." AUM ~¥318T (end-June); 1pp ≈ >¥3T. **Expectations channel, not measured flow.** Trust-account buying in the MOF August sector data remains not attributable to GPIF.

## 9. July balance of payments (MOF/BOJ primary `bp202607.pdf`, released Sep-8 08:50 JST; ¥100M)

| Item | Jul-2026 | Jun-2026 | Jul-2025 |
|---|---:|---:|---:|
| **Current account** | **+29,889 (+15.6% y/y)** | −923 | +25,863 |
| Goods & services | −9,128 | −3,637 | −9,588 |
| Goods | −3,999 | −1,352 | −1,877 |
| Exports | 112,561 (+24.1%) | 104,801 | 90,695 |
| Imports | 116,560 (+25.9%) | 106,153 | 92,572 |
| Services | −5,129 | −2,285 | −7,711 |
| Primary income | +42,896 (+5.8%) | +3,801 | +40,539 |
| Secondary income | −3,879 | −1,086 | −5,089 |

June's negative current account (−¥92.3B) was the first deficit in the series in recent memory and is now behind us; July's surplus is carried by primary income. Goods deficit widened y/y (+113%) on imports +25.9% (oil value; semiconductor imports per the press read). **BoP-basis goods differs from the customs trade balance (July −¥634.5B customs vs −¥399.9B BoP).** Financial-account detail not transcribed (column interleaving in the PDF extract; re-open if needed).

## 10. Energy / geopolitics — HAWK and BRENT own the events; SAM records the oil-in-yen input only

Sep-7→9 escalation (CNBC 9/8, 9/9; GlobalSecurity Day-194 update 9/9; Al Jazeera 9/7): US forces destroyed five Iranian crude carriers Sep-8 after two IRGC attempts on a US warship; IRGC fired ~20 ballistic missiles at Al Azraq (Jordan), 18 intercepted; Houthis struck the 400 kb/d Jazan refinery; Iran claimed strikes on two US vessels and eight tankers; Iran also said (Sep-8, Bloomberg) a Hormuz deal with Oman was "close". **Brent crossed $100 Sep-9 for the first time in ~6 weeks and settled above $101 (first since July).** Goldman raised its probability of >$120.

Oil-in-yen vendor proxy (continuous Brent × USDJPY, NOT matched-timestamp, NOT the named contract): Sep-10 01:39–01:50 UTC ≈ 101.68 × 153.69 = **¥15,627/bbl**, vs the Sep-8 vendor pair 99.28 × 153.81 = ¥15,270 ⇒ **+2.3%**: the oil leg outran the yen leg over the two sessions. The Sep-4/8 matched-hourly figure (+1.36%) remains the only clocked measurement.

## 11. Risk-off read for SAM-31 (observation only, no grade)

Sep-9 US session: VIX 16.46 (+4.7%), S&P −0.48%, gold +1.3%, DXY flat (−0.04%). Yen on the BOJ 17:00 JST reference: 153.81 → 153.12 (**+0.45%**), EUR/JPY 178.4x → 178.28. Same sign as a haven re-coupling, at trivial amplitude and with the domestic BOJ-repricing driver dominant in every contemporaneous account. **Not a VIX-spike regime; logged into the Sep-18 packet's daily screen, not graded.** The VIX 2026 low was 14.13 (CNBC 8/17).

## 12. Unchanged this session

Thesis v1.7 / LOW, no successor; book FLAT; SAM-28/31/33 OPEN on original terms; CFTC Sep-1 (pre-rally); Totan image Sep-9 15:15 JST; US funding Sep-8; Japan funding Sep-9 provisional; MOF August sector flows; Sep-3 30Y SOFT grade; 40Y no-tail ruling still owed before Sep-29; futures-pair activation HOLD to Sep-14.

## 13. Pending on the docket (next reads)

Sep-10 JST 15:15 Totan chart · Sep-10 ~18:00 JST BOJ Sep-10 provisional · Sep-10 noon ET EIA · **Sep-11 08:50 JST CGPI (Aug)** [added to CATALYSTS] · Sep-11 08:30 ET US CPI · Sep-11 15:30 ET CFTC (Sep-8 positions) · Sep-14 proxy expiry · Sep-15 20Y · Sep-16 FOMC + Aug trade · Sep-18 CPI → BOJ → SAM-28/31 close · Sep-30 17:00 JST BOJ Oct–Dec purchase schedule (new date, from `mpr260831a.pdf`).

## 14. Source clocks

BOJ `jd/2026/jd20260909.xlsx`, `ope/2026/ope20260909.xlsx`, `mpr260831a.pdf`, `fx260909.pdf`, `ko260910a1.pdf` (all fetched 2026-09-10 01:52–02:05 UTC) · MOF `bp202607.pdf` (rel 2026-09-08) · MOF ITS week 8/30–9/5 and `jgbcme.csv` via boot 01:50 UTC · vendor quotes via `FORGE/tools/market-data/fetch.py` 01:50–01:55 UTC · Polymarket 01:45 UTC · Fed Waller speech 2026-09-03 · nippon.com/Jiji 2026-09-01 10:18 JST · investing.com/Reuters 2026-09-07 · Business Insider 2026-09-09 · Nikkei Asia 2026-09-08 10:29 JST · FXStreet/TradeTheNews 2026-09-09 05:53 GMT · FXStreet/HSBC 2026-09-07 · Japan Today/Reuters and Xinhua 2026-09-04 · Japan Times 2026-09-03 (Jiji), 2026-09-05, 2026-09-08 (via mirror) · CNBC 2026-09-08/09, 2026-08-18 · GlobalSecurity 2026-09-09 · Bloomberg 2026-09-02/03/08/09 headlines only (bodies 403). Paywalled/403 bodies are cited by headline and marked as such above.
