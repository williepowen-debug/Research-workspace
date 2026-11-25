import sys,urllib.request,re,html,hashlib
sys.path.insert(0,'scripts'); from sec_contact import sec_ua
u='https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm'
b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':sec_ua()}),timeout=60).read()
open(sys.argv[1],'wb').write(b); print(len(b),hashlib.sha256(b).hexdigest()[:16])
t=re.sub(r'<[^>]+>',' ',b.decode('utf-8','ignore')); t=html.unescape(t); t=re.sub(r'[ \xa0]+',' ',t)
open(sys.argv[1]+'.txt','w').write(t)
