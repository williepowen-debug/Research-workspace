# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure. **Last session update:** 2026-10-20 session close (Will-directed, OpenAI Codex); repairs completed and pushed at `2e1117ae4`. **Last real data refresh: 2026-10-20.** Exact deployed model UNKNOWN; session `01a15a02-565d-76c1-9d89-07653c5d3b62`.

Close handoff: one newly arrived WALTER INFO packet (`SIG-W-20261020-020`) triaged, retained for next-session processing; no new evidence incorporated.

Frontiers: Treasury nominal/real **10/19** · ICE credit via FRED **10/19** · NY Fed repo **10/19** · FR2004 as-of **10/7** · ACM **10/16** · Bund fitted **10/20** · vendor intraday **10/20 11:40–11:55 ET**. FRED DGS/DFII mirror ends **10/16**, behind issuer. Evidence: `analysis/2026-10-20_catchup/REPORT.md`, `derived.json`, raw manifest. Prior October15 report is history.

## Current judgment

**Long bonds still clear at expensive yields; the weak credit tail remains the warning.** Monday10/19 Treasury10Y rose6bp, entirely real-led on fitted-par subtraction; 30Y rose5bp, also real-led. That partly reversed last week's relief: October14→19 10Y and30Y remain4bp lower. Official October15 close confirms the prior provisional rally: both long yields fell9bp. ACM October7→16 attributes the fitted10Y fall to premium compression while expected-rate component rose; model accounting does not establish buyback or haven causation.

**Credit is diverging by quality.** ICE/FRED October19 HY329bp (−2 daily), CCC1310 (+13), IG87 (+2). HY remains21bp below350, +66 from263 and9–34bp short of BOND's credit-equity lead band. Wider credit alongside last week's lower real yields defeats a simple rates-only explanation. No broad issuance freeze established: SIFMA through September is lagged aggregate evidence; a current pulled-deal census is missing.

**Dealer evidence is selective.** Latest published as-of10/7 Treasury long-end stock$135.084B (+$2.022B), one build, not two. LIQUID's primary-backed below-IG corporate net stock fell$2.795B in that same lagged week. Net stocks cannot identify gross forced sales, shorts or capacity refusal. SOFR−IORB −3bp [10/19] gives no acute median repo stress; private/offshore channels remain unobserved.

**Treasury's October16 dealer agenda asks about buyback effects and structural demand, not a specific20Y suspension.** The cut story remains speculation; November4 resolves F1/F3. October15 buyback timing bracket now complete: paid yield+10.3bp over same-day close curve, +11.4bp over vendor-adjusted operation curve. No overpaying demonstrated by this sample; F2 five-of-five OFF-THE-RUN. Tomorrow's20Y auction remains ungraded against its frozen bars.

## Regime and capital record
<!-- bond-state: thesis=v1.2.11; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=MET-REC@2026-10-01; posture=APPROVED@WQ-357 -->
C-36 TWO-PART unchanged; no thesis version, research threshold or score change. **Approval correction:** WQ357 already RULED APPROVE10/15 12:23 ET (SELL remainingTBT5), superseding this desk's stale LATER/HOLD wording. FORGE October20 still displaysTBT5, sale fill not evidenced; approval≠execution. TLT82P sold10/12. WQ280 NO-ADD; WQ360 old put card lapsed unapproved10/14, not a live execution permission. No trade executed or new trade proposed. User's October20 no-expiry-reminders instruction governs communication.

## Current dashboard

| Metric | Dated observation | Source / basis |
|---|---|---|
| Official 2Y/5Y/10Y/20Y/30Y | 4.77 /4.94 /5.15 /5.53 /5.48% [10/19]; daily+3/+5/+6/+6/+5bp | [CONF PRIMARY Treasury nominal CSV pulled10/20] |
| Official real 5Y/10Y/30Y | 2.56 /2.80 /3.21% [10/19] | [CONF PRIMARY Treasury real CSV] |
| Official10Y/30Y nominal−real | 2.35 /2.27% [10/19], each unchanged daily | [EST fitted-par subtraction; not pure inflation expectations] |
| 2s10s /5s30s | 38 /54bp [10/19], daily+3 /0 | [EST PRIMARY Treasury subtraction] |
| FRED H.15 companion | DGS10 5.09 /DGS30 5.43 /DFII10 2.74% [10/16] | [CONF MIRROR, older than issuer; not10/19 levels] |
| 10/20 intraday5Y/10Y/30Y | 4.918 /5.109 /5.430% at11:40 ET | [CONF VENDOR Yahoo bars; not closes/gate inputs] |
| 5Y5Y forward /10Y breakeven | 2.32 /2.35% [10/19] | [CONF MIRROR FRED T5YIFR/T10YIE]; forward18bp below2.50 |
| ACM10Y TP /KW10Y TP | 0.7562% [10/16] /1.0729% [10/9] | [EST PRIMARY NY Fed /MIRROR FRED]; different model/windows |
| Fed path | Nov3.920, +4bp vs EFFR ≈16% of one+25bp step10/28; strip peak4.650 Sep27 | [EST CBOT vendor evolving bar10/20 11:55]; not settlement/OIS |
| HY/CCC/B/BB/BBB/IG OAS | 329 /1310 /336 /200 /108 /87bp [10/19]; daily−2/+13/+1/−3/+2/+2 | [CONF MIRROR-WALLED ICE via FRED] |
| HY distance to350 | 21bp; >320 sustain325/323/331 [10/14–16] | [EST]; RED/REGINALD/LIQUID own consequences |
| SOFR/TGCR/EFFR/IORB | 3.87 /3.85 /3.88 /3.90% [10/19]; SOFR99th3.95 | [CONF PRIMARY NY Fed; IORB mirror]; SOFR volume$2,888B |
| SOFR−IORB | −3bp;99th percentile+5bp [10/19] | [EST]; private/offshore channels unobserved, LIQUID owns verdict |
| FR2004 stock | Long-end$135.084B (+2.022);3–6Y$54.933B (+2.048) [10/7] | [CONF PRIMARY NY Fed]; one total build after declines |
| PMMS spread | 7.40%−Treasury10Y5.10% [both10/15] =230bp | [CONF PRIMARY Freddie/Treasury; EST]; at boundary, not beyond; not MBS OAS |
| Bund fitted10Y | 3.48% [10/20]; five-session−1bp | [CONF PRIMARY Bundesbank Svensson] |
| France−Germany10Y | Screen150.8bp [10/20], vs142.3 [10/19]; bond close clock unverified | [CONF SECONDARY ideal-investisseur directly fetched]; not a fresh HANS owner grade |

## Gates and derived statistics

| Existing gate | Dated state |
|---|---|
| Real10Y≥2.50 sustain | MET unchanged (FRED keyed); Treasury2.80 [10/19],30bp through, trailing run27 in2026 file; mirrorDFII10 2.74 [10/16] |
| OLD auction add re-arm | MET9/23; add DECLINED WQ280; no fresh fire |
| WQ291 paired kill | MET first-published9/23 stock; closed window, not regraded; funding window UNGRADED |
| Inflation anchoring | T5YIFR2.32 [10/19],18bp below2.50 |
| HY marker /lead | HY329 [10/19]>300;21bp below350;+66 from263,9–34bp short of338–363; VIX leg VIOLET |
| CCC escalation | 1310 [10/19]>1100, prior fire; score4 held, no guessed score5 |
| 30Y≥5.00 | PRIMARY Treasury2026 scan through10/19:89/200 sessions, trailing run73; MIRROR through10/16:88/199, run72 |
| WQ400 Bund disorderly | >3.25 AND strict five-session rise>17bp:8th prospective evaluation NOT MET (−1bp);0/8 so far |

## Convergence Matrix

| # | Target /vector | Score | Status | Key evidence | Upgrade condition |
|---|---|---:|---|---|---|
| 1 | Long end /duration VX-BND-05 /VX-BND-12 /VX-BND-14 | 5 | 🔴🔴 | Real-rate regime; Monday partial reversal of rally; 30Y run73 | Existing top score |
| 2 | Treasury auction health VX-BND-01 /VX-BND-08 /VX-BND-13 | 4 | 🔴 | Last10Y/30Y clean; counter2;20Y bars frozen | Second composition failure with confirmed mechanism leg |
| 3 | Dealer absorption VX-BND-04 /VX-BND-16 | 2 | 🟡 | One total rebuild;F2 five OFF-THE-RUN | Existing two-build /weak-composition condition |
| 4 | HY function VX-BND-02 /VX-BND-11 | 3 | 🟠 | HY329/CCC1310; tail deteriorates, no broad access freeze verified | HY>350 or verified pulled-deal cluster |
| 5 | IG function VX-BND-03 /VX-BND-10 | 1 | ⚪ | IG87/BBB108; data broadens, no failed-syndication cluster | Existing IG120 /failed syndication |
| 6 | CDX/cash VX-BND-06 | 1 | ⚪ | Proxy z<−1.5 with cash widening = co-move; true CDX gap | Confirmed fast-layer lead |
| 7 | Credit-equity VX-BND-07 | 1 | ⚪ | HY+66; spread band unmet | Existing+75–100 with VIX<20 |

**Composite17/35 =5+4+2+3+1+1+1, unchanged:** one5, one4, one3, one2, three1. Elevated duration/auction risk, tail credit watch. Auction clean counter2;20Y10/21 could reach3 only after actual grade; TIPS/FRN excluded. Outside composite: VX-BND-15=2,VX-BND-17=1,VX-BND-18=2,VX-BND-19=3,VX-BND-20=2. French spread is secondary/current-clock-qualified, not a newly primary-certified BOND fire. FL14 LATENT.

## Exit /falsification

WQ157/WQ291 recommendation MET; WQ357 approval recovered, no fill inferred; funding window UNGRADED. Existing position falsifier10Y<4.15 AND30Y<5.00 for3 sessions plus clean refunding not met at10/19 (5.15/5.48). Convergence downgrade needs third clean nominal auction; counter2. Position construction and any60-DTE review stay TERRY-owned; no expiry-reminder duty. OPEN prediction1: BND32,65% non-steepening2s30s on10/28, base5/6 completed2026 meetings; resolves first-published primary close, ceiling11/3. VX-BND-09 auction tails remain retired.

## Immediate Catalysts (same event set as docket/CATALYSTS.tsv)

| Date | Existing obligation /disposition |
|---|---|
| 10/20 catch-up | COMPLETED: official10/15–19,FR2004 as-of10/7,dealer agenda,credit>320 sequence,prior WQ357 ruling,seven WALTER +two general packets |
| 10/21 | 20Y-R912810UX4,13:00ET: frozen indirectI'<57.96%;OLD<52.47 AND dealer>17.59;BTC<2.36. Identity-checked frozen-bars JSON prepared; no outcome assumed. BND32 registered10/20 before owed deadline |
| 10/22 | 5Y TIPS91282CRR4:OLD indirect<51.43 AND dealer>25.42;BTC<2.10;noI'. PMMS release; next FR2004 publication as-of10/14 expected10/22 |
| 10/26–29 | 2Y10/26,5Y10/27,FRN10/28,7Y10/29; freeze at10/22 announcement. Dealer agenda responses10/26 noon, meetings10/29–30 (context on existing questionnaire row) |
| 10/27,10/28–29,11/2–4 | F2 operation10/27;FOMC+UK Budget+VX-BND-20 review10/28;ECB10/29;borrowing estimates11/2;QRA/F2 11/4 |
| 10/29–11/10 macro | GDP/PCE10/29;ECI10/30;JOLTS11/3;productivity11/5;jobs11/6;CPI11/10 (issuer calendars verified10/20);BOND reads rates response |
| 11/9,11/13,12/1,12/9 | FHLB Q3;FRBNY FX report (cadence-based);sovereign CDS retest;December FOMC+SEP |
| 2027-1/25,1/27 | GPFG expert report;January FOMC |
| Standing | MOF FX /Warsh /credit /FR2004 /buyback carrier;grader repair/tests completed; acceptance and independent review at analysis/2026-10-20_monitor-repairs_ACCEPTANCE.md |

## BOTTOM LINE

U.S. long bonds retain buyers at high yields, and Monday only partly reversed last week's rally. The weakest corporate borrowers keep deteriorating, while dealer credit and Treasury stocks move differently; neither a broad issuance freeze nor a U.S. funding seizure is established. Treasury is consulting on larger buybacks and future supply, with no specific20Y suspension adopted. Tomorrow's20Y auction is the next direct demand test. The grader now uses explicit frozen bars; the repair changes no research threshold, current grade or trade approval.
