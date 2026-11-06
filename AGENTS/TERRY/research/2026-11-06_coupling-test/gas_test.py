import yfinance as yf, json, datetime as dt, statistics as st, math
P=json.load(open('data/ao_pass.json')); passed=set(P['pass_card_read'])
h=yf.download(['UNG','NG=F'],start='2000-11-01',end='2026-02-01',auto_adjust=False,progress=False)['Close']
h.to_csv('data/gas_closes.csv')
out=[]
for t in ['UNG','NG=F']:
    s=h[t].dropna(); rows=[]
    for y in range(2000,2026):
        a=s[s.index>=f'{y}-12-04']; b=s[s.index<=f'{y+1}-01-08']
        if len(a)==0 or len(b)==0 or a.index[0].year!=y or b.index[-1]<a.index[0] or a.index[0]>dt.datetime(y,12,8): continue
        p0=a.iloc[0]; p1=b.iloc[-1]; hi=s[(s.index>=a.index[0])&(s.index<=b.index[-1])].max()
        rows.append((y,p1/p0-1,hi/p0-1))
    Pa=[r for r in rows if r[0] in passed]; Fa=[r for r in rows if r[0] not in passed]
    f=lambda R:(len(R),st.median(r[1] for r in R),sum(r[2]>=.20 for r in R))
    print(t,'all n',len(rows),'median 12/4-1/8 %+.1f%%'%(100*st.median(r[1] for r in rows)),'peak>=+20%:',sum(r[2]>=.2 for r in rows))
    print('  AO pass n=%d median %+.1f%% peak>=+20%% %d'%(f(Pa)[0],100*f(Pa)[1],f(Pa)[2]))
    print('  AO fail n=%d median %+.1f%% peak>=+20%% %d'%(f(Fa)[0],100*f(Fa)[1],f(Fa)[2]))
    json.dump(rows,open(f'data/gas_{t[:2]}.json','w'))
