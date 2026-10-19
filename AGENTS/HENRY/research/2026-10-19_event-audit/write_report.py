from pathlib import Path
import json,csv
P=Path(__file__).resolve().parent
R=list(csv.DictReader(open(P/'sensitivities.csv')));E=json.load(open(P/'events.json'))
def row(s,w,sc,c='both_up'):return next(r for r in R if r['symbol']==s and r['window']==str(w) and r['scenario']==sc and r['condition']==c)
def pct(x):return f'{float(x)*100:+.2f}%'
def cell(s,w,sc):
 r=row(s,w,sc);return pct(r['stock_retained_return'])+'; '+r['losses']+'/'+r['eligible']
text='''# Four-name event audit — October19 frozen close

Mosaic remains the strongest residual weak-stock case; ADM remains weaker on most retained up days but its20-session decline is sensitive to one day. HII’s negative total returns fail a simple worst-day robustness check even though its up-day loss counts persist. Copart’s small60-session loss reverses under earnings and worst-day exclusions, and its acquisition leaves too few20-session observations after broad event removal. None establishes financing-driven weakness, ordinary rotation, or a rally-ending call.

This is a completed **bounded diagnostic**, not an exhaustive news census or causal event study. Original501-name screen and eight-name cohort remain immutable. Same October19endpoint:5/20/60sessions beginOctober12/September21/July24. Adjusted SPY and sectorETF returns define up days; strict negative stock return defines loss. Source daily rows frozen at prior study. No prediction, threshold, position, trade, standing monitor or owner priority changed.

## Comparison sheet

Each cell below: **retained-day cumulative stock return; losses / days when BOTH index and sector rose**. Baseline is the original chronological window. Excluded-day products are descriptive subsets, not corrected returns or a feasible strategy. Index/sector returns are removed on exactly the same dates, available in216-row `sensitivities.csv`; all separate index-up/sector-up counts and lag counts remain there.

|Name/window|Baseline|Earnings only removed|Captured events removed|Worst decline removed|Events + worst removed|
|---|---|---|---|---|---|
'''
for s in ['MOS','HII','ADM','CPRT']:
 for w in [20,60]:text+='|'+s+'/'+str(w)+'|'+'|'.join(cell(s,w,sc) for sc in ['baseline','earnings','events','worst','events+worst'])+'|\n'
text+='''
**Residual after events + worst, separate conditions:**

|Name|20index-up|20sector-up|20BOTH-up|60index-up|60sector-up|60BOTH-up|
|---|---|---|---|---|---|---|
'''
for s in ['MOS','HII','ADM','CPRT']:
 vals=[]
 for w in [20,60]:
  for c in ['index_up','sector_up','both_up']:
   r=row(s,w,'events+worst',c);vals.append(r['losses']+'/'+r['eligible'])
 text+='|'+s+'|'+'|'.join(vals)+'|\n'
text+='''
The original BOTH-up minimum eligible counts are5at20sessions/15at60sessions. MOS and ADM still meet these at events+worst; MOS60BOTH8/15 is just over half, not overwhelming. CPRT20BOTH2/3 fails the floor and60BOTH8/14 also fails. HII passes these counts but its worst-only retained returns are positive. The separately labelled broad ±1session halo leaves MOS60BOTH7/13 and ADM9/14, below the original floor; it cannot certify persistence. HII halo also thins to13, CPRT to13. Do not treat these exhausted samples as a clean falsification or confirmation.

## Interpretation and competing explanations

|Name|Diagnostic classification|Evidence and limits|
|---|---|---|
|Mosaic (MOS)|Persistent unexplained residual **within the main retained sample**, alongside documented operating/industry problems|20/60returns remain negative after earnings, captured events, worst-only and events+worst; all three loss majorities persist. Supply/cost curtailments and layoffs are plausible operating mechanisms; incomplete news/peer coverage prevents exclusion of company or industry causes. Broadhalo denominator fails. Completed debt issuance counters inability-to-borrow, not all financing pressure.|
|ADM|Persistent unexplained residual, **fragile economic magnitude**; industry mechanism unresolved|20retained worst-only−0.35%,60−2.42%; all three loss majorities remain. Earnings/guidance were positive, funding completed. October9USDA release coincides with largest20loss, but lower crop prices do not mechanically imply lower processing margins. No verified stronger industry/size control; halo thins belowfloor.|
|HII|Insufficient evidence for robust persistent negative performance; conditional weakness survives|Worst-only20+0.31%,60+0.75% while BOTHloss counts stay5/7and13/22 because the worst days were both-down. Removing favorable earnings/contracts makes residual performance worse; that is mechanical subset selection, not evidence the announcements caused earlier losses. Raised shipbuilding revenue/earnings and new contracts are counterevidence to operating deterioration.|
|Copart (CPRT)|Company-event-sensitive weakness; insufficient evidence for persistent unexplained or financing weakness|Removing mapped earnings session alone turns60return+1.09%; worst-only60+2.62%; broad event20sample only3BOTHdays. Earnings decline, ACV cash acquisition and material CEO award are separate company exposures; no identified causal split. Five-day stock recovery+3.89% and completed/refinanced facility oppose a blanket distress story.|

Five-day baseline: MOS−4.93%,HII+2.12%,ADM+0.11%,CPRT+3.89%; onlyMOSrepeated losses with2eligibleBOTHdays. After events+worst, MOS has zero eligible5dayBOTHobservations; no short-horizon persistence verdict. Equal-weight recovery remains counterevidence: RSP5/20/60+0.10/+0.34/+0.30%, SPY−1.49/−0.91/+3.99%. Current membership, one price vendor, outcome selection, overlapping windows, industry/product mix and small denominators all travel.

## Dated company timelines and chronology corrections

**MOS:** [August4Q2](https://www.sec.gov/Archives/edgar/data/1285785/000128578526000109/pressreleaseq22026-ex991.htm) netloss$272.8M, adjustedEPS$0.13; sulfur affordability/availability, reduced phosphate output, third-quarter sulfur$705/longton and capexcut$1.2B are operating explanations. Actual release clock unresolved, soAug4+5removed conservatively. August10tender announcement; August14pricing; August17final results and **completed$2Bnotes** (5.35%2031/5.65%2034/5.90%2036, net~$1.9833B), August28redemption notices for portions of2027/2028debt scheduledSeptember28. Notice is not proof later redemption completed. September23leadership transition/calendar notices are not performance events. [Florida primary WARN index](https://reactwarn.floridajobs.org/WarnList/Records?year=2026) records state notificationOctober14,199affected atSouthFortMeade,layoffDecember8. Do not map a secondary-reported October5letter to a public October5session; underlyingPDFdownload403. Unknownpublicclock mapsOctober14+15. Undated issuer Article archive confirms sulfur/operating constraints but cannot supply a dated shock. Potash not expanded beyond triage.

**HII:** [July29submarine award](https://www.globenewswire.com/news-release/2026/07/29/3335667/14858/en/hii-is-awarded-contracts-for-construction-of-block-vi-virginia-class-and-build-ii-columbia-class-submarines.html) was17:45ET; mapJuly30. July29stock−6.50% happened **before** that announcement. [July30Q2](https://www.sec.gov/Archives/edgar/data/1501585/000150158526000045/hii2026q2earningsrelease.htm), wire07:00ET, revenue$3.4B+10.9%,EPS$5.27, raisedshipbuildingrevenue$10.2–10.4B/reaffirmedFCF: favorable counterevidence; stock+14.09% that session. Additional production/automation/USV, August11$2.2Btaskorder, August15acceptancetrials→August17, September4afterclose strategy→September8(LaborDay), September11CVN82materials, September15airdrop taskorder, September22afterclose capacityexpansion→23, September29CVN79acceptance15:45ET→same versusRCOH/ROMULUScontracts17:15/18:30ET→30, September30Trumanarrival, October13AUKUS18:30ET→14, October19$99Mseatrialcontract/launcher demonstration. Wire archive provides clocks; issuer newsroom captures substantive releases where retrieved. Individual wire403responses retained; index timestamps are not full article retrieval. No date-specific explanation established forJuly29orSeptember28worstlosses.

**ADM:** [August4Q2](https://www.sec.gov/Archives/edgar/data/7084/000000708426000040/adm-ex991_20260630xq2.htm) adjustedEPS$1.84, GAAPEPS$1.87, net$908M; raisedyearadjustedEPSguidance. Public no later than SEC10:03ET, same session; call07:30CENTRAL=08:30ET, not07:30ET. August5underwriting known from August10filing; do not remove private agreement date without earlier public evidence. [August10completednotes](https://www.sec.gov/Archives/edgar/data/7084/000119312526342579/d102470d8k.htm):$500M4.829%2031+$500M5.269%2036; actual issuance demonstrates access. Unknownreleaseclock mapsAug10+11. Director resignation/calendarnotices excluded as administration. [USDAOctober9WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report),12ET coincides with MOS/ADMlargest20losses; [October15ERSoutlook](https://www.ers.usda.gov/topics/crops/soybeans-and-oil-crops/market-outlook) increases soybeanproductionforecast27Mbushels to4.56B, leavescrush2.78Bandfarmprice$12unchanged. Industry news is an alternative, not automatically a removed company event or a cause identified by daily close. A USDA source is not an extra independent financing signal.

**CPRT:** September10Q4revenue+2.4%, netincome attributable−17.4%; [September1issuer notice](https://www.copart.com/content/us/en/press-releases/copart-to-release-fourth-quarter-2026-results) scheduledearningsafter16ET, actualdatedrelease/20:16ET8K supports mappingSeptember11 (exactactualreleaseclock not recovered). September10agreementtoacquireACVabout$1.9Bcash separateclockunknown→Sep10+11, so do not attribute theSeptember10regular-session decline to aftercloseearnings. September17tender; September29disclosedSeptember28HSRwithdraw/refile/lawsuits→Sep29+30, not privateSep28. October1and8tenderextensions,October14HSRclearance, **October16ACVcompleted**. Material20MCEOoptionaward grantedOctober14, first captured filingOctober16afterclose; unknownfirstpublicclockunionOctober16+19, not mechanically backdated to grantOctober14. Awards require shareholderapproval; strikes$26.27/$35.03/$43.78/$52.54,four5Mtranches. This is material compensation, included alongside acquisition events; ordinarydirector/presidentchanges excluded.

**Explicit Copart correction to earlier frozen RESULT line72:** proposed-only language there was incomplete as ofOctober19. [October16closing exhibit](https://www.sec.gov/Archives/edgar/data/900075/000119312526423478/d129535dex991.htm) confirms acquisition completed; tenderexpiredOctober15at17ET,116,818,409shares/68.43%tendered. [July31annual filedSeptember29](https://www.sec.gov/Archives/edgar/data/900075/000119312526405731/cprt-20260731.htm) also reportsJanuary23,2026replacement of prior securedDecember2026revolver by unsecured$1.25BfacilitymaturingJanuary23,2031;July31unused$1.2275Bafter$22.5Mletters, covenantcompliance **asofJuly31**, not certifiedpost-acquisitioncash/drawability. PublicationSeptember29cannotselectSeptember21formation shares; the replacement event itself predates this60-sessionwindow. LIQUID independently flagged both updates in its consumed-shortlist packet, now read. Exact funding/cash bridge remains LIQUID’s work; do not confuse completed transaction with an audited latest funding bridge. Originalreport preserved as a versioned record, this explicit erratum governs current interpretation.

## Bounded peer extension

Four equity candidates, twoFXseries; no accepted new control. Old pool and rejected matches preserved.

|Case/candidate|Observed20/60performance|Disposition|
|---|---|---|
|MOS/ICL|−8.61/−6.64% vsMOS−25.55/−18.96%;20MOS-mappedBOTHloss3/7vs6/7|Return/conditionalstrengthpasses. FourAugust5SEC6Ksretrieved; financialstatement count recovered is weighted-averageEPSshares, not verifiedperiodendcount. Economic-common/unit/formation-size not certified: comparison candidate only, no forced match. Fertilizer/mining/geography mix matters.|
|HII/Fincantieri,FCT.MI|October19adjustedcloseNULL|Do not fill withunadjustedmetadataquote orOctober16close. Half-yearprimaryendpoint404; foreigncalendar/FX andsize unresolved. No usable frozen comparison.|
|ADM/Wilmar,F34.SI|Local−6.03/−10.62%;20USD−6.30%,60USDunavailable(July24FXmissing)|Alreadyweaker20thanADM−3.44%; failsrequired20strengthtest. Primaryhalfyearendpoint404; no needforce60FX/size. Foreigncloseasynchrony/mixcaveats retained.|
|CPRT/ACVA|No independentOctober19price|AcquiredOctober16, alreadydealaffectedSeptember21. Excludeasindependentoperatingcontrol, not a stronger peer selected from dealarbitrage.|

## Audit trail / limitations

`events.json`:49issuer/state entries including administration; explicit date/mode/source/removedsession mapping. `sec-inventory.json` and `filing-receipts.json`:all21in-scope8-K/8-K-A/10-Q/10-Kdocuments HTTP200, withfurther8tenderforms. `filing-dispositions.csv` inventories why annuals, duplicates and administration do or do not add a new event. This is a bounded SEC/issuercapture, not all public information. Dynamic issuer indexes/403individualwirecaptures/underlyingWARNPDF/foreign404s leave material coverage gaps. Earliest public time unknown where marked; unknownclock unions can remove favorable days and shrink denominators. No absence-of-news claim. Broadhalo is a deliberately more destructive sensitivity, not extra evidence.

`analyze.py` reproduces340frozeninputrows and216scenario-conditionrows; sign flags, counts and independentlog-sumproducts checked; `worst-days.json` specifies per-window minimumreturndate before removal, not chosen to rescue a label. OriginalCOHORTsha278210be… andrepeatRESULTsha7667de05… assertions pass. Fullinputsources retained in `sources.tar.gz` with SHA256manifest. To reproduce from checkout, use repository `.venv/bin/python` (bs4 installed), run `analyze.py` and `peers.py`. They read the committed prior `daily-audit.csv.gz` and this source archive directly when raw captures are absent. No automatedtests added for low-impact narrative changes; arithmetic/receiptintegritychecks are direct.

LIQUID owns dated terms/maturities/usable funding versus costs, companyownersoperatingnews; WALTER assembles explanations; VIOLET checks existing volatility work without treating shared causes as independent signals. No causal credit coefficient, crash odds, trade or regrading of CRU-11. Durablepacketdelivery and actualexact-versionconsumption recorded separately; nativefleetnotification/closeouttransport remains unavailable. No Willdecision needed.
'''
(P/'RESULT.md').write_text(text)
# Explicit filing census disposition, not indiscriminate form-date deletion.
F=[]
for x in json.load(open(P/'filing-receipts.json')):
 f=x['filing'];kind='Event/capital/earnings: see events.json, known announcement mapped rather than later filing'
 if f['form'] in ['10-Q','10-K']:kind='Periodic filing read; no incremental event assumed solely for form date; CPRTfacility supersession noted, replacement eventJan23outsidewindow'
 if f['items']=='5.02':kind='Ordinarypersonnel excluded; CPRTOct16material20Maward exception INCLUDED'
 if f['form']=='8-K/A':kind='Routinepresidentcompensation amendment excluded'
 F.append(dict(symbol=x['symbol'],filing_date=f['filingDate'],report_date=f['reportDate'],acceptance_utc=f['acceptanceDateTime'],form=f['form'],items=f['items'],http=x['status'],url=x['url'],disposition=kind))
with (P/'filing-dispositions.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(F[0]));w.writeheader();w.writerows(F)
print('Report written',len(text),'bytes; filing dispositions',len(F))
