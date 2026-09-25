# HY OAS 280 [9/24]: what widened, is it tape or substance, and what it does to the book

**LIQUID · Fri 2026-09-25, started 13:04 ET (`date`) · Will-directed, Tier 2 (Will: *"Okay I would like to investigate the HY credit spreads."*), spawned by PROME `prome-2e`.**
**$0 · no threshold, gate, score or standing approval moved · the 280 print is ONE observation, not a re-arm.**
**Sources:** FRED ICE BofA OAS series via `FORGE/tools/market-data/fetch.py` (latest-revised, pulled 9/25 ~13:05 ET) · `scripts/transmission_check.py` (13:04 ET) · `scripts/boot.py` (13:04 ET) · yfinance raw closes (`auto_adjust=False`), with a 9/25 intraday snapshot at ~13:05 ET · WALTER BOARD `SIG-W-20260924-006/-024`, `SIG-W-20260925-001/-007` · BOND FR2004 read (`8163ad57d`) · TERRY Q1 exposure map (`research/2026-09-25_Q1_book-exposure-map.md`) · web sweep (§1d, read-only subagent). Regressions: scratch scripts; daily changes 2023-10-02 → 2026-09-21, fitted out-of-sample for 9/22–9/24.

---

## BOTTOM LINE

1. **The move was broad on its last day, not CCC-led.** In basis points CCC led (+37 over 9/22→9/24). **As a percentage, and in its contribution to the index, it did not.** BB rose +5.1%, B +5.5% and CCC +3.4%. Single-B supplied the most index basis points (≈5.4 of ≈13.7). On 9/24 **every rung widened at or above its own 89th percentile of daily moves, investment-grade included** (IG +2 at the 96.5th percentile). So the claim "the widening is CCC-led" holds in raw basis points and fails on the basis the guard uses.
2. **Tape vs substance: PROVISIONAL beta-leaning, not clean either way.** The guard's test 1 (proportional tiers) reads **BETA**, the same shape as the 7/29 tag, though softer. Test 2 (broad developed-market beta) **splits by day**. 9/24's +7 is ≈83% explained by European HY's +11 that day (the France OAT day). 9/23's +5 is **US-specific**: European HY *tightened* 6 that day. Test 4 (rates) **cannot discriminate**, because the Treasury yield rose alongside. Test 3 (does the tail stay wide when the index retraces?) is **not yet available**.
3. **Rates caused none of the widening mechanically, but they are the likeliest cause behind it.** OAS is measured over Treasuries by construction. On its 2023–26 daily history, **HY OAS has TIGHTENED about 0.3bp per 1bp rise in the 10Y.** Rising yields have usually meant growth. A model using the 10Y, VIX and SPY (n=712, R²=0.44) predicts **about −2bp** over 9/22–9/24. **The actual move was +14bp from 9/21, a residual of about +16bp, roughly 1.7 standard deviations over three sessions.** The sign flip is what a **real-yield shock** looks like: 10Y real yield +14bp to 9/23, breakevens flat. That is a discount-rate and refinancing-cost hit, which bites CCC hardest. Equity volatility explains ≈3bp at most (VIX 14.21 → 15.67; SPY −0.8%).
3b. **The primary market is open, which argues against substance.** SoftBank's record $11.1B priced inside talk on every tranche, and the CoreWeave-linked $1.1B data-center bond priced within talk at 9.25%. **No pulled or downsized HY deal was found for 9/21–9/25**, but that is SEARCH-NOT-FOUND, not verified absence. CDX HY for 9/23–9/25 and CoreWeave's September CDS: SEARCH-NOT-FOUND.
4. **`LIQ-07` is not close.** Single-B's 15-session change on 9/24 is **+10bp (76th percentile)** against the **+28bp** bar. The count is **0-of-3**. For the next three observations B would need **≥305 / ≥305 / ≥304**, i.e. 18–19bp above 286. **Not a live prospect this week.**
5. **Re-arm path:** my estimate from the ETF tape for the **9/25 observation is +3bp ±5 (1σ), ~283, range 278–288**. It publishes **Mon 9/28 ~16:15 ET**. The estimate has under-called the last two sessions by ~4bp each, so the risk is skewed wider. **Historical base rate: 10 of the 14 first touches of ≥280 since 2023-10 went on to three consecutive prints ≥280.** Reaching the re-kill (<260 twice) needs −21bp. A two-session drop that large has happened **2.2%** of the time. **Remote.**
6. **Book: the touch changes no registered rule, because none of the named lines has a rule keyed to HY OAS.** ⛔ **X1's sizing gate stays CLOSED.** The wrapper half was adjudicated NOT ARMED on 8/28 (BROCK, KB-BRK-219). **A cross above 280 returns that DECIDED answer: X1 does not fire on the index leg alone. Fail-safe is DON'T-SIZE.**
7. ⚠️ **A basis defect sits under the word "touch".** The registered letter is **">280"**. Integer 280 is AT the line, not over it: the same arithmetic that made 260 [8/28] a non-event on the kill side. `boot.py` classifies on **≥280**. That mismatch is CATO MEDIUM, open since 9/22 and still unfixed. **Under the letter, 9/24 is not a cross.** Under the classifier it is a touch, 1-of-3. It is moot today only because X1 is closed either way. **I am not ruling it here, because that would move a threshold.**

---

## Q1 — WHAT widened, and WHERE

### 1a. By quality bucket (FRED ICE BofA OAS, bp, latest-revised)

| series | 9/21 | 9/22 | 9/23 | 9/24 | Δ 9/22→9/24 | Δ % | ≈ index wt | index-bp contribution | 9/24 d/d pctile | 15-sess Δ (base 9/03) · pctile |
|---|---|---|---|---|---|---|---|---|---|---|
| IG `BAMLC0A0CM` | 77 | 77 | 77 | 79 | +2 | +2.6% | — | — | 96.5 | −2 · 46.3 |
| BBB `BAMLC0A4CBBB` | 95 | 95 | 95 | 97 | +2 | +2.1% | — | — | 95.3 | −3 · 39.9 |
| BB `BAMLH0A1HYBB` | 153 | 156 | 159 | 164 | +8 | **+5.1%** | ~53% | ≈4.2 | 89.7 | +12 · 84.2 |
| B `BAMLH0A2HYB` | 270 | 271 | 278 | 286 | +15 | **+5.5%** | ~36% | **≈5.4** | 91.4 | **+10 · 76.1** |
| CCC `BAMLH0A3HYC` | 1,077 | 1,075 | 1,093 | 1,112 | **+37** | +3.4% | ~11% | ≈4.1 | 96.2 | **+61 · 92.0** |
| **HY `BAMLH0A0HYM2`** | 266 | 268 | 273 | **280** | **+12** | +4.5% | 100% | Σ ≈13.7 vs +12 | 92.1 | +15 · 83.0 |
| CCC−B gap | 807 | 804 | 815 | 826 | +22 | | | | 96.0 | **+51 · 94.6** |
| CCC−BB gap | 924 | 919 | 934 | **948** | +29 | | | | | **highest in the FRED window (from 2023-10)** |
| Euro HY `BAMLHE00EHYIOAS` | 273 | 272 | 266 | 277 | +5 | | | | | |

*Weights are the approximate H0A0 rating mix used in the 7/30 attribution (residual validated then). Percentiles come from `transmission_check.py`: n=780 daily changes and n=766 15-session changes since 2023-10.*

**Verdict on the CCC-led shape PROME relayed: CONFIRMED in raw bp, REFUTED as the driver of the index.** CCC is the biggest mover in basis points and the persistent one: its 15-session change is at the 92nd percentile and the CCC−B gap at the 94.6th. But CCC is about 11% of the index and moved only 3.4% proportionally. **B carried the most index basis points, and BB moved the most in percent.** ⚠️ Every percentile here is ranked against a calm three-year window (FRED's ICE history starts 2023-10, with no 2020 or 2022 stress in it). "Window max" is not "record". **The HY index's own 2026 high is 346 [3/30/2026], so 280 is not a 2026 high.** The series maximum in the window is 461 [2025-04-07]. The CCC maximum is 1,137 [2025-04-07], 25bp above today's level.

### 1b. By sector (proxies only. ⚠️ ICE sector sub-indices are terminal-gated, so there is no sector OAS)

| cohort | instrument | 9/22 close → 9/24 close | 9/25 intraday (~13:05) | read |
|---|---|---|---|---|
| **AI / data-center** (GATE-LIQ-069 L4 cohort) | CRWV · NBIS · APLD · IREN (raw) | **+3.9% · +3.1% · −5.2% · −4.9%** | 87.67 · 237.64 · 26.27 · 44.02 | Mixed. No name near the L4 −15% single-session bar. **L4 NOT FIRED**, although its HY leg (≥+5bp/session) was met on 9/23 (+5) and 9/24 (+7): worst cohort session on 9/24 was IREN −1.9%. |
| AI financing, IG issuer | ORCL | 149.20 → 139.54 = **−6.5%** | 138.31 (−7.3% vs 9/22) | The week's most-stressed AI-financing name, but **investment-grade and outside the HY index**. See 1c. |
| **Energy** | XLE · XOP · USO | **+1.3% · +1.3% · +6.3%** | XLE 61.73 · USO 147.87 (−3.4% on the day) | **Energy equities rose with oil ⇒ the evidence argues against energy credit driving this.** ⚠️ HY-Energy OAS is permanently unmeasured here, so "no energy dislocation" is UNMEASURED, not verified. |
| Banks / CRE | KRE · WAL | **−0.4% · −1.9%** | KRE 71.71 (**+1.1%**) · WAL 78.10 | **Bank leg absent**, same as the 7/30 attribution. |
| BDC / private credit | BIZD · APO | **−1.5% · −2.8%** | 12.83 · 121.16 | Soft but still above BIZD's $12.50 line. **BROCK owns the wrapper half and is running it in parallel. Not duplicated here.** |

**The weight arithmetic (KB-LIQ-091) still binds.** The AI/data-center cohort is a low single-digit share of the HY index's market value, so it cannot move the index +12bp by itself. The 9/24 day is explained by the developed-market common factor (§Q2), not by a sector.

### 1c. Oracle (answers WALTER `SIG-W-20260925-007`)
- **GATE-LIQ-069 R1 does NOT move.** R1 = a *second* agency to the IG floor: Moody's Baa2 → Baa3 or Fitch BBB → BBB−. **No rating action this week** has been found at any source I or the web sweep reached. Moody's is still **Baa2 with a NEGATIVE outlook**, and an outlook is not an action. S&P **BBB−** (7/9, R0, already logged). Fitch **BBB**. **Middle rating BBB = IG.**
- The post's "~100bp wide of BBB" is an unattributed, maturity-weighted model built on LSEG data. With S&P already at BBB−, part of that gap is the rating itself. **Not usable as a leg.** The **5Y CDS record is now CONFIRMED by a second source**, at a different level (221.78bp Markit via rallies.ai vs 227.15bp Seeking Alpha, both 9/24; §1d). CDS is L2's instrument, and L2 is **CRWV-only**. **So Oracle's CDS is outside every leg of 069, as recorded on 9/12, and it stays that way.**
- ⛔ The primary-source recheck of the agency ratings, owed since 8/24, is **still not done** (agency sites are registration-gated). NOT-ADVANCING; no gate move and no action proposed.

### 1d. Single-name vs breadth, and the PRIMARY market this week
- **TRACE breadth (advance/decline, issuer-count widening): SEARCH-NOT-FOUND.** FINRA TRACE NTMBHH/NTMBHL are terminal-gated from this box. Breadth here comes from the tier and ratio figures in 1a.
- **Primary market 9/21–9/25:** see the table below (web sweep, read-only, with sources).

| item | figure, date | source | grade |
|---|---|---|---|
| **SoftBank record HY deal** | **$11.1B**: $1B 3.5y **8.625%** · $4.5B 5.5y **9.25%** · $4.5B 7.5y **9.75%** · €500M 4y 7.125% · €500M 6y 8.0%. Priced **inside talk on every tranche** (revised talk 8.75–8.875 / 9.375–9.5 / 9.75–9.875). Orders >$20B. BB+ | American Bazaar 9/24; Bloomberg 9/23 headline (paywalled); Seoul Economic Daily 9/23 | secondary; pricing date 9/23 vs 9/24 conflicts |
| **CoreWeave-linked DC bond** (Blue Owl affiliates Cedarwood Investment Group LP / PowerHouse Data Centers LLC, Richmond VA campus) | **$1.1B 5y at 98.5 to yield 9.25%**, ~270bp over similarly rated bonds. S&P BB−. Talk "low to mid 9%" ⇒ **priced within talk, not wide** | Bloomberg 9/23 headline; briefs.co 9/21 and 9/23 | secondary |
| HY deal **pulled / postponed / downsized / priced wide**, 9/21–9/25 | **SEARCH-NOT-FOUND** | web sweep | not upgraded to "none": deal-level feeds are paywalled |
| Leveraged loan pulled | **SEARCH-NOT-FOUND** | — | same |
| US HY weekly issuance | **SEARCH-NOT-FOUND** for this week. Week to 9/19: ~$13B, "highest in months" | Debt Serious 9/19 | secondary |
| HY fund flows | This week: **SEARCH-NOT-FOUND** (Lipper 9/25 gives global bond +$9.68B, loans +$1.4B, no HY line). **Prior week (to ~9/16): global HY funds −$3.85B** | Reuters/LSEG Lipper 9/25 and 9/18 | secondary |
| **CDX HY** | **9/23–9/25: SEARCH-NOT-FOUND.** Baseline: 308 → 317 intraday on the 9/16 Fed press conference; **306 on 9/17**, "near eight-month lows" | Credit Bubble Bulletin 9/19 | single source; baseline only |
| **Oracle 5Y CDS** | **Record confirmed by a second source, at a different level:** 221.78bp (Markit via rallies.ai, 9/24) vs **227.15bp** (Seeking Alpha, 9/24 12:52 ET, +16.2% w/w) | two secondaries | the ~5bp gap is probably quote time or basis |
| **CoreWeave 5Y CDS** | **September: SEARCH-NOT-FOUND.** Last found ~855bp [7/29] (TechTimes 7/30). Proxy: CRWV 2032 bond yield +44bp to 11.60% in the week to 9/19 | Credit Bubble Bulletin (single source) | stale |
| Energy HY sector spread | **SEARCH-NOT-FOUND** (permanently terminal-gated) | — | — |
| Reporting on the HY widening | **SEARCH-NOT-FOUND.** Coverage is about Treasuries: 5Y above 5% for the first time since 2007 (9/23, "strong data plus a weak auction"; my own 5Y read: 54.31% indirect, BTC 2.21); 30Y ~5.44% [9/24], highest since 2004 | Bloomberg 9/23; Reuters 9/24 | secondary |
| **Brightline Florida, prearranged Chapter 11** | **9/24**, 17 entities, D.N.J.; **$490M new money** ($140M senior / $350M junior). Four tax-exempt series stated UNIMPAIRED ($2.2B 2024 Assured-insured · $985M 2025B · $925M 2024 · $285.7M 2024A) | **issuer release, PR Newswire 9/25 00:13 ET (primary)**; Bond Buyer | ⚠️ muni/project debt, **not in the ICE HY index**. Florida ⇒ routed to WALTER for CORAL |

**Primary-market verdict: OPEN and clearing.** The week's two AI-linked deals came inside or within talk, into >$20B of orders, and no pulled deal was found. **That argues against a substance (issuance-freeze) reading of the widening.** Primary-market stress is the 350 rung of the ladder, and it is nowhere near. It is consistent with price discovery through the **secondary** market: new AI paper clears at ~9–10% yields while the index reprices around it.

---

## Q2 — TAPE vs SUBSTANCE (the KILL_MEMO §B confirm-side guard, run at the tag)

### 2a. Guard tests at the tag (test 3 cannot be run yet; its timing property applies)

| # | test | result | reads |
|---|---|---|---|
| 1 | Tiers **proportional** (KB-LIQ-088) | BB **+5.1%** · B +5.5% · CCC **+3.4%** (9/22→9/24) | **BETA signature.** BB led CCC in percent. Same shape as 7/29 (BB +10.2% vs CCC +2.45%), but softer |
| 2 | Broad developed-market beta (KB-LIQ-091) | Model B (10Y + VIX + SPY + ΔEuro HY, R²=0.62): **9/24 fitted +5.6 of +7 actual (≈80%); 9/23 fitted −2.8 vs +5 actual (≈0%)**. Three-session share ≈ 5–6bp of +14 ≈ **40%** | **SPLIT.** The last day is tape (France/European HY common factor). The 9/23 day is US-specific |
| 4 | Rates-mechanical | OAS rose while DGS10 **rose** (4.96 [9/22] → 5.11 [9/23]; ^TNX 5.162 [9/24]) | **Not discriminating** by the guard's own letter. Only a widening with the 10Y *falling* is clean spread pressure |
| 3 | Reversal: does the tail hold when the index retraces? | **NOT AVAILABLE** until a retrace | Run on the first retrace. **If CCC holds while HY gives back its gain, upgrade to substance** |

**PROVISIONAL grade: `TAPE-CONFIRM`-leaning, MIXED, test 3 pending.** Under guard §B's fail-safe this is a **level event, never a sizing event.** It would be that anyway: X1 is conjunctive and its wrapper half is closed.

### 2b. Decomposition of +14bp (266 [9/21] → 280 [9/24]). How much is rates, volatility, or credit-specific?

| component | bp | how measured | confidence |
|---|---|---|---|
| **Treasury leg of the HY all-in yield** | **≈+20** (the yield rose, not the spread) | HY effective yield `BAMLH0A0HYM2EY` **7.46 → 7.80 (+34bp)**, less OAS +14 | VERIFIED (arithmetic) |
| **Rates → spread, historical mechanical beta** | **≈ −2 to −5** (it should have TIGHTENED) | Model A: ΔHY on Δ^TNX, ΔVIX, SPY return; rates coefficient **−0.30bp per bp**; contributions −4.4 [9/23] and −1.4 [9/24] | VERIFIED (fit); INFERRED (causal) |
| **Equity-vol / risk-off** | **≈+3** | Model A: VIX **14.21 → 15.67**, VVIX 83.2 → 90.6, SPY −0.8% → ≈+0.5 (VIX) and ≈+3.2 (SPY) | VERIFIED (fit) |
| **European / developed-market common factor** | **≈+5 to +6, all on 9/24** | Model B: Euro HY **266 → 277 (+11)** on 9/24, coefficient 0.53 | VERIFIED (fit); single day |
| **Residual: US credit-specific, real-yield regime, supply** | **≈+8 to +10** | what is left; concentrated on 9/23 (+7.8 residual in model B) | INFERRED |

**What the residual most likely is (INFERRED, ranked):**
1. **A real-yield shock, not a growth shock.** DFII10 **2.62 → 2.76** (9/21→9/23) with breakevens flat (2.34 → 2.35 → 2.33). In this regime the historical sign flips: higher real yields raise refinancing costs, and CCC (the only tier with meaningful real-yield sensitivity, per BOND's Q4 side) takes the most. **This is the "rates-driven" share, but it runs THROUGH credit, not mechanically.**
2. **Supply (weakened by the §1d evidence).** SoftBank's record ~$11.1B USD+EUR HY deal priced **9/23** (9/24 per one outlet), the same day as the US-specific +5, alongside the CoreWeave-linked $1.1B data-center deal. **Both priced inside or within talk into >$20B of orders**, so there was no indigestion at the new-issue level. Some secondary-market cheapening to make room for ~$12B of AI supply remains plausible. **Its size is untestable from here.**
3. **The dealer warehouse is filling:** FR2004 below-IG corporates **+$2.2B over 4 weeks to 9/16, 96th percentile** (BOND, n=242), in the 13-month-to-5-year buckets. This fits dealers absorbing supply. **The next reads are Thu 10/1 (as-of 9/23) and 10/8.**

⚠️ **The model caveats travel with this table.** R² is 0.44–0.62, so roughly half of daily variance is idiosyncratic; the residual standard deviation is 4.4–5.3bp per day. The European HY close is a London close, which introduces timing noise. **The split is an order-of-magnitude attribution, not an accounting identity.**

### 2c. `LIQ-07` graded on the 9/24 cells
- **Trigger leg (B 15-session ≥ +28bp):** B 286 [9/24] − 276 [9/03] = **+10bp, 76.1st percentile. NOT MET.** CCC leg (15-session ≥0): **+61, met.** Count **0-of-3.**
- **Branch S3 (REVERSED, CCC−B 15-session ≤ −35):** CCC−B is **+51**. NOT MET.
- Required B for the next three observations (bases 9/04, 9/07 and 9/08 = 277 / 277 / 276): **≥305 / ≥305 / ≥304.** The earliest the trigger can fire is **obs 9/29**, and only if B widens another ~19bp and holds there. **Prior unchanged: P(S1 or S2) = 15%, P(S4) = 70%. Nothing today moves it** (one broad day does not make a B-led 15-session run).
- ⚠️ `LIQ-07` is graded on FRED **AS FIRST PUBLISHED**. These are latest-revised pulls. First-published and latest-revised can differ by a basis point.

---

## Q3 — THE RE-ARM PATH

| item | figure | basis / source |
|---|---|---|
| Sustain count (≥280 basis; RED owns the sustain ruling) | **1-of-3** on 9/24 | FRED; RED-FT-01 is the calm-side counter-signal (<280 s3). **Its exit is RED's to grade.** |
| Needed for s=3 | **9/25 cell ≥280 (pub Mon 9/28 ~16:15 ET) AND 9/28 cell ≥280 (pub Tue 9/29 ~16:15 ET)** | Under the strict ">280" letter: **≥281 on 9/24, 9/25 and 9/28**, and 9/24 already fails that (§BOTTOM LINE ⑦) |
| **My estimate for the 9/25 cell** | **+3bp ±5 (1σ) ⇒ ≈283, 68% range 278–288** | Two nowcasts: ΔHY on HYG return + Δ5Y (R²=0.50) and on JNK + Δ5Y (R²=0.53). Inputs at 13:05 ET: HYG **77.78 (−0.14%)**, JNK **93.53 (−0.16%)**, ^FVX **5.020 (−0.5bp)**. ⚠️ **They under-called 9/23 (0.8 vs +5) and 9/24 (2.6 vs +7): the index has been widening faster than the ETFs, so the error is skewed WIDER** |
| P(9/25 ≥280) | **≈70%** (≈65% for ≥281) | Nowcast distribution. Independently, **10 of 14 first touches of ≥280 since 2023-10 went on to three consecutive prints** |
| **What would falsify ≈283** | a **9/25 cell ≤278** | Or: HYG/JNK **closing positive** on 9/25 with ^FVX flat, i.e. the intraday softness reverses into the close |
| CDX HY | **9/23–9/25 SEARCH-NOT-FOUND**; baseline 306 [9/17] (single source) | No same-day index check is available, so the 9/25 estimate rests on the ETF tape alone |
| **Re-kill side** (`GATE-HY-REKILL`, strictly <260 on two consecutive published closes) | **−21bp** from 280 to ≤259, twice | A two-session drop of ≥21bp has happened in **2.2%** of windows (n=785); a 10-session drop in 13%. **2026 observations strictly below 260: ZERO.** `review_by` 9/30 |

---

## Q4 — BOOK IMPLICATIONS, stated and never traded

**The frame (L477 Q5 / TERRY Q1): the book is one oil bet at the price level.** Its single shared falsifier is scenario (b): *oil falls and takes yields and credit down with it.* In TERRY's measured quadrants, **(c), oil up and credit widening, is the book's best case.** **9/24 was a (c)-type day** (USO +2.9%, HYG −0.27%). **9/25 intraday is (a)-type** (USO −3.4%, ^TNX +2.8bp, credit flat to soft). The HY widening that happened was led by rates plus the European common factor. **That is not (b)**, and it does not test the book's falsifier in either direction.

⛔ **X1 sizing gate: CLOSED, and the 280 touch returns the DECIDED answer.** The wrapper half was adjudicated **NOT ARMED on 8/28** (BROCK, KB-BRK-219, `17d87df22`). An absolute BDC-mark card cannot grade a relative wrappers-lead-managers claim. **X1 does not fire on the index leg alone. Fail-safe DON'T-SIZE.** BROCK's pre-registered re-arm route (b), where the wrapper basket falls more than the manager basket while HY widens CCC-led, is BROCK's to grade today. **This file does not grade it.**

| line (TERRY map row) | registered rule | what the 280 touch does to it | what it does NOT do |
|---|---|---|---|
| **KRE Dec-18 60P ×5** (#6) | **NONE on file** | Nothing. No rule keys on HY. The bank leg is **absent** in the attribution (KRE −0.4% 9/22→9/24, **+1.1% on 9/25**) | Does not make this a bank-credit transmission event |
| **KRE Jan-15-2027 25P ×1** (#8) | **NONE** (lottery, 65% OTM) | Nothing | — |
| **TLT Sep-30 77P ×20** (#4, `TRY-FIRE-004`) | HOLD to 9/30 expiry · harvest ≥$0.3469 · **NO ADD (WQ-280)** | Nothing. The rule keys on the TLT price and the date | Does not unlock an add |
| **TLT Oct-16 82P ×2** (#5) | **NONE** | Nothing directly. The rates leg that drives it (real yields) is the same driver as the residual in §2b | — |
| **APO Dec-18 95P ×1** (#11) | **NONE** ("no ruling on file"); BROCK thesis vehicle | Nothing on my side. APO **120.69 [9/24]**, 121.16 [9/25 intraday], still below the $130 line (alts-crack co-trigger moot) | Does not arm X1's wrapper half. **BROCK's call** |
| **WAL Dec-18 70P ×1** (#9, `TRY-WAL-ROLL70`) | Exit proposal if WAL official close **≥$81.90 ×3** (REGINALD grades) · time stop Fri 12/4 | Nothing. WAL **76.26 [9/24c]**, 78.10 [9/25 intraday] | — |
| **USO 37 sh** (#1) | **NONE** (Will manages by hand) | Nothing | — |
| **VLO 1 sh held / 2 staged** (#2/2s) | held: NONE · staged: `GATE-TERRY-VLO-SCALE` (F1 = Nov HO×42−CL < $95 ⇒ stand-down) | Nothing. The staged gate keys on the crack spread | — |

**Net: no line in the book has a rule the 280 print can fire.** The one HY-keyed rule on the fleet surface that matters for capital is X1, and it is decided and closed.

---

## Q5 — WHAT TO WATCH Monday and Tuesday

| # | observable | level that matters | publishes | owner |
|---|---|---|---|---|
| 1 | **HY OAS 9/25 cell** (`BAMLH0A0HYM2`) | ≥280 ⇒ 2-of-3 · ≤278 falsifies my ≈283 · **≤259 = re-kill count opens** (remote) | **Mon 9/28 ~16:15 ET** | LIQUID (⚠️ `hy_oas_watch.py` runs at **13:00 ET**, before publication, so unattended it sees the 9/25 cell only on **Tue 9/29 13:00**) |
| 2 | **HY OAS 9/28 cell** | ≥280 ⇒ **3-of-3 = the sustain condition on the ≥ basis** (RED rules sustain; X1 still CLOSED) | **Tue 9/29 ~16:15 ET** | LIQUID · RED |
| 3 | **Single-B 15-session change** (`LIQ-07`) | **B ≥305 [9/25] / ≥305 [9/28] / ≥304 [9/29]** | same prints | LIQUID |
| 4 | **CCC and CCC−BB** | CCC **1,137** = window max [2025-04-07] · CCC−BB **948** = window max [9/24] | same prints | LIQUID |
| 5 | **The reversal test (guard test 3)** | on any HY retrace: **does CCC hold?** Yes ⇒ upgrade to substance | same prints | LIQUID |
| 6 | **Real yields** DFII10 / DGS10 | 10Y 5.19 [^TNX 9/25 intraday]. Further real-led moves are the §2b residual driver | H.15 daily ~16:15 ET | BOND · HENRY |
| 7 | **SOFR / SOFR99 − IORB** into quarter-end | SOFR99−IORB **+30bp** (GATE-LIQ-079 ARM; +6 [9/24]) · **the 9/30 turn itself is the NULL** | NY Fed ~08:00 ET daily | LIQUID |
| 8 | **Wrapper vs manager baskets** (X1 re-arm route b) | BROCK's letter | BROCK's packet (spawned today) | **BROCK** |
| 9 | **France OAT−Bund / UK gilts** (European common factor = ≈80% of 9/24) | OAT−Bund >100 (HANS-T-10 FIRED 9/24, 109.9) · gilts 10Y >5.50 (T-06) / 30Y >6.00 (T-13), ~11bp away [9/25] | HANS daily · France budget early October | **HANS** |
| 10 | **Oracle rating action** | Moody's Baa2 → Baa3 or Fitch → BBB− = **GATE-LIQ-069 R1 ⇒ 2-of-2** | unscheduled | LIQUID (VULCAN on info) |
| 11 | **HY primary / fund flows** | any deal pulled, postponed or downsized; weekly HY fund flows | LSEG Lipper Thursdays | WALTER intake → LIQUID (phrases proposed in the WQ-295 packet) |
| 12 | **FR2004 dealer below-IG inventory** | the 4-week build continues **and spreads into 5–10y** ⇒ BOND's (B) warning | **Thu 10/1** (as-of 9/23) | **BOND** |
| 13 | **VIX** | >23 (HENRY cascade) / >25 · today ~15.0 | live | HENRY · VIOLET |

---

## Inbox drain (logged per BOARD_CONSUMPTION_SPEC; detail in `board_log.tsv`)
- **HANS T-10 France compound FIRED 9/24 (+ WALTER `-001`, ACTION):** *acted.* The European transmission into US HY is **measurable and was large on the fire day.** European HY rose +11 on 9/24, and model B attributes ≈5.8bp of US HY's +7 to it. ⚠️ **HANS's own caveat carries:** ~11bp of the OAT's +19 was the Bund being SOLD (fiscal and duration pricing, not flight to quality). That is the same real-yield leg as the US one: **one global duration factor, not two independent confirmations.** **Funding transmission: NONE visible** in US overnight rates (SOFR−IORB −2, SOFR99−IORB +6, SRF $0.001B [9/24]). ⚠️ The EUR cross-currency basis (`HANS-T-12`) is **dark on both desks**, so "no funding transmission" is scoped to the gauges I observe.
- **WALTER `-003` (10Y >5% since 9/16, real-yield-led):** *acted.* This is the §2b residual driver.
- **WALTER `-005` (MF CMBS DQ 6.85%, not 7.12%):** *info-only.* No LIQUID figure cites it.
- **WALTER `-007` (Oracle financing loop):** *acted* (§1c). **R1 does not move.**
- **WALTER `-008` (BZ=F/RB=F roll artefacts):** *info-only.* Noted: USO's −3.4% today is the ETF's own print, not the continuous-contract roll.
- **WALTER `-010` (gilts ~11bp under HANS lines):** *noted.* Q5 row 9.
- **PROME WQ-295 (cadence + watch terms):** *acted.* `PROME/inbox/2026-09-25_from-LIQUID_cadence-and-watch-terms.md`: **CADENCE WEEKLY**, plus a primary-market phrase gap named.
- **WALTER `-011` (HY 280 "at the line, not over it"), arrived mid-session:** *acted.* I agree on the level. **CORRECTION sent** (`AGENTS/WALTER/inbox/2026-09-25_from-LIQUID_correction-SIG-W-20260925-011-…`): -011 carries *"arbiter CONTESTED as of 8/23 ⇒ GUARD-HELD-PENDING-ARBITER."* That is stale. The arbiter answered on 8/28 (NOT ARMED), and that state is **not active** (KILL_MEMO §D). ⚠️ **The source is my own unattended watcher**: `scripts/hy_oas_watch.py` L145/L151/L300–L302 hard-code the 8/23 text. **Repair OWED**, with acceptance conditions written in the packet: point to KILL_MEMO §D instead of restating a dated state · each side carries its own state · `--selftest` passes. An independent reader goes before it is called fixed (WQ-229, gate-alert surface).
- **PROME "your WATCH_FOR list is LIVE, R3 re-test", arrived mid-session:** *deferred.* PROME's own text says it waits for the next boot (due 10/02). Cadence (its ask 3) is already declared. The file is left in `inbox/` for the next boot.
- **Brightline Florida Chapter 11 (found by the web sweep, not on the BOARD):** signal → **WALTER for routing to CORAL** (`AGENTS/WALTER/inbox/2026-09-25_from-LIQUID_brightline-florida-ch11-for-CORAL.md`). Muni/project debt, not in the HY index.
- **BROCK's wrapper half:** no packet in my inbox at close. **I read its UNCOMMITTED working file** (`AGENTS/BROCK/research/2026-09-25_HY-280-touch_wrapper-half.md`, 13:1x ET). Verify at BROCK's commit before citing. **It agrees independently on the shape:** CCC/BB **compressed** 6.891 → 6.780 over 9/22→9/24 (= my proportional test 1, BB-led), and the **wrappers LAGGED** (wrapper basket −1.75% vs managers −3.23%; beta-adjusted +0.47%, 0.3σ). ⇒ **both legs of BROCK's 8/28 re-arm test (b) FAIL; X1 stays CLOSED.** ⚠️ **Separately, BROCK reports `GATE-BRK-R2` leg (a) FIRED:** North Haven Private Income Fund accepted ~43.8% of Q3 tenders (SC TO-I/A, 9/18), its 3rd consecutive sub-100% quarter. **BROCK's gate, BROCK's routing.** By R2's own letter it is *evidence for re-adjudication, not a re-arm* of X1. **This desk keeps no private-credit gate count** (retire-and-repoint, 9/12).
