import json,sys,subprocess,datetime,os,concurrent.futures as cf
d0=datetime.date(2024,1,2); d1=datetime.date(2026,11,5)
days=[]
d=d0
while d<=d1:
    if d.weekday()<5: days.append(d)
    d+=datetime.timedelta(1)
def get(d):
    p=f"d/{d}.json"
    if os.path.exists(p) and os.path.getsize(p)>100: return
    subprocess.run(["curl","-sL","-m","20","-A","Mozilla/5.0","-o",p,f"https://cdn.cboe.com/data/us/options/market_statistics/daily/{d}_daily_options"],check=False)
with cf.ThreadPoolExecutor(6) as ex: list(ex.map(get,days))
rows=[]
for d in days:
    p=f"d/{d}.json"
    try:
        j=json.load(open(p))
        r={x['name']:x['value'] for x in j['ratios']}
        rows.append((str(d),float(r['EQUITY PUT/CALL RATIO']),float(r['TOTAL PUT/CALL RATIO']),float(r['INDEX PUT/CALL RATIO']),float(r.get('SPX + SPXW PUT/CALL RATIO',0)),float(r.get('EXCHANGE TRADED PRODUCTS PUT/CALL RATIO',0))))
    except Exception as e:
        pass
with open('pc.tsv','w') as f:
    f.write("date\tequity\ttotal\tindex\tspx\tetp\n")
    for r in rows: f.write("\t".join(map(str,r))+"\n")
print(len(rows),rows[0],rows[-1])
