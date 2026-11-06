"""Has the path coming out pulled the long end down? Same-date comparison of the Oct-27 FF contract, the official curve and ACM.
ACM is model accounting; a change in ACM is not a causal decomposition (CATO 9/28). Frontier of ACM is 11/5, so the premium row stops there."""
import urllib.request,tempfile,xlrd,datetime as dt,pandas as pd,io
b=urllib.request.urlopen(urllib.request.Request("https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xls",headers={"User-Agent":"Mozilla/5.0"}),timeout=40).read()
open('raw/ACMTermPremium.xls','wb').write(b)
sh=xlrd.open_workbook(file_contents=b).sheet_by_name("ACM Daily")
h=sh.row_values(0); ci={c:i for i,c in enumerate(h)}
A={}
for r in range(1,sh.nrows):
    v=sh.row_values(r)
    try:A[pd.Timestamp(dt.datetime.strptime(v[0],"%d-%b-%Y"))]=(float(v[ci['ACMTP10']]))
    except Exception: pass
A=pd.Series(A).sort_index()
n=pd.read_csv('raw/nominal.csv',parse_dates=['Date']).set_index('Date').sort_index()
r=pd.read_csv('raw/real.csv',parse_dates=['Date']).set_index('Date').sort_index()
s=pd.read_csv('raw/strip_table.csv',parse_dates=['Date']).set_index('Date')
w=[('2026-10-27','2026-11-05'),('2026-10-27','2026-11-06'),('2026-11-04','2026-11-05'),('2026-11-05','2026-11-06')]
for a,z in w:
    a,z=pd.Timestamp(a),pd.Timestamp(z)
    bp=lambda S:round((S[z]-S[a])*100,1)
    x={'2Y':bp(n['2 Yr']),'5Y':bp(n['5 Yr']),'10Y':bp(n['10 Yr']),'30Y':bp(n['30 Yr']),'real10':bp(r['10 YR']),'real30':bp(r['30 YR']),'2s30s':round(((n['30 Yr'][z]-n['2 Yr'][z])-(n['30 Yr'][a]-n['2 Yr'][a]))*100,1),
       'Dec_bp':round(s.Dec_bp[z]-s.Dec_bp[a],1),'Oct27':round(s.Oct27_bp[z]-s.Oct27_bp[a],1)}
    if z in A.index and a in A.index:
        x['ACM']=round((A[z]-A[a])*100,1); x['10Y_ex_ACM']=round(x['10Y']-x['ACM'],1)
    print(a.date(),'->',z.date(),x)
print(A.tail(9).round(4).to_dict())
print(n.loc['2026-10-27':'2026-10-28',['2 Yr','10 Yr','30 Yr']])
