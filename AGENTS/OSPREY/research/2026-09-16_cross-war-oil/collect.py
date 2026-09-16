import urllib.request, json, datetime, pathlib, re, concurrent.futures
from html.parser import HTMLParser
ROOT=pathlib.Path(__file__).parent
URLS={
'securewest':'https://www.securewest.com/news/weekly-mts/weekly-maritime-incident-summary-08-14-september-2026/',
'insurance':'https://www.insurancejournal.com/news/international/2026/09/16/885279.htm',
'reuters':'https://www.reuters.com/business/energy/russias-syzran-saratov-oil-refineries-hold-after-drone-attacks-sources-say-2026-09-16/',
'ukrinform':'https://www.ukrinform.net/rubric-ato/4164723-russias-syzran-and-saratov-oil-refineries-halt-operations-after-drone-attacks-reuters.html',
'kyiv_diesel':'https://kyivindependent.com/ukraines-drone-strikes-force-russias-6-largest-diesel-refineries-to-halt-or-slash-output-reuters-reports/',
'moscow_refineries':'https://www.themoscowtimes.com/2026/09/16/syzran-and-saratov-oil-refineries-halt-operations-after-drone-attacks-sources-say-a93726',
'pravda':'https://www.pravda.com.ua/eng/news/2026/09/16/8053776/',
'bbg_mirror':'https://www.ttnews.com/articles/russia-boosts-oil-flows',
'ryazan':'https://www.themoscowtimes.com/2026/09/10/rosnefts-ryazan-oil-refinery-shuts-down-after-drone-attack-industry-sources-say-a93678',
'palaemon':'https://www.palaemonmaritime.com/post/maritime-security-report-7th-13th-september-2026'}
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.skip=0; self.parts=[]
 def handle_starttag(self,t,a):
  if t in ('script','style'): self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'): self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip(): self.parts.append(d.strip())
def fetch(item):
 name,url=item; result={'name':name,'url':url,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35); raw=r.read().decode('utf-8','replace'); parser=Text(); parser.feed(raw)
  result['reuters_links']=re.findall(r'https://www\.reuters\.com/[^\s\"<>]+',raw); result.update(status=r.status,bytes=len(raw),text='\n'.join(parser.parts)); (ROOT/(name+'.txt')).write_text(result['text'])
 except Exception as e: result['error']=str(e)
 return result
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(fetch,URLS.items()))
(ROOT/'retrieval.json').write_text(json.dumps([{k:v for k,v in r.items() if k!='text'} for r in results],indent=2))
for r in results:
 print(r['name'],r.get('status',r.get('error')))
 if 'text' in r:
  lines=r['text'].splitlines()
  hits=[i for i,s in enumerate(lines) if re.search(r'17,100|7,100|CDU|3.54|three industry|month|September 16|Saratov.*halt|Ryazan.*halt',s,re.I)]
  for i in hits: print('\n'.join(lines[max(0,i-1):i+2])[:1800])
