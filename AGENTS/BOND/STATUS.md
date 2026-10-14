# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure. **Last session update:** 2026-10-14T14:20:29.517441-04:00. **Last real data refresh: 2026-10-14.** Codex/OpenAI gpt-6.1-sol;Will-launched session01a13b8c-bf81-7d83-9731-47f494922784.

Market cutoff13:59EDT;BeigeBookreadafter14:00. OfficialTreasury10/13,ICEcredit10/13,repo10/13andFR2004as-of9/30are separatefrontiers. Evidence: `analysis/2026-10-14_post-CPI/REPORT.md`,raw/derived.json;bootreceiptthere.

**Closeout:** Heavy checks PASS and localcommit99c38dbfb. OriginPUBLICATION HOLD:automaticapprovalreviewrejectedpublicGitHubexport,explicitWillapprovalpending. LivePROMEnotification/consumptionunverified;datedholdpacketinPROME/inbox.

## Current judgment

**CPI caused an initial yield jump, followed by a long-end retracement.** Yahoo/CBOE10Y08:29→08:31 5.190→5.263% (+7.3bp);CNBC13:58/13:59vendor10Y5.211% (−0.6bpvsprior) and30Y5.539% (−2.4bp). Afternoonnear-contemporaneous10Ypair:real−2.1bp,compensation+1.5bp. A firmer futures Fedpath coexists with real-yieldrelief. MorningTIPSsplit and officialOctober14close are stillunmeasured;the vendorpair is not a pureexpectations measure or gategrade.

**Financing cost is high; funding dysfunction is not established.** Priorcleanauctions/dealerunwindreused;NYFedOctober13SOFR−IORB−1bp,transactionsbeforeCPI. These do not clear today'sindividualfund/haircut/margincashneeds. Treasurydepth/fails/cash-futuresbasisnotobtained.

**Current FORGE holdings: TBT5; TLT Oct16 82P CLOSED10/12.** WQ357October14decisionclockremainsforTBT;olderTBT10/TLT1mirror superseded. No executablebrokerquotes. KillMET recommendation/fundingwindowUNGRADed andWQ280NO-ADD unchanged;TERRY/Willown capital.

## Regime
<!-- bond-state: thesis=v1.2.11; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=MET-REC@2026-10-01; posture=HOLD-NO-ADD -->
C-36 TWO-PART unchanged. Policy-path channel alive;term-premiumcontribution assessedon its ownmodel/window. No thesisversion,capitalapprovalornewthreshold. WQ400priorapprovedBunddefinitionencodedprospectively10/9.

## Current dashboard

| Metric | Dated observation | Source / basis |
|---|---|---|
| Official2Y/5Y/10Y/20Y/30Y |4.79/5.00/5.21/5.60/5.56%[10/13] |[CONF PRIMARY TreasuryCSVpulled10/14 13:57] |
| Officialreal5Y/10Y/30Y |2.67/2.88/3.28%[10/13] |[CONF PRIMARY TreasuryrealCSV,same date] |
| Official10Y/30Ynominal−real |2.33/2.28%[10/13] |[EST same-datefittedparsubtraction];10/9→13bothflat |
| October14afternoon2Y/5Y/10Y/30Y |4.827/5.019/5.211/5.539%;daily+3.4/+1.2/−0.6/−2.4bp |[CONF VENDOR CNBC13:58–13:59EDT];notdailyclose |
| October14vendorreal10Y / compensation |2.852 /2.359%;daily−2.1/+1.5bp |[CONF VENDOR / EST subtraction];nominalAug2036/TIPSJul2036,one-minutegap,nogategrade |
| 5Y5Yforward |2.33%[10/13],17bpbelow2.50 |[CONF MIRROR FRED T5YIFR];preCPIcell |
| ACM10YTP / KW10YTP |0.851455%[10/13]/1.0729%[10/9] |[EST NYFedmodel/FREDmodelmirror],distinctwindows |
| Octoberpolicyproxy / November/December/Januaryimplied |36%binaryhold/+25;3.970/4.125/4.200% |[EST YahooCBOT evolvingbars10/14 13:58EDT];November+3.5bp,distant+4bp;EFFR3.88[10/13],notsettlementorFedWatch |
| HY/CCC/IG/BBB/BB/B OAS |316/1267/83/103/191/317bp[10/13] |[CONF MIRROR FREDICElatestvintage];daily+5/+14/0/+1/+3/+7 |
| CCC−BB / HYdistance |1076bp /34bpbelow350 |[EST same-date subtraction];tail-dominated daily stress;LIQUID15-observationruleBROADENS,notaggregatefreeze |
| SOFR/EFFR/TGCR/BGCR |3.89/3.88/3.88/3.88%[10/13] |[CONF PRIMARY NYFedpublished10/14];SOFRvolume$3000B |
| SOFR−IORB |−1bp[10/13:3.89−3.90] |[EST NYFed/FREDsame-date];LIQUIDowns verdict,beforeCPI |
| FR2004stock |long-end$133.062B(−7.483w/w);3–6Y$52.885B(−7.194)[9/30] |[CONF PRIMARY re-pulled10/14];stocknotwarehousing,next10/15 |
| PMMS |7.40%[10/8];same-dateTreasuryspread218bp |[CONF Freddiepriorprimary / EST];inside180–230;next10/15;notMBSOAS |
| Bundfitted10Y / 5-sessionchange |3.51%[10/14] /−4bp[10/7→14] |[CONF PRIMARY BundesbankSvensson10.0Y / EST],observationtimeunverified |
| Goldsensitivity |MIDAScurrentownerreturn |Savedbetaunchanged;source/date/causal limits atMIDAS,notrecomputedhere |

## Gates and derived statistics

| Existing gate | Dated state |
|---|---|
| Real10Y≥2.50sustain |H15WQ246stateMETunchanged;FREDlatest10/9 2.91,through41bp. Treasury10/13 2.88,through38bp,run23;differentpublicationbasis,noproxygategrade |
| OLDauctionaddrearm |MET9/23;addDECLINEDWQ280;nofresh5Yfire |
| WQ291pairedkill |METfirst-published9/23stock;windowclosed,notregraded;9/30unwindcontextonly;fundingwindowUNGRADed |
| Inflationanchoring |T5YIFR2.33[10/13],17bpbelow2.50;10/14officialpending |
| HYmarker / lead |HY316[10/13]>300;34bpbelow350;+53from263,22–47bptoleadband338–363;VIXlegVIOLET |
| CCCescalation |1267[10/13]>1100,previousfire;noguessedscore5 |
| 30Y≥5.00 |Treasury2026scanthrough10/13:85/196observations,trailingrun69,publisheddatesonly;notFRED10/9run68 |
| WQ400Bunddisorderly |Level>3.25ANDfive-sessionrise>17.0bpSTRICT,dailyfittedseries;prospective10/9. All4prospectiveevaluationsNOTMET;latest−4bp. OtherVX19branchesungraded |

## Convergence Matrix

| # | Target / vector | Score | Key evidence | Upgrade condition |
|---|---|---:|---|---|
|1|Longend/duration VX-BND-05 / VX-BND-12 / VX-BND-14|5|Highreal-yieldregime/priorpairedkill;currentintradayretracement|Existingtopscore |
|2|Treasuryauctionhealth VX-BND-01 / VX-BND-08 / VX-BND-13|4|October7/8clean10Y/30Y;counter2|Secondcompositionfailurewithconfirmedmechanismleg |
|3|Dealerabsorption VX-BND-04 / VX-BND-16|2|9/30stockunwind;fourF2readsOFF|Existingtwo-build/weakcompositionorcarrierfire |
|4|HYfunction VX-BND-02 / VX-BND-11|3|HY316/CCC1267,weak-tailconcentration|HY>350orverifiedpulled-dealcluster |
|5|IGfunction VX-BND-03 / VX-BND-10|1|IG83;incompletefailed-syndicationcensus|ExistingIG120/failedsyndication |
|6|CDX/cash VX-BND-06|1|TrueCDXunavailable|Confirmedfast-layerlead |
|7|Credit-equity VX-BND-07|1|HY+53from263,spreadlegunmet|Existing+75–100withVIX<20 |

**Composite17/35=5+4+2+3+1+1+1,unchanged.** Auctiondowngradecounter2;nextnominal20Y-R10/21couldreach3onlyafteractualgrade. TIPS/FRNexcluded.
Outsidecomposite:VX-BND-15=2,VX-BND-17=1,VX-BND-18=2,VX-BND-19=3,VX-BND-20=2. VX19WQ400barencoded,notnewlyproposed. VX20boundedreviewserviced10/14:Ministry2027budgetstillproposal/furtherwork,expert1/25/27andassessmentplannedspring2027;qualifyingsecondholdernotlocated,absenceunproven. FL14LATENTunchanged.

## Exit / falsification

WQ157/WQ291prioroperationalrecommendation remains MET,throughTERRY+Will;inventory≠warehousing,fundingwindowUNGRADed. WQ357LATER/pathCdecision10/14appliestosurvivingTBT5. Original10Y<4.15AND30Y<5.00×3pluscleanrefundingletterunchanged;notmetat10/13. OPENpredictions0;BND30latest-revisedKWcompanionservicedwithoutACMre-grade. NextFOMCpredictionregistration10/21. VX-BND-09 auctiontailsretired.

## Immediate Catalysts (same event set as docket/CATALYSTS.tsv)

| Date | Existing obligation / disposition |
|---|---|
|10/5,10/6–8COMPLETED|Authorizedreboundresearch;3Y/10Y/30Yauctiongrades,minutes;priorreturnsreused |
|Wed10/14|CPI/BeigeBookreadCOMPLETED;WQ400encodeCOMPLETED;WQ357survivingTBTdecisionclock |
|Thu10/15|PPI08:30context;October14officialsplitconfirmation;F2op10–20Y;FR2004as-of10/7;PMMS;freeze20Y/TIPSbars |
|Fri10/16COMPLETEDTLTduty|TLT82Pclosed10/12per10/14brokerreceipt;nocurrentTLTexpiry |
|10/21,10/22,10/26–29|20Y-R912810UX4;5YTIPS91282CRR4;2Y/5Y/FRN/7Ycluster;curvepredictionregistrationby10/21 |
|10/27,10/28,11/4|F2op;FOMC+UKBudget+VX20boundedreview;QRAandF2op |
|11/9,11/13,12/1,12/9|FHLBQ3;FRBNYFXreport;USsovereignCDSretest;DecemberFOMC+SEP |
|2027-1/25,1/27|GPFGexpertreport;JanuaryFOMC |
|Standing|MOFFX/Warsh/credit/FR2004/buybackcarrier,existingdocketscope |

## BOTTOM LINE

Hot CPI pushed yields up initially, but the long end had retraced by about2PM while futures still priced a firmerFedpath. The afternoon vendorpair points to lowerreal yields and slightlyhigherinflationcompensation;officialclose/morningTIPSsplitremainpending. ExpensiveTreasuryfinancingdoesnotestablishafundingbreak;latestrepoispreCPIandcannotclearindividualcashneeds. CurrentbookisTBT5/TLTclosed;TERRYandWillownthesurvivingdecision,nocapitalactionhere.
