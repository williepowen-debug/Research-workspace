# TRADE IDEA — FXY January58/60 bull-call spread — yen diversification, weakest current case
**Setup ID:** `IDEA-FXY-OCT20`
**Terry verdict:** SHELVED — retired from daily checks (Will in the TERRY window 2026-10-29 11:50 ET: "You can retire them but I would want them to still exist where I can view previous ideas"); never approved, nothing armed; listed on `IDEA_SHELF.md` for look-back; revived only by Will's word, then re-priced from scratch.

**Prior verdict (superseded 2026-10-29 11:50):** CONDITIONAL — NOT-FIRED; unapproved proposal.
**Prepared:** 2026-10-20T11:59:53.683072-04:00. Commissionff9531ffc, Will'srecorded11:50ETword.
**Thesis-owner evidence:** SAM October20committedad61cfd5: nofreshcarryunwind, retired-toLOW/no successor, BOJfurtherhikesintendedbutOctoberunsignalled; OctoberOIS5%indicativemedian isnot a simple forecastprobability. No existingSAMtriggerrevived. TERRYconditionalconstructiononly.

> **RE-GRADE 2026-10-23 (TERRY, 19:0x ET from `date`):** breakout MET on the 10/22 close (58.44 > prior-20 high 58.30); a red FXY session came **10/23** (−0.03%, close 58.42 ≥ 58). Closing-chain screen 58C 1.30/1.60 · 60C 0.45/0.60 ⇒ mid $0.925 / worst $1.15 > the $0.90 cap ⇒ **entry blocked by its own chase cap**. Still armed for a later red FXY day ≥ $58 at ≤ $0.90. No order; card unapproved. Evidence `../research/2026-10-23_slate-regrade/NOTE.md`.

## Entry and trigger state
NOT-FIRED: completedFXYclose>58.30 (prior20closehigh), thenredFXYentrywithprice≥58.00and brokerdebit≤0.90. Lastcompleted57.79 is0.51/0.883%below58.30; live57.92still0.38/0.656%below; liveUSDJPY158.19iscontextonly, notanewSAMgate. Cheapestmarkisnotyenconfirmation.

## Instrument, size and maximum loss
2027-01-15BUY58C/SELL60C,1complexspread; netlimit0.90+1.30openingfees⇒91.30maximumoptionloss. Screenlongask1.60−shortbid0.35=1.25⇒126.30; needs0.35/28%debitimprovement. Longlegwidth66.67%, OI956/8405/vol1/91; guardpassesbutliquiditynotattractive.

## Edge and alternatives
Watchpriorityonly. Yenstrengthhasdifferentfirst-orderdriverfrombankcredit/oil, but SAMhasnotobservednewdisorderandlongFXYcanloseonpersistentUS-JPratedifferential. Proposedtighterpriceoffersbetterpayoffshape, not establishedpositiveexpectancy; no reason to paypresentwidequote.

## Exit, target and invalidation
Exitwhole1 at executablecomplexbid≥1.40 (netgain47.40assuming1.30eachwayfees), or completedFXYclose<57.68 (prior20low), or spreadbid≤0.45 (plannedloss47.60includingroundtripfees, not guaranteed); endofviewDecember18,2026. No roll/add. Theoreticalmaximumprofit108.70beforeclosingcosts; terminalbreak-even58.913includingopeningfee. NoOctoberBOJsurprisebetorautomaticmeetingprobabilitytrade.

## Book concentration and independence
Currencyexposurepotentiallydiversifiesthehot-Mideastsleeve,butoilimportshockcanweakenyen andUSdollarhavendemandcanoverwhelmJPY; no guaranteedcrashhedge. OverlapwithIEFthroughrate-spreadnarrowsandGLDthroughUSD; N_claimed1/N_eff1yenview, notindependentcarrycrashvote.

## Day colour
FXY+0.22%: call-entrydaycolourNOTMET. No measuredrootrule#6break. Currentdirectionandliquiditybothfail; a smallerlossbudgetdoesnotfixmissingedge.

## Evidence and counter-case
[InvescoFXY](https://www.invesco.com/us/en/financial-products/etfs/invesco-currencyshares-japanese-yen-trust.html) tracksJPYlesscosts;0.40%expensefromissuersearchrender, dynamicfullpagehadnointerestfield. CurrentdeposityieldUNKNOWN; donotassumeBOJratepassesstraightthrough. No cashcarryusedinEV.

Sourcepinsat`../research/2026-10-20_trade-idea-slate-data/owner-source-pins.json`; all59completedbarspertickerJuly28–October19,separateincompleteOctober20barexcludedfrom20sessionanchors. Tickerhistorycompletewithininteriorgapscan, notproofthereturnedspanhasallrequestededges. Quotes/chainrawfiles/chartcalculationsinthe same datadirectory. Long-wingssellupsideatshortstrike;limitedriskdoesnotmakeaprofitguaranteed.

## Shared execution and authority conditions

Quote retrieval **2026-10-20T11:55:17.584207-04:00** (ET); each equity/currencyquote's payload hasdateonly, so retrievalclock isnot an exchangequote timestamp. Optionchains retrievedOctober20 **11:54:43–44ET**, per-filefetch_ts/spot_asof; vendor bid/asktimestamps/delayflags unavailable, lastTrade is not freshness. No brokerconnector. Namedlegchecksreturned0 withnoLOCK/XSD/DEAD/NOBID onplannedlegs; chain-wideNONMONOadvisorydoesnotcertifyliquidity. Brokerdelta/theta/IVrank/expectedmove, complexquote, exactfees, suitabilityandfullbook/orders remainmissing. **Vendorquotes are screening, not executabletickets.**

Allthresholdsaboveare **PROPOSED CARD CONDITIONS**, not registeredfleetgates or silentchanges toanowner'skill. Triggerpermission, ownerthesis and operatorapprovalaredifferent. **NOT-FIRED; nofillapproved.** Will's11:50wordloosensproposalpermissiononly. **X1stillCLOSED/DON'T-SIZE:** a fillagainstthatrestrictionneedsWill'sexplicitnamedper-cardchoice; thisslatedoesnotwaiveit. Defaultmaximum500/cardretained; no automaticlargersizeorKellyclaim. Actualproposeddeployment0untilapproval. Neither diversificationnorapositivetarget/stopratio provesEV. Thesearealternativeideas, not abundle or acatch-up-P/Ltarget.

Foroptions, tradeonlyasonebrokercomplexorder, nevernakedleg;multiplier100andstandarddeliverableassumedandmustbeconfirmed. Feeassumption0.65/contract/sideisbudgetarithmetic, not anaccountcertification. Cappedterminalpayoffpresumesmanagedintactspread; earlyassignment/brokerinterventioncancreatecash/shareobligations/extraexpenses. Newcardtime-stopsdefineprospectiveviewhorizons; noheld-lineexpiryreminderorautomaticC5commission. No restingorderplaced, fillinferred, automaticroll, monitororscorecreated. Reviewatthenextrequesteddesktouchoractualmaterialownerchange; nofollow-upnagging. Entryprices/conditionsinvalidatedbynewbrokerbook/quotesorsourcekill.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.** ChoicesrouteviaPROMEforregistrationbeforeanyWill-facingdecisionask.
