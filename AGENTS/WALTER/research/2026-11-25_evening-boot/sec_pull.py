import sys,json,urllib.request,time
sys.path.insert(0,'scripts'); from sec_contact import sec_ua
H={'User-Agent':sec_ua(),'Accept-Encoding':'identity'}
def get(u):
    r=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=40); return r.read()
for name,cik in (('CoreWeave','0001769628'),('NVIDIA','0001045810')):
    d=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik}.json'))
    r=d['filings']['recent']; print('==',name,d['name'])
    for i in range(30):
        print(r['filingDate'][i],r.get('acceptanceDateTime',['']*99)[i][:19],r['form'][i],r['items'][i],r['accessionNumber'][i],r['primaryDocument'][i])
    time.sleep(0.3)
