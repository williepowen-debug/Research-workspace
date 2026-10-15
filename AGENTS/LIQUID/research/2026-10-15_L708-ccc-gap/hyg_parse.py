import re, gzip, sys, json, html
def parse(raw):
    m=re.search(r'<ss:Worksheet ss:Name="Holdings">(.*?)</ss:Worksheet>', raw, re.S)
    sheet=m.group(1)
    rows=[]
    for r in re.findall(r'<ss:Row[^>]*>(.*?)</ss:Row>', sheet, re.S):
        cells=[html.unescape(c) for c in re.findall(r'<ss:Data[^>]*>([^<]*)</ss:Data>', r)]
        rows.append(cells)
    asof=None
    for r in rows[:6]:
        if 'Fund Holdings as of' in r: asof=r[r.index('Fund Holdings as of')+1]
    hi=[i for i,r in enumerate(rows) if r and r[0]=='Name'][0]
    hdr=rows[hi]; out=[]
    for r in rows[hi+1:]:
        if len(r)!=len(hdr): continue
        out.append(dict(zip(hdr,r)))
    return asof,out
P='/tmp/claude-1000/-home-willi-Research-workspace-PROME/16d245b5-0cb3-4174-b43d-e76c4903c384/scratchpad/'
a13,h13=parse(gzip.open('/home/willi/Research-workspace/AGENTS/LIQUID/research/2026-10-14_credit-funding-refresh/hyg-download.xls.gz','rt',errors='replace').read())
a14,h14=parse(open(P+'hyg/fd_now.xls',errors='replace').read())
print('asof',a13,len(h13),'|',a14,len(h14))
print('cols',list(h13[0].keys()))
def key(r): return (r['Name'],r['Maturity'],r['Coupon (%)'])
d13={key(r):r for r in h13 if r['Asset Class']=='Fixed Income'}; d14={key(r):r for r in h14 if r['Asset Class']=='Fixed Income'}
common=[k for k in d13 if k in d14]
print('fixed-income 10/13',len(d13),'10/14',len(d14),'common',len(common))
for k in common:
    if 'COREWEAVE' in k[0].upper() or 'APPLIED DIGITAL' in k[0].upper() or 'ORACLE' in k[0].upper() or 'IREN' in k[0].upper() or 'NEBIUS' in k[0].upper():
        a,b=d13[k],d14[k]
        print(k, 'px',a['Price'],'->',b['Price'],'YTW',a['Yield to Worst (%)'],'->',b['Yield to Worst (%)'],'sector',a['Sector'],'w',a['Weight (%)'])
json.dump(dict(a13=a13,a14=a14,h13=h13,h14=h14),open(P+'l708/hyg_holdings.json','w'))
