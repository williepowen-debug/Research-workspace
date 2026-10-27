"""One-time manually reviewed source notes. No Gmail, Git or live sends."""
from pathlib import Path
import json,runpy
OUT=Path(__file__).resolve().parent.parent/'2026-10-27_realestate-processing'
OUT.mkdir(exist_ok=True)
def card(slug,title,domain,cluster,action,info,confidence,sources,body,**extra):
 return dict(slug=slug,title=title,domain=domain,cluster=cluster,action=action,info=info,confidence=confidence,sources=sources,body=body,**extra)
cards=[
card('trepp-seasoned-pool-correction','Trepp reverses lending-quality inference after excluding seasoned pool','CMBS','CRE',['CREED','HOMER'],['REGINALD','CARL','RED'],.88,
['https://crenews.com/subject/research-res/','https://crenews.com/2026/10/16/credit-metrics-for-2026-cmbs-loan-originations-appear-to-improve/'],
'''Trepp's delivered October 20 newsletter corrects its October 16 conservative-lending interpretation: a $1.3B seasoned/amortized multifamily pool skewed the year-to-date securitization sample. Excluding it, median aggregate LTV is 63.2% versus 59.3%; debt yield 10.32% versus 10.39%; DSCR 1.54 versus 1.50. Multifamily LTV is 67.4% versus 61%, with weaker debt yield and coverage. The pool's weighted-average LTV was 40.8%.

This is a correction by the publisher, not an independently replicated constituent calculation. Securitized this year does not mean originated this year. The public index corroborates the skew issue; the original article returned 403. Both delivered emails survive locally. This does not revise a prior WALTER conservative-lending card.

CREED ACTION: reconcile the vendor's sample correction with existing national CMBS coverage. HOMER ACTION: retain the multifamily cohort distinction in existing coverage. No owner grade or new research program.'''),
card('denver-watchlist-current-loans','Denver watchlist stress: most flagged balance remains current','multifamily','CRE',['HOMER'],['CREED','REGINALD','CARL','RED'],.97,
['https://www.trepp.com/trepptalk/denver-multifamily-watchlist-credit-stress'],
'''Trepp's October 20 analysis reports September Denver securitized multifamily watchlist balance of $3.83B out of $28.24B (13.6%), versus 1.13% delinquency. Crucially, 98% of watchlisted balance is current. Watchlist occupancy declined from 94.3% to 86.5% and DSCR from 1.47 to 1.19; $1.32B, or 34.5% of watchlist balance, has DSCR below 1.

These are vendor-defined securitized/watchlist populations, not a census of Denver apartments or $3.83B of defaults. Original loan-level servicing data were not inspected. Confirmed means the retrieved primary vendor analysis states these figures, not independent replication.

HOMER ACTION: reconcile with existing multifamily coverage, preserving current-versus-watchlist-versus-delinquent distinctions. CREED/REGINALD information only; no bank loss attribution, grade change or new monitor.'''),
card('cred-iq-modeled-refi-equity','CRED iQ estimates future multifamily equity needs, not current defaults','multifamily','CRE',['HOMER'],['CREED','REGINALD','CARL','RED'],.96,
['https://cred-iq.com/blog/2026/10/15/maturing-apartment-debt-refinance-gap/'],
'''CRED iQ's October 15 model covers $136B of fixed-rate Fannie/Freddie/CMBS apartment loans maturing October 2026–December 2028. It estimates 23% of loan count / 31% of balance needs $6.8B equity. Assumptions: 2025 NOI, 1.25 DSCR, 30-year amortization and refinancing coupons +25bp. Floating SASB, CRE CLOs and cooperatives are excluded. Printed SOFR endpoints differ by 23bp; the scenario uses 25bp. This is future proceeds modeling, not existing fixed-rate loans resetting or observed defaults.

Current 20 Exchange Place's $246M Freddie loan is modeled at $183M proceeds/$63M gap; that does not establish delinquency. Separately, the article reports Park West Village (New York, NY; 850 units, seven conduit deals) modified by its special servicer in November 2025, DSCR 1.34 underwritten versus 0.61 year-end 2025, maturity August 2027. Underlying servicer records were not read; modification is historical, not a new October default.

HOMER ACTION: reconcile within existing coverage, separating modeled refinancing needs from Park West's attributed historical modification. No bank loss estimate or owner grade.''',case=['Park West Village, New York NY']),
card('udr-apollo-conditional-jv','UDR–Apollo apartment venture: announced equity terms, conditional close','multifamily','CRE',['HOMER'],['CREED','REGINALD','CARL','RED'],.99,
['https://www.sec.gov/Archives/edgar/data/74208/000007420826000081/udr-ex99d2.htm'],
'''UDR's October 21 issuer release announces an intended joint venture comprising 19 communities / 7,059 homes at approximately $2B valuation. Apollo-managed funds and affiliates would invest $1.34B equity for roughly two-thirds ownership; UDR retains one-third, consolidation and management fees. Implied capitalization rate is approximately 6%. The contemplated repurchase option carries a 7–7.5% fixed return during a finite window starting in the fifth anniversary year.

Closing is expected October 29, subject to documentation and customary conditions. As of October 27 this release proves announced terms, not closing or funded proceeds. Equity must not be relabeled private-credit lending. The newsletter's 634-properties description is erroneous: the release identifies 634 homes under development.

HOMER ACTION: reconcile the announced valuation/capital terms with existing apartment coverage, retaining the conditional closing status. No new study, default finding, trade or owner grade.'''),
card('cbre-revenue-volume-bases','CBRE Q3: sales and leasing revenue growth does not establish transaction volumes','CRE services','CRE',['CREED'],['REGINALD','RED'],.98,
['https://www.sec.gov/Archives/edgar/data/1138118/000113811826000028/cbre-20261022x8kexx991.htm'],
'''CBRE's October 22 Q3 release reports revenue $11.517B (+12.7%) and net income $443M (+22%). Global property-sales revenue rose 28%, US property-sales revenue 37%, and industrial-leasing revenue 16%. These revenue measures are not transaction-dollar volume or leased square footage.

Critical-infrastructure-services revenue rose 80%, including acquired Pearce's contribution; this is not organic data-center volume growth. The broader infrastructure revenue figure uses a different perimeter. Project management was tempered by slower corporate real-estate capital spending.

The newsletter's delayed-deals/2027 forecast is attributed to the earnings call. That call was not read; the retrieved release does not verify the forecast. Absence from the release does not disprove what was said on the call.

CREED ACTION: reconcile the primary revenue bases with existing CRE coverage. Keep the call-derived forecast as an explicit source gap. No inference of property volumes, AI capex commitments or a new owner grade.'''),
card('chicago-office-rollover-cases','Chicago tenant rollover: whole-loan exposure and two attributed distress cases','office CMBS','CRE',['CREED'],['REGINALD','RED'],.90,
['https://www.trepp.com/trepptalk/chicago-office-tenant-lease-expirations','https://www.cbre.com/properties/properties-for-lease/office/details/US-SMPL-65417/westbrook-corporate-center-tower-2-2-westbrook-corporate-center-westchester-il-60154','https://continental-towers.com/contact/'],
'''Trepp's October 22 analysis associates $802M of Chicago-area securitized office debt with 48 significant tenant leases across 30 properties expiring before maturity; median lead is 20.5 months. Significant means largest tenant or at least 10% of NRA. These are full associated loan balances, not tenant-specific balances or expected losses. The broader top-five-tenants screen ($2.16B/44 properties) overlaps and must not be added. Four properties represent $623M/78% of the narrower exposure.

The table reports Westbrook Corporate Center (Westchester, IL), $85M, foreclosure, with Ingredion occupying 10.75%; and Continental Towers (Rolling Meadows, IL), $85M, over 90 days delinquent, Verizon 17.55%. The primary table's maturity months differ from the email/helper summary; use the table pending original-record reconciliation. Statuses are attributed as of the article, not newly dated foreclosure/default events. Court and original servicer records were not read. Official property pages establish municipality only.

CREED ACTION: reconcile these named cases with existing coverage, preserving source-date, status and exposure limits. No bank attribution or owner grade.''',case=['Westbrook Corporate Center, Westchester IL','Continental Towers, Rolling Meadows IL'])]
for c in cards: c['domain']='BANK_CRE'; c['cluster']='BANK_COLLATERAL'
(OUT/'cards-reviewed.json').write_text(json.dumps(cards,indent=2)+'\n')
old=Path(__file__).with_name('write_reviewed_cards.py').read_text()
(OUT/'write_reviewed_cards.py').write_text(old.replace('2026-10-27_realestate-mail/SOURCES.md','2026-10-27_realestate-processing/SOURCES.md'))
runpy.run_path(str(OUT/'write_reviewed_cards.py'),run_name='__main__')
