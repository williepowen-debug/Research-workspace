# LIQUID — Calendar & Data Releases

**Last Updated:** 2026-07-01 Wed (quarter-end roll: May PCE + late-June auctions → Resolved; NFP 7/2 + late-July auctions added; FOMC dates confirmed; 7/3 = July-4 observed holiday)

> **Source-of-truth pairing:** `workbook/CATALYSTS.tsv` is the machine-readable forward-event docket (dated rows, consumed by the boot countdown). **This human calendar is its twin — they must not diverge in the *event set*.** When you add or resolve a dated catalyst, update both. Rolling daily watches (HY-OAS direction, 30Y <4.90 unwind, USD/JPY, SOFR-IORB) are NOT dated catalysts — they live in STATUS danger windows + `scripts/boot.py`, not CATALYSTS.tsv.

---

## This Week (Jun 29 – Jul 3, 2026) — ⚠️ Fri Jul 3 = July-4 OBSERVED market holiday

| Date | Event | Signal Threshold | Who Cares |
|------|-------|-----------------|-----------|
| **Thu Jul 2, 8:30 ET** | **June NFP** (moved up for the holiday) | KB-LIQ-060 residue: the duration leg re-fires on a **GROWTH break**, not hawkishness. Weak print = growth-break candidate (long-end rally extends); hot print = hike pricing firms (front-end). May was +172k / 4.3% | LIQUID, HENRY, LABOR, BOND |
| **Thu Jul 2 close** | **2nd alt-mgr PE-wrapper gate watch — window effectively closes** (30d from the Jun 3-4 BCRED/Partners Group origin; 7/3 is the holiday) | Through 7/1: **CLEAN at the letter** (EDGAR-FTS: zero PE-wrapper proration filings; BXPE +$1.2B subs). Retroactive-conversion risk via July pubs (see ~Jul 31 row) | BROCK, LIQUID, REGINALD |
| **Thu Jul 2, ~4:30pm ET** | **H.4.1 (as-of Wed 7/1)** | WRESBAL drain rate after the **−$82B week → $2.9514T (as-of 6/24), first sub-$3T; cushion ~$151B** (KB-LIQ-067). <$2.8T = PROME 🟠 (canonical WRESBAL) | LIQUID, PROME, REGINALD |
| Daily | **HY OAS direction** | 275 [boot 7/1, latest FRED print] — **X1 approach band, 5bps to the >280 LIQUID half**; <260 = soft-kill (re-arms only on 2 fresh sub-265 closes); >320 = confirmation. CCC-BB 806 (pin — falsifier <400) | LIQUID |
| Daily | **Duration** | 30Y 4.91 (0.01 above the 4.90 unwind); 10Y on the 4.50 pivot; NFP is the growth-break test | LIQUID, BOND |
| Daily | **Alts/PC + vol** | APO $118 (alts-crack DEEPENING); BIZD $12.54 (line $12.50) | LIQUID, HENRY |
| Daily | **SOFR-IORB / RRP quarter-end** | +3bps ABOVE ceiling on the Q-end turn print — KB-LIQ-051 pattern says mechanical; needs 3+ sessions to be structural. RRP sustained >$10B into July = real re-activation | LIQUID |
| Daily | USD/JPY >160 | 162.49 triggered on level (repat = Sep tail; SAM 6/30: lifer→UST channel RETIRED, conditional watch only) | LIQUID, SAM |

## Later (2026)

| Date | Event | Signal Threshold | Who Cares |
|------|-------|-----------------|-----------|
| **~Jul 16** | **June TIC** (May flows) | Belgium proxy →$500B = 🟠 SAM/PROME; Japan >$20B single-month sell = SAM route (KB-LIQ-031). April: official +$49.2B carried a private −$23.1B outflow; Belgium unconfirmed | LIQUID, SAM |
| **~Jul 25** | **Q2 BDC marks** (FSK, OBDC) | **NEXUS-named credit-bifurcation transmission test** — CDLI-FSK gap / CCC-BB / mark catch-down. The bear book's load-bearing falsifier-or-confirm | BROCK, LIQUID, NEXUS |
| **~Jul 27 (modeled)** | **Late-July Treasury auctions** (2Y/5Y/7Y) | **2Y indirect is the watch** — June cycle: 2Y 55.45% (0.45pp above the <55% line, closest approach), 5Y 61.6%, 7Y 57.6%; all cleared, directs absorbed the step-down. Sustained <55% = FOI demand-hole confirm | LIQUID, BOND |
| **Jul 28-29 (CONFIRMED)** | **July FOMC — hike watch** | July-hike only ~23% (the ~75% was P(hold), transposed — ORACLE 6/22); hike seen landing Q4 (Oct-modal ~53%, hike-by-YE ~61%), consistent with 9/18 dots. Retests KB-LIQ-060 | LIQUID, HENRY, ALL |
| **~Jul 31** | **Q2 PE/PC tender publications** (retroactive 2nd-gate resolver) | Ares PMF Q2 results (expired 6/29) · Partners Group US ~$16B fund confirm (~6% vs 5% cap — same manager, not a 2nd-manager fire) · Blue Owl OCIC/OTIC Q2 · BCRED final proration. A 2nd-MANAGER gate here = contagion confirm 🟠 | BROCK, LIQUID, REGINALD |
| Late Jul / Aug (~8/14) | Q2 10-Q cycle (broader BDC marks) | NA reversal vs compounding; div-cut cascade | BROCK, LIQUID |
| **~YE2026** | **Warsh Balance-Sheet Policy review outcome** | QT pace / SRF / RRP / long-run SOMA "back in play" — Leg A future buffers (thinner). Standing multi-quarter monitor | LIQUID, REGINALD, ALL |

---

## Resolved (rolling archive)

| Date | Event | Outcome |
|------|-------|---------|
| Jun 30 → graded 7/1 | **LIQ-03 resolves (CLO AAA vs SOFR+160)** | **ACHIEVED at the letter, TAIL-FORM:** PC/MM senior AAA printed through 160 in Mar-Apr (Diameter S+170/185, SEC 8-Ks primary; like-for-like 149→170 in a month) while **benchmark BSL AAA never exceeded ~S+125 avg** (April peak) and ended June ~120-125 tightening. Within-AAA bifurcation → KB-LIQ-065; successor LIQ-04 (BSL avg >150, H2, 25%). Adversarial verify flipped the initial MISS |
| Jun 30 (finals → July) | **BCRED Q2 redemption window** | Window closed 6/30; ~10% requests vs 5% cap → ~50% expected fill, **final proration publishes July** (→ ~Jul 31 row). July distribution CUT −10% ($0.20→$0.18, 8-K 6/22); NAV $23.94/sh, $45.3B aggregate 5/31. No hard gate |
| ~Jun 30 | **Cliffwater CDLI Q1** | **NO Q1/Q2-2026 print found as of 7/1** — latest official release remains CY2025 (+9.3%, 3/31). CCLFX interval fund (adjacent): Q2 cap CUT 7%→5% vs ~17% requests. CDLI-FSK gap test rolls to the ~7/25 BDC-marks row |
| Jun 25-26 | **May PCE** | **HOT, accelerating: core +0.31% MoM / 3.42% YoY (from ~3.35%); headline +0.46% MoM / 4.03% YoY** (computed from FRED PCEPILFE/PCEPI index levels, 1-dp rounding, pulled 7/1). HEN-34 soft-core gate did NOT open — higher-for-longer / hike pricing supported; consistent with the hot May CPI |
| Jun 23-25 | **Late-June 2Y/5Y/7Y auctions** | **ALL CLEARED, no fire — but a broad indirect STEP-DOWN from the strong May cycle:** 2Y 6/23 indirect **55.45%** (0.45pp above the <55 line, closest approach; direct 34.3% absorbed, dealer only 10.2%, BTC 2.64); 5Y 6/24 **61.6%** (−13.3pp vs May, BTC 2.35 soft-middle); 7Y 6/25 **57.55%** (−20.9pp vs May, BTC 2.50). Read: softer foreign/investment-fund bid with directs absorbing — NOT a buyers' strike. Accepted basis, FiscalData API (7/1). The "5Y tailed 0.7bp, 8th straight" wire claim = UNVERIFIABLE from public primary — dealer-screen color, don't cite as fact. Watch 2Y late-July |
| Jun 24 | **EIA WPSR — Cushing** | Occurred 6/24 — Cushing / WTI delivery-dislocation read owned by HAWK/BRENT (Boundary #3 routing). LIQUID basis/calendar-spread angle only; no LIQUID-domain trip |
| Jun 24 | **BOJ Summary of Opinions** | Occurred 6/24 — hike-rationale / next-hike-cadence read owned by SAM. LIQUID tracks the Japan-UST/repat leg (armed-but-unfired; carry window LOCKED Sep-18) |
| Jun 22 | **HY OAS 6/18-6/19 prints (TRIGGER-A resolver)** | **RESOLVED BENIGN.** 263(6/17)→266(6/18)→266(6/19)→265(6/22) — the 263 was a one-print low; TRIGGER A (<265 ×2) never fired. Soft-kill threat receded, cushion 5bps stable. CCC-BB WIDENED to 791 (pin firming). → KB-LIQ-061 candidate |
| Jun 22 | **Brent Hormuz decoupling test** | **PASSED — shrug.** Iran's 6/20 re-closure was declaratory/non-kinetic; Brent fell to $77.90 (lowest since early March), curve flipped to contango. US Treasury 60-day Iran-crude license 6/22 = disinflationary. Decoupling holds (HAWK/BRENT) |
| Jun 22 | **CFTC JPY COT** (Juneteenth-delayed) | Net −150,132 (83.4% of peak); HELD through the BOJ hike, no cover. But carry window now LOCKED to Sep-18 (a Sep convexity tail, not near-term). No intervention (MOF silent 6d). SAM-domain |
| Jun 17 | **June FOMC (Warsh debut)** | **HAWKISH HOLD 3.50-3.75% unanimous 12-0.** Dots flipped hike-leaning (2026 median +~35-40bps to ~3.80%; 9/18 hike by YE; 17/18 upside inflation risk). Statement 341→130 words; "ample reserves" reaffirmed; no QT paragraph. **5 review task forces incl. Balance-Sheet Policy.** Bear-flattener: 2Y +16bps (4.18-4.22), 30Y −2 (4.90-4.93), DXY 1yr highs. Integrated 6/20 → KB-LIQ-060 authored (duration-transmission inversion) |
| Jun 18 | **May TIC (April flows)** | **Total net +$26.1B; LT +$206.0B (private LT +$164.4B / official +$41.6B); broad private −$23.1B OUTFLOW, official +$49.2B offset.** Official FOI bid carried a private-outflow month. Japan UST $1.210T↓, China $651B, UK $938B↑. Belgium unconfirmed. Touches Leg B kill (1 of 2 prints). Routed ACTION → BOND |
| Jun 18 | **5Y TIPS reopening (91282CQP9)** | **STRONG: indirect 68.6%, dealer 3.4%, BTC 2.61, real HY 1.955%.** Accepted basis, Treasury fiscal-data API |
| Jun 16 | **20Y reopening (912810UV8)** | **STRONG: indirect 71.6%, dealer 8.5%, BTC 2.75, HY 4.927%.** Long-end demand FIRMED vs soft 6/11 30Y (59.9%). Accepted basis |
| Jun 16 | **BOJ policy** | **Hiked to 1.00% as-priced.** No carry unwind (buy-rumor-sell-fact); USD/JPY stayed >160 (rate-differential, not repat). SAM-domain |
| Jun 19 | June monthly opex | No live LIQUID decisions; HYG $75P expired worthless as planned (written off 6/13), TEN closed prior |
| Jun 11 | **30Y reopening ($22B, 912810UU0)** | **SOFT-but-cleared: BTC 2.33, indirect 59.9% (vs 66.6% May), dealer 14.7% (elevated), high 5.020%.** Market rallied 7bps post-auction (30Y closed 4.951 — first sub-5 close since 6/4). TreasuryDirect, integrated 6/12 |
| Jun 10 | **10Y reopening ($39B, 91282CQQ7)** | **STRONG: BTC 2.57, indirect 78.2%, dealer 9.5%, high 4.538%.** Belly demand robust — corroborates KB-LIQ-057 (demand shows at price) |
| Jun 9 | 3Y note auction | BTC 2.64 — functional |
| Jun 11 | Initial jobless claims (wk 6/6) | **229k** — below 250k threshold but 4th straight weekly rise (210k wk-5/16 → 212k → 225k → 229k wk-6/6) |
| Jun 10 | **May CPI** | **HOT: headline +0.48% MoM / 4.18% YoY (accel from 3.78%); core +0.21% MoM / 2.81% YoY** (FRED CPIAUCSL/CPILFESL). VIX spiked 22.22 intraday. Lagged energy passthrough landed despite Brent collapse; constrains Fed into 6/17 FOMC |
| May 28 | April PCE (was ⚠️ pending) | **Headline 3.72% YoY (accel from 3.57%), core 3.27% (from 3.19%); MoM +0.38%/+0.23%** — hot-ish, predates the hot May CPI (integrated 6/12) |
| Jun 5 → resolved here | May NFP (was ⚠️ pending) | **+172k (PAYEMS), UNRATE 4.3% flat** — solid, mildly decelerating (Apr +179k, Mar +214k); contrasts the claims creep (integrated 6/12) |
| May 28 | 7Y note auction | BTC 2.52, **indirect 78.4%, dealer 10.4%** (TreasuryDirect, accepted basis — integrated 6/12) |
| May 27 | 5Y note auction | BTC 2.34 (soft side), **indirect 74.9%, dealer 12.8%** |
| May 26 | 2Y note auction | BTC 2.64, **indirect 57.6%, dealer 12.3%** |
| May 21 | ~~10Y reopening (Leg 2 gate)~~ **MISLABELED — was the 10Y TIPS reopening** (91282CPU9, `type: TIPS`, high 2.169% REAL; BTC 2.52, indirect 61.4%). Not a nominal Leg-B test; different buyer base. The actual nominal corroboration arrived 6/10 (10Y reopen, indirect 78.2% — KB-LIQ-057 corroborated) | **RESOLVED 6/12** — verify-security-type pattern (term field collapses TIPS/nominal) |
| May 20 | 20Y auction ($16B reopening) | **Soft-but-functional, no orange:** BTC 2.55 / indirect 67.7% STRONG / tail 0bp / dealer 9.4% → KB-LIQ-057 (term-premium digestion, not broken mechanism) |
| May 17 | HY OAS tightest of cycle: 276 (16bps cushion above 260 kill) | Did not breach; +4bps on 5/18 |
| May 16 | WALTER sweep: 2nd US bank failure 2026 (Georgia), Barr "PC could trigger larger credit issues" | Stage 3 convergent-narrative recognition continues (KB-LIQ-040 trajectory) |
| May 14 | Will/Prome signals: gamma momentum factor squeeze; 30Y tagged 5.046% (first since 2007) | Gamma suppression hypothesis live; duration regime break confirmed |
| May 9 | Will image-batch: BlackRock APAC PC default, debt/GDP > 1, multiple Stage 3 confirms | All processed in `BATCH_INTEGRATION_2026-05-18.md` |
| ~~May 5~~ **May 13** | **30Y new-issue auction (912810UU0) stopped 5.0460%** — first 5%+ stop since 2007; BTC 2.30, indirect 66.6% (accepted basis), dealer 11.7% — level signal, not dysfunction | **Date CORRECTED 6/12** (TreasuryDirect: no auction of any kind on 5/5; row had conflated the auction with the level story — 30Y first closed >5% on 5/4 at 5.025 (CBOE), dipped back under 5/5–5/11, durably above from 5/12) |
| Apr 17–21 | SOFR/IORB confirmation window | **RESOLVED MECHANICAL** — SOFR normalized to 3.55%, SOFR-IORB re-flipped to -10bps. Apr 15 +7bps breach was tax-day TGA build, not structural leak. KB-LIQ-051; playbook archived. |
| Apr 22 | OZK Q1 earnings | (see REGINALD/OZK STATUS) |
| Apr 21 | WAL Q1 earnings | (see REGINALD STATUS) |
| Apr 16 | Bank earnings day 1 (C/BAC/WFC/BLK/KRE/WAL) | Muted — WAL -1.55%, no credit crack |
| Apr 14 | March PPI / IMF GFSR | PPI core-core +0.2% MoM decelerating; IMF formal liquidity-facility call (PC/NBFIs named) |
| Apr 10 | March CPI / UMich | CPI 3.28% YoY; UMich 47.6 record low |
| Apr 2–3 | SOFR Q-end normalization | PASSED — 3.62%, no structural leak |
| Mar 19 | 20Y auction | Strong: BTC 2.76x, indirect 69.0% |

---

*For longer-tail historical events see `archive/` and git history.*
