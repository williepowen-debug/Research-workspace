from pathlib import Path
from bs4 import BeautifulSoup
import requests,json,concurrent.futures
p=Path('AGENTS/HENRY/research/2026-10-19_event-audit')
urls=[('USDA-WASDE-index','https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report'),('USDA-oilseed','https://www.ers.usda.gov/topics/crops/soybeans-and-oil-crops/market-outlook')]
def f(x):
 name,url=x
 try:
  r=requests.get(url,timeout=20);(p/f'raw/{name}.html').write_text(r.text);(p/f'raw/{name}.txt').write_text(BeautifulSoup(r.text,'html.parser').get_text(' ',strip=True));return dict(name=name,url=url,status=r.status_code)
 except Exception as e:return dict(name=name,url=url,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:out=list(ex.map(f,urls))
(p/'industry-receipts.json').write_text(json.dumps(out,indent=2));print(out)
