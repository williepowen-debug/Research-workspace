from pathlib import Path
from bs4 import BeautifulSoup
import requests,json,concurrent.futures
p=Path('AGENTS/HENRY/research/2026-10-19_event-audit');jobs=[]
for i in [0,2,3]:
 s=BeautifulSoup((p/f'raw/HII-wire-{i}.html').read_text(),'html.parser')
 for el in s.select('.newsLink'):
  a=el.select_one('.mainLink a');stamp=el.select_one('.date-source span')
  if not a or not stamp:continue
  title=a.text.strip();clock=stamp.text.strip();jobs.append({'name':'HII-'+a['href'].split('/')[5], 'url':'https://www.globenewswire.com'+a['href'],'title':title,'clock':clock})
jobs.append({'name':'CPRT-earnings-clock','url':'https://www.copart.com/content/us/en/press-releases/copart-to-release-fourth-quarter-2026-results'})
x=json.load(open(p/'raw/ICL-submissions.json'));r=x['filings']['recent']
for i,d in enumerate(r['filingDate']):
 if d=='2026-08-05' and r['form'][i]=='6-K':jobs.append({'name':'ICL-'+r['accessionNumber'][i][-6:],'url':'https://www.sec.gov/Archives/edgar/data/941221/'+r['accessionNumber'][i].replace('-','')+'/'+r['primaryDocument'][i]})
def f(j):
 try:
  r=requests.get(j['url'],headers={'User-Agent':'Henry Research analyst research@example.com'},timeout=25);name='raw/final-'+j['name'];(p/(name+'.html')).write_text(r.text);(p/(name+'.txt')).write_text(BeautifulSoup(r.text,'html.parser').get_text(' ',strip=True));return dict(j,status=r.status_code,file=name+'.html')
 except Exception as e:return dict(j,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:out=list(ex.map(f,jobs))
(p/'final-fetch-receipts.json').write_text(json.dumps(out,indent=2));print('captures',len(out),'non200',[j for j in out if j.get('status')!=200])
