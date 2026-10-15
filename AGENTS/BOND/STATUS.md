# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure. **Last session update:** 2026-10-15 15:18 ET (standard closeout). **Last real data refresh: 2026-10-15.** Claude Code / Opus 5.5 (claude-opus-5-5), Will-launched boot.

Frontiers: official Treasury curve **10/14** · ICE credit (FRED) **10/14** · NY Fed repo **10/14** · FR2004 as-of **9/30** (next weekly as-of publishes 10/15 ~16:15 ET) · vendor intraday **10/15 13:35–13:50 ET**. Evidence: `analysis/2026-10-15_post-PPI/REPORT.md` + `raw/`. Prior day: `analysis/2026-10-14_post-CPI/REPORT.md`.

## Current judgment

**CPI day closed as a bull flattener, and the official close confirms the vendor read.** Treasury 10/14 vs 10/13: 2Y 4.82 (+3bp), 10Y 5.19 (−2), 30Y 5.52 (−4); real 10Y 2.84 (−4); 10Y nominal−real 2.35 (+2), 30Y 2.28 (0) [CONF PRIMARY Treasury CSV 10/15]. The front priced hikes; the long end fell on lower real yields.

**PPI day: the rally came before the print, not after it.** Yahoo ^TNX was already 5.081 at the first 08:20 bar (−11bp vs 5.190), blipped +2.5bp on the 08:30 PPI release, made a 5.037 low at 10:00 and sat at 5.085 at 13:35; 30Y 5.421 (−10bp), 5Y 4.899 (−9bp), 3M flat [CONF VENDOR 5-min bars, not close]. The fleet's "rallied −14bp into hot PPI" framing is right on the level and wrong on the timing: the bid was set overnight alongside the Asia equity selloff (KOSPI −8% circuit breaker, per X-feed, unverified at exchange). Fed-funds contracts fell only 3–6bp while the 10Y fell ~10bp, so most of the move is haven demand / term premium, not policy path. **Long Treasuries were bought as the safe asset on a hot-inflation day — expensive, not broken.**

**Credit: weak tail widening, high grade flat.** HY 325 (+9), CCC 1282 (window high), IG 84 (+1) [10/14]. HY is 25bp below 350. No funding stress: SOFR−IORB −2bp [10/14].

**Buyback dig (Will-asked, `analysis/2026-10-15_buyback-dig/REPORT.md`):** Treasury is not paying up — the yield it pays over the curve is flat at ~11–13bp (10–20Y) once corrected for intraday timing; buybacks offset ~30% of new long-bond DV01 since 9/10; record 10–20Y offers ($46.4B, $40.8B) are concentrated in single 2041–42 bonds, while 20–30Y offers are below median. News sweep (`NEWS.md`): no Fed support; a 20Y cut/suspension is analyst speculation (Bloomberg 10/12), Treasury silent; quarter-to-date buybacks $43.13B vs $38B guided. No score change.

**Current FORGE holdings: TBT 5; TLT Oct16 82P closed 10/12.** WQ357 TBT decision is TERRY/Will's. TBT −3.1% on 10/15 vendor tape (39.885 at 13:45; not a broker quote). Kill MET recommendation / funding window UNGRADED and WQ280 NO-ADD unchanged.

## Regime
<!-- bond-state: thesis=v1.2.11; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=MET-REC@2026-10-01; posture=HOLD-NO-ADD -->
C-36 TWO-PART unchanged. Policy-path channel alive; term-premium contribution assessed on its own model/window. No thesis version, capital approval or new threshold this session.

## Current dashboard

| Metric | Dated observation | Source / basis |
|---|---|---|
| Official 2Y/5Y/10Y/20Y/30Y | 4.82 / 5.00 / 5.19 / 5.57 / 5.52% [10/14]; Δ +3/0/−2/−3/−4bp | [CONF PRIMARY Treasury CSV pulled 10/15 13:50] |
| Official real 5Y/10Y/30Y | 2.64 / 2.84 / 3.24% [10/14] | [CONF PRIMARY Treasury real CSV] |
| Official 10Y/30Y nominal−real | 2.35 / 2.28% [10/14]; Δ +2 / 0bp | [EST fitted-par subtraction] |
| 2s10s / 5s30s | 37 / 52bp [10/14]; Δ −5 / −4 | [EST Treasury CSV subtraction] |
| 10/15 intraday 5Y/10Y/30Y | 4.899 / 5.085 / 5.421% at 13:35; ≈ −9/−10/−10bp | [CONF VENDOR Yahoo 5-min]; not close |
| 5Y5Y forward / 10Y breakeven | 2.34 / 2.35% [10/14] | [CONF MIRROR FRED T5YIFR/T10YIE]; 16bp below 2.50 |
| ACM 10Y TP / KW 10Y TP | 0.8086% [10/14] (−4.3bp d/d) / 1.0729% [10/9] | [EST NY Fed ACM / FRED KW]; different windows |
| Fed path | Nov 3.950 = +7.0bp vs EFFR ≈ 28% of +25 at 10/28; Dec 4.105; peak 4.650 Oct-27 | [EST CBOT vendor bars 10/15 13:49]; ORACLE: Polymarket 31.5 / Kalshi 29.0 [10/15 12:39Z] |
| HY/CCC/B/BB/BBB/IG OAS | 325 / 1282 / 329 / 199 / 104 / 84bp [10/14]; Δ +9/+15/+12/+8/+1/+1 | [CONF MIRROR FRED ICE] |
| HY distance to 350 | 25bp | [EST] first cell >320 (RED/REGINALD counts 1 of 3) |
| SOFR / TGCR / EFFR / IORB | 3.88 / 3.86 / 3.88 / 3.90% [10/14]; SOFR 99th pct 3.97 | [CONF PRIMARY NY Fed]; SOFR vol $2,974B |
| SOFR−IORB | −2bp [10/14] | [EST]; LIQUID owns verdict |
| FR2004 stock | long-end $133.062B (−7.483 w/w); 3–6Y $52.885B (−7.194) [9/30] | [CONF PRIMARY]; next weekly as-of publishes Thu 10/15 ~16:15 ET, after this closeout |
| PMMS | 7.40% [10/15], unch; − Treasury 10Y 5.19 [10/14] = 221bp | [CONF Freddie / EST]; inside 180–230; not MBS OAS |
| Bund fitted 10Y | 3.45% [10/15]; −12bp vs 10/8 | [CONF PRIMARY Bundesbank Svensson] |

## Gates and derived statistics

| Existing gate | Dated state |
|---|---|
| Real 10Y ≥2.50 sustain | Treasury 2.84 [10/14], 34bp through, trailing run 24 (2026 file); FRED DFII10 2.88 [10/13]. WQ246 state MET unchanged |
| OLD auction add re-arm | MET 9/23; add DECLINED WQ280; no fresh 5Y fire |
| WQ291 paired kill | MET first-published 9/23 stock; window closed, not regraded; funding window UNGRADED |
| Inflation anchoring | T5YIFR 2.34 [10/14], 16bp below 2.50 |
| HY marker / lead | HY 325 [10/14] >300; 25bp below 350; +62 from 263, 13–38bp short of the 338–363 lead band; VIX leg VIOLET |
| CCC escalation | 1282 [10/14] >1100, prior fire; no guessed score 5 |
| 30Y ≥5.00 | Treasury 2026 scan through 10/14: 86/197 sessions, trailing run 70 |
| WQ400 Bund disorderly | Level >3.25 AND five-session rise >17.0bp strict: 5th prospective evaluation NOT MET (−12bp) |

## Convergence Matrix

| # | Target / vector | Score | Key evidence | Upgrade condition |
|---|---|---:|---|---|
| 1 | Long end / duration VX-BND-05 / VX-BND-12 / VX-BND-14 | 5 | High real-yield regime, 30Y run 70; 10/15 haven bid −10bp | Existing top score |
| 2 | Treasury auction health VX-BND-01 / VX-BND-08 / VX-BND-13 | 4 | 10/7–8 clean 10Y/30Y; counter 2; 20Y-R bars frozen | Second composition failure with confirmed mechanism leg |
| 3 | Dealer absorption VX-BND-04 / VX-BND-16 | 2 | 9/30 stock unwind; F2 reads 5 of 5 OFF-THE-RUN (10/15: 0.33%); buyback prices flat at ~11–13bp cheap to curve, timing-corrected (KB-469) | Existing two-build / weak composition or carrier fire |
| 4 | HY function VX-BND-02 / VX-BND-11 | 3 | HY 325 / CCC 1282, weak-tail + AI-infra cohort | HY >350 or verified pulled-deal cluster |
| 5 | IG function VX-BND-03 / VX-BND-10 | 1 | IG 84, BBB 104 | Existing IG 120 / failed syndication |
| 6 | CDX/cash VX-BND-06 | 1 | True CDX unavailable | Confirmed fast-layer lead |
| 7 | Credit-equity VX-BND-07 | 1 | HY +62 from 263; VIX 16.7 | Existing +75–100 with VIX <20 |

**Composite 17/35 = 5+4+2+3+1+1+1, unchanged.** Auction downgrade counter 2; 20Y-R 10/21 could reach 3 only after an actual grade. TIPS/FRN excluded. Outside composite: VX-BND-15=2, VX-BND-17=1, VX-BND-18=2, VX-BND-19=3, VX-BND-20=2. FL14 LATENT unchanged.

## Exit / falsification

WQ157/WQ291 prior operational recommendation remains MET, through TERRY + Will; inventory ≠ warehousing, funding window UNGRADED. WQ357 decision applies to surviving TBT 5. Original 10Y <4.15 AND 30Y <5.00 ×3 plus clean refunding letter unchanged; not met at 10/14 (10Y 5.19 / 30Y 5.52). OPEN predictions 0; next FOMC curve prediction registration by 10/21. VX-BND-09 auction tails retired.

## Immediate Catalysts (same event set as docket/CATALYSTS.tsv)

| Date | Existing obligation / disposition |
|---|---|
| Thu 10/15 | DONE: 10/14 official split; PMMS; 20Y/TIPS bars frozen; WQ400 eval. F2 op 10–20Y OFF-THE-RUN (0.33% recent share, $6.0B full fill, 93% into 2% Nov-2041) → RED. PENDING: FR2004 next weekly as-of ~16:15; official 10/15 close tonight |
| Fri 10/16 | Treasury primary dealer questionnaire for the 11/4 refunding (press-reported date; read special topics: 20Y / bills / buyback cap); FRED 10/15 HY cell (RED/REGINALD >320 count); TERRY WQ-365 window 15:00 |
| 10/21, 10/22, 10/26–29 | 20Y-R 912810UX4; 5Y TIPS 91282CRR4; 2Y/5Y/FRN/7Y cluster; curve prediction registration by 10/21 |
| 10/27, 10/28, 11/4 | F2 op; FOMC + UK Budget + VX20 bounded review; QRA and F2 op |
| 11/9, 11/13, 12/1, 12/9 | FHLB Q3; FRBNY FX report; US sovereign CDS retest; December FOMC + SEP |
| 2027-1/25, 1/27 | GPFG expert report; January FOMC |
| Standing | MOF FX / Warsh / credit / FR2004 / buyback carrier, existing docket scope |

## BOTTOM LINE

CPI day closed with the front end up and the long end down, the 10-year's drop mostly from lower real yields; the official close confirms yesterday's provisional read. Today Treasuries rallied about 10bp, but the move happened overnight with the Asia equity selloff, before the hot PPI print, and long bonds traded as a safe haven, which supports "expensive, not broken." Junk-bond spreads widened to 325bp with the weakness still in the lowest-rated tail and investment grade flat; funding markets are calm. No change to scores, gates or the TBT position, which stays TERRY's and Will's call.
