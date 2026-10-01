# CARL-DR-3: What prices the 2026 consumer-discretionary cross-section, and does any cut restore the cohort-income (K-shape) axis?
**Date:** 2026-10-01 | **Mode:** Thesis | **Confidence:** High on the factor arithmetic (reproducible from public prices; out-of-sample betas) · Medium on the cohort verdict (the cohort labels are DEWEY's own classification, 47 names, and only the factor-residual cuts are statistically distinguishable from noise) · High on the AZO/ORLY KPI facts (8-K Ex-99.1 primary)
**Commission:** CARL-DR-3, CARL packet 2026-07-31 (Will-approved, `c424c9d0a`), target ~2026-08-28, **delivered 34 days late**. It was dropped by omission: the 7/31 packet was moved to `inbox/processed/` without a run. Carried by `PROME/DOCKET.tsv` (the 2026-10-01 CARL-DR-3 WAKE row) and run as a PROME-spawned due-row session (prome-0c). Engine: DEWEY primary pull (Yahoo daily prices, FRED, SEC XBRL and 8-K releases) plus two data-return sub-agents for KPI extraction. No fan-out harness.
**Scoring:** CARL pre-registered the kill condition and scores it. This report supplies evidence, not a score.

> **Post-delivery, 2026-10-01 (dated receipts; the body is unchanged):**
> - **Scored by CARL 12:33 ET** (`6b8ebb5c4`; memo `PROME/inbox/2026-10-01c_from-CARL_DR-3-scored-kill-not-fired-and-DR-1-run-drop.md`, `23b627ea8`): **kill NOT fired.** The trade-down half is restored after style factors; the premium half is not restored and is staged to RED. CARL does not count low-vol style as the duration branch, but withdrew the "defensive down = K-shape refuted" read on the style + AZO-margin finding. PS-0005 is not invalidated (AZO FQ4-26 SSS +1.6%, CARL-verified at the 8-K).
> - **LIFO wording reconciled for CARL (DEWEY message, ~12:50 ET):** "+105bp net LIFO" in AZO's FQ4-26 release is the year-on-year margin effect of a SMALLER charge ($15M vs $80M in FQ4-25), not a LIFO credit. §5 states it the same way.

## Key Finding

**The AZO/ORLY anomaly is mostly a style effect, plus an AZO-specific earnings stall. It is not a consumer-cohort effect.** O'Reilly's whole underperformance is explained by its exposure to the low-volatility/defensive style, which lagged the market by about 12 points over CARL's window: ORLY's earnings rose about 14% while its P/E fell about 22%. AutoZone shows the same style hit, plus a residual of about −23 log points that sits almost entirely on its three earnings days inside the window. In each of those quarters a LIFO (inventory-accounting) charge cut gross margin by 77–212bp while domestic same-store sales grew +3.4% to +4.8%. Underneath those comps, DIY transactions fell 3–4% every quarter, masked by ticket inflation.

**One cut restores half of the cohort axis.** Group the 47 names by customer cohort and compare group medians instead of the four poster names. Then the **trade-down leg holds in every cut tested**: value/trade-down destinations beat mid-tier names in 15 of 15 label-and-model combinations (raw +5pp; +28pp after style factors), and lower-income credit names are the worst group after factors. **The premium leg does not hold in any cut.** Premium names are the worst group on raw returns (median −23pp vs SPX) and no better than mid-tier after factors. YETI and WSM were exceptions inside their own group: LULU, CMG, ONON, RH, DECK and ULTA all fell 23–80pp against the S&P.

**The leverage/duration candidate does not explain AZO/ORLY.** Their measured rate sensitivity is median for the cross-section, and the 10-year yield moved only +26bp over CARL's window. Starting valuation does not explain them either: AZO's P/E was mid-tercile at 24×, and richer names such as COST (56×) and WMT (40×) held up. **So the read "defensive names down = K-shape refuted" is not supported**, and neither is a rate story. The defensive names fell as a style, and the value group as a whole outperformed.

## 1. The anomaly, reproduced (CARL's window: 1 year to 2026-07-24)

| Name | DEWEY rel. SPX (simple, 7/24/25→7/24/26) | CARL 7/24 figure | Extended to 10/1/26 (simple rel. SPX) |
|---|---|---|---|
| S&P 500 abs. | +16.5% | +14.7% | — |
| AZO | −39.5pp | −44pp | (2026 YTD −29.9pp) |
| ORLY | −27.4pp | −30pp | (2026 YTD −19.1pp) |
| AAP | −21.1pp | −23pp | — |
| YETI | +20.4pp | +28.6pp | (2026 YTD −18.8pp; −18.7% since 7/24) |
| WSM | +10.9pp | +5.8pp | (2026 YTD +17.9pp) |

Source: Yahoo Finance daily adjusted closes via `yfinance`, pulled 2026-10-01 (last row 2026-10-01, intraday). ⚠️ **CARL's figures reproduce in sign and rank but not exactly** (gaps up to 8pp, on YETI). CARL's basis (price vs total return, close date) is not recorded on its card. Nothing below depends on the exact figure.

⚠️ **The poster pair has since moved.** YETI is −18.7% since 7/24 and now sits −18.8pp vs SPX for 2026. Half of "premium is UP" has reversed since CARL pinned it.

## 2. Factor attribution table (out-of-sample; log-return points, 7/25/25–7/24/26, 251 trading days)

Method: regress each name's daily log return on seven ETF-proxy factors over **2023-01-03 → 2025-07-23** (before the window), then apply those betas to the factor returns realised inside the window. Factors: MKT = SPY · SIZE = IWM−SPY · VALUE = IWD−IWF · MOM = MTUM−SPY · LOWVOL = USMV−SPY · QUALITY = QUAL−SPY · RATES = daily change in the 10-year Treasury yield (FRED `DGS10`, bp). Factor returns over the window: MKT +16.4 · SIZE +11.1 · VALUE +16.5 · MOM +9.0 · **LOWVOL −11.7** · QUALITY −0.2 · 10y +26bp (4.43% → 4.69%).

| Name | MKT | SIZE | VALUE | MOM | **LOWVOL** | QUAL | RATES | **Explained** | **Actual** | **Residual** | LOWVOL β (rank of 47) | Est. R² |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AZO** | +16.1 | +0.2 | −2.8 | +0.7 | **−17.7** | −0.1 | +0.2 | −3.4 | −26.2 | **−22.8** | 1.51 (4th) | 0.26 |
| **ORLY** | +15.8 | +0.4 | −4.1 | +1.0 | **−19.5** | 0.0 | +0.2 | −6.3 | −11.6 | **−5.3** | 1.66 (2nd) | 0.29 |
| AAP | +19.3 | +8.0 | +7.6 | −5.7 | +0.9 | −0.1 | −0.4 | +29.6 | −4.7 | −34.3 | −0.08 | 0.13 |
| GPC | +19.1 | +3.6 | +6.0 | −2.6 | −7.2 | −0.2 | +0.1 | +18.8 | −3.5 | −22.2 | 0.62 | 0.29 |
| **YETI** | +17.3 | +8.7 | +5.8 | −5.9 | **+10.2** | −0.2 | −0.5 | +35.4 | +31.4 | −4.0 | −0.87 | 0.31 |
| **WSM** | +15.1 | +6.7 | +11.6 | −0.1 | **+20.4** | −0.2 | −0.6 | +52.9 | +24.2 | −28.7 | −1.74 | 0.34 |

**Read across the poster pairs:**
- **AZO vs YETI:** the actual gap is 57.6 log points. Style factors explain 38.8 of it (67%); the residual gap is 18.8.
- **ORLY vs WSM:** the actual gap is 35.8. Style factors "explain" 59.2, more than all of it. WSM underperformed its own factor exposures.
- The top LOWVOL betas in the cross-section are KR 1.68, **ORLY 1.66**, MUSA 1.55, **AZO 1.51**, BJ 1.47, MCD 1.26, CASY 1.20, OLLI 1.11. These are the classic defensive stocks. That is a STYLE identity, not a customer-income identity.

**Extended to 10/1:** AZO residual −30.8, ORLY −10.1, YETI −19.7, WSM −23.6. LOWVOL lagged by 13.8 points, and the 10-year rose 83bp to 5.26% (9/29).

**Robustness (residual medians; full detail in §3):** the AZO/ORLY reading holds under seven factor specifications (CAPM; MKT+rates; FF3-style; full with USMV; full with SPLV in place of USMV; MKT+high-beta; MKT+staples). ORLY's residual ranges −5.3 to −26.4; AZO's ranges −22.8 to −42.0. ORLY ranks 20–37 of 47 (1 = worst), so it is mid-pack or better once style is removed. AZO ranks 10–25.

## 3. Cohort-axis test: does any cut restore it?

**Labels (DEWEY's a priori classification by core-customer income; ⚠️ assigned AFTER DEWEY had seen the raw return table, so not blind; tested for sensitivity below):**
- PREMIUM (11): YETI WSM RH LULU TPR RL DECK ONON ULTA CMG AXP
- VALUE / trade-down destination (19): WMT COST BJ DG DLTR FIVE OLLI TJX ROST BURL AZO ORLY AAP GPC MNRO KR CASY MUSA MCD
- LOW-INCOME CREDIT (4): CRMT SYF COF KMX
- MID (13): TGT BBY HD LOW TSCO SBUX DRI TXRH NKE ELF AN LAD ABG
- Excluded as mega-cap-contaminated: AMZN, TSLA.

**K-shape predictions:** VALUE > MID (trade-down) · PREMIUM ≥ MID (top cohort fine) · LOW-INCOME CREDIT worst.

| Cut (median, log pp) | PREMIUM | VALUE | MID | LOW-INC CREDIT | VALUE−MID (perm. p) | PREM−MID | Leg verdict |
|---|---|---|---|---|---|---|---|
| C0 raw vs SPX, CARL window | −23.0 | **−9.9** | −15.4 | −18.2 | +5.4 (0.72) | −7.6 | trade-down ✓ (not sig.) · premium ✗ |
| C0 raw, 7/25/25→10/1/26 | −19.9 | **−19.8** | −32.9 | −26.7 | +13.1 (0.28) | +13.0 | trade-down ✓ (n.s.) · premium ✓ (n.s.) |
| C0 raw, 2026 YTD | −25.6 | **−16.5** | −22.4 | −30.1 | +5.9 (0.39) | −3.3 | trade-down ✓ (n.s.) · premium ✗ |
| C1 OOS full-factor residual, CARL window | −36.1 | **−5.3** | −33.1 | **−59.4** | **+27.8 (0.001)** | −3.0 | trade-down ✓✓ · low-inc worst ✓ · premium ✗ |
| C1b same, to 10/1 | −45.7 | **−6.3** | −41.7 | **−62.4** | **+35.3 (0.001)** | −4.1 | as C1 |
| C2 in-sample residual, CARL window | −23.6 | **−3.0** | −26.6 | **−45.7** | **+23.6 (0.022)** | +3.0 | as C1 |

**Sensitivity, VALUE−MID (median gap, CARL window):**

| Label variant | raw | CAPM resid. | full-factor resid. | smallest leave-one-out value |
|---|---|---|---|---|
| base | +5.4 | +9.6 | +27.8 | +3.2 (raw) |
| ambiguous VALUE names dropped (COST MCD KR CASY MUSA GPC MNRO) | +8.0 | +14.5 | +27.2 | +5.4 |
| ambiguous names moved to MID | +7.5 | +12.0 | +15.3 | +5.0 |
| YETI and WSM excluded | +5.4 | +9.6 | +27.8 | +3.2 |
| auto parts excluded | +12.0 | +19.5 | +32.9 | +10.0 |

Positive in **15 of 15 combinations** and in every leave-one-out. Across the seven factor models × two windows, VALUE−MID ranges +9.1 to +37.4 and PREMIUM−VALUE ranges −11.6 to −41.0 (all 14 negative).

**Answer to "does any cut restore the cohort axis?" — PARTLY, and the half that returns is the trade-down half.** Three cuts restore it:
1. **Group medians instead of poster names.** The trade-down ordering is already present in CARL's own raw window, but too weakly to be distinguished from noise.
2. **Remove style factors.** The ordering becomes large and statistically distinguishable, and lower-income credit names fall to the bottom.
3. **Exclude auto parts.** This strengthens the result: auto parts were the weakest members of the VALUE group, not representatives of it.

**What no cut restores:** the premium/top-cohort leg. Premium names are the worst group raw and no better than MID after factors. The K-shape's "top cohort is fine" leg is **not visible in equities** under any cut tested here.

## 4. The other candidate factors (commission list)

| Candidate | Test | Result | Verdict |
|---|---|---|---|
| **Rates/duration by starting valuation** | Starting P/E (market cap at 7/24/25 ÷ last 10-K net income; SEC XBRL) vs window return, 42 names with P/E 0–80 | Spearman ρ = −0.13 raw (rich tercile −20.6 vs cheap −15.0 median); **+0.19 after factors**. AZO 24.1× (mid tercile), ORLY 35.2× (rich); COST 56×, ELF 60×, RH 55×, WMT 40× | **Weak and inconsistent.** It does not single out AZO; ORLY is only partly a "most expensive" case |
| **Rate sensitivity** | β to the daily 10y change, controlling for market, 2023-01→2025-07 | AZO −0.9% per +100bp, ORLY −1.2%, cross-section median −0.9% (10th–90th pct −3.0…+1.0); most rate-negative: LOW −5.1, HD −5.0, AAP −3.5. 10y moved only +26bp in CARL's window | **Rejected for AZO/ORLY:** median rate sensitivity, small rate move |
| **Leveraged-buyback model** | Negative stockholders' equity (SEC XBRL, latest 10-Q/K before 7/24/25): RH, AZO (−$3.97B), ORLY (−$1.36B), MCD, LOW, SBUX. FY buyback yield | The 6 negative-equity names: median −25.2 raw vs −12.1 for the others; **after factors −21.4 vs −24.8 (no gap)**. Buyback yield vs return ρ = +0.06 (n=45) | **Absorbed by style.** These are the same low-volatility compounders; there is no separate financing-channel effect. Leverage did not rise during the window: AZO held 2.5× and its deficit narrowed; ORLY was ~2.04–2.06× and rose to 2.17× only in Q2-26 [PRIMARY] |
| **DIY-vs-DIFM cycle** | FRED `TRFVOLUSM227NFWA` (vehicle miles, monthly, NSA); AZO domestic commercial sales; ORLY pro/DIY commentary | Miles: 12-month sum still growing +0.8% to +1.1% YoY through Jul-2026 (+0.21% YoY Jul-2026). Commercial outgrew DIY at all four names in every quarter (§5). AZO DIY transactions fell 3.4–3.6% per quarter through FY26 and more than 5% in FQ4-26 (DIY comp −0.6%) [call] | **A DIFM-over-DIY shift is real and steady in the KPIs.** It does not show in the window's comps or prices: AZO domestic SSS was +3.4% to +4.8% (ticket inflation masked the DIY count decline), and ORLY comps accelerated. **This is a cohort signal inside the auto-parts KPIs: the lower-income DIY customer is shrinking**, and AZO management named it in September. It is not what moved the stocks in CARL's window |
| **Tariff COGS exposure** | Filings and calls (§5) | AZO imports 13% of purchases directly; most of its tariff bill is Section 232, not IEEPA [call 3/3/26]. LIFO charges ($80M, $98M, $59M, $20M in four quarters) track tariff-driven cost inflation; FQ4-26 brought +145bp of IEEPA refunds. AAP: ~40% of COGS exposed at ~30%. GPC: China ~20% of US auto purchases. All four passed costs through ("industry pretty disciplined and rational") | **Tariffs reach AZO through the LIFO line, which is where its idiosyncratic residual sits.** ORLY does not report quarterly LIFO and its margin held (51.4–51.9%), so the tariff channel differs by accounting, not by exposure. There are too few names to test as a cross-sectional factor |
| **GLP-1 basket** | Company statements, 12 names | WMT: GLP-1 is a **pharmacy-sales tailwind** (~50bp of FY27 comps vs ~100bp FY25/FY26) [PRIMARY: WMT FQ2-27 presentation 2026-08-20]; WMT CFO calls the basket effect "a wash" (2026-02-19). MCD: "don't yet see evidence of it really having a material impact" (2026-02-11). No GLP-1 attribution found at TGT, DG, DLTR, TJX, ROST, BURL, YETI, WSM | **No evidence it prices this cross-section.** Not testable as a return factor (no public GLP-1 basket index) |
| **AI-adjacency / index flow** | MOM (MTUM−SPY) and high-beta (SPHB−SPY) factors | Momentum +9.0 over the window; it contributes ≤±6 pts to any name here. The high-beta model gives the same cohort ordering (VALUE−MID +14.0) | **The flow story arrives through LOWVOL, not MOM.** Low-volatility stocks lagged a high-beta market. Passive-ownership share by name: not reachable (see Process Report) |
| **Comp decomposition (traffic vs ticket)** | 8-K releases, 12 names, Q2-25 → latest | See §5 | **The K-shape is in what managers SAY, not in the traffic/ticket split** |

## 5. KPIs: what the companies report

**AutoZone (fiscal year ends late August; all [PRIMARY]: 8-K Ex-99.1)**

| Quarter (release date) | Domestic SSS | DIY comp · ticket / transactions [call] | Commercial growth | Gross margin Δ vs LY | LIFO charge | 2-day stock reaction vs SPY |
|---|---|---|---|---|---|---|
| FQ3-25, to 5/10/25 (5/27/25) | +5.0% | +3.0% · +1.5 / +1.4 | +10.7% | −77bp | 21bp ($8M) | (before window) |
| FQ4-25, to 8/30/25 (9/23/25) | +4.8% | +2.2% · +3.9 / −1.9 | +6.0% (17-wk comparison; ~12.5% on 16 wks) | −98bp | **$80M (128bp)** | +2.2 |
| FQ1-26, to 11/22/25 (12/9/25) | +4.8% | +1.5% · +4.8 / **−3.4** | +14.5% | −203bp | **$98M (212bp)** | **−10.2** |
| FQ2-26, to 2/14/26 (3/3/26) | +3.4% | +1.5% · +5.2 / **−3.6** | +9.8% | −137bp | **$59M (138bp)** | **−4.2** |
| FQ3-26, to 5/9/26 (5/26/26) | +4.1% | +2.2% · +5.6 / **−3.6** | +10.4% | −57bp | **$20M (77bp)** | **−12.4** |
| FQ4-26, to 8/29/26 (9/22/26) | **+1.6%** | **−0.6%** · ~+5 / **down >5%** | +8.6% | **+182bp** (incl. +145bp IEEPA tariff refunds ≈ $96M, and +105bp from a LIFO charge of $15M vs $80M LY) | $15M; FY26 **$192M** | +2.2 |

Sources: SSS, commercial growth, margin and LIFO from 8-K Ex-99.1 [PRIMARY]. DIY comp, ticket and transactions from earnings calls [INSTITUTIONAL: roic.ai transcripts]; on FQ3-25 the CEO said ~1% DIY ticket and the CFO said 1.5%. Adjusted debt/EBITDAR was held at **2.5×** throughout; the stockholders' deficit **narrowed** from −$3.97B to −$2.50B [PRIMARY]. Direct imports were ~13% of FY25 purchases [PRIMARY: FY25 10-K, 10/27/25].

- FY26 diluted EPS $152.55 (+5.3%), against FY25 $144.87 (−3.1%) and FY24 $149.55.
- At 7/24/26, trailing EPS was about $145.21 (DEWEY's arithmetic from the release tables), so EPS was **flat-to-down** across CARL's window while P/E fell from **25.7× to 20.4×** (now 18.1× on FY26 EPS at $2,767, 10/1).
- **The three prints inside the window sum to −26.8 log points against SPY**, which matches AZO's ~−23 factor residual. **The residual is an earnings-day phenomenon: margin (LIFO) prints with comps intact** (but DIY transactions falling; see the next bullet). Consensus expectations were not available (no free source), so whether each print "missed" is not established here.
- **AZO's DIY customer was shrinking through the whole window, hidden by price.** DIY transactions fell 3.4–3.6% in each FY26 quarter while DIY ticket rose 4.8–5.6% (same-SKU inflation, tariff pass-through). In FQ4-26 DIY transactions fell more than 5% and DIY comp turned negative. Management, 9/22/26: *"We see evidence of deferrals and trade down in DIY, particularly with the most financially challenged DIY customers"*; *"The 5% decline or north of that in transactions is not typical in this industry"* [INSTITUTIONAL: call transcript]. Earlier, on 12/9/25: *"We don't see a lot of trade down."*
- ⚠️ **For CARL's PS-0005 (written against the characterization):** FQ4-26 domestic SSS is **+1.6%**, above the registered +1.0% invalidation line but down sharply from +4.1%. CARL scores this; DEWEY flags only that the line is close and the quarter is a 16-week, post-window print.

**O'Reilly (calendar year; [PRIMARY]: 8-K Ex-99.1)**

| Quarter (release date) | Comp | Diluted EPS (YoY) | Pro / DIY note |
|---|---|---|---|
| Q2-25 (7/23/25) | +4.1% | $0.78 (+11%) | "solid growth in both professional and DIY" |
| Q3-25 (10/22/25) | +5.6% | $0.85 (+12%) | — |
| Q4-25 (2/4/26) | +5.6% | $0.71 (+13%); FY25 $2.97 (+10%) | — |
| Q1-26 (4/29/26) | +8.1% | $0.72 (+16%) | "double-digit growth in our professional business and mid-single digit growth in DIY" |
| Q2-26 (7/29/26) | +6.0% | $0.86 (+10%); $2.4B repurchases YTD | "solid growth in both professional and DIY" |

ORLY does not quantify ticket vs traffic (Q2-26 call). Its professional comp was ">7%" to "double-digit" in every quarter; DIY was low-single-digit, and **DIY transaction counts were "down low single digits"** in Q2-26 [INSTITUTIONAL: calls]. Same-SKU inflation rose from ~1.5% (Q2-25) to ~6% (Q4-25 to Q1-26). Leverage rose to **2.17×** adjusted debt/EBITDAR in Q2-26 (target 2.5×) on **$1.51B of Q2 buybacks** funded partly with commercial paper; the deficit went from −$1.23B to −$1.84B [PRIMARY].

ORLY: trailing EPS ~+14% across the window (DEWEY's arithmetic: ~$2.77 → ~$3.15; pre-split 2024 quarters ÷15, approximate). Price −11% (simple). **P/E ~35× → ~28×.** **Fundamentals accelerated while the multiple compressed, which is the signature of a style de-rating.**

**All four auto-parts names, mid-2026: commercial (DIFM) outgrew DIY at every one, and DIY turned negative.**
- AZO: DIY −0.6% against commercial +8.6% (FQ4-26).
- ORLY: DIY transactions down low single digits (Q2-26).
- AAP: comp −0.5%, DIY down low single digits; "tighter household budgets constrained spending" [PRIMARY: 8-K 8/20/26].
- GPC: retail ~−3% against commercial ~+4% (Q2-26).

Tariff exposure:
- AAP: ~40% of COGS exposed at a ~30% blended rate [call, 8/14/25].
- GPC: China ~20% of US automotive purchases [call, 7/22/25].
- AZO: 13% of purchases imported directly [10-K].
- ORLY: no percentage disclosed.

Industry: vehicle age 12.8 years (S&P Global Mobility, May 2025 [NEWS]; no 2026 release found); aftermarket forecast +5.2% for 2026 (Auto Care/MEMA, 6/11/26 [INSTITUTIONAL]).

**Traffic vs ticket across the cohort (sub-agent extraction from 8-K Ex-99.1 releases [PRIMARY]; income quotes from public call transcripts [INSTITUTIONAL: roic.ai transcription, re-checked by the sub-agent])**

| Name | Window quarters: traffic / ticket | What management says about income |
|---|---|---|
| WMT US | traffic +1.5 to +3.0 · ticket **+1.1 to +3.1 (never negative)** | "majority of our share gains came from households making more than $100,000…below $50,000…wallets are stretched" (2026-02-19) |
| Sam's Club US | traffic +3.9 to +7.0 · ticket +2.0 → **−2.5** | — (the only clean traffic-up/ticket-down series) |
| DG | traffic −0.3 to +2.6 · ticket 0 to +2.7 | "largest increase in customer count came from the highest income segment…more than $100 thousand" (Q1-26 call) |
| DLTR | traffic **−1.2 to +3.0** · ticket **+2.8 to +6.3 (ticket-led)** | "~60% [of 3M added households] earning over $100,000" (Q3-25 call) |
| TGT | 2025 traffic negative; 2026 traffic +3.6/+4.4, ticket ~0 to +1 | "across income brackets" |
| COST US | traffic +5.5 → +1.8 → +3.2 · ticket up with gas | no income split |
| TJX / ROST / BURL | transaction-led at ROST; no numeric split | TJX: same comp above and below $100k; BURL: lower-income-area stores outperformed; ROST: "every single household income group" |
| MCD US | guests down in Q1-25 and Q2-26 | low-income traffic "down nearly double-digits"…higher income "increasing nearly double digits" (2025-11-05); low income "absolutely still declining" (2026-05-07) |
| CMG | transactions −4.9 to +1.0 | "household income below $100,000…about 40% of sales…dining out less often" (2025-10-29); the lower-income cohort "improved the most" (2026-07-29) |
| YETI | US sales −4.9 (derived) → +8 | "some evidence of consumer trade down" (Q2-25 call) |
| WSM | comp brand revenue +3.2 to +6.2; no traffic/ticket | declined to characterize income |

**Read:** the K-shape is **present in management testimony** (WMT, DG, DLTR and MCD each name trade-in by, or gains from, households over $100k, and losses below $50k). It is **not present in the traffic/ticket arithmetic it predicts**: ticket never fell at WMT, DG or DLTR, and DLTR was ticket-led. The trade-in at discounters shows up as **new households**, not as smaller baskets. Off-price shows no income skew. **That is the same split the equities show:** a trade-down/low-income axis exists; a "premium is fine" axis does not show cleanly.

## 6. Verdict on the decision question

**What prices the 2026 consumer-discretionary cross-section?** Mostly **style**: market beta plus a −12-point low-volatility/defensive lag, and value/size exposure that favoured higher-beta names. Then **company-specific earnings**: AZO's LIFO margin stall, AAP's turnaround, CRMT's credit collapse. Then a **broad consumer de-rating** common to nearly every name: the median factor residual is negative in every group except VALUE.

**Does any cut restore the cohort axis?** **Yes for the trade-down leg, no for the premium leg.** A KPI cut adds a third piece: **the lower-income customer is visibly shrinking inside the auto-parts KPIs** (DIY transactions negative at all four names by mid-2026, and named by AZO management), even though prices in CARL's window did not sort on it. Three cuts restore it: group medians, style-factor residuals, and exclusion of auto parts. Once factors are removed, VALUE beats MID by 15–35 points and lower-income credit names are the worst group. AZO/ORLY were the wrong representatives of the defensive trade-down group: they are its two most low-volatility-loaded members, and the group as a whole outperformed.

**On the second half of CARL's kill condition:** *"if the leverage/duration factor explains AZO/ORLY, the 'defensive names down = K-shape refuted' read is ALSO wrong."* Leverage/duration as specified (rate β, negative equity, buyback yield) does **not** explain them. A related style factor, **low-volatility**, does explain ORLY fully and about 40% of AZO's move. Whether that counts as the "leverage/duration" branch is CARL's call. DEWEY notes that low-volatility stocks behave as bond proxies, so the two are cousins, but this window's 10-year move was only +26bp.

## Counter-Evidence

- **The labels are DEWEY's and were not blind.** I had seen the raw returns before assigning cohorts. Mitigation: the labels follow conventional customer positioning, and the VALUE−MID sign survives three relabelings and every leave-one-out. A different analyst could still label COST, MCD, TGT or TSCO differently. **Customer-income data by name (card-panel or foot-traffic demographics) would replace the labels and is not publicly reachable.**
- **The raw-return cuts are not statistically distinguishable from noise** (permutation p 0.28–0.72). Only the factor-residual cuts are (p ≤ 0.022). If CARL rejects the factor model, the trade-down restoration is directional only.
- **The factor model is a choice.** ETF proxies, daily data and R² of 0.13–0.44 per name. USMV holds some of these names (a mild circularity). The SPLV substitute, CAPM, FF3-style and high-beta specifications give the same ordering, but magnitudes vary by 2–3×.
- **Low-volatility is itself partly a consumer-defensive factor.** If the defensive de-rating happened BECAUSE investors expected a soft-landing re-acceleration or a lower-income consumer recession, "style" is not orthogonal to the macro thesis. That would be a macro-regime trade, not a cohort sort. This report cannot separate the two.
- **YETI's reversal** (−18.7% since 7/24) and **ROST's +17% comp** quarter suggest the cross-section is unstable across windows. Three windows were tested; a different window could move the medians.
- **The premium leg's failure may be mis-specification, not refutation.** The PREMIUM group mixes athletic/apparel names (LULU, ONON, DECK, NKE-adjacent) with company-specific problems. LULU (−80pp) and CMG (−52pp) drive the median.
- **The auto-parts KPIs carry a lower-income signal that the price test treats as noise.** AZO DIY transactions were −3.4% to −3.6% in every FY26 quarter, and below −5% in FQ4-26, while ticket inflation kept comps positive. If the market priced the DIY count decline rather than the comp, part of AZO's earnings-day residual is a cohort effect, which would move AZO from "anomaly" toward "confirms." This report cannot separate a margin reaction from a traffic reaction on those days.

## Source Quality Assessment

Prices and factor returns: Yahoo via `yfinance` (adjusted closes; vendor data, reproducible, not exchange-official). FRED `DGS10`, `TRFVOLUSM227NFWA` [PRIMARY]. Starting P/E, equity and buybacks: SEC XBRL companyfacts [PRIMARY]. ⚠️ The automated debt tag was unreliable (some names returned a partial `LongTermDebt` fact, and CRMT, TXRH and NKE returned stale vintages), so debt/market-cap is **not** used in any verdict. AZO/ORLY KPIs: 8-K Ex-99.1 [PRIMARY], read directly by DEWEY. Cohort KPIs: 8-K Ex-99.1 [PRIMARY] via sub-agent; income quotes from roic.ai transcripts [INSTITUTIONAL]; one DG Q2-26 quote [UNVERIFIED: allmind.ai summary] is excluded from the table. Overall: **High** for numbers, **Medium** for the cohort inference.

## References (accessed 2026-10-01)

- AutoZone 8-K Ex-99.1: SEC EDGAR CIK 866787, accessions 0001171843-25-003448 (5/27/25), -25-006024 (9/23/25), -25-007831 (12/9/25), -26-001288 (3/3/26), -26-003674 (5/26/26), -26-006159 (9/22/26). https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000866787&type=8-K
- O'Reilly 8-K Ex-99.1: CIK 898173, accessions 0000898173-25-000046 (7/23/25), -25-000055 (10/22/25), -26-000006 (2/4/26), -26-000024 (4/29/26), -26-000042 (7/29/26).
- Cohort releases (WMT 104169, TGT 27419, DG 29534, DLTR 935703, COST 909832, TJX 109198, ROST 745732, YETI 1670592, WSM 719955, BURL 1579298, MCD 63908, CMG 1058090): 8-K Ex-99.1, Q2-25 through the latest available at 2026-10-01 (accession list held in the sub-agent return; reproducible by `edgar_fetch.py <CIK> --type 8-K`).
- SEC XBRL companyfacts: https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json (47 names).
- FRED: https://fred.stlouisfed.org/series/DGS10 · https://fred.stlouisfed.org/series/TRFVOLUSM227NFWA
- Transcripts: https://www.roic.ai/quote/<TICKER>/transcripts/<FY>-year/<Q>-quarter (WMT 2026-02-19; DG Q1-26; DLTR Q3-25; MCD 2025-11-05, 2026-02-11, 2026-05-07; CMG 2025-10-29, 2026-02-03, 2026-07-29; YETI Q2-25).
- CARL baseline: `AGENTS/CARL/thesis/CHANGELOG.md` (7/24 entry, "Pinned baseline (1y to 7/24 vs SPX +14.7%)"); `AGENTS/CARL/thesis/CARL_BOOK_DESIGN.md` §2b; `AGENTS/CARL/book/README.md` PS-0005.

**Reproduction recipe** (scratch is session-scoped and not cited):
1. Prices: `yfinance.download(<47 names + SPY ^GSPC IWM IWD IWF MTUM USMV QUAL SPLV SPHB XLP>, start=2022-12-01, auto_adjust=True)`.
2. Rates: `AGENTS/DEWEY/scripts/fred_pull.py DGS10 --start 2022-12-01 --csv`.
3. Daily log returns; OLS of each name on [1, factors] over 2023-01-03..2025-07-23.
4. Contribution = β × Σ(window factor log returns); residual = Σ name log return − Σ contributions.
5. Cohort medians; two-sided permutation test on group medians (20,000 shuffles, seed 7).
6. Starting P/E = shares (dei cover, split-corrected via yfinance splits) × unadjusted close at 7/24/25 ÷ latest 10-K `NetIncomeLoss` filed before 7/24/25.

## Process Report

**Searches run:** primary pulls (Yahoo 63 tickers; FRED 3 series; SEC XBRL 47 companyfacts; AZO 7 and ORLY 5 8-K releases read directly); 2 data-return sub-agents (auto-parts filings; 12-name traffic/ticket/income). No fan-out harness: the residual was 1–2 analytical legs (engine sizing).
**Data gaps:** consensus EPS expectations (needed to say whether AZO's prints were "misses"); customer-income composition by retailer (card-panel, foot-traffic demographics); passive/index ownership by name; a GLP-1 basket return index; S&P Global Mobility vehicle-age release (spglobal.com is bot-blocked, per `fetch_url.py`).
**Source frustrations:** `XRT` failed in yfinance (NoneType). `fred_pull.py --help` is parsed as a series ID and its error message prints the full API URL **including the API key** to the terminal (BACKLOG row added). The SEC tickers JSON is gzip-encoded with no `Content-Encoding` handling in the ad hoc caller. The XBRL `LongTermDebt` tag is unreliable as a total-debt measure.
**Confidence in findings:** High that ORLY is a style de-rating and that AZO's residual is earnings-day/margin. Medium that the trade-down axis is restored (label choice; significant only after factors). High that the premium leg is not restored in any cut tested.
**If I had more time/tools:** a blind relabel by a second reader before seeing returns; Ken French daily factors (when published through the window) in place of ETF proxies; consensus data to grade AZO's prints.
**Suggestions:** if CARL keeps the equity leg, register the **group-median, style-residual** cut as its instrument, not poster names. Poster names carried a style loading the thesis does not claim.
