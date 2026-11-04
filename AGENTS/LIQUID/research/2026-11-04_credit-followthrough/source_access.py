import urllib.request,pathlib,json,concurrent.futures,hashlib
p=pathlib.Path(__file__).parent
urls={
'oracle_pricing':'https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Pricing-of-20-Billion-of-Common-Stock-and-Senior-Notes/default.aspx',
'ueno_circular':'https://www.bcp.gov.py/documents/20117/0/2026-11-03_CIRCULAR_SVSG-020_Funcionamiento_Mercado_UENO.pdf/7e37805e-b631-d38f-b816-9b331da586cf?t=1793754807022.pdf',
'ueno_valuation':'https://www.bcp.gov.py/documents/20117/2780455/2026-11-03_RESOLUCI%C3%93N_SVSG_0016_CRITERIOS_VALORIZACI%C3%93N%2B%282%29.pdf/acde17a9-c011-ac00-718c-25bb1e3697b4?t=1793754846413.pdf'}
def one(k):
 u=urls[k]
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as r: raw=r.read(); status=r.status; typ=r.headers.get('Content-Type')
  ext='.pdf' if raw.startswith(b'%PDF') else '.html';(p/(k+ext)).write_bytes(raw)
  if ext=='.pdf':
   from pdfminer.high_level import extract_text
   (p/(k+'.txt')).write_text(extract_text(p/(k+ext)))
  return {'name':k,'url':u,'status':status,'content_type':typ,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
 except Exception as e:return {'name':k,'url':u,'error':type(e).__name__+': '+str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:r=list(e.map(one,urls))
(p/'source_access.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
