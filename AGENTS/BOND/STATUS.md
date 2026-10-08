# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure. **Last session update:** 2026-10-07T20:35:10-04:00 — standard closeout requested by Will; research/documentation published through c1bdeb6e2; final runner/commit/publication receipt pending. **Last real data refresh: 2026-10-07.**

October7 primary Treasury curve and October6 credit observations below are separate frontiers. Full evidence, auction arithmetic, primary minutes and source gaps: `analysis/2026-10-07_catchup/REPORT.md`. Prior dashboard preserved at `domain/sources/2026-10-07_STATUS_pre-continuation.md`; interrupted checkpoint retained unchanged.

## Current judgment

**Strong 10Y auction demand has not generated a sustained long-end rebound.** October7 front-end yields fell while30Y rose; weakest-tier credit widened despite broader HY relief. October6 3Y fired the indirect-demand rarity marker, with cover and OLD composition tests intact. October7 10Y passed cleanly; downgrade counter now1, below3 required.

**WQ-357 LATER/path C to October14; NO-ADD (WQ-280) unchanged.** Prior WQ-291 kill remains MET as an operational exit recommendation via TERRY and Will; exit deferred. Net dealer inventory is not proof of warehousing; funding window UNGRADED. October7 intraday broker capture confirms TLT Oct16 82P ×1 and TBT10; exact time/Activity absent. No fill inferred. WQ-339 drafting only; WQ-360 fill unapproved.

## Regime
<!-- bond-state: thesis=v1.2.11; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=MET-REC@2026-10-01; posture=HOLD-NO-ADD -->
C-36 TWO-PART: policy-path channel alive; term-premium contribution remains separate. The September minutes preserve a conditional further-hike bias and report stable funding in their intermeeting window. No new October7 policy decision, new capital approval or thesis version change.

## Current dashboard

| Metric | Observation | Source / basis |
|---|---|---|
| 2Y / 5Y / 10Y / 20Y / 30Y | 4.77 / 5.03 / 5.28 / 5.71 / 5.67%; daily−2/0/+1/+3/+3bp | [CONF PRIMARY Treasury official par CSV10/7, pulled10/7~18:11ET] |
| 2s10s / 2s30s | 51 / 90bp; daily+3/+5 | [EST same-date Treasury subtraction10/7] Front rally, long end sells |
| Real5Y / 10Y / 30Y | 2.66 / 2.92 / 3.36%; daily0/+1/+1bp | [CONF PRIMARY Treasury real CSV10/7] |
| 10Y / 30Y nominal minus real | 2.36 / 2.31%; daily0/+2bp | [EST same-date par−real10/7]; do not call the30Y move exclusively real-led |
| 5Y5Y forward | 2.35%,15bp below2.50 | [CONF MIRROR FRED T5YIFR10/7, boot17:47ET] |
| ACM10Y TP / KW10Y TP | 0.9462%[10/6] /1.0847%[10/2] | [EST NYFed model / FRED model mirror]; windows differ, no causal FF decomposition |
| Fed path | October hold/+25 proxy18%; calendar-weighted YE+24.93bp vsEFFR3.88[10/6] | [EST CBOT ZQ vendor bars10/7 captured17:47ET after halt, NOT settlement]; Nov3.925/Dec4.070; independent FedWatch/OIS unavailable |
| HY / CCC / IG OAS | 303 /1214 /83bp[10/6]; daily−9/+3/−1 | [CONF MIRROR FRED ICE latest vintage]; broad relief and tail deterioration coexist |
| BBB / BB / B OAS | 102 /185 /302bp[10/6]; daily−2/−8/−12 | [CONF MIRROR FRED ICE latest vintage] |
| CCC−BB | 1029bp[10/6] | [EST1214−185]; not an aggregate issuance freeze |
| SOFR−IORB | 0bp[10/6:3.90−3.90] | [CONF MIRROR FRED same-date]; LIQUID owns funding interpretation; no retrospective auction funding grade |
| FR2004 long end | $140.545B[9/23],−$3.828B w/w;3–6Y$60.079B | [CONF NYFed last published vintage checked boot10/7]; next9/30 expected10/8. Stock≠auction flow |
| Mortgage survey | PMMS7.28%[10/1]; survey minus same-date10Y204bp | [CONF Freddie / EST difference];180–230 rearm band not breached; not MBSOAS |
| Global rates / metals / oil / volatility | HANS/SAM · MIDAS · BRENT · VIOLET | Owner sources; no copied live marks |

## Gate distances and derived counts

| Gate | Observation / state |
|---|---|
| Real10Y ≥2.50 sustained | Treasury10/7 2.92, through42bp; Treasury2026-series run20. WQ246 H.15 five-close sustain remainsMET; NO-ADD |
| OLD auction add rearm | MET9/23, add DECLINED WQ280; no new fire10/6 or10/7 |
| Paired kill WQ291 | MET10/1:3–6Y$60.079B vs$56.586B, margin+$3.493B; operational recommendation only, Will deferred to10/14 |
| Inflation anchoring | T5YIFR2.35[10/7],15bp below2.50 |
| HY row4 / issuance | HY303[10/6],3bp through300 marker,47bp below350; capital gate separate |
| CCC escalation | 1214[10/6]>1100, fired previously; no invented score5 rule |
| Credit-equity lead | HY+40 from263;35–60bp short of+75–100; VIX leg→VIOLET; inactive |
| 30Y ≥5.00 | Treasury2026 scan through10/7:82/193 observations,current run66. Separate FRED whole-series run65 through10/6. No carried rank for later Treasury print |

## Convergence Matrix

| # | Target/Vector | Score | Status | Key signal | Upgrade trigger |
|---|---|---:|:--:|---|---|
|1|Long end/duration (VX-BND-05 / VX-BND-12 / VX-BND-14)|5|🔴🔴|Prior paired kill confirmed;30Y rises despite clean10Y auction|Top score; next30Y10/8 |
|2|Treasury auction health (VX-BND-01 / VX-BND-08 / VX-BND-13)|4|🔴|3Y I-prime marker;10Y clean; counter1|Second composition failure with confirmed mechanism leg |
|3|Dealer absorption (VX-BND-04 / VX-BND-16)|2|🟡|Last stock vintage9/23; no fresh FR2004 print; prior three F2 reads OFF|Two total-stock builds with weak composition or funding confirmation; F2 newest-vintage fire |
|4|HY market function (VX-BND-02 / VX-BND-11)|3|🟠|HY303/CCC1214[10/6], bifurcated; no comprehensive pulled-deal census|HY>350 or verified pulled-deal cluster |
|5|IG market function (VX-BND-03 / VX-BND-10)|1|🟢|IG83[10/6],37bp below120|IG>120 or verified failed syndication |
|6|CDX/cash basis (VX-BND-06)|1|🟢|No new true-CDX observation; last proxy dated10/5, rate-confounded|Confirmed fast-layer lead; source gap persists |
|7|Credit-equity lead (VX-BND-07)|1|🟢|HY+40 from263, spread leg unmet|HY+75–100 from263 withVIX<20 |

**Composite17/35 =5+4+2+3+1+1+1, unchanged10/7.** One5,one4,one3,one2,three1. October6 3Y indirect57.594842%<58.90 frozenbar; OLD/cover unmet. October7 10Y indirect80.338513%, dealer2.544908%, BTC2.77; clean pooled/reopening alternatives. **Counter0→0→1.** No second confirmed mechanism failure established.

Outside composite: VX-BND-15=2; VX-BND-17=1; VX-BND-18=2; VX-BND-19=3 with undefined disorderly qualifier due10/8; VX-BND-20=2 reviewed10/7. No adopted mandate or qualifying second holder found in bounded search; absence not proven. NBIM proposal remains conditional, agency-MBS taxonomy settled. Next review10/14 and on issuer news; expert deadline1/25/27 unchanged.

## Exit / falsification and positions

1. WQ157 paired kill: I-prime plus non-auction confirmation. WQ2919/23dealer legMET; recommendation remains exit-all-duration-shorts via TERRY/Will, deferred underWQ357. Net inventory≠warehousing; funding windowUNGRADED. I-prime alone is a rarity marker, no demonstrated TLT5-day predictive separation. Leg②PARKED.
2. Position-specific:10Y<4.15 AND30Y<5.0 for3 sessions AND clean refunding; current levels do not meet. TLT Oct16 82P×1 and TBT10 confirmed in10/7capture; TERRY owns sell-or-roll management. No executable marks here.
3. Convergence downgrade: three consecutive nominal coupons with indirect≥own median AND dealer≤own median. Counter1 as of10/7. TIPS/FRN excluded. A clean10/8 could reach2, not3.
4. Predictions OPEN0; next curve-shape registration due10/21. Existing tally→PREDICTIONS archive. VX-BND-09 auction tails RETIRED/unscoreable.

## Immediate Catalysts *(source of truth `docket/CATALYSTS.tsv`; human twin — same event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| **Mon10/5 ✅ delivered ·Wed10/14 decision** | L608writtenreboundread delivered;WQ357LATER/pathC | Existing recommendation unchanged;Will/TERRYreview10/14 |
| **Tue10/6 event; serviced10/7** | COMPLETED: 3Y graded marker; VX-BND-20 review serviced10/7 | VX-BND-20 held2; no mandate located. 3Y I-prime only; counter0 after that auction |
| **Wed10/7** | 10Y-R$39B91282CRF0 13:00;FOMCminutes14:00 | COMPLETED: 10Y clean, counter1; minutes integrated |
| **Thu10/8** | 30Y-R$22B912810UW6;F2op;FR2004as-of9/30;PMMS;VX-BND-19qualifier | Publishedprimary results;noanticipatorygrade |
| **Wed10/14 ·Thu10/15** | CPI08:30;BeigeBook14:00;heldpositionclock;VX-BND-20 review;F2op10/15 | Same-date real/nominal split;Will/TERRYreview |
| **Fri10/16** | Held TLT82P expiry | TERRY sell-or-roll rail; Will approval, no automatic order |
| **10/21 ·10/22 ·10/26–29** | 20Y-R;5YTIPS;2Y/5Y/FRN/7Ycluster | IssuerPDFvisuallyverified10/5;barsatannouncements;FRNexcludedfromI-prime |
| **Wed10/28 14:00** | OctoberFOMC | Registercurve-shaperowwithbaserateby10/21;livepath→dashboard |
| **10/27 ·11/4** | F2op;QRAandF2op11/4 | F1/F3;schedulewindowends |
| **11/9 ·11/13 ·12/1 ·2027-01-25** | FHLBQ3;FRBNYFX;USsovCDSretest;Norwegianexpertreport | Asdocketed |
| **12/9 14:00 ·2027-01-27** | DecemberFOMC+SEP;JanuaryFOMC | Predictionrowsby12/2and1/20 |
| **—STANDING—** | MOFFX;Warshtaskforce;FR2004;credit;F2carrier | Ownsourcefrontiersandrecordedscope |

---


## BOTTOM LINE

Bond demand can be strong at auction while duration prices fall: that is today's10Y/30Y distinction. The minutes reinforce a conditional further-hike bias, while credit relief stops short of the weakest tier. Existing operational exit recommendation and Will's October14 deferral/no-add remain separate and unchanged. Independent dated FedWatch/OIS, trueCDX, paidMBSOAS, comprehensive failed-deal coverage and executable broker/Activity are unavailable; re-test relevant sources10/8.
