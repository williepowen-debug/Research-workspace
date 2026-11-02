# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure. **Last session update:** 2026-11-02 ~09:4x ET — Will-directed file update and closeout (Claude Code `claude-opus-5-5`): position write-back, 10/29–10/30 data, 7Y audit grade, refunding bars frozen. **Last real data refresh: 2026-11-02.**

Frontiers: Treasury nominal/real **10/30** · ICE credit via FRED **10/29** · NY Fed repo **10/30** · FR2004 as-of **10/21** · ACM **10/29** · KW **10/23** · PMMS **10/29** · TreasuryDirect auctions through **10/29**. Evidence: `analysis/2026-11-02_update/` (raw manifest, grade transcripts). Bund not refreshed this session (last 3.43% [10/28], 10/29 file).

## Current judgment

**Long bonds recovered part of the FOMC sell-off into month-end.** After the 10/28 hawkish hold (two +25bp dissents), the curve bull-steepened: official Treasury 10/28→10/30, 2Y −11bp (4.56), 10Y −11 (4.94), 30Y −6 (5.31). 2s30s widened to 75bp. Real 10Y 2.60%, still above the 2.50 stress line. December hike pricing eased from about 87% [10/28] to about 76% [11/2 evolving vendor bar, not settlement].

**Auctions: still clearing; the refunding will grade on frozen bars.** The 10/29 7Y graded clean on audit (indirect 57.77% vs the 57.43% I′ bar, +0.34pp; dealers 9.41%; cover 2.46). The October month-end cluster ends with one audit-only I′ fire (the 10/26 2Y, record bid substitution) and two clean prints. **The refunding CUSIPs appeared on TreasuryDirect 11/2, before the 11/4 QRA, and the bars were frozen the same day** — so 3Y 11/9, 10Y 11/10 and 30Y 11/12 grade REGISTERED.

**Dealers paused after the record build.** FR2004 as-of 10/21: long-end $150.816B, −$0.580B w/w, off the 10/14 high. VX-BND-04 3→2 on the THESIS letter; disagreement recorded, because the dip is 0.4% and the 11–21Y bucket rose to its highest since as-of 9/23.

**Funding is firm at month-end, not stressed.** SOFR−IORB +4/+4/+5bp over 10/28–10/30 (SOFR 3.95%, 99th 4.03, record volume $3,175B); EFFR flat 3.88. Month-end-timed; LIQUID owns the verdict.

**Credit: the index is drifting back toward 350.** HY 314 [10/28] → 326 [10/29], 24bp under 350; CCC 1325, near its 3-year-window high (1356 [10/23]). IG 89. Below the 338–363 credit-equity band.

## Regime and capital record
<!-- bond-state: thesis=v1.2.12; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=MET-REC@2026-10-01; posture=FLAT@2026-10-30 -->
C-36 TWO-PART unchanged; THESIS v1.2.12 (WQ-536 RULED A 10/29). **Position FLAT since 10/30:** FORGE 10/30 reconcile shows TBT ×10 sold 10/30, no live TBT line; WQ-357 RESOLVED by Will 10/29. TLT82P sold 10/12. WQ280 NO-ADD stands; any new expression is a new TERRY card on Will's word. No trade executed or proposed by BOND; no expiry reminders (Will 10/20).

## Current dashboard

| Metric | Dated observation | Source / basis |
|---|---|---|
| Official 2Y/5Y/10Y/20Y/30Y | 4.56 / 4.71 / 4.94 / 5.34 / 5.31% [10/30]; daily −5/−7/−4/−1/−1bp | [CONF PRIMARY Treasury par CSV pulled 11/2] |
| Official real 5Y/10Y/30Y | 2.25 / 2.60 / 3.08% [10/30]; daily −6/−3/+1 | [CONF PRIMARY Treasury real CSV] |
| 10Y/30Y nominal−real | 2.34 / 2.23% [10/30] | [EST fitted-par subtraction; not pure breakevens] |
| 2s10s / 5s30s / 2s30s | 38 / 60 / 75bp [10/30] | [EST PRIMARY subtraction] |
| 20Y−30Y | +3bp [10/30]; 20Y still above 30Y | [EST PRIMARY] |
| 5Y5Y forward / 10Y breakeven | 2.22 / 2.34% [10/30] | [CONF MIRROR FRED T5YIFR/T10YIE]; 28bp below 2.50 |
| ACM 10Y TP / KW 10Y TP | 0.6645% [10/29] / 0.9358% [10/23] | [EST PRIMARY NY Fed / MIRROR FRED]; different models |
| Fed path | 12/9 meeting: +19.0bp priced ≈ 76% of a +25bp hike (in-month method, EFFR held 3.88); strip peak 4.470 Oct-2027 (+59.0bp) | [EST CBOT vendor bars, 11/2 evolving bar 09:13 ET, not settlement; HENRY owns] |
| HY/CCC/B/BB/BBB/IG OAS | 326 / 1325 / 332 / 194 / 110 / 89bp [10/29] | [CONF MIRROR-WALLED ICE via FRED] |
| HY distance to 350 | 24bp [10/29]; peak 340 [10/22] | [EST] |
| SOFR / EFFR / IORB | 3.95 / 3.88 / 3.90% [10/30]; SOFR 99th 4.03; volume $3,175B | [CONF PRIMARY NY Fed; IORB FRED] |
| SOFR−IORB | +5bp [10/30]; +4/+4/+5 over 10/28–10/30 | [EST]; LIQUID owns the verdict |
| FR2004 stock | Long-end $150.816B (−0.580); 11–21Y $62.699B (+2.953); >21Y $49.895B (−1.058); 3–6Y $47.986B (−1.402) [as-of 10/21] | [CONF PRIMARY NY Fed] |
| PMMS spread | 7.24% − Treasury 10Y 4.98% [both 10/29] = 226bp | [CONF PRIMARY; EST]; inside 180–230, not MBS OAS |
| Bund fitted 10Y | 3.43% [10/28] (not refreshed 11/2) | [CONF PRIMARY Bundesbank] |

## Auction grades since 10/20

| Date | Security | Indirect / direct / dealer % | BTC | Grade |
|---|---|---|---:|---|
| 10/21 | 20Y-R `912810UX4` | 58.16 / 31.59 / 10.26 | 2.73 | REGISTERED CLEAN; I′ bar 57.96 (+0.20pp) |
| 10/22 | 5Y TIPS `91282CRR4` | 62.04 / 32.44 / 5.53 | 2.41 | REGISTERED CLEAN; no I′ for TIPS |
| 10/26 | 2Y `91282CRU7` | **45.68 / 41.32** / 13.00 | 2.59 | AUDIT ONLY; I′ FIRE (bar 54.82, −9.14pp); OLD not fired |
| 10/27 | 5Y `91282CRT0` | 60.05 / 29.40 / 10.56 | 2.33 | AUDIT ONLY; clean (I′ +0.63pp) |
| 10/29 | 7Y `91282CRV5` | 57.77 / 32.82 / 9.41 | 2.46 | AUDIT ONLY; clean (I′ 57.43, +0.34pp; OLD and cover not fired) |

**Frozen 11/2 for the refunding** (n=12, published 2dp; OLD indirect-min / dealer-max · BTC-min · I′): 3Y `91282CRW3` 11/9: 56.50 / 19.50 · 2.54 · 57.44 — 10Y `91282CRX1` 11/10: 63.95 / 13.38 · 2.39 · 65.05 — 30Y `912810UY2` 11/12: 59.95 / 14.74 · 2.29 · 63.89. Files `registry/auction_bars/`; grade with `.venv` python (system python lacks numpy, so I′ is not computed there).

## Gates and derived statistics

| Existing gate | Dated state |
|---|---|
| Real 10Y ≥2.50 sustain | MET; Treasury 2.60 [10/30], 10bp through; trailing run 36 sessions (2026 Treasury real file) |
| OLD auction add re-arm | MET 9/23; add DECLINED WQ280; not met at any October print |
| WQ291 paired kill | MET-REC 10/1 (closed window); funding window UNGRADED; position now flat |
| Inflation anchoring | T5YIFR 2.22 [10/30], 28bp below 2.50 |
| HY marker / lead | HY 326 [10/29] >300; 24bp below 350; lead band 338–363 touched one session 10/22 |
| CCC escalation | 1325 [10/29] >1100; score 4 held |
| 30Y ≥5.00 | 98 of 209 2026 sessions, trailing run 82 [Treasury file through 10/30] |
| WQ400 Bund disorderly | NOT MET through 10/28; 0 of 14 prospective evaluations (not refreshed 11/2) |
| F2 buyback carrier | Six of six OFF-THE-RUN through 10/27; next op 11/4 10–20Y |

## Convergence Matrix

| # | Target /vector | Score | Status | Key evidence | Upgrade condition |
|---|---|---:|---|---|---|
| 1 | Long end / duration VX-BND-05 / VX-BND-12 / VX-BND-14 | 5 | 🔴🔴 | 30Y 5.31 [10/30], run 82; real 10Y 2.60 | Existing top score |
| 2 | Treasury auction health VX-BND-01 / VX-BND-08 / VX-BND-13 | 4 | 🔴 | Counter 3 (WQ-536 A); 7Y 10/29 clean on audit; refunding bars frozen | Second composition failure with a confirmed mechanism leg; downgrade graded after the 11/4 QRA |
| 3 | Dealer absorption VX-BND-04 / VX-BND-16 | 2 | 🟡 | As-of 10/21 −$0.580B, off the 10/14 high (was 3) | Two consecutive builds again; red = fresh long-end record + composition failure |
| 4 | HY function VX-BND-02 / VX-BND-11 | 3 | 🟠 | HY 326 [10/29]; CCC 1325 | HY >350 or verified pulled-deal cluster |
| 5 | IG function VX-BND-03 / VX-BND-10 | 1 | ⚪ | IG 89 / BBB 110 | IG 120 / failed syndication |
| 6 | CDX/cash VX-BND-06 | 1 | ⚪ | No fresh proxy run; true CDX gap | Confirmed fast-layer lead |
| 7 | Credit-equity VX-BND-07 | 2 | 🟡 | HY >300 and rising, +63 over trough; one-session red letter 10/22 reverted | Band held ≥2 sessions with VIX <20 at VIOLET's close |

**Composite 18/35 = 5+4+2+3+1+1+2 (was 19):** one 5, one 4, one 3, two 2, two 1. Dealer 3→2 on its letter. **Clean-auction counter = 3 (WQ-536 RULED A, Will 10/29):** the 10/26 2Y audit-only I′ fire is recorded beside it, not a reset; the 10/29 7Y audit-only clean neither advances nor resets it. Auction health stays 4 until BOND grades the downgrade after the 11/4 QRA. Rider: the downgrade would follow the weakest 2Y in BOND's records. Outside composite: VX-BND-15=2, VX-BND-17=1 (was 2), VX-BND-18=2, VX-BND-19=3, VX-BND-20=2.

## Exit / falsification

WQ157/WQ291 recommendation MET and, in fact, executed: the sleeve is flat (TBT sold 10/30). Funding window UNGRADED. Thesis falsifier 10Y<4.15 AND 30Y<5.00 for 3 sessions plus a clean refunding: not met (4.94 / 5.31 [10/30]). Convergence downgrade: counter letter MET 10/21, standing under WQ-536 A; graded after the 11/4 QRA. Position construction is TERRY's. **OPEN predictions: 0.** VX-BND-09 auction tails remain retired.

## Immediate Catalysts (same event set as docket/CATALYSTS.tsv)

| Date | Obligation |
|---|---|
| 11/2 | Treasury borrowing estimates 15:00 ET |
| 11/3 | JOLTS |
| 11/4 | 🔴 QRA: F1/F3 buyback flip conditions; sb0607 window expiry; coupon sizes; F2 op 10–20Y |
| 11/5 | Grade the convergence downgrade (auction health 4→3?) after the QRA · Productivity · FR2004 as-of 10/28 |
| 11/6 | October jobs |
| **11/9 · 11/10 · 11/12** | 🔴 **Refunding: 3Y `91282CRW3` · 10Y `91282CRX1` · 30Y `912810UY2` — registered grades on the 11/2 frozen bars** · FHLB Q3 11/9 · CPI 11/10 |
| 11/11–11/13 | VX-BND-20 review 11/11 · FRBNY FX report 11/13 |
| 11/18, 11/19 | 20Y new issue · 10Y TIPS reopening (bars freeze 11/12–11/17) |
| 12/1, 12/9 | Sovereign CDS retest · December FOMC + SEP |
| 2027-1/25, 1/27 | GPFG expert report · January FOMC |

## BOTTOM LINE

Long bonds won back part of their post-Fed losses into month-end, but yields stay high: the 30-year has closed at or above 5% for 82 straight sessions and real 10-year yields are still above 2.5%. Auctions keep clearing; the one weak October print (the 2-year) was a change in who bought, not a lack of buyers, and dealers stopped adding long bonds after a record week. BOND's short-duration trade is closed (TBT sold 10/30), so there is no live position on this thesis. The next real test is the November 9–12 refunding, and its pass/fail bars are already locked in.
