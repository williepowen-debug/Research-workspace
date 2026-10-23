# TRADE IDEA — RSP January215/225 bull-call spread — broad participation rather than another short
**Setup ID:** `IDEA-RSP-OCT20`
**Terry verdict:** CONDITIONAL — NOT-FIRED; unapproved proposal.
**Prepared:** 2026-10-20T11:59:53.683072-04:00. Commissionff9531ffc, Will'srecorded11:50ETword.
**Thesis-owner evidence:** HENRY October19: narrowMondayrebound, improvingequalweight/Nasdaqparticipation counterevidence, negativegamma/fragility. Not a confirmedbullregime; TERRY proposes a breadth-dependentconstruction, not a newHENRYforecast.

> **RE-GRADE 2026-10-23 (TERRY, 19:0x ET from `date`):** confirmation MET on the 10/20 close (215.86; RSP/SPY 0.280684 > 0.280498) and again 10/22; the first red RSP session after it was **10/23** (−0.77%, close 216.54). Closing-chain screen 215C 6.30/10.30 · 225C 2.35/3.50 ⇒ mid $5.38 > the $4.90 cap ⇒ **no qualifying entry**; on the card's letter ("first red session") the entry case is spent; re-opening needs a rework. No order; card unapproved. Evidence `../research/2026-10-23_slate-regrade/NOTE.md`.

## Entry and trigger state
NOT-FIRED: requireacompletedRSPclose>215.00 AND same-dateRSP/SPYratio>0.280497871 (prior20alignedclosemax), thenfirstredRSPentrysessionwithRSP≥215 and brokerdebit≤4.90. LastcompletedRSP213.40 is1.60below; ratio0.278415614 is0.002082257/0.748%below. Current215.67clearspriceintraday0.67, but pairedintradayratio0.280123651 isunsynchronized/NOTtheclosingresolver; nopartialgradeasfinal. Debit5.45needs0.55improvement.

## Instrument, size and maximum loss
2027-01-15BUY215C/SELL225C,1complexspread, netlimit4.90; opening1.30feeassumed ⇒491.30maximumoptionloss. Screen7.50longask−2.05shortbid=5.45 ⇒546.30, **46.30over500cap**; nofillatthisscreen. OI687/7583, vol4/76; no namedlegfatalflag.

## Edge and alternatives
Conditional participation trade, not proof the market is cheap. Broad equityrally can pay while currentbankputsoilviewfails. Atactualoutermarkets thestructureisoverdefaultbudget; displayedmid4.925wouldstillcost493.80butisnotafill. Needpricedcomplexorderinsidecurrentmarket; nocalibratedpositiveEV/winprobability.

## Exit, target and invalidation
Exitwhole1 at executablecomplexbid≥8.00 (netgain307.40assuming1.30eachwayfees), or RSPcompletedclose<208.02 (prior20low), or spreadbid≤2.45 (plannedloss247.60inclroundtripfees, gapnotcappedthere); endofviewDecember18,2026. No roll/add. Theoreticalmaximumprofit508.70beforeclosingcosts, terminalbreak-even219.913includingopeningfee. No event-envelopereachclaim.

## Book concentration and independence
Offsetsdirection ofbank/QQQputs anddiversifiesawayfrommegacapweight, butstillUS-equityriskandfinancials/energyinsideRSP. AlsooverlapsVSTequityrisk; treatVST+RSPasa correlatedrisk-oncluster, nottwofullindependent500budgets. N_claimed1/N_eff1breadthview.

## Day colour
RSP+1.06%: call-entrydaycolourNOTMET. Requireconfirmationthenredentry; no artificialbreakusingearlierquotestaleness. No chaseabovebroker4.90debitcap.

## Evidence and counter-case
[InvescoRSP](https://www.invesco.com/us/financial-products/etfs/product-detail?productId=RSP) identifiesequalweightS&P500andquarterlyrebalance. Sectorcompositionnotmeasuredhere; no claimitexcludesfinancials/oil. Confirmedtrendnotinventedfromtodayintradaybreak.

Sourcepinsat`../research/2026-10-20_trade-idea-slate-data/owner-source-pins.json`; all59completedbarspertickerJuly28–October19,separateincompleteOctober20barexcludedfrom20sessionanchors. Tickerhistorycompletewithininteriorgapscan, notproofthereturnedspanhasallrequestededges. Quotes/chainrawfiles/chartcalculationsinthe same datadirectory. Long-wingssellupsideatshortstrike;limitedriskdoesnotmakeaprofitguaranteed.

## Shared execution and authority conditions

Quote retrieval **2026-10-20T11:55:17.584207-04:00** (ET); each equity/currencyquote's payload hasdateonly, so retrievalclock isnot an exchangequote timestamp. Optionchains retrievedOctober20 **11:54:43–44ET**, per-filefetch_ts/spot_asof; vendor bid/asktimestamps/delayflags unavailable, lastTrade is not freshness. No brokerconnector. Namedlegchecksreturned0 withnoLOCK/XSD/DEAD/NOBID onplannedlegs; chain-wideNONMONOadvisorydoesnotcertifyliquidity. Brokerdelta/theta/IVrank/expectedmove, complexquote, exactfees, suitabilityandfullbook/orders remainmissing. **Vendorquotes are screening, not executabletickets.**

Allthresholdsaboveare **PROPOSED CARD CONDITIONS**, not registeredfleetgates or silentchanges toanowner'skill. Triggerpermission, ownerthesis and operatorapprovalaredifferent. **NOT-FIRED; nofillapproved.** Will's11:50wordloosensproposalpermissiononly. **X1stillCLOSED/DON'T-SIZE:** a fillagainstthatrestrictionneedsWill'sexplicitnamedper-cardchoice; thisslatedoesnotwaiveit. Defaultmaximum500/cardretained; no automaticlargersizeorKellyclaim. Actualproposeddeployment0untilapproval. Neither diversificationnorapositivetarget/stopratio provesEV. Thesearealternativeideas, not abundle or acatch-up-P/Ltarget.

Foroptions, tradeonlyasonebrokercomplexorder, nevernakedleg;multiplier100andstandarddeliverableassumedandmustbeconfirmed. Feeassumption0.65/contract/sideisbudgetarithmetic, not anaccountcertification. Cappedterminalpayoffpresumesmanagedintactspread; earlyassignment/brokerinterventioncancreatecash/shareobligations/extraexpenses. Newcardtime-stopsdefineprospectiveviewhorizons; noheld-lineexpiryreminderorautomaticC5commission. No restingorderplaced, fillinferred, automaticroll, monitororscorecreated. Reviewatthenextrequesteddesktouchoractualmaterialownerchange; nofollow-upnagging. Entryprices/conditionsinvalidatedbynewbrokerbook/quotesorsourcekill.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.** ChoicesrouteviaPROMEforregistrationbeforeanyWill-facingdecisionask.
