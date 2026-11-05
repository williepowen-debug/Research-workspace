import sys,io,contextlib,statistics as st,warnings
warnings.filterwarnings("ignore")
sys.path.insert(0,'.')
import grade_auction as g, yfinance as yf
with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
    recs=g.load()
px=yf.download("TLT",start="2023-01-01",progress=False,auto_adjust=False)["Close"].squeeze()
idx=[d.strftime("%Y-%m-%d") for d in px.index]; pos={d:i for i,d in enumerate(idx)}
def fwd(date,h=5):
    if date not in pos or pos[date]+h>=len(px): return None
    i=pos[date]; return 100*(float(px.iloc[i+h])/float(px.iloc[i])-1)
rows=[]
for x in recs:
    if x['tips'] or x['term']!='30-Year': continue
    b=g.bench(recs,'30-Year',False,x['date'],12)
    if not b or b.get('n',0)<12: continue
    bar=b.get('ind_p15'); 
    if bar is None: continue
    r=fwd(x['date'])
    if r is None: continue
    rows.append((x['date'],x['reopening'],x['ind'],bar,x['ind']<bar,x['dlr'],r))
F=[r for r in rows if r[4]]; N=[r for r in rows if not r[4]]
s=lambda L:(len(L),round(100*sum(1 for r in L if r[6]<0)/len(L),1),round(st.median(r[6] for r in L),2))
print("30Y all prints n,hit%TLTdown,median5d: fires",s(F),"non-fires",s(N),"all",s(rows))
Fn=[r for r in F if not r[1]]; print("new issue fires",s(Fn) if Fn else None)
for r in F: print(r[0],'R' if r[1] else 'N',round(r[2],2),round(r[3],2),'dlr',round(r[5],2),'TLT5d',round(r[6],2))
