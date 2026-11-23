import zipfile,csv,io,statistics as s,sys
z=zipfile.ZipFile('g.zip');P={'sa':{}, 'au':{}}
for r in csv.DictReader(io.TextIOWrapper(z.open('psd_grains_pulses.csv'),encoding='utf-8-sig')):
    if r['Attribute_Description']!='Production':continue
    k='sa' if (r['Country_Name'],r['Commodity_Description'])==('South Africa','Corn') else 'au' if (r['Country_Name'],r['Commodity_Description'])==('Australia','Wheat') else None
    if k:P[k][int(r['Market_Year'])]=float(r['Value'])
D={}
for k in P:
    for y in P[k]:
        b=[P[k].get(y-i) for i in range(1,6)]
        if None not in b and y<=2025:D.setdefault(k,{})[y]=P[k][y]/s.mean(b)-1
ys=sorted(set(D['sa'])&set(D['au']));print('seasons',len(ys),ys[0],ys[-1])
a=[y for y in ys if D['sa'][y]<=-.15];b=[y for y in ys if D['au'][y]<=-.15];c=[y for y in ys if y in a and y in b]
f=lambda L:[(y,round(100*D['sa'][y],1),round(100*D['au'][y],1)) for y in L]
print('SA',len(a),f(a));print('AU',len(b),f(b));print('both',len(c),f(c))
print('within 10% both',f([y for y in ys if D['sa'][y]<=-.10 and D['au'][y]<=-.10]))
adj=[(y,round(100*D['sa'][y],1),round(100*D['au'][y+1],1)) for y in ys if y+1 in D['au'] and D['sa'][y]<=-.15 and D['au'][y+1]<=-.15]
print('SA my y with AU my y+1 (same calendar yr):',adj)
O={}
for l in open('../acp/oni.txt'):
    p=l.split()
    if p and p[0]=='DJF':O[int(p[1])]=float(p[3])
print('both w/ DJF ONI',[(y,O.get(y+1)) for y in c]); print('expected if independent',round(len(a)*len(b)/len(ys),1))
print('strong EN',f([y for y in ys if O.get(y+1,0)>=1.5]))
