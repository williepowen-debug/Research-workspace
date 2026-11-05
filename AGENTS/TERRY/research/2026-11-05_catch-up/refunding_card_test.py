"""TERRY read of BOND's auction pools vs forward TLT. Read-only on BOND. Description, not a backtest."""
import sys,io,contextlib,statistics as st,warnings
warnings.filterwarnings("ignore")
sys.path.insert(0,'.')
import grade_auction as g, yfinance as yf
with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
    recs=g.load()
px=yf.download("TLT",start="2023-01-01",progress=False,auto_adjust=False)["Close"].squeeze()
idx=[d.strftime("%Y-%m-%d") for d in px.index]; pos={d:i for i,d in enumerate(idx)}
def fwd(date,h):
    if date not in pos or pos[date]+h>=len(px): return None
    i=pos[date]; return 100*(float(px.iloc[i+h])/float(px.iloc[i])-1)
def low(date,h):
    if date not in pos or pos[date]+h>=len(px): return None
    i=pos[date]; return 100*(float(px.iloc[i+1:i+h+1].min())/float(px.iloc[i])-1)
s0=None; rows=[]
for x in recs:
    if x['tips'] or x['term']!='30-Year': continue
    b=g.bench(recs,'30-Year',False,x['date'],12)
    if not b or b.get('n',0)<12: continue
    if s0 is None: s0=b; print('bench keys',sorted(b.keys()))
    r5=fwd(x['date'],5)
    if r5 is None: continue
    imin=b['ind']['min']; dmax=b['dlr']['max']
    old=(imin is not None and dmax is not None and x['ind']<imin and x['dlr']>dmax)
    ip=x['ind']<b['ind_p15'] if b.get('ind_p15') is not None else False
    dhigh=(dmax is not None and x['dlr']>dmax)
    rows.append(dict(d=x['date'],reo=x['reopening'],ind=x['ind'],dlr=x['dlr'],old=old,ip=ip,ipd=ip and dhigh,r1=fwd(x['date'],1),r5=r5,r10=fwd(x['date'],10),l10=low(x['date'],10)))
def rep(n,L):
    if not L: print(n,'n=0'); return
    m=lambda k:round(st.median([r[k] for r in L if r[k] is not None]),2)
    print(n,'n',len(L),'med 1d',m('r1'),'5d',m('r5'),'10d',m('r10'),'med 10d low',m('l10'),'| 5d<=-1.6%:',sum(r['r5']<=-1.6 for r in L),'| 10d low<=-1.6%:',sum((r['l10'] or 0)<=-1.6 for r in L))
lb=g.bench(recs,'30-Year',False,'2026-11-12',12); print('control, 11/12 bars: ind_min',round(lb['ind']['min'],2),'dlr_max',round(lb['dlr']['max'],2),'btc_min',round(lb['btc']['min'],2),'ind_p15',round(lb['ind_p15'],2),'n',lb['n'],'(frozen 59.95 / 14.74 / 2.29 / 63.89)')
rep('all 30Y',rows); rep("I' fire",[r for r in rows if r['ip']]); rep("I' + high dealer",[r for r in rows if r['ipd']]); rep('OLD composition failure',[r for r in rows if r['old']])
for r in rows:
    if r['old'] or r['ipd']: print(r['d'],'R' if r['reo'] else 'N','ind',round(r['ind'],2),'dlr',round(r['dlr'],2),'OLD' if r['old'] else 'I+D','1d',round(r['r1'],2),'5d',round(r['r5'],2),'10d',None if r['r10'] is None else round(r['r10'],2))
