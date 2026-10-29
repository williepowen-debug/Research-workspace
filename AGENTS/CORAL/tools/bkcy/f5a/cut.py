import openpyxl,csv,sys,statistics as st
S=sys.argv[1]
MD="Baker,Bradford,Brevard,Charlotte,Citrus,Clay,Collier,Columbia,DeSoto,Duval,Flagler,Glades,Hamilton,Hardee,Hendry,Hernando,Hillsborough,Lake,Lee,Manatee,Marion,Nassau,Orange,Osceola,Pasco,Pinellas,Polk,Putnam,St. Johns,Sarasota,Seminole,Sumter,Suwannee,Union,Volusia".split(",")
SD="Broward,Miami-Dade,Highlands,Indian River,Martin,Monroe,Okeechobee,Palm Beach,St. Lucie".split(",")
pop={}
for r in csv.DictReader(open(S+'/co-est2025-alldata.csv',encoding='latin-1')):
    if r["STATE"]=="12" and r["SUMLEV"]=="050": pop[r["CTYNAME"].replace(" County","").upper()]=int(r["POPESTIMATE2025"])
def num(x): return 0 if x in (None,'0','-','–') else int(x)
def load(f):
    ws=openpyxl.load_workbook(f,read_only=True).active; out={}; dist=None
    for r in ws.iter_rows(values_only=True):
        n,code=r[0],r[1]
        if isinstance(n,str) and n.strip() in ('FL,M','FL,S','FL,N'): dist=n.strip(); continue
        if isinstance(n,str) and code is None and n.strip()[:2].isalpha() and ',' in n and len(n.strip())<=5: dist=n.strip(); continue
        if dist in ('FL,M','FL,S') and code and str(code).startswith('12') and not str(code).endswith('*'):
            out[n.strip().upper()]=(dist,num(r[2]),num(r[3]))
    return out
a=load(S+'/f5a/bf_f5a_0930.2026.xlsx'); b=load(S+'/f5a/bf_f5a_0930.2025.xlsx')
names=[x.upper() for x in MD+SD]
assert set(names)<=set(a) and set(names)<=set(b), (set(names)-set(a), set(names)-set(b))
rows=[]
for c in names:
    d,t1,c7=a[c]; _,t0,c70=b[c]; p=pop[c]
    rows.append((c,d,p,c7,c70,c7/p*1e5,(c7/c70-1)*100 if c70 else None,t1,t0))
T7=sum(r[3] for r in rows); T70=sum(r[4] for r in rows); P=sum(r[2] for r in rows)
print(f"M.D.+S.D. FL-resident Ch.7 (F-5A, 44 counties): {T7:,} vs {T70:,} = {(T7/T70-1)*100:+.1f}% ; {T7/P*1e5:.1f}/100k (pop V2025 {P:,})")
print(f"All chapters same perimeter: {sum(r[7] for r in rows):,} vs {sum(r[8] for r in rows):,} = {(sum(r[7] for r in rows)/sum(r[8] for r in rows)-1)*100:+.1f}%")
big=[r for r in rows if r[2]>=100000]
print(f"\nTop 5 by Ch.7 rate (counties pop>=100k, n={len(big)}):")
for r in sorted(big,key=lambda r:-r[5])[:5]: print(f"  {r[0]:<13}{r[1]}  {r[5]:6.1f}/100k  Ch7 {r[3]:,} ({r[6]:+.1f}% YoY)")
print("Top 5 by Ch.7 YoY growth (pop>=100k):")
for r in sorted(big,key=lambda r:-r[6])[:5]: print(f"  {r[0]:<13}{r[1]}  {r[6]:+6.1f}%  Ch7 {r[4]:,}->{r[3]:,}  {r[5]:.1f}/100k")
print("Bottom 3 by growth (pop>=100k):")
for r in sorted(big,key=lambda r:r[6])[:3]: print(f"  {r[0]:<13}{r[1]}  {r[6]:+6.1f}%  Ch7 {r[4]:,}->{r[3]:,}")
g=[r[6] for r in big]
print(f"\nBreadth (pop>=100k, n={len(big)}): rising {sum(x>0 for x in g)} · >+20% {sum(x>20 for x in g)} · >+30% {sum(x>30 for x in g)} · median {st.median(g):+.1f}%")
g2=[r[6] for r in rows if r[6] is not None]
print(f"Breadth (all 44): rising {sum(x>0 for x in g2)} · >+20% {sum(x>20 for x in g2)} · median {st.median(g2):+.1f}%")
for D in ('FL,M','FL,S'):
    s7=sum(r[3] for r in rows if r[1]==D); s70=sum(r[4] for r in rows if r[1]==D); print(f"{D} Ch.7 FL-res {s70:,}->{s7:,} {(s7/s70-1)*100:+.1f}%")
inc=sorted(rows,key=lambda r:-(r[3]-r[4])); tot=T7-T70
print("Share of the Ch.7 increase, top 5 counties by absolute increase:")
for r in inc[:5]: print(f"  {r[0]:<13}+{r[3]-r[4]:,} ({(r[3]-r[4])/tot*100:.1f}% of +{tot:,}); pop share {r[2]/P*100:.1f}%")
print("\nCondo/MSI metros:")
for c in ['LEE','CHARLOTTE','SARASOTA','COLLIER','PINELLAS','HILLSBOROUGH','POLK','PALM BEACH','BROWARD','MIAMI-DADE','ORANGE']:
    r=[x for x in rows if x[0]==c][0]; print(f"  {c:<13}{r[1]} {r[5]:6.1f}/100k  {r[6]:+5.1f}%  Ch7 {r[4]:,}->{r[3]:,}")
