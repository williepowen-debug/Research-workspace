# Reproduces the 2026-09-24 CFTC JPY history figures (KB-SAM-257). Needs CFTC legacy annual zips
# deacot2000.zip..deacot2026.zip from https://www.cftc.gov/files/dea/history/ in ./cot/ ; the 2026-09-15 row is
# injected by hand from the weekly deafut.txt (L 237,951 / S 117,592 / OI 542,802) because the annual file may lag.
import zipfile, csv, io, glob
rows={}
for z in sorted(glob.glob('cot/deacot*.zip')):
    zf=zipfile.ZipFile(z)
    for n in zf.namelist():
        r=csv.DictReader(io.TextIOWrapper(zf.open(n),encoding='latin-1'))
        for d in r:
            nm=d.get('Market and Exchange Names','').strip()
            if nm.startswith('JAPANESE YEN - CHICAGO MERCANTILE'):
                dt=d['As of Date in Form YYYY-MM-DD'].strip()
                L=int(d['Noncommercial Positions-Long (All)']); S=int(d['Noncommercial Positions-Short (All)'])
                rows[dt]=(L-S,int(d['Open Interest (All)']))
# add live
rows['2026-09-15']=(237951-117592,542802)
s=sorted(rows.items())
print('n=',len(s),'first',s[0][0],'last',s[-1][0])
mn=min(s,key=lambda x:x[1][0]); mx=max(s,key=lambda x:x[1][0])
print('min',mn,'max',mx)
top=sorted(s,key=lambda x:-x[1][0])[:8]
for t in top: print(t)
print('max excl 2026-09-15:', max([x for x in s if x[0]!='2026-09-15'],key=lambda x:x[1][0]))
print('max OI', max(s,key=lambda x:x[1][1]))
# largest 2-week swing
import itertools
nets=[x[1][0] for x in s]; dates=[x[0] for x in s]
d2=[(nets[i]-nets[i-2],dates[i]) for i in range(2,len(nets))]
print('top 2wk swings',sorted(d2,reverse=True)[:4])
d1=[(nets[i]-nets[i-1],dates[i]) for i in range(1,len(nets))]
print('top 1wk swings',sorted(d1,reverse=True)[:5])
for x in s[-6:]: print(x)
