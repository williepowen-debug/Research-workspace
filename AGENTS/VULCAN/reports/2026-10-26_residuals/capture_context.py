from pathlib import Path
import urllib.request,json,hashlib,datetime
from bs4 import BeautifulSoup
S=Path(__file__).resolve().parent/'sources'
urls={
'cpram.html':'https://cpram.com/lux/en/individual/publications/experts/article/what-impact-is-hyperscaler-bond-issuance-having-on-bond-markets',
'ecb.html':'https://www.ecb.europa.eu/press/blog/date/2026/html/ecb.blog20260831~dac6a37e73.en.html',
'dallas-fed.html':'https://www.dallasfed.org/research/economics/2026/0210-searls-aifinancing',
'sifma.html':'https://www.sifma.org/research/statistics/us-corporate-bonds-statistics',
'cpram-4.jpg':'https://amundicprprodcdn.azureedge.net/cmsmedia/data/shared/imageFolder/hyperscaler4-736737e8f73842d535c0f6c6de2f0bcc665b8ecc.jpg',
'cpram-5.jpg':'https://amundicprprodcdn.azureedge.net/cmsmedia/data/shared/imageFolder/hyperscaler5-f3f8f50fcd5ce9a38389767d53f3fbfa69fac598.jpg',
'cpram-6.jpg':'https://amundicprprodcdn.azureedge.net/cmsmedia/data/shared/imageFolder/hyperscaler6-6b3f4b6642ffe5c90d002c845d0efd1dc133d4f7.jpg'}
manifest=[]
for name,url in urls.items():
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'VULCAN research williepowen@gmail.com'}),timeout=35).read(); (S/name).write_bytes(data)
  if name.endswith('.html'):
   soup=BeautifulSoup(data,'html.parser'); (S/name.replace('.html','.txt')).write_text(soup.get_text(' ',strip=True))
   if name=='sifma.html': print('SIFMA downloads',[(x.get_text(' ',strip=True),x.get('href')) for x in soup.select('a[href]') if any(t in x.get('href','').lower() for t in ['.xls','.csv'])])
  manifest.append(dict(path=name,url=url,sha256=hashlib.sha256(data).hexdigest(),retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
 except Exception as e: manifest.append(dict(path=name,url=url,error=str(e)))
(S/'CONTEXT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)); print(manifest)
