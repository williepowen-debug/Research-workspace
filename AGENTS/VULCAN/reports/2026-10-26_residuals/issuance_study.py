"""Frozen four-parent USD registered-note inventory from saved SEC originals.
No price series, recurring collector, or assumed AI use-of-proceeds allocation.
"""
from pathlib import Path
import re,json,csv,datetime,collections
from decimal import Decimal
HERE=Path(__file__).resolve().parent; S=HERE/'sources'
# Settlement/close comes from each closing 8-K; exact maturity from final supplement.
DEALS=[
 ('GOOGL','2026-02-13','0001193125-26-051423','0001193125-26-046846',20),
 ('GOOGL','2026-08-10','0001193125-26-342390','0001193125-26-340264',25),
 ('META','2026-05-04','0001193125-26-204128','0001193125-26-201738',25),
 ('AMZN','2026-03-13','0001104659-26-027729','0001104659-26-027125',37),
 ('AMZN','2026-07-09','0001104659-26-082293','0001104659-26-081786',25)]
CIK={'GOOGL':1652044,'META':1326801,'AMZN':1018724,'MSFT':789019}
def norm(t): return re.sub(r'\s+',' ',t)
def url(t,a):
 row=next(r for r in json.loads((S/f'{t}-index.json').read_text()) if r['accessionNumber']==a)
 return f'https://www.sec.gov/Archives/edgar/data/{CIK[t]}/{a.replace("-","")}/{row["primaryDocument"]}'
tranches=[]; validation=[]
for tick,issued,closeacc,finalacc,expected in DEALS:
 close=norm((S/f'{tick}-{closeacc}.txt').read_text()); final=norm((S/f'{tick}-{finalacc}.txt').read_text())
 # Narrow to first operative list; never count repeated exhibit titles or a preliminary twice.
 start=close.find('The U.S. Notes consist of') if closeacc.endswith('051423') else close.find('The Notes consist of') if tick=='GOOGL' else close.find('completed an offering') if tick=='META' else close.find('closed the sale')
 assert start>=0,(tick,closeacc)
 end=close.find('The foregoing',start) if tick=='GOOGL' else close.find('pursuant',start) if tick=='AMZN' else close.find('The offering of',start)
 snippet=close[start:end]
 matches=re.findall(r'\$([\d,]+) aggregate principal amount of (?:its |our )?(.{0,65}?) notes due (\d{4})',snippet,re.I)
 assert matches,(tick,closeacc)
 total=Decimal(0);long=Decimal(0)
 for n,(amount,rate,year) in enumerate(matches,1):
  principal=Decimal(amount.replace(',','')); total+=principal
  pat=rf'{year}(?: floating rate)? notes (?:will mature on|:)\s*([A-Z][a-z]+\s+\d{{1,2}},\s+{year})'
  found=re.search(pat,final,re.I)
  assert found,(tick,year,finalacc)
  maturity=datetime.datetime.strptime(found[1],'%B %d, %Y').date(); issue=datetime.date.fromisoformat(issued)
  in_long=maturity>=issue.replace(year=issue.year+20)
  if in_long:long+=principal
  tranches.append(dict(issuer=tick,issue_date=issued,currency='USD',principal_usd=str(principal),rate=rate,maturity=str(maturity),original_term_days=(maturity-issue).days,tenor_20y_plus='YES' if in_long else 'NO',amount_basis='gross face principal',refinancing_allocation='UNKNOWN_GENERAL_CORPORATE',ai_allocation='UNKNOWN',close_accession=closeacc,final_accession=finalacc,source_close=url(tick,closeacc),source_maturity=url(tick,finalacc),locator='8-K Item 8.01 tranche list; final supplement maturity summary'))
 assert total==Decimal(expected)*10**9,(tick,total,expected)
 # Final supplement's cover includes each exact principal amount as an independent source check.
 for amount,rate,year in matches:
  assert '$'+amount in final[:20000],(tick,amount)
 validation.append(dict(issuer=tick,issue_date=issued,tranches=len(matches),gross_usd=str(total),long_20y_usd=str(long),closing_list_sum_matches_expected=True,final_cover_amounts_found=True))
with (HERE/'ISSUANCE_TRANCHES.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(tranches[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(tranches)
by=[]
for tick in ['GOOGL','MSFT','META','AMZN']:
 rr=[r for r in tranches if r['issuer']==tick];total=sum(Decimal(r['principal_usd']) for r in rr);long=sum(Decimal(r['principal_usd']) for r in rr if r['tenor_20y_plus']=='YES')
 by.append(dict(issuer=tick,gross_usd=str(total),long_20y_usd=str(long),long_share_pct=str(long/total*100) if total else 'NOT_APPLICABLE_NO_OBSERVED_ISSUE',tranches=len(rr)))
# Exhaustive filing-form scope account: all 424B2/3/5 are classified, not silently filtered.
coverage=[]
finals={d[3] for d in DEALS}
for tick in CIK:
 for r in json.loads((S/f'{tick}-index.json').read_text()):
  if r['filingDate']<'2026-01-01' or not r['form'].startswith('424B'):continue
  t=norm((S/f'{tick}-{r["accessionNumber"]}.txt').read_text());a=r['accessionNumber']
  if a in finals: state='INCLUDED_FINAL_USD_NOTES'
  elif 'subject to completion' in t[:2500].lower() or 'not complete and may be changed' in t[:2500].lower():state='EXCLUDED_PRELIMINARY'
  elif tick=='META' and r['filingDate']=='2026-10-26' or tick=='GOOGL' and r['filingDate'].startswith('2026-06') or r['form']=='424B3' or a.endswith('336853'):state='EXCLUDED_EQUITY_OR_MERGER'
  else:state='EXCLUDED_NON_USD_NOTES'
  coverage.append(dict(issuer=tick,accession=a,filed=r['filingDate'],form=r['form'],classification=state,source=url(tick,a)))
with (HERE/'ISSUANCE_SOURCE_SCOPE.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(coverage[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(coverage)
total=sum(Decimal(r['principal_usd']) for r in tranches);long=sum(Decimal(r['principal_usd']) for r in tranches if r['tenor_20y_plus']=='YES')
summary=dict(scope='Registered USD parent senior notes closed 2026-01-01 through 2026-10-26 ET; not all AI borrowing',issuers=by,total_usd=str(total),long_20y_usd=str(long),long_share_pct=str(long/total*100),tranches=len(tranches),deals=validation,prospectus_forms_classified=len(coverage),exclude_refinancing_from_gross=False,net_new_borrowing='UNKNOWN',ai_allocated_proceeds='UNKNOWN',exact_four_name_long_end_market_share='UNGRADEABLE_NO_EXACT_MATCHED_PUBLIC_DENOMINATOR')
(HERE/'ISSUANCE_RESULTS.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
