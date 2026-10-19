from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib,tarfile,io,subprocess
R=Path('/home/willi/Research-workspace');W=R/'AGENTS/WALTER';D=Path(__file__).resolve().parent;now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
# Preserve and explicitly replace the raw non-consecutive history/MA derivation.
p=D/'breadth-summary.json';raw=p.read_bytes();(D/'breadth-summary-pre-audit.json').write_bytes(raw);b=json.loads(raw);audit=json.loads((D/'session-audit.json').read_text());b['raw_price_moving_averages']={'state':'SUPERSEDED','use':'session-audit.json#moving_averages','reason':'initialderivationskippedmissingdates;strictsame-sessioncoveragecontrols'};b['historical_current_basket_ad']={'state':'SUPERSEDED','use':'session-audit.json#history','reason':'initialshared-dateintersectioncouldskipprevioussession;strictadjacentsessionauditcontrols'};p.write_text(json.dumps(b,indent=2)+'\n')
# Canonical raw bundle; loose captures are working copies, not missing delivery obligations.
rawpaths=sorted([*D.glob('spark-*.json'),*D.glob('chart-*.json'),D/'holdings-daily-us-en-spy.xlsx']);manifest=[]
with tarfile.open(D/'sources.tar.gz','w:gz') as t:
 for p in rawpaths:
  t.add(p,arcname=p.name);manifest.append({'member':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
with tarfile.open(D/'sources.tar.gz','r:gz') as t:
 for x in manifest:assert hashlib.sha256(t.extractfile(x['member']).read()).hexdigest()==x['sha256']
(D/'sources-manifest.json').write_text(json.dumps({'asof':now,'bundle':'sources.tar.gz','members':manifest,'verified':'allmemberhashesrecomputedfrombundle'},indent=2)+'\n')
(D/'.gitignore').write_text('spark-*.json\nchart-*.json\nholdings-daily-us-en-spy.xlsx\n')
(D/'HELPER.md').write_text('''# Rule9 source verification and sanity review

Thread/root/verify_breadth; read-only helper, not domain desk. Actual exact model not exposed to parent. Sources: AP1:52ET qualitative narrow rebound; Reuters via KoreaTimes11:42ET NYSEdecliners1.11:1/Nasdaqadvancers1.28:1,newhighs/lows10/2and20/242,issuesuniverseunclear. https://www.koreatimes.co.kr/amp/world/20261020/nasdaq-climbs-over-1-as-ai-linked-stocks-recover-ahead-of-key-earnings . October20KST publication is October19USmarket, not futureUSnews. AP https://apnews.com/article/494fbe4361a0360b2f6368e7a6d8f058 . These snapshot times differ from own14:57ET.

TradingViewcountryandSPXwidgetsreturnedunstampedconflictingcachedvalues;notusedfordatedcount. WSJloadingonly,Barchartaccessblocked,Nasdaqstatsunavailable. No bypassattempted. OwnSSGA/Yahoosnapshotprovidesdirectcountinstead.

Sanityreviewreadbreadth-summary/session-audit:315/503=62.62%down,186up,2flat;timestamps14:50:08–14:57:20. CurrentSPYsecuritylineproxy,classescountedseparately,notofficialindex/oneinstant. QQEW+1.31vsQQQ+1.35showsNasdaq100broadinsideitsuniverse;5/20dRSPoutperformancecontradictsuninterruptednarrowing. InitialMA/historycoverageoptimistic;strictsession-auditsupersedes. Parentpreservedpre-auditjsonandreplacedmisleadingfields. Contributionstatsuncertifiedweights>100;omitpreciseshareofindexgain. No novelcausalgrade.

Explicitfinalcloseoutreceipt: read-only investigation and sanity review complete; nofileschanged,no remainingwork. Nativehelperreceiptisnotfleetpresence/domainconsumption.
''')
(D/'RESULT.md').write_text(f'''# Market participation investigation — {now}

**Will'sexplicitcommission:** investigateindexesrisingwhilemoreindividualnamesfall. Finding: **confirmedintradayfortheSPYholdingsproxy**, notanuninterruptedall-indextrend. No standingmonitor,prediction,threshold,capitalinstructionorownergradecreated.

## Today's like-for-like evidence

SSGA'sownSPYholdingsfile(asofOctober16),503tradableequitysecuritylinesafterexcludingUSDcashandnontradableTPGCVR. Yahooall503returnedcurrent-sessionquotes,14:50:08–14:57:20ET,retrieval14:57:13–22ET. AgainstFriday10/16rawcloses:**186up,315down,2flat**;**62.6%declining**,median−0.395%,mean−0.240%. Same-vendorbarcomparisonreproducescounts;notindependentvendorproof. Classescountseparately,not500uniquecompanies. Currentholdingsproxy,notcertifiedMondayindexmembership/exchange-widebreadth. Asynchronousandprovisional,notcashclose.

| Proxy | October19intradaychangefromFriday |
|---|---:|
| SPY /capweightSP500 | +0.566% |
| RSP /equalweightSP500 | −0.234% |
| QQQ /capweightNasdaq100 | +1.353% |
| QQEW /equalweightNasdaq100 | +1.313% |
| IWM /Russell2000 | +0.283% |
| DIA /Dowproxy | +0.090% |
| SMH /semiconductors | +1.847% |
| KRE /regionalbanks | −0.802% |

ETFquotes14:56:46–14:57:23ETforcorecomparisons;completeper-symbolclockinproxy-summary.csv/analysis.json. RSP-SPYtoday**−0.800percentagepoints**. SectorETFs**3positive/8negative**:XLY+1.78,XLK+1.47,XLB+0.21;XLC−0.04,XLP−0.17,XLV−0.37,XLI−0.44,XLE−0.55,XLF−0.66,XLRE−1.17,XLU−1.88. SectorETFreturnisnotsectorconstituentcount.

ApproximateleadersAMZN+4.88,NVDA+1.44,TSLA+4.01,MSFT+0.98,AVGO+1.94. **No certifiedfractionofindexgainattributed:**primaryfileallnumericweightssum100.218976%,tradableequity99.929217%;cash/CVRandweightsnotfullyreconciled. Rankingonly;donotquote'XnamesexplainY%'. Counts/unweightedreturnconclusiondoesnotdependonweights.

## The longer-window counterevidence

Adjustedclosing-priceETFtotal-returnproxies,commonend10/16,commonstartdatepersamewindow. Cashdistributionsincludedthroughvendoradjustment;notofficialindexTR.

| Completedwindow | SPY | RSP | Equalweightminuscapweight(arithmeticpp) |
|---|---:|---:|---:|
|5sessions|−1.968%|+0.493%|+2.461pp|
|20sessions|+0.205%|+1.227%|+1.022pp|
|63sessions|+3.107%|+1.165%|−1.942pp|

The63-session**RSP/SPYratiochangeis−1.883%**,distinctfromarithmeticreturngap−1.942pp. VULCAN'sinstrumentusesratiochange;nofreshownergradeimposed. Existing10/15owner−2.83andearlier10/1−5.07staydated. RSP10/2→10/9**+1.578%**and10/9→10/16**+0.493%**;earlierseven-weekdeclinerunwasbrokenby10/9. Thus today'sS&Pnarrowingcoexistswithrecentrotationtowardequalweight;notproofitkeepsworseningeachweek. Nasdaq100equalweighttodaynearcapweightfurtherlimitsblanketclaim.

Strictcurrent-basketMAaudit:above50d218/486completeobservations,**not218/503**;missing-session/coverageandsurvivorshiplimitspreventfulluniverseheadline. Initialskip-gapsMA/historycalculationpreservedinbreadth-summary-pre-audit.jsonandexplicitlysupersededbysession-audit.json. NeitherunstampedTradingViewnorcurrentbasketbackfilliscertifiedhistoricalindexbreadth. No newhigh/lowpopulationcensushere;Reuterslate-morningcountsnarrowlyattributedinHELPER.

## Implications and falsifiers

Observation: mostsampledS&Psecuritylinesdownwhilelargeweightedleaderscarryindexhigher. Inference: indexlevelaloneoverstatesparticipationinthatsnapshot;relianceonleadersincreasesexposuretoaleaderreversal. Notaprovencrashtimerorrecessionindicator. Smallerborrowerfundingpressureandratesensitiveequityweaknessarepotentiallinkswithcredit,notmeasuredcausalattribution. Credit/breadth/AIobservationsshareantecedents;NEXUSownsindependence/synthesis,noautomaticextrabreakvote.

Whatwouldweakenpersistentnarrowing: repeatedgreenindexdayswithmajorityadvancing,sustainedRSP/SPYrecoveryandwidersectorparticipation. Someofthiscounterevidencealreadyexistsinthe5/20dwindowandNasdaq100today. Whatwouldstrengthenit: comparableclosingcountsremainnegativeonindexupdaysandpersistacrosssessionswhileequalweightlosesrelativeground. Noinventedconsecutive-daythresholdorautomationinstalled.

Sources:https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx ;Yahoochart/sparkpublicresponses(parameters/actualclocksinsource-receipt/proxy-source-receipt);issuerdescriptionhttps://www.invesco.com/us/en/financial-products/etfs/invesco-sp-500-equal-weight-etf.html . Canonicalrawsourcebundle**sources.tar.gz**,memberhashesverifiedinsources-manifest.json;looseignoredcapturesareworkingcopies. Reproduce:extractbundlelocally,runanalyze.pythenaudit_breadth.py;pull.pyisnewlivecaptureandmustnotoverwritegradedvintagewithoutnewreview.

**Routing:**oneconsolidatedBOARD015;HENRYbreadthownerandLIQUIDtime-criticalbackupACTION;VIOLET/VULCAN/NEXUS/RED/PROMEINFO. ExistingS1/R7held;noownerthresholdorscorechanged. Recipientconsumption/publicationcheckedseparately. Bootpartial/previousgeneralobligationsremainLAST_COMPLETION.
''')
sid='SIG-W-20261019-015';bp='BOARD/'+sid+'-sp500-rebound-narrow-but-recent-equalweight-recovered.md';action=['HENRY','LIQUID'];info=['VIOLET','VULCAN','NEXUS','RED','PROME'];title='S&P rebound narrow:315/503 down; Nasdaq100 and recent equalweight provide counterevidence'
body='''Will-requested investigation. SSGA SPYholdings10/16→503tradableequitylines;all503Yahooquotes14:50–14:57ETOctober19:**186up/315down/2flat**(62.6%down),median−0.40%. SPY+0.57%versusRSP−0.23%;3/11sectorETFspositive. Currentholdings/security-lineproxy,asynchronousquotes,notofficialindexmembership/exchangebreadthorclose.

Counterevidence: QQQ+1.35%/QQEW+1.31%showsNasdaq100reboundparticipation. ThroughFriday10/16,adjusted5-sessionRSP+0.49%vsSPY−1.97%;20-session+1.23%vs+0.21%.63-sessionRSP+1.16%vsSPY+3.11%(ratio−1.88%,arithmeticgap−1.94pp). RSPpositiveweeks10/9and10/16breaktheearlierdeclinerun. AcuteS&Pdivergence,notuninterruptedall-indexnarrowing.

Fullsources/replay/caveats:AGENTS/WALTER/research/2026-10-19_breadth/RESULT.md;sources.tar.gz+memberhashes. No preciseindex-contributionfractioncertified;MA/historycoveragepartial. Rule9reviewagrees. Concentration/breadth/creditarenotindependentcausalvotes;noS1/R7regradeorcrashtimingclaim.

HENRY/LIQUID ACTION: integrateintoexistingmarket-mechanics/creditcomparison;HENRYowner,LIQUIDbackupbecauseownerSTATUS10/8stale. Retainrecentbroadeningcounterevidenceandscope/clocks. OtherrecipientsINFO. No newmonitor,launch,thresholdortrade.'''
header={'to':action,'action':action,'info':info,'from':'WALTER','date':'2026-10-19','timestamp':now,'dispatched':now,'signal_id':sid,'domain':'MARKET_VOL','signal_type':'divergence','cluster':'POSITIONING_VALUATION','cluster_secondary':'AI_INFRA_CAPEX','precedence':'IMMEDIATE','confidence':0.93,'entities':['SPY','RSP','QQQ','QQEW','SSGA','S&P 500'],'source':'Will explicit investigation; SSGA primary holdings; Yahoo quotes/history; Rule9 source/sanity review','dispatch_note':'HENRYbreadthowner10/8STATUSstale;LIQUIDtime-criticalbackupcomposedACTION. NoS1/R7gradeorindependentrootcount.','event_window':'closed'}
def yaml(v):return '['+', '.join(v)+']' if isinstance(v,list) else str(v)
with (R/bp).open('x') as f:f.write('---\n'+'\n'.join(k+': '+yaml(v) for k,v in header.items())+'\n---\n\n# '+sid+' — '+title+'\n\n'+body+'\n')
def app(path,row):
 with (R/path).open('a') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow(row)
app('AGENTS/WALTER/routed/route_log.tsv',[now,sid,'Will investigation / SSGA / Yahoo / Rule9',title,'IMMEDIATE',','.join(action),','.join(info),'0.93'])
for who in action+info:
 role='ACTION' if who in action else 'INFO'
 if who=='PROME' or (who=='RED' and role=='INFO'):continue
 hp=f'AGENTS/{who}/inbox/WALTER/{sid}.md';(R/hp).parent.mkdir(parents=True,exist_ok=True)
 with (R/hp).open('x') as f:f.write(f'# {sid} — {title}\nBOARD: /{bp}\nPriority: IMMEDIATE\nRole: {role}\nFrom: WALTER\nDate: 2026-10-19\n\n## Kernel\n{body}\n\n## Why you got this\nExistingbreadth/vol/concentrationorcreditcomparisonlane;no newstudy.\n\n## Requested action\n'+('Integrateintocurrentworkretaininguniverse/clocksandcounterevidence;no newmonitororgradecommissioned.' if role=='ACTION' else 'INFOonly;nodirectedwork.')+'\n\n## Confidence / caveats\n0.93forthedatedsnapshot,notpersistence/causalityorofficialindexclose. Recipientconsumptionseparate.\n')
 app('AGENTS/WALTER/routed/delivery_log.tsv',[now,sid,who,role,'CODEX','IMMEDIATE',hp,'written_not_delivered_pending_push','Create-only;foreignworkingtree,pushdeferred;nativeindependenttransportUNKNOWN'])
print('Created015;rawbundle',len(manifest),'members;bodywordcount',len(body.split()))
