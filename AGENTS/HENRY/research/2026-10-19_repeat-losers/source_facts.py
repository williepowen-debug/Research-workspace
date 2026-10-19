"""Capture named issuer XBRL share facts/context, not weighted EPS shares."""
from bs4 import BeautifulSoup
from pathlib import Path
import json
P=Path(__file__).resolve().parent;out=[]
for s in ['HII','ADM','MCD','SBUX','PCAR','CPRT','INGR','YUM','QSR']:
 soup=BeautifulSoup((P/'raw'/('issuer-'+s+'.html')).read_text(),'html.parser');contexts={t.get('id'):t.get_text(' ',strip=True) for t in soup.find_all(lambda t:t.name and t.name.lower().endswith(':context'))}
 for t in soup.find_all(lambda t:t.name and t.name.lower().endswith(':nonfraction')):
  name=t.get('name','')
  if any(k.lower() in name.lower() for k in ['CommonStockSharesOutstanding','CommonStockSharesIssued','TreasuryStockCommonShares','EntityCommonStockSharesOutstanding']):out.append(dict(symbol=s,name=name,context=t.get('contextref'),context_text=contexts.get(t.get('contextref')),scale=t.get('scale','0'),text=t.get_text(' ',strip=True)))
(P/'issuer-share-facts.json').write_text(json.dumps(out,indent=2)+'\n');print('Retained',len(out),'named share facts, including cover/periodend distinction.')
