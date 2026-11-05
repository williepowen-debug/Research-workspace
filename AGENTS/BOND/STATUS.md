# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure. **Last session update:** 2026-11-05 09:56 ET — PROME catch-up under Will's 09:42 ET word (Claude Code `claude-opus-5-5`): November QRA read and graded, F2 carrier extended, auction-health downgrade graded, data refreshed. **Last real data refresh: 2026-11-05.**

Frontiers: Treasury nominal/real **11/4** · ICE credit via FRED **11/4** · NY Fed repo **11/4** · FR2004 as-of **10/21** (10/28 due today) · ACM **11/3** · KW **10/30** · PMMS **10/29** (11/5 due today) · Bund **11/5** · TreasuryDirect auctions through **10/29**. Evidence: `analysis/2026-11-05_catchup/` (raw manifest, Treasury documents).

## Current judgment

**The refunding brought no supply surprise now and a warning for later.** Treasury kept coupon sizes unchanged at every tenor for November–January (statement `sb0678`, 11/4). F3 NOT FIRED. But it dropped two words: August said sizes hold "for **at least** the next several quarters", November says "for the next several quarters". TBAC, its dealer advisory committee, says coupon increases will be warranted later in FY27, likely the second half, mostly in 2Y–10Y, with real debate over the 20Y and 30Y. On 11/4 the 10Y fell 5bp and the 30Y 4bp; no attribution computed.

**The buyback step-up became standing, but F1 did not fire.** Long-end operations stay at $6B each, the same two buckets, 8 ops next quarter vs 9 last. Guided liquidity support rose from up to $38B to up to $70B; realized 8/5–11/4 was $55.88B. That rise is the 8/19 step carried for a full quarter. The sb0607 reading stands: liquidity support on the letter, not YCC. ⚠️ One of the four grounds for rejecting YCC weakened: the dated window. The step-up outlived it; it stays capped with no yield target. ⚠️ F1 has no number, so this is a judgement. Treasury also says it is evaluating larger maximum purchases; next read 2/3/2027.

**Credit moved first, broadened, and eased on 11/4.** HY jumped to 344 on 10/30, held 343 / 340, then 332 [11/4], 18bp under 350 and back below the 338 band. The credit-equity upgrade was not met. On 10/30 the widening was in the better tiers: B +28bp, BB +15, CCC +2. B's 15-session change was +45bp to 11/3 (97th percentile of 383 rolling windows since 2025-05) and +22bp to 11/4 (83rd of 384). LIQUID owns that verdict: BROADENS through 11/3, REVERSES on the 11/4 print, one print with levels still wide. Its formal test LIQ-07 resolved 10/16 as ordinary repricing, no reserve-channel loop observed. B's sensitivity to real yields never reached its +0.49 trigger; October widening came on days real yields fell (KB-BND-542). ⚠️ 10/30 is month-end, so an index rebalance is an untested part of that one-day move. The "only a few names" story for CCC no longer covers September–October. No funding restriction is established: SOFR−IORB +4bp [11/4].

**New issuance went quiet in October, and this week may be reopening.** About $15B in October, the second-slowest month of 2026, averaging $3.5B a week over the last four, after $17B+ and $14B weeks in late September (Bloomberg via CAM, KB-BND-540). The words are borrowers "on the sidelines"; no pulled deal appears in any source I can reach. EDGAR filers pricing notes fell from 19 to 2, then 18 so far this week. ⚠️ That count mixes investment grade with high yield and misses private deals. Pulled deals are not observable from free sources.

**Auctions: downgrade graded, refunding next.** Three clean registered nominals under WQ-536 A and no size change, so auction health moves 4→3. ⚠️ The downgrade follows the weakest 2Y in BOND's records (10/26, audit-only, recorded beside the count). The refunding prints grade REGISTERED on bars frozen 11/2, and a fire there resets the counter.

**Rates:** curve flattened 5bp since 10/30: 2Y 4.58, 10Y 4.90, 30Y 5.28 [11/4]. Real 10Y 2.64%, run 39 sessions at or above 2.50. December hike about 82% [11/5 evolving vendor bar, not settlement; HENRY owns], up from about 76% [11/2].

## Regime and capital record
<!-- bond-state: thesis=v1.2.13; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=MET-REC@2026-10-01; posture=FLAT@2026-10-30 -->
C-36 TWO-PART unchanged; THESIS v1.2.13 (F1/F3 graded, auction health 3). **Position FLAT since 10/30:** FORGE 10/30 reconcile shows TBT ×10 sold 10/30. ⚠️ Book truth: the last broker capture is 10/30 intraday and FORGE is a stale mirror. WQ280 NO-ADD stands. **WQ-592 TLT 82/78 put spreads RULED B (declined) 11/4 on TBAC's table; Treasury's own statement now confirms it: 10Y $42B and 30Y $25B equal August, no same-tenor increase.** Any new expression is a new TERRY card on Will's word. No trade executed or proposed by BOND; no expiry reminders (Will 10/20).

## Current dashboard

| Metric | Dated observation | Source / basis |
|---|---|---|
| Official 2Y/5Y/10Y/20Y/30Y | 4.58 / 4.69 / 4.90 / 5.30 / 5.28% [11/4]; daily −3/−5/−5/−5/−4bp | [CONF PRIMARY Treasury par CSV pulled 11/5] |
| Official real 5Y/10Y/30Y | 2.39 / 2.64 / 3.08% [11/4]; daily +4/−1/−1 | [CONF PRIMARY Treasury real CSV] |
| 10Y/30Y nominal−real | 2.26 / 2.20% [11/4] | [EST fitted-par subtraction; not pure breakevens] |
| 2s10s / 5s30s / 2s30s | 32 / 59 / 70bp [11/4] | [EST PRIMARY subtraction] |
| 20Y−30Y | +2bp [11/4]; 20Y still above 30Y | [EST PRIMARY] |
| 5Y5Y forward / 10Y breakeven | 2.22 / 2.26% [11/4] | [CONF MIRROR FRED T5YIFR/T10YIE]; 28bp below 2.50 |
| ACM 10Y TP / KW 10Y TP | 0.6773% [11/3] / 0.9089% [10/30] | [EST PRIMARY NY Fed / MIRROR FRED]; different models |
| Fed path | 12/9 meeting: +20.4bp priced ≈ 82% of a +25bp hike (in-month method, EFFR held 3.88); strip peak 4.500 Oct-2027 (+62.0bp) | [EST CBOT vendor bars, 11/5 evolving bar 09:40 ET, not settlement; HENRY owns] |
| HY/CCC/B/BB/BBB/IG OAS | 332 / 1297 / 351 / 199 / 113 / 91bp [11/4] | [CONF MIRROR-WALLED ICE via FRED] |
| HY primary | October ≈$15B; $3.5B a week final four; EDGAR filers 18 so far week of 11/2 | [EST secondary, Bloomberg via CAM; EDGAR mixed IG/HY]; pulled deals not observable |
| HY distance to 350 | 18bp [11/4]; 344 [10/30], 343 [11/2], 340 [11/3] | [EST] |
| SOFR / EFFR / IORB | 3.94 / 3.88 / 3.90% [11/4]; volume $3,207B | [CONF PRIMARY NY Fed; IORB FRED] |
| SOFR−IORB | +4bp [11/4]; +5/+7 on 11/2, 11/3 | [EST]; LIQUID owns the verdict |
| FR2004 stock | Long-end $150.816B (−0.580); 11–21Y $62.699B (+2.953); >21Y $49.895B (−1.058); 3–6Y $47.986B (−1.402) [as-of 10/21] | [CONF PRIMARY NY Fed] |
| PMMS spread | 7.24% − Treasury 10Y 4.98% [both 10/29] = 226bp | [CONF PRIMARY; EST]; inside 180–230, not MBS OAS |
| Bund fitted 10Y | 3.33% [11/5], 3.38 [11/4] | [CONF PRIMARY Bundesbank] |
| HYG/IEF proxy | 0.8440 [11/5], 5th percentile of 3 months, z20 −1.04 | [EST vendor bars; true CDX unobserved] |
| Borrowing / cash | $618B Oct–Dec, $800B Jan–Mar; TGA $850B end-Dec, peak up to $1.025T ± $50B | [CONF PRIMARY Treasury sb0675, sb0678]; LIQUID owns TGA |

## Auction grades since 10/20

| Date | Security | Indirect / direct / dealer % | BTC | Grade |
|---|---|---|---:|---|
| 10/21 | 20Y-R `912810UX4` | 58.16 / 31.59 / 10.26 | 2.73 | REGISTERED CLEAN; I′ bar 57.96 (+0.20pp) |
| 10/22 | 5Y TIPS `91282CRR4` | 62.04 / 32.44 / 5.53 | 2.41 | REGISTERED CLEAN; no I′ for TIPS |
| 10/26 | 2Y `91282CRU7` | **45.68 / 41.32** / 13.00 | 2.59 | AUDIT ONLY; I′ FIRE (bar 54.82, −9.14pp); OLD not fired |
| 10/27 | 5Y `91282CRT0` | 60.05 / 29.40 / 10.56 | 2.33 | AUDIT ONLY; clean (I′ +0.63pp) |
| 10/29 | 7Y `91282CRV5` | 57.77 / 32.82 / 9.41 | 2.46 | AUDIT ONLY; clean (I′ 57.43, +0.34pp; OLD and cover not fired) |

**Frozen 11/2 for the refunding** (n=12, published 2dp; OLD indirect-min / dealer-max · BTC-min · I′): 3Y `91282CRW3` 11/9 $58B: 56.50 / 19.50 · 2.54 · 57.44 — 10Y `91282CRX1` 11/10 $42B: 63.95 / 13.38 · 2.39 · 65.05 — 30Y `912810UY2` 11/12 $25B: 59.95 / 14.74 · 2.29 · 63.89. Files `registry/auction_bars/`; grade with `.venv` python (system python lacks numpy, so I′ is not computed there). ⚠️ After a print, a PRE-PRINT line means not graded, whatever the rc; one blank Yes/No on any coupon row refuses the run (L859 read 2).

## Gates and derived statistics

| Existing gate | Dated state |
|---|---|
| Real 10Y ≥2.50 sustain | MET; Treasury 2.64 [11/4], 14bp through; trailing run 39 sessions (2026 Treasury real file) |
| OLD auction add re-arm | MET 9/23; add DECLINED WQ280; not met at any October print |
| WQ291 paired kill | MET-REC 10/1 (closed window); funding window UNGRADED; position now flat |
| Inflation anchoring | T5YIFR 2.22 [11/4], 28bp below 2.50 |
| HY marker / lead | HY 332 [11/4] >300; 18bp below 350; band 338–363 held 10/30, 11/2, 11/3, left 11/4 |
| Credit-equity upgrade (band ≥2 sessions, VIX <20) | NOT MET: one band session under VIX 20 (10/30); HY 332 on 11/4 left the band as VIX fell to 16.61 |
| CCC escalation | 1297 [11/4] >1100; score 4 held |
| 30Y ≥5.00 | 101 of 212 2026 sessions, trailing run 85 [Treasury file through 11/4] |
| WQ400 Bund disorderly | NOT MET through 11/5; 0 of 20 prospective evaluations (five-session changes −2/+1/−6/−4/−5/−9bp) |
| F2 buyback carrier | Seven of seven OFF-THE-RUN through 11/4; next op 11/17 20–30Y; carrier runs to 2/9/2027 |
| F1 / F3 | NOT FIRED at the 11/4 QRA (KB-BND-528); next read 2/3/2027 |

## Convergence Matrix

| # | Target /vector | Score | Status | Key evidence | Upgrade condition |
|---|---|---:|---|---|---|
| 1 | Long end / duration VX-BND-05 / VX-BND-12 / VX-BND-14 | 5 | 🔴🔴 | 30Y 5.28 [11/4], run 85; real 10Y 2.64 | Existing top score |
| 2 | Treasury auction health VX-BND-01 / VX-BND-08 / VX-BND-13 | 3 | 🟠 | Downgraded 4→3 on 11/5: counter 3, QRA no size change | A registered composition fire resets the counter; second composition failure with a confirmed mechanism leg |
| 3 | Dealer absorption VX-BND-04 / VX-BND-16 | 2 | 🟡 | As-of 10/21 −$0.580B, off the 10/14 high; 10/28 due today | Two consecutive builds again; red = fresh long-end record + composition failure |
| 4 | HY function VX-BND-02 / VX-BND-11 | 3 | 🟠 | HY 332 [11/4]; CCC 1297; B +22bp over 15 sessions [11/4] | HY >350 or verified pulled-deal cluster |
| 5 | IG function VX-BND-03 / VX-BND-10 | 1 | ⚪ | IG 91 / BBB 113 | IG 120 / failed syndication |
| 6 | CDX/cash VX-BND-06 | 1 | ⚪ | Proxy 5th percentile of 3 months; true CDX gap | Confirmed fast-layer lead |
| 7 | Credit-equity VX-BND-07 | 2 | 🟡 | HY left the band 11/4 at 332; upgrade not met | Band held ≥2 sessions with VIX <20 at VIOLET's close |

**Composite 17/35 = 5+3+2+3+1+1+2 (was 18):** one 5, two 3, two 2, two 1. Auction health 4→3 on its letter. **Clean-auction counter = 3 (WQ-536 RULED A, Will 10/29):** the 10/26 2Y audit-only I′ fire is recorded beside it. Rider: the downgrade follows the weakest 2Y in BOND's records. Outside composite: VX-BND-15=2, VX-BND-16=4, VX-BND-17=1, VX-BND-18=2, VX-BND-19=3, VX-BND-20=2.

## Exit / falsification

WQ157/WQ291 recommendation MET and, in fact, executed: the sleeve is flat (TBT sold 10/30). Funding window UNGRADED. Thesis falsifier 10Y<4.15 AND 30Y<5.00 for 3 sessions plus a clean refunding: not met (4.90 / 5.28 [11/4]). Convergence downgrade: applied 11/5. Position construction is TERRY's. **OPEN predictions: 1.** BND-33: at least one refunding auction fires I′, 50%, base rate 5 of 11. VX-BND-09 auction tails remain retired.

## Immediate Catalysts (same event set as docket/CATALYSTS.tsv)

| Date | Obligation |
|---|---|
| 11/5 | FR2004 as-of 10/28 · PMMS |
| 11/6 | October jobs · HY primary weekly count |
| **11/9 · 11/10 · 11/12** | 🔴 **Refunding: 3Y `91282CRW3` · 10Y `91282CRX1` · 30Y `912810UY2` — registered grades on the 11/2 frozen bars** · CPI 11/10 |
| 11/11, 11/12, 11/13 | VX-BND-20 review 11/11 · BND-33 resolves at the 30Y grade 11/12 · FHLB Combined Financial Report 11/13 (REGINALD calendar) · FRBNY FX report 11/13 |
| 11/17 | F2 op 20–30Y |
| 11/18, 11/19 | 20Y new issue $16B · 10Y TIPS reopening $19B (bars freeze 11/12–11/17) |
| 11/19 | Freeze bars for the month-end cluster |
| 11/23, 11/24, 11/25 | 2Y $69B · 5Y $70B and FRN reopening $28B · 7Y $44B |
| 12/1, 12/7, 12/9 | Sovereign CDS retest · December coupons begin · December FOMC + SEP |
| 2027-1/25, 1/27, 2/3 | GPFG expert report · January FOMC · February QRA |
| 2027-03 | 7Y converts to quarterly new issue |

## BOTTOM LINE

Treasury left auction sizes alone but dropped "at least" from its promise, and its advisers expect bigger auctions in the second half of FY27, so the supply story is delayed rather than gone. Buybacks did not ratchet again, though the larger size now runs past its original end date. The thing that moved is credit: junk spreads pulled back to 18bp from 350 on 11/4 after three sessions in the warning band, though the widening had spread beyond the weakest names, with no funding strain shown yet. New issuance slowed sharply in October and may be reopening this week. BOND has no position on this thesis; the November 9–12 refunding is the next real test, on bars locked since November 2.
